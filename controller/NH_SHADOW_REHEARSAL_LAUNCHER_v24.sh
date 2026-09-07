#!/usr/bin/env bash
#
# NH_SHADOW_REHEARSAL_LAUNCHER_v24.sh
#
# N.H SHADOW LIVE REHEARSAL LAUNCHER — v24
#   (THE ACCEPTED REPAIR-28 CONTROLLER, STAGE-4-ONLY CONTINUATION OF THE
#    COMPLETED v21 SHADOW, WITH DOORS 1-3 NOT RERUN)
#
# WHAT v24 CHANGES FROM v23, AND NOTHING ELSE
#   v23 WAS NEVER RUN. It was created and audited, and its executable mechanics
#   were already correct: exactly one outer stage, accepted Repair 28 as the sole
#   shadow-controller refresh source, the completed v21 shadow as the
#   continuation source, and the isolation, proof and authentication machinery
#   intact. v23's report-truth correction was, however, INCOMPLETE: a body of
#   inherited current-run wording in comments, expect labels and die strings
#   still described older runs. v24 COMPLETES that correction and nothing else.
#
#   IT CHANGES NOTHING EXECUTABLE. The controller command, the stage count, the
#   absence of any outer retry, the isolation model, the refresh mechanics, the
#   proof comparisons, the authentication semantics, the journal handling, the
#   credential protections and the fail-closed exit ordering are all carried
#   forward from v22 unchanged.
#
#   THE DEFECT v24 CORRECTS. v23's executable behaviour is already v24-shaped --
#   Repair 28 under test, the v21 shadow as the source -- but INHERITED
#   CURRENT-RUN WORDING still described earlier runs as though they were this
#   one. Its banner carried an earlier launcher number; several current-run
#   provenance sentences still named the earlier continuation source, the
#   earlier continuation controller, the earlier refresh transition and the
#   earlier controller under test; and its final human report described the
#   earlier run's subject as the subject of THIS run. Every one of those
#   sentences was false about the run this launcher would actually perform.
#   v24 rewrites all of them to the tuple in the CURRENT RUN block above,
#   sweeping the WHOLE file INCLUDING COMMENTS rather than the result block
#   alone.
#
#   WHAT v24 DOES NOT DO. It does not rewrite true history. v20 really did run
#   Doors 1 to 3 and really did crash at Stage 4 under Repair 27A. v21 really did
#   run one Stage 4 under Repair 27B and really did stop fail-closed at
#   CLAUDE_SPECIFICATION_STOP. Every statement describing those events is
#   preserved as history and is labelled as history. Only wording that purported
#   to describe THIS launcher, THIS run, THIS continuation source, THIS refresh,
#   THIS controller under test or THIS result was corrected.
#
# THE PROVENANCE OF THIS RUN, STATED ONCE AND EXACTLY
#   THIS LAUNCHER                v23.
#   ITS DIRECT FILE BASE         v23, which was created and audited but NEVER
#                                RUN. There is no v23 lab and no v23 result.
#   THE LAST COMPLETED LIVE RUN  v21.
#   THE CONTINUATION SOURCE      the preserved COMPLETED v21 SHADOW.
#   ANCESTOR DOORS EVIDENCE      v20, whose Doors 1 to 3 ran for real and passed.
#                                Its lab is preserved evidence and is NOT this
#                                run's continuation source.
#   SOURCE CONTROLLER            accepted Repair 27B -- the controller stored
#                                inside the completed v21 shadow.
#   CONTROLLER UNDER TEST        accepted Repair 28.
#   SOLE REFRESH SOURCE          nh_loop_REPAIR28_CANDIDATE.py, and nothing else.
#   REFRESH TRANSITION           Repair 27B -> Repair 28, in the fresh
#                                disposable copy only.
#   THE REAL CONTROLLER          unchanged, never a refresh source, never a
#                                destination. Repair 28 is NOT installed.
#   DOORS 1 TO 3                 already-completed v20 evidence. NOT rerun.
#   OUTER STAGES                 exactly one: execute-next-claude-task.
#
# HISTORY — WHAT THE COMPLETED v20 RUN ACTUALLY DID  (v20 HAS ALREADY RUN)
#   Its isolation self-test PASSED. Accepted Repair 27A was its sole shadow
#   refresh source. The protected real workspace, the preserved labs and the
#   regression seed all PASSED, and every stage carried source-proof PASS.
#
#     STAGE 1  question-validation      exit 0, ok true,
#                                       validation_inventory_complete true,
#                                       material_unknowns [],
#                                       deliverable_question_count 0.
#     STAGE 2  question-coverage-review exit 0, coverage_review_cleared true,
#                                       coverage_possible_gaps 0.
#     STAGE 3  interview-gate           exit 0, mechanical_path_unlocked true.
#     STAGE 4  execute-next-claude-task exit 1, stdout EMPTY, and stderr carrying
#                                       one Python traceback ending
#
#                                         prepared["mechanical_design_specification"]["requirements"]
#                                         TypeError: 'NoneType' object is not subscriptable
#
#   THAT CRASH IS WHY v21 EXISTED, AND IT WAS NOT A STOP. An ordinary controller
#   fail-closed stop writes a machine report and exits 1 with a stop_reason. That
#   one produced NO report at all: stdout was zero bytes.
#
#   ACCEPTED REPAIR 27B WAS THE BOUNDED CORRECTION TO EXACTLY THAT. It reads the
#   requirement count only where a specification exists. Repair 28 inherits that
#   behaviour unchanged. THIS LAUNCHER IMPLEMENTS NONE OF IT and contains no
#   preparation, specification or task_ready logic in any executable path; all of
#   it lives inside nh_loop.py.
#
# HISTORY — WHAT THE COMPLETED v21 RUN ACTUALLY DID  (v21 HAS ALREADY RUN)
#   v21 ran EXACTLY ONE outer stage, execute-next-claude-task, against the
#   accepted Repair-27B controller over the completed v20 post-Doors state.
#
#     STAGE 4  exit 1, source-proof PASS, and a REAL machine report on stdout --
#              not a crash. ok false, stop_reason CLAUDE_SPECIFICATION_STOP.
#              The Piece-3 interview gate was enforced and unlocked.
#              Correction rounds started 3, completed 2; one Claude invocation;
#              one Codex design audit. Round 3 stopped because Claude's
#              disposable correction workspace did not carry the already-frozen
#              non-candidate baseline source the GPT specification named, and
#              Claude correctly refused to invent the reconciliation.
#              NOTHING FROM ROUND 3 WAS PROMOTED: the candidate chain is still
#              v1_0 -> v1_1 -> v1_2, with no v1_3.
#
#   ACCEPTED REPAIR 28 IS THE BOUNDED CORRECTION TO EXACTLY THAT SOURCE-CORPUS
#   MISMATCH, and to nothing else. It is the controller v23 puts under test.
#
# WHY A STAGE-4-ONLY CONTINUATION IS LEGITIMATE, AND WHY IT IS NOT A SHORTCUT
#   Doors 1, 2 and 3 are not skipped. They were RUN, for real, by v20, with two
#   real GPT reviews, and they PASSED. Their outcome is not a memory of a report:
#   it is recorded in the interview journal that v21 carried forward
#   BYTE-IDENTICALLY and that this continuation carries forward again -- nine
#   authenticated, chained events whose ninth is the
#   question_coverage_review_recorded clearance itself. Rerunning them would burn
#   two more real provider calls to re-derive a clearance that is already durably
#   recorded, and would produce a DIFFERENT state from the one being continued.
#
#   THE CONTROLLER STILL ENFORCES ITS OWN GATE. execute-next-claude-task performs
#   its own Piece-3 interview clearance and its own source re-proofs, in its own
#   right, on every invocation. Nothing here bypasses, relaxes, pre-answers or
#   replaces any of them. If the controller decides the clearance is not current
#   under Repair 28, it fails closed, and that is a VALID RESULT this launcher
#   records without working around.
#
# WHAT v23 IS, AND WHAT IT IS NOT
#   It is the Stage-4-only continuation rehearsal of the accepted Repair-28
#   controller: the current accepted controller logic, run against the EXACT
#   post-Doors-1-to-3 shadow state the v21 CLAUDE_SPECIFICATION_STOP occurred in,
#   inside the already-proven isolation model, to see what
#   execute-next-claude-task actually does now that the correction workspace
#   carries the frozen non-candidate baseline source.
#
#   IT ASSUMES NO OUTCOME AT ALL. It does not assume Stage 4 must pass, that
#   Claude must be invoked, that a Codex design audit must run, that a correction
#   round must happen, or that the loop must reach PASS. It runs the real
#   Repair-28 controller once and records whatever the real controller does. A
#   NEW legitimate fail-closed stop is a VALID RESULT. No gate is loosened to
#   reach a later outcome, and this file contains no machinery for forcing the
#   workflow past a stop.
#
#   THERE IS NO OUTER RETRY. Not around the stage, not around a provider call,
#   not around the controller. The stage has exactly one call site. The
#   controller's OWN internal bounded Claude/Codex correction loop, with its
#   lifetime limit of MAX_AUTOMATIC_CORRECTION_ROUNDS = 5, is entirely
#   controller-owned and is neither duplicated nor bypassed here.
#
#   IT IS NOT another broad controller audit, IT IS NOT a new repair, and IT IS
#   NOT a search for another controller defect.
#
#   REPAIRS 20B, 21, 22, 23, 24, 25, 26, 27, 27A AND 27B ARE PRESERVED REPAIR
#   EVIDENCE ONLY. Not one of them is a refresh source. Repair 27B additionally
#   is the SOURCE controller carried by the continuation shadow. Repair 28 is the
#   SOLE refresh source.
#
# ONE KNOWN DEPENDENCY IS DELIBERATELY LEFT OPEN
#   The MANUAL route-audit-finding provenance re-proof still does not carry a
#   non-empty resume baseline. That path is NOT part of the normal Stage-4
#   execution rehearsed here. v24 never invokes it, never injects a finding to
#   force it, never repairs it, and never treats its being open as a v23 failure.
#   If Stage 4 legitimately stops at CHATGPT_REVIEW_REQUIRED, this launcher STOPS
#   THERE and records the controller\047s own result. It does not invoke
#   route-audit-finding, does not invoke question-validation, does not manufacture
#   a finding, and does not manufacture a Ness question.
#
# WHAT THIS IS
#   A disposable-laboratory launcher. It proves the protected original N.H /
#   controller workspace has not moved since this launcher was constructed,
#   proves the completed v20 Doors result and the completed v21 Stage-4 result
#   are what they are recorded to be, makes an exact throwaway copy of THE
#   PRESERVED v21 SHADOW -- the post-Doors-1-to-3 state the Repair-27B
#   CLAUDE_SPECIFICATION_STOP occurred in -- REFRESHES EXACTLY ONE FILE IN THAT
#   NEW COPY, and only in the new copy, to the accepted Repair-28 controller,
#   hides the real /home/ness behind a tmpfs, republishes that continuation copy
#   at the EXACT normal path /home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP inside a
#   Bubblewrap namespace, runs
#
#       python3 nh_loop.py execute-next-claude-task     (exactly once)
#
#   inside that namespace, and then re-proves the protected original from OUTSIDE
#   the namespace.
#
#   THREE SOURCES ARE KEPT SEPARATE AND ARE NEVER RECONCILED.
#     THE CONTINUATION SOURCE is the completed v21 shadow. It is the state this
#     run continues from, and the only thing ever copied.
#     THE HISTORICAL LINEAGE SEED is the preserved v10 continuation shadow, which
#     v20 itself was seeded from. In v23 it is PRESERVED EVIDENCE ONLY: it is
#     still authenticated, still proved whole against the v11 witness, and still
#     proved unmoved -- and it is NEVER COPIED by this launcher on any path.
#     THE PROTECTED ORIGINAL is today's real workspace. It is independently
#     frozen and independently proved.
#   No two of them are ever compared as though they should now be identical.
#   THE COMPLETED v20 LAB is a fourth, separate thing: preserved ANCESTOR
#   evidence, read only to authenticate the Doors-1-to-3 result. It is never
#   copied and is never this run's continuation source.
#
#   The one stage is run AT MOST ONCE. It captures its exact command line,
#   stdout, stderr, exit code, start and finish timestamps, and its own protected
#   source proof.
#
# WHAT NESS'S ACCEPTANCE OF REPAIR 28 DOES AND DOES NOT AUTHORISE
#   Ness has explicitly accepted Repair 28 for its bounded controller-repair
#   scope. In THIS FILE that acceptance authorises exactly one thing: using
#   nh_loop_REPAIR28_CANDIDATE.py as the sole controller refresh source for the
#   disposable shadow below. ACCEPTANCE ALONE DID NOT AUTHORISE A LIVE RUN.
#
#   REPAIR 27A AND REPAIR 27B REMAIN ACCEPTED, AND IN THIS FILE THEY ARE
#   PRESERVED EVIDENCE ONLY. Repair 28 is based on Repair 27B, which is based on
#   Repair 27A; those acceptances are not withdrawn by this file, and neither
#   candidate is ever copied anywhere by this file. Repair 27B is additionally
#   the identity the continuation shadow's own controller must equal BEFORE the
#   refresh.
#
#   ONE RUN, AND ONLY AFTER AN INDEPENDENT AUDIT. Any execution of this exact
#   launcher is conditional on ChatGPT independently auditing THIS FILE as PASS
#   first. This file makes no claim that such an audit has happened, and this
#   file's own run is NOT authorised at the time of its creation.
#
#   IT IS NOT AN INSTALLATION. The real controller/nh_loop.py is never written,
#   never replaced and never a refresh destination; it is frozen by exact
#   identity and re-proved before, during and after the run. IT IS NOT ADOPTION
#   of any N.H design, IT IS NOT acceptance of any N.H candidate, and it
#   authorises no production implementation.
#
# WHAT THIS IS NOT
#   This is validation only. It creates no N.H policy. It is not acceptance and
#   it is not adoption of any candidate. It authorises no production
#   implementation. It integrates nothing into Master or Map. It contains no Git
#   write command of any kind, and it is read-only against the protected
#   original, against the historical lineage seed, and against every preserved
#   lab -- INCLUDING THE COMPLETED v20 LAB -- in the exact sense defined
#   immediately below.
#
#   A controller PASS inside the shadow means ONLY that the isolated real
#   rehearsal reached its own PASS. It means nothing about N.H acceptance.
#
# READ-ONLY, STATED EXACTLY
#   This launcher deliberately does NOT claim "never modified" or "never
#   written" about the protected original, about the historical lineage seed, or
#   about any preserved rehearsal lab including the completed v21 lab. Those
#   phrases would be false, and a safety launcher that overstates its own
#   guarantee is worse than one that states a narrower true one. What follows is
#   the whole claim, and nothing anywhere else in this file means more than it.
#
#   SCOPE. This describes what THIS LAUNCHER'S OWN CODE does, outside the
#   Bubblewrap namespace. It says NOTHING about the sandboxed controller run.
#   Whether that run stayed contained is not asserted here; it is settled only
#   by the before/after proof in section 12, and until that proof completes the
#   report says so in as many words.
#
#   WHAT IS NEVER ISSUED. Against the protected original, against the historical
#   lineage seed and against every preserved lab -- the completed v21 lab
#   included, and it is the source side of this run's one rsync -- this
#   launcher's own code issues no create, write, append, truncate, rename, hard
#   link, symlink, unlink, rmdir, chmod, chown or utimes operation. Every
#   regular-file open of those paths is read-only. Verified by enumerating every
#   mutating command in this file: all of them target the new lab, the new
#   shadow copy, or the in-namespace overlays.
#
#   THE THREE OPERATIONS THAT ARE NOT PLAIN READS, NAMED. No closed list of
#   "read-only tools" is given here, because such a list is easy to write and
#   easy to get wrong -- this file's ancestors previously carried one that
#   omitted wc, grep, the shell's own `exec N<` redirections and, worse, flock.
#   The claim is about operations, not binaries. Three operations against
#   protected paths are not plain content reads, and all three are deliberate:
#     1. flock(2). Section 6 opens nh_candidate_transaction.lock and
#        nh_interview_journal.lock for reading and takes an EXCLUSIVE advisory
#        lock on each. That is kernel state attached to the open file
#        description, not a change to file content or to any metadata field,
#        and both locks are released in section 8 before the namespace is ever
#        entered. It is done precisely because flock is the same primitive the
#        controller itself takes, so it genuinely excludes a concurrent
#        controller instead of merely hoping for one.
#     2. A namespace-private bind mount. Section 9 binds the new shadow over the
#        protected workspace PATH inside the Bubblewrap mount namespace. Being a
#        mount point in a private namespace does not alter the host directory,
#        and nothing of that mount survives the namespace.
#     3. atime, immediately below.
#
#   ATIME. /home/ness is ext4 mounted relatime on this host, so any read can
#   refresh atime when the stored atime is older than mtime/ctime or more than
#   24 hours old. That is a real, if minimal, metadata effect on preserved
#   evidence, and it is not hidden here. atime is captured in NO proof this
#   launcher takes, so a refresh can never move a verdict in either direction;
#   ctime does not move with atime, and ctime IS captured.
#   Restoring atime afterwards was rejected: it would be an actual write, and it
#   would move ctime, which the proof does capture. Reading through a noatime
#   view was rejected: it would mean remounting the host filesystem, far more
#   invasive than the effect it avoids.
#
#   GIT. Git reads are read-only by construction, not by convention: every git
#   call goes through git_ro, which sets GIT_OPTIONAL_LOCKS=0 and passes
#   --no-optional-locks, so `git status` cannot take index.lock and cannot
#   refresh the on-disk index. There is no Git write command anywhere in this
#   file: no add, no commit, no push, no reset, no checkout, no stash, no clean,
#   no restore, no rm, no mv, no branch, no tag, no fetch, no pull and no merge.
#
#   CONSEQUENCE. No content, mode, owner, group, size, mtime, ctime, inode or
#   link count of any protected, preserved or source file is altered by this
#   launcher's own code. atime may be refreshed. Two advisory locks are taken and
#   released. Nothing else.
#
#   Everywhere below, "read-only" means exactly this and nothing stronger.
#
# GOVERNING AUTHORITY (unchanged by this file)
#   1. NH_MASTER-20_CORRECTED_v10.md      <- wins all conflicts
#   2. NH_DECISION_DEFAULTS-S19_v2_3.md   <- ADOPTED BY NESS 2026-08-13
#   3. cursorrules
#   4. NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md
#   Also read before construction: NH_CHATGPT_PROJECT_INSTRUCTIONS_FULL_v1_2.md,
#   NH_FULL_DESIGN_COMPLETION_WORKFLOW_v1_0.md, and the current Complete Design
#   and Wiring Map. Ness owns meaning, policy, acceptance, adoption and
#   permission to build.
#
#   This line is INFORMATIONAL ONLY. This launcher enforces no Decision Defaults
#   rule and derives no behaviour from any authority file; it names the current
#   authority so an operator reading it is not told a stale one.
#
# ==========================================================================
# INHERITED LAUNCHER HISTORY — v13 AND v12, IN THEIR OWN TERMS
# ==========================================================================
#
#   READ THE NEXT TWO BLOCKS AS HISTORY, NOT AS THIS RUN.
#
#   They record what v13 and v12 each did, and they quote THEIR OWN frozen
#   identities, lab keys, marker tokens and refresh targets. Not one of those is
#   v24's. Every identity THIS run asserts is in SECTION 0 and nowhere else: the
#   real controller by the digest EXP_LOOP_SHA (no generation name is claimed for
#   it), the new copy's controller refreshed FROM the accepted Repair-27B
#   identity EXP_R27B_SHA TO the accepted Repair-28 candidate EXP_R28_SHA, the
#   lab and marker keyed to REPAIR28/V24, and the seed at EXP_SEED_LOOP_SHA.
#
#   Where a block below names a Repair-19B or Repair-20B controller, a v12/v13
#   lab key or a 235885af.../3fbb2045... identity, that is what THAT launcher was
#   frozen to at the time. It is preserved provenance and is not a claim about
#   what this file does.
#
# --------------------------------------------------------------------------
# WHAT v13 WAS, AND WHAT IT CHANGED
# --------------------------------------------------------------------------
#
#   v13 IS ONE BOUNDED MECHANICAL CORRECTION TO v12, NOT A REDESIGN AND NOT A NEW
#   REPAIR. It starts from the exact bytes of NH_SHADOW_REHEARSAL_LAUNCHER_v12.sh
#   (sha256 91abb63e..., 217153 bytes, 4263 lines) and changes ONLY what LOCKING
#   THE HISTORICAL REGRESSION SEED BY ITS COMPLETE WORKSPACE IDENTITY
#   mechanically requires. Repair 19, 19A and 19B are untouched. nh_loop.py is
#   untouched. The four-stage sequence is byte-preserved. Every isolation
#   guarantee and every proof v1..v12 earned is carried forward unchanged.
#
#   THE DEFECT v13 CORRECTS, STATED EXACTLY ONCE.
#   v12 proves its regression seed with a SELECTED set of identities: the seed
#   journal, its head, the authenticity key, the v10 marker, the Repair-17 seed
#   controller, the routed signal, the standing target, the package scope, and
#   the controller-authenticated seven-event chain. Every one of those checks is
#   necessary and every one of them is kept. But together they do NOT prove the
#   COMPLETE historical source workspace. An ordinary N.H source or design file
#   inside the seed -- one that is not the journal, the head, the key, the marker
#   or the controller -- could have been changed before v12 ever started, and
#   every selected check above would still pass. v12 would then copy the
#   already-changed seed and verify the copy against that same already-changed
#   seed, and report success.
#
#   THAT MATTERS BECAUSE question-validation AND question-coverage-review READ THE
#   ACTUAL N.H SOURCE FILES. A changed historical source can change the answer
#   being tested, so the regression would no longer be the regression it claims.
#
#   HOW v13 FIXES IT, AND THE ONE THING IT REFUSES TO DO.
#   The historical regression input is given its OWN whole-source identity: a
#   canonical manifest over EVERY entry beneath the seed root -- exact relative
#   path, type, permission mode, size and sha256 for regular files, path, type and
#   mode for directories -- including the seed's Git metadata.
#
#   THE EXPECTED SIDE OF THAT MANIFEST IS NOT DERIVED FROM TODAY'S SEED, AND THIS
#   IS THE LOAD-BEARING PART OF v13. Walking the seed today, hashing what is
#   found, and freezing that as "historical proof" would bless any corruption that
#   had already happened. The expectation is instead derived from evidence
#   produced BEFORE this correction existed: the preserved, completed v11 run's
#   own proof captures. v11 recorded preserved_labs.sha256 and preserved_labs.meta
#   at four separate moments -- before, during, after question-validation, and
#   after -- and those captures covered the preserved v10 seed because the seed
#   lives inside a preserved lab. Those eight files are the historical witness.
#   They are read-only. Nothing in the v11 lab is written, repaired or
#   regenerated, and a witness that does not validate produces BLOCKED, never a
#   repair.
#
#   All four witnesses must independently yield ONE byte-identical expected
#   manifest. There is no majority vote, no averaging, no choosing, and no
#   fallback to today's seed. Disagreement stops the run.
#
#   WHAT v13 STILL REFUSES TO CLAIM.
#   v12 deleted v11's rule that the historical seed equals today's real workspace.
#   v13 does NOT bring it back in any form. The two remain deliberately different
#   facts: the seed is proved against the v11 HISTORICAL WITNESS, and today's real
#   workspace is frozen and protected independently. The complete trees are never
#   compared to each other.
#
#   WHAT v13 CHANGES FROM v12, AND ONLY THIS:
#     - the historical whole-seed manifest gate, its embedded canonicalizer, its
#       frozen v11 witness identities and its two new proof artefacts;
#     - launcher version plumbing: banner, v13 basename, v12 frozen by exact
#       sha256 and byte count, the expected controller worktree gaining exactly
#       the v13 launcher, a new collision-refusing v13 lab path, a new v13 marker
#       token, and v13 result / observation naming.
#   Nothing else. The stage rules below are v12's, unchanged.
#
# --------------------------------------------------------------------------
# WHAT v12 WAS, AND WHAT IT CHANGED
# --------------------------------------------------------------------------
#
#   v12 IS A BOUNDED REGRESSION REBASE OF v11, NOT A REDESIGN. It starts from the
#   exact bytes of NH_SHADOW_REHEARSAL_LAUNCHER_v11.sh (sha256 c1966147...,
#   277896 bytes, 5188 lines) and changes ONLY what REGRESSING THE EXACT v11 LIVE
#   FAILURE UNDER THE REPAIR-19B CONTROLLER mechanically requires. Every isolation
#   guarantee and every proof v1..v11 earned is carried forward unchanged.
#
#   THE FAILURE BEING REGRESSED, STATED EXACTLY ONCE.
#   The v11 live run recorded, in its own preserved lab:
#       STAGE1_QUESTION_VALIDATION_EXIT = 0
#       validation_inventory_complete   = true
#       material_unknowns               = []
#       questions_total                 = 1
#       deliverable_question_count      = 1
#   question-validation admitted the retry/autonomy matter as a Ness question,
#   deliverable_question_count therefore became 1, the launcher's stage-1 gate
#   stopped the sequence, question-coverage-review NEVER RAN, and the false
#   question reached the Ness-question path without the second GPT ever getting a
#   chance to challenge it.
#
#   WHAT THE THREE REPAIRS DID, AND THEY ARE ALL CONTROLLER-OWNED.
#     REPAIR 19  ADMITTED != DELIVERABLE. A newly admitted question is internally
#                admitted and PROVISIONAL until a fresh, current, matching
#                question-coverage-review has cleared its package.
#                questions_total goes on truthfully reporting that the question
#                exists; deliverable_question_count reports only what could
#                actually be put to Ness right now.
#     REPAIR 19A OVER-ASK IDENTITY IS CONTROLLER-ENFORCED. A direction-B finding
#                must name the exact question it challenges, and it continues
#                that question's own standing target instead of opening a second
#                concern beside it.
#     REPAIR 19B THE TWO SETS ARE SEPARATED. coverage_challengeable_question_ids
#                is the narrow live set that authorises an over_ask;
#                coverage_shown_question_ids is the complete set the review was
#                shown, which governs missing.
#   ALL THREE LIVE INSIDE nh_loop.py. This launcher implements none of them,
#   interprets none of them, and contains no classification, disposition,
#   direction or over-ask vocabulary in any executable path.
#
#   THE ONE DEFINING LAUNCHER CHANGE: THE STAGE-1 CONTINUATION RULE.
#   v11's stage 1 stopped on deliverable_question_count with the meaning "a
#   genuine question is now waiting for Ness". Under Repair 19B that meaning is
#   wrong twice over. First, a newly admitted question no longer makes
#   deliverable_question_count non-zero, so the ordinary path is now
#   CONTINUE TO STAGE 2 with a provisional question outstanding -- which is
#   exactly the corrected behaviour v12 exists to exercise. Second, if
#   deliverable_question_count IS non-zero before any fresh matching coverage
#   review has cleared the package, that is no longer "a question for Ness": it
#   is THE REPAIR-19 DELIVERY GATE HAVING REGRESSED, and v12 stops and says so in
#   those words.
#
#   WHAT v12 DOES NOT GATE ON, DELIBERATELY AND BY NAME.
#       questions_total
#       provisional_question_count
#       questions_provisional_pending_coverage_review
#       questions_withheld_pending_coverage_review
#   None of these stops the sequence. They are read for the REPORT ONLY, through
#   helpers that can set no stop reason and can fail no gate. "A question exists"
#   is not a stop condition in v12, and reproducing v11's
#       question exists -> stop for Ness
#   logic is precisely the defect this launcher was rebuilt to remove.
#
#   THE SECOND DEFINING CHANGE: v12 DOES NOT CLAIM THE HISTORICAL SEED IS TODAY'S
#   REAL WORKSPACE, AND THE GATE THAT SAID SO IS GONE.
#   v11 carried a CURRENT-SOURCE COMPATIBILITY GATE (its section 4c) which
#   required the preserved seed to be byte-identical to the entire current real
#   workspace apart from six classified differences. Since v11 ran, Ness has made
#   unrelated legitimate N.H-GOVERNANCE Git work, including the Unreal Engine 5
#   Wonder runtime design commit. That gate's claim is therefore NO LONGER TRUE,
#   and v12 does not recreate it in any form. It is deleted, not weakened.
#
#   TWO FACTS ARE KEPT SEPARATE INSTEAD, AND NEITHER IMPLIES THE OTHER:
#
#     A. REGRESSION SOURCE IDENTITY (section 4b).
#        The preserved v10 continuation shadow is proved to be exactly the
#        authenticated historical snapshot this regression requires: exact
#        journal, head and key digests; exactly seven events; event 7 the last,
#        carrying the exact routed signal, standing target, package scope, issue
#        key, finding key, own digest and previous digest; the exact Repair-17
#        seed controller; and the WHOLE chain and head AUTHENTICATING under the
#        controller's own digest, HMAC, chaining and head semantics.
#
#     B. CURRENT REAL WORKSPACE PRESERVATION (sections 0, 4a, 4e, 7, 11, 12).
#        The ACTUAL current real workspace state was captured when this launcher
#        was generated -- current controller branch/HEAD/complete worktree,
#        current N.H branch/HEAD/complete worktree, every launcher v1..v11, the
#        current controller bytecode, the candidates, the adopted authority, the
#        Unreal/Wonder design file and the real five-event interview state -- and
#        frozen into this file. At run time v12 REFUSES unless the real state
#        still matches exactly what it froze, and then proves it unchanged
#        before, during, after every stage, and finally from outside Bubblewrap.
#
#   THE HISTORICAL SNAPSHOT IS THE REGRESSION INPUT. TODAY'S REAL WORKSPACE IS
#   THE PROTECTED ORIGINAL. THEY ARE INTENTIONALLY NOT ASSERTED TO BE IDENTICAL,
#   and this launcher never compares them to each other on any path.
#
#   NOTHING IS RECONCILED, REVERTED OR RESET TO MAKE THEM AGREE. v12 does not
#   copy current N.H work into the regression source, does not delete it, does
#   not revert it, does not reset anything, does not check out the old N.H HEAD,
#   and does not alter the NH-GOVERNANCE repository in any way. The current
#   Unreal/Wonder work is additionally frozen BY NAME, by sha256 and by byte
#   count, in its own proof artefact, so a claim that it did not move is a
#   measured fact rather than a silence.
#
#   WHAT v12 CHANGES FROM v11, AND ONLY THIS:
#     - the frozen controller identity, to the independently audited Repair-19B
#       controller (sha256 235885af..., 1825807 bytes, 39774 lines);
#     - THE STAGE-1 CONTINUATION RULE, as described above. This is the central
#       purpose of v12;
#     - THE STAGE-2 RULE is restated to make the "do not interpret" boundary
#       executable rather than merely intended: a possible gap STOPS AND
#       PRESERVES, and this launcher never asks, and has no code able to ask,
#       whether a gap was missing or over_ask;
#     - v11's CURRENT-SOURCE COMPATIBILITY GATE IS REMOVED ENTIRELY, together
#       with its six permitted-difference constants, for the reason above;
#     - THE REGRESSION SOURCE gets its own named verdict, its own reserved exit
#       code and its own proof artefacts, separate from the preserved-lab set,
#       so a moved regression source is never reported as, or hidden behind,
#       any other verdict;
#     - the CURRENT REAL N.H HEAD is re-read, not inherited. v11 froze
#       ce3a38f4...; that is now three commits behind and is NOT carried forward.
#       The frozen N.H HEAD is the real current one;
#     - THE CONTROLLER BYTECODE IS NOW FROZEN BY IDENTITY RATHER THAN ASSERTED
#       ABSENT. controller/__pycache__/nh_loop.cpython-314.pyc exists on disk
#       now. v11 would have failed closed on it, correctly, because v11 was
#       frozen to a moment when it did not exist. v12 freezes the real current
#       file by sha256 and byte count, requires that exact bytecode set and no
#       other, and proves it UNCHANGED across the read-only seed-authentication
#       import rather than proving it absent;
#     - the expected controller worktree gains the bytecode line and v12 itself
#       -- still an EXACT match, never "anything untracked is acceptable";
#     - v11's own identity is now frozen and gated, as v1..v10 already are;
#     - a fresh collision-refusing REGRESSION lab path, keyed to REPAIR19B, to
#       V12, to the exact Repair-19B controller sha256 and to the routed signal;
#     - the shadow marker token, keyed to the same four things;
#     - the completed v11 lab is now named as PRESERVED evidence, so this run
#       refuses to collide with it and witnesses that it did not move;
#     - the preserved-lab sweep is widened from NH_AICP_SHADOW_REHEARSAL_* to
#       NH_AICP_*, so every disposable artefact Ness holds under /home/ness is
#       witnessed rather than only the rehearsal labs. This is strictly more
#       protection and it names no additional path;
#     - the report is the v12 result block required by the authorising
#       instruction, including the controller-owned stage-1 and stage-2 scalars;
#     - the observations pass is now REPAIR-19B REGRESSION V12. It records; it
#       decides nothing and it can fail no verdict.
#   Nothing else. THE FOUR STAGES, THE PER-STAGE EVIDENCE CAPTURE, EVERY
#   ISOLATION GUARANTEE, EVERY PROVIDER-CALL LIMIT AND EVERY FAIL-CLOSED PATH ARE
#   CARRIED FORWARD.
#
#   QUESTION DELIVERY IS NOT PART OF v12, AND CANNOT BE.
#   There is no next-question-group call and no record-ness-answer call anywhere
#   in this file. Neither command name appears in any executable line; both
#   appear only in prose such as this. This launcher composes no question,
#   displays no question and answers no question. It contains no answer to any
#   question Ness has ever given, and it never touches the disposable
#   question-delivery workspace -- that path does not occur in this file at all.
#
#   THE WHOLE POINT is to prove that the corrected PRE-DELIVERY machinery gets
#   its chance to work BEFORE Ness is involved: that an admitted question stays
#   provisional, that the fresh independent coverage review actually runs, and
#   that the second GPT gets to challenge the question before anyone calls it
#   deliverable.
#
#   THE MODELS AND THE CORRECTION CAP ARE NOT SET HERE AND ARE NOT OVERRIDDEN.
#   gpt-5.6-sol at effort high, claude-opus-5 at xhigh, and a lifetime allowance
#   of 5 correction rounds are all frozen inside nh_loop.py. This launcher sets
#   none of them, contains no alternate model selection, and passes no
#   environment variable that could influence any of them: --clearenv wipes the
#   environment and the only NH_-prefixed variable set back for a real stage is
#   NH_LOOP_INTERVIEW_STATE_DIR.
#
#   THE THREE EXPLAINED WORKSPACE-ROOT DIRECTORIES GATE IS CARRIED FORWARD
#   UNCHANGED IN MEANING AND IN STRENGTH. .agents, .codex and the workspace-root
#   .git are still frozen in section 4a by exact path and exact safe shape --
#   present, a real directory, not a symlink, not a special file, EMPTY AT EVERY
#   DEPTH -- and the workspace root must still NOT resolve as a Git repository.
#   The current disk state was re-read for this rebase rather than inherited: all
#   three are still present, still real directories, still not symlinks, still
#   recursively empty, and the workspace root still does not resolve as a
#   repository.
#
# ==========================================================================
# THE v21 SEQUENCE, EXACTLY
# ==========================================================================
#
#   THERE IS ONE STAGE. THERE IS NO STAGE 1, NO STAGE 2 AND NO STAGE 3.
#
#   STAGE 4.  python3 nh_loop.py execute-next-claude-task
#             EXACTLY ONCE. The controller owns the GPT design work, the Claude
#             execution, the fresh GPT/Codex audit, the same-session Claude
#             corrections, the five-round correction cap and every existing stop
#             condition. It also owns, and re-enforces in its own right, the
#             Piece-3 interview clearance and its source re-proofs. This launcher
#             does not reinterpret audit findings and implements no second repair
#             loop. Whatever execute reports is the controller result, and v21
#             records it without reinterpreting it.
#
#   DOORS 1 TO 3 ARE NOT RERUN, AND THEY ARE NOT SKIPPED EITHER.
#   question-validation, question-coverage-review and interview-gate were RUN by
#   v20, for real, against this exact state, and all three PASSED. Their result is
#   carried forward inside the continuation source's own authenticated interview
#   journal, which this run copies byte-identically and never refreshes. No
#   constant naming those three commands exists in this file, there is no call
#   site able to run them, and the single controller call site passes STAGE4_CMD
#   and nothing else.
#
#   THERE IS NO RETRY ANYWHERE. Not around the stage, not around a provider call,
#   not around the controller. The stage is not duplicated. There is no fallback
#   invocation and no alternate validator.
#
#   AN EARLY STOP IS A RESULT, NOT A FAILURE, and this launcher never labels one
#   as a failure. Equally, an exit of 0 is never treated as a verdict about N.H:
#   every fact reported below is the controller's own, quoted verbatim, and an
#   absent field is reported as UNAVAILABLE rather than given a value.
#
#   IF THE CONTROLLER STOPS AT CHATGPT_REVIEW_REQUIRED, THIS LAUNCHER STOPS
#   THERE. It does not invoke route-audit-finding. It does not invoke
#   question-validation. It does not manufacture a finding. It does not
#   manufacture a Ness question. The independent ChatGPT review happens OUTSIDE
#   the controller, and only Ness may authorise what follows it.
set -Eeuo pipefail
umask 077

# ==========================================================================
# SECTION 0 — FROZEN IDENTITIES. FAIL CLOSED AGAINST ALL OF THEM.
# ==========================================================================
#
# EVERY VALUE IN THIS SECTION WAS READ FROM THE REAL CURRENT DISK STATE WHEN THIS
# LAUNCHER WAS CONSTRUCTED. Not one of them is inherited from a report.

readonly HOME_REAL="/home/ness"
readonly WS="/home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP"
readonly CTRL="${WS}/controller"
readonly NHGOV="${WS}/NH-GOVERNANCE"
readonly STATE="${WS}/nh_interview_state"
readonly CAND_DIR="${NHGOV}/05_ACTIVE_CANDIDATE"
readonly AUTH_DIR="${NHGOV}/01_AUTHORITATIVE"

# Twenty-one launcher files now live in controller/. All twenty-one are accounted
# for explicitly: twenty by exact identity, and this one by presence.
readonly LAUNCHER_V1_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v1.sh"
readonly LAUNCHER_V2_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v2.sh"
readonly LAUNCHER_V3_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v3.sh"
readonly LAUNCHER_V4_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v4.sh"
readonly LAUNCHER_V5_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v5.sh"
readonly LAUNCHER_V6_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v6.sh"
readonly LAUNCHER_V7_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v7.sh"
readonly LAUNCHER_V8_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v8.sh"
readonly LAUNCHER_V9_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v9.sh"
readonly LAUNCHER_V10_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v10.sh"
readonly LAUNCHER_V11_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v11.sh"
readonly LAUNCHER_V12_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v12.sh"
readonly LAUNCHER_V13_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v13.sh"
readonly LAUNCHER_V14_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v14.sh"
readonly LAUNCHER_V15_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v15.sh"
readonly LAUNCHER_V16_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v16.sh"
readonly LAUNCHER_V17_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v17.sh"
readonly LAUNCHER_V18_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v18.sh"
readonly LAUNCHER_V19_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v19.sh"
readonly LAUNCHER_V20_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v20.sh"
readonly LAUNCHER_V21_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v21.sh"
readonly LAUNCHER_V22_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v22.sh"
readonly LAUNCHER_V23_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v23.sh"
readonly LAUNCHER_V24_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v24.sh"

# v1..v19 are ALL preserved unchanged, and all of them are frozen here so this
# launcher fails closed if any of them moved. Each is historical validation
# evidence in its own right. Their per-version provenance notes are carried
# forward from v20 without change.
readonly EXP_LAUNCHER_V1_SHA="99fb0ad912b8af79a34217099c3585cee17b9011d09a2fe58071257000f10d7c"
readonly EXP_LAUNCHER_V1_BYTES="40897"
readonly EXP_LAUNCHER_V2_SHA="bb97ac49fb45f7647ee4ff2dc7a8fe21331113108ca915f1209acab7a5b70cf3"
readonly EXP_LAUNCHER_V2_BYTES="99298"
readonly EXP_LAUNCHER_V3_SHA="499b0a60c4a5b67d631e793e4f3dacb2cd3191fa07bb27e71f41e1b1da91d9b4"
readonly EXP_LAUNCHER_V3_BYTES="102494"
readonly EXP_LAUNCHER_V4_SHA="fdc62fdd59a2c39116964ee426a632306c468aaafc95d603a1bc8a806fd974c0"
readonly EXP_LAUNCHER_V4_BYTES="112576"
readonly EXP_LAUNCHER_V5_SHA="2648825e0bab060d3e8e0a79fbcca25b7cc6c5d3b8f011659c323075d1f3feba"
readonly EXP_LAUNCHER_V5_BYTES="140784"
readonly EXP_LAUNCHER_V6_SHA="e12d61830b59004ff9ab06a67db4de411f1f23176aba95b1e3afc6448528b132"
readonly EXP_LAUNCHER_V6_BYTES="158865"
readonly EXP_LAUNCHER_V7_SHA="8cce9c73b5ff3f16639a9756bf2532954f2fe6203af49e2f2f1d14cff1692dac"
readonly EXP_LAUNCHER_V7_BYTES="163580"
readonly EXP_LAUNCHER_V8_SHA="9a26049e3892005b4499a4dc1e3cfe87d2a193a6e56d48bda4d0ca55c24d256e"
readonly EXP_LAUNCHER_V8_BYTES="180695"
readonly EXP_LAUNCHER_V9_SHA="9d1f4218f6ef28acb70258fe05d9f2a6d1840468e5beb0e8d3c8c36bc36f5fe9"
readonly EXP_LAUNCHER_V9_BYTES="187641"
readonly EXP_LAUNCHER_V10_SHA="088da6ce1b4bda1173b83303cb1a3972241b70d1c54eebf9acbf89b620d1aca1"
readonly EXP_LAUNCHER_V10_BYTES="237741"
readonly EXP_LAUNCHER_V11_SHA="c1966147c3cff752c43864c691075cdd5ce1f503ae15f53e05bc8152ffef7800"
readonly EXP_LAUNCHER_V11_BYTES="277896"
readonly EXP_LAUNCHER_V12_SHA="91abb63e93c5f3614b5069d795ae01d601e852d6619f3263cf02baf28bd5056e"
readonly EXP_LAUNCHER_V12_BYTES="217153"
readonly EXP_LAUNCHER_V13_SHA="59bf029fe88e0bd16353cb49208974cd21e616fbff03008623dfa43f478ece63"
readonly EXP_LAUNCHER_V13_BYTES="254827"
readonly EXP_LAUNCHER_V14_SHA="19bac92c64f634210374344239b728896245d96aef1e3197bf1d50dacaecf1ea"
readonly EXP_LAUNCHER_V14_BYTES="267561"
readonly EXP_LAUNCHER_V15_SHA="7eca43b645a107c8cb6a12ab6fd208b2bc859cdec00d142e200270db358a40bd"
readonly EXP_LAUNCHER_V15_BYTES="279451"
readonly EXP_LAUNCHER_V16_SHA="69a7f8a668bf8ec7b97148c1fba19051d8ed1e46bd78c4a70147990fbbfa0f3b"
readonly EXP_LAUNCHER_V16_BYTES="300833"
readonly EXP_LAUNCHER_V17_SHA="a429324e50ae41b34bcf03b10a23328b7b715e54b57eb8ca48bacf5c1f11d8f9"
readonly EXP_LAUNCHER_V17_BYTES="329617"
readonly EXP_LAUNCHER_V18_SHA="af98e0a4149d34feb2c121364a769008b8a25f8ede3377d28c010125c8d70533"
readonly EXP_LAUNCHER_V18_BYTES="343437"
readonly EXP_LAUNCHER_V19_SHA="7284fa7bd98c525197f74cde7de2cbcf837974886cce61902f6be7d64aade7ae"
readonly EXP_LAUNCHER_V19_BYTES="355707"

# v20 IS PRESERVED ANCESTOR EVIDENCE. IT WAS RUN, EXACTLY ONCE.
# IT IS NOT THIS FILE'S DIRECT PREDECESSOR (v23 IS) AND IT IS NOT THIS RUN'S
# CONTINUATION SOURCE (THE COMPLETED v21 SHADOW IS).
#
# It ran against the accepted Repair-27A controller over the preserved v10
# seven-event state. Its Stage 1, Stage 2 and Stage 3 all PASSED -- which is what
# proved accepted Repair 27A carried the workflow through Doors 1 to 3 -- and its
# Stage 4 CRASHED with an unhandled TypeError inside the preparation report,
# producing NO machine report at all. Its completed lab --
# PRESERVED_LAB_REPAIR27A_V20 below -- holds that exact crash AND the
# Doors-1-to-3 clearance this continuation carries forward, so it is historical
# ANCESTOR evidence in its own right. It is NOT this run's continuation source.
#
# NOTHING ABOUT v20 IS RETRACTED BY v23 EXISTING. v20 was correct for the
# controller it was frozen to; the crash it recorded was a real controller
# result. v20 is preserved launcher history and is gated here by the exact
# identity read from disk when v21 was frozen. v24 never runs it.
readonly EXP_LAUNCHER_V20_SHA="e89612b696a125f46f53b330b79c0ac4a583622a77bc45bbd6865fe4fb310426"
readonly EXP_LAUNCHER_V20_BYTES="371456"

# v21 IS THE LAST COMPLETED LIVE RUN AND IT RAN, exactly once, against the
# accepted Repair-27B controller. Its single Stage 4 reached the real correction
# loop and stopped fail-closed at CLAUDE_SPECIFICATION_STOP; its completed lab
# holds that exact stop AND is this run's continuation source. It is now gated by
# exact identity like v1..v20, and that expectation is the identity read from
# disk when v22 was frozen. v24 never runs it.
readonly EXP_LAUNCHER_V21_SHA="de72e6630c39d7a0ad9969cfa9140e26356c6dbbb9adbcf3bab98bd7cc0654b4"
readonly EXP_LAUNCHER_V21_BYTES="378161"

# v22 IS PRESERVED LAUNCHER HISTORY. It was created and independently audited
# but WAS NEVER RUN, so there is no v22 lab and no v22 result to authenticate.
# It is v23's base, not this file's; this file's immediate base is v23 below.
# It is gated by exact identity like every launcher before it.
readonly EXP_LAUNCHER_V22_SHA="e3d059481a3d43552b612b9704ec88b48639290652b00708522b710e1c063f9d"
readonly EXP_LAUNCHER_V22_BYTES="399929"

# v23 is THIS file's IMMEDIATE BASE. It was created and audited but WAS NEVER
# RUN, so there is no v23 lab and no v23 result to authenticate. It is gated by
# exact identity like every launcher before it.
readonly EXP_LAUNCHER_V23_SHA="8950f036ccad971d417802cb2f6d30d65ef562ff05d3d86af6678dcd6a34aa10"
readonly EXP_LAUNCHER_V23_BYTES="404910"

# --- controller: THE REAL PROTECTED CONTROLLER ---
#
#   EXP_LOOP_*  is the REAL controller on disk. It is PROTECTED.
#               ITS IDENTITY HERE IS ITS DIGEST, NOT A GENERATION NAME.
#
#               WHY NO NAME IS ASSERTED, STATED FROM EVIDENCE THIS FILE HOLDS.
#               Earlier launchers labelled this file "Repair 20", and one
#               v12-era comment called it "Repair 19B". Those two cannot both be
#               right, and this file carries enough to settle part of it:
#
#                 * Repair 19B's controller digest is
#                   235885af469a6b5f3f428d206c77072712ef4b8d68caa37acf43445fc321bf02,
#                   carried in PRESERVED_LAB_REPAIR19B_V13's own path. It is NOT
#                   EXP_LOOP_SHA, so the real controller is DISPROVED to be
#                   Repair 19B. That inherited comment was simply wrong;
#                 * the same holds for every other generation this file knows by
#                   digest -- Repair 17 (EXP_SEED_LOOP_SHA), 20B, 21, 22, 23, 24,
#                   25, 26, 27, 27A and 27B. EXP_LOOP_SHA equals none of them,
#                   which is exactly what "the real controller is never a refresh
#                   source and is never overwritten by one" has to mean;
#                 * "Repair 20" names a generation this file holds NO digest for.
#                   It is therefore neither confirmed nor denied here, and it is
#                   not asserted.
#
#               assert_real_controller_is_no_known_candidate() below turns the
#               second bullet into a mechanical check rather than a claim, so it
#               fails the run closed instead of merely reading well.
#
#               What IS proved, before/during/after and on every path, is the
#               exact sha256, byte count and line count below. That is what this
#               launcher asserts about the real controller, and all it asserts.
#               It is asserted before, during and after, it is opened read-only
#               on every path, it is never a write destination anywhere in this
#               launcher, and it is NOT what the shadow is refreshed to.
readonly EXP_LOOP_SHA="bdc4e74673d500ed654f5b7e83333ea620445bff8696d02a80197ed62630ce6a"
readonly EXP_LOOP_BYTES="1850341"
readonly EXP_LOOP_LINES="40217"

# --- controller: THE REPAIR-20B CANDIDATE -- PRESERVED REPAIR EVIDENCE ---
#
# It WAS the refresh source of v14. In v21 it is preserved repair evidence only:
# never a refresh source, never copied anywhere, gated by exact identity so this
# run can state that it did not move.
readonly R20B_CANDIDATE_BASENAME="nh_loop_REPAIR20B_CANDIDATE.py"
readonly R20B_CANDIDATE="${CTRL}/nh_loop_REPAIR20B_CANDIDATE.py"
readonly EXP_R20B_SHA="3fbb204524348b7e9d32409a81d417e817aec5a3a3239b87e215313490ea5963"
readonly EXP_R20B_BYTES="1855288"
readonly EXP_R20B_LINES="40307"

# --- controller: THE REPAIR-21 CANDIDATE -- PRESERVED REPAIR EVIDENCE ---
#
# It WAS the refresh source of v15. Preserved repair evidence only in v24.
readonly R21_CANDIDATE_BASENAME="nh_loop_REPAIR21_CANDIDATE.py"
readonly R21_CANDIDATE="${CTRL}/nh_loop_REPAIR21_CANDIDATE.py"
readonly EXP_R21_SHA="a54f9e5ffd77470e9c0eb60552aa207e5ab24c8b45bff09765fe552fa5c910cd"
readonly EXP_R21_BYTES="1859838"
readonly EXP_R21_LINES="40385"

# --- controller: THE REPAIR-22 CANDIDATE -- PRESERVED REPAIR EVIDENCE ---
#
# It WAS the refresh source of v16, which was never run. Preserved repair
# evidence only in v24.
readonly R22_CANDIDATE_BASENAME="nh_loop_REPAIR22_CANDIDATE.py"
readonly R22_CANDIDATE="${CTRL}/nh_loop_REPAIR22_CANDIDATE.py"
readonly EXP_R22_SHA="d4ca703ec10d6de8d9de5b62e72b5f3e51a6dadb315e7d1e3b6a87031b088453"
readonly EXP_R22_BYTES="1878168"
readonly EXP_R22_LINES="40750"

# --- controller: THE REPAIR-23 CANDIDATE -- PRESERVED REPAIR EVIDENCE ---
#
# Repair 23 closed five independently confirmed loop-consistency defects
# (I-03..I-07). Preserved evidence only: never a refresh source, never copied,
# gated purely so this run can state that it did not move.
readonly R23_CANDIDATE_BASENAME="nh_loop_REPAIR23_CANDIDATE.py"
readonly R23_CANDIDATE="${CTRL}/nh_loop_REPAIR23_CANDIDATE.py"
readonly EXP_R23_SHA="b7e276587e0f251c5d1ad2232a3a8bb60a967852b1e4b4e5a3efdc9052f95358"
readonly EXP_R23_BYTES="1934196"
readonly EXP_R23_LINES="41868"

# --- controller: THE REPAIR-24 CANDIDATE -- PRESERVED REPAIR EVIDENCE ---
#
# Repair 24 closed the route-audit-finding provenance and source/route-pairing
# defect. Preserved evidence only, on exactly the same terms as Repair 23.
readonly R24_CANDIDATE_BASENAME="nh_loop_REPAIR24_CANDIDATE.py"
readonly R24_CANDIDATE="${CTRL}/nh_loop_REPAIR24_CANDIDATE.py"
readonly EXP_R24_SHA="3306c1cae945002b319b579a80671ade8d4e41d02e02d559bf94a91af472b6ca"
readonly EXP_R24_BYTES="1973239"
readonly EXP_R24_LINES="42700"

# --- controller: THE ACCEPTED REPAIR-25 CANDIDATE -- PRESERVED REPAIR EVIDENCE ---
#
# It WAS the refresh source of v18. Repair 25 corrected the
# execute-next-claude-task CHATGPT_REVIEW_REQUIRED stop so that a blocking
# chatgpt_review_required audit finding no longer reports itself as an
# already-made Piece-3 transition and no longer hands the operator
# route-audit-finding and question-validation as immediate commands. That
# correction stands and is still accepted; Repair 27B inherits it.
readonly R25_CANDIDATE_BASENAME="nh_loop_REPAIR25_CANDIDATE.py"
readonly R25_CANDIDATE="${CTRL}/nh_loop_REPAIR25_CANDIDATE.py"
readonly EXP_R25_SHA="91b89aadafe613f28393269c6dcb3321d8872de0bf6c97f3cdbc874be7e97595"
readonly EXP_R25_BYTES="1976533"
readonly EXP_R25_LINES="42753"

# --- controller: THE ACCEPTED REPAIR-26 CANDIDATE -- PRESERVED REPAIR EVIDENCE ---
#
# It WAS the refresh source of v19, and it did its job. Preserved repair evidence
# only in v24.
readonly R26_CANDIDATE_BASENAME="nh_loop_REPAIR26_CANDIDATE.py"
readonly R26_CANDIDATE="${CTRL}/nh_loop_REPAIR26_CANDIDATE.py"
readonly EXP_R26_SHA="8970e9e4ee4e1d2219b36ec89215b8e92ccd1ecadce2dd1ff111c63b6ba18c36"
readonly EXP_R26_BYTES="1984429"
readonly EXP_R26_LINES="42909"

# --- controller: THE REPAIR-27 CANDIDATE -- PRESERVED REPAIR EVIDENCE ---
#
# Repair 27 separated CANDIDATE CUSTODY from the complete clearance-frozen source
# worktree. Preserved repair evidence only: never a refresh source, never copied.
readonly R27_CANDIDATE_BASENAME="nh_loop_REPAIR27_CANDIDATE.py"
readonly R27_CANDIDATE="${CTRL}/nh_loop_REPAIR27_CANDIDATE.py"
readonly EXP_R27_SHA="9b906342f46fb1352001cef687fe34f377c737de74e76984a785ff9f65cf055f"
readonly EXP_R27_BYTES="2005020"
readonly EXP_R27_LINES="43336"

# --- controller: THE ACCEPTED REPAIR-27A CANDIDATE
#     (PRESERVED REPAIR EVIDENCE, AND THE CONTROLLER THE CONTINUATION SOURCE
#      CARRIES -- BUT NOT THE v21 REFRESH SOURCE) ---
#
# It WAS the refresh source of v20, the completed rehearsal this file continues.
# It remains ACCEPTED. In v21 it is preserved repair evidence: it is gated by
# exact identity, witnessed in the before/during/after sweep, never written to,
# and NOT copied into the shadow by this launcher on any path.
#
# IT IS ALSO THE EXACT CONTROLLER STILL SITTING INSIDE THE CONTINUATION SOURCE,
# because that is the controller v20 ran. The refresh in section 7b is therefore
# authorised as the bounded transition Repair 27A -> Repair 27B, IN THE NEW COPY
# ONLY, and EXP_R27A_SHA is what the new copy's controller must be BEFORE that
# refresh happens.
readonly R27A_CANDIDATE_BASENAME="nh_loop_REPAIR27A_CANDIDATE.py"
readonly R27A_CANDIDATE="${CTRL}/nh_loop_REPAIR27A_CANDIDATE.py"
readonly EXP_R27A_SHA="53902f6fc020141dc567870ba75188f1622bc7241a022a5d36f465a6559ba43a"
readonly EXP_R27A_BYTES="2025002"
readonly EXP_R27A_LINES="43767"

# --- controller: THE ACCEPTED REPAIR-27B CANDIDATE -- THIS RUN'S SOURCE CONTROLLER
#
# THIS IS THE CONTROLLER THE COMPLETED v21 SHADOW WAS RUN UNDER, so it is the
# controller this run's continuation source carries and the FROM side of this
# run's one refresh transition. It is NOT this launcher's refresh source: the
# only controller refresh source anywhere in this launcher is accepted Repair 28
# below.
#
# WHAT v21 EXISTED TO EXERCISE, AND WHAT IT PROVED.
#
# v20 refreshed its shadow to Repair 27A and RAN. Repair 27A did its job through
# Doors 1 to 3 -- Stages 1, 2 and 3 all passed under it. v20's Stage 4 then
# CRASHED, and that one crash is the whole reason this launcher exists:
# run_prepare_next_claude_task read
#     prepared["mechanical_design_specification"]["requirements"]
# unconditionally while building the preparation report, and a task_ready = false
# preparation legitimately carries no mechanical design specification, so the
# subscript raised
#     TypeError: 'NoneType' object is not subscriptable
# with stdout completely empty and no machine report written at all.
#
# ACCEPTED REPAIR 27B IS THE BOUNDED CORRECTION TO EXACTLY THAT, AND TO NOTHING
# ELSE. The requirement count is read only where a specification exists;
# otherwise the field is left at the None it was initialised to -- not zero,
# which would falsely report a specification carrying no requirements, and not an
# invented empty specification -- and one plain line is appended saying no Claude
# instruction and no new mechanical design specification were required. It is a
# report-only block. WHICH kind of task_ready = false this is remains read
# downstream from the bounded not_ready_reason field alone, exactly as before.
#
# THIS LAUNCHER TESTS THAT CORRECTION AND NOTHING BROADER. It implements none of
# it, interprets none of it, and contains no preparation, specification,
# task_ready or not_ready_reason logic in any executable path. All of it lives
# inside nh_loop.py.
#
# Ness has ACCEPTED Repair 27B for its bounded controller-repair scope and
# authorised continuation of the shadow rehearsal. Acceptance authorises this
# shadow refresh and nothing else: the real controller is not installed to, and
# this candidate is copied into the NEW DISPOSABLE COPY only. It is never renamed
# to nh_loop.py on the real filesystem, never copied over the real controller,
# and never promoted.
#
# It is gated exactly as strictly as the real controller, is never written to,
# and is asserted as a precondition, again under both original locks, and again
# at the moment it is about to be read.
readonly R27B_CANDIDATE_BASENAME="nh_loop_REPAIR27B_CANDIDATE.py"
readonly R27B_CANDIDATE="${CTRL}/nh_loop_REPAIR27B_CANDIDATE.py"
readonly EXP_R27B_SHA="137bec6c6463556b17aefa077e6d08cbf60c4e34c359b62d428596c4f82cd9b9"
readonly EXP_R27B_BYTES="2026272"
readonly EXP_R27B_LINES="43786"

# --- ACCEPTED REPAIR 28: THE SOLE SHADOW-CONTROLLER REFRESH SOURCE OF v24 ---
#
# Accepted by Ness for the bounded Repair-28 controller-repair scope: the
# already-frozen non-candidate baseline source bytes are now carried into, and
# verified inside, Claude's disposable CORRECTION workspace. It corrects the
# source-corpus mismatch the completed v21 run proved, and nothing else.
#
# IT IS NOT INSTALLED. It is copied ONLY into the fresh disposable v22 shadow,
# never over the real controller, and the real controller is re-asserted
# unchanged at the moment of the copy and again afterwards.
readonly R28_CANDIDATE_BASENAME="nh_loop_REPAIR28_CANDIDATE.py"
readonly R28_CANDIDATE="${CTRL}/nh_loop_REPAIR28_CANDIDATE.py"
readonly EXP_R28_SHA="6d5e716fc6b2d777c4f65c726588a6e96b98ee67277f907c7d253ecc48edc172"
readonly EXP_R28_BYTES="2036766"
readonly EXP_R28_LINES="44010"

readonly EXP_CTRL_BRANCH="main"
readonly EXP_CTRL_HEAD="db46a51967b1af1aa873bc0c0e847a0a95221bdf"

# --- THE CONTROLLER BYTECODE, FROZEN BY IDENTITY ---
#
# Three .pyc files exist under the protected controller directory, compiled from
# the real controller and from the Repair-23 and Repair-24 candidates by ordinary
# offline verification work. They are legitimate present state. Deleting them
# would be a write to the protected original, which this launcher never performs
# on any path, and asserting their absence would fail this run closed on files
# that are simply there.
#
# So all three are frozen exactly like every other protected artefact: these
# EXACT paths, these EXACT digests, these EXACT byte counts, and NO OTHER
# bytecode path anywhere under controller/. A fourth .pyc, a different digest, or
# a __pycache__ under a subdirectory all fail the run closed. Nothing here
# whitelists "any bytecode"; it names three files and refuses everything else.
#
# The set is also proved UNCHANGED across the read-only seed-authentication
# import in section 4b. That import runs python3 with -B AND
# PYTHONDONTWRITEBYTECODE=1, so it must not rewrite these files; the proof is
# what establishes that rather than the flags being trusted.
readonly CTRL_PYCACHE_DIR="${CTRL}/__pycache__"
readonly CTRL_PYCACHE_FILES=(
  "${CTRL}/__pycache__/nh_loop.cpython-314.pyc"
  "${CTRL}/__pycache__/nh_loop_REPAIR23_CANDIDATE.cpython-314.pyc"
  "${CTRL}/__pycache__/nh_loop_REPAIR24_CANDIDATE.cpython-314.pyc"
)
readonly CTRL_PYCACHE_SHAS=(
  "8dba8fd75b1b13d42fc69a38814f6bc04b694e8dacd45c3a665a6f03a2d83e06"
  "92540f2dc11031c5371b4de0267af88ff019a0d2d58cd14f7327b51cd631c712"
  "48b2810e15eb00bde7d7bb583c0f6aba73d82a49b65d924097de7bdb9365498f"
)
readonly CTRL_PYCACHE_BYTES_LIST=(
  "1424836"
  "1489190"
  "1515581"
)
readonly CTRL_PYCACHE_STATUS_LINES=(
  "!! __pycache__/nh_loop.cpython-314.pyc"
  "!! __pycache__/nh_loop_REPAIR23_CANDIDATE.cpython-314.pyc"
  "!! __pycache__/nh_loop_REPAIR24_CANDIDATE.cpython-314.pyc"
)

# --- N.H: THE REAL CURRENT STATE, RE-READ, NOT INHERITED ---
#
# Nothing is reset, nothing is checked out, and no old HEAD is restored on any
# path.
readonly EXP_NH_BRANCH="nh-design-loop"
readonly EXP_NH_HEAD="64af315f8185881d0350b29b7f93d5465dee57e7"

# The preserved Authority Integrity candidate chain, unchanged since v4.
readonly CAND_V10="NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_0_CANDIDATE.md"
readonly CAND_V11="NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_1_CANDIDATE.md"
readonly CAND_V12="NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_2_CANDIDATE.md"

# The adopted Decision Defaults v2.3 and the exact reviewed candidate it was
# adopted from. Both are untracked entries in the N.H worktree, both are frozen
# by sha256 and byte count, and neither is "an extra file we allowed through".
readonly CAND_DD23="NH_DECISION_DEFAULTS-S19_v2_3_CANDIDATE.md"
readonly AUTH_DD23="NH_DECISION_DEFAULTS-S19_v2_3.md"

readonly EXP_V10_SHA="e6ee27fcd33f49a276de7753334cb18dd5d7d1f4d11a25d8b86dd236bfeebe3c"
readonly EXP_V10_BYTES="51315"
readonly EXP_V11_SHA="964b6dbd0a16756d65d5a6e185298eb554d6475d9da3826266b7571c8a7d8cbd"
readonly EXP_V11_BYTES="73685"
readonly EXP_V12_SHA="2245ae26ebf4b833ca36c798f82f543d807f281136e388f0f4204982c9a3cb55"
readonly EXP_V12_BYTES="109986"
readonly EXP_DD23_CAND_SHA="87003365532eee78cb7388be9beccccc4950bfaaf8074749dafad6b146e4e367"
readonly EXP_DD23_CAND_BYTES="41782"
readonly EXP_DD23_AUTH_SHA="0cd54be20ef9ec6078631cc06114e7aeded69330e72a1c85d9eec9ed108262ef"
readonly EXP_DD23_AUTH_BYTES="42595"

# --- THE CURRENT UNREAL / WONDER DESIGN WORK, FROZEN BY NAME ---
#
# It is a TRACKED file at the current N.H HEAD, so the HEAD freeze and the
# whole-worktree hash already cover it. It is ALSO frozen here by name, by
# sha256, by byte count and by mode, and witnessed in its own proof artefact, so
# this run can state UNREAL_WONDER_WORK_CHANGED=NO as a measured fact rather than
# as one unchanged line inside a listing of thousands.
readonly UNREAL_WONDER_REL="05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md"
readonly EXP_UNREAL_WONDER_SHA="114a118c242ea553b11488eb6380da1458f3788084c4f86332ba45b9a6896273"
readonly EXP_UNREAL_WONDER_BYTES="53190"
readonly EXP_UNREAL_WONDER_MODE="644"

# --- REAL interview state (identities only; the key's CONTENTS are never read) ---
#
# THE REAL JOURNAL STILL HOLDS ITS OWN FIVE EVENTS. It is NOT the continuation
# source, it is NOT overlaid into the shadow, and nothing this run produces is
# ever written back to it.
readonly EXP_JOURNAL_SHA="39c6af157222df10203d426e06ab323bb222041aa7b0838f1130f0518aef9945"
readonly EXP_JOURNAL_BYTES="15604"
readonly EXP_JOURNAL_EVENTS="5"
readonly EXP_HEAD_SHA="b55e8b3f5916445db84a4fc9e6d342113b8a538ba20fe5c20dc94f7c7a42cf90"
readonly EXP_KEY_SHA="6a129d96ed1af2e5f7c890821c8fddd27c7e4b368847884274712e126bf797d7"
readonly EXP_PKG_SCOPE="nullpkg_1ffc9ec7aae12b75ef50400da674812f"
readonly EXP_PKG_SCOPE_OCCURRENCES="5"

# --------------------------------------------------------------------------
# THE HISTORICAL LINEAGE SEED — THE PRESERVED v10 CONTINUATION SHADOW
#                                     (PRESERVED EVIDENCE; NEVER COPIED IN v21)
# --------------------------------------------------------------------------
#
# THIS IS THE STATE BEFORE THE FALSE v11 QUESTION EXISTED. It is what v18, v19
# and v20 were each seeded from, and it is therefore the lineage root of the
# continuation source this run copies.
#
# IN v21 IT IS PRESERVED EVIDENCE ONLY AND IS NEVER A COPY SOURCE. Its complete
# authentication -- exact journal, head and key digests; exactly seven events;
# event 7 the last, carrying the exact routed signal, standing target, package
# scope, issue key, finding key, own digest and previous digest; the exact
# Repair-17 seed controller; the WHOLE chain and head authenticating under the
# controller's own semantics; and the complete historical workspace manifest
# proved against the preserved v11 witness -- is carried forward from v20
# UNCHANGED, because a continuation whose lineage root has silently moved is not
# the continuation it claims to be.
#
# This path appears in this file only in readonly assignments, in printf and in
# comparisons. It is never a write target, never an rsync source, never deleted,
# never renamed, never chmod-ed, never normalised, and no Git command is ever run
# inside it.
readonly PRESERVED_LAB_REPAIR17_CONTINUATION_V10="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR17_CONTINUATION_V10_6a3ce02e4a0448d5a7206f6eb4260bbcb87989da9f0a541feafea7dd4be0dc19_rs_2593b06ab1684bbf19a6ffb70d915bd2"

readonly REGRESSION_SOURCE="${PRESERVED_LAB_REPAIR17_CONTINUATION_V10}/shadow/NH_CLAUDE_CODEX_DESIGN_LOOP"
readonly REGRESSION_SOURCE_MODE="HISTORICAL_LINEAGE_SEED_PRESERVED_NOT_COPIED"

# The seed's OWN controller file. It is the REPAIR-17 controller, because that is
# what the completed v10 run was executed with. This path is read; it is never
# written and, in v24, never copied.
readonly SEED_LOOP="${REGRESSION_SOURCE}/controller/nh_loop.py"

readonly SEED_STATE="${REGRESSION_SOURCE}/nh_interview_state"
readonly SEED_JOURNAL="${SEED_STATE}/nh_interview_journal.jsonl"
readonly SEED_JOURNAL_HEAD="${SEED_STATE}/nh_interview_journal.head"
readonly SEED_AUTH_KEY="${SEED_STATE}/nh_interview_authenticity.key"

# The lineage seed's frozen identity. Read from the preserved seed itself, never
# inherited from any report.
#
# The authenticity key is frozen by sha256 ONLY. Its CONTENTS are never read into
# this launcher, never printed, and never written into any proof artefact.
readonly EXP_SEED_JOURNAL_SHA="38e36d4dc4b8de24437857ebbe30199f13122017e374a486caf2cfc2d3b19036"
readonly EXP_SEED_JOURNAL_BYTES="65683"
readonly EXP_SEED_JOURNAL_LINES="7"
readonly EXP_SEED_JOURNAL_EVENTS="7"
readonly EXP_SEED_HEAD_SHA="cb913314f2b198f4d8352d7145e05ff40c09b86a3852e2a12bd7da6556bc03eb"
readonly EXP_SEED_KEY_SHA="6a129d96ed1af2e5f7c890821c8fddd27c7e4b368847884274712e126bf797d7"
readonly EXP_SEED_PKG_SCOPE_OCCURRENCES="7"

readonly EXP_SEED_LOOP_SHA="6a3ce02e4a0448d5a7206f6eb4260bbcb87989da9f0a541feafea7dd4be0dc19"
readonly EXP_SEED_LOOP_BYTES="1749880"
readonly EXP_SEED_LOOP_LINES="38331"

# The v10 shadow marker the lineage seed carries, frozen by content.
readonly EXP_SEED_V10_MARKER_SHA="4ea96ff31275c49db573d52f80f40bc368b48d272ea3c3c950aede77d3fbd3a3"

# --------------------------------------------------------------------------
# LINEAGE EVENT 7 -- THE ROUTED SIGNAL, FROZEN FIELD BY FIELD
# --------------------------------------------------------------------------
#
# These are IDENTIFIERS AND DIGESTS ONLY. Not one of them is a classification, a
# disposition, a verdict or an answer, and nothing in this launcher reads the
# signal's title, its evidence or any other wording.
#
# A ROUTED SIGNAL IS NOT A QUESTION. Only the controller's ordinary
# question-validation may ever turn one into a question, and this launcher
# neither performs nor influences that -- it does not run question-validation at
# all.
readonly EXP_SEED_EVENT7_TYPE="review_signal_recorded"
readonly EXP_SEED_EVENT7_ROUTE="chatgpt_review_required"
readonly EXP_SEED_EVENT7_SIGNAL_SOURCE="question_coverage_review"
readonly EXP_ROUTED_SIGNAL_ID="rs_2593b06ab1684bbf19a6ffb70d915bd2"
readonly EXP_STANDING_TARGET_ID="st_028ac341df713a4c189028c9971b4375"
readonly EXP_SEED_EVENT7_ISSUE_KEY="authority_control_retry_values_scope"
readonly EXP_SEED_EVENT7_FINDING_KEY="older_retry_decision_does_not_reach_new_seam"
readonly EXP_SEED_EVENT7_SHA="9e4fd131d16290abff4ef29aca75cf7c93ee8c57e90e25a2939191a1a7eaa5d0"
readonly EXP_SEED_EVENT6_SHA="c2031885d8bc6251ae3904932a0dda4215dec5c2ba9b4ff1c2501be143691730"

# Disk-derived witness counts over the lineage seed journal, frozen so a
# substituted or truncated journal cannot pass by shape alone.
readonly EXP_SEED_EVENT7_SHA_OCCURRENCES="1"
readonly EXP_SEED_EVENT6_SHA_OCCURRENCES="2"
readonly EXP_SEED_ROUTED_SIGNAL_OCCURRENCES="1"
readonly EXP_SEED_STANDING_TARGET_OCCURRENCES="1"

# --------------------------------------------------------------------------
# THE CONTINUATION SOURCE — THE COMPLETED v21 SHADOW
# --------------------------------------------------------------------------
#
# THIS IS THE STATE THE REPAIR-27B CLAUDE_SPECIFICATION_STOP ACTUALLY HAPPENED
# IN, and that is
# precisely why it is the continuation source. Re-seeding from the v10 lineage
# seed would mean rerunning Doors 1 to 3 to get back here -- two more real
# provider calls, and a DIFFERENT state from the one being continued. Seeding
# from anywhere else would not be this continuation at all.
#
# It is preserved evidence in its own right AND it is the read-only source this
# run copies its shadow from. Both facts are true at once and the second grants
# no write permission whatsoever: this path appears in this file only in readonly
# assignments, in printf, in comparisons, and as the SOURCE side of one rsync. It
# is never a write target, never deleted, never renamed, never chmod-ed, never
# normalised, and no Git command is ever run inside it.
readonly PRESERVED_LAB_REPAIR27A_V20="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR27A_V20_53902f6fc020141dc567870ba75188f1622bc7241a022a5d36f465a6559ba43a_rs_2593b06ab1684bbf19a6ffb70d915bd2"

# THE COMPLETED v21 LAB. It is BOTH preserved evidence AND this run's READ-ONLY
# continuation source. Neither role grants write permission: it is never written
# to, never normalised, never chmod-ed, never renamed, never reused as a lab and
# never deleted.
readonly PRESERVED_LAB_REPAIR27B_V21="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR27B_CONTINUATION_V21_137bec6c6463556b17aefa077e6d08cbf60c4e34c359b62d428596c4f82cd9b9_rs_2593b06ab1684bbf19a6ffb70d915bd2"

readonly CONTINUATION_SOURCE="${PRESERVED_LAB_REPAIR27B_V21}/shadow/NH_CLAUDE_CODEX_DESIGN_LOOP"
readonly CONTINUATION_SOURCE_MODE="COMPLETED_V21_POST_DOORS_1_TO_3_SHADOW"

readonly CONT_LOOP="${CONTINUATION_SOURCE}/controller/nh_loop.py"
readonly CONT_STATE="${CONTINUATION_SOURCE}/nh_interview_state"
readonly CONT_JOURNAL="${CONT_STATE}/nh_interview_journal.jsonl"
readonly CONT_JOURNAL_HEAD="${CONT_STATE}/nh_interview_journal.head"
readonly CONT_AUTH_KEY="${CONT_STATE}/nh_interview_authenticity.key"

# The continuation source's frozen identity. Read from the preserved v21 shadow
# itself when this launcher was written, never inherited from any report.
#
# The authenticity key is frozen by sha256 ONLY, and it is BYTE-IDENTICAL to the
# lineage seed's key: the controller only ever appends authenticated events, and
# no refresh anywhere ever touched the key. EXP_CONT_KEY_SHA equalling
# EXP_SEED_KEY_SHA is therefore a measured continuity fact, not a coincidence.
readonly EXP_CONT_JOURNAL_SHA="5b05f1151c279b2fc9c667f7e5ba261a9e5b449650687860a1d8f8f032181bac"
readonly EXP_CONT_JOURNAL_BYTES="182913"
readonly EXP_CONT_JOURNAL_LINES="9"
readonly EXP_CONT_JOURNAL_EVENTS="9"
readonly EXP_CONT_HEAD_SHA="c8a85e4dc45b4a387c28bbc2849afbb7a0abbb32c0394f041aac9b39670e3657"
readonly EXP_CONT_KEY_SHA="6a129d96ed1af2e5f7c890821c8fddd27c7e4b368847884274712e126bf797d7"
readonly EXP_CONT_PKG_SCOPE_OCCURRENCES="9"

# THE CONTINUATION SOURCE'S OWN CONTROLLER -- THE EXACT ACCEPTED REPAIR-27B FILE.
#
# This is what makes the refresh a bounded, provable transition rather than an
# overwrite. The continuation controller must be EXACTLY EXP_R27B_SHA, and the
# real controller must be EXACTLY EXP_LOOP_SHA; either side being anything else
# fails the run CLOSED.
readonly EXP_CONT_LOOP_SHA="137bec6c6463556b17aefa077e6d08cbf60c4e34c359b62d428596c4f82cd9b9"
readonly EXP_CONT_LOOP_BYTES="2026272"
readonly EXP_CONT_LOOP_LINES="43786"

# The v21 shadow marker the continuation source carries, frozen by content. It is
# positive proof that this source is a v21 SHADOW and not any real workspace.
readonly EXP_CONT_V21_MARKER_SHA="4f3af0ce199360a11ec8eb285dda98bcfe3cd40e9047a87595a8bd323ef257ee"

# --------------------------------------------------------------------------
# CONTINUATION EVENT 9 -- THE DOORS-1-TO-3 CLEARANCE, FROZEN FIELD BY FIELD
# --------------------------------------------------------------------------
#
# Event 9 is the question_coverage_review_recorded clearance v20's Stage 2
# produced and v20's Stage 3 read. IT IS THE WHOLE REASON DOORS 1 TO 3 DO NOT
# NEED RERUNNING, so it is frozen field by field and its chain is authenticated
# under the controller's own semantics rather than merely being present.
#
# IDENTIFIERS AND DIGESTS ONLY. Nothing here is a classification, a disposition,
# a verdict or an answer, and this launcher reads no wording from any event.
readonly EXP_CONT_EVENT9_TYPE="question_coverage_review_recorded"
readonly EXP_CONT_EVENT9_VALIDATION_SET_ID="vs_70ad914d542f6346acf494cdd4adb15b"
readonly EXP_CONT_EVENT9_SHA="57ceb34ad720b7c31fbf20ed8de6efbc07857d5bdaac14d4d2ffbaa83bc2920e"
readonly EXP_CONT_EVENT8_SHA="5897f9ffe9fceb3d27c3c7eeb7d53feeaed5147398c0b3b72b65f264b11d7f1d"

# Disk-derived witness counts over the continuation journal, frozen so a
# substituted, truncated or padded journal cannot pass by shape alone. Event 9's
# own digest occurs once; event 8's occurs twice (as event 8's own event_sha256
# and as event 9's prev_event_sha256); the lineage event-7 digest occurs twice
# for the same structural reason; the routed signal and the standing target each
# occur twice, because event 8 continues the same standing target event 7 opened.
readonly EXP_CONT_EVENT9_SHA_OCCURRENCES="1"
readonly EXP_CONT_EVENT8_SHA_OCCURRENCES="2"
readonly EXP_CONT_EVENT7_SHA_OCCURRENCES="2"
readonly EXP_CONT_ROUTED_SIGNAL_OCCURRENCES="2"
readonly EXP_CONT_STANDING_TARGET_OCCURRENCES="2"
readonly EXP_CONT_VALIDATION_SET_OCCURRENCES="2"

# --------------------------------------------------------------------------
# THE COMPLETE CONTINUATION-SOURCE MANIFEST, FROZEN BY DIGEST    (NEW IN v21)
# --------------------------------------------------------------------------
#
# Computed at construction time by running the SAME canonicalizer the v11
# historical-witness gate uses, against the completed v21 shadow.
#
# CANONICAL IDENTITY, STATED EXACTLY:
#   regular file   relative path, type=file, permission mode, byte size, sha256
#   directory      relative path, type=directory, permission mode
# UID, GID, atime, mtime, ctime, inode, link count and filesystem block
# allocation are NOT identity and are ignored. The seed root itself is not an
# entry; only paths strictly beneath it are.
#
# WHAT THIS EXPECTATION IS, AND HONESTLY WHAT IT IS NOT.
#   The v10 lineage seed's manifest is derived from the preserved v11 witnesses
#   -- evidence written BEFORE that gate existed -- precisely so that walking a
#   possibly-corrupted seed today could not bless the corruption. THAT RULE
#   CANNOT APPLY HERE, and pretending otherwise would be a lie: the completed v20
#   lab was created by v20 itself, after every earlier run, so no earlier
#   independent witness of it exists and none can be manufactured.
#
#   THE EXPECTATION BELOW IS THEREFORE A CONSTRUCTION-TIME FREEZE. It proves the
#   continuation source has not moved between this launcher's construction and
#   its run, and has not moved DURING the run. It does NOT, by itself, prove the
#   v20 lab was untouched between v20 finishing and v21 being written.
#
#   WHAT CARRIES THAT WEIGHT INSTEAD IS FOUR INDEPENDENT ANCHORS, each asserted
#   separately in assert_continuation_source and none of them derived from this
#   manifest:
#     1. the continuation controller must be EXACTLY the accepted Repair-27B
#        candidate -- the controller v21 ran under -- whose identity is frozen
#        independently in this section and gated independently against the real
#        controller directory;
#     2. the authenticity key must be BYTE-IDENTICAL to the v10 lineage seed's
#        key, which is proved separately against the preserved v11 witness;
#     3. the whole nine-event chain and the journal head must AUTHENTICATE under
#        the controller's own digest, HMAC, chaining and head semantics -- a
#        hand-edited or forged event cannot survive that, whatever strings it
#        carries;
#     4. the v21 shadow marker must carry the exact v21 token content.
#   A tampered continuation source would have to defeat all four AND the frozen
#   manifest. This is stated as what it is rather than dressed up as the v11
#   historical-witness rule.
readonly EXP_CONT_MANIFEST_SHA="f7b178a59c36dfca33911ae9fe6d86b3e4ed860453d40f7d21467933880ddbac"
readonly EXP_CONT_MANIFEST_ENTRIES="308"
readonly EXP_CONT_MANIFEST_FILES="234"
readonly EXP_CONT_MANIFEST_DIRS="74"
readonly EXP_CONT_MANIFEST_SYMLINKS="0"

# --------------------------------------------------------------------------
# THE COMPLETED v20 RESULT, FROZEN ARTEFACT BY ARTEFACT           (NEW IN v21)
# --------------------------------------------------------------------------
#
# WHY THIS GATE EXISTS. A continuation is only as good as the run it continues.
# If the recorded v20 result is not what this launcher believes it is, then
# skipping Doors 1 to 3 is unjustified and the whole premise of v24 is false. So
# the v20 result is PROVED, from the preserved v20 artefacts themselves, before
# anything is copied and again under both original locks.
#
# IT IS PROVED TWICE OVER, AND NEITHER HALF REPLACES THE OTHER:
#   BY DIGEST   every artefact below must carry its exact frozen sha256 and byte
#               count, so a single changed byte anywhere in the recorded result
#               fails the run closed;
#   BY CONTENT  the controller's OWN reported fields are re-read out of those
#               same artefacts and required to be exactly the recorded values.
#
# NOTHING IS REINTERPRETED AND NOTHING IS REGENERATED. No v20 stage is rerun, no
# artefact is repaired, normalised or rewritten, and no expectation is recomputed
# from anything other than the frozen values in this section.
readonly V20_PROOF_DIR="${PRESERVED_LAB_REPAIR27A_V20}/proof"

# The four v20 stage slugs, exactly as v20 named its own artefacts. These strings
# are ARTEFACT FILENAMES BEING READ. They are not controller commands, they are
# never passed to nh_loop.py, and there is no call site in this file able to do
# so -- the single controller call site passes STAGE4_CMD and nothing else.
readonly V20_STAGE1_ARTEFACT="question-validation"
readonly V20_STAGE2_ARTEFACT="coverage-review"
readonly V20_STAGE3_ARTEFACT="interview-gate"
readonly V20_STAGE4_ARTEFACT="execute"

readonly EXP_V20_S1_EXITCODE_SHA="9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"
readonly EXP_V20_S1_STDOUT_SHA="9eadb181da09e952f2a6b25021a19f34d950a01f15b83c4cbf170db9d4508c60"
readonly EXP_V20_S1_STDOUT_BYTES="19542"
readonly EXP_V20_S2_EXITCODE_SHA="9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"
readonly EXP_V20_S2_STDOUT_SHA="bddb6b5ce8ecf78287f707222019a74e5233ad1817752a64ce176f3fb0801037"
readonly EXP_V20_S2_STDOUT_BYTES="9268"
readonly EXP_V20_S3_EXITCODE_SHA="9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"
readonly EXP_V20_S3_STDOUT_SHA="93bd3fa5d4073ad3091e355ab01806bde7020d355a1b754608ec89a4b9694900"
readonly EXP_V20_S3_STDOUT_BYTES="5718"
readonly EXP_V20_S4_EXITCODE_SHA="4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865"
readonly EXP_V20_S4_STDOUT_SHA="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
readonly EXP_V20_S4_STDOUT_BYTES="0"
readonly EXP_V20_S4_STDERR_SHA="7e1615290ebb1ad569cb3063ca7a1bf8efc6eb851af82b777e8b6c07b4765337"
readonly EXP_V20_S4_STDERR_BYTES="935"
# Every v20 stage recorded its own protected-source proof, and all four say PASS.
# The four files are byte-identical, so one digest covers all of them.
readonly EXP_V20_SOURCE_PROOF_SHA="c26de83abdc9496cd1301470918ec39ecca1cf389ef0ae1c6504da1800d1c431"
readonly EXP_V20_SOURCE_PROOF_VALUE="PASS"
# v20's own controller-refresh proof, which is what makes "the continuation
# source carries accepted Repair 27A" a recorded fact rather than an inference.
readonly EXP_V20_REFRESH_AFTER_SHA="60584ad7c64c0795ad0159ccd94309671024c2fa17f1d6cfea34b55b75966798"
readonly EXP_V20_REFRESH_COMPOSITE_SHA="2d6e3e990938a8b0722e1e7953db579254348580f5948bcfdacaabd9a8619013"

# THE EXACT REQUIRED v20 STAGE FACTS, as the controller reported them.
readonly EXP_V20_S1_EXIT="0"
readonly EXP_V20_S2_EXIT="0"
readonly EXP_V20_S3_EXIT="0"
readonly EXP_V20_S4_EXIT="1"

# THE EXACT REPAIR-27A CRASH, BY ITS THREE LOAD-BEARING LINES.
#
# Each must occur in the preserved v20 execute.stderr. Together they are the
# subscript that failed, the exception it raised, and the function it happened
# in. The frozen stderr digest above already pins the whole traceback byte for
# byte; these three make the refusal message name the actual defect instead of
# printing a digest mismatch with no detail.
readonly EXP_V20_S4_CRASH_SUBSCRIPT='prepared["mechanical_design_specification"]["requirements"]'
readonly EXP_V20_S4_CRASH_TYPE="TypeError: 'NoneType' object is not subscriptable"
readonly EXP_V20_S4_CRASH_FUNC="in run_prepare_next_claude_task"

# --------------------------------------------------------------------------
# THE COMPLETED v21 RESULT, FROZEN ARTEFACT BY ARTEFACT           (NEW IN v22)
# --------------------------------------------------------------------------
#
# WHY THIS GATE EXISTS. v24 continues the state the v21 CLAUDE_SPECIFICATION_STOP
# happened in. If the recorded v21 result is not what this launcher believes it
# is, the whole premise of v24 is false. So the v21 result is PROVED, from the
# preserved v21 artefacts themselves, before anything is copied and again under
# both original locks.
#
# IT IS PROVED TWICE OVER, AND NEITHER HALF REPLACES THE OTHER:
#   BY DIGEST   every artefact below must carry its exact frozen sha256 and byte
#               count, so a single changed byte anywhere in the recorded result
#               fails the run closed;
#   BY CONTENT  the controller's OWN reported fields are re-read out of those
#               same artefacts and required to be exactly the recorded values.
#
# HOW v21's STAGE 4 DIFFERS FROM v20's, AND WHY THAT MATTERS HERE.
#   v20's Stage 4 CRASHED: stdout was zero bytes and there was no report at all.
#   v21's Stage 4 STOPPED FAIL-CLOSED: it wrote a complete machine report and
#   exited 1 with stop_reason CLAUDE_SPECIFICATION_STOP. A non-empty stdout is
#   therefore REQUIRED here, exactly as an empty one was required there, and the
#   report's own fields are read back rather than a traceback being matched.
#
# NOTHING IS REINTERPRETED AND NOTHING IS REGENERATED. No v21 stage is rerun, no
# artefact is repaired, normalised or rewritten, and no expectation is recomputed
# from anything other than the frozen values in this section.
readonly V21_PROOF_DIR="${PRESERVED_LAB_REPAIR27B_V21}/proof"

# v21 named its single stage's artefacts with this slug. It is an ARTEFACT
# FILENAME BEING READ. It is not a controller command, it is never passed to
# nh_loop.py, and the single controller call site passes STAGE4_CMD alone.
readonly V21_STAGE4_ARTEFACT="execute"

readonly EXP_V21_S4_EXITCODE_SHA="4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865"
readonly EXP_V21_S4_STDOUT_SHA="c0d541e37af81aba8a37d2dbf3a9a3283ff45779d756430970dd4891e60f4971"
readonly EXP_V21_S4_STDOUT_BYTES="100123"
readonly EXP_V21_S4_STDERR_SHA="a3123d17f8a84461cf1080a483ddb40ed27dfb6c440da3b58ba8f9be9dfded0b"
readonly EXP_V21_S4_STDERR_BYTES="5397"
readonly EXP_V21_S4_COMMAND_SHA="d5477d330585e8badcb4346fd0b64d81db787d4bec1113eda1e2914eb4277966"
readonly EXP_V21_SOURCE_PROOF_SHA="c26de83abdc9496cd1301470918ec39ecca1cf389ef0ae1c6504da1800d1c431"
readonly EXP_V21_SOURCE_PROOF_VALUE="PASS"
readonly EXP_V21_S4_EXIT="1"

# v21's own controller-refresh and isolation proofs, which are what make "the
# continuation source carries accepted Repair 27B" and "v21 ran contained"
# recorded facts rather than inferences.
readonly EXP_V21_REFRESH_AFTER_SHA="08c5a45c5951dc579f08325c8aeeca43c515454cce171e560daed7a80049a616"
readonly EXP_V21_REFRESH_COMPOSITE_SHA="2d6e3e990938a8b0722e1e7953db579254348580f5948bcfdacaabd9a8619013"
readonly EXP_V21_ISOLATION_SELFTEST_SHA="5cf5673751efac138f1a5d7835889c5daed02d52c4c57634c440d0ba628143f0"

# v21's OWN preserved authentication of the completed v20 Doors-1-to-3 result.
# v22 re-authenticates the v20 artefacts directly as well; this artefact is
# additionally frozen so the CHAIN of authentications is itself evidence.
readonly EXP_V21_V20_AUTH_SHA="0d86172db06d23f47f8d3115a6c2529713060ba3b9f1d23047cf43f4e1e140ae"

# THE EXACT REQUIRED v21 STAGE-4 FACTS, as the controller reported them at TOP
# LEVEL. Every one of these is read back through the same REPORT_PARSER the v20
# gate uses; none is inferred from prose.
readonly EXP_V21_S4_OK="false"
readonly EXP_V21_S4_STOP_REASON='"CLAUDE_SPECIFICATION_STOP"'
readonly EXP_V21_S4_PREPARATION_OK="true"
readonly EXP_V21_S4_PIECE3_ENFORCED="true"
readonly EXP_V21_S4_PIECE3_UNLOCKED="true"
readonly EXP_V21_S4_ROUNDS_STARTED="3"
readonly EXP_V21_S4_ROUNDS_COMPLETED="2"
readonly EXP_V21_S4_CLAUDE_INVOCATIONS="1"
readonly EXP_V21_S4_CODEX_AUDITS="1"
readonly EXP_V21_S4_ROUND_LIMIT="5"
readonly EXP_V21_S4_NESS_QUESTION_ASKED="false"
readonly EXP_V21_S4_PIECE3_ROUTE="null"
readonly EXP_V21_S4_ACCEPTANCE_CLAIMED="false"

# THE ROUND-3 FACTS THAT LIVE INSIDE correction_history AND ARE THEREFORE NOT
# TOP-LEVEL FIELDS. They are gated as EXACT NEEDLES in the preserved report, in
# the same way the v20 gate pins its three crash lines. Reading them as
# top-level fields would be wrong: the top-level stop-marker fields describe the
# INITIAL design write, which never happened, and are legitimately false.
readonly EXP_V21_R3_STOP_MARKER='"claude_specification_stop_marker": true,'
readonly EXP_V21_R3_STOP_VERIFIED='"claude_specification_stop_verified": true,'
readonly EXP_V21_R3_STOP_CLASS='"claude_specification_stop_classification": "source_or_technical_unknown",'
readonly EXP_V21_R3_SPEC_SHA='"correction_specification_sha256": "c6fab32788bc2ea499fa8e6ebe0e37663d91555b173e8321e2e2374fdb8bd39a",'
readonly EXP_V21_R3_REVIEW_SIGNAL='"review_signal_recorded": null,'

# The two blocking finding titles the stopped round carried, verbatim. They are
# READ as evidence that this is the recorded round; nothing classifies them, and
# no disposition, verdict or answer is derived from them anywhere in this file.
readonly EXP_V21_R3_FINDING1="The static question identity freezes the first authority outcome across later evidence changes"
readonly EXP_V21_R3_FINDING2="The candidate names superseded Decision Defaults v2.2 as current governing authority"

# THE ONE PATH THE REFRESH IS AUTHORISED TO CHANGE IN THE NEW COPY.
#
# It governs one comparison only: NEW COPY vs CONTINUATION SOURCE, in section 7b.
readonly REFRESH_ALLOWED_EXACT_LOOP="controller/nh_loop.py"

# --- THE THREE EXPLAINED WORKSPACE-ROOT DIRECTORIES ---
#
# .agents, .codex and .git at the protected workspace ROOT are classified as
# explained Codex/tool workspace artefacts, and are frozen by exact path and
# exact safe shape. Their future contents are NOT trusted, they are NOT N.H
# authority, and their presence authorises no Codex configuration, no skills and
# no Git activity. The classification covers THREE EMPTY DIRECTORIES; it does not
# whitelist their future contents, and one entry appearing under any of them
# fails the run.
readonly WS_SPECIAL_DIRS=(
  "${WS}/.agents"
  "${WS}/.codex"
  "${WS}/.git"
)
readonly WS_SPECIAL_DIR_EXPECTED_ENTRIES="0"

readonly JOURNAL="${STATE}/nh_interview_journal.jsonl"
readonly JOURNAL_HEAD="${STATE}/nh_interview_journal.head"
readonly AUTH_KEY="${STATE}/nh_interview_authenticity.key"
readonly LOCK_TXN="${STATE}/nh_candidate_transaction.lock"
readonly LOCK_JOURNAL="${STATE}/nh_interview_journal.lock"

# --- lab: NEW, keyed to REPAIR27B, to V21, to the exact accepted Repair-27B
#     controller identity AND to the routed signal this rehearsal carries forward.
#
# Never reused. If this exact path already exists the launcher ABORTS in section
# 3: it does not delete it, does not clean it, does not overwrite it and does not
# write into it. No older lab is ever deleted to make room.
#
# THE COMPLETED v20 LAB PATH IS NOT THIS PATH. v20 DID run, so its lab exists; it
# is PRESERVED_LAB_REPAIR27B_V21 above, it is this run's READ-ONLY continuation
# source, and this launcher will neither reuse nor delete it.
readonly LAB="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR28_CONTINUATION_V24_6d5e716fc6b2d777c4f65c726588a6e96b98ee67277f907c7d253ecc48edc172_rs_2593b06ab1684bbf19a6ffb70d915bd2"

# THE PRESERVED EARLIER REHEARSAL LABS. These constants exist so the launcher can
# refuse to collide with any of them and can witness that none moved. Each
# appears in this file ONLY in a readonly assignment, a printf and a comparison
# -- never in a write position.
readonly PRESERVED_LAB_V1="/home/ness/NH_AICP_SHADOW_REHEARSAL_ce3a38f43f287a56bd635ed836edf002a2db50a7"
readonly PRESERVED_LAB_REPAIR9="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR9_acc8dee2c3ae0a27738fc1c1b4b08bb30bb55243d8ce9c22c393c6505e798690"
readonly PRESERVED_LAB_REPAIR10="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR10_704ad177f1ec25a33f1fe026a94429dad96d65c62030737cb4cfc23d1e28be6f"
readonly PRESERVED_LAB_REPAIR14="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR14_76b60e90e2bc6835edb088df7126428e2365e16cb376cb00274a086de1698957"
readonly PRESERVED_LAB_REPAIR15="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR15_94f0734f65da7e13964858c06f9e9fec4774f72045115caa03ecc34759d4a9e9"
readonly PRESERVED_LAB_REPAIR16="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR16_882fe3e510544b97361bd31853d39d5269b0e1fb4d39dbc2b0a387f139b10833"
readonly PRESERVED_LAB_REPAIR17="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR17_6a3ce02e4a0448d5a7206f6eb4260bbcb87989da9f0a541feafea7dd4be0dc19"
readonly PRESERVED_LAB_REPAIR18_CONTINUATION_V11="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR18_CONTINUATION_V11_440cf8cf4286b4682c5add47e49d8e19de4020d4c8a0ffbe320573dc654969c2_rs_2593b06ab1684bbf19a6ffb70d915bd2"
readonly PRESERVED_LAB_REPAIR19B_V13="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR19B_V13_235885af469a6b5f3f428d206c77072712ef4b8d68caa37acf43445fc321bf02_rs_2593b06ab1684bbf19a6ffb70d915bd2"
readonly PRESERVED_LAB_REPAIR20B_V14="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR20B_V14_3fbb204524348b7e9d32409a81d417e817aec5a3a3239b87e215313490ea5963_rs_2593b06ab1684bbf19a6ffb70d915bd2"
readonly PRESERVED_LAB_REPAIR21_V15="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR21_V15_a54f9e5ffd77470e9c0eb60552aa207e5ab24c8b45bff09765fe552fa5c910cd_rs_2593b06ab1684bbf19a6ffb70d915bd2"
readonly PRESERVED_LAB_REPAIR25_V18="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR25_V18_91b89aadafe613f28393269c6dcb3321d8872de0bf6c97f3cdbc874be7e97595_rs_2593b06ab1684bbf19a6ffb70d915bd2"
readonly PRESERVED_LAB_REPAIR26_V19="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR26_V19_8970e9e4ee4e1d2219b36ec89215b8e92ccd1ecadce2dd1ff111c63b6ba18c36_rs_2593b06ab1684bbf19a6ffb70d915bd2"

# --------------------------------------------------------------------------
# THE v11 HISTORICAL WITNESS — THE ONLY AUTHORISED SOURCE OF THE EXPECTED
# HISTORICAL LINEAGE-SEED IDENTITY
# --------------------------------------------------------------------------
#
# Carried forward from v20 unchanged. The completed v11 run captured the FULL
# preserved-artefact sweep at four separate moments in its own life -- before,
# during, after question-validation and after. The preserved v10 seed sits inside
# a preserved lab, so every one of those four captures already contains a
# complete record of it: a sha256 for every regular file, and type / mode / size
# for every entry. That is the historical witness, and it was written before the
# defect it closes was known.
#
# EACH FILE IS FROZEN BY ITS OWN sha256 AND BYTE COUNT. A moved witness fails the
# run CLOSED, before any provider or model call. Nothing here is written,
# repaired, normalised or regenerated: this lab appears in this file only in
# readonly assignments, in printf, and as a READ-ONLY input.
#
# All four snapshots must independently yield ONE byte-identical expected
# manifest. There is no majority vote, no averaging, no choosing, and no fallback
# to today's seed. Disagreement stops the run.
readonly V11_PROOF_DIR="${PRESERVED_LAB_REPAIR18_CONTINUATION_V11}/proof"

readonly V11_WITNESS_SNAPSHOTS=(
  "original.before"
  "original.during"
  "original.after-question-validation"
  "original.after"
)

readonly EXP_V11_WITNESS_SHA_FILE_SHA="a7b163e4f58b699f3cd719533260e00eda8d71477ee2b8b008502d964ab3232f"
readonly EXP_V11_WITNESS_SHA_FILE_BYTES="951013"
readonly EXP_V11_WITNESS_META_FILE_SHA="3915f56086f285246b1670e5fa34cdd550dadad475656827d84130f143614949"
readonly EXP_V11_WITNESS_META_FILE_BYTES="1150504"

# --------------------------------------------------------------------------
# THE CANONICAL HISTORICAL LINEAGE-SEED MANIFEST, FROZEN BY DIGEST
# --------------------------------------------------------------------------
#
# Computed by running the canonicalizer below against the four v11 witnesses --
# NOT against the current seed. All four agreed. 308 total = 234 regular files +
# 74 directories.
readonly EXP_HIST_SEED_MANIFEST_SHA="b21c480b4cb79d5ae5f82663332832afd16b08c3df6c25338f4e7b3bc72399bd"
readonly EXP_HIST_SEED_MANIFEST_ENTRIES="308"
readonly EXP_HIST_SEED_MANIFEST_FILES="234"
readonly EXP_HIST_SEED_MANIFEST_DIRS="74"
readonly EXP_HIST_SEED_MANIFEST_SYMLINKS="0"

# THE PRESERVED-ARTEFACT SWEEP GLOB.
#
# Every disposable artefact Ness holds directly under /home/ness is witnessed
# before, during and after this run. THE COMPLETED v20 LAB IS INSIDE THIS SWEEP,
# entry by entry, which is what makes "the v20 lab did not move" a measured fact
# rather than a promise. The new lab is excluded from it explicitly because that
# one is being written by design.
readonly PRESERVED_SWEEP_GLOB="NH_AICP_*"

readonly SHADOW_WS="${LAB}/shadow/NH_CLAUDE_CODEX_DESIGN_LOOP"
readonly RUNTIME_TMP="${LAB}/runtime/tmp"
readonly PROOF="${LAB}/proof"
readonly SHADOW_MARKER_NAME=".nh_shadow_marker"

# --- THE ONE STAGE ---
#
# It has one slug, and every artefact it produces is that slug plus a fixed
# suffix, so a reader can find all of its evidence by name alone:
#
#   <slug>.command     the exact argv, one element per line
#   <slug>.stdout      the machine report
#   <slug>.stderr      the live progress
#   <slug>.exit-code   the integer, or NOT-RUN
#   <slug>.started     ISO-8601 UTC, taken immediately before the namespace
#   <slug>.finished    ISO-8601 UTC, taken immediately after it exits
#   original.after-<slug>/   that stage's own protected-source proof
readonly STAGE4_SLUG="execute"

# THE ONE CONTROLLER COMMAND. This constant is used at EXACTLY ONE executable
# call site, in section 11. THERE IS NO SECOND CONTROLLER COMMAND CONSTANT
# ANYWHERE IN THIS FILE, and therefore nothing this launcher could pass to
# nh_loop.py other than the value below.
readonly STAGE4_CMD="execute-next-claude-task"

readonly ALL_STAGE_SLUGS=(
  "$STAGE4_SLUG"
)

# --- toolchain ---
readonly BWRAP="/usr/bin/bwrap"
readonly PY3="/usr/bin/python3"
readonly NODE_BIN="/home/ness/.nvm/versions/node/v24.18.0/bin"

# --- host model-auth / config witness set (HASHES AND METADATA ONLY) ---
readonly HOST_CODEX="/home/ness/.codex"
readonly HOST_CLAUDE="/home/ness/.claude"
readonly HOST_CLAUDE_JSON="/home/ness/.claude.json"

# --- reserved verdict exit codes ---
readonly RC_ORIGINAL_PROOF_FAIL=90
readonly RC_CREDENTIAL_WITNESS_CHANGED=91
readonly RC_PRESERVED_LAB_PROOF_FAIL=92
readonly RC_LAB_CREDENTIAL_FOUND=93
# The historical lineage seed has its own verdict and its own reserved code, so a
# moved lineage seed is never reported as, or hidden behind, a preserved-lab or
# protected-workspace verdict.
readonly RC_REGRESSION_SEED_PROOF_FAIL=94
# NEW IN v21. The continuation source gets its own verdict and its own reserved
# code for exactly the same reason: it is the one piece of state this entire
# continuation depends on, and if it moves the run must say so in those words
# rather than as one changed line inside a listing of thousands.
readonly RC_CONTINUATION_SOURCE_PROOF_FAIL=95

# THE EARLY-STOP STATUS. It is NOT a safety verdict and it is NOT corruption.
#
# With one stage it can only mean that a protected object changed during the
# stage while the final proofs still passed. It exists so that condition can
# never be reported as an ordinary success.
#
# 3 is chosen deliberately: nh_loop.py returns only 0, 1 and 2, so 3 cannot be
# confused with a controller status, and it sits well clear of the 90-95 safety
# codes, which still outrank it.
readonly RC_SEQUENCE_STOPPED=3

# Proof artefacts of the PROTECTED ORIGINAL that MUST be byte-identical before
# and after.
readonly PROTECTED_PROOF_FILES=(
  "nh_loop.identity"
  "controller_bytecode.identity"
  "launchers.identity"
  "controller.git"
  "governance.git"
  "candidates.sha256"
  "authority.sha256"
  "unreal_wonder.sha256"
  "interview_state.sha256"
  "interview_state.meta"
  "journal.counts"
  "workspace.files.sha256"
  "workspace.meta"
)

# Proof artefacts of PRESERVED EARLIER LABS. Kept as their own set, with their
# own verdict and their own reserved exit code, so a preserved-evidence failure
# is never reported as, or hidden behind, a protected-workspace verdict. THE
# COMPLETED v20 LAB IS COVERED HERE, entry by entry, like every other NH_AICP_*
# artefact.
readonly PRESERVED_LAB_PROOF_FILES=(
  "preserved_labs.sha256"
  "preserved_labs.meta"
)

# Proof artefacts of THE HISTORICAL LINEAGE SEED, in their own set with their own
# verdict and their own reserved exit code.
readonly REGRESSION_SEED_PROOF_FILES=(
  "regression_seed.identity"
  "regression_seed.historical_witness"
  "regression_seed.historical_manifest"
)

# Proof artefacts of THE CONTINUATION SOURCE, in their own set with their own
# verdict and their own reserved exit code.        (NEW IN v21)
readonly CONTINUATION_SOURCE_PROOF_FILES=(
  "continuation_source.identity"
  "continuation_source.manifest"
  "continuation_source.v20_result"
)

# Host model-auth / config witness. Reported separately and honestly: a
# concurrently running host Claude Code or Codex session legitimately rewrites
# ~/.claude.json and ~/.claude/* while this launcher runs, and that is NOT an
# isolation breach. It is still surfaced, and it still fails the launcher.
readonly CREDENTIAL_PROOF_FILES=(
  "credentials.sha256"
  "credentials.meta"
)

# ==========================================================================
# SECTION 1 — PLUMBING
# ==========================================================================

say()  { printf '%s\n' "$*"; }
note() { printf '[ok]    %s\n' "$*"; }
step() { printf '\n=== %s ===\n' "$*"; }

# ---- audit state. Every claim any report makes is derived from these. --------
LAB_CREATED=0
RUN_STARTED=0
CONTROLLER_REFRESH="NOT-RUN"
# THE INHERITED REPAIR-25 SEAM OBSERVATION FIELD.
#
# ITS NAME IS DELIBERATE AND IS NOT REBASED. The seam it observes is a REPAIR-25
# invariant. Accepted Repair 27B is built, through 27A, 27, 26, on accepted
# Repair 25 and INHERITS that behaviour unchanged; Repair 27B did not invent it,
# and renaming the field would claim otherwise.
#
# NOT-RUN until the observation pass runs. It then becomes exactly one of
# PASS / FAIL / NOT-EXERCISED, and NOT-EXERCISED IS NOT A FAILURE: it simply
# means Stage 4 ended for some other reason, including an ordinary full PASS.
# It gates NO stage, grants NO pass and can stop nothing.
REPAIR25_CHATGPT_STOP_HANDOFF="NOT-RUN"
CONTINUATION_STATE="NOT-RUN"
REPORTED=0
AFTER_PROOF_DONE=0
ORIGINAL_PROOF="NOT-RUN"
PRESERVED_LAB_PROOF="NOT-RUN"
REGRESSION_SEED_PROOF="NOT-RUN"
CONTINUATION_SOURCE_PROOF="NOT-RUN"
V21_RESULT_AUTHENTICATED="NOT-RUN"
V20_RESULT_AUTHENTICATED="NOT-RUN"
LAB_CREDENTIAL_SCAN="NOT-RUN"

# THE ONE STAGE RESULT. NOT-RUN is a real, reported state and is never silently
# rendered as success or as failure: a stage that never ran because the launcher
# stopped earlier is a different fact from a stage that ran and returned zero,
# and this launcher keeps the two apart everywhere.
EXEC_RC="NOT-RUN"
STAGE_RC=""

# WHY THE RUN STOPPED, in this launcher's own words. Set once and reported
# verbatim. "" means nothing observed forbade completion.
SEQUENCE_STOP_REASON=""

# The stage's protected-source proof verdict, and the flag that stops downstream
# work the instant it fails.
STAGE_SOURCE_PROOF=""
CONTAINMENT_BREACHED=0

# LOCKS_TAKEN / LOCKS_HELD : the two advisory locks are the one operation this
# launcher performs against the protected original that is NOT a plain read, so
# the report must be able to say exactly whether they were taken and whether they
# are still held. They are COUNTS, not booleans, and each is updated the instant
# its own lock is acquired or released.
LOCKS_TAKEN=0
LOCKS_HELD=0

# The shared, honest tail. Both the block path and the unexpected-exit path use
# it, so the two can never drift apart and claim different things.
report_state() {
  # --- what actually ran ---
  if [ "$RUN_STARTED" = "1" ]; then
    printf 'The isolated controller stage WAS entered, so real Codex / Claude\n' >&2
    printf 'provider calls may already have been made.\n' >&2
    printf '  stage 4  execute-next-claude-task : %s\n' "$EXEC_RC" >&2
    if [ -n "$SEQUENCE_STOP_REASON" ]; then
      printf '  the run stopped because: %s\n' "$SEQUENCE_STOP_REASON" >&2
    fi
  else
    printf 'No isolated controller stage was started.\n' >&2
    printf 'No model or provider call was made.\n' >&2
  fi
  printf 'Doors 1-3 (question-validation, question-coverage-review,\n' >&2
  printf 'interview-gate) were NOT run by this launcher on any path. It holds no\n' >&2
  printf 'constant and no call site able to run them.\n' >&2

  # --- what can honestly be said about the protected original ---
  if [ "$AFTER_PROOF_DONE" = "1" ]; then
    printf 'The protected original WAS re-proved after the run: %s\n' "$ORIGINAL_PROOF" >&2
  elif [ "$RUN_STARTED" = "1" ]; then
    printf 'The protected original has NOT been re-proved. This launcher issued\n' >&2
    printf 'no create, write, append, truncate, rename, link, unlink, chmod, chown\n' >&2
    printf 'or utimes against it, but a sandboxed stage was entered and whether\n' >&2
    printf 'that stage stayed contained is UNVERIFIED. Do not assume the original\n' >&2
    printf 'is untouched -- re-verify it by hand before drawing any conclusion.\n' >&2
  else
    printf 'This launcher issued no create, write, append, truncate, rename, link,\n' >&2
    printf 'unlink, chmod, chown or utimes against the protected original.\n' >&2
    printf 'No sandboxed stage was entered.\n' >&2
  fi

  if [ "$LOCKS_HELD" -gt 0 ]; then
    printf 'Advisory locks on the interview-state lock files: %s of 2 taken, %s\n' \
           "$LOCKS_TAKEN" "$LOCKS_HELD" >&2
    printf 'STILL HELD by this process. They are released as it exits.\n' >&2
  elif [ "$LOCKS_TAKEN" -gt 0 ]; then
    printf 'Advisory locks on the interview-state lock files: %s of 2 taken, all\n' \
           "$LOCKS_TAKEN" >&2
    printf 'released. Advisory locks change no file content and no metadata field.\n' >&2
  else
    printf 'No lock was taken on the protected original.\n' >&2
  fi
  printf 'Reads can refresh atime, which no proof captures. The complete and\n' >&2
  printf 'exact statement is under READ-ONLY, STATED EXACTLY in this launcher.\n' >&2

  # --- the preserved earlier rehearsals, the lineage seed and the source ---
  printf '\nThe preserved earlier rehearsal labs are never reused and never deleted\n' >&2
  printf 'by this launcher on any path. They are opened only for reading, to\n' >&2
  printf 'witness them; that can refresh atime, which no proof captures, and\n' >&2
  printf 'changes nothing else about them:\n' >&2
  printf '  %s\n' "$PRESERVED_LAB_V1" >&2
  printf '  %s\n' "$PRESERVED_LAB_REPAIR9" >&2
  printf '  %s\n' "$PRESERVED_LAB_REPAIR10" >&2
  printf '  %s\n' "$PRESERVED_LAB_REPAIR14" >&2
  printf '  %s\n' "$PRESERVED_LAB_REPAIR15" >&2
  printf '  %s\n' "$PRESERVED_LAB_REPAIR16" >&2
  printf '  %s\n' "$PRESERVED_LAB_REPAIR17" >&2
  printf '  %s\n' "$PRESERVED_LAB_REPAIR17_CONTINUATION_V10" >&2
  printf '  %s\n' "$PRESERVED_LAB_REPAIR18_CONTINUATION_V11" >&2
  printf '  %s\n' "$PRESERVED_LAB_REPAIR19B_V13" >&2
  printf '  %s\n' "$PRESERVED_LAB_REPAIR20B_V14" >&2
  printf '  %s\n' "$PRESERVED_LAB_REPAIR21_V15" >&2
  printf '  %s\n' "$PRESERVED_LAB_REPAIR25_V18" >&2
  printf '  %s\n' "$PRESERVED_LAB_REPAIR26_V19" >&2
  printf '  %s\n' "$PRESERVED_LAB_REPAIR27A_V20" >&2
  printf '  %s\n' "$PRESERVED_LAB_REPAIR27B_V21" >&2
  printf 'The v10 lab is this run\047s HISTORICAL LINEAGE SEED. It was read to be\n' >&2
  printf 'authenticated and for nothing else: in v24 it is never copied.\n' >&2
  printf 'The v21 lab is this run\047s CONTINUATION SOURCE. It was read to be\n' >&2
  printf 'copied, to be authenticated, and to have the completed v21 Stage-4\n' >&2
  printf 'result proved from its own artefacts. The v20 lab is preserved\n' >&2
  printf 'ANCESTOR evidence only -- it is where Doors 1 to 3 actually ran and\n' >&2
  printf 'passed -- and it is read to authenticate that earlier result, never\n' >&2
  printf 'copied as this run\047s continuation source. Nothing else was done to\n' >&2
  printf 'either: no create, write, append, truncate, rename, link, unlink,\n' >&2
  printf 'chmod, chown or utimes was issued against them, and no Git command was\n' >&2
  printf 'run inside them.\n' >&2
  if [ "$AFTER_PROOF_DONE" = "1" ]; then
    printf 'They were re-witnessed after the run: %s\n' "$PRESERVED_LAB_PROOF" >&2
    printf 'The lineage seed was re-witnessed by name: %s\n' "$REGRESSION_SEED_PROOF" >&2
    printf 'The continuation source was re-witnessed by name: %s\n' "$CONTINUATION_SOURCE_PROOF" >&2
  fi

  # --- what is left on disk ---
  if [ "$LAB_CREATED" = "1" ]; then
    printf '\nA disposable lab WAS created by this run and is being left on disk for\n' >&2
    printf 'inspection (this launcher never deletes a lab):\n' >&2
    printf '  %s\n' "$LAB" >&2
    printf 'Its contents depend on how far this run got, and it INCLUDES a copy of\n' >&2
    printf 'the N.H interview authenticity key. It is mode 0700.\n' >&2
    printf 'Lab credential marker scan: %s\n' "$LAB_CREDENTIAL_SCAN" >&2
    printf 'That scan is a SHAPE scan and is never proof that the lab holds no\n' >&2
    printf 'credential material. Treat the lab as sensitive either way.\n' >&2
    printf 'Review it, then delete it. This launcher refuses to run again while\n' >&2
    printf 'that path exists.\n' >&2
  else
    printf '\nThis run created no lab.\n' >&2
  fi
}

die() {
  REPORTED=1
  printf '\n[BLOCKED] %s\n' "$*" >&2
  printf '\nSHADOW_REHEARSAL=BLOCKED\n' >&2
  report_state
  exit 1
}

# An EXIT handler, deliberately NOT an ERR handler. An ERR trap fires even under
# `set +e`, so it would hijack the places where a non-zero exit is EXPECTED and
# handled on purpose: the isolation self-test, and above all the four real
# controller stages, whose non-zero exits are ordinary outcomes this launcher
# exists to record. An ERR trap there would abort before the AFTER proof ever ran
# -- destroying the most important safety output -- while printing claims that
# were false at that point.
on_exit() {
  local rc=$?
  trap - EXIT
  if [ "$rc" -ne 0 ] && [ "$REPORTED" != "1" ]; then
    REPORTED=1
    printf '\n[BLOCKED] the launcher stopped unexpectedly (exit %s)\n' "$rc" >&2
    printf '\nSHADOW_REHEARSAL=BLOCKED\n' >&2
    report_state
  fi
  exit "$rc"
}
trap on_exit EXIT

need_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "required command not found: $1"
}

expect() {
  # expect <label> <actual> <expected>
  local label="$1" actual="$2" expected="$3"
  if [ "$actual" != "$expected" ]; then
    die "frozen identity mismatch for ${label}
        expected: ${expected}
        actual:   ${actual}
      The protected source state has moved since this launcher was constructed.
      The regression refuses to run against source that is not the source it was
      frozen against.
      NOTHING IS RESOLVED BY RESETTING, REVERTING OR CHECKING ANYTHING OUT. If
      the movement is legitimate, re-freeze a new launcher against the real
      current state deliberately, exactly as every earlier rebase did."
  fi
  note "${label} matches frozen identity"
}

# These MUST fail loudly. The naive `sha256sum -- "$1" | awk '{print $1}'` form
# inside a command substitution yields an EMPTY string when sha256sum cannot read
# the file, and printf then happily records a blank hash with exit status zero.
# Two captures that failed the same way -- an unreadable file before and after --
# produce byte-identical listings, compare EQUAL, and get reported as proof that
# nothing changed. A distinct sentinel cannot be mistaken for a hash, fails every
# frozen comparison, and is visible in the proof artefacts.
sha_of() {
  local out
  if out="$(sha256sum -- "$1")"; then
    printf '%s\n' "${out%% *}"
  else
    printf 'SHA256-UNREADABLE\n'
  fi
}

bytes_of() {
  local out
  if out="$(stat -c '%s' -- "$1")"; then
    printf '%s\n' "$out"
  else
    printf 'STAT-UNREADABLE\n'
  fi
}

mode_of() {
  local out
  if out="$(stat -c '%a' -- "$1")"; then
    printf '%s\n' "$out"
  else
    printf 'STAT-UNREADABLE\n'
  fi
}

# Read-only git. GIT_OPTIONAL_LOCKS=0 keeps `git status` from refreshing (and
# therefore writing) the index. THERE IS NO GIT WRITE ANYWHERE IN THIS FILE.
git_ro() {
  local repo="$1"; shift
  GIT_OPTIONAL_LOCKS=0 GIT_TERMINAL_PROMPT=0 git --no-optional-locks -C "$repo" "$@"
}

# ==========================================================================
# SECTION 2 — ORIGINAL PROOF CAPTURE (hashes and metadata only, never secrets)
# ==========================================================================

capture_original_proof() {
  local out="$1"
  mkdir -p "$out"

  # Every capture error in this function lands here, and a non-empty errors file
  # fails the capture. A proof that is silently incomplete is worse than no
  # proof: two equally incomplete captures compare EQUAL and are then reported as
  # evidence of containment.
  local cap_err="${out}/capture.errors"
  : > "$cap_err"

  local d lf c

  # --- nh_loop.py identity ---
  {
    printf 'sha256 %s\n' "$(sha_of "${CTRL}/nh_loop.py")"
    printf 'bytes  %s\n'  "$(bytes_of "${CTRL}/nh_loop.py")"
    printf 'lines  %s\n'  "$(wc -l < "${CTRL}/nh_loop.py")"
    printf 'stat   %s\n'  "$(stat -c 'mode=%f perm=%a uid=%u gid=%g size=%s mtime=%Y ctime=%Z inode=%i links=%h' -- "${CTRL}/nh_loop.py")"
  } > "${out}/nh_loop.identity"

  # --- the accepted Repair-20B candidate identity (NEW IN v14) ---
  # Captured before, during and after exactly like the real controller, so the
  # sweep proves the file this rehearsal reads was not edited underneath it.
  {
    printf 'sha256 %s\n' "$(sha_of "$R20B_CANDIDATE")"
    printf 'bytes  %s\n'  "$(bytes_of "$R20B_CANDIDATE")"
    printf 'lines  %s\n'  "$(wc -l < "$R20B_CANDIDATE")"
    printf 'stat   %s\n'  "$(stat -c 'mode=%f perm=%a uid=%u gid=%g size=%s mtime=%Y ctime=%Z inode=%i links=%h' -- "$R20B_CANDIDATE")"
  } > "${out}/repair20b_candidate.identity"

  # --- the Repair-21 candidate identity (NEW IN v15) ---
  # Preserved repair evidence in v16, not the refresh source. Captured before,
  # during and after exactly as it was in v15, so the sweep proves it was not
  # edited underneath this run.
  {
    printf 'sha256 %s\n' "$(sha_of "$R21_CANDIDATE")"
    printf 'bytes  %s\n'  "$(bytes_of "$R21_CANDIDATE")"
    printf 'lines  %s\n'  "$(wc -l < "$R21_CANDIDATE")"
    printf 'stat   %s\n'  "$(stat -c 'mode=%f perm=%a uid=%u gid=%g size=%s mtime=%Y ctime=%Z inode=%i links=%h' -- "$R21_CANDIDATE")"
  } > "${out}/repair21_candidate.identity"

  # --- the ACCEPTED REPAIR-25 candidate identity ---
  #
  # PRESERVED REPAIR EVIDENCE in v20, not the refresh source. It WAS v18's
  # refresh source, and its proof keeps its own truthful name. Captured before,
  # during and after exactly as it was in v18, so the sweep proves it was not
  # edited underneath this run.
  {
    printf 'sha256 %s\n' "$(sha_of "$R25_CANDIDATE")"
    printf 'bytes  %s\n'  "$(bytes_of "$R25_CANDIDATE")"
    printf 'lines  %s\n'  "$(wc -l < "$R25_CANDIDATE")"
    printf 'stat   %s\n'  "$(stat -c 'mode=%f perm=%a uid=%u gid=%g size=%s mtime=%Y ctime=%Z inode=%i links=%h' -- "$R25_CANDIDATE")"
  } > "${out}/repair25_candidate.identity"

  # --- the ACCEPTED REPAIR-26 candidate identity ---
  #
  # PRESERVED REPAIR EVIDENCE in v20, not the refresh source. It WAS v19's
  # refresh source, and its proof keeps its own truthful name.
  # Captured before, during and after exactly like the real controller, so the
  # sweep proves the file this rehearsal reads was not edited underneath it. The
  # artefact is named for what it actually measures.
  {
    printf 'sha256 %s\n' "$(sha_of "$R26_CANDIDATE")"
    printf 'bytes  %s\n'  "$(bytes_of "$R26_CANDIDATE")"
    printf 'lines  %s\n'  "$(wc -l < "$R26_CANDIDATE")"
    printf 'stat   %s\n'  "$(stat -c 'mode=%f perm=%a uid=%u gid=%g size=%s mtime=%Y ctime=%Z inode=%i links=%h' -- "$R26_CANDIDATE")"
  } > "${out}/repair26_candidate.identity"

  # --- the REPAIR-27 candidate identity (NEW IN v20) ---
  # Preserved repair evidence, not the refresh source. Captured before, during
  # and after so the sweep proves it was not edited underneath this run.
  {
    printf 'sha256 %s\n' "$(sha_of "$R27_CANDIDATE")"
    printf 'bytes  %s\n'  "$(bytes_of "$R27_CANDIDATE")"
    printf 'lines  %s\n'  "$(wc -l < "$R27_CANDIDATE")"
    printf 'stat   %s\n'  "$(stat -c 'mode=%f perm=%a uid=%u gid=%g size=%s mtime=%Y ctime=%Z inode=%i links=%h' -- "$R27_CANDIDATE")"
  } > "${out}/repair27_candidate.identity"

  # --- the ACCEPTED REPAIR-27A candidate identity (NEW IN v20) ---
  #
  # THE ONE FILE THIS REHEARSAL EXISTS TO TEST, and the sole refresh source.
  # Captured before, during and after exactly like the real controller, so the
  # sweep proves the file this rehearsal reads was not edited underneath it.
  {
    printf 'sha256 %s\n' "$(sha_of "$R27A_CANDIDATE")"
    printf 'bytes  %s\n'  "$(bytes_of "$R27A_CANDIDATE")"
    printf 'lines  %s\n'  "$(wc -l < "$R27A_CANDIDATE")"
    printf 'stat   %s\n'  "$(stat -c 'mode=%f perm=%a uid=%u gid=%g size=%s mtime=%Y ctime=%Z inode=%i links=%h' -- "$R27A_CANDIDATE")"
  } > "${out}/repair27a_candidate.identity"

  # --- the ACCEPTED REPAIR-27B candidate identity (NEW IN v21) ---
  #
  # THE ONE FILE THIS CONTINUATION EXISTS TO TEST, and the sole refresh source.
  # Captured before, during and after exactly like the real controller, so the
  # sweep proves the file this run reads was not edited underneath it.
  {
    printf 'sha256 %s\n' "$(sha_of "$R27B_CANDIDATE")"
    printf 'bytes  %s\n'  "$(bytes_of "$R27B_CANDIDATE")"
    printf 'lines  %s\n'  "$(wc -l < "$R27B_CANDIDATE")"
    printf 'stat   %s\n'  "$(stat -c 'mode=%f perm=%a uid=%u gid=%g size=%s mtime=%Y ctime=%Z inode=%i links=%h' -- "$R27B_CANDIDATE")"
  } > "${out}/repair27b_candidate.identity"

  # --- controller bytecode identity (NEW IN v12; CORRECTED IN v18) ---
  #
  # THE v17 RUNTIME BLOCKER THIS CLOSES. v17 correctly moved the frozen bytecode
  # state from ONE file to THREE, into CTRL_PYCACHE_FILES / CTRL_PYCACHE_SHAS /
  # CTRL_PYCACHE_BYTES_LIST, and assert_controller_bytecode_frozen() was
  # correctly rewritten to iterate them. THIS block was not: it still read the
  # obsolete singular scalar CTRL_PYCACHE_FILE, which v17 no longer defines.
  # Under `set -Eeuo pipefail` the very first capture -- original.before, taken
  # before the lab is even created -- would have aborted the launcher with an
  # unbound-variable error, so v17 could never have reached its own rehearsal.
  #
  # NO COMPATIBILITY SCALAR IS REINTRODUCED. Restoring a single CTRL_PYCACHE_FILE
  # would only make the old one-file proof run again, which is exactly the
  # incomplete proof v17 replaced. This records the COMPLETE frozen set instead,
  # from the SAME arrays the assertion uses, so the proof and the gate can never
  # describe different bytecode.
  #
  # DETERMINISTIC AND BYTE-STABLE. The path listing is sorted; the per-file block
  # walks the array indices in order; nothing here reads a clock, a PID or a
  # directory order. Two captures over an unchanged tree produce identical bytes,
  # which is what makes the before/during/after comparison meaningful at all.
  #
  # A second .pyc appearing anywhere under the controller shows up here as a new
  # path and fails the before/after comparison.
  {
    printf 'bytecode_paths\n'
    find "${CTRL}" -name '__pycache__' -o -name '*.pyc' 2>> "$cap_err" | LC_ALL=C sort
    printf 'frozen_count   %s\n' "${#CTRL_PYCACHE_FILES[@]}"
    for _bc in "${!CTRL_PYCACHE_FILES[@]}"; do
      printf 'frozen_file    %s\n' "${CTRL_PYCACHE_FILES[$_bc]}"
      printf 'sha256         %s\n' "$(sha_of "${CTRL_PYCACHE_FILES[$_bc]}")"
      printf 'bytes          %s\n' "$(bytes_of "${CTRL_PYCACHE_FILES[$_bc]}")"
    done
    unset _bc
  } > "${out}/controller_bytecode.identity"

  # --- all TWENTY launcher artefacts: v1-v19 must stay byte-identical, and
  #     this file must stay byte-identical to itself across the run ---
  #
  # v20 cannot hash-gate on itself in the frozen-identity gate, which is exactly
  # why it must appear HERE: the before/during/after comparison is what proves
  # the running launcher did not change underneath itself.
  {
    for lf in "$LAUNCHER_V1_BASENAME" "$LAUNCHER_V2_BASENAME" \
              "$LAUNCHER_V3_BASENAME" "$LAUNCHER_V4_BASENAME" \
              "$LAUNCHER_V5_BASENAME" "$LAUNCHER_V6_BASENAME" \
              "$LAUNCHER_V7_BASENAME" "$LAUNCHER_V8_BASENAME" \
              "$LAUNCHER_V9_BASENAME" "$LAUNCHER_V10_BASENAME" \
              "$LAUNCHER_V11_BASENAME" "$LAUNCHER_V12_BASENAME" \
              "$LAUNCHER_V13_BASENAME" "$LAUNCHER_V14_BASENAME" \
              "$LAUNCHER_V15_BASENAME" "$LAUNCHER_V16_BASENAME" \
              "$LAUNCHER_V17_BASENAME" "$LAUNCHER_V18_BASENAME" \
              "$LAUNCHER_V19_BASENAME" "$LAUNCHER_V20_BASENAME"; do
      if [ -f "${CTRL}/${lf}" ]; then
        printf '%s %s %s\n' "$(sha_of "${CTRL}/${lf}")" "$(bytes_of "${CTRL}/${lf}")" "$lf"
      else
        printf '%s %s %s\n' "ABSENT" "ABSENT" "$lf"
      fi
    done
  } > "${out}/launchers.identity"

  # --- controller git state (read-only) ---
  # --ignored=traditional, for two reasons. Plain --untracked-files=all silently
  # omits every gitignored path, so a capture without an --ignored mode cannot
  # see .claude/ or __pycache__/ at all. And --ignored=matching is not enough
  # either: it COLLAPSES an ignored directory to the directory itself, so a probe
  # file dropped into __pycache__/ leaves `!! __pycache__/` completely unchanged.
  # Only traditional mode can witness the ignored set file by file -- which
  # matters more in v12 than in any earlier launcher, because the controller
  # bytecode now lives in exactly that ignored set.
  {
    printf 'branch %s\n' "$(git_ro "$CTRL" rev-parse --abbrev-ref HEAD)"
    printf 'head   %s\n' "$(git_ro "$CTRL" rev-parse HEAD)"
    printf 'status\n'
    git_ro "$CTRL" status --porcelain=v1 --untracked-files=all --ignored=traditional \
      | LC_ALL=C sort
  } > "${out}/controller.git"

  # --- N.H git state (read-only) ---
  {
    printf 'branch %s\n' "$(git_ro "$NHGOV" rev-parse --abbrev-ref HEAD)"
    printf 'head   %s\n' "$(git_ro "$NHGOV" rev-parse HEAD)"
    printf 'status\n'
    git_ro "$NHGOV" status --porcelain=v1 --untracked-files=all --ignored=traditional \
      | LC_ALL=C sort
  } > "${out}/governance.git"

  # --- the four active candidates ---
  {
    for c in "$CAND_V10" "$CAND_V11" "$CAND_V12" "$CAND_DD23"; do
      printf '%s %s %s\n' "$(sha_of "${CAND_DIR}/${c}")" "$(bytes_of "${CAND_DIR}/${c}")" "$c"
    done
  } > "${out}/candidates.sha256"

  # --- the adopted authoritative Decision Defaults ---
  {
    printf '%s %s %s\n' "$(sha_of "${AUTH_DIR}/${AUTH_DD23}")" \
                        "$(bytes_of "${AUTH_DIR}/${AUTH_DD23}")" "$AUTH_DD23"
  } > "${out}/authority.sha256"

  # --- the current Unreal / Wonder design work, witnessed BY NAME (NEW IN v12) ---
  {
    printf '%s %s %s %s\n' "$(sha_of "${NHGOV}/${UNREAL_WONDER_REL}")" \
                           "$(bytes_of "${NHGOV}/${UNREAL_WONDER_REL}")" \
                           "$(mode_of "${NHGOV}/${UNREAL_WONDER_REL}")" \
                           "$UNREAL_WONDER_REL"
  } > "${out}/unreal_wonder.sha256"

  # --- every authenticated interview-state file ---
  : > "${out}/interview_state.sha256"
  hash_tree_into "$STATE" "${out}/interview_state.sha256" "$cap_err" \
    || die "could not hash the interview state; see ${cap_err}"

  find "$STATE" -maxdepth 1 -printf '%y %m %U %G %s %T@ %C@ %i %n %p\n' 2>> "$cap_err" \
    | LC_ALL=C sort \
    > "${out}/interview_state.meta"

  # --- journal line / event / scope counts ---
  {
    printf 'lines           %s\n' "$(wc -l < "$JOURNAL")"
    printf 'events          %s\n' "$(grep -c '[^[:space:]]' -- "$JOURNAL" || true)"
    printf 'bytes           %s\n' "$(bytes_of "$JOURNAL")"
    printf 'journal_sha256  %s\n' "$(sha_of "$JOURNAL")"
    printf 'head_sha256     %s\n' "$(sha_of "$JOURNAL_HEAD")"
    printf 'key_sha256      %s\n' "$(sha_of "$AUTH_KEY")"
    printf 'pkg_scope       %s\n' "$EXP_PKG_SCOPE"
    printf 'pkg_occurrences %s\n' "$(grep -c -F -- "$EXP_PKG_SCOPE" "$JOURNAL" || true)"
  } > "${out}/journal.counts"

  # --- complete protected workspace: every file hashed ---
  : > "${out}/workspace.files.sha256"
  hash_tree_into "$WS" "${out}/workspace.files.sha256" "$cap_err" \
    || die "could not hash the protected workspace; see ${cap_err}"

  # --- complete protected workspace: metadata for every entry ---
  find "$WS" -xdev -printf '%y %m %U %G %s %T@ %C@ %i %n %p\n' 2>> "$cap_err" \
    | LC_ALL=C sort \
    > "${out}/workspace.meta"

  # --- PRESERVED LABS AND ARTEFACTS: read-only witness ---
  #
  # Every NH_AICP_* artefact under /home/ness. This launcher's own lab is
  # excluded because it is being written by design. A preserved lab is NOT
  # required to exist: absence before and absence after is simply no change.
  # Appearing or vanishing mid-run is a change, and fails.
  #
  # Capture errors are NOT suppressed. A preserved lab that cannot be fully
  # traversed would otherwise produce the same partial listing before and after,
  # compare equal, and be reported as PRESERVED_LAB_PROOF=PASS on a witness that
  # never actually covered the evidence.
  local plab_raw="${out}/preserved_labs.raw"
  : > "$plab_raw"
  for d in "${HOME_REAL}"/${PRESERVED_SWEEP_GLOB}; do
    [ -e "$d" ] || continue
    [ "$d" != "$LAB" ] || continue
    hash_tree_into "$d" "$plab_raw" "$cap_err" \
      || die "could not hash the preserved artefact ${d}; see ${cap_err}"
  done
  LC_ALL=C sort "$plab_raw" > "${out}/preserved_labs.sha256"
  rm -f "$plab_raw"

  # Built through a raw file rather than `{ ... } | sort`, because a pipeline puts
  # the group in a SUBSHELL: a die() in there would exit only the subshell.
  # Written this way, the status is checked in the current shell and cannot be
  # lost.
  local plab_meta_raw="${out}/preserved_labs.meta.raw"
  : > "$plab_meta_raw"
  for d in "${HOME_REAL}"/${PRESERVED_SWEEP_GLOB}; do
    [ -e "$d" ] || continue
    [ "$d" != "$LAB" ] || continue
    find "$d" -xdev -printf '%y %m %U %G %s %T@ %C@ %i %n %p\n' \
         >> "$plab_meta_raw" 2>> "$cap_err" \
      || die "could not read metadata for the preserved artefact ${d}; see ${cap_err}"
  done
  LC_ALL=C sort "$plab_meta_raw" > "${out}/preserved_labs.meta"
  rm -f "$plab_meta_raw"

  # --- THE REGRESSION SOURCE, WITNESSED BY NAME, IN ITS OWN PROOF SET ---
  #
  # The authenticity key's CONTENTS are never read here. Only its sha256 is
  # taken, and a sha256 is a one-way digest from which no key can be recovered.
  {
    printf 'regression_source                %s\n' "$REGRESSION_SOURCE"
    printf 'regression_source_mode           %s\n' "$REGRESSION_SOURCE_MODE"
    printf 'seed_journal_sha256              %s\n' "$(sha_of "$SEED_JOURNAL")"
    printf 'seed_journal_bytes               %s\n' "$(bytes_of "$SEED_JOURNAL")"
    printf 'seed_journal_lines               %s\n' "$(wc -l < "$SEED_JOURNAL")"
    printf 'seed_journal_events              %s\n' "$(grep -c '[^[:space:]]' -- "$SEED_JOURNAL" || true)"
    printf 'seed_head_sha256                 %s\n' "$(sha_of "$SEED_JOURNAL_HEAD")"
    printf 'seed_key_sha256                  %s\n' "$(sha_of "$SEED_AUTH_KEY")"
    printf 'seed_marker_sha256               %s\n' "$(sha_of "${REGRESSION_SOURCE}/${SHADOW_MARKER_NAME}")"
    printf 'seed_loop_sha256                 %s\n' "$(sha_of "$SEED_LOOP")"
    printf 'seed_loop_bytes                  %s\n' "$(bytes_of "$SEED_LOOP")"
    printf 'seed_loop_lines                  %s\n' "$(wc -l < "$SEED_LOOP")"
    printf 'seed_pkg_scope_occurrences       %s\n' "$(grep -c -F -- "$EXP_PKG_SCOPE" "$SEED_JOURNAL" || true)"
    printf 'seed_event7_sha_occurrences      %s\n' "$(grep -c -F -- "$EXP_SEED_EVENT7_SHA" "$SEED_JOURNAL" || true)"
    printf 'seed_event6_sha_occurrences      %s\n' "$(grep -c -F -- "$EXP_SEED_EVENT6_SHA" "$SEED_JOURNAL" || true)"
    printf 'seed_routed_signal_occurrences   %s\n' "$(grep -c -F -- "$EXP_ROUTED_SIGNAL_ID" "$SEED_JOURNAL" || true)"
    printf 'seed_standing_target_occurrences %s\n' "$(grep -c -F -- "$EXP_STANDING_TARGET_ID" "$SEED_JOURNAL" || true)"
  } > "${out}/regression_seed.identity"

  # --- THE COMPLETE HISTORICAL WORKSPACE, RE-WITNESSED AT EVERY CAPTURE POINT ---
  #                                                            (NEW IN v13)
  # Two artefacts, both in OBSERVE-ONLY mode:
  #
  #   regression_seed.historical_witness   the frozen expectation, plus the
  #                                        OBSERVED sha256 and byte count of all
  #                                        eight v11 witness files, plus the
  #                                        observed live-seed digest and counts.
  #   regression_seed.historical_manifest  the complete canonical manifest of the
  #                                        current seed: every relative path,
  #                                        type, mode, size and file digest. This
  #                                        is the exact diffable representation,
  #                                        so a change is reported as the one
  #                                        line that moved rather than as a
  #                                        digest mismatch with no detail.
  #
  # NOTHING IS ASSERTED HERE ON PURPOSE. The ASSERTION lives in
  # assert_historical_seed_manifest, which runs before the lab exists, again once
  # the proof directory exists, and again under both locks immediately before the
  # copy. This capture exists so that a seed or witness which moves DURING the run
  # is caught by the ordinary before / during / after comparison and reported as
  # the regression-seed verdict with its reserved exit code, instead of aborting
  # the capture and destroying the evidence of what changed.
  #
  # The authenticity key appears in the manifest only as a sha256 and a byte
  # count, exactly as it already does in regression_seed.identity above. Its
  # CONTENTS are never read into any artefact.
  if ! PYTHONDONTWRITEBYTECODE=1 "$PY3" -B -c "$HIST_SEED_PROOF" \
        "$REGRESSION_SOURCE" \
        "$EXP_HIST_SEED_MANIFEST_SHA" \
        "$EXP_HIST_SEED_MANIFEST_ENTRIES" \
        "$EXP_HIST_SEED_MANIFEST_FILES" \
        "$EXP_HIST_SEED_MANIFEST_DIRS" \
        "$EXP_HIST_SEED_MANIFEST_SYMLINKS" \
        "$EXP_V11_WITNESS_SHA_FILE_SHA" \
        "$EXP_V11_WITNESS_SHA_FILE_BYTES" \
        "$EXP_V11_WITNESS_META_FILE_SHA" \
        "$EXP_V11_WITNESS_META_FILE_BYTES" \
        "${out}/regression_seed.historical_manifest" \
        "${out}/regression_seed.historical_witness" \
        "capture" \
        "${V11_PROOF_DIR}/${V11_WITNESS_SNAPSHOTS[0]}" \
        "${V11_PROOF_DIR}/${V11_WITNESS_SNAPSHOTS[1]}" \
        "${V11_PROOF_DIR}/${V11_WITNESS_SNAPSHOTS[2]}" \
        "${V11_PROOF_DIR}/${V11_WITNESS_SNAPSHOTS[3]}" \
        > /dev/null 2>> "$cap_err"; then
    die "could not capture the historical regression-seed witness; see ${cap_err}"
  fi

  # --- THE CONTINUATION SOURCE, WITNESSED BY NAME, IN ITS OWN PROOF SET ---
  #                                                            (NEW IN v21)
  # Three artefacts, all in OBSERVE-ONLY mode:
  #
  #   continuation_source.identity    the selected identities of the completed
  #                                   v20 shadow -- journal, head, key, marker,
  #                                   controller, and the clearance counts.
  #   continuation_source.manifest    the complete canonical manifest of the
  #                                   current continuation source: every relative
  #                                   path, type, mode, size and file digest, so
  #                                   a change is reported as the one line that
  #                                   moved rather than as a digest mismatch with
  #                                   no detail.
  #   continuation_source.v20_result  the recorded v20 stage exit codes, source
  #                                   proofs and report digests, so a preserved
  #                                   v20 artefact that moves DURING the run is
  #                                   caught by the ordinary before/after
  #                                   comparison.
  #
  # NOTHING IS ASSERTED HERE ON PURPOSE. The ASSERTIONS live in
  # assert_continuation_source and assert_v20_result_authenticated, which run
  # before the lab exists, again once the proof directory exists, and again under
  # both locks immediately before the copy. This capture exists so that a source
  # or artefact which moves DURING the run is caught by the ordinary
  # before / during / after comparison and reported as the continuation-source
  # verdict with its reserved exit code, instead of aborting the capture and
  # destroying the evidence of what changed.
  #
  # The authenticity key appears here only as a sha256 and a byte count. Its
  # CONTENTS are never read into any artefact.
  {
    printf 'continuation_source              %s\n' "$CONTINUATION_SOURCE"
    printf 'continuation_source_mode         %s\n' "$CONTINUATION_SOURCE_MODE"
    printf 'cont_journal_sha256              %s\n' "$(sha_of "$CONT_JOURNAL")"
    printf 'cont_journal_bytes               %s\n' "$(bytes_of "$CONT_JOURNAL")"
    printf 'cont_journal_lines               %s\n' "$(wc -l < "$CONT_JOURNAL")"
    printf 'cont_journal_events              %s\n' "$(grep -c '[^[:space:]]' -- "$CONT_JOURNAL" || true)"
    printf 'cont_head_sha256                 %s\n' "$(sha_of "$CONT_JOURNAL_HEAD")"
    printf 'cont_key_sha256                  %s\n' "$(sha_of "$CONT_AUTH_KEY")"
    printf 'cont_marker_sha256               %s\n' "$(sha_of "${CONTINUATION_SOURCE}/${SHADOW_MARKER_NAME}")"
    printf 'cont_loop_sha256                 %s\n' "$(sha_of "$CONT_LOOP")"
    printf 'cont_loop_bytes                  %s\n' "$(bytes_of "$CONT_LOOP")"
    printf 'cont_loop_lines                  %s\n' "$(wc -l < "$CONT_LOOP")"
    printf 'cont_pkg_scope_occurrences       %s\n' "$(grep -c -F -- "$EXP_PKG_SCOPE" "$CONT_JOURNAL" || true)"
    printf 'cont_event9_sha_occurrences      %s\n' "$(grep -c -F -- "$EXP_CONT_EVENT9_SHA" "$CONT_JOURNAL" || true)"
    printf 'cont_event8_sha_occurrences      %s\n' "$(grep -c -F -- "$EXP_CONT_EVENT8_SHA" "$CONT_JOURNAL" || true)"
    printf 'cont_event7_sha_occurrences      %s\n' "$(grep -c -F -- "$EXP_SEED_EVENT7_SHA" "$CONT_JOURNAL" || true)"
    printf 'cont_routed_signal_occurrences   %s\n' "$(grep -c -F -- "$EXP_ROUTED_SIGNAL_ID" "$CONT_JOURNAL" || true)"
    printf 'cont_standing_target_occurrences %s\n' "$(grep -c -F -- "$EXP_STANDING_TARGET_ID" "$CONT_JOURNAL" || true)"
    printf 'cont_validation_set_occurrences  %s\n' "$(grep -c -F -- "$EXP_CONT_EVENT9_VALIDATION_SET_ID" "$CONT_JOURNAL" || true)"
  } > "${out}/continuation_source.identity"

  if ! PYTHONDONTWRITEBYTECODE=1 "$PY3" -B -c "$HIST_SEED_PROOF" \
        "$CONTINUATION_SOURCE" \
        "$EXP_CONT_MANIFEST_SHA" \
        "$EXP_CONT_MANIFEST_ENTRIES" \
        "$EXP_CONT_MANIFEST_FILES" \
        "$EXP_CONT_MANIFEST_DIRS" \
        "$EXP_CONT_MANIFEST_SYMLINKS" \
        "UNUSED-IN-FROZEN-MODE" \
        "0" \
        "UNUSED-IN-FROZEN-MODE" \
        "0" \
        "${out}/continuation_source.manifest" \
        "-" \
        "frozen-capture" \
        > /dev/null 2>> "$cap_err"; then
    die "could not capture the continuation-source manifest; see ${cap_err}"
  fi

  {
    printf 'v20_proof_dir                    %s\n' "$V20_PROOF_DIR"
    printf 's1_exit                          %s\n' "$(cat -- "${V20_PROOF_DIR}/${V20_STAGE1_ARTEFACT}.exit-code" 2>> "$cap_err")"
    printf 's1_source_proof                  %s\n' "$(cat -- "${V20_PROOF_DIR}/${V20_STAGE1_ARTEFACT}.source-proof" 2>> "$cap_err")"
    printf 's1_stdout_sha256                 %s\n' "$(sha_of "${V20_PROOF_DIR}/${V20_STAGE1_ARTEFACT}.stdout")"
    printf 's2_exit                          %s\n' "$(cat -- "${V20_PROOF_DIR}/${V20_STAGE2_ARTEFACT}.exit-code" 2>> "$cap_err")"
    printf 's2_source_proof                  %s\n' "$(cat -- "${V20_PROOF_DIR}/${V20_STAGE2_ARTEFACT}.source-proof" 2>> "$cap_err")"
    printf 's2_stdout_sha256                 %s\n' "$(sha_of "${V20_PROOF_DIR}/${V20_STAGE2_ARTEFACT}.stdout")"
    printf 's3_exit                          %s\n' "$(cat -- "${V20_PROOF_DIR}/${V20_STAGE3_ARTEFACT}.exit-code" 2>> "$cap_err")"
    printf 's3_source_proof                  %s\n' "$(cat -- "${V20_PROOF_DIR}/${V20_STAGE3_ARTEFACT}.source-proof" 2>> "$cap_err")"
    printf 's3_stdout_sha256                 %s\n' "$(sha_of "${V20_PROOF_DIR}/${V20_STAGE3_ARTEFACT}.stdout")"
    printf 's4_exit                          %s\n' "$(cat -- "${V20_PROOF_DIR}/${V20_STAGE4_ARTEFACT}.exit-code" 2>> "$cap_err")"
    printf 's4_source_proof                  %s\n' "$(cat -- "${V20_PROOF_DIR}/${V20_STAGE4_ARTEFACT}.source-proof" 2>> "$cap_err")"
    printf 's4_stdout_sha256                 %s\n' "$(sha_of "${V20_PROOF_DIR}/${V20_STAGE4_ARTEFACT}.stdout")"
    printf 's4_stdout_bytes                  %s\n' "$(bytes_of "${V20_PROOF_DIR}/${V20_STAGE4_ARTEFACT}.stdout")"
    printf 's4_stderr_sha256                 %s\n' "$(sha_of "${V20_PROOF_DIR}/${V20_STAGE4_ARTEFACT}.stderr")"
    printf 's4_stderr_bytes                  %s\n' "$(bytes_of "${V20_PROOF_DIR}/${V20_STAGE4_ARTEFACT}.stderr")"
    printf 'refresh_after_sha256             %s\n' "$(sha_of "${V20_PROOF_DIR}/controller-refresh.after")"
    printf 'refresh_composite_sha256         %s\n' "$(sha_of "${V20_PROOF_DIR}/controller-refresh.composite")"
  } > "${out}/continuation_source.v20_result"

  # --- host model-auth / config witness: HASHES AND METADATA ONLY ---
  # Contents are never read into the proof. A sha256 is a one-way digest and no
  # credential value can be recovered from it.
  #
  # This witness keeps its OWN error file rather than sharing cap_err, because it
  # is deliberately a separate, lesser signal: a concurrently running host Claude
  # Code or Codex session legitimately rewrites these files, and that must not be
  # confused with a containment failure. But a witness that could not be taken is
  # not the same as a witness that came back unchanged, so a non-empty error file
  # becomes its own CAPTURE-FAILED verdict rather than silently reading as
  # UNCHANGED.
  local cred_err="${out}/credentials.errors"
  : > "$cred_err"
  {
    local f h
    for f in "$HOST_CLAUDE_JSON" \
             "${HOST_CLAUDE}/.credentials.json" \
             "${HOST_CLAUDE}/settings.json" \
             "${HOST_CLAUDE}/settings.local.json" \
             "${HOST_CODEX}/auth.json" \
             "${HOST_CODEX}/config.toml" \
             "/home/ness/.netrc"; do
      if [ ! -e "$f" ]; then
        printf '%s  %s\n' "ABSENT" "$f"
      elif h="$(sha256sum -- "$f" 2>> "$cred_err")"; then
        printf '%s  %s\n' "${h%% *}" "$f"
      else
        printf '%s  %s\n' "UNREADABLE" "$f"
        printf 'sha256sum failed for %s\n' "$f" >> "$cred_err"
      fi
    done
    # errexit is suspended around this pipeline ON PURPOSE. The whole point of
    # the credential witness is that a capture failure becomes a CAPTURE-FAILED
    # VERDICT, not a dead launcher. Under `set -e` with pipefail, an unreadable
    # file anywhere under .ssh or .config makes this pipeline non-zero and the
    # shell exits IMMEDIATELY -- before the PIPESTATUS check below, before
    # cred_err is written, and before section 12 ever evaluates the verdict.
    local dd st
    for dd in "/home/ness/.ssh" "/home/ness/.config"; do
      if [ -d "$dd" ]; then
        set +e
        find "$dd" -maxdepth 1 -type f -print0 2>> "$cred_err" \
          | LC_ALL=C sort -z 2>> "$cred_err" \
          | xargs -0 -r sha256sum -- 2>> "$cred_err"
        st=("${PIPESTATUS[@]}")
        set -e
        if [ "${st[0]}" != "0" ] || [ "${st[1]}" != "0" ] || [ "${st[2]}" != "0" ]; then
          printf 'traversal or hashing failed under %s (statuses: %s)\n' \
                 "$dd" "${st[*]}" >> "$cred_err"
        fi
      fi
    done
  } > "${out}/credentials.sha256"

  # Built through a raw file with every status checked, NOT through
  # `{ ... } | sort`: `find ... || true` erases every non-zero find status, and a
  # truncated metadata stream that is truncated identically before and after
  # compares EQUAL and reads as UNCHANGED while nothing was actually witnessed.
  local cred_meta_raw="${out}/credentials.meta.raw"
  : > "$cred_meta_raw"
  local p prc
  for p in "$HOST_CLAUDE_JSON" "${HOST_CLAUDE}/.credentials.json" \
           "${HOST_CODEX}/auth.json" "${HOST_CODEX}/config.toml" \
           "/home/ness/.netrc" "/home/ness/.ssh" "/home/ness/.config" \
           "$HOST_CODEX" "$HOST_CLAUDE"; do
    if [ -e "$p" ]; then
      prc=0
      find "$p" -maxdepth 1 -printf '%y %m %U %G %s %T@ %C@ %i %n %p\n' \
           >> "$cred_meta_raw" 2>> "$cred_err" || prc=$?
      if [ "$prc" -ne 0 ]; then
        printf 'metadata read failed for %s (status %s)\n' "$p" "$prc" >> "$cred_err"
      fi
    else
      printf 'ABSENT %s\n' "$p" >> "$cred_meta_raw"
    fi
  done
  if ! LC_ALL=C sort "$cred_meta_raw" > "${out}/credentials.meta" 2>> "$cred_err"; then
    printf 'sort of the credential metadata witness failed\n' >> "$cred_err"
  fi
  rm -f "$cred_meta_raw"

  # Finally: this capture is only a proof if it was complete.
  if [ -s "$cap_err" ]; then
    die "the protected-original proof capture did not complete cleanly.
      An incomplete capture must never be compared as if it were a proof.
      See ${cap_err}"
  fi
}

# hash_tree_into <dir> <out_file> <err_file>
# Appends "sha256  path" for every regular file under <dir>. Returns 0 only when
# EVERY stage of the pipeline succeeded.
#
# The naive form -- find | sort | xargs sha256sum -- reports only the LAST
# stage's status, so a find that cannot traverse a subtree yields a silently
# incomplete listing with an exit status of zero. An incomplete hash listing that
# is incomplete in the same way before and after would compare EQUAL and be
# reported as proof.
hash_tree_into() {
  local dir="$1" out_file="$2" err_file="$3"
  find "$dir" -xdev -type f -print0 2>> "$err_file" \
    | LC_ALL=C sort -z \
    | xargs -0 -r sha256sum -- >> "$out_file" 2>> "$err_file"
  local st=("${PIPESTATUS[@]}")
  [ "${st[0]}" = "0" ] && [ "${st[1]}" = "0" ] && [ "${st[2]}" = "0" ]
}

# scan_lab_for_credentials <report_path>
# Returns 0 when NO KNOWN CREDENTIAL MARKER was found in the persistent lab, 1
# when one was, and 2 when the scan ITSELF could not be completed. Only PATHS are
# ever written to the report. No matched content is read into the report,
# printed, or kept anywhere.
#
# 0 does NOT mean the lab holds no model login material, and this comment must
# not say that it does -- see the verdict name NO-KNOWN-MARKERS.
#
# The 2 case exists because a suppressed scan failure is indistinguishable from a
# clean result: an unreadable file, a traversal error or a killed grep would
# otherwise leave an empty report and be reported as CLEAN. Every caller treats
# anything other than 0 as fail-closed.
scan_lab_for_credentials() {
  local report="$1"
  local errfile="${report}.errors"
  local rc=0

  : > "$report"  || return 2
  : > "$errfile" || return 2

  # 1. login files carried in by name.
  find "$LAB" \( -name '.credentials.json' -o -name 'auth.json' -o -name '.claude.json' \
                 -o -name 'id_rsa*' -o -name 'id_ed25519*' -o -name '.netrc' \) \
       -print >> "$report" 2>> "$errfile" || rc=$?
  if [ "$rc" -ne 0 ]; then
    return 2
  fi

  # 2. credential-shaped CONTENT written into any lab file, which a filename
  #    check cannot see. Each marker's first character is written as a
  #    one-character bracket expression because the lab contains a copy of this
  #    launcher, so a plain literal would match its own source text and report
  #    every run as carrying credentials.
  #
  #    -a, NOT -I. -I makes grep treat any file containing a NUL byte as
  #    non-matching, so a credential written into a file that also holds binary
  #    data would be invisible -- and the lab now necessarily contains compiled
  #    python bytecode, which is exactly such a file.
  #
  #    THIS IS A SHAPE-BASED SCAN AND A PASSING RESULT IS NOT "CLEAN". It cannot
  #    see a token in an unrecognised shape, and it cannot see into compressed or
  #    encoded content. The verdict is named for what it actually establishes.
  grep -ral -E 's[k]-[A-Za-z0-9_-]{16,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|"[a]ccess_token"|"[r]efresh_token"|"[i]d_token"|"[a]ccessToken"|"[r]efreshToken"|"[i]dToken"|[e]yJ[A-Za-z0-9_-]{16,}\.[A-Za-z0-9_-]{16,}' \
       -- "$LAB" >> "$report" 2>> "$errfile" || rc=$?
  # grep: 0 matched, 1 matched nothing, 2 or more an operational failure.
  if [ "$rc" -gt 1 ]; then
    return 2
  fi

  # Anything on stderr means the sweep did not cover everything it was asked to.
  if [ -s "$errfile" ]; then
    return 2
  fi

  if [ -s "$report" ]; then
    return 1
  fi
  return 0
}

# compare_proof_set <before_dir> <after_dir> <label> <file...>
compare_proof_set() {
  local a="$1" b="$2" label="$3"; shift 3
  local rc=0 f dst
  for f in "$@"; do
    dst="${PROOF}/DIFF.${label}.${f}.txt"
    if diff -u "${a}/${f}" "${b}/${f}" > "$dst" 2>&1; then
      rm -f "$dst"
    else
      rc=1
      say "[DIFFERS] ${f}  ->  ${dst}"
    fi
  done
  return "$rc"
}

# ==========================================================================
# SECTION 3 — FAIL-CLOSED PRECONDITIONS
# ==========================================================================

step "PRECONDITIONS"

[ "$(id -u)" -ne 0 ] || die "refusing to run as root; run as the user ness"
[ "$(id -un)" = "ness" ] || die "must run as the user ness (found: $(id -un))"

for c in sha256sum stat find sort xargs diff rsync flock git awk grep sed wc mkdir; do
  need_cmd "$c"
done

[ -x "$BWRAP" ] || die "Bubblewrap is unavailable at ${BWRAP}; isolation cannot be established"
note "Bubblewrap present: $("$BWRAP" --version)"

[ -x "$PY3" ] || die "python3 is unavailable at ${PY3}"
[ -d "$NODE_BIN" ] || die "node bin directory missing: ${NODE_BIN}"
[ -x "${NODE_BIN}/codex" ] || die "codex client not found at ${NODE_BIN}/codex"
[ -x "${NODE_BIN}/claude" ] || die "claude client not found at ${NODE_BIN}/claude"

[ -d "$WS" ]    || die "protected workspace missing: ${WS}"
[ -d "$CTRL" ]  || die "controller missing: ${CTRL}"
[ -d "$NHGOV" ] || die "N.H checkout missing: ${NHGOV}"
[ -d "$STATE" ] || die "interview state missing: ${STATE}"
[ -d "$AUTH_DIR" ] || die "N.H 01_AUTHORITATIVE missing: ${AUTH_DIR}"
[ -d "$HOST_CODEX" ]  || die "host .codex missing; the copy-on-write credential overlay cannot be built"
[ -d "$HOST_CLAUDE" ] || die "host .claude missing; the copy-on-write credential overlay cannot be built"
[ -f "$HOST_CLAUDE_JSON" ] || die "host .claude.json missing; the client cannot start inside the namespace"

# Every earlier rehearsal is preserved evidence and this run must not collide
# with any of them.
for _plab in "$PRESERVED_LAB_V1" "$PRESERVED_LAB_REPAIR9" \
             "$PRESERVED_LAB_REPAIR10" "$PRESERVED_LAB_REPAIR14" \
             "$PRESERVED_LAB_REPAIR15" "$PRESERVED_LAB_REPAIR16" \
             "$PRESERVED_LAB_REPAIR17" \
             "$PRESERVED_LAB_REPAIR17_CONTINUATION_V10" \
             "$PRESERVED_LAB_REPAIR18_CONTINUATION_V11" \
             "$PRESERVED_LAB_REPAIR19B_V13" \
             "$PRESERVED_LAB_REPAIR20B_V14" \
             "$PRESERVED_LAB_REPAIR21_V15" \
             "$PRESERVED_LAB_REPAIR25_V18" \
             "$PRESERVED_LAB_REPAIR26_V19" \
             "$PRESERVED_LAB_REPAIR27A_V20" \
             "$PRESERVED_LAB_REPAIR27B_V21"; do
  if [ "$LAB" = "$_plab" ]; then
    die "the configured lab path is a preserved rehearsal lab:
        ${LAB}
      That lab is evidence. Refusing to reuse it."
  fi
done
unset _plab
note "new lab path is distinct from every preserved rehearsal lab"

# The completed v13 lab is historical evidence and must still be there. It is
# never written to, never normalised, never repaired and never reused: this is a
# presence-and-shape assertion only, and the before/during/after preserved-lab
# sweep is what proves it did not move.
if [ ! -d "$PRESERVED_LAB_REPAIR19B_V13" ] || [ -L "$PRESERVED_LAB_REPAIR19B_V13" ]; then
  die "the completed v13 rehearsal lab is missing or is not an ordinary directory:
        ${PRESERVED_LAB_REPAIR19B_V13}
      It holds the exact provider-backed failure Repair 20B corrects. Refusing to
      rehearse without the evidence it succeeds."
fi
note "the completed v13 lab is present and is not this run's lab"

if [ ! -d "$PRESERVED_LAB_REPAIR20B_V14" ] || [ -L "$PRESERVED_LAB_REPAIR20B_V14" ]; then
  die "the completed v14 rehearsal lab is missing or is not an ordinary directory:
        ${PRESERVED_LAB_REPAIR20B_V14}
      It holds the exact provider-backed failure Repair 21 corrects. Refusing to
      rehearse without the evidence it succeeds."
fi
note "the completed v14 lab is present and is not this run's lab"

# The completed v15 lab is PRESERVED REHEARSAL EVIDENCE. It is NOT this run's
# direct predecessor evidence: this run's continuation source is the completed
# v21 shadow, and its Doors-1-to-3 ancestor evidence is the completed v20 lab.
# It is never written to, never normalised, never repaired, never reused and never
# deleted: this is a presence-and-shape assertion only, and the
# before/during/after preserved-artefact sweep is what proves it did not move.
if [ ! -d "$PRESERVED_LAB_REPAIR21_V15" ] || [ -L "$PRESERVED_LAB_REPAIR21_V15" ]; then
  die "the completed v15 rehearsal lab is missing or is not an ordinary directory:
        ${PRESERVED_LAB_REPAIR21_V15}
      It holds the exact provider-backed Stage-1 refusal Repair 22 corrects.
      Refusing to rehearse without the evidence it succeeds."
fi
note "the completed v15 lab is present and is not this run's lab"

# The completed v18 lab is PRESERVED REHEARSAL EVIDENCE: v18 RAN
# and its Stage-1 MATERIAL_UNKNOWN_UNRESOLVED refusal is exactly what accepted
# Repair 26 corrects. It is never written to, never normalised, never repaired,
# never reused, never used as this run's seed and never deleted: this is a
# presence-and-shape assertion only, and the before/during/after
# preserved-artefact sweep is what proves it did not move.
if [ ! -d "$PRESERVED_LAB_REPAIR25_V18" ] || [ -L "$PRESERVED_LAB_REPAIR25_V18" ]; then
  die "the completed v18 rehearsal lab is missing or is not an ordinary directory:
        ${PRESERVED_LAB_REPAIR25_V18}
      It holds the exact provider-backed Stage-1 refusal Repair 26 corrects.
      Refusing to rehearse without the evidence it succeeds."
fi
if [ "$PRESERVED_LAB_REPAIR25_V18" = "$LAB" ]; then
  die "the configured lab path IS the completed v18 lab:
        ${LAB}
      That lab is evidence. Refusing to reuse it."
fi
if [ "$PRESERVED_LAB_REPAIR25_V18" = "$REGRESSION_SOURCE" ] \
   || [ "${PRESERVED_LAB_REPAIR25_V18}/shadow/NH_CLAUDE_CODEX_DESIGN_LOOP" = "$REGRESSION_SOURCE" ]; then
  die "the completed v18 lab is being used as this run's regression seed:
        ${REGRESSION_SOURCE}
      v24 continues from the completed v21 shadow, and its lineage seed is the
      preserved Repair-17 CONTINUATION v10 shadow. Neither of those is the v18
      lab. Refusing to continue from a state this launcher was not frozen
      against."
fi
note "the completed v18 lab is present, is not this run's lab and is not its seed"

# The completed v19 lab is PRESERVED REHEARSAL EVIDENCE: v19 RAN
# and its Stage-4 PREPARATION_FAILED refusal is exactly what accepted Repair 27A
# (through Repair 27) corrects. It is never written to, never normalised, never
# repaired, never reused, never used as this run's seed and never deleted: this
# is a presence-and-shape assertion only, and the before/during/after
# preserved-artefact sweep is what proves it did not move.
if [ ! -d "$PRESERVED_LAB_REPAIR26_V19" ] || [ -L "$PRESERVED_LAB_REPAIR26_V19" ]; then
  die "the completed v19 rehearsal lab is missing or is not an ordinary directory:
        ${PRESERVED_LAB_REPAIR26_V19}
      It holds the exact provider-backed Stage-4 refusal Repair 27A corrects.
      Refusing to rehearse without the evidence it succeeds."
fi
if [ "$PRESERVED_LAB_REPAIR26_V19" = "$LAB" ]; then
  die "the configured lab path IS the completed v19 lab:
        ${LAB}
      That lab is evidence. Refusing to reuse it."
fi
if [ "$PRESERVED_LAB_REPAIR26_V19" = "$REGRESSION_SOURCE" ] \
   || [ "${PRESERVED_LAB_REPAIR26_V19}/shadow/NH_CLAUDE_CODEX_DESIGN_LOOP" = "$REGRESSION_SOURCE" ]; then
  die "the completed v19 lab is being used as this run's regression seed:
        ${REGRESSION_SOURCE}
      v24 continues from the completed v21 shadow, and its lineage seed is the
      preserved Repair-17 CONTINUATION v10 shadow. Neither of those is the v19
      lab. Refusing to continue from a state this launcher was not frozen
      against."
fi
note "the completed v19 lab is present, is not this run's lab and is not its seed"

# The completed v20 lab is PRESERVED ANCESTOR EVIDENCE. It is NOT this file's
# direct predecessor (v23 is) and it is NOT this run's continuation source (the
# completed v21 shadow is). v20 RAN: its Stages 1, 2 and 3 passed -- the
# Doors-1-to-3 clearance this continuation still rests on -- and its Stage 4
# crashed inside the preparation report, which is what accepted Repair 27B
# corrected.
#
# IT GRANTS NO WRITE PERMISSION. It is never written to, never normalised, never
# repaired, never reused as a lab and never deleted. It IS read, for ONE purpose
# only: to authenticate the recorded v20 Doors result. IT IS NEVER COPIED and is
# never the source side of any rsync. The before/during/after preserved-artefact
# sweep is what proves it did not move.
if [ ! -d "$PRESERVED_LAB_REPAIR27A_V20" ] || [ -L "$PRESERVED_LAB_REPAIR27A_V20" ]; then
  die "the completed v20 rehearsal lab is missing or is not an ordinary directory:
        ${PRESERVED_LAB_REPAIR27A_V20}
      It holds the Doors-1-to-3 result this continuation still rests on.
      Refusing to continue without the ancestor evidence it depends on."
fi
if [ "$PRESERVED_LAB_REPAIR27A_V20" = "$LAB" ]; then
  die "the configured lab path IS the completed v20 lab:
        ${LAB}
      That lab is preserved ancestor Doors evidence. Refusing to write
      into it."
fi
if [ ! -d "$V20_PROOF_DIR" ] || [ -L "$V20_PROOF_DIR" ]; then
  die "the completed v20 proof directory is missing or is not an ordinary
      directory:
        ${V20_PROOF_DIR}
      Without it the v20 result cannot be authenticated and a Stage-4-only
      continuation is not justified. Refusing to continue."
fi
# The completed v21 lab is THE LAST COMPLETED LIVE RUN'S EVIDENCE and, uniquely,
# THIS RUN'S CONTINUATION SOURCE. v21 RAN: its single Stage 4 reached the real
# correction loop, round 3 began, and it stopped fail-closed at
# CLAUDE_SPECIFICATION_STOP because Claude's correction workspace did not carry
# the frozen non-candidate baseline source the GPT specification named. That is
# exactly what accepted Repair 28 corrects.
#
# BOTH FACTS ARE TRUE AT ONCE AND THE SECOND GRANTS NO WRITE PERMISSION. It is
# never written to, never normalised, never chmod-ed, never renamed, never
# repaired, never reused as a lab and never deleted. It IS read: to authenticate
# the recorded v21 result, to authenticate the state being continued, and as the
# SOURCE side of one rsync. The before/during/after preserved-artefact sweep is
# what proves it did not move.
if [ ! -d "$PRESERVED_LAB_REPAIR27B_V21" ] || [ -L "$PRESERVED_LAB_REPAIR27B_V21" ]; then
  die "the completed v21 rehearsal lab is missing or is not an ordinary directory:
        ${PRESERVED_LAB_REPAIR27B_V21}
      It holds the exact Stage-4 CLAUDE_SPECIFICATION_STOP Repair 28 corrects AND
      the Doors-1-to-3 clearance this continuation carries forward. Refusing to
      continue without the run it continues."
fi
if [ "$PRESERVED_LAB_REPAIR27B_V21" = "$LAB" ]; then
  die "the configured lab path IS the completed v21 lab:
        ${LAB}
      That lab is evidence AND this run's continuation source. Refusing to write
      into it."
fi
if [ ! -d "$V21_PROOF_DIR" ] || [ -L "$V21_PROOF_DIR" ]; then
  die "the completed v21 proof directory is missing or is not an ordinary
      directory:
        ${V21_PROOF_DIR}
      Without it the v21 result cannot be authenticated and a Stage-4-only
      continuation is not justified. Refusing to continue."
fi
if [ "$PRESERVED_LAB_REPAIR27A_V20" = "$PRESERVED_LAB_REPAIR27B_V21" ]; then
  die "the preserved v20 and v21 labs resolve to the same path. They are two
      different runs and this launcher never conflates them. Refusing to
      continue."
fi
note "the completed v21 lab is present, is not this run's lab, and is its READ-ONLY continuation source"

if [ "$CONTINUATION_SOURCE" = "$REGRESSION_SOURCE" ]; then
  die "the continuation source and the historical lineage seed resolve to the
      same path:
        ${CONTINUATION_SOURCE}
      They are two different facts and this launcher never conflates them.
      Refusing to continue."
fi
note "the completed v20 lab is present, is not this run's lab, and is preserved ANCESTOR Doors-1-to-3 evidence"

# The lab must not already exist. Never silently reuse. Never delete.
if [ -e "$LAB" ]; then
  die "the lab path already exists:
        ${LAB}
      This launcher never reuses and never deletes an earlier lab. Review it,
      move it aside or remove it yourself, then run this launcher again."
fi
note "lab path is free: ${LAB}"

# ==========================================================================
# SECTION 4 — FROZEN SOURCE IDENTITY GATE
# ==========================================================================

# --------------------------------------------------------------------------
# SECTION 4a — THE THREE EXPLAINED WORKSPACE-ROOT DIRECTORIES
# --------------------------------------------------------------------------
#
# Six properties are asserted for each, and every one of them fails the run
# CLOSED: it exists; it is NOT a symlink (checked before any -d test, because -d
# follows a link); it IS a real directory; it contains exactly zero entries;
# nothing exists under it at ANY depth; and, for the workspace root as a whole,
# it does not resolve as a Git repository.
#
# WHY THIS IS A GATE AND NOT A TOLERANCE. These three paths lie outside both Git
# checkouts, so neither worktree status can see them. Without this gate they
# would enter the proof only through workspace.meta -- frozen as the normal
# baseline and copied into the shadow with nothing having asserted what they are.
#
# WHAT THIS FUNCTION NEVER DOES. It never creates, deletes, normalises, chmods or
# writes anything, inside those directories or anywhere else. It only tests.
assert_workspace_special_dirs() {
  local d listing st count
  for d in "${WS_SPECIAL_DIRS[@]}"; do
    if [ ! -e "$d" ] && [ ! -L "$d" ]; then
      die "an explained workspace-root directory is MISSING:
        ${d}
      v12 is frozen to this exact set of three empty directories. Nothing is
      created to repair it: re-freeze a launcher against the real current state
      deliberately, exactly as every earlier rebase did."
    fi

    if [ -L "$d" ]; then
      die "an explained workspace-root directory is a SYMLINK:
        ${d} -> $(readlink -- "$d" 2>/dev/null || printf '<unreadable>')
      A symlink here could redirect the shadow copy, so this fails closed."
    fi

    if [ ! -d "$d" ]; then
      die "an explained workspace-root path is not a directory:
        ${d}
        found: $(stat -c '%F' -- "$d" 2>/dev/null || printf '<unreadable>')
      The classification covers empty DIRECTORIES only. Refusing to rehearse."
    fi

    # Empty at every depth. No pipeline is used, so pipefail cannot reach this
    # and a traversal failure cannot be mistaken for an empty directory.
    st=0
    listing="$(find "$d" -mindepth 1 -printf '%y %p\n' 2>&1)" || st=$?
    if [ "$st" -ne 0 ]; then
      die "an explained workspace-root directory could not be traversed:
        ${d}
      A directory that cannot be read is not a directory proved empty."
    fi
    if [ -z "$listing" ]; then
      count=0
    else
      count="$(printf '%s\n' "$listing" | grep -c '' || true)"
    fi
    if [ "$count" != "$WS_SPECIAL_DIR_EXPECTED_ENTRIES" ]; then
      die "an explained workspace-root directory is NO LONGER EMPTY:
        ${d}
        entries found:       ${count}
        frozen expectation:  ${WS_SPECIAL_DIR_EXPECTED_ENTRIES}
${listing}
      These three directories are classified as EMPTY Codex/tool workspace
      artefacts and nothing more. Nothing is deleted and nothing is normalised
      here. Review what appeared, then re-freeze deliberately if it is
      legitimate."
    fi

    note "explained workspace-root directory verified empty and unchanged in shape: ${d}"
  done

  # The workspace ROOT must NOT resolve as a Git repository. This is what proves
  # the root .git is not a functional repository -- and it is stricter than
  # inspecting that directory's contents, because it also fails if some ENCLOSING
  # directory ever became a repository that could capture the workspace.
  local root_git_dir grc=0
  root_git_dir="$(git_ro "$WS" rev-parse --git-dir 2>/dev/null)" || grc=$?
  if [ "$grc" -eq 0 ]; then
    die "the protected workspace ROOT resolves as a Git repository:
        ${WS}
        git-dir: ${root_git_dir}
      It must not. The root .git is frozen as an EMPTY, non-functional Codex
      workspace artefact, and the only repositories this launcher reads are the
      controller repository and the NH-GOVERNANCE repository."
  fi
  note "the workspace root does not resolve as a Git repository; root .git is non-functional"

  expect "controller git-dir"    "$(git_ro "$CTRL" rev-parse --absolute-git-dir)"  "${CTRL}/.git"
  expect "NH-GOVERNANCE git-dir" "$(git_ro "$NHGOV" rev-parse --absolute-git-dir)" "${NHGOV}/.git"
}

# --------------------------------------------------------------------------
# SECTION 4b — THE HISTORICAL LINEAGE SEED, AND THE SIGNAL IT CARRIES
#              (PRESERVED EVIDENCE IN v21; NEVER COPIED)
# --------------------------------------------------------------------------
#
# IN v21 THIS SOURCE IS NOT COPIED. It is the preserved v10 shadow that pre-dates
# the false v11 question, and it is the lineage root of the completed v20 shadow
# this run actually continues from. Its complete authentication is carried
# forward from v20 unchanged, because a continuation whose lineage root has
# silently moved is not the continuation it claims to be. The continuation source
# itself is gated separately in section 4b4.
#
# The lineage state is worth exactly as much as the proof that it IS that state.
# This gate establishes it in four escalating steps, and every one of them fails
# the run CLOSED, long before the isolation self-test and therefore long before
# any possible provider or model call:
#
#   1. SHAPE. The preserved v10 lab and the regression source inside it exist,
#      are real directories, and are not symlinks. A symlink here could redirect
#      the rsync SOURCE and silently seed the run from somewhere else entirely.
#
#   2. IDENTITY. The seed journal, journal head and authenticity key match the
#      exact sha256 / byte / line / event counts frozen above; the seed still
#      carries the v10 shadow marker with its exact content; AND the seed
#      controller is the EXACT Repair-17 file.
#
#   3. THE SIGNAL. The journal holds exactly seven events; event 7 is the LAST
#      one; and its type, route, signal source, routed signal id, standing target
#      id, issue key, finding key, package scope, own digest and previous digest
#      are exactly the frozen ones.
#
#   4. AUTHENTICITY. The whole seven-event chain and the journal head
#      AUTHENTICATE under the CONTROLLER'S OWN semantics -- its event digest, its
#      HMAC over its own canonical authentication material, its sequence and
#      previous-digest chaining, and its head authentication -- not merely "the
#      JSON line is present". Step 3 without step 4 would accept a forged or
#      hand-edited event that happened to carry the right strings.
#
# WHAT THIS GATE DELIBERATELY DOES NOT DO.
#   It does not classify the signal. It does not decide whether it is settled,
#   mechanical, dependent or genuinely open. It does not convert it into a
#   question, does not answer it, and does not read its title or its evidence
#   text at any point. Only identifiers and digests are compared.
#
#   AND IT DOES NOT COMPARE THE SEED TO THE CURRENT REAL WORKSPACE. v11 had a
#   further gate that did exactly that. It is gone. The seed is proved to be the
#   authenticated HISTORICAL snapshot, full stop; today's real workspace is
#   protected separately in section 4e and is never required to equal it.
#
# WHY THE CONTROLLER'S OWN CODE, AND NOT A REIMPLEMENTATION HERE.
#   A second implementation of the authentication rule is exactly the "parallel
#   gate" mistake this project refuses everywhere else: it would drift, and a
#   drifted verifier that says PASS is worse than no verifier. nh_loop.py is
#   imported READ-ONLY as a module and its own functions are called. It is never
#   executed as a program here, no provider is contacted, and nothing is written.
#
# WHY -B AND PYTHONDONTWRITEBYTECODE ARE LOAD-BEARING.
#   An ordinary import would rewrite controller/__pycache__/nh_loop.cpython-*.pyc
#   inside the PROTECTED workspace. That is a real write to the protected
#   original and it would fail the controller-bytecode gate on the second,
#   under-lock assertion. Both are set, and the bytecode is proved UNCHANGED
#   afterwards rather than the flags being trusted.
readonly SEED_AUTH_CHECKER='
import hmac, importlib.util, json, sys

loop_path = sys.argv[1]
state_dir = sys.argv[2]
expected_count = int(sys.argv[3])
expected_fields = []
for item in sys.argv[4:]:
    name, _, value = item.partition("=")
    expected_fields.append((name, value))

spec = importlib.util.spec_from_file_location("nh_loop_readonly_seed_check", loop_path)
if spec is None or spec.loader is None:
    sys.exit(2)
module = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(module)
except BaseException:
    sys.exit(2)

try:
    with open(state_dir + "/nh_interview_authenticity.key", "rb") as handle:
        key = handle.read()
    with open(state_dir + "/nh_interview_journal.jsonl", encoding="utf-8") as handle:
        raw_lines = handle.read().splitlines()
    with open(state_dir + "/nh_interview_journal.head", encoding="utf-8") as handle:
        head = json.load(handle)
except (OSError, ValueError):
    sys.exit(3)

if not key:
    sys.exit(3)

events = []
for line in raw_lines:
    if not line.strip():
        continue
    try:
        events.append(json.loads(line))
    except ValueError:
        sys.exit(4)

if len(events) != expected_count:
    sys.stdout.write("event count is %d, expected %d\n" % (len(events), expected_count))
    sys.exit(5)

previous = None
for index, event in enumerate(events, 1):
    if event.get("event_seq") != index:
        sys.stdout.write("event %d carries event_seq %r\n" % (index, event.get("event_seq")))
        sys.exit(6)
    if event.get("prev_event_sha256") != previous:
        sys.stdout.write("event %d does not chain to its predecessor\n" % index)
        sys.exit(7)
    if event.get("event_sha256") != module.interview_event_digest(event):
        sys.stdout.write("event %d digest does not match its own body\n" % index)
        sys.exit(8)
    if not module.interview_event_auth_ok(key, event):
        sys.stdout.write("event %d is not authenticated by this controller\n" % index)
        sys.exit(9)
    previous = event.get("event_sha256")

last = events[-1]
for name, value in expected_fields:
    if last.get(name) != value:
        sys.stdout.write("last event %s is %r, expected %r\n" % (name, last.get(name), value))
        sys.exit(10)

if not hmac.compare_digest(
    str(head.get("head_auth_sha256")),
    str(module.interview_journal_head_auth(key, head)),
):
    sys.stdout.write("the journal head is not authenticated by this controller\n")
    sys.exit(11)
if head.get("committed_event_seq") != len(events) or head.get("intent_event_seq") != len(events):
    sys.stdout.write("the journal head does not sit at event %d\n" % len(events))
    sys.exit(12)
if head.get("committed_event_sha256") != last.get("event_sha256") or head.get("intent_event_sha256") != last.get("event_sha256"):
    sys.stdout.write("the journal head does not name the last event\n")
    sys.exit(13)

sys.stdout.write("REGRESSION_SOURCE_AUTHENTICATED\n")
'

# --------------------------------------------------------------------------
# THE HISTORICAL SEED CANONICALIZER AND WHOLE-WORKSPACE PROOF   (NEW IN v13)
# --------------------------------------------------------------------------
#
# ONE deterministic, READ-ONLY program with TWO input sides that must produce
# byte-identical canonical manifests:
#
#   EXPECTED  built ONLY from the frozen v11 witness files. Never from the
#             current seed. This is what makes the expectation historical.
#   LIVE      built ONLY from a read-only walk of the current regression source.
#
# It writes NOTHING except the two proof artefacts it is explicitly given paths
# for, and those live inside this run's own lab. It never writes to the v11 lab,
# to the v10 seed, or to the protected workspace.
#
# EVERY AMBIGUITY FAILS CLOSED. A symlink, a special file, a duplicate relative
# path, a malformed path, a path escaping the seed root, a regular file with no
# digest record, or a digest record with no regular-file metadata all REFUSE.
# Nothing is guessed, nothing is silently dropped, and nothing is deduplicated to
# make an ambiguity go away.
#
# WHAT IS DELIBERATELY NOT IDENTITY: UID, GID, atime, mtime, ctime, inode, link
# count and block allocation. They are not source content and reads and copies
# legitimately move some of them. Type, mode, size, file digest and exact
# relative path are the identity.
readonly HIST_SEED_PROOF='
import hashlib, os, sys

# TWO MODES, ONE IMPLEMENTATION.
#
#   gate     ASSERTS. Verifies every frozen witness identity, derives the
#            expected manifest independently from all four witnesses, requires
#            them to agree, requires the frozen digest and counts, walks the live
#            seed and requires exact equality. Any refusal exits non-zero and the
#            launcher BLOCKS.
#
#   capture  OBSERVES. Writes the two comparable proof artefacts and exits 0
#            whatever it finds, so that a seed or witness which moves DURING the
#            run is caught by the before/during/after artefact comparison and
#            reported as the regression-seed verdict, rather than aborting the
#            capture and losing the evidence. It asserts nothing: the gate above
#            is what asserts.
#
# TWO MORE MODES WERE ADDED IN v21, FOR THE CONTINUATION SOURCE. They use the
# SAME canonical rule and the SAME walker -- a second implementation would be
# exactly the parallel-gate mistake this project refuses -- and they differ in
# one way only: there is no older independent witness of the completed v20
# shadow, and none can be manufactured, so the expectation is the digest and
# counts frozen into the launcher at construction time.
#
#   frozen          ASSERTS against that frozen digest and those frozen counts.
#                   It performs NO witness derivation and REFUSES to be given a
#                   witness snapshot, so it can never silently borrow whatever
#                   authority the v11 witness rule carries.
#   frozen-capture  OBSERVES, on the same terms as capture.
#
# The gate and capture modes above are unchanged in behaviour.
CAPTURE_MODE = False
FROZEN_ONLY = False

class Refused(Exception):
    pass

def die(msg):
    if CAPTURE_MODE:
        raise Refused(msg)
    sys.stdout.write("HISTORICAL_SEED_REFUSED " + msg + "\n")
    sys.exit(3)

def check_rel(rel):
    if rel == "":
        die("empty relative path")
    if rel.startswith("/"):
        die("absolute path where a relative one was required: " + repr(rel))
    for ch in ("\t", "\n", "\r"):
        if ch in rel:
            die("path contains a field separator: " + repr(rel))
    for ch in rel:
        if ord(ch) < 32:
            die("path contains a control character: " + repr(rel))
    for part in rel.split("/"):
        if part == "" or part == "." or part == "..":
            die("malformed path component in " + repr(rel))
    return rel

def rel_under(root, path):
    if path == root:
        return None
    prefix = root + "/"
    if not path.startswith(prefix):
        return None
    return check_rel(path[len(prefix):])

def norm_mode(text):
    try:
        value = int(text, 8)
    except ValueError:
        die("unreadable permission mode " + repr(text))
    if value < 0 or value > 0o7777:
        die("permission mode out of range " + repr(text))
    return format(value, "o")

def norm_size(text):
    if not text.isdigit():
        die("unreadable size " + repr(text))
    return str(int(text))

def norm_sha(text):
    value = text.strip().lower()
    if len(value) != 64:
        die("unreadable sha256 " + repr(text))
    for ch in value:
        if ch not in "0123456789abcdef":
            die("unreadable sha256 " + repr(text))
    return value

def sha256_of(path):
    digest = hashlib.sha256()
    try:
        handle = open(path, "rb")
    except OSError as exc:
        die("cannot read " + path + " (" + str(exc) + ")")
    try:
        while True:
            chunk = handle.read(1048576)
            if not chunk:
                break
            digest.update(chunk)
    except OSError as exc:
        die("cannot read " + path + " (" + str(exc) + ")")
    finally:
        handle.close()
    return digest.hexdigest()

def witness_file_identity(path, want_sha, want_bytes):
    if os.path.islink(path):
        die("historical witness is a symlink: " + path)
    if not os.path.isfile(path):
        die("historical witness is missing or is not an ordinary file: " + path)
    try:
        size = os.lstat(path).st_size
    except OSError as exc:
        die("cannot stat historical witness " + path + " (" + str(exc) + ")")
    got_sha = sha256_of(path)
    if got_sha != want_sha:
        die("historical witness sha256 moved for " + path +
            " expected " + want_sha + " actual " + got_sha)
    if str(size) != str(want_bytes):
        die("historical witness byte count moved for " + path +
            " expected " + str(want_bytes) + " actual " + str(size))
    return got_sha, size

def read_lines(path):
    try:
        handle = open(path, "rb")
    except OSError as exc:
        die("cannot read " + path + " (" + str(exc) + ")")
    try:
        raw = handle.read()
    except OSError as exc:
        die("cannot read " + path + " (" + str(exc) + ")")
    finally:
        handle.close()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        die("historical witness is not valid UTF-8: " + path)
    if text.endswith("\n"):
        text = text[:-1]
    if text == "":
        return []
    return text.split("\n")

def serialize(entries):
    lines = []
    for entry in entries:
        if entry[0] == "file":
            lines.append("file\t%s\t%s\t%s\t%s" % (entry[1], entry[2], entry[3], entry[4]))
        else:
            lines.append("dir\t%s\t%s" % (entry[1], entry[2]))
    encoded = []
    for line in lines:
        try:
            encoded.append(line.encode("utf-8"))
        except UnicodeEncodeError:
            die("canonical manifest record is not UTF-8 encodable")
    encoded.sort()
    if len(set(encoded)) != len(encoded):
        die("duplicate canonical manifest record")
    out = b""
    for line in encoded:
        out += line + b"\n"
    return out

def build_from_witness(sha_path, meta_path, root):
    meta = {}
    for line in read_lines(meta_path):
        if line == "":
            continue
        fields = line.split(" ", 9)
        if len(fields) != 10:
            die("malformed witness metadata record: " + repr(line))
        ftype = fields[0]
        mode = fields[1]
        size = fields[4]
        path = fields[9]
        rel = rel_under(root, path)
        if rel is None:
            continue
        if ftype == "l":
            die("historical witness carries a SYMLINK at " + repr(rel) +
                " where the recorded history has none")
        if ftype != "f" and ftype != "d":
            die("historical witness carries a special entry of type " +
                repr(ftype) + " at " + repr(rel))
        if rel in meta:
            die("duplicate relative path in historical witness metadata: " + repr(rel))
        meta[rel] = (ftype, norm_mode(mode), norm_size(size))
    shas = {}
    for line in read_lines(sha_path):
        if line == "":
            continue
        if len(line) < 67 or line[64:66] != "  ":
            die("malformed witness digest record: " + repr(line))
        path = line[66:]
        rel = rel_under(root, path)
        if rel is None:
            continue
        if rel in shas:
            die("duplicate relative path in historical witness digests: " + repr(rel))
        shas[rel] = norm_sha(line[:64])
    for rel in meta:
        if meta[rel][0] == "f" and rel not in shas:
            die("regular file in historical witness metadata has no digest record: " + repr(rel))
    for rel in shas:
        if rel not in meta:
            die("historical witness digest record has no metadata record: " + repr(rel))
        if meta[rel][0] != "f":
            die("historical witness digest record is not a regular file: " + repr(rel))
    entries = []
    for rel in meta:
        ftype, mode, size = meta[rel]
        if ftype == "f":
            entries.append(("file", rel, mode, size, shas[rel]))
        else:
            entries.append(("dir", rel, mode))
    return serialize(entries)

def build_from_live(root):
    if os.path.islink(root):
        die("the regression source root is a symlink")
    if not os.path.isdir(root):
        die("the regression source root is missing or is not a directory")
    try:
        root_dev = os.lstat(root).st_dev
    except OSError as exc:
        die("cannot stat the regression source root (" + str(exc) + ")")
    entries = []
    seen = {}
    pending = [root]
    while pending:
        current = pending.pop()
        try:
            names = sorted(os.listdir(current))
        except OSError as exc:
            die("cannot read directory " + current + " (" + str(exc) + ")")
        for name in names:
            path = os.path.join(current, name)
            rel = rel_under(root, path)
            if rel is None:
                die("the live walk produced a path outside the seed root: " + repr(path))
            if rel in seen:
                die("duplicate relative path in the live seed: " + repr(rel))
            seen[rel] = True
            try:
                st = os.lstat(path)
            except OSError as exc:
                die("cannot stat " + path + " (" + str(exc) + ")")
            mode = format(st.st_mode & 0o7777, "o")
            if os.path.islink(path):
                die("the live seed carries a SYMLINK at " + repr(rel) +
                    " where the historical witness has none")
            if os.path.isdir(path):
                entries.append(("dir", rel, mode))
                if st.st_dev != root_dev:
                    die("the live seed crosses a filesystem boundary at " + repr(rel))
                pending.append(path)
            elif os.path.isfile(path):
                entries.append(("file", rel, mode, str(st.st_size), sha256_of(path)))
            else:
                die("the live seed carries a special entry at " + repr(rel))
    return serialize(entries)

def counts(manifest):
    total = 0
    files = 0
    dirs = 0
    for line in manifest.split(b"\n"):
        if line == b"":
            continue
        total += 1
        if line.startswith(b"file\t"):
            files += 1
        elif line.startswith(b"dir\t"):
            dirs += 1
        else:
            die("unrecognised canonical manifest record")
    return total, files, dirs

if len(sys.argv) < 14:
    die("wrong argument count")
root = sys.argv[1].rstrip("/")
want_manifest_sha = sys.argv[2]
want_entries = sys.argv[3]
want_files = sys.argv[4]
want_dirs = sys.argv[5]
want_symlinks = sys.argv[6]
want_sha_file_sha = sys.argv[7]
want_sha_file_bytes = sys.argv[8]
want_meta_file_sha = sys.argv[9]
want_meta_file_bytes = sys.argv[10]
emit_manifest = sys.argv[11]
emit_witness = sys.argv[12]
mode = sys.argv[13]
snapshots = sys.argv[14:]

if mode not in ("gate", "capture", "frozen", "frozen-capture"):
    die("unknown mode " + repr(mode))
CAPTURE_MODE = mode in ("capture", "frozen-capture")
FROZEN_ONLY = mode in ("frozen", "frozen-capture")

if not snapshots and not FROZEN_ONLY:
    die("no historical witness snapshot was supplied")
if snapshots and FROZEN_ONLY:
    die("a frozen-expectation mode takes no witness snapshot")
if want_symlinks != "0":
    die("this canonical rule refuses any expected symlink count other than zero")

def observe(path):
    if os.path.islink(path):
        return "SYMLINK", "SYMLINK"
    if not os.path.isfile(path):
        return "ABSENT-OR-NOT-A-REGULAR-FILE", "ABSENT-OR-NOT-A-REGULAR-FILE"
    try:
        size = os.lstat(path).st_size
    except OSError:
        return "STAT-UNREADABLE", "STAT-UNREADABLE"
    try:
        return sha256_of(path), str(size)
    except Refused:
        return "SHA256-UNREADABLE", str(size)

if CAPTURE_MODE:
    # OBSERVE ONLY. Two artefacts whose bytes change if EITHER the frozen v11
    # witness moves OR the historical seed moves, so the ordinary
    # before / during / after-every-stage / after comparison proves the
    # historical regression source stayed exactly where the gate found it.
    lines = []
    if FROZEN_ONLY:
        lines.append("expectation_source               CONSTRUCTION_TIME_FROZEN_DIGEST")
        lines.append("expectation_from_older_witness   NO")
    else:
        lines.append("historical_witness_source        PRESERVED_V11_WITNESSES")
        lines.append("expectation_from_current_seed    NO")
    lines.append("frozen_manifest_sha256           " + want_manifest_sha)
    lines.append("frozen_entries                   " + want_entries)
    lines.append("frozen_regular_files             " + want_files)
    lines.append("frozen_directories               " + want_dirs)
    lines.append("frozen_symlinks                  " + want_symlinks)
    lines.append("frozen_witness_sha256_file_sha   " + want_sha_file_sha)
    lines.append("frozen_witness_sha256_file_bytes " + want_sha_file_bytes)
    lines.append("frozen_witness_meta_file_sha     " + want_meta_file_sha)
    lines.append("frozen_witness_meta_file_bytes   " + want_meta_file_bytes)
    lines.append("seed_root                        " + root)
    for snapshot in snapshots:
        for leaf in ("preserved_labs.sha256", "preserved_labs.meta"):
            path = snapshot + "/" + leaf
            got_sha, got_bytes = observe(path)
            lines.append("witness " + os.path.basename(snapshot) + " " + leaf +
                         " " + got_sha + " " + got_bytes)
    try:
        live = build_from_live(root)
        live_total, live_files, live_dirs = counts(live)
        lines.append("live_seed_manifest_sha256        " +
                     hashlib.sha256(live).hexdigest())
        lines.append("live_seed_entries                " + str(live_total))
        lines.append("live_seed_regular_files          " + str(live_files))
        lines.append("live_seed_directories            " + str(live_dirs))
    except Refused as exc:
        live = ("LIVE_SEED_UNREADABLE " + str(exc) + "\n").encode("utf-8")
        lines.append("live_seed_manifest_sha256        UNREADABLE")
    if emit_manifest != "-":
        handle = open(emit_manifest, "wb")
        handle.write(live)
        handle.close()
    if emit_witness != "-":
        handle = open(emit_witness, "w", encoding="utf-8")
        handle.write("\n".join(lines) + "\n")
        handle.close()
    if FROZEN_ONLY:
        sys.stdout.write("CONTINUATION_SOURCE_CAPTURED\n")
    else:
        sys.stdout.write("HISTORICAL_REGRESSION_SEED_CAPTURED\n")
    sys.exit(0)

report = []
if FROZEN_ONLY:
    report.append("expectation_source               CONSTRUCTION_TIME_FROZEN_DIGEST")
    report.append("expectation_from_older_witness   NO")
else:
    report.append("historical_witness_source        PRESERVED_V11_WITNESSES")
    report.append("expectation_from_current_seed    NO")
report.append("canonical_rule                   " +
              "relpath+type+mode(+size+sha256 for regular files); "
              "root excluded; uid/gid/times/inode/nlink/blocks ignored")
report.append("seed_root                        " + root)

if FROZEN_ONLY:
    # THE FROZEN-EXPECTATION PATH, ADDED IN v21 FOR THE CONTINUATION SOURCE.
    #
    # There is no older independent witness of the completed v20 shadow, and none
    # can be manufactured, so the expectation is the digest and counts frozen
    # into the launcher at construction time. THIS PROVES THE SOURCE HAS NOT
    # MOVED SINCE THAT FREEZE, and it does not claim more than that. The anchors
    # that carry the rest -- the Repair-27A controller identity, the authenticity
    # key being equal to the one the lineage seed carries, the whole chain
    # authenticating under the semantics of the controller itself, and the exact
    # v20 marker -- are asserted by the shell gate and are not derived from this
    # manifest.
    live = build_from_live(root)
    live_sha = hashlib.sha256(live).hexdigest()
    if live_sha != want_manifest_sha:
        die("THE CONTINUATION SOURCE HAS MOVED. Its canonical manifest is " +
            live_sha + ", not the frozen " + want_manifest_sha)
    total, files, dirs = counts(live)
    if str(total) != want_entries or str(files) != want_files or str(dirs) != want_dirs:
        die("THE CONTINUATION SOURCE HAS MOVED. Its canonical manifest counts are "
            "entries " + str(total) + " files " + str(files) + " dirs " + str(dirs) +
            ", not the frozen entries " + want_entries + " files " + want_files +
            " dirs " + want_dirs)
    expected = live
    report.append("canonical_manifest_sha256        " + live_sha)
    report.append("canonical_entries                " + str(total))
    report.append("canonical_regular_files          " + str(files))
    report.append("canonical_directories            " + str(dirs))
    report.append("canonical_symlinks               0")
    report.append("live_source_matches_frozen       YES")
else:
    manifests = []
    for snapshot in snapshots:
        sha_path = snapshot + "/preserved_labs.sha256"
        meta_path = snapshot + "/preserved_labs.meta"
        got_sha_sha, sha_size = witness_file_identity(sha_path, want_sha_file_sha, want_sha_file_bytes)
        got_meta_sha, meta_size = witness_file_identity(meta_path, want_meta_file_sha, want_meta_file_bytes)
        report.append("witness_snapshot                 " + os.path.basename(snapshot))
        report.append("  preserved_labs.sha256_path     " + sha_path)
        report.append("  preserved_labs.sha256_sha256   " + got_sha_sha)
        report.append("  preserved_labs.sha256_bytes    " + str(sha_size))
        report.append("  preserved_labs.meta_path       " + meta_path)
        report.append("  preserved_labs.meta_sha256     " + got_meta_sha)
        report.append("  preserved_labs.meta_bytes      " + str(meta_size))
        manifests.append((snapshot, build_from_witness(sha_path, meta_path, root)))

    first_snapshot, expected = manifests[0]
    for snapshot, manifest in manifests[1:]:
        if manifest != expected:
            die("the historical witnesses do NOT agree. " +
                os.path.basename(snapshot) + " yields a different canonical seed " +
                "manifest from " + os.path.basename(first_snapshot) + ". There is no " +
                "majority vote, no average and no fallback to the current seed.")
    report.append("cross_witness_agreement          YES")

    expected_sha = hashlib.sha256(expected).hexdigest()
    if expected_sha != want_manifest_sha:
        die("the canonical historical manifest derived from the v11 witnesses is " +
            expected_sha + ", not the frozen " + want_manifest_sha)
    total, files, dirs = counts(expected)
    if str(total) != want_entries or str(files) != want_files or str(dirs) != want_dirs:
        die("the canonical historical manifest counts moved: entries " + str(total) +
            " files " + str(files) + " dirs " + str(dirs))
    report.append("canonical_manifest_sha256        " + expected_sha)
    report.append("canonical_entries                " + str(total))
    report.append("canonical_regular_files          " + str(files))
    report.append("canonical_directories            " + str(dirs))
    report.append("canonical_symlinks               0")

    live = build_from_live(root)
    if live != expected:
        expected_set = set(expected.split(b"\n"))
        live_set = set(live.split(b"\n"))
        detail = []
        for line in sorted(expected_set - live_set):
            if line:
                detail.append("  HISTORICAL ONLY: " + line.decode("utf-8", "replace"))
        for line in sorted(live_set - expected_set):
            if line:
                detail.append("  CURRENT SEED ONLY: " + line.decode("utf-8", "replace"))
        die("THE HISTORICAL REGRESSION SOURCE HAS MOVED. The current seed does not " +
            "match the workspace the preserved v11 witness recorded.\n" +
            "\n".join(detail[:200]))
    report.append("live_seed_matches_historical     YES")

if emit_manifest != "-":
    try:
        handle = open(emit_manifest, "wb")
        handle.write(expected)
        handle.close()
    except OSError as exc:
        die("cannot write the manifest artefact (" + str(exc) + ")")
if emit_witness != "-":
    try:
        handle = open(emit_witness, "w", encoding="utf-8")
        handle.write("\n".join(report) + "\n")
        handle.close()
    except OSError as exc:
        die("cannot write the witness artefact (" + str(exc) + ")")

sys.stdout.write("\n".join(report) + "\n")
if FROZEN_ONLY:
    sys.stdout.write("CONTINUATION_SOURCE_MANIFEST_PROVEN\n")
else:
    sys.stdout.write("HISTORICAL_REGRESSION_SEED_PROVEN\n")
'

# assert_historical_seed_manifest <emit_manifest_path|-> <emit_witness_path|->
#
# THE WHOLE-HISTORICAL-WORKSPACE GATE. It is called only from
# assert_regression_source, so it runs at every point that function runs: as a
# precondition before the lab exists, again once the proof directory exists so
# the artefacts are recorded, and again under both original locks immediately
# before the copy. All three are before the isolation self-test and therefore
# before any possible provider or model call.
#
# It REPAIRS NOTHING. There is no retry, no fallback and no recovery path: the
# only outcomes are proven and BLOCKED.
assert_historical_seed_manifest() {
  local emit_manifest="$1" emit_witness="$2"
  local snapshot_args=() snap
  for snap in "${V11_WITNESS_SNAPSHOTS[@]}"; do
    snapshot_args+=("${V11_PROOF_DIR}/${snap}")
  done

  local hist_out hist_rc=0
  set +e
  hist_out="$(
    PYTHONDONTWRITEBYTECODE=1 "$PY3" -B -c "$HIST_SEED_PROOF" \
      "$REGRESSION_SOURCE" \
      "$EXP_HIST_SEED_MANIFEST_SHA" \
      "$EXP_HIST_SEED_MANIFEST_ENTRIES" \
      "$EXP_HIST_SEED_MANIFEST_FILES" \
      "$EXP_HIST_SEED_MANIFEST_DIRS" \
      "$EXP_HIST_SEED_MANIFEST_SYMLINKS" \
      "$EXP_V11_WITNESS_SHA_FILE_SHA" \
      "$EXP_V11_WITNESS_SHA_FILE_BYTES" \
      "$EXP_V11_WITNESS_META_FILE_SHA" \
      "$EXP_V11_WITNESS_META_FILE_BYTES" \
      "$emit_manifest" \
      "$emit_witness" \
      "gate" \
      "${snapshot_args[@]}" 2>&1
  )"
  hist_rc=$?
  set -e

  if [ "$hist_rc" -ne 0 ] \
     || ! printf '%s' "$hist_out" | grep -q '^HISTORICAL_REGRESSION_SEED_PROVEN$'; then
    die "THE COMPLETE HISTORICAL REGRESSION SOURCE DID NOT PROVE AGAINST THE
      PRESERVED v11 WITNESS (status ${hist_rc}):
${hist_out}
      The selected journal, head, key, marker and controller identities are not
      enough on their own: question-validation and question-coverage-review read
      the actual N.H source files, so an ordinary changed source file inside the
      seed changes the answer being tested.
      NOTHING IS REPAIRED HERE. The v11 witness is not regenerated, the seed is
      not normalised, and no expectation is recomputed from the current seed.
      Refusing to rehearse."
  fi
  note "the complete historical regression workspace matches the preserved v11 witness"
  note "all four v11 witness snapshots independently yield one identical manifest"
}

# THE CONTROLLER BYTECODE, PROVED FROZEN RATHER THAN PROVED ABSENT.
#
# v11's ancestor of this function required NO bytecode to exist. Three exist now,
# compiled from real controller and candidate sources, so the requirement is
# restated as an IDENTITY requirement: exactly this bytecode set, exactly this
# digest, exactly this byte count, and no other .pyc or __pycache__ anywhere
# under the controller. Nothing is deleted and nothing is regenerated here.
assert_controller_bytecode_frozen() {
  local where="$1" found expected i
  found="$(find "${CTRL}" -name '__pycache__' -o -name '*.pyc' 2>/dev/null | LC_ALL=C sort)"
  expected="$(printf '%s\n' "$CTRL_PYCACHE_DIR" "${CTRL_PYCACHE_FILES[@]}" | LC_ALL=C sort)"
  if [ "$found" != "$expected" ]; then
    die "the python bytecode set under the protected controller directory is not
      the frozen one ${where}:
        expected:
${expected}
        found:
${found}
      Nothing is deleted here. A launcher frozen to one exact moment fails closed
      and is re-frozen deliberately."
  fi
  for i in "${!CTRL_PYCACHE_FILES[@]}"; do
    expect "controller bytecode $((i+1)) sha256 ${where}" \
           "$(sha_of "${CTRL_PYCACHE_FILES[$i]}")"   "${CTRL_PYCACHE_SHAS[$i]}"
    expect "controller bytecode $((i+1)) bytes  ${where}" \
           "$(bytes_of "${CTRL_PYCACHE_FILES[$i]}")" "${CTRL_PYCACHE_BYTES_LIST[$i]}"
  done
}

assert_regression_source() {
  # 1. SHAPE -- the preserved lab and the regression source inside it.
  if [ -L "$PRESERVED_LAB_REPAIR17_CONTINUATION_V10" ]; then
    die "the preserved v10 lab is a SYMLINK:
        ${PRESERVED_LAB_REPAIR17_CONTINUATION_V10}
      A symlink here could redirect the regression copy. Refusing to rehearse."
  fi
  if [ ! -d "$PRESERVED_LAB_REPAIR17_CONTINUATION_V10" ]; then
    die "the preserved v10 lab is missing or is not a directory:
        ${PRESERVED_LAB_REPAIR17_CONTINUATION_V10}
      It is BOTH the completed v10 evidence and this run's only authorised
      regression source. Nothing is created to repair it."
  fi
  if [ -L "$REGRESSION_SOURCE" ]; then
    die "the regression source workspace is a SYMLINK:
        ${REGRESSION_SOURCE}
      Refusing to rehearse."
  fi
  if [ ! -d "$REGRESSION_SOURCE" ]; then
    die "the regression source workspace is missing or is not a directory:
        ${REGRESSION_SOURCE}
      Refusing to rehearse."
  fi
  if [ -L "$SEED_STATE" ] || [ ! -d "$SEED_STATE" ]; then
    die "the regression source interview state is missing or is not a real
      directory:
        ${SEED_STATE}
      Refusing to rehearse."
  fi
  for _sf in "$SEED_JOURNAL" "$SEED_JOURNAL_HEAD" "$SEED_AUTH_KEY" "$SEED_LOOP"; do
    if [ -L "$_sf" ] || [ ! -f "$_sf" ]; then
      die "a regression source file is missing or is not an ordinary,
      non-symlink file:
        ${_sf}
      Refusing to rehearse."
    fi
  done
  unset _sf
  note "the preserved v10 lab and its regression source are real, non-symlink directories"

  # 2. IDENTITY -- exactly the historical snapshot this launcher was frozen to.
  expect "regression seed journal sha256" "$(sha_of "$SEED_JOURNAL")"   "$EXP_SEED_JOURNAL_SHA"
  expect "regression seed journal bytes"  "$(bytes_of "$SEED_JOURNAL")" "$EXP_SEED_JOURNAL_BYTES"
  expect "regression seed journal lines"  "$(wc -l < "$SEED_JOURNAL")"  "$EXP_SEED_JOURNAL_LINES"
  expect "regression seed journal events" \
         "$(grep -c '[^[:space:]]' -- "$SEED_JOURNAL" || true)" "$EXP_SEED_JOURNAL_EVENTS"
  expect "regression seed journal head sha256"     "$(sha_of "$SEED_JOURNAL_HEAD")" "$EXP_SEED_HEAD_SHA"
  expect "regression seed authenticity key sha256" "$(sha_of "$SEED_AUTH_KEY")"     "$EXP_SEED_KEY_SHA"
  expect "regression seed v10 shadow marker sha256" \
         "$(sha_of "${REGRESSION_SOURCE}/${SHADOW_MARKER_NAME}")" "$EXP_SEED_V10_MARKER_SHA"
  expect "regression seed authenticated package scope occurrences" \
         "$(grep -c -F -- "$EXP_PKG_SCOPE" "$SEED_JOURNAL" || true)" \
         "$EXP_SEED_PKG_SCOPE_OCCURRENCES"

  # 2b. THE SEED'S OWN CONTROLLER -- THE EXACT REPAIR-17 FILE.
  #
  # The refresh in section 7b is authorised as a transition between two NAMED
  # identities. If the seed controller is anything other than the exact Repair-17
  # file this launcher was frozen against, then whatever the refresh would be
  # replacing is not what this launcher believes it is replacing, and the run is
  # refused rather than guessed at.
  expect "regression seed controller sha256 (Repair 17)" "$(sha_of "$SEED_LOOP")"   "$EXP_SEED_LOOP_SHA"
  expect "regression seed controller bytes  (Repair 17)" "$(bytes_of "$SEED_LOOP")" "$EXP_SEED_LOOP_BYTES"
  expect "regression seed controller lines  (Repair 17)" "$(wc -l < "$SEED_LOOP")"  "$EXP_SEED_LOOP_LINES"

  # 3. THE SIGNAL -- present exactly once, by identifier and by digest. These are
  #    counts over the journal file, so a duplicated or planted identifier fails
  #    just as loudly as a missing one.
  expect "regression seed event 7 digest occurrences" \
         "$(grep -c -F -- "$EXP_SEED_EVENT7_SHA" "$SEED_JOURNAL" || true)" \
         "$EXP_SEED_EVENT7_SHA_OCCURRENCES"
  expect "regression seed event 6 digest occurrences" \
         "$(grep -c -F -- "$EXP_SEED_EVENT6_SHA" "$SEED_JOURNAL" || true)" \
         "$EXP_SEED_EVENT6_SHA_OCCURRENCES"
  expect "regression seed routed signal occurrences" \
         "$(grep -c -F -- "$EXP_ROUTED_SIGNAL_ID" "$SEED_JOURNAL" || true)" \
         "$EXP_SEED_ROUTED_SIGNAL_OCCURRENCES"
  expect "regression seed standing target occurrences" \
         "$(grep -c -F -- "$EXP_STANDING_TARGET_ID" "$SEED_JOURNAL" || true)" \
         "$EXP_SEED_STANDING_TARGET_OCCURRENCES"

  # 4. AUTHENTICITY -- the controller's own digest, HMAC, chain and head rules.
  #
  # Not one identifier above is trusted because the string is there. This step is
  # what makes the regression source evidence rather than text.
  assert_controller_bytecode_frozen "before the regression-source authentication step"
  local seed_auth_out seed_auth_rc=0
  set +e
  seed_auth_out="$(
    PYTHONDONTWRITEBYTECODE=1 "$PY3" -B -c "$SEED_AUTH_CHECKER" \
      "${CTRL}/nh_loop.py" \
      "$SEED_STATE" \
      "$EXP_SEED_JOURNAL_EVENTS" \
      "type=${EXP_SEED_EVENT7_TYPE}" \
      "route=${EXP_SEED_EVENT7_ROUTE}" \
      "signal_source=${EXP_SEED_EVENT7_SIGNAL_SOURCE}" \
      "routed_signal_id=${EXP_ROUTED_SIGNAL_ID}" \
      "standing_target_id=${EXP_STANDING_TARGET_ID}" \
      "issue_key=${EXP_SEED_EVENT7_ISSUE_KEY}" \
      "finding_key=${EXP_SEED_EVENT7_FINDING_KEY}" \
      "package_scope_id=${EXP_PKG_SCOPE}" \
      "event_sha256=${EXP_SEED_EVENT7_SHA}" \
      "prev_event_sha256=${EXP_SEED_EVENT6_SHA}" 2>&1
  )"
  seed_auth_rc=$?
  set -e
  assert_controller_bytecode_frozen "after the regression-source authentication step"

  # The authentication result is preserved as its own named proof artefact once
  # the lab exists. On the first, pre-lab invocation there is nowhere to write it
  # yet, and the gate still fails closed either way.
  if [ -d "$PROOF" ]; then
    {
      printf 'regression_source   %s\n' "$REGRESSION_SOURCE"
      printf 'controller_used     %s\n' "${CTRL}/nh_loop.py"
      printf 'controller_sha256   %s\n' "$EXP_LOOP_SHA"
      printf 'expected_events     %s\n' "$EXP_SEED_JOURNAL_EVENTS"
      printf 'checker_status      %s\n' "$seed_auth_rc"
      printf 'checker_output\n%s\n' "$seed_auth_out"
    } > "${PROOF}/regression-seed-authentication.txt" 2>/dev/null || true
  fi

  if [ "$seed_auth_rc" -ne 0 ] \
     || ! printf '%s' "$seed_auth_out" | grep -q '^REGRESSION_SOURCE_AUTHENTICATED$'; then
    die "the regression source did NOT authenticate under the controller's own
      journal semantics (status ${seed_auth_rc}):
${seed_auth_out}
      The historical state is not proved to be the state v10 left. Nothing is
      repaired, reconstructed or replaced here. Refusing to rehearse."
  fi
  note "the seven-event regression source authenticates under the controller's own semantics"
  note "the routed review signal ${EXP_ROUTED_SIGNAL_ID} is present as the last event, unresolved"

  # 5. THE COMPLETE HISTORICAL WORKSPACE.  NEW IN v13.
  #
  # Steps 2 to 4 prove the INTERVIEW JOURNAL is the authentic historical one.
  # They say nothing about the rest of the workspace, and the rest of the
  # workspace is what question-validation and question-coverage-review actually
  # read. This step proves EVERY entry beneath the seed root -- every ordinary
  # N.H source and design file, every directory, every mode, and the seed's Git
  # metadata -- is byte-for-byte what the preserved v11 witness recorded, using
  # an expectation that was written before this correction existed.
  #
  # THE RELATIONSHIP IS ADDITIVE AND NEITHER HALF REPLACES THE OTHER:
  #   complete historical workspace identity
  # + interview journal authenticity
  # = a valid regression source.
  #
  # It runs here, inside this function, so it is asserted on all three of this
  # function's invocations rather than once. A historical seed that changed
  # between the precondition and the copy therefore fails too.
  if [ -d "$PROOF" ]; then
    assert_historical_seed_manifest \
      "${PROOF}/regression-seed-historical-manifest.txt" \
      "${PROOF}/regression-seed-historical-witness.txt"
  else
    assert_historical_seed_manifest "-" "-"
  fi

  # The regression-source identity, written as its own standalone artefact so a
  # reader never has to dig it out of a directory of captures.
  if [ -d "$PROOF" ]; then
    {
      printf 'REGRESSION SOURCE IDENTITY\n'
      printf '  path                    %s\n' "$REGRESSION_SOURCE"
      printf '  mode                    %s\n' "$REGRESSION_SOURCE_MODE"
      printf '  journal sha256          %s\n' "$EXP_SEED_JOURNAL_SHA"
      printf '  journal bytes           %s\n' "$EXP_SEED_JOURNAL_BYTES"
      printf '  journal events          %s\n' "$EXP_SEED_JOURNAL_EVENTS"
      printf '  head sha256             %s\n' "$EXP_SEED_HEAD_SHA"
      printf '  authenticity key sha256 %s\n' "$EXP_SEED_KEY_SHA"
      printf '  routed signal id        %s\n' "$EXP_ROUTED_SIGNAL_ID"
      printf '  standing target id      %s\n' "$EXP_STANDING_TARGET_ID"
      printf '  package scope id        %s\n' "$EXP_PKG_SCOPE"
      printf '  seed controller sha256  %s\n' "$EXP_SEED_LOOP_SHA"
      printf '  seed controller bytes   %s\n' "$EXP_SEED_LOOP_BYTES"
      printf '  seed controller lines   %s\n' "$EXP_SEED_LOOP_LINES"
      printf '\n'
      printf 'THIS IS A HISTORICAL SNAPSHOT. IT IS NOT ASSERTED TO EQUAL THE\n'
      printf 'CURRENT REAL WORKSPACE, AND THIS LAUNCHER NEVER COMPARES THE TWO.\n'
      printf 'The current real N.H checkout has legitimately moved since this\n'
      printf 'snapshot was taken. That movement is protected, not reconciled:\n'
      printf 'see the frozen current-source gate and the original.* proofs.\n'
    } > "${PROOF}/regression-seed-identity.txt" 2>/dev/null || true
  fi
}

# --------------------------------------------------------------------------
# SECTION 4b2 — THE CONTROLLER REPORT PARSER
# --------------------------------------------------------------------------
#
# RELOCATED IN v21, NOT REWRITTEN. In v20 this lived in section 11, because
# nothing before the stages needed it. In v21 the v20-result authentication gate
# below reads the controller's own reported fields out of the preserved v20
# stdout artefacts, and that gate runs long before any stage, so the definition
# has to precede it. It is used by that gate AND by the section-11 display
# readers; there is exactly ONE report parser in this file and no second
# implementation of the rule.
#
# A structural parse, done by the same python3 the controller itself runs,
# reading only.
#
# WHY NOT grep. Matching with `grep -m1 -F '  "<key>": '` is not anchored to
# anything: -F matches a SUBSTRING anywhere in the line, so a nested key at
# four-space indent -- `    "ok": false,` -- contains the two-space form and
# matches, and -m1 then returns that nested key in place of the real top-level
# one. The controller's reports carry nested objects with exactly these names, so
# this was never theoretical.
#
# WHAT IT IS. The controller prints human lines and then ONE
# json.dumps(indent=2, sort_keys=True) report, so the report is the unique JSON
# object that starts at the beginning of a line and whose parse consumes the rest
# of the file except trailing whitespace. Every line-start "{" is tried with
# raw_decode; a candidate counts only if it decodes to a dict AND reaches EOF.
# Exactly one candidate must qualify -- zero or several is ambiguous output and
# is refused.
#
# The value is printed as canonical compact JSON, so true, 0, [] and "0" are all
# distinguishable and a type confusion cannot pass as a match.
#
# Exit status: 0 value printed, 2 unreadable file, 3 no single complete report,
# 4 no such TOP-LEVEL key. Every one of them fails a gate closed.
readonly REPORT_PARSER='
import json, sys
try:
    with open(sys.argv[1], encoding="utf-8") as handle:
        text = handle.read()
except OSError:
    sys.exit(2)
decoder = json.JSONDecoder()
starts = []
if text.startswith("{"):
    starts.append(0)
at = text.find("\n{")
while at != -1:
    starts.append(at + 1)
    at = text.find("\n{", at + 1)
found = []
for start in starts:
    try:
        value, end = decoder.raw_decode(text, start)
    except ValueError:
        continue
    if isinstance(value, dict) and text[end:].strip() == "":
        found.append(value)
if len(found) != 1:
    sys.exit(3)
report = found[0]
if sys.argv[2] not in report:
    sys.exit(4)
sys.stdout.write(
    json.dumps(report[sys.argv[2]], sort_keys=True, separators=(",", ":"))
)
'

# --------------------------------------------------------------------------
# SECTION 4b3 — THE COMPLETED v20 RESULT, AUTHENTICATED BEFORE IT MAY BE
#               CONTINUED FROM                                   (NEW IN v21)
# --------------------------------------------------------------------------
#
# THE WHOLE PREMISE OF v24 RESTS ON THIS GATE. v24 does not rerun Doors 1, 2 and
# 3. That is only legitimate if v20 actually ran them and they actually passed,
# and if the Stage-4 result really was the Repair-27A preparation-report crash
# rather than some other outcome. So the recorded v20 result is PROVED here, from
# the preserved v20 artefacts themselves, and the run is REFUSED if it cannot be.
#
# WHAT IS REQUIRED, EXACTLY:
#   Stage 1  exit 0, ok true, validation_inventory_complete true,
#            material_unknowns [], deliverable_question_count 0
#   Stage 2  exit 0, coverage_review_cleared true, coverage_possible_gaps 0
#   Stage 3  exit 0, mechanical_path_unlocked true
#   Stage 4  exit 1, stdout EMPTY, stderr carrying the exact confirmed Repair-27A
#            crash: the subscript
#              prepared["mechanical_design_specification"]["requirements"]
#            raising TypeError: 'NoneType' object is not subscriptable inside
#            run_prepare_next_claude_task
#   AND every one of the four v20 stage source-proofs must read PASS.
#
# IT IS PROVED TWICE OVER AND NEITHER HALF REPLACES THE OTHER. Every artefact is
# first required to carry its exact frozen sha256 and byte count, so a single
# changed byte anywhere in the recorded result fails the run closed; then the
# controller's own fields are re-read out of those same artefacts and required to
# be exactly the recorded values.
#
# NOTHING IS REINTERPRETED AND NOTHING IS REGENERATED. No v20 stage is rerun --
# there is no call site able to run one -- no artefact is repaired, normalised or
# rewritten, and no expectation is recomputed from anything but section 0.

# v20_require_artefact <label> <path> <expected sha256> <expected bytes|->
v20_require_artefact() {
  local label="$1" path="$2" want_sha="$3" want_bytes="$4"
  if [ -L "$path" ] || [ ! -f "$path" ]; then
    die "a required completed-v20 artefact is missing or is not an ordinary,
      non-symlink file:
        ${path}
      The v20 result cannot be authenticated, so this continuation is refused.
      Nothing is regenerated and no v20 stage is rerun."
  fi
  expect "v20 ${label} sha256" "$(sha_of "$path")" "$want_sha"
  if [ "$want_bytes" != "-" ]; then
    expect "v20 ${label} bytes" "$(bytes_of "$path")" "$want_bytes"
  fi
}

# v20_require_field <label> <stdout path> <key> <expected canonical JSON>
#
# TRUE only when the preserved v20 report states, at TOP LEVEL, exactly
# <expected>. Unreadable, unparseable, ambiguous, absent, wrong-type and
# different all fail, and all fail CLOSED.
v20_require_field() {
  local label="$1" file="$2" key="$3" want="$4" actual rc
  set +e
  actual="$("$PY3" -c "$REPORT_PARSER" "$file" "$key" 2>/dev/null)"
  rc=$?
  set -e
  if [ "$rc" -ne 0 ]; then
    die "the preserved v20 ${label} report could not be read for ${key}
      (parser status ${rc}):
        ${file}
      The v20 result cannot be authenticated, so this continuation is refused.
      Nothing is regenerated and no v20 stage is rerun."
  fi
  expect "v20 ${label} ${key}" "$actual" "$want"
}

assert_v20_result_authenticated() {
  local s1="${V20_PROOF_DIR}/${V20_STAGE1_ARTEFACT}"
  local s2="${V20_PROOF_DIR}/${V20_STAGE2_ARTEFACT}"
  local s3="${V20_PROOF_DIR}/${V20_STAGE3_ARTEFACT}"
  local s4="${V20_PROOF_DIR}/${V20_STAGE4_ARTEFACT}"

  # 1. THE PROOF DIRECTORY ITSELF.
  if [ -L "$V20_PROOF_DIR" ] || [ ! -d "$V20_PROOF_DIR" ]; then
    die "the completed v20 proof directory is missing or is not a real
      directory:
        ${V20_PROOF_DIR}
      Without it the v20 result cannot be authenticated and this continuation is
      refused. Nothing is created to repair it."
  fi

  # 2. EVERY REQUIRED ARTEFACT, BY EXACT IDENTITY.
  v20_require_artefact "stage1 exit-code"    "${s1}.exit-code"    "$EXP_V20_S1_EXITCODE_SHA"  "-"
  v20_require_artefact "stage1 stdout"       "${s1}.stdout"       "$EXP_V20_S1_STDOUT_SHA"    "$EXP_V20_S1_STDOUT_BYTES"
  v20_require_artefact "stage1 source-proof" "${s1}.source-proof" "$EXP_V20_SOURCE_PROOF_SHA" "-"
  v20_require_artefact "stage2 exit-code"    "${s2}.exit-code"    "$EXP_V20_S2_EXITCODE_SHA"  "-"
  v20_require_artefact "stage2 stdout"       "${s2}.stdout"       "$EXP_V20_S2_STDOUT_SHA"    "$EXP_V20_S2_STDOUT_BYTES"
  v20_require_artefact "stage2 source-proof" "${s2}.source-proof" "$EXP_V20_SOURCE_PROOF_SHA" "-"
  v20_require_artefact "stage3 exit-code"    "${s3}.exit-code"    "$EXP_V20_S3_EXITCODE_SHA"  "-"
  v20_require_artefact "stage3 stdout"       "${s3}.stdout"       "$EXP_V20_S3_STDOUT_SHA"    "$EXP_V20_S3_STDOUT_BYTES"
  v20_require_artefact "stage3 source-proof" "${s3}.source-proof" "$EXP_V20_SOURCE_PROOF_SHA" "-"
  v20_require_artefact "stage4 exit-code"    "${s4}.exit-code"    "$EXP_V20_S4_EXITCODE_SHA"  "-"
  v20_require_artefact "stage4 stdout"       "${s4}.stdout"       "$EXP_V20_S4_STDOUT_SHA"    "$EXP_V20_S4_STDOUT_BYTES"
  v20_require_artefact "stage4 stderr"       "${s4}.stderr"       "$EXP_V20_S4_STDERR_SHA"    "$EXP_V20_S4_STDERR_BYTES"
  v20_require_artefact "stage4 source-proof" "${s4}.source-proof" "$EXP_V20_SOURCE_PROOF_SHA" "-"
  v20_require_artefact "controller-refresh.after" \
                       "${V20_PROOF_DIR}/controller-refresh.after"     "$EXP_V20_REFRESH_AFTER_SHA"     "-"
  v20_require_artefact "controller-refresh.composite" \
                       "${V20_PROOF_DIR}/controller-refresh.composite" "$EXP_V20_REFRESH_COMPOSITE_SHA" "-"

  # 3. THE RECORDED EXIT CODES AND SOURCE PROOFS, READ BACK.
  expect "v20 stage1 exit code" "$(cat -- "${s1}.exit-code")" "$EXP_V20_S1_EXIT"
  expect "v20 stage2 exit code" "$(cat -- "${s2}.exit-code")" "$EXP_V20_S2_EXIT"
  expect "v20 stage3 exit code" "$(cat -- "${s3}.exit-code")" "$EXP_V20_S3_EXIT"
  expect "v20 stage4 exit code" "$(cat -- "${s4}.exit-code")" "$EXP_V20_S4_EXIT"
  expect "v20 stage1 source-proof" "$(cat -- "${s1}.source-proof")" "$EXP_V20_SOURCE_PROOF_VALUE"
  expect "v20 stage2 source-proof" "$(cat -- "${s2}.source-proof")" "$EXP_V20_SOURCE_PROOF_VALUE"
  expect "v20 stage3 source-proof" "$(cat -- "${s3}.source-proof")" "$EXP_V20_SOURCE_PROOF_VALUE"
  expect "v20 stage4 source-proof" "$(cat -- "${s4}.source-proof")" "$EXP_V20_SOURCE_PROOF_VALUE"

  # 4. THE CONTROLLER'S OWN DOORS-1-TO-3 FACTS, READ BACK FROM ITS OWN REPORTS.
  v20_require_field "stage1" "${s1}.stdout" "ok"                            "true"
  v20_require_field "stage1" "${s1}.stdout" "validation_inventory_complete" "true"
  v20_require_field "stage1" "${s1}.stdout" "material_unknowns"             "[]"
  v20_require_field "stage1" "${s1}.stdout" "deliverable_question_count"    "0"
  v20_require_field "stage2" "${s2}.stdout" "ok"                            "true"
  v20_require_field "stage2" "${s2}.stdout" "coverage_review_cleared"       "true"
  v20_require_field "stage2" "${s2}.stdout" "coverage_possible_gaps"        "0"
  v20_require_field "stage3" "${s3}.stdout" "ok"                            "true"
  v20_require_field "stage3" "${s3}.stdout" "mechanical_path_unlocked"      "true"

  # 5. THE STAGE-4 CRASH, PROVED AS A CRASH AND NOT AS A STOP.
  #
  #    An ordinary controller fail-closed stop writes a machine report on stdout
  #    and exits 1 with a stop_reason. This one wrote NOTHING. The empty stdout is
  #    therefore load-bearing evidence in its own right and is required as such.
  expect "v20 stage4 stdout is empty" "$(bytes_of "${s4}.stdout")" "0"
  local needle
  for needle in "$EXP_V20_S4_CRASH_SUBSCRIPT" \
                "$EXP_V20_S4_CRASH_TYPE" \
                "$EXP_V20_S4_CRASH_FUNC"; do
    if ! grep -q -F -- "$needle" "${s4}.stderr"; then
      die "the preserved v20 Stage-4 stderr does not carry the exact confirmed
      Repair-27A crash. This line was required and is absent:
        ${needle}
      v21 exists to continue from THAT crash. Refusing to continue from a
      Stage-4 result that is not the one recorded. Nothing is reinterpreted and
      no v20 stage is rerun."
    fi
  done

  V20_RESULT_AUTHENTICATED="PASS"
  note "the completed v20 Doors-1-to-3 result authenticates: stages 1, 2 and 3 exit 0 and PASS"
  note "the completed v20 Stage-4 result authenticates: exit 1, empty stdout, the exact Repair-27A crash"

  # The authentication result is preserved as its own named proof artefact once
  # the lab exists. On the first, pre-lab invocation there is nowhere to write it
  # yet, and the gate still fails closed either way.
  if [ -d "$PROOF" ]; then
    {
      printf 'COMPLETED v20 RESULT AUTHENTICATION\n'
      printf '  proof directory           %s\n' "$V20_PROOF_DIR"
      printf '  predecessor launcher      %s\n' "$LAUNCHER_V20_BASENAME"
      printf '  predecessor sha256        %s\n' "$EXP_LAUNCHER_V20_SHA"
      printf '\n'
      printf '  stage1 question-validation      exit %s  source-proof %s\n' \
             "$EXP_V20_S1_EXIT" "$EXP_V20_SOURCE_PROOF_VALUE"
      printf '    ok true, validation_inventory_complete true,\n'
      printf '    material_unknowns [], deliverable_question_count 0\n'
      printf '  stage2 question-coverage-review exit %s  source-proof %s\n' \
             "$EXP_V20_S2_EXIT" "$EXP_V20_SOURCE_PROOF_VALUE"
      printf '    ok true, coverage_review_cleared true, coverage_possible_gaps 0\n'
      printf '  stage3 interview-gate           exit %s  source-proof %s\n' \
             "$EXP_V20_S3_EXIT" "$EXP_V20_SOURCE_PROOF_VALUE"
      printf '    ok true, mechanical_path_unlocked true\n'
      printf '  stage4 execute-next-claude-task exit %s  source-proof %s\n' \
             "$EXP_V20_S4_EXIT" "$EXP_V20_SOURCE_PROOF_VALUE"
      printf '    stdout EMPTY (%s bytes) -- a crash, not a stop\n' "$EXP_V20_S4_STDOUT_BYTES"
      printf '    stderr sha256 %s (%s bytes)\n' "$EXP_V20_S4_STDERR_SHA" "$EXP_V20_S4_STDERR_BYTES"
      printf '    %s\n' "$EXP_V20_S4_CRASH_FUNC"
      printf '    %s\n' "$EXP_V20_S4_CRASH_SUBSCRIPT"
      printf '    %s\n' "$EXP_V20_S4_CRASH_TYPE"
      printf '\n'
      printf 'THESE FACTS WERE PROVED FROM THE PRESERVED v20 ARTEFACTS, TWICE:\n'
      printf 'by exact frozen sha256 and byte count, and by re-reading the\n'
      printf 'controller\047s own reported fields out of those same artefacts.\n'
      printf 'No v20 stage was rerun, nothing was regenerated, nothing was\n'
      printf 'reinterpreted, and the v20 lab was never written to.\n'
      printf '\n'
      printf 'THIS IS WHAT MAKES A STAGE-4-ONLY CONTINUATION LEGITIMATE. Doors 1\n'
      printf 'to 3 are not skipped: they were run for real by v20, they passed,\n'
      printf 'and their outcome is carried forward inside the continuation\n'
      printf 'source\047s own authenticated interview journal.\n'
      printf 'V20_RESULT_AUTHENTICATED = %s\n' "$V20_RESULT_AUTHENTICATED"
    } > "${PROOF}/v20-result-authentication.txt" 2>/dev/null || true
  fi
}

# v21_require_artefact <label> <path> <expected sha256> <expected bytes|->
v21_require_artefact() {
  local label="$1" path="$2" want_sha="$3" want_bytes="$4"
  if [ -L "$path" ] || [ ! -f "$path" ]; then
    die "a required completed-v21 artefact is missing or is not an ordinary,
      non-symlink file:
        ${path}
      The v21 result cannot be authenticated, so this continuation is refused.
      Nothing is regenerated and no v21 stage is rerun."
  fi
  expect "v21 ${label} sha256" "$(sha_of "$path")" "$want_sha"
  if [ "$want_bytes" != "-" ]; then
    expect "v21 ${label} bytes" "$(bytes_of "$path")" "$want_bytes"
  fi
}

# v21_require_field <label> <stdout path> <key> <expected canonical JSON>
v21_require_field() {
  local label="$1" file="$2" key="$3" want="$4" actual rc
  set +e
  actual="$("$PY3" -c "$REPORT_PARSER" "$file" "$key" 2>/dev/null)"
  rc=$?
  set -e
  if [ "$rc" -ne 0 ]; then
    die "the preserved v21 ${label} report could not be read for ${key}
      (parser status ${rc}):
        ${file}
      The v21 result cannot be authenticated, so this continuation is refused.
      Nothing is regenerated and no v21 stage is rerun."
  fi
  expect "v21 ${label} ${key}" "$actual" "$want"
}

# v21_require_needle <label> <file> <exact needle>
v21_require_needle() {
  local label="$1" file="$2" needle="$3"
  if ! grep -q -F -- "$needle" "$file"; then
    die "the preserved v21 Stage-4 report does not carry a required recorded
      fact. This exact line was required and is absent:
        ${needle}
      v22 exists to continue from THAT recorded stop. Refusing to continue from
      a Stage-4 result that is not the one recorded. Nothing is reinterpreted
      and no v21 stage is rerun. (${label})"
  fi
}

assert_v21_result_authenticated() {
  local s4="${V21_PROOF_DIR}/${V21_STAGE4_ARTEFACT}"

  # 1. THE PROOF DIRECTORY ITSELF.
  if [ -L "$V21_PROOF_DIR" ] || [ ! -d "$V21_PROOF_DIR" ]; then
    die "the completed v21 proof directory is missing or is not a real
      directory:
        ${V21_PROOF_DIR}
      Without it the v21 result cannot be authenticated and this continuation is
      refused. Nothing is created to repair it."
  fi

  # 2. EVERY REQUIRED ARTEFACT, BY EXACT IDENTITY.
  v21_require_artefact "stage4 command"      "${s4}.command"      "$EXP_V21_S4_COMMAND_SHA"   "-"
  v21_require_artefact "stage4 exit-code"    "${s4}.exit-code"    "$EXP_V21_S4_EXITCODE_SHA"  "-"
  v21_require_artefact "stage4 stdout"       "${s4}.stdout"       "$EXP_V21_S4_STDOUT_SHA"    "$EXP_V21_S4_STDOUT_BYTES"
  v21_require_artefact "stage4 stderr"       "${s4}.stderr"       "$EXP_V21_S4_STDERR_SHA"    "$EXP_V21_S4_STDERR_BYTES"
  v21_require_artefact "stage4 source-proof" "${s4}.source-proof" "$EXP_V21_SOURCE_PROOF_SHA" "-"
  v21_require_artefact "controller-refresh.after" \
                       "${V21_PROOF_DIR}/controller-refresh.after"     "$EXP_V21_REFRESH_AFTER_SHA"     "-"
  v21_require_artefact "controller-refresh.composite" \
                       "${V21_PROOF_DIR}/controller-refresh.composite" "$EXP_V21_REFRESH_COMPOSITE_SHA" "-"
  v21_require_artefact "isolation-selftest" \
                       "${V21_PROOF_DIR}/isolation-selftest.txt"       "$EXP_V21_ISOLATION_SELFTEST_SHA" "-"
  v21_require_artefact "its own v20-result authentication" \
                       "${V21_PROOF_DIR}/v20-result-authentication.txt" "$EXP_V21_V20_AUTH_SHA" "-"

  # 3. THE RECORDED EXIT CODE AND SOURCE PROOF, READ BACK.
  expect "v21 stage4 exit code"    "$(cat -- "${s4}.exit-code")"    "$EXP_V21_S4_EXIT"
  expect "v21 stage4 source-proof" "$(cat -- "${s4}.source-proof")" "$EXP_V21_SOURCE_PROOF_VALUE"

  # 4. v21 RAN EXACTLY ONE OUTER STAGE, AND IT WAS execute-next-claude-task.
  #    The recorded command artefact is required to name that command and to
  #    name none of Doors 1 to 3.
  if ! grep -q -F -- "$STAGE4_CMD" "${s4}.command"; then
    die "the preserved v21 command artefact does not name ${STAGE4_CMD}:
        ${s4}.command
      Refusing to continue from a run whose single stage is not the one
      recorded."
  fi
  local _door
  for _door in "question-validation" "question-coverage-review" "interview-gate"; do
    if grep -q -F -- "$_door" "${s4}.command"; then
      die "the preserved v21 command artefact names ${_door}. v21 is recorded as
      a Stage-4-only run, and a command artefact naming a Door contradicts the
      evidence this continuation rests on. Refusing to continue."
    fi
  done

  # 5. THE STAGE-4 STOP, PROVED AS A STOP AND NOT AS A CRASH.
  #
  #    v20's Stage 4 produced NO report. v21's produced a complete one. A
  #    non-empty stdout is therefore load-bearing evidence in its own right.
  if [ "$(bytes_of "${s4}.stdout")" = "0" ]; then
    die "the preserved v21 Stage-4 stdout is EMPTY. A fail-closed stop writes a
      machine report; an empty stdout is a crash. That is not the recorded v21
      result. Refusing to continue."
  fi

  # 6. THE CONTROLLER'S OWN TOP-LEVEL STAGE-4 FACTS, READ BACK FROM ITS REPORT.
  v21_require_field "stage4" "${s4}.stdout" "ok"                                  "$EXP_V21_S4_OK"
  v21_require_field "stage4" "${s4}.stdout" "stop_reason"                         "$EXP_V21_S4_STOP_REASON"
  v21_require_field "stage4" "${s4}.stdout" "preparation_ok"                      "$EXP_V21_S4_PREPARATION_OK"
  v21_require_field "stage4" "${s4}.stdout" "piece3_interview_gate_enforced"      "$EXP_V21_S4_PIECE3_ENFORCED"
  v21_require_field "stage4" "${s4}.stdout" "piece3_interview_gate_unlocked"      "$EXP_V21_S4_PIECE3_UNLOCKED"
  v21_require_field "stage4" "${s4}.stdout" "correction_rounds_started"           "$EXP_V21_S4_ROUNDS_STARTED"
  v21_require_field "stage4" "${s4}.stdout" "correction_rounds_completed"         "$EXP_V21_S4_ROUNDS_COMPLETED"
  v21_require_field "stage4" "${s4}.stdout" "total_claude_invocations"            "$EXP_V21_S4_CLAUDE_INVOCATIONS"
  v21_require_field "stage4" "${s4}.stdout" "total_codex_design_audit_invocations" "$EXP_V21_S4_CODEX_AUDITS"
  v21_require_field "stage4" "${s4}.stdout" "correction_round_limit"              "$EXP_V21_S4_ROUND_LIMIT"
  v21_require_field "stage4" "${s4}.stdout" "ness_question_asked"                 "$EXP_V21_S4_NESS_QUESTION_ASKED"
  v21_require_field "stage4" "${s4}.stdout" "piece3_route"                        "$EXP_V21_S4_PIECE3_ROUTE"
  v21_require_field "stage4" "${s4}.stdout" "acceptance_or_adoption_claimed"      "$EXP_V21_S4_ACCEPTANCE_CLAIMED"

  # 7. THE ROUND-3 FACTS THAT LIVE INSIDE correction_history, AS EXACT NEEDLES.
  v21_require_needle "round-3 stop marker"          "${s4}.stdout" "$EXP_V21_R3_STOP_MARKER"
  v21_require_needle "round-3 stop verified"        "${s4}.stdout" "$EXP_V21_R3_STOP_VERIFIED"
  v21_require_needle "round-3 stop classification"  "${s4}.stdout" "$EXP_V21_R3_STOP_CLASS"
  v21_require_needle "round-3 specification digest" "${s4}.stdout" "$EXP_V21_R3_SPEC_SHA"
  v21_require_needle "round-3 review signal null"   "${s4}.stdout" "$EXP_V21_R3_REVIEW_SIGNAL"
  v21_require_needle "round-3 blocking finding 1"   "${s4}.stdout" "$EXP_V21_R3_FINDING1"
  v21_require_needle "round-3 blocking finding 2"   "${s4}.stdout" "$EXP_V21_R3_FINDING2"

  V21_RESULT_AUTHENTICATED="PASS"
  note "the completed v21 Stage-4 result authenticates: exit 1, a real report, CLAUDE_SPECIFICATION_STOP"
  note "v21 ran exactly one outer stage and it was ${STAGE4_CMD}; no Door appears in its command artefact"

  if [ -d "$PROOF" ]; then
    {
      printf 'COMPLETED v21 RESULT AUTHENTICATION\n'
      printf '  proof directory           %s\n' "$V21_PROOF_DIR"
      printf '  predecessor launcher      %s\n' "$LAUNCHER_V21_BASENAME"
      printf '  predecessor sha256        %s\n' "$EXP_LAUNCHER_V21_SHA"
      printf '\n'
      printf '  stage4 execute-next-claude-task exit %s  source-proof %s\n' \
             "$EXP_V21_S4_EXIT" "$EXP_V21_SOURCE_PROOF_VALUE"
      printf '    stdout %s bytes -- a real machine report, NOT a crash\n' "$EXP_V21_S4_STDOUT_BYTES"
      printf '    ok false, stop_reason CLAUDE_SPECIFICATION_STOP\n'
      printf '    preparation_ok true\n'
      printf '    piece3_interview_gate_enforced true, piece3_interview_gate_unlocked true\n'
      printf '    correction_rounds_started 3, correction_rounds_completed 2\n'
      printf '    total_claude_invocations 1, total_codex_design_audit_invocations 1\n'
      printf '    correction_round_limit 5 (controller-owned)\n'
      printf '    ness_question_asked false, piece3_route null\n'
      printf '\n'
      printf '  ROUND 3, from correction_history (exact recorded lines):\n'
      printf '    %s\n' "$EXP_V21_R3_STOP_MARKER"
      printf '    %s\n' "$EXP_V21_R3_STOP_VERIFIED"
      printf '    %s\n' "$EXP_V21_R3_STOP_CLASS"
      printf '    %s\n' "$EXP_V21_R3_SPEC_SHA"
      printf '    %s\n' "$EXP_V21_R3_REVIEW_SIGNAL"
      printf '    blocking finding 1: %s\n' "$EXP_V21_R3_FINDING1"
      printf '    blocking finding 2: %s\n' "$EXP_V21_R3_FINDING2"
      printf '\n'
      printf 'THESE FACTS WERE PROVED FROM THE PRESERVED v21 ARTEFACTS, TWICE:\n'
      printf 'by exact frozen sha256 and byte count, and by re-reading the\n'
      printf 'controller\047s own reported fields and exact recorded lines out of\n'
      printf 'those same artefacts. No v21 stage was rerun, nothing was\n'
      printf 'regenerated, nothing was reinterpreted, and the v21 lab was never\n'
      printf 'written to.\n'
      printf '\n'
      printf 'NOTHING FROM ROUND 3 WAS PROMOTED. That is not taken from this\n'
      printf 'report: it is proved separately, by the continuation source itself\n'
      printf 'carrying exactly the three-candidate chain v1_0 -> v1_1 -> v1_2 and\n'
      printf 'no v1_3, under the frozen whole-workspace manifest.\n'
      printf 'V21_RESULT_AUTHENTICATED = %s\n' "$V21_RESULT_AUTHENTICATED"
    } > "${PROOF}/v21-result-authentication.txt" 2>/dev/null || true
  fi
}

# --------------------------------------------------------------------------
# SECTION 4b4 — THE CONTINUATION SOURCE, AND THE CLEARANCE IT CARRIES
#                                                              (NEW IN v21)
# --------------------------------------------------------------------------
#
# v24 continues the exact state the Repair-27B CLAUDE_SPECIFICATION_STOP
# happened in, and that state
# is worth exactly as much as the proof that it IS that state. This gate
# establishes it in five escalating steps, and every one of them fails the run
# CLOSED, long before the isolation self-test and therefore long before any
# possible provider or model call:
#
#   1. SHAPE. The preserved v21 lab and the continuation source inside it exist,
#      are real directories, and are not symlinks. A symlink here could redirect
#      the rsync SOURCE and silently seed the run from somewhere else entirely.
#
#   2. IDENTITY. The journal, journal head, authenticity key and v21 shadow
#      marker match the exact sha256 / byte / line / event counts frozen in
#      section 0, AND the continuation controller is the EXACT accepted
#      Repair-27B file.
#
#   3. THE CLEARANCE. The journal holds exactly nine events; event 9 is the LAST
#      one; and the digests, the routed signal, the standing target, the package
#      scope and the validation set occur exactly the frozen number of times.
#
#   4. AUTHENTICITY. The whole nine-event chain and the journal head AUTHENTICATE
#      under the semantics of the controller that is about to read them -- the
#      accepted Repair-28 candidate's own event digest, its HMAC over its own
#      canonical authentication material, its sequence and previous-digest
#      chaining, and its head authentication. Step 3 without step 4 would accept a
#      forged or hand-edited event that happened to carry the right strings.
#
#   5. THE COMPLETE WORKSPACE. Every entry beneath the continuation source --
#      every ordinary N.H source and design file, every directory, every
#      permission mode and its Git metadata -- matches the canonical manifest
#      frozen in section 0.
#
# WHAT THIS GATE DELIBERATELY DOES NOT DO.
#   It does not classify anything. It does not decide whether any signal is
#   settled, mechanical, dependent or genuinely open. It does not convert
#   anything into a question, does not answer one, and does not read any title or
#   evidence text at any point. Only identifiers and digests are compared.
#
#   AND IT DOES NOT COMPARE THE CONTINUATION SOURCE TO ANYTHING ELSE. Not to the
#   v10 lineage seed, and not to today's real workspace. Those are separately
#   frozen, separately proved facts, and this launcher never compares any two of
#   the three on any path.
#
# WHY THE CONTROLLER'S OWN CODE, AND NOT A REIMPLEMENTATION HERE.
#   A second implementation of the authentication rule is exactly the "parallel
#   gate" mistake this project refuses everywhere else: it would drift, and a
#   drifted verifier that says PASS is worse than no verifier. The accepted
#   Repair-28 candidate is imported READ-ONLY as a module and its own functions
#   are called. It is never executed as a program here, no provider is contacted,
#   and nothing is written.
#
# WHY -B AND PYTHONDONTWRITEBYTECODE ARE LOAD-BEARING.
#   An ordinary import would rewrite a .pyc inside the PROTECTED controller
#   directory. That is a real write to the protected original and it would fail
#   the controller-bytecode gate. Both are set, and the bytecode is proved
#   UNCHANGED across the import rather than the flags being trusted.
assert_continuation_source() {
  # 1. SHAPE.
  if [ -L "$PRESERVED_LAB_REPAIR27B_V21" ]; then
    die "the preserved v21 lab is a SYMLINK:
        ${PRESERVED_LAB_REPAIR27B_V21}
      A symlink here could redirect the continuation copy. Refusing to continue."
  fi
  if [ ! -d "$PRESERVED_LAB_REPAIR27B_V21" ]; then
    die "the preserved v21 lab is missing or is not a directory:
        ${PRESERVED_LAB_REPAIR27B_V21}
      It is BOTH the completed v21 evidence and this run's only authorised
      continuation source. Nothing is created to repair it."
  fi
  if [ -L "$CONTINUATION_SOURCE" ]; then
    die "the continuation source workspace is a SYMLINK:
        ${CONTINUATION_SOURCE}
      Refusing to continue."
  fi
  if [ ! -d "$CONTINUATION_SOURCE" ]; then
    die "the continuation source workspace is missing or is not a directory:
        ${CONTINUATION_SOURCE}
      Refusing to continue."
  fi
  if [ -L "$CONT_STATE" ] || [ ! -d "$CONT_STATE" ]; then
    die "the continuation source interview state is missing or is not a real
      directory:
        ${CONT_STATE}
      Refusing to continue."
  fi
  for _cf in "$CONT_JOURNAL" "$CONT_JOURNAL_HEAD" "$CONT_AUTH_KEY" "$CONT_LOOP"; do
    if [ -L "$_cf" ] || [ ! -f "$_cf" ]; then
      die "a continuation source file is missing or is not an ordinary,
      non-symlink file:
        ${_cf}
      Refusing to continue."
    fi
  done
  unset _cf
  note "the preserved v21 lab and its continuation source are real, non-symlink directories"

  # 2. IDENTITY.
  expect "continuation journal sha256" "$(sha_of "$CONT_JOURNAL")"   "$EXP_CONT_JOURNAL_SHA"
  expect "continuation journal bytes"  "$(bytes_of "$CONT_JOURNAL")" "$EXP_CONT_JOURNAL_BYTES"
  expect "continuation journal lines"  "$(wc -l < "$CONT_JOURNAL")"  "$EXP_CONT_JOURNAL_LINES"
  expect "continuation journal events" \
         "$(grep -c '[^[:space:]]' -- "$CONT_JOURNAL" || true)" "$EXP_CONT_JOURNAL_EVENTS"
  expect "continuation journal head sha256"     "$(sha_of "$CONT_JOURNAL_HEAD")" "$EXP_CONT_HEAD_SHA"
  expect "continuation authenticity key sha256" "$(sha_of "$CONT_AUTH_KEY")"     "$EXP_CONT_KEY_SHA"
  expect "continuation v21 shadow marker sha256" \
         "$(sha_of "${CONTINUATION_SOURCE}/${SHADOW_MARKER_NAME}")" "$EXP_CONT_V21_MARKER_SHA"
  expect "continuation authenticated package scope occurrences" \
         "$(grep -c -F -- "$EXP_PKG_SCOPE" "$CONT_JOURNAL" || true)" \
         "$EXP_CONT_PKG_SCOPE_OCCURRENCES"

  # THE KEY IS THE SAME KEY THE LINEAGE SEED CARRIED, AND THAT IS A MEASURED
  # CONTINUITY FACT. The controller only ever appends authenticated events, and
  # no refresh on any path ever touched the key. If these two ever differ, the
  # continuation source is not a descendant of the lineage seed at all.
  expect "continuation key equals the lineage seed key" \
         "$EXP_CONT_KEY_SHA" "$EXP_SEED_KEY_SHA"

  # 2b. THE CONTINUATION SOURCE'S OWN CONTROLLER -- THE EXACT REPAIR-27B FILE.
  #
  # The refresh in section 7b is authorised as a transition between two NAMED
  # identities. If the continuation controller is anything other than the exact
  # accepted Repair-27B file this launcher was frozen against, then whatever the
  # refresh would be replacing is not what this launcher believes it is
  # replacing, and the run is refused rather than guessed at.
  expect "continuation controller sha256 (accepted Repair 27B)" \
         "$(sha_of "$CONT_LOOP")"   "$EXP_CONT_LOOP_SHA"
  expect "continuation controller bytes  (accepted Repair 27B)" \
         "$(bytes_of "$CONT_LOOP")" "$EXP_CONT_LOOP_BYTES"
  expect "continuation controller lines  (accepted Repair 27B)" \
         "$(wc -l < "$CONT_LOOP")"  "$EXP_CONT_LOOP_LINES"
  expect "continuation controller is the accepted Repair-27B identity" \
         "$EXP_CONT_LOOP_SHA" "$EXP_R27B_SHA"

  # 3. THE CLEARANCE -- present exactly the frozen number of times, by identifier
  #    and by digest. These are counts over the journal file, so a duplicated or
  #    planted identifier fails just as loudly as a missing one.
  expect "continuation event 9 digest occurrences" \
         "$(grep -c -F -- "$EXP_CONT_EVENT9_SHA" "$CONT_JOURNAL" || true)" \
         "$EXP_CONT_EVENT9_SHA_OCCURRENCES"
  expect "continuation event 8 digest occurrences" \
         "$(grep -c -F -- "$EXP_CONT_EVENT8_SHA" "$CONT_JOURNAL" || true)" \
         "$EXP_CONT_EVENT8_SHA_OCCURRENCES"
  expect "continuation lineage event 7 digest occurrences" \
         "$(grep -c -F -- "$EXP_SEED_EVENT7_SHA" "$CONT_JOURNAL" || true)" \
         "$EXP_CONT_EVENT7_SHA_OCCURRENCES"
  expect "continuation routed signal occurrences" \
         "$(grep -c -F -- "$EXP_ROUTED_SIGNAL_ID" "$CONT_JOURNAL" || true)" \
         "$EXP_CONT_ROUTED_SIGNAL_OCCURRENCES"
  expect "continuation standing target occurrences" \
         "$(grep -c -F -- "$EXP_STANDING_TARGET_ID" "$CONT_JOURNAL" || true)" \
         "$EXP_CONT_STANDING_TARGET_OCCURRENCES"
  expect "continuation validation set occurrences" \
         "$(grep -c -F -- "$EXP_CONT_EVENT9_VALIDATION_SET_ID" "$CONT_JOURNAL" || true)" \
         "$EXP_CONT_VALIDATION_SET_OCCURRENCES"

  # 4. AUTHENTICITY -- the controller's own digest, HMAC, chain and head rules.
  #
  # Not one identifier above is trusted because the string is there. This step is
  # what makes the carried-forward Doors-1-to-3 clearance evidence rather than
  # text.
  assert_controller_bytecode_frozen "before the continuation-source authentication step"
  local cont_auth_out cont_auth_rc=0
  set +e
  cont_auth_out="$(
    PYTHONDONTWRITEBYTECODE=1 "$PY3" -B -c "$SEED_AUTH_CHECKER" \
      "$R28_CANDIDATE" \
      "$CONT_STATE" \
      "$EXP_CONT_JOURNAL_EVENTS" \
      "type=${EXP_CONT_EVENT9_TYPE}" \
      "package_scope_id=${EXP_PKG_SCOPE}" \
      "validation_set_id=${EXP_CONT_EVENT9_VALIDATION_SET_ID}" \
      "event_sha256=${EXP_CONT_EVENT9_SHA}" \
      "prev_event_sha256=${EXP_CONT_EVENT8_SHA}" 2>&1
  )"
  cont_auth_rc=$?
  set -e
  assert_controller_bytecode_frozen "after the continuation-source authentication step"

  if [ -d "$PROOF" ]; then
    {
      printf 'continuation_source %s\n' "$CONTINUATION_SOURCE"
      printf 'controller_used     %s\n' "$R28_CANDIDATE"
      printf 'controller_sha256   %s\n' "$EXP_R28_SHA"
      printf 'expected_events     %s\n' "$EXP_CONT_JOURNAL_EVENTS"
      printf 'checker_status      %s\n' "$cont_auth_rc"
      printf 'checker_output\n%s\n' "$cont_auth_out"
    } > "${PROOF}/continuation-source-authentication.txt" 2>/dev/null || true
  fi

  if [ "$cont_auth_rc" -ne 0 ] \
     || ! printf '%s' "$cont_auth_out" | grep -q '^REGRESSION_SOURCE_AUTHENTICATED$'; then
    die "the continuation source did NOT authenticate under the controller's own
      journal semantics (status ${cont_auth_rc}):
${cont_auth_out}
      The carried-forward Doors-1-to-3 clearance is not proved to be the state
      v20 left. Nothing is repaired, reconstructed or replaced here, and no Door
      is rerun to manufacture a new one. Refusing to continue."
  fi
  note "the nine-event continuation source authenticates under the controller's own semantics"
  note "event 9 is the recorded question-coverage-review clearance v20's Stage 2 produced"
  note "the routed review signal ${EXP_ROUTED_SIGNAL_ID} is carried forward unchanged"

  # 5. THE COMPLETE CONTINUATION WORKSPACE.
  #
  # Steps 2 to 4 prove the INTERVIEW JOURNAL is the authentic post-Doors state.
  # They say nothing about the rest of the workspace, and the rest of the
  # workspace is what execute-next-claude-task actually reads and re-proves. This
  # step proves EVERY entry beneath the continuation source is exactly what this
  # launcher froze.
  if [ -d "$PROOF" ]; then
    assert_continuation_manifest "${PROOF}/continuation-source-manifest.txt"
  else
    assert_continuation_manifest "-"
  fi

  # The continuation-source identity, written as its own standalone artefact so a
  # reader never has to dig it out of a directory of captures.
  if [ -d "$PROOF" ]; then
    {
      printf 'CONTINUATION SOURCE IDENTITY\n'
      printf '  path                    %s\n' "$CONTINUATION_SOURCE"
      printf '  mode                    %s\n' "$CONTINUATION_SOURCE_MODE"
      printf '  journal sha256          %s\n' "$EXP_CONT_JOURNAL_SHA"
      printf '  journal bytes           %s\n' "$EXP_CONT_JOURNAL_BYTES"
      printf '  journal events          %s\n' "$EXP_CONT_JOURNAL_EVENTS"
      printf '  head sha256             %s\n' "$EXP_CONT_HEAD_SHA"
      printf '  authenticity key sha256 %s\n' "$EXP_CONT_KEY_SHA"
      printf '  v21 shadow marker sha256 %s\n' "$EXP_CONT_V21_MARKER_SHA"
      printf '  routed signal id        %s\n' "$EXP_ROUTED_SIGNAL_ID"
      printf '  standing target id      %s\n' "$EXP_STANDING_TARGET_ID"
      printf '  package scope id        %s\n' "$EXP_PKG_SCOPE"
      printf '  validation set id       %s\n' "$EXP_CONT_EVENT9_VALIDATION_SET_ID"
      printf '  event 9 type            %s\n' "$EXP_CONT_EVENT9_TYPE"
      printf '  event 9 sha256          %s\n' "$EXP_CONT_EVENT9_SHA"
      printf '  controller sha256       %s  (accepted Repair 27B)\n' "$EXP_CONT_LOOP_SHA"
      printf '  controller bytes        %s\n' "$EXP_CONT_LOOP_BYTES"
      printf '  controller lines        %s\n' "$EXP_CONT_LOOP_LINES"
      printf '\n'
      printf 'THIS IS THE COMPLETED v21 SHADOW. IT IS NOT ASSERTED TO EQUAL THE\n'
      printf 'CURRENT REAL WORKSPACE OR THE v10 LINEAGE SEED, AND THIS LAUNCHER\n'
      printf 'NEVER COMPARES ANY TWO OF THE THREE.\n'
      printf 'Its nine-event journal carries the Doors-1-to-3 clearance v20\047s\n'
      printf 'stages 1, 2 and 3 produced and v21 carried through unchanged. That\n'
      printf 'is why v24 does not rerun them,\n'
      printf 'and it is why the journal, its head and the authenticity key are\n'
      printf 'copied forward byte-identically and are never refreshed.\n'
    } > "${PROOF}/continuation-source-identity.txt" 2>/dev/null || true
  fi
}

# assert_continuation_manifest <emit_manifest_path|->
#
# THE WHOLE-CONTINUATION-WORKSPACE GATE. It runs at every point
# assert_continuation_source runs: as a precondition before the lab exists, again
# once the proof directory exists so the artefact is recorded, and again under
# both original locks immediately before the copy. All three are before the
# isolation self-test and therefore before any possible provider or model call.
#
# It REPAIRS NOTHING. There is no retry, no fallback and no recovery path: the
# only outcomes are proven and BLOCKED.
assert_continuation_manifest() {
  local emit_manifest="$1"
  local cont_out cont_rc=0
  set +e
  cont_out="$(
    PYTHONDONTWRITEBYTECODE=1 "$PY3" -B -c "$HIST_SEED_PROOF" \
      "$CONTINUATION_SOURCE" \
      "$EXP_CONT_MANIFEST_SHA" \
      "$EXP_CONT_MANIFEST_ENTRIES" \
      "$EXP_CONT_MANIFEST_FILES" \
      "$EXP_CONT_MANIFEST_DIRS" \
      "$EXP_CONT_MANIFEST_SYMLINKS" \
      "UNUSED-IN-FROZEN-MODE" \
      "0" \
      "UNUSED-IN-FROZEN-MODE" \
      "0" \
      "$emit_manifest" \
      "-" \
      "frozen" 2>&1
  )"
  cont_rc=$?
  set -e

  if [ "$cont_rc" -ne 0 ] \
     || ! printf '%s' "$cont_out" | grep -q '^CONTINUATION_SOURCE_MANIFEST_PROVEN$'; then
    die "THE COMPLETE CONTINUATION SOURCE DID NOT PROVE AGAINST ITS FROZEN
      MANIFEST (status ${cont_rc}):
${cont_out}
      The journal, head, key and controller identities are not enough on their
      own: execute-next-claude-task reads and re-proves the actual N.H source
      files, so an ordinary changed source file inside the continuation source
      changes what is being continued.
      NOTHING IS REPAIRED HERE. The v21 lab is not normalised, no expectation is
      recomputed, and no Door is rerun. Refusing to continue."
  fi
  note "the complete continuation workspace matches the manifest frozen into this launcher"
}

# --------------------------------------------------------------------------
# SECTION 4c — DELIBERATELY EMPTY
# --------------------------------------------------------------------------
#
# v11 carried a CURRENT-SOURCE COMPATIBILITY GATE here. It required the preserved
# seed to be byte-identical to the entire current real workspace apart from six
# classified differences, and it existed to stop a continuation running stale
# source.
#
# IT IS REMOVED IN v12 AND IS NOT REPLACED BY ANYTHING WEAKER.
#
# Its claim is no longer true. Since v11 ran, Ness has made unrelated legitimate
# N.H-GOVERNANCE work -- the Unreal Engine 5 Wonder runtime design commit and its
# follow-up permissions fix -- and re-freezing that gate would either force a
# false assertion into this launcher or require loosening it until it proved
# nothing. Both were rejected.
#
# WHAT REPLACES IT IS TWO SEPARATE, TRUE STATEMENTS:
#   A. section 4b proves the regression source IS the exact authenticated
#      historical snapshot;
#   B. section 4e proves the CURRENT REAL WORKSPACE still matches what this
#      launcher froze when it was constructed, and sections 7, 11 and 12 prove it
#      unchanged before, during, after every stage and finally from outside the
#      Bubblewrap namespace.
#
# NEITHER STATEMENT IMPLIES THE OTHER, AND v12 NEVER ASSERTS THAT IT DOES. The
# historical snapshot is the regression INPUT. Today's real workspace is the
# protected ORIGINAL. They are intentionally not asserted to be identical, and no
# code path anywhere in this file compares one against the other.

# --------------------------------------------------------------------------
# SECTION 4d — THE NEW-COPY CONTROLLER REFRESH
# --------------------------------------------------------------------------
#
# THE ONLY WRITE THIS LAUNCHER MAKES INTO THE NEW SHADOW BEFORE THE MARKER.
#
# The continuation source was run with the accepted Repair-27B controller, which
# it proves by digest. This launcher must therefore NOT simply run the
# byte-for-byte v21 shadow unchanged -- that would reproduce the Repair-27B
# CLAUDE_SPECIFICATION_STOP again and would test nothing Repair 28 changed --
# and must NOT copy the real
# workspace instead, which would discard the nine-event Doors-1-to-3 clearance
# with it. (The real controller's own generation name is deliberately not asserted
# anywhere: see the EXP_LOOP_* note in section 0. Only its digest is proved, and
# it is never a refresh source or destination on any path.)
#
# So exactly one path in the NEW COPY is replaced, and four separate proofs
# bracket it. Each of them fails the run CLOSED, and all four happen before the
# marker is placed and therefore long before anything enters Bubblewrap and long
# before any possible provider call:
#
#   BEFORE     the new copy's controller is the EXACT accepted Repair-27B file.
#   AFTER      the refreshed file is the EXACT accepted Repair-28 identity --
#              sha256, byte count AND line count. A short read, a truncated write
#              or a substituted source all fail here.
#   COMPOSITE  the new copy differs from the continuation source in EXACTLY
#              controller/nh_loop.py and in NO other path, compared by content at
#              every depth. This is what proves "only the controller was
#              refreshed" instead of merely asserting it.
#   PRESERVED  the new copy's interview journal, journal head and authenticity
#              key are still byte-identical to the continuation source's
#              nine-event state, and still carry event 9 exactly once.
#
# WHAT IS NEVER REFRESHED. The interview journal, the journal head, the
# authenticity key, the candidates, the NH-GOVERNANCE tree, its Git metadata, any
# source package, and every launcher file. The composite proof is what makes that
# list enforceable rather than aspirational. NOTHING IS EVER COPIED BACK.
#
# THE REFRESH SOURCE IS THE ACCEPTED REPAIR-27B CANDIDATE, OPENED READ-ONLY.
#
# WHAT IS ACTUALLY TRUE HERE:
#   * ${R27B_CANDIDATE} is the ONLY copy source. It is opened read-only, never
#     written, never renamed and never chmod-ed, and its identity has already
#     been asserted twice -- once as a precondition and once under both original
#     locks -- before this function is ever called.
#   * ${CTRL}/nh_loop.py, the REAL controller, appears in this function ONLY as
#     an identity that is RE-ASSERTED UNCHANGED, at the moment of the copy and
#     again immediately after it. It is never a copy source here, never a copy
#     destination anywhere, and is never opened for writing on any path.
#   * ${R27A_CANDIDATE} is preserved repair evidence. It is re-asserted unchanged
#     at the moment of the copy and again afterwards, and it is never copied.
#
# NEITHER THE CONTINUATION SOURCE NOR THE LINEAGE SEED IS EVER WRITTEN TO. The
# write target below is ${SHADOW_WS}, which is the new disposable lab. Both
# sources are re-read and proved unmoved immediately afterwards, each by name, in
# its own proof artefact.

# The content-difference comparator. It compares two trees by PATH, SHAPE and
# CONTENT at every depth.
#
# In v12 it has EXACTLY ONE caller: the composite new-copy-vs-seed proof. v11
# used the same code for a second purpose -- comparing the seed against the real
# workspace -- and that caller is gone.
#
# It compares CONTENT, not timestamps. mtime, atime and ctime necessarily differ
# between an original and a copy taken later, and comparing them would make this
# proof fire on every run for no reason.
readonly TREE_COMPARATOR='
import hashlib, os, stat, sys

left_root = sys.argv[1]
right_root = sys.argv[2]
left_label = sys.argv[3]
right_label = sys.argv[4]
allow_left_only = set()
allow_right_only = set()
allow_differs = set()
allow_differs_exact = {}
for item in sys.argv[5:]:
    parts = item.split(":")
    role = parts[0]
    if role == "LEFT_ONLY" and len(parts) == 2:
        allow_left_only.add(parts[1])
    elif role == "RIGHT_ONLY" and len(parts) == 2:
        allow_right_only.add(parts[1])
    elif role == "DIFFERS" and len(parts) == 2:
        allow_differs.add(parts[1])
    elif role == "DIFFERS_EXACT" and len(parts) == 4:
        allow_differs_exact[parts[1]] = (parts[2], parts[3])
    else:
        sys.stdout.write("unknown or malformed allowance %s\n" % item)
        sys.exit(2)

def digest_of(path):
    sha = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            chunk = handle.read(1048576)
            if not chunk:
                break
            sha.update(chunk)
    return sha.hexdigest()

def raise_error(exc):
    raise exc

def walk(root):
    # os.walk SILENTLY treats a missing or unreadable root as an empty tree and
    # swallows every traversal error underneath it. Two silently-empty walks
    # would compare EQUAL and this proof would report a refresh that never
    # happened as clean. Both are closed here: the root must be a real directory,
    # and onerror re-raises instead of skipping.
    if not os.path.isdir(root):
        raise OSError("not a directory: %s" % root)
    entries = {}
    for base, dirs, files in os.walk(root, onerror=raise_error):
        dirs.sort()
        files.sort()
        for name in dirs + files:
            path = os.path.join(base, name)
            rel = os.path.relpath(path, root)
            info = os.lstat(path)
            if stat.S_ISLNK(info.st_mode):
                entries[rel] = ("symlink", os.readlink(path))
            elif stat.S_ISDIR(info.st_mode):
                entries[rel] = ("dir", "")
            elif stat.S_ISREG(info.st_mode):
                entries[rel] = ("file", digest_of(path))
            else:
                entries[rel] = ("special", "")
    return entries

try:
    left = walk(left_root)
    right = walk(right_root)
except OSError as exc:
    sys.stdout.write("TRAVERSAL-FAILED %s\n" % exc)
    sys.exit(2)

unexplained = []
for rel in sorted(set(left) | set(right)):
    in_left = rel in left
    in_right = rel in right
    if in_left and in_right and left[rel] == right[rel]:
        continue
    if in_left and not in_right:
        if rel not in allow_left_only:
            unexplained.append("%s-ONLY   %s" % (left_label, rel))
    elif in_right and not in_left:
        if rel not in allow_right_only:
            unexplained.append("%s-ONLY   %s" % (right_label, rel))
    elif rel in allow_differs:
        continue
    elif rel in allow_differs_exact:
        # AN EXACT PAIR, NOT A TOLERANCE. The two sides must be regular files
        # carrying exactly the two frozen digests. Anything else -- a drifted
        # controller on either side, a directory, a symlink -- is unexplained.
        want_left, want_right = allow_differs_exact[rel]
        if left[rel] != ("file", want_left) or right[rel] != ("file", want_right):
            unexplained.append(
                "DIFFERS-NOT-THE-AUTHORISED-PAIR  %s  %s=%s:%s  %s=%s:%s"
                % (rel,
                   left_label, left[rel][0], left[rel][1][:16],
                   right_label, right[rel][0], right[rel][1][:16]))
    else:
        unexplained.append("DIFFERS     %s  %s=%s %s=%s" % (rel, left_label, left[rel][1][:16], right_label, right[rel][1][:16]))

missing = []
for rel in sorted(allow_right_only):
    if rel in left or rel not in right:
        missing.append("EXPECTED %s-ONLY DIFFERENCE ABSENT  %s" % (right_label, rel))
for rel in sorted(allow_left_only):
    if rel in right or rel not in left:
        missing.append("EXPECTED %s-ONLY DIFFERENCE ABSENT  %s" % (left_label, rel))
for rel in sorted(allow_differs):
    if rel not in left or rel not in right or left[rel] == right[rel]:
        missing.append("EXPECTED CONTENT DIFFERENCE ABSENT    %s" % rel)
for rel in sorted(allow_differs_exact):
    if rel not in left or rel not in right or left[rel] == right[rel]:
        missing.append("EXPECTED AUTHORISED-PAIR DIFFERENCE ABSENT  %s" % rel)

for line in unexplained:
    sys.stdout.write(line + "\n")
for line in missing:
    sys.stdout.write(line + "\n")

if unexplained:
    sys.exit(1)
if missing:
    sys.exit(3)
sys.stdout.write("TREE_COMPARISON_CLEAN\n")
'

assert_new_copy_before_refresh() {
  local target="${SHADOW_WS}/controller/nh_loop.py"
  if [ -L "$target" ] || [ ! -f "$target" ]; then
    die "the new shadow copy's controller is missing or is not an ordinary,
      non-symlink file:
        ${target}
      Refusing to refresh anything through it."
  fi
  {
    printf 'phase              before-refresh\n'
    printf 'path               %s\n' "$target"
    printf 'sha256             %s\n' "$(sha_of "$target")"
    printf 'bytes              %s\n' "$(bytes_of "$target")"
    printf 'lines              %s\n' "$(wc -l < "$target")"
    printf 'expected_sha256    %s\n' "$EXP_R27B_SHA"
    printf 'expected_bytes     %s\n' "$EXP_R27B_BYTES"
    printf 'expected_lines     %s\n' "$EXP_R27B_LINES"
  } > "${PROOF}/controller-refresh.before"
  expect "new copy controller sha256 BEFORE refresh (accepted Repair 27B)" \
         "$(sha_of "$target")"   "$EXP_R27B_SHA"
  expect "new copy controller bytes  BEFORE refresh (accepted Repair 27B)" \
         "$(bytes_of "$target")" "$EXP_R27B_BYTES"
  expect "new copy controller lines  BEFORE refresh (accepted Repair 27B)" \
         "$(wc -l < "$target")"  "$EXP_R27B_LINES"
  note "the new copy's controller is the exact accepted Repair-27B file the continuation source carried"
}

refresh_new_copy_controller() {
  local target="${SHADOW_WS}/controller/nh_loop.py"
  local staging="${SHADOW_WS}/controller/.nh_loop.py.repair28-refresh"

  # THE REFRESH SOURCE IS THE ACCEPTED REPAIR-28 CANDIDATE, NOT THE REAL
  # CONTROLLER AND NOT ANY EARLIER CANDIDATE. It is asserted immediately, at the
  # moment it is about to be read, and it must be an ordinary non-symlink file: a
  # symlink here could redirect the copy to any file on the system.
  [ -L "$R28_CANDIDATE" ] && die "the accepted Repair-28 candidate is a SYMLINK:
        ${R28_CANDIDATE}
      Refusing to refresh the shadow through it."
  [ -f "$R28_CANDIDATE" ] \
    || die "the accepted Repair-28 candidate is missing at ${R28_CANDIDATE}"
  expect "refresh source sha256 (accepted Repair 28 candidate)" \
         "$(sha_of "$R28_CANDIDATE")"   "$EXP_R28_SHA"
  expect "refresh source bytes  (accepted Repair 28 candidate)" \
         "$(bytes_of "$R28_CANDIDATE")" "$EXP_R28_BYTES"
  expect "refresh source lines  (accepted Repair 28 candidate)" \
         "$(wc -l < "$R28_CANDIDATE")"  "$EXP_R28_LINES"

  # AND EVERY PRESERVED REPAIR CANDIDATE IS RE-ASSERTED UNCHANGED AT THE SAME
  # MOMENT. None of them is the source, and proving them here is what makes "the
  # shadow was refreshed to Repair 27B and to nothing else" measurable rather
  # than merely asserted.
  expect "Repair20B unchanged at refresh (preserved, not the source)" \
         "$(sha_of "$R20B_CANDIDATE")" "$EXP_R20B_SHA"
  expect "Repair21 unchanged at refresh (preserved, not the source)" \
         "$(sha_of "$R21_CANDIDATE")" "$EXP_R21_SHA"
  expect "Repair22 unchanged at refresh (preserved, not the source)" \
         "$(sha_of "$R22_CANDIDATE")" "$EXP_R22_SHA"
  expect "Repair23 unchanged at refresh (preserved, not the source)" \
         "$(sha_of "$R23_CANDIDATE")" "$EXP_R23_SHA"
  expect "Repair24 unchanged at refresh (preserved, not the source)" \
         "$(sha_of "$R24_CANDIDATE")" "$EXP_R24_SHA"
  expect "Repair25 unchanged at refresh (preserved, not the source)" \
         "$(sha_of "$R25_CANDIDATE")" "$EXP_R25_SHA"
  expect "Repair26 unchanged at refresh (preserved, not the source)" \
         "$(sha_of "$R26_CANDIDATE")" "$EXP_R26_SHA"
  expect "Repair27 unchanged at refresh (preserved, not the source)" \
         "$(sha_of "$R27_CANDIDATE")" "$EXP_R27_SHA"
  expect "Repair27A unchanged at refresh (preserved, not the source)" \
         "$(sha_of "$R27A_CANDIDATE")" "$EXP_R27A_SHA"
  expect "Repair27B unchanged at refresh (preserved source-controller, not the source)" \
         "$(sha_of "$R27B_CANDIDATE")" "$EXP_R27B_SHA"

  # AND THE REAL CONTROLLER IS RE-ASSERTED UNCHANGED AT THE SAME MOMENT. It is
  # not the source and it is not the destination; this proves it was not touched
  # by the one write this launcher makes into the shadow.
  expect "real controller sha256 unchanged at refresh" \
         "$(sha_of "${CTRL}/nh_loop.py")"   "$EXP_LOOP_SHA"
  expect "real controller bytes  unchanged at refresh" \
         "$(bytes_of "${CTRL}/nh_loop.py")" "$EXP_LOOP_BYTES"
  expect "real controller lines  unchanged at refresh" \
         "$(wc -l < "${CTRL}/nh_loop.py")"  "$EXP_LOOP_LINES"

  # ATOMIC: staged, then renamed over the target within the same directory, so
  # the target is never observable half-written. A failed copy leaves the staging
  # name behind in the disposable lab and the composite proof below reports it as
  # an unexplained path rather than ignoring it.
  cp -- "$R28_CANDIDATE" "$staging" \
    || die "could not stage the accepted Repair-28 candidate into the new shadow copy:
        ${staging}
      Nothing has been renamed over the new copy's controller."
  chmod 0644 -- "$staging" \
    || die "could not set the mode on the staged Repair-28 candidate: ${staging}"
  mv -f -- "$staging" "$target" \
    || die "could not move the staged Repair-28 candidate into place:
        ${target}"
  CONTROLLER_REFRESH="PERFORMED"
  note "the new copy's controller/nh_loop.py refreshed to the accepted Repair-28 candidate"
}

assert_new_copy_after_refresh() {
  local target="${SHADOW_WS}/controller/nh_loop.py"
  {
    printf 'phase              after-refresh\n'
    printf 'path               %s\n' "$target"
    printf 'source             %s\n' "$R28_CANDIDATE"
    printf 'sha256             %s\n' "$(sha_of "$target")"
    printf 'bytes              %s\n' "$(bytes_of "$target")"
    printf 'lines              %s\n' "$(wc -l < "$target")"
    printf 'expected_sha256    %s\n' "$EXP_R28_SHA"
    printf 'expected_bytes     %s\n' "$EXP_R28_BYTES"
    printf 'expected_lines     %s\n' "$EXP_R28_LINES"
    printf 'real_controller    %s\n' "${CTRL}/nh_loop.py"
    printf 'real_sha256        %s\n' "$(sha_of "${CTRL}/nh_loop.py")"
    printf 'real_expected      %s\n' "$EXP_LOOP_SHA"
    printf 'repair20b_preserved %s\n' "$(sha_of "$R20B_CANDIDATE")"
    printf 'repair21_preserved %s\n' "$(sha_of "$R21_CANDIDATE")"
    printf 'repair22_preserved %s\n' "$(sha_of "$R22_CANDIDATE")"
    printf 'repair23_preserved %s\n' "$(sha_of "$R23_CANDIDATE")"
    printf 'repair24_preserved %s\n' "$(sha_of "$R24_CANDIDATE")"
    printf 'repair25_preserved %s\n' "$(sha_of "$R25_CANDIDATE")"
    printf 'repair26_preserved %s\n' "$(sha_of "$R26_CANDIDATE")"
    printf 'repair27_preserved %s\n' "$(sha_of "$R27_CANDIDATE")"
    printf 'repair27a_preserved %s\n' "$(sha_of "$R27A_CANDIDATE")"
    printf 'repair27b_preserved %s\n' "$(sha_of "$R27B_CANDIDATE")"
  } > "${PROOF}/controller-refresh.after"
  expect "new copy controller sha256 AFTER refresh (accepted Repair 28 candidate)" \
         "$(sha_of "$target")"   "$EXP_R28_SHA"
  expect "new copy controller bytes  AFTER refresh (accepted Repair 28 candidate)" \
         "$(bytes_of "$target")" "$EXP_R28_BYTES"
  expect "new copy controller lines  AFTER refresh (accepted Repair 28 candidate)" \
         "$(wc -l < "$target")"  "$EXP_R28_LINES"
  expect "real controller sha256 unchanged AFTER refresh" \
         "$(sha_of "${CTRL}/nh_loop.py")" "$EXP_LOOP_SHA"
  expect "Repair20B unchanged AFTER refresh (preserved, not the source)" \
         "$(sha_of "$R20B_CANDIDATE")" "$EXP_R20B_SHA"
  expect "Repair21 unchanged AFTER refresh (preserved, not the source)" \
         "$(sha_of "$R21_CANDIDATE")" "$EXP_R21_SHA"
  expect "Repair22 unchanged AFTER refresh (preserved, not the source)" \
         "$(sha_of "$R22_CANDIDATE")" "$EXP_R22_SHA"
  expect "Repair23 unchanged AFTER refresh (preserved, not the source)" \
         "$(sha_of "$R23_CANDIDATE")" "$EXP_R23_SHA"
  expect "Repair24 unchanged AFTER refresh (preserved, not the source)" \
         "$(sha_of "$R24_CANDIDATE")" "$EXP_R24_SHA"
  expect "Repair25 unchanged AFTER refresh (preserved, not the source)" \
         "$(sha_of "$R25_CANDIDATE")" "$EXP_R25_SHA"
  expect "Repair26 unchanged AFTER refresh (preserved, not the source)" \
         "$(sha_of "$R26_CANDIDATE")" "$EXP_R26_SHA"
  expect "Repair27 unchanged AFTER refresh (preserved, not the source)" \
         "$(sha_of "$R27_CANDIDATE")" "$EXP_R27_SHA"
  expect "Repair27A unchanged AFTER refresh (preserved, not the source)" \
         "$(sha_of "$R27A_CANDIDATE")" "$EXP_R27A_SHA"
  expect "Repair27B unchanged AFTER refresh (preserved source-controller, not the source)" \
         "$(sha_of "$R27B_CANDIDATE")" "$EXP_R27B_SHA"
  note "the refreshed shadow controller is the exact accepted Repair-28 identity"
}

# THE COMPOSITE PROOF: ONE PATH CHANGED, AND ONLY ONE.
#
# The allowance list is exactly ONE entry. No source-only allowance, no
# new-copy-only allowance, no other content allowance: at this point the new copy
# still carries the continuation source's own v20 marker, because the v21 marker
# is not placed until after this proof passes. That ordering is required, not
# incidental -- placing the marker first would put a second legitimate difference
# into this comparison and weaken it.
assert_new_copy_differs_only_by_controller() {
  local cmp_out cmp_rc=0
  set +e
  cmp_out="$(
    PYTHONDONTWRITEBYTECODE=1 "$PY3" -B -c "$TREE_COMPARATOR" \
      "$SHADOW_WS" \
      "$CONTINUATION_SOURCE" \
      "NEWCOPY" \
      "SOURCE" \
      "DIFFERS_EXACT:${REFRESH_ALLOWED_EXACT_LOOP}:${EXP_R28_SHA}:${EXP_R27B_SHA}" 2>&1
  )"
  cmp_rc=$?
  set -e

  printf '%s\n' "$cmp_out" > "${PROOF}/controller-refresh.composite" 2>/dev/null || true

  case "$cmp_rc" in
    0)
      if ! printf '%s' "$cmp_out" | grep -q '^TREE_COMPARISON_CLEAN$'; then
        die "the new-copy / continuation-source composite comparison returned
      success without stating it. Refusing to continue on an unreadable result."
      fi
      ;;
    1)
      die "THE CONTROLLER REFRESH CHANGED SOMETHING OTHER THAN nh_loop.py.
${cmp_out}
      The refresh is authorised for exactly one path in the new copy and for no
      other. Everything listed above is outside that authorisation -- an extra
      path, a missing path, a changed journal, a changed head, a changed key, a
      changed candidate, a changed governance file, or a controller that is not
      the exact Repair-28/Repair-27B pair.
      Nothing is reverted or reconciled here. Refusing to continue."
      ;;
    3)
      die "THE CONTROLLER REFRESH DID NOT TAKE EFFECT.
${cmp_out}
      The new copy no longer differs from the continuation source in the one
      place it must. A refresh that left the copy identical to the source would
      rehearse the Repair-27B controller -- the one that stopped at
      CLAUDE_SPECIFICATION_STOP -- while reporting a Repair-28 run."
      ;;
    *)
      die "the new-copy / continuation-source composite comparison could not be
      completed (status ${cmp_rc}):
${cmp_out}
      A comparison that did not finish is not a comparison that passed."
      ;;
  esac
  note "the new copy differs from the continuation source in EXACTLY controller/nh_loop.py"
}

# THE CARRIED-FORWARD CLEARANCE ITSELF, PROVED PRESERVED BY NAME.
#
# The composite proof above already covers these three files. They are proved
# again here, individually and by name, because they are the entire reason a
# Stage-4-only continuation is legitimate: a reader must be able to see "the
# nine-event Doors-1-to-3 journal survived the refresh" as its own verdict, not
# infer it from the absence of a line in a listing of thousands.
assert_new_copy_continuation_state_preserved() {
  local ns="${SHADOW_WS}/nh_interview_state"
  local nj="${ns}/nh_interview_journal.jsonl"
  local nh="${ns}/nh_interview_journal.head"
  local nk="${ns}/nh_interview_authenticity.key"

  for _nf in "$nj" "$nh" "$nk"; do
    if [ -L "$_nf" ] || [ ! -f "$_nf" ]; then
      die "a new-copy interview-state file is missing or is not an ordinary,
      non-symlink file after the controller refresh:
        ${_nf}"
    fi
  done
  unset _nf

  expect "new copy journal sha256 (unchanged by the refresh)" \
         "$(sha_of "$nj")"   "$EXP_CONT_JOURNAL_SHA"
  expect "new copy journal bytes  (unchanged by the refresh)" \
         "$(bytes_of "$nj")" "$EXP_CONT_JOURNAL_BYTES"
  expect "new copy journal events (unchanged by the refresh)" \
         "$(grep -c '[^[:space:]]' -- "$nj" || true)" "$EXP_CONT_JOURNAL_EVENTS"
  expect "new copy journal head sha256 (unchanged by the refresh)" \
         "$(sha_of "$nh")" "$EXP_CONT_HEAD_SHA"
  expect "new copy authenticity key sha256 (unchanged by the refresh)" \
         "$(sha_of "$nk")" "$EXP_CONT_KEY_SHA"
  expect "new copy event 9 digest occurrences (unchanged by the refresh)" \
         "$(grep -c -F -- "$EXP_CONT_EVENT9_SHA" "$nj" || true)" \
         "$EXP_CONT_EVENT9_SHA_OCCURRENCES"
  expect "new copy routed signal occurrences (unchanged by the refresh)" \
         "$(grep -c -F -- "$EXP_ROUTED_SIGNAL_ID" "$nj" || true)" \
         "$EXP_CONT_ROUTED_SIGNAL_OCCURRENCES"
  expect "new copy standing target occurrences (unchanged by the refresh)" \
         "$(grep -c -F -- "$EXP_STANDING_TARGET_ID" "$nj" || true)" \
         "$EXP_CONT_STANDING_TARGET_OCCURRENCES"
  expect "new copy validation set occurrences (unchanged by the refresh)" \
         "$(grep -c -F -- "$EXP_CONT_EVENT9_VALIDATION_SET_ID" "$nj" || true)" \
         "$EXP_CONT_VALIDATION_SET_OCCURRENCES"
  CONTINUATION_STATE="PRESERVED"
  note "the new copy still carries the nine-event Doors-1-to-3 clearance, unaltered"
}

# THE HISTORICAL LINEAGE SEED, RE-READ AND PROVED UNMOVED ACROSS THE REFRESH.
assert_seed_unmoved_after_refresh() {
  {
    printf 'regression_source                %s\n' "$REGRESSION_SOURCE"
    printf 'seed_loop_sha256                 %s\n' "$(sha_of "$SEED_LOOP")"
    printf 'seed_loop_bytes                  %s\n' "$(bytes_of "$SEED_LOOP")"
    printf 'seed_loop_lines                  %s\n' "$(wc -l < "$SEED_LOOP")"
    printf 'seed_journal_sha256              %s\n' "$(sha_of "$SEED_JOURNAL")"
    printf 'seed_head_sha256                 %s\n' "$(sha_of "$SEED_JOURNAL_HEAD")"
    printf 'seed_key_sha256                  %s\n' "$(sha_of "$SEED_AUTH_KEY")"
    printf 'seed_marker_sha256               %s\n' "$(sha_of "${REGRESSION_SOURCE}/${SHADOW_MARKER_NAME}")"
  } > "${PROOF}/regression-seed-unmoved.txt"

  expect "lineage seed controller sha256 AFTER the refresh (still Repair 17)" \
         "$(sha_of "$SEED_LOOP")"   "$EXP_SEED_LOOP_SHA"
  expect "lineage seed controller bytes  AFTER the refresh (still Repair 17)" \
         "$(bytes_of "$SEED_LOOP")" "$EXP_SEED_LOOP_BYTES"
  expect "lineage seed journal sha256 AFTER the refresh" \
         "$(sha_of "$SEED_JOURNAL")" "$EXP_SEED_JOURNAL_SHA"
  expect "lineage seed journal head sha256 AFTER the refresh" \
         "$(sha_of "$SEED_JOURNAL_HEAD")" "$EXP_SEED_HEAD_SHA"
  expect "lineage seed authenticity key sha256 AFTER the refresh" \
         "$(sha_of "$SEED_AUTH_KEY")" "$EXP_SEED_KEY_SHA"
  expect "lineage seed v10 shadow marker sha256 AFTER the refresh" \
         "$(sha_of "${REGRESSION_SOURCE}/${SHADOW_MARKER_NAME}")" \
         "$EXP_SEED_V10_MARKER_SHA"
  note "the historical lineage seed is unmoved across the controller refresh"
}

# THE CONTINUATION SOURCE, RE-READ AND PROVED UNMOVED ACROSS THE REFRESH.
#
# It is the source side of this run's one rsync and the only state this
# continuation depends on, so it gets its own named proof rather than being one
# unchanged line inside the preserved-artefact sweep.
assert_continuation_source_unmoved_after_refresh() {
  {
    printf 'continuation_source              %s\n' "$CONTINUATION_SOURCE"
    printf 'cont_loop_sha256                 %s\n' "$(sha_of "$CONT_LOOP")"
    printf 'cont_loop_bytes                  %s\n' "$(bytes_of "$CONT_LOOP")"
    printf 'cont_loop_lines                  %s\n' "$(wc -l < "$CONT_LOOP")"
    printf 'cont_journal_sha256              %s\n' "$(sha_of "$CONT_JOURNAL")"
    printf 'cont_head_sha256                 %s\n' "$(sha_of "$CONT_JOURNAL_HEAD")"
    printf 'cont_key_sha256                  %s\n' "$(sha_of "$CONT_AUTH_KEY")"
    printf 'cont_marker_sha256               %s\n' "$(sha_of "${CONTINUATION_SOURCE}/${SHADOW_MARKER_NAME}")"
  } > "${PROOF}/continuation-source-unmoved.txt"

  expect "continuation controller sha256 AFTER the refresh (still Repair 27B)" \
         "$(sha_of "$CONT_LOOP")"   "$EXP_CONT_LOOP_SHA"
  expect "continuation controller bytes  AFTER the refresh (still Repair 27B)" \
         "$(bytes_of "$CONT_LOOP")" "$EXP_CONT_LOOP_BYTES"
  expect "continuation journal sha256 AFTER the refresh" \
         "$(sha_of "$CONT_JOURNAL")" "$EXP_CONT_JOURNAL_SHA"
  expect "continuation journal head sha256 AFTER the refresh" \
         "$(sha_of "$CONT_JOURNAL_HEAD")" "$EXP_CONT_HEAD_SHA"
  expect "continuation authenticity key sha256 AFTER the refresh" \
         "$(sha_of "$CONT_AUTH_KEY")" "$EXP_CONT_KEY_SHA"
  expect "continuation v21 shadow marker sha256 AFTER the refresh" \
         "$(sha_of "${CONTINUATION_SOURCE}/${SHADOW_MARKER_NAME}")" \
         "$EXP_CONT_V21_MARKER_SHA"
  note "the completed v21 continuation source is unmoved across the controller refresh"
}

# --------------------------------------------------------------------------
# SECTION 4e — THE CURRENT REAL WORKSPACE, FROZEN AND GATED
# --------------------------------------------------------------------------
#
# THIS IS FACT B. It has nothing to do with the historical regression source and
# is never compared against it.
#
# Everything asserted here was read from the REAL CURRENT DISK STATE when this
# launcher was constructed. The run REFUSES unless that state is still exactly
# what was frozen. A refusal here is never resolved by resetting, reverting,
# checking out or cleaning anything: if the movement is legitimate, a new
# launcher is frozen against the new real state deliberately.
#
# It must be asserted TWICE: once as a precondition, and again immediately before
# the shadow copy while both original locks are held. Without the second
# assertion the before-proof captured at copy time would silently become the
# accepted baseline for any change made after the first gate, and that changed
# state would then be copied and would pass both the during and the after
# comparisons.
assert_real_controller_is_no_known_candidate() {
  # Every controller generation this file holds a digest for, by name. Repair 17
  # comes from the seed; Repair 19B from the preserved v13 lab's own path; the
  # rest from the frozen candidate constants. "Repair 20" is deliberately absent
  # because no digest for it exists here -- an unknown name is not checkable and
  # is not asserted anywhere in this launcher.
  local known name dig
  known=(
    "Repair 17:${EXP_SEED_LOOP_SHA}"
    "Repair 19B:235885af469a6b5f3f428d206c77072712ef4b8d68caa37acf43445fc321bf02"
    "Repair 20B:${EXP_R20B_SHA}"
    "Repair 21:${EXP_R21_SHA}"
    "Repair 22:${EXP_R22_SHA}"
    "Repair 23:${EXP_R23_SHA}"
    "Repair 24:${EXP_R24_SHA}"
    "Repair 25:${EXP_R25_SHA}"
    "Repair 26:${EXP_R26_SHA}"
    "Repair 27:${EXP_R27_SHA}"
    "Repair 27A:${EXP_R27A_SHA}"
    "Repair 27B:${EXP_R27B_SHA}"
    "Repair 28:${EXP_R28_SHA}"
  )
  for entry in "${known[@]}"; do
    name="${entry%%:*}"
    dig="${entry##*:}"
    if [ "$EXP_LOOP_SHA" = "$dig" ]; then
      die "the real controller ${CTRL}/nh_loop.py has the digest of ${name}:
        ${dig}
      That means a candidate has been installed over the real controller. This
      launcher refuses to rehearse on top of that: nothing is restored, nothing
      is reverted, and the run stops here."
    fi
  done
  unset entry
  note "the real controller is none of the ${#known[@]} controller generations this file knows by digest"
}

assert_frozen_identities() {
  # THE REAL CONTROLLER -- PROTECTED AND NEVER WRITTEN TO. Identified by its
  # exact frozen digest, never by a generation name.
  [ -L "${CTRL}/nh_loop.py" ] && die "the real controller is a SYMLINK: ${CTRL}/nh_loop.py"
  expect "nh_loop.py sha256"  "$(sha_of "${CTRL}/nh_loop.py")"        "$EXP_LOOP_SHA"
  expect "nh_loop.py bytes"   "$(bytes_of "${CTRL}/nh_loop.py")"      "$EXP_LOOP_BYTES"
  expect "nh_loop.py lines"   "$(wc -l < "${CTRL}/nh_loop.py")"       "$EXP_LOOP_LINES"

  # AND IT IS NONE OF THE CANDIDATES. Mechanical, not prose: the real
  # controller's digest is compared against every controller generation this
  # file knows a digest for. If it ever equals one, a candidate has been
  # installed over the real controller -- the exact thing every launcher since
  # v1 has promised does not happen -- and the run fails CLOSED here rather than
  # reporting a rehearsal on top of it.
  assert_real_controller_is_no_known_candidate

  # THE REPAIR-20B CANDIDATE -- PRESERVED REPAIR EVIDENCE in v20, not the refresh
  # source. Gated exactly as strictly as the real controller and equally never
  # written to.
  [ -L "$R20B_CANDIDATE" ] && die "the Repair-20B candidate is a SYMLINK: ${R20B_CANDIDATE}"
  [ -f "$R20B_CANDIDATE" ] \
    || die "the Repair-20B candidate is missing from ${CTRL}; it is preserved
      repair evidence and must be present"
  expect "Repair20B candidate sha256" "$(sha_of "$R20B_CANDIDATE")"   "$EXP_R20B_SHA"
  expect "Repair20B candidate bytes"  "$(bytes_of "$R20B_CANDIDATE")" "$EXP_R20B_BYTES"
  expect "Repair20B candidate lines"  "$(wc -l < "$R20B_CANDIDATE")"  "$EXP_R20B_LINES"

  # THE REPAIR-21 CANDIDATE -- PRESERVED REPAIR EVIDENCE in v20, not the refresh
  # source. Gated exactly as strictly as the real controller and equally never
  # written to.
  [ -L "$R21_CANDIDATE" ] && die "the Repair-21 candidate is a SYMLINK: ${R21_CANDIDATE}"
  [ -f "$R21_CANDIDATE" ] \
    || die "the Repair-21 candidate is missing from ${CTRL}; it is preserved
      repair evidence and must be present"
  expect "Repair21 candidate sha256" "$(sha_of "$R21_CANDIDATE")"   "$EXP_R21_SHA"
  expect "Repair21 candidate bytes"  "$(bytes_of "$R21_CANDIDATE")" "$EXP_R21_BYTES"
  expect "Repair21 candidate lines"  "$(wc -l < "$R21_CANDIDATE")"  "$EXP_R21_LINES"

  # THE REPAIR-22 CANDIDATE -- PRESERVED REPAIR EVIDENCE in v20, not the refresh
  # source. Gated exactly as strictly as the real controller and equally never
  # written to.
  [ -L "$R22_CANDIDATE" ] && die "the Repair-22 candidate is a SYMLINK: ${R22_CANDIDATE}"
  [ -f "$R22_CANDIDATE" ] \
    || die "the Repair-22 candidate is missing from ${CTRL}; it is preserved
      repair evidence and must be present"
  expect "Repair22 candidate sha256" "$(sha_of "$R22_CANDIDATE")"   "$EXP_R22_SHA"
  expect "Repair22 candidate bytes"  "$(bytes_of "$R22_CANDIDATE")" "$EXP_R22_BYTES"
  expect "Repair22 candidate lines"  "$(wc -l < "$R22_CANDIDATE")"  "$EXP_R22_LINES"

  # THE REPAIR-23 CANDIDATE -- PRESERVED REPAIR EVIDENCE. Never a refresh source.
  [ -L "$R23_CANDIDATE" ] && die "the Repair-23 candidate is a SYMLINK: ${R23_CANDIDATE}"
  [ -f "$R23_CANDIDATE" ] \
    || die "the Repair-23 candidate is missing from ${CTRL}; it is preserved
      repair evidence and must be present"
  expect "Repair23 candidate sha256" "$(sha_of "$R23_CANDIDATE")"   "$EXP_R23_SHA"
  expect "Repair23 candidate bytes"  "$(bytes_of "$R23_CANDIDATE")" "$EXP_R23_BYTES"
  expect "Repair23 candidate lines"  "$(wc -l < "$R23_CANDIDATE")"  "$EXP_R23_LINES"

  # THE REPAIR-24 CANDIDATE -- PRESERVED REPAIR EVIDENCE. Never a refresh source.
  [ -L "$R24_CANDIDATE" ] && die "the Repair-24 candidate is a SYMLINK: ${R24_CANDIDATE}"
  [ -f "$R24_CANDIDATE" ] \
    || die "the Repair-24 candidate is missing from ${CTRL}; it is preserved
      repair evidence and must be present"
  expect "Repair24 candidate sha256" "$(sha_of "$R24_CANDIDATE")"   "$EXP_R24_SHA"
  expect "Repair24 candidate bytes"  "$(bytes_of "$R24_CANDIDATE")" "$EXP_R24_BYTES"
  expect "Repair24 candidate lines"  "$(wc -l < "$R24_CANDIDATE")"  "$EXP_R24_LINES"

  # THE ACCEPTED REPAIR-25 CANDIDATE -- PRESERVED REPAIR EVIDENCE in v20, not the
  # refresh source. It WAS v18's refresh source. Gated exactly as strictly as the
  # real controller and equally never written to.
  [ -L "$R25_CANDIDATE" ] && die "the accepted Repair-25 candidate is a SYMLINK: ${R25_CANDIDATE}"
  [ -f "$R25_CANDIDATE" ] \
    || die "the accepted Repair-25 candidate is missing from ${CTRL}; it is preserved
      repair evidence and must be present"
  expect "Repair25 candidate sha256" "$(sha_of "$R25_CANDIDATE")"   "$EXP_R25_SHA"
  expect "Repair25 candidate bytes"  "$(bytes_of "$R25_CANDIDATE")" "$EXP_R25_BYTES"
  expect "Repair25 candidate lines"  "$(wc -l < "$R25_CANDIDATE")"  "$EXP_R25_LINES"

  # THE ACCEPTED REPAIR-26 CANDIDATE -- PRESERVED REPAIR EVIDENCE in v20, not the
  # refresh source. It WAS v19's refresh source. Gated exactly as strictly as the
  # real controller and equally never written to.
  [ -L "$R26_CANDIDATE" ] && die "the accepted Repair-26 candidate is a SYMLINK: ${R26_CANDIDATE}"
  [ -f "$R26_CANDIDATE" ] \
    || die "the accepted Repair-26 candidate is missing from ${CTRL}; it is preserved
      repair evidence and must be present"
  expect "Repair26 candidate sha256" "$(sha_of "$R26_CANDIDATE")"   "$EXP_R26_SHA"
  expect "Repair26 candidate bytes"  "$(bytes_of "$R26_CANDIDATE")" "$EXP_R26_BYTES"
  expect "Repair26 candidate lines"  "$(wc -l < "$R26_CANDIDATE")"  "$EXP_R26_LINES"

  # THE REPAIR-27 CANDIDATE -- PRESERVED REPAIR EVIDENCE. Never a refresh source.
  [ -L "$R27_CANDIDATE" ] && die "the Repair-27 candidate is a SYMLINK: ${R27_CANDIDATE}"
  [ -f "$R27_CANDIDATE" ] \
    || die "the Repair-27 candidate is missing from ${CTRL}; it is preserved
      repair evidence and must be present"
  expect "Repair27 candidate sha256" "$(sha_of "$R27_CANDIDATE")"   "$EXP_R27_SHA"
  expect "Repair27 candidate bytes"  "$(bytes_of "$R27_CANDIDATE")" "$EXP_R27_BYTES"
  expect "Repair27 candidate lines"  "$(wc -l < "$R27_CANDIDATE")"  "$EXP_R27_LINES"

  # THE ACCEPTED REPAIR-27A CANDIDATE -- PRESERVED REPAIR EVIDENCE in v24, and
  # the controller the continuation source carries. It is NOT the refresh source.
  # Gated exactly as strictly as the real controller and equally never written to.
  [ -L "$R27A_CANDIDATE" ] && die "the accepted Repair-27A candidate is a SYMLINK: ${R27A_CANDIDATE}"
  [ -f "$R27A_CANDIDATE" ] \
    || die "the accepted Repair-27A candidate is missing from ${CTRL}; it is preserved
      repair evidence and the identity the continuation source must carry, and it
      must be present"
  expect "Repair27A candidate sha256" "$(sha_of "$R27A_CANDIDATE")"   "$EXP_R27A_SHA"
  expect "Repair27A candidate bytes"  "$(bytes_of "$R27A_CANDIDATE")" "$EXP_R27A_BYTES"
  expect "Repair27A candidate lines"  "$(wc -l < "$R27A_CANDIDATE")"  "$EXP_R27A_LINES"

  # THE ACCEPTED REPAIR-27B CANDIDATE -- THE SOURCE CONTROLLER carried by the v21
  # continuation shadow, and the identity the new copy must equal BEFORE the
  # refresh. It is NOT this run's refresh source and NOT the controller under
  # test; accepted Repair 28 is both. It is gated exactly as strictly as the real
  # controller and is equally never written to, and it is asserted here as a
  # precondition, again under both original locks, and again at the moment it is
  # about to be read.
  [ -L "$R27B_CANDIDATE" ] && die "the accepted Repair-27B candidate is a SYMLINK: ${R27B_CANDIDATE}"
  [ -f "$R27B_CANDIDATE" ] \
    || die "the accepted Repair-27B candidate is missing from ${CTRL}; it is the one
      file this continuation exists to test and must be present"
  expect "Repair27B candidate sha256" "$(sha_of "$R27B_CANDIDATE")"   "$EXP_R27B_SHA"
  expect "Repair27B candidate bytes"  "$(bytes_of "$R27B_CANDIDATE")" "$EXP_R27B_BYTES"
  expect "Repair27B candidate lines"  "$(wc -l < "$R27B_CANDIDATE")"  "$EXP_R27B_LINES"
  expect "Repair28 candidate sha256"  "$(sha_of "$R28_CANDIDATE")"   "$EXP_R28_SHA"
  expect "Repair28 candidate bytes"   "$(bytes_of "$R28_CANDIDATE")" "$EXP_R28_BYTES"
  expect "Repair28 candidate lines"   "$(wc -l < "$R28_CANDIDATE")"  "$EXP_R28_LINES"

  # Launchers v1..v11 are ALL preserved evidence and every one of them is gated
  # by exact identity. None is edited, renamed, moved or deleted by this
  # launcher on any path.
  [ -f "${CTRL}/${LAUNCHER_V1_BASENAME}" ] \
    || die "launcher v1 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v1 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V1_BASENAME}")"   "$EXP_LAUNCHER_V1_SHA"
  expect "launcher v1 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V1_BASENAME}")" "$EXP_LAUNCHER_V1_BYTES"

  [ -f "${CTRL}/${LAUNCHER_V2_BASENAME}" ] \
    || die "launcher v2 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v2 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V2_BASENAME}")"   "$EXP_LAUNCHER_V2_SHA"
  expect "launcher v2 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V2_BASENAME}")" "$EXP_LAUNCHER_V2_BYTES"

  [ -f "${CTRL}/${LAUNCHER_V3_BASENAME}" ] \
    || die "launcher v3 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v3 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V3_BASENAME}")"   "$EXP_LAUNCHER_V3_SHA"
  expect "launcher v3 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V3_BASENAME}")" "$EXP_LAUNCHER_V3_BYTES"

  [ -f "${CTRL}/${LAUNCHER_V4_BASENAME}" ] \
    || die "launcher v4 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v4 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V4_BASENAME}")"   "$EXP_LAUNCHER_V4_SHA"
  expect "launcher v4 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V4_BASENAME}")" "$EXP_LAUNCHER_V4_BYTES"

  [ -f "${CTRL}/${LAUNCHER_V5_BASENAME}" ] \
    || die "launcher v5 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v5 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V5_BASENAME}")"   "$EXP_LAUNCHER_V5_SHA"
  expect "launcher v5 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V5_BASENAME}")" "$EXP_LAUNCHER_V5_BYTES"

  [ -f "${CTRL}/${LAUNCHER_V6_BASENAME}" ] \
    || die "launcher v6 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v6 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V6_BASENAME}")"   "$EXP_LAUNCHER_V6_SHA"
  expect "launcher v6 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V6_BASENAME}")" "$EXP_LAUNCHER_V6_BYTES"

  [ -f "${CTRL}/${LAUNCHER_V7_BASENAME}" ] \
    || die "launcher v7 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v7 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V7_BASENAME}")"   "$EXP_LAUNCHER_V7_SHA"
  expect "launcher v7 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V7_BASENAME}")" "$EXP_LAUNCHER_V7_BYTES"

  [ -f "${CTRL}/${LAUNCHER_V8_BASENAME}" ] \
    || die "launcher v8 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v8 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V8_BASENAME}")"   "$EXP_LAUNCHER_V8_SHA"
  expect "launcher v8 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V8_BASENAME}")" "$EXP_LAUNCHER_V8_BYTES"

  [ -f "${CTRL}/${LAUNCHER_V9_BASENAME}" ] \
    || die "launcher v9 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v9 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V9_BASENAME}")"   "$EXP_LAUNCHER_V9_SHA"
  expect "launcher v9 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V9_BASENAME}")" "$EXP_LAUNCHER_V9_BYTES"

  [ -f "${CTRL}/${LAUNCHER_V10_BASENAME}" ] \
    || die "launcher v10 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v10 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V10_BASENAME}")"   "$EXP_LAUNCHER_V10_SHA"
  expect "launcher v10 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V10_BASENAME}")" "$EXP_LAUNCHER_V10_BYTES"

  # v11 RAN once, against the Repair-18 controller, and its lab holds the exact
  # live failure v12 regressed. It is preserved launcher history, not this file's
  # predecessor, and is gated by identity exactly like v1..v10. v24 never runs it.
  [ -f "${CTRL}/${LAUNCHER_V11_BASENAME}" ] \
    || die "launcher v11 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v11 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V11_BASENAME}")"   "$EXP_LAUNCHER_V11_SHA"
  expect "launcher v11 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V11_BASENAME}")" "$EXP_LAUNCHER_V11_BYTES"

  # v12 was constructed and independently audited, and it was DELIBERATELY NEVER
  # RUN, because that audit found the whole-historical-source gap v13 closed. It
  # is preserved unchanged as blocked historical evidence, not this file's
  # predecessor, and is gated by identity exactly like v1..v11. v24 never runs it.
  [ -f "${CTRL}/${LAUNCHER_V12_BASENAME}" ] \
    || die "launcher v12 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v12 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V12_BASENAME}")"   "$EXP_LAUNCHER_V12_SHA"
  expect "launcher v12 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V12_BASENAME}")" "$EXP_LAUNCHER_V12_BYTES"

  # v13 is preserved launcher history, not this file. It is gated by exact
  # identity like v1..v12. v24 never runs it.
  [ -f "${CTRL}/${LAUNCHER_V13_BASENAME}" ] \
    || die "launcher v13 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v13 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V13_BASENAME}")"   "$EXP_LAUNCHER_V13_SHA"
  expect "launcher v13 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V13_BASENAME}")" "$EXP_LAUNCHER_V13_BYTES"

  # v14 is preserved launcher history, not this file. It is gated by exact
  # identity like v1..v13. v24 never runs it.
  [ -f "${CTRL}/${LAUNCHER_V14_BASENAME}" ] \
    || die "launcher v14 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v14 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V14_BASENAME}")"   "$EXP_LAUNCHER_V14_SHA"
  expect "launcher v14 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V14_BASENAME}")" "$EXP_LAUNCHER_V14_BYTES"

  # v15 RAN once, against the Repair-21 controller, and its lab holds the exact
  # Stage-1 refusal v16 regressed. It is preserved launcher history, not this
  # file's predecessor. It is now gated by exact identity like v1..v14, and that
  # expectation was established from the completed v15 lab's own preserved
  # witnesses rather than from today's filename. v24 never runs it.
  [ -f "${CTRL}/${LAUNCHER_V15_BASENAME}" ] \
    || die "launcher v15 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v15 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V15_BASENAME}")"   "$EXP_LAUNCHER_V15_SHA"
  expect "launcher v15 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V15_BASENAME}")" "$EXP_LAUNCHER_V15_BYTES"

  # v16 was constructed and NEVER RUN. It is preserved launcher history and is
  # gated by exact identity like v1..v15. v24 never runs it.
  [ -f "${CTRL}/${LAUNCHER_V16_BASENAME}" ] \
    || die "launcher v16 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v16 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V16_BASENAME}")"   "$EXP_LAUNCHER_V16_SHA"
  expect "launcher v16 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V16_BASENAME}")" "$EXP_LAUNCHER_V16_BYTES"

  # v17 was constructed and NEVER RUN. It was independently audited and found
  # blocked by two defects v18 corrected, so no v17 lab and no v17 result exist
  # and none is claimed. It is preserved launcher history and is gated by exact
  # identity like v1..v16. v24 never runs it.
  [ -f "${CTRL}/${LAUNCHER_V17_BASENAME}" ] \
    || die "launcher v17 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v17 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V17_BASENAME}")"   "$EXP_LAUNCHER_V17_SHA"
  expect "launcher v17 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V17_BASENAME}")" "$EXP_LAUNCHER_V17_BYTES"

  # v18 RAN, exactly once, against the accepted Repair-25 controller. Its
  # completed lab holds the exact Stage-1 refusal Repair 26 corrects. It is gated
  # by exact identity like v1..v17. v24 never runs it.
  [ -f "${CTRL}/${LAUNCHER_V18_BASENAME}" ] \
    || die "launcher v18 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v18 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V18_BASENAME}")"   "$EXP_LAUNCHER_V18_SHA"
  expect "launcher v18 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V18_BASENAME}")" "$EXP_LAUNCHER_V18_BYTES"

  # v19 RAN, exactly once, against the accepted Repair-26 controller, and it is
  # preserved launcher history rather than this file's predecessor.
  # Its Stages 1-3 passed and its Stage 4 stopped
  # fail-closed with PREPARATION_FAILED; its completed lab holds that exact
  # refusal. It is now gated by exact identity like v1..v18, and that expectation
  # is the identity read from disk when v20 was frozen. v24 never runs it.
  [ -f "${CTRL}/${LAUNCHER_V19_BASENAME}" ] \
    || die "launcher v19 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v19 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V19_BASENAME}")"   "$EXP_LAUNCHER_V19_SHA"
  expect "launcher v19 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V19_BASENAME}")" "$EXP_LAUNCHER_V19_BYTES"

  # v20 is PRESERVED ANCESTOR EVIDENCE AND IT RAN, exactly once, against the
  # accepted Repair-27A controller. Its Stages 1-3 passed and its Stage 4 crashed
  # inside the preparation report; its completed lab holds that exact crash and
  # supplies the Doors-1-to-3 clearance this continuation rests on. It is NOT this
  # file's predecessor (v23 is) and it is NOT this run's continuation source (the
  # completed v21 shadow is). It is now gated by exact identity like v1..v19, and
  # that expectation is the identity read from disk when v21 was frozen.
  # v24 never runs it.
  [ -f "${CTRL}/${LAUNCHER_V20_BASENAME}" ] \
    || die "launcher v20 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v20 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V20_BASENAME}")"   "$EXP_LAUNCHER_V20_SHA"
  expect "launcher v20 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V20_BASENAME}")" "$EXP_LAUNCHER_V20_BYTES"

  # v21 IS THE LAST COMPLETED LIVE RUN AND IT RAN, exactly once, against the
  # accepted Repair-27B controller. Its single Stage 4 stopped fail-closed at
  # CLAUDE_SPECIFICATION_STOP, and its completed lab is this run's continuation
  # source. It is gated by exact identity like v1..v20. v24 never runs it.
  [ -f "${CTRL}/${LAUNCHER_V21_BASENAME}" ] \
    || die "launcher v21 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v21 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V21_BASENAME}")"   "$EXP_LAUNCHER_V21_SHA"
  expect "launcher v21 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V21_BASENAME}")" "$EXP_LAUNCHER_V21_BYTES"

  # v22 is PRESERVED LAUNCHER HISTORY. It was created and audited but NEVER RUN,
  # so it has no lab and no result of its own. It is v23's base, not this file's.
  # It is gated by exact identity like v1..v21. v24 never runs it.
  [ -f "${CTRL}/${LAUNCHER_V22_BASENAME}" ] \
    || die "launcher v22 is missing from ${CTRL}; it is preserved launcher history and must be present"
  expect "launcher v22 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V22_BASENAME}")"   "$EXP_LAUNCHER_V22_SHA"
  expect "launcher v22 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V22_BASENAME}")" "$EXP_LAUNCHER_V22_BYTES"

  # v23 is THIS file's IMMEDIATE BASE. It was created and audited but NEVER RUN,
  # so it has no lab and no result of its own. It is gated by exact identity like
  # v1..v22. v24 never runs it.
  [ -f "${CTRL}/${LAUNCHER_V23_BASENAME}" ] \
    || die "launcher v23 is missing from ${CTRL}; it is this file's audited base and must be present"
  expect "launcher v23 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V23_BASENAME}")"   "$EXP_LAUNCHER_V23_SHA"
  expect "launcher v23 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V23_BASENAME}")" "$EXP_LAUNCHER_V23_BYTES"

  # Launcher v24 is THIS file. It cannot hash-gate on itself, so it is accounted
  # for BY PRESENCE, and it is carried in the before/during/after proof set so any
  # change to it during the run is caught there instead.
  [ -s "${CTRL}/${LAUNCHER_V24_BASENAME}" ] \
    || die "launcher v24 is missing or empty at ${CTRL}/${LAUNCHER_V24_BASENAME}"
  note "all twenty-four launcher artefacts present in ${CTRL}"

  # The controller bytecode, frozen by identity rather than asserted absent.
  assert_controller_bytecode_frozen "in the frozen source gate"

  # The three explained workspace-root directories, frozen by exact shape.
  assert_workspace_special_dirs

  expect "controller branch"  "$(git_ro "$CTRL" rev-parse --abbrev-ref HEAD)" "$EXP_CTRL_BRANCH"
  expect "controller HEAD"    "$(git_ro "$CTRL" rev-parse HEAD)"              "$EXP_CTRL_HEAD"

  # The controller worktree must be EXACTLY these entries and nothing else: the
  # modified nh_loop.py, the twenty-four launcher artefacts, the eleven preserved
  # repair candidates, the gitignored editor file, and the gitignored controller
  # bytecode. Nothing is filtered out.
  #
  # THE v24 LINE IS THE ONLY ADDITION v24 MAKES TO THIS SET. It is this file,
  # untracked exactly as every launcher before it.
  #
  # THE BYTECODE LINE IS NEW IN v12 AND IS DELIBERATE. v11's expected set did not
  # contain it, because the file did not exist when v11 was frozen. It exists
  # now. It is listed here rather than tolerated, and its digest and byte count
  # are additionally gated by assert_controller_bytecode_frozen, so an arbitrary
  # future .pyc cannot pass merely by occupying the same path.
  #
  # NOTE ON THE THREE EXPLAINED WORKSPACE-ROOT DIRECTORIES. None of them appears
  # in this status and none of them could: .agents, .codex and .git sit at the
  # WORKSPACE root, which is outside this repository's worktree entirely. That is
  # exactly why they are gated separately in section 4a.
  #
  # The --ignored mode is load-bearing, and traditional is the only sufficient
  # one. Plain --untracked-files=all omits every gitignored path, so a gate built
  # on it would see neither .claude/settings.local.json nor the bytecode.
  # --ignored=matching would see the directories but COLLAPSE them, so arbitrary
  # ignored children would pass the gate and be copied into the shadow.
  local ctrl_status ctrl_status_expected
  ctrl_status="$(
    git_ro "$CTRL" status --porcelain=v1 --untracked-files=all --ignored=traditional \
      | LC_ALL=C sort
  )"
  ctrl_status_expected="$(
    printf '%s\n' \
      " M nh_loop.py" \
      "!! .claude/settings.local.json" \
      "${CTRL_PYCACHE_STATUS_LINES[@]}" \
      "?? ${LAUNCHER_V1_BASENAME}" \
      "?? ${LAUNCHER_V2_BASENAME}" \
      "?? ${LAUNCHER_V3_BASENAME}" \
      "?? ${LAUNCHER_V4_BASENAME}" \
      "?? ${LAUNCHER_V5_BASENAME}" \
      "?? ${LAUNCHER_V6_BASENAME}" \
      "?? ${LAUNCHER_V7_BASENAME}" \
      "?? ${LAUNCHER_V8_BASENAME}" \
      "?? ${LAUNCHER_V9_BASENAME}" \
      "?? ${LAUNCHER_V10_BASENAME}" \
      "?? ${LAUNCHER_V11_BASENAME}" \
      "?? ${LAUNCHER_V12_BASENAME}" \
      "?? ${LAUNCHER_V13_BASENAME}" \
      "?? ${LAUNCHER_V14_BASENAME}" \
      "?? ${LAUNCHER_V15_BASENAME}" \
      "?? ${LAUNCHER_V16_BASENAME}" \
      "?? ${LAUNCHER_V17_BASENAME}" \
      "?? ${LAUNCHER_V18_BASENAME}" \
      "?? ${LAUNCHER_V19_BASENAME}" \
      "?? ${LAUNCHER_V20_BASENAME}" \
      "?? ${LAUNCHER_V21_BASENAME}" \
      "?? ${LAUNCHER_V22_BASENAME}" \
      "?? ${LAUNCHER_V23_BASENAME}" \
      "?? ${LAUNCHER_V24_BASENAME}" \
      "?? ${R20B_CANDIDATE_BASENAME}" \
      "?? ${R21_CANDIDATE_BASENAME}" \
      "?? ${R22_CANDIDATE_BASENAME}" \
      "?? ${R23_CANDIDATE_BASENAME}" \
      "?? ${R24_CANDIDATE_BASENAME}" \
      "?? ${R25_CANDIDATE_BASENAME}" \
      "?? ${R26_CANDIDATE_BASENAME}" \
      "?? ${R27_CANDIDATE_BASENAME}" \
      "?? ${R27A_CANDIDATE_BASENAME}" \
      "?? ${R27B_CANDIDATE_BASENAME}" \
      "?? ${R28_CANDIDATE_BASENAME}" | LC_ALL=C sort
  )"
  expect "controller worktree" "$ctrl_status" "$ctrl_status_expected"

  # THE REAL CURRENT N.H BRANCH AND HEAD. Re-read for v12, not inherited: v11's
  # ce3a38f4 is three commits behind and is deliberately NOT carried forward.
  expect "N.H branch"         "$(git_ro "$NHGOV" rev-parse --abbrev-ref HEAD)" "$EXP_NH_BRANCH"
  expect "N.H HEAD"           "$(git_ro "$NHGOV" rev-parse HEAD)"              "$EXP_NH_HEAD"

  # The N.H worktree must be EXACTLY these five untracked entries and nothing
  # else. Any SIXTH entry of any kind -- tracked, untracked, ignored, staged,
  # modified or deleted -- fails this gate closed. Nothing is filtered and
  # nothing is accepted merely because it looks harmless.
  #
  # THE UNREAL / WONDER WORK IS NOT IN THIS LIST BECAUSE IT IS COMMITTED. It is a
  # TRACKED file at the frozen HEAD above, so a clean worktree is exactly what
  # proves it is present and unmodified. It is additionally frozen by name
  # immediately below, so this run can state that it did not move as a measured
  # fact rather than as a silence.
  local nh_status nh_status_expected
  nh_status="$(
    git_ro "$NHGOV" status --porcelain=v1 --untracked-files=all --ignored=traditional \
      | LC_ALL=C sort
  )"
  nh_status_expected="$(
    printf '%s\n' \
      "?? 01_AUTHORITATIVE/${AUTH_DD23}" \
      "?? 05_ACTIVE_CANDIDATE/${CAND_V10}" \
      "?? 05_ACTIVE_CANDIDATE/${CAND_V11}" \
      "?? 05_ACTIVE_CANDIDATE/${CAND_V12}" \
      "?? 05_ACTIVE_CANDIDATE/${CAND_DD23}" | LC_ALL=C sort
  )"
  expect "N.H worktree" "$nh_status" "$nh_status_expected"

  expect "candidate v1.0 sha256" "$(sha_of "${CAND_DIR}/${CAND_V10}")"   "$EXP_V10_SHA"
  expect "candidate v1.0 bytes"  "$(bytes_of "${CAND_DIR}/${CAND_V10}")" "$EXP_V10_BYTES"
  expect "candidate v1.1 sha256" "$(sha_of "${CAND_DIR}/${CAND_V11}")"   "$EXP_V11_SHA"
  expect "candidate v1.1 bytes"  "$(bytes_of "${CAND_DIR}/${CAND_V11}")" "$EXP_V11_BYTES"
  expect "candidate v1.2 sha256" "$(sha_of "${CAND_DIR}/${CAND_V12}")"   "$EXP_V12_SHA"
  expect "candidate v1.2 bytes"  "$(bytes_of "${CAND_DIR}/${CAND_V12}")" "$EXP_V12_BYTES"

  expect "decision defaults v2.3 candidate sha256" \
         "$(sha_of "${CAND_DIR}/${CAND_DD23}")"   "$EXP_DD23_CAND_SHA"
  expect "decision defaults v2.3 candidate bytes"  \
         "$(bytes_of "${CAND_DIR}/${CAND_DD23}")" "$EXP_DD23_CAND_BYTES"
  expect "decision defaults v2.3 adopted sha256" \
         "$(sha_of "${AUTH_DIR}/${AUTH_DD23}")"   "$EXP_DD23_AUTH_SHA"
  expect "decision defaults v2.3 adopted bytes"  \
         "$(bytes_of "${AUTH_DIR}/${AUTH_DD23}")" "$EXP_DD23_AUTH_BYTES"

  # THE CURRENT UNREAL / WONDER DESIGN WORK, GATED BY NAME. Not copied anywhere,
  # not reverted, not reset, not deleted. Only read and required to be unmoved.
  [ -f "${NHGOV}/${UNREAL_WONDER_REL}" ] \
    || die "the current Unreal/Wonder design file is missing from the N.H checkout:
        ${NHGOV}/${UNREAL_WONDER_REL}
      It is legitimate current N.H work and this run must witness it unchanged.
      Nothing is restored or checked out here."
  expect "Unreal/Wonder design sha256" \
         "$(sha_of "${NHGOV}/${UNREAL_WONDER_REL}")"   "$EXP_UNREAL_WONDER_SHA"
  expect "Unreal/Wonder design bytes"  \
         "$(bytes_of "${NHGOV}/${UNREAL_WONDER_REL}")" "$EXP_UNREAL_WONDER_BYTES"
  expect "Unreal/Wonder design mode"   \
         "$(mode_of "${NHGOV}/${UNREAL_WONDER_REL}")"  "$EXP_UNREAL_WONDER_MODE"

  # THE REAL INTERVIEW STATE. Still its own five events. It is not the regression
  # source, it is never overlaid into the shadow, and nothing this run produces
  # is ever written back to it.
  expect "journal sha256"  "$(sha_of "$JOURNAL")"          "$EXP_JOURNAL_SHA"
  expect "journal bytes"   "$(bytes_of "$JOURNAL")"        "$EXP_JOURNAL_BYTES"
  expect "journal events"  "$(grep -c '[^[:space:]]' -- "$JOURNAL" || true)" "$EXP_JOURNAL_EVENTS"
  expect "journal head sha256"     "$(sha_of "$JOURNAL_HEAD")" "$EXP_HEAD_SHA"
  expect "authenticity key sha256" "$(sha_of "$AUTH_KEY")"    "$EXP_KEY_SHA"
  expect "authenticated package scope occurrences" \
         "$(grep -c -F -- "$EXP_PKG_SCOPE" "$JOURNAL" || true)" "$EXP_PKG_SCOPE_OCCURRENCES"

  [ -f "$LOCK_TXN" ]     || die "candidate-transaction lock file missing: ${LOCK_TXN}"
  [ -f "$LOCK_JOURNAL" ] || die "interview-journal lock file missing: ${LOCK_JOURNAL}"

  # THE REGRESSION-SOURCE GATE lives INSIDE this function on purpose, so it is
  # asserted on both invocations: once as a precondition -- before the lab
  # exists, before the isolation self-test, and therefore before any possible
  # provider or model call -- and once again under both original locks
  # immediately before the copy. Without the second assertion, a regression
  # source that moved in between would become the accepted baseline and would
  # then be copied and compared only against itself.
  #
  # THERE IS NO SECOND CALL HERE. v11 followed this with a gate comparing the
  # seed to the real workspace. That gate is gone and nothing replaces it.
  assert_regression_source

  # THE COMPLETED v20 RESULT AND THE CONTINUATION SOURCE, both asserted INSIDE
  # this function on purpose, so both are re-asserted on every one of its
  # invocations: once as a precondition -- before the lab exists, before the
  # isolation self-test, and therefore before any possible provider or model call
  # -- and once again under both original locks immediately before the copy.
  # Without the second assertion, a v20 artefact or a continuation source that
  # moved in between would become the accepted baseline and would then be copied
  # and compared only against itself.
  #
  # THE ORDER IS DELIBERATE. The v20 RESULT is authenticated first, because if
  # Doors 1 to 3 did not actually pass then continuing from their state is
  # unjustified whatever that state looks like.
  assert_v20_result_authenticated
  assert_v21_result_authenticated
  assert_continuation_source

  note "every frozen identity matches; the current real source state has not moved"
  note "the completed v20 result authenticates, so Doors 1 to 3 genuinely passed"
  note "the completed v21 result authenticates, so a Stage-4-only continuation is justified"
  note "the continuation source is the authenticated completed v21 shadow"
  note "the lineage seed is the authenticated historical snapshot"
  note "the three are NOT asserted to be identical, and no two were ever compared"
}

step "FROZEN SOURCE IDENTITY"
assert_frozen_identities

# ==========================================================================
# SECTION 5 — CREATE THE LAB
# ==========================================================================

step "LAB"

# The leaf is created WITHOUT -p, so this single mkdir(2) is the real guard and
# not the earlier [ -e ] test.
#
# `mkdir -p` would have made that earlier test the only guard, and a test
# followed by a permissive create is not atomic: between them a concurrent
# launcher could create the same lab and both runs would proceed into it. And a
# symlink planted at that path would be ACCEPTED by `mkdir -p` -- silently
# redirecting every proof write, and the `rsync --delete` below, to wherever the
# symlink pointed, including a preserved lab. `mkdir` without -p fails EEXIST.
mkdir -m 0700 -- "$LAB" || die "could not atomically create the lab:
        ${LAB}
      Either it already exists, or something else occupies that exact path.
      This launcher never reuses and never deletes an earlier lab."
LAB_CREATED=1          # from here on, every failure report must disclose the lab

# And the thing just created must be a real directory, not a symlink to one.
[ -d "$LAB" ] || die "the lab path is not a directory after creation: ${LAB}"
[ ! -L "$LAB" ] || die "the lab path is a symlink; refusing to write through it: ${LAB}"

mkdir -m 0700 -p "${LAB}/shadow" "${LAB}/runtime" "$RUNTIME_TMP" "$PROOF"
chmod 0700 "$LAB"

# EVERY stage artefact is created here, for all four stages, so the watch
# commands printed below actually work the moment they are offered.
#
# The exit-code and timestamp files are pre-seeded with NOT-RUN rather than left
# empty, because an empty file is ambiguous: it reads equally as "the stage has
# not run yet", "the stage ran and wrote nothing" and "the write failed".
# NOT-RUN says which. Section 11 overwrites each the moment its stage runs, so a
# file still reading NOT-RUN at the end is positive evidence that the stage was
# never entered.
for _slug in "${ALL_STAGE_SLUGS[@]}"; do
  : > "${PROOF}/${_slug}.stdout"
  : > "${PROOF}/${_slug}.stderr"
  printf 'NOT-RUN\n' > "${PROOF}/${_slug}.command"
  printf 'NOT-RUN\n' > "${PROOF}/${_slug}.exit-code"
  printf 'NOT-RUN\n' > "${PROOF}/${_slug}.started"
  printf 'NOT-RUN\n' > "${PROOF}/${_slug}.finished"
  printf 'NOT-RUN\n' > "${PROOF}/${_slug}.source-proof"
  chmod 0600 "${PROOF}/${_slug}.stdout"   "${PROOF}/${_slug}.stderr" \
             "${PROOF}/${_slug}.command"  "${PROOF}/${_slug}.exit-code" \
             "${PROOF}/${_slug}.started"  "${PROOF}/${_slug}.finished" \
             "${PROOF}/${_slug}.source-proof"
done
unset _slug
note "lab created atomically (mode 0700): ${LAB}"
say  "        NOTE: the lab will contain a copy of the N.H interview authenticity"
say  "        key, because the controller cannot append authenticated journal"
say  "        events without it. Delete the lab after review."
say  ""
say  "        TO WATCH THIS RUN LIVE, from another terminal, run any of these:"
say  ""
for _slug in "${ALL_STAGE_SLUGS[@]}"; do
  say  "          tail -F ${PROOF}/${_slug}.stderr"
done
unset _slug
say  ""
say  "        Or every stream at once:"
say  ""
say  "          tail -F ${PROOF}/*.stdout ${PROOF}/*.stderr"
say  ""
say  "        The controller writes its live progress to stderr. stdout carries"
say  "        the machine report. Neither stream dumps candidate contents."

# The source gates ran before the lab existed, so their named proof artefacts had
# nowhere to be written. Re-run them now that the proof directory is there, so the
# artefacts exist for the audit. These are pure re-reads of the same read-only
# checks; they write nothing outside the lab and they can only fail closed.
step "HISTORICAL LINEAGE SEED IDENTITY AND AUTHENTICATION (recorded to proof)"
assert_regression_source
note "lineage-seed proof artefacts written to ${PROOF}"

step "COMPLETED v20 RESULT AUTHENTICATION (recorded to proof)"
assert_v20_result_authenticated
note "v20-result authentication artefact written to ${PROOF}"

step "COMPLETED v21 RESULT AUTHENTICATION (recorded to proof)"
assert_v21_result_authenticated
note "v21-result authentication artefact written to ${PROOF}"

step "CONTINUATION SOURCE IDENTITY AND AUTHENTICATION (recorded to proof)"
assert_continuation_source
note "continuation-source proof artefacts written to ${PROOF}"

# ==========================================================================
# SECTION 6 — TAKE BOTH ORIGINAL LOCKS, NON-BLOCKING
# ==========================================================================

step "ORIGINAL LOCKS"

# flock(2) is the same kernel lock primitive the controller takes with
# fcntl.flock, so this genuinely excludes a concurrent controller.
exec 200<"$LOCK_TXN"
flock -n -x 200 || die "the original candidate-transaction lock is held by another process.
      Something else is mid-transaction on the protected original. Refusing to copy."
# Counted the instant it is held, so the die() below -- which can fire while THIS
# lock is held -- reports the truth.
LOCKS_TAKEN=$((LOCKS_TAKEN + 1))
LOCKS_HELD=$((LOCKS_HELD + 1))
note "candidate-transaction lock acquired (non-blocking)"

exec 201<"$LOCK_JOURNAL"
flock -n -x 201 || die "the original interview-journal lock is held by another process.
      Something else is mid-append on the protected original. Refusing to copy."
LOCKS_TAKEN=$((LOCKS_TAKEN + 1))
LOCKS_HELD=$((LOCKS_HELD + 1))
note "interview-journal lock acquired (non-blocking)"

# ==========================================================================
# SECTION 7 — PROOF BEFORE, COPY, VERIFY COPY, REFRESH, PROOF DURING
#             (locks held)
# ==========================================================================

step "ORIGINAL PROOF (BEFORE)"
capture_original_proof "${PROOF}/original.before"
note "before-proof written to ${PROOF}/original.before"

step "FROZEN SOURCE IDENTITY (RE-ASSERTED UNDER LOCK)"
assert_frozen_identities
note "the captured before-proof is the frozen source, not merely self-consistent"

step "CONTINUATION SHADOW COPY (SOURCE: THE COMPLETED v21 SHADOW)"

# THE SOURCE OF THIS COPY IS THE COMPLETED v21 SHADOW WORKSPACE, NOT THE REAL
# WORKSPACE, NOT THE v10 LINEAGE SEED, AND NOT ANY QUESTION-DELIVERY COPY. It is
# the exact state the Repair-27B CLAUDE_SPECIFICATION_STOP happened in, and it carries the
# Doors-1-to-3 clearance in its own nine-event authenticated journal, which is
# the whole reason it is the continuation source.
#
# The real workspace is NOT copied. Its interview journal is NOT overlaid onto
# the copy -- there is no real interview-state overlay anywhere in this file, in
# this copy or in the namespace. The lineage seed is NOT copied. Event 9 is NOT
# replaced. The journal is NOT reset. Real candidate state is NOT copied over the
# source. Neither source is cleaned, normalised or repaired in any way.
#
# EXACTLY ONE FILE IN THE NEW COPY IS TOUCHED AFTER THIS RSYNC, and not until the
# copy has been proved byte-truthful against the seed: controller/nh_loop.py, in
# section 7b immediately below.
#
# The copy is EXACT. Nothing is excluded. Never copied, because they are not in
# the workspace at all: .ssh, .netrc, .config, and the host .codex / .claude,
# which are namespace-only anonymous copy-on-write overlays instead.
#
# All launcher scripts present in the seed ARE copied, because the shadow is a
# truthful copy and they are files in it. They are inert inside the namespace:
# nothing in the rehearsal executes them, and the controller only ever runs git
# against NH-GOVERNANCE, never against controller/.

mkdir -m 0700 -p "$SHADOW_WS"
rsync -aHAX --numeric-ids --delete "${CONTINUATION_SOURCE}/" "${SHADOW_WS}/" \
  || die "rsync copy of the continuation source into the new shadow failed"
note "continuation source copied into ${SHADOW_WS}"

step "CONTINUATION SHADOW COPY VERIFICATION (AGAINST THE SOURCE, BEFORE ANY REFRESH)"

# THIS VERIFICATION HAPPENS BEFORE THE CONTROLLER REFRESH, NOT AFTER IT. The
# order is load-bearing: refreshing first and verifying afterwards would leave the
# initial copy itself unverified, and the composite proof in section 7b would then
# be comparing a refreshed copy against a seed with no established baseline in
# between. Verified first, refreshed second, re-proved third.
#
# Checksum dry-run compare, AGAINST THE CONTINUATION SOURCE -- never against the
# real workspace and never against the lineage seed. Comparing the new shadow to
# either would be wrong on its face: they legitimately differ, and v21 makes no
# claim about how.
#
# The exit STATUS is captured separately and is required to be zero. Discarding it
# with `|| true` would make a killed or otherwise failing dry run
# indistinguishable from a clean one.
set +e
COPY_DIFF="$(rsync -aHAXn --delete --checksum --itemize-changes "${CONTINUATION_SOURCE}/" "${SHADOW_WS}/" 2>&1)"
COPY_RC=$?
set -e
if [ "$COPY_RC" -ne 0 ] || [ -n "$COPY_DIFF" ]; then
  {
    printf 'rsync verification exit status: %s\n' "$COPY_RC"
    printf '%s\n' "$COPY_DIFF"
  } > "${PROOF}/DIFF.shadow-copy.txt"
  die "the continuation shadow could not be proved identical to the preserved v21
      shadow (rsync exit status ${COPY_RC}).
      See ${PROOF}/DIFF.shadow-copy.txt
      Refusing to continue against a copy that is not proved truthful."
fi
note "the new shadow is a byte-truthful copy of the preserved v21 continuation source"

# ==========================================================================
# SECTION 7b — THE REPAIR-27B -> ACCEPTED-REPAIR-28 NEW-COPY CONTROLLER REFRESH
#              (still under both original locks)
# ==========================================================================
#
# Runs here, and only here: after the initial copy has been proved byte-truthful
# against the continuation source, and before the during-proof, the lock release
# and the shadow marker. It is inside the lock window on purpose, so the real controller that is
# read as the refresh source is the same one the under-lock frozen-identity
# assertion just proved, with no window in between, and so the during-proof that
# follows also covers the refresh.

step "NEW-COPY CONTROLLER REFRESH: BEFORE-STATE (must be the exact accepted Repair-27B file)"
assert_new_copy_before_refresh

step "NEW-COPY CONTROLLER REFRESH: REPLACING ONLY controller/nh_loop.py"
refresh_new_copy_controller

step "NEW-COPY CONTROLLER REFRESH: AFTER-STATE (must be the exact accepted Repair-28 file)"
assert_new_copy_after_refresh

step "NEW-COPY CONTROLLER REFRESH: COMPOSITE PROOF (exactly one path changed)"
assert_new_copy_differs_only_by_controller

step "CONTINUATION STATE PRESERVED (nine events, the Doors-1-to-3 clearance intact)"
assert_new_copy_continuation_state_preserved

step "HISTORICAL LINEAGE SEED UNMOVED ACROSS THE REFRESH"
assert_seed_unmoved_after_refresh

step "COMPLETED v21 CONTINUATION SOURCE UNMOVED ACROSS THE REFRESH"
assert_continuation_source_unmoved_after_refresh

step "ORIGINAL PROOF (DURING) — proving the original did not move while copying or refreshing"
capture_original_proof "${PROOF}/original.during"
if ! compare_proof_set "${PROOF}/original.before" "${PROOF}/original.during" "during" \
        "${PROTECTED_PROOF_FILES[@]}"; then
  die "the protected original changed WHILE it was being copied or refreshed.
      The copy is not a coherent snapshot. Refusing to rehearse."
fi
note "protected original unchanged across the whole copy and refresh window"

if ! compare_proof_set "${PROOF}/original.before" "${PROOF}/original.during" "during-labs" \
        "${PRESERVED_LAB_PROOF_FILES[@]}"; then
  die "a preserved earlier lab changed WHILE the shadow was being copied or
      refreshed. Preserved evidence must never move, and that includes the
      completed v11 lab. Refusing to rehearse."
fi
note "preserved earlier labs unchanged across the whole copy and refresh window"

if ! compare_proof_set "${PROOF}/original.before" "${PROOF}/original.during" "during-seed" \
        "${REGRESSION_SEED_PROOF_FILES[@]}"; then
  die "THE HISTORICAL LINEAGE SEED CHANGED WHILE THE SHADOW WAS BEING COPIED OR
      REFRESHED. The lineage root of the state being continued must never move.
      Refusing to continue."
fi
note "the historical lineage seed unchanged across the whole copy and refresh window"

if ! compare_proof_set "${PROOF}/original.before" "${PROOF}/original.during" "during-cont" \
        "${CONTINUATION_SOURCE_PROOF_FILES[@]}"; then
  die "THE CONTINUATION SOURCE OR THE RECORDED v21 RESULT CHANGED WHILE THE
      SHADOW WAS BEING COPIED OR REFRESHED. The completed v21 shadow this whole
      continuation depends on must never move. Refusing to continue."
fi
note "the continuation source and the recorded v21 result unchanged across the whole copy and refresh window"

# ==========================================================================
# SECTION 8 — RELEASE BOTH ORIGINAL LOCKS, THEN PLACE THE MARKER
# ==========================================================================

step "RELEASING ORIGINAL LOCKS"

# Only the lock FILES were copied. Kernel lock ownership is dropped here and is
# never carried into the namespace: these descriptors are closed before bwrap.
# Each count is decremented as its own descriptor closes. Closing the descriptor
# releases the lock unconditionally, so the decrement follows the close rather
# than the flock -u, whose status is not relied upon.
flock -u 200 || true
exec 200<&-
LOCKS_HELD=$((LOCKS_HELD - 1))
flock -u 201 || true
exec 201<&-
LOCKS_HELD=$((LOCKS_HELD - 1))
note "both original locks released; no lock ownership enters the shadow"

# The regression shadow marker. It exists ONLY in a shadow, never in the real
# original, so its presence inside the namespace at the normal N.H path is
# positive proof that the substitution happened and the real workspace is not
# what is mounted.
#
# The continuation source already carries v20's own marker, because it IS a v20
# shadow, so this write OVERWRITES an inherited marker in the NEW lab rather than
# creating a fresh one. Nothing is overwritten in the v20 lab: the target below is
# ${SHADOW_WS}, which is the new disposable lab, and the continuation source
# itself is never opened for writing. The write happens AFTER copy verification
# AND AFTER the whole section 7b refresh proof, so it can never pollute either
# comparison -- both legitimately saw the v20 marker on both sides and matched it.
#
# It sits at the workspace root, outside both Git checkouts, so neither
# repository worktree status is affected.
#
# The token identifies FOUR things: Repair 28, the v24 Stage-4-only
# continuation, the exact accepted Repair-28 controller sha256, and the routed
# signal this rehearsal carries forward. It therefore cannot collide with any
# earlier rehearsal marker, including the v21 marker the continuation source
# carries.
SHADOW_TOKEN="nh-shadow-repair28-continuation-v24-${EXP_R28_SHA}-${EXP_ROUTED_SIGNAL_ID}"
printf '%s\n' "$SHADOW_TOKEN" > "${SHADOW_WS}/${SHADOW_MARKER_NAME}"
printf '%s\n' "$SHADOW_TOKEN" > "${RUNTIME_TMP}/.nh_shadow_tmp_marker"
note "shadow marker placed"

# ==========================================================================
# SECTION 9 — THE BUBBLEWRAP NAMESPACE
# ==========================================================================
#
# ONE NAMESPACE PER CONTROLLER STAGE. Every stage gets the identical argument
# vector, built by this one function, so no stage can be run under weaker
# isolation than the self-test proved.
#
# WHY ONE NAMESPACE PER STAGE IS SAFE. The only controller state that must
# survive from one stage to the next is the shadow's own interview state, and
# that lives inside ${SHADOW_WS}, a real directory in the lab bind-mounted into
# every stage. It persists because it is a real file, not because a namespace
# persisted. What is re-created per stage is the anonymous credential overlay,
# the materialised .claude.json and /run, none of which carries controller state.
# The same-Claude-session requirement is a WITHIN-execute requirement and stage 4
# is one namespace holding one execute, so it is fully preserved.
#
# NOTHING HERE INJECTS, FAKES OR PRE-ANSWERS ANY CONTRACT. Not a question, not a
# validation result, not a coverage clearance, not a gap finding, not a gate
# state, not a design specification, not an audit verdict and not a correction
# result. --clearenv wipes the environment and the ONLY NH_-prefixed variable set
# back for a real stage is NH_LOOP_INTERVIEW_STATE_DIR, which points at the
# shadow's own interview state.
#
# NO REAL N.H INTERVIEW STATE IS OVERLAID. The real journal, head and key are not
# bound in, not copied in, and not reachable: /home/ness is tmpfs and the real
# workspace path is occupied by the shadow bind.
#
# THERE IS NO COPYBACK PATH. Nothing inside the namespace can write to the real
# workspace, to any preserved lab, or to the regression source, because none of
# them is bound in and /home/ness is hidden.
build_bwrap_args() {
  local claude_json_fd="$1"
  BWRAP_ARGS=(
    # --- namespaces ---
    --die-with-parent
    --new-session
    --unshare-all
    --share-net                       # ONLY because real provider calls need it
    --hostname nh-shadow-rehearsal

    # --- host root, read-only ---
    --ro-bind / /
    --proc /proc
    --dev /dev
    --tmpfs /dev/shm

    # --- the real /home/ness disappears completely ---
    # This also puts every preserved lab AND the regression source out of reach:
    # they live under /home/ness and are not among the paths put back below, so
    # nothing inside the namespace can even see them, let alone write to them.
    --tmpfs /home/ness

    # --- put back only what is mechanically required ---
    --ro-bind "${HOME_REAL}/.nvm" "${HOME_REAL}/.nvm"

    # anonymous copy-on-write credential overlays: writable inside, writes land
    # in an invisible tmpfs, the host copies can never be reached
    --overlay-src "$HOST_CODEX"  --tmp-overlay "${HOME_REAL}/.codex"
    --overlay-src "$HOST_CLAUDE" --tmp-overlay "${HOME_REAL}/.claude"

    # .claude.json is materialised from a file descriptor straight into the
    # namespace tmpfs. It is writable inside, it is discarded when the namespace
    # dies, and it is NEVER copied into the persistent lab.
    --perms 0600 --file "$claude_json_fd" "$HOST_CLAUDE_JSON"

    # THE SUBSTITUTION: the shadow appears at the exact canonical path that
    # nh_loop.py hardcodes and resolves with realpath().
    --bind "$SHADOW_WS" "$WS"

    # disposable /tmp, kept in the lab
    --bind "$RUNTIME_TMP" /tmp

    # isolated runtime dirs
    --tmpfs /run
    --perms 0700 --dir /run/user/1000

    # --- environment: cleared, then only the required values ---
    --clearenv
    --setenv HOME "$HOME_REAL"
    --setenv USER ness
    --setenv LOGNAME ness
    --setenv PATH "${NODE_BIN}:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    --setenv LANG C.utf8
    --setenv TERM dumb
    --setenv TMPDIR /tmp
    --setenv XDG_RUNTIME_DIR /run/user/1000
    --setenv CODEX_HOME "${HOME_REAL}/.codex"
    --setenv CLAUDE_CONFIG_DIR "${HOME_REAL}/.claude"
    --setenv NH_LOOP_INTERVIEW_STATE_DIR "${WS}/nh_interview_state"
    --setenv GIT_OPTIONAL_LOCKS 0
    --setenv GIT_CONFIG_NOSYSTEM 1
    --setenv GIT_CONFIG_GLOBAL /dev/null
    --setenv GIT_TERMINAL_PROMPT 0
    --setenv GCM_INTERACTIVE never
    --setenv NO_COLOR 1

    --chdir "${WS}/controller"
  )
  # Nothing else is forwarded. --clearenv means OPENAI_API_KEY, ANTHROPIC_API_KEY,
  # GitHub tokens, cloud credentials and proxy credentials cannot reach the
  # sandbox from this shell's environment. The clients use their own login state
  # through the copy-on-write credential mounts above.
  #
  # NO MODEL, EFFORT OR CORRECTION-CAP VARIABLE IS SET HERE OR ANYWHERE IN THIS
  # FILE. gpt-5.6-sol / high, claude-opus-5 / xhigh and the five-round cap are
  # controller-owned and are not overridden.
}

# ==========================================================================
# SECTION 10 — ISOLATION SELF-TEST (no models, no controller, no python)
# ==========================================================================

step "ISOLATION SELF-TEST"

# This proves the namespace is actually the namespace we asked for, BEFORE any
# real model call happens. It runs /bin/sh only. It never invokes python, Codex,
# Claude or nh_loop.py. If any assertion fails the rehearsal is refused; the
# isolation is never weakened to continue.
#
# It runs ONCE, and that is sufficient BECAUSE every stage below is launched with
# the argument vector produced by build_bwrap_args -- the same function, with the
# same single argument, re-invoked per stage. There is no per-stage variation for
# a self-test to miss.
read -r -d '' SELFTEST <<'SELFTEST_EOF' || true
set -eu
fail() { printf 'SELFTEST_FAIL %s\n' "$*" >&2; exit 9; }

# exact mount-point -> fstype from /proc/self/mountinfo (last match wins, i.e.
# the mount actually on top at that path)
fstype_at() {
  target="$1"
  awk -v t="$target" '
    {
      mp = $5
      sep = 0
      for (i = 7; i <= NF; i++) if ($i == "-") { sep = i; break }
      if (sep && mp == t) ft = $(sep+1)
    }
    END { if (ft != "") print ft }
  ' /proc/self/mountinfo
}

# read the hostname from procfs, not from a `hostname` binary that may not exist
[ "$(cat /proc/sys/kernel/hostname)" = "nh-shadow-rehearsal" ] \
  || fail "hostname is not the sandbox hostname -- UTS namespace not established"
[ "$HOME" = "/home/ness" ] || fail "HOME wrong"
[ "$USER" = "ness" ] || fail "USER wrong"
[ "$TMPDIR" = "/tmp" ] || fail "TMPDIR wrong"
[ "$CODEX_HOME" = "/home/ness/.codex" ] || fail "CODEX_HOME wrong"
[ "$CLAUDE_CONFIG_DIR" = "/home/ness/.claude" ] || fail "CLAUDE_CONFIG_DIR wrong"

# no host secret may have leaked in through the environment
for v in OPENAI_API_KEY ANTHROPIC_API_KEY GITHUB_TOKEN GH_TOKEN AWS_ACCESS_KEY_ID \
         AWS_SECRET_ACCESS_KEY GOOGLE_APPLICATION_CREDENTIALS HTTPS_PROXY_CREDENTIALS; do
  eval "val=\${$v:-}"
  [ -z "${val}" ] || fail "host secret env leaked into the namespace: $v"
done

# NOTHING may pre-answer any controller contract from outside. The complete set
# of NH_-prefixed variables must be exactly the two this launcher sets: the
# shadow interview-state dir, and the self-test's own marker token. Any other
# NH_* variable -- anything that could steer the controller, supply a
# not_ready_reason, or manufacture a coverage clearance -- fails the isolation
# here, before any model call.
nh_vars="$(env | sed -n 's/^\(NH_[A-Za-z0-9_]*\)=.*/\1/p' | LC_ALL=C sort | tr '\n' ',')"
[ "$nh_vars" = "NH_LOOP_INTERVIEW_STATE_DIR,NH_SHADOW_TOKEN," ] \
  || fail "unexpected NH_* environment inside the namespace: ${nh_vars}"
[ "$NH_LOOP_INTERVIEW_STATE_DIR" = "/home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/nh_interview_state" ] \
  || fail "NH_LOOP_INTERVIEW_STATE_DIR does not point at the shadow interview state"

# NO INHERITED FILE DESCRIPTOR MAY REACH THE NAMESPACE.
#
# Bubblewrap does not close descriptors it was not asked about, and a mount
# namespace does not revoke an already-open one. A writable file or directory
# descriptor inherited from the invoking shell would still resolve through
# /proc/self/fd/N to the real object, reaching the protected workspace, the
# regression source or a preserved lab even though /home/ness is hidden by tmpfs.
#
# Only stdin, stdout and stderr may be present. FD 11 is consumed by bwrap's
# --file and is gone by now.
#
# The ONLY tolerated entry is one whose readlink is EMPTY -- a descriptor which
# no longer existed by the time it was inspected, and a closed descriptor can
# carry nothing.
#
# There is deliberately NO exemption for descriptors whose target looks like
# /proc/<pid>/fd. Such an exemption would accept an inherited handle on another
# process's descriptor table, and /proc/self/fd/<N>/<M> would then traverse
# through it to the protected workspace -- the exact class of escape this check
# exists to stop.
for f in /proc/self/fd/*; do
  n="${f##*/}"
  case "$n" in 0|1|2) continue ;; esac
  tgt="$(readlink "$f" 2>/dev/null || true)"
  [ -n "$tgt" ] || continue
  fail "inherited file descriptor leaked into the namespace: ${n} -> ${tgt}"
done

# the real home is gone
t="$(fstype_at /home/ness)"
[ "$t" = "tmpfs" ] || fail "/home/ness is not tmpfs (got: ${t:-none}) -- the real home is not hidden"

# EVERY disposable N.H artefact directory must be unreachable from inside --
# every preserved rehearsal lab, the regression source that lives inside one of
# them, and every other NH_AICP_ artefact. /home/ness is tmpfs and none of them
# was put back.
for d in /home/ness/NH_AICP_*; do
  [ ! -e "$d" ] || fail "a preserved N.H lab or artefact is visible inside the namespace: $d"
done

# the real credential material is not reachable
[ ! -e /home/ness/.ssh ]    || fail ".ssh is visible inside the namespace"
[ ! -e /home/ness/.netrc ]  || fail ".netrc is visible inside the namespace"
[ ! -e /home/ness/.config ] || fail ".config is visible inside the namespace"

# .codex and .claude are anonymous copy-on-write overlays
t="$(fstype_at /home/ness/.codex)"
[ "$t" = "overlay" ] || fail "/home/ness/.codex is not an overlay (got: ${t:-none})"
t="$(fstype_at /home/ness/.claude)"
[ "$t" = "overlay" ] || fail "/home/ness/.claude is not an overlay (got: ${t:-none})"

# the overlays are writable, and by construction writes go to the invisible
# tmpfs upper layer, never to the host
probe="/home/ness/.codex/.nh_shadow_cow_probe"
: > "$probe" || fail ".codex overlay is not writable"
rm -f "$probe"
probe="/home/ness/.claude/.nh_shadow_cow_probe"
: > "$probe" || fail ".claude overlay is not writable"
rm -f "$probe"

# the client config is present and writable, and it is namespace-only
[ -f /home/ness/.claude.json ] || fail ".claude.json missing inside the namespace"
[ -w /home/ness/.claude.json ] || fail ".claude.json not writable inside the namespace"

# the toolchain is reachable
[ -x /home/ness/.nvm/versions/node/v24.18.0/bin/codex ]  || fail "codex not reachable"
[ -x /home/ness/.nvm/versions/node/v24.18.0/bin/claude ] || fail "claude not reachable"
[ -x /usr/bin/python3 ] || fail "python3 not reachable"

# THE SUBSTITUTION: the normal N.H path is the shadow, not the original
[ -f "/home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/.nh_shadow_marker" ] \
  || fail "the workspace at the normal path is NOT the shadow -- refusing"
[ "$(cat /home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/.nh_shadow_marker)" = "$NH_SHADOW_TOKEN" ] \
  || fail "shadow marker token mismatch at the normal path"
[ -w /home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/NH-GOVERNANCE/05_ACTIVE_CANDIDATE ] \
  || fail "the shadow candidate directory is not writable"
[ -w /home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/nh_interview_state ] \
  || fail "the shadow interview state is not writable"
[ -d /home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/controller ] || fail "shadow controller missing"

# realpath of the N.H checkout must still be the canonical hardcoded path
rp="$(cd /home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/NH-GOVERNANCE && pwd -P)"
[ "$rp" = "/home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/NH-GOVERNANCE" ] \
  || fail "canonical path substitution not visible (got: $rp)"

# /tmp is the lab runtime tmp
[ -f /tmp/.nh_shadow_tmp_marker ] || fail "/tmp is not the lab runtime tmp"

# runtime dir
[ -d /run/user/1000 ] || fail "/run/user/1000 missing"

printf 'SELFTEST_PASS\n'
SELFTEST_EOF

build_bwrap_args 11
exec 11<"$HOST_CLAUDE_JSON"
set +e
SELFTEST_OUT="$(
  "$BWRAP" "${BWRAP_ARGS[@]}" \
    --setenv NH_SHADOW_TOKEN "$SHADOW_TOKEN" \
    -- /bin/sh -c "$SELFTEST" 2>&1 </dev/null
)"
SELFTEST_RC=$?
set -e
exec 11<&- 2>/dev/null || true

printf '%s\n' "$SELFTEST_OUT" > "${PROOF}/isolation-selftest.txt"
if [ "$SELFTEST_RC" -ne 0 ] || ! printf '%s' "$SELFTEST_OUT" | grep -q '^SELFTEST_PASS$'; then
  printf '%s\n' "$SELFTEST_OUT" >&2
  die "the required namespace isolation could not be established (rc=${SELFTEST_RC}).
      See ${PROOF}/isolation-selftest.txt
      The isolation is NOT weakened to continue. No model call was made."
fi
note "isolation self-test PASS (see ${PROOF}/isolation-selftest.txt)"

# The copy-on-write proof, checked from OUTSIDE: the probe files the self-test
# wrote into the overlays must not exist on the host.
[ ! -e "${HOST_CODEX}/.nh_shadow_cow_probe" ] \
  || die "copy-on-write overlay LEAKED to the host .codex -- refusing to rehearse"
[ ! -e "${HOST_CLAUDE}/.nh_shadow_cow_probe" ] \
  || die "copy-on-write overlay LEAKED to the host .claude -- refusing to rehearse"
note "copy-on-write overlays proved non-leaking from outside the namespace"

# The persistent lab must contain no model login material. Checked here BEFORE
# any stage runs, and again AFTER them all (section 12), because everything the
# sandboxed stages can write -- the shadow workspace, /tmp and the captured
# stdout/stderr -- is lab-backed, while the credential overlays are readable
# inside the namespace.
PRE_SCAN_RC=0
scan_lab_for_credentials "${PROOF}/credential-scan.before.txt" || PRE_SCAN_RC=$?
case "$PRE_SCAN_RC" in
  0) note "no known credential marker found inside the persistent lab" ;;
  1) die "model login material was found inside the persistent lab -- refusing to rehearse.
      See ${PROOF}/credential-scan.before.txt" ;;
  *) die "the persistent lab could not be scanned for model login material
      (scan status ${PRE_SCAN_RC}). A scan that did not complete is not a clean
      scan. See ${PROOF}/credential-scan.before.txt.errors" ;;
esac

# ==========================================================================
# SECTION 11 — THE ONE-STAGE REAL CONTINUATION (ACCEPTED REPAIR 28)
# ==========================================================================
#
# ONE stage, inside Bubblewrap, AT MOST ONCE:
#
#   python3 nh_loop.py execute-next-claude-task
#
# THERE IS EXACTLY ONE CALL SITE IN THIS FILE, and it passes STAGE4_CMD. No retry
# loop, no fallback invocation, no duplicate stage, no alternate validator, and
# no second outer correction loop. The controller's OWN internal bounded
# correction loop inside execute-next-claude-task, with its lifetime limit of 5
# rounds, is entirely controller-owned and is neither duplicated nor bypassed
# here.
#
# DOORS 1 TO 3 ARE NOT RUN HERE, AND CANNOT BE. There is no question-validation
# stage, no question-coverage-review stage and no interview-gate stage. No
# constant in this file holds any of those command names, and the single call
# site below can pass nothing but STAGE4_CMD. Their result was produced for real
# by v20, authenticated in section 4b3, and is carried forward inside the
# continuation source's own nine-event interview journal.
#
# THE CONTROLLER STILL ENFORCES ITS OWN GATE. execute-next-claude-task performs
# its own Piece-3 interview clearance and its own source re-proofs on every
# invocation. Nothing here bypasses, relaxes, pre-answers or replaces any of
# them. If the controller decides the carried-forward clearance is not usable, it
# fails closed, and that is a VALID RESULT this launcher records without working
# around.
#
# QUESTION DELIVERY IS NOT PART OF THIS RUN AND CANNOT BE. No question is
# composed, displayed, delivered or answered. No answer of Ness's appears
# anywhere in this file. The disposable question-delivery workspace is not
# referenced.
#
# WHATEVER EXECUTE REPORTS IS THE CONTROLLER RESULT, AND v21 RECORDS IT WITHOUT
# REINTERPRETING IT. An early stop is a valid observational outcome, is not a
# launcher fault, is not converted into success, and is not worked around.

# READ-ONLY REPORT READERS. They can set no stop reason, can fail no gate, and
# are never consulted by any decision. They exist so the result block can quote
# the controller's own scalars instead of paraphrasing them. They use the single
# REPORT_PARSER defined in section 4b2; there is no second parser in this file.
read_report_value() {
  local file="$1" key="$2" out rc
  set +e
  out="$("$PY3" -c "$REPORT_PARSER" "$file" "$key" 2>/dev/null)"
  rc=$?
  set -e
  if [ "$rc" -eq 0 ] && [ -n "$out" ]; then printf '%s' "$out"; else printf 'UNAVAILABLE'; fi
}

# NOT-RUN is preserved as NOT-RUN. A stage that never ran has no report to quote,
# and printing UNAVAILABLE for it would blur "the stage was never entered" into
# "the field was missing". An ABSENT FIELD IS REPORTED AS UNAVAILABLE AND IS
# NEVER GIVEN AN INVENTED VALUE.
stage_scalar() {
  # stage_scalar <stage_rc> <stdout_file> <key>
  if [ "$1" = "NOT-RUN" ]; then printf 'NOT-RUN'; else read_report_value "$2" "$3"; fi
}

# run_controller_stage <slug> <controller command> <human label>
#
# Runs ONE controller command inside its own namespace and records ALL of its
# evidence: the exact argv, stdout, stderr, exit code, start and finish
# timestamps, and its own protected-source proof.
#
# The result is returned through the global STAGE_RC rather than through the
# function's own exit status ON PURPOSE: under `set -e` a function that returns
# non-zero would abort the launcher at the call site, and a non-zero controller
# exit is an ORDINARY, EXPECTED outcome this launcher exists to record --
# aborting there would destroy the after-proof, which is the most important thing
# this launcher produces.
run_controller_stage() {
  local slug="$1" cmd="$2" label="$3"
  local so="${PROOF}/${slug}.stdout"
  local se="${PROOF}/${slug}.stderr"
  local rcf="${PROOF}/${slug}.exit-code"
  local cmdf="${PROOF}/${slug}.command"
  local startf="${PROOF}/${slug}.started"
  local finishf="${PROOF}/${slug}.finished"
  local rc

  step "STAGE: ${label}"
  say "Running, inside the namespace:"
  say "  ${PY3} ${WS}/controller/nh_loop.py ${cmd}"
  say ""
  say "Live output is being written to:"
  say "  ${so}"
  say "  ${se}"
  say ""

  # THE EXACT ARGV, one element per line, so what ran is a recorded fact rather
  # than something a reader has to reconstruct from prose.
  {
    printf '%s\n' "$PY3"
    printf '%s\n' "${WS}/controller/nh_loop.py"
    printf '%s\n' "$cmd"
  } > "$cmdf"

  # The identical argument vector the self-test used.
  build_bwrap_args 11
  exec 11<"$HOST_CLAUDE_JSON"

  # From here on no report may claim that no model or provider call was made. Set
  # before the stage starts, not after, because a stage killed mid-flight may
  # already have reached a provider.
  RUN_STARTED=1

  date -u +%Y-%m-%dT%H:%M:%SZ > "$startf"
  set +e
  "$BWRAP" "${BWRAP_ARGS[@]}" \
    -- "$PY3" "${WS}/controller/nh_loop.py" "$cmd" \
    > "$so" \
    2> "$se" \
    < /dev/null
  rc=$?
  set -e
  date -u +%Y-%m-%dT%H:%M:%SZ > "$finishf"

  exec 11<&- 2>/dev/null || true
  printf '%s\n' "$rc" > "$rcf"
  STAGE_RC="$rc"
  note "${label} finished with exit code ${rc}"

  # THIS STAGE'S OWN PROTECTED-SOURCE PROOF, taken from OUTSIDE the namespace,
  # immediately, so a containment failure is recorded against the stage that
  # caused it rather than discovered once at the end.
  step "PROTECTED-SOURCE PROOF AFTER ${label}"
  capture_original_proof "${PROOF}/original.after-${slug}"
  STAGE_SOURCE_PROOF="PASS"
  if ! compare_proof_set "${PROOF}/original.before" \
                         "${PROOF}/original.after-${slug}" \
                         "after-${slug}" "${PROTECTED_PROOF_FILES[@]}"; then
    STAGE_SOURCE_PROOF="FAIL"
  fi
  if ! compare_proof_set "${PROOF}/original.before" \
                         "${PROOF}/original.after-${slug}" \
                         "after-${slug}-labs" "${PRESERVED_LAB_PROOF_FILES[@]}"; then
    STAGE_SOURCE_PROOF="FAIL"
  fi
  if ! compare_proof_set "${PROOF}/original.before" \
                         "${PROOF}/original.after-${slug}" \
                         "after-${slug}-seed" "${REGRESSION_SEED_PROOF_FILES[@]}"; then
    STAGE_SOURCE_PROOF="FAIL"
  fi
  if ! compare_proof_set "${PROOF}/original.before" \
                         "${PROOF}/original.after-${slug}" \
                         "after-${slug}-cont" "${CONTINUATION_SOURCE_PROOF_FILES[@]}"; then
    STAGE_SOURCE_PROOF="FAIL"
  fi
  printf '%s\n' "$STAGE_SOURCE_PROOF" > "${PROOF}/${slug}.source-proof"
  if [ "$STAGE_SOURCE_PROOF" = "FAIL" ]; then
    CONTAINMENT_BREACHED=1
    SEQUENCE_STOP_REASON="the protected original, a preserved lab, the lineage seed or the continuation source CHANGED during ${label}"
    say "[CONTAINMENT] a protected object changed during ${label}."
    say "              Evidence is preserved."
  else
    note "protected original, preserved labs, lineage seed and continuation source unchanged across ${label}"
  fi
}

# --------------------------------------------------------------------------
# STAGE 4 — THE ONE EXECUTE
# --------------------------------------------------------------------------
#
# EXACTLY ONE outer execution of the controller. There is no retry here and
# nothing reruns it. The controller owns everything inside it: the GPT mechanical
# design specification, Claude's application of it, the fresh GPT/Codex audit,
# the same-session Claude corrections and its own lifetime limit of 5 correction
# rounds. This launcher does not reinterpret audit findings and implements no
# second repair loop.
run_controller_stage "$STAGE4_SLUG" "$STAGE4_CMD" "STAGE 4 — execute-next-claude-task"
EXEC_RC="$STAGE_RC"
# The stage's own failure is a stop reason too, so the summary states WHY the run
# ended rather than leaving a bare status to be interpreted. The controller's own
# non-zero status is still what this launcher returns; this only names it.
if [ "$EXEC_RC" -ne 0 ] && [ -z "$SEQUENCE_STOP_REASON" ]; then
  SEQUENCE_STOP_REASON="stage 4 execute-next-claude-task exited ${EXEC_RC}"
fi

# The exit status this launcher will finally return for the controller portion of
# the run. With one stage it is that stage's status and nothing else.
#
# nh_loop.py defines exactly three exit codes -- 0, 1 and 2 -- so this value can
# never collide with the reserved safety codes 90-95 used below.
SHADOW_RC="$EXEC_RC"

# --------------------------------------------------------------------------
# THE CONTROLLER-OWNED SCALARS THE RESULT BLOCK QUOTES
# --------------------------------------------------------------------------
#
# Extracted ONCE, here, after the stage has run, and used only for display. Not
# one of these values influenced any decision anywhere in this file.
#
# NO VALUE IS INVENTED. A field the controller did not report comes back as
# UNAVAILABLE, and a stage that never ran comes back as NOT-RUN. Neither is ever
# silently rendered as a number, a verdict or a pass.
S4_OUT="${PROOF}/${STAGE4_SLUG}.stdout"

OBS_S4_OK="$(stage_scalar "$EXEC_RC" "$S4_OUT" "ok")"
OBS_S4_STOP_REASON="$(stage_scalar "$EXEC_RC" "$S4_OUT" "stop_reason")"
OBS_S4_INTERVIEW_STOP_REASON="$(stage_scalar "$EXEC_RC" "$S4_OUT" "interview_stop_reason")"
OBS_S4_AUDIT_VERDICT="$(stage_scalar "$EXEC_RC" "$S4_OUT" "final_design_audit_verdict")"
OBS_S4_HIGHEST_SEVERITY="$(stage_scalar "$EXEC_RC" "$S4_OUT" "final_highest_severity")"
OBS_S4_AUDIT_CHATGPT_REQ="$(stage_scalar "$EXEC_RC" "$S4_OUT" "design_audit_chatgpt_review_required")"
OBS_S4_FINAL_CHATGPT_REQ="$(stage_scalar "$EXEC_RC" "$S4_OUT" "final_chatgpt_review_required")"
OBS_S4_FINAL_BLOCKING_CHATGPT_REQ="$(stage_scalar "$EXEC_RC" "$S4_OUT" "final_blocking_chatgpt_review_required")"
OBS_S4_CHATGPT_AUDIT_PERFORMED="$(stage_scalar "$EXEC_RC" "$S4_OUT" "chatgpt_independent_audit_performed")"
OBS_S4_PIECE3_QV_REQUIRED="$(stage_scalar "$EXEC_RC" "$S4_OUT" "piece3_question_validation_required")"
OBS_S4_PIECE3_ROUTE="$(stage_scalar "$EXEC_RC" "$S4_OUT" "piece3_route")"
OBS_S4_PIECE3_ROUTED_TITLES="$(stage_scalar "$EXEC_RC" "$S4_OUT" "piece3_routed_finding_titles")"
OBS_S4_ROUTING_PROVENANCE="$(stage_scalar "$EXEC_RC" "$S4_OUT" "design_audit_routing_provenance")"
OBS_S4_NESS_QUESTION_ASKED="$(stage_scalar "$EXEC_RC" "$S4_OUT" "ness_question_asked")"
OBS_S4_NESS_DECISION_MANUFACTURED="$(stage_scalar "$EXEC_RC" "$S4_OUT" "ness_decision_manufactured")"
OBS_S4_ROUNDS_STARTED="$(stage_scalar "$EXEC_RC" "$S4_OUT" "correction_rounds_started")"
OBS_S4_ROUNDS_COMPLETED="$(stage_scalar "$EXEC_RC" "$S4_OUT" "correction_rounds_completed")"
OBS_S4_TOTAL_CLAUDE="$(stage_scalar "$EXEC_RC" "$S4_OUT" "total_claude_invocations")"
OBS_S4_TOTAL_CODEX_AUDITS="$(stage_scalar "$EXEC_RC" "$S4_OUT" "total_codex_design_audit_invocations")"

# THE TWO FIELDS THE CORRECTED BLOCK OWNS. Repair 27B decides only whether the
# requirement count is read at all; it never invents one. UNAVAILABLE here is the
# CORRECT reading for a task_ready = false preparation, and it is not a failure.
# WHICH kind of not-ready this is stays the controller's business, read from its
# own bounded not_ready_reason field.
OBS_S4_PREPARATION_OK="$(stage_scalar "$EXEC_RC" "$S4_OUT" "preparation_ok")"
OBS_S4_TASK_READY="$(stage_scalar "$EXEC_RC" "$S4_OUT" "task_ready")"
OBS_S4_NOT_READY_REASON="$(stage_scalar "$EXEC_RC" "$S4_OUT" "not_ready_reason")"
OBS_S4_MDS_SHA="$(stage_scalar "$EXEC_RC" "$S4_OUT" "mechanical_design_specification_sha256")"
OBS_S4_MDS_REQ_COUNT="$(stage_scalar "$EXEC_RC" "$S4_OUT" "mechanical_design_requirement_count")"
OBS_S4_PIECE3_GATE_ENFORCED="$(stage_scalar "$EXEC_RC" "$S4_OUT" "piece3_interview_gate_enforced")"
OBS_S4_PIECE3_GATE_UNLOCKED="$(stage_scalar "$EXEC_RC" "$S4_OUT" "piece3_interview_gate_unlocked")"

{
  printf 'CONTROLLER-OWNED OBSERVATION EXTRACTION\n'
  printf '=======================================\n'
  printf 'Extracted for display only. No value below gated anything.\n\n'
  printf 'STAGE 4 execute-next-claude-task (the only stage v23 runs)\n'
  printf '  exit                          %s\n' "$EXEC_RC"
  printf '  ok                            %s\n' "$OBS_S4_OK"
  printf '  stop_reason                   %s\n' "$OBS_S4_STOP_REASON"
  printf '  interview_stop_reason         %s\n' "$OBS_S4_INTERVIEW_STOP_REASON"
  printf '  preparation_ok                %s\n' "$OBS_S4_PREPARATION_OK"
  printf '  task_ready                    %s\n' "$OBS_S4_TASK_READY"
  printf '  not_ready_reason              %.400s\n' "$OBS_S4_NOT_READY_REASON"
  printf '  mechanical_design_requirement_count %s\n' "$OBS_S4_MDS_REQ_COUNT"
  printf '\n'
  printf 'DOORS 1-3 WERE NOT RUN BY THIS LAUNCHER. Their v20 result was\n'
  printf 'authenticated before anything was copied:\n'
  printf '  V20_RESULT_AUTHENTICATED      %s\n' "$V20_RESULT_AUTHENTICATED"
} > "${PROOF}/controller-observations.txt" 2>/dev/null || true

# ==========================================================================
# SECTION 11b — v24 STAGE OBSERVATIONS
#               (READ-ONLY, DECIDES NOTHING)
# ==========================================================================
#
# A convenience pass over the lab's OWN captured output, so the behaviour of the
# one stage is easy to inspect without reading thousands of lines by hand.
#
# IT RECORDS; IT DECIDES NOTHING. It sets no verdict, it can fail no check, and
# every safety verdict below is computed entirely separately.
#
# NO PARTICULAR NATURAL OUTCOME IS REQUIRED. In particular:
#   - a fail-closed stop is the controller working;
#   - ZERO Claude invocations may be entirely correct;
#   - a task_ready = false preparation with no mechanical design specification is
#     exactly the state Repair 28 exists to correct, and is not an
#     error;
#   - a stop at CHATGPT_REVIEW_REQUIRED is where this launcher stops, on purpose.
# These observations record what happened. They do not invent PASS.
#
# It reads only the stage files this launcher created. It never reads the shadow
# candidates and never echoes candidate content: it prints scalar,
# controller-owned report fields and fixed live-progress marker counts, each
# truncated.
step "v23 STAGE OBSERVATIONS"

observe_v24_stage() {
  local out="${PROOF}/v24-stage-observations.txt"
  local s4="$S4_OUT"
  local s4e="${PROOF}/${STAGE4_SLUG}.stderr"
  local n_new n_resume n_seed n_audit n_verdict n_corrspec n_stopreview

  n_new="$(grep -c -F -- 'invoking claude (new session'                        "$s4e" 2>/dev/null || true)"
  n_resume="$(grep -c -F -- 'resuming the package claude session'              "$s4e" 2>/dev/null || true)"
  n_seed="$(grep -c -F -- 'next target seeded byte-identical'                  "$s4e" 2>/dev/null || true)"
  n_audit="$(grep -c -F -- 'fresh codex design audit starting'                 "$s4e" 2>/dev/null || true)"
  n_verdict="$(grep -c -F -- 'codex verdict for'                               "$s4e" 2>/dev/null || true)"
  n_corrspec="$(grep -c -F -- 'running ONE fresh gpt correction-specification' "$s4e" 2>/dev/null || true)"
  n_stopreview="$(grep -c -F -- 'running ONE fresh gpt review of the claude specification stop' "$s4e" 2>/dev/null || true)"

  {
    printf 'v23 STAGE OBSERVATIONS -- descriptive only, no verdict\n'
    printf '=====================================================================\n\n'

    printf 'WHAT THIS RUN CONTINUED\n'
    printf '  continuation source : %s\n' "$CONTINUATION_SOURCE"
    printf '  source mode         : %s\n' "$CONTINUATION_SOURCE_MODE"
    printf '  journal             : %s events, sha256 %s\n' \
           "$EXP_CONT_JOURNAL_EVENTS" "$EXP_CONT_JOURNAL_SHA"
    printf '  journal head        : sha256 %s\n' "$EXP_CONT_HEAD_SHA"
    printf '  last event          : %s, sha256 %s\n' \
           "$EXP_CONT_EVENT9_TYPE" "$EXP_CONT_EVENT9_SHA"
    printf '  validation set      : %s\n' "$EXP_CONT_EVENT9_VALIDATION_SET_ID"
    printf '  routed signal       : %s\n' "$EXP_ROUTED_SIGNAL_ID"
    printf '  standing target     : %s\n' "$EXP_STANDING_TARGET_ID"
    printf '  package scope       : %s\n' "$EXP_PKG_SCOPE"
    printf '\n'
    printf '  THIS IS THE COMPLETED v21 SHADOW, THE EXACT STATE IN WHICH THE\n'
    printf '  REPAIR-27B CONTROLLER REACHED CLAUDE_SPECIFICATION_STOP. Its ninth\n'
    printf '  event is the question-coverage-review\n'
    printf '  clearance v20\047s Stage 2 produced and v20\047s Stage 3 read. That is\n'
    printf '  why Doors 1 to 3 were not rerun here: they were run for real, they\n'
    printf '  passed, and their outcome is carried forward in this journal.\n'
    printf '\n'
    printf '  ITS LINEAGE ROOT IS THE PRESERVED v10 SHADOW, WHICH PRE-DATES THE\n'
    printf '  FALSE v11 QUESTION. That lineage seed was authenticated and proved\n'
    printf '  whole against the preserved v11 witness, and in v24 it was never\n'
    printf '  copied. No answered question-delivery state was used, and no answer\n'
    printf '  of Ness\047s appears anywhere in this launcher.\n'
    printf '\n'
    printf 'THE COMPLETED v20 DOORS RESULT THIS CONTINUATION INHERITS (ANCESTOR)\n'
    printf '  V20_RESULT_AUTHENTICATED : %s\n' "$V20_RESULT_AUTHENTICATED"
    printf '  stage 1 question-validation      exit %s, source-proof %s\n' \
           "$EXP_V20_S1_EXIT" "$EXP_V20_SOURCE_PROOF_VALUE"
    printf '  stage 2 question-coverage-review exit %s, source-proof %s\n' \
           "$EXP_V20_S2_EXIT" "$EXP_V20_SOURCE_PROOF_VALUE"
    printf '  stage 3 interview-gate           exit %s, source-proof %s\n' \
           "$EXP_V20_S3_EXIT" "$EXP_V20_SOURCE_PROOF_VALUE"
    printf '  stage 4 execute-next-claude-task exit %s, source-proof %s, stdout EMPTY\n' \
           "$EXP_V20_S4_EXIT" "$EXP_V20_SOURCE_PROOF_VALUE"
    printf '    %s\n' "$EXP_V20_S4_CRASH_SUBSCRIPT"
    printf '    %s\n' "$EXP_V20_S4_CRASH_TYPE"
    printf '\n'
    printf 'THE CONTROLLER REFRESH THIS RUN PERFORMED\n'
    printf '  source controller : %s  (accepted Repair 27B)\n' "$EXP_R27B_SHA"
    printf '  refreshed to      : %s  (accepted Repair 28 candidate)\n' "$EXP_R28_SHA"
    printf '  real controller   : %s  (unchanged, NOT installed, never a\n' "$EXP_LOOP_SHA"
    printf '                       refresh source and never a destination)\n'
    printf '  lineage seed      : %s  (Repair 17, preserved, NOT copied in v24)\n' "$EXP_SEED_LOOP_SHA"
    printf '  Repair20B         : %s  (preserved, NOT a refresh source)\n' "$EXP_R20B_SHA"
    printf '  Repair21          : %s  (preserved, NOT a refresh source)\n' "$EXP_R21_SHA"
    printf '  Repair22          : %s  (preserved, NOT a refresh source)\n' "$EXP_R22_SHA"
    printf '  Repair23          : %s  (preserved, NOT a refresh source)\n' "$EXP_R23_SHA"
    printf '  Repair24          : %s  (preserved, NOT a refresh source)\n' "$EXP_R24_SHA"
    printf '  Repair25          : %s  (preserved, NOT a refresh source)\n' "$EXP_R25_SHA"
    printf '  Repair26          : %s  (preserved, NOT a refresh source)\n' "$EXP_R26_SHA"
    printf '  Repair27          : %s  (preserved, NOT a refresh source)\n' "$EXP_R27_SHA"
    printf '  Repair27A         : %s  (preserved, NOT a refresh source)\n' "$EXP_R27A_SHA"
    printf '  Repair27B         : %s  (preserved source-controller, NOT a refresh source)\n' "$EXP_R27B_SHA"
    printf '  refresh state     : %s\n' "$CONTROLLER_REFRESH"
    printf '  continuation state: %s\n' "$CONTINUATION_STATE"
    printf '  paths refreshed   : controller/nh_loop.py, and no other\n'
    printf '\n'
    printf '  The refresh was applied to the NEW disposable copy only, after that\n'
    printf '  copy had been proved byte-truthful against the continuation source,\n'
    printf '  and it was proved afterwards to have changed exactly one path. The\n'
    printf '  interview journal, journal head and authenticity key were NOT\n'
    printf '  refreshed and remain byte-identical to the continuation source. The\n'
    printf '  completed v21 lab was not written to at any point.\n\n'

    printf 'STAGE EXIT CODE AND TIMESTAMPS\n'
    printf '  stage 4  execute-next-claude-task : %s\n' "$EXEC_RC"
    printf '\n'
    local slug
    for slug in "${ALL_STAGE_SLUGS[@]}"; do
      printf '  %-20s started %s  finished %s  source-proof %s\n' \
        "$slug" \
        "$(cat "${PROOF}/${slug}.started" 2>/dev/null || printf 'unknown')" \
        "$(cat "${PROOF}/${slug}.finished" 2>/dev/null || printf 'unknown')" \
        "$(cat "${PROOF}/${slug}.source-proof" 2>/dev/null || printf 'NOT-RUN')"
    done
    printf '\n'
    if [ -n "$SEQUENCE_STOP_REASON" ]; then
      printf 'THE RUN ENDED HERE:\n  %s\n\n' "$SEQUENCE_STOP_REASON"
    else
      printf 'The stage completed and nothing observed forbade completion.\n\n'
    fi

    printf 'HOW TO READ THIS CODE\n'
    printf '  The controller uses exactly three: 0 ok, 1 fail-closed, 2 usage.\n'
    printf '  A fail-closed stop is the controller doing its job, and it is not a\n'
    printf '  launcher fault. An exit of 0 is not a verdict about N.H.\n\n'

    printf '==========================================\n'
    printf 'STAGE 4 -- EXECUTE-NEXT-CLAUDE-TASK (one only)\n'
    printf '==========================================\n'
    printf '  ok                         %s\n' "$OBS_S4_OK"
    printf '  stop_reason                %s\n' "$OBS_S4_STOP_REASON"
    printf '  interview_stop_reason      %s\n' "$OBS_S4_INTERVIEW_STOP_REASON"
    printf '\n'
    printf 'CONFIGURATION THIS CONTROLLER IS FROZEN TO:\n'
    grep -E '"(claude_model|claude_output_format|claude_allowed_tools|claude_permission_mode|claude_package_session_scope|claude_timeout_seconds)":' \
         "$s4" 2>/dev/null | cut -c1-200 || true
    printf '\n'
    printf 'THE PIECE-3 SEAM (the controller re-enforcing its own gate, in its own\n'
    printf 'right, over the carried-forward clearance):\n'
    printf '  piece3_interview_gate_enforced  %s\n' "$OBS_S4_PIECE3_GATE_ENFORCED"
    printf '  piece3_interview_gate_unlocked  %s\n' "$OBS_S4_PIECE3_GATE_UNLOCKED"
    grep -E '"(piece3_interview_gate_enforced|piece3_interview_gate_unlocked|piece3_question_validation_required|piece3_route)":' \
         "$s4" 2>/dev/null | cut -c1-200 || true
    printf '\n'
    printf 'THE PREPARATION REPORT -- THE EXACT BLOCK REPAIR 27B CORRECTS:\n'
    printf '  preparation_ok                      %s\n' "$OBS_S4_PREPARATION_OK"
    printf '  task_ready                          %s\n' "$OBS_S4_TASK_READY"
    printf '  not_ready_reason                    %.400s\n' "$OBS_S4_NOT_READY_REASON"
    printf '  mechanical_design_specification_sha256 %s\n' "$OBS_S4_MDS_SHA"
    printf '  mechanical_design_requirement_count %s\n' "$OBS_S4_MDS_REQ_COUNT"
    printf '\n'
    printf '  HOW TO READ THOSE FIVE. Under Repair 28, which inherits this from\n'
    printf '  Repair 27B unchanged, the requirement count is\n'
    printf '  read ONLY where a mechanical design specification exists. On a\n'
    printf '  task_ready = false preparation there is none, so the field stays at\n'
    printf '  the None it was initialised to and is reported here as UNAVAILABLE.\n'
    printf '  UNAVAILABLE IS THE CORRECT READING THERE AND IS NOT A FAILURE. A\n'
    printf '  zero would be worse than useless: it would claim a specification\n'
    printf '  exists and carries no requirements. WHICH kind of not-ready this is\n'
    printf '  is read from not_ready_reason, which the controller owns; this\n'
    printf '  launcher classifies nothing.\n'
    printf '\n'
    grep -E '"(preparation_ok|task_ready|not_ready_reason|prepared_classification|claude_instruction_source|mechanical_design_specification_sha256|mechanical_design_requirement_count)":' \
         "$s4" 2>/dev/null | cut -c1-200 || true
    printf '\n'
    printf 'CLAUDE MANDATORY SPECIFICATION STOP:\n'
    grep -E '"(claude_specification_stop_marker|claude_specification_stop_verified|claude_specification_stop_classification)":' \
         "$s4" 2>/dev/null | cut -c1-200 || true
    printf '\n'
    printf 'CLAUDE PACKAGE SESSION (one per package execution):\n'
    grep -E '"(initial_claude_session_mode|initial_claude_session_ok|claude_invoked|claude_package_session_established|claude_package_session_lost|claude_package_session_invocations|claude_package_session_new_invocations|claude_package_session_resumed_invocations|initial_claude_invocations|claude_correction_invocations|total_claude_invocations)":' \
         "$s4" 2>/dev/null | cut -c1-200 || true
    printf '\n'
    printf 'CORRECTION LOOP AND FRESH GPT AUDITS:\n'
    grep -E '"(correction_loop_enabled|correction_round_limit|correction_rounds_started|correction_rounds_completed|correction_performed|total_codex_design_audit_invocations|final_design_audit_verdict|final_highest_severity|stop_reason)":' \
         "$s4" 2>/dev/null | cut -c1-200 || true
    printf '\n'
    printf 'FRESH GPT CORRECTION-SPECIFICATION REVIEWS (per round):\n'
    grep -E '"(correction_specification_invoked|correction_specification_exit_code|correction_specification_ok|correction_specification_sha256)":' \
         "$s4" 2>/dev/null | cut -c1-200 || true
    printf '  These live inside correction_history, one group per round. An empty\n'
    printf '  section means no correction round was started.\n\n'

    printf 'LIVE-PROGRESS MARKER COUNTS (from the execute stage stderr):\n'
    printf '  new claude session started                : %s\n' "$n_new"
    printf '  resumed the package session               : %s\n' "$n_resume"
    printf '  next target seeded from blocked           : %s\n' "$n_seed"
    printf '  fresh OpenAI/Codex audits begun           : %s\n' "$n_audit"
    printf '  OpenAI/Codex verdicts recorded            : %s\n' "$n_verdict"
    printf '  fresh GPT correction-specification reviews: %s\n' "$n_corrspec"
    printf '  fresh GPT reviews of a claude stop        : %s\n' "$n_stopreview"
    printf '\n'

    printf 'WHAT THESE COUNTS DO AND DO NOT MEAN\n'
    if [ "$EXEC_RC" = "NOT-RUN" ]; then
      printf '  The stage never ran, so every count above is necessarily zero.\n'
    elif [ "${n_new:-0}" -eq 0 ] 2>/dev/null; then
      printf '  ZERO Claude invocations. This is NOT automatically a failure: the\n'
      printf '  controller enforces the interview gate again in its own right, and\n'
      printf '  may fail closed before Claude is considered. Read\n'
      printf '  piece3_interview_gate_unlocked, task_ready, not_ready_reason and\n'
      printf '  stop_reason above.\n'
    else
      printf '  Claude was invoked, so the mechanical path was open for this package\n'
      printf '  and the GPT specification reached Claude for application.\n'
    fi
    if [ "${n_resume:-0}" -gt 0 ] 2>/dev/null; then
      printf '  A RESUMED Claude call occurred, so same-package session continuity\n'
      printf '  was exercised for real by this run.\n'
    else
      printf '  No resumed Claude call occurred. This is NOT a failure: if the\n'
      printf '  candidate reached PASS, or the loop never started a correction\n'
      printf '  round, there was nothing to resume.\n'
    fi
    printf '\n'

    printf 'THE FIXED CONTROLLER-OWNED CONFIGURATION\n'
    printf '  The lifetime correction allowance is 5 rounds\n'
    printf '  (MAX_AUTOMATIC_CORRECTION_ROUNDS). It is owned by nh_loop.py and this\n'
    printf '  launcher neither sets nor influences it; the correction_round_limit\n'
    printf '  field above is the controller stating it.\n'
    printf '  The OpenAI reasoning role is gpt-5.6-sol at effort high, invoked\n'
    printf '  through the read-only, ephemeral Codex CLI transport. Claude is\n'
    printf '  claude-opus-5 at xhigh. Both are the controller-owned configuration\n'
    printf '  frozen inside the shadow controller sha256 %s --\n' "$EXP_R28_SHA"
    printf '  this launcher sets neither and overrides neither, and --clearenv\n'
    printf '  wipes the environment so no model, effort or cap variable can reach\n'
    printf '  the namespace from this shell.\n\n'

    printf 'THIS SECTION DECIDES NOTHING\n'
    printf '  It assigns no verdict, passes nothing and fails nothing. The only\n'
    printf '  verdicts this launcher holds are the containment, lineage-seed,\n'
    printf '  continuation-source and credential ones in the RESULT block, and\n'
    printf '  they are computed entirely separately.\n'
  } > "$out" 2>/dev/null || true

  note "v23 stage observations written to ${out}"
}
observe_v24_stage || true

# ==========================================================================
# SECTION 11c — THE INHERITED REPAIR-25 CHATGPT-STOP HANDOFF OBSERVATION
#               (READ-ONLY, CONDITIONAL, DECIDES NOTHING, GATES NO STAGE)
# ==========================================================================
#
# WHOSE INVARIANT THIS IS, STATED EXACTLY. The seam observed here is a REPAIR-25
# invariant. The controller under test in v24 is ACCEPTED REPAIR 28, which is
# built through 27A, 27 and 26 on accepted Repair 25 and INHERITS this behaviour
# unchanged. Repair 27B did not invent it and does not claim it: the observer is
# checking that INHERITED Repair-25 seam still holds under Repair 27B. That is
# why the field, the artefact and the verdict all keep the Repair-25 name.
#
# WHAT THIS IS. Repair 25 corrected exactly one thing: the
# execute-next-claude-task stop taken when a validated design audit carries a
# BLOCKING finding routed chatgpt_review_required. Before Repair 25 that stop
# marked the issue as an already-made Piece-3 transition -- setting
# piece3_question_validation_required = true, naming a piece3_route, listing the
# routed finding titles -- and handed the operator
# `python3 nh_loop.py route-audit-finding` and
# `python3 nh_loop.py question-validation` as immediate commands, in the same
# report whose first sentence said independent ChatGPT review was required
# FIRST. Both cannot be true, and nothing had been routed.
#
# WHEN IT RUNS. ONLY when Stage 4 actually reported
# stop_reason = "CHATGPT_REVIEW_REQUIRED". On every other outcome, including an
# ordinary full PASS, it records NOT-EXERCISED and stops.
#
# NOT-EXERCISED IS NOT A FAILURE, and this launcher contains no code able to
# make the branch fire. NO FAKE AUDIT FINDING IS INJECTED, no second case is
# run, no controller is re-run, and no finding is manufactured. The branch was
# already independently audited and offline-tested; v24 is a CONTINUATION
# rehearsal, not failure injection.
#
# AND IF THE BRANCH DOES FIRE, THIS LAUNCHER STOPS THERE. It does not invoke
# route-audit-finding, does not invoke question-validation, and holds no call
# site able to invoke either. The three command strings below are GREP NEEDLES
# matched against the captured Stage-4 stdout; they are never passed to
# nh_loop.py, and the single controller call site in this file passes STAGE4_CMD
# and nothing else.
#
# IT DECIDES NOTHING AND CANNOT TRIGGER PIECE 3. Every check below reads files
# this launcher already captured. It runs no controller command, invokes no
# model, appends to no journal, and cannot set SEQUENCE_STOP_REASON. Its result
# is one observational string and it gates no stage.
step "REPAIR-25 CHATGPT-STOP HANDOFF OBSERVATION"

observe_repair25_chatgpt_stop_handoff() {
  local out="${PROOF}/repair25-chatgpt-stop-handoff.txt"
  local s4="$S4_OUT"
  local verdict="NOT-EXERCISED" fail_count=0
  local reason="Stage 4 did not report CHATGPT_REVIEW_REQUIRED"
  # THE THREE EXACT FORBIDDEN IMMEDIATE-COMMAND STRINGS. Ordinary explanatory
  # prose may legitimately contain the words route-audit-finding or
  # question-validation while describing the later CONDITIONAL path; that is
  # expected and is not what is checked. Only the old immediate-command
  # behaviour is forbidden, so the needles are the exact command lines and the
  # exact old Repair-24 sentence opening.
  local cmd_route="python3 nh_loop.py route-audit-finding"
  local cmd_qv="python3 nh_loop.py question-validation"
  local old_wording="WHERE THIS ISSUE GOES NEXT: the independent question-validation"
  local f_route="not-checked" f_qv="not-checked" f_wording="not-checked"
  local journal_delta="not-checked"

  # ---- REQUIRED-FACT HELPER. Records a mismatch; can stop nothing. ----------
  _r25_require() {
    local name="$1" actual="$2" expected="$3"
    if [ "$actual" = "$expected" ]; then
      printf '  [ok]   %-46s %s\n' "$name" "$actual"
    else
      printf '  [FAIL] %-46s %s   (Repair 25 requires %s)\n' "$name" "$actual" "$expected"
      fail_count=$((fail_count + 1))
    fi
  }

  if [ "$EXEC_RC" = "NOT-RUN" ] || [ ! -s "$s4" ]; then
    verdict="NOT-EXERCISED"
    reason="Stage 4 never ran, so the Repair-25 stop branch was never reached"
  elif [ "$OBS_S4_STOP_REASON" != '"CHATGPT_REVIEW_REQUIRED"' ]; then
    verdict="NOT-EXERCISED"
    reason="Stage 4 stop_reason is ${OBS_S4_STOP_REASON}, not CHATGPT_REVIEW_REQUIRED"
  else
    verdict="PASS"
    reason="Stage 4 reached CHATGPT_REVIEW_REQUIRED; every Repair-25 seam fact was checked"
    # THE FORBIDDEN IMMEDIATE-COMMAND LINES, from the exact Stage-4 human stdout.
    if grep -q -F -- "$cmd_route" "$s4" 2>/dev/null; then f_route="PRESENT"; else f_route="absent"; fi
    if grep -q -F -- "$cmd_qv"    "$s4" 2>/dev/null; then f_qv="PRESENT";    else f_qv="absent";    fi
    if grep -q -F -- "$old_wording" "$s4" 2>/dev/null; then f_wording="PRESENT"; else f_wording="absent"; fi
  fi

  {
    printf 'REPAIR-25 CHATGPT-STOP HANDOFF OBSERVATION\n'
    printf '  -- read-only, conditional, gates no stage, triggers no piece 3\n'
    printf '=====================================================================\n\n'
    printf 'WHAT REPAIR 25 REQUIRES OF THIS STOP\n'
    printf '  A validated blocking chatgpt_review_required audit finding STOPS the\n'
    printf '  automatic loop and does NOT cross into piece 3. The independent\n'
    printf '  ChatGPT review happens OUTSIDE the controller; only afterwards, and\n'
    printf '  only if that review confirms it, may someone explicitly invoke\n'
    printf '  route-audit-finding -- which re-proves the whole upstream result --\n'
    printf '  and only after that succeeds does question-validation follow.\n\n'
    printf 'CONTROLLER UNDER TEST\n'
    printf '  shadow controller : %s  (accepted Repair 28)\n' "$EXP_R28_SHA"
    printf '  Repair 28 is based on accepted Repair 27B, which is based on\n'
    printf '  Repair 27, which is based on accepted Repair 26, which is based on\n'
    printf '  accepted Repair 25, and it INHERITS the stop behaviour observed\n'
    printf '  below. This observer checks that INHERITED Repair-25 seam;\n'
    printf '  Repair 28 did not invent it.\n'
    printf '  Repair25 preserved : %s  (NOT the refresh source)\n' "$EXP_R25_SHA"
    printf '  Repair27A preserved: %s  (NOT the refresh source)\n' "$EXP_R27A_SHA"
    printf '  Repair27B preserved: %s  (the source controller, NOT the refresh source)\n' "$EXP_R27B_SHA"
    printf '  refresh state     : %s\n\n' "$CONTROLLER_REFRESH"
    printf 'STAGE 4 OUTCOME\n'
    printf '  exit                       %s\n' "$EXEC_RC"
    printf '  stop_reason                %s\n' "$OBS_S4_STOP_REASON"
    printf '  interview_stop_reason      %s\n' "$OBS_S4_INTERVIEW_STOP_REASON"
    printf '  ok                         %s\n\n' "$OBS_S4_OK"
    printf 'CONTROLLER-OWNED STAGE-4 FACTS (recorded, never interpreted)\n'
    printf '  final_design_audit_verdict              %s\n' "$OBS_S4_AUDIT_VERDICT"
    printf '  final_highest_severity                  %s\n' "$OBS_S4_HIGHEST_SEVERITY"
    printf '  design_audit_chatgpt_review_required    %s\n' "$OBS_S4_AUDIT_CHATGPT_REQ"
    printf '  final_chatgpt_review_required           %s\n' "$OBS_S4_FINAL_CHATGPT_REQ"
    printf '  final_blocking_chatgpt_review_required  %s\n' "$OBS_S4_FINAL_BLOCKING_CHATGPT_REQ"
    printf '  chatgpt_independent_audit_performed     %s\n' "$OBS_S4_CHATGPT_AUDIT_PERFORMED"
    printf '  piece3_question_validation_required     %s\n' "$OBS_S4_PIECE3_QV_REQUIRED"
    printf '  piece3_route                            %s\n' "$OBS_S4_PIECE3_ROUTE"
    printf '  piece3_routed_finding_titles            %.400s\n' "$OBS_S4_PIECE3_ROUTED_TITLES"
    printf '  design_audit_routing_provenance         %.400s\n' "$OBS_S4_ROUTING_PROVENANCE"
    printf '  ness_question_asked                     %s\n' "$OBS_S4_NESS_QUESTION_ASKED"
    printf '  ness_decision_manufactured              %s\n' "$OBS_S4_NESS_DECISION_MANUFACTURED"
    printf '  correction_rounds_started               %s\n' "$OBS_S4_ROUNDS_STARTED"
    printf '  correction_rounds_completed             %s\n' "$OBS_S4_ROUNDS_COMPLETED"
    printf '  total_claude_invocations                %s\n' "$OBS_S4_TOTAL_CLAUDE"
    printf '  total_codex_design_audit_invocations    %s\n\n' "$OBS_S4_TOTAL_CODEX_AUDITS"

    if [ "$verdict" = "NOT-EXERCISED" ]; then
      printf 'THE REPAIR-25 STOP BRANCH WAS NOT EXERCISED\n'
      printf '  %s.\n\n' "$reason"
      printf '  THIS IS NOT A FAILURE. The branch is only reachable when a\n'
      printf '  validated design audit carries a BLOCKING finding routed\n'
      printf '  chatgpt_review_required, and whether that happens is entirely the\n'
      printf '  controller\047s and the auditing model\047s business.\n'
      printf '  NOTHING HERE MANUFACTURES ONE. No audit finding is injected, no\n'
      printf '  second case is run, no controller is re-run, and no route command\n'
      printf '  is invoked to force the path. v24 is an integrated rehearsal, not\n'
      printf '  failure injection.\n\n'
    else
      printf 'THE REPAIR-25 REQUIRED SEAM FACTS\n'
      _r25_require "design_audit_chatgpt_review_required" \
                   "$OBS_S4_AUDIT_CHATGPT_REQ" "true"
      _r25_require "final_blocking_chatgpt_review_required" \
                   "$OBS_S4_FINAL_BLOCKING_CHATGPT_REQ" "true"
      _r25_require "chatgpt_independent_audit_performed" \
                   "$OBS_S4_CHATGPT_AUDIT_PERFORMED" "false"
      _r25_require "piece3_question_validation_required" \
                   "$OBS_S4_PIECE3_QV_REQUIRED" "false"
      _r25_require "piece3_route" "$OBS_S4_PIECE3_ROUTE" "null"
      _r25_require "piece3_routed_finding_titles" \
                   "$OBS_S4_PIECE3_ROUTED_TITLES" "[]"
      _r25_require "ness_question_asked" "$OBS_S4_NESS_QUESTION_ASKED" "false"
      _r25_require "ness_decision_manufactured" \
                   "$OBS_S4_NESS_DECISION_MANUFACTURED" "false"
      # The provenance must be a non-null JSON OBJECT. Its presence is evidence
      # for the later manual handoff and is NOT a route: every piece3 field
      # above must still be empty beside it.
      case "$OBS_S4_ROUTING_PROVENANCE" in
        '{'*'}')
          printf '  [ok]   %-46s non-null JSON object\n' "design_audit_routing_provenance" ;;
        *)
          printf '  [FAIL] %-46s %.120s   (Repair 25 requires a non-null JSON object)\n' \
                 "design_audit_routing_provenance" "$OBS_S4_ROUTING_PROVENANCE"
          fail_count=$((fail_count + 1)) ;;
      esac
      printf '\n'
      printf 'THE EXACT STAGE-4 HUMAN STDOUT (the old immediate-command behaviour)\n'
      printf '  Ordinary explanatory prose MAY name route-audit-finding or\n'
      printf '  question-validation while describing the later CONDITIONAL path.\n'
      printf '  That is expected and is not tested. Only these exact immediate\n'
      printf '  command lines and the exact old Repair-24 sentence are forbidden.\n'
      _r25_require "\"${cmd_route}\" line" "$f_route" "absent"
      _r25_require "\"${cmd_qv}\" line"    "$f_qv"    "absent"
      _r25_require "old \"WHERE THIS ISSUE GOES NEXT\" wording" "$f_wording" "absent"
      printf '\n'
      printf 'THIS LAUNCHER\047S OWN BEHAVIOUR ON THIS PATH\n'
      printf '  route-audit-finding invoked by this launcher   : no (no call site)\n'
      printf '  question-validation run by this launcher       : no (no call site)\n'
      printf '  question-coverage-review run by this launcher  : no (no call site)\n'
      printf '  interview-gate run by this launcher            : no (no call site)\n'
      printf '  next-question-group / record-ness-answer       : no (no call site)\n'
      printf '  declare-stranded-candidate                     : no (no call site)\n'
      printf '  a Ness question manufactured by this launcher  : no\n'
      printf '  an audit finding manufactured by this launcher : no\n\n'
      if [ "$fail_count" -gt 0 ]; then
        verdict="FAIL"
        reason="Stage 4 reached CHATGPT_REVIEW_REQUIRED but ${fail_count} required Repair-25 seam fact(s) did not hold"
      fi
    fi

    printf 'THE SHADOW INTERVIEW JOURNAL\n'
    printf '  STATED HONESTLY: this launcher takes NO per-stage snapshot of the\n'
    printf '  SHADOW journal, so no existing snapshot comparison can prove, by\n'
    printf '  itself, that the shadow journal gained no piece-3 routed event\n'
    printf '  during Stage 4. That claim is therefore NOT made here, and no\n'
    printf '  second journal checker is added to manufacture it.\n'
    printf '  WHAT IS PROVED ELSEWHERE, and what actually matters for safety:\n'
    printf '  the REAL interview journal is frozen by identity and re-proved\n'
    printf '  before, during and after every stage by the protected-source proof\n'
    printf '  set, so nothing this run did reached it.\n'
    printf '  The shadow journal is preserved in the disposable lab for direct\n'
    printf '  inspection, exactly as it stands after the run:\n'
    printf '    %s/nh_interview_state/nh_interview_journal.jsonl\n' "$SHADOW_WS"
    printf '  Its final state, read now, from OUTSIDE the namespace:\n'
    printf '    events                            : %s\n' "$(grep -c '[^[:space:]]' -- "${SHADOW_WS}/nh_interview_state/nh_interview_journal.jsonl" 2>/dev/null || printf 'UNAVAILABLE')"
    printf '    sha256                            : %s\n' "$(sha_of "${SHADOW_WS}/nh_interview_state/nh_interview_journal.jsonl" 2>/dev/null || printf 'UNAVAILABLE')"
    printf '    routed_issue_recorded occurrences : %s\n' "$(grep -c -F -- 'routed_issue_recorded' "${SHADOW_WS}/nh_interview_state/nh_interview_journal.jsonl" 2>/dev/null || printf '0')"
    printf '  The continuation source carried %s events before this run.\n' "$EXP_CONT_JOURNAL_EVENTS"
    printf '  These numbers are RECORDED, not interpreted. This launcher draws\n'
    printf '  no conclusion from them and no verdict anywhere depends on them.\n\n'
    printf 'REPAIR25_CHATGPT_STOP_HANDOFF = %s\n' "$verdict"
    printf '  reason: %s\n\n' "$reason"
    printf 'HOW TO READ THIS VERDICT\n'
    printf '  PASS           Stage 4 reached CHATGPT_REVIEW_REQUIRED and every\n'
    printf '                 required Repair-25 seam fact held.\n'
    printf '  FAIL           Stage 4 reached CHATGPT_REVIEW_REQUIRED and at least\n'
    printf '                 one required seam fact contradicted Repair 25.\n'
    printf '  NOT-EXERCISED  Stage 4 ended for another reason, including a full\n'
    printf '                 PASS. THIS IS NOT A LAUNCHER FAILURE.\n'
    printf '  NOT-RUN        this observation never ran at all.\n'
    printf '  This verdict gates no stage, unlocks nothing, and is not a\n'
    printf '  judgement about N.H, about any candidate, or about acceptance.\n'
  } > "$out" 2>&1 || true

  REPAIR25_CHATGPT_STOP_HANDOFF="$verdict"
  printf '%s\n' "REPAIR25_CHATGPT_STOP_HANDOFF=${verdict}"
  printf '%s\n' "  ${reason}"
}

observe_repair25_chatgpt_stop_handoff || true

# ==========================================================================
# SECTION 12 — RE-PROVE THE ORIGINAL, FROM OUTSIDE THE NAMESPACE
# ==========================================================================
#
# This runs REGARDLESS of how the four stages went -- whether stage 1 failed
# technically and stages 2, 3 and 4 never ran, whether a later stage declined to
# permit continuation, whether the gate stayed closed, or whether the controller
# ran to completion and returned any code at all. The ordinary success or failure
# of the controller has no bearing on whether the protected original must be
# re-proved. It always must.

step "ORIGINAL PROOF (AFTER)"

capture_original_proof "${PROOF}/original.after"

ORIGINAL_PROOF="PASS"
if ! compare_proof_set "${PROOF}/original.before" "${PROOF}/original.after" "after" \
        "${PROTECTED_PROOF_FILES[@]}"; then
  ORIGINAL_PROOF="FAIL"
fi

PRESERVED_LAB_PROOF="PASS"
if ! compare_proof_set "${PROOF}/original.before" "${PROOF}/original.after" "after-labs" \
        "${PRESERVED_LAB_PROOF_FILES[@]}"; then
  PRESERVED_LAB_PROOF="FAIL"
fi

REGRESSION_SEED_PROOF="PASS"
if ! compare_proof_set "${PROOF}/original.before" "${PROOF}/original.after" "after-seed" \
        "${REGRESSION_SEED_PROOF_FILES[@]}"; then
  REGRESSION_SEED_PROOF="FAIL"
fi

CONTINUATION_SOURCE_PROOF="PASS"
if ! compare_proof_set "${PROOF}/original.before" "${PROOF}/original.after" "after-cont" \
        "${CONTINUATION_SOURCE_PROOF_FILES[@]}"; then
  CONTINUATION_SOURCE_PROOF="FAIL"
fi

# All four containment verdicts are SETTLED at this exact point, so the flag is
# raised here and not one line later.
#
# Everything below -- the host credential witness, the summary -- is separate and
# lesser. If any of it aborts unexpectedly, the report must still state the
# verdicts this launcher genuinely holds. Raising the flag after those steps
# would let an abort in a lesser check downgrade a real verdict back to "not
# re-proved", which would hide a real ORIGINAL_WORKSPACE_PROOF=FAIL behind
# "unverified" -- the most dangerous possible misreport for this launcher.
AFTER_PROOF_DONE=1

CREDENTIAL_WITNESS="UNCHANGED"
if ! compare_proof_set "${PROOF}/original.before" "${PROOF}/original.after" "after-cred" \
        "${CREDENTIAL_PROOF_FILES[@]}"; then
  CREDENTIAL_WITNESS="CHANGED"
fi
# A witness that could not be taken is not a witness that came back unchanged,
# and it must not be reported as one. This outranks CHANGED: if the capture was
# incomplete, "CHANGED" would itself be an unfounded claim.
if [ -s "${PROOF}/original.before/credentials.errors" ] \
   || [ -s "${PROOF}/original.during/credentials.errors" ] \
   || [ -s "${PROOF}/original.after/credentials.errors" ]; then
  CREDENTIAL_WITNESS="CAPTURE-FAILED"
fi

# What the run may have left in the lab. This is a different question from the
# host credential witness above: the host files can be perfectly UNCHANGED while
# a sandboxed stage has copied or echoed their contents into the lab, which is
# writable by design. Only a post-run scan can settle it.
POST_SCAN_RC=0
scan_lab_for_credentials "${PROOF}/credential-scan.after.txt" || POST_SCAN_RC=$?
case "$POST_SCAN_RC" in
  0) LAB_CREDENTIAL_SCAN="NO-KNOWN-MARKERS" ;;
  1) LAB_CREDENTIAL_SCAN="FOUND" ;;
  *) LAB_CREDENTIAL_SCAN="SCAN-FAILED" ;;
esac

# ==========================================================================
# SECTION 13 — SUMMARY
# ==========================================================================

# This summary IS the report, so the exit handler must not print a second one.
REPORTED=1

printf '\n'
printf '===========================================================\n'
printf 'N.H SHADOW REHEARSAL (v24, ACCEPTED REPAIR-28, STAGE-4-ONLY CONTINUATION) — RESULT\n'
printf '===========================================================\n'
printf 'LAUNCHER=%s\n'                          "$LAUNCHER_V24_BASENAME"
printf 'SHADOW_LAB=%s\n'                        "$LAB"
printf 'RUN_KIND=STAGE_4_ONLY_CONTINUATION_OF_THE_COMPLETED_V21_SHADOW\n'
printf 'CONTINUATION_SOURCE=%s\n'               "$CONTINUATION_SOURCE"
printf 'CONTINUATION_SOURCE_MODE=%s\n'          "$CONTINUATION_SOURCE_MODE"
printf 'CONTINUATION_SOURCE_LAB=%s\n'           "$PRESERVED_LAB_REPAIR27B_V21"
printf 'CONTINUATION_SOURCE_IS_ALSO_PRESERVED_EVIDENCE=YES\n'
printf 'CONTINUATION_SOURCE_EVER_A_WRITE_DESTINATION=NO\n'
printf 'HISTORICAL_LINEAGE_SEED=%s\n'           "$REGRESSION_SOURCE"
printf 'HISTORICAL_LINEAGE_SEED_MODE=%s\n'      "$REGRESSION_SOURCE_MODE"
printf 'HISTORICAL_LINEAGE_SEED_COPIED_IN_V24=NO\n'
printf '\n'
printf 'FROZEN_REAL_CONTROLLER_SHA256=%s\n'     "$EXP_LOOP_SHA"
printf 'REAL_CONTROLLER_INSTALLED_REPAIR27B=NO\n'
printf 'REAL_CONTROLLER_INSTALLED_REPAIR27A=NO\n'
printf 'REAL_CONTROLLER_INSTALLED_REPAIR27=NO\n'
printf 'REAL_CONTROLLER_INSTALLED_REPAIR26=NO\n'
printf 'REAL_CONTROLLER_INSTALLED_REPAIR25=NO\n'
printf 'REAL_CONTROLLER_INSTALLED_REPAIR24=NO\n'
printf 'REAL_CONTROLLER_INSTALLED_REPAIR23=NO\n'
printf 'REAL_CONTROLLER_INSTALLED_REPAIR22=NO\n'
printf 'REAL_CONTROLLER_INSTALLED_REPAIR21=NO\n'
printf 'REAL_CONTROLLER_INSTALLED_REPAIR20B=NO\n'
printf 'REPAIR28_ACCEPTED_BY_NESS=YES\n'
printf 'REPAIR28_ACCEPTANCE_AUTHORISES_ONLY_THIS_SHADOW_REFRESH=YES\n'
printf 'REPAIR28_ACCEPTANCE_ALONE_DID_NOT_AUTHORISE_A_LIVE_RUN=YES\n'
printf 'REPAIR28_INSTALLED=NO\n'
printf 'REAL_CONTROLLER_INSTALLED_REPAIR28=NO\n'
printf 'NH_ADOPTION_OR_ACCEPTANCE_PERFORMED=NO\n'
printf 'SHADOW_CONTROLLER_UNDER_TEST=REPAIR28\n'
printf 'SHADOW_CONTROLLER_SHA256=%s\n'          "$EXP_R28_SHA"
printf 'SHADOW_CONTROLLER_SOURCE=%s\n'          "$R28_CANDIDATE"
printf 'SHADOW_REFRESH_SOURCE_IS_REPAIR28_ONLY=YES\n'
printf 'SOURCE_CONTROLLER=REPAIR27B\n'
printf 'SOURCE_CONTROLLER_SHA256=%s\n'          "$EXP_R27B_SHA"
printf 'CONTROLLER_REFRESH_TRANSITION=REPAIR27B_TO_REPAIR28\n'
printf 'REPAIR28_IS_BASED_ON_ACCEPTED_REPAIR27B=YES\n'
printf 'REPAIR27B_IS_BASED_ON_ACCEPTED_REPAIR27A=YES\n'
printf 'REPAIR27A_IS_BASED_ON_REPAIR27=YES\n'
printf 'REPAIR27_IS_BASED_ON_ACCEPTED_REPAIR26=YES\n'
printf 'REPAIR26_IS_BASED_ON_ACCEPTED_REPAIR25=YES\n'
printf 'REPAIR28_KNOWN_MANUAL_ROUTE_AUDIT_PROVENANCE_DEPENDENCY=OPEN\n'
printf 'REPAIR20B_PRESERVED_SHA256=%s\n'        "$EXP_R20B_SHA"
printf 'REPAIR20B_USED_AS_REFRESH_SOURCE=NO\n'
printf 'REPAIR21_PRESERVED_SHA256=%s\n'         "$EXP_R21_SHA"
printf 'REPAIR21_USED_AS_REFRESH_SOURCE=NO\n'
printf 'REPAIR22_PRESERVED_SHA256=%s\n'         "$EXP_R22_SHA"
printf 'REPAIR22_USED_AS_REFRESH_SOURCE=NO\n'
printf 'REPAIR23_PRESERVED_SHA256=%s\n'         "$EXP_R23_SHA"
printf 'REPAIR23_USED_AS_REFRESH_SOURCE=NO\n'
printf 'REPAIR24_PRESERVED_SHA256=%s\n'         "$EXP_R24_SHA"
printf 'REPAIR24_USED_AS_REFRESH_SOURCE=NO\n'
printf 'REPAIR25_PRESERVED_SHA256=%s\n'         "$EXP_R25_SHA"
printf 'REPAIR25_USED_AS_REFRESH_SOURCE=NO\n'
printf 'REPAIR26_PRESERVED_SHA256=%s\n'         "$EXP_R26_SHA"
printf 'REPAIR26_USED_AS_REFRESH_SOURCE=NO\n'
printf 'REPAIR27_PRESERVED_SHA256=%s\n'         "$EXP_R27_SHA"
printf 'REPAIR27_USED_AS_REFRESH_SOURCE=NO\n'
printf 'REPAIR27A_PRESERVED_SHA256=%s\n'        "$EXP_R27A_SHA"
printf 'REPAIR27B_PRESERVED_SHA256=%s\n'        "$EXP_R27B_SHA"
printf 'REPAIR27A_USED_AS_REFRESH_SOURCE=NO\n'
printf 'REPAIR27B_USED_AS_REFRESH_SOURCE=NO\n'
printf 'REPAIR27B_IS_THE_CONTROLLER_THE_CONTINUATION_SOURCE_CARRIED=YES\n'
printf 'REPAIR27A_IS_THE_CONTROLLER_THE_SOURCE_CARRIED=NO\n'
printf '\n'
printf 'PREDECESSOR_LAUNCHER=%s\n'              "$LAUNCHER_V23_BASENAME"
printf 'PREDECESSOR_LAUNCHER_SHA256=%s\n'       "$EXP_LAUNCHER_V22_SHA"
printf 'PREDECESSOR_LAUNCHER_BYTES=%s\n'        "$EXP_LAUNCHER_V22_BYTES"
printf 'PREDECESSOR_LAUNCHER_WAS_RUN=NO\n'
printf 'PREDECESSOR_LAB=NONE_V23_WAS_NOT_RUN\n'
printf '\n'
printf 'CONTINUATION_SOURCE_RUN_LAUNCHER=%s\n'  "$LAUNCHER_V21_BASENAME"
printf 'CONTINUATION_SOURCE_RUN_LAUNCHER_SHA256=%s\n' "$EXP_LAUNCHER_V21_SHA"
printf 'CONTINUATION_SOURCE_RUN_WAS_RUN=YES\n'
printf 'V21_RESULT_AUTHENTICATED=%s\n'          "$V21_RESULT_AUTHENTICATED"
printf 'V21_STAGE4_EXECUTE_EXIT=%s\n'           "$EXP_V21_S4_EXIT"
printf 'V21_STAGE4_STDOUT_BYTES=%s\n'           "$EXP_V21_S4_STDOUT_BYTES"
printf 'V21_STAGE4_WAS_A_STOP_NOT_A_CRASH=YES\n'
printf 'V21_STAGE4_STOP_REASON=%s\n'            "$EXP_V21_S4_STOP_REASON"
printf 'V21_CORRECTION_ROUNDS_STARTED=%s\n'     "$EXP_V21_S4_ROUNDS_STARTED"
printf 'V21_CORRECTION_ROUNDS_COMPLETED=%s\n'   "$EXP_V21_S4_ROUNDS_COMPLETED"
printf 'V21_LAB_IS_THIS_RUN_CONTINUATION_SOURCE=YES\n'
printf 'V21_LAB_REUSED=NO\n'
printf 'V21_LAB_WRITTEN_TO=NO\n'
printf '\n'
printf 'ANCESTOR_DOORS_EVIDENCE_LAUNCHER=%s\n'  "$LAUNCHER_V20_BASENAME"
printf 'V20_RESULT_AUTHENTICATED=%s\n'          "$V20_RESULT_AUTHENTICATED"
printf 'V20_STAGE1_QUESTION_VALIDATION_EXIT=%s\n'   "$EXP_V20_S1_EXIT"
printf 'V20_STAGE1_OK=true\n'
printf 'V20_STAGE1_VALIDATION_INVENTORY_COMPLETE=true\n'
printf 'V20_STAGE1_MATERIAL_UNKNOWNS=[]\n'
printf 'V20_STAGE1_DELIVERABLE_QUESTION_COUNT=0\n'
printf 'V20_STAGE2_COVERAGE_REVIEW_EXIT=%s\n'       "$EXP_V20_S2_EXIT"
printf 'V20_STAGE2_COVERAGE_REVIEW_CLEARED=true\n'
printf 'V20_STAGE2_COVERAGE_POSSIBLE_GAPS=0\n'
printf 'V20_STAGE3_INTERVIEW_GATE_EXIT=%s\n'        "$EXP_V20_S3_EXIT"
printf 'V20_STAGE3_MECHANICAL_PATH_UNLOCKED=true\n'
printf 'V20_STAGE4_EXECUTE_EXIT=%s\n'               "$EXP_V20_S4_EXIT"
printf 'V20_STAGE4_STDOUT_BYTES=%s\n'               "$EXP_V20_S4_STDOUT_BYTES"
printf 'V20_STAGE4_WAS_A_CRASH_NOT_A_STOP=YES\n'
printf 'V20_STAGE4_CRASH_SUBSCRIPT=%s\n'            "$EXP_V20_S4_CRASH_SUBSCRIPT"
printf 'V20_STAGE4_CRASH_TYPE=%s\n'                 "$EXP_V20_S4_CRASH_TYPE"
printf 'V20_ALL_FOUR_STAGE_SOURCE_PROOFS=%s\n'      "$EXP_V20_SOURCE_PROOF_VALUE"
printf 'V20_LAB_REUSED=NO\n'
printf 'V20_LAB_WRITTEN_TO=NO\n'
printf 'V20_LAB_IS_THIS_RUN_CONTINUATION_SOURCE=NO\n'
printf 'V20_LAB_IS_PRESERVED_ANCESTOR_DOORS_EVIDENCE=YES\n'
printf '\n'
printf 'DOORS_1_TO_3_RERUN_BY_V24=NO\n'
printf 'DOOR1_QUESTION_VALIDATION_STAGE_EXISTS_IN_V24=NO\n'
printf 'DOOR2_QUESTION_COVERAGE_REVIEW_STAGE_EXISTS_IN_V24=NO\n'
printf 'DOOR3_INTERVIEW_GATE_STAGE_EXISTS_IN_V24=NO\n'
printf 'DOORS_1_TO_3_CLEARANCE_CARRIED_FORWARD_IN_THE_JOURNAL=YES\n'
printf 'CONTROLLER_STILL_ENFORCES_ITS_OWN_PIECE3_CLEARANCE=YES\n'
printf 'OUTER_CONTROLLER_STAGES_EXECUTED=1\n'
printf 'OUTER_RETRY_EXISTS=NO\n'
printf 'CONTROLLER_INTERNAL_CORRECTION_LOOP_OWNED_BY_NH_LOOP=YES\n'
printf 'CONTROLLER_INTERNAL_CORRECTION_ROUND_LIMIT=5\n'
printf '\n'
printf 'SEED_CONTROLLER_SHA256=%s\n'            "$EXP_SEED_LOOP_SHA"
printf 'CONTINUATION_CONTROLLER_SHA256=%s\n'    "$EXP_CONT_LOOP_SHA"
printf 'CONTROLLER_REFRESH=%s\n'                "$CONTROLLER_REFRESH"
printf 'CONTINUATION_STATE=%s\n'                "$CONTINUATION_STATE"
printf 'CONTINUATION_JOURNAL_EVENTS=%s\n'       "$EXP_CONT_JOURNAL_EVENTS"
printf 'CONTINUATION_LAST_EVENT_TYPE=%s\n'      "$EXP_CONT_EVENT9_TYPE"
printf 'CONTINUATION_VALIDATION_SET_ID=%s\n'    "$EXP_CONT_EVENT9_VALIDATION_SET_ID"
printf 'ROUTED_SIGNAL=%s\n'                     "$EXP_ROUTED_SIGNAL_ID"
printf 'STANDING_TARGET=%s\n'                   "$EXP_STANDING_TARGET_ID"
printf 'PACKAGE_SCOPE=%s\n'                     "$EXP_PKG_SCOPE"
printf '\n'
printf 'CONTINUATION_MANIFEST_EXPECTATION_SOURCE=CONSTRUCTION_TIME_FROZEN_DIGEST\n'
printf 'CONTINUATION_MANIFEST_SHA256=%s\n'      "$EXP_CONT_MANIFEST_SHA"
printf 'CONTINUATION_MANIFEST_ENTRIES=%s\n'     "$EXP_CONT_MANIFEST_ENTRIES"
printf 'CONTINUATION_MANIFEST_FILES=%s\n'       "$EXP_CONT_MANIFEST_FILES"
printf 'CONTINUATION_MANIFEST_DIRS=%s\n'        "$EXP_CONT_MANIFEST_DIRS"
printf 'CONTINUATION_MANIFEST_SYMLINKS=%s\n'    "$EXP_CONT_MANIFEST_SYMLINKS"
printf 'HISTORICAL_SEED_EXPECTATION_SOURCE=PRESERVED_V11_WITNESSES\n'
printf 'HISTORICAL_SEED_EXPECTATION_FROM_CURRENT_SEED=NO\n'
printf 'HISTORICAL_SEED_MANIFEST_SHA256=%s\n'   "$EXP_HIST_SEED_MANIFEST_SHA"
printf 'HISTORICAL_SEED_MANIFEST_ENTRIES=%s\n'  "$EXP_HIST_SEED_MANIFEST_ENTRIES"
printf 'HISTORICAL_SEED_MANIFEST_FILES=%s\n'    "$EXP_HIST_SEED_MANIFEST_FILES"
printf 'HISTORICAL_SEED_MANIFEST_DIRS=%s\n'     "$EXP_HIST_SEED_MANIFEST_DIRS"
printf 'HISTORICAL_SEED_MANIFEST_SYMLINKS=%s\n' "$EXP_HIST_SEED_MANIFEST_SYMLINKS"
printf '\n'
printf 'STAGE4_EXECUTE_EXIT=%s\n'               "$EXEC_RC"
printf 'STAGE4_OK=%s\n'                         "$OBS_S4_OK"
printf 'STAGE4_STOP_REASON=%s\n'                "$OBS_S4_STOP_REASON"
printf 'STAGE4_INTERVIEW_STOP_REASON=%s\n'      "$OBS_S4_INTERVIEW_STOP_REASON"
printf '\n'
printf 'STAGE4_FINAL_DESIGN_AUDIT_VERDICT=%s\n'             "$OBS_S4_AUDIT_VERDICT"
printf 'STAGE4_FINAL_HIGHEST_SEVERITY=%s\n'                 "$OBS_S4_HIGHEST_SEVERITY"
printf 'STAGE4_DESIGN_AUDIT_CHATGPT_REVIEW_REQUIRED=%s\n'   "$OBS_S4_AUDIT_CHATGPT_REQ"
printf 'STAGE4_FINAL_CHATGPT_REVIEW_REQUIRED=%s\n'          "$OBS_S4_FINAL_CHATGPT_REQ"
printf 'STAGE4_FINAL_BLOCKING_CHATGPT_REVIEW_REQUIRED=%s\n' "$OBS_S4_FINAL_BLOCKING_CHATGPT_REQ"
printf 'STAGE4_CHATGPT_INDEPENDENT_AUDIT_PERFORMED=%s\n'    "$OBS_S4_CHATGPT_AUDIT_PERFORMED"
printf 'STAGE4_PIECE3_QUESTION_VALIDATION_REQUIRED=%s\n'    "$OBS_S4_PIECE3_QV_REQUIRED"
printf 'STAGE4_PIECE3_ROUTE=%s\n'                           "$OBS_S4_PIECE3_ROUTE"
printf 'STAGE4_PIECE3_ROUTED_FINDING_TITLES=%.400s\n'       "$OBS_S4_PIECE3_ROUTED_TITLES"
printf 'STAGE4_DESIGN_AUDIT_ROUTING_PROVENANCE=%.400s\n'    "$OBS_S4_ROUTING_PROVENANCE"
printf 'STAGE4_NESS_QUESTION_ASKED=%s\n'                    "$OBS_S4_NESS_QUESTION_ASKED"
printf 'STAGE4_NESS_DECISION_MANUFACTURED=%s\n'             "$OBS_S4_NESS_DECISION_MANUFACTURED"
printf 'STAGE4_CORRECTION_ROUNDS_STARTED=%s\n'              "$OBS_S4_ROUNDS_STARTED"
printf 'STAGE4_CORRECTION_ROUNDS_COMPLETED=%s\n'            "$OBS_S4_ROUNDS_COMPLETED"
printf 'STAGE4_TOTAL_CLAUDE_INVOCATIONS=%s\n'               "$OBS_S4_TOTAL_CLAUDE"
printf 'STAGE4_TOTAL_CODEX_DESIGN_AUDIT_INVOCATIONS=%s\n'   "$OBS_S4_TOTAL_CODEX_AUDITS"
printf '\n'
printf 'STAGE4_PIECE3_INTERVIEW_GATE_ENFORCED=%s\n'         "$OBS_S4_PIECE3_GATE_ENFORCED"
printf 'STAGE4_PIECE3_INTERVIEW_GATE_UNLOCKED=%s\n'         "$OBS_S4_PIECE3_GATE_UNLOCKED"
printf 'STAGE4_PREPARATION_OK=%s\n'                         "$OBS_S4_PREPARATION_OK"
printf 'STAGE4_TASK_READY=%s\n'                             "$OBS_S4_TASK_READY"
printf 'STAGE4_NOT_READY_REASON=%.400s\n'                   "$OBS_S4_NOT_READY_REASON"
printf 'STAGE4_MECHANICAL_DESIGN_SPECIFICATION_SHA256=%s\n' "$OBS_S4_MDS_SHA"
printf 'STAGE4_MECHANICAL_DESIGN_REQUIREMENT_COUNT=%s\n'    "$OBS_S4_MDS_REQ_COUNT"
printf 'ABSENT_FIELDS_ARE_REPORTED_UNAVAILABLE_NEVER_INVENTED=YES\n'
printf 'LONG_FIELDS_TRUNCATED_FOR_DISPLAY=YES\n'
printf '\n'
printf 'REPAIR25_CHATGPT_STOP_HANDOFF=%s\n'     "$REPAIR25_CHATGPT_STOP_HANDOFF"
printf 'REPAIR25_HANDOFF_IS_AN_INHERITED_SEAM_UNDER_REPAIR28=YES\n'
printf 'REPAIR25_HANDOFF_NOT_EXERCISED_IS_NOT_A_FAILURE=YES\n'
printf 'REPAIR25_HANDOFF_OBSERVATION_GATES_NO_STAGE=YES\n'
printf 'V24_INJECTED_A_FINDING_TO_FORCE_THE_BRANCH=NO\n'
printf 'V24_INVOKED_ROUTE_AUDIT_FINDING=NO\n'
printf 'V24_INVOKED_QUESTION_VALIDATION=NO\n'
printf 'V24_INVOKED_QUESTION_COVERAGE_REVIEW=NO\n'
printf 'V24_INVOKED_INTERVIEW_GATE=NO\n'
printf 'V24_INVOKED_NEXT_QUESTION_GROUP=NO\n'
printf 'V24_INVOKED_RECORD_NESS_ANSWER=NO\n'
printf 'V24_INVOKED_DECLARE_STRANDED_CANDIDATE=NO\n'
printf 'V24_MANUFACTURED_A_NESS_QUESTION=NO\n'
printf 'V24_MANUFACTURED_A_FINDING=NO\n'
printf '\n'
printf 'SEQUENCE_STOP_REASON=%s\n'              "${SEQUENCE_STOP_REASON:-none}"
printf 'SHADOW_CONTROLLER_EXIT=%s\n'            "$SHADOW_RC"
printf '\n'
printf 'ORIGINAL_WORKSPACE_PROOF=%s\n'          "$ORIGINAL_PROOF"
printf 'PRESERVED_LAB_PROOF=%s\n'               "$PRESERVED_LAB_PROOF"
printf 'REGRESSION_SEED_PROOF=%s\n'             "$REGRESSION_SEED_PROOF"
printf 'CONTINUATION_SOURCE_PROOF=%s\n'         "$CONTINUATION_SOURCE_PROOF"
printf 'HOST_CREDENTIAL_WITNESS=%s\n'           "$CREDENTIAL_WITNESS"
printf 'LAB_CREDENTIAL_SCAN=%s\n'               "$LAB_CREDENTIAL_SCAN"
printf '\n'
for _slug in "${ALL_STAGE_SLUGS[@]}"; do
  printf 'STAGE_%s_COMMAND=%s\n'     "$_slug" "${PROOF}/${_slug}.command"
  printf 'STAGE_%s_STDOUT=%s\n'      "$_slug" "${PROOF}/${_slug}.stdout"
  printf 'STAGE_%s_STDERR=%s\n'      "$_slug" "${PROOF}/${_slug}.stderr"
  printf 'STAGE_%s_EXIT_CODE=%s\n'   "$_slug" "${PROOF}/${_slug}.exit-code"
  printf 'STAGE_%s_SOURCE_PROOF=%s\n' "$_slug" "${PROOF}/${_slug}.source-proof"
done
unset _slug
printf '\n'
printf 'PROOF_ORIGINAL_BEFORE=%s\n'                  "${PROOF}/original.before"
printf 'PROOF_ORIGINAL_DURING=%s\n'                  "${PROOF}/original.during"
printf 'PROOF_ORIGINAL_AFTER_STAGE4=%s\n'            "${PROOF}/original.after-${STAGE4_SLUG}"
printf 'PROOF_ORIGINAL_AFTER=%s\n'                   "${PROOF}/original.after"
printf 'PROOF_V20_RESULT_AUTHENTICATION=%s\n'        "${PROOF}/v20-result-authentication.txt"
printf 'PROOF_V21_RESULT_AUTHENTICATION=%s\n'        "${PROOF}/v21-result-authentication.txt"
printf 'PROOF_CONTINUATION_SOURCE_IDENTITY=%s\n'     "${PROOF}/continuation-source-identity.txt"
printf 'PROOF_CONTINUATION_SOURCE_AUTHENTICATION=%s\n' "${PROOF}/continuation-source-authentication.txt"
printf 'PROOF_CONTINUATION_SOURCE_MANIFEST=%s\n'     "${PROOF}/continuation-source-manifest.txt"
printf 'PROOF_CONTINUATION_SOURCE_UNMOVED=%s\n'      "${PROOF}/continuation-source-unmoved.txt"
printf 'PROOF_REGRESSION_SEED_AUTHENTICATION=%s\n'   "${PROOF}/regression-seed-authentication.txt"
printf 'PROOF_REGRESSION_SEED_IDENTITY=%s\n'         "${PROOF}/regression-seed-identity.txt"
printf 'PROOF_REGRESSION_SEED_UNMOVED=%s\n'          "${PROOF}/regression-seed-unmoved.txt"
printf 'PROOF_REGRESSION_SEED_HISTORICAL_WITNESS=%s\n'  "${PROOF}/regression-seed-historical-witness.txt"
printf 'PROOF_REGRESSION_SEED_HISTORICAL_MANIFEST=%s\n' "${PROOF}/regression-seed-historical-manifest.txt"
printf 'PROOF_CONTROLLER_REFRESH_BEFORE=%s\n'        "${PROOF}/controller-refresh.before"
printf 'PROOF_CONTROLLER_REFRESH_AFTER=%s\n'         "${PROOF}/controller-refresh.after"
printf 'PROOF_CONTROLLER_REFRESH_COMPOSITE=%s\n'     "${PROOF}/controller-refresh.composite"
printf 'PROOF_ISOLATION_SELFTEST=%s\n'               "${PROOF}/isolation-selftest.txt"
printf 'PROOF_CREDENTIAL_SCAN_BEFORE=%s\n'           "${PROOF}/credential-scan.before.txt"
printf 'PROOF_CREDENTIAL_SCAN_AFTER=%s\n'            "${PROOF}/credential-scan.after.txt"
printf 'PROOF_CONTROLLER_OBSERVATIONS=%s\n'          "${PROOF}/controller-observations.txt"
printf 'PROOF_V24_OBSERVATIONS=%s\n'                 "${PROOF}/v24-stage-observations.txt"
printf 'PROOF_REPAIR25_CHATGPT_STOP_HANDOFF=%s\n'    "${PROOF}/repair25-chatgpt-stop-handoff.txt"
printf '===========================================================\n'

printf '\nSHADOW_CONTROLLER_EXIT is the status of the one stage that ran, and\n'
printf 'nothing more. NOT-RUN would mean the launcher stopped before the stage;\n'
printf 'IT IS NOT A PASS AND IT IS NOT A FAILURE.\n'

printf '\nAN EXIT OF 0 IS NOT A VERDICT ABOUT N.H. Every fact above is the\n'
printf 'controller quoted verbatim. A field the controller did not report is\n'
printf 'printed as UNAVAILABLE and is never given an invented value; a stage that\n'
printf 'never ran is printed as NOT-RUN.\n'

printf '\nWHY THIS CONTINUATION SKIPS NO DOOR\n'
printf '  This run is v23. It continues the completed v21 shadow, and the Doors\n'
printf '  were never its to run.\n'
printf '  question-validation, question-coverage-review and interview-gate were\n'
printf '  RUN by v20, for real, against this exact state, with two real GPT\n'
printf '  reviews, and all three passed. That result was authenticated here from\n'
printf '  v20\047s own preserved artefacts -- twice: by exact frozen digest and by\n'
printf '  re-reading the controller\047s own reported fields -- before anything was\n'
printf '  copied. Their outcome is carried forward inside the continuation\n'
printf '  source\047s nine-event authenticated interview journal, whose ninth event\n'
printf '  is the coverage-review clearance itself, and that journal was copied\n'
printf '  byte-identically and never refreshed.\n'
printf '  V20_RESULT_AUTHENTICATED above is that gate\047s verdict. If it had not\n'
printf '  passed, this launcher would have refused before the lab was created.\n'
printf '  AND THE CONTROLLER STILL ENFORCED ITS OWN GATE. execute-next-claude-task\n'
printf '  performs its own Piece-3 clearance and its own source re-proofs on every\n'
printf '  invocation; nothing here bypassed, relaxed, pre-answered or replaced any\n'
printf '  of them.\n'

if [ "$ORIGINAL_PROOF" = "FAIL" ]; then
  printf '\nThe protected ORIGINAL workspace changed during the rehearsal.\n'
  printf 'Isolation did not hold. See the DIFF.after.* files under:\n'
  printf '  %s\n' "$PROOF"
fi

if [ "$PRESERVED_LAB_PROOF" = "FAIL" ]; then
  printf '\nA PRESERVED earlier lab changed during this run. That is preserved\n'
  printf 'evidence and it must never move. See the DIFF.after-labs.* files under:\n'
  printf '  %s\n' "$PROOF"
fi

if [ "$REGRESSION_SEED_PROOF" = "FAIL" ]; then
  printf '\nTHE HISTORICAL LINEAGE SEED CHANGED DURING THIS RUN. It is the lineage\n'
  printf 'root of the state being continued and it must never move. See the\n'
  printf 'DIFF.after-seed.* files under:\n'
  printf '  %s\n' "$PROOF"
fi

if [ "$CONTINUATION_SOURCE_PROOF" = "FAIL" ]; then
  printf '\nTHE CONTINUATION SOURCE CHANGED DURING THIS RUN. The completed v21\n'
  printf 'shadow this whole continuation depends on must never move, and a change\n'
  printf 'to it outranks any apparent controller result. See the DIFF.after-cont.*\n'
  printf 'files under:\n'
  printf '  %s\n' "$PROOF"
fi

if [ "$LAB_CREDENTIAL_SCAN" = "FOUND" ]; then
  printf '\nModel login material was found inside the persistent lab AFTER the\n'
  printf 'run. The lab is mode 0700 and nothing has been deleted. The exact\n'
  printf 'paths -- never the contents -- are listed in:\n'
  printf '  %s\n' "${PROOF}/credential-scan.after.txt"
  printf 'Treat the lab as sensitive, review it, then delete it.\n'
fi

if [ "$LAB_CREDENTIAL_SCAN" = "SCAN-FAILED" ]; then
  printf '\nThe post-run scan of the lab for model login material did NOT\n'
  printf 'complete. This is NOT a clean result: nothing is known either way.\n'
  printf 'See:\n'
  printf '  %s\n' "${PROOF}/credential-scan.after.txt.errors"
  printf 'Treat the lab as sensitive until it has been inspected by hand.\n'
fi

if [ "$CREDENTIAL_WITNESS" = "CHANGED" ]; then
  printf '\nHost model-auth/config files changed during the run. See the\n'
  printf 'DIFF.after-cred.* files under:\n'
  printf '  %s\n' "$PROOF"
  printf 'If another Claude Code or Codex session was running on this host, that\n'
  printf 'session rewrites ~/.claude.json and ~/.claude/* on its own and this is\n'
  printf 'expected. Otherwise treat it as an isolation finding and investigate.\n'
fi

if [ "$CREDENTIAL_WITNESS" = "CAPTURE-FAILED" ]; then
  printf '\nThe host model-auth/config witness could not be taken completely, so\n'
  printf 'NOTHING is claimed about whether those files moved. See the\n'
  printf 'credentials.errors files under:\n'
  printf '  %s\n' "${PROOF}/original.before"
  printf '  %s\n' "${PROOF}/original.after"
fi

printf '\nSCOPE OF THIS RESULT\n'
printf '  This was validation only, in a disposable laboratory.\n'
printf '  A controller PASS means ONLY that the isolated real rehearsal reached\n'
printf '  its own PASS. It is NOT N.H acceptance and NOT adoption of any\n'
printf '  candidate. No N.H policy was created. Nothing was integrated into\n'
printf '  Master or Map. All results live only in the lab.\n'
printf '\n  Every question record, coverage record, routed signal, candidate and\n'
printf '  GPT/Claude output this run produced exists ONLY inside the disposable\n'
printf '  shadow. The real workspace was re-proved from outside the namespace\n'
printf '  after the run, and that verdict is ORIGINAL_WORKSPACE_PROOF above.\n'
printf '\n  THREE SOURCES WERE KEPT SEPARATE AND NONE WAS RECONCILED WITH ANOTHER.\n'
printf '  The CONTINUATION SOURCE is the completed v21 shadow -- the exact state\n'
printf '  the Repair-27B CLAUDE_SPECIFICATION_STOP happened in, and the only\n'
printf '  thing copied. The\n'
printf '  HISTORICAL LINEAGE SEED is the preserved v10 shadow that pre-dates the\n'
printf '  false v11 question; it was authenticated, proved whole against the\n'
printf '  preserved v11 witness, and NEVER COPIED in v24. The PROTECTED ORIGINAL\n'
printf '  is today\047s real workspace, independently frozen and independently\n'
printf '  proved. No two of the three were ever compared to each other, nothing\n'
printf '  was reset, reverted, checked out, cleaned or copied back, and no Git\n'
printf '  write of any kind was issued.\n'
printf '\n  THE CONTROLLER REFRESH CHANGED THE NEW COPY AND NOTHING ELSE.\n'
printf '  controller/nh_loop.py inside the disposable v24 shadow was verified to\n'
printf '  be the ACCEPTED REPAIR-27B identity the continuation source carries,\n'
printf '  then replaced with the ACCEPTED REPAIR-28 CANDIDATE, which was opened\n'
printf '  read-only as the source and was never written to. Repair 28 was the ONLY refresh\n'
printf '  source: the real controller is byte-for-byte the file this launcher\n'
printf '  froze and re-proved before, during and after, and it was never a source\n'
printf '  and never a destination. Repair 20B, 21, 22, 23, 24, 25, 26, 27 and 27A\n'
printf '  are preserved repair evidence that this run read, proved unchanged, and\n'
printf '  never copied into the shadow.\n'
printf '  REPAIR 28 IS ACCEPTED BY NESS FOR ITS BOUNDED CONTROLLER-REPAIR SCOPE,\n'
printf '  AND IT IS NOT INSTALLED. That acceptance authorised this shadow refresh\n'
printf '  and nothing else: no N.H design was accepted or adopted here, nothing\n'
printf '  was integrated into the Master or the Design and Wiring Map, and no\n'
printf '  implementation was authorised. The nine-event journal, its head and the\n'
printf '  authenticity key were not refreshed and are byte-identical to the\n'
printf '  continuation source.\n'
printf '\n  WHAT THIS RUN WAS TESTING, EXACTLY.\n'
printf '  v20 RAN. Its Stages 1, 2 and 3 all PASSED. Its Stage 4 then CRASHED --\n'
printf '  not stopped -- with an unhandled TypeError, writing NO machine report at\n'
printf '  all: run_prepare_next_claude_task read\n'
printf '      prepared["mechanical_design_specification"]["requirements"]\n'
printf '  unconditionally, while a task_ready = false preparation legitimately\n'
printf '  carries no mechanical design specification.\n'
printf '  ACCEPTED REPAIR 27B corrected that, and v21 then ran it: v21 reached the\n'
printf '  real correction loop and stopped fail-closed at\n'
printf '  CLAUDE_SPECIFICATION_STOP, because Claude\047s correction workspace did\n'
printf '  not carry the already-frozen non-candidate baseline source the GPT\n'
printf '  specification named. ACCEPTED REPAIR 28 IS THE BOUNDED CORRECTION TO\n'
printf '  EXACTLY THAT SOURCE-CORPUS MISMATCH. Repair 27B\047s earlier\n'
printf '  preparation-report correction is inherited historical behaviour, not\n'
printf '  the current test target.\n'
printf '  THIS RUN TESTED REPAIR 28 AND NOTHING BROADER. It assumed no\n'
printf '  outcome: not that Stage 4 must pass, not that Claude must be invoked,\n'
printf '  not that a Codex design audit must run, not that a correction round must\n'
printf '  happen, and not that the loop must reach PASS. The real Repair-28\n'
printf '  controller was run once and whatever it did was recorded. A NEW\n'
printf '  legitimate fail-closed stop is a VALID RESULT, and no gate was loosened,\n'
printf '  bypassed or reinterpreted to reach a later outcome. It was not a search\n'
printf '  for another controller defect.\n'
printf '  THE STAGE-4 OBSERVER WATCHES AN INHERITED REPAIR-25 SEAM. Repair 28\n'
printf '  inherits it through 27B, 27A, 27, 26 and 25; it did not invent it. If Stage 4\n'
printf '  reached the CHATGPT_REVIEW_REQUIRED stop,\n'
printf '  REPAIR25_CHATGPT_STOP_HANDOFF above records what the controller actually\n'
printf '  reported; if it did not, that observation reads NOT-EXERCISED, which is\n'
printf '  not a failure and was not forced.\n'
printf '\n  ONE KNOWN DEPENDENCY IS DELIBERATELY LEFT OPEN, AND THIS RUN DID NOT\n'
printf '  TOUCH IT. The MANUAL route-audit-finding provenance re-proof still does\n'
printf '  not carry a non-empty resume baseline. That path is not part of the\n'
printf '  normal Stage-4 execution rehearsed here. This launcher never invoked\n'
printf '  route-audit-finding, never invoked question-validation, never injected a\n'
printf '  finding to force either, never manufactured a Ness question, never\n'
printf '  repaired the dependency, and does not treat its being open as a v23\n'
printf '  failure. If Stage 4 stopped at CHATGPT_REVIEW_REQUIRED, this run STOPPED\n'
printf '  THERE and recorded the controller\047s own result.\n'
printf '\n  NO QUESTION WAS DELIVERED, COMPOSED OR ANSWERED. No question-delivery\n'
printf '  command was invoked, no question-delivery workspace was used, and this\n'
printf '  launcher asked Ness nothing.\n'
printf '\n  This launcher decided nothing about what any signal or question means.\n'
printf '  It made no classification and no disposition. Only the controller\047s own\n'
printf '  stages may ever do that, and only Ness may answer a question the\n'
printf '  controller eventually admits AND a fresh coverage review has cleared.\n'
printf '\n  The lab holds a copy of the N.H interview authenticity key.\n'
printf '  Delete the lab once the rehearsal has been reviewed.\n'
printf '\n  LAB_CREDENTIAL_SCAN is a SHAPE scan, not proof of absence.\n'
printf '  NO-KNOWN-MARKERS means only that no known credential marker was\n'
printf '  found in readable, uncompressed lab content. It cannot see a token\n'
printf '  in an unrecognised shape, and it cannot see into compressed or\n'
printf '  encoded data. Treat the lab as sensitive regardless of this line.\n\n'

# Fail closed: a protected-original mismatch outranks any apparent shadow
# success; a preserved-evidence mismatch outranks it too; and a moved lineage
# seed or a moved continuation source outranks everything about the controller,
# because either means the run did not continue what it said it continued. All
# six safety verdicts use reserved codes the controller never returns, so a
# containment failure can never be mistaken for an ordinary controller exit, and
# an ordinary controller exit can never be mistaken for a containment failure.
if [ "$ORIGINAL_PROOF" = "FAIL" ]; then
  exit "$RC_ORIGINAL_PROOF_FAIL"
fi
if [ "$PRESERVED_LAB_PROOF" = "FAIL" ]; then
  exit "$RC_PRESERVED_LAB_PROOF_FAIL"
fi
if [ "$REGRESSION_SEED_PROOF" = "FAIL" ]; then
  exit "$RC_REGRESSION_SEED_PROOF_FAIL"
fi
if [ "$CONTINUATION_SOURCE_PROOF" = "FAIL" ]; then
  exit "$RC_CONTINUATION_SOURCE_PROOF_FAIL"
fi
# Anything other than a completed marker sweep fails closed: FOUND means material
# is there, SCAN-FAILED means nothing is known, and neither may pass.
if [ "$LAB_CREDENTIAL_SCAN" != "NO-KNOWN-MARKERS" ]; then
  exit "$RC_LAB_CREDENTIAL_FOUND"
fi
# Likewise UNCHANGED is the only acceptable witness state; CHANGED and
# CAPTURE-FAILED both fail closed.
if [ "$CREDENTIAL_WITNESS" != "UNCHANGED" ]; then
  exit "$RC_CREDENTIAL_WITNESS_CHANGED"
fi

# THE CONTROLLER'S OWN FAILURE, PRESERVED VERBATIM. If the stage returned 1 or 2
# that is the controller fail-closing, and this launcher reports exactly what it
# said rather than replacing it with a status of its own.
if [ "$SHADOW_RC" -ne 0 ]; then
  exit "$SHADOW_RC"
fi

# THE STAGE RETURNED ZERO AND SOMETHING STILL STOPPED THE RUN. With one stage
# that can only be a containment observation whose final proofs nonetheless
# passed. It is not success and must not be reported as one, so it gets its own
# status.
if [ -n "$SEQUENCE_STOP_REASON" ]; then
  exit "$RC_SEQUENCE_STOPPED"
fi

# The stage ran, the execute returned 0, and every safety verdict passed.
exit 0

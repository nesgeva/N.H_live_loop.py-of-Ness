#!/usr/bin/env bash
#
# NH_SHADOW_REHEARSAL_LAUNCHER_v13.sh
#
# N.H SHADOW LIVE REHEARSAL LAUNCHER — v13
#   (REPAIR-19B CONTROLLER, BOUNDED REGRESSION OF THE EXACT v11 LIVE FAILURE,
#    WITH THE HISTORICAL REGRESSION SEED LOCKED BY WHOLE-WORKSPACE IDENTITY)
#
# WHAT THIS IS
#   A disposable-laboratory launcher, and specifically a REGRESSION one. It
#   proves the protected original N.H / controller workspace has not moved since
#   this launcher was constructed, makes an exact throwaway copy of THE PRESERVED
#   v10 CONTINUATION SHADOW -- the last state that exists BEFORE the false v11
#   question was ever admitted -- REFRESHES EXACTLY ONE FILE IN THAT NEW COPY,
#   and only in the new copy, to the independently audited Repair-19B controller,
#   hides the real /home/ness behind a tmpfs, republishes that regression copy at
#   the EXACT normal path /home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP inside a
#   Bubblewrap namespace, runs the sequence
#
#       1. python3 nh_loop.py question-validation          (one real GPT review)
#       2. python3 nh_loop.py question-coverage-review     (one real GPT review)
#       3. python3 nh_loop.py interview-gate               (read-only, no model)
#       4. python3 nh_loop.py execute-next-claude-task     (at most once)
#
#   inside that namespace, and then re-proves the protected original from
#   OUTSIDE the namespace.
#
#   Each stage is run AT MOST ONCE, in that order, and only while the stage
#   before it PERMITS CONTINUATION on the controller's own reported facts. Every
#   stage captures its exact command line, stdout, stderr, exit code, start and
#   finish timestamps, and its own protected-source proof.
#
# WHAT THIS IS NOT
#   This is validation only. It creates no N.H policy. It is not acceptance and
#   it is not adoption of any candidate. It authorises no production
#   implementation. It integrates nothing into Master or Map. It contains no Git
#   write command of any kind, and it is read-only against the protected
#   original, against the historical regression source, and against every
#   preserved lab in the exact sense defined immediately below.
#
#   A controller PASS inside the shadow means ONLY that the isolated real
#   rehearsal reached its own PASS. It means nothing about N.H acceptance.
#
# READ-ONLY, STATED EXACTLY
#   This launcher deliberately does NOT claim "never modified" or "never
#   written" about the protected original, about the historical regression
#   source, or about any preserved rehearsal lab. Those phrases would be false,
#   and a safety launcher that overstates its own guarantee is worse than one
#   that states a narrower true one. What follows is the whole claim, and nothing
#   anywhere else in this file means more than it.
#
#   SCOPE. This describes what THIS LAUNCHER'S OWN CODE does, outside the
#   Bubblewrap namespace. It says NOTHING about the sandboxed controller runs.
#   Whether those runs stayed contained is not asserted here; it is settled only
#   by the before/after proof in section 12, and until that proof completes the
#   report says so in as many words.
#
#   WHAT IS NEVER ISSUED. Against the protected original, against the historical
#   regression source and against every preserved lab, this launcher's own code
#   issues no create, write, append, truncate, rename, hard link, symlink,
#   unlink, rmdir, chmod, chown or utimes operation. Every regular-file open of
#   those paths is read-only. Verified by enumerating every mutating command in
#   this file: all of them target the new lab, the new shadow copy, or the
#   in-namespace overlays.
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
#   link count of any protected, preserved or regression-source file is altered
#   by this launcher's own code. atime may be refreshed. Two advisory locks are
#   taken and released. Nothing else.
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
# WHAT v13 IS, AND WHAT IT CHANGES
# ==========================================================================
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
# ==========================================================================
# WHAT v12 WAS, AND WHAT IT CHANGED
# ==========================================================================
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
# THE v13 SEQUENCE, EXACTLY
# ==========================================================================
#
#   STAGE 1.  python3 nh_loop.py question-validation
#             ONE real, fresh GPT/Codex review over the preserved seven-event
#             regression state. It is the ONLY way a question can come into
#             existence, it asks Ness nothing, and it invokes Claude never.
#
#             CONTINUE TO STAGE 2 when, and only when, the controller's own
#             report states ALL of:
#                 ok                            = true
#                 validation_inventory_complete = true
#                 material_unknowns             = []
#                 deliverable_question_count    = 0
#
#             STOP when the stage exits non-zero, when the report cannot be read,
#             when the inventory is incomplete, or when a material unknown
#             remains. Those are unusable or incomplete inventories and there is
#             nothing for a coverage review to challenge.
#
#             STOP AND REPORT A REGRESSION when deliverable_question_count is
#             greater than zero here, because no fresh matching coverage review
#             has run yet in this sequence and under Repair 19B nothing can be
#             deliverable before one has.
#
#             A NON-ZERO provisional_question_count DOES NOT STOP ANYTHING. It is
#             the corrected behaviour. It is reported and it is not gated.
#
#   STAGE 2.  python3 nh_loop.py question-coverage-review
#             EXACTLY ONE fresh independent review.
#             STOP on a technical failure.
#             STOP AND PRESERVE THE RESULT when coverage_possible_gaps > 0. That
#             is a VALID LIVE RESULT, not a fault. The gap is not turned into a
#             question, is not delivered, is not answered, and is not classified:
#             this launcher does not guess in shell code whether a gap was
#             missing or over_ask, and has no code able to. The controller owns
#             all classification.
#             CONTINUE TO STAGE 3 only when coverage_possible_gaps = 0 AND
#             coverage_review_cleared = true. Anything inconsistent stops
#             fail-closed.
#
#   STAGE 3.  python3 nh_loop.py interview-gate
#             Read-only. No provider call. CONTINUE only when the controller's
#             own mechanical_path_unlocked = true. Exit code 0 alone is never
#             enough. This launcher asks Ness nothing here and never forces a
#             gate open.
#
#   STAGE 4.  python3 nh_loop.py execute-next-claude-task
#             EXACTLY ONCE. The controller owns the GPT design work, the Claude
#             execution, the fresh GPT/Codex audit, the same-session Claude
#             corrections, the five-round correction cap and every existing stop
#             condition. This launcher does not reinterpret audit findings and
#             implements no second repair loop. Whatever execute reports is the
#             final v13 result.
#
#   THERE IS NO RETRY ANYWHERE. Not around a stage, not around a provider call,
#   not around the controller. No stage is duplicated. There is no fallback
#   invocation and no alternate validator.
#
#   AN EARLY STOP IS A RESULT, NOT A FAILURE, and this launcher never labels one
#   as a failure merely because a later stage did not run. Equally, an exit of 0
#   is never treated as permission to continue: every continuation decision is
#   taken from the controller-owned state fields, never from a status alone.

set -Eeuo pipefail
umask 077

# ==========================================================================
# SECTION 0 — FROZEN IDENTITIES. FAIL CLOSED AGAINST ALL OF THEM.
# ==========================================================================
#
# EVERY VALUE IN THIS SECTION WAS READ FROM THE REAL CURRENT DISK STATE WHEN THIS
# LAUNCHER WAS CONSTRUCTED. Not one of them is inherited from v11 or from any
# report. Where v11's frozen value is now stale -- the N.H HEAD above all -- the
# real current value is frozen here and v11's is deliberately NOT carried
# forward.

readonly HOME_REAL="/home/ness"
readonly WS="/home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP"
readonly CTRL="${WS}/controller"
readonly NHGOV="${WS}/NH-GOVERNANCE"
readonly STATE="${WS}/nh_interview_state"
readonly CAND_DIR="${NHGOV}/05_ACTIVE_CANDIDATE"
readonly AUTH_DIR="${NHGOV}/01_AUTHORITATIVE"

# Thirteen launcher files now live in controller/. All thirteen are accounted for
# explicitly: twelve by exact identity, and this one by presence.
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

# v1..v12 are ALL preserved unchanged, and all twelve are frozen here so this
# launcher fails closed if any of them moved. Each is historical validation
# evidence in its own right.
#
# v11 RAN, exactly once, against the Repair-18 controller over the preserved
# seven-event state, and its lab holds the exact live failure this regression
# reproduces. Nothing about v11 is retracted by v12 or v13 existing: v11 was
# correct for the controller it was frozen to, and the rule it applied is wrong
# only under Repair 19B, which did not exist when it was written.
#
# v12 is this file's DIRECT PREDECESSOR. It was constructed, independently
# audited by ChatGPT, and DELIBERATELY NEVER RUN: that audit found the
# whole-historical-source gap this file exists to close, so v12 was preserved
# unchanged as blocked historical evidence rather than executed. It is frozen
# here by exact sha256 and byte count like every earlier launcher.
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
# v13 is the completed rehearsal this launcher succeeds. Its identity is not
# taken from today's filename: it is the identity the completed v13 lab's own
# preserved before/during/after witnesses recorded for the file that actually
# ran, and today's v13 must still match it exactly.
readonly EXP_LAUNCHER_V13_SHA="59bf029fe88e0bd16353cb49208974cd21e616fbff03008623dfa43f478ece63"
readonly EXP_LAUNCHER_V13_BYTES="254827"
# v14 is the completed rehearsal this launcher succeeds. Its identity is the
# one the completed v14 lab's own preserved before/during/after-question-
# validation/after witnesses recorded for the file that actually ran -- eight
# independent records, all agreeing -- and today's v14 must still match it.
readonly EXP_LAUNCHER_V14_SHA="19bac92c64f634210374344239b728896245d96aef1e3197bf1d50dacaecf1ea"
readonly EXP_LAUNCHER_V14_BYTES="267561"
# v15 is THIS file's DIRECT PREDECESSOR and the completed rehearsal it
# succeeds. Its identity is NOT taken from today's filename: it is the identity
# the completed v15 lab's own preserved before / during / after-question-
# validation / after witnesses recorded for the file that actually ran -- four
# independent snapshots, each carrying launchers.identity, all four agreeing on
# one sha256 and one byte count -- and today's v15 must still match it exactly.
# v15 RAN, exactly once, against the Repair-21 controller over the preserved
# seven-event state, and its lab holds the exact live Stage-1 refusal Repair 22
# exists to correct. Nothing about v15 is retracted by v16 existing.
readonly EXP_LAUNCHER_V15_SHA="7eca43b645a107c8cb6a12ab6fd208b2bc859cdec00d142e200270db358a40bd"
readonly EXP_LAUNCHER_V15_BYTES="279451"

# --- controller: THE REAL PROTECTED CONTROLLER (REPAIR 20) ---
#
# THE ONE STRUCTURAL DIFFERENCE BETWEEN v13 AND v14 STARTS HERE.
#
# In v13 these three constants were BOTH the real controller AND the file the
# new shadow copy was refreshed to, because those were the same file. In v14
# they are NOT the same file and are deliberately split:
#
#   EXP_LOOP_*  is the REAL controller on disk -- Repair 20. It is PROTECTED.
#               It is asserted before, during and after, it is opened read-only
#               on every path, it is never a write destination anywhere in this
#               launcher, and it is NOT what the shadow is refreshed to.
#   EXP_R20B_*  is the independently audited and Ness-accepted Repair 20B
#               CANDIDATE. It is the file the NEW SHADOW COPY is refreshed to,
#               and the only reason this launcher exists.
#
# Repair 20B IS NOT INSTALLED. It is never renamed to nh_loop.py on the real
# filesystem, never copied over the real controller, and never promoted. The
# only place its bytes are written is inside the new disposable lab.
readonly EXP_LOOP_SHA="bdc4e74673d500ed654f5b7e83333ea620445bff8696d02a80197ed62630ce6a"
readonly EXP_LOOP_BYTES="1850341"
readonly EXP_LOOP_LINES="40217"

# --- controller: THE ACCEPTED REPAIR-20B CANDIDATE (the refresh source) ---
#
# Ness explicitly accepted Repair 20B for its bounded controller-repair scope.
# That acceptance authorises these exact bytes for this disposable validation
# and authorises nothing else: not replacing the real controller, not modifying
# nh_loop.py, not deleting or renaming this candidate, not any N.H acceptance,
# adoption, Master/Map integration or implementation.
readonly R20B_CANDIDATE_BASENAME="nh_loop_REPAIR20B_CANDIDATE.py"
readonly R20B_CANDIDATE="${CTRL}/nh_loop_REPAIR20B_CANDIDATE.py"
readonly EXP_R20B_SHA="3fbb204524348b7e9d32409a81d417e817aec5a3a3239b87e215313490ea5963"
readonly EXP_R20B_BYTES="1855288"
readonly EXP_R20B_LINES="40307"

# --- controller: THE REPAIR-21 CANDIDATE
#     (PRESERVED REPAIR EVIDENCE — NOT THE v16 REFRESH SOURCE) ---
#
# WHAT CHANGED BETWEEN v14 AND v15, AND IT IS THIS.
#
# v14 refreshed its shadow to Repair 20B. Repair 20B did its job: the v13 parser
# refusal did not recur. v14 then stopped at Stage 1 on a DIFFERENT and deeper
# refusal -- the accepted B9 retry-values closure record was "outside the
# relevant source closure this controller derived for the bound package" --
# because the authenticated package binding seeded the relevant-source walk from
# the v1.0 root alone and discarded the custodied v1.1/v1.2 chain it had just
# re-proved. Repair 21 is the bounded correction to that, and this launcher
# exists to run it once, in a fresh disposable shadow.
#
# REPAIR 20B IS NOT THE REFRESH SOURCE ANY MORE. It stays frozen above as
# PRESERVED REPAIR EVIDENCE: it is gated by exact identity, witnessed in the
# before/during/after sweep, and never written to -- but it is not copied into
# the shadow by this launcher on any path.
#
# REPAIR 21 IS NOT INSTALLED. It is never renamed to nh_loop.py on the real
# filesystem, never copied over the real controller, and never promoted. The
# only place its bytes are written is inside the new disposable v15 lab.
readonly R21_CANDIDATE_BASENAME="nh_loop_REPAIR21_CANDIDATE.py"
readonly R21_CANDIDATE="${CTRL}/nh_loop_REPAIR21_CANDIDATE.py"
readonly EXP_R21_SHA="a54f9e5ffd77470e9c0eb60552aa207e5ab24c8b45bff09765fe552fa5c910cd"
readonly EXP_R21_BYTES="1859838"
readonly EXP_R21_LINES="40385"

# --- controller: THE REPAIR-22 CANDIDATE (THE v16 REFRESH SOURCE) ---
#
# WHAT CHANGED BETWEEN v15 AND v16, AND IT IS THIS.
#
# v15 refreshed its shadow to Repair 21. Repair 21 did its job: the v14
# relevant-source-closure refusal did not recur in the form v14 produced. v15
# then stopped at Stage 1 on the NEXT and more exact refusal, and that one
# refusal is the whole reason this launcher exists:
#
#   question-validation derived a relevant-source closure for the bound
#   package, and then REJECTED the model because source_paths_checked omitted
#   81 files of that closure -- even though the exact closure had never been
#   supplied to the model before the call was made. The controller was
#   grading the reply against a requirement the reply was never shown.
#
# REPAIR 22 IS THE BOUNDED CORRECTION TO EXACTLY THAT, AND TO NOTHING ELSE. On
# the authenticated revalidation path the controller now:
#   1. derives the exact relevant-source closure BEFORE Codex is invoked;
#   2. puts that exact required path list into the prompt;
#   3. carries that exact frozen closure across the model-call boundary;
#   4. validates source_paths_checked against that SAME closure afterwards.
#
# THIS LAUNCHER TESTS THAT CORRECTION AND NOTHING BROADER. It implements none
# of the four steps, interprets none of them, and contains no closure, binding
# or source-selection logic in any executable path. All four live inside
# nh_loop.py.
#
# NEITHER REPAIR 20B NOR REPAIR 21 IS THE REFRESH SOURCE ANY MORE. Both stay
# frozen above as PRESERVED REPAIR EVIDENCE: both are gated by exact identity,
# both are witnessed in the before/during/after sweep, and neither is ever
# written to -- but neither is copied into the shadow by this launcher on any
# path.
#
# REPAIR 22 IS NOT INSTALLED AND IS NOT ACCEPTED. It is never renamed to
# nh_loop.py on the real filesystem, never copied over the real controller, and
# never promoted. The only place its bytes are written is inside the new
# disposable v16 lab. Ness's permission for this construction was "test it
# pls", which authorises ONE disposable shadow rehearsal and nothing else.
readonly R22_CANDIDATE_BASENAME="nh_loop_REPAIR22_CANDIDATE.py"
readonly R22_CANDIDATE="${CTRL}/nh_loop_REPAIR22_CANDIDATE.py"
readonly EXP_R22_SHA="d4ca703ec10d6de8d9de5b62e72b5f3e51a6dadb315e7d1e3b6a87031b088453"
readonly EXP_R22_BYTES="1878168"
readonly EXP_R22_LINES="40750"

readonly EXP_CTRL_BRANCH="main"
readonly EXP_CTRL_HEAD="db46a51967b1af1aa873bc0c0e847a0a95221bdf"

# --- THE CONTROLLER BYTECODE, FROZEN BY IDENTITY  (NEW IN v12) ---
#
# WHY THIS EXISTS AND WHY IT IS NOT AN ABSENCE CHECK.
# v11 asserted that NO python bytecode existed under controller/, because none
# did when v11 was frozen. One does now:
#   controller/__pycache__/nh_loop.cpython-314.pyc
# compiled from the current Repair-19B controller. Carrying v11's absence
# assertion forward would fail this run closed on a file that is simply there,
# and deleting it would be a write to the protected original, which this launcher
# never performs.
#
# So it is frozen exactly like every other protected artefact: this EXACT path,
# this EXACT digest, this EXACT byte count, and NO OTHER bytecode path anywhere
# under controller/. A second .pyc, a different digest, or a __pycache__ under a
# subdirectory all fail the run closed.
#
# It is also proved UNCHANGED across the read-only seed-authentication import in
# section 4b. That import runs python3 with -B AND PYTHONDONTWRITEBYTECODE=1, so
# it must not rewrite this file; the proof is what establishes that rather than
# the flags being trusted.
readonly CTRL_PYCACHE_DIR="${CTRL}/__pycache__"
readonly CTRL_PYCACHE_FILE="${CTRL}/__pycache__/nh_loop.cpython-314.pyc"
readonly CTRL_PYCACHE_STATUS_LINE="!! __pycache__/nh_loop.cpython-314.pyc"
readonly EXP_CTRL_PYCACHE_SHA="8dba8fd75b1b13d42fc69a38814f6bc04b694e8dacd45c3a665a6f03a2d83e06"
readonly EXP_CTRL_PYCACHE_BYTES="1424836"

# --- N.H: THE REAL CURRENT STATE, RE-READ, NOT INHERITED ---
#
# v11 froze ce3a38f43f287a56bd635ed836edf002a2db50a7. That HEAD is now three
# commits behind: Ness has since made unrelated legitimate N.H-GOVERNANCE work,
# including the Unreal Engine 5 Wonder runtime design commit and its follow-up
# permissions fix. THAT IS NOT AN ERROR AND IS NOT REPAIRED HERE. The real
# current HEAD is frozen below, nothing is reset, nothing is checked out, and no
# old HEAD is restored on any path.
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

# --- THE CURRENT UNREAL / WONDER DESIGN WORK, FROZEN BY NAME  (NEW IN v12) ---
#
# It is a TRACKED file at the current N.H HEAD, so the HEAD freeze and the
# whole-worktree hash already cover it. It is ALSO frozen here by name, by
# sha256, by byte count and by mode, and witnessed in its own proof artefact,
# because the authorising instruction requires this run to be able to state
# UNREAL_WONDER_WORK_CHANGED=NO as a measured fact rather than as one unchanged
# line inside a listing of thousands.
readonly UNREAL_WONDER_REL="05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md"
readonly EXP_UNREAL_WONDER_SHA="114a118c242ea553b11488eb6380da1458f3788084c4f86332ba45b9a6896273"
readonly EXP_UNREAL_WONDER_BYTES="53190"
readonly EXP_UNREAL_WONDER_MODE="644"

# --- REAL interview state (identities only; the key's CONTENTS are never read) ---
#
# THE REAL JOURNAL STILL HOLDS ITS OWN FIVE EVENTS. It is NOT the regression
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
# THE REGRESSION SOURCE — THE PRESERVED v10 CONTINUATION SHADOW
# --------------------------------------------------------------------------
#
# THIS IS THE STATE BEFORE THE FALSE v11 QUESTION EXISTED, and that is precisely
# why it is the regression source. Seeding from the answered question-delivery
# copy, or from any state that already carries the admitted question, would
# rehearse the aftermath instead of the defect. The regression must begin BEFORE
# the false question was ever admitted, and this seed is the last preserved state
# that satisfies that.
#
# It is preserved evidence in its own right AND it is the read-only source this
# run copies its shadow from. Both facts are true at once and the second grants
# no write permission whatsoever: this path appears in this file only in readonly
# assignments, in printf, in comparisons, and as the SOURCE side of an rsync. It
# is never a write target, never deleted, never renamed, never chmod-ed, never
# normalised, and no Git command is ever run inside it.
readonly PRESERVED_LAB_REPAIR17_CONTINUATION_V10="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR17_CONTINUATION_V10_6a3ce02e4a0448d5a7206f6eb4260bbcb87989da9f0a541feafea7dd4be0dc19_rs_2593b06ab1684bbf19a6ffb70d915bd2"

# The EXACT workspace inside that lab which becomes this run's shadow. It carries
# the seven-event interview journal whose event 7 is the routed review signal
# still UNRESOLVED, and that event exists NOWHERE else.
readonly REGRESSION_SOURCE="${PRESERVED_LAB_REPAIR17_CONTINUATION_V10}/shadow/NH_CLAUDE_CODEX_DESIGN_LOOP"
readonly REGRESSION_SOURCE_MODE="HISTORICAL_EXACT_FAILURE_SNAPSHOT"

# The seed's OWN controller file. It is the REPAIR-17 controller, because that is
# what the completed v10 run was executed with, and it is the file the refresh in
# section 7b replaces IN THE NEW COPY ONLY. This path is read; it is never
# written.
readonly SEED_LOOP="${REGRESSION_SOURCE}/controller/nh_loop.py"

readonly SEED_STATE="${REGRESSION_SOURCE}/nh_interview_state"
readonly SEED_JOURNAL="${SEED_STATE}/nh_interview_journal.jsonl"
readonly SEED_JOURNAL_HEAD="${SEED_STATE}/nh_interview_journal.head"
readonly SEED_AUTH_KEY="${SEED_STATE}/nh_interview_authenticity.key"

# The regression source's frozen identity. Read from the preserved seed itself
# when this launcher was written, never inherited from any report.
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

# THE SEED'S OWN CONTROLLER IDENTITY -- THE EXACT REPAIR-17 FILE.
#
# This is what makes the refresh a bounded, provable transition rather than an
# overwrite. The seed controller must be EXACTLY Repair 17 and the real
# controller must be EXACTLY Repair 19B; either side being anything else fails
# the run CLOSED.
readonly EXP_SEED_LOOP_SHA="6a3ce02e4a0448d5a7206f6eb4260bbcb87989da9f0a541feafea7dd4be0dc19"
readonly EXP_SEED_LOOP_BYTES="1749880"
readonly EXP_SEED_LOOP_LINES="38331"

# The v10 shadow marker the seed already carries, frozen by content.
readonly EXP_SEED_V10_MARKER_SHA="4ea96ff31275c49db573d52f80f40bc368b48d272ea3c3c950aede77d3fbd3a3"

# --------------------------------------------------------------------------
# EVENT 7 -- THE UNRESOLVED ROUTED SIGNAL, FROZEN FIELD BY FIELD
# --------------------------------------------------------------------------
#
# These are IDENTIFIERS AND DIGESTS ONLY. Not one of them is a classification, a
# disposition, a verdict or an answer, and nothing in this launcher reads the
# signal's title, its evidence or any other wording. They exist for exactly one
# purpose: to prove that the state being regressed is the state v9 recorded and
# v10 left STILL UNRESOLVED, and not some other journal that merely happens to
# have seven lines.
#
# A ROUTED SIGNAL IS NOT A QUESTION. Only the controller's ordinary
# question-validation may ever turn one into a question, and this launcher
# neither performs nor influences that.
readonly EXP_SEED_EVENT7_TYPE="review_signal_recorded"
readonly EXP_SEED_EVENT7_ROUTE="chatgpt_review_required"
readonly EXP_SEED_EVENT7_SIGNAL_SOURCE="question_coverage_review"
readonly EXP_ROUTED_SIGNAL_ID="rs_2593b06ab1684bbf19a6ffb70d915bd2"
readonly EXP_STANDING_TARGET_ID="st_028ac341df713a4c189028c9971b4375"
readonly EXP_SEED_EVENT7_ISSUE_KEY="authority_control_retry_values_scope"
readonly EXP_SEED_EVENT7_FINDING_KEY="older_retry_decision_does_not_reach_new_seam"
readonly EXP_SEED_EVENT7_SHA="9e4fd131d16290abff4ef29aca75cf7c93ee8c57e90e25a2939191a1a7eaa5d0"
readonly EXP_SEED_EVENT6_SHA="c2031885d8bc6251ae3904932a0dda4215dec5c2ba9b4ff1c2501be143691730"

# Disk-derived witness counts over the seed journal, frozen so a substituted or
# truncated journal cannot pass by shape alone. event 7's own digest occurs once
# (as its event_sha256); event 6's digest occurs twice (as event 6's own
# event_sha256 and as event 7's prev_event_sha256).
readonly EXP_SEED_EVENT7_SHA_OCCURRENCES="1"
readonly EXP_SEED_EVENT6_SHA_OCCURRENCES="2"
readonly EXP_SEED_ROUTED_SIGNAL_OCCURRENCES="1"
readonly EXP_SEED_STANDING_TARGET_OCCURRENCES="1"

# THE ONE PATH THE REFRESH IS AUTHORISED TO CHANGE IN THE NEW COPY.
#
# This is the ONLY surviving member of what v11 called its permitted-difference
# set, and it now governs one comparison only: NEW COPY vs SEED, in section 7b.
# It is NOT used to compare the seed against the real workspace -- that
# comparison does not exist in v12 and its removal is deliberate.
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

# --- lab: NEW, keyed to REPAIR19B, to V13, to the exact Repair-19B controller
#     identity AND to the routed signal this regression exists to carry forward.
#
# Never reused. If this exact path already exists the launcher ABORTS in section
# 3: it does not delete it, does not clean it, does not overwrite it and does not
# write into it. No older lab is ever deleted to make room.
#
# THE v12 LAB PATH IS NOT THIS PATH AND IS NEVER TOUCHED. v12 was never run, so
# no v12 lab exists; if one ever appears it is evidence and this launcher will
# neither reuse nor delete it.
readonly LAB="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR22_V16_d4ca703ec10d6de8d9de5b62e72b5f3e51a6dadb315e7d1e3b6a87031b088453_rs_2593b06ab1684bbf19a6ffb70d915bd2"

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
# The completed v11 rehearsal -- the Repair-18 CONTINUATION run -- is preserved
# evidence in its own right and holds the exact live failure v12 regresses. v12
# must never collide with it and must witness that it did not move.
readonly PRESERVED_LAB_REPAIR18_CONTINUATION_V11="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR18_CONTINUATION_V11_440cf8cf4286b4682c5add47e49d8e19de4020d4c8a0ffbe320573dc654969c2_rs_2593b06ab1684bbf19a6ffb70d915bd2"
# The COMPLETED v13 rehearsal. It holds the exact provider-backed Stage-1
# question-validation refusal that Repair 20B exists to correct, so it is
# historical evidence in its own right. v14 must never collide with it, never
# write into it, never reuse it and never normalise it, and must witness that it
# did not move.
readonly PRESERVED_LAB_REPAIR19B_V13="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR19B_V13_235885af469a6b5f3f428d206c77072712ef4b8d68caa37acf43445fc321bf02_rs_2593b06ab1684bbf19a6ffb70d915bd2"
# The COMPLETED v14 rehearsal. It holds the exact provider-backed Stage-1
# relevant-source-closure refusal that Repair 21 exists to correct, so it is
# historical evidence in its own right. v15 must never collide with it, never
# write into it, never reuse it and never normalise it.
readonly PRESERVED_LAB_REPAIR20B_V14="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR20B_V14_3fbb204524348b7e9d32409a81d417e817aec5a3a3239b87e215313490ea5963_rs_2593b06ab1684bbf19a6ffb70d915bd2"
# The COMPLETED v15 rehearsal. It holds the exact provider-backed Stage-1
# refusal Repair 22 exists to correct -- question-validation rejecting the model
# for not checking closure files the controller never supplied before the call
# -- so it is historical evidence in its own right. v16 must never collide with
# it, never write into it, never reuse it, never normalise it and never delete
# it, and must witness that it did not move. It sits under /home/ness as an
# NH_AICP_* artefact, so the before/during/after preserved-artefact sweep
# already covers it entry by entry; it is ALSO named here so the collision
# refusal and the presence assertion can speak about it directly.
readonly PRESERVED_LAB_REPAIR21_V15="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR21_V15_a54f9e5ffd77470e9c0eb60552aa207e5ab24c8b45bff09765fe552fa5c910cd_rs_2593b06ab1684bbf19a6ffb70d915bd2"

# --------------------------------------------------------------------------
# THE v11 HISTORICAL WITNESS — THE ONLY AUTHORISED SOURCE OF THE EXPECTED
# HISTORICAL SEED IDENTITY                                    (NEW IN v13)
# --------------------------------------------------------------------------
#
# WHY THESE FILES AND NOT TODAY'S SEED.
# The whole point of v13 is that the historical expectation must PRE-DATE this
# correction. Walking the seed now and freezing whatever is found would bless any
# corruption that already happened, which is precisely the hole being closed.
#
# The completed v11 run captured the FULL preserved-artefact sweep at four
# separate moments in its own life -- before, during, after question-validation
# and after. The preserved v10 seed sits inside a preserved lab, so every one of
# those four captures already contains a complete record of the seed: a sha256
# for every regular file, and type / mode / size for every entry. That is the
# historical witness, and it was written before this defect was known.
#
# EACH FILE IS FROZEN BY ITS OWN sha256 AND BYTE COUNT. A moved witness fails the
# run CLOSED, before any provider or model call. Nothing here is written,
# repaired, normalised or regenerated: this lab appears in this file only in
# readonly assignments, in printf, and as a READ-ONLY input.
#
# All four snapshots are currently byte-identical to one another, which is itself
# evidence that the seed did not move during the v11 run. They are nevertheless
# parsed and compared INDEPENDENTLY below, because "the files are identical" and
# "the manifests they yield are identical" are different claims and only the
# second one is the claim this gate makes.
#
# AN HONEST NOTE ON THE ORDER OF THE TWO WITNESS CHECKS. Because every snapshot
# is frozen against the SAME pair of digests above, a witness that disagreed with
# its siblings would necessarily have different bytes and would therefore already
# have failed the per-file identity check, which runs first. The independent
# four-way derivation and agreement requirement is kept anyway, for two honest
# reasons: it is what actually ESTABLISHED the expectation at construction time,
# and it is the check that would catch a construction-time error in which these
# frozen digests were mistakenly taken from a single snapshot rather than from
# four agreeing ones. It is defence in depth, and it is described as such rather
# than being presented as the primary lock.
readonly V11_PROOF_DIR="${PRESERVED_LAB_REPAIR18_CONTINUATION_V11}/proof"

readonly V11_WITNESS_SNAPSHOTS=(
  "original.before"
  "original.during"
  "original.after-question-validation"
  "original.after"
)

# sha256 and byte count of preserved_labs.sha256 in every snapshot above.
readonly EXP_V11_WITNESS_SHA_FILE_SHA="a7b163e4f58b699f3cd719533260e00eda8d71477ee2b8b008502d964ab3232f"
readonly EXP_V11_WITNESS_SHA_FILE_BYTES="951013"

# sha256 and byte count of preserved_labs.meta in every snapshot above.
readonly EXP_V11_WITNESS_META_FILE_SHA="3915f56086f285246b1670e5fa34cdd550dadad475656827d84130f143614949"
readonly EXP_V11_WITNESS_META_FILE_BYTES="1150504"

# --------------------------------------------------------------------------
# THE CANONICAL HISTORICAL SEED MANIFEST, FROZEN BY DIGEST      (NEW IN v13)
# --------------------------------------------------------------------------
#
# Computed at construction time by running the canonicalizer below against the
# four v11 witnesses above -- NOT against the current seed. All four agreed.
#
# CANONICAL IDENTITY, STATED EXACTLY:
#   regular file   relative path, type=file, permission mode, byte size, sha256
#   directory      relative path, type=directory, permission mode
#
# UID, GID, atime, mtime, ctime, inode, link count and filesystem block
# allocation are NOT identity and are ignored on both sides. They are not source
# content, and reads and copies legitimately move some of them.
#
# CANONICAL ROOT CONVENTION, STATED EXPLICITLY BECAUSE IT IS A ONE-ENTRY
# DIFFERENCE. The seed root directory itself is NOT an entry; only paths strictly
# beneath it are. The v11 witness metadata additionally carries the root's own
# directory line, so the witness holds 309 records under the seed root while this
# manifest holds 308. That is a counting convention, not a discrepancy, and the
# manifest was NOT adjusted to hit any number: 308 total = 234 regular files +
# 74 directories is exactly what the v11 final report recorded for the
# exhaustively enumerated seed workspace, and exactly what the canonical rule
# above produces from the preserved witness.
readonly EXP_HIST_SEED_MANIFEST_SHA="b21c480b4cb79d5ae5f82663332832afd16b08c3df6c25338f4e7b3bc72399bd"
readonly EXP_HIST_SEED_MANIFEST_ENTRIES="308"
readonly EXP_HIST_SEED_MANIFEST_FILES="234"
readonly EXP_HIST_SEED_MANIFEST_DIRS="74"
readonly EXP_HIST_SEED_MANIFEST_SYMLINKS="0"

# THE PRESERVED-ARTEFACT SWEEP GLOB.
#
# WIDENED IN v12 from NH_AICP_SHADOW_REHEARSAL_* to NH_AICP_*, so every
# disposable artefact Ness holds directly under /home/ness is witnessed before,
# during and after this run rather than only the rehearsal labs. This is strictly
# MORE protection than v11 had. It names no additional path, and the new lab is
# excluded from it explicitly because that one is being written by design.
readonly PRESERVED_SWEEP_GLOB="NH_AICP_*"

readonly SHADOW_WS="${LAB}/shadow/NH_CLAUDE_CODEX_DESIGN_LOOP"
readonly RUNTIME_TMP="${LAB}/runtime/tmp"
readonly PROOF="${LAB}/proof"
readonly SHADOW_MARKER_NAME=".nh_shadow_marker"

# --- THE FOUR STAGES, in the exact order they may run ---
#
# Each stage has one slug, and every artefact it produces is that slug plus a
# fixed suffix, so a reader can find all of one stage's evidence by name alone:
#
#   <slug>.command     the exact argv, one element per line
#   <slug>.stdout      the machine report
#   <slug>.stderr      the live progress
#   <slug>.exit-code   the integer, or NOT-RUN
#   <slug>.started     ISO-8601 UTC, taken immediately before the namespace
#   <slug>.finished    ISO-8601 UTC, taken immediately after it exits
#   original.after-<slug>/   that stage's own protected-source proof
readonly STAGE1_SLUG="question-validation"
readonly STAGE2_SLUG="coverage-review"
readonly STAGE3_SLUG="interview-gate"
readonly STAGE4_SLUG="execute"

# THE FOUR CONTROLLER COMMANDS. Each of these constants is used at EXACTLY ONE
# executable call site, in section 11, in this order. There is no fifth
# controller command anywhere in this file.
readonly STAGE1_CMD="question-validation"
readonly STAGE2_CMD="question-coverage-review"
readonly STAGE3_CMD="interview-gate"
readonly STAGE4_CMD="execute-next-claude-task"

readonly ALL_STAGE_SLUGS=(
  "$STAGE1_SLUG" "$STAGE2_SLUG" "$STAGE3_SLUG" "$STAGE4_SLUG"
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
# NEW IN v12. The regression source has its own verdict and its own reserved
# code, so a moved regression source is never reported as, or hidden behind, a
# preserved-lab or protected-workspace verdict.
readonly RC_REGRESSION_SEED_PROOF_FAIL=94

# THE EARLY-STOP STATUS. It is NOT a safety verdict and it is NOT corruption.
#
# It means exactly this: the natural one-pass sequence stopped safely before
# completing all four stages. Every reason it can carry is a legitimate
# observation of the CURRENT shadow state and none of them is a fault.
#
# It exists because the last stage's own status cannot carry that meaning. A
# coverage review that routes a gap exits 0; a closed gate exits 0. Returning
# that 0 would report a sequence that stopped as a run that finished, which is
# the one thing this launcher must never do.
#
# 3 is chosen deliberately: nh_loop.py returns only 0, 1 and 2, so 3 cannot be
# confused with a controller status, and it sits well clear of the 90-94 safety
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
# is never reported as, or hidden behind, a protected-workspace verdict.
readonly PRESERVED_LAB_PROOF_FILES=(
  "preserved_labs.sha256"
  "preserved_labs.meta"
)

# Proof artefacts of THE REGRESSION SOURCE, in their own set with their own
# verdict and their own reserved exit code. The regression source lives inside a
# preserved lab and is therefore already inside the sweep above; it is witnessed
# separately BY NAME because it is the one piece of state this entire regression
# depends on. If it moves, the run must say so in those words rather than as one
# changed line inside a listing of thousands.
readonly REGRESSION_SEED_PROOF_FILES=(
  "regression_seed.identity"
  # NEW IN v13. The COMPLETE historical workspace identity, and the v11 witness
  # it is derived from, both re-proved at every capture point. The selected
  # identities above prove the interview journal is authentic; these two prove
  # the whole historical source is the one the v11 witness recorded. Neither
  # replaces the other and both are required.
  "regression_seed.historical_witness"
  "regression_seed.historical_manifest"
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
# The one new v14 observation field. NOT-RUN until the exact-regression
# observation runs, so the RESULT block is truthful when the sequence stops
# before Stage 1 and never reports a recurrence it did not measure.
REPAIR20B_EXACT_REGRESSION_RECURRED="NOT-RUN"
REPAIR21_EXACT_REGRESSION_RECURRED="NOT-RUN"
# The one new v16 observation field. NOT-RUN until the exact-regression
# observation runs, so the RESULT block is truthful when the sequence stops
# before Stage 1 and never reports a recurrence it did not measure. It controls
# NO stage and grants NO pass.
REPAIR22_EXACT_REGRESSION_RECURRED="NOT-RUN"
REGRESSION_CONTINUATION_STATE="NOT-RUN"
REPORTED=0
AFTER_PROOF_DONE=0
ORIGINAL_PROOF="NOT-RUN"
PRESERVED_LAB_PROOF="NOT-RUN"
REGRESSION_SEED_PROOF="NOT-RUN"
LAB_CREDENTIAL_SCAN="NOT-RUN"

# The four stage results. NOT-RUN is a real, reported state and is never silently
# rendered as success or as failure: a stage that never ran because an earlier
# one stopped the sequence is a different fact from a stage that ran and returned
# zero, and this launcher keeps the two apart everywhere.
VALIDATION_RC="NOT-RUN"
COVERAGE_RC="NOT-RUN"
GATE_RC="NOT-RUN"
EXEC_RC="NOT-RUN"
STAGE_RC=""

# WHY THE SEQUENCE STOPPED, in this launcher's own words. Set once, the first
# time a stage declines to permit continuation, and reported verbatim. "" means
# every stage that was reached permitted the next one.
SEQUENCE_STOP_REASON=""

# Per-stage protected-source proof verdicts, and the flag that stops downstream
# work the instant one of them fails.
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
    printf 'At least one isolated controller stage WAS entered, so real Codex /\n' >&2
    printf 'Claude provider calls may already have been made.\n' >&2
    printf '  stage 1  question-validation      : %s\n' "$VALIDATION_RC" >&2
    printf '  stage 2  question-coverage-review : %s\n' "$COVERAGE_RC" >&2
    printf '  stage 3  interview-gate           : %s\n' "$GATE_RC" >&2
    printf '  stage 4  execute-next-claude-task : %s\n' "$EXEC_RC" >&2
    if [ -n "$SEQUENCE_STOP_REASON" ]; then
      printf '  the sequence stopped because: %s\n' "$SEQUENCE_STOP_REASON" >&2
    fi
  else
    printf 'No isolated controller stage was started.\n' >&2
    printf 'No model or provider call was made.\n' >&2
  fi

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

  # --- the preserved earlier rehearsals and the regression source ---
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
  printf 'The v10 lab is ALSO this run\047s regression source. It was read to be\n' >&2
  printf 'copied and to be authenticated, and nothing else was done to it: no\n' >&2
  printf 'create, write, append, truncate, rename, link, unlink, chmod, chown or\n' >&2
  printf 'utimes was issued against it, and no Git command was run inside it.\n' >&2
  if [ "$AFTER_PROOF_DONE" = "1" ]; then
    printf 'They were re-witnessed after the run: %s\n' "$PRESERVED_LAB_PROOF" >&2
    printf 'The regression source was re-witnessed by name: %s\n' "$REGRESSION_SEED_PROOF" >&2
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

  # --- the Repair-22 candidate identity (NEW IN v16) ---
  # THE ONE FILE THIS REHEARSAL EXISTS TO TEST. Captured before, during and
  # after exactly like the real controller, so the sweep proves the file this
  # rehearsal reads was not edited underneath it.
  {
    printf 'sha256 %s\n' "$(sha_of "$R22_CANDIDATE")"
    printf 'bytes  %s\n'  "$(bytes_of "$R22_CANDIDATE")"
    printf 'lines  %s\n'  "$(wc -l < "$R22_CANDIDATE")"
    printf 'stat   %s\n'  "$(stat -c 'mode=%f perm=%a uid=%u gid=%g size=%s mtime=%Y ctime=%Z inode=%i links=%h' -- "$R22_CANDIDATE")"
  } > "${out}/repair22_candidate.identity"

  # --- controller bytecode identity (NEW IN v12) ---
  # The complete bytecode set under controller/, by path, plus the frozen file's
  # own digest and byte count. A second .pyc appearing anywhere under the
  # controller shows up here as a new path and fails the before/after comparison.
  {
    printf 'bytecode_paths\n'
    find "${CTRL}" -name '__pycache__' -o -name '*.pyc' 2>> "$cap_err" | LC_ALL=C sort
    printf 'frozen_file    %s\n' "$CTRL_PYCACHE_FILE"
    printf 'sha256         %s\n' "$(sha_of "$CTRL_PYCACHE_FILE")"
    printf 'bytes          %s\n' "$(bytes_of "$CTRL_PYCACHE_FILE")"
  } > "${out}/controller_bytecode.identity"

  # --- all thirteen launcher artefacts: v1-v12 must stay byte-identical, and
  #     this file must stay byte-identical to itself across the run ---
  {
    for lf in "$LAUNCHER_V1_BASENAME" "$LAUNCHER_V2_BASENAME" \
              "$LAUNCHER_V3_BASENAME" "$LAUNCHER_V4_BASENAME" \
              "$LAUNCHER_V5_BASENAME" "$LAUNCHER_V6_BASENAME" \
              "$LAUNCHER_V7_BASENAME" "$LAUNCHER_V8_BASENAME" \
              "$LAUNCHER_V9_BASENAME" "$LAUNCHER_V10_BASENAME" \
              "$LAUNCHER_V11_BASENAME" "$LAUNCHER_V12_BASENAME" \
              "$LAUNCHER_V13_BASENAME" "$LAUNCHER_V14_BASENAME" \
              "$LAUNCHER_V15_BASENAME" "$LAUNCHER_V16_BASENAME"; do
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
             "$PRESERVED_LAB_REPAIR21_V15"; do
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

# The completed v15 lab is the direct predecessor evidence for THIS run. It is
# never written to, never normalised, never repaired, never reused and never
# deleted: this is a presence-and-shape assertion only, and the
# before/during/after preserved-artefact sweep is what proves it did not move.
if [ ! -d "$PRESERVED_LAB_REPAIR21_V15" ] || [ -L "$PRESERVED_LAB_REPAIR21_V15" ]; then
  die "the completed v15 rehearsal lab is missing or is not an ordinary directory:
        ${PRESERVED_LAB_REPAIR21_V15}
      It holds the exact provider-backed Stage-1 refusal Repair 22 corrects.
      Refusing to rehearse without the evidence it succeeds."
fi
note "the completed v15 lab is present and is not this run's lab"

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
# SECTION 4b — THE REGRESSION SOURCE, AND THE SIGNAL IT CARRIES
# --------------------------------------------------------------------------
#
# v12 exists to regress the exact live failure from a state that PRE-DATES the
# false question, and that state is worth exactly as much as the proof that it IS
# that state. This gate establishes it in four escalating steps, and every one of
# them fails the run CLOSED, long before the isolation self-test and therefore
# long before any possible provider or model call:
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
CAPTURE_MODE = False

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

if mode != "gate" and mode != "capture":
    die("unknown mode " + repr(mode))
CAPTURE_MODE = (mode == "capture")

if not snapshots:
    die("no historical witness snapshot was supplied")
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
    sys.stdout.write("HISTORICAL_REGRESSION_SEED_CAPTURED\n")
    sys.exit(0)

report = []
report.append("historical_witness_source        PRESERVED_V11_WITNESSES")
report.append("expectation_from_current_seed    NO")
report.append("canonical_rule                   " +
              "relpath+type+mode(+size+sha256 for regular files); "
              "root excluded; uid/gid/times/inode/nlink/blocks ignored")
report.append("seed_root                        " + root)

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
# v11's ancestor of this function required NO bytecode to exist. One exists now,
# compiled from the current Repair-19B controller, so the requirement is
# restated as an IDENTITY requirement: exactly this bytecode set, exactly this
# digest, exactly this byte count, and no other .pyc or __pycache__ anywhere
# under the controller. Nothing is deleted and nothing is regenerated here.
assert_controller_bytecode_frozen() {
  local where="$1" found expected
  found="$(find "${CTRL}" -name '__pycache__' -o -name '*.pyc' 2>/dev/null | LC_ALL=C sort)"
  expected="$(printf '%s\n' "$CTRL_PYCACHE_DIR" "$CTRL_PYCACHE_FILE" | LC_ALL=C sort)"
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
  expect "controller bytecode sha256 ${where}" "$(sha_of "$CTRL_PYCACHE_FILE")"   "$EXP_CTRL_PYCACHE_SHA"
  expect "controller bytecode bytes  ${where}" "$(bytes_of "$CTRL_PYCACHE_FILE")" "$EXP_CTRL_PYCACHE_BYTES"
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
# The preserved v10 shadow was run with the Repair-17 controller. The current
# real controller is the independently audited Repair-19B one. v12 must therefore
# NOT simply run the byte-for-byte v10 shadow unchanged -- that would rehearse
# Repair 17 again and would test nothing the repairs changed -- and must NOT copy
# the real workspace instead, which would discard the seven-event state and the
# unresolved routed signal with it.
#
# So exactly one path in the NEW COPY is replaced, and four separate proofs
# bracket it. Each of them fails the run CLOSED, and all four happen before the
# marker is placed and therefore long before anything enters Bubblewrap and long
# before any possible provider call:
#
#   BEFORE     the new copy's controller is the EXACT Repair-17 file.
#   AFTER      the refreshed file is the EXACT Repair-19B identity -- sha256,
#              byte count AND line count. A short read, a truncated write or a
#              substituted source all fail here.
#   COMPOSITE  the new copy differs from the seed in EXACTLY
#              controller/nh_loop.py and in NO other path, compared by content at
#              every depth. This is what proves "only the controller was
#              refreshed" instead of merely asserting it.
#   PRESERVED  the new copy's interview journal, journal head and authenticity
#              key are still byte-identical to the seed's seven-event state, and
#              still carry event 7 exactly once.
#
# WHAT IS NEVER REFRESHED. The interview journal, the journal head, the
# authenticity key, the candidates, the NH-GOVERNANCE tree, its Git metadata, any
# source package, and every launcher file. The composite proof is what makes that
# list enforceable rather than aspirational. NOTHING IS EVER COPIED BACK.
#
# THE REFRESH SOURCE IS THE REAL CONTROLLER, OPENED READ-ONLY. ${CTRL}/nh_loop.py
# appears in this function only as the SOURCE of a copy. It is never opened for
# writing, never renamed, never chmod-ed, and its identity has already been
# asserted twice -- once as a precondition and once under both original locks --
# before this function is ever called.
#
# THE HISTORICAL SEED IS NEVER WRITTEN TO. The write target below is
# ${SHADOW_WS}, which is the new disposable lab. The seed is re-read and proved
# unmoved immediately afterwards, by name, in its own proof artefact.

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
# --------------------------------------------------------------------------
# THE SAME-MESSAGE DIAGNOSTIC MATCHER  (NEW IN v15)
# --------------------------------------------------------------------------
#
# WHY v14's PREDICATE IS NOT COPIED FORWARD.
#
# v14 decided "the exact regression recurred" by grepping for each component
# SEPARATELY across the whole of Stage-1 output and ANDing the results. Two of
# those components -- the issue key and the B9 path -- appear in that concern's
# routed evidence on essentially every run, so they were effectively always
# true. The field therefore collapsed to a single global grep for the third
# string, and ANY unrelated issue quoting ANY other file could have made v15
# report a recurrence that did not happen. v14's own completed run demonstrates
# the two always-on halves. That predicate is a false-positive generator and it
# is deliberately replaced here rather than inherited.
#
# WHAT THIS DOES INSTEAD. It splits Stage-1 output into INDIVIDUAL DIAGNOSTIC
# MESSAGES and requires every component to occur inside ONE SAME message.
#
# Two message sources, both controller-owned and both read read-only:
#   * the JSON report on stdout, whose "errors" array has one string per
#     diagnostic -- the authoritative form;
#   * the stderr text, split on the controller's own "  - " bullet convention,
#     with wrapped continuation lines belonging to the bullet above them.
#
# It prints MATCH or NO-MATCH and nothing else. It classifies no meaning, reads
# no design content, and never decides a stage.
readonly SAME_MESSAGE_MATCHER='
import json, sys

stdout_path, stderr_path = sys.argv[1], sys.argv[2]
needles = sys.argv[3:]
if not needles:
    sys.stdout.write("NO-MATCH\n"); raise SystemExit(0)

messages = []

# 1. The JSON report'"'"'s own errors array: one element is one diagnostic.
try:
    with open(stdout_path, "r", encoding="utf-8", errors="replace") as handle:
        blob = handle.read()
    start = blob.find("{")
    if start >= 0:
        report = json.loads(blob[start:])
        if isinstance(report, dict):
            for key in ("errors", "material_unknowns"):
                for item in report.get(key) or ():
                    if isinstance(item, str):
                        messages.append(item)
except Exception:
    pass

# 2. stderr, split on the controller'"'"'s own bullet convention. A line that
#    starts a bullet begins a new message; anything else continues the current
#    one, which is how a wrapped diagnostic stays ONE message.
try:
    with open(stderr_path, "r", encoding="utf-8", errors="replace") as handle:
        current = None
        for raw in handle:
            line = raw.rstrip("\n")
            if line.lstrip().startswith("- "):
                if current is not None:
                    messages.append(current)
                current = line.lstrip()[2:]
            elif current is not None:
                current = current + " " + line.strip()
            else:
                messages.append(line)
        if current is not None:
            messages.append(current)
except Exception:
    pass

for message in messages:
    if all(needle in message for needle in needles):
        sys.stdout.write("MATCH\n"); raise SystemExit(0)
sys.stdout.write("NO-MATCH\n")
'

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
    printf 'expected_sha256    %s\n' "$EXP_SEED_LOOP_SHA"
    printf 'expected_bytes     %s\n' "$EXP_SEED_LOOP_BYTES"
    printf 'expected_lines     %s\n' "$EXP_SEED_LOOP_LINES"
  } > "${PROOF}/controller-refresh.before"
  expect "new copy controller sha256 BEFORE refresh (Repair 17)" \
         "$(sha_of "$target")"   "$EXP_SEED_LOOP_SHA"
  expect "new copy controller bytes  BEFORE refresh (Repair 17)" \
         "$(bytes_of "$target")" "$EXP_SEED_LOOP_BYTES"
  expect "new copy controller lines  BEFORE refresh (Repair 17)" \
         "$(wc -l < "$target")"  "$EXP_SEED_LOOP_LINES"
  note "the new copy's controller is the exact Repair-17 file the seed carried"
}

refresh_new_copy_controller() {
  local target="${SHADOW_WS}/controller/nh_loop.py"
  local staging="${SHADOW_WS}/controller/.nh_loop.py.repair22-refresh"

  # THE REFRESH SOURCE IS THE REPAIR-22 CANDIDATE, NOT THE REAL CONTROLLER AND
  # NOT ANY EARLIER CANDIDATE. It is asserted immediately, at the moment it is
  # about to be read, and it must be an ordinary non-symlink file: a symlink here
  # could redirect the copy to any file on the system.
  [ -L "$R22_CANDIDATE" ] && die "the Repair-22 candidate is a SYMLINK:
        ${R22_CANDIDATE}
      Refusing to refresh the shadow through it."
  [ -f "$R22_CANDIDATE" ] \
    || die "the Repair-22 candidate is missing at ${R22_CANDIDATE}"
  expect "refresh source sha256 (Repair 22 candidate)" \
         "$(sha_of "$R22_CANDIDATE")"   "$EXP_R22_SHA"
  expect "refresh source bytes  (Repair 22 candidate)" \
         "$(bytes_of "$R22_CANDIDATE")" "$EXP_R22_BYTES"
  expect "refresh source lines  (Repair 22 candidate)" \
         "$(wc -l < "$R22_CANDIDATE")"  "$EXP_R22_LINES"

  # AND REPAIR 20B AND REPAIR 21 ARE RE-ASSERTED UNCHANGED AT THE SAME MOMENT.
  # Both are preserved repair evidence, neither is the source, and proving both
  # here is what makes "the shadow was refreshed to Repair 22 and to nothing
  # else" measurable rather than merely asserted.
  expect "Repair20B unchanged at refresh (preserved, not the source)" \
         "$(sha_of "$R20B_CANDIDATE")" "$EXP_R20B_SHA"
  expect "Repair21 unchanged at refresh (preserved, not the source)" \
         "$(sha_of "$R21_CANDIDATE")" "$EXP_R21_SHA"

  # AND THE REAL CONTROLLER IS RE-ASSERTED UNCHANGED AT THE SAME MOMENT. It is
  # not the source and it is not the destination; this proves it was not touched
  # by the one write this launcher makes into the shadow.
  expect "real controller sha256 unchanged at refresh (Repair 20)" \
         "$(sha_of "${CTRL}/nh_loop.py")"   "$EXP_LOOP_SHA"
  expect "real controller bytes  unchanged at refresh (Repair 20)" \
         "$(bytes_of "${CTRL}/nh_loop.py")" "$EXP_LOOP_BYTES"
  expect "real controller lines  unchanged at refresh (Repair 20)" \
         "$(wc -l < "${CTRL}/nh_loop.py")"  "$EXP_LOOP_LINES"

  # ATOMIC: staged, then renamed over the target within the same directory, so
  # the target is never observable half-written. A failed copy leaves the staging
  # name behind in the disposable lab and the composite proof below reports it as
  # an unexplained path rather than ignoring it.
  cp -- "$R22_CANDIDATE" "$staging" \
    || die "could not stage the Repair-22 candidate into the new shadow copy:
        ${staging}
      Nothing has been renamed over the new copy's controller."
  chmod 0644 -- "$staging" \
    || die "could not set the mode on the staged Repair-22 candidate: ${staging}"
  mv -f -- "$staging" "$target" \
    || die "could not move the staged Repair-22 candidate into place:
        ${target}"
  CONTROLLER_REFRESH="PERFORMED"
  note "the new copy's controller/nh_loop.py refreshed to the Repair-22 candidate"
}

assert_new_copy_after_refresh() {
  local target="${SHADOW_WS}/controller/nh_loop.py"
  {
    printf 'phase              after-refresh\n'
    printf 'path               %s\n' "$target"
    printf 'source             %s\n' "$R22_CANDIDATE"
    printf 'sha256             %s\n' "$(sha_of "$target")"
    printf 'bytes              %s\n' "$(bytes_of "$target")"
    printf 'lines              %s\n' "$(wc -l < "$target")"
    printf 'expected_sha256    %s\n' "$EXP_R22_SHA"
    printf 'expected_bytes     %s\n' "$EXP_R22_BYTES"
    printf 'expected_lines     %s\n' "$EXP_R22_LINES"
    printf 'real_controller    %s\n' "${CTRL}/nh_loop.py"
    printf 'real_sha256        %s\n' "$(sha_of "${CTRL}/nh_loop.py")"
    printf 'real_expected      %s\n' "$EXP_LOOP_SHA"
    printf 'repair20b_preserved %s\n' "$(sha_of "$R20B_CANDIDATE")"
    printf 'repair21_preserved %s\n' "$(sha_of "$R21_CANDIDATE")"
  } > "${PROOF}/controller-refresh.after"
  expect "new copy controller sha256 AFTER refresh (Repair 22)" \
         "$(sha_of "$target")"   "$EXP_R22_SHA"
  expect "new copy controller bytes  AFTER refresh (Repair 22)" \
         "$(bytes_of "$target")" "$EXP_R22_BYTES"
  expect "new copy controller lines  AFTER refresh (Repair 22)" \
         "$(wc -l < "$target")"  "$EXP_R22_LINES"
  expect "real controller sha256 unchanged AFTER refresh (Repair 20)" \
         "$(sha_of "${CTRL}/nh_loop.py")" "$EXP_LOOP_SHA"
  expect "Repair20B unchanged AFTER refresh (preserved, not the source)" \
         "$(sha_of "$R20B_CANDIDATE")" "$EXP_R20B_SHA"
  expect "Repair21 unchanged AFTER refresh (preserved, not the source)" \
         "$(sha_of "$R21_CANDIDATE")" "$EXP_R21_SHA"
  note "the refreshed shadow controller is the exact Repair-22 identity"
}

# THE COMPOSITE PROOF: ONE PATH CHANGED, AND ONLY ONE.
#
# The allowance list is exactly ONE entry. No seed-only allowance, no
# new-copy-only allowance, no other content allowance: at this point the new copy
# still carries the seed's own v10 marker, because the v12 marker is not placed
# until after this proof passes. That ordering is required, not incidental --
# placing the marker first would put a second legitimate difference into this
# comparison and weaken it.
assert_new_copy_differs_only_by_controller() {
  local cmp_out cmp_rc=0
  set +e
  cmp_out="$(
    PYTHONDONTWRITEBYTECODE=1 "$PY3" -B -c "$TREE_COMPARATOR" \
      "$SHADOW_WS" \
      "$REGRESSION_SOURCE" \
      "NEWCOPY" \
      "SEED" \
      "DIFFERS_EXACT:${REFRESH_ALLOWED_EXACT_LOOP}:${EXP_R22_SHA}:${EXP_SEED_LOOP_SHA}" 2>&1
  )"
  cmp_rc=$?
  set -e

  printf '%s\n' "$cmp_out" > "${PROOF}/controller-refresh.composite" 2>/dev/null || true

  case "$cmp_rc" in
    0)
      if ! printf '%s' "$cmp_out" | grep -q '^TREE_COMPARISON_CLEAN$'; then
        die "the new-copy / seed composite comparison returned success without
      stating it. Refusing to rehearse on an unreadable result."
      fi
      ;;
    1)
      die "THE CONTROLLER REFRESH CHANGED SOMETHING OTHER THAN nh_loop.py.
${cmp_out}
      The refresh is authorised for exactly one path in the new copy and for no
      other. Everything listed above is outside that authorisation -- an extra
      path, a missing path, a changed journal, a changed head, a changed key, a
      changed candidate, a changed governance file, a changed launcher, or a
      controller that is not the exact Repair-22/Repair-17 pair.
      Nothing is reverted or reconciled here. Refusing to rehearse."
      ;;
    3)
      die "THE CONTROLLER REFRESH DID NOT TAKE EFFECT.
${cmp_out}
      The new copy no longer differs from the seed in the one place it must. A
      refresh that left the copy identical to the seed would rehearse the
      Repair-17 controller while reporting a Repair-22 run."
      ;;
    *)
      die "the new-copy / seed composite comparison could not be completed
      (status ${cmp_rc}):
${cmp_out}
      A comparison that did not finish is not a comparison that passed."
      ;;
  esac
  note "the new copy differs from the regression source in EXACTLY controller/nh_loop.py"
}

# THE REGRESSION CONTINUATION STATE ITSELF, PROVED PRESERVED BY NAME.
#
# The composite proof above already covers these three files. They are proved
# again here, individually and by name, because they are the entire reason this
# regression exists: a reader must be able to see "the seven-event journal
# survived the refresh" as its own verdict, not infer it from the absence of a
# line in a listing of thousands.
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
         "$(sha_of "$nj")"   "$EXP_SEED_JOURNAL_SHA"
  expect "new copy journal bytes  (unchanged by the refresh)" \
         "$(bytes_of "$nj")" "$EXP_SEED_JOURNAL_BYTES"
  expect "new copy journal events (unchanged by the refresh)" \
         "$(grep -c '[^[:space:]]' -- "$nj" || true)" "$EXP_SEED_JOURNAL_EVENTS"
  expect "new copy journal head sha256 (unchanged by the refresh)" \
         "$(sha_of "$nh")" "$EXP_SEED_HEAD_SHA"
  expect "new copy authenticity key sha256 (unchanged by the refresh)" \
         "$(sha_of "$nk")" "$EXP_SEED_KEY_SHA"
  expect "new copy event 7 digest occurrences (unchanged by the refresh)" \
         "$(grep -c -F -- "$EXP_SEED_EVENT7_SHA" "$nj" || true)" \
         "$EXP_SEED_EVENT7_SHA_OCCURRENCES"
  expect "new copy routed signal occurrences (unchanged by the refresh)" \
         "$(grep -c -F -- "$EXP_ROUTED_SIGNAL_ID" "$nj" || true)" \
         "$EXP_SEED_ROUTED_SIGNAL_OCCURRENCES"
  expect "new copy standing target occurrences (unchanged by the refresh)" \
         "$(grep -c -F -- "$EXP_STANDING_TARGET_ID" "$nj" || true)" \
         "$EXP_SEED_STANDING_TARGET_OCCURRENCES"
  REGRESSION_CONTINUATION_STATE="PRESERVED"
  note "the new copy still carries the seven-event regression state, unaltered"
}

# THE HISTORICAL SEED, RE-READ AND PROVED UNMOVED ACROSS THE REFRESH.
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

  expect "regression seed controller sha256 AFTER the refresh (still Repair 17)" \
         "$(sha_of "$SEED_LOOP")"   "$EXP_SEED_LOOP_SHA"
  expect "regression seed controller bytes  AFTER the refresh (still Repair 17)" \
         "$(bytes_of "$SEED_LOOP")" "$EXP_SEED_LOOP_BYTES"
  expect "regression seed journal sha256 AFTER the refresh" \
         "$(sha_of "$SEED_JOURNAL")" "$EXP_SEED_JOURNAL_SHA"
  expect "regression seed journal head sha256 AFTER the refresh" \
         "$(sha_of "$SEED_JOURNAL_HEAD")" "$EXP_SEED_HEAD_SHA"
  expect "regression seed authenticity key sha256 AFTER the refresh" \
         "$(sha_of "$SEED_AUTH_KEY")" "$EXP_SEED_KEY_SHA"
  expect "regression seed v10 shadow marker sha256 AFTER the refresh" \
         "$(sha_of "${REGRESSION_SOURCE}/${SHADOW_MARKER_NAME}")" \
         "$EXP_SEED_V10_MARKER_SHA"
  note "the historical regression source is unmoved across the controller refresh"
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
assert_frozen_identities() {
  # THE REAL CONTROLLER -- Repair 20 -- PROTECTED AND NEVER WRITTEN TO.
  [ -L "${CTRL}/nh_loop.py" ] && die "the real controller is a SYMLINK: ${CTRL}/nh_loop.py"
  expect "nh_loop.py sha256"  "$(sha_of "${CTRL}/nh_loop.py")"        "$EXP_LOOP_SHA"
  expect "nh_loop.py bytes"   "$(bytes_of "${CTRL}/nh_loop.py")"      "$EXP_LOOP_BYTES"
  expect "nh_loop.py lines"   "$(wc -l < "${CTRL}/nh_loop.py")"       "$EXP_LOOP_LINES"

  # THE ACCEPTED REPAIR-20B CANDIDATE -- the refresh source, gated exactly as
  # strictly as the real controller and equally never written to.
  [ -L "$R20B_CANDIDATE" ] && die "the Repair-20B candidate is a SYMLINK: ${R20B_CANDIDATE}"
  [ -f "$R20B_CANDIDATE" ] \
    || die "the accepted Repair-20B candidate is missing from ${CTRL}; it is the
      one file this rehearsal exists to test and must be present"
  expect "Repair20B candidate sha256" "$(sha_of "$R20B_CANDIDATE")"   "$EXP_R20B_SHA"
  expect "Repair20B candidate bytes"  "$(bytes_of "$R20B_CANDIDATE")" "$EXP_R20B_BYTES"
  expect "Repair20B candidate lines"  "$(wc -l < "$R20B_CANDIDATE")"  "$EXP_R20B_LINES"

  # THE REPAIR-21 CANDIDATE -- PRESERVED REPAIR EVIDENCE in v16, not the refresh
  # source. Gated exactly as strictly as the real controller and equally never
  # written to.
  [ -L "$R21_CANDIDATE" ] && die "the Repair-21 candidate is a SYMLINK: ${R21_CANDIDATE}"
  [ -f "$R21_CANDIDATE" ] \
    || die "the Repair-21 candidate is missing from ${CTRL}; it is preserved
      repair evidence and must be present"
  expect "Repair21 candidate sha256" "$(sha_of "$R21_CANDIDATE")"   "$EXP_R21_SHA"
  expect "Repair21 candidate bytes"  "$(bytes_of "$R21_CANDIDATE")" "$EXP_R21_BYTES"
  expect "Repair21 candidate lines"  "$(wc -l < "$R21_CANDIDATE")"  "$EXP_R21_LINES"

  # THE REPAIR-22 CANDIDATE -- THE v16 REFRESH SOURCE, gated exactly as strictly
  # as the real controller and equally never written to. It is the one file this
  # rehearsal exists to test, and it is asserted here as a precondition, again
  # under both original locks, and again at the moment it is about to be read.
  [ -L "$R22_CANDIDATE" ] && die "the Repair-22 candidate is a SYMLINK: ${R22_CANDIDATE}"
  [ -f "$R22_CANDIDATE" ] \
    || die "the Repair-22 candidate is missing from ${CTRL}; it is the one file
      this rehearsal exists to test and must be present"
  expect "Repair22 candidate sha256" "$(sha_of "$R22_CANDIDATE")"   "$EXP_R22_SHA"
  expect "Repair22 candidate bytes"  "$(bytes_of "$R22_CANDIDATE")" "$EXP_R22_BYTES"
  expect "Repair22 candidate lines"  "$(wc -l < "$R22_CANDIDATE")"  "$EXP_R22_LINES"

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

  # v11 is this file's DIRECT PREDECESSOR. It RAN once, against the Repair-18
  # controller, and its lab holds the exact live failure v12 regresses. It is
  # gated by identity exactly like v1..v10.
  [ -f "${CTRL}/${LAUNCHER_V11_BASENAME}" ] \
    || die "launcher v11 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v11 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V11_BASENAME}")"   "$EXP_LAUNCHER_V11_SHA"
  expect "launcher v11 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V11_BASENAME}")" "$EXP_LAUNCHER_V11_BYTES"

  # v12 is this file's DIRECT PREDECESSOR. It was constructed and independently
  # audited, and it was DELIBERATELY NEVER RUN, because that audit found the
  # whole-historical-source gap this file closes. It is preserved unchanged as
  # blocked historical evidence and is gated by identity exactly like v1..v11.
  [ -f "${CTRL}/${LAUNCHER_V12_BASENAME}" ] \
    || die "launcher v12 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v12 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V12_BASENAME}")"   "$EXP_LAUNCHER_V12_SHA"
  expect "launcher v12 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V12_BASENAME}")" "$EXP_LAUNCHER_V12_BYTES"

  # Launcher v13 is THIS file. It cannot hash-gate on itself, but it must be the
  # file that is present, and it is carried in the before/after proof set so any
  # change to it during the run is caught.
  [ -f "${CTRL}/${LAUNCHER_V13_BASENAME}" ] \
    || die "launcher v13 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v13 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V13_BASENAME}")"   "$EXP_LAUNCHER_V13_SHA"
  expect "launcher v13 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V13_BASENAME}")" "$EXP_LAUNCHER_V13_BYTES"

  # Launcher v14 is THIS file. It cannot hash-gate on itself, but it must be the
  # file that is present, and it is carried in the before/after proof set so any
  # change to it during the run is caught.
  [ -f "${CTRL}/${LAUNCHER_V14_BASENAME}" ] \
    || die "launcher v14 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v14 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V14_BASENAME}")"   "$EXP_LAUNCHER_V14_SHA"
  expect "launcher v14 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V14_BASENAME}")" "$EXP_LAUNCHER_V14_BYTES"

  # v15 is this file's DIRECT PREDECESSOR. It RAN once, against the Repair-21
  # controller, and its lab holds the exact Stage-1 refusal v16 regresses. It is
  # now gated by exact identity like v1..v14, and that expectation was
  # established from the completed v15 lab's own preserved witnesses rather than
  # from today's filename.
  [ -f "${CTRL}/${LAUNCHER_V15_BASENAME}" ] \
    || die "launcher v15 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v15 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V15_BASENAME}")"   "$EXP_LAUNCHER_V15_SHA"
  expect "launcher v15 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V15_BASENAME}")" "$EXP_LAUNCHER_V15_BYTES"

  # Launcher v16 is THIS file. It cannot hash-gate on itself, but it must be the
  # file that is present, and it is carried in the before/after proof set so any
  # change to it during the run is caught.
  [ -s "${CTRL}/${LAUNCHER_V16_BASENAME}" ] \
    || die "launcher v16 is missing or empty at ${CTRL}/${LAUNCHER_V16_BASENAME}"
  note "all sixteen launcher artefacts present in ${CTRL}"

  # The controller bytecode, frozen by identity rather than asserted absent.
  assert_controller_bytecode_frozen "in the frozen source gate"

  # The three explained workspace-root directories, frozen by exact shape.
  assert_workspace_special_dirs

  expect "controller branch"  "$(git_ro "$CTRL" rev-parse --abbrev-ref HEAD)" "$EXP_CTRL_BRANCH"
  expect "controller HEAD"    "$(git_ro "$CTRL" rev-parse HEAD)"              "$EXP_CTRL_HEAD"

  # The controller worktree must be EXACTLY these sixteen entries and nothing
  # else: the modified nh_loop.py, the thirteen launcher artefacts, the
  # gitignored editor file, and the gitignored controller bytecode. Nothing is
  # filtered out.
  #
  # THE v13 LINE IS THE ONLY ADDITION v13 MAKES TO THIS SET. It is this file,
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
      "${CTRL_PYCACHE_STATUS_LINE}" \
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
      "?? ${R20B_CANDIDATE_BASENAME}" \
      "?? ${R21_CANDIDATE_BASENAME}" \
      "?? ${R22_CANDIDATE_BASENAME}" | LC_ALL=C sort
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

  note "every frozen identity matches; the current real source state has not moved"
  note "the regression source is the authenticated historical snapshot"
  note "the two are NOT asserted to be identical, and were never compared"
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

# The regression-source gate ran before the lab existed, so its two named proof
# artefacts had nowhere to be written. Re-run it now that the proof directory is
# there, so the artefacts exist for the audit. This is a pure re-read of the same
# read-only checks; it writes nothing outside the lab and it can only fail
# closed.
step "REGRESSION SOURCE IDENTITY AND AUTHENTICATION (recorded to proof)"
assert_regression_source
note "regression-source proof artefacts written to ${PROOF}"

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

step "REGRESSION SHADOW COPY (SOURCE: THE PRESERVED v10 CONTINUATION SHADOW)"

# THE SOURCE OF THIS COPY IS THE PRESERVED v10 SHADOW WORKSPACE, NOT THE REAL
# WORKSPACE, AND NOT THE QUESTION-DELIVERY COPY. It is the last preserved state
# that pre-dates the false v11 question, which is the whole reason it is the
# regression source.
#
# The real workspace is NOT copied. Its interview journal is NOT overlaid onto
# the seed -- there is no real interview-state overlay anywhere in this file, in
# this copy or in the namespace. Event 7 is NOT replaced. The seed journal is NOT
# reset. Real candidate state is NOT copied over the seed. The seed is NOT
# cleaned, normalised or repaired in any way.
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
rsync -aHAX --numeric-ids --delete "${REGRESSION_SOURCE}/" "${SHADOW_WS}/" \
  || die "rsync copy of the regression source into the new shadow failed"
note "regression source copied into ${SHADOW_WS}"

step "REGRESSION SHADOW COPY VERIFICATION (AGAINST THE SEED, BEFORE ANY REFRESH)"

# THIS VERIFICATION HAPPENS BEFORE THE CONTROLLER REFRESH, NOT AFTER IT. The
# order is load-bearing: refreshing first and verifying afterwards would leave the
# initial copy itself unverified, and the composite proof in section 7b would then
# be comparing a refreshed copy against a seed with no established baseline in
# between. Verified first, refreshed second, re-proved third.
#
# Checksum dry-run compare, AGAINST THE REGRESSION SOURCE -- never against the
# real workspace. Comparing the new shadow to the real workspace would be wrong on
# its face: the two legitimately differ, and v12 makes no claim about how.
#
# The exit STATUS is captured separately and is required to be zero. Discarding it
# with `|| true` would make a killed or otherwise failing dry run
# indistinguishable from a clean one.
set +e
COPY_DIFF="$(rsync -aHAXn --delete --checksum --itemize-changes "${REGRESSION_SOURCE}/" "${SHADOW_WS}/" 2>&1)"
COPY_RC=$?
set -e
if [ "$COPY_RC" -ne 0 ] || [ -n "$COPY_DIFF" ]; then
  {
    printf 'rsync verification exit status: %s\n' "$COPY_RC"
    printf '%s\n' "$COPY_DIFF"
  } > "${PROOF}/DIFF.shadow-copy.txt"
  die "the regression shadow could not be proved identical to the preserved seed
      (rsync exit status ${COPY_RC}).
      See ${PROOF}/DIFF.shadow-copy.txt
      Refusing to rehearse against a copy that is not proved truthful."
fi
note "the new shadow is a byte-truthful copy of the preserved regression source"

# ==========================================================================
# SECTION 7b — THE REPAIR-17 -> REPAIR-19B NEW-COPY CONTROLLER REFRESH
#              (still under both original locks)
# ==========================================================================
#
# Runs here, and only here: after the initial copy has been proved byte-truthful
# against the seed, and before the during-proof, the lock release and the shadow
# marker. It is inside the lock window on purpose, so the real controller that is
# read as the refresh source is the same one the under-lock frozen-identity
# assertion just proved, with no window in between, and so the during-proof that
# follows also covers the refresh.

step "NEW-COPY CONTROLLER REFRESH: BEFORE-STATE (must be the exact Repair-17 file)"
assert_new_copy_before_refresh

step "NEW-COPY CONTROLLER REFRESH: REPLACING ONLY controller/nh_loop.py"
refresh_new_copy_controller

step "NEW-COPY CONTROLLER REFRESH: AFTER-STATE (must be the exact Repair-19B file)"
assert_new_copy_after_refresh

step "NEW-COPY CONTROLLER REFRESH: COMPOSITE PROOF (exactly one path changed)"
assert_new_copy_differs_only_by_controller

step "REGRESSION CONTINUATION STATE PRESERVED (seven events, event 7 intact)"
assert_new_copy_continuation_state_preserved

step "HISTORICAL REGRESSION SOURCE UNMOVED ACROSS THE REFRESH"
assert_seed_unmoved_after_refresh

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
  die "THE REGRESSION SOURCE CHANGED WHILE THE SHADOW WAS BEING COPIED OR
      REFRESHED. The historical snapshot this regression depends on must never
      move. Refusing to rehearse."
fi
note "the regression source unchanged across the whole copy and refresh window"

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
# The seed already carries v10's own marker, because the seed IS a v10 shadow, so
# this write OVERWRITES an inherited marker in the NEW lab rather than creating a
# fresh one. Nothing is overwritten in the v10 lab: the target below is
# ${SHADOW_WS}, which is the new disposable lab, and the seed itself is never
# opened for writing. The write happens AFTER copy verification AND AFTER the
# whole section 7b refresh proof, so it can never pollute either comparison --
# both legitimately saw the v10 marker on both sides and matched it.
#
# It sits at the workspace root, outside both Git checkouts, so neither
# repository worktree status is affected.
#
# The token identifies FOUR things: Repair 19B, the v13 regression, the exact
# Repair-19B controller sha256, and the routed signal this regression exists to
# carry forward. It therefore cannot collide with any earlier rehearsal marker.
SHADOW_TOKEN="nh-shadow-repair22-regression-v16-${EXP_R22_SHA}-${EXP_ROUTED_SIGNAL_ID}"
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
# SECTION 11 — THE REPAIR-19B REGRESSION SEQUENCE
# ==========================================================================
#
# Four stages, in this exact order, each inside Bubblewrap, each AT MOST ONCE:
#
#   1. question-validation           one real fresh GPT review
#   2. question-coverage-review      one real fresh GPT review
#   3. interview-gate                read-only, no provider call
#   4. execute-next-claude-task      exactly once
#
# THERE IS EXACTLY ONE CALL SITE PER STAGE IN THIS FILE. No retry loop, no
# fallback invocation, no duplicate stage, no alternate validator, and no second
# outer correction loop. The controller's OWN internal bounded correction loop
# inside execute-next-claude-task, with its lifetime limit of 5 rounds, is
# entirely controller-owned and is neither duplicated nor bypassed here.
#
# QUESTION DELIVERY IS NOT PART OF THIS SEQUENCE AND CANNOT BE. No question is
# composed, displayed, delivered or answered. No answer of Ness's appears
# anywhere in this file. The disposable question-delivery workspace is not
# referenced. If stage 1 admits a question it stays PROVISIONAL inside the
# disposable v13 shadow, which is precisely the corrected behaviour this run
# exists to observe.
#
# CONTINUATION IS EARNED, NOT ASSUMED. A stage may only be followed by the next
# one when the stage before it PERMITS CONTINUATION, and permission is read from
# the controller's OWN reported facts rather than from an exit code alone. That
# distinction is load-bearing: a coverage review that finds possible gaps exits
# ZERO and is doing its job correctly, so an exit-code-only rule would march
# straight past exactly the finding that should stop the run.
#
# EVERY STOP BELOW IS A VALID OBSERVATIONAL OUTCOME. None of them is a launcher
# fault, none is converted into success, and none is worked around.

# THE REPORT PARSER. A structural parse, done by the same python3 the controller
# itself runs, reading only.
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

# THE NESTED READER. Same structural parse, one level deeper.
#
# IT EXISTS FOR THE REPORT ONLY AND GATES NOTHING. The authorising instruction
# requires the v13 result to state STAGE2_MISSING_GAPS and STAGE2_OVER_ASK_GAPS,
# and the controller reports those two counts inside the nested
# coverage_gaps_by_direction object. Reading them for display is not the same as
# interpreting them: no continuation decision anywhere in this file consults
# either value, and this launcher never asks whether a gap was one kind or the
# other. Stage 2 stops on coverage_possible_gaps alone.
#
# Exit status: 0 value printed, 2 unreadable, 3 no single complete report, 4 no
# such top-level key, 5 the top-level value is not an object containing the
# nested key. Anything other than 0 is reported as UNAVAILABLE and never as a
# number.
readonly REPORT_NESTED_PARSER='
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
outer = report[sys.argv[2]]
if not isinstance(outer, dict) or sys.argv[3] not in outer:
    sys.exit(5)
sys.stdout.write(
    json.dumps(outer[sys.argv[3]], sort_keys=True, separators=(",", ":"))
)
'

# require_report_value <file> <key> <expected canonical JSON> <human description>
#
# TRUE only when the controller's own report states, at TOP LEVEL, exactly
# <expected>. Unreadable, unparseable, ambiguous, absent, wrong-type and
# different all fail, and all fail CLOSED.
#
# THIS IS THE ONLY FUNCTION IN THIS FILE THAT CAN STOP THE SEQUENCE ON A
# CONTROLLER-REPORTED FACT.
require_report_value() {
  local file="$1" key="$2" expected="$3" description="$4" actual rc
  set +e
  actual="$("$PY3" -c "$REPORT_PARSER" "$file" "$key" 2>/dev/null)"
  rc=$?
  set -e
  case "$rc" in
    0) ;;
    2) SEQUENCE_STOP_REASON="the controller's report could not be read from ${file}, so ${description} could not be established"
       return 1 ;;
    3) SEQUENCE_STOP_REASON="the controller's stdout does not end in exactly one complete JSON report, so ${description} could not be established"
       return 1 ;;
    4) SEQUENCE_STOP_REASON="the controller's report states no TOP-LEVEL ${key}, so ${description} could not be established"
       return 1 ;;
    *) SEQUENCE_STOP_REASON="the controller's report could not be parsed (parser status ${rc}) while establishing ${description}"
       return 1 ;;
  esac
  if [ "$actual" != "$expected" ]; then
    SEQUENCE_STOP_REASON="${description}: the controller reports ${key} = ${actual}"
    return 1
  fi
  return 0
}

# READ-ONLY REPORT READERS. They can set no stop reason, can fail no gate, and
# are never consulted by any continuation decision. They exist so the result
# block can quote the controller's own scalars instead of paraphrasing them.
read_report_value() {
  local file="$1" key="$2" out rc
  set +e
  out="$("$PY3" -c "$REPORT_PARSER" "$file" "$key" 2>/dev/null)"
  rc=$?
  set -e
  if [ "$rc" -eq 0 ] && [ -n "$out" ]; then printf '%s' "$out"; else printf 'UNAVAILABLE'; fi
}

read_report_nested_value() {
  local file="$1" key="$2" sub="$3" out rc
  set +e
  out="$("$PY3" -c "$REPORT_NESTED_PARSER" "$file" "$key" "$sub" 2>/dev/null)"
  rc=$?
  set -e
  if [ "$rc" -eq 0 ] && [ -n "$out" ]; then printf '%s' "$out"; else printf 'UNAVAILABLE'; fi
}

# NOT-RUN is preserved as NOT-RUN. A stage that never ran has no report to quote,
# and printing UNAVAILABLE for it would blur "the sequence stopped earlier" into
# "the field was missing".
stage_scalar() {
  # stage_scalar <stage_rc> <stdout_file> <key>
  if [ "$1" = "NOT-RUN" ]; then printf 'NOT-RUN'; else read_report_value "$2" "$3"; fi
}

stage_nested_scalar() {
  # stage_nested_scalar <stage_rc> <stdout_file> <key> <nested key>
  if [ "$1" = "NOT-RUN" ]; then printf 'NOT-RUN'; else read_report_nested_value "$2" "$3" "$4"; fi
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

  # The identical argument vector every other stage and the self-test used.
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
  # immediately, so a containment failure is attributed to the stage that caused
  # it rather than discovered once at the end with no way to tell which stage
  # moved the original.
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
  printf '%s\n' "$STAGE_SOURCE_PROOF" > "${PROOF}/${slug}.source-proof"
  if [ "$STAGE_SOURCE_PROOF" = "FAIL" ]; then
    CONTAINMENT_BREACHED=1
    SEQUENCE_STOP_REASON="the protected original, a preserved lab or the regression source CHANGED during ${label}"
    say "[CONTAINMENT] a protected object changed during ${label}."
    say "              No further stage is run. Evidence is preserved."
  else
    note "protected original, preserved labs and regression source unchanged across ${label}"
  fi
}

# stage_may_continue -- true only when nothing observed so far forbids the next
# stage. Checked before every stage after the first.
stage_may_continue() {
  [ "$CONTAINMENT_BREACHED" -eq 0 ] && [ -z "$SEQUENCE_STOP_REASON" ]
}

announce_stop() {
  say ""
  say "THE SEQUENCE STOPS HERE, and that is a RESULT, not a fault:"
  say "  ${SEQUENCE_STOP_REASON}"
  say ""
  say "No further stage is run. Every artefact already captured is preserved,"
  say "and the final protected-source and containment proofs are still taken."
}

# --------------------------------------------------------------------------
# STAGE 1 — THE FRESH QUESTION-VALIDATION
# --------------------------------------------------------------------------
#
# One real GPT review, read-only against N.H, ephemeral. It is the ONLY way a
# question can come into existence, it asks Ness nothing, and it invokes Claude
# never. Nothing here answers a question, fabricates an event or edits a journal.
#
# THIS IS THE CENTRAL PURPOSE OF v12 AND OF v13. Under Repair 19B an admitted question is
# PROVISIONAL, so the ordinary corrected outcome is
#     deliverable_question_count = 0  with  provisional_question_count >= 1
# and the correct launcher behaviour is TO CONTINUE TO THE COVERAGE REVIEW, so
# the second GPT gets its chance to challenge the question before anyone calls it
# deliverable.
run_controller_stage "$STAGE1_SLUG" "$STAGE1_CMD" "STAGE 1 — question-validation"
VALIDATION_RC="$STAGE_RC"

# 1. THE STAGE ITSELF MUST HAVE SUCCEEDED.
if [ "$VALIDATION_RC" -ne 0 ]; then
  SEQUENCE_STOP_REASON="stage 1 question-validation exited ${VALIDATION_RC}"
fi

# 2. THE CONTROLLER'S OWN RESULT MUST BE CLEAN.
if stage_may_continue; then
  require_report_value "${PROOF}/${STAGE1_SLUG}.stdout" "ok" "true" \
    "stage 1 did not report a clean result" || true
fi

# 3. THE INVENTORY MUST BE USABLE AND COMPLETE. An incomplete inventory is not a
#    failure; it simply means there is nothing yet for a coverage review to
#    challenge, so the sequence stops and preserves the result.
if stage_may_continue; then
  require_report_value "${PROOF}/${STAGE1_SLUG}.stdout" \
    "validation_inventory_complete" "true" \
    "the question inventory is not complete, so there is nothing a coverage review may challenge" || true
fi
if stage_may_continue; then
  require_report_value "${PROOF}/${STAGE1_SLUG}.stdout" \
    "material_unknowns" "[]" \
    "the source check left a material unknown, so the inventory is not usable" || true
fi

# 4. THE REPAIR-19 DELIVERY GATE. THIS IS THE ONE RULE THIS REGRESSION EXISTS TO EXERCISE.
#
#    deliverable_question_count MUST BE ZERO HERE. No fresh matching coverage
#    review has run yet in this sequence, and under Repair 19B nothing can be
#    deliverable before one has cleared the question's own package. Zero is the
#    corrected behaviour and it CONTINUES the sequence.
#
#    A NON-ZERO VALUE HERE IS A REGRESSION, NOT A QUESTION FOR NESS. It would
#    mean an admitted question became deliverable before the second GPT had any
#    chance to challenge it -- which is exactly the v11 live failure. The stop
#    reason says so in those words, so nobody can read it as "the interview
#    working" the way v11's wording invited.
#
#    NOTHING ELSE ABOUT QUESTIONS IS GATED. questions_total,
#    provisional_question_count, questions_provisional_pending_coverage_review
#    and questions_withheld_pending_coverage_review are read for the report only,
#    through helpers that can stop nothing. "A question exists" is NOT a stop
#    condition in v12 or v13.
if stage_may_continue; then
  require_report_value "${PROOF}/${STAGE1_SLUG}.stdout" \
    "deliverable_question_count" "0" \
    "THE REPAIR-19 DELIVERY GATE REGRESSED -- a question is deliverable before any fresh matching coverage review has cleared it, which is the exact v11 failure this run exists to regress" || true
fi

if ! stage_may_continue; then
  announce_stop
else
  note "stage 1 permits continuation: the inventory is complete and NOTHING is"
  note "deliverable yet. Any admitted question is still provisional and the fresh"
  note "independent coverage review now gets its chance to challenge it."
  # ------------------------------------------------------------------------
  # STAGE 2 — THE FRESH INDEPENDENT COVERAGE REVIEW
  # ------------------------------------------------------------------------
  #
  # One real GPT review. It challenges the COMPLETE inventory stage 1 just
  # recorded. It cannot create a question, cannot address Ness and cannot unlock
  # anything by itself.
  run_controller_stage "$STAGE2_SLUG" "$STAGE2_CMD" "STAGE 2 — question-coverage-review"
  COVERAGE_RC="$STAGE_RC"

  # 1. TECHNICAL FAILURE STOPS.
  if [ "$COVERAGE_RC" -ne 0 ]; then
    SEQUENCE_STOP_REASON="stage 2 question-coverage-review exited ${COVERAGE_RC}"
  fi

  # 2. THE CONTROLLER'S OWN RESULT MUST BE CLEAN.
  if stage_may_continue; then
    require_report_value "${PROOF}/${STAGE2_SLUG}.stdout" "ok" "true" \
      "stage 2 did not report a clean result" || true
  fi

  # 3. A POSSIBLE GAP STOPS AND PRESERVES THE RESULT.
  #
  #    A GAP EXITS ZERO. Read the finding, not the status.
  #
  #    THIS LAUNCHER DOES NOT INTERPRET THE GAP. It does not turn it into a
  #    question, does not deliver it, does not answer it, does not run any
  #    question-delivery command, and does not decide -- and has no code able to
  #    decide -- whether the gap was a missing choice or an over-ask. The
  #    controller owns every part of that classification. Stopping here is a
  #    VALID LIVE RESULT.
  if stage_may_continue; then
    require_report_value "${PROOF}/${STAGE2_SLUG}.stdout" \
      "coverage_possible_gaps" "0" \
      "the fresh coverage review found a possible gap and routed it as a signal; this is a valid live result and the launcher preserves it without interpreting it" || true
  fi

  # 4. AND A CLEARANCE MUST ACTUALLY HAVE BEEN RECORDED. Zero gaps without a
  #    recorded clearance is an inconsistent result, and inconsistent fails
  #    closed rather than being read as success.
  if stage_may_continue; then
    require_report_value "${PROOF}/${STAGE2_SLUG}.stdout" \
      "coverage_review_cleared" "true" \
      "the fresh coverage review reported no gaps but recorded no clearance, which is inconsistent" || true
  fi

  if ! stage_may_continue; then
    announce_stop
  else
    note "stage 2 permits continuation: zero possible gaps AND a recorded clearance"
    # ----------------------------------------------------------------------
    # STAGE 3 — THE INTERVIEW GATE
    # ----------------------------------------------------------------------
    #
    # Read-only. No provider call of any kind. It reports the exact clearance
    # that execute-next-claude-task itself enforces. This launcher asks Ness
    # nothing here and never forces a gate open.
    run_controller_stage "$STAGE3_SLUG" "$STAGE3_CMD" "STAGE 3 — interview-gate"
    GATE_RC="$STAGE_RC"

    if [ "$GATE_RC" -ne 0 ]; then
      SEQUENCE_STOP_REASON="stage 3 interview-gate exited ${GATE_RC}"
    fi
    if stage_may_continue; then
      # A CLOSED GATE EXITS ZERO and reports itself. It is a legitimate state and
      # it stops the sequence. EXIT CODE 0 ALONE IS NEVER ENOUGH.
      require_report_value "${PROOF}/${STAGE3_SLUG}.stdout" \
        "mechanical_path_unlocked" "true" \
        "the mechanical Claude path is CLOSED for this package, and this launcher never forces it open" || true
    fi

    if ! stage_may_continue; then
      announce_stop
    else
      note "stage 3 permits continuation: the interview gate is genuinely unlocked"
      # --------------------------------------------------------------------
      # STAGE 4 — THE ONE EXECUTE
      # --------------------------------------------------------------------
      #
      # EXACTLY ONE outer execution of the controller. There is no retry here and
      # nothing reruns it. The controller owns everything inside it: the GPT
      # mechanical design specification, Claude's application of it, the fresh
      # GPT/Codex audit, the same-session Claude corrections and its own lifetime
      # limit of 5 correction rounds. This launcher does not reinterpret audit
      # findings and implements no second repair loop.
      #
      # WHATEVER EXECUTE REPORTS IS THE FINAL v13 RESULT.
      run_controller_stage "$STAGE4_SLUG" "$STAGE4_CMD" "STAGE 4 — execute-next-claude-task"
      EXEC_RC="$STAGE_RC"
      # The last stage's own failure is a stop reason too, so the summary states
      # WHY the run ended rather than leaving a bare status to be interpreted.
      # The controller's own non-zero status is still what this launcher returns;
      # this only names it.
      if [ "$EXEC_RC" -ne 0 ] && [ -z "$SEQUENCE_STOP_REASON" ]; then
        SEQUENCE_STOP_REASON="stage 4 execute-next-claude-task exited ${EXEC_RC}"
      fi
    fi
  fi
fi

# The exit status this launcher will finally return for the controller portion of
# the run: the status of the LAST stage that actually ran. Every individual stage
# status is also written to its own file and printed in the summary, so no reader
# ever has to infer a stage's result from this single number.
#
# nh_loop.py defines exactly three exit codes -- 0, 1 and 2 -- so this value can
# never collide with the reserved safety codes 90-94 used below.
if   [ "$EXEC_RC"       != "NOT-RUN" ]; then SHADOW_RC="$EXEC_RC"
elif [ "$GATE_RC"       != "NOT-RUN" ]; then SHADOW_RC="$GATE_RC"
elif [ "$COVERAGE_RC"   != "NOT-RUN" ]; then SHADOW_RC="$COVERAGE_RC"
else                                          SHADOW_RC="$VALIDATION_RC"
fi

# --------------------------------------------------------------------------
# THE CONTROLLER-OWNED SCALARS THE RESULT BLOCK QUOTES
# --------------------------------------------------------------------------
#
# Extracted ONCE, here, after every stage that was going to run has run, and used
# only for display. Not one of these values influenced any continuation decision:
# every gate above had already been evaluated by require_report_value before this
# point is reached.
S1_OUT="${PROOF}/${STAGE1_SLUG}.stdout"
S2_OUT="${PROOF}/${STAGE2_SLUG}.stdout"
S3_OUT="${PROOF}/${STAGE3_SLUG}.stdout"
S4_OUT="${PROOF}/${STAGE4_SLUG}.stdout"

OBS_S1_DELIVERABLE="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "deliverable_question_count")"
OBS_S1_PROVISIONAL="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "provisional_question_count")"
OBS_S1_QUESTIONS_TOTAL="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "questions_total")"
OBS_S1_INVENTORY_COMPLETE="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "validation_inventory_complete")"
OBS_S1_STOP_REASON="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "interview_stop_reason")"
# The additional controller-owned Stage-1 fields v15 records so the
# source-closure question can be read from the controller's own report rather
# than inferred. Each is read exactly as every other scalar is read, and an
# absent field reports itself absent rather than defaulting to anything.
OBS_S1_OK="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "ok")"
OBS_S1_MATERIAL_UNKNOWNS="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "material_unknowns")"
OBS_S1_AUTH_USED="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "authenticated_revalidation_identity_used")"
OBS_S1_AUTH_ROOT="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "authenticated_revalidation_root_path")"
OBS_S1_AUTH_SCOPE="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "authenticated_revalidation_package_scope_id")"
OBS_S1_SOURCE_BINDING="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "source_binding_sha256")"
OBS_S1_SOURCE_MANIFEST="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "source_manifest_sha256")"
OBS_S1_VALIDATION_SET="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "validation_set_id")"

# --- THE REPAIR-22-SPECIFIC STAGE-1 OBSERVATIONS (NEW IN v16) ---
#
# These exist so a reader can see, from the controller's OWN report, whether
# Repair 22 reached and exercised its new PRE-CALL path at all -- deriving the
# exact relevant-source closure before Codex is invoked, stating it in the
# prompt, and carrying it across the model-call boundary -- and then what the
# post-validation boundary recorded.
#
# EVERY ONE OF THEM IS READ-ONLY AND GATES NOTHING. They are read through
# stage_scalar, which can set no stop reason and can fail no gate, and not one
# of them is consulted by any continuation decision anywhere in this file.
#
# NO VALUE IS INVENTED. A field the controller did not report comes back as
# UNAVAILABLE, and a stage that never ran comes back as NOT-RUN. Neither is
# ever silently rendered as a number, as a path count or as a pass.
OBS_S1_AUTH_CHAIN="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "authenticated_revalidation_chain_paths")"
OBS_S1_PRECALL_REQUIRED_PATHS="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "precall_required_relevant_source_paths")"
OBS_S1_PRECALL_CLOSURE_SHA="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "precall_required_relevant_source_closure_sha256")"
OBS_S1_PRECALL_BINDING_SHA="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "precall_package_source_binding_sha256")"
OBS_S1_PRECALL_BINDING_SEEDS="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "precall_package_source_binding_seeds")"
OBS_S1_PRECALL_STATED_IN_PROMPT="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "precall_required_source_stated_in_prompt")"
OBS_S1_SOURCE_PATHS_CHECKED="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "validation_source_paths_checked")"
OBS_S1_CLOSURE_PATHS="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "relevant_closure_paths")"
OBS_S1_CLOSURE_SHA="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "relevant_closure_sha256")"
OBS_S1_BINDING_SHA="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "package_source_binding_sha256")"
OBS_S1_BINDING_SEEDS="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "package_source_binding_seeds")"
OBS_S1_ADMITTED="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "validation_admitted")"
OBS_S1_PARKED="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "validation_parked")"
OBS_S1_REFUSED="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "validation_refused")"
OBS_S1_STRIPPED="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "validation_stripped")"
OBS_S1_ERRORS="$(stage_scalar "$VALIDATION_RC" "$S1_OUT" "errors")"

OBS_S2_CLEARED="$(stage_scalar "$COVERAGE_RC" "$S2_OUT" "coverage_review_cleared")"
OBS_S2_POSSIBLE_GAPS="$(stage_scalar "$COVERAGE_RC" "$S2_OUT" "coverage_possible_gaps")"
OBS_S2_MISSING_GAPS="$(stage_nested_scalar "$COVERAGE_RC" "$S2_OUT" "coverage_gaps_by_direction" "missing")"
OBS_S2_OVER_ASK_GAPS="$(stage_nested_scalar "$COVERAGE_RC" "$S2_OUT" "coverage_gaps_by_direction" "over_ask")"
OBS_S2_STOP_REASON="$(stage_scalar "$COVERAGE_RC" "$S2_OUT" "interview_stop_reason")"

OBS_S3_UNLOCKED="$(stage_scalar "$GATE_RC" "$S3_OUT" "mechanical_path_unlocked")"
OBS_S3_STOP_REASON="$(stage_scalar "$GATE_RC" "$S3_OUT" "interview_stop_reason")"

OBS_S4_STOP_REASON="$(stage_scalar "$EXEC_RC" "$S4_OUT" "stop_reason")"
OBS_S4_INTERVIEW_STOP_REASON="$(stage_scalar "$EXEC_RC" "$S4_OUT" "interview_stop_reason")"

{
  printf 'CONTROLLER-OWNED OBSERVATION EXTRACTION\n'
  printf '=======================================\n'
  printf 'Extracted for display only. No value below gated anything.\n\n'
  printf 'STAGE 1 question-validation\n'
  printf '  exit                          %s\n' "$VALIDATION_RC"
  printf '  ok / stop reason              %s\n' "$OBS_S1_STOP_REASON"
  printf '  validation_inventory_complete %s\n' "$OBS_S1_INVENTORY_COMPLETE"
  printf '  questions_total               %s   <- NOT a gate in v13\n' "$OBS_S1_QUESTIONS_TOTAL"
  printf '  provisional_question_count    %s   <- NOT a gate in v13\n' "$OBS_S1_PROVISIONAL"
  printf '  deliverable_question_count    %s   <- the ONE gated question field\n' "$OBS_S1_DELIVERABLE"
  printf '\nSTAGE 2 question-coverage-review\n'
  printf '  exit                          %s\n' "$COVERAGE_RC"
  printf '  interview_stop_reason         %s\n' "$OBS_S2_STOP_REASON"
  printf '  coverage_review_cleared       %s\n' "$OBS_S2_CLEARED"
  printf '  coverage_possible_gaps        %s   <- the gated field\n' "$OBS_S2_POSSIBLE_GAPS"
  printf '  gaps_by_direction.missing     %s   <- reported, never interpreted\n' "$OBS_S2_MISSING_GAPS"
  printf '  gaps_by_direction.over_ask    %s   <- reported, never interpreted\n' "$OBS_S2_OVER_ASK_GAPS"
  printf '\nSTAGE 3 interview-gate\n'
  printf '  exit                          %s\n' "$GATE_RC"
  printf '  mechanical_path_unlocked      %s\n' "$OBS_S3_UNLOCKED"
  printf '  interview_stop_reason         %s\n' "$OBS_S3_STOP_REASON"
  printf '\nSTAGE 4 execute-next-claude-task\n'
  printf '  exit                          %s\n' "$EXEC_RC"
  printf '  stop_reason                   %s\n' "$OBS_S4_STOP_REASON"
  printf '  interview_stop_reason         %s\n' "$OBS_S4_INTERVIEW_STOP_REASON"
} > "${PROOF}/controller-observations.txt" 2>/dev/null || true

# ==========================================================================
# SECTION 11b — REPAIR-19B REGRESSION V13 OBSERVATIONS
#               (READ-ONLY, DECIDES NOTHING)
# ==========================================================================
#
# A convenience pass over the lab's OWN captured output, so the behaviour of all
# four stages is easy to inspect without reading thousands of lines by hand.
#
# IT RECORDS; IT DECIDES NOTHING. It sets no verdict, it can fail no check, and
# every safety verdict below is computed entirely separately.
#
# NO PARTICULAR NATURAL OUTCOME IS REQUIRED. In particular:
#   - a validation that admits a PROVISIONAL question is Repair 19 working;
#   - a coverage gap is the fresh review doing its job;
#   - a CLOSED interview gate is a legitimate state;
#   - ZERO Claude invocations may be entirely correct;
#   - stages left NOT-RUN are the sequence stopping where it should.
# These observations record what happened. They do not invent PASS.
#
# It reads only the stage files this launcher created. It never reads the shadow
# candidates and never echoes candidate content: it prints scalar,
# controller-owned report fields and fixed live-progress marker counts, each
# truncated, plus routed SIGNAL IDENTIFIERS, which are controller-generated ids
# and carry no design or question text.
step "REPAIR-22 REGRESSION V16 OBSERVATIONS"

observe_repair22_regression_v16() {
  local out="${PROOF}/repair22-regression-v16-observations.txt"
  local s1="$S1_OUT" s2="$S2_OUT" s3="$S3_OUT" s4="$S4_OUT"
  local s4e="${PROOF}/${STAGE4_SLUG}.stderr"
  local n_new n_resume n_seed n_audit n_verdict n_corrspec n_stopreview n_gapline

  n_new="$(grep -c -F -- 'invoking claude (new session'                        "$s4e" 2>/dev/null || true)"
  n_resume="$(grep -c -F -- 'resuming the package claude session'              "$s4e" 2>/dev/null || true)"
  n_seed="$(grep -c -F -- 'next target seeded byte-identical'                  "$s4e" 2>/dev/null || true)"
  n_audit="$(grep -c -F -- 'fresh codex design audit starting'                 "$s4e" 2>/dev/null || true)"
  n_verdict="$(grep -c -F -- 'codex verdict for'                               "$s4e" 2>/dev/null || true)"
  n_corrspec="$(grep -c -F -- 'running ONE fresh gpt correction-specification' "$s4e" 2>/dev/null || true)"
  n_stopreview="$(grep -c -F -- 'running ONE fresh gpt review of the claude specification stop' "$s4e" 2>/dev/null || true)"
  n_gapline="$(grep -c -E '^       routed signal '                             "$s2" 2>/dev/null || true)"

  {
    printf 'REPAIR-22 REGRESSION V16 OBSERVATIONS -- descriptive only, no verdict\n'
    printf '=====================================================================\n\n'

    printf 'WHAT THIS RUN REGRESSED\n'
    printf '  regression source : %s\n' "$REGRESSION_SOURCE"
    printf '  source mode       : %s\n' "$REGRESSION_SOURCE_MODE"
    printf '  seed journal      : %s events, sha256 %s\n' \
           "$EXP_SEED_JOURNAL_EVENTS" "$EXP_SEED_JOURNAL_SHA"
    printf '  seed journal head : sha256 %s\n' "$EXP_SEED_HEAD_SHA"
    printf '  last seed event   : %s, sha256 %s\n' \
           "$EXP_SEED_EVENT7_TYPE" "$EXP_SEED_EVENT7_SHA"
    printf '  routed signal     : %s\n' "$EXP_ROUTED_SIGNAL_ID"
    printf '  standing target   : %s\n' "$EXP_STANDING_TARGET_ID"
    printf '  package scope     : %s\n' "$EXP_PKG_SCOPE"
    printf '\n'
    printf '  THIS SEED PRE-DATES THE FALSE v11 QUESTION. That is why it is the\n'
    printf '  regression source: the defect can only be exercised from a state in\n'
    printf '  which the question has not yet been admitted. No answered\n'
    printf '  question-delivery state was used, and no answer of Ness\047s appears\n'
    printf '  anywhere in this launcher.\n'
    printf '\n'
    printf '  IT IS A HISTORICAL SNAPSHOT AND IS NOT CLAIMED TO BE TODAY\047S REAL\n'
    printf '  WORKSPACE. The real N.H checkout has legitimately moved since it was\n'
    printf '  taken. That movement was protected and witnessed, never reconciled:\n'
    printf '  nothing was reset, reverted, checked out or copied back.\n'
    printf '\n'
    printf 'THE CONTROLLER REFRESH THIS RUN PERFORMED\n'
    printf '  seed controller   : %s  (Repair 17)\n' "$EXP_SEED_LOOP_SHA"
    printf '  refreshed to      : %s  (Repair 22 candidate)\n' "$EXP_R22_SHA"
    printf '  real controller   : %s  (Repair 20, NOT installed, unchanged)\n' "$EXP_LOOP_SHA"
    printf '  Repair20B         : %s  (preserved, NOT a refresh source)\n' "$EXP_R20B_SHA"
    printf '  Repair21          : %s  (preserved, NOT a refresh source)\n' "$EXP_R21_SHA"
    printf '  refresh state     : %s\n' "$CONTROLLER_REFRESH"
    printf '  continuation state: %s\n' "$REGRESSION_CONTINUATION_STATE"
    printf '  paths refreshed   : controller/nh_loop.py, and no other\n'
    printf '\n'
    printf '  The refresh was applied to the NEW disposable copy only, after that\n'
    printf '  copy had been proved byte-truthful against the seed, and it was\n'
    printf '  proved afterwards to have changed exactly one path. The interview\n'
    printf '  journal, journal head and authenticity key were NOT refreshed and\n'
    printf '  remain byte-identical to the seed. The historical v10 lab was not\n'
    printf '  written to at any point.\n\n'

    printf 'STAGE EXIT CODES AND TIMESTAMPS\n'
    printf '  stage 1  question-validation      : %s\n' "$VALIDATION_RC"
    printf '  stage 2  question-coverage-review : %s\n' "$COVERAGE_RC"
    printf '  stage 3  interview-gate           : %s\n' "$GATE_RC"
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
      printf 'THE SEQUENCE STOPPED EARLY, on purpose:\n  %s\n\n' "$SEQUENCE_STOP_REASON"
    else
      printf 'Every stage that was reached permitted the next one.\n\n'
    fi

    printf 'HOW TO READ THESE CODES\n'
    printf '  The controller uses exactly three: 0 ok, 1 fail-closed, 2 usage.\n'
    printf '  A coverage review that FINDS POSSIBLE GAPS exits 0 -- it routes each\n'
    printf '  gap as a signal. A CLOSED interview gate also exits 0 and reports\n'
    printf '  itself. So an exit code alone never decides whether the next stage\n'
    printf '  may run; the controller-owned fields below are what decide.\n\n'

    printf '==========================================\n'
    printf 'STAGE 1 -- FRESH QUESTION-VALIDATION\n'
    printf '==========================================\n'
    printf 'THE REPAIR-19 DELIVERY GATE, AS THIS RUN OBSERVED IT:\n'
    printf '  questions_total            %s   (NOT a gate in v13)\n' "$OBS_S1_QUESTIONS_TOTAL"
    printf '  provisional_question_count %s   (NOT a gate in v13)\n' "$OBS_S1_PROVISIONAL"
    printf '  deliverable_question_count %s   (the ONE gated question field)\n' "$OBS_S1_DELIVERABLE"
    printf '\n'
    printf '  ADMITTED != DELIVERABLE. A question that exists is not a question\n'
    printf '  that may be put to Ness. Only a current, matching, fresh independent\n'
    printf '  coverage review can make an admitted question deliverable, and this\n'
    printf '  launcher stopped on nothing except that one field.\n\n'
    grep -E '"(ok|interview_stop_reason|validation_set_id|validation_pages_recorded|validation_pages_expected|validation_inventory_complete|deliverable_question_count|provisional_question_count|questions_provisional_pending_coverage_review|questions_withheld_pending_coverage_review|coverage_cleared_package_scopes|questions_total|stale_question_count|revalidation_required|routed_issues_awaiting_validation|codex_invoked|codex_invocations|codex_exit_code|expected_validation_page|continuing_validation_set_id|authenticated_revalidation_identity_used|authenticated_revalidation_package_scope_id|authenticated_revalidation_root_path|authenticated_revalidation_historical_validation_set_id|authenticated_identity_grants_no_clearance)":' \
         "$s1" 2>/dev/null | cut -c1-200 || true
    printf '\n'

    printf '==========================================\n'
    printf 'STAGE 2 -- FRESH INDEPENDENT COVERAGE REVIEW\n'
    printf '==========================================\n'
    printf 'THE GATED FIELD AND THE TWO REPORTED-ONLY DIRECTION COUNTS:\n'
    printf '  coverage_possible_gaps     %s   (the gated field)\n' "$OBS_S2_POSSIBLE_GAPS"
    printf '  coverage_review_cleared    %s   (also gated)\n' "$OBS_S2_CLEARED"
    printf '  gaps_by_direction.missing  %s   (reported, never interpreted)\n' "$OBS_S2_MISSING_GAPS"
    printf '  gaps_by_direction.over_ask %s   (reported, never interpreted)\n' "$OBS_S2_OVER_ASK_GAPS"
    printf '\n'
    printf '  THIS LAUNCHER DID NOT CLASSIFY ANY GAP. It did not decide whether a\n'
    printf '  finding was a missing choice or an over-ask, did not turn any gap\n'
    printf '  into a question, did not deliver one and did not answer one. Repair\n'
    printf '  19A\047s over-ask identity rule and Repair 19B\047s separation of the\n'
    printf '  challengeable set from the shown set are entirely controller-owned.\n\n'
    grep -E '"(ok|interview_stop_reason|coverage_review_invoked|coverage_review_exit_code|coverage_review_cleared|coverage_possible_gaps|coverage_gaps_by_direction|coverage_challengeable_question_ids|coverage_shown_question_ids|coverage_over_ask_findings|coverage_validation_not_current|coverage_authenticated_root_used|coverage_validation_set_id|coverage_package_scope_id|coverage_scope_root_path|coverage_source_paths_checked|coverage_manifest_sha256|coverage_relevant_closure_paths|coverage_inventory_issue_count|coverage_binding_bytes)":' \
         "$s2" 2>/dev/null | cut -c1-200 || true
    printf '\n'
    printf 'ROUTED REVIEW SIGNALS (identifiers only, never gap wording):\n'
    printf '  routed signal lines recorded: %s\n' "$n_gapline"
    grep -E '^       routed signal ' "$s2" 2>/dev/null | head -50 | cut -c1-200 || true
    printf '  (listing bounded to the first 50; the count above is complete.)\n'
    printf '  A routed signal is NOT a question. It is handed to the ordinary\n'
    printf '  question-validation stage, which alone may ever make a question.\n\n'

    printf '==========================================\n'
    printf 'STAGE 3 -- INTERVIEW GATE (read-only)\n'
    printf '==========================================\n'
    printf '  mechanical_path_unlocked   %s\n' "$OBS_S3_UNLOCKED"
    printf '\n'
    grep -E '"(ok|interview_stop_reason|mechanical_path_unlocked|coverage_review_current|coverage_review_validation_set_id|validation_set_id|validation_inventory_complete|revalidation_required|open_group_index|stale_question_count|routed_issues_awaiting_validation)":' \
         "$s3" 2>/dev/null | cut -c1-200 || true
    printf '\n'

    printf '==========================================\n'
    printf 'STAGE 4 -- EXECUTE-NEXT-CLAUDE-TASK (one only)\n'
    printf '==========================================\n'
    printf '  stop_reason                %s\n' "$OBS_S4_STOP_REASON"
    printf '\n'
    printf 'CONFIGURATION THIS CONTROLLER IS FROZEN TO:\n'
    grep -E '"(claude_model|claude_output_format|claude_allowed_tools|claude_permission_mode|claude_package_session_scope|claude_timeout_seconds)":' \
         "$s4" 2>/dev/null | cut -c1-200 || true
    printf '\n'
    printf 'THE PIECE-3 SEAM (did the gate let this run begin at all):\n'
    grep -E '"(piece3_interview_gate_enforced|piece3_interview_gate_unlocked|piece3_question_validation_required|piece3_route)":' \
         "$s4" 2>/dev/null | cut -c1-200 || true
    printf '\n'
    printf 'THE GPT MECHANICAL DESIGN SPECIFICATION (presence and validation):\n'
    grep -E '"(preparation_ok|prepared_classification|claude_instruction_source|mechanical_design_specification_sha256)":' \
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
      printf '  Stage 4 never ran, so every count above is necessarily zero. That\n'
      printf '  is not a failure: the sequence stopped earlier, for the reason\n'
      printf '  recorded at the top of this file, and stopping there is exactly\n'
      printf '  what the gate exists to do.\n'
    elif [ "${n_new:-0}" -eq 0 ] 2>/dev/null; then
      printf '  ZERO Claude invocations. This is NOT automatically a failure: the\n'
      printf '  controller enforces the interview gate again in its own right, and\n'
      printf '  may fail closed before Claude is considered. Read\n'
      printf '  piece3_interview_gate_unlocked and stop_reason above.\n'
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
    printf '  The lifetime correction allowance is 5 rounds. It is owned by\n'
    printf '  nh_loop.py and this launcher neither sets nor influences it; the\n'
    printf '  correction_round_limit field above is the controller stating it.\n'
    printf '  The OpenAI reasoning role is gpt-5.6-sol at effort high, invoked\n'
    printf '  through the read-only, ephemeral Codex CLI transport. Claude is\n'
    printf '  claude-opus-5 at xhigh. Both are the controller-owned configuration\n'
    printf '  frozen into nh_loop.py sha256 %s --\n' "$EXP_LOOP_SHA"
    printf '  this launcher sets neither and overrides neither.\n\n'

    printf 'THIS SECTION DECIDES NOTHING\n'
    printf '  It assigns no verdict, passes nothing and fails nothing. The only\n'
    printf '  verdicts this launcher holds are the containment, regression-source\n'
    printf '  and credential ones in the RESULT block, and they are computed\n'
    printf '  entirely separately.\n'
  } > "$out" 2>/dev/null || true

  note "repair-22 regression v16 observations written to ${out}"
}
observe_repair22_regression_v16 || true

# --------------------------------------------------------------------------
# THE EXACT-REGRESSION OBSERVATIONS -- THREE OF THEM IN v16
# --------------------------------------------------------------------------
#
# v16 CARRIES v15's TWO EARLIER OBSERVATIONS FORWARD UNCHANGED and adds exactly
# ONE new one for the exact blocker the completed v15 run exposed:
#
#   question-validation derived a relevant-source closure for the bound package
#   and then refused the model because source_paths_checked omitted files of
#   that closure -- a closure the model had never been given before the call.
#
# THE NEW OBSERVATION DELIBERATELY DOES NOT REQUIRE ANY PARTICULAR COUNT. The
# completed v15 run said "81 file(s)", but the defect under test is MISSING
# REQUIRED CLOSURE PATHS, not the spelling of a number. Pinning the count would
# make the observation report false on a recurrence of the very same defect
# with one more or one fewer file, which is the opposite of what it is for.
#
# ALL THREE OBSERVATIONS CONTROL NO STAGE AND GRANT NO PASS, and false is never
# automatically a pass for any of them.
#
# DESCRIPTIVE ONLY. It classifies nothing, decides no policy, and grants no
# pass. It reports whether the EXACT technical refusal the completed v13 run
# produced recurs, and it reports it as one plainly named field.
#
# The v13 failure was, precisely:
#   question-validation -> QUESTION_VALIDATION_REFUSED, because issue
#   authority_control_retry_values_scope quoted the accepted B9 retry-values
#   PACKAGE_COMPLETE closure record, and the controller reported that the
#   quotation lay inside "0 bounded source record(s)" -- because the
#   hard-wrapped bold Package-status statement was not an admitted bounded
#   record form.
#
# ABSENCE OF THE OLD STRING IS NOT A PASS AND IS NOT REPORTED AS ONE. Stage 1
# can fail for entirely unrelated reasons, or not run at all, and this section
# says so rather than inferring success. The launcher's safety verdict is
# computed elsewhere and is not touched here.
step "REPAIR-22 EXACT REGRESSION OBSERVATION"

same_message() {
  # same_message <needle> [<needle> ...] -> "yes" | "no"
  # MATCH only when ONE diagnostic message carries every needle.
  local verdict
  verdict="$(
    PYTHONDONTWRITEBYTECODE=1 "$PY3" -B -c "$SAME_MESSAGE_MATCHER" \
      "$S1_OUT" "${PROOF}/${STAGE1_SLUG}.stderr" "$@" 2>/dev/null
  )" || verdict="NO-MATCH"
  case "$verdict" in
    MATCH) printf 'yes' ;;
    *)     printf 'no' ;;
  esac
}

observe_exact_regressions() {
  local out="${PROOF}/repair22-exact-regression.txt"
  local s1="$S1_OUT" s1e="${PROOF}/${STAGE1_SLUG}.stderr"
  local issue="authority_control_retry_values_scope"
  local b9="NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md"
  local zero="0 bounded source record(s)"
  local outside="outside the relevant source closure"
  local unrelated="a witness from unrelated material proves nothing about this package"
  # THE TWO NEEDLES OF THE NEW v16 OBSERVATION. Both must occur inside ONE SAME
  # Stage-1 diagnostic message. NO COUNT IS REQUIRED: the completed v15 run said
  # "81 file(s)", but the defect being tested is missing required closure paths,
  # not the spelling of the count, so the number is deliberately absent from both
  # needles and the text between them is spanned by the message itself.
  local nocheck="codex question-validation did not check"
  local derived="inside the relevant source closure this controller derived for the package"
  local r20b="false" r21="false" r22="false" b9_anywhere="no" stage1_ran="yes"

  if [ "$VALIDATION_RC" = "NOT-RUN" ] || [ ! -s "$s1" ] && [ ! -s "$s1e" ]; then
    stage1_ran="no"
  fi

  if [ "$stage1_ran" = "yes" ]; then
    # A. THE v13 PARSER REFUSAL -- all three components in ONE message.
    [ "$(same_message "$issue" "$b9" "$zero")" = "yes" ] && r20b="true"
    # B. THE v14 SOURCE-CLOSURE REFUSAL -- all four components in ONE message.
    [ "$(same_message "$issue" "$b9" "$outside" "$unrelated")" = "yes" ] && r21="true"
    # C. THE v15 MISSING-CLOSURE-PATH REFUSAL -- the exact blocker Repair 22
    #    exists for. Both components in ONE message, through the same
    #    SAME-MESSAGE machinery, with no count required.
    [ "$(same_message "$nocheck" "$derived")" = "yes" ] && r22="true"
    grep -q -F -- "$b9" "$s1" 2>/dev/null && b9_anywhere="yes"
    grep -q -F -- "$b9" "$s1e" 2>/dev/null && b9_anywhere="yes"
  fi

  {
    printf 'REPAIR-22 / REPAIR-21 / REPAIR-20B EXACT REGRESSION OBSERVATION\n'
    printf '  -- descriptive only, no verdict, gates no stage\n'
    printf '======================================================================\n\n'
    printf 'WHAT THIS OBSERVES\n'
    printf '  whether any of the three exact prior Stage-1 refusals recurs under\n'
    printf '  Repair 22. It assigns no verdict, passes nothing and gates no stage.\n\n'
    printf 'HOW A RECURRENCE IS DECIDED (CORRECTED IN v15, UNCHANGED IN v16)\n'
    printf '  Every component must occur inside ONE SAME diagnostic message.\n'
    printf '  v14 tested the components independently across all Stage-1 output,\n'
    printf '  which made two always-true halves and could report a recurrence\n'
    printf '  that never happened. That predicate is not used here.\n'
    printf '  The new v16 test requires NO count: the defect is missing required\n'
    printf '  closure paths, not the spelling of the number of them.\n\n'
    printf 'CONTROLLER UNDER TEST\n'
    printf '  shadow controller  : %s  (Repair 22 candidate)\n' "$EXP_R22_SHA"
    printf '  real controller    : %s  (Repair 20, unchanged, NOT installed)\n' "$EXP_LOOP_SHA"
    printf '  Repair20B          : %s  (preserved, NOT the refresh source)\n' "$EXP_R20B_SHA"
    printf '  Repair21           : %s  (preserved, NOT the refresh source)\n' "$EXP_R21_SHA"
    printf '  refresh state      : %s\n\n' "$CONTROLLER_REFRESH"
    printf 'STAGE 1 question-validation -- CONTROLLER-OWNED FIELDS\n'
    printf '  exit                                    %s\n' "$VALIDATION_RC"
    printf '  ok                                      %s\n' "$OBS_S1_OK"
    printf '  interview_stop_reason                   %s\n' "$OBS_S1_STOP_REASON"
    printf '  validation_inventory_complete           %s\n' "$OBS_S1_INVENTORY_COMPLETE"
    printf '  material_unknowns                       %s\n' "$OBS_S1_MATERIAL_UNKNOWNS"
    printf '  questions_total                         %s\n' "$OBS_S1_QUESTIONS_TOTAL"
    printf '  provisional_question_count              %s\n' "$OBS_S1_PROVISIONAL"
    printf '  deliverable_question_count              %s\n' "$OBS_S1_DELIVERABLE"
    printf '  authenticated_revalidation_identity_used %s\n' "$OBS_S1_AUTH_USED"
    printf '  authenticated_revalidation_root_path    %s\n' "$OBS_S1_AUTH_ROOT"
    printf '  authenticated_revalidation_package_scope_id %s\n' "$OBS_S1_AUTH_SCOPE"
    printf '  source_binding_sha256                   %s\n' "$OBS_S1_SOURCE_BINDING"
    printf '  source_manifest_sha256                  %s\n' "$OBS_S1_SOURCE_MANIFEST"
    printf '  validation_set_id                       %s\n' "$OBS_S1_VALIDATION_SET"
    printf '  authenticated_revalidation_chain_paths  %.400s\n\n' "$OBS_S1_AUTH_CHAIN"
    printf 'THE REPAIR-22 PRE-CALL PATH, AS THE CONTROLLER REPORTED IT\n'
    printf '  These five fields exist only in Repair 22. They say whether the\n'
    printf '  controller derived the exact relevant-source closure BEFORE Codex\n'
    printf '  was invoked, and whether it stated that exact required path list in\n'
    printf '  the prompt. UNAVAILABLE means the controller did not report the\n'
    printf '  field -- most likely because the run never reached that boundary --\n'
    printf '  and NOT-RUN means Stage 1 never ran. Neither is a pass and neither\n'
    printf '  is a number.\n'
    printf '  precall_required_relevant_source_paths          %s\n' "$OBS_S1_PRECALL_REQUIRED_PATHS"
    printf '  precall_required_relevant_source_closure_sha256 %s\n' "$OBS_S1_PRECALL_CLOSURE_SHA"
    printf '  precall_package_source_binding_sha256           %s\n' "$OBS_S1_PRECALL_BINDING_SHA"
    printf '  precall_package_source_binding_seeds            %.400s\n' "$OBS_S1_PRECALL_BINDING_SEEDS"
    printf '  precall_required_source_stated_in_prompt        %s\n\n' "$OBS_S1_PRECALL_STATED_IN_PROMPT"
    printf 'THE POST-VALIDATION RECORD BOUNDARY, IF STAGE 1 REACHED IT\n'
    printf '  Long list fields are truncated for display only; the complete\n'
    printf '  controller output is preserved verbatim in the Stage-1 stdout file.\n'
    printf '  validation_source_paths_checked   %.400s\n' "$OBS_S1_SOURCE_PATHS_CHECKED"
    printf '  relevant_closure_paths            %.400s\n' "$OBS_S1_CLOSURE_PATHS"
    printf '  relevant_closure_sha256           %s\n' "$OBS_S1_CLOSURE_SHA"
    printf '  package_source_binding_sha256     %s\n' "$OBS_S1_BINDING_SHA"
    printf '  package_source_binding_seeds      %.400s\n' "$OBS_S1_BINDING_SEEDS"
    printf '  validation_admitted               %.400s\n' "$OBS_S1_ADMITTED"
    printf '  validation_parked                 %.400s\n' "$OBS_S1_PARKED"
    printf '  validation_refused                %.400s\n' "$OBS_S1_REFUSED"
    printf '  validation_stripped               %.400s\n' "$OBS_S1_STRIPPED"
    printf '  errors                            %.400s\n\n' "$OBS_S1_ERRORS"
    printf 'THE AUTHENTICATED CHAIN AND THE LIST FIELDS, AS THE CONTROLLER PRINTED THEM\n'
    printf '  (verbatim controller lines; this launcher interprets none of them)\n'
    if [ -s "$s1" ]; then
      grep -E '"(authenticated_revalidation_chain_paths|validation_admitted|validation_parked|validation_refused|validation_stripped|material_unknowns|errors)"' "$s1" 2>/dev/null | cut -c1-400 | sed 's/^/  /' || true
    else
      printf '  (no Stage-1 stdout)\n'
    fi
    printf '\n'
    printf 'RELEVANT-SOURCE CLOSURE, IF THE CONTROLLER REPORTED ONE\n'
    if [ -s "$s1" ] && grep -qE '"(relevant_closure_paths|relevant_closure_path_count|relevant_closure_sha256)"' "$s1" 2>/dev/null; then
      grep -E '"(relevant_closure_paths|relevant_closure_path_count|relevant_closure_sha256)"' "$s1" | cut -c1-400 | sed 's/^/  /'
    else
      printf '  UNAVAILABLE -- the controller did not report a closure count or\n'
      printf '  path set in its ordinary output. No count is inferred here, and no\n'
      printf '  number from any offline analysis is carried into this evidence.\n'
    fi
    printf '\n'
    printf 'COMPONENT PRESENCE (informational; NOT the recurrence test)\n'
    printf '  Stage 1 produced output                 : %s\n' "$stage1_ran"
    printf '  B9 closure basename anywhere in output  : %s\n\n' "$b9_anywhere"
    printf 'SAME-MESSAGE RECURRENCE TESTS\n'
    printf '  A. v13 parser refusal   (issue + B9 + "%s")\n' "$zero"
    printf 'REPAIR20B_EXACT_REGRESSION_RECURRED = %s\n\n' "$r20b"
    printf '  B. v14 closure refusal  (issue + B9 + "%s" + "%s")\n' "$outside" "$unrelated"
    printf 'REPAIR21_EXACT_REGRESSION_RECURRED = %s\n\n' "$r21"
    printf '  C. v15 missing-closure-path refusal, THE EXACT BLOCKER REPAIR 22\n'
    printf '     EXISTS FOR   ("%s"\n' "$nocheck"
    printf '                   + "%s")\n' "$derived"
    printf '     No count is required, by design.\n'
    printf 'REPAIR22_EXACT_REGRESSION_RECURRED = %s\n\n' "$r22"
    printf 'HOW TO READ THIS SECTION\n'
    printf '  true  means that exact prior refusal happened again, in one message.\n'
    printf '  false is NOT a pass. Stage 1 may have failed for an entirely\n'
    printf '  different reason, or may not have run at all. Read the Stage-1 exit\n'
    printf '  and interview_stop_reason above, and the launcher RESULT block,\n'
    printf '  which this section does not influence. No semantic classification is\n'
    printf '  made here and none may be inferred from it.\n\n'
    printf 'THE THREE OUTCOMES THIS RUN EXISTS TO DISTINGUISH\n'
    printf '  A. REPAIR22_EXACT_REGRESSION_RECURRED = true\n'
    printf '     The same missing-relevant-closure-path refusal appeared again.\n'
    printf '  B. REPAIR22_EXACT_REGRESSION_RECURRED = false AND Stage 1 stopped\n'
    printf '     later for another ordinary controller reason. THIS IS A VALID\n'
    printf '     RESULT. Repair 22\047s own offline audit observed that the unchanged\n'
    printf '     closure machinery may afterwards expose unresolved-reference\n'
    printf '     material. Nothing in this launcher fixes, bypasses, suppresses\n'
    printf '     or reinterprets that: a later MATERIAL_UNKNOWN or any other\n'
    printf '     existing gate is preserved exactly and stops the sequence under\n'
    printf '     the ordinary rules. The next blocker is not launcher work.\n'
    printf '  C. Stage 1 fully succeeded and the normal sequence continued.\n'
    printf '  Read STAGE1_QUESTION_VALIDATION_EXIT, interview_stop_reason and\n'
    printf '  SEQUENCE_STOP_REASON in the RESULT block to tell them apart. This\n'
    printf '  section chooses between them for nobody.\n'
  } > "$out" 2>/dev/null || true

  REPAIR20B_EXACT_REGRESSION_RECURRED="$r20b"
  REPAIR21_EXACT_REGRESSION_RECURRED="$r21"
  REPAIR22_EXACT_REGRESSION_RECURRED="$r22"
  printf '%s\n' "REPAIR20B_EXACT_REGRESSION_RECURRED=${r20b}"
  printf '%s\n' "REPAIR21_EXACT_REGRESSION_RECURRED=${r21}"
  printf '%s\n' "REPAIR22_EXACT_REGRESSION_RECURRED=${r22}"
}

observe_exact_regressions || true

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

# All three containment verdicts are SETTLED at this exact point, so the flag is
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
printf 'N.H SHADOW REHEARSAL (v16, REPAIR-22 REGRESSION) — RESULT\n'
printf '===========================================================\n'
printf 'SHADOW_LAB=%s\n'                        "$LAB"
printf 'REGRESSION_SOURCE=%s\n'                 "$REGRESSION_SOURCE"
printf 'REGRESSION_SOURCE_MODE=%s\n'            "$REGRESSION_SOURCE_MODE"
printf 'FROZEN_REAL_CONTROLLER_SHA256=%s\n'     "$EXP_LOOP_SHA"
printf 'REAL_CONTROLLER_IS_REPAIR20=YES\n'
printf 'REAL_CONTROLLER_INSTALLED_REPAIR22=NO\n'
printf 'REAL_CONTROLLER_INSTALLED_REPAIR21=NO\n'
printf 'REAL_CONTROLLER_INSTALLED_REPAIR20B=NO\n'
printf 'REPAIR22_ACCEPTED=NO\n'
printf 'SHADOW_CONTROLLER_UNDER_TEST=REPAIR22\n'
printf 'SHADOW_CONTROLLER_SHA256=%s\n'          "$EXP_R22_SHA"
printf 'SHADOW_CONTROLLER_SOURCE=%s\n'          "$R22_CANDIDATE"
printf 'SHADOW_REFRESH_SOURCE_IS_REPAIR22_ONLY=YES\n'
printf 'REPAIR20B_PRESERVED_SHA256=%s\n'        "$EXP_R20B_SHA"
printf 'REPAIR20B_USED_AS_REFRESH_SOURCE=NO\n'
printf 'REPAIR21_PRESERVED_SHA256=%s\n'         "$EXP_R21_SHA"
printf 'REPAIR21_USED_AS_REFRESH_SOURCE=NO\n'
printf 'PREDECESSOR_LAUNCHER=%s\n'              "$LAUNCHER_V15_BASENAME"
printf 'PREDECESSOR_LAUNCHER_SHA256=%s\n'       "$EXP_LAUNCHER_V15_SHA"
printf 'PREDECESSOR_LAB=%s\n'                   "$PRESERVED_LAB_REPAIR21_V15"
printf 'REPAIR20B_EXACT_REGRESSION_RECURRED=%s\n' "$REPAIR20B_EXACT_REGRESSION_RECURRED"
printf 'REPAIR21_EXACT_REGRESSION_RECURRED=%s\n' "$REPAIR21_EXACT_REGRESSION_RECURRED"
printf 'REPAIR22_EXACT_REGRESSION_RECURRED=%s\n' "$REPAIR22_EXACT_REGRESSION_RECURRED"
printf 'RECURRENCE_TEST_REQUIRES_SAME_DIAGNOSTIC_MESSAGE=YES\n'
printf 'REPAIR22_RECURRENCE_TEST_REQUIRES_EXACT_COUNT=NO\n'
printf 'EXACT_REGRESSION_OBSERVATIONS_GATE_NO_STAGE=YES\n'
printf 'SEED_CONTROLLER_SHA256=%s\n'            "$EXP_SEED_LOOP_SHA"
printf 'CONTROLLER_REFRESH=%s\n'                "$CONTROLLER_REFRESH"
printf 'REGRESSION_CONTINUATION_STATE=%s\n'     "$REGRESSION_CONTINUATION_STATE"
printf 'REGRESSION_SEED_JOURNAL_EVENTS=%s\n'    "$EXP_SEED_JOURNAL_EVENTS"
printf 'REGRESSION_ROUTED_SIGNAL=%s\n'          "$EXP_ROUTED_SIGNAL_ID"
printf 'REGRESSION_STANDING_TARGET=%s\n'        "$EXP_STANDING_TARGET_ID"
printf 'REGRESSION_PACKAGE_SCOPE=%s\n'          "$EXP_PKG_SCOPE"
printf '\n'
printf 'HISTORICAL_SEED_EXPECTATION_SOURCE=PRESERVED_V11_WITNESSES\n'
printf 'HISTORICAL_SEED_EXPECTATION_FROM_CURRENT_SEED=NO\n'
printf 'HISTORICAL_SEED_MANIFEST_SHA256=%s\n'   "$EXP_HIST_SEED_MANIFEST_SHA"
printf 'HISTORICAL_SEED_MANIFEST_ENTRIES=%s\n'  "$EXP_HIST_SEED_MANIFEST_ENTRIES"
printf 'HISTORICAL_SEED_MANIFEST_FILES=%s\n'    "$EXP_HIST_SEED_MANIFEST_FILES"
printf 'HISTORICAL_SEED_MANIFEST_DIRS=%s\n'     "$EXP_HIST_SEED_MANIFEST_DIRS"
printf 'HISTORICAL_SEED_MANIFEST_SYMLINKS=%s\n' "$EXP_HIST_SEED_MANIFEST_SYMLINKS"
printf '\n'
printf 'STAGE1_QUESTION_VALIDATION_EXIT=%s\n'   "$VALIDATION_RC"
printf 'STAGE1_OK=%s\n'                         "$OBS_S1_OK"
printf 'STAGE1_INTERVIEW_STOP_REASON=%s\n'      "$OBS_S1_STOP_REASON"
printf 'STAGE1_VALIDATION_INVENTORY_COMPLETE=%s\n' "$OBS_S1_INVENTORY_COMPLETE"
printf 'STAGE1_MATERIAL_UNKNOWNS=%.400s\n'      "$OBS_S1_MATERIAL_UNKNOWNS"
printf 'STAGE1_QUESTIONS_TOTAL=%s\n'            "$OBS_S1_QUESTIONS_TOTAL"
printf 'STAGE1_DELIVERABLE_QUESTION_COUNT=%s\n' "$OBS_S1_DELIVERABLE"
printf 'STAGE1_PROVISIONAL_QUESTION_COUNT=%s\n' "$OBS_S1_PROVISIONAL"
printf 'STAGE1_AUTH_REVALIDATION_IDENTITY_USED=%s\n' "$OBS_S1_AUTH_USED"
printf 'STAGE1_AUTH_REVALIDATION_ROOT_PATH=%.400s\n' "$OBS_S1_AUTH_ROOT"
printf 'STAGE1_AUTH_REVALIDATION_CHAIN_PATHS=%.400s\n' "$OBS_S1_AUTH_CHAIN"
printf 'STAGE1_AUTH_REVALIDATION_PACKAGE_SCOPE_ID=%s\n' "$OBS_S1_AUTH_SCOPE"
printf 'STAGE1_SOURCE_BINDING_SHA256=%s\n'      "$OBS_S1_SOURCE_BINDING"
printf '\n'
printf 'STAGE1_PRECALL_REQUIRED_RELEVANT_SOURCE_PATHS=%s\n'          "$OBS_S1_PRECALL_REQUIRED_PATHS"
printf 'STAGE1_PRECALL_REQUIRED_RELEVANT_SOURCE_CLOSURE_SHA256=%s\n' "$OBS_S1_PRECALL_CLOSURE_SHA"
printf 'STAGE1_PRECALL_PACKAGE_SOURCE_BINDING_SHA256=%s\n'           "$OBS_S1_PRECALL_BINDING_SHA"
printf 'STAGE1_PRECALL_PACKAGE_SOURCE_BINDING_SEEDS=%.400s\n'        "$OBS_S1_PRECALL_BINDING_SEEDS"
printf 'STAGE1_PRECALL_REQUIRED_SOURCE_STATED_IN_PROMPT=%s\n'        "$OBS_S1_PRECALL_STATED_IN_PROMPT"
printf '\n'
printf 'STAGE1_VALIDATION_SOURCE_PATHS_CHECKED=%.400s\n' "$OBS_S1_SOURCE_PATHS_CHECKED"
printf 'STAGE1_RELEVANT_CLOSURE_PATHS=%.400s\n' "$OBS_S1_CLOSURE_PATHS"
printf 'STAGE1_RELEVANT_CLOSURE_SHA256=%s\n'    "$OBS_S1_CLOSURE_SHA"
printf 'STAGE1_PACKAGE_SOURCE_BINDING_SHA256=%s\n' "$OBS_S1_BINDING_SHA"
printf 'STAGE1_PACKAGE_SOURCE_BINDING_SEEDS=%.400s\n' "$OBS_S1_BINDING_SEEDS"
printf 'STAGE1_SOURCE_MANIFEST_SHA256=%s\n'     "$OBS_S1_SOURCE_MANIFEST"
printf 'STAGE1_VALIDATION_SET_ID=%s\n'          "$OBS_S1_VALIDATION_SET"
printf 'STAGE1_VALIDATION_ADMITTED=%.400s\n'    "$OBS_S1_ADMITTED"
printf 'STAGE1_VALIDATION_PARKED=%.400s\n'      "$OBS_S1_PARKED"
printf 'STAGE1_VALIDATION_REFUSED=%.400s\n'     "$OBS_S1_REFUSED"
printf 'STAGE1_VALIDATION_STRIPPED=%.400s\n'    "$OBS_S1_STRIPPED"
printf 'STAGE1_ERRORS=%.400s\n'                 "$OBS_S1_ERRORS"
printf 'STAGE1_LONG_FIELDS_TRUNCATED_FOR_DISPLAY=YES\n'
printf '\n'
printf 'STAGE2_COVERAGE_REVIEW_EXIT=%s\n'       "$COVERAGE_RC"
printf 'STAGE2_COVERAGE_REVIEW_CLEARED=%s\n'    "$OBS_S2_CLEARED"
printf 'STAGE2_COVERAGE_POSSIBLE_GAPS=%s\n'     "$OBS_S2_POSSIBLE_GAPS"
printf 'STAGE2_MISSING_GAPS=%s\n'               "$OBS_S2_MISSING_GAPS"
printf 'STAGE2_OVER_ASK_GAPS=%s\n'              "$OBS_S2_OVER_ASK_GAPS"
printf '\n'
printf 'STAGE3_INTERVIEW_GATE_EXIT=%s\n'        "$GATE_RC"
printf 'STAGE3_GATE_UNLOCKED=%s\n'              "$OBS_S3_UNLOCKED"
printf '\n'
printf 'STAGE4_EXECUTE_EXIT=%s\n'               "$EXEC_RC"
printf 'STAGE4_STOP_REASON=%s\n'                "$OBS_S4_STOP_REASON"
printf '\n'
printf 'SEQUENCE_STOP_REASON=%s\n'              "${SEQUENCE_STOP_REASON:-none}"
printf 'SHADOW_CONTROLLER_EXIT=%s\n'            "$SHADOW_RC"
printf '\n'
printf 'ORIGINAL_WORKSPACE_PROOF=%s\n'          "$ORIGINAL_PROOF"
printf 'PRESERVED_LAB_PROOF=%s\n'               "$PRESERVED_LAB_PROOF"
printf 'REGRESSION_SEED_PROOF=%s\n'             "$REGRESSION_SEED_PROOF"
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
printf 'PROOF_ORIGINAL_AFTER_STAGE1=%s\n'            "${PROOF}/original.after-${STAGE1_SLUG}"
printf 'PROOF_ORIGINAL_AFTER_STAGE2=%s\n'            "${PROOF}/original.after-${STAGE2_SLUG}"
printf 'PROOF_ORIGINAL_AFTER_STAGE3=%s\n'            "${PROOF}/original.after-${STAGE3_SLUG}"
printf 'PROOF_ORIGINAL_AFTER_STAGE4=%s\n'            "${PROOF}/original.after-${STAGE4_SLUG}"
printf 'PROOF_ORIGINAL_AFTER=%s\n'                   "${PROOF}/original.after"
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
printf 'PROOF_V16_OBSERVATIONS=%s\n'                 "${PROOF}/repair22-regression-v16-observations.txt"
printf 'PROOF_REPAIR22_REGRESSION=%s\n'              "${PROOF}/repair22-exact-regression.txt"
printf '===========================================================\n'

printf '\nSHADOW_CONTROLLER_EXIT is the status of the LAST stage that ran, and\n'
printf 'nothing more. Each stage has its own exit code above and its own\n'
printf 'exit-code file in the proof directory, so no stage result has to be\n'
printf 'inferred from that one number. NOT-RUN means the sequence stopped before\n'
printf 'that stage; IT IS NOT A PASS AND IT IS NOT A FAILURE, and a run that\n'
printf 'stopped early is never labelled a failure merely because a later stage\n'
printf 'did not run.\n'

printf '\nAN EXIT OF 0 IS NOT PERMISSION TO CONTINUE. A coverage review that\n'
printf 'finds possible gaps routes each one as a signal and exits 0; a CLOSED\n'
printf 'interview gate reports itself and exits 0. This launcher therefore reads\n'
printf 'the controller-owned state fields, never the status alone, and\n'
printf 'SEQUENCE_STOP_REASON above states in plain words why the sequence ended\n'
printf 'where it did.\n'

printf '\nWHAT THIS REGRESSION WAS FOR\n'
printf '  ADMITTED != DELIVERABLE. Under Repair 19B a newly admitted question is\n'
printf '  provisional until a fresh, current, matching coverage review has\n'
printf '  cleared its package. STAGE1_PROVISIONAL_QUESTION_COUNT above may\n'
printf '  therefore be non-zero while STAGE1_DELIVERABLE_QUESTION_COUNT is zero,\n'
printf '  and that combination is the CORRECTED behaviour, not a fault: it is\n'
printf '  what lets stage 2 run at all.\n'
printf '  This launcher stopped on deliverable_question_count and on nothing else\n'
printf '  about questions. It did not stop merely because a question exists.\n'

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
  printf '\nTHE REGRESSION SOURCE CHANGED DURING THIS RUN. The historical snapshot\n'
  printf 'this whole regression depends on must never move, and a change to it\n'
  printf 'outranks any apparent controller result. See the DIFF.after-seed.*\n'
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
printf '  GPT/Claude output this rehearsal produced exists ONLY inside the\n'
printf '  disposable shadow. The real workspace was re-proved from outside the\n'
printf '  namespace after the run, and that verdict is ORIGINAL_WORKSPACE_PROOF\n'
printf '  above.\n'
printf '\n  THE HISTORICAL SNAPSHOT AND TODAY\047S REAL WORKSPACE ARE TWO DIFFERENT\n'
printf '  THINGS, AND THIS RUN NEVER CLAIMED OTHERWISE.\n'
printf '  The regression source is a preserved historical shadow that pre-dates\n'
printf '  the false v11 question. The current real N.H checkout has legitimately\n'
printf '  moved since it was taken -- including the Unreal/Wonder design work --\n'
printf '  and that movement was PROTECTED, not reconciled. Nothing was reset,\n'
printf '  reverted, checked out, cleaned or copied back; no Git write of any kind\n'
printf '  was issued; and no current N.H work was copied into the regression\n'
printf '  source. The two were never compared to each other.\n'
printf '\n  THE HISTORICAL SEED WAS PROVED WHOLE, AGAINST EVIDENCE OLDER THAN THIS\n'
printf '  LAUNCHER. Every entry beneath the regression source -- every ordinary\n'
printf '  N.H source and design file, every directory, every permission mode and\n'
printf '  the seed\047s own Git metadata -- was proved identical to what the\n'
printf '  preserved, completed v11 run recorded in its own proof captures. That\n'
printf '  expectation was NOT computed from the seed as it stands today, because\n'
printf '  doing so would have blessed any change that had already happened. All\n'
printf '  four v11 captures had to yield one identical manifest; there was no\n'
printf '  majority vote and no fallback. This matters because question-validation\n'
printf '  and question-coverage-review read the actual source files, so a changed\n'
printf '  historical source would silently change the answer being tested.\n'
printf '\n  THE CONTROLLER REFRESH CHANGED THE NEW COPY AND NOTHING ELSE.\n'
printf '  controller/nh_loop.py inside the disposable v16 shadow was replaced\n'
printf '  with the REPAIR-22 CANDIDATE, which was opened read-only as the source\n'
printf '  and was never written to. Repair 22 was the ONLY refresh source: the\n'
printf '  real controller is still Repair 20 and was never a source and never a\n'
printf '  destination, and Repair 20B and Repair 21 are preserved repair\n'
printf '  evidence that this run read, proved unchanged, and never copied into\n'
printf '  the shadow. Repair 22 IS NOT INSTALLED AND IS NOT ACCEPTED. The\n'
printf '  historical seed still carries its own Repair-17 controller. The\n'
printf '  seven-event journal, its head and the authenticity key were not\n'
printf '  refreshed and are byte-identical to the seed.\n'
printf '\n  WHAT THIS RUN WAS TESTING, EXACTLY.\n'
printf '  The completed v15 rehearsal stopped at Stage 1 because\n'
printf '  question-validation derived a relevant-source closure for the bound\n'
printf '  package and then refused the model for not having checked files of\n'
printf '  that closure -- a closure the model was never given before the call.\n'
printf '  Repair 22 derives the closure BEFORE the call, states the exact\n'
printf '  required paths in the prompt, carries that frozen closure across the\n'
printf '  model-call boundary, and validates against that same closure\n'
printf '  afterwards. This launcher tested THAT correction and nothing broader:\n'
printf '  it implements none of those four steps and interprets none of them.\n'
printf '\n  A LATER STOP IS A VALID RESULT AND WAS NOT WORKED AROUND.\n'
printf '  If Stage 1 passed the Repair-22 boundary and then stopped on an\n'
printf '  existing MATERIAL_UNKNOWN or any other existing controller gate, that\n'
printf '  stop was preserved exactly under the ordinary rules. No gate was\n'
printf '  altered, relaxed, bypassed or reinterpreted to make Repair 22 look\n'
printf '  successful, and the next blocker was not turned into launcher work.\n'
printf '\n  NO QUESTION WAS DELIVERED, COMPOSED OR ANSWERED. No question-delivery\n'
printf '  command was invoked, no question-delivery workspace was used, and this\n'
printf '  launcher asked Ness nothing. That is the point: the corrected\n'
printf '  pre-delivery machinery was given its chance to work BEFORE Ness is\n'
printf '  involved.\n'
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
# success; a preserved-evidence mismatch outranks it too; and a moved regression
# source outranks everything about the controller, because it means the run did
# not regress what it said it regressed. All five safety verdicts use reserved
# codes the controller never returns, so a containment failure can never be
# mistaken for an ordinary controller exit, and an ordinary controller exit can
# never be mistaken for a containment failure.
if [ "$ORIGINAL_PROOF" = "FAIL" ]; then
  exit "$RC_ORIGINAL_PROOF_FAIL"
fi
if [ "$PRESERVED_LAB_PROOF" = "FAIL" ]; then
  exit "$RC_PRESERVED_LAB_PROOF_FAIL"
fi
if [ "$REGRESSION_SEED_PROOF" = "FAIL" ]; then
  exit "$RC_REGRESSION_SEED_PROOF_FAIL"
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

# THE CONTROLLER'S OWN FAILURE, PRESERVED VERBATIM. If a stage returned 1 or 2
# that is the controller fail-closing, and this launcher reports exactly what it
# said rather than replacing it with a status of its own.
if [ "$SHADOW_RC" -ne 0 ]; then
  exit "$SHADOW_RC"
fi

# A SEQUENCE THAT STOPPED ON A ZERO EXIT. The stage succeeded as a command and
# the sequence still stopped: an incomplete inventory, a material unknown, a
# pre-coverage delivery regression, a coverage gap or a closed gate. That is not
# success and must not be reported as one, so it gets its own status.
if [ -n "$SEQUENCE_STOP_REASON" ]; then
  exit "$RC_SEQUENCE_STOPPED"
fi

# All four stages ran, the execute returned 0, and every safety verdict passed.
exit 0

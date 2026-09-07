#!/usr/bin/env bash
#
# NH_SHADOW_REHEARSAL_LAUNCHER_v10.sh
#
# N.H SHADOW LIVE REHEARSAL LAUNCHER — v10  (REPAIR-17 CONTROLLER, CONTINUATION)
#
# WHAT THIS IS
#   A disposable-laboratory launcher, and specifically a CONTINUATION one. It
#   proves the protected original N.H / controller workspace has not moved,
#   makes an exact throwaway copy of THE PRESERVED v9 SHADOW WORKSPACE rather
#   than of the real workspace, proves that seed still represents the current
#   real source, hides the real /home/ness behind a tmpfs, republishes that
#   continuation copy at the
#   EXACT normal path /home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP inside a Bubblewrap
#   namespace, runs the REPAIR-17 sequence
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
#   original and against every preserved lab in the exact sense defined
#   immediately below.
#
#   A controller PASS inside the shadow means ONLY that the isolated real
#   rehearsal reached its own PASS. It means nothing about N.H acceptance.
#
# READ-ONLY, STATED EXACTLY
#   This launcher deliberately does NOT claim "never modified" or "never
#   written" about the protected original or about any preserved rehearsal lab.
#   Those phrases would be false, and a safety launcher that overstates its own
#   guarantee is worse than one that states a narrower true one. What follows is
#   the whole claim, and nothing anywhere else in this file means more than it.
#
#   SCOPE. This describes what THIS LAUNCHER'S OWN CODE does, outside the
#   Bubblewrap namespace. It says NOTHING about the sandboxed controller runs.
#   Whether those runs stayed contained is not asserted here; it is settled only
#   by the before/after proof in section 12, and until that proof completes the
#   report says so in as many words.
#
#   WHAT IS NEVER ISSUED. Against the protected original and against every
#   preserved lab, this launcher's own code issues no create, write, append,
#   truncate, rename, hard link, symlink, unlink, rmdir, chmod, chown or utimes
#   operation. Every regular-file open of those paths is read-only. Verified by
#   enumerating every mutating command in this file: all of them target the lab,
#   the shadow copy, or the in-namespace overlays.
#
#   THE THREE OPERATIONS THAT ARE NOT PLAIN READS, NAMED. No closed list of
#   "read-only tools" is given here, because such a list is easy to write and
#   easy to get wrong -- this file's ancestor previously carried one that omitted
#   wc, grep, the shell's own `exec N<` redirections and, worse, flock. The claim
#   is about operations, not binaries. Three operations against protected paths
#   are not plain content reads, and all three are deliberate:
#     1. flock(2). Section 6 opens nh_candidate_transaction.lock and
#        nh_interview_journal.lock for reading and takes an EXCLUSIVE advisory
#        lock on each. That is kernel state attached to the open file
#        description, not a change to file content or to any metadata field,
#        and both locks are released in section 8 before the namespace is ever
#        entered. It is done precisely because flock is the same primitive the
#        controller itself takes, so it genuinely excludes a concurrent
#        controller instead of merely hoping for one.
#     2. A namespace-private bind mount. Section 9 binds the shadow over the
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
#   file.
#
#   CONSEQUENCE. No content, mode, owner, group, size, mtime, ctime, inode or
#   link count of any protected or preserved file is altered by this launcher's
#   own code. atime may be refreshed. Two advisory locks are taken and released.
#   Nothing else.
#
#   Everywhere below, "read-only" means exactly this and nothing stronger.
#
# GOVERNING AUTHORITY (unchanged by this file)
#   1. NH_MASTER-20_CORRECTED_v10.md      <- wins all conflicts
#   2. NH_DECISION_DEFAULTS-S19_v2_3.md   <- ADOPTED BY NESS 2026-08-13
#   3. cursorrules
#   4. NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md
#   Ness owns meaning, policy, acceptance, adoption and permission to build.
#
#   The adopted Decision Defaults are v2.3. v4 of this launcher named v2.2,
#   which was correct when v4 was written and is now historical: v2.3 was
#   adopted on 2026-08-13, supersedes v2.2, and preserves v2.2 unchanged as
#   prior authority. This line is INFORMATIONAL ONLY. This launcher enforces no
#   Decision Defaults rule and derives no behaviour from either file; it names
#   the current authority so an operator reading it is not told a stale one.
#
#   v2.3's revised §0 working division is the division Repair 11 mechanises:
#   GPT determines the exact bounded mechanical design or correction
#   specification, Claude APPLIES that specification and does not independently
#   choose a different N.H design, and Ness alone owns meaning and acceptance.
#   This launcher observes that division being exercised. It enforces none of
#   it -- the controller does -- and it decides nothing about whether the
#   controller got it right.
#
# ==========================================================================
# WHAT v10 IS, AND WHAT IT CHANGES
# ==========================================================================
#
#   v10 IS A BOUNDED CONTINUATION REBASE OF v9, NOT A REDESIGN.
#   It starts from the exact bytes of NH_SHADOW_REHEARSAL_LAUNCHER_v9.sh
#   (sha256 9d1f4218..., 187641 bytes, 3562 lines) and changes ONLY what
#   CONTINUING THE PRESERVED v9 SHADOW STATE mechanically requires. Every
#   isolation guarantee and every proof v1..v9 earned is carried forward
#   unchanged, and the v9..v2 histories below are retained deliberately so none
#   of it can be lost.
#
#   THE ONE DEFINING CHANGE.
#     THE SHADOW COPY SOURCE IS NO LONGER THE REAL WORKSPACE.
#     It is the preserved v9 shadow workspace:
#       /home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR17_6a3ce02e...
#         /shadow/NH_CLAUDE_CODEX_DESIGN_LOOP
#     Everything else follows from that.
#
#   WHY. v9 RAN, exactly once, and it stopped exactly where it should have.
#   Stage 1 question-validation exited 0 with a complete inventory and no
#   deliverable question; stage 2 question-coverage-review exited 0 and reported
#   coverage_possible_gaps = 1, so stages 3 and 4 were never reached. In doing
#   so the coverage review appended ONE authenticated journal event -- event 7,
#   type review_signal_recorded -- into the v9 SHADOW journal and nowhere else.
#   That event is the routed signal
#       rs_2593b06ab1684bbf19a6ffb70d915bd2
#   against standing target
#       st_028ac341df713a4c189028c9971b4375
#   and it exists ONLY inside that preserved shadow. The real workspace journal
#   still has its own five events and is NOT touched by this launcher. Copying
#   the real workspace again would therefore throw the routed signal away and
#   re-run the same seam from the same starting state. Copying the preserved v9
#   shadow instead is the whole point of v10: EVENT 7 SURVIVES.
#
#   WHAT v10 CHANGES FROM v9, AND ONLY THIS:
#     - THE SHADOW COPY SOURCE, and the copy VERIFICATION source with it. Both
#       are now the preserved v9 continuation seed. The verification compares
#       the new shadow against THAT seed, never against the real workspace as
#       if the two were identical -- they are not, and section 4c proves
#       exactly how they differ;
#     - a new CONTINUATION PRECONDITION (section 4b). The v9 lab and its seed
#       must be present, real directories and not symlinks; the seed journal
#       must hold exactly seven events; event 7 must be the last event and must
#       carry the exact type, route, signal source, routed signal id, standing
#       target id, issue key, finding key, package scope, event digest and
#       previous digest frozen below; and the WHOLE seven-event chain and the
#       journal head must AUTHENTICATE under the controller's OWN digest, HMAC
#       and head semantics -- not merely parse as JSON. Any failure refuses the
#       run before the isolation self-test and therefore before any possible
#       provider call;
#     - a new CURRENT-SOURCE COMPATIBILITY GATE (section 4c). A continuation may
#       not run stale source. The complete file/path/content difference set
#       between the real workspace and the seed is computed, and exactly four
#       differences are permitted: the seed carries the v9 shadow marker; the
#       seed journal and journal head carry the seven-event continuation state
#       while the real ones carry five; and the real workspace carries this
#       launcher, which the historical seed cannot. ANY other difference of any
#       kind -- an extra path, a missing path, a changed byte in nh_loop.py, a
#       changed governance file, a changed candidate, a changed launcher --
#       FAILS THE RUN CLOSED, before any provider call;
#     - v9's own identity is now frozen and gated, as v1..v8 already are;
#     - v10 itself now exists in controller/, so the exact expected controller
#       worktree gains one more entry -- still an EXACT match, never
#       "anything untracked is acceptable";
#     - a fresh disposable CONTINUATION lab path, keyed to the Repair-17
#       controller AND to the routed signal being continued;
#     - the shadow marker token, keyed to Repair 17, to the v10 continuation,
#       to the exact controller sha256 and to the routed signal id;
#     - the completed v9 lab is now named as PRESERVED evidence, so this run
#       refuses to collide with it and witnesses that it did not move. It is
#       preserved evidence AND the read-only continuation seed at the same
#       time, and being the seed authorises NOTHING to be written into it;
#     - the v9 continuation seed's own identity is captured as a named proof
#       artefact in the PRESERVED-LAB proof set, so a seed that moved is
#       reported as a preserved-evidence failure and never as a
#       protected-workspace one;
#     - the observations pass is now REPAIR-17 CONTINUATION V10, replacing the
#       Repair-17 one. It records; it decides nothing and it can fail no
#       verdict.
#   Nothing else. THE FOUR STAGES, THE CONTINUATION GATE, THE PER-STAGE
#   EVIDENCE CAPTURE, EVERY ISOLATION GUARANTEE, EVERY PROVIDER-CALL LIMIT
#   AND EVERY FAIL-CLOSED PATH ARE CARRIED FORWARD BYTE-FOR-BYTE.
#
#   THE ROUTED SIGNAL IS NOT A QUESTION, AND THIS LAUNCHER NEVER MAKES IT ONE.
#   Event 7 is a ROUTED REVIEW SIGNAL. It is not a Ness question, it is not a
#   settled finding, and it is not a verdict. This launcher does NOT classify
#   it, does NOT decide whether it is settled, mechanical, dependent or
#   genuinely open, does NOT convert it into a question and does NOT hard-code
#   any answer to it. Its title and evidence are provenance only and are never
#   read by any executable path here. The FIRST live stage of this run is a
#   FRESH ordinary question-validation over the preserved seven-event state,
#   and the controller's own question-validation is the ONLY thing that may
#   ever decide what that signal really is. This launcher contains no
#   classification, no disposition vocabulary and no interpretation of either.
#
#   THE REAL WORKSPACE STILL GETS v9's FULL PROTECTION, UNWEAKENED.
#   Copying from the seed does not relax anything about the real original. It
#   is still frozen by exact branch, HEAD and complete status; still proved
#   before the copy; still re-asserted under both advisory locks; still proved
#   during the copy; still proved after every stage that runs; and still proved
#   finally from OUTSIDE the Bubblewrap namespace. No continuation event is
#   ever written back to the real interview journal, no candidate produced in
#   the continuation is ever promoted to real N.H, and everything this run
#   creates stays inside the new disposable v10 lab.
#
#   THE THREE EXPLAINED WORKSPACE-ROOT DIRECTORIES GATE IS CARRIED FORWARD
#   UNCHANGED IN MEANING AND IN STRENGTH. .agents, .codex and the
#   workspace-root .git are still frozen in section 4a by exact path and exact
#   safe shape -- present, a real directory, not a symlink, not a special
#   file, EMPTY AT EVERY DEPTH -- and the workspace root must still NOT
#   resolve as a Git repository. Nothing about that gate is loosened. The
#   current disk state was re-read for this rebase rather than inherited from
#   v9: all three are still present, still real directories, still not
#   symlinks, still recursively empty, and the workspace root still does not
#   resolve as a repository. Nothing under them is created, deleted,
#   populated or normalised by this launcher on any path.
#
#   REPAIR 17 STILL NEEDS NO LAUNCHER CHANGE AT ALL, AND STILL GETS NONE.
#   Repair 17 changed exactly one thing in the controller: the
#   QUESTION-VALIDATION PROMPT. That prompt states this controller's own
#   existing classification -> disposition mapping to the model, rendered
#   mechanically from QUESTION_VALIDATION_DISPOSITION_BY_CLASSIFICATION so the
#   vocabulary the model is handed is the SAME one the validator enforces --
#   including
#       genuinely_open_for_ness -> admit_ness_question
#   All of that is inside nh_loop.py. THIS LAUNCHER DOES NOT UNDERSTAND,
#   PARSE, REPAIR, NORMALISE, TRANSLATE OR INTERPRET THAT VOCABULARY. It
#   contains no executable handling of ask_ness, admit_ness_question, a
#   classification, a disposition, a question-validation field error or any
#   prompt content. It runs the same controller stages it ran before and
#   preserves each stage's stdout and stderr verbatim and in full. There is NO
#   new parser, NO classifier, NO retry and NO provider fallback, and no
#   controller result is ever translated or repaired. THE CONTROLLER ALONE
#   OWNS whether question-validation passes or refuses.
#
#   REPAIR 16'S BOUNDED CODEX DIAGNOSTIC IS STILL PRESERVED, BY DOING NOTHING
#   NEW. Where a real Codex official error occurs, the controller's ordinary
#   Stage output carries the safe bounded
#       official error message / message_chars / message_bytes / message_sha256
#   where available. That is ordinary controller stdout and stderr, which this
#   launcher has captured verbatim and in full to <slug>.stdout and
#   <slug>.stderr per stage since v7, so it keeps flowing to the proof with no
#   change of any kind here. Raw Codex JSONL is never exposed by this
#   launcher, exactly as before.
#
#   WHAT THE v9 RUN ACTUALLY RECORDED, STATED ONCE AND ONLY AS PROVENANCE.
#   The completed v9 lab holds:
#       STAGE1_QUESTION_VALIDATION_EXIT = 0
#       STAGE2_COVERAGE_REVIEW_EXIT     = 0
#       STAGE3_INTERVIEW_GATE_EXIT      = NOT-RUN
#       STAGE4_EXECUTE_EXIT             = NOT-RUN
#       coverage_possible_gaps          = 1
#   and its before / during / after-question-validation / after-coverage-review
#   / after witnesses of the protected original are byte-identical to one
#   another, which is what ORIGINAL_WORKSPACE_PROOF=PASS,
#   PRESERVED_LAB_PROOF=PASS and HOST_CREDENTIAL_WITNESS=UNCHANGED mean for
#   that run. NOTHING in this launcher depends on any of it: the seed is
#   authenticated here, from the seed itself, by the controller's own
#   semantics, and the preserved-lab witness is taken at the start of THIS run
#   and compared only against that capture -- so it fails only if something
#   moves DURING this run.
#
#   THE HISTORY BELOW IS v9's, v8's, v7's, v6's, v5's, v4's, v3's AND v2's,
#   retained in full.
#
#   v9 WAS A BOUNDED REBASE OF v8, NOT A REDESIGN.
#
#   It starts from the exact bytes of NH_SHADOW_REHEARSAL_LAUNCHER_v8.sh
#   (sha256 9a26049e..., 180695 bytes, 3451 lines) and changes ONLY what the
#   Repair-17 controller identity and a fresh one-time lab mechanically
#   require. Every isolation guarantee and every proof v1..v8 earned is
#   carried forward unchanged, and the v8..v2 histories below are retained
#   deliberately so none of it can be lost.
#
#   v8 RAN, exactly once. Its lab is preserved at
#   /home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR16_882fe3e5...  and it is
#   preserved evidence in its own right. NOTHING about what that run observed
#   is asserted anywhere in this file. This launcher invents no historical
#   metadata for that lab and requires none: like every other preserved lab it
#   is captured at the start of THIS run and compared only against that
#   capture, so it fails only if something moves DURING this run.
#
#   WHAT v9 CHANGES FROM v8, AND ONLY THIS:
#     - the frozen controller identity, to the Repair-17 controller
#       (sha256 6a3ce02e..., 1749880 bytes, 38331 lines);
#     - v8's own identity is now frozen and gated, as v1..v7 already are;
#     - v9 itself now exists in controller/, so the exact expected controller
#       worktree gains one more entry -- still an EXACT match, never
#       "anything untracked is acceptable";
#     - a fresh disposable lab path keyed to the Repair-17 controller;
#     - the shadow marker token, keyed to the Repair-17 controller;
#     - the Repair-16 lab is now named as PRESERVED evidence, so this run
#       refuses to collide with it and witnesses that it did not move. The
#       preserved-lab hash and metadata sweep already globs every
#       NH_AICP_SHADOW_REHEARSAL_* directory except the new lab, so the
#       Repair-16 lab enters that proof with no change to the sweep;
#     - the observations pass is now REPAIR-17, replacing the Repair-16 one.
#       It records; it decides nothing and it can fail no verdict.
#   Nothing else. THE FOUR STAGES, THE CONTINUATION GATE, THE PER-STAGE
#   EVIDENCE CAPTURE, EVERY ISOLATION GUARANTEE, EVERY PROVIDER-CALL LIMIT
#   AND EVERY FAIL-CLOSED PATH ARE CARRIED FORWARD BYTE-FOR-BYTE.
#
#   THE THREE EXPLAINED WORKSPACE-ROOT DIRECTORIES GATE IS CARRIED FORWARD
#   UNCHANGED IN MEANING AND IN STRENGTH. .agents, .codex and the
#   workspace-root .git are still frozen in section 4a by exact path and exact
#   safe shape -- present, a real directory, not a symlink, not a special
#   file, EMPTY AT EVERY DEPTH -- and the workspace root must still NOT
#   resolve as a Git repository. Nothing about that gate is loosened. The
#   current disk state was re-read for this rebase rather than inherited from
#   v8: all three are still present, still real directories, still not
#   symlinks, still recursively empty, and the workspace root still does not
#   resolve as a repository. Nothing under them is created, deleted,
#   populated or normalised by this launcher on any path.
#
#   REPAIR 17 NEEDS NO LAUNCHER CHANGE AT ALL, AND GETS NONE.
#   Repair 17 changed exactly one thing in the controller: the
#   QUESTION-VALIDATION PROMPT. That prompt now states this controller's own
#   existing classification -> disposition mapping to the model, rendered
#   mechanically from QUESTION_VALIDATION_DISPOSITION_BY_CLASSIFICATION so the
#   vocabulary the model is handed is the SAME one the validator enforces --
#   including
#       genuinely_open_for_ness -> admit_ness_question
#   All of that is inside nh_loop.py. THIS LAUNCHER DOES NOT UNDERSTAND,
#   PARSE, REPAIR, NORMALISE, TRANSLATE OR INTERPRET THAT VOCABULARY. It
#   contains no executable handling of ask_ness, admit_ness_question, a
#   classification, a disposition, a question-validation field error or any
#   prompt content. It runs the same controller stage it ran before and
#   preserves that stage's stdout and stderr verbatim and in full. There is NO
#   new parser, NO classifier, NO retry and NO provider fallback, and no
#   controller result is ever translated or repaired. THE CONTROLLER ALONE
#   OWNS whether question-validation passes or refuses.
#
#   REPAIR 16'S BOUNDED CODEX DIAGNOSTIC IS STILL PRESERVED, BY DOING NOTHING
#   NEW. Where a real Codex official error occurs, the controller's ordinary
#   Stage output carries the safe bounded
#       official error message / message_chars / message_bytes / message_sha256
#   where available. That is ordinary controller stdout and stderr, which this
#   launcher has captured verbatim and in full to <slug>.stdout and
#   <slug>.stderr per stage since v7, so it keeps flowing to the proof with no
#   change of any kind here. Raw Codex JSONL is never exposed by this
#   launcher, exactly as before.
#
#   THE HISTORY BELOW IS v8's, v7's, v6's, v5's, v4's, v3's AND v2's, retained
#   in full.
#
#   v8 WAS A BOUNDED REBASE OF v7, NOT A REDESIGN.
#   It starts from the exact bytes of NH_SHADOW_REHEARSAL_LAUNCHER_v7.sh
#   (sha256 8cce9c73..., 163580 bytes, 3141 lines) and changes ONLY what the
#   Repair-16 controller identity, a fresh one-time lab, and one newly
#   explained workspace-root condition mechanically require. Every isolation
#   guarantee and every proof v1..v7 earned is carried forward unchanged, and
#   the v7..v2 histories below are retained deliberately so none of it can be
#   lost.
#
#   v7 RAN, exactly once. Its lab is preserved at
#   /home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR15_94f0734f...  and it recorded
#   the defect Repair 16 corrects: stage 1 question-validation failed closed
#   with exit 1 on
#       codex reported 1 error event(s) on stdout, the first on line 61:
#       the turn is not clean and its final message is discarded
#   which named the fact of a Codex error event but disclosed nothing bounded
#   about it, so the failure could not be told apart from any other unclean
#   turn without reading raw provider output. Stages 2, 3 and 4 were therefore
#   never reached.
#
#   WHAT v8 CHANGES FROM v7, AND ONLY THIS:
#     - the frozen controller identity, to the Repair-16 controller
#       (sha256 882fe3e5..., 1748707 bytes, 38307 lines);
#     - v7's own identity is now frozen and gated, as v1..v6 already are;
#     - v8 itself now exists in controller/, so the exact expected controller
#       worktree gains one more entry -- still an EXACT match, never
#       "anything untracked is acceptable";
#     - a fresh disposable lab path keyed to the Repair-16 controller;
#     - the shadow marker token, keyed to the Repair-16 controller;
#     - the Repair-15 lab is now named as PRESERVED evidence, so this run
#       refuses to collide with it and witnesses that it did not move. The
#       preserved-lab hash and metadata sweep already globs every
#       NH_AICP_SHADOW_REHEARSAL_* directory except the new lab, so the
#       Repair-15 lab enters that proof with no change to the sweep;
#     - THE THREE EXPLAINED WORKSPACE-ROOT DIRECTORIES ARE NOW FROZEN
#       EXPLICITLY BY SHAPE. See the block immediately below;
#     - the observations pass is now REPAIR-16, replacing the Repair-15 one.
#       It records; it decides nothing and it can fail no verdict.
#   Nothing else. THE FOUR STAGES, THE CONTINUATION GATE, THE PER-STAGE
#   EVIDENCE CAPTURE, EVERY ISOLATION GUARANTEE, EVERY PROVIDER-CALL LIMIT
#   AND EVERY FAIL-CLOSED PATH ARE CARRIED FORWARD BYTE-FOR-BYTE.
#
#   REPAIR 16 NEEDS NO LAUNCHER CHANGE AT ALL, AND GETS NONE.
#   Repair 16 changed exactly one thing in the controller: its Codex error
#   diagnostic. Where a real Codex official error occurs, the controller's
#   ordinary Stage output should now carry the safe bounded
#       official error message / message_chars / message_bytes / message_sha256
#   where available. That output is ordinary controller stdout and stderr, and
#   v7 already captures both, verbatim and in full, to <slug>.stdout and
#   <slug>.stderr per stage. So v8 adds NO error parser, NO classifier, NO
#   retry and NO provider fallback, and it does not scrape or reinterpret the
#   message. It preserves the bytes and nothing more. The controller alone owns
#   the meaning of CODEX_TECHNICAL_FAILURE. Raw Codex JSONL is never exposed by
#   this launcher, exactly as before.
#
#   THE THREE EXPLAINED WORKSPACE-ROOT DIRECTORIES.
#   Between the v7 run and this rebase, three new entries appeared at the
#   protected workspace root:
#       .agents   .codex   .git
#   all three born together at 2026-08-14 01:18:54, all three EMPTY, during
#   the period in which Codex was opened locally for the Repair-16
#   independent audit. Official Codex documentation identifies exactly these
#   names as special workspace paths under a writable root -- .codex as
#   project-local Codex configuration space and .agents as project-local
#   agent/skill space -- so for this bounded job they are classified as
#   explained Codex/tool workspace artefacts.
#
#   THAT CLASSIFICATION IS NARROW, AND IS STATED NARROWLY.
#   It does NOT make their future contents trusted. It does NOT make them N.H
#   authority. It does NOT authorise Codex configuration, skills or Git
#   activity. This launcher never deletes them, never normalises them and
#   never creates anything inside them.
#
#   WHY THEY ARE GATED EXPLICITLY RATHER THAN TOLERATED. They sit at the
#   workspace root, OUTSIDE both Git checkouts, so no `git status` gate in
#   this file can ever see them: they would otherwise enter the proof only
#   through workspace.meta, be frozen as the normal baseline, and be copied
#   into the shadow, with nothing anywhere having asserted what they are. That
#   is precisely the "silently frozen as normal" outcome this launcher family
#   refuses. Section 4a therefore freezes all three by exact path and exact
#   safe shape -- present, a real directory, not a symlink, not a special
#   file, containing exactly zero entries at any depth -- and additionally
#   proves that the root .git is NOT a functional Git repository. Any of them
#   missing, replaced, or non-empty FAILS THE RUN CLOSED, and because the gate
#   lives inside assert_frozen_identities it is asserted twice, the first time
#   long before the isolation self-test and therefore long before any possible
#   provider or model call.
#
#   THE ROOT .git IS NEVER USED AS A REPOSITORY BY THIS LAUNCHER. Every Git
#   read goes through git_ro with an explicit repository argument, and the only
#   two values ever passed are ${CTRL} and ${NHGOV} -- the controller
#   repository and the NH-GOVERNANCE repository, with their own frozen
#   branches, HEADs and statuses. ${WS} is never passed to git_ro as a
#   repository, and section 4a asserts that the workspace root does not resolve
#   as a Git repository at all.
#
#   NOTE ON THE PRESERVED REPAIR-15 LAB. Its content is byte-identical to the
#   moment the Repair-15 rehearsal ended, and v8 requires NO historical
#   metadata of it: like every other preserved lab it is captured before this
#   run and compared only against its own capture afterwards, so whatever it
#   already disclosed as historically changed is irrelevant here. It fails only
#   if something moves DURING this run.
#
#   THE HISTORY BELOW IS v7's, v6's, v5's, v4's, v3's AND v2's, retained in
#   full.
#
#   v7 WAS A BOUNDED REBASE OF v6, NOT A REDESIGN.
#   It starts from the exact bytes of NH_SHADOW_REHEARSAL_LAUNCHER_v6.sh
#   (sha256 e12d6183..., 158865 bytes, 3066 lines) and changes ONLY what the
#   Repair-15 controller identity and a fresh one-time lab mechanically
#   require. Every isolation guarantee and every proof v1..v6 earned is
#   carried forward unchanged, and the v6..v2 histories below are retained
#   deliberately so none of it can be lost.
#
#   v6 RAN, exactly once. Its lab is preserved at
#   /home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR14_76b60e90...  and it recorded
#   the defect Repair 15 corrects: stage 1 question-validation wrote a
#   complete, enumeration-complete, zero-unknown authenticated validation,
#   and stage 2 question-coverage-review then refused it as NOT CURRENT
#   before invoking any model, because replay's source re-proof could not
#   ask the authenticated package-identity question and the ordinary one is
#   unanswerable while the package's own custodied v1.0/v1.1/v1.2 chain sits
#   in the worktree. Stages 3 and 4 were therefore never reached.
#
#   WHAT v7 CHANGES FROM v6, AND ONLY THIS:
#     - the frozen controller identity, to the Repair-15 controller
#       (sha256 94f0734f..., 1741855 bytes, 38180 lines);
#     - v6's own identity is now frozen and gated, as v1..v5 already are;
#     - v7 itself now exists in controller/, so the exact expected controller
#       worktree gains one more entry -- still an EXACT match, never
#       "anything untracked is acceptable";
#     - a fresh disposable lab path keyed to the Repair-15 controller;
#     - the shadow marker token, keyed to the Repair-15 controller;
#     - the Repair-14 lab is now named as PRESERVED evidence, so this run
#       refuses to collide with it and witnesses that it did not move. The
#       preserved-lab hash and metadata sweep already globs every
#       NH_AICP_SHADOW_REHEARSAL_* directory except the new lab, so the
#       Repair-14 lab enters that proof with no change to the sweep;
#     - the observations pass is now REPAIR-15, replacing the Repair-14 one.
#       It records; it decides nothing and it can fail no verdict.
#   Nothing else. THE FOUR STAGES, THE CONTINUATION GATE, THE PER-STAGE
#   EVIDENCE CAPTURE, EVERY ISOLATION GUARANTEE, EVERY PROVIDER-CALL LIMIT
#   AND EVERY FAIL-CLOSED PATH ARE CARRIED FORWARD BYTE-FOR-BYTE.
#
#   NOTE ON THE PRESERVED REPAIR-14 LAB. Its content is byte-identical to
#   the moment the Repair-14 rehearsal ended. One metadata caveat is on the
#   record and is stated here so no later reader is surprised: during the
#   Repair-15 audit a `git status` was run inside that lab, which rewrote
#   shadow/.../NH-GOVERNANCE/.git/index (a stat cache), and the original
#   bytes were then restored from the real worktree. The file's CONTENT is
#   the original content; its ctime records both writes. This launcher
#   captures that lab's hashes and metadata before AND after its own run and
#   compares the two, so the caveat is invisible to this proof: it fails only
#   if something moves DURING this run.
#
#   THE HISTORY BELOW IS v6's, v5's, v4's, v3's AND v2's, retained in full.
#
#   v6 WAS A BOUNDED REBASE OF v5, NOT A REDESIGN.
#   It starts from the exact bytes of NH_SHADOW_REHEARSAL_LAUNCHER_v5.sh
#   (sha256 2648825e..., 140784 bytes, 2685 lines) and changes ONLY what the
#   Repair-14 controller and the corrected stage sequence mechanically require.
#   Every isolation guarantee and every proof v1..v5 earned is carried forward
#   unchanged; the v5, v4, v3 and v2 histories below are retained deliberately
#   so none of it can be lost.
#
#   v5 WAS NEVER RUN. Its lab path was never created, and the Repair-11
#   controller it was frozen to no longer exists on disk -- Repairs 12, 13 and
#   14 replaced it. v5 is preserved unedited as validation evidence, exactly as
#   v1..v4 are, and this launcher gates on ALL FIVE still being byte-identical.
#
#   WHAT v6 CHANGES FROM v5, AND ONLY THIS:
#     - the frozen controller identity, to the Repair-14 controller
#       (sha256 76b60e90..., 1729587 bytes, 37948 lines);
#     - v5's own identity is now frozen and gated, as v1..v4 already are;
#     - v6 itself now exists in controller/, so the exact expected controller
#       worktree gains one more entry -- still an EXACT match, never "anything
#       untracked is acceptable";
#     - a fresh disposable lab path keyed to the Repair-14 controller;
#     - the shadow marker token, keyed to the Repair-14 controller;
#     - THE REAL TEST SEQUENCE IS NOW FOUR STAGES and begins with
#       question-validation. v5's three-stage sequence is obsolete: under
#       Repairs 12/13/14 the recorded validation of the current package is
#       preserved history and NOT current authority, so question-coverage-review
#       refuses before it invokes any model until a fresh validation exists. A
#       rehearsal that starts at the coverage review therefore cannot reach the
#       stage it exists to exercise;
#     - EVERY STAGE NOW CAPTURES its exact command line, stdout, stderr, exit
#       code, start and finish timestamps, and its own protected-source proof;
#     - CONTINUATION IS GATED ON THE CONTROLLER'S OWN REPORTED FACTS, not on an
#       exit code alone. An incomplete validation, a material unknown, an open
#       question for Ness, a coverage gap, a closed interview gate, a changed
#       protected source or any non-zero exit stops the sequence there;
#     - the observations pass is now REPAIR-14, replacing the Repair-11 one. It
#       records; it decides nothing and it can fail no verdict.
#   Nothing else. No isolation change, no proof weakened, no new machinery
#   beyond the per-stage evidence capture and the continuation gate.
#
#   THE HISTORY BELOW IS v5's, v4's, v3's AND v2's, retained in full.
#
#   v5 WAS A BOUNDED REBASE OF v4, NOT A REDESIGN.
#   It starts from the exact bytes of NH_SHADOW_REHEARSAL_LAUNCHER_v4.sh
#   (sha256 fdc62fdd..., 112576 bytes, 2203 lines) and changes ONLY what the
#   Repair-11 controller mechanically requires. Every isolation guarantee and
#   every proof v1/v2/v3/v4 earned is carried forward unchanged; the v4, v3 and
#   v2 histories below are retained deliberately so none of it can be lost.
#
#   v1, v2, v3 and v4 are all preserved on disk. None is edited, renamed or
#   deleted, and this launcher gates on ALL FOUR still being byte-identical.
#
#   WHAT v5 CHANGES FROM v4, AND ONLY THIS:
#     - the frozen controller identity, to the Repair-11 controller;
#     - v4's own identity is now frozen and gated, as v1's, v2's and v3's
#       already are;
#     - v5 itself now exists in controller/, so the exact expected controller
#       worktree gains one more entry -- still an EXACT match, never "anything
#       untracked is acceptable";
#     - the controller worktree no longer contains __pycache__/. v4 froze
#       `!! __pycache__/nh_loop.cpython-314.pyc` and that path does not exist on
#       disk now, so v5 freezes the real current set instead of inheriting v4's.
#       This is exactly the fail-closed behaviour v4's own comment describes:
#       the identity is re-frozen deliberately, never relaxed;
#     - the N.H worktree gained the two adopted-Decision-Defaults entries, and
#       both are accounted for EXPLICITLY rather than tolerated:
#           01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_3.md
#           05_ACTIVE_CANDIDATE/NH_DECISION_DEFAULTS-S19_v2_3_CANDIDATE.md
#       alongside the preserved Authority Integrity candidate chain v1.0 / v1.1
#       / v1.2, which is unchanged. Every one of the five entries is frozen by
#       sha256 and byte count, and any sixth entry of any kind fails the run;
#     - a new proof artefact, authority.sha256, freezing the adopted
#       authoritative Decision Defaults file in 01_AUTHORITATIVE/ alongside the
#       candidates. It is part of the protected proof set and is compared
#       before / during / after like every other member of it;
#     - a fresh disposable lab path keyed to the Repair-11 controller;
#     - the shadow marker token, keyed to the Repair-11 controller;
#     - the Repair-10 lab is named as preserved evidence alongside the Repair-9
#       and v1 labs;
#     - THE REAL TEST SEQUENCE IS NOW THREE STAGES, described in full below;
#     - the observations pass is now REPAIR-11, replacing the Repair-10-only
#       one. It records; it decides nothing and it can fail no verdict.
#   Nothing else. No isolation change, no proof weakened, no new machinery.
#
#   1. FROZEN CONTROLLER IDENTITY IS THE REPAIR-11 ONE.
#      nh_loop.py is now
#        sha256 9eace9acc4a551b0ccb325172818040bcb38cd15e22da822c863053f34aa9859
#        bytes  1684347
#        lines  36980
#      Repair 11 moves the DESIGN AUTHORSHIP to GPT: the preparation stage
#      returns a validated mechanical_design_specification, Claude APPLIES it
#      rather than deriving a design of its own, Claude may declare a mandatory
#      specification STOP which the controller itself proves real from its own
#      disposable-workspace evidence, and each correction round runs ONE fresh
#      GPT correction-specification review before Claude is asked to correct
#      anything. Repair 11 also inserts a FRESH INDEPENDENT question-coverage
#      review between "question-validation says its inventory is complete" and
#      "the mechanical path may unlock". None of that is simulated here -- the
#      real controller decides what happens.
#
#   2. WHY v4's SINGLE COMMAND IS NO LONGER SUFFICIENT.
#      v4 ran only execute-next-claude-task. Under Repair 11 the mechanical path
#      cannot unlock until a fresh, independent coverage review has challenged
#      the completed question inventory, so a rehearsal that runs only
#      execute-next-claude-task exercises the new gate exclusively from its
#      closed side and never runs the review that is the repair's centrepiece.
#      v5 therefore runs the coverage review first, observes the gate, and only
#      then runs the one execute. See THE REPAIR-11 SEQUENCE below.
#
#   3. THE CLAUDE SESSION STORE STILL SURVIVES THE EXECUTE NAMESPACE.
#      Repair 10's requirement is unchanged and is preserved exactly: several
#      Claude invocations inside the ONE execute-next-claude-task execution must
#      reach the SAME Claude Code session. CLAUDE_CONFIG_DIR points at the
#      anonymous copy-on-write overlay on ${HOME_REAL}/.claude, and stage 3 is
#      ONE bwrap namespace holding ONE controller process, so the overlay's
#      tmpfs upper layer lives for the whole of that execution. Session
#      transcripts written by the first Claude invocation are visible to a later
#      --resume, and every one of them is discarded with the namespace.
#
#      The three stages are three separate namespaces, and that is deliberate
#      and safe. Session continuity is required WITHIN one execute, never across
#      commands: stages 1 and 2 invoke Claude at all. What must persist between
#      stages is the shadow's own interview state -- the journal event a clear
#      coverage review appends, or the routing signals a gap-bearing one records
#      -- and that lives in ${SHADOW_WS}, a real directory in the lab that is
#      bind-mounted into every stage, so it persists by construction. Only the
#      anonymous credential overlays and /run are re-created per stage, and
#      neither carries controller state.
#
#   4. A RESUMED CLAUDE CALL IS NOT REQUIRED FOR SUCCESS, AND NEITHER IS A
#      CLAUDE CALL AT ALL.
#      If the coverage review finds a possible gap, the mechanical path stays
#      closed, execute-next-claude-task fails closed at its real gate, and ZERO
#      Claude invocations occur. That is a legitimate, correct outcome and this
#      launcher does NOT fail on it. Equally, if the candidate reaches PASS on
#      its first audit there is no second correction round and so nothing to
#      resume. The observations pass records which of these happened; it never
#      forces any of them.
#
# ==========================================================================
# THE REPAIR-11 SEQUENCE, EXACTLY
# ==========================================================================
#
#   STAGE 1.  python3 nh_loop.py question-coverage-review
#             ONE real, fresh GPT/Codex review. Read-only, ephemeral, resuming
#             no audit or design history. stdout, stderr and exit code are
#             captured to three separate files.
#
#             IF IT EXITS NON-ZERO: stages 2 and 3 are NOT run. The evidence is
#             preserved and control passes straight to the outside after-proof.
#
#   STAGE 2.  python3 nh_loop.py interview-gate
#             Read-only. Makes no provider call. stdout, stderr and exit code
#             are captured separately.
#
#             This stage is OBSERVATIONAL. It records whether the mechanical
#             path is currently unlocked after the fresh coverage review. A
#             CLOSED gate is not a failure of this stage and is not a failure of
#             this launcher.
#
#             IF IT HAS A TECHNICAL, NON-ZERO FAILURE: stage 3 is NOT run.
#
#   STAGE 3.  python3 nh_loop.py execute-next-claude-task
#             Run EXACTLY ONCE. There is no retry around it and no retry around
#             any other stage.
#
#   NOTHING IS FAKED, INJECTED OR PRE-ANSWERED.
#   No controller result is supplied, steered or manufactured by this launcher
#   at any stage. --clearenv wipes the environment and the only NH_-prefixed
#   variable set back for a real stage is NH_LOOP_INTERVIEW_STATE_DIR, pointing
#   at the shadow's own interview state. The isolation self-test asserts that
#   the complete set of NH_* variables inside the namespace is exactly what this
#   launcher set, so nothing can pre-answer a contract from outside.
#
#   A COVERAGE GAP IS NOT A LAUNCHER FAILURE, AND IT EXITS ZERO.
#   Read this carefully, because it is the one place where the exit code and the
#   English meaning genuinely come apart. In the Repair-11 controller a coverage
#   review that finds possible gaps records each one as a ROUTING SIGNAL and
#   returns interview_stop_reason coverage_gaps_routed with ok=true -- that is,
#   EXIT 0. The review did its job; it found something. So stage 1 exiting zero
#   does NOT mean "coverage is clear", and this launcher must never read it that
#   way. Stage 1 continues to stages 2 and 3 on a zero exit, and if the gap
#   left the mechanical path closed then execute-next-claude-task fails closed
#   at its own real gate. THAT IS VALID EVIDENCE, not a fault, and the
#   observations record it as such.
#   A TECHNICAL failure of the review -- a preflight failure, an unmet
#   precondition, a Codex transport failure, source that moved under the review,
#   a reply that failed validation, an unproved source manifest -- returns
#   ok=false and EXIT 1, and THAT is what stops the sequence.
#   Whether coverage was CLEAR is read from coverage_review_cleared and
#   coverage_possible_gaps in the controller's own report, never from an exit
#   code.
#
#   THE LAUNCHER ADDS NO RETRY AND MANUFACTURES NO CLEARANCE.
#   It never re-runs a stage, never edits the shadow's interview state, never
#   writes a coverage clearance, and never sets a controller-behaviour variable.
#   The only thing it does between stages is read an exit code and decide
#   whether to run the next one.
#
#   THE CONTROLLER'S LIFETIME CORRECTION LIMIT REMAINS EXACTLY 5.
#   It is owned by nh_loop.py (MAX_AUTOMATIC_CORRECTION_ROUNDS) and this
#   launcher neither sets it, reads it as configuration, nor influences it. The
#   observations pass reports the value the controller states for itself.
#
#   THE HISTORY BELOW IS v4's, v3's AND v2's, retained in full.
#
#   v4 WAS A REBASE OF v3, NOT A REDESIGN.
#   It started from the exact bytes of NH_SHADOW_REHEARSAL_LAUNCHER_v3.sh
#   (sha256 499b0a60..., 102494 bytes, 2026 lines) and changed ONLY what the
#   Repair-10 controller mechanically required.
#
#   WHAT v4 CHANGED FROM v3, AND ONLY THAT:
#     - the frozen controller identity, to the Repair-10 controller
#       (sha256 704ad177..., 1447775 bytes, 31873 lines);
#     - v3's own identity became frozen and gated, as v1's and v2's already were;
#     - v4 itself existed in controller/, so the expected controller worktree
#       gained one more entry;
#     - a fresh disposable lab path keyed to the Repair-10 controller;
#     - the shadow marker token, keyed to the Repair-10 controller;
#     - the Repair-9 lab named as preserved evidence alongside the v1 lab;
#     - a post-run, read-only OBSERVATIONS pass over the lab's own captured
#       output. It recorded; it decided nothing.
#   Repair 10 gave ONE Claude session per package execution, resumed that exact
#   session on later correction rounds, pinned claude-opus-5, granted Edit, and
#   seeded the next-version candidate. All of that is still true under Repair 11
#   and is still not simulated here.
#
#   v3 WAS A REBASE, NOT A REDESIGN.
#   It started from the exact bytes of NH_SHADOW_REHEARSAL_LAUNCHER_v2.sh
#   (sha256 bb97ac49..., 99298 bytes, 1978 lines) and changed ONLY what the
#   closed Repair 9 controller mechanically required. Every hardening v2
#   earned -- and it earned a lot, across several review rounds -- is carried
#   forward unchanged and is listed in the v2 history below, which is retained
#   deliberately so none of it can be quietly lost in a later rebase.
#
#   WHAT v3 CHANGED FROM v2, AND ONLY THAT:
#     - the frozen controller identity, to the closed Repair 9 controller
#       (sha256 acc8dee2..., 1382464 bytes, 30473 lines);
#     - v2's own identity became frozen and gated, as v1's already was;
#     - v3 itself existed in controller/, so the expected controller worktree
#       gained one more entry;
#     - a fresh disposable lab path keyed to the Repair 9 controller;
#     - the shadow marker token, keyed to the Repair 9 controller;
#     - every protected-state identity re-read from disk rather than inherited.
#   Repair 9 made the ordinary package audit CURRENT_PACKAGE_ONLY and deferred
#   whole-system wiring to the final Bundle 8 stage.
#
#   THE HISTORY BELOW IS v2's. It records defects already found and fixed, and
#   is kept so a future rebase cannot reintroduce them.
#
#   2. EVERY OTHER FROZEN VALUE WAS RE-READ FROM DISK, NOT INHERITED.
#      Controller and N.H Git state, the candidates, the interview journal,
#      journal head, authenticity-key identity and the authenticated package
#      scope were all re-derived from the live workspace when this file was
#      written. This is re-verified in v5 too, and it is not an assumption
#      carried over: two of v4's frozen values -- the controller ignored-file
#      set and the N.H untracked set -- had genuinely MOVED, and v5 freezes what
#      is actually on disk rather than what v4 recorded.
#
#   3. THE CONTROLLER-WORKTREE PROOF IS STRICTER, NOT WEAKER.
#      v1 filtered its own basename out of `git status` with a grep and then
#      compared the remainder. That form also passes when a launcher is MISSING,
#      because it only subtracts. v2 instead asserts the COMPLETE porcelain
#      status is EXACTLY the expected lines. Nothing is filtered, no untracked
#      path is ignored, an absent launcher fails, and any extra entry of any
#      kind fails. v5 keeps that discipline over seven controller entries and
#      five N.H entries.
#
#   4. A NEW DISPOSABLE LAB PATH, AND EVERY EARLIER REHEARSAL IS PRESERVED.
#      The v1 lab
#        /home/ness/NH_AICP_SHADOW_REHEARSAL_ce3a38f43f287a56bd635ed836edf002a2db50a7
#      is preserved evidence, as are the Repair-9 and Repair-10 labs. None is
#      ever reused and none is ever deleted by this launcher, and all are
#      read-only to it in the exact sense set out under READ-ONLY, STATED
#      EXACTLY above -- no create, write, truncate, rename, chmod, chown or
#      delete, with an atime refresh the one effect a read can have. They are
#      additionally carried in the before / during / after proof set as a
#      hash-and-metadata witness, so any change to their content or to any
#      captured metadata field fails the run closed.
#
#   5. THE ISOLATION MODEL IS v1'S, UNCHANGED.
#      Canonical path substitution, host /home/ness hidden behind tmpfs, model
#      configuration exposed only through anonymous copy-on-write overlays and
#      a file-descriptor materialised .claude.json, no persistent credential
#      copy in the lab, network only because provider calls require it,
#      self-test before any model work, fail closed if isolation is not proved,
#      after-proof performed outside the namespace, protected-original mismatch
#      overriding any apparent shadow success, a separate credential witness,
#      and no Git or GitHub write anywhere.
#
#   6. THE NEW CONTRACTS ARE TESTED NATURALLY.
#      Repair 8 made not_ready_reason a required, bounded field of the Codex
#      preparation result; Repair 11 makes mechanical_design_specification a
#      required, validated object when task_ready is true. This launcher does
#      NOT fake, inject, pre-answer or steer either one. If a real Codex reply
#      does not carry the required field correctly, the controller fails closed
#      on its own and the evidence is preserved in the lab. That outcome is a
#      legitimate result of this rehearsal, not a launcher fault.
#
#   7. THE SAFETY VERDICTS HAVE RESERVED EXIT CODES.
#      v1 exited 2 for a protected-original failure and 3 for a changed
#      credential witness, both of which a controller run can also return on
#      its own, so an automated reader could not tell a containment failure
#      from an ordinary controller exit. v2 reserved 90 through 93 -- values the
#      controller never returns -- for its four safety verdicts, and otherwise
#      returns the controller's exit code verbatim. That is still true here:
#      nh_loop.py defines exactly three exit codes, EXIT_OK 0, EXIT_FAILED_CHECK
#      1 and EXIT_USAGE 2, so 90-93 remain unambiguous. The override itself is
#      unchanged: a protected-original mismatch still outranks any apparent
#      shadow success. Each verdict is computed from its own proof set and
#      reported under its own name, so no one verdict can stand in for another.
#      Because v5 runs three stages, EACH stage's exit code is also written to
#      its own file, so no reader ever has to infer a stage's result from this
#      launcher's single process exit status.
#
#   8. CORRECTIONS FROM THE INDEPENDENT REVIEW OF v2.
#      An independent read-only reviewer found real mechanical defects in the
#      first draft of v2. Each was verified against this host before it was
#      fixed, and each fix is local to the defect:
#        - the lab leaf was created with `mkdir -p` after a separate [ -e ]
#          test. That is not atomic, and `mkdir -p` ACCEPTS a pre-existing
#          symlink -- confirmed on this host -- which would have redirected
#          every proof write and the `rsync --delete` to wherever it pointed.
#          The leaf is now created with a single non-`-p` mkdir and is proved
#          to be a real directory. (section 5)
#        - nothing closed or checked inherited file descriptors. bwrap does not
#          close what it was not asked about, and an inherited descriptor still
#          resolves through /proc/self/fd despite the tmpfs. The self-test now
#          refuses any descriptor beyond stdin/stdout/stderr, before any model
#          call. (section 10)
#        - the worktree gate used --untracked-files=all, which silently omits
#          every gitignored path, so it could not see .claude/ or __pycache__/
#          and would not have seen anything dropped into the ignored state/,
#          runs/, logs/ or cache/ paths either. It now uses --ignored=traditional
#          and freezes the complete set. (section 4)
#        - the shadow copy excluded two directories that exist with real
#          content while the launcher reported a byte-truthful copy, and the
#          verification applied the same exclusions, so it could only ever
#          prove equality modulo them. Neither path is referenced in
#          nh_loop.py; both are now copied and the claim is literally true.
#          (section 7)
#        - the copy verification ended in `|| true`, so a killed or failing
#          rsync was indistinguishable from a clean one and an unverified copy
#          would have been accepted. The exit status is now required to be
#          zero as well as the output empty. (section 7)
#        - the frozen gate ran once, before the locks were taken, so a change
#          made between the gate and the before-proof would have become the
#          accepted baseline, been copied, and passed every later comparison.
#          The whole gate is now re-asserted under lock immediately before the
#          copy. (section 7)
#        - the metadata proofs captured mtime but not ctime or inode, so a
#          pure-metadata change to a protected file could leave every captured
#          field and every content hash identical. ctime and inode are now
#          captured everywhere. (section 2)
#        - the lab credential check ran only BEFORE the run, while everything
#          the run can write is lab-backed and the credential overlays are
#          readable inside the namespace. It now also runs AFTER, as its own
#          reported verdict, and additionally looks for credential-shaped
#          content rather than filenames alone. (sections 2, 10, 12)
#
#   9. CORRECTIONS FROM THE SECOND INDEPENDENT REVIEW ROUND.
#      A fresh review of the corrected file found six more real defects, four of
#      them introduced by the round-one fixes themselves. Each was again
#      verified on this host before being fixed:
#        - the descriptor check exempted any descriptor whose target looked like
#          /proc/<pid>/fd, which would have accepted an inherited handle on
#          another process's descriptor table and let /proc/self/fd/<N>/<M>
#          traverse through it. Measured: no LIVE descriptor ever has such a
#          target -- the enumeration artefacts always read back empty -- so the
#          exemption was pure hole and is gone. (section 10)
#        - --ignored=matching COLLAPSES an ignored directory. Measured: a probe
#          file dropped into __pycache__/ leaves `!! __pycache__/` byte-
#          identical, so arbitrary ignored children would have passed the gate.
#          Both gates and both captures now use --ignored=traditional and freeze
#          the exact ignored FILE list. (sections 2, 4)
#        - the credential content scan used -I, which makes grep treat any file
#          containing a NUL byte as non-matching. Measured: a credential in a
#          file with NUL bytes was MISSED under -I and is CAUGHT under -a. A JWT
#          shape was added too, because a bare opaque token with no surrounding
#          field name matched nothing. (section 2)
#        - the credential scan suppressed its own errors, so an unreadable file
#          or a killed grep produced an empty report and read as CLEAN.
#          Measured: an unreadable lab file now returns SCAN-FAILED instead of
#          CLEAN. The scan distinguishes 0 clean / 1 found / 2 could-not-scan,
#          and only 0 passes. (sections 2, 10, 12)
#        - the preserved-lab and workspace hash captures used the naive
#          find | sort | xargs form, which reports only the LAST stage's status.
#          Measured: a failing find in that pipeline gives PIPESTATUS "1 0 0"
#          while the pipeline reports success -- so a capture that silently
#          missed a subtree the same way before and after would have compared
#          EQUAL and been reported as proof. All tree hashing now goes through
#          hash_tree_into, which checks every stage. (section 2)
#        - the host credential witness discarded its capture errors, so a
#          witness that could not be taken was indistinguishable from one that
#          came back unchanged. It now has its own CAPTURE-FAILED verdict, and
#          only UNCHANGED passes. (sections 2, 12)
#
#  10. CORRECTIONS AFTER A THIRD REVIEW PASS: THE CREDENTIAL VERDICTS THEMSELVES
#      COULD STILL LIE. Both were reproduced on this host before being fixed.
#
#      FALSE "UNCHANGED". The round-two fix routed find and xargs errors to
#      credentials.errors, but the per-file hashes still went through the naive
#      `sha256sum | awk` form. Inside a command substitution that yields an
#      EMPTY string on failure with exit status zero, so an unreadable
#      credential file recorded a BLANK hash and wrote nothing to
#      credentials.errors. Reproduced: with the file unreadable for both
#      captures, the two listings were byte-identical, compared EQUAL, and the
#      witness read UNCHANGED while nothing had actually been witnessed.
#      Now: sha_of and bytes_of emit distinct sentinels instead of empty, and
#      the credential loop checks each hash explicitly and records every failure
#      to credentials.errors, so the same scenario now yields CAPTURE-FAILED.
#      The during-capture is consulted too, not only before and after.
#
#      FALSE "CLEAN". The lab scan is shape-based, and a shape scan cannot
#      establish absence. Reproduced, two credentials it does not see: an opaque
#      token in a shape no marker covers, and a real access_token inside a
#      gzipped blob. No marker set fixes the second case. The verdict is
#      therefore no longer called CLEAN. It is NO-KNOWN-MARKERS, the summary
#      states plainly that this is not proof of absence, and the block report
#      repeats it, so nobody can read that line as the lab being safe.
#
#      Both remain fail-closed: anything other than NO-KNOWN-MARKERS exits 93,
#      and anything other than UNCHANGED exits 91.
#
#  11. THE CREDENTIAL PIPELINE EXITED BEFORE ITS OWN CAPTURE-FAILED HANDLING.
#      Removing `|| true` from the .ssh / .config hashing pipeline in item 10
#      made it fail-closed in the worst possible way. With `set -e` and pipefail
#      both in force, one unreadable file under those directories made the
#      pipeline non-zero and the shell exited THERE -- before the PIPESTATUS
#      check, before anything was written to credentials.errors, and before
#      section 12 ever evaluated CREDENTIAL_WITNESS. Reproduced on this host:
#      the run aborted and no verdict of any kind was assigned, so the one
#      scenario CAPTURE-FAILED exists to report was the one scenario that
#      guaranteed it could never be reported.
#      Fixed by suspending errexit around that pipeline with the same
#      set +e / set -e idiom this file already uses for the self-test and the
#      real runs, capturing PIPESTATUS, then recording the failure.
#
#      The preserved-lab metadata capture was rebuilt the same way, through a
#      raw file instead of `{ ... } | sort`. A pipeline puts the group in a
#      SUBSHELL, so a die() inside it exits only the subshell; it happens to
#      propagate today because pipefail is set, but a fail-closed guarantee must
#      not depend on a shell option set 1500 lines earlier.
#
#  12. THE FILE STILL MADE FALSE "NEVER MODIFIED" GUARANTEES.
#      A first attempt at the atime problem added an accurate explanation but
#      left the absolute claims standing next to it -- the header still said the
#      launcher "never writes to the protected original", note 4 still said the
#      preserved lab is "never modified", and the runtime report still printed
#      "Nothing was written to the protected original" and "never reused,
#      modified or deleted". An accurate footnote does not repair an inaccurate
#      guarantee, least of all in the lines an operator actually reads.
#      Every one of those claims was replaced by the exact operation-level
#      statement in READ-ONLY, STATED EXACTLY at the top of this file, and the
#      two runtime report strings now say precisely what is and is not issued
#      against those paths.
#
#  13. THE REPLACEMENT GUARANTEE WAS ITSELF STILL INACCURATE.
#      The first READ-ONLY, STATED EXACTLY block fixed the absolute claims but
#      introduced a new false one: it asserted the protected paths are opened
#      "only through find, sha256sum, stat, diff, git rev-parse / status and the
#      rsync SOURCE side". That closed enumeration is wrong three ways. It omits
#      `wc -l < nh_loop.py` and the `grep -c` counts over the journal; it omits
#      the shell's own `exec 200<` / `exec 201<` opens; and most seriously it
#      omits flock(2), which is not a read at all. It also listed diff, which is
#      only ever run against proof files inside the lab. And it made a blanket
#      statement with no carve-out for the sandboxed run, contradicting this
#      file's own discipline that containment is UNVERIFIED until the after-proof
#      completes.
#      The block now states the property rather than a list of binaries, names
#      all three operations that are not plain content reads, and scopes itself
#      explicitly to this launcher's own code outside the namespace.
#
#  14. THE CORRECTED GUARANTEE CONTRADICTED THE LAUNCHER'S OWN RUNTIME REPORT.
#      Fixing the header left report_state still printing, of the protected
#      original, "it opens it only for reading" -- the very sentence item 13
#      had just deleted from the header for being false, and now the line an
#      operator actually sees at the moment a run blocks. The two also listed
#      different operation sets, so the file contradicted itself about its own
#      central safety claim.
#      report_state now states the same operation set as the header, and says
#      what actually happened to the two advisory locks, gated on
#      LOCKS_TAKEN / LOCKS_HELD counters in the same style as LAB_CREATED and
#      RUN_STARTED -- because most failure paths never reach section 6, and a
#      design-level sentence about locks would be false on every one of them.
#
#  15. PARTIAL LOCK ACQUISITION WAS REPORTED AS "NO LOCK WAS TAKEN".
#      The flags from item 14 were set once, after BOTH locks were acquired.
#      Acquisition is not atomic across the two: the candidate-transaction lock
#      can be taken and the interview-journal lock then refused by a concurrent
#      holder, which dies immediately -- with the first lock still held and both
#      flags still 0, so the report stated "No lock was taken on the protected
#      original" while this process held one. Reproduced against a real
#      concurrent holder.
#      They are now COUNTS, incremented the instant each lock is acquired and
#      decremented as each descriptor closes.
#
#  16. THE CREDENTIAL METADATA CAPTURE HAD THE FAULT ALREADY FIXED NEXT DOOR.
#      Item 11 rebuilt the credential HASH pipeline but left the credential
#      METADATA pipeline as `{ ... find ... || true ... } | sort`, carrying both
#      of the same defects. `|| true` erased every non-zero find status, and a
#      failing sort in that pipeline was still exposed to set -e + pipefail and
#      could kill the launcher before the CAPTURE-FAILED verdict existed.
#      Rebuilt through a raw file with every status checked and recorded. No
#      group-pipeline remains anywhere in capture_original_proof, so pipefail
#      cannot reach any capture.
#
# THE LAB CONTAINS A COPY OF THE N.H INTERVIEW AUTHENTICITY KEY.
#   The controller cannot append authenticated journal events without it, and
#   the Repair-11 coverage review appends exactly such an event when it clears,
#   so the shadow copy of nh_interview_state/ necessarily includes the key. The
#   lab is created mode 0700. Delete the lab when the rehearsal has been
#   reviewed. No MODEL login material is ever copied into the lab.
#
# USAGE
#   bash /home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/controller/NH_SHADOW_REHEARSAL_LAUNCHER_v10.sh
#
#   Run it manually, from an ordinary terminal, as the user "ness".
#   It takes no arguments. It refuses to run as root.
#
#   PRECONDITION: no other Claude Code / Codex session should be running on this
#   host while it runs, or the host credential witness will report CHANGED
#   because that other session is rewriting ~/.claude.json under you.
#
set -Eeuo pipefail
umask 077

# ==========================================================================
# SECTION 0 — FROZEN IDENTITIES. FAIL CLOSED AGAINST ALL OF THEM.
# ==========================================================================

readonly HOME_REAL="/home/ness"
readonly WS="/home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP"
readonly CTRL="${WS}/controller"
readonly NHGOV="${WS}/NH-GOVERNANCE"
readonly STATE="${WS}/nh_interview_state"
readonly CAND_DIR="${NHGOV}/05_ACTIVE_CANDIDATE"
readonly AUTH_DIR="${NHGOV}/01_AUTHORITATIVE"

# Ten launcher files now live in controller/. All ten are accounted for
# explicitly: nine by exact identity, and this one by presence.
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

# v1..v8 are ALL preserved unchanged, and all eight are frozen here so this
# launcher fails closed if any of them moved. Each is historical validation
# evidence in its own right: each was hardened and closed against the controller
# identity current at the time, and each is superseded only in the sense that
# the controller it was frozen to no longer exists.
#
# v5 is a special case worth stating plainly: it was written, reviewed and never
# run. Its lab was never created. It is evidence of what was frozen against the
# Repair-11 controller, and nothing about it is retracted by v6 existing.
#
# v6 is the opposite case and equally preserved: it RAN, exactly once, and its
# lab is the Repair-14 evidence. Its stage-2 refusal is the defect Repair 15
# corrects. Nothing about v6 is retracted by v7 existing.
#
# v7 is the same case as v6: it RAN, exactly once, and its lab is the Repair-15
# evidence named above. Its stage-1 Codex-error diagnostic is the defect
# Repair 16 corrects. Nothing about v7 is retracted by v8 existing.
#
# v8 is the same case as v7 and v6: it RAN, exactly once, and its lab is the
# Repair-16 evidence named below. NOTHING about what that run observed is
# asserted here -- this launcher invents no historical metadata for it and
# needs none. Nothing about v8 is retracted by v9 existing.
#
# v9 is this file's DIRECT PREDECESSOR and is preserved evidence in its own
# right. It RAN, exactly once, against the Repair-17 controller, and its lab is
# BOTH the Repair-17 evidence AND the read-only continuation seed this launcher
# copies from. Being the seed authorises nothing to be written into it: it is
# gated by identity exactly like v1..v8, its lab is witnessed before, during and
# after this run like every other preserved lab, and no code path anywhere in
# this file opens any path under it for writing.
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

# --- controller: THE REPAIR-17 IDENTITY ---
readonly EXP_LOOP_SHA="6a3ce02e4a0448d5a7206f6eb4260bbcb87989da9f0a541feafea7dd4be0dc19"
readonly EXP_LOOP_BYTES="1749880"
readonly EXP_LOOP_LINES="38331"
readonly EXP_CTRL_BRANCH="main"
readonly EXP_CTRL_HEAD="db46a51967b1af1aa873bc0c0e847a0a95221bdf"

# --- N.H ---
readonly EXP_NH_BRANCH="nh-design-loop"
readonly EXP_NH_HEAD="ce3a38f43f287a56bd635ed836edf002a2db50a7"

# The preserved Authority Integrity candidate chain, unchanged since v4.
readonly CAND_V10="NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_0_CANDIDATE.md"
readonly CAND_V11="NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_1_CANDIDATE.md"
readonly CAND_V12="NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_2_CANDIDATE.md"

# NEW SINCE v4, AND ACCOUNTED FOR EXPLICITLY RATHER THAN TOLERATED.
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

# --- interview state (identities only; the key's CONTENTS are never read) ---
readonly EXP_JOURNAL_SHA="39c6af157222df10203d426e06ab323bb222041aa7b0838f1130f0518aef9945"
readonly EXP_JOURNAL_BYTES="15604"
readonly EXP_JOURNAL_EVENTS="5"
readonly EXP_HEAD_SHA="b55e8b3f5916445db84a4fc9e6d342113b8a538ba20fe5c20dc94f7c7a42cf90"
readonly EXP_KEY_SHA="6a129d96ed1af2e5f7c890821c8fddd27c7e4b368847884274712e126bf797d7"
readonly EXP_PKG_SCOPE="nullpkg_1ffc9ec7aae12b75ef50400da674812f"
readonly EXP_PKG_SCOPE_OCCURRENCES="5"

# --------------------------------------------------------------------------
# THE v9 CONTINUATION SEED  (NEW IN v10 -- the defining change)
# --------------------------------------------------------------------------
#
# The completed v9 lab. It is preserved evidence in its own right AND it is the
# read-only source this run copies its shadow from. Both facts are true at once
# and the second grants no write permission whatsoever: this path appears in
# this file only in readonly assignments, in printf, in comparisons, and as the
# SOURCE side of an rsync. It is never a write target, never deleted, never
# renamed, never chmod-ed, never normalised, and no Git command is ever run
# inside it.
readonly PRESERVED_LAB_REPAIR17="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR17_6a3ce02e4a0448d5a7206f6eb4260bbcb87989da9f0a541feafea7dd4be0dc19"

# The EXACT workspace inside that lab which becomes this run's shadow. This is
# the whole point of v10: it carries the seven-event interview journal whose
# event 7 is the routed review signal the v9 coverage review produced, and that
# event exists NOWHERE else -- not in the real workspace, not in any earlier
# lab.
readonly V9_CONTINUATION_SEED="${PRESERVED_LAB_REPAIR17}/shadow/NH_CLAUDE_CODEX_DESIGN_LOOP"

readonly SEED_STATE="${V9_CONTINUATION_SEED}/nh_interview_state"
readonly SEED_JOURNAL="${SEED_STATE}/nh_interview_journal.jsonl"
readonly SEED_JOURNAL_HEAD="${SEED_STATE}/nh_interview_journal.head"
readonly SEED_AUTH_KEY="${SEED_STATE}/nh_interview_authenticity.key"

# The seed's frozen identity. Read from the preserved seed itself when this
# launcher was written, never inherited from any report.
#
# The authenticity key is frozen by sha256 ONLY. Its CONTENTS are never read
# into this launcher, never printed, and never written into any proof artefact.
readonly EXP_SEED_JOURNAL_SHA="38e36d4dc4b8de24437857ebbe30199f13122017e374a486caf2cfc2d3b19036"
readonly EXP_SEED_JOURNAL_BYTES="65683"
readonly EXP_SEED_JOURNAL_LINES="7"
readonly EXP_SEED_JOURNAL_EVENTS="7"
readonly EXP_SEED_HEAD_SHA="cb913314f2b198f4d8352d7145e05ff40c09b86a3852e2a12bd7da6556bc03eb"
readonly EXP_SEED_KEY_SHA="6a129d96ed1af2e5f7c890821c8fddd27c7e4b368847884274712e126bf797d7"
readonly EXP_SEED_PKG_SCOPE_OCCURRENCES="7"

# The v9 shadow marker the seed already carries. It is one of the exactly four
# permitted real-vs-seed differences (section 4c) and it is deliberately frozen
# by content, not merely tolerated by name.
readonly EXP_SEED_V9_MARKER_SHA="8ec92b2c4c993de8e44cb1c437ac88ae17ac8087e517eabfa8b3c2dd458b04ba"

# --------------------------------------------------------------------------
# EVENT 7 -- THE CONTINUATION SIGNAL, FROZEN FIELD BY FIELD
# --------------------------------------------------------------------------
#
# These are IDENTIFIERS AND DIGESTS ONLY. Not one of them is a classification,
# a disposition, a verdict or an answer, and nothing in this launcher reads the
# signal's title, its evidence or any other wording. They exist for exactly one
# purpose: to prove that the state being continued is the state v9 actually
# left, and not some other journal that merely happens to have seven lines.
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

# --------------------------------------------------------------------------
# THE EXACTLY FOUR PERMITTED REAL-vs-SEED DIFFERENCES  (section 4c)
# --------------------------------------------------------------------------
#
# A continuation may not run stale source. The seed is a HISTORICAL copy of the
# real workspace plus whatever the completed v9 run legitimately created, so it
# is allowed to differ from the current real workspace in exactly these four
# places and nowhere else. Every one of them is classified, not tolerated:
#
#   1. .nh_shadow_marker
#        SEED ONLY. v9 shadow provenance -- the marker v9 wrote after its copy
#        verification so the namespace could prove the substitution happened.
#   2. nh_interview_state/nh_interview_journal.jsonl
#        DIFFERS. v9 controller-owned interview continuation state: the seed
#        holds seven authenticated events, the real workspace holds its own
#        untouched five. Events 6 and 7 exist only in the seed.
#   3. nh_interview_state/nh_interview_journal.head
#        DIFFERS. The same continuation state: the seed head is committed at
#        event 7, the real head at event 5.
#   4. controller/NH_SHADOW_REHEARSAL_LAUNCHER_v10.sh
#        REAL ONLY. This launcher. The historical v9 seed was copied before it
#        existed and therefore cannot contain it.
#
# ANY OTHER DIFFERENCE OF ANY KIND FAILS THE RUN CLOSED, before any provider
# call: an extra path, a missing path, a changed byte in nh_loop.py, in any
# launcher v1..v9, in the NH-GOVERNANCE tree, in a candidate, in an authority
# file, in the Decision Defaults, in cursorrules, in the Companion, in the
# Working Map, or in any ordinary workspace file.
readonly SEED_DIFF_ALLOWED_SEED_ONLY=".nh_shadow_marker"
readonly SEED_DIFF_ALLOWED_REAL_ONLY="controller/NH_SHADOW_REHEARSAL_LAUNCHER_v10.sh"
readonly SEED_DIFF_ALLOWED_DIFFERS_JOURNAL="nh_interview_state/nh_interview_journal.jsonl"
readonly SEED_DIFF_ALLOWED_DIFFERS_HEAD="nh_interview_state/nh_interview_journal.head"

# --- THE THREE EXPLAINED WORKSPACE-ROOT DIRECTORIES (NEW IN v8) ---
#
# .agents, .codex and .git appeared together at the protected workspace ROOT at
# 2026-08-14 01:18:54, all three empty, while Codex was open locally for the
# Repair-16 independent audit. Official Codex documentation names exactly these
# three as special workspace paths under a writable root, so they are
# classified here as explained Codex/tool workspace artefacts -- and NOTHING
# more than that. Their future contents are not trusted, they are not N.H
# authority, and their presence authorises no Codex configuration, no skills
# and no Git activity.
#
# They are listed here so section 4a can freeze them BY EXACT PATH AND EXACT
# SAFE SHAPE. They are deliberately NOT tolerated as "some extra dot
# directories": each must be present, a real directory, not a symlink, not a
# special file, and EMPTY AT EVERY DEPTH. Anything else fails the run closed.
#
# Note what this does NOT do. It does not whitelist arbitrary future files
# under them. A single entry appearing under any of the three fails the gate,
# which is the whole point: the classification covers three empty directories,
# not a writable area.
readonly WS_SPECIAL_DIRS=(
  "${WS}/.agents"
  "${WS}/.codex"
  "${WS}/.git"
)

# The exact expected shape, asserted for every member of the set above.
readonly WS_SPECIAL_DIR_EXPECTED_ENTRIES="0"

readonly JOURNAL="${STATE}/nh_interview_journal.jsonl"
readonly JOURNAL_HEAD="${STATE}/nh_interview_journal.head"
readonly AUTH_KEY="${STATE}/nh_interview_authenticity.key"
readonly LOCK_TXN="${STATE}/nh_candidate_transaction.lock"
readonly LOCK_JOURNAL="${STATE}/nh_interview_journal.lock"

# --- lab: NEW, keyed to the Repair-17 controller identity AND to the exact
#     routed signal this continuation exists to carry forward ---
# Never reused. If this exact path already exists the launcher ABORTS in
# section 3: it does not delete it, does not clean it, does not overwrite it and
# does not write into it.
#
# It is deliberately NOT the v9 lab path. The v9 lab is preserved evidence and
# the read-only continuation seed; writing this run's output into it would
# destroy the very state this run exists to continue.
readonly LAB="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR17_CONTINUATION_V10_6a3ce02e4a0448d5a7206f6eb4260bbcb87989da9f0a541feafea7dd4be0dc19_rs_2593b06ab1684bbf19a6ffb70d915bd2"

# THE PRESERVED EARLIER REHEARSAL LABS. These constants exist so the launcher
# can refuse to collide with any of them and can witness that none moved. Each
# appears in this file ONLY in a readonly assignment, a printf and a comparison
# -- never in a write position.
#
# These paths are READ-ONLY in the exact sense defined under READ-ONLY, STATED
# EXACTLY in the file header: no create, write, truncate, rename, chmod, chown
# or delete is ever issued against them, and the one effect a read can have is
# an atime refresh, which no proof captures. The same applies to the protected
# workspace, which must also be read to be hashed and copied.
readonly PRESERVED_LAB_V1="/home/ness/NH_AICP_SHADOW_REHEARSAL_ce3a38f43f287a56bd635ed836edf002a2db50a7"
readonly PRESERVED_LAB_REPAIR9="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR9_acc8dee2c3ae0a27738fc1c1b4b08bb30bb55243d8ce9c22c393c6505e798690"
readonly PRESERVED_LAB_REPAIR10="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR10_704ad177f1ec25a33f1fe026a94429dad96d65c62030737cb4cfc23d1e28be6f"
# The Repair-14 rehearsal ran, and its lab is now preserved evidence in its
# own right: it holds the one-time four-stage run whose stage-2 refusal is
# exactly what Repair 15 corrects. v7 must never collide with it and must
# witness that it did not move.
readonly PRESERVED_LAB_REPAIR14="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR14_76b60e90e2bc6835edb088df7126428e2365e16cb376cb00274a086de1698957"
# The Repair-15 rehearsal ran, and its lab is now preserved evidence in its own
# right: it holds the one-time run whose stage-1 Codex-error diagnostic is
# exactly what Repair 16 corrects. v8 must never collide with it and must
# witness that it did not move.
#
# NO HISTORICAL METADATA OF IT IS REQUIRED HERE, and none is asserted. Like
# every other preserved lab it is captured at the start of THIS run and compared
# only against that capture, so its CURRENT content and tree state from before
# v8 is what is preserved. Anything it previously disclosed as historically
# changed is outside this proof by construction; the proof fails only if
# something moves DURING this run.
readonly PRESERVED_LAB_REPAIR15="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR15_94f0734f65da7e13964858c06f9e9fec4774f72045115caa03ecc34759d4a9e9"
# The Repair-16 rehearsal ran, and its lab is now preserved evidence in its own
# right: it is the completed one-time v8 rehearsal. v9 must never collide with
# it and must witness that it did not move.
#
# NO HISTORICAL METADATA OF IT IS REQUIRED HERE, and none is asserted. Nothing
# about what that run observed is claimed anywhere in this file. Like every
# other preserved lab it is captured at the start of THIS run and compared only
# against that capture, so its CURRENT content and tree state from before v9 is
# what is preserved. Anything it previously disclosed as historically changed is
# outside this proof by construction; the proof fails only if something moves
# DURING this run.
readonly PRESERVED_LAB_REPAIR16="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR16_882fe3e510544b97361bd31853d39d5269b0e1fb4d39dbc2b0a387f139b10833"
# The Repair-17 rehearsal ran, and its lab -- the completed one-time v9
# rehearsal -- is preserved evidence in its own right. v10 must never collide
# with it and must witness that it did not move.
#
# IT IS ALSO THIS RUN'S CONTINUATION SEED, and that changes nothing about its
# protection. It is declared as PRESERVED_LAB_REPAIR17 above, next to the seed
# constants, so the two roles are visibly the same path; it is named here so the
# collision refusal, the preserved-lab sweep and the report all cover it
# explicitly rather than only by glob.
#
# NO HISTORICAL METADATA OF IT IS REQUIRED HERE, and none is asserted. Like
# every other preserved lab it is captured at the start of THIS run and compared
# only against that capture, so the proof fails only if something moves DURING
# this run.

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

# --- reserved verdict exit codes (see header note 7) ---
readonly RC_ORIGINAL_PROOF_FAIL=90
readonly RC_CREDENTIAL_WITNESS_CHANGED=91
readonly RC_PRESERVED_LAB_PROOF_FAIL=92
readonly RC_LAB_CREDENTIAL_FOUND=93

# THE EARLY-STOP STATUS. It is NOT a safety verdict and it is NOT corruption.
#
# It means exactly this: the natural one-pass sequence stopped safely before
# completing all four stages -- an inventory that needs another segment, a
# material unknown, a genuine question now waiting for Ness, a coverage gap, or
# a closed interview gate. Every one of those is a legitimate observation of the
# CURRENT shadow state and none of them is a fault.
#
# It exists because the last stage's own status cannot carry that meaning. A
# coverage review that routes a gap exits 0; a closed gate exits 0. Returning
# that 0 would report a sequence that stopped as a run that finished, which is
# the one thing this launcher must never do.
#
# 3 is chosen deliberately: nh_loop.py returns only 0, 1 and 2, so 3 cannot be
# confused with a controller status, and it sits well clear of the 90-93 safety
# codes, which still outrank it.
readonly RC_SEQUENCE_STOPPED=3

# Proof artefacts of the PROTECTED ORIGINAL that MUST be byte-identical before
# and after. authority.sha256 is new in v5: the adopted Decision Defaults v2.3
# file is now part of the protected state and is frozen like the candidates.
readonly PROTECTED_PROOF_FILES=(
  "nh_loop.identity"
  "launchers.identity"
  "controller.git"
  "governance.git"
  "candidates.sha256"
  "authority.sha256"
  "interview_state.sha256"
  "interview_state.meta"
  "journal.counts"
  "workspace.files.sha256"
  "workspace.meta"
)

# Proof artefacts of PRESERVED EARLIER REHEARSAL LABS -- the v1, Repair-9,
# Repair-10, Repair-14, Repair-15 and Repair-16 labs, the last two being the
# completed v7 and v8 rehearsals. Kept as their own set, with their own verdict
# and their own reserved exit code, so a preserved-evidence failure is never
# reported as, or hidden behind, a protected-workspace verdict.
readonly PRESERVED_LAB_PROOF_FILES=(
  "preserved_labs.sha256"
  "preserved_labs.meta"
  "continuation_seed.identity"
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
#
# LAB_CREATED : the disposable lab exists on disk, so no report may say that
#               nothing was created.
# RUN_STARTED : an isolated controller stage was entered, so no report may say
#               that no model or provider call was made.
# REPORTED    : a full report has already been printed, so the exit handler must
#               not print a second, contradictory one.
# AFTER_PROOF_DONE : the post-run re-proof of the protected original actually
#                    completed, so ORIGINAL_PROOF holds a real verdict. Until
#                    then no report may say anything about containment.
LAB_CREATED=0
RUN_STARTED=0
REPORTED=0
AFTER_PROOF_DONE=0
ORIGINAL_PROOF="NOT-RUN"
PRESERVED_LAB_PROOF="NOT-RUN"
LAB_CREDENTIAL_SCAN="NOT-RUN"

# The four stage results. NOT-RUN is a real, reported state and is never
# silently rendered as success or as failure: a stage that never ran because an
# earlier one stopped the sequence is a different fact from a stage that ran and
# returned zero, and this launcher keeps the two apart everywhere.
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
# work the instant one of them fails. A containment failure is not something to
# carry on through: the remaining stages are abandoned and the final proofs are
# still taken.
STAGE_SOURCE_PROOF=""
CONTAINMENT_BREACHED=0

# LOCKS_TAKEN / LOCKS_HELD : the two advisory locks on the interview-state lock
# files are the one operation this launcher performs against the protected
# original that is NOT a plain read, so the report must be able to say exactly
# whether they were taken and whether they are still held. Without these flags
# the report could only make a design-level statement about locks, which would
# be false on every path that fails before section 6 ever runs.
#
# They are COUNTS, not booleans, and each is updated the instant its own lock is
# acquired or released -- never once at the end of section 6. Acquisition is
# not atomic across the two locks: the candidate-transaction lock can be taken
# and the interview-journal lock then refused by a concurrent holder, which
# dies immediately. A single flag set after both would still read 0 on that
# path, so the report would state "No lock was taken" while this process was in
# fact holding one.
LOCKS_TAKEN=0
LOCKS_HELD=0

# The shared, honest tail. Both the block path and the unexpected-exit path use
# it, so the two can never drift apart and claim different things.
#
# Every sentence below is gated on evidence this launcher actually has. In
# particular it must NEVER assert that the protected original is untouched
# merely because the launcher's own code does not write to it: once a sandboxed
# stage has been entered, containment is a claim about the ISOLATION, and only
# the completed AFTER proof can settle it.
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

  # The advisory locks are the one non-read operation this launcher performs
  # against the protected original, so the report states exactly what happened
  # to them rather than claiming the original was "only read". Gated on the
  # counts, because most failure paths never reach section 6 at all.
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

  # --- the preserved earlier rehearsals ---
  # Deliberately NOT "never modified": reading them can refresh atime on this
  # relatime filesystem. See READ-ONLY, STATED EXACTLY in the file header.
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
  printf 'The last of those is ALSO this run\047s continuation seed. It was read to\n' >&2
  printf 'be copied and to be authenticated, and nothing else was done to it: no\n' >&2
  printf 'create, write, append, truncate, rename, link, unlink, chmod, chown or\n' >&2
  printf 'utimes was issued against it, and no Git command was run inside it.\n' >&2
  if [ "$AFTER_PROOF_DONE" = "1" ]; then
    printf 'They were re-witnessed after the run: %s\n' "$PRESERVED_LAB_PROOF" >&2
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

# An EXIT handler, deliberately NOT an ERR handler.
#
# An ERR trap fires even under `set +e`, so it would hijack the places where a
# non-zero exit is EXPECTED and handled on purpose: the isolation self-test, and
# above all the three real controller stages, whose non-zero exits are ordinary
# outcomes this launcher exists to record. An ERR trap there would abort before
# the AFTER proof ever ran -- destroying the most important safety output --
# while printing claims that were false at that point. An EXIT handler fires
# once, only on actual script exit, and cannot interfere with a handled status.
on_exit() {
  local rc=$?
  trap - EXIT
  if [ "$rc" -ne 0 ] && [ "$REPORTED" != "1" ]; then
    REPORTED=1
    printf '\n[BLOCKED] the launcher stopped unexpectedly (exit %s)\n' "$rc" >&2
    printf '\nSHADOW_REHEARSAL=BLOCKED\n' >&2
    # No fixed claim about the proof here: report_state states exactly what was
    # and was not established, from the flags, so this path cannot contradict it.
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
      The protected source state has moved. The rehearsal refuses to run against
      source that is not the source this launcher was frozen against."
  fi
  note "${label} matches frozen identity"
}

# These MUST fail loudly. The naive `sha256sum -- "$1" | awk '{print $1}'` form
# inside a command substitution yields an EMPTY string when sha256sum cannot
# read the file, and printf then happily records a blank hash with exit status
# zero. Two captures that failed the same way -- an unreadable file before and
# after -- produce byte-identical listings, compare EQUAL, and get reported as
# proof that nothing changed. Verified on this host: with the naive form, an
# unreadable credential file yields a blank hash in both captures and the
# witness reads UNCHANGED while nothing was actually witnessed.
#
# A distinct sentinel cannot be mistaken for a hash, fails every frozen
# comparison, and is visible in the proof artefacts.
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

# Read-only git. GIT_OPTIONAL_LOCKS=0 keeps `git status` from refreshing (and
# therefore writing) the index. There is no Git write anywhere in this file.
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
  # proof: two equally incomplete captures compare EQUAL and are then reported
  # as evidence of containment.
  local cap_err="${out}/capture.errors"
  : > "$cap_err"

  # --- nh_loop.py identity ---
  {
    printf 'sha256 %s\n' "$(sha_of "${CTRL}/nh_loop.py")"
    printf 'bytes  %s\n'  "$(bytes_of "${CTRL}/nh_loop.py")"
    printf 'lines  %s\n'  "$(wc -l < "${CTRL}/nh_loop.py")"
    printf 'stat   %s\n'  "$(stat -c 'mode=%f perm=%a uid=%u gid=%g size=%s mtime=%Y ctime=%Z inode=%i links=%h' -- "${CTRL}/nh_loop.py")"
  } > "${out}/nh_loop.identity"

  # --- all ten launcher artefacts: v1-v9 must stay byte-identical, and this
  #     file must stay byte-identical to itself across the run ---
  {
    local lf
    for lf in "$LAUNCHER_V1_BASENAME" "$LAUNCHER_V2_BASENAME" \
              "$LAUNCHER_V3_BASENAME" "$LAUNCHER_V4_BASENAME" \
              "$LAUNCHER_V5_BASENAME" "$LAUNCHER_V6_BASENAME" \
              "$LAUNCHER_V7_BASENAME" "$LAUNCHER_V8_BASENAME" \
              "$LAUNCHER_V9_BASENAME" "$LAUNCHER_V10_BASENAME"; do
      if [ -f "${CTRL}/${lf}" ]; then
        printf '%s %s %s\n' "$(sha_of "${CTRL}/${lf}")" "$(bytes_of "${CTRL}/${lf}")" "$lf"
      else
        printf '%s %s %s\n' "ABSENT" "ABSENT" "$lf"
      fi
    done
  } > "${out}/launchers.identity"

  # --- controller git state (read-only) ---
  # --ignored=traditional, for two reasons.
  #
  # Plain --untracked-files=all silently omits every gitignored path, so a
  # capture without an --ignored mode cannot see .claude/ or __pycache__/ at all.
  #
  # And --ignored=matching is not enough either: it COLLAPSES an ignored
  # directory to the directory itself. Measured on this host, a probe file
  # dropped into __pycache__/ leaves `!! __pycache__/` completely unchanged,
  # while traditional mode lists each ignored file individually and the probe
  # appears immediately. Only traditional mode can witness the ignored set.
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
  # The three Authority Integrity versions plus the preserved reviewed source of
  # the adopted Decision Defaults v2.3.
  {
    local c
    for c in "$CAND_V10" "$CAND_V11" "$CAND_V12" "$CAND_DD23"; do
      printf '%s %s %s\n' "$(sha_of "${CAND_DIR}/${c}")" "$(bytes_of "${CAND_DIR}/${c}")" "$c"
    done
  } > "${out}/candidates.sha256"

  # --- the adopted authoritative Decision Defaults ---
  # New in v5. This file is the current adopted behavioural authority and it is
  # an untracked entry in the N.H worktree, so it is frozen and witnessed in its
  # own right rather than left to the whole-workspace hash alone.
  {
    printf '%s %s %s\n' "$(sha_of "${AUTH_DIR}/${AUTH_DD23}")" \
                        "$(bytes_of "${AUTH_DIR}/${AUTH_DD23}")" "$AUTH_DD23"
  } > "${out}/authority.sha256"

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

  # --- PRESERVED REHEARSAL LABS: read-only witness ---
  # Every earlier shadow-rehearsal lab -- the v1, Repair-9, Repair-10,
  # Repair-14, Repair-15 and Repair-16 labs, the last two being the completed
  # v7 and v8 rehearsals -- is preserved evidence. This launcher's own lab is
  # excluded because it is being written by design. If any preserved lab
  # changes at all between before and after, the comparison fails and this run
  # fails closed.
  #
  # A preserved lab is NOT required to exist: earlier reports instruct Ness to
  # delete a lab once it has been reviewed. Absence before and absence after is
  # simply no change. Appearing or vanishing mid-run is a change, and fails.
  # Capture errors are NOT suppressed here. A preserved lab that cannot be fully
  # traversed would otherwise produce the same partial listing before and after,
  # compare equal, and be reported as PRESERVED_LAB_PROOF=PASS on a witness that
  # never actually covered the evidence.
  local plab_raw="${out}/preserved_labs.raw"
  : > "$plab_raw"
  {
    local d
    for d in "${HOME_REAL}"/NH_AICP_SHADOW_REHEARSAL_*; do
      [ -e "$d" ] || continue
      [ "$d" != "$LAB" ] || continue
      hash_tree_into "$d" "$plab_raw" "$cap_err" \
        || die "could not hash the preserved rehearsal lab ${d}; see ${cap_err}"
    done
  }
  LC_ALL=C sort "$plab_raw" > "${out}/preserved_labs.sha256"
  rm -f "$plab_raw"

  # Built through a raw file rather than `{ ... } | sort`, because a pipeline
  # puts the group in a SUBSHELL: a die() in there would exit only the subshell.
  # It happens to propagate today because pipefail is set, but that makes a
  # fail-closed guarantee depend on a shell option set 1500 lines away. Written
  # this way, the status is checked in the current shell and cannot be lost.
  local plab_meta_raw="${out}/preserved_labs.meta.raw"
  : > "$plab_meta_raw"
  for d in "${HOME_REAL}"/NH_AICP_SHADOW_REHEARSAL_*; do
    [ -e "$d" ] || continue
    [ "$d" != "$LAB" ] || continue
    find "$d" -xdev -printf '%y %m %U %G %s %T@ %C@ %i %n %p\n' \
         >> "$plab_meta_raw" 2>> "$cap_err" \
      || die "could not read metadata for the preserved rehearsal lab ${d}; see ${cap_err}"
  done
  LC_ALL=C sort "$plab_meta_raw" > "${out}/preserved_labs.meta"
  rm -f "$plab_meta_raw"

  # --- THE v9 CONTINUATION SEED, WITNESSED BY NAME (NEW IN v10) ---
  #
  # The seed lives inside the preserved v9 lab, so it is already inside the
  # sweep above. It is ALSO witnessed here by name, because it is the one piece
  # of state this entire continuation depends on: if it moves, the run must say
  # so in those words rather than as one changed line inside a listing of
  # thousands.
  #
  # It belongs to the PRESERVED-LAB proof set, not the protected-workspace one,
  # so a seed that moved is reported as a preserved-evidence failure with the
  # preserved-evidence exit code -- never as a protected-workspace failure.
  #
  # The authenticity key's CONTENTS are never read here. Only its sha256 is
  # taken, and a sha256 is a one-way digest from which no key can be recovered.
  {
    printf 'seed_journal_sha256              %s\n' "$(sha_of "$SEED_JOURNAL")"
    printf 'seed_journal_bytes               %s\n' "$(bytes_of "$SEED_JOURNAL")"
    printf 'seed_journal_lines               %s\n' "$(wc -l < "$SEED_JOURNAL")"
    printf 'seed_journal_events              %s\n' "$(grep -c '[^[:space:]]' -- "$SEED_JOURNAL" || true)"
    printf 'seed_head_sha256                 %s\n' "$(sha_of "$SEED_JOURNAL_HEAD")"
    printf 'seed_key_sha256                  %s\n' "$(sha_of "$SEED_AUTH_KEY")"
    printf 'seed_marker_sha256               %s\n' "$(sha_of "${V9_CONTINUATION_SEED}/${SHADOW_MARKER_NAME}")"
    printf 'seed_pkg_scope_occurrences       %s\n' "$(grep -c -F -- "$EXP_PKG_SCOPE" "$SEED_JOURNAL" || true)"
    printf 'seed_event7_sha_occurrences      %s\n' "$(grep -c -F -- "$EXP_SEED_EVENT7_SHA" "$SEED_JOURNAL" || true)"
    printf 'seed_event6_sha_occurrences      %s\n' "$(grep -c -F -- "$EXP_SEED_EVENT6_SHA" "$SEED_JOURNAL" || true)"
    printf 'seed_routed_signal_occurrences   %s\n' "$(grep -c -F -- "$EXP_ROUTED_SIGNAL_ID" "$SEED_JOURNAL" || true)"
    printf 'seed_standing_target_occurrences %s\n' "$(grep -c -F -- "$EXP_STANDING_TARGET_ID" "$SEED_JOURNAL" || true)"
  } > "${out}/continuation_seed.identity"

  # --- host model-auth / config witness: HASHES AND METADATA ONLY ---
  # Contents are never read into the proof. A sha256 is a one-way digest and no
  # credential value can be recovered from it.
  #
  # This witness keeps its OWN error file rather than sharing cap_err, because
  # it is deliberately a separate, lesser signal: a concurrently running host
  # Claude Code or Codex session legitimately rewrites these files, and that must
  # not be confused with a containment failure. But a witness that could not be
  # taken is not the same as a witness that came back unchanged, so a non-empty
  # error file becomes its own CAPTURE-FAILED verdict rather than silently
  # reading as UNCHANGED.
  local cred_err="${out}/credentials.errors"
  : > "$cred_err"
  # Each hash is taken explicitly, with its own status checked and its own error
  # routed to cred_err. Going through sha_of here would record the sentinel but
  # would NOT record an error, and this witness is judged purely by before/after
  # comparison with no frozen constant to fall back on -- so a failure that
  # repeated identically would still compare equal and read as UNCHANGED.
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
    # errexit is suspended around this pipeline ON PURPOSE, using the same
    # set +e / set -e idiom this launcher already uses for the self-test and for
    # the three real stages.
    #
    # The whole point of the credential witness is that a capture failure
    # becomes a CAPTURE-FAILED VERDICT, not a dead launcher. Under `set -e` with
    # pipefail, an unreadable file anywhere under .ssh or .config makes this
    # pipeline non-zero and the shell exits IMMEDIATELY -- before the PIPESTATUS
    # check below, before cred_err is written, and before section 12 ever
    # evaluates CREDENTIAL_WITNESS. Verified on this host: the run aborts and no
    # verdict is ever assigned. Suspending errexit here is what lets the failure
    # be recorded and reported instead of just killing the run.
    local d st
    for d in "/home/ness/.ssh" "/home/ness/.config"; do
      if [ -d "$d" ]; then
        set +e
        find "$d" -maxdepth 1 -type f -print0 2>> "$cred_err" \
          | LC_ALL=C sort -z 2>> "$cred_err" \
          | xargs -0 -r sha256sum -- 2>> "$cred_err"
        st=("${PIPESTATUS[@]}")
        set -e
        if [ "${st[0]}" != "0" ] || [ "${st[1]}" != "0" ] || [ "${st[2]}" != "0" ]; then
          printf 'traversal or hashing failed under %s (statuses: %s)\n' \
                 "$d" "${st[*]}" >> "$cred_err"
        fi
      fi
    done
  } > "${out}/credentials.sha256"

  # Built through a raw file with every status checked, NOT through
  # `{ ... } | sort`, for the same two reasons the hash pipeline was rebuilt:
  #
  #   - `find ... || true` erases every non-zero find status. A find killed by a
  #     signal writes no stderr of its own, leaves a PARTIAL metadata stream,
  #     and leaves credentials.errors empty. Truncated identically before and
  #     after, the two captures compare EQUAL and the witness reads UNCHANGED
  #     while nothing was actually witnessed -- the same false verdict this
  #     witness already had to be repaired for once.
  #   - a failing `sort` inside that pipeline was still exposed to
  #     set -e + pipefail, so it could kill the launcher before section 12 ever
  #     produced the CAPTURE-FAILED verdict. That is exactly the failure class
  #     already fixed for the hashing pipeline, and it was left standing here.
  #
  # There is no pipeline now, so pipefail cannot reach it, and every status is
  # recorded rather than discarded.
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
# incomplete listing with an exit status of zero. Measured on this host: a
# failing find in that pipeline gives PIPESTATUS "1 0 0" while the pipeline as a
# whole reports success. An incomplete hash listing that is incomplete in the
# same way before and after would compare EQUAL and be reported as proof.
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
# when one was, and 2 when the scan ITSELF could not be completed. Only PATHS
# are ever written to the report. No matched content is read into the report,
# printed, or kept anywhere.
#
# 0 does NOT mean the lab holds no model login material, and this comment must
# not say that it does -- see the marker discussion below and the verdict name
# NO-KNOWN-MARKERS. The executable report is careful about this; the wording
# here is held to the same standard, because a comment that overclaims is how
# the next reader comes to trust something the code never established.
#
# The 2 case exists because a suppressed scan failure is indistinguishable from
# a clean result: an unreadable file, a traversal error or a killed grep would
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
  #    check cannot see. The markers are deliberately high-specificity: they
  #    match the shapes the host login files actually use, and none of them
  #    occurs anywhere in the protected workspace, so a hit means something new.
  #
  #    The variable names OPENAI_API_KEY / ANTHROPIC_API_KEY are deliberately
  #    NOT markers: they appear in this launcher's own env-leak self-test, which
  #    is copied into the shadow, and would fire on every run.
  #
  #    Each marker's first character is written as a one-character bracket
  #    expression for the same reason. The lab contains a copy of this launcher,
  #    so a plain literal would match its own source text and report every run
  #    as carrying credentials -- which, being a fail-closed gate, would block
  #    every run. "[a]ccess_token" matches the string access_token but does not
  #    match itself. The PRIVATE KEY marker needs no such treatment: its own
  #    text contains [A-Z ]* literally and therefore cannot match itself.
  #
  #    -a, NOT -I. -I makes grep treat any file containing a NUL byte as
  #    non-matching, so a credential written into a file that also holds binary
  #    data would be invisible. Verified on this host: a file containing NUL
  #    bytes plus an access_token field is MISSED under -I and CAUGHT under -a.
  #
  #    The last marker is a JWT shape. Without it a raw opaque token written on
  #    its own, with no surrounding JSON field name and no sk- prefix, would not
  #    be recognised.
  #
  #    This is a SHAPE-based scan and is bounded by that. It does not compare
  #    against the real credential values, because doing so would mean reading
  #    host secrets into this process -- which this launcher does not do
  #    anywhere, by design.
  #
  #    THEREFORE A PASSING RESULT IS NOT "CLEAN" AND MUST NEVER BE CALLED THAT.
  #    Verified on this host, two credentials that this scan does NOT see:
  #      - an opaque token in a shape no marker covers (a bare hex string);
  #      - any credential inside compressed or encoded content, e.g. a gzipped
  #        JSON blob holding a real access_token.
  #    No marker set fixes the second case, so the verdict is named for what it
  #    actually establishes -- NO-KNOWN-MARKERS -- and the summary says plainly
  #    that this is not proof of absence.
  #    The key-prefix marker is deliberately GENERIC -- s[k]- followed by at
  #    least 16 key characters -- rather than a list of known vendor prefixes.
  #    A prefix list missed classic sk-..., service-account sk-svcacct-... and
  #    anything a client starts issuing tomorrow. The generic form subsumes
  #    sk-ant- and sk-proj- as well. Both snake_case and camelCase OAuth field
  #    names are covered, because the two clients do not agree on which they
  #    emit.
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
             "$PRESERVED_LAB_REPAIR17"; do
  if [ "$LAB" = "$_plab" ]; then
    die "the configured lab path is a preserved rehearsal lab:
        ${LAB}
      That lab is evidence. Refusing to reuse it."
  fi
done
unset _plab
note "new lab path is distinct from every preserved rehearsal lab"

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
# SECTION 4a — THE THREE EXPLAINED WORKSPACE-ROOT DIRECTORIES  (NEW IN v8)
# --------------------------------------------------------------------------
#
# .agents, .codex and .git at the protected workspace ROOT are classified as
# explained Codex/tool workspace artefacts, and are frozen here by exact path
# and exact safe shape. Six properties are asserted for each, and every one of
# them fails the run CLOSED:
#
#   1. it exists;
#   2. it is NOT a symlink  (checked before any -d test, because -d follows a
#      link and would otherwise accept a symlink to a directory);
#   3. it IS a real directory, not a special file;
#   4. it contains exactly zero entries;
#   5. nothing exists under it at ANY depth -- no file, no subdirectory, no
#      special entry;
#   6. and, for the workspace root as a whole, it does not resolve as a Git
#      repository, which is what establishes that the root .git is not a
#      functional repository or any other active store.
#
# WHY THIS IS A GATE AND NOT A TOLERANCE. These three paths lie outside both
# Git checkouts, so neither worktree status can see them. Without this gate they
# would enter the proof only through workspace.meta -- frozen as the normal
# baseline and copied into the shadow with nothing having asserted what they
# are. The classification covers THREE EMPTY DIRECTORIES. It does not whitelist
# their future contents: one entry appearing under any of them fails the run.
#
# WHAT THIS FUNCTION NEVER DOES. It never creates, deletes, normalises, chmods
# or writes anything, inside those directories or anywhere else. It only tests.
# Nothing under them is ever treated as authority, candidate material,
# interview state or N.H package content -- no code path anywhere in this file
# reads from them at all.
#
# THE ROOT .git IS NEVER USED AS A REPOSITORY BY THIS LAUNCHER. Every Git read
# goes through git_ro with an explicit repository argument, and the only two
# values ever passed are ${CTRL} and ${NHGOV}. ${WS} is passed to git_ro in
# exactly one place -- the assertion below, whose entire purpose is to require
# that it FAILS.
assert_workspace_special_dirs() {
  local d listing st count
  for d in "${WS_SPECIAL_DIRS[@]}"; do
    # 1. present. -e alone would be false for a dangling symlink, so -L is
    #    tested too: a dangling symlink must be reported as the wrong SHAPE
    #    below, never as simply absent.
    if [ ! -e "$d" ] && [ ! -L "$d" ]; then
      die "an explained workspace-root directory is MISSING:
        ${d}
      v9 is frozen to this exact set of three empty directories. One of them
      has been removed. Nothing is created to repair it: re-freeze the launcher
      against the real current state deliberately, exactly as every earlier
      rebase did."
    fi

    # 2. not a symlink. Tested BEFORE -d, which follows symlinks.
    if [ -L "$d" ]; then
      die "an explained workspace-root directory is a SYMLINK:
        ${d} -> $(readlink -- "$d" 2>/dev/null || printf '<unreadable>')
      A symlink here could redirect the shadow copy, so this fails closed.
      Refusing to rehearse."
    fi

    # 3. a real directory, not a special file.
    if [ ! -d "$d" ]; then
      die "an explained workspace-root path is not a directory:
        ${d}
        found: $(stat -c '%F' -- "$d" 2>/dev/null || printf '<unreadable>')
      The classification covers empty DIRECTORIES only. Refusing to rehearse."
    fi

    # 4 and 5. empty at every depth.
    #
    # No pipeline is used, so pipefail cannot reach this and a traversal failure
    # cannot be mistaken for an empty directory. find's status is checked, and
    # its stderr is folded into the listing so an unreadable subtree makes the
    # listing non-empty as well as the status non-zero. Either one fails.
    st=0
    listing="$(find "$d" -mindepth 1 -printf '%y %p\n' 2>&1)" || st=$?
    if [ "$st" -ne 0 ]; then
      die "an explained workspace-root directory could not be traversed:
        ${d}
      A directory that cannot be read is not a directory proved empty.
      Refusing to rehearse."
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
      artefacts and nothing more. Their contents are NOT trusted, are NOT N.H
      authority, and are NOT authorised material. Nothing is deleted and nothing
      is normalised here. Review what appeared, then re-freeze this launcher
      deliberately if it is legitimate."
    fi

    note "explained workspace-root directory verified empty and unchanged in shape: ${d}"
  done

  # 6. The workspace ROOT must NOT resolve as a Git repository. This is what
  #    proves the root .git is not a functional repository -- and it is stricter
  #    than inspecting that directory's contents, because it also fails if some
  #    ENCLOSING directory ever became a repository that could capture the
  #    workspace. Either way the two real repositories are the only ones this
  #    launcher reads, and they are asserted separately just below.
  local root_git_dir grc=0
  root_git_dir="$(git_ro "$WS" rev-parse --git-dir 2>/dev/null)" || grc=$?
  if [ "$grc" -eq 0 ]; then
    die "the protected workspace ROOT resolves as a Git repository:
        ${WS}
        git-dir: ${root_git_dir}
      It must not. The root .git is frozen as an EMPTY, non-functional Codex
      workspace artefact, and the only repositories this launcher reads are the
      controller repository and the NH-GOVERNANCE repository. Refusing to
      rehearse."
  fi
  note "the workspace root does not resolve as a Git repository; root .git is non-functional"

  # And the two REAL repositories are exactly the frozen ones, each resolving to
  # its own git-dir inside its own checkout. Their branches, HEADs and complete
  # statuses are frozen separately below.
  expect "controller git-dir"    "$(git_ro "$CTRL" rev-parse --absolute-git-dir)"  "${CTRL}/.git"
  expect "NH-GOVERNANCE git-dir" "$(git_ro "$NHGOV" rev-parse --absolute-git-dir)" "${NHGOV}/.git"
}


# --------------------------------------------------------------------------
# SECTION 4b — THE CONTINUATION SEED, AND THE SIGNAL IT CARRIES  (NEW IN v10)
# --------------------------------------------------------------------------
#
# v10 exists to continue the state the completed v9 run left behind, and that
# state is worth exactly as much as the proof that it IS that state. This gate
# establishes it in four escalating steps, and every one of them fails the run
# CLOSED, long before the isolation self-test and therefore long before any
# possible provider or model call:
#
#   1. SHAPE. The preserved v9 lab and the seed workspace inside it exist, are
#      real directories, and are not symlinks. A symlink here could redirect
#      the rsync SOURCE and silently seed the run from somewhere else entirely.
#
#   2. IDENTITY. The seed journal, journal head and authenticity key match the
#      exact sha256 / byte / line / event counts frozen above, and the seed
#      still carries the v9 shadow marker with its exact content.
#
#   3. THE SIGNAL. The journal holds exactly seven events; event 7 is the LAST
#      one; and its type, route, signal source, routed signal id, standing
#      target id, issue key, finding key, package scope, own digest and
#      previous digest are exactly the frozen ones.
#
#   4. AUTHENTICITY. The whole seven-event chain and the journal head
#      AUTHENTICATE under the CONTROLLER'S OWN semantics -- its event digest,
#      its HMAC over its own canonical authentication material, its sequence
#      and previous-digest chaining, and its head authentication -- not merely
#      "the JSON line is present". Step 3 without step 4 would accept a forged
#      or hand-edited event that happened to carry the right strings.
#
# WHAT THIS GATE DELIBERATELY DOES NOT DO.
#   It does not classify the signal. It does not decide whether it is settled,
#   mechanical, dependent or genuinely open. It does not convert it into a
#   question, does not answer it, and does not read its title or its evidence
#   text at any point. Only identifiers and digests are compared. The FIRST
#   live stage of this run is a fresh ordinary question-validation, and the
#   controller alone may ever decide what this signal really is.
#
# WHY THE CONTROLLER'S OWN CODE, AND NOT A REIMPLEMENTATION HERE.
#   A second implementation of the authentication rule is exactly the "parallel
#   gate" mistake this project refuses everywhere else: it would drift, and a
#   drifted verifier that says PASS is worse than no verifier. nh_loop.py is
#   imported READ-ONLY as a module and its own functions are called. It is
#   never executed as a program here, no provider is contacted, and nothing is
#   written.
#
# WHY -B AND PYTHONDONTWRITEBYTECODE ARE LOAD-BEARING.
#   An ordinary import writes controller/__pycache__/nh_loop.cpython-*.pyc into
#   the PROTECTED workspace. That is a real write to the protected original, it
#   would appear in workspace.files.sha256 and workspace.meta, and it would fail
#   the controller worktree gate on the second, under-lock assertion of
#   assert_frozen_identities. Both are set, and the absence of bytecode is
#   proved afterwards rather than assumed.
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

sys.stdout.write("SEED_CONTINUATION_AUTHENTICATED\n")
'

assert_no_controller_bytecode() {
  local where="$1" found
  found="$(find "${CTRL}" -name '__pycache__' -o -name '*.pyc' 2>/dev/null || true)"
  if [ -n "$found" ]; then
    die "python bytecode appeared in the protected controller directory ${where}:
${found}
      A read-only authentication step must write NOTHING into the protected
      original. Remove it, then investigate why -B and PYTHONDONTWRITEBYTECODE
      did not hold."
  fi
}

assert_continuation_seed() {
  # 1. SHAPE -- the preserved lab and the seed inside it.
  if [ -L "$PRESERVED_LAB_REPAIR17" ]; then
    die "the preserved v9 lab is a SYMLINK:
        ${PRESERVED_LAB_REPAIR17}
      A symlink here could redirect the continuation copy. Refusing to rehearse."
  fi
  if [ ! -d "$PRESERVED_LAB_REPAIR17" ]; then
    die "the preserved v9 lab is missing or is not a directory:
        ${PRESERVED_LAB_REPAIR17}
      It is BOTH the preserved Repair-17 evidence and this run's only authorised
      continuation seed. Nothing is created to repair it. Refusing to rehearse."
  fi
  if [ -L "$V9_CONTINUATION_SEED" ]; then
    die "the v9 continuation seed workspace is a SYMLINK:
        ${V9_CONTINUATION_SEED}
      Refusing to rehearse."
  fi
  if [ ! -d "$V9_CONTINUATION_SEED" ]; then
    die "the v9 continuation seed workspace is missing or is not a directory:
        ${V9_CONTINUATION_SEED}
      Refusing to rehearse."
  fi
  if [ -L "$SEED_STATE" ] || [ ! -d "$SEED_STATE" ]; then
    die "the v9 continuation seed interview state is missing or is not a real
      directory:
        ${SEED_STATE}
      Refusing to rehearse."
  fi
  for _sf in "$SEED_JOURNAL" "$SEED_JOURNAL_HEAD" "$SEED_AUTH_KEY"; do
    if [ -L "$_sf" ] || [ ! -f "$_sf" ]; then
      die "a v9 continuation seed interview-state file is missing or is not an
      ordinary, non-symlink file:
        ${_sf}
      Refusing to rehearse."
    fi
  done
  unset _sf
  note "the preserved v9 lab and its continuation seed are real, non-symlink directories"

  # 2. IDENTITY -- exactly the seed this launcher was frozen against.
  expect "seed journal sha256" "$(sha_of "$SEED_JOURNAL")"   "$EXP_SEED_JOURNAL_SHA"
  expect "seed journal bytes"  "$(bytes_of "$SEED_JOURNAL")" "$EXP_SEED_JOURNAL_BYTES"
  expect "seed journal lines"  "$(wc -l < "$SEED_JOURNAL")"  "$EXP_SEED_JOURNAL_LINES"
  expect "seed journal events" \
         "$(grep -c '[^[:space:]]' -- "$SEED_JOURNAL" || true)" "$EXP_SEED_JOURNAL_EVENTS"
  expect "seed journal head sha256"     "$(sha_of "$SEED_JOURNAL_HEAD")" "$EXP_SEED_HEAD_SHA"
  expect "seed authenticity key sha256" "$(sha_of "$SEED_AUTH_KEY")"     "$EXP_SEED_KEY_SHA"
  expect "seed v9 shadow marker sha256" \
         "$(sha_of "${V9_CONTINUATION_SEED}/${SHADOW_MARKER_NAME}")" "$EXP_SEED_V9_MARKER_SHA"
  expect "seed authenticated package scope occurrences" \
         "$(grep -c -F -- "$EXP_PKG_SCOPE" "$SEED_JOURNAL" || true)" \
         "$EXP_SEED_PKG_SCOPE_OCCURRENCES"

  # 3. THE SIGNAL -- present exactly once, by identifier and by digest.
  #    These are counts over the journal file, so a duplicated or planted
  #    identifier fails just as loudly as a missing one.
  expect "seed event 7 digest occurrences" \
         "$(grep -c -F -- "$EXP_SEED_EVENT7_SHA" "$SEED_JOURNAL" || true)" \
         "$EXP_SEED_EVENT7_SHA_OCCURRENCES"
  expect "seed event 6 digest occurrences" \
         "$(grep -c -F -- "$EXP_SEED_EVENT6_SHA" "$SEED_JOURNAL" || true)" \
         "$EXP_SEED_EVENT6_SHA_OCCURRENCES"
  expect "seed routed signal occurrences" \
         "$(grep -c -F -- "$EXP_ROUTED_SIGNAL_ID" "$SEED_JOURNAL" || true)" \
         "$EXP_SEED_ROUTED_SIGNAL_OCCURRENCES"
  expect "seed standing target occurrences" \
         "$(grep -c -F -- "$EXP_STANDING_TARGET_ID" "$SEED_JOURNAL" || true)" \
         "$EXP_SEED_STANDING_TARGET_OCCURRENCES"

  # 4. AUTHENTICITY -- the controller's own digest, HMAC, chain and head rules.
  #
  # Not one identifier above is trusted because the string is there. This step
  # is what makes the seed evidence rather than text.
  assert_no_controller_bytecode "before the seed authentication step"
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
  assert_no_controller_bytecode "after the seed authentication step"

  if [ "$seed_auth_rc" -ne 0 ] \
     || ! printf '%s' "$seed_auth_out" | grep -q '^SEED_CONTINUATION_AUTHENTICATED$'; then
    die "the v9 continuation seed did NOT authenticate under the controller's own
      journal semantics (status ${seed_auth_rc}):
${seed_auth_out}
      The continuation state is not proved to be the state v9 left. Nothing is
      repaired, reconstructed or replaced here. Refusing to rehearse."
  fi
  note "the seven-event continuation seed authenticates under the controller's own semantics"
  note "the routed review signal ${EXP_ROUTED_SIGNAL_ID} is present as the last event, unresolved"
}

# --------------------------------------------------------------------------
# SECTION 4c — CURRENT-SOURCE COMPATIBILITY GATE  (NEW IN v10)
# --------------------------------------------------------------------------
#
# A CONTINUATION MAY NOT RUN STALE SOURCE.
#
# The seed is a copy of the real workspace as it stood when v9 ran, plus what
# that run legitimately created. If the real project has moved since -- a
# corrected nh_loop.py, an edited candidate, a new authority file, a changed
# Working Map -- then continuing from the seed would silently rehearse against
# source that no longer exists, and would do it while claiming to be current.
#
# So the COMPLETE path-and-content difference set is computed here and required
# to be EXACTLY the four classified differences frozen in section 0. Not "at
# most" and not "including": both directions are checked, and an expected
# difference that has VANISHED fails too, because a seed whose journal has
# reverted to the real five-event one is not a continuation seed at all.
#
# This runs inside assert_frozen_identities, so it happens twice: once as a
# precondition, before the isolation self-test and therefore before any
# possible provider call, and once again under both original locks immediately
# before the copy.
#
# It compares CONTENT, not timestamps. mtime, atime and ctime necessarily
# differ between an original and a copy taken later, and comparing them would
# make the gate fire on every run for no reason. What matters for staleness is
# the bytes, the set of paths, and the shape of each entry.
readonly SEED_SOURCE_COMPARATOR='
import hashlib, os, stat, sys

real_root = sys.argv[1]
seed_root = sys.argv[2]
allow_seed_only = set()
allow_real_only = set()
allow_differs = set()
for item in sys.argv[3:]:
    role, _, rel = item.partition(":")
    if role == "SEED_ONLY":
        allow_seed_only.add(rel)
    elif role == "REAL_ONLY":
        allow_real_only.add(rel)
    elif role == "DIFFERS":
        allow_differs.add(rel)
    else:
        sys.stdout.write("unknown allowance role %s\n" % role)
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
    # would compare EQUAL and this gate would report a stale seed as compatible
    # -- the exact "incomplete capture reported as proof" failure this launcher
    # family refuses everywhere else. Both are closed here: the root must be a
    # real directory, and onerror re-raises instead of skipping.
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
    real = walk(real_root)
    seed = walk(seed_root)
except OSError as exc:
    sys.stdout.write("TRAVERSAL-FAILED %s\n" % exc)
    sys.exit(2)

unexplained = []
for rel in sorted(set(real) | set(seed)):
    in_real = rel in real
    in_seed = rel in seed
    if in_real and in_seed and real[rel] == seed[rel]:
        continue
    if in_real and not in_seed:
        if rel not in allow_real_only:
            unexplained.append("REAL-ONLY   %s" % rel)
    elif in_seed and not in_real:
        if rel not in allow_seed_only:
            unexplained.append("SEED-ONLY   %s" % rel)
    else:
        if rel not in allow_differs:
            unexplained.append("DIFFERS     %s  real=%s seed=%s" % (rel, real[rel][1][:16], seed[rel][1][:16]))

missing = []
for rel in sorted(allow_seed_only):
    if rel in real or rel not in seed:
        missing.append("EXPECTED SEED-ONLY DIFFERENCE ABSENT  %s" % rel)
for rel in sorted(allow_real_only):
    if rel in seed or rel not in real:
        missing.append("EXPECTED REAL-ONLY DIFFERENCE ABSENT  %s" % rel)
for rel in sorted(allow_differs):
    if rel not in real or rel not in seed or real[rel] == seed[rel]:
        missing.append("EXPECTED CONTENT DIFFERENCE ABSENT    %s" % rel)

for line in unexplained:
    sys.stdout.write(line + "\n")
for line in missing:
    sys.stdout.write(line + "\n")

if unexplained:
    sys.exit(1)
if missing:
    sys.exit(3)
sys.stdout.write("SEED_SOURCE_COMPATIBLE\n")
'

assert_seed_matches_current_source() {
  local cmp_out cmp_rc=0
  set +e
  cmp_out="$(
    PYTHONDONTWRITEBYTECODE=1 "$PY3" -B -c "$SEED_SOURCE_COMPARATOR" \
      "$WS" \
      "$V9_CONTINUATION_SEED" \
      "SEED_ONLY:${SEED_DIFF_ALLOWED_SEED_ONLY}" \
      "REAL_ONLY:${SEED_DIFF_ALLOWED_REAL_ONLY}" \
      "DIFFERS:${SEED_DIFF_ALLOWED_DIFFERS_JOURNAL}" \
      "DIFFERS:${SEED_DIFF_ALLOWED_DIFFERS_HEAD}" 2>&1
  )"
  cmp_rc=$?
  set -e

  if [ -d "$PROOF" ]; then
    printf '%s\n' "$cmp_out" > "${PROOF}/continuation-seed-compatibility.txt" 2>/dev/null || true
  fi

  case "$cmp_rc" in
    0)
      if ! printf '%s' "$cmp_out" | grep -q '^SEED_SOURCE_COMPATIBLE$'; then
        die "the real-source / continuation-seed comparison returned success without
      stating it. Refusing to rehearse on an unreadable result."
      fi
      ;;
    1)
      die "THE REAL PROJECT SOURCE HAS DRIFTED FROM THE v9 CONTINUATION SEED.
${cmp_out}
      A continuation may not run stale source. The seed is permitted to differ
      from the current real workspace in exactly four classified places -- the
      v9 shadow marker, the seven-event interview journal, its head, and this
      launcher, which the historical seed cannot contain. Everything listed
      above is outside that set.
      Nothing is copied, normalised or reconciled here. Review the drift, then
      decide deliberately. Refusing to rehearse."
      ;;
    3)
      die "AN EXPECTED CONTINUATION DIFFERENCE IS ABSENT.
${cmp_out}
      The seed no longer differs from the real workspace in the way a genuine
      v9 continuation seed must. The most serious form of this is a seed whose
      interview journal has reverted to the real five-event one -- which would
      mean the routed review signal is gone and there is nothing to continue.
      Refusing to rehearse."
      ;;
    *)
      die "the real-source / continuation-seed comparison could not be completed
      (status ${cmp_rc}):
${cmp_out}
      A comparison that did not finish is not a comparison that passed.
      Refusing to rehearse."
      ;;
  esac

  note "the v9 continuation seed still represents the current real source"
  note "  permitted differences, and only these four:"
  note "    seed only : ${SEED_DIFF_ALLOWED_SEED_ONLY}  (v9 shadow provenance)"
  note "    differs   : ${SEED_DIFF_ALLOWED_DIFFERS_JOURNAL}  (v9 continuation state)"
  note "    differs   : ${SEED_DIFF_ALLOWED_DIFFERS_HEAD}  (v9 continuation state)"
  note "    real only : ${SEED_DIFF_ALLOWED_REAL_ONLY}  (this launcher)"
}

# The complete frozen gate, as a function, because it must be asserted TWICE:
# once as a precondition, and again immediately before the shadow copy while
# both original locks are held. Without the second assertion the before-proof
# captured at copy time would silently become the accepted baseline for any
# change made after the first gate, and that changed state would then be copied
# and would pass both the during and the after comparisons.
assert_frozen_identities() {
  expect "nh_loop.py sha256"  "$(sha_of "${CTRL}/nh_loop.py")"        "$EXP_LOOP_SHA"
  expect "nh_loop.py bytes"   "$(bytes_of "${CTRL}/nh_loop.py")"      "$EXP_LOOP_BYTES"
  expect "nh_loop.py lines"   "$(wc -l < "${CTRL}/nh_loop.py")"       "$EXP_LOOP_LINES"

  # Launcher v1 is preserved unchanged and is gated on explicitly.
  [ -f "${CTRL}/${LAUNCHER_V1_BASENAME}" ] \
    || die "launcher v1 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v1 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V1_BASENAME}")"   "$EXP_LAUNCHER_V1_SHA"
  expect "launcher v1 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V1_BASENAME}")" "$EXP_LAUNCHER_V1_BYTES"

  # v2 is preserved evidence too, and is gated on by identity exactly like v1.
  [ -f "${CTRL}/${LAUNCHER_V2_BASENAME}" ] \
    || die "launcher v2 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v2 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V2_BASENAME}")"   "$EXP_LAUNCHER_V2_SHA"
  expect "launcher v2 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V2_BASENAME}")" "$EXP_LAUNCHER_V2_BYTES"

  # v3 is preserved evidence and is gated on by identity exactly like v1 and v2.
  [ -f "${CTRL}/${LAUNCHER_V3_BASENAME}" ] \
    || die "launcher v3 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v3 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V3_BASENAME}")"   "$EXP_LAUNCHER_V3_SHA"
  expect "launcher v3 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V3_BASENAME}")" "$EXP_LAUNCHER_V3_BYTES"

  # v4 is this file's DIRECT PREDECESSOR and is preserved evidence in its own
  # right, so it is now gated by identity exactly like v1, v2 and v3.
  [ -f "${CTRL}/${LAUNCHER_V4_BASENAME}" ] \
    || die "launcher v4 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v4 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V4_BASENAME}")"   "$EXP_LAUNCHER_V4_SHA"
  expect "launcher v4 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V4_BASENAME}")" "$EXP_LAUNCHER_V4_BYTES"

  # v5 is this file's DIRECT PREDECESSOR and is preserved evidence in its own
  # right, so it is now gated by identity exactly like v1..v4. It was written,
  # reviewed and never run; nothing about it is retracted by v6 existing.
  [ -f "${CTRL}/${LAUNCHER_V5_BASENAME}" ] \
    || die "launcher v5 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v5 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V5_BASENAME}")"   "$EXP_LAUNCHER_V5_SHA"
  expect "launcher v5 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V5_BASENAME}")" "$EXP_LAUNCHER_V5_BYTES"

  # v6 is this file's DIRECT PREDECESSOR. It RAN once, against the Repair-14
  # controller, and its lab is preserved evidence; it is gated by identity
  # exactly like v1..v5.
  [ -f "${CTRL}/${LAUNCHER_V6_BASENAME}" ] \
    || die "launcher v6 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v6 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V6_BASENAME}")"   "$EXP_LAUNCHER_V6_SHA"
  expect "launcher v6 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V6_BASENAME}")" "$EXP_LAUNCHER_V6_BYTES"

  # v7 is this file's DIRECT PREDECESSOR. It RAN once, against the Repair-15
  # controller, and its lab is preserved evidence; it is gated by identity
  # exactly like v1..v6.
  [ -f "${CTRL}/${LAUNCHER_V7_BASENAME}" ] \
    || die "launcher v7 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v7 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V7_BASENAME}")"   "$EXP_LAUNCHER_V7_SHA"
  expect "launcher v7 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V7_BASENAME}")" "$EXP_LAUNCHER_V7_BYTES"

  # v8 is this file's DIRECT PREDECESSOR. It RAN once, against the Repair-16
  # controller, and its lab is preserved evidence; it is gated by identity
  # exactly like v1..v7.
  [ -f "${CTRL}/${LAUNCHER_V8_BASENAME}" ] \
    || die "launcher v8 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v8 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V8_BASENAME}")"   "$EXP_LAUNCHER_V8_SHA"
  expect "launcher v8 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V8_BASENAME}")" "$EXP_LAUNCHER_V8_BYTES"

  # v9 is this file's DIRECT PREDECESSOR. It RAN once, against the Repair-17
  # controller; its lab is preserved evidence AND this run's continuation seed.
  # It is gated by identity exactly like v1..v8, and being the seed's author
  # earns it no exemption of any kind.
  [ -f "${CTRL}/${LAUNCHER_V9_BASENAME}" ] \
    || die "launcher v9 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v9 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V9_BASENAME}")"   "$EXP_LAUNCHER_V9_SHA"
  expect "launcher v9 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V9_BASENAME}")" "$EXP_LAUNCHER_V9_BYTES"

  # Launcher v10 is THIS file. It cannot hash-gate on itself, but it must be the
  # file that is present, and it is carried in the before/after proof set so any
  # change to it during the run is caught.
  [ -s "${CTRL}/${LAUNCHER_V10_BASENAME}" ] \
    || die "launcher v10 is missing or empty at ${CTRL}/${LAUNCHER_V10_BASENAME}"
  note "all ten launcher artefacts present in ${CTRL}"

  # The three explained workspace-root directories, frozen by exact shape.
  # Asserted here so it is covered by BOTH invocations of this function: once as
  # a precondition, long before the isolation self-test and therefore long
  # before any possible provider or model call, and again under lock immediately
  # before the shadow copy.
  assert_workspace_special_dirs

  expect "controller branch"  "$(git_ro "$CTRL" rev-parse --abbrev-ref HEAD)" "$EXP_CTRL_BRANCH"
  expect "controller HEAD"    "$(git_ro "$CTRL" rev-parse HEAD)"              "$EXP_CTRL_HEAD"

  # The controller worktree must be EXACTLY these twelve entries and nothing
  # else: the modified nh_loop.py, the ten launcher artefacts, and the one
  # gitignored editor FILE. Nothing is filtered out.
  #
  # NOTE ON __pycache__, RESTATED FOR v10 BECAUSE IT MATTERS MORE HERE. This
  # gate lists no bytecode entry, and none exists on disk. v10 imports
  # nh_loop.py as a module in section 4b to authenticate the continuation seed
  # with the controller's OWN semantics, and an ordinary import would write
  # controller/__pycache__/nh_loop.cpython-*.pyc into the protected workspace --
  # a real write to the protected original, and one that would then fail this
  # very gate on the second, under-lock assertion. Every such invocation
  # therefore runs python3 with -B AND with PYTHONDONTWRITEBYTECODE=1, and
  # section 4b additionally proves afterwards that no bytecode appeared.
  #
  # NOTE ON THE THREE EXPLAINED WORKSPACE-ROOT DIRECTORIES. None of them appears
  # in this status and none of them could: .agents, .codex and .git sit at the
  # WORKSPACE root, which is outside this repository's worktree entirely. That is
  # exactly why they are gated separately and explicitly in section 4a, rather
  # than being left to a Git status that structurally cannot see them.
  #
  # NOTE ON __pycache__. v4 additionally froze
  #   !! __pycache__/nh_loop.cpython-314.pyc
  # That path does not exist on disk now. v5 does NOT carry it forward: the
  # expected set is re-read from the real current worktree, so the gate stays an
  # EXACT match against what is actually there rather than an inherited list
  # that happens to be wrong. If the bytecode is ever regenerated this gate
  # stops the run, which is the correct behaviour for a launcher frozen to one
  # exact moment: it fails closed and the identity is re-frozen deliberately.
  #
  # The --ignored mode is load-bearing, and traditional is the only sufficient
  # one. Plain --untracked-files=all omits every gitignored path, so a gate
  # built on it would NOT see .claude/settings.local.json, and would equally not
  # see anything dropped into the gitignored state/, runs/, logs/ or cache/
  # paths this repository also ignores. --ignored=matching would see the
  # directories but COLLAPSE them: measured on this host, a probe file dropped
  # into an ignored directory leaves its `!! dir/` line byte-identical, so
  # arbitrary ignored children would pass the gate and be copied into the
  # shadow. traditional lists every ignored file individually, so the gate
  # freezes the real, complete set.
  local ctrl_status ctrl_status_expected
  ctrl_status="$(
    git_ro "$CTRL" status --porcelain=v1 --untracked-files=all --ignored=traditional \
      | LC_ALL=C sort
  )"
  ctrl_status_expected="$(
    printf '%s\n' \
      " M nh_loop.py" \
      "!! .claude/settings.local.json" \
      "?? ${LAUNCHER_V1_BASENAME}" \
      "?? ${LAUNCHER_V2_BASENAME}" \
      "?? ${LAUNCHER_V3_BASENAME}" \
      "?? ${LAUNCHER_V4_BASENAME}" \
      "?? ${LAUNCHER_V5_BASENAME}" \
      "?? ${LAUNCHER_V6_BASENAME}" \
      "?? ${LAUNCHER_V7_BASENAME}" \
      "?? ${LAUNCHER_V8_BASENAME}" \
      "?? ${LAUNCHER_V9_BASENAME}" \
      "?? ${LAUNCHER_V10_BASENAME}" | LC_ALL=C sort
  )"
  expect "controller worktree" "$ctrl_status" "$ctrl_status_expected"

  expect "N.H branch"         "$(git_ro "$NHGOV" rev-parse --abbrev-ref HEAD)" "$EXP_NH_BRANCH"
  expect "N.H HEAD"           "$(git_ro "$NHGOV" rev-parse HEAD)"              "$EXP_NH_HEAD"

  # The N.H worktree must be EXACTLY these five entries and nothing else.
  #
  # v4 froze three: the Authority Integrity candidate chain v1.0 / v1.1 / v1.2.
  # Two more exist now and BOTH ARE ACCOUNTED FOR EXPLICITLY rather than
  # tolerated as "some extra untracked files":
  #
  #   01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_3.md
  #       the Decision Defaults adopted by Ness on 2026-08-13, superseding v2.2.
  #   05_ACTIVE_CANDIDATE/NH_DECISION_DEFAULTS-S19_v2_3_CANDIDATE.md
  #       the exact reviewed candidate that adoption was taken from, preserved
  #       unchanged as the adoption source.
  #
  # The preserved Authority Integrity candidate chain is unchanged and every one
  # of the five entries is additionally frozen below by sha256 and byte count.
  # Any SIXTH entry of any kind -- tracked, untracked, ignored, staged, modified
  # or deleted -- fails this gate closed. Nothing is filtered and nothing is
  # accepted merely because it looks harmless.
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

  # The adopted Decision Defaults v2.3 and its preserved reviewed source.
  expect "decision defaults v2.3 candidate sha256" \
         "$(sha_of "${CAND_DIR}/${CAND_DD23}")"   "$EXP_DD23_CAND_SHA"
  expect "decision defaults v2.3 candidate bytes"  \
         "$(bytes_of "${CAND_DIR}/${CAND_DD23}")" "$EXP_DD23_CAND_BYTES"
  expect "decision defaults v2.3 adopted sha256" \
         "$(sha_of "${AUTH_DIR}/${AUTH_DD23}")"   "$EXP_DD23_AUTH_SHA"
  expect "decision defaults v2.3 adopted bytes"  \
         "$(bytes_of "${AUTH_DIR}/${AUTH_DD23}")" "$EXP_DD23_AUTH_BYTES"

  expect "journal sha256"  "$(sha_of "$JOURNAL")"          "$EXP_JOURNAL_SHA"
  expect "journal bytes"   "$(bytes_of "$JOURNAL")"        "$EXP_JOURNAL_BYTES"
  expect "journal events"  "$(grep -c '[^[:space:]]' -- "$JOURNAL" || true)" "$EXP_JOURNAL_EVENTS"
  expect "journal head sha256"     "$(sha_of "$JOURNAL_HEAD")" "$EXP_HEAD_SHA"
  expect "authenticity key sha256" "$(sha_of "$AUTH_KEY")"    "$EXP_KEY_SHA"
  expect "authenticated package scope occurrences" \
         "$(grep -c -F -- "$EXP_PKG_SCOPE" "$JOURNAL" || true)" "$EXP_PKG_SCOPE_OCCURRENCES"

  [ -f "$LOCK_TXN" ]     || die "candidate-transaction lock file missing: ${LOCK_TXN}"
  [ -f "$LOCK_JOURNAL" ] || die "interview-journal lock file missing: ${LOCK_JOURNAL}"

  # THE CONTINUATION GATES (new in v10). They live INSIDE this function on
  # purpose, so they are asserted on both of its invocations: once as a
  # precondition -- before the lab exists, before the isolation self-test, and
  # therefore before any possible provider or model call -- and once again under
  # both original locks immediately before the copy. Without the second
  # assertion, a seed or a real source that moved in between would become the
  # accepted baseline and would then be copied and compared only against itself.
  assert_continuation_seed
  assert_seed_matches_current_source

  note "every frozen identity matches; source state has not moved"
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
# launcher could create the same lab and both runs would proceed into it, and a
# symlink planted at that path would be ACCEPTED by `mkdir -p` -- silently
# redirecting every proof write, and the `rsync --delete` below, to wherever the
# symlink pointed, including a preserved lab. Verified on this host: `mkdir -p`
# succeeds on a pre-existing symlink, `mkdir` without -p fails EEXIST.
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
# commands printed below actually work the moment they are offered. Without this
# they do not exist until the redirects in section 11 create them, and
# `tail -f` on a missing file exits immediately with "no files remaining" --
# guidance that looks helpful and cannot be followed.
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
  chmod 0600 "${PROOF}/${_slug}.stdout"   "${PROOF}/${_slug}.stderr" \
             "${PROOF}/${_slug}.command"  "${PROOF}/${_slug}.exit-code" \
             "${PROOF}/${_slug}.started"  "${PROOF}/${_slug}.finished"
done
unset _slug
note "lab created atomically (mode 0700): ${LAB}"
say  "        NOTE: the lab will contain a copy of the N.H interview authenticity"
say  "        key, because the controller cannot append authenticated journal"
say  "        events without it -- and both the fresh question-validation and a"
say  "        clear coverage review append exactly such events. Delete the lab"
say  "        after review."
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
say  "        The controller writes its live progress to stderr -- the fresh GPT"
say  "        reviews, correction round, model pinned, new-or-resumed Claude"
say  "        session, seeded target, fresh OpenAI/Codex audit and verdict."
say  "        stdout carries the machine report."
say  ""
say  "        Neither stream dumps candidate contents."

# ==========================================================================
# SECTION 6 — TAKE BOTH ORIGINAL LOCKS, NON-BLOCKING
# ==========================================================================

step "ORIGINAL LOCKS"

# flock(2) is the same kernel lock primitive the controller takes with
# fcntl.flock, so this genuinely excludes a concurrent controller.
exec 200<"$LOCK_TXN"
flock -n -x 200 || die "the original candidate-transaction lock is held by another process.
      Something else is mid-transaction on the protected original. Refusing to copy."
# Counted the instant it is held, so the die() below -- which can fire while
# THIS lock is held -- reports the truth.
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
# SECTION 7 — PROOF BEFORE, COPY, VERIFY COPY, PROOF DURING  (locks held)
# ==========================================================================

step "ORIGINAL PROOF (BEFORE)"
capture_original_proof "${PROOF}/original.before"
note "before-proof written to ${PROOF}/original.before"

# Re-assert the WHOLE frozen gate against the state that was just captured, with
# both original locks held and before a single byte is copied.
#
# The first assertion happened before the lab existed and before the locks were
# taken. Anything that changed the protected original in that window would
# otherwise have been captured here as the accepted BEFORE baseline, copied into
# the shadow, and then compared only against itself -- passing the during and
# after comparisons while the rehearsal ran against source that is not the
# frozen source.
step "FROZEN SOURCE IDENTITY (RE-ASSERTED UNDER LOCK)"
assert_frozen_identities
note "the captured before-proof is the frozen source, not merely self-consistent"

step "CONTINUATION SHADOW COPY (SOURCE: THE PRESERVED v9 SHADOW)"

# THE SOURCE OF THIS COPY IS THE PRESERVED v9 SHADOW WORKSPACE, NOT THE REAL
# WORKSPACE. That is the defining change of v10 and it is stated here, at the
# exact line where it takes effect, so no reader can mistake what is being
# copied.
#
# The real workspace is NOT copied. Its interview journal is NOT overlaid onto
# the seed. Event 7 is NOT replaced. The seed journal is NOT reset to five
# events. Real candidate state is NOT copied over the seed. The seed is NOT
# cleaned, normalised or repaired in any way. The whole point of v10 is that
# the seven-event continuation state -- and the unresolved routed review signal
# that is its last event -- survives into this run intact.
#
# The real workspace keeps every one of its own protections regardless: it was
# frozen, proved before this copy, re-asserted under both locks moments ago,
# and it is proved again during the copy, after every stage, and finally from
# outside the namespace.
#
# The copy is EXACT. Nothing is excluded.
#
# v1 excluded controller/__pycache__/ and write-test/ as build noise and
# scratch. Both existed on disk with real content, and the same exclusions were
# applied to the verification, so the verification could only ever prove "equal
# apart from the excluded paths" while the launcher reported a byte-truthful
# copy. Neither path is referenced anywhere in nh_loop.py, so copying them
# changes no controller behaviour, and copying them makes the claim and the
# check agree.
#
# Never copied, because they are not in the workspace at all:
#   .ssh .netrc .config       - never copied
#   host .codex / .claude     - never copied; they are namespace-only anonymous
#                               copy-on-write overlays instead
#
# All five launcher scripts ARE copied, because the shadow is a truthful copy of
# the workspace and they are files in it. They are inert inside the namespace:
# nothing in the rehearsal executes them, and the controller only ever runs git
# against NH-GOVERNANCE, never against controller/, so their presence cannot
# affect any gate.

mkdir -m 0700 -p "$SHADOW_WS"
rsync -aHAX --numeric-ids --delete "${V9_CONTINUATION_SEED}/" "${SHADOW_WS}/" \
  || die "rsync copy of the v9 continuation seed into the new shadow failed"
note "v9 continuation seed copied into ${SHADOW_WS}"

step "CONTINUATION SHADOW COPY VERIFICATION (AGAINST THE v9 SEED)"

# Checksum dry-run compare, AGAINST THE v9 CONTINUATION SEED -- never against
# the real workspace. Comparing the new shadow to the real workspace would be
# wrong on its face: the two legitimately differ, in exactly the four ways
# section 4c enumerates, and a verification that expected them to be identical
# would either fail every run or have to be weakened until it proved nothing.
# The claim being made here is precise: THIS SHADOW IS A BYTE-TRUTHFUL COPY OF
# THE PRESERVED v9 SHADOW, which is a different and stronger claim than
# "resembles the real workspace".
#
# Any itemised line at all means the new shadow is not a truthful copy of the
# seed, and the rehearsal must not proceed.
#
# The exit STATUS is captured separately and is required to be zero. Discarding
# it with `|| true` would make a killed or otherwise failing dry run
# indistinguishable from a clean one: rsync would print nothing, COPY_DIFF would
# be empty, and an entirely unverified copy would be accepted as proved.
set +e
COPY_DIFF="$(rsync -aHAXn --delete --checksum --itemize-changes "${V9_CONTINUATION_SEED}/" "${SHADOW_WS}/" 2>&1)"
COPY_RC=$?
set -e
if [ "$COPY_RC" -ne 0 ] || [ -n "$COPY_DIFF" ]; then
  {
    printf 'rsync verification exit status: %s\n' "$COPY_RC"
    printf '%s\n' "$COPY_DIFF"
  } > "${PROOF}/DIFF.shadow-copy.txt"
  die "the continuation shadow could not be proved identical to the preserved
      v9 seed (rsync exit status ${COPY_RC}).
      See ${PROOF}/DIFF.shadow-copy.txt
      Refusing to rehearse against a copy that is not proved truthful."
fi
note "the new shadow is a byte-truthful copy of the preserved v9 continuation seed"

step "ORIGINAL PROOF (DURING) — proving the original did not move while copying"
capture_original_proof "${PROOF}/original.during"
if ! compare_proof_set "${PROOF}/original.before" "${PROOF}/original.during" "during" \
        "${PROTECTED_PROOF_FILES[@]}"; then
  die "the protected original changed WHILE it was being copied.
      The copy is not a coherent snapshot. Refusing to rehearse."
fi
note "protected original unchanged across the whole copy window"

if ! compare_proof_set "${PROOF}/original.before" "${PROOF}/original.during" "during-labs" \
        "${PRESERVED_LAB_PROOF_FILES[@]}"; then
  die "a preserved earlier rehearsal lab changed WHILE the shadow was being copied.
      Preserved rehearsal evidence must never move. Refusing to rehearse."
fi
note "preserved earlier rehearsal labs unchanged across the whole copy window"

# ==========================================================================
# SECTION 8 — RELEASE BOTH ORIGINAL LOCKS
# ==========================================================================

step "RELEASING ORIGINAL LOCKS"

# Only the lock FILES were copied. Kernel lock ownership is dropped here and is
# never carried into the namespace: these descriptors are closed before bwrap.
# Each count is decremented as its own descriptor closes. Closing the
# descriptor releases the lock unconditionally, so the decrement follows the
# close rather than the flock -u, whose status is not relied upon.
flock -u 200 || true
exec 200<&-
LOCKS_HELD=$((LOCKS_HELD - 1))
flock -u 201 || true
exec 201<&-
LOCKS_HELD=$((LOCKS_HELD - 1))
note "both original locks released; no lock ownership enters the shadow"

# The continuation shadow marker. It exists ONLY in a shadow, never in the real
# original, so its presence inside the namespace at the normal N.H path is
# positive proof that the substitution happened and the real workspace is not
# what is mounted.
#
# ONE THING IS DIFFERENT IN v10 AND IS STATED PLAINLY. The seed already carries
# v9's own marker, because the seed IS a v9 shadow, so this write OVERWRITES an
# inherited marker in the NEW lab rather than creating a fresh one. Nothing is
# overwritten in the v9 lab: the target below is ${SHADOW_WS}, which is the new
# disposable lab, and the seed itself is never opened for writing. The write
# still happens AFTER copy verification, so it can never pollute that
# comparison -- the verification above legitimately saw the v9 marker on both
# sides and matched it.
#
# It sits at the workspace root, outside both Git checkouts, so neither
# repository worktree status is affected.
#
# The token identifies FOUR things: Repair 17, the v10 continuation, the exact
# controller sha256, and the routed signal this continuation exists to carry
# forward. It therefore cannot collide with any earlier rehearsal marker --
# including the v9 one, which the seed carried in and which this line replaces.
# If
# anything ever mounted a preserved shadow here instead of the new one, the
# token check in the self-test would fail rather than pass.
SHADOW_TOKEN="nh-shadow-repair17-continuation-v10-${EXP_LOOP_SHA}-${EXP_ROUTED_SIGNAL_ID}"
printf '%s\n' "$SHADOW_TOKEN" > "${SHADOW_WS}/${SHADOW_MARKER_NAME}"
printf '%s\n' "$SHADOW_TOKEN" > "${RUNTIME_TMP}/.nh_shadow_tmp_marker"
note "shadow marker placed"

# ==========================================================================
# SECTION 9 — THE BUBBLEWRAP NAMESPACE
# ==========================================================================
#
# One namespace PER STAGE. Every stage gets the identical argument vector, built
# by this one function, so no stage can be run under weaker isolation than the
# self-test proved:
#
#   bwrap
#    -> python3 nh_loop.py question-coverage-review
#       -> Codex          -> Codex helpers / nested sandbox
#   bwrap
#    -> python3 nh_loop.py interview-gate        (no provider call at all)
#   bwrap
#    -> python3 nh_loop.py execute-next-claude-task
#       -> Codex          -> Codex helpers / nested sandbox
#       -> Claude
#
# WHY THREE NAMESPACES IS SAFE. The only controller state that must survive from
# one stage to the next is the shadow's own interview state -- the coverage
# clearance event, or the routed gap signals -- and that lives inside
# ${SHADOW_WS}, a real directory in the lab bind-mounted into every stage. It
# persists because it is a real file, not because a namespace persisted. What is
# re-created per stage is the anonymous credential overlay, the materialised
# .claude.json and /run, none of which carries controller state. Repair 10's
# same-session requirement is a WITHIN-execute requirement and stage 3 is one
# namespace holding one execute, so it is fully preserved.
#
# NOTHING HERE INJECTS, FAKES OR PRE-ANSWERS ANY CONTRACT.
#   Not not_ready_reason, not task_ready, not mechanical_design_specification,
#   not a coverage clearance, not a possible-gap finding, not a package-local
#   audit result, not a question-validation result, not a Codex verdict, not a
#   Claude correction result, and not a Claude specification stop. --clearenv
#   wipes the environment and the ONLY NH_-prefixed variable set back for a real
#   stage is NH_LOOP_INTERVIEW_STATE_DIR, which points at the shadow's own
#   interview state. Whether the real GPT coverage review, the real GPT design
#   specification, the real GPT correction specification and the real Claude
#   application behave as Repair 11 intends is exactly what this rehearsal
#   exists to find out. If a required schema is not produced, the controller
#   fails closed on its own and this launcher preserves that evidence. There is
#   no launcher-level retry.
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
    # This also puts every preserved rehearsal lab out of reach: they live
    # under /home/ness and are not among the paths put back below, so nothing
    # inside the namespace can even see them, let alone write to them.
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
  # Nothing else is forwarded. --clearenv means OPENAI_API_KEY,
  # ANTHROPIC_API_KEY, GitHub tokens, cloud credentials and proxy credentials
  # cannot reach the sandbox from this shell's environment. The clients use
  # their own login state through the copy-on-write credential mounts above.
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
# It runs ONCE, and that is sufficient BECAUSE every stage below is launched
# with the argument vector produced by build_bwrap_args -- the same function,
# with the same single argument, re-invoked per stage. There is no per-stage
# variation for a self-test to miss. A stage cannot be run under weaker
# isolation than what was proved here without editing build_bwrap_args itself.
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
# NH_* variable -- anything that could steer the controller, supply
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
# /proc/self/fd/N to the real object, reaching the protected workspace or a
# preserved lab even though /home/ness is hidden by tmpfs.
#
# Only stdin, stdout and stderr may be present. FD 11 is consumed by bwrap's
# --file and is gone by now.
#
# The ONLY tolerated entry is one whose readlink is EMPTY. That is a descriptor
# which no longer existed by the time it was inspected -- the shell's own
# directory handle for this very glob, already closed -- and a closed descriptor
# can carry nothing. Measured on this host: the live entries are exactly 0, 1
# and 2, and the enumeration artefacts always read back empty.
#
# There is deliberately NO exemption for descriptors whose target looks like
# /proc/<pid>/fd. Such an exemption would accept an inherited handle on another
# process's descriptor table, and /proc/self/fd/<N>/<M> would then traverse
# through it to the protected workspace or a preserved lab -- the exact class of
# escape this check exists to stop.
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

# every preserved rehearsal lab must be unreachable from inside: /home/ness is
# tmpfs and none of them was put back.
for d in /home/ness/NH_AICP_SHADOW_REHEARSAL_*; do
  [ ! -e "$d" ] || fail "a preserved rehearsal lab is visible inside the namespace: $d"
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
# inside the namespace. A pre-run check alone would leave a claim about the
# lab's final contents that nothing had actually tested.
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
# SECTION 11 — THE REPAIR-17 REAL TEST SEQUENCE, OVER CONTINUATION STATE
# ==========================================================================
#
# Four stages, in this exact order, each inside Bubblewrap, each AT MOST ONCE:
#
#   1. question-validation           one real fresh GPT review
#   2. question-coverage-review      one real fresh GPT review
#   3. interview-gate                read-only, no provider call
#   4. execute-next-claude-task      exactly once
#
# THE SEQUENCE IS v9's, UNCHANGED. What differs is only the state it starts
# from: the shadow now carries the preserved seven-event journal, so stage 1 is
# a FRESH question-validation over a history whose last event is the unresolved
# routed review signal rs_2593b06ab1684bbf19a6ffb70d915bd2. Nothing here tells
# the controller what to make of that signal.
#
# THIS LAUNCHER MAKES NO DISPOSITION AND FORCES NO OUTCOME.
#   It does not classify the routed signal, does not convert it into a Ness
#   question, does not answer one, does not decide whether the signal is
#   settled, mechanical, dependent or genuinely open, and contains no
#   classification or disposition vocabulary at all. Whatever stage 1 concludes
#   is the controller's own result.
#
#   Both natural outcomes are left exactly as v9 left them, and neither is
#   nudged:
#     - IF the fresh validation ADMITS A REAL NESS QUESTION, the existing
#       continuation gate below stops the sequence at stage 1 on
#       deliverable_question_count, because only Ness may answer it. Stages 2,
#       3 and 4 stay NOT-RUN, the interview gate is never opened, and the state
#       is preserved in this disposable lab for inspection.
#     - IF the fresh validation resolves the signal mechanically and the fresh
#       coverage review then clears, the ordinary interview gate -- the
#       controller's, not this launcher's -- decides whether the mechanical
#       path unlocks, exactly as it always did.
#   No stage is added, removed, reordered or repeated to reach either one.
#
# NOTHING IS INSERTED. There is no record-ness-answer, no next-question-group,
# no manual signal conversion, no retry, no alternate validator and no extra
# Claude call anywhere in this file.
#
# WHY THE SEQUENCE NOW STARTS AT QUESTION-VALIDATION. Under Repairs 12/13/14 the
# recorded validation of the current package is preserved history and is NOT
# current authority: it was taken while Decision Defaults v2.2 was adopted, and
# v2.3 is adopted now. question-coverage-review refuses -- before it invokes any
# model -- until a fresh validation against the current sources exists. A
# rehearsal that began at the coverage review could therefore never reach the
# stages it exists to exercise. v5's three-stage sequence is obsolete for that
# reason and for no other.
#
# THERE IS NO RETRY ANYWHERE. Not around a stage, not around a provider call,
# not around the controller. Each stage runs at most once. This launcher never
# answers a question, never fabricates or edits a journal event, never forces a
# gate open and never attempts a second execution. The controller owns its own
# design, application, fresh audit and bounded correction-round behaviour --
# including its lifetime limit of 5 correction rounds -- and none of it is
# duplicated or bypassed here.
#
# CONTINUATION IS EARNED, NOT ASSUMED. A stage may only be followed by the next
# one when the stage before it PERMITS CONTINUATION, and permission is read from
# the controller's OWN reported facts rather than from an exit code alone. That
# distinction is load-bearing: a coverage review that finds possible gaps exits
# ZERO and is doing its job correctly, so an exit-code-only rule would march
# straight past exactly the finding that should stop the run.
#
# Any of the following stops the sequence there, preserves every artefact
# already captured, and proceeds directly to the final proofs:
#
#   * a non-zero exit from any stage;
#   * a report this launcher cannot read a required scalar out of;
#   * an incomplete validation inventory;
#   * a material unknown;
#   * an open question waiting for Ness;
#   * a coverage gap;
#   * a closed interview gate;
#   * a protected-source proof that differs from the before-proof.
#
# EVERY ONE OF THOSE IS A VALID OBSERVATIONAL OUTCOME. None of them is a
# launcher fault, none is converted into success, and none is worked around.

# THE REPORT PARSER. A REAL ONE, BECAUSE THE FIRST ATTEMPT WAS NOT.
#
# WHAT WAS WRONG. The first version of this gate matched the report with
#   grep -m1 -F "  \"<key>\": "
# and called that "anchored to a top-level key". It is not anchored to anything:
# -F matches a SUBSTRING anywhere in the line, so a nested key at four-space
# indent -- `    "ok": false,` -- contains the two-space form and matches. With
# -m1 taking the FIRST hit, a nested key appearing earlier in the file is
# returned in place of the real top-level one. The controller's own reports
# carry nested objects with exactly these names, so this was not theoretical.
#
# It also stripped the trailing comma and was then compared against a value that
# still had one ("[],"), so the material-unknowns check could never pass. That
# failed closed, which is the safe direction, but it meant a check that looked
# like it was testing something was testing nothing.
#
# WHAT IT IS NOW. A structural parse, done by the same python3 the controller
# itself runs, reading only. The controller prints human lines and then ONE
# json.dumps(indent=2, sort_keys=True) report, so the report is the unique JSON
# object that starts at the beginning of a line and whose parse consumes the
# rest of the file except trailing whitespace. Every line-start "{" is tried
# with raw_decode; a candidate counts only if it decodes to a dict AND reaches
# EOF. Exactly one candidate must qualify -- zero or several is ambiguous output
# and is refused.
#
# The value is printed as canonical compact JSON, so true, 0, [] and "0" are all
# distinguishable and a type confusion cannot pass as a match.
#
# Exit status: 0 value printed, 2 unreadable file, 3 no single complete report,
# 4 no such TOP-LEVEL key. Anything else is an unexpected interpreter failure.
# Every one of them fails the gate closed.
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

# require_report_value <file> <key> <expected canonical JSON> <human description>
# True only when the controller's own report states, at TOP LEVEL, exactly
# <expected>. Unreadable, unparseable, ambiguous, absent, wrong-type and
# different all fail, and all fail CLOSED.
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
# aborting there would destroy the after-proof, which is the most important
# thing this launcher produces.
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

  # From here on no report may claim that no model or provider call was made.
  # Set before the stage starts, not after, because a stage killed mid-flight
  # may already have reached a provider.
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
  printf '%s\n' "$STAGE_SOURCE_PROOF" > "${PROOF}/${slug}.source-proof"
  if [ "$STAGE_SOURCE_PROOF" = "FAIL" ]; then
    CONTAINMENT_BREACHED=1
    SEQUENCE_STOP_REASON="the protected original or a preserved lab CHANGED during ${label}"
    say "[CONTAINMENT] the protected original changed during ${label}."
    say "              No further stage is run. Evidence is preserved."
  else
    note "protected original and preserved labs unchanged across ${label}"
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
# never. Under Repair 12 it binds the already-known package from this
# controller's own authenticated history; under Repairs 13/14 that history is
# read and proved by the controller itself and cannot be supplied to it.
#
# Nothing here answers a question, fabricates an event or edits the journal.
run_controller_stage "$STAGE1_SLUG" "$STAGE1_CMD" "STAGE 1 — question-validation"
VALIDATION_RC="$STAGE_RC"

if [ "$VALIDATION_RC" -ne 0 ]; then
  SEQUENCE_STOP_REASON="stage 1 question-validation exited ${VALIDATION_RC}"
fi
if stage_may_continue; then
  # THE CONTROLLER'S OWN FACTS, not an exit code. A validation can exit 0 having
  # recorded a page of a larger inventory, having left a material unknown, or
  # having created a genuine question for Ness -- and none of those may be
  # followed by a coverage review.
  require_report_value "${PROOF}/${STAGE1_SLUG}.stdout" "ok" "true" \
    "stage 1 did not report a clean result" || true
fi
if stage_may_continue; then
  require_report_value "${PROOF}/${STAGE1_SLUG}.stdout" \
    "validation_inventory_complete" "true" \
    "the question inventory is not complete, so there is nothing a coverage review may challenge" || true
fi
if stage_may_continue; then
  require_report_value "${PROOF}/${STAGE1_SLUG}.stdout" \
    "material_unknowns" "[]" \
    "the source check left a material unknown" || true
fi
if stage_may_continue; then
  require_report_value "${PROOF}/${STAGE1_SLUG}.stdout" \
    "deliverable_question_count" "0" \
    "a genuine question is now waiting for Ness, and only Ness may answer it" || true
fi

if ! stage_may_continue; then
  announce_stop
else
  # ------------------------------------------------------------------------
  # STAGE 2 — THE FRESH INDEPENDENT COVERAGE REVIEW
  # ------------------------------------------------------------------------
  #
  # One real GPT review. It challenges the COMPLETE inventory stage 1 just
  # recorded. It cannot create a question, cannot address Ness and cannot unlock
  # anything by itself.
  run_controller_stage "$STAGE2_SLUG" "$STAGE2_CMD" "STAGE 2 — question-coverage-review"
  COVERAGE_RC="$STAGE_RC"

  if [ "$COVERAGE_RC" -ne 0 ]; then
    SEQUENCE_STOP_REASON="stage 2 question-coverage-review exited ${COVERAGE_RC}"
  fi
  if stage_may_continue; then
    require_report_value "${PROOF}/${STAGE2_SLUG}.stdout" "ok" "true" \
      "stage 2 did not report a clean result" || true
  fi
  if stage_may_continue; then
    # A GAP EXITS ZERO. Read the finding, not the status.
    require_report_value "${PROOF}/${STAGE2_SLUG}.stdout" \
      "coverage_possible_gaps" "0" \
      "the fresh coverage review found a possible missed Ness choice and routed it as a signal" || true
  fi
  if stage_may_continue; then
    require_report_value "${PROOF}/${STAGE2_SLUG}.stdout" \
      "coverage_review_cleared" "true" \
      "the fresh coverage review did not record a clearance" || true
  fi

  if ! stage_may_continue; then
    announce_stop
  else
    # ----------------------------------------------------------------------
    # STAGE 3 — THE INTERVIEW GATE
    # ----------------------------------------------------------------------
    #
    # Read-only. No provider call of any kind. It reports the exact clearance
    # that execute-next-claude-task itself enforces.
    run_controller_stage "$STAGE3_SLUG" "$STAGE3_CMD" "STAGE 3 — interview-gate"
    GATE_RC="$STAGE_RC"

    if [ "$GATE_RC" -ne 0 ]; then
      SEQUENCE_STOP_REASON="stage 3 interview-gate exited ${GATE_RC}"
    fi
    if stage_may_continue; then
      # A CLOSED GATE EXITS ZERO and reports itself. It is a legitimate state
      # and it stops the sequence; it is never forced open.
      require_report_value "${PROOF}/${STAGE3_SLUG}.stdout" \
        "mechanical_path_unlocked" "true" \
        "the mechanical Claude path is CLOSED for this package" || true
    fi

    if ! stage_may_continue; then
      announce_stop
    else
      # --------------------------------------------------------------------
      # STAGE 4 — THE ONE EXECUTE
      # --------------------------------------------------------------------
      #
      # EXACTLY ONE outer execution of the controller. There is no retry here
      # and nothing reruns it. The controller owns everything inside it: the
      # GPT mechanical design specification, Claude's application of it, the
      # fresh GPT audit, and up to its own lifetime limit of correction rounds.
      run_controller_stage "$STAGE4_SLUG" "$STAGE4_CMD" "STAGE 4 — execute-next-claude-task"
      EXEC_RC="$STAGE_RC"
      # The last stage's own failure is a stop reason too, so the summary states
      # WHY the run ended rather than leaving a bare status to be interpreted.
      # The controller's own non-zero status is still what this launcher
      # returns; this only names it.
      if [ "$EXEC_RC" -ne 0 ] && [ -z "$SEQUENCE_STOP_REASON" ]; then
        SEQUENCE_STOP_REASON="stage 4 execute-next-claude-task exited ${EXEC_RC}"
      fi
    fi
  fi
fi

# The exit status this launcher will finally return for the controller portion
# of the run: the status of the LAST stage that actually ran. Every individual
# stage status is also written to its own file and printed in the summary, so no
# reader ever has to infer a stage's result from this single number.
#
# nh_loop.py defines exactly three exit codes -- 0, 1 and 2 -- so this value can
# never collide with the reserved safety codes 90-93 used below.
if   [ "$EXEC_RC"       != "NOT-RUN" ]; then SHADOW_RC="$EXEC_RC"
elif [ "$GATE_RC"       != "NOT-RUN" ]; then SHADOW_RC="$GATE_RC"
elif [ "$COVERAGE_RC"   != "NOT-RUN" ]; then SHADOW_RC="$COVERAGE_RC"
else                                          SHADOW_RC="$VALIDATION_RC"
fi

# ==========================================================================
# SECTION 11b — REPAIR-17 CONTINUATION V10 OBSERVATIONS
#               (READ-ONLY, DECIDES NOTHING)
# ==========================================================================
#
# A convenience pass over the lab's OWN captured output, so the behaviour of all
# four stages is easy to inspect without reading thousands of lines by hand.
#
# IT RECORDS; IT DECIDES NOTHING. It sets no verdict, it can fail no check, and
# every safety verdict below is computed exactly as it was in v5.
#
# NO PARTICULAR NATURAL OUTCOME IS REQUIRED. In particular:
#   - a validation that creates a genuine question for Ness is the interview
#     working, not a failure;
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
step "REPAIR-17 CONTINUATION V10 OBSERVATIONS"

observe_repair17_continuation_v10() {
  local out="${PROOF}/repair17-continuation-v10-observations.txt"
  local s1="${PROOF}/${STAGE1_SLUG}.stdout"
  local s2="${PROOF}/${STAGE2_SLUG}.stdout"
  local s3="${PROOF}/${STAGE3_SLUG}.stdout"
  local s4="${PROOF}/${STAGE4_SLUG}.stdout"
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
    printf 'REPAIR-17 CONTINUATION V10 OBSERVATIONS -- descriptive only, no verdict\n'
    printf '======================================================================\n\n'

    printf 'WHAT THIS RUN CONTINUED\n'
    printf '  continuation seed : %s\n' "$V9_CONTINUATION_SEED"
    printf '  seed journal      : %s events, sha256 %s\n' \
           "$EXP_SEED_JOURNAL_EVENTS" "$EXP_SEED_JOURNAL_SHA"
    printf '  seed journal head : sha256 %s\n' "$EXP_SEED_HEAD_SHA"
    printf '  last seed event   : %s, sha256 %s\n' \
           "$EXP_SEED_EVENT7_TYPE" "$EXP_SEED_EVENT7_SHA"
    printf '  routed signal     : %s\n' "$EXP_ROUTED_SIGNAL_ID"
    printf '  standing target   : %s\n' "$EXP_STANDING_TARGET_ID"
    printf '  route             : %s\n' "$EXP_SEED_EVENT7_ROUTE"
    printf '  signal source     : %s\n' "$EXP_SEED_EVENT7_SIGNAL_SOURCE"
    printf '  package scope     : %s\n' "$EXP_PKG_SCOPE"
    printf '\n'
    printf '  The whole seven-event chain and the journal head authenticated under\n'
    printf '  the controller\047s own digest, HMAC and head semantics before this run\n'
    printf '  began, and the seed was proved to still represent the current real\n'
    printf '  source apart from four classified differences.\n'
    printf '\n'
    printf '  THE ROUTED SIGNAL WAS NOT INTERPRETED BY THIS LAUNCHER. It was carried\n'
    printf '  in as the seed\047s last event and handed to the ordinary\n'
    printf '  question-validation stage. This launcher did not classify it, did not\n'
    printf '  convert it into a question, did not answer it, and did not decide\n'
    printf '  whether it is settled, mechanical, dependent or genuinely open.\n'
    printf '  Whatever stage 1 made of it is the controller\047s own result, recorded\n'
    printf '  verbatim below and in the stage files.\n\n'

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
    grep -E '"(ok|interview_stop_reason|validation_set_id|validation_pages_recorded|validation_pages_expected|validation_inventory_complete|deliverable_question_count|questions_total|stale_question_count|revalidation_required|routed_issues_awaiting_validation|codex_invoked|codex_invocations|codex_exit_code|expected_validation_page|continuing_validation_set_id|authenticated_revalidation_identity_used|authenticated_revalidation_package_scope_id|authenticated_revalidation_root_path|authenticated_revalidation_historical_validation_set_id|authenticated_identity_grants_no_clearance)":' \
         "$s1" 2>/dev/null | cut -c1-200 || true
    printf '\n'
    printf 'REPAIR 12/13/14: the authenticated package identity above names WHICH\n'
    printf 'package was revalidated. It is identity evidence only and grants no\n'
    printf 'clearance of any kind -- the controller states that itself in the\n'
    printf 'authenticated_identity_grants_no_clearance field.\n\n'

    printf '==========================================\n'
    printf 'STAGE 2 -- FRESH INDEPENDENT COVERAGE REVIEW\n'
    printf '==========================================\n'
    grep -E '"(ok|interview_stop_reason|coverage_review_invoked|coverage_review_exit_code|coverage_review_cleared|coverage_possible_gaps|coverage_validation_not_current|coverage_authenticated_root_used|coverage_validation_set_id|coverage_package_scope_id|coverage_scope_root_path|coverage_source_paths_checked|coverage_manifest_sha256|coverage_relevant_closure_paths|coverage_inventory_issue_count|coverage_binding_bytes)":' \
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
    grep -E '"(ok|interview_stop_reason|mechanical_path_unlocked|coverage_review_current|coverage_review_validation_set_id|validation_set_id|validation_inventory_complete|revalidation_required|open_group_index|stale_question_count|routed_issues_awaiting_validation)":' \
         "$s3" 2>/dev/null | cut -c1-200 || true
    printf '\n'

    printf '==========================================\n'
    printf 'STAGE 4 -- EXECUTE-NEXT-CLAUDE-TASK (one only)\n'
    printf '==========================================\n'
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
    printf 'CLAUDE MANDATORY SPECIFICATION STOP (Repair 11):\n'
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
    printf 'FRESH GPT CORRECTION-SPECIFICATION REVIEWS (per round, Repair 11):\n'
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
    printf '  this launcher sets neither.\n\n'

    printf 'THIS SECTION DECIDES NOTHING\n'
    printf '  It assigns no verdict, passes nothing and fails nothing. The only\n'
    printf '  verdicts this launcher holds are the containment and credential ones\n'
    printf '  in the RESULT block, and they are computed entirely separately.\n'
  } > "$out" 2>/dev/null || true

  note "repair-17 continuation v10 observations written to ${out}"
}
observe_repair17_continuation_v10 || true

# ==========================================================================
# SECTION 12 — RE-PROVE THE ORIGINAL, FROM OUTSIDE THE NAMESPACE
# ==========================================================================
#
# This runs REGARDLESS of how the four stages went -- whether stage 1 failed
# technically and stages 2, 3 and 4 never ran, whether a later stage declined to
# permit continuation, whether the gate stayed closed, or whether the controller
# ran to completion and returned any code at all. The ordinary success or
# failure of the controller has no bearing on whether the protected original
# must be re-proved. It always must.

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

# Both containment verdicts are SETTLED at this exact point, so the flag is
# raised here and not one line later.
#
# Everything below -- the host credential witness, the summary -- is separate
# and lesser. If any of it aborts unexpectedly, the report must still state the
# verdict this launcher genuinely holds. Raising the flag after those steps
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
printf 'N.H SHADOW REHEARSAL (v10, REPAIR-17 CONTINUATION) — RESULT\n'
printf '===========================================================\n'
printf 'SHADOW_LAB=%s\n'                     "$LAB"
printf 'FROZEN_CONTROLLER_SHA256=%s\n'       "$EXP_LOOP_SHA"
printf 'CONTINUATION_SEED=%s\n'              "$V9_CONTINUATION_SEED"
printf 'CONTINUATION_SEED_JOURNAL_EVENTS=%s\n' "$EXP_SEED_JOURNAL_EVENTS"
printf 'CONTINUATION_ROUTED_SIGNAL=%s\n'     "$EXP_ROUTED_SIGNAL_ID"
printf 'CONTINUATION_STANDING_TARGET=%s\n'   "$EXP_STANDING_TARGET_ID"
printf 'STAGE1_QUESTION_VALIDATION_EXIT=%s\n' "$VALIDATION_RC"
printf 'STAGE2_COVERAGE_REVIEW_EXIT=%s\n'    "$COVERAGE_RC"
printf 'STAGE3_INTERVIEW_GATE_EXIT=%s\n'     "$GATE_RC"
printf 'STAGE4_EXECUTE_EXIT=%s\n'            "$EXEC_RC"
printf 'SEQUENCE_STOP_REASON=%s\n'           "${SEQUENCE_STOP_REASON:-none}"
printf 'SHADOW_CONTROLLER_EXIT=%s\n'         "$SHADOW_RC"
printf 'ORIGINAL_WORKSPACE_PROOF=%s\n'       "$ORIGINAL_PROOF"
printf 'PRESERVED_LAB_PROOF=%s\n'            "$PRESERVED_LAB_PROOF"
printf 'HOST_CREDENTIAL_WITNESS=%s\n'        "$CREDENTIAL_WITNESS"
printf 'LAB_CREDENTIAL_SCAN=%s\n'            "$LAB_CREDENTIAL_SCAN"
for _slug in "${ALL_STAGE_SLUGS[@]}"; do
  printf 'STAGE_%s_STDOUT=%s\n' "$_slug" "${PROOF}/${_slug}.stdout"
  printf 'STAGE_%s_STDERR=%s\n' "$_slug" "${PROOF}/${_slug}.stderr"
done
unset _slug
printf 'REPAIR17_CONTINUATION_V10_OBSERVATIONS=%s\n' "${PROOF}/repair17-continuation-v10-observations.txt"
printf 'CONTINUATION_SEED_COMPATIBILITY=%s\n'      "${PROOF}/continuation-seed-compatibility.txt"
printf '===========================================================\n'

printf '\nSHADOW_CONTROLLER_EXIT is the status of the LAST stage that ran, and\n'
printf 'nothing more. Each stage has its own exit code above and its own\n'
printf 'exit-code file in the proof directory, so no stage result has to be\n'
printf 'inferred from that one number. NOT-RUN means the sequence stopped before\n'
printf 'that stage; it is not a pass and it is not a failure.\n'

printf '\nAN EXIT OF 0 IS NOT PERMISSION TO CONTINUE. A coverage review that\n'
printf 'finds possible gaps routes each one as a signal and exits 0; a CLOSED\n'
printf 'interview gate reports itself and exits 0. This launcher therefore reads\n'
printf 'the controller-owned fields, never the status alone, and SEQUENCE_STOP_REASON\n'
printf 'above states in plain words why the sequence ended where it did. Read the\n'
printf 'fields themselves in:\n'
printf '  %s\n' "${PROOF}/repair17-continuation-v10-observations.txt"

printf '\nA SEQUENCE THAT STOPPED EARLY IS A RESULT, NOT A FAILURE. An incomplete\n'
printf 'inventory, a material unknown, an open question for Ness, a coverage gap\n'
printf 'or a closed gate are all legitimate observations of the CURRENT shadow\n'
printf 'state. Nothing here was fixtured, seeded or forced to make a later stage\n'
printf 'run.\n'

if [ "$ORIGINAL_PROOF" = "FAIL" ]; then
  printf '\nThe protected ORIGINAL workspace changed during the rehearsal.\n'
  printf 'Isolation did not hold. See the DIFF.after.* files under:\n'
  printf '  %s\n' "$PROOF"
fi

if [ "$PRESERVED_LAB_PROOF" = "FAIL" ]; then
  printf '\nA PRESERVED earlier rehearsal lab changed during this run. That is\n'
  printf 'preserved evidence and it must never move. See the DIFF.after-labs.*\n'
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
printf '\n  THIS WAS A CONTINUATION, AND CONTINUATION CHANGES NONE OF THAT.\n'
printf '  The shadow was seeded from the preserved v9 shadow so the routed\n'
printf '  review signal recorded there would survive into a fresh\n'
printf '  question-validation. Nothing from that seed, and nothing this run\n'
printf '  produced, was written back to the real interview journal, head or key;\n'
printf '  no candidate produced here was promoted to real N.H; and the preserved\n'
printf '  v9 lab was read only -- to be copied and to be authenticated -- and is\n'
printf '  covered by PRESERVED_LAB_PROOF above like every other preserved lab.\n'
printf '\n  This launcher decided nothing about what the routed signal means. It\n'
printf '  made no classification and no disposition. Only the controller\047s own\n'
printf '  question-validation may ever do that, and only Ness may answer a\n'
printf '  question it admits.\n'
printf '\n  The lab holds a copy of the N.H interview authenticity key.\n'
printf '  Delete the lab once the rehearsal has been reviewed.\n'
printf '\n  LAB_CREDENTIAL_SCAN is a SHAPE scan, not proof of absence.\n'
printf '  NO-KNOWN-MARKERS means only that no known credential marker was\n'
printf '  found in readable, uncompressed lab content. It cannot see a token\n'
printf '  in an unrecognised shape, and it cannot see into compressed or\n'
printf '  encoded data. Treat the lab as sensitive regardless of this line.\n\n'

# Fail closed: a protected-original mismatch outranks any apparent shadow
# success, and a preserved-evidence mismatch outranks it too. All four safety
# verdicts use reserved codes the controller never returns, so a containment
# failure can never be mistaken for an ordinary controller exit, and an ordinary
# controller exit can never be mistaken for a containment failure.
if [ "$ORIGINAL_PROOF" = "FAIL" ]; then
  exit "$RC_ORIGINAL_PROOF_FAIL"
fi
if [ "$PRESERVED_LAB_PROOF" = "FAIL" ]; then
  exit "$RC_PRESERVED_LAB_PROOF_FAIL"
fi
# Anything other than a completed marker sweep fails closed: FOUND means
# material is there, SCAN-FAILED means nothing is known, and neither may pass.
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
# the sequence still stopped: an incomplete inventory, a material unknown, an
# open question, a coverage gap or a closed gate. That is not success and must
# not be reported as one, so it gets its own status.
if [ -n "$SEQUENCE_STOP_REASON" ]; then
  exit "$RC_SEQUENCE_STOPPED"
fi

# All four stages ran, the execute returned 0, and every safety verdict passed.
exit 0

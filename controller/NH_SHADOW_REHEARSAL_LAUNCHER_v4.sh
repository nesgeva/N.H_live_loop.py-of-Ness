#!/usr/bin/env bash
#
# NH_SHADOW_REHEARSAL_LAUNCHER_v4.sh
#
# N.H SHADOW LIVE REHEARSAL LAUNCHER — v4  (REPAIR-10 CONTROLLER)
#
# WHAT THIS IS
#   A disposable-laboratory launcher. It proves the protected original N.H /
#   controller workspace has not moved, makes an exact throwaway shadow copy of
#   it, hides the real /home/ness behind a tmpfs, republishes the shadow at the
#   EXACT normal path /home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP inside a Bubblewrap
#   namespace, runs EXACTLY ONE real
#
#       python3 nh_loop.py execute-next-claude-task
#
#   inside that namespace, and then re-proves the protected original from
#   OUTSIDE the namespace.
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
#   Bubblewrap namespace. It says NOTHING about the sandboxed controller run.
#   Whether that run stayed contained is not asserted here; it is settled only
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
#   easy to get wrong -- this file previously carried one that omitted wc, grep,
#   the shell's own `exec N<` redirections and, worse, flock. The claim is about
#   operations, not binaries. Three operations against protected paths are not
#   plain content reads, and all three are deliberate:
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
#   24 hours old. Measured while this launcher was written: 0 of the preserved
#   lab's 261 files were due for such a refresh, but a run a day later would
#   refresh all of them. That is a real, if minimal, metadata effect on
#   preserved evidence, and it is not hidden here. atime is captured in NO proof
#   this launcher takes, so a refresh can never move a verdict in either
#   direction; ctime does not move with atime, and ctime IS captured.
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
#   2. NH_DECISION_DEFAULTS-S19_v2_2.md
#   3. cursorrules
#   4. NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md
#   Ness owns meaning, policy, acceptance, adoption and permission to build.
#
# ==========================================================================
# WHAT v4 IS, AND WHAT IT CHANGES
# ==========================================================================
#
#   v4 IS A REBASE OF v3, NOT A REDESIGN.
#   It starts from the exact bytes of NH_SHADOW_REHEARSAL_LAUNCHER_v3.sh
#   (sha256 499b0a60..., 102494 bytes, 2026 lines) and changes ONLY what the
#   Repair-10 controller mechanically requires. Every isolation guarantee and
#   every proof v1/v2/v3 earned is carried forward unchanged; the v3 and v2
#   histories below are retained deliberately so none of it can be lost.
#
#   v1, v2 and v3 are all preserved on disk. None is edited, renamed or
#   deleted, and this launcher gates on ALL THREE still being byte-identical.
#
#   WHAT v4 CHANGES FROM v3, AND ONLY THIS:
#     - the frozen controller identity, to the Repair-10 controller;
#     - v3's own identity is now frozen and gated, as v1's and v2's already are;
#     - v4 itself now exists in controller/, so the exact expected controller
#       worktree gains one more entry -- still an EXACT match, never "anything
#       untracked is acceptable";
#     - a fresh disposable lab path keyed to the Repair-10 controller;
#     - the shadow marker token, keyed to the Repair-10 controller;
#     - the Repair-9 lab is named as preserved evidence alongside the v1 lab;
#     - a post-run, read-only OBSERVATIONS pass over the lab's own captured
#       output, so the Repair-10 behaviours are easy to inspect. It records; it
#       decides nothing and it can fail no verdict.
#   Nothing else. No isolation change, no proof weakened, no new machinery.
#
#   1. FROZEN CONTROLLER IDENTITY IS THE REPAIR-10 ONE.
#      nh_loop.py is now
#        sha256 704ad177f1ec25a33f1fe026a94429dad96d65c62030737cb4cfc23d1e28be6f
#        bytes  1447775
#        lines  31873
#      Repair 10 gives ONE Claude session per package execution, resumes that
#      exact session on later correction rounds, pins claude-opus-5, grants
#      Edit, and seeds the next-version candidate. The OpenAI reasoning role is
#      gpt-5.6-sol at effort HIGH, invoked through the existing read-only,
#      ephemeral Codex CLI transport; Claude stays at xhigh. None of that is
#      simulated here -- the real controller decides what happens.
#
#   2. THE CLAUDE SESSION STORE MUST SURVIVE THE WHOLE NAMESPACE.
#      Repair 10 needs several Claude invocations inside the ONE controller
#      execution to reach the SAME Claude Code session. That already works
#      under v3's design and is preserved exactly: CLAUDE_CONFIG_DIR points at
#      the anonymous copy-on-write overlay on ${HOME_REAL}/.claude, there is
#      exactly ONE bwrap namespace holding exactly ONE controller process, and
#      the overlay's tmpfs upper layer lives for the lifetime of that
#      namespace. Session transcripts written by the first Claude invocation are
#      therefore visible to a later --resume, and every one of them is discarded
#      with the namespace. The host ~/.claude is never reachable or writable.
#
#   3. A RESUMED CLAUDE CALL IS NOT REQUIRED FOR SUCCESS.
#      If the candidate reaches PASS on its first audit there is no second
#      correction round and so nothing to resume. That is a legitimate outcome
#      and this launcher does NOT fail on it. The observations pass records
#      which of the two happened; it never forces either.
#
#   THE HISTORY BELOW IS v3's AND v2's, retained in full.
#
#   v3 IS A REBASE, NOT A REDESIGN.
#   It starts from the exact bytes of NH_SHADOW_REHEARSAL_LAUNCHER_v2.sh
#   (sha256 bb97ac49..., 99298 bytes, 1978 lines) and changes ONLY what the
#   closed Repair 9 controller mechanically requires. Every hardening v2
#   earned -- and it earned a lot, across several review rounds -- is carried
#   forward unchanged and is listed in the v2 history below, which is retained
#   deliberately so none of it can be quietly lost in a later rebase.
#
#   v1 and v2 are both preserved on disk. Neither is edited, renamed, deleted
#   or superseded by this file, and this launcher gates on BOTH still being
#   byte-identical. v2 is now historical validation evidence: it was hardened
#   and closed against the PRE-Repair-9 controller, and it is superseded only
#   in the sense that the controller it was frozen to no longer exists.
#
#   WHAT v3 CHANGES FROM v2, AND ONLY THIS:
#     - the frozen controller identity, to the closed Repair 9 controller;
#     - v2's own identity is now frozen and gated, as v1's already was;
#     - v3 itself now exists in controller/, so the exact expected controller
#       worktree gains one more entry -- it is still an EXACT six-entry match,
#       never "anything untracked is acceptable";
#     - a fresh disposable lab path keyed to the Repair 9 controller;
#     - the shadow marker token, keyed to the Repair 9 controller;
#     - every protected-state identity re-read from disk rather than inherited.
#   Nothing else. No isolation change, no proof weakened, no new machinery.
#
#   1. FROZEN CONTROLLER IDENTITY IS THE CLOSED REPAIR-9 ONE.
#      Repair 9 is closed. nh_loop.py is now
#        sha256 acc8dee2c3ae0a27738fc1c1b4b08bb30bb55243d8ce9c22c393c6505e798690
#        bytes  1382464
#        lines  30473
#      Repair 9 made the ordinary package audit CURRENT_PACKAGE_ONLY and
#      deferred whole-system wiring to the final Bundle 8 stage. Those prompts
#      are exercised naturally by this rehearsal; nothing here simulates them.
#      v2's frozen controller identity (a52d383f..., 1367891 bytes, 30243
#      lines) is the pre-Repair-9 controller and is deliberately not accepted.
#      v1's (13ef2b13...) is older still and likewise not accepted.
#
#   THE HISTORY BELOW IS v2's. It records defects already found and fixed, and
#   is kept so a future rebase cannot reintroduce them.
#
#   2. EVERY OTHER FROZEN VALUE WAS RE-READ FROM DISK, NOT INHERITED.
#      Controller and N.H Git state, the three v1.0/v1.1/v1.2 candidates, the
#      interview journal, journal head, authenticity-key identity and the
#      authenticated package scope were all re-derived from the live workspace
#      when this file was written. They happen to be unchanged since v1, and
#      that is a re-verified fact here, not an assumption carried over.
#
#   3. THE CONTROLLER-WORKTREE PROOF IS STRICTER, NOT WEAKER.
#      v1 filtered its own basename out of `git status` with a grep and then
#      compared the remainder. Two launcher files now exist in controller/, and
#      the weak fix would have been to filter two lines instead of one. That
#      form also passes when a launcher is MISSING, because it only subtracts.
#      v2 instead asserts the COMPLETE porcelain status is EXACTLY the three
#      expected lines: the modified nh_loop.py plus both launcher artifacts.
#      Nothing is filtered, no untracked path is ignored, an absent launcher
#      fails, and any fourth entry of any kind fails.
#
#   4. A NEW DISPOSABLE LAB PATH, AND THE FIRST REHEARSAL IS PRESERVED.
#      The v1 lab
#        /home/ness/NH_AICP_SHADOW_REHEARSAL_ce3a38f43f287a56bd635ed836edf002a2db50a7
#      is preserved evidence. It is never reused and never deleted by this
#      launcher, and it is read-only to it in the exact sense set out under
#      READ-ONLY, STATED EXACTLY above -- no create, write, truncate, rename,
#      chmod, chown or delete, with an atime refresh the one effect a read can
#      have. It is additionally carried in the before / during / after proof set
#      as a hash-and-metadata witness, so any change to its content or to any
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
#      and no Git or GitHub write anywhere. Bubblewrap 0.11.1 on this host
#      establishes that model with no incompatibility, so nothing is relaxed.
#
#   6. THE NEW PREPARATION CONTRACT IS TESTED NATURALLY.
#      Repair 8 makes not_ready_reason a required, bounded field of the Codex
#      preparation result. This launcher does NOT fake it, inject it,
#      pre-answer it or steer it in any way. It sets no controller-behaviour
#      environment variable: --clearenv wipes the environment and only
#      NH_LOOP_INTERVIEW_STATE_DIR is set back, pointing at the shadow's own
#      interview state. The isolation self-test asserts that the complete set
#      of NH_-prefixed variables inside the namespace is exactly what this
#      launcher set, so nothing can pre-answer the contract from the outside.
#      If the real Codex preparation does not return the required field
#      correctly, the controller fails closed on its own and the evidence is
#      preserved in the lab. That outcome is a legitimate result of this
#      rehearsal, not a launcher fault.
#
#   7. THE SAFETY VERDICTS HAVE RESERVED EXIT CODES.
#      v1 exited 2 for a protected-original failure and 3 for a changed
#      credential witness, both of which a controller run can also return on
#      its own, so an automated reader could not tell a containment failure
#      from an ordinary controller exit. v2 reserves 90 through 93 -- values
#      the controller never returns -- for its four safety verdicts, and
#      otherwise returns the controller's exit code verbatim. The override
#      itself is unchanged: a protected-original mismatch still outranks any
#      apparent shadow success. Each verdict is computed from its own proof
#      set and reported under its own name, so no one verdict can stand in for
#      another.
#
#   8. CORRECTIONS FROM THE INDEPENDENT REVIEW OF THIS FILE.
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
#          runs/, logs/ or cache/ paths either. It now uses --ignored=matching
#          and freezes the complete five-entry set. (section 4)
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
#      real run, capturing PIPESTATUS, then recording the failure. Re-verified:
#      the same unreadable file now yields CREDENTIAL_WITNESS=CAPTURE-FAILED
#      with the failing statuses recorded, and the launcher stays alive to
#      report it.
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
#      Every one of those claims has been replaced by the exact operation-level
#      statement in READ-ONLY, STATED EXACTLY at the top of this file, and the
#      two runtime report strings now say precisely what is and is not issued
#      against those paths. The claims that remain -- no create, write,
#      truncate, rename, chmod, chown or delete, never reused, never deleted --
#      were re-verified against the source by enumerating every mutating
#      command in the file: all of them target the lab, the shadow, or the
#      in-namespace overlay, and PRESERVED_LAB_V1 appears only in a readonly
#      assignment, a printf and a comparison.
#
#  13. THE REPLACEMENT GUARANTEE WAS ITSELF STILL INACCURATE.
#      The first READ-ONLY, STATED EXACTLY block fixed the absolute claims but
#      introduced a new false one: it asserted the protected paths are opened
#      "only through find, sha256sum, stat, diff, git rev-parse / status and the
#      rsync SOURCE side". That closed enumeration is wrong three ways. It omits
#      `wc -l < nh_loop.py` and the `grep -c` counts over the journal; it omits
#      the shell's own `exec 200<` / `exec 201<` opens; and most seriously it
#      omits flock(2), which is not a read at all -- section 6 takes an
#      EXCLUSIVE advisory lock on two files inside the protected original. It
#      also listed diff, which is only ever run against proof files inside the
#      lab. And it made a blanket statement with no carve-out for the sandboxed
#      run, contradicting this file's own discipline that containment is
#      UNVERIFIED until the after-proof completes.
#      The block now states the property rather than a list of binaries, names
#      all three operations that are not plain content reads (the advisory
#      locks, the namespace-private bind mount, and atime), and scopes itself
#      explicitly to this launcher's own code outside the namespace. A closed
#      list of "safe tools" was not repaired but removed: it is exactly the kind
#      of claim that is easy to write and easy to get wrong.
#
#  14. THE CORRECTED GUARANTEE CONTRADICTED THE LAUNCHER'S OWN RUNTIME REPORT.
#      Fixing the header left report_state still printing, of the protected
#      original, "it opens it only for reading" -- the very sentence item 13
#      had just deleted from the header for being false, and now the line an
#      operator actually sees at the moment a run blocks. The two also listed
#      different operation sets, so the file contradicted itself about its own
#      central safety claim.
#      report_state now states the same operation set as the header, and says
#      what actually happened to the two advisory locks, gated on new
#      LOCKS_TAKEN / LOCKS_HELD flags in the same style as LAB_CREATED and
#      RUN_STARTED -- because most failure paths never reach section 6, and a
#      design-level sentence about locks would be false on every one of them.
#      Verified on this host that the sentence those flags print is itself true:
#      taking and releasing an advisory lock leaves mode, uid, gid, size, mtime,
#      ctime, inode and link count byte-identical.
#      The preserved-lab sentence keeps "opened only for reading" because there
#      it IS accurate: the two locks are taken on interview-state files inside
#      the protected original, never on a preserved lab.
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
#      decremented as each descriptor closes. All five states were exercised:
#      before any lock, both held, both released, second lock contended
#      (now "1 of 2 taken, 1 STILL HELD"), and first lock contended (correctly
#      still "No lock was taken").
#
#  16. THE CREDENTIAL METADATA CAPTURE HAD THE FAULT ALREADY FIXED NEXT DOOR.
#      Item 11 rebuilt the credential HASH pipeline but left the credential
#      METADATA pipeline as `{ ... find ... || true ... } | sort`, carrying both
#      of the same defects. `|| true` erased every non-zero find status, so a
#      find killed by a signal -- which writes no stderr of its own -- left a
#      partial stream with credentials.errors empty; truncated identically
#      before and after, the captures compare EQUAL and read as UNCHANGED. And
#      a failing sort in that pipeline was still exposed to set -e + pipefail
#      and could kill the launcher before the CAPTURE-FAILED verdict existed.
#      Rebuilt through a raw file with every status checked and recorded. No
#      group-pipeline remains anywhere in capture_original_proof, so pipefail
#      cannot reach any capture. Verified: an unreadable directory now leaves
#      the launcher alive and yields CAPTURE-FAILED.
#
# THE LAB CONTAINS A COPY OF THE N.H INTERVIEW AUTHENTICITY KEY.
#   The controller cannot append authenticated journal events without it, so the
#   shadow copy of nh_interview_state/ necessarily includes it. The lab is
#   created mode 0700. Delete the lab when the rehearsal has been reviewed.
#   No MODEL login material is ever copied into the lab.
#
# USAGE
#   bash /home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/controller/NH_SHADOW_REHEARSAL_LAUNCHER_v4.sh
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

# Both launcher files live in controller/. Both are accounted for explicitly.
readonly LAUNCHER_V1_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v1.sh"
readonly LAUNCHER_V2_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v2.sh"
readonly LAUNCHER_V3_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v3.sh"
readonly LAUNCHER_V4_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v4.sh"

# v1 and v2 are BOTH preserved unchanged, and both are frozen here so this
# launcher fails closed if either moved. v2 is now historical validation
# evidence in its own right: it was hardened and closed against the PRE-Repair-9
# controller, and v3 exists precisely because that controller identity changed.
readonly EXP_LAUNCHER_V1_SHA="99fb0ad912b8af79a34217099c3585cee17b9011d09a2fe58071257000f10d7c"
readonly EXP_LAUNCHER_V1_BYTES="40897"
readonly EXP_LAUNCHER_V2_SHA="bb97ac49fb45f7647ee4ff2dc7a8fe21331113108ca915f1209acab7a5b70cf3"
readonly EXP_LAUNCHER_V2_BYTES="99298"
readonly EXP_LAUNCHER_V3_SHA="499b0a60c4a5b67d631e793e4f3dacb2cd3191fa07bb27e71f41e1b1da91d9b4"
readonly EXP_LAUNCHER_V3_BYTES="102494"

# --- controller: THE REPAIR-10 IDENTITY ---
readonly EXP_LOOP_SHA="704ad177f1ec25a33f1fe026a94429dad96d65c62030737cb4cfc23d1e28be6f"
readonly EXP_LOOP_BYTES="1447775"
readonly EXP_LOOP_LINES="31873"
readonly EXP_CTRL_BRANCH="main"
readonly EXP_CTRL_HEAD="db46a51967b1af1aa873bc0c0e847a0a95221bdf"

# --- N.H ---
readonly EXP_NH_BRANCH="nh-design-loop"
readonly EXP_NH_HEAD="ce3a38f43f287a56bd635ed836edf002a2db50a7"

readonly CAND_V10="NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_0_CANDIDATE.md"
readonly CAND_V11="NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_1_CANDIDATE.md"
readonly CAND_V12="NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_2_CANDIDATE.md"

readonly EXP_V10_SHA="e6ee27fcd33f49a276de7753334cb18dd5d7d1f4d11a25d8b86dd236bfeebe3c"
readonly EXP_V10_BYTES="51315"
readonly EXP_V11_SHA="964b6dbd0a16756d65d5a6e185298eb554d6475d9da3826266b7571c8a7d8cbd"
readonly EXP_V11_BYTES="73685"
readonly EXP_V12_SHA="2245ae26ebf4b833ca36c798f82f543d807f281136e388f0f4204982c9a3cb55"
readonly EXP_V12_BYTES="109986"

# --- interview state (identities only; the key's CONTENTS are never read) ---
readonly EXP_JOURNAL_SHA="39c6af157222df10203d426e06ab323bb222041aa7b0838f1130f0518aef9945"
readonly EXP_JOURNAL_BYTES="15604"
readonly EXP_JOURNAL_EVENTS="5"
readonly EXP_HEAD_SHA="b55e8b3f5916445db84a4fc9e6d342113b8a538ba20fe5c20dc94f7c7a42cf90"
readonly EXP_KEY_SHA="6a129d96ed1af2e5f7c890821c8fddd27c7e4b368847884274712e126bf797d7"
readonly EXP_PKG_SCOPE="nullpkg_1ffc9ec7aae12b75ef50400da674812f"
readonly EXP_PKG_SCOPE_OCCURRENCES="5"

readonly JOURNAL="${STATE}/nh_interview_journal.jsonl"
readonly JOURNAL_HEAD="${STATE}/nh_interview_journal.head"
readonly AUTH_KEY="${STATE}/nh_interview_authenticity.key"
readonly LOCK_TXN="${STATE}/nh_candidate_transaction.lock"
readonly LOCK_JOURNAL="${STATE}/nh_interview_journal.lock"

# --- lab: NEW, keyed to the repaired controller identity ---
readonly LAB="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR10_704ad177f1ec25a33f1fe026a94429dad96d65c62030737cb4cfc23d1e28be6f"

# The v1 rehearsal's lab. PRESERVED EVIDENCE. This constant exists so the
# launcher can refuse to collide with it and can witness that it did not move.
# It appears nowhere in this file in a write position: it is only ever compared
# against, and read by `find` / `sha256sum` through the preserved-lab witness.
#
# This path is READ-ONLY in the exact sense defined under READ-ONLY, STATED
# EXACTLY in the file header: no create, write, truncate, rename, chmod, chown
# or delete is ever issued against it, and the one effect a read can have is an
# atime refresh, which no proof captures. The same applies to the protected
# workspace, which must also be read to be hashed and copied.
readonly PRESERVED_LAB_V1="/home/ness/NH_AICP_SHADOW_REHEARSAL_ce3a38f43f287a56bd635ed836edf002a2db50a7"

# The Repair-9 rehearsal lab. ALSO PRESERVED EVIDENCE, on exactly the same
# terms as the v1 lab above: never reused, never deleted, read-only in the
# sense defined in the header, and carried in the preserved-lab witness set
# by the glob below so any change to it fails this run closed.
readonly PRESERVED_LAB_REPAIR9="/home/ness/NH_AICP_SHADOW_REHEARSAL_REPAIR9_acc8dee2c3ae0a27738fc1c1b4b08bb30bb55243d8ce9c22c393c6505e798690"

readonly SHADOW_WS="${LAB}/shadow/NH_CLAUDE_CODEX_DESIGN_LOOP"
readonly RUNTIME_TMP="${LAB}/runtime/tmp"
readonly PROOF="${LAB}/proof"
readonly SHADOW_MARKER_NAME=".nh_shadow_marker"

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

# Proof artefacts of the PROTECTED ORIGINAL that MUST be byte-identical before
# and after.
readonly PROTECTED_PROOF_FILES=(
  "nh_loop.identity"
  "launchers.identity"
  "controller.git"
  "governance.git"
  "candidates.sha256"
  "interview_state.sha256"
  "interview_state.meta"
  "journal.counts"
  "workspace.files.sha256"
  "workspace.meta"
)

# Proof artefacts of PRESERVED EARLIER REHEARSAL LABS, including the v1 lab.
# Kept as their own set, with their own verdict and their own reserved exit
# code, so a preserved-evidence failure is never reported as, or hidden behind,
# a protected-workspace verdict.
readonly PRESERVED_LAB_PROOF_FILES=(
  "preserved_labs.sha256"
  "preserved_labs.meta"
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
# RUN_STARTED : the isolated controller run was entered, so no report may say
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
# merely because the launcher's own code does not write to it: once the
# sandboxed run has been entered, containment is a claim about the ISOLATION,
# and only the completed AFTER proof can settle it.
report_state() {
  # --- what actually ran ---
  if [ "$RUN_STARTED" = "1" ]; then
    printf 'The isolated controller run WAS entered, so real Codex / Claude\n' >&2
    printf 'provider calls may already have been made.\n' >&2
  else
    printf 'No isolated controller run was started.\n' >&2
    printf 'No model or provider call was made.\n' >&2
  fi

  # --- what can honestly be said about the protected original ---
  if [ "$AFTER_PROOF_DONE" = "1" ]; then
    printf 'The protected original WAS re-proved after the run: %s\n' "$ORIGINAL_PROOF" >&2
  elif [ "$RUN_STARTED" = "1" ]; then
    printf 'The protected original has NOT been re-proved. This launcher issued\n' >&2
    printf 'no create, write, append, truncate, rename, link, unlink, chmod, chown\n' >&2
    printf 'or utimes against it, but a sandboxed run was entered and whether that\n' >&2
    printf 'run stayed contained is UNVERIFIED. Do not assume the original is\n' >&2
    printf 'untouched -- re-verify it by hand before drawing any conclusion.\n' >&2
  else
    printf 'This launcher issued no create, write, append, truncate, rename, link,\n' >&2
    printf 'unlink, chmod, chown or utimes against the protected original.\n' >&2
    printf 'No sandboxed run was entered.\n' >&2
  fi

  # The advisory locks are the one non-read operation this launcher performs
  # against the protected original, so the report states exactly what happened
  # to them rather than claiming the original was "only read". Gated on the
  # flags, because most failure paths never reach section 6 at all.
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

  # --- the preserved v1 rehearsal ---
  # Deliberately NOT "never modified": reading it can refresh atime on this
  # relatime filesystem. See READ-ONLY, STATED EXACTLY in the file header.
  printf '\nThe preserved v1 rehearsal lab is never reused and never deleted by\n' >&2
  printf 'this launcher on any path. It is opened only for reading, to witness\n' >&2
  printf 'it; that can refresh atime, which no proof captures, and changes\n' >&2
  printf 'nothing else about it:\n' >&2
  printf '  %s\n' "$PRESERVED_LAB_V1" >&2
  if [ "$AFTER_PROOF_DONE" = "1" ]; then
    printf 'It was re-witnessed after the run: %s\n' "$PRESERVED_LAB_PROOF" >&2
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
# An ERR trap fires even under `set +e`, so it would hijack the two places where
# a non-zero exit is EXPECTED and handled on purpose: the isolation self-test,
# and above all the one real controller run, whose non-zero exit is an ordinary
# outcome this launcher exists to record. An ERR trap there would abort before
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

  # --- both launcher artefacts: v1 must stay byte-identical, and this file
  #     must stay byte-identical to itself across the run ---
  {
    local lf
    for lf in "$LAUNCHER_V1_BASENAME" "$LAUNCHER_V2_BASENAME" \
              "$LAUNCHER_V3_BASENAME" "$LAUNCHER_V4_BASENAME"; do
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

  # --- the three candidates ---
  {
    local c
    for c in "$CAND_V10" "$CAND_V11" "$CAND_V12"; do
      printf '%s %s %s\n' "$(sha_of "${CAND_DIR}/${c}")" "$(bytes_of "${CAND_DIR}/${c}")" "$c"
    done
  } > "${out}/candidates.sha256"

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
  # Every earlier shadow-rehearsal lab, including the v1 lab, is preserved
  # evidence. This launcher's own lab is excluded because it is being written
  # by design. If any preserved lab changes at all between before and after,
  # the comparison fails and this run fails closed.
  #
  # A preserved lab is NOT required to exist: v1's own report instructs Ness to
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
    # the one real run.
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
  #    be recognised. Verified against a realistic 224-file lab copy: these
  #    markers produce no false positive, and they catch a bare JWT.
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
  #
  #    Verified on this host against a realistic 225-file lab that includes the
  #    git object stores, python bytecode and the captured stdout of the real v1
  #    rehearsal: zero false positives, while classic, service-account,
  #    Anthropic and project keys, both OAuth field spellings, private keys and
  #    bare JWTs are all caught, and the pattern does not match its own source.
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

for c in sha256sum stat find sort xargs diff rsync flock git awk grep wc mkdir; do
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
[ -d "$HOST_CODEX" ]  || die "host .codex missing; the copy-on-write credential overlay cannot be built"
[ -d "$HOST_CLAUDE" ] || die "host .claude missing; the copy-on-write credential overlay cannot be built"
[ -f "$HOST_CLAUDE_JSON" ] || die "host .claude.json missing; the client cannot start inside the namespace"

# The v1 rehearsal is preserved evidence and this run must not collide with it.
for _plab in "$PRESERVED_LAB_V1" "$PRESERVED_LAB_REPAIR9"; do
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

  # v3 is this file's DIRECT PREDECESSOR and is preserved evidence in its own
  # right, so it is now gated by identity exactly like v1 and v2.
  [ -f "${CTRL}/${LAUNCHER_V3_BASENAME}" ] \
    || die "launcher v3 is missing from ${CTRL}; it is preserved evidence and must be present"
  expect "launcher v3 sha256" "$(sha_of "${CTRL}/${LAUNCHER_V3_BASENAME}")"   "$EXP_LAUNCHER_V3_SHA"
  expect "launcher v3 bytes"  "$(bytes_of "${CTRL}/${LAUNCHER_V3_BASENAME}")" "$EXP_LAUNCHER_V3_BYTES"

  # Launcher v4 is THIS file. It cannot hash-gate on itself, but it must be the
  # file that is present, and it is carried in the before/after proof set so any
  # change to it during the run is caught.
  [ -s "${CTRL}/${LAUNCHER_V4_BASENAME}" ] \
    || die "launcher v4 is missing or empty at ${CTRL}/${LAUNCHER_V4_BASENAME}"
  note "all four launcher artefacts present in ${CTRL}"

  expect "controller branch"  "$(git_ro "$CTRL" rev-parse --abbrev-ref HEAD)" "$EXP_CTRL_BRANCH"
  expect "controller HEAD"    "$(git_ro "$CTRL" rev-parse HEAD)"              "$EXP_CTRL_HEAD"

  # The controller worktree must be EXACTLY these five entries and nothing else:
  # the modified nh_loop.py, the two launcher artefacts, and the two gitignored
  # editor/build FILES. Nothing is filtered out.
  #
  # The --ignored mode is load-bearing, and traditional is the only sufficient
  # one. Plain --untracked-files=all omits every gitignored path, so a gate
  # built on it would NOT have seen .claude/settings.local.json or the
  # __pycache__ bytecode, and would equally not have seen anything dropped into
  # the gitignored state/, runs/, logs/ or cache/ paths this repository also
  # ignores. --ignored=matching would have seen the directories but COLLAPSED
  # them: measured on this host, a probe file dropped into __pycache__/ leaves
  # `!! __pycache__/` byte-identical, so arbitrary ignored children would pass
  # the gate and be copied into the shadow. traditional lists every ignored file
  # individually, so the gate freezes the real, complete set.
  #
  # This is deliberately strict. If the bytecode file is ever regenerated under
  # a different interpreter version this gate stops the run, which is the
  # correct behaviour for a launcher frozen to one exact moment: it fails
  # closed and the identity is re-frozen deliberately.
  local ctrl_status ctrl_status_expected
  ctrl_status="$(
    git_ro "$CTRL" status --porcelain=v1 --untracked-files=all --ignored=traditional \
      | LC_ALL=C sort
  )"
  ctrl_status_expected="$(
    printf '%s\n' \
      " M nh_loop.py" \
      "!! .claude/settings.local.json" \
      "!! __pycache__/nh_loop.cpython-314.pyc" \
      "?? ${LAUNCHER_V1_BASENAME}" \
      "?? ${LAUNCHER_V2_BASENAME}" \
      "?? ${LAUNCHER_V3_BASENAME}" \
      "?? ${LAUNCHER_V4_BASENAME}" | LC_ALL=C sort
  )"
  expect "controller worktree" "$ctrl_status" "$ctrl_status_expected"

  expect "N.H branch"         "$(git_ro "$NHGOV" rev-parse --abbrev-ref HEAD)" "$EXP_NH_BRANCH"
  expect "N.H HEAD"           "$(git_ro "$NHGOV" rev-parse HEAD)"              "$EXP_NH_HEAD"

  local nh_status nh_status_expected
  nh_status="$(
    git_ro "$NHGOV" status --porcelain=v1 --untracked-files=all --ignored=traditional \
      | LC_ALL=C sort
  )"
  nh_status_expected="$(
    printf '%s\n' \
      "?? 05_ACTIVE_CANDIDATE/${CAND_V10}" \
      "?? 05_ACTIVE_CANDIDATE/${CAND_V11}" \
      "?? 05_ACTIVE_CANDIDATE/${CAND_V12}" | LC_ALL=C sort
  )"
  expect "N.H worktree" "$nh_status" "$nh_status_expected"

  expect "candidate v1.0 sha256" "$(sha_of "${CAND_DIR}/${CAND_V10}")"   "$EXP_V10_SHA"
  expect "candidate v1.0 bytes"  "$(bytes_of "${CAND_DIR}/${CAND_V10}")" "$EXP_V10_BYTES"
  expect "candidate v1.1 sha256" "$(sha_of "${CAND_DIR}/${CAND_V11}")"   "$EXP_V11_SHA"
  expect "candidate v1.1 bytes"  "$(bytes_of "${CAND_DIR}/${CAND_V11}")" "$EXP_V11_BYTES"
  expect "candidate v1.2 sha256" "$(sha_of "${CAND_DIR}/${CAND_V12}")"   "$EXP_V12_SHA"
  expect "candidate v1.2 bytes"  "$(bytes_of "${CAND_DIR}/${CAND_V12}")" "$EXP_V12_BYTES"

  expect "journal sha256"  "$(sha_of "$JOURNAL")"          "$EXP_JOURNAL_SHA"
  expect "journal bytes"   "$(bytes_of "$JOURNAL")"        "$EXP_JOURNAL_BYTES"
  expect "journal events"  "$(grep -c '[^[:space:]]' -- "$JOURNAL" || true)" "$EXP_JOURNAL_EVENTS"
  expect "journal head sha256"     "$(sha_of "$JOURNAL_HEAD")" "$EXP_HEAD_SHA"
  expect "authenticity key sha256" "$(sha_of "$AUTH_KEY")"    "$EXP_KEY_SHA"
  expect "authenticated package scope occurrences" \
         "$(grep -c -F -- "$EXP_PKG_SCOPE" "$JOURNAL" || true)" "$EXP_PKG_SCOPE_OCCURRENCES"

  [ -f "$LOCK_TXN" ]     || die "candidate-transaction lock file missing: ${LOCK_TXN}"
  [ -f "$LOCK_JOURNAL" ] || die "interview-journal lock file missing: ${LOCK_JOURNAL}"

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

# The two live-output files are created EMPTY here, so the watch command
# printed below actually works the moment it is offered. Without this they do
# not exist until the redirect in section 11 creates them, and `tail -f` on a
# missing file exits immediately with "no files remaining" -- guidance that
# looks helpful and cannot be followed. Section 11 truncates and rewrites both
# through its own redirect exactly as before; nothing downstream changes.
: > "${PROOF}/shadow-run.stdout"
: > "${PROOF}/shadow-run.stderr"
chmod 0600 "${PROOF}/shadow-run.stdout" "${PROOF}/shadow-run.stderr"
note "lab created atomically (mode 0700): ${LAB}"
say  "        NOTE: the lab will contain a copy of the N.H interview authenticity"
say  "        key, because the controller cannot append authenticated journal"
say  "        events without it. Delete the lab after review."
say  ""
say  "        TO WATCH THIS RUN LIVE, from another terminal, run exactly:"
say  ""
say  "          tail -F ${PROOF}/shadow-run.stderr"
say  ""
say  "        Repair 10 writes its live progress to stderr -- correction round,"
say  "        model pinned, new-or-resumed Claude session, seeded target, fresh"
say  "        OpenAI/Codex audit and verdict. stdout carries the machine report:"
say  ""
say  "          tail -F ${PROOF}/shadow-run.stdout"
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

step "SHADOW COPY"

# The copy is EXACT. Nothing is excluded.
#
# v1 excluded controller/__pycache__/ and write-test/ as build noise and
# scratch. Both exist on disk with real content, and the same exclusions were
# applied to the verification below, so the verification could only ever prove
# "equal apart from the excluded paths" while the launcher reported a
# byte-truthful copy. Neither path is referenced anywhere in nh_loop.py, so
# copying them changes no controller behaviour, and copying them makes the
# claim and the check agree.
#
# Never copied, because they are not in the workspace at all:
#   .ssh .netrc .config       - never copied
#   host .codex / .claude     - never copied; they are namespace-only anonymous
#                               copy-on-write overlays instead
#
# Both launcher scripts ARE copied, because the shadow is a truthful copy of the
# workspace and they are files in it. They are inert inside the namespace:
# nothing in the rehearsal executes them, and the controller only ever runs git
# against NH-GOVERNANCE, never against controller/, so their presence cannot
# affect any gate.

mkdir -m 0700 -p "$SHADOW_WS"
rsync -aHAX --numeric-ids --delete "${WS}/" "${SHADOW_WS}/" \
  || die "rsync copy of the workspace into the shadow failed"
note "workspace copied into ${SHADOW_WS}"

step "SHADOW COPY VERIFICATION"

# Checksum dry-run compare. Any itemised line at all means the shadow is not a
# truthful copy of the original, and the rehearsal must not proceed.
#
# The exit STATUS is captured separately and is required to be zero. Discarding
# it with `|| true` would make a killed or otherwise failing dry run
# indistinguishable from a clean one: rsync would print nothing, COPY_DIFF would
# be empty, and an entirely unverified copy would be accepted as proved.
set +e
COPY_DIFF="$(rsync -aHAXn --delete --checksum --itemize-changes "${WS}/" "${SHADOW_WS}/" 2>&1)"
COPY_RC=$?
set -e
if [ "$COPY_RC" -ne 0 ] || [ -n "$COPY_DIFF" ]; then
  {
    printf 'rsync verification exit status: %s\n' "$COPY_RC"
    printf '%s\n' "$COPY_DIFF"
  } > "${PROOF}/DIFF.shadow-copy.txt"
  die "the shadow copy could not be proved identical to the original
      (rsync exit status ${COPY_RC}).
      See ${PROOF}/DIFF.shadow-copy.txt
      Refusing to rehearse against a copy that is not proved truthful."
fi
note "shadow is a byte-truthful copy of the protected original"

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

# The shadow marker. It exists ONLY in the shadow, never in the original, so its
# presence inside the namespace at the normal N.H path is positive proof that
# the substitution happened and the real workspace is not what is mounted.
# Written AFTER copy verification so it can never pollute that comparison. It
# sits at the workspace root, outside both Git checkouts, so neither repository
# worktree status is affected.
#
# The token is keyed to the Repair-10 controller identity, so it cannot collide
# with any earlier rehearsal's marker: if anything ever mounted a preserved
# shadow here instead, the token check below would fail rather than pass.
SHADOW_TOKEN="nh-shadow-repair10-${EXP_LOOP_SHA}"
printf '%s\n' "$SHADOW_TOKEN" > "${SHADOW_WS}/${SHADOW_MARKER_NAME}"
printf '%s\n' "$SHADOW_TOKEN" > "${RUNTIME_TMP}/.nh_shadow_tmp_marker"
note "shadow marker placed"

# ==========================================================================
# SECTION 9 — THE BUBBLEWRAP NAMESPACE
# ==========================================================================

# One OUTER namespace. Everything below inherits it:
#
#   bwrap
#    -> python3 nh_loop.py execute-next-claude-task
#       -> Codex          -> Codex helpers / nested sandbox
#       -> Claude
#
# NOTE ON THE REPAIR-8 AND REPAIR-9 LIVE CONTRACTS:
#   Nothing here injects, fakes or pre-answers not_ready_reason, task_ready, a
#   package-local audit result, a question-validation result, a Codex verdict,
#   or a Claude correction result. --clearenv wipes the environment and the
#   ONLY NH_-prefixed variable set back for the real run is
#   NH_LOOP_INTERVIEW_STATE_DIR, which points at the shadow's own interview
#   state. Whether the real Codex preparation returns Repair 8's required
#   not_ready_reason correctly, and whether Repair 9's CURRENT_PACKAGE_ONLY
#   audit and preparation prompts behave as intended against real Codex, is
#   exactly what this rehearsal exists to find out. If a required schema is not
#   produced, the controller fails closed on its own and this launcher
#   preserves that evidence. There is no launcher-level retry.
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
    # This also puts the preserved v1 rehearsal lab out of reach: it lives
    # under /home/ness and is not among the paths put back below, so nothing
    # inside the namespace can even see it, let alone write to it.
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

# NOTHING may pre-answer the repair-8 preparation contract from outside. The
# complete set of NH_-prefixed variables must be exactly the two this launcher
# sets: the shadow interview-state dir, and the self-test's own marker token.
# Any other NH_* variable -- anything that could steer the controller or supply
# not_ready_reason -- fails the isolation here, before any model call.
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

# the preserved v1 rehearsal lab, and every other sibling lab, must be
# unreachable from inside: /home/ness is tmpfs and they were never put back.
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
# the run, and again AFTER it (section 12), because everything the sandboxed run
# can write -- the shadow workspace, /tmp and the captured stdout/stderr -- is
# lab-backed, while the credential overlays are readable inside the namespace.
# A pre-run check alone would leave a claim about the lab's final contents that
# nothing had actually tested.
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
# SECTION 11 — THE ONE REAL TEST
# ==========================================================================
#
# EXACTLY ONE outer execution of the controller, inside Bubblewrap.
# There is no retry loop here and nothing reruns it. If it fails, it fails once.
# The controller owns its own bounded internal correction loop, its own lifetime
# correction-round limit, its own OpenAI reasoning role (gpt-5.6-sol at effort
# HIGH, invoked through the read-only, ephemeral Codex CLI transport) and its
# own Claude configuration (claude-opus-5 at xhigh, with one package session per
# execution), and all of that is left exactly as it is.
#
step "ONE ISOLATED REAL REHEARSAL"

say "Running, inside the namespace:"
say "  ${PY3} ${WS}/controller/nh_loop.py execute-next-claude-task"
say ""
say "Live output is being written to:"
say "  ${PROOF}/shadow-run.stdout"
say "  ${PROOF}/shadow-run.stderr"
say "(tail -f either file from another terminal to watch it.)"
say ""

build_bwrap_args 11
exec 11<"$HOST_CLAUDE_JSON"

# From here on no report may claim that no model or provider call was made.
RUN_STARTED=1

# A non-zero exit here is an ORDINARY, EXPECTED outcome that this launcher
# exists to record. It must not abort the script: the AFTER proof below is the
# most important thing this launcher produces and it runs either way.
#
# In particular, a controller fail-closed caused by the repair-8 preparation
# contract -- for example a missing or malformed not_ready_reason from the real
# Codex preparation -- lands here as a plain non-zero exit code, is recorded,
# and the evidence is preserved in the lab. That is a legitimate result of this
# rehearsal. It is never retried and never papered over.
set +e
"$BWRAP" "${BWRAP_ARGS[@]}" \
  -- "$PY3" "${WS}/controller/nh_loop.py" execute-next-claude-task \
  > "${PROOF}/shadow-run.stdout" \
  2> "${PROOF}/shadow-run.stderr" \
  < /dev/null
SHADOW_RC=$?
set -e

exec 11<&- 2>/dev/null || true
printf '%s\n' "$SHADOW_RC" > "${PROOF}/shadow-run.exit-code"
note "isolated controller run finished with exit code ${SHADOW_RC}"

# ==========================================================================
# SECTION 11b — REPAIR-10 OBSERVATIONS (READ-ONLY, DECIDES NOTHING)
# ==========================================================================
#
# A convenience pass over the lab's OWN captured output, so the Repair-10
# behaviours are easy to inspect without reading 2000 lines by hand.
#
# IT RECORDS; IT DECIDES NOTHING. It sets no verdict, it can fail no check, and
# every safety verdict below is computed exactly as it was in v3. In particular
# a RESUMED Claude call is NOT required: if the candidate reaches PASS on its
# first audit there is no second correction round and so nothing to resume, and
# that is a legitimate outcome recorded as such.
#
# It reads only ${PROOF}/shadow-run.* , which this launcher created. It never
# reads the shadow candidates and never echoes candidate content: it counts
# fixed controller-owned markers, and prints only scalar configuration and
# session fields from the controller's own JSON report, each truncated.
step "REPAIR-10 OBSERVATIONS"

observe_repair10() {
  local out="${PROOF}/repair10-observations.txt"
  local so="${PROOF}/shadow-run.stdout"
  local se="${PROOF}/shadow-run.stderr"
  local n_new n_resume n_seed n_audit n_verdict

  n_new="$(grep -c -F -- 'invoking claude (new session'     "$se" 2>/dev/null || true)"
  n_resume="$(grep -c -F -- 'resuming the package claude session' "$se" 2>/dev/null || true)"
  n_seed="$(grep -c -F -- 'next target seeded byte-identical'     "$se" 2>/dev/null || true)"
  n_audit="$(grep -c -F -- 'fresh codex design audit starting'    "$se" 2>/dev/null || true)"
  n_verdict="$(grep -c -F -- 'codex verdict for'                  "$se" 2>/dev/null || true)"

  {
    printf 'REPAIR-10 OBSERVATIONS -- descriptive only, no verdict\n'
    printf 'controller exit code: %s\n\n' "$SHADOW_RC"

    printf 'CONFIGURATION THIS CONTROLLER IS FROZEN TO (from its own report):\n'
    grep -E '"(claude_model|claude_output_format|claude_allowed_tools|claude_permission_mode|claude_package_session_scope)"' \
         "$so" 2>/dev/null | cut -c1-200 || true
    printf '\n'

    printf 'CLAUDE PACKAGE SESSION (one per package execution):\n'
    grep -E '"(initial_claude_session_mode|initial_claude_session_ok|claude_package_session_established|claude_package_session_lost|claude_package_session_lost_reason|claude_package_session_invocations|claude_package_session_new_invocations|claude_package_session_resumed_invocations)"' \
         "$so" 2>/dev/null | cut -c1-200 || true
    printf '\n'

    printf 'CORRECTION LOOP:\n'
    grep -E '"(correction_round_limit|correction_rounds_started|correction_rounds_completed|claude_correction_invocations|total_codex_design_audit_invocations|final_design_audit_verdict|stop_reason)"' \
         "$so" 2>/dev/null | cut -c1-200 || true
    printf '\n'

    printf 'LIVE-PROGRESS MARKER COUNTS (from stderr):\n'
    printf '  new claude session started      : %s\n' "$n_new"
    printf '  resumed the package session     : %s\n' "$n_resume"
    printf '  next target seeded from blocked : %s\n' "$n_seed"
    printf '  fresh OpenAI/Codex audits begun : %s\n' "$n_audit"
    printf '  OpenAI/Codex verdicts recorded  : %s\n' "$n_verdict"
    printf '\n'

    if [ "${n_resume:-0}" -gt 0 ] 2>/dev/null; then
      printf 'A RESUMED Claude call occurred, so same-package session continuity\n'
      printf 'was exercised for real by this run.\n'
    else
      printf 'No resumed Claude call occurred. This is NOT a failure: if the\n'
      printf 'candidate reached PASS, or the loop stopped before a second\n'
      printf 'correction round, there was nothing to resume. Read stop_reason\n'
      printf 'and final_design_audit_verdict above to see which happened.\n'
    fi
    printf '\n'
    printf 'The OpenAI reasoning role is gpt-5.6-sol at effort high, invoked\n'
    printf 'through the read-only, ephemeral Codex CLI transport. Claude is\n'
    printf 'claude-opus-5 at xhigh. Both are the controller-owned configuration\n'
    printf 'frozen into nh_loop.py sha256 %s -- this launcher sets neither.\n' "$EXP_LOOP_SHA"
  } > "$out" 2>/dev/null || true

  note "repair-10 observations written to ${out}"
}
observe_repair10 || true

# ==========================================================================
# SECTION 12 — RE-PROVE THE ORIGINAL, FROM OUTSIDE THE NAMESPACE
# ==========================================================================

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
# the sandboxed run has copied or echoed their contents into the lab, which is
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
printf '==================================================\n'
printf 'N.H SHADOW LIVE REHEARSAL (v4, REPAIR-10) — RESULT\n'
printf '==================================================\n'
printf 'SHADOW_LAB=%s\n'               "$LAB"
printf 'FROZEN_CONTROLLER_SHA256=%s\n' "$EXP_LOOP_SHA"
printf 'SHADOW_CONTROLLER_EXIT=%s\n'   "$SHADOW_RC"
printf 'ORIGINAL_WORKSPACE_PROOF=%s\n' "$ORIGINAL_PROOF"
printf 'PRESERVED_LAB_PROOF=%s\n'      "$PRESERVED_LAB_PROOF"
printf 'HOST_CREDENTIAL_WITNESS=%s\n'  "$CREDENTIAL_WITNESS"
printf 'LAB_CREDENTIAL_SCAN=%s\n'      "$LAB_CREDENTIAL_SCAN"
printf 'SHADOW_STDOUT=%s\n'            "${PROOF}/shadow-run.stdout"
printf 'SHADOW_STDERR=%s\n'            "${PROOF}/shadow-run.stderr"
printf 'REPAIR10_OBSERVATIONS=%s\n'    "${PROOF}/repair10-observations.txt"
printf '==================================================\n'

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
printf '\n  The lab holds a copy of the N.H interview authenticity key.\n'
printf '  Delete the lab once the rehearsal has been reviewed.\n'
printf '\n  LAB_CREDENTIAL_SCAN is a SHAPE scan, not proof of absence.\n'
printf '  NO-KNOWN-MARKERS means only that no known credential marker was\n'
printf '  found in readable, uncompressed lab content. It cannot see a token\n'
printf '  in an unrecognised shape, and it cannot see into compressed or\n'
printf '  encoded data. Treat the lab as sensitive regardless of this line.\n\n'

# Fail closed: a protected-original mismatch outranks any apparent shadow
# success, and a preserved-evidence mismatch outranks it too. All three safety
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
exit "$SHADOW_RC"

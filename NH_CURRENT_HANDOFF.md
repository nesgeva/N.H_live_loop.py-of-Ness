# N.H Current Handoff

Verified on 2026-09-06. Read this file together with the project `AGENTS.md`.

## User goal

Continue in a fresh Codex task because the current conversation is extremely long and the desktop app is buffering. Preserve all completed work. Restart the normal N.H question-validation flow from the beginning, with A19 as the one current package, but do not start a provider or the loop without Ness's explicit instruction in the new task.

## Current N.H state

- The N.H loop is not running.
- The fresh `nh_interview_state` directory has zero journal records and no current-work pointer.
- The former state is preserved, not deleted, in `nh_interview_state.disconnected-before-full-restart`.
- Four former active candidate documents were moved to `NH-GOVERNANCE/05_INACTIVE_CANDIDATE`. They were not deleted.
- `NH-GOVERNANCE/05_ACTIVE_CANDIDATE/NH_A19_CURRENT_QUESTION_VALIDATION_SELECTION_v1_0_CANDIDATE.md` identifies A19 as the one current question-validation package.
- No A19 provider run was started after the fresh-state reset.

## Latest verified controller fix

`controller/nh_loop.py` was corrected so a brand-new empty state can be read before its first authentication key is created. After the fix:

- `interview-status` reads the empty state successfully.
- `interview-gate` reads the empty state successfully and remains closed because no new package-bound validation exists yet.
- `supervisor-status` and `loop-status` now fail closed for the expected reason: the fresh state has no authenticated package-bound validation. They no longer crash on the missing key.

## Uncommitted work that must be preserved

The controller repository has uncommitted changes in:

- `controller/nh_loop.py`
- `controller/nh_supervisor/commands.py`
- `controller/nh_supervisor/constants.py`
- `controller/nh_supervisor/engine.py`
- `controller/nh_supervisor/schema.py`

The governance repository also has the candidate moves and the new A19 selection file as uncommitted changes. Do not reset, checkout, overwrite, or discard any of these changes.

## Desktop buffering investigation

- Seven temporary Codex cache folders were moved to a recoverable backup.
- The project, conversations, sign-in, and settings were not changed by that cleanup.
- Buffering continued after the cleanup, so cache size was ruled out as the cause.
- The computer had ample free disk space and memory, and basic network checks were healthy.
- The current app log showed the realtime voice session starting successfully, while the desktop interface repeatedly struggled to apply updates to this very long conversation. A fresh task is therefore the best next diagnostic step, but this is a strong inference rather than absolute proof.

## Next safe step

1. Open a new Codex task in this same project.
2. Read `AGENTS.md` and this handoff.
3. Re-run the four read-only live-state checks from `controller/`.
4. Report the verified fresh state to Ness in short Hebrew.
5. Wait for Ness's explicit instruction before starting A19 question validation.

Git and the current files remain the source of truth. This handoff is only a continuation guide.

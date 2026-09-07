# Current handoff — Bundle Seven question loop

Updated: 2026-08-31, Asia/Jerusalem.

## Current state

- Nothing is running now: the approved external run ended safely.
- The saved Bundle Seven baseline still covers all 10 packages, 36 features and about 190 sources.
- A complete Bundle Seven question list is not ready yet.
- The run made two real provider calls:
  - A19 returned content, but the local validator rejected it. No A19 validation or questions were committed.
  - A17 returned valid content, passed the supervised custody/authorization path and was recorded as a complete validation with no open questions.
- The remaining eight packages did not call the model. The local control binding refused after it saw A19 and A17 as two competing transition scopes.
- No further external run is authorized. Do not spend Usage without a new explicit approval from Ness.

## Exact run outcome

- Command result: `QUESTION_VALIDATION_REFUSED`.
- External invocations: 2.
- A17 durable validation: event 1863, validation set `vs_66f09c6c7ea65819fb4943675c07868b`.
- A19 durable terminal: `result_invalid`; its rejected content remains preserved in custody history and changed no question or decision.
- A20, A21, A22, A23, A24, B29, B30 and B-INT-10 were skipped before provider contact because the ordinary CPB single-transition control rule refused the batch state.
- No merged Bundle Seven question inventory was recorded.

## Local correction completed after the run

The Bundle Seven audit now has a narrow control-only anchor resolver:

1. Ordinary supervisor status and ordinary package transitions still use the unchanged CPB single-transition rule.
2. The explicit Bundle Seven batch uses the latest proved established package only for the worker lease/control proof; that package does not select which Bundle Seven member is checked.
3. The exact ten package scopes come only from the authenticated Bundle Seven baseline plan.
4. Inside that batch, sibling package validations are treated as members of one audit plan rather than competing Q transitions. Evidence outside the ten-package plan still fails closed.
5. After a successful ten-package merge, the exact validation sets named by the merge become audit history. Later events for the same package still participate in the ordinary transition rule.

Verification:

- Syntax checks passed.
- The focused Bundle Seven and ordinary two-transition safety tests passed: 6 tests.
- The complete stabilization suite passed: **113 tests in 113.330 seconds**.
- The ordinary CPB two-transition refusal test still passes.
- A read-only build against the current live journal proved that the special Bundle Seven control context can be constructed without weakening the ordinary context.
- No external model was invoked by these fixes or tests.

## Important current journal fact

Until the ten-package audit completes and records its merge, the ordinary current-package resolver will continue to see the preserved A17/A19 batch evidence as a contradiction. This is intentional fail-closed behavior. The next Bundle Seven run must use the special batch control path; an ordinary live-loop run must not be started over this intermediate state.

## What remains

1. Obtain fresh explicit approval for external Usage.
2. Resume the supervised Bundle Seven batch:
   - retry A19 once through the corrected path,
   - reuse/skip the already-complete A17 validation,
   - run the remaining eight packages once each,
   - continue past a package failure without merging incomplete results.
3. Record the merged inventory only after all ten package validations and all 36 feature checks are complete.
4. Ask separately before running the independent whole-inventory coverage review, because that is another external review.
5. Present the resulting complete question groups to Ness only after coverage passes.

## User requirements

- Follow the original project instructions and fail closed.
- Do small fixes and tests locally without external Usage.
- Use a large external review only when necessary and after explaining it.
- Do not restart all of Bundle Seven unnecessarily; reuse the saved baseline, A17 validation, journal and checkpoints.
- If one package fails, continue checking the other packages, but do not merge or present a complete list until every failure is resolved.
- State only what was actually verified; do not describe estimates as facts.
- Keep explanations short and simple.
- Do not upload, commit or push anything unless Ness explicitly asks.

## Safe next step

Explain that the local transition fix is complete and tested. Ask Ness for one new external authorization to resume the batch. Do not automatically launch the independent coverage review under that authorization.

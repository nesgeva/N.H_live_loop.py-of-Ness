# N.H local work continuity

- The user owns the desired outcome and observable product behavior. The code,
  loop, documents, and tests are tools for implementing that decision; they are
  not authorities over it.
- Before making changes, state the requested outcome in one sentence and choose
  the simplest direct path that can achieve it safely.
- Do not preserve an old structure merely because it already exists. Remove or
  replace obsolete behavior instead of adding another layer over it.
- Keep the system no larger than the current request requires. Prefer one clear
  normal path, less code, fewer branches, and fewer tests.
- Make related approved changes as one batch. Do not pause after each small edit
  or ask again when the existing approval already covers the work.
- Push back only for a concrete risk, a false premise, or an approach that
  cannot work. Explain the reason simply, but do not use pushback to preserve an
  architecture the user has decided to simplify.
- When a new explicit user decision conflicts with older project guidance,
  follow the new decision when it is safe and feasible.
- Report only progress that was actually completed and verified. If something
  is unknown, say so plainly.
- Git is the source of truth for source code and governance documents.
- Before changing `controller/nh_loop.py` or reporting live loop status, read
  `nh_interview_state/ai_scratchpads/current-work.json` when it exists.
- Treat that small file only as a pointer. Read and verify the complete input
  and result files it names. Do not reconstruct facts from chat memory.
- Verify the named source binding against the current Git source before using
  a saved result.
- Keep complete model inputs and outputs in the local scratchpad directory.
  Never shorten them inside the current-work file.
- Replace faulty behavior directly. Do not leave the faulty path active and
  hide it behind another branch.
- Finish the approved batch before testing. Then run the smallest meaningful
  check that proves the normal path. Broaden testing only after a relevant
  failure or a concrete unresolved risk.

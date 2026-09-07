# N.H Design Loop UI

This is the local browser surface for N.H’s existing authenticated interview.
It does not generate, validate, reinterpret, or settle questions itself.

The page uses the controller’s existing commands:

- `interview-status` and `interview-gate` for read-only state;
- `next-question-group` when a verified question is actually displayed;
- `record-ness-answer` when Ness presses **Save this answer**.

The interface now also contains the first local supervisor surface:

- **Your decisions** keeps the existing authenticated Piece-3 interview;
- **What's changing** renders only audit, custody, and pass events freshly
  re-proved by the controller's authenticated `supervisor-status` command;
- **Current status** distinguishes working, diagnosis, recovery, Ness decision,
  practical user action, safety hold, and acceptance-ready states;
- **Technical details** keeps the underlying identities available without making
  them the primary user experience.

The automatic worker and UI state model are implemented as candidates in
`supervisor.py` and `worker.py`. They are not automatically started against the
installed controller yet. The installed controller still has a five-round
lifetime correction stop and does not yet implement
`diagnose-next-correction-batch` or `supervisor-status`. Until a separately
reviewed controller candidate supplies those commands, the page truthfully says
that mechanical work is ready but no supervised run is active.

The worker's separate local journal is a private recovery/scheduling log only.
It is held in an owner-only `0700` directory as an owner-only, single-link
`0600` file and stores only bounded recovery projections, never complete
controller reports. Its unkeyed hash chain is not authority for browser state,
findings, PASS, candidate custody, questions, or acceptance readiness.
Local journal protocol version 2 uses the controller's ASCII-escaped canonical
JSON and binds every event to executable, source, package, candidate, and report
identity; old prototype records are refused rather than reinterpreted.

The candidate worker also uses a separate owner-only lease and lock in the same
anchored state directory. It excludes a second worker, heartbeats during model
commands and recovery waits, expires after a crash, and checks boot ID plus
process start time so PID reuse cannot impersonate the prior worker. These
mechanics remain disabled against the active Repair31 controller until the
reviewed successor supplies authenticated `supervisor-status` and recovery
commands.

Start it with:

```bash
python3 interview_ui/server.py
```

It binds only to `127.0.0.1` and opens the local page automatically. Technical
details are available but visually secondary. The persistent context panel leads
with the plain-language N.H feature, its purpose, the current stage, and why Ness
is or is not being asked.

Run the local no-provider checks with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest -v \
  test_supervisor.py test_worker.py test_server.py test_rehearsal.py
```

The full rehearsal proves a five-correction batch, a separate diagnosis step,
round-six continuation, a final PASS transition, and readiness for explicit
acceptance using deterministic fake controller reports. It does not claim that
the active controller can perform that sequence yet.

#!/usr/bin/env python3
"""The persistent local supervisor process.

Section 13.1 is the ONLY state machine this worker performs, and Section 13.5
supplies its two lease gates.  It composes no question, finding, correction
specification, filename, candidate byte, route, PASS, acceptance, dependency
class, binding, carrier, occurrence ordinal, outcome fact, error signal token,
classification row id, probe fact, audit usability class, work-item identity,
provider-request identity, episode identity, probe identity, result custody
identity, capability baseline, semantic scope key, scope-exhaustion identity,
unlock generation, novelty key, canonical addition slot, or retry-series key.

Recovery calls the controller's own read-only ``supervisor-operation-status``
and branches on its six exact ``recovery_outcome`` strings.  It never duplicates
a controller decision and never looks for substitute booleans.
"""

from __future__ import annotations

import os
import sys
import threading
import time
from dataclasses import dataclass, field
from typing import Any, Callable

_UI_DIR = os.path.dirname(os.path.abspath(__file__))
if _UI_DIR not in sys.path:
    sys.path.insert(0, _UI_DIR)

import supervisor  # noqa: E402
from nh_supervisor import constants as controller_constants  # noqa: E402

RECOVERY_OUTCOMES = (
    "COMPLETED",
    "SAFE_TO_RESUME",
    "SAFE_TO_RETRY",
    "WAIT",
    "NEEDS_USER_ACTION",
    "SAFETY_HOLD",
)

# Section 13.1 -- the commands the worker may ever run, and nothing else.
WORKER_COMMANDS = frozenset(
    (
        "supervisor-status",
        "supervisor-operation-status",
        "execute-next-claude-task",
        "diagnose-next-correction-batch",
        "process-custodied-provider-result",
        "close-open-consumption",
        "reconcile-provider-request",
        "probe-provider-availability",
        "open-new-provider-episode",
        "record-semantic-scope-unlock",
        "question-validation",
        "question-coverage-review",
        # v1_8 section 20.2 -- ALL FIVE new execution commands.  The two
        # INSTALLED execution commands (process-custodied-provider-result and
        # reconcile-provider-request) keep exactly the registrations they
        # already have above; nothing here re-registers or re-classifies them.
        "continue-design-loop",
        "dispatch-piece3-provider-review",
        "commit-piece3-provider-result",
        "prepare-next-design-task",
        "execute-initial-design",
    )
)

# v1_8 section 20.2 -- the CLOSED continuation command set the accepted branch
# may run, and nothing else.  The public question-validation and
# question-coverage-review are DELIBERATELY NOT IN IT: they keep their
# installed direct behaviour for the ordinary loop and for operator use
# (T2-PUBLIC-COMMANDS-UNCHANGED), and the continuation reaches the same
# underlying logic through its own two names.
CONTINUATION_COMMANDS = frozenset(
    (
        "continue-design-loop",
        "dispatch-piece3-provider-review",
        "commit-piece3-provider-result",
        "prepare-next-design-task",
        "execute-initial-design",
        "process-custodied-provider-result",
        "reconcile-provider-request",
    )
)
# v1_8 section 12.3d E5 / section 18 Row M -- the missing completion of an
# interrupted transition operation is appended by the command that STARTED it,
# which is already a member of the set above.  There is NO eighth continuation
# execution command, and the read-only ``supervisor-operation-status`` is never
# routed here: it writes nothing, ever.
assert "supervisor-operation-status" not in CONTINUATION_COMMANDS
assert not (
    CONTINUATION_COMMANDS & {"question-validation", "question-coverage-review"}
)

# Section 11.7 -- the commands that may reach the provider at all.  One retry
# series covers all three, so none of them runs before the series is eligible.
PROVIDER_CONTACTING_COMMANDS = frozenset(
    (
        "execute-next-claude-task",
        "diagnose-next-correction-batch",
        "reconcile-provider-request",
        "probe-provider-availability",
        "question-validation",
        "question-coverage-review",
        # v1_8 section 20.2 -- the new execution commands that reach a
        # provider.  commit-piece3-provider-result is PROVIDER-FREE by
        # construction (T2-ONE-CALL) and is DELIBERATELY ABSENT, so no retry
        # series gates it.
        #
        # Accepted role-split v1_6 section 5.1 removes prepare-next-design-task
        # for the SAME reason: its operations are a bounded LOCAL derivation
        # that contacts nobody, so no provider retry series may gate it either.
        # The worker still RECOGNISES and RUNS the command -- only its
        # classification moves.
        "continue-design-loop",
        "dispatch-piece3-provider-review",
        "execute-initial-design",
    )
)
assert "commit-piece3-provider-result" not in PROVIDER_CONTACTING_COMMANDS
assert "prepare-next-design-task" not in PROVIDER_CONTACTING_COMMANDS
assert "prepare-next-design-task" in WORKER_COMMANDS

# v1_8 section 7.5, as corrected by accepted role-split v1_6 section 5.1 -- the
# THREE continuation commands that reach a provider.  Mirrored from the
# controller's own registry so the two can never drift, and deliberately
# NARROWER than the installed global set above: it is the accepted continuation
# classification, not the ordinary-loop one.
CONTINUATION_PROVIDER_CONTACTING_COMMANDS = frozenset(
    controller_constants.CONTINUATION_PROVIDER_CONTACTING_COMMANDS
)
assert len(CONTINUATION_PROVIDER_CONTACTING_COMMANDS) == 3
assert "reconcile-provider-request" not in CONTINUATION_PROVIDER_CONTACTING_COMMANDS
assert (
    "process-custodied-provider-result"
    not in CONTINUATION_PROVIDER_CONTACTING_COMMANDS
)
assert (
    "commit-piece3-provider-result" not in CONTINUATION_PROVIDER_CONTACTING_COMMANDS
)
# The INSTALLED global set is untouched and still carries all six of its own.
assert "reconcile-provider-request" in PROVIDER_CONTACTING_COMMANDS

# Section 13.1 -- the states in which the worker runs nothing at all.
NON_RUNNING_STATES = frozenset(
    (
        supervisor.WorkflowState.NEEDS_NESS_DECISION,
        supervisor.WorkflowState.NEEDS_USER_ACTION,
        supervisor.WorkflowState.READY_FOR_ACCEPTANCE,
        supervisor.WorkflowState.SAFETY_HOLD,
        supervisor.WorkflowState.IDLE,
        # v1_8 section 20.2 -- ACCEPTED_FOR_DESIGN_ONLY REMAINS IN
        # NON_RUNNING_STATES, so no ORDINARY supervisor command runs in that
        # state, exactly as today.  What changes is not this set: the accepted
        # branch of _step() gains ONE bounded route that may run ONLY a command
        # from the closed continuation set above, and only after the read-only
        # loop-status names it.
        supervisor.WorkflowState.ACCEPTED_FOR_DESIGN_ONLY,
    )
)

BINDING_FIELDS = (
    "controller_executable_identity",
    "package_scope_id",
    "source_binding_sha256",
)
BINDING_CHANGE_RETIRE_ACTION = "retire_for_binding_change"


@dataclass(frozen=True)
class CommandResult:
    command: str
    report: dict
    returncode: int = 0


@dataclass
class StepOutcome:
    state: str
    action: str
    detail: str = ""
    next_delay_seconds: float = 0.0
    recovery_outcome: Any = None
    ran_command: Any = None


class Clock:
    def now(self):
        return time.time()

    def wait(self, seconds):
        if seconds > 0:
            time.sleep(seconds)
        return True


@dataclass
class WorkerObservation:
    """What the worker keeps for the CURRENT RUN only, and nothing more."""

    supervisor_operation_id: Any = None

    def forget(self):
        self.supervisor_operation_id = None


def null_envelope(supervisor_operation_id=None, supervisor_command=None):
    """Section 11.1 / 4.11 (a) -- the caller-owned portion, and nothing else.

    Every caller constructs all three ``unlock_evidence_*`` fields as present and
    NULL, for every command without exception.  The worker never receives,
    stores, echoes, or presents an evidence value, and it holds no
    ``pre_state_sha256`` and no ``input_envelope_sha256`` at all.
    """
    return {
        "supervisor_operation_id": supervisor_operation_id,
        "supervisor_command": supervisor_command,
        "unlock_evidence_kind": None,
        "unlock_evidence_identity": None,
        "unlock_evidence_sha256": None,
    }


class SupervisorWorker:
    """One worker, one lease, one command at a time."""

    def __init__(self, runner, *, scheduling=None, lease=None, lease_binding=None,
                 own_run_id=None, clock=None, binding=None):
        self.runner = runner
        self.scheduling = scheduling
        self.lease = lease
        self.lease_binding = lease_binding or {}
        self.own_run_id = own_run_id
        self.clock = clock or Clock()
        self.binding = binding or {}
        self.observation = WorkerObservation()
        self.stopped = False
        self.local_observations = []
        self._lock = threading.Lock()

    # -- lease ---------------------------------------------------------------
    def acquire(self):
        if self.lease is None:
            return "ABSENT_PROVED"
        outcome, held = self.lease.acquire(self.lease_binding, now=int(self.clock.now()))
        if outcome in ("ACQUIRED", "RENEWED") and held is not None:
            self.own_run_id = held["run_id"]
        return outcome

    def heartbeat(self):
        """Section 13.5 gate 4 -- one failed heartbeat stops new work at once."""
        if self.lease is None:
            return False
        ok, state = self.lease.heartbeat(self.lease_binding, now=int(self.clock.now()))
        if not ok:
            self.stopped = True
        return ok

    def release(self):
        if self.lease is None:
            return False
        return self.lease.release(self.lease_binding, now=int(self.clock.now()))

    def start_gate_open(self):
        """Section 13.5 gate 1, evaluated by the controller's own predicate."""
        if self.lease is None:
            return False, "no lease is configured"
        state, held, _reason = self.lease.evaluate(
            self.lease_binding, now=int(self.clock.now())
        )
        return supervisor.new_work_start_gate(
            state, held, self.own_run_id, self.lease_binding, int(self.clock.now())
        )

    # -- one bounded step ----------------------------------------------------
    def step(self):
        with self._lock:
            return self._step()

    def _step(self):
        status = self.runner("supervisor-status", None)
        report = status.report
        # A durably accepted package has no remaining package work to
        # revalidate.  Source movement is still reported, but it must not hide
        # the controller's separately proved post-acceptance continuation.
        accepted_continuation_proved = (
            isinstance(report, dict)
            and report.get("command") == "supervisor-status"
            and report.get("ok") is True
            and report.get("journal_authentication_proved") is True
            and report.get("authenticated_state_current") is True
            and report.get("workflow_state") == "ACCEPTED_FOR_DESIGN_ONLY"
            and report.get("acceptance_truth") == "PROVED_ACCEPTED"
        )
        # The controller recomputes its installed executable identity for every
        # status command.  A worker keeps the exact binding under which it
        # acquired its lease.  Once those proved bindings differ, this process
        # may finish no more work: the production lifecycle stops its heartbeat
        # and releases the original lease before any fresh worker can acquire.
        #
        # This check deliberately precedes report_is_proved().  A changed
        # source/controller binding is itself one reason the ordinary report is
        # not source-current.  Requiring source-currentness first made the
        # retirement branch unreachable and left the obsolete worker renewing
        # its lease forever.  The narrower authentication proof below is still
        # mandatory: only a successful authenticated supervisor-status record
        # may retire a worker.
        binding_observation_proved = (
            isinstance(report, dict)
            and report.get("command") == "supervisor-status"
            and report.get("ok") is True
            and report.get("journal_authentication_proved") is True
            and report.get("authenticated_state_current") is True
        )
        changed_binding_fields = tuple(
            field
            for field in BINDING_FIELDS
            if self.lease_binding.get(field) is not None
            and report.get(field) is not None
            and self.lease_binding.get(field) != report.get(field)
        )
        if (
            binding_observation_proved
            and changed_binding_fields
            and report.get("workflow_state") == supervisor.WorkflowState.SAFETY_HOLD.value
            and (report.get("run_lease") or {}).get("lease_state")
            == "INVALID_UNPROVED"
        ):
            self.stopped = True
            controller_changed = (
                "controller_executable_identity" in changed_binding_fields
            )
            return StepOutcome(
                state=supervisor.WorkflowState.SAFETY_HOLD.value,
                action=BINDING_CHANGE_RETIRE_ACTION,
                detail=(
                    "Controller changed; fresh worker required."
                    if controller_changed
                    else "Worker binding changed; fresh worker required."
                ),
            )

        if not (
            supervisor.report_is_proved(report) or accepted_continuation_proved
        ):
            return StepOutcome(
                state=supervisor.WorkflowState.IDLE.value,
                action="wait",
                detail=(
                    "no fresh authenticated supervisor-status report is available, "
                    "so no supervised run is active and nothing is claimed"
                ),
                next_delay_seconds=supervisor.LEASE_HEARTBEAT_INTERVAL_SECONDS,
            )

        state = supervisor.WorkflowState(report["workflow_state"])
        next_command = report.get("next_command")

        # Recovery FIRST: every incomplete operation is reconciled through the
        # controller's own read-only command before any provider command runs.
        recovery = self.reconcile_incomplete_operation(report)
        if recovery is not None:
            return recovery

        # v1_8 section 20.3 -- the accepted branch, in this exact order.
        # Steps 1 and 2 above are the installed gates, applied unchanged.
        if accepted_continuation_proved:
            continuation = self._continuation_step(report, state)
            if continuation is not None:
                return continuation

        if state in NON_RUNNING_STATES:
            return StepOutcome(
                state=state.value,
                action="wait",
                detail=self._non_running_detail(state, report),
                next_delay_seconds=supervisor.LEASE_HEARTBEAT_INTERVAL_SECONDS,
            )

        if next_command is None:
            return StepOutcome(
                state=state.value,
                action="wait",
                detail="the controller names no next safe command",
                next_delay_seconds=supervisor.LEASE_HEARTBEAT_INTERVAL_SECONDS,
            )
        if next_command not in WORKER_COMMANDS:
            self.local_observations.append(
                "the controller named a command this worker may not run: %s"
                % next_command
            )
            return StepOutcome(
                state=supervisor.WorkflowState.SAFETY_HOLD.value,
                action="fail_closed",
                detail="unknown next command",
            )

        # Section 13.1 -- the two flags the worker is permitted to act on, and
        # nothing else decides these two commands.
        if next_command == "probe-provider-availability" and not report.get(
            "availability_probe_automatic_eligible"
        ):
            return self._wait("the bounded probe is not automatically eligible", state)
        if next_command == "open-new-provider-episode" and not report.get(
            "episode_unlock_automatic_eligible"
        ):
            return self._wait(
                "only a person may open the next provider episode in this state", state
            )
        if next_command == "record-semantic-scope-unlock" and not report.get(
            "semantic_scope_unlock_available"
        ):
            return self._wait("no semantic scope unlock is available", state)

        # Section 4.5a -- the worker fails closed on an inconsistent dependency
        # projection rather than repairing it.
        problem = self._dependency_projection_problem(report)
        if problem is not None:
            self.local_observations.append(problem)
            return StepOutcome(
                state=supervisor.WorkflowState.SAFETY_HOLD.value,
                action="fail_closed",
                detail=problem,
            )

        # Section 11.7 -- "does no provider work before next_eligible_epoch".
        # The bound is on the WORK, not on the reported state: reconciliation,
        # probing and dispatch all share one series, so an unreachable endpoint
        # or an unreachable lookup can never be polled in a hot loop whatever
        # state the controller currently projects.
        series_key = report.get("retry_series_key")
        if (
            next_command in PROVIDER_CONTACTING_COMMANDS
            and series_key
            and self.scheduling is not None
            and not self.scheduling.eligible(series_key, self.clock.now())
        ):
            return self._wait(
                "the bounded backoff for this dependency has not elapsed",
                state,
                delay=self.scheduling.wait_seconds(series_key, self.clock.now()),
            )

        ok, reason = self.start_gate_open()
        if not ok:
            return StepOutcome(
                state=state.value,
                action="wait",
                detail="the new-work start gate is closed: %s" % reason,
                next_delay_seconds=supervisor.LEASE_HEARTBEAT_INTERVAL_SECONDS,
            )

        request = None
        if next_command == "record-semantic-scope-unlock":
            request = null_envelope(
                self.observation.supervisor_operation_id, next_command
            )
        result = self.runner(next_command, request)
        if next_command == "record-semantic-scope-unlock":
            identity = result.report.get("supervisor_operation_id")
            if identity is not None:
                self.observation.supervisor_operation_id = identity
            if result.report.get("unlock_accepted") or result.report.get(
                "recovery_outcome"
            ) == "COMPLETED":
                self.observation.forget()
        self.record_scheduling_outcome(series_key, result=result, prior_report=report)
        return StepOutcome(
            state=state.value,
            action="ran_command",
            detail=str(result.report.get("outcome") or result.report.get("boundary") or ""),
            ran_command=next_command,
        )

    # -- Section 11.7 -- the private durable backoff, and nothing more --------
    def record_scheduling_outcome(self, previous_series_key=None, *, result=None,
                                  prior_report=None):
        """Schedule or clear the ONE private backoff series this step affects.

        Section 11.7 is worker-private state: the controller records the
        dependency and derives the retry-series key, and this worker records only
        when it may next do provider work.  It decides nothing.  It reads the
        fresh authenticated post-operation ``supervisor-status`` for the key, the
        dependency, and the state binding, and it writes no operation id, no
        envelope, and no evidence.
        """
        if self.scheduling is None:
            return None
        # A successful operation cannot create a technical retry dependency.
        # Clear the already-bound private series directly instead of paying for
        # another full supervisor projection only to prove that same fact.
        if result is not None and result.report.get("ok") is True:
            binding = self.scheduling_binding(prior_report or {})
            for stale in self.scheduling.series_keys():
                self.scheduling.clear_series(stale, binding)
            return None
        status = self.runner("supervisor-status", None)
        report = status.report
        if not supervisor.report_is_proved(report):
            return None
        series_key = report.get("retry_series_key")
        record = report.get("dependency_record") or {}
        retry_mode = record.get("retry_mode")
        now = int(self.clock.now())
        binding = self.scheduling_binding(report)
        if series_key and retry_mode in supervisor.AUTOMATIC_RETRY_MODES:
            return self.scheduling.schedule_backoff(
                series_key,
                binding,
                now,
                dependency_identity=report.get("dependency_identity"),
                dependency_identity_binding=report.get("dependency_identity_binding"),
                work_item_identity=report.get("work_item_identity"),
                episode_identity=report.get(
                    "provider_availability_episode_identity"
                ),
                output_retries_used=int(report.get("output_retries_used") or 0),
                post_operation_state_sha256=report.get("state_binding_sha256"),
            )
        # Section 11.7: "A successful operation clears the series."  Section
        # 11.6: a recomputed key that differs from the stored one clears the old
        # series rather than inheriting its attempt count.  Both are the same
        # act -- every series this worker holds that is not the one the fresh
        # authenticated report names is no longer current, so it is cleared.
        for stale in self.scheduling.series_keys():
            if stale == series_key and retry_mode in supervisor.AUTOMATIC_RETRY_MODES:
                continue
            self.scheduling.clear_series(stale, binding)
        return None

    def record_transition_scheduling_outcome(self, series_key,
                                             scheduling_binding=None,
                                             scheduling_metadata=None,
                                             result=None):
        """v1_8 section 20.3 -- schedule or clear the TRANSITION series.

        The same worker-private mechanism section 11.7 already defines, applied
        to the series the controller derived for the transition work.  NO
        SECOND SCHEDULER and no second key space is created, and the worker
        decides nothing: it re-reads the controller's fresh ``loop-status``
        answer and records what that answer implies.

        "A successful operation clears the series."  A position that is still
        waiting, recovering or reconciling is the bounded technical dependency
        case, and backs the same series off.
        """
        if self.scheduling is None or not series_key:
            return None
        if result is not None and result.report.get("ok") is True:
            binding = scheduling_binding
            if binding is not None:
                binding = {
                    "controller_executable_identity": self.lease_binding.get(
                        "controller_executable_identity"
                    ),
                    "source_binding_sha256": binding.get("source_binding_sha256"),
                    "package_scope_id": binding.get("package_scope_id"),
                    "candidate_path": binding.get("candidate_path"),
                    "candidate_sha256": binding.get("candidate_sha256"),
                    "candidate_bytes": binding.get("candidate_bytes"),
                    "work_item_identity": binding.get("work_item_identity"),
                }
                self.scheduling.clear_series(series_key, binding)
            return None
        status = self.runner("supervisor-status", None)
        report = status.report
        if not supervisor.report_is_proved(report):
            return None
        loop = self.runner("loop-status", None).report
        # THE EXACT TRANSITION BINDING AND METADATA, copied from the controller.
        #
        # The ordinary ``scheduling_binding(report)`` and the supervisor-status
        # dependency/episode/state fields all describe the ACCEPTED package P,
        # and P deliberately stays current while Q transitions.  Recording Q's
        # series under any of them would produce a MIXED P/Q private record, and
        # a retry series must describe ONE exact piece of work.
        #
        # So every value below comes from the controller's own loop projection,
        # over the same scope the series was derived for.  The worker copies;
        # it derives nothing.
        binding = scheduling_binding or loop.get("loop_scheduling_binding")
        metadata = scheduling_metadata or loop.get("loop_scheduling_metadata") or {}
        if binding is None:
            return None
        binding = {
            "controller_executable_identity": self.lease_binding.get(
                "controller_executable_identity"
            ),
            "source_binding_sha256": binding.get("source_binding_sha256"),
            "package_scope_id": binding.get("package_scope_id"),
            "candidate_path": binding.get("candidate_path"),
            "candidate_sha256": binding.get("candidate_sha256"),
            "candidate_bytes": binding.get("candidate_bytes"),
            "work_item_identity": binding.get("work_item_identity"),
        }
        now = int(self.clock.now())
        waiting = loop.get("loop_state") in (
            "LOOP_WAITING_RECOVERING",
            "LOOP_TRANSITION_RECONCILE_REQUIRED",
        )
        if waiting:
            return self.scheduling.schedule_backoff(
                series_key,
                binding,
                now,
                # ALL FROM THE TRANSITION, never from P's supervisor-status.
                dependency_identity=metadata.get("dependency_identity"),
                dependency_identity_binding=metadata.get(
                    "dependency_identity_binding"
                ),
                work_item_identity=metadata.get("work_item_identity"),
                episode_identity=metadata.get(
                    "provider_availability_episode_identity"
                ),
                output_retries_used=int(metadata.get("output_retries_used") or 0),
                post_operation_state_sha256=metadata.get(
                    "post_operation_state_sha256"
                ),
            )
        self.scheduling.clear_series(series_key, binding)
        return None

    def scheduling_binding(self, report):
        """The exact binding every private record carries.  No report is stored.

        Every value is copied from the fresh authenticated report; nothing here
        is derived, decided, or invented by the worker, and the controller
        report itself is never stored.
        """
        return {
            "controller_executable_identity": self.lease_binding.get(
                "controller_executable_identity"
            ),
            "source_binding_sha256": report.get("source_binding_sha256"),
            "package_scope_id": report.get("package_scope_id"),
            "candidate_path": report.get("candidate_path"),
            "candidate_sha256": report.get("candidate_sha256"),
            "candidate_bytes": report.get("candidate_bytes"),
            "work_item_identity": report.get("work_item_identity"),
            "provider_availability_episode_identity": report.get(
                "provider_availability_episode_identity"
            ),
            "retry_series_key": report.get("retry_series_key"),
            "controller_report_sha256": None,
        }

    def _continuation_step(self, report, state):
        """v1_8 section 20.3 -- the ONE bounded accepted-branch route.

        The worker DECIDES NOTHING here.  It reads the controller's read-only
        ``loop-status`` answer and runs the command it is told to run, or
        waits.  It composes no question, finding, correction, filename,
        candidate byte, route, PASS, acceptance, dependency class, binding,
        outcome fact or identity of any kind, and it decides no package and no
        target path.  THE WORKER GAINS ONE BRANCH AND ZERO DECISIONS.

        Returns a StepOutcome, or None to fall through to the ordinary
        non-running wait.
        """
        # 4. loop-status (read-only).
        loop = self.runner("loop-status", None)
        loop_report = loop.report
        loop_state = loop_report.get("loop_state")
        loop_next = loop_report.get("loop_next_command")

        # 5. loop_next_command is null -> wait, with the loop_state's honest
        #    detail.  A stop is a stop; it is never reported as completion.
        if loop_next is None:
            return self._wait(
                "%s: %s"
                % (
                    loop_state or "no loop state",
                    loop_report.get("loop_detail")
                    or "the controller names no next safe continuation command",
                ),
                state,
            )

        # 6. loop_next_command not in the closed set -> SAFETY_HOLD, fail
        #    closed.  This mirrors the installed refusal for an unknown next
        #    command.
        if loop_next not in CONTINUATION_COMMANDS or loop_next not in WORKER_COMMANDS:
            self.local_observations.append(
                "the controller named a continuation command this worker may "
                "not run: %s" % loop_next
            )
            return StepOutcome(
                state=supervisor.WorkflowState.SAFETY_HOLD.value,
                action="fail_closed",
                detail="unknown continuation command",
            )

        # 7. provider-contacting and the backoff series is not eligible -> wait.
        #
        # v1_8 section 20.3 step 7.  THE SERIES IS THE TRANSITION'S OWN, taken
        # from the controller's loop-status answer.
        #
        # It is deliberately NOT ``report["retry_series_key"]``: that is the
        # ACCEPTED package P's series, and during a transition P stays current
        # with no dependency of its own -- in the real event-84 state its key is
        # null.  Gating Q's provider stages on it would not gate them at all.
        #
        # The worker still decides nothing: the controller derives the series,
        # and this applies the EXISTING scheduling gate to it.
        series_key = loop_report.get("loop_retry_series_key")
        scheduling_binding = loop_report.get("loop_scheduling_binding")
        # v1_8 section 7.5 -- THE CONTINUATION CLASSIFICATION, NOT THE GLOBAL ONE.
        #
        # The installed global PROVIDER_CONTACTING_COMMANDS includes
        # reconcile-provider-request, because in the ORDINARY loop that command
        # shares one retry series with the dispatch it reconciles.  The accepted
        # continuation classification is different and deliberate: exactly FOUR
        # continuation commands reach a provider, and reconcile-provider-request
        # is one of the THREE that do not -- it performs an authoritative lookup
        # and records; it never dispatches.
        #
        # Gating the accepted branch on the global set deadlocked E2: the
        # controller correctly derives NO continuation series for a
        # provider-free command, and the worker then refused to run it for
        # lacking the series it is not supposed to have.  The ordinary global
        # set is UNCHANGED and still governs every non-continuation step.
        if loop_next in CONTINUATION_PROVIDER_CONTACTING_COMMANDS:
            # A MISSING SERIES IS NOT PERMISSION TO BYPASS THE BACKOFF.  If the
            # controller could not prove the exact work this stage is about to
            # run, the provider does not run at all.
            if not series_key or not scheduling_binding:
                return self._wait(
                    "the controller proved no retry series for this "
                    "continuation stage, so no provider work may begin",
                    state,
                )
            if self.scheduling is not None and not self.scheduling.eligible(
                series_key, self.clock.now()
            ):
                return self._wait(
                    "the bounded backoff for this dependency has not elapsed",
                    state,
                    delay=self.scheduling.wait_seconds(series_key, self.clock.now()),
                )

        # 8. start gate closed or lease not proved live -> wait.
        ok, reason = self.start_gate_open()
        if not ok:
            return self._wait(
                "the new-work start gate is closed: %s" % reason, state
            )

        # 9. run exactly one continuation command; record the scheduling
        #    outcome.
        # AUTONOMOUS: approved by user [2026-08-22]
        result = self.runner(loop_next, None)
        # Recorded against the EXACT transition series this command was gated
        # on, so a technical failure backs the right work off and a success
        # clears the right series.
        self.record_transition_scheduling_outcome(
            series_key, scheduling_binding,
            loop_report.get("loop_scheduling_metadata"),
            result=result,
        )
        return StepOutcome(
            state=state.value,
            action="ran_command",
            detail=str(
                result.report.get("outcome")
                or result.report.get("boundary")
                or loop_state
                or ""
            ),
            ran_command=loop_next,
        )

    def _wait(self, detail, state, delay=None):
        return StepOutcome(
            state=state.value,
            action="wait",
            detail=detail,
            next_delay_seconds=(
                supervisor.LEASE_HEARTBEAT_INTERVAL_SECONDS if delay is None else delay
            ),
        )

    def _non_running_detail(self, state, report):
        if state == supervisor.WorkflowState.NEEDS_USER_ACTION:
            record = report.get("dependency_record") or {}
            detail = record.get("plain_language_dependency") or (
                "one named external action is required"
            )
            code = record.get("user_action_code")
            if code:
                detail += " (%s)" % code
            if code == "provider_repeatedly_unavailable":
                detail += (
                    " -- after that named action a PERSON may run "
                    "open-new-provider-episode. This worker never runs it here."
                )
            return detail
        if state == supervisor.WorkflowState.NEEDS_NESS_DECISION:
            return "waiting for an authenticated answer and its fresh revalidation"
        if state == supervisor.WorkflowState.READY_FOR_ACCEPTANCE:
            return "waiting for separate explicit acceptance; nothing is accepted"
        if state == supervisor.WorkflowState.ACCEPTED_FOR_DESIGN_ONLY:
            # v1_8 section 24.8 -- amended for the transition case only.  The
            # acceptance itself remains terminal FOR ITS OWN PACKAGE; what is
            # no longer an unqualified truth, while a transition is genuinely
            # in progress, is "no next package is started here".
            if report.get("loop_transition_active"):
                return (
                    "accepted for design-only status; this package's workflow "
                    "is terminal, and a separate bounded continuation is "
                    "choosing and preparing the next design package"
                )
            return (
                "accepted for design-only status; this workflow is terminal and "
                "no next package is started here"
            )
        if state == supervisor.WorkflowState.SAFETY_HOLD:
            return "waiting for a proved safe unlock; nothing is written and no command runs"
        return "no supervised run is active"

    def _dependency_projection_problem(self, report):
        identity = report.get("dependency_identity")
        record = report.get("dependency_record")
        placement = report.get("dependency_durable_record_placement")
        carrier = report.get("dependency_carrier_event_seq")
        ordinal = report.get("dependency_occurrence_ordinal")
        if identity is None:
            if record is not None or carrier is not None or ordinal is not None:
                return "the report projects a dependency slot without an identity"
            return None
        if record is None:
            return "the report projects a dependency identity with no record"
        if record.get("dependency_identity_binding") != report.get(
            "dependency_identity_binding"
        ):
            return "the reported binding contradicts the record"
        if placement == "none_read_only_projection":
            if carrier is not None or ordinal is not None:
                return (
                    "a read-only lease projection must name no carrier and no ordinal"
                )
            return None
        if carrier is None or ordinal is None:
            return "the report projects a durable dependency with no occurrence"
        return None

    # -- recovery ------------------------------------------------------------
    def reconcile_incomplete_operation(self, report):
        """Call the controller's own read-only recovery command, and branch on it."""
        identity = self.observation.supervisor_operation_id
        if identity is None:
            return None
        result = self.runner(
            "supervisor-operation-status",
            null_envelope(identity, "record-semantic-scope-unlock"),
        )
        outcome = result.report.get("recovery_outcome")
        if outcome not in RECOVERY_OUTCOMES:
            self.local_observations.append(
                "supervisor-operation-status returned no recognised recovery outcome"
            )
            return StepOutcome(
                state=supervisor.WorkflowState.SAFETY_HOLD.value,
                action="fail_closed",
                detail="unrecognised recovery outcome",
                recovery_outcome=outcome,
            )
        if outcome == "COMPLETED":
            self.observation.forget()
            return None
        if outcome == "SAFE_TO_RESUME":
            next_command = result.report.get("next_command")
            if next_command is None:
                return None
            ok, reason = self.start_gate_open()
            if not ok:
                return StepOutcome(
                    state=report["workflow_state"],
                    action="wait",
                    detail="the new-work start gate is closed: %s" % reason,
                    recovery_outcome=outcome,
                )
            resumed = self.runner(next_command, null_envelope(identity, next_command))
            if resumed.report.get("unlock_accepted") or resumed.report.get(
                "recovery_outcome"
            ) == "COMPLETED":
                self.observation.forget()
            return StepOutcome(
                state=report["workflow_state"],
                action="resumed",
                detail=next_command,
                recovery_outcome=outcome,
                ran_command=next_command,
            )
        if outcome == "SAFE_TO_RETRY":
            return StepOutcome(
                state=report["workflow_state"],
                action="retry_permitted",
                recovery_outcome=outcome,
            )
        # WAIT, NEEDS_USER_ACTION and SAFETY_HOLD never invoke a generative call.
        return StepOutcome(
            state=(
                supervisor.WorkflowState.SAFETY_HOLD.value
                if outcome == "SAFETY_HOLD"
                else report["workflow_state"]
            ),
            action="wait",
            detail=outcome,
            recovery_outcome=outcome,
            next_delay_seconds=supervisor.LEASE_HEARTBEAT_INTERVAL_SECONDS,
        )

    # -- bounded run loop ----------------------------------------------------
    def run(self, max_steps=1):
        outcomes = []
        for _index in range(max_steps):
            if self.stopped:
                break
            outcome = self.step()
            outcomes.append(outcome)
            if outcome.action in ("fail_closed",):
                break
            if outcome.next_delay_seconds:
                self.clock.wait(min(outcome.next_delay_seconds, 900))
        return outcomes

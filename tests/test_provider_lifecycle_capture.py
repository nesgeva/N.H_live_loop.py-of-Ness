import hashlib
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
# ROOT itself is required: the import below is of the PACKAGE
# ``interview_ui.progress_view``, which resolves only when ROOT is on the path.
# Without it this module imported only by accident of the working directory.
for directory in (ROOT, ROOT / "controller", ROOT / "interview_ui"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import nh_loop  # noqa: E402
from nh_supervisor import classify, engine  # noqa: E402
from interview_ui.progress_view import project_progress  # noqa: E402


def codex_stream(message):
    return (
        json.dumps(
            {
                "type": "item.completed",
                "item": {"type": "agent_message", "id": "m1", "text": message},
            },
            separators=(",", ":"),
        )
        + "\n"
        + json.dumps(
            {
                "type": "turn.completed",
                "usage": {
                    "input_tokens": 1,
                    "cached_input_tokens": 0,
                    "output_tokens": 1,
                    "reasoning_output_tokens": 0,
                },
            },
            separators=(",", ":"),
        )
        + "\n"
    ).encode()


def request(identity="pr_lifecycle_test"):
    return SimpleNamespace(
        provider_kind="gpt_question_validation",
        provider_endpoint_identity=nh_loop.SUPERVISOR_CODEX_ENDPOINT,
        provider_request_identity=identity,
        prompt_material_sha256="a" * 64,
        required_inputs_sha256="b" * 64,
    )


class FakeProcess:
    pid = 99999999

    def __init__(self, argv, *, stdout, stderr, returncode=0, out=b"", err=b"", **kwargs):
        self.returncode = returncode
        self.stdout_handle = stdout
        self.stderr_handle = stderr
        self.out = out
        self.err = err

    def communicate(self, input=None, timeout=None):
        self.stdout_handle.write(self.out)
        self.stderr_handle.write(self.err)
        return None, None


class ProviderLifecycleCaptureTests(unittest.TestCase):

    # SECOND-MODEL SWITCH (2026-09-02): these fixtures are Codex JSONL streams,
    # so the switch is held on "codex" for this class whatever is installed.
    def setUp(self):
        patcher = mock.patch.object(nh_loop, "SECOND_MODEL_PROVIDER", "codex")
        patcher.start()
        self.addCleanup(patcher.stop)

    def dispatch(self, *, returncode, out, err=b""):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        transport = nh_loop.NhCliProviderTransport(
            lambda: SimpleNamespace(state_dir=folder.name)
        )
        made = lambda argv, **kwargs: FakeProcess(
            argv, returncode=returncode, out=out, err=err, **kwargs
        )
        with mock.patch.object(nh_loop.subprocess, "Popen", side_effect=made), mock.patch.object(
            nh_loop.nh_supervisor.lease,
            "read_process_start_ticks",
            return_value=123,
        ), mock.patch.object(
            nh_loop.nh_supervisor.lease,
            "boot_id_sha256",
            return_value="c" * 64,
        ):
            observation = transport._dispatch_codex(
                request(),
                {},
                prompt="offline",
                launch_binding={"dispatch_event_seq": 7, "dispatch_event_sha256": "d" * 64},
            )
        fact = transport._read_codex_launch_fact("pr_lifecycle_test")
        return transport, observation, fact, Path(folder.name)

    def test_success_stream_is_directly_preserved_and_result_remains_usable(self):
        payload = '{"whole_check_complete":true}'
        _transport, observation, fact, root = self.dispatch(
            returncode=0, out=codex_stream(payload)
        )
        self.assertEqual(payload.encode(), observation.body)
        self.assertEqual("completed", fact["launch_state"])
        self.assertEqual(0, fact["provider_returncode"])
        self.assertTrue(fact["result_message_present"])
        stdout_path = root / nh_loop.CODEX_LAUNCH_ARTIFACT_DIRNAME / fact["stdout_artifact_name"]
        self.assertEqual(fact["stdout_sha256"], hashlib.sha256(stdout_path.read_bytes()).hexdigest())

    def test_nonzero_exit_preserves_stderr_and_is_a_terminal_local_failure(self):
        _transport, observation, fact, root = self.dispatch(
            returncode=17, out=b"", err=b"codex local failure\n"
        )
        self.assertEqual("local_process_failed", observation.transport_outcome)
        stderr_path = root / nh_loop.CODEX_LAUNCH_ARTIFACT_DIRNAME / fact["stderr_artifact_name"]
        self.assertEqual(b"codex local failure\n", stderr_path.read_bytes())
        facts = engine.build_provider_outcome_facts(
            observation,
            {"capability_record_sha256": "e" * 64, "provider_error_signal_map": []},
            0,
        )
        self.assertEqual("E8", classify.classify_provider_outcome(facts))

    def test_dead_parent_can_recover_a_complete_result_from_direct_stdout(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        transport = nh_loop.NhCliProviderTransport(
            lambda: SimpleNamespace(state_dir=folder.name)
        )
        req = request("pr_interrupted")
        stdout_path = Path(transport._codex_artifact_path(req.provider_request_identity, "stdout", create=True))
        stderr_path = Path(transport._codex_artifact_path(req.provider_request_identity, "stderr", create=True))
        stdout_path.write_bytes(codex_stream('{"saved":true}'))
        stderr_path.write_bytes(b"")
        os.chmod(stdout_path, 0o600)
        os.chmod(stderr_path, 0o600)
        transport._write_codex_launch_fact(
            req,
            launch_state="launched",
            launch_call_attempted=True,
            launch_succeeded=True,
            failure_stage=None,
            provider_pid=99999999,
            provider_process_start_ticks=123,
            boot_id="c" * 64,
            dispatch_binding={"dispatch_event_seq": 8, "dispatch_event_sha256": "f" * 64},
            stdout_artifact_name=stdout_path.name,
            stderr_artifact_name=stderr_path.name,
        )
        recovered = transport.recover_local_provider_observation(
            req, {"event_seq": 8, "event_sha256": "f" * 64}
        )
        self.assertEqual("result_found", recovered["state"])
        self.assertEqual(b'{"saved":true}', recovered["observation"].body)

    def test_a_dead_process_that_wrote_nothing_is_a_terminal_local_failure(self):
        """Ness, 2026-09-03 ("yes"): killing a run mid-call stranded B30 -- the request sat
        at dispatch_begun, the local CLI has no lookup, and the package needed a human.
        The child writes its OWN stdout artifact, so an EMPTY one plus a dead process is
        unambiguous: the call produced nothing.  A PARTIAL stream stays unknown (below)."""
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        transport = nh_loop.NhCliProviderTransport(
            lambda: SimpleNamespace(state_dir=folder.name)
        )
        req = request("pr_killed")
        stdout_path = Path(transport._codex_artifact_path(req.provider_request_identity, "stdout", create=True))
        stderr_path = Path(transport._codex_artifact_path(req.provider_request_identity, "stderr", create=True))
        stdout_path.write_bytes(b"")
        stderr_path.write_bytes(b"[claude-code:unrecognized_model]\n")
        os.chmod(stdout_path, 0o600)
        os.chmod(stderr_path, 0o600)
        transport._write_codex_launch_fact(
            req,
            launch_state="launched",
            launch_call_attempted=True,
            launch_succeeded=True,
            failure_stage=None,
            provider_pid=99999999,
            provider_process_start_ticks=123,
            boot_id="c" * 64,
            dispatch_binding={"dispatch_event_seq": 9, "dispatch_event_sha256": "1" * 64},
            stdout_artifact_name=stdout_path.name,
            stderr_artifact_name=stderr_path.name,
        )
        recovered = transport.recover_local_provider_observation(
            req, {"event_seq": 9, "event_sha256": "1" * 64}
        )
        self.assertEqual("terminal_local_failure", recovered["state"])
        self.assertIsNotNone(recovered.get("observation"))
        self.assertRegex(recovered["evidence_sha256"], r"^[0-9a-f]{64}$")

    def test_dead_process_without_complete_result_stays_honestly_unknown_with_evidence(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        transport = nh_loop.NhCliProviderTransport(
            lambda: SimpleNamespace(state_dir=folder.name)
        )
        req = request("pr_partial")
        stdout_path = Path(transport._codex_artifact_path(req.provider_request_identity, "stdout", create=True))
        stderr_path = Path(transport._codex_artifact_path(req.provider_request_identity, "stderr", create=True))
        stdout_path.write_bytes(b'{"type":"turn.started"}\n')
        stderr_path.write_bytes(b"connection ended\n")
        os.chmod(stdout_path, 0o600)
        os.chmod(stderr_path, 0o600)
        transport._write_codex_launch_fact(
            req,
            launch_state="launched",
            launch_call_attempted=True,
            launch_succeeded=True,
            failure_stage=None,
            provider_pid=99999999,
            provider_process_start_ticks=123,
            boot_id="c" * 64,
            dispatch_binding={"dispatch_event_seq": 9, "dispatch_event_sha256": "1" * 64},
            stdout_artifact_name=stdout_path.name,
            stderr_artifact_name=stderr_path.name,
        )
        recovered = transport.recover_local_provider_observation(
            req, {"event_seq": 9, "event_sha256": "1" * 64}
        )
        self.assertEqual("outcome_unknown", recovered["state"])
        self.assertRegex(recovered["evidence_sha256"], r"^[0-9a-f]{64}$")

    def test_event_1000_reconciliation_stop_is_not_reported_as_no_ness_request(self):
        events = [
            {
                "event_seq": 999,
                "type": "provider_request_reconciled",
                "package_id": "A19",
                "provider_request_identity": "pr_uncertain",
                "next_workflow_state": "NEEDS_USER_ACTION",
                "dependency_record": {
                    "user_action_code": "provider_outcome_confirmation_required"
                },
            },
            {"event_seq": 1000, "type": "supervisor_operation_completed", "package_id": "A19"},
        ]
        view = project_progress(
            events,
            {"pid": 123, "controller_executable_identity": "old"},
            "",
            alive=lambda *_: False,
            installed_controller_identity="new",
        )
        self.assertEqual("provider_reconciliation", view["needs_ness_kind"])
        self.assertIn("provider outcome", view["needs_ness"].lower())
        self.assertEqual("Provider outcome reconciliation stopped", view["stage"])
        self.assertFalse(view["worker_restart_required"])
        self.assertNotIn(
            "older-controller",
            view["question_path"]["questions_can_be_asked_when"],
        )
        self.assertFalse(view["question_path"]["ness_question_ready_record_exists"])


if __name__ == "__main__":
    unittest.main()

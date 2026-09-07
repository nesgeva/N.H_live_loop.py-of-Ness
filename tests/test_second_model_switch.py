"""The second-model switch (Ness, 2026-09-02, TEMPORARY).

Every checking provider role reaches its model through ONE argv builder and
ONE reply parser, selected by nh_loop.SECOND_MODEL_PROVIDER:
"codex" reproduces today's GPT-via-Codex command byte for byte; "claude" runs
the Claude CLI read-only on claude-opus-5 (1M window, 64k output; 2026-09-03).  Spec:
/home/ness/nh_audit_handoff/specs/2026-09-02-second-model-switch-design.md
"""
import json
import os
import re
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
for directory in (ROOT, ROOT / "controller", ROOT / "interview_ui"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import nh_loop  # noqa: E402

# Never let these tests write into the controller's persistent reply folder.
_CAPTURE_DIR = tempfile.TemporaryDirectory(prefix="nh_switch_tests_")
_REAL_CAPTURE_DIR = nh_loop.SECOND_MODEL_REPLY_CAPTURE_DIR
_PATCHES = (
    mock.patch.object(nh_loop, "SECOND_MODEL_REPLY_CAPTURE_DIR", _CAPTURE_DIR.name),
    mock.patch.object(nh_loop, "live_progress_log_path", lambda: os.path.join(_CAPTURE_DIR.name, "diary.log")),
)


def setUpModule():
    for patch in _PATCHES:
        patch.start()


def tearDownModule():
    for patch in _PATCHES:
        patch.stop()
    _CAPTURE_DIR.cleanup()


def switched(value):
    return mock.patch.object(nh_loop, "SECOND_MODEL_PROVIDER", value)


TODAYS_CODEX_ARGV = [
    "codex", "exec", "-m", nh_loop.CODEX_MODEL,
    "-c", 'model_reasoning_effort="%s"' % nh_loop.CODEX_REASONING_EFFORT,
    "-s", "read-only", "--ephemeral", "--json", "--color", "never",
    "-C", nh_loop.NH_REPO_PATH, "-",
]


class ArgvBuilder(unittest.TestCase):
    def test_the_switch_is_one_of_the_two_known_values(self):
        self.assertIn(nh_loop.SECOND_MODEL_PROVIDER, nh_loop.SECOND_MODEL_PROVIDERS)
        self.assertEqual(nh_loop.SECOND_MODEL_CLAUDE_MODEL, "claude-opus-5")

    def test_codex_form_is_todays_literal(self):
        with switched("codex"):
            self.assertEqual(nh_loop.second_model_argv(), TODAYS_CODEX_ARGV)

    def test_codex_form_schema_and_web_search_insertions(self):
        with switched("codex"):
            argv = nh_loop.second_model_argv(output_schema={"type": "object"}, web_search=True)
        self.assertEqual(argv[:3], ["codex", "--search", "exec"])
        i = argv.index("--output-schema")
        self.assertTrue(argv[i + 1].endswith(".json"))
        with open(argv[i + 1], encoding="utf-8") as handle:
            self.assertEqual(json.load(handle), {"type": "object"})
        os.unlink(argv[i + 1])
        self.assertEqual(argv[-3:], ["-C", nh_loop.NH_REPO_PATH, "-"])

    def test_claude_form_is_read_only_and_pinned(self):
        with switched("claude"):
            argv = nh_loop.second_model_argv(output_schema={"type": "object"})
        self.assertEqual(argv[:2], ["claude", "-p"])
        self.assertEqual(argv[argv.index("--model") + 1], "claude-opus-5")
        self.assertEqual(argv[argv.index("--effort") + 1], nh_loop.SECOND_MODEL_CLAUDE_EFFORT)
        self.assertEqual(argv[argv.index("--tools") + 1], nh_loop.CLAUDE_READ_TOOLS)
        self.assertEqual(
            argv[argv.index("--disallowed-tools") + 1],
            nh_loop.CLAUDE_ACCEPTANCE_EXPLANATION_DENIED_TOOLS,
        )
        for flag in ("--no-session-persistence", "--strict-mcp-config"):
            self.assertIn(flag, argv)
        self.assertEqual(argv[argv.index("--output-format") + 1], "json")
        self.assertEqual(argv[argv.index("--mcp-config") + 1], '{"mcpServers":{}}')
        self.assertEqual(json.loads(argv[argv.index("--json-schema") + 1]), {"type": "object"})
        self.assertNotIn("--add-dir", argv)
        self.assertNotIn("--permission-mode", argv)
        self.assertNotIn("Write", argv[argv.index("--tools") + 1])
        self.assertNotIn("Bash", argv[argv.index("--tools") + 1])

    def test_claude_form_without_schema_still_demands_one_json_object(self):
        with switched("claude"):
            argv = nh_loop.second_model_argv()
        self.assertEqual(json.loads(argv[argv.index("--json-schema") + 1]), {"type": "object"})
        self.assertNotIn("--output-schema", argv)
        with switched("claude"):
            smoke = nh_loop.second_model_argv(smoke=True)
        self.assertNotIn("--json-schema", smoke)

    def test_failed_claude_reply_is_described_and_saved(self):
        envelope = json.dumps({"type": "result", "subtype": "error_max_turns", "is_error": True,
                               "num_turns": 7, "result": "I could not finish because ..."})
        errors = []
        with switched("claude"):
            self.assertIsNone(nh_loop.extract_second_model_message(envelope, errors))
        self.assertEqual(len(errors), 1)
        self.assertIn("is_error=true", errors[0])
        self.assertIn("subtype=\"error_max_turns\"", errors[0])
        self.assertIn("result_head=", errors[0])
        saved = errors[0].split("saved=")[1].rstrip(")")
        self.assertTrue(os.path.exists(saved), saved)
        self.assertEqual(open(saved, encoding="utf-8").read(), envelope)
        self.assertEqual(oct(os.stat(saved).st_mode & 0o777), "0o600")
        os.unlink(saved)

    def test_unknown_provider_refuses(self):
        with switched("gemini"):
            with self.assertRaises(ValueError):
                nh_loop.second_model_argv()

    def test_executable_and_missing_text_follow_the_switch(self):
        with switched("codex"):
            self.assertEqual(nh_loop.second_model_executable(), "codex")
            self.assertEqual(nh_loop.second_model_missing_text(), "codex executable not found on PATH")
        with switched("claude"):
            self.assertEqual(nh_loop.second_model_executable(), "claude")
            self.assertEqual(nh_loop.second_model_missing_text(), "claude executable not found on PATH")


class ReplyParser(unittest.TestCase):
    def test_codex_form_delegates_to_the_installed_codex_parser(self):
        with switched("codex"), mock.patch.object(
            nh_loop, "extract_codex_agent_message", return_value='{"a":1}'
        ) as parser:
            errors = []
            self.assertEqual(nh_loop.extract_second_model_message("raw", errors), '{"a":1}')
        parser.assert_called_once_with("raw", errors)

    def test_claude_form_parses_one_envelope(self):
        envelope = json.dumps({
            "type": "result", "subtype": "success", "is_error": False,
            "result": "```json\n{\"a\":1}\n```",
        })
        with switched("claude"):
            self.assertEqual(nh_loop.extract_second_model_message(envelope, []), '{"a":1}')

    def test_claude_error_envelope_is_none_with_an_error(self):
        errors = []
        with switched("claude"):
            self.assertIsNone(nh_loop.extract_second_model_message(json.dumps({"is_error": True}), errors))
        self.assertTrue(errors)


class EndpointMap(unittest.TestCase):
    def test_endpoint_map_follows_the_switch(self):
        with switched("codex"):
            m = nh_loop.supervisor_endpoint_binding()
        self.assertEqual(m["gpt_question_validation"], nh_loop.SUPERVISOR_CODEX_ENDPOINT)
        self.assertEqual(m["codex_next_package_selection"], nh_loop.SUPERVISOR_CODEX_ENDPOINT)
        self.assertEqual(m["claude_initial_design"], nh_loop.SUPERVISOR_CLAUDE_ENDPOINT)
        with switched("claude"):
            m = nh_loop.supervisor_endpoint_binding()
        self.assertEqual(m["gpt_question_validation"], nh_loop.SUPERVISOR_SECOND_MODEL_CLAUDE_ENDPOINT)
        self.assertEqual(m["codex_next_package_selection"], nh_loop.SUPERVISOR_SECOND_MODEL_CLAUDE_ENDPOINT)
        self.assertEqual(m["claude_initial_design"], nh_loop.SUPERVISOR_CLAUDE_ENDPOINT)
        self.assertNotEqual(nh_loop.SUPERVISOR_SECOND_MODEL_CLAUDE_ENDPOINT, nh_loop.SUPERVISOR_CLAUDE_ENDPOINT)
        self.assertNotEqual(nh_loop.SUPERVISOR_SECOND_MODEL_CLAUDE_ENDPOINT, nh_loop.SUPERVISOR_CODEX_ENDPOINT)


TODAYS_CODEX_SMOKE_ARGV = [
    "codex", "exec", "--model", nh_loop.CODEX_MODEL,
    "-c", 'model_reasoning_effort="%s"' % nh_loop.CODEX_REASONING_EFFORT,
    "--sandbox", "read-only", "--ephemeral", "--cd", nh_loop.NH_REPO_PATH, "-",
]


class FakeCompleted(SimpleNamespace):
    pass


def fake_run(record):
    def run(argv, **kwargs):
        record.append((list(argv), dict(kwargs)))
        return FakeCompleted(returncode=0, stdout=b"", stderr=b"")
    return run


class SupervisorDispatch(unittest.TestCase):
    """_dispatch_codex builds its argv through the switch; capture pattern from
    interview_ui/test_provider_routing.py."""

    def capture(self, kind, endpoint):
        request = SimpleNamespace(
            provider_kind=kind,
            provider_endpoint_identity=endpoint,
            provider_request_identity="pr_offline_switch_probe",
            prompt_material_sha256="a" * 64,
            required_inputs_sha256="b" * 64,
        )
        material = {"result_schema_id": "offline_route_probe", "result_schema_version": 1}
        seen = {}

        class FakeProcess:
            pid = 99999999
            returncode = 0

            def __init__(self, argv, **kwargs):
                seen["argv"] = list(argv)
                seen["kwargs"] = dict(kwargs)

            def communicate(self, input=None, timeout=None):
                return b"", b""

        with tempfile.TemporaryDirectory() as folder:
            transport = nh_loop.NhCliProviderTransport(lambda: SimpleNamespace(state_dir=folder))
            with mock.patch.object(nh_loop.subprocess, "Popen", FakeProcess):
                transport._dispatch_codex(request, material)
        return seen["argv"]

    def test_codex_switch_keeps_the_installed_argv_and_schema_file(self):
        with switched("codex"):
            argv = self.capture("gpt_question_validation", nh_loop.SUPERVISOR_CODEX_ENDPOINT)
            self.assertEqual(argv[:2], ["codex", "exec"])
            self.assertIn("--output-schema", argv)
            audit = self.capture("codex_design_audit", nh_loop.SUPERVISOR_CODEX_ENDPOINT)
            self.assertEqual(audit[:3], ["codex", "--search", "exec"])

    def test_claude_switch_runs_the_claude_cli_with_an_inline_schema(self):
        with switched("claude"):
            argv = self.capture("gpt_question_validation", nh_loop.SUPERVISOR_SECOND_MODEL_CLAUDE_ENDPOINT)
            self.assertEqual(argv[:2], ["claude", "-p"])
            self.assertIn("--json-schema", argv)
            self.assertNotIn("--output-schema", argv)
            self.assertNotIn("--add-dir", argv)
            audit = self.capture("codex_design_audit", nh_loop.SUPERVISOR_SECOND_MODEL_CLAUDE_ENDPOINT)
            self.assertNotIn("standalone_web_search", audit)


class LegacyLaunchers(unittest.TestCase):
    LAUNCHERS = (
        ("run_codex_next_package", ()),
        ("run_codex_prepare_task", ("prompt",)),
        ("run_codex_design_audit", ("prompt",)),
        ("run_codex_correction_specification", ("prompt",)),
        ("run_codex_claude_stop_review", ("prompt",)),
        ("run_codex_question_validation", ("prompt",)),
    )

    def launch(self, name, args):
        record = []
        with mock.patch.object(nh_loop.subprocess, "run", fake_run(record)):
            getattr(nh_loop, name)(*args, [])
        self.assertEqual(len(record), 1, name)
        return record[0]

    def test_codex_switch_reproduces_each_installed_argv(self):
        with switched("codex"):
            for name, args in self.LAUNCHERS:
                argv, kwargs = self.launch(name, args)
                expected = list(TODAYS_CODEX_ARGV)
                if name == "run_codex_design_audit":
                    expected[1:1] = ["--search"]
                self.assertEqual(argv, expected, name)
                self.assertEqual(kwargs["cwd"], nh_loop.NH_REPO_PATH)
                self.assertIs(kwargs["shell"], False)
            argv, _ = self.launch("run_codex_smoke", ())
            self.assertEqual(argv, TODAYS_CODEX_SMOKE_ARGV)

    def test_claude_switch_runs_the_claude_cli_for_each_launcher(self):
        with switched("claude"):
            for name, args in self.LAUNCHERS:
                argv, kwargs = self.launch(name, args)
                self.assertEqual(argv[:2], ["claude", "-p"], name)
                self.assertEqual(argv[argv.index("--model") + 1], "claude-opus-5", name)
                self.assertEqual(argv[argv.index("--output-format") + 1], "json", name)
                self.assertEqual(kwargs["cwd"], nh_loop.NH_REPO_PATH)
            argv, _ = self.launch("run_codex_smoke", ())
            self.assertEqual(argv[:2], ["claude", "-p"])
            self.assertEqual(argv[argv.index("--output-format") + 1], "text")

    def test_missing_executable_message_names_the_selected_program(self):
        def missing(argv, **kwargs):
            raise FileNotFoundError(argv[0])
        for value, program in (("codex", "codex"), ("claude", "claude")):
            with switched(value), mock.patch.object(nh_loop.subprocess, "run", missing):
                errors = []
                invoked, code, out = nh_loop.run_codex_question_validation("p", errors)
            self.assertFalse(invoked)
            self.assertEqual(errors, ["%s executable not found on PATH" % program])

    def test_question_validation_ignores_the_checkpoint_under_claude(self):
        record = []

        def never(*args, **kwargs):
            raise AssertionError("resumable Codex review must not run under claude")

        with switched("claude"), mock.patch.object(
            nh_loop, "run_resumable_codex_review", never
        ), mock.patch.object(nh_loop.subprocess, "run", fake_run(record)):
            nh_loop.run_codex_question_validation("prompt", [], checkpoint="/tmp/nh-nonexistent-checkpoint.json")
        self.assertEqual(len(record), 1)
        self.assertEqual(record[0][0][:2], ["claude", "-p"])

    def test_question_validation_still_resumes_under_codex(self):
        called = []
        with switched("codex"), mock.patch.object(
            nh_loop, "run_resumable_codex_review", lambda p, e, c: called.append(c) or (True, 0, "")
        ):
            nh_loop.run_codex_question_validation("prompt", [], checkpoint="/tmp/x.json")
        self.assertEqual(called, ["/tmp/x.json"])


class ParseSites(unittest.TestCase):
    def test_every_second_model_parse_site_uses_the_switched_parser(self):
        source = open(nh_loop.__file__, encoding="utf-8").read()
        # The def, and the single delegating call inside extract_second_model_message.
        self.assertEqual(len(re.findall(r"extract_codex_agent_message\(", source)), 2)
        self.assertGreaterEqual(len(re.findall(r"extract_second_model_message\(", source)), 12)


class PreflightAndInterfaceGate(unittest.TestCase):
    def test_preflight_requires_codex_only_under_the_codex_switch(self):
        with switched("codex"):
            self.assertEqual(
                nh_loop.required_provider_executables(),
                (("claude_found", "claude"), ("codex_found", "codex")),
            )
        with switched("claude"):
            self.assertEqual(
                nh_loop.required_provider_executables(),
                (("claude_found", "claude"),),
            )

    def _production(self):
        import production  # interview_ui is on sys.path
        return production

    def test_interface_gate_skips_codex_under_the_claude_switch(self):
        production = self._production()
        calls = []

        def run(argv, **kwargs):
            calls.append(list(argv))
            if argv[0] == "codex":
                raise AssertionError("codex must not be consulted under the claude switch")
            return SimpleNamespace(
                returncode=0, stdout=json.dumps({"loggedIn": True, "authMethod": "claude.ai"}), stderr=""
            )

        with mock.patch.object(production, "second_model_provider", lambda: "claude"):
            result = production.verify_provider_authentication(run=run)
        self.assertEqual(result, {"codex": "NOT_REQUIRED_SECOND_MODEL_CLAUDE", "claude": "CURRENT_SUBSCRIPTION"})
        self.assertEqual(calls, [["claude", "auth", "status", "--json"]])

    def test_interface_gate_still_demands_codex_under_the_codex_switch(self):
        production = self._production()

        def run(argv, **kwargs):
            if argv[0] == "codex":
                return SimpleNamespace(returncode=0, stdout="", stderr="Logged in using ChatGPT\n")
            return SimpleNamespace(
                returncode=0, stdout=json.dumps({"loggedIn": True, "authMethod": "claude.ai"}), stderr=""
            )

        with mock.patch.object(production, "second_model_provider", lambda: "codex"):
            result = production.verify_provider_authentication(run=run)
        self.assertEqual(result, {"codex": "CHATGPT_LOGIN", "claude": "CURRENT_SUBSCRIPTION"})

        def not_logged_in(argv, **kwargs):
            return SimpleNamespace(returncode=1, stdout="", stderr="")

        with mock.patch.object(production, "second_model_provider", lambda: "codex"):
            with self.assertRaises(production.ProductionLaunchError):
                production.verify_provider_authentication(run=not_logged_in)

    def test_interface_reads_the_switch_from_the_controller(self):
        production = self._production()
        with switched("claude"):
            self.assertEqual(production.second_model_provider(), "claude")
        with switched("codex"):
            self.assertEqual(production.second_model_provider(), "codex")


class ReauditFixes(unittest.TestCase):
    def test_recovery_readers_accept_both_local_cli_endpoints(self):
        self.assertEqual(
            nh_loop.LOCAL_CLI_SECOND_MODEL_ENDPOINTS,
            frozenset((nh_loop.SUPERVISOR_CODEX_ENDPOINT, nh_loop.SUPERVISOR_SECOND_MODEL_CLAUDE_ENDPOINT)),
        )
        import inspect
        for name in ("prove_local_provider_process_not_launched", "recover_local_provider_observation"):
            source = inspect.getsource(getattr(nh_loop.NhCliProviderTransport, name))
            self.assertNotIn('"local_codex_cli_chatgpt"', source, name)
            self.assertIn("LOCAL_CLI_SECOND_MODEL_ENDPOINTS", source, name)

    def test_recovery_reads_the_launch_fact_for_a_second_model_request(self):
        calls = []
        with tempfile.TemporaryDirectory() as folder:
            transport = nh_loop.NhCliProviderTransport(lambda: SimpleNamespace(state_dir=folder))
            with mock.patch.object(
                nh_loop.NhCliProviderTransport, "_read_codex_launch_fact",
                lambda self, identity: calls.append(identity) or None,
            ):
                for endpoint, expected in (
                    (nh_loop.SUPERVISOR_SECOND_MODEL_CLAUDE_ENDPOINT, ["pr_second"]),
                    (nh_loop.SUPERVISOR_CODEX_ENDPOINT, ["pr_second", "pr_codex"]),
                    ("somewhere_else", ["pr_second", "pr_codex"]),
                ):
                    prepared = SimpleNamespace(
                        provider_endpoint_identity=endpoint,
                        provider_request_identity="pr_second" if "second" in endpoint else ("pr_codex" if "codex" in endpoint else "pr_other"),
                    )
                    self.assertIsNone(transport.recover_local_provider_observation(prepared, None))
                    self.assertEqual(calls, expected)

    def test_checkpoint_cleanup_only_on_the_codex_form(self):
        source = open(nh_loop.__file__, encoding="utf-8").read()
        self.assertEqual(source.count('second_model_executable() == "codex" and not clear_codex_review_checkpoint('), 2)

    def test_second_model_label_follows_the_switch(self):
        with switched("codex"):
            self.assertEqual(nh_loop.second_model_label(), ("codex", nh_loop.CODEX_MODEL, nh_loop.CODEX_REASONING_EFFORT))
        with switched("claude"):
            self.assertEqual(nh_loop.second_model_label(), ("claude", "claude-opus-5", nh_loop.SECOND_MODEL_CLAUDE_EFFORT))

    def test_operator_text_no_longer_claims_claude_is_not_invoked(self):
        source = open(nh_loop.__file__, encoding="utf-8").read()
        self.assertNotIn('"  claude:      not invoked"', source)
        self.assertNotIn("invokes Claude never", source)
        self.assertNotIn('"  [%s] codex invoked (exactly once, never retried)"', source)


class FailureCapture(unittest.TestCase):
    def test_nonzero_exit_saves_both_streams_and_reports_their_heads(self):
        def failing(argv, **kwargs):
            return FakeCompleted(returncode=1, stdout=b'{"is_error":true,"result":"Failed to authenticate"}', stderr=b"[claude-code:unrecognized_model] x\n")
        errors = []
        with switched("claude"), mock.patch.object(nh_loop.subprocess, "run", failing):
            invoked, code, out = nh_loop.run_codex_question_validation("p", errors)
        self.assertTrue(invoked); self.assertEqual(code, 1)
        self.assertEqual(len(errors), 1)
        self.assertIn("claude exited with code 1", errors[0])
        self.assertIn("Failed to authenticate", errors[0])
        self.assertIn("unrecognized_model", errors[0])
        for label in ("stdout_saved=", "stderr_saved="):
            path = errors[0].split(label)[1].split(";")[0].rstrip(")")
            self.assertTrue(os.path.exists(path), path); os.unlink(path)


class AlwaysSaved(unittest.TestCase):
    def test_capture_dir_is_persistent_and_outside_the_governed_repo(self):
        d = _REAL_CAPTURE_DIR
        self.assertFalse(d.startswith("/tmp"))
        self.assertFalse(d.startswith(nh_loop.NH_REPO_PATH))
        self.assertTrue(d.startswith(os.path.dirname(nh_loop.NH_REPO_PATH)))

    def test_a_successful_reply_is_saved_before_it_is_judged(self):
        envelope = json.dumps({"type": "result", "subtype": "success", "is_error": False, "result": "{\"a\":1}"})
        with tempfile.TemporaryDirectory() as folder, switched("claude"), mock.patch.object(
            nh_loop, "SECOND_MODEL_REPLY_CAPTURE_DIR", folder
        ):
            self.assertEqual(nh_loop.extract_second_model_message(envelope, []), '{"a":1}')
            files = os.listdir(folder)
            self.assertEqual(len(files), 1)
            self.assertEqual(open(os.path.join(folder, files[0]), encoding="utf-8").read(), envelope)
            self.assertEqual(oct(os.stat(os.path.join(folder, files[0])).st_mode & 0o777), "0o600")


class LiveDiary(unittest.TestCase):
    def test_diary_lives_beside_the_interview_state_dir(self):
        with mock.patch.dict(os.environ, {"NH_LOOP_INTERVIEW_STATE_DIR": "/x/y/nh_interview_state"}):
            path = nh_loop.live_progress_log_path.__wrapped__() if hasattr(nh_loop.live_progress_log_path, "__wrapped__") else None
        # the module patch replaces the function; check the real one on its source instead
        import inspect
        source = inspect.getsource(nh_loop).split("def live_progress_log_path():")[1].split("def live_log")[0]
        self.assertIn("NH_LOOP_INTERVIEW_STATE_DIR", source)
        self.assertIn("LIVE_PROGRESS_LOG_BASENAME", source)
        self.assertEqual(nh_loop.LIVE_PROGRESS_LOG_BASENAME, "nh_live_progress.log")

    def test_live_log_appends_timestamped_lines_and_never_raises(self):
        path = nh_loop.live_progress_log_path()
        before = len(open(path, encoding="utf-8").read().splitlines()) if os.path.exists(path) else 0
        nh_loop.live_log("first   line\nwith   noise")
        nh_loop.live_log("second")
        with open(path, encoding="utf-8") as handle:
            lines = handle.read().splitlines()[before:]
        self.assertEqual(len(lines), 2)
        self.assertRegex(lines[0], r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}  first line with noise$")
        self.assertEqual(oct(os.stat(path).st_mode & 0o777), "0o600")
        with mock.patch.object(nh_loop, "live_progress_log_path", lambda: "/proc/nonexistent/diary.log"):
            nh_loop.live_log("must not raise")

    def test_a_launcher_call_writes_start_and_end_lines(self):
        path = nh_loop.live_progress_log_path()
        before = len(open(path, encoding="utf-8").read().splitlines()) if os.path.exists(path) else 0

        def run(argv, **kwargs):
            return FakeCompleted(returncode=0, stdout=b"", stderr=b"")

        with switched("claude"), mock.patch.object(nh_loop.subprocess, "run", run):
            nh_loop.run_codex_question_validation("p", [])
        with open(path, encoding="utf-8") as handle:
            lines = handle.read().splitlines()[before:]
        self.assertEqual(len(lines), 2)
        self.assertIn("call start: claude claude-opus-5", lines[0])
        self.assertIn("call end: claude exit 0", lines[1])


if __name__ == "__main__":
    unittest.main()

class OneShotBatchTimeout(unittest.TestCase):
    """2026-09-03 02:50: the one-shot Bundle Seven batch was killed by the launcher's own
    65-minute per-command timeout (sized for ONE model call).  The batch form must run the
    controller without that limit; the lease heartbeat is what proves liveness."""

    def make_runner(self, factory, **kwargs):
        import production  # interview_ui is on sys.path
        seen = {}

        def run(argv, **run_kwargs):
            seen["timeout"] = run_kwargs.get("timeout")
            return SimpleNamespace(returncode=0, stdout='{"ok": true, "errors": []}', stderr="")

        runner = factory(production, run=run, **kwargs)
        with mock.patch.object(production.server, "parse_controller_report", lambda text: {"ok": True, "errors": []}):
            runner("supervisor-status", None)
        return production, seen

    def test_the_default_runner_keeps_the_single_command_timeout(self):
        production, seen = self.make_runner(lambda p, **kw: p.WorkerControllerRunner(**kw))
        self.assertEqual(seen["timeout"], production.WORKER_CONTROLLER_TIMEOUT_SECONDS)
        self.assertEqual(production.WORKER_CONTROLLER_TIMEOUT_SECONDS, 3900)

    def test_the_one_shot_batch_runner_has_no_timeout(self):
        production, seen = self.make_runner(lambda p, **kw: p.one_shot_batch_runner(**kw))
        self.assertIsNone(seen["timeout"])

class CoverageReviewOutputSchema(unittest.TestCase):
    """2026-09-03 02:37 and 12:53: on the Claude path a coverage review was launched with
    the bare {"type": "object"} schema and came back with every value as a STRING
    ("true", "[...]"), so the controller refused it as result_invalid (journal 2325/2326)
    and paid again.  Validation calls already get a typed schema; coverage reviews must too."""

    def test_the_coverage_schema_types_every_key_and_passes_the_shape_checker(self):
        schema = nh_loop.question_coverage_review_model_output_schema()
        self.assertEqual(nh_loop.codex_structured_output_schema_errors(schema), [])
        props = schema["properties"]
        self.assertEqual(set(props), nh_loop.COVERAGE_REVIEW_REQUIRED_KEYS)
        self.assertEqual(props["whole_check_complete"]["type"], "boolean")
        self.assertEqual(props["coverage_review_complete"]["type"], "boolean")
        for key in ("source_paths_checked", "unknowns"):
            self.assertEqual(props[key]["type"], "array")
            self.assertEqual(props[key]["items"]["type"], "string")
        gap = props["possible_gaps"]
        self.assertEqual(gap["type"], "array")
        self.assertEqual(gap["items"]["type"], "object")
        self.assertEqual(gap["items"]["properties"]["direction"]["enum"], ["missing", "over_ask"])

    def test_the_supervised_transport_picks_a_typed_schema_for_both_piece3_kinds(self):
        self.assertEqual(
            nh_loop.supervisor_output_schema_for_kind("gpt_question_coverage_review"),
            nh_loop.question_coverage_review_model_output_schema(),
        )
        self.assertEqual(
            nh_loop.supervisor_output_schema_for_kind("gpt_question_validation"),
            nh_loop.question_validation_model_output_schema(),
        )
        self.assertEqual(
            nh_loop.supervisor_output_schema_for_kind("gpt_question_validation", {"output_schema": {"type": "object"}}),
            {"type": "object"},
        )
        self.assertIsNone(nh_loop.supervisor_output_schema_for_kind("codex_design_audit"))

class CoverageTitleBound(unittest.TestCase):
    """2026-09-03 13:29: a 29-minute coverage review was refused for exactly three gap
    titles of 209-212 characters against a 200-character bound the prompt never stated.
    Ness ("1 and 2"): tell the checker the numbers, and relax the title bound to 300."""

    def test_the_title_bound_is_300(self):
        self.assertEqual(nh_loop.BINDING_MAX_TITLE_CHARS, 300)

    def test_a_250_character_signal_title_is_accepted(self):
        real = "01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md"  # a real governed file
        signal = {"issue_key": "k1", "finding_key": "f1", "signal_title": "t" * 250,
                  "finding_evidence": ["evidence line"], "source_evidence": [real]}
        errors = []
        out = nh_loop.validate_review_signal(signal, "the test signal", [real], errors)
        self.assertEqual(errors, [], errors)
        self.assertIsNotNone(out)

    def test_the_coverage_prompt_states_the_numbers(self):
        tail = nh_loop.COVERAGE_REVIEW_PROMPT_TAIL
        self.assertIn("at most 300 characters", tail)
        self.assertIn("at most 600 characters", tail)

class RecordedRefusals(unittest.TestCase):
    """Ness, 2026-09-03 ("accepted for fixing", options A and E of the root-cause report):
    A) a refused checker reply's validator reasons are RECORDED (the supervisor computed them
    as "schema_problems" and dropped them); E) a package stage stops after a bounded number
    of refused replies WITH recorded reasons, whatever the provider episode."""

    def make_transport(self, tmp, scope="B30"):
        import inspect
        context = SimpleNamespace(state_dir=tmp, binding=SimpleNamespace(package_scope_id=scope))
        return nh_loop.NhCliProviderTransport(lambda: context)

    def prepared(self, rid="pr_test1", kind="coverage_review"):
        return SimpleNamespace(provider_request_identity=rid, provider_kind="gpt_question_coverage_review", work_item_kind=kind)

    def test_a_refusal_is_recorded_with_its_reasons_and_in_the_diary(self):
        with tempfile.TemporaryDirectory() as tmp:
            transport = self.make_transport(tmp)
            diary = os.path.join(tmp, "diary.log")
            with mock.patch.object(nh_loop, "live_progress_log_path", lambda: diary), \
                 mock.patch.dict(os.environ, {"NH_LOOP_LIVE_LOG": "1"}):
                path = transport.record_result_refusal(self.prepared(), {"schema_problems": ["title too long", "second reason"]})
            self.assertTrue(os.path.isfile(path))
            record = json.load(open(path))
            self.assertEqual(record["problems"], ["title too long", "second reason"])
            self.assertEqual((record["package_scope_id"], record["work_item_kind"], record["provider_request_identity"]), ("B30", "coverage_review", "pr_test1"))
            self.assertEqual(transport.refused_request_identities("B30", "coverage_review"), {"pr_test1": ["title too long", "second reason"]})
            self.assertEqual(transport.refused_request_identities("B30", "question_validation"), {})
            self.assertIn("REFUSED", open(diary).read())

    def test_the_supervisor_result_path_records_a_refusal(self):
        import inspect
        import nh_supervisor.commands as commands
        seen = []
        provider = SimpleNamespace(record_result_refusal=lambda prepared, admission: seen.append((prepared, admission)))
        context = SimpleNamespace(provider=provider)
        commands.record_result_refusal_if_possible(context, "PREPARED", {"schema_problems": ["x"]})
        self.assertEqual(seen, [("PREPARED", {"schema_problems": ["x"]})])
        commands.record_result_refusal_if_possible(SimpleNamespace(provider=object()), "P", {})  # no recorder: no error
        self.assertIn("record_result_refusal_if_possible", inspect.getsource(commands._observe_and_close))

    def test_explained_invalid_replies_are_counted_per_current_package_stage_window(self):
        def custody(seq, scope, kind, rid, valid):
            return {"event_seq": seq, "type": "provider_result_custody_recorded", "package_scope_id": scope,
                    "work_item_kind": kind, "provider_request_identity": rid, "result_schema_valid": valid}
        events = [custody(1, "B30", "coverage_review", "pr_a", False), custody(2, "B30", "coverage_review", "pr_b", False),
                  custody(3, "B30", "coverage_review", "pr_c", True), custody(4, "A19", "coverage_review", "pr_d", False),
                  custody(5, "B30", "question_validation", "pr_e", False)]
        explained = {"pr_a": ["r1"], "pr_b": ["r2"], "pr_d": ["r3"], "pr_e": ["r4"]}
        hits = nh_loop.bundle_seven_explained_invalid_replies(events, "B30", "coverage_review", explained)
        self.assertEqual([h["provider_request_identity"] for h in hits], ["pr_a", "pr_b"])
        self.assertEqual(nh_loop.bundle_seven_explained_invalid_replies(events, "B30", "coverage_review", {}), [])
        self.assertEqual(nh_loop.BUNDLE_SEVEN_STAGE_INVALID_REPLY_CAP, 3)
        import inspect
        self.assertIn("BUNDLE_SEVEN_STAGE_INVALID_REPLY_CAP", inspect.getsource(nh_loop.run_supervised_bundle_seven_question_validation))

    def test_validation_page_success_resets_the_invalid_reply_budget(self):
        def custody(seq, rid):
            return {
                "event_seq": seq,
                "type": "provider_result_custody_recorded",
                "package_scope_id": "A19",
                "work_item_kind": "question_validation",
                "provider_request_identity": rid,
                "result_schema_valid": False,
            }

        events = [
            custody(10, "part3_bad"),
            {
                "event_seq": 20,
                "type": "validation_recorded",
                "package_scope_id": "A19",
                "page_index": 3,
                "page_count": 4,
            },
            custody(30, "part4_bad_1"),
            custody(40, "part4_bad_2"),
        ]
        explained = {
            "part3_bad": ["old page"],
            "part4_bad_1": ["current page first"],
            "part4_bad_2": ["current page second"],
        }
        hits = nh_loop.bundle_seven_explained_invalid_replies(
            events, "A19", "question_validation", explained
        )
        self.assertEqual(
            [event["provider_request_identity"] for event in hits],
            ["part4_bad_1", "part4_bad_2"],
        )

    def test_the_second_title_cap_follows_the_first(self):
        self.assertEqual(nh_loop.NESS_QUESTION_TITLE_MAX_CHARS, nh_loop.BINDING_MAX_TITLE_CHARS)

class OutputTokenCeiling(unittest.TestCase):
    """A20 page 2 (2026-09-03 14:56) died: "Claude's response exceeded the 32000 output
    token maximum ... set the CLAUDE_CODE_MAX_OUTPUT_TOKENS environment variable"."""

    def test_the_second_model_subprocess_carries_the_output_ceiling(self):
        import inspect
        src = inspect.getsource(nh_loop.NhCliProviderTransport._dispatch_codex)
        self.assertIn("CLAUDE_CODE_MAX_OUTPUT_TOKENS", src)
        self.assertEqual(nh_loop.SECOND_MODEL_MAX_OUTPUT_TOKENS, "64000")


class OverlongTitleAdjusted(unittest.TestCase):
    """Ness, 2026-09-03 ("both"): a coverage finding whose title overruns the bound is
    RECORDED with a shortened title and its full text kept as evidence, instead of the
    whole review being refused.  An unsafe title is still refused."""

    PATH = "01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md"

    def gap(self, title):
        return {"direction": "over_ask", "issue_key": "q_1", "finding_key": "f_1",
                "signal_title": title, "finding_evidence": ["why this is an over-ask"],
                "source_evidence": [self.PATH]}

    def check(self, title):
        errors = []
        with tempfile.TemporaryDirectory() as tmp:
            diary = os.path.join(tmp, "diary.log")
            with mock.patch.object(nh_loop, "live_progress_log_path", lambda: diary), \
                 mock.patch.dict(os.environ, {"NH_LOOP_LIVE_LOG": "1"}):
                entry = nh_loop.validate_coverage_review_gap(
                    self.gap(title), "the test gap", [self.PATH],
                    {"q_1": {"question_id": "q_1"}}, {"q_1"}, errors)
            written = open(diary).read() if os.path.isfile(diary) else ""
        return entry, errors, written

    def test_an_overlong_title_is_shortened_and_its_full_text_kept(self):
        title = "T" * 397
        entry, errors, diary = self.check(title)
        self.assertEqual(errors, [], errors)
        self.assertIsNotNone(entry)
        self.assertEqual(len(entry["signal_title"]), nh_loop.BINDING_MAX_TITLE_CHARS)
        self.assertTrue(title.startswith(entry["signal_title"]))
        self.assertIn(title, entry["finding_evidence"])
        self.assertIn("title shortened", diary)

    def test_a_shortened_title_never_ends_in_a_space(self):
        # Real data (B30 coverage, 2026-09-03 14:24): two of the eight overlong titles
        # were 305 and 307 characters, so the cut at 300 landed on a space and the
        # shortened title was still refused as "not one bounded plain line".
        title = "T" * 299 + " " + "X" * 10
        entry, errors, _ = self.check(title)
        self.assertEqual(errors, [], errors)
        self.assertEqual(entry["signal_title"], "T" * 299)
        self.assertIn(title, entry["finding_evidence"])

    def test_a_title_within_the_bound_is_untouched(self):
        title = "T" * 120
        entry, errors, diary = self.check(title)
        self.assertEqual(errors, [], errors)
        self.assertEqual(entry["signal_title"], title)
        self.assertEqual(entry["finding_evidence"], ["why this is an over-ask"])
        self.assertNotIn("title shortened", diary)

    def test_an_unsafe_title_is_still_refused(self):
        entry, errors, _ = self.check("line one\nline two")
        self.assertIsNone(entry)
        self.assertTrue(errors)

#!/usr/bin/env python3
"""Offline proof of the corrected Codex provider route.

Nothing here launches a process, opens a socket, opens a browser, starts the
worker, or calls either module's ``main``.  Every subprocess boundary is
serviced by an explicit fake; the real spawn entry points are replaced for the
whole module by guards that fail the test if anything reaches them.

What is proved:

* production authentication now proves ONE bounded ``codex login status`` run
  whose STDOUT OR STDERR carries one whole stripped line exactly equal to
  ``Logged in using ChatGPT``, and fails closed on every other route.  The
  installed CLI reports that line on stderr with an empty stdout, so a
  stdout-only check rejected a correct ChatGPT login;
* it needs no ``OPENROUTER_API_KEY``, no ``OPENAI_API_KEY``, and never reads
  ``openrouter.config.toml``;
* the existing Claude subscription check is unchanged in meaning;
* the live supervisor Codex argv is the ChatGPT-CLI argv -- ``gpt-5.6-sol`` at
  reasoning effort ``high``, read-only, ephemeral, JSON, in NH-GOVERNANCE --
  and carries no ``--profile`` and no OpenRouter reference;
* no live Codex invocation function in the controller still forces a profile;
* the Claude route's model, effort, tools, permission mode, MCP configuration
  and disposable-workspace refusal are untouched.
"""

from __future__ import annotations

import builtins
import inspect
import io
import os
import socket
import subprocess
import sys
import tempfile
import unittest
import webbrowser
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

sys.dont_write_bytecode = True

APP_DIR = Path(__file__).resolve().parent
ROOT_DIR = APP_DIR.parent
CONTROLLER_DIR = ROOT_DIR / "controller"
CONTROLLER_SOURCE_PATH = CONTROLLER_DIR / "nh_loop.py"
NH_REPO_PATH = str(ROOT_DIR / "NH-GOVERNANCE")

for _entry in (str(APP_DIR), str(CONTROLLER_DIR)):
    if _entry not in sys.path:
        sys.path.insert(0, _entry)

import production  # noqa: E402  -- import only; main() is never called
import nh_loop  # noqa: E402  -- import only; main() is never called


CODEX_STATUS_ARGV = ("codex", "login", "status")
CLAUDE_STATUS_ARGV = ("claude", "auth", "status", "--json")

# What the installed CLI actually reports: return code 0, EMPTY stdout, and the
# proof line on stderr.  Reading stdout alone rejected a correct ChatGPT login.
CHATGPT_PROOF = "Logged in using ChatGPT"
CODEX_REAL_LOGIN = SimpleNamespace(returncode=0, stdout="", stderr=CHATGPT_PROOF + "\n")
API_KEY_LOGIN_TEXT = "Logged in using an API key\n"
NOT_LOGGED_IN_TEXT = "Not logged in. Run `codex login`.\n"
CLAUDE_SUBSCRIPTION_STDOUT = '{"loggedIn": true, "authMethod": "claude.ai"}'

CREDENTIAL_ENV_KEYS = ("OPENROUTER_API_KEY", "OPENAI_API_KEY", "ANTHROPIC_API_KEY")

# The live Codex invocation functions this correction had to reach.
LIVE_CODEX_INVOCATIONS = (
    "run_codex_smoke",
    "run_codex_next_package",
    "run_codex_prepare_task",
    "run_codex_design_audit",
    "run_codex_correction_specification",
    "run_codex_claude_stop_review",
    "run_codex_question_validation",
)


class UnexpectedProcessLaunch(AssertionError):
    """Something tried to reach a real process, socket or browser."""


def _forbid(label):
    def guard(*args, **kwargs):
        raise UnexpectedProcessLaunch(
            "%s was reached with %r -- this suite services every subprocess "
            "boundary with an explicit fake" % (label, args[:1])
        )

    return guard


_GUARDED = (
    (subprocess, "run"),
    (subprocess, "Popen"),
    (subprocess, "call"),
    (subprocess, "check_call"),
    (subprocess, "check_output"),
    (os, "system"),
    (os, "popen"),
    (os, "posix_spawn"),
    (os, "posix_spawnp"),
    (os, "execv"),
    (os, "execve"),
    (os, "execvp"),
    (os, "fork"),
    (socket, "socket"),
    (socket, "create_connection"),
    (webbrowser, "open"),
    (webbrowser, "open_new"),
)

_PATCHERS = []


_SECOND_MODEL_PATCHES = []


def setUpModule():
    # SECOND-MODEL SWITCH (2026-09-02): this module proves the ChatGPT-CLI route,
    # so it runs with the controller's switch held on "codex" whatever the
    # installed value is.  tests/test_second_model_switch.py proves the switch.
    for patcher in (
        mock.patch.object(nh_loop, "SECOND_MODEL_PROVIDER", "codex"),
        mock.patch.object(production, "second_model_provider", lambda: "codex"),
    ):
        patcher.start()
        _SECOND_MODEL_PATCHES.append(patcher)
    for target, attribute in _GUARDED:
        if not hasattr(target, attribute):
            continue
        patcher = mock.patch.object(
            target, attribute, _forbid("%s.%s" % (target.__name__, attribute))
        )
        patcher.start()
        _PATCHERS.append(patcher)


def tearDownModule():
    while _SECOND_MODEL_PATCHES:
        _SECOND_MODEL_PATCHES.pop().stop()
    while _PATCHERS:
        _PATCHERS.pop().stop()


class FakeRun:
    """A ``subprocess.run`` stand-in that services only scripted argv."""

    def __init__(self, responses):
        self.responses = dict(responses)
        self.calls = []

    def __call__(self, argv, **kwargs):
        key = tuple(argv)
        self.calls.append(SimpleNamespace(argv=list(argv), kwargs=dict(kwargs)))
        if key not in self.responses:
            raise UnexpectedProcessLaunch("unscripted subprocess argv: %r" % (key,))
        outcome = self.responses[key]
        if isinstance(outcome, BaseException):
            raise outcome
        return outcome

    @property
    def argv_list(self):
        return [call.argv for call in self.calls]


def completed(returncode=0, stdout="", stderr=""):
    return SimpleNamespace(returncode=returncode, stdout=stdout, stderr=stderr)


def chatgpt_and_claude(codex=None, claude=None):
    """The scripted happy path both providers report today."""
    return FakeRun(
        {
            CODEX_STATUS_ARGV: CODEX_REAL_LOGIN if codex is None else codex,
            CLAUDE_STATUS_ARGV: (
                completed(0, CLAUDE_SUBSCRIPTION_STDOUT) if claude is None else claude
            ),
        }
    )


def value_after(argv, flag):
    return argv[argv.index(flag) + 1]


class ClearedCredentialEnvironment:
    """Run a body with every provider API key removed from the environment."""

    def __enter__(self):
        kept = {
            key: value
            for key, value in os.environ.items()
            if key not in CREDENTIAL_ENV_KEYS
        }
        self._patcher = mock.patch.dict(os.environ, kept, clear=True)
        self._patcher.start()
        return self

    def __exit__(self, *exc_info):
        self._patcher.stop()
        return False


# ---------------------------------------------------------------------------
# 1-3.  The Codex ChatGPT login proof, and every rejected route.
# ---------------------------------------------------------------------------
class CodexChatgptAuthenticationTest(unittest.TestCase):
    def test_chatgpt_proof_on_stderr_is_accepted(self):
        """The real observed CLI result: rc 0, empty stdout, proof on stderr."""
        run = chatgpt_and_claude(codex=CODEX_REAL_LOGIN)
        self.assertEqual(CODEX_REAL_LOGIN.stdout, "")
        self.assertEqual(CODEX_REAL_LOGIN.stderr, "Logged in using ChatGPT\n")
        with ClearedCredentialEnvironment():
            labels = production.verify_provider_authentication(run=run)
        self.assertEqual(labels["codex"], "CHATGPT_LOGIN")
        self.assertEqual(
            run.argv_list, [list(CODEX_STATUS_ARGV), list(CLAUDE_STATUS_ARGV)]
        )

    def test_chatgpt_proof_on_stdout_is_also_accepted(self):
        run = chatgpt_and_claude(codex=completed(0, CHATGPT_PROOF + "\n", ""))
        with ClearedCredentialEnvironment():
            labels = production.verify_provider_authentication(run=run)
        self.assertEqual(labels["codex"], "CHATGPT_LOGIN")

    def test_proof_is_an_exact_line_and_never_a_substring(self):
        """A decorated or embedded occurrence is not the proof."""
        not_proof = (
            "Logged in using ChatGPT (nesgeva2005@gmail.com)\n",
            "Not logged in using ChatGPT\n",
            "logged in using chatgpt\n",
            "Logged in using ChatGPT Codex API key\n",
        )
        for text in not_proof:
            for stream in ("stdout", "stderr"):
                with self.subTest(text=text.strip(), stream=stream):
                    outcome = completed(
                        0,
                        text if stream == "stdout" else "",
                        text if stream == "stderr" else "",
                    )
                    run = chatgpt_and_claude(codex=outcome)
                    with ClearedCredentialEnvironment():
                        with self.assertRaises(production.ProductionLaunchError):
                            production.verify_provider_authentication(run=run)

    def test_surrounding_whitespace_and_extra_lines_still_prove_the_login(self):
        outcome = completed(0, "", "  Logged in using ChatGPT  \nsome other note\n")
        run = chatgpt_and_claude(codex=outcome)
        with ClearedCredentialEnvironment():
            labels = production.verify_provider_authentication(run=run)
        self.assertEqual(labels["codex"], "CHATGPT_LOGIN")

    def test_codex_status_is_the_bounded_local_command(self):
        run = chatgpt_and_claude()
        with ClearedCredentialEnvironment():
            production.verify_provider_authentication(run=run)
        call = run.calls[0]
        self.assertEqual(call.argv, ["codex", "login", "status"])
        self.assertEqual(call.kwargs["cwd"], str(production.CONTROLLER_DIR))
        self.assertIs(call.kwargs["text"], True)
        self.assertIs(call.kwargs["capture_output"], True)
        self.assertIs(call.kwargs["check"], False)
        self.assertGreater(call.kwargs["timeout"], 0)
        self.assertLessEqual(call.kwargs["timeout"], 30)
        self.assertEqual(call.kwargs["env"]["CODEX_HOME"], "/home/ness/.codex")

    def test_api_key_only_login_is_rejected_on_either_stream(self):
        for outcome in (
            completed(0, API_KEY_LOGIN_TEXT, ""),
            completed(0, "", API_KEY_LOGIN_TEXT),
        ):
            with self.subTest(stdout=outcome.stdout, stderr=outcome.stderr):
                run = chatgpt_and_claude(codex=outcome)
                with ClearedCredentialEnvironment():
                    with self.assertRaises(production.ProductionLaunchError):
                        production.verify_provider_authentication(run=run)
                # Fails closed on Codex: Claude is never consulted afterwards.
                self.assertEqual(run.argv_list, [list(CODEX_STATUS_ARGV)])

    def test_absent_login_is_rejected_on_either_stream(self):
        for outcome in (
            completed(1, NOT_LOGGED_IN_TEXT, ""),
            completed(1, "", NOT_LOGGED_IN_TEXT),
        ):
            with self.subTest(stdout=outcome.stdout, stderr=outcome.stderr):
                run = chatgpt_and_claude(codex=outcome)
                with ClearedCredentialEnvironment():
                    with self.assertRaises(production.ProductionLaunchError):
                        production.verify_provider_authentication(run=run)
                self.assertEqual(run.argv_list, [list(CODEX_STATUS_ARGV)])

    def test_nonzero_exit_is_rejected_even_carrying_the_proof(self):
        """A zero return code stays a separate, required condition."""
        run = chatgpt_and_claude(codex=completed(1, "", CHATGPT_PROOF + "\n"))
        with ClearedCredentialEnvironment():
            with self.assertRaises(production.ProductionLaunchError):
                production.verify_provider_authentication(run=run)
        self.assertEqual(run.argv_list, [list(CODEX_STATUS_ARGV)])

    def test_zero_exit_with_empty_output_is_rejected(self):
        run = chatgpt_and_claude(codex=completed(0, "", ""))
        with ClearedCredentialEnvironment():
            with self.assertRaises(production.ProductionLaunchError):
                production.verify_provider_authentication(run=run)

    def test_absent_streams_are_rejected(self):
        run = chatgpt_and_claude(codex=completed(0, None, None))
        with ClearedCredentialEnvironment():
            with self.assertRaises(production.ProductionLaunchError):
                production.verify_provider_authentication(run=run)

    def test_spawn_failure_and_timeout_fail_closed(self):
        for failure in (
            FileNotFoundError("codex"),
            subprocess.TimeoutExpired(list(CODEX_STATUS_ARGV), 30),
        ):
            with self.subTest(failure=type(failure).__name__):
                run = chatgpt_and_claude(codex=failure)
                with ClearedCredentialEnvironment():
                    with self.assertRaises(production.ProductionLaunchError):
                        production.verify_provider_authentication(run=run)


# ---------------------------------------------------------------------------
# 4-6.  No OpenRouter key, no OpenAI key, no OpenRouter profile read.
# ---------------------------------------------------------------------------
class NoOpenRouterDependencyTest(unittest.TestCase):
    def test_openrouter_and_openai_keys_are_absent_and_not_required(self):
        run = chatgpt_and_claude()
        with ClearedCredentialEnvironment():
            for key in CREDENTIAL_ENV_KEYS:
                self.assertNotIn(key, os.environ)
            self.assertNotIn("OPENROUTER_API_KEY", production.provider_environment())
            self.assertNotIn("OPENAI_API_KEY", production.provider_environment())
            labels = production.verify_provider_authentication(run=run)
        self.assertEqual(
            labels, {"codex": "CHATGPT_LOGIN", "claude": "CURRENT_SUBSCRIPTION"}
        )
        for call in run.calls:
            for key in CREDENTIAL_ENV_KEYS:
                self.assertNotIn(key, call.kwargs["env"])

    def test_authentication_opens_no_openrouter_profile(self):
        opened = []
        real_open = builtins.open
        real_io_open = io.open
        real_os_open = os.open
        real_path_open = Path.open

        def record(path):
            opened.append(str(path))

        def fake_open(file, *args, **kwargs):
            record(file)
            return real_open(file, *args, **kwargs)

        def fake_io_open(file, *args, **kwargs):
            record(file)
            return real_io_open(file, *args, **kwargs)

        def fake_os_open(path, *args, **kwargs):
            record(path)
            return real_os_open(path, *args, **kwargs)

        def fake_path_open(self, *args, **kwargs):
            record(self)
            return real_path_open(self, *args, **kwargs)

        run = chatgpt_and_claude()
        with ClearedCredentialEnvironment():
            with mock.patch.object(builtins, "open", fake_open), mock.patch.object(
                io, "open", fake_io_open
            ), mock.patch.object(os, "open", fake_os_open), mock.patch.object(
                Path, "open", fake_path_open
            ):
                production.verify_provider_authentication(run=run)
        for path in opened:
            self.assertNotIn("openrouter", path.lower())
            self.assertFalse(path.endswith(".toml"), path)

    def test_production_carries_no_openrouter_surface(self):
        for absent in (
            "CODEX_PROFILE",
            "CODEX_PROFILE_PATH",
            "OPENROUTER_API_KEY_ENV",
            "tomllib",
        ):
            self.assertFalse(hasattr(production, absent), absent)
        source = CONTROLLER_SOURCE_PATH.read_text(encoding="utf-8")
        self.assertNotIn("openrouter", source.lower())
        production_source = (APP_DIR / "production.py").read_text(encoding="utf-8")
        self.assertNotIn("openrouter", production_source.lower())
        self.assertNotIn("OPENAI_API_KEY", production_source)


# ---------------------------------------------------------------------------
# 7-8.  The Claude subscription check keeps its exact meaning.
# ---------------------------------------------------------------------------
class ClaudeSubscriptionAuthenticationTest(unittest.TestCase):
    def test_subscription_results_remain_accepted(self):
        for method in ("claude.ai", "subscription"):
            with self.subTest(authMethod=method):
                run = chatgpt_and_claude(
                    claude=completed(
                        0, '{"loggedIn": true, "authMethod": "%s"}' % method
                    )
                )
                with ClearedCredentialEnvironment():
                    labels = production.verify_provider_authentication(run=run)
                self.assertEqual(labels["claude"], "CURRENT_SUBSCRIPTION")

    def test_non_subscription_results_remain_rejected(self):
        rejected = (
            completed(0, '{"loggedIn": true, "authMethod": "apiKey"}'),
            completed(0, '{"loggedIn": false, "authMethod": "claude.ai"}'),
            completed(1, '{"loggedIn": true, "authMethod": "claude.ai"}'),
            completed(0, "not json"),
        )
        for outcome in rejected:
            with self.subTest(stdout=outcome.stdout, rc=outcome.returncode):
                run = chatgpt_and_claude(claude=outcome)
                with ClearedCredentialEnvironment():
                    with self.assertRaises(production.ProductionLaunchError):
                        production.verify_provider_authentication(run=run)

    def test_claude_status_binding_is_unchanged(self):
        run = chatgpt_and_claude()
        with ClearedCredentialEnvironment():
            production.verify_provider_authentication(run=run)
        call = run.calls[1]
        self.assertEqual(call.argv, ["claude", "auth", "status", "--json"])
        self.assertEqual(call.kwargs["cwd"], str(production.CONTROLLER_DIR))
        self.assertEqual(call.kwargs["env"]["CLAUDE_CONFIG_DIR"], "/home/ness/.claude")
        self.assertEqual(call.kwargs["timeout"], 30)
        self.assertIs(call.kwargs["check"], False)
        self.assertNotIn("ANTHROPIC_API_KEY", call.kwargs["env"])
        self.assertEqual(production.CLAUDE_CONFIG_DIR, "/home/ness/.claude")


# ---------------------------------------------------------------------------
# 9-10.  The live supervisor Codex argv.
# ---------------------------------------------------------------------------
class SupervisorCodexArgvTest(unittest.TestCase):
    def capture(self):
        request = SimpleNamespace(
            provider_kind="codex_design_audit",
            provider_endpoint_identity=nh_loop.SUPERVISOR_CODEX_ENDPOINT,
            provider_request_identity="pr_offline_argv_probe",
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
                seen["kwargs"]["input"] = input
                seen["kwargs"]["timeout"] = timeout
                return b"", b""

        with tempfile.TemporaryDirectory() as folder:
            transport = nh_loop.NhCliProviderTransport(
                lambda: SimpleNamespace(state_dir=folder)
            )
            with mock.patch.object(nh_loop.subprocess, "Popen", FakeProcess):
                transport._dispatch_codex(request, material)
        self.assertIn("argv", seen)
        return seen

    def test_live_codex_argv_is_the_chatgpt_cli_route(self):
        seen = self.capture()
        argv = seen["argv"]
        self.assertEqual(argv[0], "codex")
        self.assertEqual(argv[1], "exec")
        self.assertEqual(value_after(argv, "-m"), "gpt-5.6-sol")
        self.assertEqual(nh_loop.CODEX_MODEL, "gpt-5.6-sol")
        self.assertIn('model_reasoning_effort="high"', argv)
        self.assertEqual(
            value_after(argv, "-c"), 'model_reasoning_effort="high"'
        )
        self.assertEqual(nh_loop.CODEX_REASONING_EFFORT, "high")
        self.assertEqual(value_after(argv, "-s"), "read-only")
        self.assertIn("--ephemeral", argv)
        self.assertIn("--json", argv)
        self.assertEqual(value_after(argv, "--color"), "never")
        self.assertEqual(value_after(argv, "-C"), NH_REPO_PATH)
        self.assertEqual(argv[-1], "-")
        self.assertEqual(seen["kwargs"]["cwd"], NH_REPO_PATH)
        self.assertIs(seen["kwargs"]["shell"], False)
        self.assertEqual(seen["kwargs"]["env"]["CODEX_HOME"], "/home/ness/.codex")
        self.assertGreater(seen["kwargs"]["timeout"], 0)

    def test_live_codex_argv_carries_no_profile_and_no_openrouter(self):
        argv = self.capture()["argv"]
        self.assertNotIn("--profile", argv)
        for token in argv:
            self.assertNotIn("openrouter", str(token).lower())
        self.assertFalse(hasattr(nh_loop, "CODEX_PROFILE"))

    def test_supervisor_codex_endpoint_identity_is_chatgpt(self):
        self.assertEqual(nh_loop.SUPERVISOR_CODEX_ENDPOINT, "local_codex_cli_chatgpt")
        binding = nh_loop.supervisor_endpoint_binding()
        for kind, endpoint in binding.items():
            if kind in nh_loop.SUPERVISOR_CLAUDE_PROVIDER_KINDS:
                self.assertEqual(endpoint, "local_claude_code_subscription")
            else:
                self.assertEqual(endpoint, "local_codex_cli_chatgpt")


# ---------------------------------------------------------------------------
# 11.  No live Codex invocation still forces a profile.
# ---------------------------------------------------------------------------
class ControllerCodexSourceTest(unittest.TestCase):
    def test_no_live_codex_invocation_forces_a_profile(self):
        targets = [(name, getattr(nh_loop, name)) for name in LIVE_CODEX_INVOCATIONS]
        targets.append(
            (
                "NhCliProviderTransport._dispatch_codex",
                nh_loop.NhCliProviderTransport._dispatch_codex,
            )
        )
        # SECOND-MODEL SWITCH (2026-09-02): every live invocation builds its argv
        # through the ONE builder, and the codex literals live there.
        builder = inspect.getsource(nh_loop.second_model_argv)
        self.assertIn('"codex"', builder)
        self.assertIn("CODEX_MODEL", builder)
        self.assertIn("CODEX_REASONING_EFFORT", builder)
        self.assertIn("--ephemeral", builder)
        self.assertIn("read-only", builder)
        self.assertNotIn("--profile", builder)
        self.assertNotIn("CODEX_PROFILE", builder)
        self.assertNotIn("openrouter", builder.lower())
        for name, function in targets:
            with self.subTest(function=name):
                source = inspect.getsource(function)
                self.assertIn("second_model_argv(", source)
                self.assertNotIn("--profile", source)
                self.assertNotIn("CODEX_PROFILE", source)
                self.assertNotIn("openrouter", source.lower())

    def test_controller_source_has_no_active_profile_dependency(self):
        source = CONTROLLER_SOURCE_PATH.read_text(encoding="utf-8")
        self.assertNotIn("--profile", source)
        self.assertNotIn("CODEX_PROFILE", source)
        self.assertNotIn("openrouter", source.lower())


# ---------------------------------------------------------------------------
# The Claude route keeps its write/sandbox boundaries and adds only bounded web
# research for the Ness-approved Build-vs-Borrow check.
# ---------------------------------------------------------------------------
class ClaudeRouteUnchangedTest(unittest.TestCase):
    def test_claude_route_constants_are_unchanged(self):
        self.assertEqual(
            nh_loop.SUPERVISOR_CLAUDE_ENDPOINT, "local_claude_code_subscription"
        )
        self.assertEqual(nh_loop.CLAUDE_EXECUTE_MODEL, "claude-opus-5")
        self.assertEqual(nh_loop.CLAUDE_EFFORT, "xhigh")
        self.assertEqual(
            nh_loop.CLAUDE_EXECUTE_TOOLS,
            "Read,Glob,Grep,Write,Edit,WebSearch,WebFetch",
        )
        self.assertEqual(
            nh_loop.CLAUDE_EXECUTE_ALLOWED_TOOLS, "WebSearch,WebFetch"
        )
        self.assertEqual(
            nh_loop.CLAUDE_EXECUTE_DENIED_TOOLS,
            "Agent,Artifact,AskUserQuestion,Bash,BashOutput,ExitPlanMode,KillBash,"
            "KillShell,ListMcpResources,MultiEdit,NotebookEdit,NotebookRead,"
            "ReadMcpResource,SendMessage,Skill,SlashCommand,Task,TodoWrite,Workflow",
        )
        self.assertEqual(nh_loop.CLAUDE_EXECUTE_PERMISSION_MODE, "acceptEdits")
        self.assertEqual(nh_loop.CLAUDE_EXECUTE_OUTPUT_FORMAT, "stream-json")
        self.assertIn(
            "bypassPermissions", nh_loop.CLAUDE_FORBIDDEN_PERMISSION_MODES
        )
        self.assertNotIn("Bash", nh_loop.CLAUDE_EXECUTE_TOOLS)
        self.assertNotIn("Mcp", nh_loop.CLAUDE_EXECUTE_TOOLS)

    def test_build_vs_borrow_rules_reach_design_and_audit_prompts(self):
        claude_rules = "\n".join(nh_loop.CLAUDE_BUILD_VS_BORROW_BLOCK)
        self.assertIn("BUILD VS BORROW", claude_rules)
        self.assertIn("PARTIAL REUSE", claude_rules)
        self.assertIn("untrusted external evidence", claude_rules)
        self.assertIn("Do not install", claude_rules)
        self.assertIn(
            "BUILD-VS-BORROW INDEPENDENT CHALLENGE",
            nh_loop.CODEX_BUILD_VS_BORROW_AUDIT_INSTRUCTION,
        )
        self.assertIn(
            "BUNDLE 8 EXTERNAL-ALTERNATIVES BOUNDARY",
            nh_loop.NEXT_PACKAGE_PROMPT,
        )

    def test_codex_web_search_is_scoped_to_design_audits(self):
        legacy = inspect.getsource(nh_loop.run_codex_design_audit)
        supervisor = inspect.getsource(
            nh_loop.NhCliProviderTransport._dispatch_codex
        )
        # SECOND-MODEL SWITCH (2026-09-02): the literal lives in the builder;
        # callers ask for it with web_search=True, and only the design audit does.
        builder = inspect.getsource(nh_loop.second_model_argv)
        self.assertIn('"standalone_web_search"', builder)
        self.assertIn("web_search=True", legacy)
        self.assertIn(
            'request.provider_kind == "codex_design_audit"', supervisor
        )
        self.assertNotIn(
            "web_search=True",
            inspect.getsource(nh_loop.run_codex_next_package),
        )

    def test_claude_invocation_keeps_its_bounded_shape(self):
        source = inspect.getsource(nh_loop.run_claude_design_write)
        for fragment in (
            '"--model",',
            "CLAUDE_EXECUTE_MODEL,",
            '"--effort",',
            "CLAUDE_EFFORT,",
            '"--tools",',
            "CLAUDE_EXECUTE_TOOLS,",
            '"--allowed-tools",',
            "CLAUDE_EXECUTE_ALLOWED_TOOLS,",
            '"--disallowed-tools",',
            "CLAUDE_EXECUTE_DENIED_TOOLS,",
            '"--permission-mode",',
            "CLAUDE_EXECUTE_PERMISSION_MODE,",
            '"--mcp-config",',
            '\'{"mcpServers":{}}\'',
            '"--strict-mcp-config",',
            "workspace_is_outside_real_repo(",
            "claude is never run against the real N.H ",
            "--resume",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, source)
        # Named only in the prose above the argv; never passed as an argument.
        self.assertNotIn('"--add-dir"', source)
        self.assertNotIn('"--dangerously-skip-permissions"', source)
        self.assertNotIn('"--fork-session"', source)

    def test_claude_disposable_workspace_is_never_the_real_checkout(self):
        errors = []
        self.assertFalse(
            nh_loop.workspace_is_outside_real_repo(nh_loop.NH_REPO_PATH, errors)
        )
        self.assertTrue(errors)


# ---------------------------------------------------------------------------
# 12.  The guards themselves.
# ---------------------------------------------------------------------------
class SubprocessGuardTest(unittest.TestCase):
    def test_unscripted_argv_fails_the_fake(self):
        run = FakeRun({})
        with self.assertRaises(UnexpectedProcessLaunch):
            run(["codex", "exec"])

    def test_real_spawn_entry_points_are_guarded(self):
        for target, attribute in ((subprocess, "run"), (subprocess, "Popen"),
                                  (os, "system"), (socket, "socket")):
            with self.subTest(entry="%s.%s" % (target.__name__, attribute)):
                with self.assertRaises(UnexpectedProcessLaunch):
                    getattr(target, attribute)(["true"])

    def test_no_module_main_was_executed(self):
        self.assertEqual(production.__name__, "production")
        self.assertEqual(nh_loop.__name__, "nh_loop")


if __name__ == "__main__":
    unittest.main()

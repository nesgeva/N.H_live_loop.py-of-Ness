import inspect
import hashlib
import io
import os
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
for directory in (ROOT, ROOT / "controller"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import nh_loop  # noqa: E402


class DisposableResultReadTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory(
            prefix=nh_loop.DISPOSABLE_WORKSPACE_PREFIX
        )
        self.addCleanup(self.folder.cleanup)
        Path(self.folder.name, "target.md").write_bytes(b"safe")

    def test_symlink_replacement_after_scan_is_never_followed(self):
        errors = []
        after = nh_loop.scan_workspace_tree(self.folder.name, errors)
        self.assertEqual([], errors)
        outside = Path(self.folder.name).parent / "nh-outside-result"
        outside.write_bytes(b"secret")
        self.addCleanup(lambda: outside.unlink(missing_ok=True))
        target = Path(self.folder.name, "target.md")
        target.unlink()
        target.symlink_to(outside)

        payload = nh_loop.read_disposable_regular_bytes(
            self.folder.name, ("target.md",), 1024, after["target.md"], errors
        )

        self.assertIsNone(payload)
        self.assertTrue(errors)

    def test_both_supervisor_claude_write_routes_use_safe_reader(self):
        correction = inspect.getsource(
            nh_loop.NhCliProviderTransport._dispatch_claude
        )
        initial = inspect.getsource(
            nh_loop.NhCliProviderTransport._dispatch_claude_initial_design
        )
        self.assertIn("read_disposable_regular_bytes(", correction)
        self.assertIn("read_disposable_regular_bytes(", initial)
        self.assertNotIn("with open(target_path", correction)
        self.assertNotIn("with open(target_path", initial)


class DisposableCleanupTests(unittest.TestCase):
    def operation(self, fail):
        errors = []
        holder = {}

        @nh_loop.owns_disposable_workspaces
        def run():
            path = tempfile.mkdtemp(prefix=nh_loop.DISPOSABLE_WORKSPACE_PREFIX)
            holder["path"] = path
            nh_loop._register_disposable_workspace(path, errors)
            if fail:
                raise RuntimeError("forced")
            return path

        try:
            path = run()
        except RuntimeError:
            active = getattr(nh_loop._DISPOSABLE_WORKSPACE_SCOPE, "active", None)
            self.assertIsNone(active)
            return holder["path"], errors
        return path, errors

    def test_workspace_is_removed_on_normal_return(self):
        path, errors = self.operation(False)
        self.assertFalse(os.path.lexists(path))
        self.assertEqual([], errors)

    def test_workspace_is_removed_on_exception(self):
        path, errors = self.operation(True)
        self.assertEqual([], errors)
        self.assertFalse(os.path.lexists(path))

    def test_real_design_entry_points_own_all_nested_workspaces(self):
        self.assertTrue(
            hasattr(nh_loop.NhCliProviderTransport._dispatch_claude, "__wrapped__")
        )
        self.assertTrue(
            hasattr(
                nh_loop.NhCliProviderTransport._dispatch_claude_initial_design,
                "__wrapped__",
            )
        )


class FakeOwnedProcess:
    pid = 99999999

    def __init__(self, argv, *, stdout, stderr, **_kwargs):
        self.argv = argv
        self.stdout_handle = stdout
        self.stderr_handle = stderr
        self.stdin = io.BytesIO()
        self.returncode = None
        self.terminated = False
        self.killed = False
        self.waits = []

    def terminate(self):
        self.terminated = True

    def kill(self):
        self.killed = True

    def wait(self, timeout=None):
        self.waits.append(timeout)
        self.returncode = -15
        return self.returncode


class CodexLaunchOwnershipTests(unittest.TestCase):
    def test_launch_fact_failure_reaps_child_and_releases_resources(self):
        state = tempfile.TemporaryDirectory()
        self.addCleanup(state.cleanup)
        transport = nh_loop.NhCliProviderTransport(
            lambda: SimpleNamespace(state_dir=state.name)
        )
        request = SimpleNamespace(
            provider_kind="gpt_question_validation",
            provider_endpoint_identity=nh_loop.SUPERVISOR_CODEX_ENDPOINT,
            provider_request_identity="pr_launch_fact_failure",
            prompt_material_sha256="a" * 64,
            required_inputs_sha256="b" * 64,
        )
        captured = {}

        def make_process(argv, **kwargs):
            captured["process"] = FakeOwnedProcess(argv, **kwargs)
            captured["env"] = kwargs["env"]
            schema_path = (
                argv[argv.index("--output-schema") + 1]
                if "--output-schema" in argv
                else None
            )
            captured["schema_path"] = schema_path
            return captured["process"]

        with mock.patch.object(nh_loop, "SECOND_MODEL_PROVIDER", "codex"), mock.patch.object(
            nh_loop.subprocess, "Popen", side_effect=make_process
        ), mock.patch.object(
            nh_loop.nh_supervisor.lease, "read_process_start_ticks", return_value=123
        ), mock.patch.object(
            nh_loop.nh_supervisor.lease, "boot_id_sha256", return_value="c" * 64
        ), mock.patch.object(
            transport, "_write_codex_launch_fact", side_effect=OSError("disk full")
        ):
            with self.assertRaises(OSError):
                transport._dispatch_codex(request, {}, prompt="offline")

        process = captured["process"]
        self.assertTrue(process.terminated)
        self.assertEqual([5], process.waits)
        self.assertTrue(process.stdin.closed)
        self.assertTrue(process.stdout_handle.closed)
        self.assertTrue(process.stderr_handle.closed)
        self.assertTrue(
            nh_loop.CODEX_CHILD_ENVIRONMENT_EXCLUDED.isdisjoint(captured["env"])
        )
        self.assertEqual("/home/ness", captured["env"]["HOME"])
        self.assertEqual(transport.codex_home, captured["env"]["CODEX_HOME"])
        if captured["schema_path"] is not None:
            self.assertFalse(Path(captured["schema_path"]).exists())


class CodexChildEnvironmentTests(unittest.TestCase):
    def ambient(self):
        return {
            name: "inherited-%s" % name.lower()
            for name in nh_loop.CODEX_CHILD_ENVIRONMENT_EXCLUDED
        }

    def test_every_direct_second_model_codex_path_uses_clean_child_environment(self):
        calls = []

        def completed(_argv, **kwargs):
            calls.append(kwargs)
            return SimpleNamespace(
                returncode=0,
                stdout=(nh_loop.CODEX_SMOKE_REPLY + "\n").encode("utf-8"),
                stderr=b"",
            )

        cases = (
            (nh_loop.run_codex_smoke, ([],)),
            (nh_loop.run_codex_next_package, ([],)),
            (nh_loop.run_codex_prepare_task, ("prompt", [])),
            (nh_loop.run_codex_design_audit, ("prompt", [])),
            (nh_loop.run_codex_correction_specification, ("prompt", [])),
            (nh_loop.run_codex_claude_stop_review, ("prompt", [])),
            (nh_loop.run_codex_question_validation, ("prompt", [])),
        )
        ambient = self.ambient()
        ambient["NH_UNRELATED_SENTINEL"] = "preserved"
        ambient["CODEX_CI"] = "preserved-ci-mode"
        ambient["CODEX_SQLITE_HOME"] = "/home/ness/.codex/../.codex/sqlite"
        with mock.patch.dict(os.environ, ambient, clear=False), mock.patch.object(
            nh_loop, "SECOND_MODEL_PROVIDER", "codex"
        ), mock.patch.object(nh_loop.subprocess, "run", side_effect=completed):
            for function, args in cases:
                function(*args)

        self.assertEqual(len(cases), len(calls))
        for call in calls:
            self.assertTrue(
                nh_loop.CODEX_CHILD_ENVIRONMENT_EXCLUDED.isdisjoint(call["env"])
            )
            self.assertEqual("preserved", call["env"]["NH_UNRELATED_SENTINEL"])
            self.assertEqual("preserved-ci-mode", call["env"]["CODEX_CI"])
            self.assertEqual(
                "/home/ness/.codex/sqlite", call["env"]["CODEX_SQLITE_HOME"]
            )
            self.assertEqual(nh_loop.NH_REPO_PATH, call["cwd"])

    def test_resumable_failure_cleans_environment_and_saves_safe_stderr(self):
        real_popen = subprocess.Popen
        captured = {}
        thread_id = "019d2f48-75c8-7ec1-8c42-2d0c57bc88bd"
        stderr_bytes = b"private local diagnostic token=do-not-log"

        def launch(_argv, **kwargs):
            captured["env"] = kwargs["env"]
            program = (
                "import sys; sys.stdin.buffer.read(); "
                "sys.stdout.write('{\\\"type\\\":\\\"thread.started\\\","
                "\\\"thread_id\\\":\\\"%s\\\"}\\n'); sys.stdout.flush(); "
                "sys.stderr.buffer.write(%r); sys.stderr.flush(); sys.exit(1)"
                % (thread_id, stderr_bytes)
            )
            process = real_popen(
                [sys.executable, "-c", program],
                stdin=kwargs["stdin"],
                stdout=kwargs["stdout"],
                stderr=kwargs["stderr"],
                cwd=kwargs["cwd"],
                env=kwargs["env"],
                shell=False,
            )
            captured["process"] = process
            return process

        with tempfile.TemporaryDirectory(dir="/tmp") as folder:
            checkpoint = {
                "path": str(Path(folder) / "checkpoint.json"),
                "progress_path": str(Path(folder) / "progress.json"),
            }
            ambient = self.ambient()
            sqlite_home = "/home/ness/.codex/sqlite"
            ambient["CODEX_SQLITE_HOME"] = sqlite_home
            ambient["CODEX_CI"] = "preserved-ci-mode"
            with mock.patch.dict(os.environ, ambient, clear=False), mock.patch.object(
                nh_loop, "SECOND_MODEL_REPLY_CAPTURE_DIR", folder
            ), mock.patch.object(
                nh_loop, "read_codex_review_checkpoint", return_value={"thread_id": thread_id}
            ), mock.patch.object(
                nh_loop, "write_codex_review_checkpoint", return_value=True
            ), mock.patch.object(
                nh_loop, "write_codex_review_progress", return_value=True
            ), mock.patch.object(
                nh_loop.subprocess, "Popen", side_effect=launch
            ):
                errors = []
                invoked, code, _stdout = nh_loop.run_resumable_codex_review(
                    "prompt", errors, checkpoint
                )
            captured["process"].stdout.close()
            captured["process"].stderr.close()

            self.assertTrue(invoked)
            self.assertEqual(1, code)
            self.assertTrue(
                nh_loop.CODEX_CHILD_ENVIRONMENT_EXCLUDED.isdisjoint(captured["env"])
            )
            self.assertEqual(sqlite_home, captured["env"]["CODEX_SQLITE_HOME"])
            self.assertEqual("preserved-ci-mode", captured["env"]["CODEX_CI"])
            self.assertEqual(1, len(errors))
            self.assertNotIn("private local diagnostic", errors[0])
            self.assertIn("stderr_bytes=%d" % len(stderr_bytes), errors[0])
            self.assertIn(
                "stderr_sha256=%s" % hashlib.sha256(stderr_bytes).hexdigest(),
                errors[0],
            )
            stderr_path = errors[0].split("stderr_saved=", 1)[1].split(";", 1)[0]
            self.assertEqual(stderr_bytes, Path(stderr_path).read_bytes())
            self.assertEqual(0o600, stat.S_IMODE(os.stat(stderr_path).st_mode))


if __name__ == "__main__":
    unittest.main()

"""Write-boundary re-proof for the ONE live writer (audit repair, 2026-09-02).

Ness's decision: the supervisor's ``_promote_candidate`` stays the only code
path that creates a file in the governed repository, and it gains the
safety checks the former legacy writer performed at
its own write boundary: branch, frozen HEAD, no tracked modification, a
controlled new candidate path, the interview clearance for the package, and
a post-write observation of the repository shape.

The supervisor package calls no Git and no interview code itself, so the
checks are handed in through ONE context seam, ``write_boundary_prover``,
exactly as ``interview_gate_reader`` is.  A context WITHOUT the seam refuses
to write: absence is a stop, never an all-clear.
"""
import os
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
from nh_supervisor import commands, engine, runtime  # noqa: E402


CANDIDATE_REL = "05_ACTIVE_CANDIDATE/NH_TEST_THING_v1_0_CANDIDATE.md"


def fake_context(candidate_dir, prover):
    return SimpleNamespace(
        candidate_dir=candidate_dir,
        transition_target_path=None,
        write_boundary_prover=prover,
        binding=SimpleNamespace(package_scope_id="A99", head_sha="a" * 40),
    )


def intended_body():
    return {
        "package_scope_id": "A99",
        "candidate_path": CANDIDATE_REL,
        "head_sha": "a" * 40,
        "branch": nh_loop.REQUIRED_BRANCH,
    }


class PromoterConsumesTheProver(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="nh_wbp_")
        self.candidate_dir = os.path.join(self.tmp, "05_ACTIVE_CANDIDATE")
        os.makedirs(self.candidate_dir)

    def test_context_without_a_prover_refuses_and_writes_nothing(self):
        context = fake_context(self.candidate_dir, None)
        with self.assertRaises(engine.SupervisorRefusal):
            commands._promote_candidate(context, intended_body(), b"x")
        self.assertEqual(os.listdir(self.candidate_dir), [])

    def test_a_missing_seam_attribute_refuses_too(self):
        context = fake_context(self.candidate_dir, None)
        del context.write_boundary_prover
        with self.assertRaises(engine.SupervisorRefusal):
            commands._promote_candidate(context, intended_body(), b"x")
        self.assertEqual(os.listdir(self.candidate_dir), [])

    def test_a_refusing_prover_stops_the_write_before_it_happens(self):
        calls = []

        def prover(facts):
            calls.append(facts["phase"])
            return ["the branch is wrong"]

        context = fake_context(self.candidate_dir, prover)
        with self.assertRaises(engine.SupervisorRefusal) as caught:
            commands._promote_candidate(context, intended_body(), b"x")
        self.assertIn("the branch is wrong", str(caught.exception))
        self.assertEqual(calls, ["before"])
        self.assertEqual(os.listdir(self.candidate_dir), [])

    def test_a_clean_prover_is_asked_before_and_after_and_the_file_is_written(self):
        seen = []

        def prover(facts):
            seen.append(dict(facts))
            return []

        context = fake_context(self.candidate_dir, prover)
        commands._promote_candidate(context, intended_body(), b"payload")
        self.assertEqual([f["phase"] for f in seen], ["before", "after"])
        for facts in seen:
            self.assertEqual(facts["package_scope_id"], "A99")
            self.assertEqual(facts["candidate_path"], CANDIDATE_REL)
            self.assertEqual(facts["expected_head_sha"], "a" * 40)
            self.assertEqual(
                facts["real_path"],
                os.path.join(self.candidate_dir, os.path.basename(CANDIDATE_REL)),
            )
        with open(seen[0]["real_path"], "rb") as handle:
            self.assertEqual(handle.read(), b"payload")

    def test_a_prover_refusing_after_the_write_is_reported_as_a_refusal(self):
        def prover(facts):
            return ["HEAD moved"] if facts["phase"] == "after" else []

        context = fake_context(self.candidate_dir, prover)
        with self.assertRaises(engine.SupervisorRefusal) as caught:
            commands._promote_candidate(context, intended_body(), b"x")
        self.assertIn("HEAD moved", str(caught.exception))

    def test_build_context_carries_the_seam(self):
        self.assertIn("write_boundary_prover", engine.SupervisorContext.__dataclass_fields__)
        self.assertIn("write_boundary_prover", runtime.build_context.__code__.co_varnames)


def git(repo, *args):
    return subprocess.run(
        ["git", "-C", repo] + list(args), check=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
    ).stdout.strip()


class ControllerProverAgainstADisposableRepository(unittest.TestCase):
    """nh_loop.supervisor_write_boundary_prover against a throwaway Git repo."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="nh_wbp_repo_")
        self.repo = os.path.join(self.tmp, "NH-GOVERNANCE")
        os.makedirs(os.path.join(self.repo, "05_ACTIVE_CANDIDATE"))
        with open(os.path.join(self.repo, "README.md"), "w") as handle:
            handle.write("governed\n")
        with open(os.path.join(self.repo, "05_ACTIVE_CANDIDATE", ".keep"), "w") as handle:
            handle.write("")
        git(self.repo, "init", "-q", "-b", nh_loop.REQUIRED_BRANCH)
        git(self.repo, "-c", "user.email=t@t", "-c", "user.name=t", "add", "-A")
        git(self.repo, "-c", "user.email=t@t", "-c", "user.name=t",
            "commit", "-q", "-m", "base")
        self.head = git(self.repo, "rev-parse", "HEAD")
        self.saved_repo = nh_loop.NH_REPO_PATH
        nh_loop.NH_REPO_PATH = self.repo
        self.unlocked = {"unlocked": True, "reasons": [], "errors": []}
        self.gate_patch = mock.patch.object(
            nh_loop, "evaluate_interview_clearance", lambda scope: self.unlocked
        )
        self.gate_patch.start()

    def tearDown(self):
        self.gate_patch.stop()
        nh_loop.NH_REPO_PATH = self.saved_repo

    def facts(self, phase="before", head=None):
        return {
            "phase": phase,
            "package_scope_id": "A99",
            "candidate_path": CANDIDATE_REL,
            "real_path": os.path.join(self.repo, CANDIDATE_REL),
            "expected_head_sha": head or self.head,
        }

    def test_clean_repository_on_the_required_branch_passes_before(self):
        self.assertEqual(nh_loop.supervisor_write_boundary_prover(self.facts()), [])

    def test_wrong_branch_refuses(self):
        git(self.repo, "checkout", "-q", "-b", "elsewhere")
        errors = nh_loop.supervisor_write_boundary_prover(self.facts())
        self.assertTrue(any(nh_loop.REQUIRED_BRANCH in e for e in errors), errors)

    def test_moved_head_refuses(self):
        errors = nh_loop.supervisor_write_boundary_prover(self.facts(head="b" * 40))
        self.assertTrue(any("HEAD" in e for e in errors), errors)

    def test_a_modified_tracked_file_refuses(self):
        with open(os.path.join(self.repo, "README.md"), "a") as handle:
            handle.write("edited\n")
        errors = nh_loop.supervisor_write_boundary_prover(self.facts())
        self.assertTrue(any("README.md" in e for e in errors), errors)

    def test_an_unrelated_untracked_candidate_is_refused(self):
        other = os.path.join(self.repo, "05_ACTIVE_CANDIDATE", "OTHER_v1_0_CANDIDATE.md")
        with open(other, "w") as handle:
            handle.write("x")
        errors = nh_loop.supervisor_write_boundary_prover(self.facts())
        self.assertTrue(any("untracked set" in e for e in errors), errors)

    def test_an_authenticated_preexisting_candidate_is_allowed_exactly(self):
        other_rel = "05_ACTIVE_CANDIDATE/OTHER_v1_0_CANDIDATE.md"
        with open(os.path.join(self.repo, other_rel), "w") as handle:
            handle.write("x")
        self.assertEqual(
            nh_loop.supervisor_write_boundary_prover(
                self.facts(),
                allowed_preexisting_untracked_paths=(other_rel,),
            ),
            [],
        )
        with open(os.path.join(self.repo, CANDIDATE_REL), "w") as handle:
            handle.write("candidate")
        self.assertEqual(
            nh_loop.supervisor_write_boundary_prover(
                self.facts("after"),
                allowed_preexisting_untracked_paths=(other_rel,),
            ),
            [],
        )

    def test_after_phase_refuses_any_extra_untracked_file(self):
        with open(os.path.join(self.repo, CANDIDATE_REL), "w") as handle:
            handle.write("candidate")
        extra_rel = "05_ACTIVE_CANDIDATE/EXTRA_v1_0_CANDIDATE.md"
        with open(os.path.join(self.repo, extra_rel), "w") as handle:
            handle.write("extra")
        errors = nh_loop.supervisor_write_boundary_prover(self.facts("after"))
        self.assertTrue(any("untracked set" in e for e in errors), errors)

    def test_a_locked_interview_gate_refuses(self):
        self.unlocked = {"unlocked": False, "reasons": ["genuine_ness_questions_still_blocking"], "errors": []}
        errors = nh_loop.supervisor_write_boundary_prover(self.facts())
        self.assertTrue(any("clearance" in e for e in errors), errors)

    def test_a_target_outside_the_candidate_grammar_refuses(self):
        facts = self.facts()
        facts["candidate_path"] = "01_AUTHORITATIVE/NH_MASTER.md"
        facts["real_path"] = os.path.join(self.repo, facts["candidate_path"])
        errors = nh_loop.supervisor_write_boundary_prover(facts)
        self.assertTrue(errors)

    def test_after_phase_requires_the_new_file_to_be_the_only_change(self):
        real = os.path.join(self.repo, CANDIDATE_REL)
        with open(real, "w") as handle:
            handle.write("new candidate")
        self.assertEqual(nh_loop.supervisor_write_boundary_prover(self.facts("after")), [])
        with open(os.path.join(self.repo, "README.md"), "a") as handle:
            handle.write("edited\n")
        errors = nh_loop.supervisor_write_boundary_prover(self.facts("after"))
        self.assertTrue(any("README.md" in e for e in errors), errors)

    def test_after_phase_refuses_a_symlink_target(self):
        real = os.path.join(self.repo, CANDIDATE_REL)
        with open(os.path.join(self.tmp, "outside"), "w") as handle:
            handle.write("x")
        os.symlink(os.path.join(self.tmp, "outside"), real)
        errors = nh_loop.supervisor_write_boundary_prover(self.facts("after"))
        self.assertTrue(any("ordinary file" in e for e in errors), errors)


class RecoveryReprovesTheBoundary(unittest.TestCase):
    def test_b8_recovery_branches_re_run_the_after_proof(self):
        import inspect
        from nh_supervisor import commands as c
        for fn in (c._b6g_correction_apply, c._b6g_initial_design):
            source = inspect.getsource(fn)
            b8 = source.index('boundary == "B8"')
            recover = source.index("_recover_stranded_candidate_custody(", b8)
            proof = source.index('_require_write_boundary(', b8)
            self.assertLess(proof, recover, fn.__name__)


if __name__ == "__main__":
    unittest.main()

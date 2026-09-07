#!/usr/bin/env bash
#
# NH_SHADOW_REHEARSAL_LAUNCHER_v1.sh
#
# N.H SHADOW LIVE REHEARSAL LAUNCHER — v1
#
# WHAT THIS IS
#   A disposable-laboratory launcher. It proves the protected original N.H /
#   controller workspace has not moved, makes an exact throwaway shadow copy of
#   it, hides the real /home/ness behind a tmpfs, republishes the shadow at the
#   EXACT normal path /home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP inside a Bubblewrap
#   namespace, runs EXACTLY ONE real
#
#       python3 nh_loop.py execute-next-claude-task
#
#   inside that namespace, and then re-proves the protected original from
#   OUTSIDE the namespace.
#
# WHAT THIS IS NOT
#   This is validation only. It creates no N.H policy. It is not acceptance and
#   it is not adoption of any candidate. It authorises no production
#   implementation. It integrates nothing into Master or Map. It never writes to
#   the protected original, and it contains no Git write command of any kind.
#
#   A controller PASS inside the shadow means ONLY that the isolated real
#   rehearsal reached its own PASS. It means nothing about N.H acceptance.
#
# GOVERNING AUTHORITY (unchanged by this file)
#   1. NH_MASTER-20_CORRECTED_v10.md
#   2. NH_DECISION_DEFAULTS-S19_v2_2.md
#   3. cursorrules
#   4. NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md
#
# ISOLATION DESIGN (implements the read-only Codex preflight result
# SHADOW_REHEARSAL_PREFLIGHT = PASS)
#   - copy-and-cd alone is NOT safe: nh_loop.py hardcodes
#     NH_REPO_PATH = /home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/NH-GOVERNANCE and
#     resolves it with os.path.realpath(), so the shadow must appear at that
#     exact canonical path. A bind mount does that; a copy in another directory
#     does not.
#   - the whole of /home/ness is therefore hidden with a tmpfs first, and only
#     the mechanically required pieces are put back.
#   - .codex and .claude are ANONYMOUS copy-on-write overlays: the sandbox may
#     write to them, the writes go to an invisible tmpfs, and the host copies
#     cannot be reached.
#   - the real .ssh, .netrc, .config and any Git credential helper state stay
#     hidden and are never copied into the persistent lab.
#   - network stays available ONLY because the real Codex / Claude provider
#     calls require it.
#
# THE LAB CONTAINS A COPY OF THE N.H INTERVIEW AUTHENTICITY KEY.
#   The controller cannot append authenticated journal events without it, so the
#   shadow copy of nh_interview_state/ necessarily includes it. The lab is
#   created mode 0700. Delete the lab when the rehearsal has been reviewed.
#   No MODEL login material is ever copied into the lab.
#
# USAGE
#   bash /home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/controller/NH_SHADOW_REHEARSAL_LAUNCHER_v1.sh
#
#   Run it manually, from an ordinary terminal, as the user "ness".
#   It takes no arguments. It refuses to run as root.
#
#   PRECONDITION: no other Claude Code / Codex session should be running on this
#   host while it runs, or the host credential witness will report CHANGED
#   because that other session is rewriting ~/.claude.json under you.
#
set -Eeuo pipefail
umask 077

# ==========================================================================
# SECTION 0 — FROZEN IDENTITIES. FAIL CLOSED AGAINST ALL OF THEM.
# ==========================================================================

readonly HOME_REAL="/home/ness"
readonly WS="/home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP"
readonly CTRL="${WS}/controller"
readonly NHGOV="${WS}/NH-GOVERNANCE"
readonly STATE="${WS}/nh_interview_state"
readonly CAND_DIR="${NHGOV}/05_ACTIVE_CANDIDATE"

readonly LAUNCHER_BASENAME="NH_SHADOW_REHEARSAL_LAUNCHER_v1.sh"

# --- controller ---
readonly EXP_LOOP_SHA="13ef2b138415a06a31100fcf6d6a167ee79dd3c48a78c438adc4dd7305551e76"
readonly EXP_LOOP_BYTES="1354304"
readonly EXP_LOOP_LINES="30002"
readonly EXP_CTRL_BRANCH="main"
readonly EXP_CTRL_HEAD="db46a51967b1af1aa873bc0c0e847a0a95221bdf"
readonly EXP_CTRL_STATUS_CORE=" M nh_loop.py"

# --- N.H ---
readonly EXP_NH_BRANCH="nh-design-loop"
readonly EXP_NH_HEAD="ce3a38f43f287a56bd635ed836edf002a2db50a7"

readonly CAND_V10="NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_0_CANDIDATE.md"
readonly CAND_V11="NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_1_CANDIDATE.md"
readonly CAND_V12="NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_2_CANDIDATE.md"

readonly EXP_V10_SHA="e6ee27fcd33f49a276de7753334cb18dd5d7d1f4d11a25d8b86dd236bfeebe3c"
readonly EXP_V10_BYTES="51315"
readonly EXP_V11_SHA="964b6dbd0a16756d65d5a6e185298eb554d6475d9da3826266b7571c8a7d8cbd"
readonly EXP_V11_BYTES="73685"
readonly EXP_V12_SHA="2245ae26ebf4b833ca36c798f82f543d807f281136e388f0f4204982c9a3cb55"
readonly EXP_V12_BYTES="109986"

# --- interview state ---
readonly EXP_JOURNAL_SHA="39c6af157222df10203d426e06ab323bb222041aa7b0838f1130f0518aef9945"
readonly EXP_JOURNAL_BYTES="15604"
readonly EXP_JOURNAL_EVENTS="5"
readonly EXP_HEAD_SHA="b55e8b3f5916445db84a4fc9e6d342113b8a538ba20fe5c20dc94f7c7a42cf90"
readonly EXP_KEY_SHA="6a129d96ed1af2e5f7c890821c8fddd27c7e4b368847884274712e126bf797d7"
readonly EXP_PKG_SCOPE="nullpkg_1ffc9ec7aae12b75ef50400da674812f"
readonly EXP_PKG_SCOPE_OCCURRENCES="5"

readonly JOURNAL="${STATE}/nh_interview_journal.jsonl"
readonly JOURNAL_HEAD="${STATE}/nh_interview_journal.head"
readonly AUTH_KEY="${STATE}/nh_interview_authenticity.key"
readonly LOCK_TXN="${STATE}/nh_candidate_transaction.lock"
readonly LOCK_JOURNAL="${STATE}/nh_interview_journal.lock"

# --- lab (keyed to the frozen N.H HEAD, exactly as specified) ---
readonly LAB="/home/ness/NH_AICP_SHADOW_REHEARSAL_ce3a38f43f287a56bd635ed836edf002a2db50a7"
readonly SHADOW_WS="${LAB}/shadow/NH_CLAUDE_CODEX_DESIGN_LOOP"
readonly RUNTIME_TMP="${LAB}/runtime/tmp"
readonly PROOF="${LAB}/proof"
readonly SHADOW_MARKER_NAME=".nh_shadow_marker"

# --- toolchain ---
readonly BWRAP="/usr/bin/bwrap"
readonly PY3="/usr/bin/python3"
readonly NODE_BIN="/home/ness/.nvm/versions/node/v24.18.0/bin"

# --- host model-auth / config witness set (HASHES AND METADATA ONLY) ---
readonly HOST_CODEX="/home/ness/.codex"
readonly HOST_CLAUDE="/home/ness/.claude"
readonly HOST_CLAUDE_JSON="/home/ness/.claude.json"

# Proof artefacts that MUST be byte-identical before and after.
readonly PROTECTED_PROOF_FILES=(
  "nh_loop.identity"
  "controller.git"
  "governance.git"
  "candidates.sha256"
  "interview_state.sha256"
  "interview_state.meta"
  "journal.counts"
  "workspace.files.sha256"
  "workspace.meta"
)

# Host model-auth / config witness. Reported separately and honestly: a
# concurrently running host Claude Code or Codex session legitimately rewrites
# ~/.claude.json and ~/.claude/* while this launcher runs, and that is NOT an
# isolation breach. It is still surfaced, and it still fails the launcher.
readonly CREDENTIAL_PROOF_FILES=(
  "credentials.sha256"
  "credentials.meta"
)

# ==========================================================================
# SECTION 1 — PLUMBING
# ==========================================================================

say()  { printf '%s\n' "$*"; }
note() { printf '[ok]    %s\n' "$*"; }
step() { printf '\n=== %s ===\n' "$*"; }

# ---- audit state. Every claim any report makes is derived from these. --------
#
# LAB_CREATED : the disposable lab exists on disk, so no report may say that
#               nothing was created.
# RUN_STARTED : the isolated controller run was entered, so no report may say
#               that no model or provider call was made.
# REPORTED    : a full report has already been printed, so the exit handler must
#               not print a second, contradictory one.
# AFTER_PROOF_DONE : the post-run re-proof of the protected original actually
#                    completed, so ORIGINAL_PROOF holds a real verdict. Until
#                    then no report may say anything about containment.
LAB_CREATED=0
RUN_STARTED=0
REPORTED=0
AFTER_PROOF_DONE=0
ORIGINAL_PROOF="NOT-RUN"

# The shared, honest tail. Both the block path and the unexpected-exit path use
# it, so the two can never drift apart and claim different things.
#
# Every sentence below is gated on evidence this launcher actually has. In
# particular it must NEVER assert that the protected original is untouched
# merely because the launcher's own code does not write to it: once the
# sandboxed run has been entered, containment is a claim about the ISOLATION,
# and only the completed AFTER proof can settle it.
report_state() {
  # --- what actually ran ---
  if [ "$RUN_STARTED" = "1" ]; then
    printf 'The isolated controller run WAS entered, so real Codex / Claude\n' >&2
    printf 'provider calls may already have been made.\n' >&2
  else
    printf 'No isolated controller run was started.\n' >&2
    printf 'No model or provider call was made.\n' >&2
  fi

  # --- what can honestly be said about the protected original ---
  if [ "$AFTER_PROOF_DONE" = "1" ]; then
    printf 'The protected original WAS re-proved after the run: %s\n' "$ORIGINAL_PROOF" >&2
  elif [ "$RUN_STARTED" = "1" ]; then
    printf 'The protected original has NOT been re-proved. This launcher never\n' >&2
    printf 'writes to it, but a sandboxed run was entered and whether that run\n' >&2
    printf 'stayed contained is UNVERIFIED. Do not assume the original is\n' >&2
    printf 'untouched -- re-verify it by hand before drawing any conclusion.\n' >&2
  else
    printf 'Nothing was written to the protected original: this launcher only ever\n' >&2
    printf 'reads it, and no sandboxed run was entered.\n' >&2
  fi

  # --- what is left on disk ---
  if [ "$LAB_CREATED" = "1" ]; then
    printf '\nA disposable lab WAS created by this run and is being left on disk for\n' >&2
    printf 'inspection (this launcher never deletes a lab):\n' >&2
    printf '  %s\n' "$LAB" >&2
    printf 'Its contents depend on how far this run got, and it INCLUDES a copy of\n' >&2
    printf 'the N.H interview authenticity key. It is mode 0700.\n' >&2
    printf 'Review it, then delete it. This launcher refuses to run again while\n' >&2
    printf 'that path exists.\n' >&2
  else
    printf 'This run created no lab.\n' >&2
  fi
}

die() {
  REPORTED=1
  printf '\n[BLOCKED] %s\n' "$*" >&2
  printf '\nSHADOW_REHEARSAL=BLOCKED\n' >&2
  report_state
  exit 1
}

# An EXIT handler, deliberately NOT an ERR handler.
#
# An ERR trap fires even under `set +e`, so it would hijack the two places where
# a non-zero exit is EXPECTED and handled on purpose: the isolation self-test,
# and above all the one real controller run, whose non-zero exit is an ordinary
# outcome this launcher exists to record. An ERR trap there would abort before
# the AFTER proof ever ran -- destroying the most important safety output --
# while printing claims that were false at that point. An EXIT handler fires
# once, only on actual script exit, and cannot interfere with a handled status.
on_exit() {
  local rc=$?
  trap - EXIT
  if [ "$rc" -ne 0 ] && [ "$REPORTED" != "1" ]; then
    REPORTED=1
    printf '\n[BLOCKED] the launcher stopped unexpectedly (exit %s)\n' "$rc" >&2
    printf '\nSHADOW_REHEARSAL=BLOCKED\n' >&2
    # No fixed claim about the proof here: report_state states exactly what was
    # and was not established, from the flags, so this path cannot contradict it.
    report_state
  fi
  exit "$rc"
}
trap on_exit EXIT

need_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "required command not found: $1"
}

expect() {
  # expect <label> <actual> <expected>
  local label="$1" actual="$2" expected="$3"
  if [ "$actual" != "$expected" ]; then
    die "frozen identity mismatch for ${label}
        expected: ${expected}
        actual:   ${actual}
      The protected source state has moved. The rehearsal refuses to run against
      source that is not the source this launcher was frozen against."
  fi
  note "${label} matches frozen identity"
}

sha_of()   { sha256sum -- "$1" | awk '{print $1}'; }
bytes_of() { stat -c '%s' -- "$1"; }

# Read-only git. GIT_OPTIONAL_LOCKS=0 keeps `git status` from refreshing (and
# therefore writing) the index. There is no Git write anywhere in this file.
git_ro() {
  local repo="$1"; shift
  GIT_OPTIONAL_LOCKS=0 GIT_TERMINAL_PROMPT=0 git --no-optional-locks -C "$repo" "$@"
}

# ==========================================================================
# SECTION 2 — ORIGINAL PROOF CAPTURE (hashes and metadata only, never secrets)
# ==========================================================================

capture_original_proof() {
  local out="$1"
  mkdir -p "$out"

  # --- nh_loop.py identity ---
  {
    printf 'sha256 %s\n' "$(sha_of "${CTRL}/nh_loop.py")"
    printf 'bytes  %s\n'  "$(bytes_of "${CTRL}/nh_loop.py")"
    printf 'lines  %s\n'  "$(wc -l < "${CTRL}/nh_loop.py")"
    printf 'stat   %s\n'  "$(stat -c 'mode=%f perm=%a uid=%u gid=%g size=%s mtime=%Y ctime=%Z inode=%i links=%h' -- "${CTRL}/nh_loop.py")"
  } > "${out}/nh_loop.identity"

  # --- controller git state (read-only) ---
  {
    printf 'branch %s\n' "$(git_ro "$CTRL" rev-parse --abbrev-ref HEAD)"
    printf 'head   %s\n' "$(git_ro "$CTRL" rev-parse HEAD)"
    printf 'status\n'
    git_ro "$CTRL" status --porcelain=v1 --untracked-files=all | LC_ALL=C sort
  } > "${out}/controller.git"

  # --- N.H git state (read-only) ---
  {
    printf 'branch %s\n' "$(git_ro "$NHGOV" rev-parse --abbrev-ref HEAD)"
    printf 'head   %s\n' "$(git_ro "$NHGOV" rev-parse HEAD)"
    printf 'status\n'
    git_ro "$NHGOV" status --porcelain=v1 --untracked-files=all | LC_ALL=C sort
  } > "${out}/governance.git"

  # --- the three candidates ---
  {
    local c
    for c in "$CAND_V10" "$CAND_V11" "$CAND_V12"; do
      printf '%s %s %s\n' "$(sha_of "${CAND_DIR}/${c}")" "$(bytes_of "${CAND_DIR}/${c}")" "$c"
    done
  } > "${out}/candidates.sha256"

  # --- every authenticated interview-state file ---
  find "$STATE" -maxdepth 1 -type f -print0 \
    | LC_ALL=C sort -z \
    | xargs -0 -r sha256sum -- \
    > "${out}/interview_state.sha256"

  find "$STATE" -maxdepth 1 -printf '%y %m %U %G %s %T@ %n %p\n' \
    | LC_ALL=C sort \
    > "${out}/interview_state.meta"

  # --- journal line / event / scope counts ---
  {
    printf 'lines           %s\n' "$(wc -l < "$JOURNAL")"
    printf 'events          %s\n' "$(grep -c '[^[:space:]]' -- "$JOURNAL" || true)"
    printf 'bytes           %s\n' "$(bytes_of "$JOURNAL")"
    printf 'journal_sha256  %s\n' "$(sha_of "$JOURNAL")"
    printf 'head_sha256     %s\n' "$(sha_of "$JOURNAL_HEAD")"
    printf 'key_sha256      %s\n' "$(sha_of "$AUTH_KEY")"
    printf 'pkg_scope       %s\n' "$EXP_PKG_SCOPE"
    printf 'pkg_occurrences %s\n' "$(grep -c -F -- "$EXP_PKG_SCOPE" "$JOURNAL" || true)"
  } > "${out}/journal.counts"

  # --- complete protected workspace: every file hashed ---
  find "$WS" -xdev -type f -print0 \
    | LC_ALL=C sort -z \
    | xargs -0 -r sha256sum -- \
    > "${out}/workspace.files.sha256"

  # --- complete protected workspace: metadata for every entry ---
  find "$WS" -xdev -printf '%y %m %U %G %s %T@ %n %p\n' \
    | LC_ALL=C sort \
    > "${out}/workspace.meta"

  # --- host model-auth / config witness: HASHES AND METADATA ONLY ---
  # Contents are never read into the proof. A sha256 is a one-way digest and no
  # credential value can be recovered from it.
  {
    local f
    for f in "$HOST_CLAUDE_JSON" \
             "${HOST_CLAUDE}/.credentials.json" \
             "${HOST_CLAUDE}/settings.json" \
             "${HOST_CLAUDE}/settings.local.json" \
             "${HOST_CODEX}/auth.json" \
             "${HOST_CODEX}/config.toml" \
             "/home/ness/.netrc"; do
      if [ -e "$f" ]; then
        printf '%s  %s\n' "$(sha_of "$f")" "$f"
      else
        printf '%s  %s\n' "ABSENT" "$f"
      fi
    done
    local d
    for d in "/home/ness/.ssh" "/home/ness/.config"; do
      if [ -d "$d" ]; then
        find "$d" -maxdepth 1 -type f -print0 2>/dev/null \
          | LC_ALL=C sort -z \
          | xargs -0 -r sha256sum -- 2>/dev/null || true
      fi
    done
  } > "${out}/credentials.sha256"

  {
    local p
    for p in "$HOST_CLAUDE_JSON" "${HOST_CLAUDE}/.credentials.json" \
             "${HOST_CODEX}/auth.json" "${HOST_CODEX}/config.toml" \
             "/home/ness/.netrc" "/home/ness/.ssh" "/home/ness/.config" \
             "$HOST_CODEX" "$HOST_CLAUDE"; do
      if [ -e "$p" ]; then
        find "$p" -maxdepth 1 -printf '%y %m %U %G %s %T@ %n %p\n' 2>/dev/null || true
      else
        printf 'ABSENT %s\n' "$p"
      fi
    done
  } | LC_ALL=C sort > "${out}/credentials.meta"
}

# compare_proof <before_dir> <after_dir> <label> <array-name...>
compare_proof_set() {
  local a="$1" b="$2" label="$3"; shift 3
  local rc=0 f dst
  for f in "$@"; do
    dst="${PROOF}/DIFF.${label}.${f}.txt"
    if diff -u "${a}/${f}" "${b}/${f}" > "$dst" 2>&1; then
      rm -f "$dst"
    else
      rc=1
      say "[DIFFERS] ${f}  ->  ${dst}"
    fi
  done
  return "$rc"
}

# ==========================================================================
# SECTION 3 — FAIL-CLOSED PRECONDITIONS
# ==========================================================================

step "PRECONDITIONS"

[ "$(id -u)" -ne 0 ] || die "refusing to run as root; run as the user ness"
[ "$(id -un)" = "ness" ] || die "must run as the user ness (found: $(id -un))"

for c in sha256sum stat find sort xargs diff rsync flock git awk grep wc mkdir; do
  need_cmd "$c"
done

[ -x "$BWRAP" ] || die "Bubblewrap is unavailable at ${BWRAP}; isolation cannot be established"
note "Bubblewrap present: $("$BWRAP" --version)"

[ -x "$PY3" ] || die "python3 is unavailable at ${PY3}"
[ -d "$NODE_BIN" ] || die "node bin directory missing: ${NODE_BIN}"
[ -x "${NODE_BIN}/codex" ] || die "codex client not found at ${NODE_BIN}/codex"
[ -x "${NODE_BIN}/claude" ] || die "claude client not found at ${NODE_BIN}/claude"

[ -d "$WS" ]    || die "protected workspace missing: ${WS}"
[ -d "$CTRL" ]  || die "controller missing: ${CTRL}"
[ -d "$NHGOV" ] || die "N.H checkout missing: ${NHGOV}"
[ -d "$STATE" ] || die "interview state missing: ${STATE}"
[ -d "$HOST_CODEX" ]  || die "host .codex missing; the copy-on-write credential overlay cannot be built"
[ -d "$HOST_CLAUDE" ] || die "host .claude missing; the copy-on-write credential overlay cannot be built"
[ -f "$HOST_CLAUDE_JSON" ] || die "host .claude.json missing; the client cannot start inside the namespace"

# The lab must not already exist. Never silently reuse. Never delete.
if [ -e "$LAB" ]; then
  die "the lab path already exists:
        ${LAB}
      This launcher never reuses and never deletes an earlier lab. Review it,
      move it aside or remove it yourself, then run this launcher again."
fi
note "lab path is free: ${LAB}"

# ==========================================================================
# SECTION 4 — FROZEN SOURCE IDENTITY GATE
# ==========================================================================

step "FROZEN SOURCE IDENTITY"

expect "nh_loop.py sha256"  "$(sha_of "${CTRL}/nh_loop.py")"        "$EXP_LOOP_SHA"
expect "nh_loop.py bytes"   "$(bytes_of "${CTRL}/nh_loop.py")"      "$EXP_LOOP_BYTES"
expect "nh_loop.py lines"   "$(wc -l < "${CTRL}/nh_loop.py")"       "$EXP_LOOP_LINES"

expect "controller branch"  "$(git_ro "$CTRL" rev-parse --abbrev-ref HEAD)" "$EXP_CTRL_BRANCH"
expect "controller HEAD"    "$(git_ro "$CTRL" rev-parse HEAD)"              "$EXP_CTRL_HEAD"

# The controller worktree must be exactly "only nh_loop.py modified". This
# launcher itself lives in controller/ and is therefore permitted to appear as
# the single extra untracked entry -- and nothing else may.
CTRL_STATUS_CORE="$(
  git_ro "$CTRL" status --porcelain=v1 --untracked-files=all \
    | grep -v -x -F "?? ${LAUNCHER_BASENAME}" || true
)"
expect "controller worktree" "$CTRL_STATUS_CORE" "$EXP_CTRL_STATUS_CORE"

expect "N.H branch"         "$(git_ro "$NHGOV" rev-parse --abbrev-ref HEAD)" "$EXP_NH_BRANCH"
expect "N.H HEAD"           "$(git_ro "$NHGOV" rev-parse HEAD)"              "$EXP_NH_HEAD"

NH_STATUS="$(git_ro "$NHGOV" status --porcelain=v1 --untracked-files=all | LC_ALL=C sort)"
NH_STATUS_EXPECTED="$(
  printf '%s\n' \
    "?? 05_ACTIVE_CANDIDATE/${CAND_V10}" \
    "?? 05_ACTIVE_CANDIDATE/${CAND_V11}" \
    "?? 05_ACTIVE_CANDIDATE/${CAND_V12}" | LC_ALL=C sort
)"
expect "N.H worktree" "$NH_STATUS" "$NH_STATUS_EXPECTED"

expect "candidate v1.0 sha256" "$(sha_of "${CAND_DIR}/${CAND_V10}")"   "$EXP_V10_SHA"
expect "candidate v1.0 bytes"  "$(bytes_of "${CAND_DIR}/${CAND_V10}")" "$EXP_V10_BYTES"
expect "candidate v1.1 sha256" "$(sha_of "${CAND_DIR}/${CAND_V11}")"   "$EXP_V11_SHA"
expect "candidate v1.1 bytes"  "$(bytes_of "${CAND_DIR}/${CAND_V11}")" "$EXP_V11_BYTES"
expect "candidate v1.2 sha256" "$(sha_of "${CAND_DIR}/${CAND_V12}")"   "$EXP_V12_SHA"
expect "candidate v1.2 bytes"  "$(bytes_of "${CAND_DIR}/${CAND_V12}")" "$EXP_V12_BYTES"

expect "journal sha256"  "$(sha_of "$JOURNAL")"          "$EXP_JOURNAL_SHA"
expect "journal bytes"   "$(bytes_of "$JOURNAL")"        "$EXP_JOURNAL_BYTES"
expect "journal events"  "$(grep -c '[^[:space:]]' -- "$JOURNAL" || true)" "$EXP_JOURNAL_EVENTS"
expect "journal head sha256"     "$(sha_of "$JOURNAL_HEAD")" "$EXP_HEAD_SHA"
expect "authenticity key sha256" "$(sha_of "$AUTH_KEY")"    "$EXP_KEY_SHA"
expect "authenticated package scope occurrences" \
       "$(grep -c -F -- "$EXP_PKG_SCOPE" "$JOURNAL" || true)" "$EXP_PKG_SCOPE_OCCURRENCES"

[ -f "$LOCK_TXN" ]     || die "candidate-transaction lock file missing: ${LOCK_TXN}"
[ -f "$LOCK_JOURNAL" ] || die "interview-journal lock file missing: ${LOCK_JOURNAL}"

note "every frozen identity matches; source state has not moved"

# ==========================================================================
# SECTION 5 — CREATE THE LAB
# ==========================================================================

step "LAB"

mkdir -m 0700 -p "$LAB"
LAB_CREATED=1          # from here on, every failure report must disclose the lab
mkdir -m 0700 -p "${LAB}/shadow" "${LAB}/runtime" "$RUNTIME_TMP" "$PROOF"
chmod 0700 "$LAB"
note "lab created (mode 0700): ${LAB}"
say  "        NOTE: the lab will contain a copy of the N.H interview authenticity"
say  "        key, because the controller cannot append authenticated journal"
say  "        events without it. Delete the lab after review."

# ==========================================================================
# SECTION 6 — TAKE BOTH ORIGINAL LOCKS, NON-BLOCKING
# ==========================================================================

step "ORIGINAL LOCKS"

# flock(2) is the same kernel lock primitive the controller takes with
# fcntl.flock, so this genuinely excludes a concurrent controller.
exec 200<"$LOCK_TXN"
flock -n -x 200 || die "the original candidate-transaction lock is held by another process.
      Something else is mid-transaction on the protected original. Refusing to copy."
note "candidate-transaction lock acquired (non-blocking)"

exec 201<"$LOCK_JOURNAL"
flock -n -x 201 || die "the original interview-journal lock is held by another process.
      Something else is mid-append on the protected original. Refusing to copy."
note "interview-journal lock acquired (non-blocking)"

# ==========================================================================
# SECTION 7 — PROOF BEFORE, COPY, VERIFY COPY, PROOF DURING  (locks held)
# ==========================================================================

step "ORIGINAL PROOF (BEFORE)"
capture_original_proof "${PROOF}/original.before"
note "before-proof written to ${PROOF}/original.before"

step "SHADOW COPY"

# What is deliberately NOT copied:
#   controller/__pycache__/   - build noise
#   write-test/               - scratch, not part of the rehearsal
#   .ssh .netrc .config       - not in the workspace at all, and never copied
#   host .codex / .claude     - never copied; they are namespace-only anonymous
#                               copy-on-write overlays instead
#   /tmp/nh_design_loop_disposable_*  - not in the workspace at all
RSYNC_EXCLUDES=(
  "--exclude=/controller/__pycache__/"
  "--exclude=/write-test/"
)

mkdir -m 0700 -p "$SHADOW_WS"
rsync -aHAX --numeric-ids --delete "${RSYNC_EXCLUDES[@]}" "${WS}/" "${SHADOW_WS}/" \
  || die "rsync copy of the workspace into the shadow failed"
note "workspace copied into ${SHADOW_WS}"

step "SHADOW COPY VERIFICATION"

# Checksum dry-run compare. Any itemised line at all means the shadow is not a
# truthful copy of the original, and the rehearsal must not proceed.
COPY_DIFF="$(
  rsync -aHAXn --delete --checksum --itemize-changes "${RSYNC_EXCLUDES[@]}" \
        "${WS}/" "${SHADOW_WS}/" 2>&1 || true
)"
if [ -n "$COPY_DIFF" ]; then
  printf '%s\n' "$COPY_DIFF" > "${PROOF}/DIFF.shadow-copy.txt"
  die "the shadow copy differs from the original.
      See ${PROOF}/DIFF.shadow-copy.txt
      Refusing to rehearse against an untruthful copy."
fi
note "shadow is a byte-truthful copy of the protected original"

step "ORIGINAL PROOF (DURING) — proving the original did not move while copying"
capture_original_proof "${PROOF}/original.during"
if ! compare_proof_set "${PROOF}/original.before" "${PROOF}/original.during" "during" \
        "${PROTECTED_PROOF_FILES[@]}"; then
  die "the protected original changed WHILE it was being copied.
      The copy is not a coherent snapshot. Refusing to rehearse."
fi
note "protected original unchanged across the whole copy window"

# ==========================================================================
# SECTION 8 — RELEASE BOTH ORIGINAL LOCKS
# ==========================================================================

step "RELEASING ORIGINAL LOCKS"

# Only the lock FILES were copied. Kernel lock ownership is dropped here and is
# never carried into the namespace: these descriptors are closed before bwrap.
flock -u 200 || true
exec 200<&-
flock -u 201 || true
exec 201<&-
note "both original locks released; no lock ownership enters the shadow"

# The shadow marker. It exists ONLY in the shadow, never in the original, so its
# presence inside the namespace at the normal N.H path is positive proof that
# the substitution happened and the real workspace is not what is mounted.
# Written AFTER copy verification so it can never pollute that comparison. It
# sits at the workspace root, outside both Git checkouts, so neither repository
# worktree status is affected.
SHADOW_TOKEN="nh-shadow-${EXP_NH_HEAD}"
printf '%s\n' "$SHADOW_TOKEN" > "${SHADOW_WS}/${SHADOW_MARKER_NAME}"
printf '%s\n' "$SHADOW_TOKEN" > "${RUNTIME_TMP}/.nh_shadow_tmp_marker"
note "shadow marker placed"

# ==========================================================================
# SECTION 9 — THE BUBBLEWRAP NAMESPACE
# ==========================================================================

# One OUTER namespace. Everything below inherits it:
#
#   bwrap
#    -> python3 nh_loop.py execute-next-claude-task
#       -> Codex          -> Codex helpers / nested sandbox
#       -> Claude
#
build_bwrap_args() {
  local claude_json_fd="$1"
  BWRAP_ARGS=(
    # --- namespaces ---
    --die-with-parent
    --new-session
    --unshare-all
    --share-net                       # ONLY because real provider calls need it
    --hostname nh-shadow-rehearsal

    # --- host root, read-only ---
    --ro-bind / /
    --proc /proc
    --dev /dev
    --tmpfs /dev/shm

    # --- the real /home/ness disappears completely ---
    --tmpfs /home/ness

    # --- put back only what is mechanically required ---
    --ro-bind "${HOME_REAL}/.nvm" "${HOME_REAL}/.nvm"

    # anonymous copy-on-write credential overlays: writable inside, writes land
    # in an invisible tmpfs, the host copies can never be reached
    --overlay-src "$HOST_CODEX"  --tmp-overlay "${HOME_REAL}/.codex"
    --overlay-src "$HOST_CLAUDE" --tmp-overlay "${HOME_REAL}/.claude"

    # .claude.json is materialised from a file descriptor straight into the
    # namespace tmpfs. It is writable inside, it is discarded when the namespace
    # dies, and it is NEVER copied into the persistent lab.
    --perms 0600 --file "$claude_json_fd" "$HOST_CLAUDE_JSON"

    # THE SUBSTITUTION: the shadow appears at the exact canonical path that
    # nh_loop.py hardcodes and resolves with realpath().
    --bind "$SHADOW_WS" "$WS"

    # disposable /tmp, kept in the lab
    --bind "$RUNTIME_TMP" /tmp

    # isolated runtime dirs
    --tmpfs /run
    --perms 0700 --dir /run/user/1000

    # --- environment: cleared, then only the required values ---
    --clearenv
    --setenv HOME "$HOME_REAL"
    --setenv USER ness
    --setenv LOGNAME ness
    --setenv PATH "${NODE_BIN}:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    --setenv LANG C.utf8
    --setenv TERM dumb
    --setenv TMPDIR /tmp
    --setenv XDG_RUNTIME_DIR /run/user/1000
    --setenv CODEX_HOME "${HOME_REAL}/.codex"
    --setenv CLAUDE_CONFIG_DIR "${HOME_REAL}/.claude"
    --setenv NH_LOOP_INTERVIEW_STATE_DIR "${WS}/nh_interview_state"
    --setenv GIT_OPTIONAL_LOCKS 0
    --setenv GIT_CONFIG_NOSYSTEM 1
    --setenv GIT_CONFIG_GLOBAL /dev/null
    --setenv GIT_TERMINAL_PROMPT 0
    --setenv GCM_INTERACTIVE never
    --setenv NO_COLOR 1

    --chdir "${WS}/controller"
  )
  # Nothing else is forwarded. --clearenv means OPENAI_API_KEY,
  # ANTHROPIC_API_KEY, GitHub tokens, cloud credentials and proxy credentials
  # cannot reach the sandbox from this shell's environment. The clients use
  # their own login state through the copy-on-write credential mounts above.
}

# ==========================================================================
# SECTION 10 — ISOLATION SELF-TEST (no models, no controller, no python)
# ==========================================================================

step "ISOLATION SELF-TEST"

# This proves the namespace is actually the namespace we asked for, BEFORE any
# real model call happens. It runs /bin/sh only. It never invokes python, Codex,
# Claude or nh_loop.py. If any assertion fails the rehearsal is refused; the
# isolation is never weakened to continue.
read -r -d '' SELFTEST <<'SELFTEST_EOF' || true
set -eu
fail() { printf 'SELFTEST_FAIL %s\n' "$*" >&2; exit 9; }

# exact mount-point -> fstype from /proc/self/mountinfo (last match wins, i.e.
# the mount actually on top at that path)
fstype_at() {
  target="$1"
  awk -v t="$target" '
    {
      mp = $5
      sep = 0
      for (i = 7; i <= NF; i++) if ($i == "-") { sep = i; break }
      if (sep && mp == t) ft = $(sep+1)
    }
    END { if (ft != "") print ft }
  ' /proc/self/mountinfo
}

# read the hostname from procfs, not from a `hostname` binary that may not exist
[ "$(cat /proc/sys/kernel/hostname)" = "nh-shadow-rehearsal" ] \
  || fail "hostname is not the sandbox hostname -- UTS namespace not established"
[ "$HOME" = "/home/ness" ] || fail "HOME wrong"
[ "$USER" = "ness" ] || fail "USER wrong"
[ "$TMPDIR" = "/tmp" ] || fail "TMPDIR wrong"
[ "$CODEX_HOME" = "/home/ness/.codex" ] || fail "CODEX_HOME wrong"
[ "$CLAUDE_CONFIG_DIR" = "/home/ness/.claude" ] || fail "CLAUDE_CONFIG_DIR wrong"

# no host secret may have leaked in through the environment
for v in OPENAI_API_KEY ANTHROPIC_API_KEY GITHUB_TOKEN GH_TOKEN AWS_ACCESS_KEY_ID \
         AWS_SECRET_ACCESS_KEY GOOGLE_APPLICATION_CREDENTIALS HTTPS_PROXY_CREDENTIALS; do
  eval "val=\${$v:-}"
  [ -z "${val}" ] || fail "host secret env leaked into the namespace: $v"
done

# the real home is gone
t="$(fstype_at /home/ness)"
[ "$t" = "tmpfs" ] || fail "/home/ness is not tmpfs (got: ${t:-none}) -- the real home is not hidden"

# the real credential material is not reachable
[ ! -e /home/ness/.ssh ]    || fail ".ssh is visible inside the namespace"
[ ! -e /home/ness/.netrc ]  || fail ".netrc is visible inside the namespace"
[ ! -e /home/ness/.config ] || fail ".config is visible inside the namespace"

# .codex and .claude are anonymous copy-on-write overlays
t="$(fstype_at /home/ness/.codex)"
[ "$t" = "overlay" ] || fail "/home/ness/.codex is not an overlay (got: ${t:-none})"
t="$(fstype_at /home/ness/.claude)"
[ "$t" = "overlay" ] || fail "/home/ness/.claude is not an overlay (got: ${t:-none})"

# the overlays are writable, and by construction writes go to the invisible
# tmpfs upper layer, never to the host
probe="/home/ness/.codex/.nh_shadow_cow_probe"
: > "$probe" || fail ".codex overlay is not writable"
rm -f "$probe"
probe="/home/ness/.claude/.nh_shadow_cow_probe"
: > "$probe" || fail ".claude overlay is not writable"
rm -f "$probe"

# the client config is present and writable, and it is namespace-only
[ -f /home/ness/.claude.json ] || fail ".claude.json missing inside the namespace"
[ -w /home/ness/.claude.json ] || fail ".claude.json not writable inside the namespace"

# the toolchain is reachable
[ -x /home/ness/.nvm/versions/node/v24.18.0/bin/codex ]  || fail "codex not reachable"
[ -x /home/ness/.nvm/versions/node/v24.18.0/bin/claude ] || fail "claude not reachable"
[ -x /usr/bin/python3 ] || fail "python3 not reachable"

# THE SUBSTITUTION: the normal N.H path is the shadow, not the original
[ -f "/home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/.nh_shadow_marker" ] \
  || fail "the workspace at the normal path is NOT the shadow -- refusing"
[ "$(cat /home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/.nh_shadow_marker)" = "$NH_SHADOW_TOKEN" ] \
  || fail "shadow marker token mismatch at the normal path"
[ -w /home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/NH-GOVERNANCE/05_ACTIVE_CANDIDATE ] \
  || fail "the shadow candidate directory is not writable"
[ -d /home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/controller ] || fail "shadow controller missing"

# realpath of the N.H checkout must still be the canonical hardcoded path
rp="$(cd /home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/NH-GOVERNANCE && pwd -P)"
[ "$rp" = "/home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/NH-GOVERNANCE" ] \
  || fail "canonical path substitution not visible (got: $rp)"

# /tmp is the lab runtime tmp
[ -f /tmp/.nh_shadow_tmp_marker ] || fail "/tmp is not the lab runtime tmp"

# runtime dir
[ -d /run/user/1000 ] || fail "/run/user/1000 missing"

printf 'SELFTEST_PASS\n'
SELFTEST_EOF

build_bwrap_args 11
exec 11<"$HOST_CLAUDE_JSON"
set +e
SELFTEST_OUT="$(
  "$BWRAP" "${BWRAP_ARGS[@]}" \
    --setenv NH_SHADOW_TOKEN "$SHADOW_TOKEN" \
    -- /bin/sh -c "$SELFTEST" 2>&1 </dev/null
)"
SELFTEST_RC=$?
set -e
exec 11<&- 2>/dev/null || true

printf '%s\n' "$SELFTEST_OUT" > "${PROOF}/isolation-selftest.txt"
if [ "$SELFTEST_RC" -ne 0 ] || ! printf '%s' "$SELFTEST_OUT" | grep -q '^SELFTEST_PASS$'; then
  printf '%s\n' "$SELFTEST_OUT" >&2
  die "the required namespace isolation could not be established (rc=${SELFTEST_RC}).
      See ${PROOF}/isolation-selftest.txt
      The isolation is NOT weakened to continue. No model call was made."
fi
note "isolation self-test PASS (see ${PROOF}/isolation-selftest.txt)"

# The copy-on-write proof, checked from OUTSIDE: the probe files the self-test
# wrote into the overlays must not exist on the host.
[ ! -e "${HOST_CODEX}/.nh_shadow_cow_probe" ] \
  || die "copy-on-write overlay LEAKED to the host .codex -- refusing to rehearse"
[ ! -e "${HOST_CLAUDE}/.nh_shadow_cow_probe" ] \
  || die "copy-on-write overlay LEAKED to the host .claude -- refusing to rehearse"
note "copy-on-write overlays proved non-leaking from outside the namespace"

# The persistent lab must contain no model login material.
if find "$LAB" \( -name '.credentials.json' -o -name 'auth.json' -o -name '.claude.json' \
                  -o -name 'id_rsa*' -o -name 'id_ed25519*' -o -name '.netrc' \) \
        -print -quit | grep -q . ; then
  die "model login material was found inside the persistent lab -- refusing to rehearse"
fi
note "no model login material exists inside the persistent lab"

# ==========================================================================
# SECTION 11 — THE ONE REAL TEST
# ==========================================================================
#
# EXACTLY ONE outer execution of the controller, inside Bubblewrap.
# There is no retry loop here and nothing reruns it. If it fails, it fails once.
# The controller's own bounded correction loop, its own lifetime correction-round
# limit, its own Codex (gpt-5.6-sol / xhigh / read-only-ephemeral where it says
# so) and its own Claude configuration are left exactly as they are.
#
step "ONE ISOLATED REAL REHEARSAL"

say "Running, inside the namespace:"
say "  ${PY3} ${WS}/controller/nh_loop.py execute-next-claude-task"
say ""
say "Live output is being written to:"
say "  ${PROOF}/shadow-run.stdout"
say "  ${PROOF}/shadow-run.stderr"
say "(tail -f either file from another terminal to watch it.)"
say ""

build_bwrap_args 11
exec 11<"$HOST_CLAUDE_JSON"

# From here on no report may claim that no model or provider call was made.
RUN_STARTED=1

# A non-zero exit here is an ORDINARY, EXPECTED outcome that this launcher
# exists to record. It must not abort the script: the AFTER proof below is the
# most important thing this launcher produces and it runs either way.
set +e
"$BWRAP" "${BWRAP_ARGS[@]}" \
  -- "$PY3" "${WS}/controller/nh_loop.py" execute-next-claude-task \
  > "${PROOF}/shadow-run.stdout" \
  2> "${PROOF}/shadow-run.stderr" \
  < /dev/null
SHADOW_RC=$?
set -e

exec 11<&- 2>/dev/null || true
printf '%s\n' "$SHADOW_RC" > "${PROOF}/shadow-run.exit-code"
note "isolated controller run finished with exit code ${SHADOW_RC}"

# ==========================================================================
# SECTION 12 — RE-PROVE THE ORIGINAL, FROM OUTSIDE THE NAMESPACE
# ==========================================================================

step "ORIGINAL PROOF (AFTER)"

capture_original_proof "${PROOF}/original.after"

ORIGINAL_PROOF="PASS"
if ! compare_proof_set "${PROOF}/original.before" "${PROOF}/original.after" "after" \
        "${PROTECTED_PROOF_FILES[@]}"; then
  ORIGINAL_PROOF="FAIL"
fi

# The protected verdict is SETTLED at this exact point, so the flag is raised
# here and not one line later.
#
# Everything below -- the host credential witness, the summary -- is separate
# and lesser. If any of it aborts unexpectedly, the report must still state the
# verdict this launcher genuinely holds. Raising the flag after those steps
# would let an abort in a lesser check downgrade a real verdict back to "not
# re-proved", which would hide a real ORIGINAL_WORKSPACE_PROOF=FAIL behind
# "unverified" -- the most dangerous possible misreport for this launcher.
AFTER_PROOF_DONE=1

CREDENTIAL_WITNESS="UNCHANGED"
if ! compare_proof_set "${PROOF}/original.before" "${PROOF}/original.after" "after-cred" \
        "${CREDENTIAL_PROOF_FILES[@]}"; then
  CREDENTIAL_WITNESS="CHANGED"
fi

# ==========================================================================
# SECTION 13 — SUMMARY
# ==========================================================================

# This summary IS the report, so the exit handler must not print a second one.
REPORTED=1

printf '\n'
printf '==================================================\n'
printf 'N.H SHADOW LIVE REHEARSAL — RESULT\n'
printf '==================================================\n'
printf 'SHADOW_LAB=%s\n'               "$LAB"
printf 'SHADOW_CONTROLLER_EXIT=%s\n'   "$SHADOW_RC"
printf 'ORIGINAL_WORKSPACE_PROOF=%s\n' "$ORIGINAL_PROOF"
printf 'HOST_CREDENTIAL_WITNESS=%s\n'  "$CREDENTIAL_WITNESS"
printf 'SHADOW_STDOUT=%s\n'            "${PROOF}/shadow-run.stdout"
printf 'SHADOW_STDERR=%s\n'            "${PROOF}/shadow-run.stderr"
printf '==================================================\n'

if [ "$ORIGINAL_PROOF" = "FAIL" ]; then
  printf '\nThe protected ORIGINAL workspace changed during the rehearsal.\n'
  printf 'Isolation did not hold. See the DIFF.after.* files under:\n'
  printf '  %s\n' "$PROOF"
fi

if [ "$CREDENTIAL_WITNESS" = "CHANGED" ]; then
  printf '\nHost model-auth/config files changed during the run. See the\n'
  printf 'DIFF.after-cred.* files under:\n'
  printf '  %s\n' "$PROOF"
  printf 'If another Claude Code or Codex session was running on this host, that\n'
  printf 'session rewrites ~/.claude.json and ~/.claude/* on its own and this is\n'
  printf 'expected. Otherwise treat it as an isolation finding and investigate.\n'
fi

printf '\nSCOPE OF THIS RESULT\n'
printf '  This was validation only, in a disposable laboratory.\n'
printf '  A controller PASS means ONLY that the isolated real rehearsal reached\n'
printf '  its own PASS. It is NOT N.H acceptance and NOT adoption of any\n'
printf '  candidate. No N.H policy was created. Nothing was integrated into\n'
printf '  Master or Map. All results live only in the lab.\n'
printf '\n  The lab holds a copy of the N.H interview authenticity key.\n'
printf '  Delete the lab once the rehearsal has been reviewed.\n\n'

# Fail closed: the original proof outranks the shadow result.
if [ "$ORIGINAL_PROOF" = "FAIL" ]; then
  exit 2
fi
if [ "$CREDENTIAL_WITNESS" = "CHANGED" ]; then
  exit 3
fi
exit "$SHADOW_RC"

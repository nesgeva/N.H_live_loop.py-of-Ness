# N.H Claude+Codex Design Loop — Controller

This repository is the local controller for the N.H Claude+Codex design loop.

It is **separate from the N.H governance repository**. Nothing here is part of governance.

The controller **must read** the real governance repository — that is how it checks authority, current design, dependencies, and the actual files. Reading is normal operation.

The controller **must not change** that repository. No writes, commits, pushes, merges, or rebases, and no other modification of it, unless the specific action has been explicitly authorized.

### Controller v1 is read-only toward governance, unconditionally

Controller **v1** is read-only toward the N.H governance repository **unconditionally**. It has **no capability** to write, commit, push, merge, rebase, fetch, reset, checkout, or modify remotes there. There is no flag, no configuration, and no authorization that turns any of that on in v1 — the capability simply does not exist.

The broader rule above still stands as the general rule for the future: a later controller version may perform an N.H repository-changing action **only** when that specific action has been explicitly authorized.

That future possibility does **not** apply to v1. In v1 the answer is always no, authorized or not.

## Who decides what

Ness remains the decision-maker. That includes:

- meaning
- policy
- priorities
- acceptance
- adoption
- permission to build

Nothing in this loop changes that. The loop produces proposals and review findings; Ness decides.

## The roles in the loop

- **Claude** is the design writer. It drafts the design work.
- **Codex/ChatGPT** is the independent, read-only reviewer. It reviews what Claude wrote and reports findings. It does not write the design and does not change anything.

## How findings are meant to flow

Mechanical BLOCK findings — the ones with a clear, objective fix — will eventually return automatically to Claude for correction, followed by a fresh review. That cycle is meant to run without pulling Ness in.

Only genuinely open Ness decisions should reach Ness: the questions that actually require judgement about meaning, policy, priorities, acceptance, adoption, or permission to build.

## Design and wiring together

Design and the matching wiring are handled together, not as separate passes. A design that cannot be wired up is not finished.

## Mode

The initial mode is **DESIGN-ONLY**.

The controller must never:

- auto-accept
- auto-adopt
- push to GitHub
- implement production N.H

Those are Ness's calls, made deliberately and outside this loop.

## What exists right now

The first controller stage — `status`, `preflight` safety checks, and the read-only `snapshot` — was built as controller **v1** and is preserved in Git history at its checkpoint. That foundation still runs unchanged.

The next stage added `codex-smoke`, a bounded, read-only Codex invocation, and is also preserved in Git history at its checkpoint.

```
python3 nh_loop.py codex-smoke
```

It runs the existing preflight checks first and fails closed without invoking Codex if they do not pass. If they pass, it makes exactly one Codex model run — read-only sandbox, ephemeral, fixed prompt on stdin, bounded timeout — and succeeds only if Codex exits 0 and replies with the exact expected line. Anything else fails closed.

Codex is invoked locally through its CLI, but the model request itself goes to its normal official service — the inference is not local or offline.

`codex-smoke` **cannot change N.H**. It sends no N.H file contents, prints no N.H file contents, and writes no files, state, logs, caches, commits, branches, or remotes anywhere. It proves only that the controller can safely invoke Codex and read one exact answer back.

The next stage added `claude-smoke`, a bounded Claude invocation with no tools at all, and is also preserved in Git history at its checkpoint.

```
python3 nh_loop.py claude-smoke
```

It follows the same shape as `codex-smoke`. It runs the existing preflight checks first and fails closed without invoking Claude if they do not pass. If they pass, it makes exactly one Claude run — fixed prompt on stdin, bounded timeout — and succeeds only if Claude exits 0 and replies with the exact expected line. Anything else fails closed.

Claude is launched locally through the Claude CLI, but its model request goes to its normal official service — the inference is not local or offline. These three smoke commands — `codex-smoke`, `claude-smoke`, and `claude-read-smoke` — are the only network or model behaviour in the controller.

`claude-smoke` isolates Claude completely, using three separate measures together:

- an **empty `--tools` value**, so no built-in Claude tools are available: no Read, Edit, Write, Bash, Glob, Grep, or Web
- an **empty `--mcp-config`** (`{"mcpServers":{}}`) together with **`--strict-mcp-config`**, so no user, project, local, or plugin MCP servers — and therefore no MCP tools — are available either
- **`--no-session-persistence`**, so the smoke does not persist Claude session history

With zero built-in tools and zero MCP tools, Claude cannot read, edit, write, search, or execute commands in N.H at all.

`claude-smoke` is a **connectivity and safety smoke only**. It is not actual N.H design writing. It sends no N.H file contents, prints no N.H file contents, and writes no files, state, logs, caches, commits, branches, or remotes anywhere. It proves only that the controller can safely invoke Claude with no tools at all and read one exact answer back.

**The current stage adds exactly one thing on top of that: `claude-read-smoke`, bounded read-only Claude access to the real N.H governance checkout.**

```
python3 nh_loop.py claude-read-smoke
```

Like the earlier smokes, it runs the existing preflight checks first and fails closed without invoking Claude if they do not pass. If they pass, it makes exactly one Claude run — invoked with `-p` and `--effort xhigh`, working directory `/home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/NH-GOVERNANCE` — and succeeds only if Claude exits 0 and replies with the exact expected line `CLAUDE_READ_CONTROLLER_OK`. Anything else fails closed.

The difference from `claude-smoke` is that Claude is no longer isolated from N.H. It is granted exactly three tools:

- **Read**
- **Glob**
- **Grep**

It is granted **no Edit, no Write, and no Bash**. In this stage Claude can inspect N.H but cannot edit it, write to it, or run commands in it.

The other isolation measures are unchanged:

- an **empty `--mcp-config`** together with **`--strict-mcp-config`**, so MCP remains disabled and no MCP tools are available
- **`--no-session-persistence`**, so session persistence remains disabled

Claude is instructed to read exactly one file, `01_AUTHORITATIVE/cursorrules`. The controller does **not** embed the contents of that file in the prompt — Claude has to read it through its own bounded read access, which is the point of the stage.

Observed so far: Python compilation passed, a real `claude-read-smoke` run passed, and the N.H governance Git working tree remained clean after the run.

`claude-read-smoke` proves only that the controller can grant Claude bounded read-only access to the real N.H checkout. It does **not** grant design-writing access, and it is not actual N.H design writing.

Still **not** implemented:

- actual Claude design-writing access — the controller cannot yet let Claude write N.H design work
- the automatic Claude → Codex → correction orchestration
- the browser UI, which comes later

The controller remains **DESIGN-ONLY**, and Ness still owns meaning, policy, priorities, acceptance, adoption, and permission to build.

## Intended interface

The intended final user interface is a local browser page. The browser UI, the controller, the repository checkout, the loop state, and the orchestration all run on the local machine.

Claude Code and Codex are invoked locally through their CLIs, but their model requests go to their normal official services. The model inference itself is not local or offline.

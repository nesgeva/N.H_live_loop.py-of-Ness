#!/usr/bin/env python3
"""Read-only STDIO MCP bridge to the existing N.H live-loop controller."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


WORKSPACE = Path(__file__).resolve().parent.parent
CONTROLLER = WORKSPACE / "controller" / "nh_loop.py"
PROTOCOL_VERSION = "2025-06-18"

TOOLS = [
    {
        "name": "nh_live_status",
        "title": "N.H Live Status",
        "description": "Return the real N.H controller supervisor-status result.",
        "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
        "annotations": {
            "readOnlyHint": True,
            "destructiveHint": False,
            "idempotentHint": True,
            "openWorldHint": False,
        },
    },
    {
        "name": "nh_live_next",
        "title": "N.H Live Next",
        "description": "Return the real N.H controller loop-status result.",
        "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
        "annotations": {
            "readOnlyHint": True,
            "destructiveHint": False,
            "idempotentHint": True,
            "openWorldHint": False,
        },
    },
]


def send(message: dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(message, separators=(",", ":")) + "\n")
    sys.stdout.flush()


def error(request_id: Any, code: int, message: str) -> None:
    send({"jsonrpc": "2.0", "id": request_id, "error": {"code": code, "message": message}})


def controller_status(command: str) -> dict[str, Any]:
    completed = subprocess.run(
        [sys.executable, "-B", str(CONTROLLER), command],
        cwd=WORKSPACE,
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )
    if completed.returncode != 0:
        detail = completed.stderr.strip() or completed.stdout.strip() or "no diagnostic output"
        raise RuntimeError(f"N.H controller exited {completed.returncode}: {detail}")
    try:
        result = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError("N.H controller did not return valid JSON") from exc
    if not isinstance(result, dict):
        raise RuntimeError("N.H controller returned a non-object JSON result")
    return result


def call_tool(name: str, arguments: Any) -> dict[str, Any]:
    if arguments not in (None, {}):
        raise ValueError("This read-only tool accepts no arguments")
    command = {
        "nh_live_status": "supervisor-status",
        "nh_live_next": "loop-status",
    }.get(name)
    if command is None:
        raise KeyError(name)
    result = controller_status(command)
    return {
        "content": [{"type": "text", "text": json.dumps(result, indent=2, sort_keys=True)}],
        "structuredContent": result,
        "isError": False,
    }


def handle(request: dict[str, Any]) -> bool:
    method = request.get("method")
    request_id = request.get("id")

    if method == "initialize":
        send(
            {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "protocolVersion": PROTOCOL_VERSION,
                    "capabilities": {"tools": {"listChanged": False}},
                    "serverInfo": {"name": "nh-live-readonly", "version": "1.0.0"},
                    "instructions": "Read-only status bridge. The existing N.H controller is the source of truth.",
                },
            }
        )
    elif method == "tools/list":
        send({"jsonrpc": "2.0", "id": request_id, "result": {"tools": TOOLS}})
    elif method == "tools/call":
        params = request.get("params", {})
        try:
            result = call_tool(params.get("name"), params.get("arguments", {}))
        except KeyError:
            error(request_id, -32602, "Unknown tool")
        except (RuntimeError, ValueError) as exc:
            send(
                {
                    "jsonrpc": "2.0",
                    "id": request_id,
                    "result": {
                        "content": [{"type": "text", "text": str(exc)}],
                        "isError": True,
                    },
                }
            )
        else:
            send({"jsonrpc": "2.0", "id": request_id, "result": result})
    elif method == "ping":
        send({"jsonrpc": "2.0", "id": request_id, "result": {}})
    elif method == "shutdown":
        send({"jsonrpc": "2.0", "id": request_id, "result": None})
    elif method == "exit":
        return False
    elif request_id is not None:
        error(request_id, -32601, "Method not found")
    return True


def main() -> int:
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            request = json.loads(line)
            if not isinstance(request, dict):
                raise ValueError
        except (json.JSONDecodeError, ValueError):
            error(None, -32700, "Parse error")
            continue
        if not handle(request):
            break
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Fail if rendering changes committed outputs besides the generated timestamp."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent
CLI = Path(__file__).resolve().parent / "hero_pipeline_cli.py"
HEROES_JSON = "site/data/heroes.json"
GENERATED_TIMESTAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")


def _run_git(root: Path, *args: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", "-C", str(root), *args],
        check=False,
        capture_output=True,
    )


def _decode(payload: bytes) -> str:
    return payload.decode("utf-8", errors="replace")


def _porcelain_paths(root: Path) -> list[tuple[str, str]]:
    result = _run_git(
        root,
        "status",
        "--porcelain=v1",
        "--untracked-files=all",
    )
    if result.returncode != 0:
        raise RuntimeError(_decode(result.stderr) or "git status failed")
    rows: list[tuple[str, str]] = []
    for raw in _decode(result.stdout).splitlines():
        if not raw:
            continue
        status = raw[:2]
        path = raw[3:]
        if path.startswith('"') and path.endswith('"'):
            path = path[1:-1]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        rows.append((status, path))
    return rows


def _head_bytes(root: Path, relpath: str) -> bytes | None:
    result = _run_git(root, "show", f"HEAD:{relpath}")
    if result.returncode != 0:
        return None
    return result.stdout


def _site_without_timestamp(payload: object) -> object:
    if not isinstance(payload, dict):
        return payload
    result = dict(payload)
    meta = dict(result.get("meta") or {})
    meta.pop("generated", None)
    result["meta"] = meta
    return result


def _timestamp_from(payload: object) -> object:
    if not isinstance(payload, dict):
        return None
    meta = payload.get("meta")
    if not isinstance(meta, dict):
        return None
    return meta.get("generated")


def heroes_json_drift(committed: bytes, current: bytes) -> list[str]:
    """Return errors if heroes.json differs beyond a valid generated timestamp."""
    errors: list[str] = []
    try:
        old = json.loads(committed.decode("utf-8"))
        new = json.loads(current.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        return [f"{HEROES_JSON} is not valid UTF-8 JSON: {exc}"]
    timestamp = _timestamp_from(new)
    if not isinstance(timestamp, str) or not GENERATED_TIMESTAMP_RE.fullmatch(
        timestamp
    ):
        errors.append(
            f"{HEROES_JSON} meta.generated must be a UTC timestamp "
            f"YYYY-MM-DDTHH:MM:SSZ, got {timestamp!r}"
        )
    if _site_without_timestamp(old) != _site_without_timestamp(new):
        errors.append(
            f"{HEROES_JSON} changed besides meta.generated"
        )
    return errors


def drift_errors(root: Path) -> list[str]:
    """Compare the working tree to HEAD, allowing only the generated timestamp."""
    errors: list[str] = []
    for status, relpath in _porcelain_paths(root):
        if status.strip() == "??":
            errors.append(f"unexpected untracked file: {relpath}")
            continue
        current_path = root / relpath
        committed = _head_bytes(root, relpath)
        if committed is None:
            errors.append(f"unexpected uncommitted path: {relpath}")
            continue
        if not current_path.is_file():
            errors.append(f"missing tracked file: {relpath}")
            continue
        current = current_path.read_bytes()
        if relpath == HEROES_JSON:
            errors.extend(heroes_json_drift(committed, current))
            continue
        if current != committed:
            errors.append(f"rendered output drifted: {relpath}")
    return errors


def render_views(root: Path) -> None:
    result = subprocess.run(
        [sys.executable, str(CLI), "views"],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip()
        raise RuntimeError(detail or "views rendering failed")


def main(argv: Iterable[str] | None = None) -> int:
    del argv
    render_views(ROOT)
    errors = drift_errors(ROOT)
    if errors:
        print("Rendered output drifted:", file=sys.stderr)
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("Rendered outputs match HEAD (timestamp excepted)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

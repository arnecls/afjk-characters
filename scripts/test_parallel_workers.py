#!/usr/bin/env python3
"""Choose pytest-xdist worker count from a memory budget probe.

Peak RSS measured on subset (test_skill_descriptions + test_hero_schema)
with ``-n auto``; extrapolated to full suite with 20% headroom. Budget 1536 MB.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VENV_PY = ROOT / ".venv" / "bin" / "python"
MEMORY_LIMIT_MB = 1536
SUBSET_PATHS = (
    "scripts/test_skill_descriptions.py",
    "scripts/test_hero_schema.py",
)
FULL_SUITE_TEST_COUNT = 471
# Subset probe peak ~891 MB (13 procs, -n auto); extrapolated full suite ~2142 MB
# → capped workers (not auto) on this machine.


def _python() -> str:
    return str(VENV_PY if VENV_PY.exists() else sys.executable)


def _pytest_cmd(*args: str) -> list[str]:
    return [_python(), "-m", "pytest", *args]


def _tree_pids(root_pid: int) -> set[int]:
    pids = {root_pid}
    try:
        out = subprocess.check_output(
            ["pgrep", "-P", str(root_pid)],
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return pids
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        child = int(line)
        pids |= _tree_pids(child)
    return pids


def _pid_rss_kb(pid: int) -> int:
    try:
        out = subprocess.check_output(
            ["ps", "-o", "rss=", "-p", str(pid)],
            text=True,
            stderr=subprocess.DEVNULL,
        )
        return int(out.strip())
    except (subprocess.CalledProcessError, ValueError, OSError):
        return 0


def _collect_test_count() -> int:
    proc = subprocess.run(
        _pytest_cmd(*SUBSET_PATHS, "--collect-only", "-q"),
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    match = re.search(r"(\d+)\s+tests?\s+collected", proc.stdout)
    if match:
        return int(match.group(1))
    return 235


def _probe_peak_rss_mb() -> tuple[float, int]:
    """Run parallel subset probe; return (peak_mb, max_worker_processes)."""
    cmd = _pytest_cmd(*SUBSET_PATHS, "-n", "auto", "-q", "--tb=no")
    proc = subprocess.Popen(
        cmd,
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    peak_kb = 0
    max_workers = 0
    while proc.poll() is None:
        pids = _tree_pids(proc.pid)
        max_workers = max(max_workers, len(pids))
        rss = sum(_pid_rss_kb(pid) for pid in pids)
        peak_kb = max(peak_kb, rss)
        time.sleep(0.25)
    if proc.returncode != 0:
        return 0.0, 0
    return peak_kb / 1024.0, max_workers


def main() -> None:
    override = os.environ.get("PYTEST_WORKERS")
    if override:
        print(override.strip())
        return

    peak_mb, worker_count = _probe_peak_rss_mb()
    if peak_mb <= 0 or worker_count <= 0:
        print("auto")
        return

    subset_count = _collect_test_count()
    extrapolated = peak_mb * (FULL_SUITE_TEST_COUNT / subset_count) * 1.2
    if extrapolated <= MEMORY_LIMIT_MB:
        print("auto")
        return

    per_worker_mb = peak_mb / worker_count
    capped = max(1, int(MEMORY_LIMIT_MB / per_worker_mb))
    print(str(capped))


if __name__ == "__main__":
    main()

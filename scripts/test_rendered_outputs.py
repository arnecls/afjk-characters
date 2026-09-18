"""Tests for post-render whole-tree output drift detection."""

from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from assert_rendered_outputs import (
    HEROES_JSON,
    drift_errors,
    heroes_json_drift,
)

COMMITTED = {
    "meta": {"generated": "2026-01-01T00:00:00Z", "hero_count": 1},
    "heroes": [{"name": "Cassadee"}],
}


def _payload(generated: str = "2026-09-18T12:00:00Z", **changes: object) -> bytes:
    body = json.loads(json.dumps(COMMITTED))
    body["meta"]["generated"] = generated
    body.update(changes)
    return json.dumps(body, indent=2).encode("utf-8")


def _git(root: Path, *args: str) -> None:
    subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        capture_output=True,
    )


def _repo_with(files: dict[str, bytes]) -> Path:
    root = Path(tempfile.mkdtemp())
    _git(root, "init")
    _git(root, "config", "user.email", "test@example.com")
    _git(root, "config", "user.name", "Test")
    for relpath, payload in files.items():
        path = root / relpath
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
    _git(root, "add", "-A")
    _git(root, "commit", "-m", "seed")
    return root


class HeroesJsonDriftTests(unittest.TestCase):
    def test_timestamp_only_change_is_allowed(self) -> None:
        self.assertEqual(
            heroes_json_drift(_payload("2026-01-01T00:00:00Z"), _payload()),
            [],
        )

    def test_missing_timestamp_is_rejected(self) -> None:
        current = json.loads(_payload())
        del current["meta"]["generated"]
        errors = heroes_json_drift(
            _payload("2026-01-01T00:00:00Z"),
            json.dumps(current).encode("utf-8"),
        )
        self.assertTrue(errors)
        self.assertIn("meta.generated", errors[0])

    def test_malformed_timestamp_is_rejected(self) -> None:
        errors = heroes_json_drift(
            _payload("2026-01-01T00:00:00Z"),
            _payload("not-a-timestamp"),
        )
        self.assertTrue(errors)
        self.assertIn("UTC timestamp", errors[0])

    def test_other_json_changes_are_rejected(self) -> None:
        current = json.loads(_payload())
        current["heroes"][0]["name"] = "Alsa"
        errors = heroes_json_drift(
            _payload("2026-01-01T00:00:00Z"),
            json.dumps(current).encode("utf-8"),
        )
        self.assertTrue(any("besides meta.generated" in item for item in errors))


class WorkingTreeDriftTests(unittest.TestCase):
    def test_line_ending_drift_is_rejected(self) -> None:
        root = _repo_with({"heroes-overview.csv": b"a,b\r\n1,2\r\n"})
        (root / "heroes-overview.csv").write_bytes(b"a,b\n1,2\n")
        self.assertIn(
            "rendered output drifted: heroes-overview.csv",
            drift_errors(root),
        )

    def test_unexpected_untracked_file_is_rejected(self) -> None:
        root = _repo_with({"Heroes.md": b"# Heroes\n"})
        (root / "extra.md").write_bytes(b"oops\n")
        self.assertIn("unexpected untracked file: extra.md", drift_errors(root))

    def test_preexisting_local_modification_is_rejected(self) -> None:
        root = _repo_with({"Heroes.md": b"# Heroes\n"})
        (root / "Heroes.md").write_bytes(b"# Dirty\n")
        self.assertIn("rendered output drifted: Heroes.md", drift_errors(root))

    def test_timestamp_only_working_tree_is_clean(self) -> None:
        root = _repo_with({HEROES_JSON: _payload("2026-01-01T00:00:00Z")})
        (root / HEROES_JSON).write_bytes(_payload("2026-09-18T15:01:02Z"))
        self.assertEqual(drift_errors(root), [])


if __name__ == "__main__":
    unittest.main()

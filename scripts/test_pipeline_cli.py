"""CLI scope tests for download, analyze, validate, and views."""

from __future__ import annotations

import inspect
import subprocess
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
CLI = SCRIPTS / "hero_pipeline_cli.py"


class PipelineCliScopeTests(unittest.TestCase):
    def test_views_rejects_hero_flag(self) -> None:
        result = subprocess.run(
            [sys.executable, str(CLI), "views", "--hero", "cassadee"],
            cwd=SCRIPTS.parent,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unrecognized arguments: --hero", result.stderr)

    def test_download_analyze_validate_keep_hero_flag(self) -> None:
        text = CLI.read_text(encoding="utf-8")
        for name in ("download", "analyze", "validate"):
            self.assertIn(f'{name}_p.add_argument("--hero")', text, name)

    def test_pipeline_views_is_full_roster(self) -> None:
        from hero_pipeline import pipeline

        self.assertNotIn("hero_id", inspect.signature(pipeline.views).parameters)
        self.assertIn("hero_id", inspect.signature(pipeline.analyze).parameters)
        self.assertIn("hero_id", inspect.signature(pipeline.download).parameters)
        self.assertIn("hero_id", inspect.signature(pipeline.validate).parameters)


if __name__ == "__main__":
    unittest.main()

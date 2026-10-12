#!/usr/bin/env python3
"""Tests for the mix synergy index zone/temp-buff keys and JS helpers."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

from hero_pipeline import pipeline
from hero_pipeline.presentation.project import project_roster
from hero_pipeline.presentation.site_payload import build_mix_synergy_index
from hero_pipeline.storage import load_config

_CACHE: dict = {}

NODE = shutil.which("node")
MIX_JS = ROOT / "site" / "js" / "src" / "views-mix.js"


def index() -> dict:
    """Build the mix synergy index once per test process."""
    if not _CACHE:
        processed, relationships, snapshot = pipeline.score()
        view = project_roster(
            snapshot,
            config=load_config(),
            analyses=processed["heroes"],
            relationships=relationships,
        )
        _CACHE["index"] = build_mix_synergy_index(view)
    return _CACHE["index"]


class MixSynergyIndexTests(unittest.TestCase):
    def test_existing_key_kept(self) -> None:
        self.assertIn("perseus", index()["byReceiver"])

    def test_grouping_uplift_pairs(self) -> None:
        uplift = index()["groupingUplift"]
        self.assertGreater(uplift["perseus"]["estrilda"], 0)
        self.assertGreater(uplift["orion"]["estrilda"], 0)
        self.assertNotIn("estrilda", uplift.get("silvina", {}))
        for receivers in uplift.values():
            for value in receivers.values():
                self.assertGreater(value, 0)
        for receiver in ("ravion", "nerion", "silven"):
            self.assertNotIn("estrilda", uplift.get(receiver, {}))

    def test_temp_buff_and_distinct_allies(self) -> None:
        idx = index()
        self.assertGreater(idx["tempBuff"]["perseus"]["isabella"], 0)
        self.assertEqual(idx["distinctAllies"]["perseus"], 2)
        self.assertEqual(idx["distinctAllies"]["orion"], 2)

    def test_groupers(self) -> None:
        groupers = index()["groupers"]
        self.assertIn("mehira", groupers)
        self.assertEqual(groupers, sorted(groupers))


HARNESS = r"""
const fs = require("fs");
const vm = require("vm");
const noop = function () {};
const window = {
  matchMedia: function () { return { matches: false, addEventListener: noop }; },
  AFKJ: {
    utils: { escapeHtml: String },
    config: {}, chips: {}, tiers: {},
    views: { grid: {} },
  },
};
vm.runInNewContext(fs.readFileSync(process.argv[2], "utf8"), {
  window: window, document: { addEventListener: noop }, console: console,
});
const mix = window.AFKJ.views.mix;
const index = {
  groupers: ["mehira"],
  groupingUplift: { perseus: { estrilda: 2 }, orion: { estrilda: 1 } },
  distinctAllies: { perseus: 2 },
  tempBuff: { perseus: { isabella: 4, other: 3, x: 1 } },
};
const no = function () { return false; };
const out = {
  noGrouper: mix.mixGroupingUplift(index, "estrilda", ["perseus"], no, 2),
  teamGrouper: mix.mixGroupingUplift(
    index, "estrilda", ["perseus", "mehira"], no, 2),
  teamGrouperMarked: mix.mixGroupingUplift(
    index, "estrilda", ["perseus", "mehira"],
    function (s) { return s === "perseus"; }, 2),
  candidateGrouper: mix.mixGroupingUplift(
    index, "mehira", ["perseus", "estrilda"], no, 2),
  first: mix.mixDistinctAlliesBonus(index, "isabella", ["perseus"], no, 2),
  second: mix.mixDistinctAlliesBonus(
    index, "isabella", ["perseus", "other"], no, 2),
  third: mix.mixDistinctAlliesBonus(
    index, "isabella", ["perseus", "other", "x"], no, 2),
};
console.log(JSON.stringify(out));
"""


@unittest.skipUnless(NODE, "node is not installed; JS helper test skipped")
class MixJsHelperTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / "harness.js"
            script.write_text(HARNESS, encoding="utf-8")
            check = subprocess.run(
                [NODE, "--check", str(MIX_JS)], capture_output=True, text=True
            )
            assert check.returncode == 0, check.stderr
            run = subprocess.run(
                [NODE, str(script), str(MIX_JS)],
                capture_output=True,
                text=True,
            )
        assert run.returncode == 0, run.stderr
        cls.out = json.loads(run.stdout.strip().splitlines()[-1])

    def test_uplift_needs_grouper(self) -> None:
        self.assertEqual(self.out["noGrouper"], 0)
        # Mehira on team: only candidate pairs (estrilda -> perseus).
        self.assertEqual(self.out["teamGrouper"], 2)
        self.assertEqual(self.out["teamGrouperMarked"], 4)

    def test_candidate_grouper_lifts_existing_pairs(self) -> None:
        # Estrilda is already in the drop zone; Mehira groups.
        self.assertEqual(self.out["candidateGrouper"], 2)

    def test_second_distinct_provider_only(self) -> None:
        self.assertEqual(self.out["first"], 0)
        self.assertEqual(self.out["second"], 2.0)
        self.assertEqual(self.out["third"], 0)


if __name__ == "__main__":
    unittest.main()

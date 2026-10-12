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
from hero_pipeline.relationships import scoring
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

    def test_protection_pairs(self) -> None:
        protection = index()["protection"]
        self.assertGreater(protection["frieren"]["alna"], 0)
        # Gunnar's protection is tile-bound and lives in tileBuff instead.
        for receivers in protection.values():
            self.assertNotIn("gunnar", receivers)
            for value in receivers.values():
                self.assertGreater(value, 0)

    def test_tile_buff_pairs(self) -> None:
        idx = index()
        tile = idx["tileBuff"]
        self.assertGreater(tile["gwyneth"]["gunnar"], 0)
        self.assertGreater(tile["gwyneth"]["hugin"], 0)
        # Hugin's ultimate Haste reaches any ally, so it stays outside.
        self.assertLess(
            tile["gwyneth"]["hugin"], idx["byReceiver"]["gwyneth"]["hugin"]
        )
        self.assertNotIn("gunnar", tile.get("sylphira", {}))
        for receiver, providers in tile.items():
            for provider, value in providers.items():
                self.assertIn(provider, idx["tileBuffers"])
                self.assertGreater(value, 0)
                self.assertLessEqual(
                    value, idx["byReceiver"][receiver][provider] + 1e-3
                )

    def test_tile_buffers_have_labels(self) -> None:
        self.assertEqual(
            index()["tileBuffers"], sorted(scoring.STATIC_TILE_BUFF_LABELS)
        )

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
  protection: { gwyneth: { gunnar: 6 }, frieren: { gunnar: 4 } },
};
const tiles = {
  tileBuffers: ["gunnar", "hugin"],
  tileBuff: {
    gwyneth: { gunnar: 28, hugin: 3 },
    gunnar: { hugin: 3 },
    hugin: { gunnar: 9 },
    carry: { gunnar: 10 },
  },
};
const no = function () { return false; };
const gwynethMarked = function (s) { return s === "gwyneth"; };
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
  protOne: mix.mixProtectionCorrection(index, "gunnar", ["gwyneth"], no, 2),
  protTwo: mix.mixProtectionCorrection(
    index, "gunnar", ["gwyneth", "frieren"], no, 2),
  protMarked: mix.mixProtectionCorrection(
    index, "gunnar", ["gwyneth", "frieren"],
    function (s) { return s === "frieren"; }, 2),
  tileHugin: mix.mixTileBuffCorrection(
    tiles, "hugin", ["gwyneth", "gunnar"], no, 2),
  tileGunnar: mix.mixTileBuffCorrection(
    tiles, "gunnar", ["gwyneth", "hugin"], no, 2),
  tileCycle: mix.mixTileBuffCorrection(tiles, "gunnar", ["hugin"], no, 2),
  tileReceiver: mix.mixTileBuffCorrection(tiles, "carry", ["gunnar"], no, 2),
  tileNoBuffer: mix.mixTileBuffCorrection(tiles, "carry", ["gwyneth"], no, 2),
  tileMarked: mix.mixTileBuffCorrection(
    tiles, "hugin", ["gwyneth", "gunnar"], gwynethMarked, 2),
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

    def test_protection_counts_best_receiver_only(self) -> None:
        self.assertEqual(self.out["protOne"], 0)
        # 6 + 4 summed by the base score; only the 6 should remain.
        self.assertEqual(self.out["protTwo"], -4)
        # Marked frieren counts 8; gwyneth's 6 is removed.
        self.assertEqual(self.out["protMarked"], -6)

    def test_tile_buffer_reaches_one_receiver(self) -> None:
        # Gunnar keeps Gwyneth; Hugin only gains by buffing Gunnar (3)
        # instead of the 3 + 3 the base sum credited.
        self.assertEqual(self.out["tileHugin"], -3)
        # Gunnar takes Gwyneth (28) and Hugin moves onto Gunnar (3 - 3):
        # gain 28 instead of the 28 + 9 the base sum credited.
        self.assertEqual(self.out["tileGunnar"], -9)

    def test_tile_buffers_cannot_stand_behind_each_other(self) -> None:
        # Gunnar -> Hugin (9) and Hugin -> Gunnar (3) cannot both hold.
        self.assertEqual(self.out["tileCycle"], 0)

    def test_tile_receiver_candidate_gains_free_buffer(self) -> None:
        self.assertEqual(self.out["tileReceiver"], 10)
        self.assertEqual(self.out["tileNoBuffer"], 0)

    def test_tile_marked_receiver(self) -> None:
        # Gwyneth counts double: base sum 6 + 3, marginal gain still 3.
        self.assertEqual(self.out["tileMarked"], -6)


if __name__ == "__main__":
    unittest.main()

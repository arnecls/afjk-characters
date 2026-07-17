#!/usr/bin/env python3
"""Tests for proximity-aura synergy reach gating."""

from __future__ import annotations

import importlib.util
import json
import re
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))


def _load_rs():
    spec = importlib.util.spec_from_file_location(
        "rewrite_summaries", SCRIPTS / "rewrite-summaries.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["rewrite_summaries"] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def _load_gen():
    spec = importlib.util.spec_from_file_location(
        "gen_overview", SCRIPTS / "generate-heroes-overview.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["gen_overview"] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def _hero_blocks() -> dict[str, str]:
    text = (ROOT / "Heroes.md").read_text(encoding="utf-8")
    blocks: dict[str, str] = {}
    for block in re.split(r"\n(?=## )", text):
        if block.startswith("## "):
            first = block.splitlines()[0].replace("## ", "").split(" - ", 1)[0]
            blocks[first.strip()] = block
    return blocks


class ProximityDetectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.rs = _load_rs()
        blocks = _hero_blocks()
        cls.shakir = cls.rs.parse_hero_block(blocks["Shakir"])
        cls.rs.analyze_hero(cls.shakir)
        twins = cls.rs.parse_hero_block(blocks["Elijah & Lailah"])
        cls.rs.analyze_hero(twins)
        cls.twins = twins

    def test_shakir_detects_proximity_haste(self) -> None:
        self.assertIn("Haste", self.shakir.proximity_aura_buff_labels)
        self.assertIn(
            "Damage taken", self.shakir.proximity_aura_buff_labels
        )
        self.assertEqual(self.shakir.proximity_aura_radius, 2.0)

    def test_twins_global_haste_not_proximity(self) -> None:
        self.assertNotIn("Haste", self.twins.proximity_aura_buff_labels)

    def test_perseus_detects_fertile_ground_proximity(self) -> None:
        blocks = _hero_blocks()
        perseus = self.rs.parse_hero_block(blocks["Perseus"])
        self.rs.analyze_hero(perseus)
        self.assertIn("ATK", perseus.proximity_aura_buff_labels)
        self.assertIn("Phys DEF", perseus.proximity_aura_buff_labels)
        self.assertIn("Magic DEF", perseus.proximity_aura_buff_labels)
        self.assertEqual(perseus.proximity_aura_radius, 1.0)


class ProximityReachGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        from process_config import apply_config

        cls.rs = _load_rs()
        cls.gen = _load_gen()
        apply_config(
            json.loads((ROOT / "data/heroes_config.json").read_text())
        )
        blocks = _hero_blocks()
        keys = [
            "Shakir",
            "Hugin",
            "Bonnie",
            "Frieren",
            "Shemira",
            "Marilee",
            "Hepler",
            "Baelran",
            "Elijah & Lailah",
            "Damian",
        ]
        cls.heroes = []
        for key in keys:
            hero = cls.rs.parse_hero_block(blocks[key])
            cls.rs.analyze_hero(hero)
            cls.heroes.append(hero)
        cls.by_title = {h.title: h for h in cls.heroes}
        display = {h.title: cls.gen.short_name(h.title) for h in cls.heroes}
        text = (ROOT / "Heroes.md").read_text(encoding="utf-8")
        perseus = cls.rs.parse_hero_block(blocks["Perseus"])
        cls.rs.analyze_hero(perseus)
        cls.perseus = perseus
        tasi = cls.rs.parse_hero_block(blocks["Tasi"])
        cls.rs.analyze_hero(tasi)
        cls.tasi = tasi
        cls.heroes.extend([perseus, tasi])
        display[perseus.title] = "Perseus"
        display[tasi.title] = "Tasi"
        cls.behavior = cls.rs.build_behavior_for_heroes(
            cls.heroes, display, heroes_text=text
        )
        cls.shakir = cls.by_title["Shakir - Furious Howl"]
        cls.hepler = cls.by_title["Hepler - Master of Forms"]

    def _score(self, provider_title: str, receiver_title: str) -> float:
        provider = self.by_title[provider_title]
        receiver = self.by_title[receiver_title]
        behavior = self.behavior[receiver.title]
        score, _ = self.gen.score_synergy(
            provider,
            receiver,
            behavior.movement,
            behavior.synergy_signature_speed or "average",
            behavior,
        )
        return score

    def test_shakir_excludes_ranged_backline(self) -> None:
        for recv in (
            "Hugin - Maverick Smith",
            "Bonnie - Obsidian Claws",
            "Frieren - The Legendary Mage",
            "Shemira - Corpsemaker",
            "Marilee - Forest's Arrow",
        ):
            with self.subTest(receiver=recv):
                self.assertEqual(
                    self._score("Shakir - Furious Howl", recv),
                    0.0,
                    msg=f"expected no Shakir synergy for {recv}",
                )

    def test_shakir_includes_melee_haste_users(self) -> None:
        for recv in (
            "Hepler - Master of Forms",
            "Baelran - Dawnblade",
        ):
            with self.subTest(receiver=recv):
                self.assertGreater(
                    self._score("Shakir - Furious Howl", recv),
                    0.0,
                    msg=f"expected Shakir synergy for {recv}",
                )

    def test_global_providers_still_match_hugin(self) -> None:
        for prov in (
            "Elijah & Lailah - Celestial Twins",
            "Damian - Woody Wonder",
        ):
            with self.subTest(provider=prov):
                self.assertGreater(
                    self._score(prov, "Hugin - Maverick Smith"),
                    0.0,
                )

    def test_receiver_can_reach_helper(self) -> None:
        self.assertFalse(
            self.gen.receiver_can_reach_proximity_aura(None, 2.0)
        )
        self.assertFalse(
            self.gen.receiver_can_reach_proximity_aura(7.0, 2.0)
        )
        self.assertTrue(
            self.gen.receiver_can_reach_proximity_aura(1.0, 2.0)
        )

    def test_perseus_excludes_long_range_tasi(self) -> None:
        behavior = self.behavior[self.tasi.title]
        score, _ = self.gen.score_synergy(
            self.perseus,
            self.tasi,
            behavior.movement,
            behavior.synergy_signature_speed or "average",
            behavior,
        )
        self.assertEqual(score, 0.0)

    def test_perseus_includes_melee_hepler(self) -> None:
        behavior = self.behavior[self.hepler.title]
        score, _ = self.gen.score_synergy(
            self.perseus,
            self.hepler,
            behavior.movement,
            behavior.synergy_signature_speed or "average",
            behavior,
        )
        self.assertGreater(score, 0.0)


class PositionalTileRegressionTests(unittest.TestCase):
    def test_moving_receiver_skips_positional_tile_buff(self) -> None:
        gen = _load_gen()
        rs = _load_rs()
        provider = rs.Hero(title="Prov - Test", damage_type="Physical")
        provider.effects = [
            rs.Effect(
                category="buff",
                label="ATK",
                tier="base",
                targeting="Single target",
                magnitude="high",
                qualitative="tile buff",
            )
        ]
        provider.positional_tile_buff_labels = frozenset({"ATK"})
        provider.proximity_aura_buff_labels = frozenset()
        receiver = rs.Hero(title="Recv - Test", damage_type="Physical")
        receiver.benefit_stats = ["ATK"]
        behavior = rs.HeroBehavior(
            movement="moving",
            movement_note="",
            casting_speed="average",
            avg_attack_range=1.0,
        )
        score, _ = gen.score_synergy(
            provider, receiver, "moving", "average", behavior
        )
        self.assertEqual(score, 0.0)

    def test_gunnar_scores_no_synergy_for_moving_perseus(self) -> None:
        gen = _load_gen()
        from test_roster_cache import hero_by_short_name
        import json
        from pathlib import Path

        gunnar = hero_by_short_name("Gunnar")
        perseus = hero_by_short_name("Perseus")
        proc = json.loads(
            (Path(__file__).resolve().parent.parent / "data" / "heroes_data_processed.json").read_text()
        )
        behavior = _load_rs().HeroBehavior(**proc["heroes"]["Perseus"]["behavior"])
        score, reasons = gen.score_combined_synergy(
            gunnar,
            perseus,
            gen._make_enabler_matchers({}),
            behavior,
            behavior.movement,
            behavior.synergy_signature_speed or "average",
        )
        self.assertEqual(score, 0.0)
        self.assertEqual(reasons, [])


if __name__ == "__main__":
    unittest.main()

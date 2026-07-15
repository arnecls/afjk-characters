#!/usr/bin/env python3
"""Tests for summoner-targeted synergy scoring."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent


def _load_modules():
    spec_rs = importlib.util.spec_from_file_location(
        "rewrite_summaries", SCRIPTS / "rewrite-summaries.py"
    )
    rs = importlib.util.module_from_spec(spec_rs)
    sys.modules["rewrite_summaries"] = rs
    assert spec_rs.loader is not None
    spec_rs.loader.exec_module(rs)

    spec_gen = importlib.util.spec_from_file_location(
        "gen_overview", SCRIPTS / "generate-heroes-overview.py"
    )
    gen = importlib.util.module_from_spec(spec_gen)
    sys.modules["gen_overview"] = gen
    assert spec_gen.loader is not None
    spec_gen.loader.exec_module(gen)
    return rs, gen


rs, gen = _load_modules()


def _full_roster():
    from test_roster_cache import full_roster

    return full_roster()


def _summon_effect(label: str, magnitude: str = "low") -> rs.Effect:
    return rs.Effect(
        "buff",
        label,
        "base",
        "All summons",
        0.0,
        source_section="Skill5",
        magnitude=magnitude,
    )


class SummonSynergyTests(unittest.TestCase):
    def test_peggy_lamentis_credits_def_without_receiver_benefit_stat(self):
        heroes, matchers, behavior = _full_roster()
        peggy = next(h for h in heroes if h.title.startswith("Peggy"))
        lamentis = next(h for h in heroes if h.title.startswith("Lamentis"))
        self.assertNotIn("Physical DEF", lamentis.benefit_stats)
        self.assertNotIn("Magic DEF", lamentis.benefit_stats)

        score, reasons = gen.score_summon_synergy(peggy, lamentis)
        self.assertGreater(score, 0.0)
        joined = " ".join(reasons)
        self.assertIn("DEF", joined)
        self.assertTrue(any("(all summons" in r for r in reasons))

    def test_peggy_florabelle_not_excluded_for_atk_only_summon_match(self):
        heroes, _, _ = _full_roster()
        peggy = next(h for h in heroes if h.title.startswith("Peggy"))
        florabelle = next(h for h in heroes if h.title.startswith("Florabelle"))

        score, reasons = gen.score_summon_synergy(peggy, florabelle)
        self.assertGreater(score, 0.0)
        self.assertTrue(any(r.startswith("ATK via ") for r in reasons))
        self.assertFalse(gen.should_exclude_synergy(reasons, florabelle))

    def test_ranged_damage_gated_by_summon_profile(self):
        heroes, _, _ = _full_roster()
        peggy = next(h for h in heroes if h.title.startswith("Peggy"))
        florabelle = next(h for h in heroes if h.title.startswith("Florabelle"))
        cecia = next(h for h in heroes if h.title.startswith("Cecia"))

        flor_score, flor_reasons = gen.score_summon_synergy(peggy, florabelle)
        cecia_score, cecia_reasons = gen.score_summon_synergy(peggy, cecia)
        self.assertIn("Ranged damage", " ".join(flor_reasons))
        self.assertNotIn("Ranged damage", " ".join(cecia_reasons))
        self.assertGreater(flor_score, cecia_score)

    def test_untagged_summon_hero_scores_zero(self):
        import summoner_registry as sr

        provider = rs.Hero("PeggyLike - Test", "Physical")
        receiver = rs.Hero("Incidental - Test", "Physical")
        provider.summon_effects = [_summon_effect("ATK", "low")]

        original_profiles = sr._profiles
        sr._profiles = {
            name: profile
            for name, profile in sr.load_profiles().items()
            if name != "Incidental"
        }
        try:
            score, reasons = gen.score_summon_synergy(provider, receiver)
            self.assertEqual(score, 0.0)
            self.assertEqual(reasons, [])
        finally:
            sr._profiles = original_profiles

    def test_synthetic_provider_scores_all_summon_buff_labels(self):
        import summoner_registry as sr

        provider = rs.Hero("Buffer - Test", "Physical")
        receiver = rs.Hero("Summoner - Test", "Physical")
        provider.summon_effects = [
            _summon_effect("ATK", "low"),
            _summon_effect("DEF", "average"),
            _summon_effect("Haste", "high"),
            _summon_effect("Ranged damage", "low"),
        ]

        original_profiles = sr._profiles
        sr._profiles = {
            **sr.load_profiles(),
            "Summoner": {
                "has_ranged_summons": False,
                "sources": [{"section": "Ultimate", "tier": "base"}],
            },
        }
        try:
            score, reasons = gen.score_summon_synergy(provider, receiver)
            joined = " ".join(reasons)
            self.assertIn("ATK", joined)
            self.assertIn("DEF", joined)
            self.assertIn("Haste", joined)
            self.assertNotIn("Ranged damage", joined)
            self.assertGreater(score, 0.0)
        finally:
            sr._profiles = original_profiles

    def test_marcille_no_longer_receives_summon_buffs(self):
        heroes, _, _ = _full_roster()
        peggy = next(h for h in heroes if h.title.startswith("Peggy"))
        marcille = next(h for h in heroes if h.title.startswith("Marcille"))

        score, reasons = gen.score_summon_synergy(peggy, marcille)
        self.assertEqual(score, 0.0)
        self.assertEqual(reasons, [])

    def test_lucy_receives_summon_buffs(self):
        heroes, _, _ = _full_roster()
        peggy = next(h for h in heroes if h.title.startswith("Peggy"))
        lucy = next(h for h in heroes if h.title.startswith("Lucy"))

        score, reasons = gen.score_summon_synergy(peggy, lucy)
        self.assertGreater(score, 0.0)
        self.assertTrue(any("(all summons" in r for r in reasons))


if __name__ == "__main__":
    unittest.main()

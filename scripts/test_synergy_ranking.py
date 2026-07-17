#!/usr/bin/env python3
"""Tests for synergy ranking with Prydwen tier preference."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))


def _load_gen():
    spec = importlib.util.spec_from_file_location(
        "gen_overview", SCRIPTS / "generate-heroes-overview.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["gen_overview"] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


gen = _load_gen()


def _hero(title: str) -> SimpleNamespace:
    return SimpleNamespace(title=title, effects=[])


def _shield_receiver(text: str) -> SimpleNamespace:
    return SimpleNamespace(
        title="Tank - Hero",
        benefit_stats=["Shield"],
        skill_chunks=[("base", text, "Skill")],
        effects=[],
        summon_effects=[],
        positional_tile_buff_labels=frozenset(),
        proximity_aura_buff_labels=frozenset(),
        proximity_aura_radius=None,
    )


def _shield_provider() -> SimpleNamespace:
    return SimpleNamespace(
        title="Guard - Hero",
        effects=[
            SimpleNamespace(
                category="buff",
                label="Shield",
                targeting="Multiple targets",
                magnitude="high",
                conditional=None,
            )
        ],
        summon_effects=[],
        positional_tile_buff_labels=frozenset(),
        proximity_aura_buff_labels=frozenset(),
        proximity_aura_radius=None,
    )


class ShieldMaxHpSynergyTests(unittest.TestCase):
    def test_shield_does_not_score_for_max_hp_only_receiver(self) -> None:
        rs_spec = importlib.util.spec_from_file_location(
            "rewrite_summaries",
            SCRIPTS / "rewrite-summaries.py",
        )
        rs = importlib.util.module_from_spec(rs_spec)
        sys.modules["rewrite_summaries"] = rs
        assert rs_spec.loader is not None
        rs_spec.loader.exec_module(rs)

        receiver = SimpleNamespace(
            title="Scaler - Hero",
            benefit_stats=["Max HP"],
            effects=[],
            summon_effects=[],
            positional_tile_buff_labels=frozenset(),
            proximity_aura_buff_labels=frozenset(),
            proximity_aura_radius=None,
        )
        provider = _shield_provider()
        score, reasons = gen.score_synergy(provider, receiver)
        self.assertEqual(score, 0.0)
        self.assertEqual(reasons, [])

    def test_shield_does_not_score_for_self_shield_only_receiver(self) -> None:
        receiver = _shield_receiver(
            "The hero gains a shield equal to 25% of max HP for 7s."
        )
        score, reasons = gen.score_synergy(_shield_provider(), receiver)
        self.assertEqual(score, 0.0)
        self.assertEqual(reasons, [])

    def test_shield_does_not_score_for_battle_start_self_shield(self) -> None:
        receiver = _shield_receiver(
            "When a battle starts, Kruger gains a shield that blocks damage."
        )
        score, reasons = gen.score_synergy(_shield_provider(), receiver)
        self.assertEqual(score, 0.0)
        self.assertEqual(reasons, [])

    def test_shield_scores_for_when_gaining_shield_payoff(self) -> None:
        receiver = _shield_receiver(
            "When gaining a shield, Callan recovers HP equal to 15% "
            "of the shield's max value."
        )
        score, reasons = gen.score_synergy(_shield_provider(), receiver)
        self.assertGreater(score, 0.0)
        self.assertTrue(any(r.startswith("Shield via ") for r in reasons))

    def test_shield_scores_for_generic_while_shielded_payoff(self) -> None:
        receiver = _shield_receiver(
            "While shielded, he further reduces damage taken by an extra 5%."
        )
        score, reasons = gen.score_synergy(_shield_provider(), receiver)
        self.assertGreater(score, 0.0)
        self.assertTrue(any(r.startswith("Shield via ") for r in reasons))

    def test_shield_does_not_score_for_named_self_skill_shield(self) -> None:
        receiver = _shield_receiver(
            "Ulmus knocks back adjacent enemies by 1 tile when the shield "
            "granted by Verdant Barrier breaks or vanishes."
        )
        score, reasons = gen.score_synergy(_shield_provider(), receiver)
        self.assertEqual(score, 0.0)
        self.assertEqual(reasons, [])


class SynergyTierRankingTests(unittest.TestCase):
    def test_equal_or_better_avg_tier_ranks_above_worse(self) -> None:
        receiver = _hero("Receiver - Hero")
        better = _hero("Better - Provider")
        worse = _hero("Worse - Provider")
        tiers = {
            "Receiver - Hero": {
                "afk_stages": "B",
                "dream_realm": "B",
                "dream_realm_endless": "B",
                "pvp": "B",
            },
            "Better - Provider": {
                "afk_stages": "S",
                "dream_realm": "S",
                "dream_realm_endless": "S",
                "pvp": "S",
            },
            "Worse - Provider": {
                "afk_stages": "C",
                "dream_realm": "C",
                "dream_realm_endless": "C",
                "pvp": "C",
            },
        }
        ranked = [
            (0.95, ["reason"], "Worse - Provider"),
            (0.90, ["reason"], "Better - Provider"),
        ]
        ranked.sort(
            key=lambda x: (
                -gen._prydwen_tier_preference(
                    tiers.get(receiver.title, {}),
                    tiers.get(x[2], {}),
                ),
                -x[0],
                x[2],
            )
        )
        self.assertEqual(ranked[0][2], "Better - Provider")
        self.assertEqual(ranked[1][2], "Worse - Provider")

    def test_equal_avg_tier_beats_worse_despite_lower_score(self) -> None:
        tiers = {
            "Receiver - Hero": {
                "afk_stages": "A",
                "dream_realm": "A",
                "dream_realm_endless": "A",
                "pvp": "A",
            },
            "Equal - Provider": {
                "afk_stages": "A",
                "dream_realm": "A",
                "dream_realm_endless": "A",
                "pvp": "A",
            },
            "Worse - Provider": {
                "afk_stages": "B",
                "dream_realm": "B",
                "dream_realm_endless": "B",
                "pvp": "B",
            },
        }
        receiver_tiers = tiers["Receiver - Hero"]
        ranked = [
            (0.95, ["reason"], "Worse - Provider"),
            (0.80, ["reason"], "Equal - Provider"),
        ]
        ranked.sort(
            key=lambda x: (
                -gen._prydwen_tier_preference(
                    receiver_tiers, tiers.get(x[2], {})
                ),
                -x[0],
                x[2],
            )
        )
        self.assertEqual(ranked[0][2], "Equal - Provider")
        self.assertEqual(ranked[1][2], "Worse - Provider")


class ObviousStatBufferDisplayTests(unittest.TestCase):
    def test_enabler_only_pick_not_filtered_as_obvious_buffer(self) -> None:
        counts = {"Satrana": 99, "Twins": 104}
        satrana = {
            "provider": "Satrana",
            "score": 14.5,
            "reasons": [
                "Enables Magic damage from allies via Ally grant (Sparks)"
            ],
        }
        self.assertFalse(
            gen.should_filter_obvious_stat_buffer_pick(satrana, counts, 20)
        )

    def test_stat_buff_only_pick_filtered_when_roster_wide(self) -> None:
        counts = {"Twins": 104}
        twins = {
            "provider": "Twins",
            "score": 11.0,
            "reasons": ["ATK via ATK (multiple targets, average)"],
        }
        self.assertTrue(
            gen.should_filter_obvious_stat_buffer_pick(twins, counts, 20)
        )

    def test_hybrid_pick_kept_when_it_also_enables(self) -> None:
        counts = {"Twins": 104}
        twins = {
            "provider": "Twins",
            "score": 11.0,
            "reasons": [
                "ATK via ATK (multiple targets, average)",
                "Enables Magic damage from allies via Magic damage (area)",
            ],
        }
        self.assertFalse(
            gen.should_filter_obvious_stat_buffer_pick(twins, counts, 20)
        )

    def test_display_picks_sorted_by_score_after_filter(self) -> None:
        counts = {"Twins": 104, "Satrana": 3, "Evie": 3}
        picks = [
            {
                "provider": "Evie",
                "score": 14.0,
                "reasons": [
                    "ATK via ATK (multiple targets, high)",
                    "Enables Magic damage from allies via Magic damage",
                ],
            },
            {
                "provider": "Twins",
                "score": 11.0,
                "reasons": ["ATK via ATK (multiple targets, average)"],
            },
            {
                "provider": "Satrana",
                "score": 14.5,
                "reasons": [
                    "Enables Magic damage from allies via Ally grant (Sparks)"
                ],
            },
        ]
        shown = gen.filter_synergy_picks_for_display(picks, counts, 20, 2)
        self.assertEqual(
            [p["provider"] for p in shown],
            ["Satrana", "Evie"],
        )


class SynergyStatBuffReachTests(unittest.TestCase):
    def _receiver(self) -> SimpleNamespace:
        return SimpleNamespace(
            title="Carry - Hero",
            benefit_stats=["ATK"],
            effects=[],
            summon_effects=[],
            special_effects=[],
            positional_tile_buff_labels=frozenset(),
            proximity_aura_buff_labels=frozenset(),
            proximity_aura_radius=None,
        )

    def _buff_provider(self, label: str, targeting: str) -> SimpleNamespace:
        return SimpleNamespace(
            title="Buffer - Hero",
            benefit_stats=[],
            effects=[
                SimpleNamespace(
                    category="buff",
                    label=label,
                    targeting=targeting,
                    magnitude="high",
                    conditional=None,
                )
            ],
            summon_effects=[],
            special_effects=[],
            positional_tile_buff_labels=frozenset(),
            proximity_aura_buff_labels=frozenset(),
            proximity_aura_radius=None,
        )

    def test_synergy_stat_buff_reach_is_flat_for_all_receivers(self) -> None:
        receiver = self._receiver()
        multi, _ = gen.score_synergy(
            self._buff_provider("ATK", "Multiple targets"), receiver
        )
        single, _ = gen.score_synergy(
            self._buff_provider("ATK", "Single target"), receiver
        )
        receiver_shield = SimpleNamespace(
            title="Tank - Hero",
            benefit_stats=["Shield"],
            effects=[],
            summon_effects=[],
            special_effects=[],
            positional_tile_buff_labels=frozenset(),
            proximity_aura_buff_labels=frozenset(),
            proximity_aura_radius=None,
        )
        area_shield, _ = gen.score_synergy(
            self._buff_provider("Shield", "Area"), receiver_shield
        )
        single_shield, _ = gen.score_synergy(
            self._buff_provider("Shield", "Single target"), receiver_shield
        )
        self.assertEqual(multi, single)
        self.assertEqual(area_shield, single_shield)


class SynergySelfFilterTests(unittest.TestCase):
    def test_hero_not_listed_as_own_synergy_partner(self) -> None:
        from test_roster_cache import full_roster

        heroes, matchers, behavior = full_roster()
        lyca = next(h for h in heroes if gen.short_name(h.title) == "Lyca")
        entries = gen.rank_synergy_entries(lyca, heroes, matchers, behavior)
        providers = {gen.short_name(title) for _score, _reasons, title in entries}
        self.assertNotIn("Lyca", providers)
        score, reasons = gen.score_combined_synergy(
            lyca, lyca, matchers, behavior[lyca.title]
        )
        self.assertEqual(score, 0.0)
        self.assertEqual(reasons, [])


class UltimateEnergyPreferenceTests(unittest.TestCase):
    def setUp(self) -> None:
        self._saved_tags = gen._BEHAVIOR_TAGS
        self._saved_pref = gen.HIGH_DAMAGE_ULT_ENERGY_PREF_MULT

    def tearDown(self) -> None:
        gen._BEHAVIOR_TAGS = self._saved_tags
        gen.HIGH_DAMAGE_ULT_ENERGY_PREF_MULT = self._saved_pref

    def _behavior(self, *, ult_speed: str = "slow") -> SimpleNamespace:
        return SimpleNamespace(
            movement="moving",
            movement_note="",
            casting_speed=ult_speed,
            signature_skill_name="Ultimate",
            signature_skill_is_ult=True,
            signature_skill_speed=ult_speed,
            synergy_signature_speed=ult_speed,
            synergy_signature_is_ult=True,
            ult_speed=ult_speed,
            signature_first_cast_needs_energy=False,
            non_ult_speed="average",
            avg_attack_range=2.0,
            placement_constraints=[],
            skill_overview={},
        )

    def _receiver(self, name: str) -> SimpleNamespace:
        return SimpleNamespace(
            title=f"{name} - Mage",
            benefit_stats=[],
            effects=[],
            summon_effects=[],
            special_effects=[],
            positional_tile_buff_labels=frozenset(),
            proximity_aura_buff_labels=frozenset(),
            proximity_aura_radius=None,
        )

    def _buff_provider(self, label: str) -> SimpleNamespace:
        return SimpleNamespace(
            title="Buffer - Support",
            benefit_stats=[],
            effects=[
                SimpleNamespace(
                    category="buff",
                    label=label,
                    targeting="Multiple targets",
                    magnitude="high",
                    conditional=None,
                    qualitative=f"grants allies {label.lower()}",
                )
            ],
            summon_effects=[],
            special_effects=[],
            positional_tile_buff_labels=frozenset(),
            proximity_aura_buff_labels=frozenset(),
            proximity_aura_radius=None,
        )

    def _battle_start_energy_provider(self) -> SimpleNamespace:
        return SimpleNamespace(
            title="Battery - Support",
            benefit_stats=[],
            effects=[],
            summon_effects=[],
            special_effects=[],
            positional_tile_buff_labels=frozenset(),
            proximity_aura_buff_labels=frozenset(),
            proximity_aura_radius=None,
            skill_chunks=[
                (
                    "base",
                    "When a battle starts, grants all allies 120 Energy.",
                    "Skill1",
                )
            ],
        )

    def test_receiver_prefers_ultimate_energy_for_tagged_carries(self) -> None:
        gen._BEHAVIOR_TAGS = {
            "Frieren": frozenset({"high-damage-ult"}),
            "Marcille": frozenset({"high-damage-ult"}),
            "Shemira": frozenset({"high-damage-ult"}),
            "Natsu": frozenset(
                {"high-damage-ult", "high-initial-energy"}
            ),
        }
        self.assertTrue(
            gen.receiver_prefers_ultimate_energy(self._receiver("Frieren"))
        )
        self.assertTrue(
            gen.receiver_prefers_ultimate_energy(self._receiver("Marcille"))
        )
        self.assertTrue(
            gen.receiver_prefers_ultimate_energy(self._receiver("Shemira"))
        )
        self.assertFalse(
            gen.receiver_prefers_ultimate_energy(self._receiver("Natsu"))
        )

    def test_battle_start_ult_excluded_from_ultimate_energy_preference(self) -> None:
        gen._BEHAVIOR_TAGS = {
            "Carry": frozenset({"high-damage-ult", "battle-start-ult"}),
        }
        self.assertFalse(
            gen.receiver_prefers_ultimate_energy(self._receiver("Carry"))
        )

    def test_energy_beats_haste_for_qualifying_receiver(self) -> None:
        gen._BEHAVIOR_TAGS = {"Carry": frozenset({"high-damage-ult"})}
        receiver = self._receiver("Carry")
        behavior = self._behavior(ult_speed="slow")
        haste_score, _ = gen.score_synergy(
            self._buff_provider("Haste"),
            receiver,
            signature_speed="slow",
            receiver_behavior=behavior,
        )
        energy_score, _ = gen.score_synergy(
            self._buff_provider("Energy"),
            receiver,
            signature_speed="slow",
            receiver_behavior=behavior,
        )
        self.assertGreater(energy_score, haste_score)

    def test_energy_preference_not_applied_without_tag(self) -> None:
        receiver = self._receiver("Carry")
        behavior = self._behavior(ult_speed="slow")
        gen._BEHAVIOR_TAGS = {"Carry": frozenset({"high-damage-ult"})}
        tagged_score, _ = gen.score_synergy(
            self._buff_provider("Energy"),
            receiver,
            signature_speed="slow",
            receiver_behavior=behavior,
        )
        gen._BEHAVIOR_TAGS = {}
        untagged_score, _ = gen.score_synergy(
            self._buff_provider("Energy"),
            receiver,
            signature_speed="slow",
            receiver_behavior=behavior,
        )
        self.assertGreater(tagged_score, untagged_score)

    def test_early_battle_energy_gets_ultimate_carry_boost(self) -> None:
        gen._BEHAVIOR_TAGS = {"Carry": frozenset({"high-damage-ult"})}
        receiver = self._receiver("Carry")
        behavior = self._behavior(ult_speed="slow")
        provider = self._battle_start_energy_provider()
        boosted, _ = gen.score_early_battle_energy_synergy(
            provider, receiver, behavior
        )
        gen.HIGH_DAMAGE_ULT_ENERGY_PREF_MULT = 1.0
        baseline, _ = gen.score_early_battle_energy_synergy(
            provider, receiver, behavior
        )
        self.assertGreater(boosted, baseline)
        self.assertGreater(boosted, 0.0)


class SlowFirstCastEnergyTests(unittest.TestCase):
    def _behavior(
        self,
        *,
        synergy_speed: str = "fast",
        first_cast_needs_energy: bool = True,
    ) -> SimpleNamespace:
        return SimpleNamespace(
            movement="stationary",
            movement_note="",
            casting_speed=synergy_speed,
            signature_skill_name="Ultimate",
            signature_skill_is_ult=True,
            signature_skill_speed=synergy_speed,
            synergy_signature_speed=synergy_speed,
            synergy_signature_is_ult=True,
            signature_first_cast_needs_energy=first_cast_needs_energy,
            ult_speed=synergy_speed,
            non_ult_speed="fast",
            avg_attack_range=10.0,
            placement_constraints=[],
            skill_overview={},
        )

    def _receiver(self, name: str) -> SimpleNamespace:
        return SimpleNamespace(
            title=f"{name} - Mage",
            benefit_stats=["ATK"],
            effects=[],
            summon_effects=[],
            special_effects=[],
            positional_tile_buff_labels=frozenset(),
            proximity_aura_buff_labels=frozenset(),
            proximity_aura_radius=None,
        )

    def _battle_start_energy_provider(self) -> SimpleNamespace:
        return SimpleNamespace(
            title="Battery - Support",
            benefit_stats=[],
            effects=[],
            summon_effects=[],
            special_effects=[],
            positional_tile_buff_labels=frozenset(),
            proximity_aura_buff_labels=frozenset(),
            proximity_aura_radius=None,
            skill_chunks=[
                (
                    "base",
                    "When a battle starts, grants all allies 120 Energy.",
                    "Skill1",
                )
            ],
        )

    def test_receiver_wants_early_battle_energy_for_slow_first_cast(self) -> None:
        behavior = self._behavior(synergy_speed="fast")
        self.assertTrue(gen.receiver_wants_early_battle_energy(behavior))

    def test_receiver_skips_early_battle_energy_without_first_cast_need(
        self,
    ) -> None:
        behavior = self._behavior(
            synergy_speed="fast", first_cast_needs_energy=False
        )
        self.assertFalse(gen.receiver_wants_early_battle_energy(behavior))

    def test_early_battle_energy_scores_for_slow_first_cast_ult(self) -> None:
        receiver = self._receiver("Tasi")
        behavior = self._behavior(synergy_speed="fast")
        provider = self._battle_start_energy_provider()
        score, reasons = gen.score_early_battle_energy_synergy(
            provider, receiver, behavior
        )
        self.assertGreater(score, 0.0)
        self.assertTrue(any("Energy via" in r for r in reasons))

    def test_tasi_behavior_flags_slow_first_cast(self) -> None:
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            "rewrite_summaries", SCRIPTS / "rewrite-summaries.py"
        )
        rs = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(rs)
        text = (Path(__file__).resolve().parent.parent / "Heroes.md").read_text(
            encoding="utf-8"
        )
        blocks = {}
        for block in text.split("\n## "):
            if block.startswith("## "):
                block = block[3:]
            elif not block.startswith("Tasi"):
                continue
            if block.startswith("Tasi"):
                blocks["Tasi"] = "## " + block
                break
        hero = rs.parse_hero_block(blocks["Tasi"])
        rs.analyze_hero(hero)
        display = {hero.title: "Tasi"}
        behavior = rs.build_behavior_for_heroes(
            [hero], display, heroes_text=text
        )[hero.title]
        self.assertTrue(behavior.signature_first_cast_needs_energy)
        self.assertTrue(behavior.signature_skill_is_ult)


class ThadorEarlyEnergyTests(unittest.TestCase):
    def _provider(self, text: str) -> SimpleNamespace:
        return SimpleNamespace(
            skill_chunks=[("base", text, "Skill1")],
        )

    def _receiver_behavior(self, *, first_cast: bool = False) -> SimpleNamespace:
        return SimpleNamespace(
            signature_skill_is_ult=True,
            synergy_signature_is_ult=True,
            synergy_signature_speed="slow",
            signature_first_cast_needs_energy=first_cast,
            ult_speed="slow",
        )

    def test_lieutenant_350_beats_all_allies_120(self) -> None:
        lieutenant = self._provider(
            "Grants Thador's lieutenant 350 Energy when a battle starts."
        )
        lyca = self._provider(
            "When a battle starts, grants all allies 120 Energy."
        )
        lt_pts, _ = gen.provider_early_battle_ally_energy(lieutenant)
        lyca_pts, _ = gen.provider_early_battle_ally_energy(lyca)
        self.assertGreater(lt_pts, lyca_pts)

    def test_lieutenant_beats_lyca_for_high_damage_ult_receiver(self) -> None:
        gen._BEHAVIOR_TAGS = {"Carry": frozenset({"high-damage-ult"})}
        receiver = SimpleNamespace(title="Carry - Mage")
        behavior = self._receiver_behavior()
        lieutenant = SimpleNamespace(
            title="Thador - Tank",
            skill_chunks=[
                (
                    "ex+10",
                    "Grants Thador's lieutenant 350 Energy when a battle starts.",
                    "Ex. Skill",
                )
            ],
        )
        lyca = SimpleNamespace(
            title="Lyca - Support",
            skill_chunks=[
                (
                    "base",
                    "When a battle starts, grants all allies 120 Energy.",
                    "Skill1",
                )
            ],
        )
        thador_score, _ = gen.score_early_battle_energy_synergy(
            lieutenant, receiver, behavior
        )
        lyca_score, _ = gen.score_early_battle_energy_synergy(
            lyca, receiver, behavior
        )
        self.assertGreater(thador_score, lyca_score)

    def test_early_battle_energy_not_filtered_as_obvious_buffer(self) -> None:
        pick = {
            "provider": "Thador",
            "score": 25.0,
            "reasons": [
                "Energy via Energy recovery (350 at battle start, lieutenant) "
                "`signature fuel`"
            ],
        }
        counts = {"Thador": 50}
        self.assertFalse(
            gen.should_filter_obvious_stat_buffer_pick(pick, counts, 20)
        )
        ranked = gen.rank_synergy_picks_for_display(
            [pick], counts, threshold=20
        )
        self.assertEqual(len(ranked), 1)


class FaramorEnemyGroupingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        rs_spec = importlib.util.spec_from_file_location(
            "rewrite_summaries",
            SCRIPTS / "rewrite-summaries.py",
        )
        cls.rs = importlib.util.module_from_spec(rs_spec)
        sys.modules["rewrite_summaries"] = cls.rs
        assert rs_spec.loader is not None
        rs_spec.loader.exec_module(cls.rs)

        import heroes_io as io

        cls.heroes = {
            record["name"]: record for record in io.load_heroes_data()["heroes"]
        }

    def _analyzed(self, name: str):
        hero = self.rs.hero_from_record(self.heroes[name])
        self.rs.analyze_hero(hero)
        return hero

    def test_tagged_grouper_matches(self) -> None:
        match = gen.match_enemy_grouping(self._analyzed("Eironn"))
        self.assertIsNotNone(match)
        self.assertGreater(match[0], 0.0)
        self.assertIn("Displace", match[1])

    def test_untagged_displace_does_not_match(self) -> None:
        self.assertIsNone(gen.match_enemy_grouping(self._analyzed("Nara")))

    def test_faramor_ranks_grouper_in_display_set(self) -> None:
        faramor = self._analyzed("Faramor")
        heroes = [self._analyzed(name) for name in ("Eironn", "Isabella")]
        matchers = gen._make_enabler_matchers({})
        behavior = self.rs.build_behavior_for_heroes(
            [faramor], {faramor.title: "Faramor"}, heroes_text=""
        )[faramor.title]
        ranked = gen.rank_synergy_entries(
            faramor,
            heroes,
            matchers,
            {faramor.title: behavior},
        )
        providers = {title for _score, _reasons, title in ranked}
        self.assertIn("Eironn - Stormsword", providers)
        eironn_entry = next(
            entry for entry in ranked if entry[2] == "Eironn - Stormsword"
        )
        self.assertTrue(
            any("Enemy grouping" in reason for reason in eironn_entry[1])
        )
        display, _fallback = gen.display_synergy_picks_for_receiver(
            [
                {
                    "provider": gen.short_name(title),
                    "score": score,
                    "reasons": reasons,
                }
                for score, reasons, title in ranked
            ],
            {"Eironn": 30, "Isabella": 40},
            threshold=20,
            max_syn=6,
        )
        self.assertIn("Eironn", [p["provider"] for p in display])


class CommonStatBufferNamesTests(unittest.TestCase):
    def _pick(self, provider: str, score: float) -> dict:
        return {
            "provider": provider,
            "score": score,
            "reasons": ["ATK via ATK (multiple targets, high)"],
        }

    def test_returns_up_to_four_common_buffers(self) -> None:
        picks = [
            self._pick("Rowan", 30.0),
            self._pick("Lyca", 28.0),
            self._pick("Ravion", 24.0),
            self._pick("Thador", 20.0),
            self._pick("Pandora", 16.0),
        ]
        counts = {
            "Rowan": 43,
            "Lyca": 30,
            "Ravion": 95,
            "Thador": 32,
            "Pandora": 14,
        }
        names = gen.common_stat_buffer_names(picks, counts, threshold=20)
        self.assertEqual(names, ["Rowan", "Lyca", "Ravion", "Thador"])

    def test_stops_at_available_common_buffers(self) -> None:
        picks = [
            self._pick("Rowan", 30.0),
            self._pick("Pandora", 16.0),
        ]
        counts = {"Rowan": 43, "Pandora": 14}
        names = gen.common_stat_buffer_names(picks, counts, threshold=20)
        self.assertEqual(names, ["Rowan"])


class DisplaySynergyFallbackTests(unittest.TestCase):
    def _pick(self, provider: str, score: float) -> dict:
        return {
            "provider": provider,
            "score": score,
            "reasons": ["Energy via Energy (single target, high)"],
        }

    def test_fallback_to_common_buffers_when_all_filtered(self) -> None:
        picks = [
            self._pick("Rowan", 3.24),
            self._pick("Thador", 3.24),
            self._pick("Ravion", 2.16),
            self._pick("Hugin", 1.84),
        ]
        counts = {"Rowan": 37, "Thador": 28, "Ravion": 92, "Hugin": 29}
        ranked = gen.rank_synergy_picks_for_display(picks, counts, threshold=20)
        self.assertEqual(ranked, [])
        display, from_fallback = gen.display_synergy_picks_for_receiver(
            picks, counts, threshold=20, max_syn=6
        )
        self.assertTrue(from_fallback)
        self.assertEqual(
            [p["provider"] for p in display],
            ["Rowan", "Thador", "Ravion", "Hugin"],
        )

    def test_no_fallback_when_enabler_pick_remains(self) -> None:
        picks = [
            {
                "provider": "Bonnie",
                "score": 12.0,
                "reasons": ["Enables Magic damage from allies via Magic (area)"],
            },
            self._pick("Rowan", 3.0),
        ]
        counts = {"Bonnie": 50, "Rowan": 40}
        display, from_fallback = gen.display_synergy_picks_for_receiver(
            picks, counts, threshold=20, max_syn=6
        )
        self.assertFalse(from_fallback)
        self.assertEqual([p["provider"] for p in display], ["Bonnie"])


class ContinuousDamageMatcherTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        rs_spec = importlib.util.spec_from_file_location(
            "rewrite_summaries",
            SCRIPTS / "rewrite-summaries.py",
        )
        cls.rs = importlib.util.module_from_spec(rs_spec)
        sys.modules["rewrite_summaries"] = cls.rs
        assert rs_spec.loader is not None
        rs_spec.loader.exec_module(cls.rs)

        import heroes_io as io

        cls.heroes = {
            record["name"]: record for record in io.load_heroes_data()["heroes"]
        }

    def _analyzed(self, name: str):
        hero = self.rs.hero_from_record(self.heroes[name])
        self.rs.analyze_hero(hero)
        return hero

    def test_perseus_does_not_match_tick_damage(self) -> None:
        self.assertIsNone(gen.match_dot_damage(self._analyzed("Perseus")))

    def test_healer_antandra_does_not_match(self) -> None:
        self.assertIsNone(gen.match_dot_damage(self._analyzed("Antandra")))

    def test_channel_berial_does_not_match(self) -> None:
        self.assertIsNone(gen.match_dot_damage(self._analyzed("Berial")))

    def test_legitimate_dot_providers_match(self) -> None:
        for name in (
            "Daimon",
            "Ludovic",
            "Mikola",
            "Pippa",
            "Satrana",
            "Talene",
            "Viperian",
            "Contess",
        ):
            with self.subTest(hero=name):
                match = gen.match_dot_damage(self._analyzed(name))
                self.assertIsNotNone(match, msg=f"{name} should match")
                self.assertNotIn("tick damage", match[1].lower())

    def test_targeting_weights_produce_distinct_scores(self) -> None:
        single = self.rs.Effect(
            category="damage",
            label="DoT",
            tier="base",
            targeting="Single target",
            tick=1.0,
            duration=5.0,
        )
        area = self.rs.Effect(
            category="damage",
            label="DoT",
            tier="base",
            targeting="Area",
            tick=1.0,
            duration=5.0,
        )
        all_units = self.rs.Effect(
            category="damage",
            label="DoT",
            tier="base",
            targeting="All units",
            tick=1.0,
            duration=5.0,
        )

        def score_for(effect: object) -> float:
            provider = SimpleNamespace(
                title="Provider - Hero",
                effects=[effect],
                special_effects=[],
                damage_entries=[],
            )
            match = gen.match_dot_damage(provider)
            assert match is not None
            return match[0]

        single_score = score_for(single)
        area_score = score_for(area)
        all_units_score = score_for(all_units)
        self.assertGreater(area_score, single_score)
        self.assertGreater(all_units_score, area_score)
        self.assertAlmostEqual(single_score, 1.5 * 2.5)
        self.assertAlmostEqual(area_score, 4.0 * 2.5)
        self.assertAlmostEqual(all_units_score, 5.0 * 2.5)


if __name__ == "__main__":
    unittest.main()

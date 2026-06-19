#!/usr/bin/env python3
"""Regression tests for hero summary parsing (rewrite-summaries.py)."""

from __future__ import annotations

import importlib.util
import re
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent


def _load_rs():
    spec = importlib.util.spec_from_file_location(
        "rewrite_summaries", SCRIPTS / "rewrite-summaries.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["rewrite_summaries"] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


rs = _load_rs()


def _hero_by_short_name(name: str):
    text = rs.HEROES_MD.read_text(encoding="utf-8")
    blocks = [b for b in re.split(r"\n(?=## )", text) if b.startswith("## ")]
    for block in blocks:
        if block.startswith(f"## {name} "):
            hero = rs.parse_hero_block(block)
            rs.analyze_hero(hero)
            return hero
    raise KeyError(name)


from healing_types import (
    DIRECT_HEALING_LABEL,
    HEALING_OVER_TIME_LABEL,
    is_hp_recovery_label,
)


def _hero_with_magnitudes(name: str):
    text = rs.HEROES_MD.read_text(encoding="utf-8")
    blocks = [b for b in re.split(r"\n(?=## )", text) if b.startswith("## ")]
    skills_by_title = rs.load_skills_by_title_from_blocks(blocks)
    for block in blocks:
        if block.startswith(f"## {name} "):
            hero = rs.parse_hero_block(block)
            rs.analyze_hero(hero)
            rs.assign_magnitudes([hero], skills_by_title)
            return hero
    raise KeyError(name)


def _effects(hero, category: str, label: str | None = None):
    for e in hero.effects:
        if e.category != category:
            continue
        if label is not None and e.label != label:
            continue
        yield e


def _throughput_test_hero(
    title: str,
    cooldown: float,
    pct: float,
    label: str,
    category: str,
):
    if category == "buff":
        text = f"Increases ATK of all allies by {pct:.0f}% for 8s."
        targeting = "All units"
    else:
        text = f"Reduces targets' ATK by {pct:.0f}% for 6s."
        targeting = "Multiple targets"
    section = "Skill1"
    hero = rs.Hero(title, "Physical")
    hero.skill_chunks = [("base", text, section)]
    hero.effects = [
        rs.Effect(
            category,
            label,
            "base",
            targeting,
            pct,
            source_section=section,
        )
    ]
    skill = rs.SkillMeta(
        section, None, False, cooldown, 0.0, None, None, text
    )
    return hero, [skill]


def _assign_magnitudes_for_heroes(heroes, skills_by_title):
    rs.assign_magnitudes(heroes, skills_by_title)
    return heroes


class SummaryParsingTests(unittest.TestCase):
    def test_nazrik_prey_debuffs(self):
        hero = _hero_by_short_name("Nazrik")
        labels = {e.label for e in _effects(hero, "debuff")}
        self.assertIn("Vitality debuff", labels)
        self.assertIn("Damage taken debuff", labels)
        self.assertIn("Healing debuff", labels)
        for e in _effects(hero, "debuff"):
            if e.label in (
                "Vitality debuff",
                "Damage taken debuff",
                "Healing debuff",
            ):
                self.assertNotEqual(e.targeting, "Self", e.label)

    def test_kruger_knock_down_no_ally_lifedrain(self):
        hero = _hero_by_short_name("Kruger")
        cc = {e.label for e in _effects(hero, "cc")}
        self.assertIn("Knock down", cc)
        ally_life = [
            e
            for e in _effects(hero, "buff", "Lifedrain buff")
            if e.targeting != "Self"
        ]
        self.assertEqual(ally_life, [])

    def test_harak_knock_down(self):
        hero = _hero_by_short_name("Harak")
        cc = {e.label for e in _effects(hero, "cc")}
        self.assertIn("Knock down", cc)

    def test_silven_knock_down(self):
        hero = _hero_by_short_name("Silven")
        cc = {e.label for e in _effects(hero, "cc")}
        self.assertIn("Knock down", cc)

    def test_cassadee_knock_up(self):
        hero = _hero_by_short_name("Cassadee")
        cc = {e.label for e in _effects(hero, "cc")}
        self.assertIn("Knock up", cc)

    def test_nara_knock_up_and_down(self):
        hero = _hero_by_short_name("Nara")
        cc = {e.label for e in _effects(hero, "cc")}
        self.assertIn("Knock up", cc)
        self.assertIn("Knock down", cc)

    def test_zandrok_knock_up(self):
        hero = _hero_by_short_name("Zandrok")
        cc = {e.label for e in _effects(hero, "cc")}
        self.assertIn("Knock up", cc)

    def test_atalanta_no_ally_healing_buff(self):
        hero = _hero_by_short_name("Atalanta")
        ally_heal = [
            e
            for e in _effects(hero, "buff")
            if is_hp_recovery_label(e.label)
            and e.targeting != "Self"
        ]
        self.assertEqual(ally_heal, [])

    def test_antandra_guarded_ally_heal_is_self(self):
        clause = (
            "While the shield is active, the guarded ally also heals "
            "Antandra for 60% of the damage they deal."
        )
        self.assertTrue(rs._healing_targets_self(clause))
        self.assertEqual(
            rs._resolve_buff_targeting(clause, DIRECT_HEALING_LABEL), "Self"
        )
        hero = _hero_by_short_name("Antandra")
        ally_heal = [
            e
            for e in _effects(hero, "buff")
            if is_hp_recovery_label(e.label)
            and e.targeting != "Self"
        ]
        self.assertEqual(ally_heal, [])

    def test_evie_invincible_self(self):
        hero = _hero_by_short_name("Evie")
        inv = list(_effects(hero, "buff", "Invincible"))
        self.assertTrue(inv)
        self.assertEqual(inv[0].targeting, "Self")
        provides = [
            s for s in hero.special_effects if s.label == "Invincibility"
        ]
        self.assertTrue(provides)
        self.assertEqual(provides[0].targeting, "Self")

    def test_harak_tidal_assault_invincible_self(self):
        hero = _hero_by_short_name("Harak")
        skill1 = hero.skill_slices.get("Skill1")
        self.assertIsNotNone(skill1)
        inv = [e for e in skill1.effects if e.label == "Invincible"]
        self.assertTrue(inv)
        self.assertEqual(inv[0].targeting, "Self")
        ally_inv = [
            e
            for e in _effects(hero, "buff", "Invincible")
            if e.targeting != "Self"
        ]
        self.assertEqual(ally_inv, [])

    def test_aurora_starlit_slumber_invincible_self(self):
        hero = _hero_by_short_name("Aurora")
        inv = list(_effects(hero, "buff", "Invincible"))
        self.assertTrue(inv)
        self.assertEqual(inv[0].targeting, "Self")
        provides = [
            s for s in hero.special_effects if s.label == "Invincibility"
        ]
        self.assertTrue(provides)
        self.assertEqual(provides[0].targeting, "Self")

    def test_salazer_no_ally_lifedrain(self):
        hero = _hero_by_short_name("Salazer")
        ally_life = [
            e
            for e in _effects(hero, "buff", "Lifedrain buff")
            if e.targeting != "Self"
        ]
        self.assertEqual(ally_life, [])

    def test_self_lifedrain_buffs_target_self_not_allies(self):
        for name in (
            "Brutus",
            "Salazer",
            "Shakir",
            "Thoran",
            "Valka",
            "Satrana",
            "Seth",
            "Harak",
            "Igor",
            "Kruger",
            "Mehira",
            "Sylphira",
            "Zorya",
            "Walker",
        ):
            hero = _hero_by_short_name(name)
            ally_life = [
                e
                for e in _effects(hero, "buff", "Lifedrain buff")
                if e.targeting != "Self"
            ]
            self.assertEqual(ally_life, [], name)

    def test_ally_lifedrain_buffs_stay_non_self(self):
        for name in ("Daimon", "Kordan", "Koko", "Dunlingr", "Ravion"):
            hero = _hero_by_short_name(name)
            ally_life = [
                e
                for e in _effects(hero, "buff", "Lifedrain buff")
                if e.targeting == "Self"
            ]
            self.assertEqual(ally_life, [], name)

    def test_vala_mythic_haste_buff_is_self(self):
        hero = _hero_by_short_name("Vala")
        ally_haste = [
            e
            for e in _effects(hero, "buff", "Haste buff")
            if e.targeting != "Self"
        ]
        self.assertEqual(ally_haste, [])

    def test_florabelle_overgrowth_buffs_target_summons(self):
        hero = _hero_by_short_name("Florabelle")
        skill1 = hero.skill_slices.get("Skill1")
        self.assertIsNotNone(skill1)
        for label in ("Haste buff", "Lifedrain buff"):
            buffs = [e for e in skill1.summon_effects if e.label == label]
            self.assertTrue(buffs, label)
            self.assertEqual(buffs[0].targeting, rs.SUMMON_BUFF_TARGETING)

    def test_kulu_blast_mania_penetration_is_self(self):
        hero = _hero_by_short_name("Kulu")
        ex = hero.skill_slices.get("Ex. Skill")
        self.assertIsNotNone(ex)
        pen = [
            e for e in ex.effects if e.label == "DEF Penetration buff"
        ]
        self.assertTrue(pen)
        self.assertEqual(pen[0].targeting, "Self")
        self.assertEqual(pen[0].numeric, 35.0)

    def test_zanie_turret_buffs_target_summons(self):
        hero = _hero_by_short_name("Zanie")
        ultimate = hero.skill_slices.get("Ultimate")
        self.assertIsNotNone(ultimate)
        self_atk = [
            e for e in ultimate.effects if e.label == "ATK buff"
        ]
        self.assertTrue(self_atk)
        self.assertEqual(self_atk[0].targeting, "Self")
        summon_atk = [
            e for e in ultimate.summon_effects if e.label == "ATK buff"
        ]
        self.assertTrue(summon_atk)
        self.assertEqual(summon_atk[0].targeting, rs.SUMMON_BUFF_TARGETING)
        repairs = hero.skill_slices.get("Skill2")
        self.assertIsNotNone(repairs)
        ally_shields = [
            e for e in repairs.effects if e.label == "Shield"
        ]
        self.assertEqual(ally_shields, [])
        summon_shields = [
            e for e in repairs.summon_effects if e.label == "Shield"
        ]
        self.assertTrue(summon_shields)
        self.assertEqual(
            summon_shields[0].targeting, rs.SUMMON_BUFF_TARGETING
        )
        focus = hero.skill_slices.get("Unlocks at Legendary+")
        self.assertIsNotNone(focus)
        pen = next(
            e for e in focus.effects if e.label == "DEF Penetration buff"
        )
        self.assertEqual(pen.targeting, "Self")
        overload = hero.skill_slices.get("Ex. Skill")
        self.assertIsNotNone(overload)
        ally_atk = [e for e in overload.effects if e.label == "ATK buff"]
        self.assertEqual(ally_atk, [])
        summon_atk = [
            e for e in overload.summon_effects if e.label == "ATK buff"
        ]
        self.assertTrue(summon_atk)
        self.assertEqual(summon_atk[0].targeting, rs.SUMMON_BUFF_TARGETING)

    def test_aurora_summon_damage_stays_summons_only(self):
        hero = _hero_by_short_name("Aurora")
        summon_dmg = [
            e for e in hero.summon_effects if e.label == "Damage dealt buff"
        ]
        self.assertTrue(summon_dmg)
        self.assertTrue(
            all(e.targeting == rs.SUMMON_BUFF_TARGETING for e in summon_dmg)
        )

    def test_aurora_haste_stays_summons_only(self):
        hero = _hero_by_short_name("Aurora")
        haste = [e for e in hero.summon_effects if e.label == "Haste buff"]
        self.assertTrue(haste)
        self.assertTrue(
            all(e.targeting == rs.SUMMON_BUFF_TARGETING for e in haste)
        )

    def test_solise_ally_healing_targeting(self):
        hero = _hero_by_short_name("Solise")
        healing = next(e for e in _effects(hero, "buff", DIRECT_HEALING_LABEL))
        self.assertIn(
            healing.targeting, ("All units", "Multiple targets", "Single target")
        )
        skill2 = hero.skill_slices.get("Skill2")
        self.assertIsNotNone(skill2)
        favor = next(e for e in skill2.effects if e.label == DIRECT_HEALING_LABEL)
        self.assertEqual(favor.targeting, "Multiple targets")
        skill1 = hero.skill_slices.get("Skill1")
        self.assertIsNotNone(skill1)
        bulbs = [e for e in skill1.effects if e.label == HEALING_OVER_TIME_LABEL]
        self.assertTrue(bulbs)

    def test_healing_level_upgrade_keeps_ally_targeting(self):
        hero = _hero_by_short_name("Solise")
        healing = next(e for e in _effects(hero, "buff", DIRECT_HEALING_LABEL))
        self.assertNotEqual(healing.targeting, "Self")
        self.assertGreaterEqual(healing.numeric or 0, 220.0)

    def test_zandrok_ally_max_hp_from_inspire(self):
        hero = _hero_by_short_name("Zandrok")
        ally_max_hp = [
            e
            for e in _effects(hero, "buff", "Max HP buff")
            if e.targeting != "Self"
        ]
        self.assertEqual(len(ally_max_hp), 1)
        self.assertEqual(ally_max_hp[0].targeting, "Multiple targets")
        self.assertGreaterEqual(ally_max_hp[0].numeric or 0, 20.0)

    def test_shakir_haste_buff_in_summary_not_debuff(self):
        hero = _hero_by_short_name("Shakir")
        haste_debuff = [
            e for e in hero.effects if e.category == "debuff" and e.label == "Haste debuff"
        ]
        self.assertEqual(haste_debuff, [])
        haste_buff = [
            e for e in _effects(hero, "buff", "Haste buff")
            if e.targeting != "Self"
        ]
        self.assertTrue(haste_buff)
        summary = rs.format_summary(hero, "Shakir")
        self.assertIn("#### Buffs provided by Shakir", summary)
        self.assertIn("Haste buff", summary)
        self.assertNotIn("- Haste —", summary)
        self.assertIn("Vitality", summary)

    def test_zandrok_lifedrain_is_ally_buff_not_self(self):
        hero = _hero_by_short_name("Zandrok")
        self_life = [
            e
            for e in _effects(hero, "buff", "Lifedrain buff")
            if e.targeting == "Self"
        ]
        self.assertEqual(self_life, [])
        ally_life = [
            e
            for e in _effects(hero, "buff", "Lifedrain buff")
            if e.targeting != "Self"
        ]
        self.assertTrue(ally_life)
        tags = rs.format_skill_card_tags(hero, "skill1")
        self.assertIn("Lifedrain buff", tags)
        self.assertNotIn("Lifedrain buff — Self", tags)

    def test_bonnie_self_form_not_enemy_require(self):
        hero = _hero_by_short_name("Bonnie")
        form_requires = [
            s
            for s in hero.special_effects
            if s.kind == "requires" and s.label == "Form or stance active"
        ]
        self.assertEqual(form_requires, [])
        provides = {
            s.label for s in hero.special_effects if s.kind == "provides"
        }
        self.assertIn("Transformation", provides)
        self.assertIn("Invincibility", provides)

    def test_aurora_dream_sleep_not_enemy_cc(self):
        hero = _hero_by_short_name("Aurora")
        sleep_cc = list(_effects(hero, "cc", "Sleep"))
        self.assertEqual(sleep_cc, [])
        provides = {
            s.label for s in hero.special_effects if s.kind == "provides"
        }
        self.assertIn("Dream sleep (transformation)", provides)

    def test_tasi_hypnotize_still_sleep_cc(self):
        hero = _hero_by_short_name("Tasi")
        sleep_cc = list(_effects(hero, "cc", "Sleep"))
        self.assertGreater(len(sleep_cc), 0)

    def test_cyran_displacement_parsed_as_cc(self):
        hero = _hero_by_short_name("Cyran")
        displace = list(_effects(hero, "cc", "Displace"))
        self.assertGreater(len(displace), 0)

    def test_alna_damage_excludes_immunity_and_mitigation(self):
        hero = _hero_by_short_name("Alna")
        physical = next(e for e in hero.damage_entries if e[0] == "Physical")
        self.assertNotIn("Self", physical[1])
        self.assertIn("All units", physical[1])

    def test_brutus_damage_excludes_self_targeting(self):
        hero = _hero_by_short_name("Brutus")
        for dt, tgt in hero.damage_entries:
            self.assertNotIn("Self", tgt, dt)

    def test_seth_damage_excludes_self_targeting(self):
        hero = _hero_by_short_name("Seth")
        for dt, tgt in hero.damage_entries:
            self.assertNotIn("Self", tgt, dt)
        hp_loss = next(e for e in hero.damage_entries if e[0] == "HP loss")
        self.assertIn("Single target", hp_loss[1])

    def test_alsa_ex_skill_not_counted_as_self_damage(self):
        hero = _hero_by_short_name("Alsa")
        for dt, tgt in hero.damage_entries:
            self.assertNotIn("Self", tgt, dt)

    def test_no_hero_damage_entries_use_self_targeting(self):
        text = rs.HEROES_MD.read_text(encoding="utf-8")
        blocks = [b for b in re.split(r"\n(?=## )", text) if b.startswith("## ")]
        offenders: list[str] = []
        for block in blocks:
            hero = rs.parse_hero_block(block)
            rs.analyze_hero(hero)
            short = hero.title.split(" - ")[0]
            for dt, tgt in hero.damage_entries:
                if "Self" in tgt:
                    offenders.append(f"{short}: {dt} -> {tgt}")
        self.assertEqual(offenders, [])

    def test_summary_excludes_primary_damage_type_line(self):
        hero = _hero_by_short_name("Aliceth")
        summary = rs.format_summary(hero, "Aliceth")
        self.assertNotIn("Primary damage type", summary)
        self.assertIn("Physical —", summary)

    def test_behavior_header_includes_primary_damage_type(self):
        hero = _hero_by_short_name("Chippy")
        text = rs.HEROES_MD.read_text(encoding="utf-8")
        blocks = [b for b in re.split(r"\n(?=## )", text) if b.startswith("## ")]
        skills = rs.load_skills_by_title_from_blocks(blocks)
        rs.assign_magnitudes([hero], skills)
        behavior = rs.build_behavior_for_heroes(
            [hero], {hero.title: "Chippy"}
        )[hero.title]
        lines = rs.format_behavior_section("Chippy", behavior, hero=hero)
        text = "\n".join(lines)
        self.assertIn("- **Damage types**: Physical `low`", text)
        overview_idx = text.index("#### Skill overview")
        damage_idx = text.index("- **Damage types**:")
        self.assertLess(damage_idx, overview_idx)

    def test_healing_throughput_favors_faster_cadence(self):
        fast = _hero_with_magnitudes("Fay")
        slow = _hero_with_magnitudes("Hewynn")
        fast_heal = max(
            rs._MAG_ORDER.index(e.magnitude)
            for e in _effects(fast, "buff")
            if e.label == DIRECT_HEALING_LABEL and e.targeting != "Self"
        )
        slow_heal = max(
            rs._MAG_ORDER.index(e.magnitude)
            for e in _effects(slow, "buff")
            if e.label == HEALING_OVER_TIME_LABEL and e.targeting == "All units"
        )
        self.assertGreaterEqual(fast_heal, slow_heal)

    def test_buff_throughput_favors_faster_cadence(self):
        heroes = []
        skills_by_title = {}
        for i, cd in enumerate([5, 6, 7, 8, 12, 15, 18, 22]):
            title = f"BuffTest{i} - Hero"
            hero, skills = _throughput_test_hero(
                title, cd, 25, "ATK buff", "buff"
            )
            heroes.append(hero)
            skills_by_title[title] = skills
        _assign_magnitudes_for_heroes(heroes, skills_by_title)
        fast_mag = rs._MAG_ORDER.index(heroes[0].effects[0].magnitude)
        slow_mag = rs._MAG_ORDER.index(heroes[-1].effects[0].magnitude)
        self.assertGreaterEqual(fast_mag, slow_mag)

    def test_debuff_throughput_favors_faster_cadence(self):
        heroes = []
        skills_by_title = {}
        for i, cd in enumerate([5, 6, 7, 8, 12, 15, 18, 22]):
            title = f"DebuffTest{i} - Hero"
            hero, skills = _throughput_test_hero(
                title, cd, 20, "ATK debuff", "debuff"
            )
            heroes.append(hero)
            skills_by_title[title] = skills
        _assign_magnitudes_for_heroes(heroes, skills_by_title)
        fast_mag = rs._MAG_ORDER.index(heroes[0].effects[0].magnitude)
        slow_mag = rs._MAG_ORDER.index(heroes[-1].effects[0].magnitude)
        self.assertGreaterEqual(fast_mag, slow_mag)

    def test_damage_throughput_favors_faster_cadence(self):
        text_low = "Deals 180% (ATK-based) damage to all enemies."
        text_high = "Deals 420% (ATK-based) damage to all enemies."
        fast_skills = [
            rs.SkillMeta(
                "Skill1", None, False, 8.0, 0.0, None, None, text_low
            )
        ]
        slow_skills = [
            rs.SkillMeta(
                "Skill2", None, False, 25.0, 0.0, None, None, text_high
            ),
        ]
        burst_fast = rs._score_damage_chunk(
            text_low, "Physical", "All units", skills=None
        )
        burst_slow = rs._score_damage_chunk(
            text_high, "Physical", "All units", skills=None
        )
        self.assertGreater(burst_slow, burst_fast)
        tp_fast = rs._score_damage_chunk(
            text_low,
            "Physical",
            "All units",
            section="Skill1",
            skills=fast_skills,
        )
        tp_slow = rs._score_damage_chunk(
            text_high,
            "Physical",
            "All units",
            section="Skill2",
            skills=slow_skills,
        )
        self.assertGreater(tp_fast, tp_slow)

    def test_saida_energy_drain_targets_enemy(self):
        hero = _hero_by_short_name("Saida")
        drains = list(_effects(hero, "debuff", "Energy drain"))
        self.assertTrue(drains, "expected Energy drain debuff on Saida")
        for e in drains:
            self.assertNotEqual(e.targeting, "Self", e.qualitative)
        best = max((e.numeric or 0) for e in drains)
        self.assertGreaterEqual(best, 220.0)

    def test_pang_stance_energy_cost_not_enemy_drain(self):
        hero = _hero_by_short_name("Pang")
        drains = list(_effects(hero, "debuff", "Energy drain"))
        self.assertEqual(drains, [])

    def test_pang_self_buffs_not_listed_as_ally_providers(self):
        hero = _hero_by_short_name("Pang")
        ally_buffs = [
            e
            for e in hero.effects
            if e.category == "buff" and e.targeting != "Self"
        ]
        labels = {e.label for e in ally_buffs}
        self.assertIn("ATK buff", labels)
        self.assertNotIn("DEF Penetration buff", labels)
        self.assertNotIn("Shield", {e.label for e in ally_buffs if e.tier != "EX+10"})
        for e in ally_buffs:
            if e.label == "ATK buff":
                self.assertEqual(e.targeting, "Multiple targets")
                self.assertLessEqual(e.numeric or 0, 25.0)
            if e.label == "Shield":
                self.assertIn("allied hero", e.qualitative.lower())
        intro = rs.format_buffs_provided_intro(hero, "Pang")
        self.assertIsNotNone(intro)
        assert intro is not None
        self.assertNotIn("DEF Penetration", intro)
        self.assertIn("ATK buff (Mythic+)", intro)
        self.assertIn("Shield (EX+10)", intro)

    def test_sinbad_energy_recovery_efficiency_not_energy_drain(self):
        hero = _hero_by_short_name("Sinbad")
        drains = list(_effects(hero, "debuff", "Energy drain"))
        self.assertEqual(drains, [])

    def test_ulmus_cheat_death_in_provides(self):
        hero = _hero_by_short_name("Ulmus")
        provides = {
            s.label for s in hero.special_effects if s.kind == "provides"
        }
        self.assertIn("Cheat death", provides)
        self.assertNotIn("Revive ally", provides)

    def test_thoran_saida_cheat_death_not_revive_ally(self):
        for name in ("Thoran", "Saida", "Berial"):
            hero = _hero_by_short_name(name)
            provides = {
                s.label for s in hero.special_effects if s.kind == "provides"
            }
            self.assertIn("Cheat death", provides, name)
            self.assertNotIn("Revive ally", provides, name)

    def test_marcille_revive_ally_not_cheat_death(self):
        hero = _hero_by_short_name("Marcille")
        provides = {
            s.label for s in hero.special_effects if s.kind == "provides"
        }
        self.assertIn("Revive ally", provides)
        self.assertNotIn("Cheat death", provides)

    def test_bonnie_magic_damage_amplification_is_debuff_not_provide(self):
        hero = _hero_by_short_name("Bonnie")
        provides = {
            s.label for s in hero.special_effects if s.kind == "provides"
        }
        debuff_labels = {
            e.label for e in hero.effects if e.category == "debuff"
        }
        self.assertNotIn("Magic damage amplification", provides)
        self.assertIn("Magic damage amplification", debuff_labels)

    def test_bonnie_does_not_require_ally_debuffs(self):
        hero = _hero_by_short_name("Bonnie")
        require_labels = {
            s.label for s in hero.special_effects if s.kind == "requires"
        }
        self.assertIn("Magic damage from allies", require_labels)
        self.assertNotIn("Debuff on target", require_labels)
        self.assertNotIn("Debuff on target (Aging)", require_labels)

    def test_berial_damage_taken_debuff_not_magic_amplification(self):
        hero = _hero_by_short_name("Berial")
        debuff_labels = {
            e.label for e in hero.effects if e.category == "debuff"
        }
        self.assertIn("Damage taken debuff", debuff_labels)
        self.assertNotIn("Magic damage amplification", debuff_labels)

    def test_satrana_magic_damage_reduction_buff(self):
        hero = _hero_by_short_name("Satrana")
        buff_labels = {e.label for e in hero.effects if e.category == "buff"}
        self.assertIn("Magic damage reduction", buff_labels)

    def test_kazim_requires_knock_up_from_allies(self):
        hero = _hero_by_short_name("Kazim")
        knock_requires = [
            s
            for s in hero.special_effects
            if s.kind == "requires" and s.label == "Knock up from allies"
        ]
        self.assertEqual(len(knock_requires), 1)
        self.assertEqual(knock_requires[0].targeting, "Enemies")

    def test_dionel_requires_ally_stat_buffs(self):
        hero = _hero_by_short_name("Dionel")
        ally_buff_requires = [
            s
            for s in hero.special_effects
            if s.kind == "requires" and s.label == "Ally stat buffs"
        ]
        self.assertEqual(len(ally_buff_requires), 1)
        self.assertIn("ATK", hero.benefit_stats)

    def test_dionel_nectar_feast_self_buffs_not_ally_providers(self):
        hero = _hero_by_short_name("Dionel")
        ally_atk = [
            e
            for e in _effects(hero, "buff", "ATK buff")
            if e.targeting != "Self"
        ]
        ally_spd = [
            e
            for e in _effects(hero, "buff", "ATK SPD buff")
            if e.targeting != "Self"
        ]
        self.assertEqual(ally_atk, [])
        self.assertEqual(ally_spd, [])
        self_atk = list(_effects(hero, "buff", "ATK buff"))
        self_spd = list(_effects(hero, "buff", "ATK SPD buff"))
        self.assertTrue(self_atk)
        self.assertTrue(self_spd)
        tags = rs.format_skill_card_tags(hero, "skill2")
        self.assertIn("ATK buff — Self", tags)
        self.assertIn("ATK SPD buff — Self", tags)
        self.assertIsNone(rs.format_buffs_provided_intro(hero, "Dionel"))
        summary = rs.format_summary(hero, "Dionel")
        self.assertNotIn("#### Buffs provided by Dionel", summary)

    def test_ulmus_displacement_not_knock_up_require(self):
        hero = _hero_by_short_name("Ulmus")
        knock_requires = [
            s
            for s in hero.special_effects
            if s.kind == "requires" and s.label == "Knock up from allies"
        ]
        self.assertEqual(knock_requires, [])


class HeroEffectAggregateTests(unittest.TestCase):
    """Roster-wide hero.effects must not inflate buff numerics across skills."""

    def _max_slice_numeric(self, hero, label: str) -> float:
        vals = [
            e.numeric
            for sl in hero.skill_slices.values()
            for e in sl.effects
            if e.category == "buff" and e.label == label and e.numeric is not None
        ]
        return max(vals) if vals else 0.0

    def test_roster_atk_buff_matches_per_skill_slices(self):
        for short in ("Aliceth", "Gunnar", "Hugin"):
            hero = _hero_by_short_name(short)
            slice_max = self._max_slice_numeric(hero, "ATK buff")
            live_vals = [
                e.numeric
                for e in hero.effects
                if e.category == "buff" and e.label == "ATK buff" and e.numeric
            ]
            self.assertTrue(live_vals, short)
            self.assertEqual(max(live_vals), slice_max, short)

    def test_aliceth_atk_buff_not_inflated_by_execute_threshold(self):
        hero = _hero_with_magnitudes("Aliceth")
        atk = [e for e in hero.effects if e.label == "ATK buff"]
        self.assertTrue(atk)
        self.assertEqual(max(e.numeric for e in atk), 16.0)
        self.assertEqual(atk[0].magnitude, "low")


class BenefitStatTests(unittest.TestCase):
    """Benefit stats for synergy matching — healing need vs healer output."""

    def test_smokey_ally_healer_does_not_seek_healing(self):
        hero = _hero_by_short_name("Smokey")
        self.assertNotIn("Healing", hero.benefit_stats)
        self.assertIn("ATK", hero.benefit_stats)

    def test_brutus_self_life_drain_does_not_seek_life_drain(self):
        hero = _hero_by_short_name("Brutus")
        self.assertNotIn("Life Drain", hero.benefit_stats)

    def test_talene_hp_cost_seeks_healing_not_life_drain(self):
        hero = _hero_by_short_name("Talene")
        self.assertIn("Healing", hero.benefit_stats)
        self.assertNotIn("Life Drain", hero.benefit_stats)


if __name__ == "__main__":
    unittest.main()

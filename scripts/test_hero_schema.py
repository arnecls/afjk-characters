#!/usr/bin/env python3
"""Tests for hero_schema.py and schema round-trip parity."""

from __future__ import annotations

import importlib.util
import re
import subprocess
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

import hero_schema as hs
import heroes_io as io
from test_helpers import assert_tag_in, assert_tag_not_in, tag_labels


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


def _analyze_heroes_from_blocks(blocks: list[str]) -> tuple[list, dict[str, str], dict]:
    from test_roster_cache import analyze_heroes_from_blocks

    return analyze_heroes_from_blocks(blocks)


class EnumMappingTests(unittest.TestCase):
    def test_stat_round_trip(self):
        self.assertEqual(hs.to_schema_stat("ATK SPD"), "atk_spd")
        self.assertEqual(hs.to_display_stat("atk_spd"), "ATK SPD")

    def test_damage_round_trip(self):
        self.assertEqual(hs.to_schema_damage_type("HP loss"), "hp_loss")
        self.assertEqual(hs.to_display_damage_type("hp_loss"), "HP loss")
        self.assertEqual(hs.to_display_damage_type("dot"), "DoT")

    def test_tier_round_trip(self):
        self.assertEqual(hs.to_schema_tier("Legendary+"), "legendary+")
        self.assertEqual(hs.to_display_tier("legendary+"), "Legendary+")
        self.assertEqual(hs.to_display_tier("ex+10"), "EX+10")

    def test_cc_round_trip(self):
        self.assertEqual(hs.to_schema_cc("Knock up"), "knock_up")
        self.assertEqual(hs.to_display_cc("knock_up"), "Knock up")
        self.assertEqual(hs.to_schema_cc("Blind"), "blind")
        self.assertEqual(hs.to_schema_cc("Bind"), "bind")
        self.assertEqual(hs.to_schema_cc("Pin"), "bind")
        self.assertEqual(hs.to_display_cc("pin"), "Bind")
        self.assertEqual(hs.to_schema_cc("Displace"), "displace")
        self.assertEqual(hs.to_display_cc("displace"), "Displace")
        self.assertEqual(hs.to_schema_cc("Knock back"), "knock_back")
        self.assertEqual(hs.to_display_cc("knock_back"), "Knock back")
        self.assertEqual(hs.to_schema_cc("Freeze"), "bind")
        self.assertEqual(hs.to_display_cc("freeze"), "Bind")
        self.assertEqual(hs.to_schema_immunity("Untargetable"), "untargetable")
        self.assertEqual(hs.to_display_immunity("untargetable"), "Untargetable")

    def test_faction_round_trip(self):
        self.assertEqual(hs.to_schema_faction("Wilder"), "wilder")
        self.assertEqual(hs.to_display_faction("wilder"), "Wilder")


class RoundTripTests(unittest.TestCase):
    def _hero_by_title_prefix(self, prefix: str):
        data = io.load_heroes_data()
        text = io.reconstruct_heroes_md(data)
        blocks = [b for b in re.split(r"\n(?=## )", text) if b.startswith(f"## {prefix}")]
        self.assertTrue(blocks, f"hero not found: {prefix}")
        heroes, _blocks, _role = _analyze_heroes_from_blocks(blocks)
        return heroes[0], data

    def _round_trip(self, prefix: str):
        hero, data = self._hero_by_title_prefix(prefix)
        record = next(h for h in data["heroes"] if h["title"] == hero.title)
        serialized = hs.serialize_processed_hero(
            hero,
            record,
            is_energy_provider=False,
            is_melee=False,
            is_dual_range=False,
            behavior={
                "movement": "moving",
                "movement_note": "",
                "casting_speed": "average",
                "signature_skill_name": "Test",
                "signature_skill_is_ult": False,
                "signature_skill_speed": "average",
                "synergy_signature_speed": "average",
                "synergy_signature_is_ult": False,
                "ult_speed": "slow",
                "non_ult_speed": "fast",
            },
        )
        restored = hs.deserialize_hero(
            hero.title, serialized, hero.damage_type or "Physical"
        )
        rs.assign_magnitudes([restored])
        return hero, restored

    def test_aliceth_effect_labels_preserved(self):
        before, after = self._round_trip("Aliceth")
        before_keys = {(e.category, e.label) for e in before.effects}
        after_keys = {(e.category, e.label) for e in after.effects}
        self.assertEqual(before_keys, after_keys)

    def test_round_trip_summary_parity(self):
        for prefix in ("Aliceth",):
            before, after = self._round_trip(prefix)
            short = gen.short_name(before.title)
            self.assertEqual(
                rs.format_summary(before, short).strip(),
                rs.format_summary(after, short).strip(),
                prefix,
            )

    def test_aliceth_full_ascension_numerics(self):
        processed = io.load_processed()
        hero = processed["heroes"]["Aliceth"]
        sealed = hero["skills"]["Sealed Fate"]
        pen = next(
            e
            for e in sealed["effects"]
            if e.get("name") == "DEF Penetration"
        )
        self.assertEqual(pen["value"][0]["value"], 55.0)
        marked = [
            e
            for e in sealed["effects"]
            if e.get("name") == "Marked target (focus fire)"
        ]
        self.assertTrue(
            not marked or hs._numeric_from_value(marked[0].get("value")) is None
        )
        focus = hero["skills"]["Hero Focus"]
        atk = next(e for e in focus["effects"] if e.get("name") == "ATK")
        self.assertEqual(atk["value"][0]["value"], 16.0)

    def test_targeting_label_round_trip(self):
        for prefix in ("Alna", "Athalia", "Carolina", "Gerda", "Gunnar"):
            hero, _data = self._hero_by_title_prefix(prefix)
            for _section, slice_ in hero.skill_slices.items():
                for eff in slice_.effects:
                    schema_eff = hs.effect_to_schema(eff)
                    restored = hs.schema_effect_to_effect(schema_eff)
                    self.assertEqual(
                        restored.targeting,
                        eff.targeting,
                        f"{prefix} / {_section} / {eff.label}",
                    )

    def test_dionel_untargetable_immunity(self):
        hero, _data = self._hero_by_title_prefix("Dionel")
        section = rs.CATEGORY_TO_SECTION["ultimate"]
        imms = [
            (i.immunity_type, i.targeting)
            for i in hero.skill_slices[section].cc_immunities
        ]
        self.assertIn(("Untargetable", "Self"), imms)

    def test_antandra_shield_assault_unaffected_self(self):
        hero, _data = self._hero_by_title_prefix("Antandra")
        section = rs.CATEGORY_TO_SECTION["ultimate"]
        imms = [
            (i.immunity_type, i.targeting)
            for i in hero.skill_slices[section].cc_immunities
        ]
        self.assertIn(("Unaffected", "Self"), imms)

    def test_alna_shared_resolve_ally_buffs_no_spurious_max_hp_debuff(self):
        hero, _data = self._hero_by_title_prefix("Alna")
        section = rs.CATEGORY_TO_SECTION["skill1"]
        sl = hero.skill_slices[section]
        labels = {(e.category, e.label, e.targeting) for e in sl.effects}
        empower = [
            se
            for se in sl.special_effects
            if se.kind == "provides" and se.label == "Ally empower"
        ]
        self.assertTrue(empower)
        self.assertIn(("buff", "Max HP", "Single target"), labels)
        self.assertNotIn(("debuff", "Max HP", "Single target"), labels)

    def test_antandra_gale_barrier_damage_taken_ally(self):
        hero, _data = self._hero_by_title_prefix("Antandra")
        section = rs.CATEGORY_TO_SECTION["skill4"]
        dmg_taken = [
            e for e in hero.skill_slices[section].effects
            if e.label == "Damage taken"
        ]
        self.assertTrue(dmg_taken)
        self.assertEqual(dmg_taken[0].targeting, "Single target")

    def test_antandra_enhance_force_phys_def_self(self):
        hero, _data = self._hero_by_title_prefix("Antandra")
        section = rs.CATEGORY_TO_SECTION["skill5"]
        phys_def = [
            e for e in hero.skill_slices[section].effects
            if e.label == "Phys DEF"
        ]
        self.assertTrue(phys_def)
        self.assertEqual(phys_def[0].targeting, "Self")

    def test_rhys_defensive_stance_self_buffs(self):
        hero, _data = self._hero_by_title_prefix("Rhys")
        section = rs.CATEGORY_TO_SECTION["skill1"]
        sl = hero.skill_slices[section]
        crit = [e for e in sl.effects if e.label == "Crit"]
        self.assertTrue(crit)
        self.assertEqual(crit[0].targeting, "Self")
        imms = [(i.immunity_type, i.targeting) for i in sl.cc_immunities]
        self.assertIn(("Immune", "Self"), imms)

    def test_eironn_tempest_guard_dodge_self(self):
        hero, _data = self._hero_by_title_prefix("Eironn")
        section = rs.CATEGORY_TO_SECTION["skill2"]
        dodge = [
            e for e in hero.skill_slices[section].effects
            if e.label == "Dodge chance"
        ]
        self.assertTrue(dodge)
        self.assertEqual(dodge[0].targeting, "Self")

    def test_marcille_hero_focus_chant_haste_self(self):
        hero, _data = self._hero_by_title_prefix("Marcille")
        section = rs.CATEGORY_TO_SECTION["ultimate"]
        haste = [
            e
            for e in hero.skill_slices[section].effects
            if e.label == "Haste"
        ]
        self.assertTrue(haste)
        self.assertEqual(haste[0].targeting, "Self")

    def test_cassadee_hero_focus_no_spurious_tidal_strength(self):
        hero, _data = self._hero_by_title_prefix("Cassadee")
        section = rs.CATEGORY_TO_SECTION["skill3"]
        labels = {e.label for e in hero.skill_slices[section].effects}
        self.assertNotIn("Tidal Strength", labels)
        haste = [e for e in hero.skill_slices[section].effects if e.label == "Haste"]
        self.assertTrue(haste)
        self.assertTrue(all(e.targeting == "Self" for e in haste))

    def test_cassadee_running_tide_path_knockback_and_supreme_magic_def(self):
        hero, _data = self._hero_by_title_prefix("Cassadee")
        ult = hero.skill_slices["Ultimate"]
        supreme = hero.skill_slices["Unlocks at Supreme+"]
        knockback = [e for e in ult.effects if e.category == "cc"]
        self.assertTrue(knockback)
        self.assertEqual(knockback[0].targeting, "Area")
        self.assertEqual(knockback[0].area, "path")
        self.assertEqual(knockback[0].area_direction, "selected_target")
        magic_def = [
            e for e in supreme.effects if e.category == "debuff" and e.label == "Magic DEF"
        ]
        self.assertTrue(magic_def)
        self.assertEqual(magic_def[0].tier, "Supreme+")
        tags = rs.format_skill_card_tags(hero, "ultimate")
        labels = tag_labels(tags)
        self.assertIn("Magic DEF — path (Supreme+)", labels)
        self.assertIn("Knock back — path", labels)

    def test_cassadee_tidal_strength_magic_damage_blessed_ally(self):
        hero, _data = self._hero_by_title_prefix("Cassadee")
        skill2 = hero.skill_slices["Skill2"]
        damage = [
            e
            for e in skill2.effects
            if e.category == "damage" and e.label == "Magic"
        ]
        self.assertTrue(damage)
        self.assertNotIn(
            "Tidal Strength",
            {e.label for e in skill2.effects},
        )
        base = [e for e in damage if e.tier == "base"]
        self.assertTrue(base)
        self.assertEqual(base[0].targeting, "Single target")
        triggers = [
            c
            for c in base[0].conditions
            if c.get("type") == "trigger_condition"
            and c.get("trigger") == "normal_attack"
        ]
        self.assertTrue(triggers)
        bless = [
            se
            for se in hero.skill_slices["Ex. Skill"].special_effects
            if se.kind == "provides"
            and se.label == "Ally blessing"
            and se.targeting == "All units"
        ]
        self.assertTrue(bless)
        skill2_tags = rs.format_skill_card_tags(hero, "skill2")
        skill2_labels = tag_labels(skill2_tags)
        self.assertIn("Magic", skill2_labels)
        skill4_tags = rs.format_skill_card_tags(hero, "skill4")
        skill4_labels = tag_labels(skill4_tags)
        self.assertNotIn("Magic — path", skill4_labels)

    def test_cassadee_skill1_cc_targeting_with_ex10(self):
        data = io.load_heroes_data()
        record = next(r for r in data["heroes"] if r.get("name") == "Cassadee")
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        tags = rs.format_skill_card_tags(hero, "skill1")
        labels = tag_labels(tags)
        self.assertIn("Stun — Single target", labels)
        self.assertIn("Stun — Multiple targets (EX+10)", labels)
        self.assertIn("Knock up — Single target", labels)
        self.assertIn("Knock up — Multiple targets (EX+10)", labels)

    def test_skill_card_cc_tag_includes_single_target(self):
        self.assertEqual(
            rs._skill_card_tag_for_effect("Stun", "Single target", is_cc=True),
            "Stun — Single target",
        )
        self.assertEqual(
            rs._skill_card_tag_for_effect(
                "Knock back", "Single target", is_cc=True
            ),
            "Knock back — Single target",
        )

    def test_cassadee_processed_skill1_effects_preserve_targeting_variants(self):
        hero, _data = self._hero_by_title_prefix("Cassadee")
        skill1 = hero.skill_slices["Skill1"]
        effects = hs._merge_effects(skill1.effects)

        base_stun = [
            e
            for e in effects
            if e.category == "cc" and e.label == "Stun" and e.tier == "base"
        ]
        self.assertTrue(base_stun)
        self.assertEqual(base_stun[0].targeting, "Single target")

        base_knockup = [
            e
            for e in effects
            if e.category == "cc" and e.label == "Knock up" and e.tier == "base"
        ]
        self.assertTrue(base_knockup)
        self.assertEqual(base_knockup[0].targeting, "Single target")

        ex10_stun = [
            e
            for e in effects
            if e.category == "cc" and e.label == "Stun" and e.tier == "EX+10"
        ]
        self.assertTrue(ex10_stun)
        self.assertEqual(ex10_stun[0].targeting, "Multiple targets")

        ex10_knockup = [
            e
            for e in effects
            if e.category == "cc" and e.label == "Knock up" and e.tier == "EX+10"
        ]
        self.assertTrue(ex10_knockup)
        self.assertEqual(ex10_knockup[0].targeting, "Multiple targets")

    def test_cross_skill_enhancement_tags_include_ascension_tier(self):
        hero, _data = self._hero_by_title_prefix("Cassadee")
        tags = rs.format_skill_card_tags(hero, "ultimate")
        labels = tag_labels(tags)
        self.assertIn("Magic DEF — path (Supreme+)", labels)
        reinier, _ = self._hero_by_title_prefix("Reinier")
        skill4_tags = rs.format_skill_card_tags(reinier, "skill4")
        skill4_labels = tag_labels(skill4_tags)
        self.assertIn("Damage taken (EX+10)", skill4_labels)

    def test_zandrok_rallying_roar_wedge_path_damage(self):
        hero, _data = self._hero_by_title_prefix("Zandrok")
        skill1 = hero.skill_slices["Skill1"]
        path_damage = [
            e
            for e in skill1.effects
            if e.category == "damage" and e.area == "path"
        ]
        self.assertEqual(len(path_damage), 1)
        self.assertEqual(path_damage[0].label, "Physical")
        self.assertEqual(path_damage[0].area_count, 5)
        self.assertEqual(path_damage[0].area_direction, "front")
        active_area = [
            e
            for e in skill1.effects
            if e.category == "buff"
            and e.label in ("Haste", "Lifedrain")
            and e.targeting == "Area"
        ]
        self.assertTrue(active_area)
        self.assertTrue(all(e.area_count == 2 for e in active_area))

    def test_zandrok_skill5_no_native_supreme_suffix(self):
        hero, _data = self._hero_by_title_prefix("Zandrok")
        tags = rs.format_skill_card_tags(hero, "skill5")
        labels = tag_labels(tags)
        stacking = [
            se
            for se in hero.skill_slices["Unlocks at Supreme+"].special_effects
            if se.kind == "provides" and se.label == "Stacking"
        ]
        self.assertTrue(stacking)
        self.assertFalse(any("(Supreme+)" in label for label in labels))

    def test_ascension_cards_omit_native_tier_suffix(self):
        native_by_category = {
            "skill3": "Legendary+",
            "skill4": "Mythic+",
            "skill5": "Supreme+",
        }
        for record in io.load_heroes_data()["heroes"]:
            hero = rs.hero_from_record(record)
            rs.analyze_hero(hero)
            for category, native in native_by_category.items():
                for tag in rs.format_skill_card_tags(hero, category):
                    self.assertNotIn(
                        f"({native})",
                        tag["label"],
                        f"{record.get('name')}/{category}: {tag['label']}",
                    )

    def test_brutus_skill1_phys_def_has_area_targeting(self):
        data = io.load_heroes_data()
        record = next(r for r in data["heroes"] if r.get("name") == "Brutus")
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        tags = rs.format_skill_card_tags(hero, "skill1")
        labels = tag_labels(tags)
        self.assertIn("Phys DEF — Area", labels)
        self.assertIn("Taunt — Area", labels)
        phys = next(
            e
            for e in hero.skill_slices["Skill1"].effects
            if e.category == "debuff" and e.label == "Phys DEF"
        )
        self.assertEqual(phys.targeting, "Area")
        self.assertEqual(phys.area_count, 2)

    def test_lucca_skill1_disarm_and_shield(self):
        hero, _data = self._hero_by_title_prefix("Lucca")
        skill1 = hero.skill_slices["Skill1"]
        disarm = [
            e
            for e in skill1.effects
            if e.category == "cc" and e.label == "Disarm"
        ]
        self.assertEqual(len(disarm), 1)
        self.assertEqual(disarm[0].numeric, 4.0)
        self.assertEqual(disarm[0].targeting, "Single target")
        shields = [e for e in skill1.effects if e.label == "Shield"]
        self.assertEqual(len(shields), 1)
        self.assertEqual(shields[0].numeric, 340.0)
        self.assertEqual(shields[0].targeting, "Self")
        tags = rs.format_skill_card_tags(hero, "skill1")
        labels = tag_labels(tags)
        self.assertIn("Disarm — Single target", labels)
        self.assertIn("Shield — Self", labels)

    def test_canonical_chip_key_preserves_targeting_for_lifedrain_and_healing(
        self,
    ):
        lifedrain_single = rs._canonical_skill_card_chip_key(
            "Lifedrain — Single target"
        )
        lifedrain_multi = rs._canonical_skill_card_chip_key(
            "Lifedrain — Multiple targets"
        )
        healing_self = rs._canonical_skill_card_chip_key(
            "Direct healing — Self (EX+5)"
        )
        hot_area = rs._canonical_skill_card_chip_key("HoT — Area")
        self.assertEqual(lifedrain_single, "lifedrain:single target")
        self.assertEqual(lifedrain_multi, "lifedrain:multiple targets")
        self.assertEqual(healing_self, "direct healing:self:ex+5")
        self.assertEqual(hot_area, "hot:area")
        self.assertNotEqual(lifedrain_single, lifedrain_multi)

    def test_kordan_ultimate_lifedrain_shows_area_targeting(self):
        data = io.load_heroes_data()
        record = next(r for r in data["heroes"] if "Kordan" in r.get("title", ""))
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        tags = rs.format_skill_card_tags(hero, "ultimate")
        labels = tag_labels(tags)
        self.assertIn("Lifedrain — Area", labels)
        self.assertNotIn("Lifedrain — Single target", labels)

    def test_daimon_skill1_shield_is_self_not_single_target(self):
        data = io.load_heroes_data()
        record = next(r for r in data["heroes"] if r.get("title", "").startswith("Daimon"))
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        tags = rs.format_skill_card_tags(hero, "skill1")
        labels = tag_labels(tags)
        self.assertIn("Shield — Self", labels)
        self.assertNotIn("Shield — Single target", labels)

    def test_skill_card_chip_rendering_includes_targeting(self):
        script = SCRIPTS / "test_skill_card_chips.js"
        result = subprocess.run(
            ["node", str(script)],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            result.returncode,
            0,
            msg=result.stdout + result.stderr,
        )

    def test_theme_toggle_resolution(self):
        script = SCRIPTS / "test_theme.js"
        result = subprocess.run(
            ["node", str(script)],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            result.returncode,
            0,
            msg=result.stdout + result.stderr,
        )

    def test_synergy_overflow_small_count_wording(self):
        script = SCRIPTS / "test_synergy_overflow.js"
        result = subprocess.run(
            ["node", str(script)],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            result.returncode,
            0,
            msg=result.stdout + result.stderr,
        )

    def test_evie_skill1_magic_def_shows_both_targetings(self):
        data = io.load_heroes_data()
        record = next(r for r in data["heroes"] if r.get("name") == "Evie")
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        tags = rs.format_skill_card_tags(hero, "skill1")
        labels = tag_labels(tags)
        self.assertIn("Magic DEF — Single target", labels)
        self.assertIn("Magic DEF — All units", labels)
        keys = [rs._canonical_skill_card_chip_key(label) for label in labels]
        self.assertEqual(len(keys), len(set(keys)))

    def test_arden_dark_cloud_bind_is_area(self):
        data = io.load_heroes_data()
        record = next(r for r in data["heroes"] if r.get("name") == "Arden")
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        skill1 = hero.skill_slices["Skill1"]
        binds = [
            e
            for e in skill1.effects
            if e.category == "cc"
            and e.label == "Bind"
            and e.tier in ("Mythic+", "EX+10")
        ]
        self.assertEqual({e.tier for e in binds}, {"Mythic+", "EX+10"})
        self.assertTrue(all(e.targeting == "Area" for e in binds), binds)
        self.assertTrue(all(e.area_count == 2 for e in binds), binds)

    def test_aliceth_aegis_wings_invincible_targets_ally(self):
        data = io.load_heroes_data()
        record = next(r for r in data["heroes"] if r.get("name") == "Aliceth")
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        aegis = hero.skill_slices["Ex. Skill"]
        invincible = next(
            se
            for se in aegis.special_effects
            if se.kind == "provides"
            and se.label == "Invincibility"
            and se.tier == "Mythic+"
        )
        self.assertEqual(invincible.targeting, "Single target")

    def test_contess_hp_loss_vulnerability_is_debuff(self):
        data = io.load_heroes_data()
        record = next(r for r in data["heroes"] if r.get("name") == "Contess")
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        expulsion = hero.skill_slices["Ex. Skill"]
        hp_loss = next(
            e
            for e in expulsion.effects
            if e.category == "debuff" and e.label == "HP loss"
        )
        self.assertEqual(hp_loss.targeting, "Single target")
        self.assertTrue(
            any(c.get("type") == "count" for c in hp_loss.conditions),
            hp_loss.conditions,
        )
        tags = rs.format_skill_card_tags(hero, "skill4")
        self.assertIn(
            {"label": "HP loss", "polarity": "debuff"},
            tags,
        )

    def test_contess_quiet_period_energy_is_ultimate_cast_based(self):
        data = io.load_heroes_data()
        record = next(r for r in data["heroes"] if r.get("name") == "Contess")
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        quiet = hero.skill_slices["Skill2"]
        energy = next(
            e
            for e in quiet.effects
            if e.category == "debuff" and e.label == "Energy"
        )
        self.assertIn(
            {
                "type": "trigger_condition",
                "trigger": "cast",
                "skill_type": "ultimate",
            },
            energy.conditions,
        )

    def test_thoran_cheat_death_on_skill2_not_ultimate(self):
        data = io.load_heroes_data()
        record = next(r for r in data["heroes"] if r.get("name") == "Thoran")
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        ult = hero.skill_slices["Ultimate"]
        res = hero.skill_slices["Skill2"]
        ult_cheat = [
            se.label
            for se in ult.special_effects
            if se.kind == "provides" and se.label == "Cheat death"
        ]
        res_cheat = [
            se.label
            for se in res.special_effects
            if se.kind == "provides" and se.label == "Cheat death"
        ]
        self.assertEqual(ult_cheat, [])
        self.assertEqual(len(res_cheat), 1)
        ult_interrupt = [
            e for e in ult.effects if e.category == "cc" and e.label == "Interrupt"
        ]
        self.assertEqual(ult_interrupt, [])

    def test_zorya_ex_skill_owns_ally_ultimate_require(self):
        data = io.load_heroes_data()
        record = next(r for r in data["heroes"] if r.get("name") == "Zorya")
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        ult = hero.skill_slices["Ultimate"]
        ex = hero.skill_slices["Ex. Skill"]
        ult_req = [
            se.label
            for se in ult.special_effects
            if se.kind == "requires" and "Ultimate" in se.label
        ]
        ex_req = [
            se.label
            for se in ex.special_effects
            if se.kind == "requires" and "Ultimate" in se.label
        ]
        self.assertEqual(ult_req, [])
        self.assertTrue(ex_req)

    def test_nara_eerie_execution_owns_max_hp_shockwave(self):
        processed = io.load_processed()
        eerie = processed["heroes"]["Nara"]["skills"]["Eerie Execution"]
        max_hp = [
            effect
            for effect in eerie["effects"]
            if effect.get("type") == "damage"
            and effect.get("damage_type") == "max_hp"
        ]
        self.assertEqual(len(max_hp), 1)
        self.assertEqual(max_hp[0]["tier"], "mythic+")
        self.assertEqual(max_hp[0]["value"][0]["value"], 15.0)
        self.assertEqual(max_hp[0]["targeting_label"], "Area")

    def test_nara_crimson_vengeance_keeps_only_physical_true_branches(self):
        processed = io.load_processed()
        crimson = processed["heroes"]["Nara"]["skills"]["Crimson Vengeance"]
        damage_types = {
            effect["damage_type"]
            for effect in crimson["effects"]
            if effect.get("type") == "damage"
        }
        self.assertIn("physical", damage_types)
        self.assertIn("true", damage_types)
        self.assertNotIn("max_hp", damage_types)
        self.assertFalse({"true", "max_hp"} <= damage_types)

    def test_contess_supreme_rule_triggers(self):
        data = io.load_heroes_data()
        record = next(r for r in data["heroes"] if r.get("name") == "Contess")
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        supreme = hero.skill_slices["Unlocks at Supreme+"]
        stun = next(
            e
            for e in supreme.effects
            if e.category == "cc" and e.label.lower() == "stun"
        )
        silence = next(
            e
            for e in supreme.effects
            if e.category == "cc" and e.label.lower() == "silence"
        )
        self.assertIn(
            {
                "type": "trigger_condition",
                "trigger": "rule_violation",
                "rule": "be_civil",
            },
            stun.conditions,
        )
        self.assertIn(
            {
                "type": "trigger_condition",
                "trigger": "rule_violation",
                "rule": "be_quiet",
            },
            silence.conditions,
        )

    def test_natsu_ultimate_mode_branches(self):
        data = io.load_heroes_data()
        record = next(r for r in data["heroes"] if r.get("name") == "Natsu")
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        ult = hero.skill_slices["Ultimate"]
        modes = {
            tuple(
                c["mode"]
                for c in e.conditions
                if c.get("type") == "skill_mode"
            )
            for e in ult.effects
            if e.conditions
        }
        self.assertIn(("lightning_fire_dragon",), modes)
        self.assertIn(("fire_dragon_king",), modes)

    def test_vala_checkmate_mode_branches(self):
        data = io.load_heroes_data()
        record = next(r for r in data["heroes"] if r.get("name") == "Vala")
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        skill = hero.skill_slices["Skill2"]
        modes = {
            tuple(
                c["mode"]
                for c in e.conditions
                if c.get("type") == "skill_mode"
            )
            for e in skill.effects
            if e.conditions
        }
        self.assertIn(("skyblaster",), modes)
        self.assertIn(("sword",), modes)

    def test_marilee_battlefield_learning_true_damage_conversion(self):
        data = io.load_heroes_data()
        record = next(r for r in data["heroes"] if r.get("name") == "Marilee")
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        ex = hero.skill_slices["Ex. Skill"]
        true_hit = next(
            e for e in ex.effects if e.category == "damage" and e.label == "True damage"
        )
        self.assertIn(
            {
                "type": "stack_count",
                "stacks": 6,
                "stack_comparison": "at_max",
            },
            true_hit.conditions,
        )
        self.assertIn(
            {"type": "trigger_condition", "trigger": "normal_attack"},
            true_hit.conditions,
        )
        provides = [
            se for se in ex.special_effects if se.kind == "provides"
        ]
        self.assertTrue(
            any(se.label == "DoT conversion" for se in provides),
            provides,
        )

    def test_aliceth_aegis_wings_blind_cc(self):
        processed = io.load_processed()
        wings = processed["heroes"]["Aliceth"]["skills"][
            "Aegis Wings"
        ]
        cc_types = {
            e.get("cc-type")
            for e in wings["effects"]
            if e.get("type") == "crowd_control"
        }
        self.assertIn("blind", cc_types)

    def test_passive_only_skills_have_no_effects(self):
        processed = io.load_processed()
        for title, hero in processed["heroes"].items():
            for skill_name, skill in hero["skills"].items():
                if skill.get("passive_only"):
                    self.assertEqual(
                        skill.get("effects", []),
                        [],
                        f"{title} / {skill_name}",
                    )

    def test_no_schema_enum_tokens_in_overview(self):
        overview = (ROOT / "heroes-overview.md").read_text(encoding="utf-8")
        forbidden = [
            "atk_spd",
            "hp_loss",
            "knock_down",
            "legendary+",
            "buff_stat",
            "debuff_stat",
        ]
        for token in forbidden:
            self.assertNotIn(token, overview, f"raw schema token in overview: {token}")

    def test_processed_and_synergies_title_sets_match(self):
        processed = io.load_processed()
        synergies = io.load_synergies()
        self.assertEqual(
            set(processed["heroes"]),
            set(synergies["heroes"]),
        )


class SkillOverviewTests(unittest.TestCase):
    _behavior_cache: dict[str, object] | None = None

    @classmethod
    def _all_heroes_analyzed(cls):
        from test_roster_cache import analyze_heroes_from_blocks, hero_blocks

        return analyze_heroes_from_blocks(hero_blocks())

    @classmethod
    def _behavior_by_title(cls) -> dict[str, object]:
        if cls._behavior_cache is None:
            heroes, _blocks, role_category_by_title = cls._all_heroes_analyzed()
            display_by_title = {
                h.title: h.title.split(" - ", 1)[0].strip() for h in heroes
            }
            cls._behavior_cache = rs.build_behavior_for_heroes(
                heroes, display_by_title
            )
        return cls._behavior_cache

    def _hero_block(self, display_name: str) -> str:
        from test_roster_cache import block_for_short_name

        return block_for_short_name(display_name)

    def _hero_analyzed(self, display_name: str):
        """Analyze one hero block — for per-hero skill card / effect checks."""
        from test_roster_cache import hero_by_short_name

        return hero_by_short_name(display_name)

    def _hero_by_display(self, display_name: str):
        """Full roster (cached) — needed for behavior / overview peer thresholds."""
        heroes, _blocks, _role = self._all_heroes_analyzed()
        behavior_by_title = self._behavior_by_title()
        display_by_title = {
            h.title: h.title.split(" - ", 1)[0].strip() for h in heroes
        }
        for hero in heroes:
            if display_by_title[hero.title] == display_name:
                return hero, behavior_by_title[hero.title]
        self.fail(f"hero not found: {display_name}")

    def test_hugin_skill_overview_speeds(self):
        _, behavior = self._hero_by_display("Hugin")
        overview = behavior.skill_overview
        self.assertEqual(overview["signature"].speed, "fast")
        self.assertEqual(overview["ultimate"].speed, "slow")
        self.assertEqual(overview["non_ultimate"].speed, "fast")

    def test_format_behavior_includes_prydwen_tiers_line(self):
        _, behavior = self._hero_by_display("Aliceth")
        tiers = {
            "afk_stages": "B",
            "dream_realm": "B",
            "dream_realm_endless": "S+",
            "pvp": "S",
        }
        lines = rs.format_behavior_section(
            "Aliceth", behavior, prydwen_tiers=tiers
        )
        text = "\n".join(lines)
        self.assertIn("### Aliceth's behavior\n", text)
        self.assertIn(
            "`AFK Stages [B]`, `Dream Realm [B]`, "
            "`Dream Realm (Endless) [S+]`, `PVP [S]`",
            text,
        )
        sig_idx = text.index("- **Signature skill**")
        tier_idx = text.index("`AFK Stages [B]`")
        self.assertLess(tier_idx, sig_idx)

    def test_format_behavior_has_skill_overview(self):
        _, behavior = self._hero_by_display("Hugin")
        lines = rs.format_behavior_section("Hugin", behavior)
        text = "\n".join(lines)
        self.assertIn("#### Skill overview", text)
        self.assertIn("speed `fast`", text)
        self.assertNotIn("Signature skill speed:", text)
        self.assertNotIn("damage `none`", text)
        self.assertNotIn("- Ultimate:", text)
        self.assertIn("- **Signature skill**:", text)
        self.assertIn("- **Ultimate**:", text)
        self.assertIn("- **Ally composition**:", text)
        self.assertIn("- **Self placement**:", text)

    def test_non_ult_signature_keeps_ultimate_row(self):
        _, behavior = self._hero_by_display("Daimon")
        text = "\n".join(rs.format_behavior_section("Daimon", behavior))
        self.assertIn("- **Ultimate**:", text)

    def test_ravion_damage_types_line_in_behavior_header(self):
        hero, behavior = self._hero_by_display("Ravion")
        text = "\n".join(
            rs.format_behavior_section("Ravion", behavior, hero=hero)
        )
        self.assertIn("- **Damage types**:", text)
        self.assertIn("HP loss", text)
        overview_idx = text.index("#### Skill overview")
        damage_idx = text.index("- **Damage types**:")
        self.assertLess(damage_idx, overview_idx)
        self.assertTrue(behavior.skill_overview["signature"].damage_types)

    def test_play_overview_before_skill_overview(self):
        hero, behavior = self._hero_by_display("Aliceth")
        overview = "First sentence. Second sentence. Third sentence. "
        overview += "Fourth sentence. Fifth sentence."
        text = "\n".join(
            rs.format_behavior_section(
                "Aliceth",
                behavior,
                hero=hero,
                play_overview=overview,
            )
        )
        play_idx = text.index("#### Play overview")
        overview_idx = text.index("#### Skill overview")
        self.assertLess(play_idx, overview_idx)
        self.assertIn(overview, text)

    def test_play_overview_omitted_when_blank(self):
        _, behavior = self._hero_by_display("Aliceth")
        text = "\n".join(
            rs.format_behavior_section(
                "Aliceth",
                behavior,
                play_overview="",
            )
        )
        self.assertNotIn("#### Play overview", text)

    def test_skill_summary_subsections_after_overview_metrics(self):
        _, behavior = self._hero_by_display("Aliceth")
        summaries = rs._load_skill_summaries().get("Aliceth", {})
        categories = set(summaries)
        lines = rs.format_behavior_section(
            "Aliceth",
            behavior,
            skill_summaries=summaries,
            hero_categories=categories,
        )
        text = "\n".join(lines)
        overview_idx = text.index("#### Skill overview")
        ultimate_idx = text.index("##### Ultimate")
        self.assertGreater(ultimate_idx, overview_idx)
        self.assertIn(summaries["ultimate"], text)
        self.assertLess(
            text.index(summaries["ultimate"]),
            text.index("##### Skill 1"),
        )

    def test_skill_summary_skips_missing_categories(self):
        _, behavior = self._hero_by_display("Chippy")
        summaries = {
            "ultimate": "call allies together for a combined powerful slam",
            "skill1": "leap at single target dealing damage",
        }
        lines = rs.format_behavior_section(
            "Chippy",
            behavior,
            skill_summaries=summaries,
            hero_categories={"ultimate", "skill1", "skill2"},
        )
        text = "\n".join(lines)
        self.assertIn("##### Ultimate", text)
        self.assertIn("##### Skill 1", text)
        self.assertNotIn("##### Skill 2", text)

    def test_mythic_plus_display_label(self):
        _, behavior = self._hero_by_display("Aliceth")
        summaries = rs._load_skill_summaries().get("Aliceth", {})
        categories = set(summaries)
        text = "\n".join(
            rs.format_behavior_section(
                "Aliceth",
                behavior,
                skill_summaries=summaries,
                hero_categories=categories,
            )
        )
        self.assertIn("##### Mythic+", text)
        self.assertNotIn("##### Ex. Skill", text)

    def test_format_skill_cards_aliceth(self):
        hero = self._hero_analyzed("Aliceth")
        summaries = rs._load_skill_summaries().get("Aliceth", {})
        categories = set(summaries)
        source_skills: list[dict] = []
        for record in io.load_heroes_data()["heroes"]:
            if record["name"] == "Aliceth":
                source_skills = record.get("skills", [])
                break
        cards = rs.format_skill_cards(
            hero,
            summaries,
            categories,
            source_skills=source_skills,
        )
        self.assertEqual(len(cards), 6)
        labels = [c["label"] for c in cards]
        self.assertIn("Mythic+", labels)
        self.assertNotIn("Ex. Skill", labels)
        ultimate = next(c for c in cards if c["category"] == "ultimate")
        self.assertEqual(ultimate["name"], "Radiant Rain")
        self.assertIn("flies into the air", ultimate["description"].lower())
        self.assertEqual(ultimate["meta"]["Skill Range"], "8 tiles")
        self.assertGreater(len(ultimate["levels"]), 0)
        self.assertIn(summaries["ultimate"], ultimate["summary"])
        ultimate_tags = " ".join(tag_labels(ultimate["tags"]))
        self.assertIn("Physical", ultimate_tags)
        self.assertIn("HP loss", ultimate_tags)
        self.assertIn("Unaffected — Self", ultimate_tags)
        self.assertNotIn("`high`", ultimate_tags)
        skill1 = next(c for c in cards if c["category"] == "skill1")
        skill1_tags = " ".join(tag_labels(skill1["tags"]))
        self.assertIn("Stun", skill1_tags)
        mythic = next(c for c in cards if c["category"] == "skill4")
        mythic_keys = [
            rs._canonical_skill_card_chip_key(t["label"])
            for t in mythic["tags"]
        ]
        self.assertEqual(len(mythic_keys), len(set(mythic_keys)))
        blind_keys = [k for k in mythic_keys if k.startswith("blind:")]
        self.assertGreaterEqual(len(blind_keys), 1)
        self.assertEqual(len(blind_keys), len(set(blind_keys)))

    def test_skill_card_chip_key_haste_debuff_distinct_from_haste_buff(self):
        label_key = rs._canonical_skill_card_chip_key("Haste")
        self.assertEqual(label_key, "haste")
        buff_dedupe = f"{label_key}:buff"
        debuff_dedupe = f"{label_key}:debuff"
        self.assertNotEqual(buff_dedupe, debuff_dedupe)

    def test_skill_card_chip_key_damage_dealt_debuff_distinct_from_damage_taken(
        self,
    ):
        debuff_key = rs._canonical_skill_card_chip_key("Damage dealt")
        taken_key = rs._canonical_skill_card_chip_key("Damage taken")
        buff_key = rs._canonical_skill_card_chip_key("Damage dealt — Self")
        self.assertEqual(debuff_key, "damage dealt")
        self.assertEqual(taken_key, "damage taken")
        self.assertEqual(buff_key, "damage dealt:self")
        self.assertNotEqual(f"{debuff_key}:debuff", taken_key)
        self.assertNotEqual(f"{buff_key}:buff", f"{debuff_key}:debuff")

    def test_skill_card_self_tag_implies_self_target(self):
        import hero_schema as hs

        hero = self._hero_analyzed("Aliceth")
        section = rs.CATEGORY_TO_SECTION["skill3"]
        tags = rs.format_skill_card_tags(hero, "skill3")
        assert_tag_in(self, "ATK — Self", tags, polarity="buff")
        for effect in hero.skill_slices[section].effects:
            if effect.label == "ATK" and effect.targeting == "Self":
                schema = hs.effect_to_schema(effect)
                self.assertEqual(schema.get("target"), "self")
                break
        else:
            self.fail("expected Self ATK buff on Aliceth Hero Focus")

    def test_skill_card_chip_key_energy_recovery_debuff_distinct(self):
        label_key = rs._canonical_skill_card_chip_key("Energy")
        self.assertEqual(label_key, "energy")
        self.assertNotEqual(f"{label_key}:buff", f"{label_key}:debuff")

    def test_skill_card_chip_key_ranged_def_buff_not_ranged_damage(self):
        key = rs._canonical_skill_card_chip_key("Ranged DEF — Self")
        self.assertEqual(key, "ranged def:self")
        self.assertNotEqual(key, "ranged")

    def test_eironn_legendary_skill_card_ranged_def_tags(self):
        hero = self._hero_analyzed("Eironn")
        tags = rs.format_skill_card_tags(hero, "skill3")
        self.assertEqual(tag_labels(tags), ["Ranged DEF — Self"])
        keys = [rs._canonical_skill_card_chip_key(t["label"]) for t in tags]
        self.assertIn("ranged def:self", keys)
        self.assertNotIn("ranged", keys)
        self.assertNotIn("def buff", keys)

    def test_perseus_skill2_skill_card_phys_and_magic_def_buffs(self):
        hero = self._hero_analyzed("Perseus")
        tags = rs.format_skill_card_tags(hero, "skill2")
        labels = tag_labels(tags)
        self.assertIn("ATK — Multiple targets", labels)
        self.assertIn("Phys DEF — Multiple targets", labels)
        self.assertIn("Magic DEF — Multiple targets", labels)
        keys = [rs._canonical_skill_card_chip_key(t["label"]) for t in tags]
        self.assertIn("atk:multiple targets", keys)
        self.assertIn("phys def:multiple targets", keys)
        self.assertIn("magic def:multiple targets", keys)
        self.assertEqual(len(keys), len(set(keys)))

    def test_contess_skill2_skill_card_energy_recovery_debuff(self):
        hero = self._hero_analyzed("Contess")
        tags = rs.format_skill_card_tags(hero, "skill2")
        assert_tag_in(self, "Energy — Multiple targets", tags, polarity="debuff")
        assert_tag_not_in(self, "Energy", tags, polarity="buff")

    def test_galahad_ultimate_skill_card_includes_haste_debuff(self):
        hero = self._hero_analyzed("Galahad")
        tags = rs.format_skill_card_tags(hero, "ultimate")
        assert_tag_in(self, "Haste — Area", tags, polarity="debuff")
        assert_tag_in(self, "Movement speed — Area", tags, polarity="debuff")
        dedupe_keys = []
        for tag in tags:
            key = rs._canonical_skill_card_chip_key(tag["label"])
            if tag.get("polarity"):
                key = f"{key}:{tag['polarity']}"
            dedupe_keys.append(key)
        self.assertEqual(len(dedupe_keys), len(set(dedupe_keys)))

    def test_kazim_skill5_self_targeted_energy_recovery_tag(self):
        hero = self._hero_analyzed("Kazim")
        tags = rs.format_skill_card_tags(hero, "skill5")
        assert_tag_in(self, "Energy — Self", tags, polarity="buff")
        assert_tag_in(self, "ATK SPD — Self", tags, polarity="buff")
        keys = [rs._canonical_skill_card_chip_key(t["label"]) for t in tags]
        self.assertIn("energy:self", keys)
        self.assertIn("atk spd:self", keys)

    def test_tasi_ultimate_cc_tags_include_targeting(self):
        hero = self._hero_analyzed("Tasi")
        tags = rs.format_skill_card_tags(hero, "ultimate")
        labels = tag_labels(tags)
        self.assertIn("Sleep — All units", labels)
        self.assertNotIn("Bind", labels)
        keys = [rs._canonical_skill_card_chip_key(t["label"]) for t in tags]
        self.assertIn("sleep:all units", keys)
        self.assertNotIn("bind", keys)
        self.assertEqual(len(keys), len(set(keys)))

    def test_tasi_skill1_cc_tag_includes_area_targeting(self):
        hero = self._hero_analyzed("Tasi")
        tags = rs.format_skill_card_tags(hero, "skill1")
        assert_tag_in(self, "Stun — Area", tags)
        self.assertEqual(
            rs._canonical_skill_card_chip_key("Stun — Area"),
            "stun:area",
        )

    def test_cc_chip_keys_dedupe_by_targeting(self):
        area_key = rs._canonical_skill_card_chip_key("Bind — Area")
        single_key = rs._canonical_skill_card_chip_key("Bind")
        self.assertEqual(area_key, "bind:area")
        self.assertEqual(single_key, "bind")
        self.assertNotEqual(area_key, single_key)

    def test_kazim_skill_cards_omit_implicit_max_hp_damage(self):
        hero = self._hero_analyzed("Kazim")
        for category in ("ultimate", "skill1", "skill2"):
            tags = rs.format_skill_card_tags(hero, category)
            tag_text = " ".join(tag_labels(tags))
            self.assertNotIn(
                "Max HP-based damage",
                tag_text,
                msg=f"{category} should not show implicit max-HP chip",
            )
        ult_tags = rs.format_skill_card_tags(hero, "ultimate")
        self.assertIn("Physical", tag_labels(ult_tags))
        mythic_tags = rs.format_skill_card_tags(hero, "skill4")
        self.assertNotIn("True damage", tag_labels(mythic_tags))
        mythic_labels = tag_labels(mythic_tags)
        self.assertTrue(
            any(label.startswith("Max HP-based damage") for label in mythic_labels),
            mythic_labels,
        )

    def test_skill_card_damage_tags_match_skill_slices(self):
        """Damage chips come from skill_slices, not a parallel text re-parse."""
        samples = ("Kazim", "Aliceth", "Galahad", "Athalia")
        for display in samples:
            hero = self._hero_analyzed(display)
            for category in rs.SKILL_CATEGORY_ORDER:
                section = rs.CATEGORY_TO_SECTION.get(category)
                if not section or section not in hero.skill_slices:
                    continue
                tags = rs.format_skill_card_tags(hero, category)
                labels = tag_labels(tags)
                damage_in_tags = [
                    label
                    for label in labels
                    if label.split(" (")[0] in rs._SKILL_CARD_DAMAGE_KEYS
                ]
                expected = rs._skill_card_damage_labels(
                    hero, hero.skill_slices[section], category
                )
                self.assertEqual(
                    damage_in_tags,
                    expected,
                    msg=f"{display}/{category}",
                )

    def test_processed_skill_card_tags_match_live_analysis(self):
        processed = io.load_processed()
        data = io.load_heroes_data()
        rs_mod = rs
        for record in data["heroes"]:
            short = record.get("name") or record["title"].split(" - ", 1)[0]
            if short not in processed["heroes"]:
                continue
            hero = rs_mod.hero_from_record(record)
            rs_mod.analyze_hero(hero)
            for skill in processed["heroes"][short].get("skills", {}).values():
                category = skill.get("category")
                stored = skill.get("skill_card_tags")
                if not category or stored is None:
                    continue
                live = rs_mod.format_skill_card_tags(hero, category)
                self.assertEqual(
                    stored,
                    live,
                    msg=f"{short}/{category}",
                )

    def test_signature_skill_body_omits_description(self):
        _, behavior = self._hero_by_display("Aliceth")
        body = rs._format_signature_skill_body("Aliceth", behavior)
        self.assertEqual(body, "Radiant Rain (ultimate)")
        self.assertNotIn("aerial", body)
        text = "\n".join(rs.format_behavior_section("Aliceth", behavior))
        self.assertIn("- **Signature skill**: Radiant Rain (ultimate)", text)
        self.assertNotIn("aerial area arrow rain", text)

    def test_signature_categories_override_and_calculated(self):
        sig = rs._load_signature_categories()
        self.assertNotIn("signature_override", sig["Aliceth"])
        self.assertEqual(sig["Aliceth"]["signature_calculated"], "ultimate")

        _, alna = self._hero_by_display("Alna")
        self.assertEqual(alna.signature_skill_name, "Shared Resolve")
        self.assertFalse(alna.signature_skill_is_ult)
        self.assertEqual(alna.signature_skill_speed, "average")
        self.assertEqual(sig["Alna"]["signature_override"], "skill1")
        self.assertEqual(sig["Alna"]["signature_calculated"], "skill2")

        _, aurora = self._hero_by_display("Aurora")
        self.assertEqual(aurora.signature_skill_name, "Starlit Slumber")
        self.assertTrue(aurora.signature_skill_is_ult)
        self.assertTrue(aurora.synergy_signature_is_ult)
        self.assertEqual(sig["Aurora"]["signature_calculated"], "skill1")

    def test_cassadee_signature_first_cast_speed(self):
        _, behavior = self._hero_by_display("Cassadee")
        sig_metrics = behavior.skill_overview["signature"]
        self.assertEqual(sig_metrics.speed, "average")
        self.assertEqual(sig_metrics.first_cast_speed, "fast")
        text = "\n".join(rs.format_behavior_section("Cassadee", behavior))
        self.assertIn("first cast speed `fast`", text)
        self.assertIn("speed `average`", text)

    def test_bryon_signature_skill(self):
        _, behavior = self._hero_by_display("Bryon")
        self.assertEqual(behavior.signature_skill_name, "Shadow Flash")
        self.assertFalse(behavior.signature_skill_is_ult)
        sig_metrics = behavior.skill_overview["signature"]
        self.assertEqual(sig_metrics.speed, "slow")
        text = "\n".join(rs.format_behavior_section("Bryon", behavior))
        self.assertIn("- **Ultimate**:", text)

    def test_niru_signature_first_cast_speed(self):
        _, behavior = self._hero_by_display("Niru")
        sig_metrics = behavior.skill_overview["signature"]
        self.assertEqual(sig_metrics.speed, "fast")
        self.assertEqual(sig_metrics.first_cast_speed, "none")
        text = "\n".join(rs.format_behavior_section("Niru", behavior))
        self.assertNotIn("first cast speed", text)

    def test_high_initial_energy_ultimate_first_cast_speed(self):
        for display in ("Kordan", "Cyran"):
            _, behavior = self._hero_by_display(display)
            overview = behavior.skill_overview
            row = (
                overview["signature"]
                if behavior.signature_skill_is_ult
                else overview["ultimate"]
            )
            self.assertEqual(
                row.first_cast_speed,
                "fast",
                msg=display,
            )

    def test_pang_high_ie_ult_speed_fast_hides_first_cast_line(self):
        """Roster-wide fast ult speed collapses redundant first-cast label."""
        _, behavior = self._hero_by_display("Pang")
        self.assertTrue(behavior.signature_skill_is_ult)
        sig_metrics = behavior.skill_overview["signature"]
        self.assertEqual(sig_metrics.speed, "fast")
        self.assertEqual(sig_metrics.first_cast_speed, "none")

    def test_aurora_ultimate_first_cast_not_fast_from_passive_setup(self):
        _, behavior = self._hero_by_display("Aurora")
        self.assertTrue(behavior.signature_skill_is_ult)
        sig_metrics = behavior.skill_overview["signature"]
        self.assertNotEqual(sig_metrics.first_cast_speed, "fast")

    def test_velara_ultimate_first_cast_not_fast_without_high_ie(self):
        _, behavior = self._hero_by_display("Velara")
        self.assertTrue(behavior.signature_skill_is_ult)
        sig_metrics = behavior.skill_overview["signature"]
        self.assertNotEqual(sig_metrics.first_cast_speed, "fast")

    def test_include_skill_summaries_false_omits_subsections(self):
        _, behavior = self._hero_by_display("Aliceth")
        summaries = rs._load_skill_summaries().get("Aliceth", {})
        categories = set(summaries)
        text = "\n".join(
            rs.format_behavior_section(
                "Aliceth",
                behavior,
                skill_summaries=summaries,
                hero_categories=categories,
                include_skill_summaries=False,
            )
        )
        self.assertIn("#### Skill overview", text)
        self.assertNotIn("##### Ultimate", text)
        self.assertNotIn(summaries["ultimate"], text)


class PlacementConstraintTests(unittest.TestCase):
    def _hero_by_title_prefix(self, prefix: str):
        data = io.load_heroes_data()
        text = io.reconstruct_heroes_md(data)
        blocks = [b for b in re.split(r"\n(?=## )", text) if b.startswith(f"## {prefix}")]
        self.assertTrue(blocks, f"hero not found: {prefix}")
        heroes, _blocks, _role = _analyze_heroes_from_blocks(blocks)
        return heroes[0], data

    def _hero_skills(self, display_name: str):
        from test_roster_cache import block_for_short_name

        return rs.load_skill_meta(block_for_short_name(display_name))

    def test_hugin_placement_constraints(self):
        constraints = rs.detect_placement_constraints(
            self._hero_skills("Hugin"), "Hugin"
        )
        kinds = {c.kind for c in constraints}
        self.assertIn("ally_placement", kinds)
        self.assertIn("self_placement", kinds)

    def test_phraesto_placement_constraints(self):
        constraints = rs.detect_placement_constraints(
            self._hero_skills("Phraesto"), "Phraesto"
        )
        kinds = {c.kind for c in constraints}
        self.assertIn("ally_placement", kinds)
        self.assertIn("self_placement", kinds)

    def test_ravion_composition_not_grid_placement(self):
        constraints = rs.detect_placement_constraints(
            self._hero_skills("Ravion"), "Ravion"
        )
        self.assertTrue(constraints)
        self.assertTrue(all(c.kind == "ally_composition" for c in constraints))
        self.assertNotIn("ally_placement", {c.kind for c in constraints})

    def test_bonnie_has_no_placement_constraints(self):
        constraints = rs.detect_placement_constraints(
            self._hero_skills("Bonnie"), "Bonnie"
        )
        self.assertEqual(constraints, [])

    def test_galahad_ally_composition(self):
        constraints = rs.detect_placement_constraints(
            self._hero_skills("Galahad"), "Galahad"
        )
        kinds = {c.kind for c in constraints}
        self.assertIn("ally_composition", kinds)
        texts = [c.text for c in constraints if c.kind == "ally_composition"]
        self.assertTrue(any("prioritizes ally behind" in t for t in texts), texts)

    def test_galahad_heroes2_typo_still_detected(self):
        """heroes2/fandom text misspells prioritizing as priortizing."""
        text = (
            "When a battle starts, Galahad marks the nearest allied hero, "
            "priortizing the one behind her."
        )
        constraints = rs.detect_placement_constraints(
            [rs.SkillMeta("Ex. Skill", None, False, None, None, None, None, text)],
            "Galahad",
        )
        self.assertTrue(constraints)

    def test_niru_ally_composition(self):
        constraints = rs.detect_placement_constraints(
            self._hero_skills("Niru"), "Niru"
        )
        kinds = {c.kind for c in constraints}
        self.assertIn("ally_composition", kinds)

    def test_thoran_ally_placement(self):
        constraints = rs.detect_placement_constraints(
            self._hero_skills("Thoran"), "Thoran"
        )
        kinds = {c.kind for c in constraints}
        self.assertIn("ally_placement", kinds)
        texts = [c.text for c in constraints if c.kind == "ally_placement"]
        self.assertTrue(any("Soul Pact" in t for t in texts), texts)

    def test_thoran_heroes2_on_tile_behind(self):
        text = (
            "Before a battle starts, Thoran signs a pact with the ally "
            "on the tile behind him, agreeing to take 50% of the damage "
            "for this ally until the battle ends."
        )
        constraints = rs.detect_placement_constraints(
            [rs.SkillMeta("Ex. Skill", None, False, None, None, None, None, text)],
            "Thoran",
        )
        self.assertTrue(constraints)

    def test_sonja_ally_placement(self):
        constraints = rs.detect_placement_constraints(
            self._hero_skills("Sonja"), "Sonja"
        )
        kinds = {c.kind for c in constraints}
        self.assertIn("ally_placement", kinds)
        texts = [c.text for c in constraints if c.kind == "ally_placement"]
        self.assertTrue(any("left and right" in t for t in texts), texts)

    def test_gunnar_ally_placement(self):
        constraints = rs.detect_placement_constraints(
            self._hero_skills("Gunnar"), "Gunnar"
        )
        kinds = {c.kind for c in constraints}
        self.assertIn("ally_placement", kinds)
        texts = [c.text for c in constraints if c.kind == "ally_placement"]
        self.assertTrue(any("Doomfield" in t for t in texts), texts)

    def test_aliceth_brightfeather_ally_composition(self):
        constraints = rs.detect_placement_constraints(
            self._hero_skills("Aliceth"), "Aliceth"
        )
        kinds = {c.kind for c in constraints}
        self.assertIn("ally_composition", kinds)
        texts = [c.text for c in constraints if c.kind == "ally_composition"]
        self.assertTrue(
            any("Brightfeather" in t and "row" in t for t in texts),
            texts,
        )

    def test_aliceth_hero_focus_not_debuff_require(self):
        hero, _data = self._hero_by_title_prefix("Aliceth")
        requires = [e for e in hero.special_effects if e.kind == "requires"]
        debuff_requires = [
            e
            for e in requires
            if e.label in ("Debuff on target", "Debuff on target (Aging)")
        ]
        self.assertEqual([e.label for e in debuff_requires], [], debuff_requires)

    def test_twins_stellar_bond_placement(self):
        constraints = rs.detect_placement_constraints(
            self._hero_skills("Elijah & Lailah"), "Twins"
        )
        kinds = {c.kind for c in constraints}
        self.assertIn("ally_placement", kinds)
        texts = [c.text for c in constraints if c.kind == "ally_placement"]
        self.assertTrue(any("Stellar Bond" in t for t in texts), texts)

    def test_reinier_symmetrical_placement(self):
        constraints = rs.detect_placement_constraints(
            self._hero_skills("Reinier"), "Reinier"
        )
        kinds = {c.kind for c in constraints}
        self.assertIn("ally_placement", kinds)
        texts = [c.text for c in constraints if c.kind == "ally_placement"]
        self.assertTrue(any("symmetrical" in t for t in texts), texts)

    def _hero_by_short_name(self, display_name: str):
        from test_roster_cache import block_for_short_name

        hero = rs.parse_hero_block(block_for_short_name(display_name))
        rs.analyze_hero(hero)
        return hero

    def test_satrana_sparks_ally_placement(self):
        constraints = rs.detect_placement_constraints(
            self._hero_skills("Satrana"), "Satrana"
        )
        kinds = {c.kind for c in constraints}
        self.assertIn("ally_placement", kinds)
        texts = [c.text for c in constraints if c.kind == "ally_placement"]
        self.assertTrue(
            any("within 2 tiles" in t and "Sparks" in t for t in texts),
            texts,
        )

    def test_satrana_enables_bonnie_magic_damage_via_sparks(self):
        satrana = self._hero_by_short_name("Satrana")
        match = gen.match_ally_enabled_magic_damage(satrana)
        self.assertIsNotNone(match)
        pts, detail = match
        self.assertGreater(pts, 7.25)
        self.assertIn("sparks", detail.lower())
        self.assertIn("within 2 tiles", detail)

    def test_cassadee_enables_ally_magic_damage_on_hit(self):
        cassadee = self._hero_by_short_name("Cassadee")
        match = gen.match_ally_enabled_magic_damage(cassadee)
        self.assertIsNotNone(match)
        _pts, detail = match
        self.assertIn("Ally blessing", detail)

    def test_himmel_hero_party_placement(self):
        constraints = rs.detect_placement_constraints(
            self._hero_skills("Himmel"), "Himmel"
        )
        kinds = {c.kind for c in constraints}
        self.assertIn("ally_placement", kinds)
        texts = [c.text for c in constraints if c.kind == "ally_placement"]
        self.assertTrue(any("Hero Party" in t for t in texts), texts)


@unittest.skipUnless(hs.jsonschema is not None, "jsonschema not installed")
class MovementDetectionTests(unittest.TestCase):
    def _behavior(self, display_name: str):
        from test_roster_cache import analyze_heroes_from_blocks, hero_blocks

        heroes, block_by_title, role_category_by_title = analyze_heroes_from_blocks(
            hero_blocks()
        )
        display_by_title = {
            h.title: h.title.split(" - ", 1)[0].strip() for h in heroes
        }
        hero_class_by_title = {
            h.title: gen._parse_hero_class(block_by_title[h.title]).lower()
            for h in heroes
        }
        behavior_by_title = rs.build_behavior_for_heroes(
            heroes,
            display_by_title,
            hero_class_by_title=hero_class_by_title,
        )
        for hero in heroes:
            if display_by_title[hero.title] == display_name:
                return behavior_by_title[hero.title]
        self.fail(f"hero not found: {display_name}")

    def test_natsu_is_moving(self):
        behavior = self._behavior("Natsu")
        self.assertEqual(behavior.movement, "moving")

    def test_nara_is_mostly_stationary(self):
        behavior = self._behavior("Nara")
        self.assertEqual(behavior.movement, "mostly stationary")

    def test_gunnar_stays_stationary(self):
        behavior = self._behavior("Gunnar")
        self.assertEqual(behavior.movement, "stationary")

    def test_daimon_stays_stationary(self):
        behavior = self._behavior("Daimon")
        self.assertEqual(behavior.movement, "stationary")

    def test_florabelle_stays_stationary(self):
        behavior = self._behavior("Florabelle")
        self.assertEqual(behavior.movement, "stationary")

    def test_callan_inactive_while_ultimate(self):
        behavior = self._behavior("Callan")
        self.assertIn("inactive while ultimate is running", behavior.movement_note)

    def test_zorya_inactive_while_dormant(self):
        behavior = self._behavior("Zorya")
        self.assertIn("inactive while dormant", behavior.movement_note)


class ConditionParsingTests(unittest.TestCase):
    def test_hp_threshold_below(self):
        conds = rs.parse_conditions_from_text(
            "when their HP ratio drops below 50% for the first time",
            "buff",
        )
        self.assertIn(
            {
                "type": "hp_threshold",
                "hp_ratio": 0.5,
                "comparison": "below",
            },
            conds,
        )
        self.assertIn(
            {"type": "duration_gate", "gate": "first_time"},
            conds,
        )

    def test_duration_gate_cooldown(self):
        conds = rs.parse_conditions_from_text(
            "This effect can trigger once per enemy every 2s.",
            "buff",
        )
        self.assertIn(
            {
                "type": "duration_gate",
                "gate": "once_per_enemy",
                "interval": 2.0,
            },
            conds,
        )

    def test_duration_gate_once_per_battle(self):
        conds = rs.parse_conditions_from_text(
            "This skill can be used once per battle.",
            "buff",
        )
        self.assertIn(
            {"type": "duration_gate", "gate": "once_per_battle"},
            conds,
        )

    def test_stack_count_up_to(self):
        conds = rs.parse_conditions_from_text(
            "Each enemy hit increases Phys DEF, up to 6 stacks.",
            "buff",
        )
        self.assertIn(
            {
                "type": "stack_count",
                "stacks": 6,
                "stack_comparison": "up_to",
            },
            conds,
        )

    def test_stack_count_at_max(self):
        conds = rs.parse_conditions_from_text(
            "When Aging reaches its maximum stack on an enemy",
            "debuff",
        )
        self.assertIn(
            {"type": "stack_count", "stack_comparison": "at_max"},
            conds,
        )

    def test_hp_threshold_above(self):
        conds = rs.parse_conditions_from_text(
            "while the ally's HP ratio is above 40%",
            "buff",
        )
        self.assertEqual(
            conds[0],
            {
                "type": "hp_threshold",
                "hp_ratio": 0.4,
                "comparison": "above",
            },
        )

    def test_status_controlled_enemies(self):
        conds = rs.parse_conditions_from_text(
            "strike controlled enemies below with lightning",
            "damage",
        )
        self.assertIn(
            {"type": "status_condition", "status": "controlled"},
            conds,
        )

    def test_unit_type_non_summoned(self):
        conds = rs.parse_conditions_from_text(
            "whenever a non-summoned enemy is controlled",
            "buff",
        )
        self.assertIn(
            {"type": "unit_type", "unit_type": "non_summoned"},
            conds,
        )

    def test_resolve_effect_conditions_merges_battle_phase(self):
        conds = rs._resolve_effect_conditions(
            "buff",
            "can only be used once for each guarded ally per battle",
        )
        self.assertIn(
            {"type": "battle_phase", "phase": "once_per_battle"},
            conds,
        )

    def test_effect_to_schema_serializes_structured_conditions(self):
        effect = rs.Effect(
            category="buff",
            label="Damage taken",
            tier="base",
            targeting="Self",
            conditions=[
                {
                    "type": "hp_threshold",
                    "hp_ratio": 0.5,
                    "comparison": "below",
                }
            ],
        )
        schema = hs.effect_to_schema(effect)
        self.assertEqual(
            schema["conditions"],
            [
                {
                    "type": "hp_threshold",
                    "hp_ratio": 0.5,
                    "comparison": "below",
                }
            ],
        )

    def test_arden_natures_resilience_unit_type_condition(self):
        record = next(
            r
            for r in io.load_heroes_data()["heroes"]
            if r.get("name") == "Arden"
        )
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        sl = hero.skill_slices["Skill2"]
        merged = hs._merge_effects(sl.effects)
        schema = hs.effect_to_schema(merged[0])
        types = {c.get("type") for c in schema.get("conditions") or []}
        self.assertIn("unit_type", types)


class SeasonMappingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.seasons = io.load_seasons()

    def test_starter_story_launch(self) -> None:
        name, number = hs.map_date_to_season("2024-03-27", self.seasons)
        self.assertEqual(name, "Starter Story")
        self.assertEqual(number, 0)

    def test_song_of_strife_start(self) -> None:
        name, number = hs.map_date_to_season("2024-05-10", self.seasons)
        self.assertEqual(name, "Song of Strife")
        self.assertEqual(number, 1)

    def test_galahad_release_season(self) -> None:
        name, number = hs.map_date_to_season("2025-12-18", self.seasons)
        self.assertEqual(name, "Thorns of Devotion")
        self.assertEqual(number, 5)

    def test_missing_release_date(self) -> None:
        self.assertEqual(hs.map_date_to_season(None, self.seasons), (None, None))


class SchemaValidationTests(unittest.TestCase):
    def test_processed_json_validates(self):
        processed = io.load_processed()
        hs.validate_processed(processed)

    def test_synergies_json_validates(self):
        synergies = io.load_synergies()
        hs.validate_synergies(synergies)


class ValidateScriptTests(unittest.TestCase):
    def test_validate_processed_exits_zero(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPTS / "validate_processed.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            result.returncode,
            0,
            msg=result.stderr or result.stdout,
        )


if __name__ == "__main__":
    unittest.main()

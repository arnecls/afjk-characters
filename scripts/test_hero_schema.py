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
    heroes = [rs.parse_hero_block(b) for b in blocks]
    block_by_title = {h.title: b for h, b in zip(heroes, blocks)}
    for hero in heroes:
        rs.analyze_hero(hero)
    role_category_by_title = gen._role_category_by_title(heroes, block_by_title)
    skills_by_title = rs.load_skills_by_title_from_blocks(blocks)
    rs.assign_magnitudes(heroes, skills_by_title, role_category_by_title)
    return heroes, block_by_title, role_category_by_title


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
        for prefix in ("Aliceth", "Lorsan", "Contess"):
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
            if e.get("name") == "DEF Penetration buff"
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
        atk = next(e for e in focus["effects"] if e.get("name") == "ATK buff")
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
        processed = io.load_processed()
        skill = processed["heroes"]["Dionel"]["skills"][
            "Dawn Light"
        ]
        imm_types = {
            e.get("immunity_type")
            for e in skill.get("effects", [])
            if e.get("type") == "immunity"
        }
        self.assertIn("untargetable", imm_types)

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
    _roster_cache: tuple[list, dict[str, str], dict[str, str]] | None = None
    _behavior_cache: dict[str, object] | None = None

    @classmethod
    def _all_heroes_analyzed(cls):
        if cls._roster_cache is None:
            text = (ROOT / "Heroes.md").read_text(encoding="utf-8")
            blocks = [b for b in re.split(r"\n(?=## )", text) if b.startswith("## ")]
            cls._roster_cache = _analyze_heroes_from_blocks(blocks)
        return cls._roster_cache

    @classmethod
    def _behavior_by_title(cls) -> dict[str, object]:
        if cls._behavior_cache is None:
            heroes, _blocks, role_category_by_title = cls._all_heroes_analyzed()
            display_by_title = {
                h.title: h.title.split(" - ", 1)[0].strip() for h in heroes
            }
            cls._behavior_cache = rs.build_behavior_for_heroes(
                heroes, display_by_title, role_category_by_title=role_category_by_title
            )
        return cls._behavior_cache

    def _hero_block(self, display_name: str) -> str:
        text = (ROOT / "Heroes.md").read_text(encoding="utf-8")
        blocks = [b for b in re.split(r"\n(?=## )", text) if b.startswith("## ")]
        matching = [
            b
            for b in blocks
            if b.split("\n", 1)[0].removeprefix("## ").split(" - ", 1)[0].strip()
            == display_name
        ]
        self.assertEqual(len(matching), 1, f"hero not found: {display_name}")
        return matching[0]

    def _hero_analyzed(self, display_name: str):
        """Analyze one hero block — for per-hero skill card / effect checks."""
        heroes, _, _role = _analyze_heroes_from_blocks([self._hero_block(display_name)])
        return heroes[0]

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
        ultimate_tags = " ".join(ultimate["tags"])
        self.assertIn("Physical", ultimate_tags)
        self.assertIn("HP loss", ultimate_tags)
        self.assertIn("Invincible — Self", ultimate_tags)
        self.assertNotIn("`high`", ultimate_tags)
        skill1 = next(c for c in cards if c["category"] == "skill1")
        skill1_tags = " ".join(skill1["tags"])
        self.assertIn("Stun", skill1_tags)
        mythic = next(c for c in cards if c["category"] == "skill4")
        mythic_keys = [rs._canonical_skill_card_chip_key(t) for t in mythic["tags"]]
        self.assertEqual(len(mythic_keys), len(set(mythic_keys)))
        self.assertEqual(mythic_keys.count("blind"), 1)

    def test_skill_card_chip_key_haste_debuff_distinct_from_haste_buff(self):
        buff_key = rs._canonical_skill_card_chip_key("Haste buff")
        debuff_key = rs._canonical_skill_card_chip_key("Haste debuff")
        self.assertEqual(buff_key, "haste")
        self.assertEqual(debuff_key, "haste debuff")
        self.assertNotEqual(buff_key, debuff_key)

    def test_skill_card_chip_key_energy_recovery_debuff_distinct(self):
        buff_key = rs._canonical_skill_card_chip_key("Energy recovery")
        debuff_key = rs._canonical_skill_card_chip_key("Energy recovery debuff")
        self.assertEqual(buff_key, "energy recovery")
        self.assertEqual(debuff_key, "energy recovery debuff")
        self.assertNotEqual(buff_key, debuff_key)

    def test_contess_skill2_skill_card_energy_recovery_debuff(self):
        hero = self._hero_analyzed("Contess")
        tags = rs.format_skill_card_tags(hero, "skill2")
        self.assertIn("Energy recovery debuff", tags)
        keys = [rs._canonical_skill_card_chip_key(t) for t in tags]
        self.assertIn("energy recovery debuff", keys)
        self.assertNotIn("energy recovery", keys)

    def test_galahad_ultimate_skill_card_includes_haste_debuff(self):
        hero = self._hero_analyzed("Galahad")
        summaries = rs._load_skill_summaries().get("Galahad", {})
        categories = set(summaries)
        tags = rs.format_skill_card_tags(hero, "ultimate")
        self.assertIn("Haste debuff", tags)
        self.assertIn("Movement speed debuff", tags)
        self.assertIn("Haste buff", tags)
        keys = [rs._canonical_skill_card_chip_key(t) for t in tags]
        self.assertEqual(len(keys), len(set(keys)))

    def test_kazim_skill5_self_targeted_energy_recovery_tag(self):
        hero = self._hero_analyzed("Kazim")
        tags = rs.format_skill_card_tags(hero, "skill5")
        self.assertIn("Energy recovery — Self", tags)
        self.assertIn("ATK SPD buff — Self", tags)
        keys = [rs._canonical_skill_card_chip_key(t) for t in tags]
        self.assertIn("energy recovery", keys)
        self.assertIn("atk spd", keys)

    def test_kazim_skill_cards_omit_implicit_max_hp_damage(self):
        hero = self._hero_analyzed("Kazim")
        for category in ("ultimate", "skill1", "skill2"):
            tags = rs.format_skill_card_tags(hero, category)
            tag_text = " ".join(tags)
            self.assertNotIn(
                "Max HP-based damage",
                tag_text,
                msg=f"{category} should not show implicit max-HP chip",
            )
        ult_tags = rs.format_skill_card_tags(hero, "ultimate")
        self.assertIn("Physical", ult_tags)
        mythic_tags = rs.format_skill_card_tags(hero, "skill4")
        self.assertNotIn("True damage", mythic_tags)
        self.assertIn("Max HP-based damage", mythic_tags)

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
                damage_in_tags = [
                    tag for tag in tags if tag in rs._SKILL_CARD_DAMAGE_KEYS
                ]
                expected = rs._skill_card_damage_labels(
                    hero, hero.skill_slices[section]
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
        self.assertEqual(alna.signature_skill_speed, "fast")
        self.assertEqual(sig["Alna"]["signature_override"], "skill1")
        self.assertEqual(sig["Alna"]["signature_calculated"], "skill2")

        _, aurora = self._hero_by_display("Aurora")
        self.assertEqual(aurora.signature_skill_name, "Starlit Slumber")
        self.assertTrue(aurora.signature_skill_is_ult)
        self.assertFalse(aurora.synergy_signature_is_ult)
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
        self.assertEqual(sig_metrics.first_cast_speed, "fast")
        text = "\n".join(rs.format_behavior_section("Niru", behavior))
        self.assertIn("first cast speed `fast`", text)

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
    def _hero_skills(self, display_name: str):
        text = (ROOT / "Heroes.md").read_text(encoding="utf-8")
        for block in re.split(r"\n(?=## )", text):
            if not block.startswith("## "):
                continue
            title = block.splitlines()[0].replace("## ", "").strip()
            if title.split(" - ", 1)[0].strip() == display_name:
                return rs.load_skill_meta(block)
        self.fail(f"hero block not found: {display_name}")

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

    def test_aliceth_ally_composition(self):
        constraints = rs.detect_placement_constraints(
            self._hero_skills("Aliceth"), "Aliceth"
        )
        kinds = {c.kind for c in constraints}
        self.assertIn("ally_composition", kinds)
        texts = [c.text for c in constraints if c.kind == "ally_composition"]
        self.assertTrue(
            any("nearest ally in same row" in t for t in texts),
            texts,
        )


@unittest.skipUnless(hs.jsonschema is not None, "jsonschema not installed")
class MovementDetectionTests(unittest.TestCase):
    def _behavior(self, display_name: str):
        text = (ROOT / "Heroes.md").read_text(encoding="utf-8")
        blocks = [b for b in re.split(r"\n(?=## )", text) if b.startswith("## ")]
        heroes, block_by_title, role_category_by_title = _analyze_heroes_from_blocks(
            blocks
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
            role_category_by_title=role_category_by_title,
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

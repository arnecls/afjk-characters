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
        hero = rs.parse_hero_block(blocks[0])
        rs.analyze_hero(hero)
        rs.assign_magnitudes([hero])
        return hero, data

    def _round_trip(self, prefix: str):
        hero, data = self._hero_by_title_prefix(prefix)
        record = next(h for h in data["heroes"] if h["title"] == hero.title)
        serialized = hs.serialize_processed_hero(
            hero,
            record,
            is_energy_provider=False,
            behavior={
                "movement": "moving",
                "movement_note": "",
                "casting_speed": "normal",
                "signature_skill_name": "Test",
                "signature_skill_is_ult": False,
                "signature_skill_speed": "normal",
                "synergy_signature_speed": "normal",
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
        before_keys = {(e.category, e.label, e.targeting) for e in before.effects}
        after_keys = {(e.category, e.label, e.targeting) for e in after.effects}
        self.assertEqual(before_keys, after_keys)

    def test_aliceth_full_ascension_numerics(self):
        processed = io.load_processed()
        hero = processed["heroes"]["Aliceth - Radiant Wings"]
        sealed = hero["skills"]["Sealed Fate"]
        pen = next(
            e
            for e in sealed["effects"]
            if e.get("name") == "DEF Penetration buff"
        )
        self.assertEqual(pen["value"][0]["value"], 40.0)
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
        skill = processed["heroes"]["Dionel - Venus of Dawn"]["skills"][
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
        wings = processed["heroes"]["Aliceth - Radiant Wings"]["skills"][
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
    def _hero_by_display(self, display_name: str):
        text = (ROOT / "Heroes.md").read_text(encoding="utf-8")
        blocks = [b for b in re.split(r"\n(?=## )", text) if b.startswith("## ")]
        heroes = [rs.parse_hero_block(b) for b in blocks]
        for hero in heroes:
            rs.analyze_hero(hero)
        rs.assign_magnitudes(heroes)
        display_by_title = {
            h.title: h.title.split(" - ", 1)[0].strip() for h in heroes
        }
        behavior_by_title = rs.build_behavior_for_heroes(heroes, display_by_title)
        for hero in heroes:
            if display_by_title[hero.title] == display_name:
                return hero, behavior_by_title[hero.title]
        self.fail(f"hero not found: {display_name}")

    def test_hugin_skill_overview_speeds(self):
        _, behavior = self._hero_by_display("Hugin")
        overview = behavior.skill_overview
        self.assertEqual(overview["signature"].speed, "slow")
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
        self.assertIn("speed `slow`", text)
        self.assertNotIn("Signature skill speed:", text)
        self.assertNotIn("damage `none`", text)
        self.assertNotIn("- Ultimate:", text)
        self.assertIn("- **Signature skill (ultimate)**:", text)
        self.assertIn("- **Ally composition**:", text)
        self.assertIn("- **Self placement**:", text)

    def test_non_ult_signature_keeps_ultimate_row(self):
        _, behavior = self._hero_by_display("Daimon")
        text = "\n".join(rs.format_behavior_section("Daimon", behavior))
        self.assertIn("- **Ultimate**:", text)

    def test_ravion_true_damage_line_in_skill_overview(self):
        _, behavior = self._hero_by_display("Ravion")
        text = "\n".join(rs.format_behavior_section("Ravion", behavior))
        self.assertIn("- **True damage**:", text)
        self.assertIn("HP loss", text)
        self.assertTrue(behavior.skill_overview["signature"].true_damage)

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
        hero, _ = self._hero_by_display("Aliceth")
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
        self.assertNotIn(" — ", ultimate_tags)
        self.assertNotIn("`high`", ultimate_tags)
        skill1 = next(c for c in cards if c["category"] == "skill1")
        skill1_tags = " ".join(skill1["tags"])
        self.assertIn("Stun", skill1_tags)
        mythic = next(c for c in cards if c["category"] == "skill4")
        mythic_keys = [rs._canonical_skill_card_chip_key(t) for t in mythic["tags"]]
        self.assertEqual(len(mythic_keys), len(set(mythic_keys)))
        self.assertEqual(mythic_keys.count("blind"), 1)

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
        self.assertEqual(alna.signature_skill_name, "Winter Anthem")
        self.assertTrue(alna.signature_skill_is_ult)
        self.assertEqual(alna.signature_skill_speed, "fast")
        self.assertEqual(sig["Alna"]["signature_override"], "ultimate")
        self.assertEqual(sig["Alna"]["signature_calculated"], "skill2")

        _, aurora = self._hero_by_display("Aurora")
        self.assertEqual(aurora.signature_skill_name, "Starlit Slumber")
        self.assertTrue(aurora.signature_skill_is_ult)
        self.assertFalse(aurora.synergy_signature_is_ult)
        self.assertEqual(sig["Aurora"]["signature_calculated"], "skill1")

    def test_cassadee_signature_first_cast_speed(self):
        _, behavior = self._hero_by_display("Cassadee")
        sig_metrics = behavior.skill_overview["signature"]
        self.assertEqual(sig_metrics.speed, "slow")
        self.assertEqual(sig_metrics.first_cast_speed, "fast")
        text = "\n".join(rs.format_behavior_section("Cassadee", behavior))
        self.assertIn("first cast speed `fast`", text)
        self.assertIn("speed `slow`", text)

    def test_bryon_signature_first_cast_speed(self):
        _, behavior = self._hero_by_display("Bryon")
        sig_metrics = behavior.skill_overview["signature"]
        self.assertEqual(sig_metrics.speed, "fast")
        self.assertEqual(sig_metrics.first_cast_speed, "fast")
        text = "\n".join(rs.format_behavior_section("Bryon", behavior))
        self.assertIn("first cast speed `fast`", text)

    def test_niru_signature_first_cast_speed(self):
        _, behavior = self._hero_by_display("Niru")
        sig_metrics = behavior.skill_overview["signature"]
        self.assertEqual(sig_metrics.speed, "slow")
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

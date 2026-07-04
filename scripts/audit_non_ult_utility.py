#!/usr/bin/env python3
"""Propose non-ult-utility behavior tags from per-section skill overview metrics."""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

import heroes_io as io
import roster_analysis as ra

rs, gen = ra.analysis_modules()

NON_ULT_SECTIONS = rs.NON_ULT_SKILL_SECTIONS
SECTION_SUMMARY_KEY = {
    "Skill1": "skill1",
    "Skill2": "skill2",
    "Ex. Skill": "skill4",
}
METRIC_FIELDS = ("damage", "heal", "buffs", "debuffs")
BLOCKING_TAGS = frozenset({"high-damage-ult", "battle-start-ult"})
TAG = "non-ult-utility"

MAG_PTS = {"none": 0, "low": 0, "average": 1, "high": 2}
_MAG_ORDER = {"none": 0, "low": 1, "average": 2, "high": 3}

_ULT_SUPPORT_VERBS = re.compile(
    r"\b(buff|enhance|boost|stack|empower|grant|additional|extend|volley|"
    r"reduces?|increase[sd]?)\b",
    re.I,
)
_ULT_REF = re.compile(
    r"\bultimate\b|\bult\b|\bsignature skill\b",
    re.I,
)
_STRONG_ATTACK = re.compile(
    r"multiple attacks|repeated .{0,20}attacks?|progressively grow|multi-hit|"
    r"deal .{0,15}damage|frontal area attacks|sweeping|max hp-based damage|"
    r"arc damage|three-hit|counter with an? ",
    re.I,
)


@dataclass
class SectionUtility:
    high_fields: int = 0
    utility_pts: int = 0
    damage_pts: int = 0
    buff_pts: int = 0
    peak_damage_mag: str = "none"
    strong_attack: bool = False


@dataclass
class HeroUtility:
    high_total: int = 0
    utility_total: int = 0
    sec_util: int = 0
    sec_dmg: int = 0
    dmg_effect_secs: int = 0
    buff_pts: int = 0
    dmg_pts_total: int = 0
    strong_attack: int = 0


def _skill_section_text(skills: list, section: str) -> str:
    for skill in skills:
        if skill.section == section:
            return skill.text or ""
    return ""


def _ultimate_skill(skills: list):
    for skill in skills:
        if skill.section == "Ultimate":
            return skill
    return None


def is_ultimate_support(summary_text: str, skill_text: str) -> bool:
    """True when a non-ult skill primarily buffs or enhances the ultimate."""
    combined = f"{summary_text}\n{skill_text}".strip()
    if not combined:
        return False
    if not _ULT_REF.search(combined):
        return False
    if _ULT_SUPPORT_VERBS.search(combined):
        return True
    if re.search(r"on ultimate|casting ultimate|ultimate cast|ultimate hit", combined, re.I):
        return True
    return False


def high_field_count(metrics: rs.SkillOverviewMetrics) -> int:
    return sum(1 for field in METRIC_FIELDS if getattr(metrics, field) == "high")


def peak_damage_effect_mag(hero, section: str) -> str:
    """Highest damage-effect magnitude in a section's skill slice."""
    sl = hero.skill_slices.get(section)
    if not sl:
        return "none"
    mags = [
        e.magnitude
        for e in sl.effects + sl.summon_effects
        if e.category == "damage"
    ]
    if not mags:
        return "none"
    return max(mags, key=lambda m: _MAG_ORDER.get(m, 0))


def compute_hero_utility(
    hero,
    skills: list,
    speeds: dict,
    damage_thresholds: tuple[float, float],
    damage_type_thresholds: dict,
    summaries: dict[str, str],
) -> tuple[HeroUtility, list[str]]:
    totals = HeroUtility()
    notes: list[str] = []
    for section in NON_ULT_SECTIONS:
        summary_key = SECTION_SUMMARY_KEY.get(section, "")
        summary_text = summaries.get(summary_key, "")
        skill_text = _skill_section_text(skills, section)
        if is_ultimate_support(summary_text, skill_text):
            notes.append(f"skip {section}: ultimate-support")
            continue

        metrics = rs.compute_section_skill_metrics(
            hero,
            skills,
            section,
            speeds,
            damage_thresholds,
            damage_type_thresholds,
        )
        heal, buffs, debuffs = rs._section_effect_metrics(hero, section)
        peak_dmg = peak_damage_effect_mag(hero, section)
        dmg_pts = max(MAG_PTS[metrics.damage], MAG_PTS[peak_dmg])
        buff_pts = MAG_PTS[buffs]
        utility_pts = (
            dmg_pts
            + MAG_PTS[heal]
            + buff_pts
            + MAG_PTS[debuffs]
        )
        highs = high_field_count(metrics)
        sec = SectionUtility(
            high_fields=highs,
            utility_pts=utility_pts,
            damage_pts=dmg_pts,
            buff_pts=buff_pts,
            peak_damage_mag=peak_dmg,
            strong_attack=bool(_STRONG_ATTACK.search(summary_text)),
        )

        totals.high_total += sec.high_fields
        totals.utility_total += sec.utility_pts
        totals.buff_pts += sec.buff_pts
        totals.dmg_pts_total += sec.damage_pts
        if sec.utility_pts >= 2:
            totals.sec_util += 1
        if sec.damage_pts >= 1:
            totals.sec_dmg += 1
        if peak_dmg in ("average", "high"):
            totals.dmg_effect_secs += 1
        if sec.strong_attack:
            totals.strong_attack += 1

        if highs or utility_pts >= 2:
            notes.append(
                f"{section}: {highs} high, {utility_pts} util "
                f"(dmg={metrics.damage}/{peak_dmg})"
            )

    return totals, notes


def _path_b_burst(behavior_tags: frozenset[str], totals: HeroUtility) -> bool:
    if totals.utility_total < 5:
        return False
    if totals.sec_util < 2 or totals.sec_dmg < 2 or totals.dmg_effect_secs < 2:
        return False
    if "battle-start-burst" not in behavior_tags:
        return False
    return "aoe-damage" in behavior_tags or "enemy-debuffer" in behavior_tags


def _path_b_hp_shield(behavior_tags: frozenset[str], totals: HeroUtility) -> bool:
    if totals.utility_total < 5:
        return False
    if totals.sec_util < 2 or totals.sec_dmg < 2 or totals.dmg_effect_secs < 2:
        return False
    if "hp-scaling" not in behavior_tags:
        return False
    return totals.buff_pts >= 3 and totals.dmg_pts_total >= 2


def _path_b_attack(behavior_tags: frozenset[str], totals: HeroUtility) -> bool:
    if "summoner" in behavior_tags:
        return False
    if totals.utility_total < 4:
        return False
    if totals.sec_util < 2 or totals.sec_dmg < 2:
        return False
    return totals.strong_attack >= 2


def qualifies_non_ult_utility(
    hero,
    skills: list,
    speeds: dict,
    damage_thresholds: tuple[float, float],
    damage_type_thresholds: dict,
    summaries: dict[str, str],
    behavior_tags: frozenset[str],
) -> tuple[bool, str, list[str]]:
    if behavior_tags & BLOCKING_TAGS:
        return False, "", ["blocked by ult-reliant tag"]

    ult = _ultimate_skill(skills)
    if ult and rs.text_has_start_of_battle_ultimate(ult.text, "Ultimate"):
        return False, "", ["blocked by start-of-battle ultimate"]

    totals, notes = compute_hero_utility(
        hero,
        skills,
        speeds,
        damage_thresholds,
        damage_type_thresholds,
        summaries,
    )

    if totals.high_total >= 2:
        return True, "path A", notes
    if _path_b_attack(behavior_tags, totals):
        return True, "path B_attack", notes
    if _path_b_burst(behavior_tags, totals):
        return True, "path B_burst", notes
    if _path_b_hp_shield(behavior_tags, totals):
        return True, "path B_hp_shield", notes

    return False, "", notes


def main() -> int:
    apply = "--apply" in sys.argv
    raw = json.loads(io.HEROES_DATA.read_text(encoding="utf-8"))
    processed = json.loads(io.HEROES_DATA_PROCESSED.read_text(encoding="utf-8"))
    summaries_by_short = json.loads(
        (ROOT / "data" / "heroes_data_skill_summary.json").read_text(encoding="utf-8")
    )
    current_tags = json.loads(
        (ROOT / "data" / "hero_behavior_tags.json").read_text(encoding="utf-8")
    )

    role_by_title = {
        p["long_name"]: p["role_category"]
        for p in processed["heroes"].values()
    }
    analysis = ra.get_roster_analysis(raw, role_by_title)

    per_skill_speeds = rs.compute_per_skill_speeds(analysis.skills_by_title)
    damage_thresholds = rs.build_section_damage_thresholds(
        analysis.heroes, analysis.skills_by_title
    )
    damage_type_thresholds = rs.build_damage_type_thresholds(
        analysis.heroes, analysis.skills_by_title
    )

    proposed: dict[str, list[str]] = {}
    for hero in analysis.heroes:
        short = gen.short_name(hero.title)
        skills = analysis.skills_by_title[hero.title]
        speeds = per_skill_speeds.get(hero.title, {})
        tags = frozenset(current_tags.get(short, []))
        ok, path, notes = qualifies_non_ult_utility(
            hero,
            skills,
            speeds,
            damage_thresholds,
            damage_type_thresholds,
            summaries_by_short.get(short, {}),
            tags,
        )
        if ok:
            proposed[short] = notes
            print(f"{short}: YES ({path}) — {'; '.join(notes)}")

    print(f"\n{len(proposed)} heroes qualify for {TAG}")

    if apply:
        tags_path = ROOT / "data" / "hero_behavior_tags.json"
        tag_data = json.loads(tags_path.read_text(encoding="utf-8"))
        changed = 0
        for short in tag_data:
            has_tag = TAG in tag_data[short]
            should = short in proposed
            if should and not has_tag:
                tag_data[short].append(TAG)
                tag_data[short].sort()
                changed += 1
            elif not should and has_tag:
                tag_data[short] = [t for t in tag_data[short] if t != TAG]
                changed += 1
        tags_path.write_text(
            json.dumps(tag_data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print(f"Applied {TAG} updates to {changed} heroes in hero_behavior_tags.json")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

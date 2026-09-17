"""Roster-wide magnitude calibration over analyzed effect lists."""

from __future__ import annotations

import statistics
from collections import defaultdict
from typing import Any

from .records import Effect, Hero, SkillMeta
from . import effects as rs


def recompute_damage_scores(
    heroes: list[Hero],
    skills_by_title: dict[str, list[SkillMeta]],
) -> None:
    for hero in heroes:
        skills = skills_by_title.get(hero["title"], [])
        if not skills:
            continue
        primary = hero["damage_type"] or "Physical"
        hero["damage_scores"].clear()
        for _tier, text, section in hero["skill_chunks"]:
            if rs._chunk_is_companion_focused(text):
                continue
            if rs._skill_chunk_has_ally_only_damage(text):
                continue
            tgt = rs.detect_targeting(text)
            for damage_type in rs.detect_damage_types(text, primary):
                if damage_type not in rs.TRUE_DAMAGE_TYPES:
                    continue
                score = rs._score_true_damage_chunk(
                    text,
                    damage_type,
                    tgt,
                    section=section,
                    skills=skills,
                )
                if score > 0:
                    hero["damage_scores"][damage_type] = max(
                        hero["damage_scores"].get(damage_type, 0.0),
                        score,
                    )


def assign_damage_magnitudes(heroes: list[Hero]) -> None:
    by_type: dict[str, list[float]] = defaultdict(list)
    for hero in heroes:
        for damage_type, score in hero["damage_scores"].items():
            if damage_type in rs.TRUE_DAMAGE_TYPES:
                by_type[damage_type].append(score)

    thresholds: dict[str, tuple[float, float]] = {}
    for damage_type, scores in by_type.items():
        thresholds[damage_type] = rs._quantile_thresholds(scores)

    for hero in heroes:
        for damage_type in hero["damage_scores"]:
            if damage_type not in rs.TRUE_DAMAGE_TYPES:
                continue
            score = hero["damage_scores"][damage_type]
            t1, t2 = thresholds.get(damage_type, rs._FALLBACK_DAMAGE_THRESHOLDS)
            hero["damage_magnitudes"][damage_type] = (
                "low" if score <= t1 else "average" if score <= t2 else "high"
            )


def assign_magnitudes(
    heroes: list[Hero],
    skills_by_title: dict[str, list[SkillMeta]] | None = None,
) -> None:
    skills_map = skills_by_title or {}
    if skills_map:
        recompute_damage_scores(heroes, skills_map)
    by_key: dict[str, list[tuple[Hero, Effect]]] = defaultdict(list)
    for hero in heroes:
        for eff in hero["effects"] + hero["summon_effects"]:
            by_key[f"{eff['category']}:{eff['label']}"].append((hero, eff))
    for group in by_key.values():
        category = group[0][1]["category"]
        label = group[0][1]["label"]
        if category == "cc":
            for _hero, effect in group:
                effect["magnitude"] = rs.qualitative_magnitude(effect)
            continue
        if label in rs._ALWAYS_HIGH_BUFFS:
            for _hero, effect in group:
                effect["magnitude"] = rs.qualitative_magnitude(effect)
            continue
        if category == "debuff" and label in rs._ALWAYS_MEDIUM_DEBUFFS:
            for _hero, effect in group:
                effect["magnitude"] = rs.qualitative_magnitude(effect)
            continue
        use_throughput = rs._effect_uses_throughput(category, label) and bool(
            skills_map
        )
        scored: list[tuple[Any, Hero, Effect]] = []
        for hero, effect in group:
            if use_throughput:
                skills = skills_map.get(hero["title"], [])
                val = (
                    rs._effect_throughput_score(effect, hero, skills)
                    if skills
                    else effect["numeric"]
                )
                scored.append(
                    (val if val and val > 0 else effect["numeric"], hero, effect)
                )
            else:
                scored.append((effect["numeric"], hero, effect))
        nums = sorted(v for v, _hero, _effect in scored if v is not None)
        if len(nums) >= 6:
            t1, t2 = statistics.quantiles(nums, n=3)
            for val, _hero, effect in scored:
                if val is None:
                    effect["magnitude"] = rs.qualitative_magnitude(effect)
                else:
                    effect["magnitude"] = (
                        rs.qualitative_magnitude(effect)
                        if use_throughput and val <= 0
                        else (
                            "low"
                            if val <= t1
                            else "average"
                            if val <= t2
                            else "high"
                        )
                    )
        else:
            for _val, _hero, effect in scored:
                effect["magnitude"] = rs.qualitative_magnitude(effect)
    for hero in heroes:
        for eff in hero["effects"] + hero["summon_effects"]:
            rs.apply_conditional_magnitude(eff)
    assign_damage_magnitudes(heroes)

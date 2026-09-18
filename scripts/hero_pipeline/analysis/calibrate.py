"""Roster-relative calibration over ID-keyed local analyses."""

from __future__ import annotations

import copy
import re
from typing import Any, Mapping, cast

from healing_types import is_hp_recovery_label

from ..contracts import (
    AnalysisContext,
    CalibratedAnalysis,
    HeroManifestEntry,
    LocalAnalysis,
    ProcessedRoster,
    RosterSnapshot,
)
from ..storage import _manifest_entries
from . import behavior as bh
from . import schema_effects as se
from . import scoring_facts as gen
from . import serialize as hs
from . import magnitudes as mag
from .records import SkillMeta, HeroRecord
from .skill_meta import from_schema_skill
from .damage import _effect_throughput_score


def calibrate_roster(
    analyses_by_id: Mapping[str, LocalAnalysis],
    snapshot: RosterSnapshot,
) -> tuple[ProcessedRoster, list[CalibratedAnalysis], AnalysisContext]:
    """Apply roster-wide calibration to ID-keyed local mappings."""
    unknown = sorted(set(analyses_by_id) - set(snapshot["bundles"]))
    if unknown:
        raise ValueError(
            "local analysis key does not match a roster id: "
            + ", ".join(unknown)
        )
    for hero_id, analysis in analyses_by_id.items():
        if analysis.get("id") != hero_id:
            raise ValueError(
                f"local analysis key {hero_id!r} does not match "
                f"record id {analysis.get('id')!r}"
            )
    ordered = sorted(
        analyses_by_id.items(),
        key=lambda item: snapshot["bundles"][item[0]]["manifest"]["order"],
    )
    skills_by_id = {
        hero_id: _skills_for_analysis(analysis, snapshot["bundles"][hero_id])
        for hero_id, analysis in ordered
    }
    working = [
        _working_record(hero_id, analysis, stamp_sections=True)
        for hero_id, analysis in ordered
    ]
    mag.assign_magnitudes(working, skills_by_id)
    behavior_inputs = _behavior_inputs(snapshot)
    display_by_id = {
        hero_id: analysis["display_name"] for hero_id, analysis in ordered
    }
    class_by_id = {
        hero_id: str(
            (snapshot["bundles"][hero_id]["source"].get("source") or {}).get(
                "class"
            )
            or analysis.get("class")
            or ""
        )
        for hero_id, analysis in ordered
    }
    behavior_by_id = bh.build_behavior_for_heroes(
        working,
        display_by_id,
        hero_class_by_title=class_by_id,
        skills_by_title_input=skills_by_id,
        block_by_title_input={
            hero_id: " ".join(skill["text"] for skill in skills)
            for hero_id, skills in skills_by_id.items()
        },
        signature_by_display_input=behavior_inputs["signatures"],
        placement_overrides_input=behavior_inputs["placement"],
        movement_overrides_input=behavior_inputs["movement"],
        walk_speeds_input=behavior_inputs["walk_speeds"],
        behavior_tags_input=behavior_inputs["behavior_tags"],
        skill_names_by_display_input=behavior_inputs["skill_names"],
    )
    processed = _serialize_processed(
        working,
        snapshot,
        behavior_by_id,
        analyses_by_id,
        skills_by_id,
        class_by_id,
    )
    context: AnalysisContext = {
        "skills_by_id": skills_by_id,
        "hero_class_by_id": class_by_id,
        "behavior_by_id": cast(dict[str, object], behavior_by_id),
    }
    return (
        cast(ProcessedRoster, processed),
        [cast(CalibratedAnalysis, row) for row in processed["heroes"].values()],
        context,
    )


def _json_value(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: _json_value(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_value(item) for item in value]
    return value


def _skills_for_analysis(
    analysis: Mapping[str, Any],
    bundle: Mapping[str, Any],
) -> list[Any]:
    source_skills = list(
        (bundle.get("source") or {}).get("source", {}).get("skills") or []
    )
    source_by_section = {
        skill.get("section"): skill for skill in source_skills
    }
    metas = []
    for skill in (analysis.get("skills") or {}).values():
        section = se.CATEGORY_TO_SECTION.get(
            str(skill.get("category") or ""),
            str(skill.get("category") or ""),
        )
        metas.append(
            from_schema_skill(
                skill,
                source_skill=source_by_section.get(section),
            )
        )
    return metas


def _working_record(
    hero_id: str,
    analysis: Mapping[str, Any],
    *,
    stamp_sections: bool,
) -> HeroRecord:
    converted = se.working_effects_from_skills(
        analysis,
        stamp_sections=stamp_sections,
    )
    damage_entries = [
        (hs.to_display_damage_type(row[0]), row[1])
        for row in analysis.get("damage_entries") or []
    ]
    raw_range = analysis.get("default_range")
    default_range = (
        int(raw_range) if isinstance(raw_range, (int, float)) else None
    )
    from .records import Hero

    return Hero(
        title=hero_id,
        damage_type=analysis.get("primary_damage_type") or "Physical",
        skill_chunks=[
            tuple(chunk) for chunk in analysis.get("skill_chunks") or []
        ],
        skill_slices=converted["skill_slices"],
        effects=converted["effects"],
        summon_effects=converted["summon_effects"],
        cc_immunities=converted["cc_immunities"],
        special_effects=converted["special_effects"],
        damage_entries=damage_entries,
        damage_magnitudes={
            hs.to_display_damage_type(dt): mag_label
            for dt, mag_label in (analysis.get("damage_magnitudes") or {}).items()
        },
        benefit_stats=[
            hs.to_display_stat(stat)
            for stat in analysis.get("benefit_stats") or []
        ],
        scalar_stat_shares={
            hs.to_display_stat(stat): float(share)
            for stat, share in (analysis.get("scalar_stat_shares") or {}).items()
        },
        default_range=default_range,
        positional_tile_buff_labels=frozenset(
            analysis.get("positional_tile_buff_labels") or []
        ),
        proximity_aura_buff_labels=frozenset(
            analysis.get("proximity_aura_buff_labels") or []
        ),
        proximity_aura_radius=analysis.get("proximity_aura_radius"),
        id=hero_id,
        display_name=analysis.get("display_name"),
        long_name=analysis.get("long_name"),
        section_effects=converted["section_effects"],
    )


def _behavior_inputs(snapshot: Mapping[str, Any]) -> dict[str, Any]:
    result: dict[str, dict[str, Any]] = {
        "signatures": {},
        "placement": {},
        "movement": {},
        "walk_speeds": {},
        "behavior_tags": {},
        "skill_names": {},
    }
    for entry in _manifest_entries(snapshot["manifest"]):
        hero_id = entry["id"]
        bundle = snapshot["bundles"][hero_id]
        source_doc = bundle["source"]
        ai = bundle["ai"]
        overrides = bundle["overrides"]
        local = (bundle.get("analysis") or {}).get("local") or {}
        signature: dict[str, Any] = {}
        if local.get("signature_calculated"):
            signature["signature_calculated"] = local["signature_calculated"]
        signature.update(overrides.get("signature") or {})
        if signature:
            result["signatures"][hero_id] = signature
        if overrides.get("placement_constraints"):
            result["placement"][hero_id] = copy.deepcopy(
                overrides["placement_constraints"]
            )
        if overrides.get("movement"):
            result["movement"][hero_id] = copy.deepcopy(overrides["movement"])
        walk_speed = (source_doc.get("external") or {}).get("walk_speed")
        if walk_speed is not None:
            result["walk_speeds"][hero_id] = walk_speed
        result["behavior_tags"][hero_id] = list(ai.get("behavior_tags") or [])
        names: dict[str, str] = {}
        for skill in (source_doc.get("source") or {}).get("skills") or []:
            category = bh.SECTION_TO_SKILL_CATEGORY.get(skill.get("section", ""))
            if category and skill.get("name"):
                names[category] = skill["name"]
        result["skill_names"][hero_id] = names
    return result


def analyze_bundles(snapshot: Mapping[str, Any]) -> list[Any]:
    """Run hero-local analysis for every bundle."""
    from .local import analyze_local

    heroes = []
    for entry in _manifest_entries(snapshot["manifest"]):
        bundle = snapshot["bundles"][entry["id"]]
        heroes.append(analyze_local(cast(HeroManifestEntry, entry), bundle))
    return heroes


def _section_token(section: str | None) -> str:
    return {
        "Ultimate": "ultimate",
        "Skill1": "skill1",
        "Skill2": "skill2",
        "Unlocks at Legendary+": "skill3",
        "Ex. Skill": "skill4",
        "Unlocks at Supreme+": "skill5",
    }.get(section or "", "passive")


def _effect_key(effect: Any) -> str:
    section = _section_token(effect["source_section"])
    parts: tuple[str, ...]
    if effect["category"] == "buff" and is_hp_recovery_label(effect["label"]):
        parts = (effect["category"], effect["label"], section)
    elif effect["category"] == "buff":
        bucket = "self" if effect["targeting"] == "Self" else "ally"
        parts = (effect["category"], effect["label"], bucket)
    elif effect["category"] in {"cc", "debuff"}:
        parts = (effect["category"], effect["label"], effect["targeting"])
    else:
        parts = (effect["category"], effect["label"])
    return "|".join(parts)


def _extra_analysis_fields(
    working: HeroRecord,
    summary: Mapping[str, Any],
    *,
    skills: list[Any],
    hero_class: str,
    behavior: Any,
    bundle: Mapping[str, Any],
    id_by_display: Mapping[str, str],
) -> dict[str, Any]:
    effects: dict[str, dict[str, Any]] = {}
    skill_effect_magnitudes: dict[str, str] = {}
    for section, effect in working["section_effects"]:
        key = "|".join(
            (
                _section_token(section),
                effect["category"],
                effect["label"],
                effect["targeting"],
            )
        )
        skill_effect_magnitudes[key] = effect["magnitude"]
    merged_effects = list(working["effects"]) + list(working["summon_effects"])
    signature_section = behavior["signature_skill_section"]
    signature_name = behavior["signature_skill_name"]

    for effect in merged_effects:
        raw = _effect_throughput_score(effect, working, skills)
        effect_facts = {
            "magnitude": effect["magnitude"],
            "weight": raw,
        }
        if effect["category"] == "cc" and gen._cc_effect_in_signature(
            effect,
            working,
            signature_section,
            signature_name,
        ):
            effect_facts["signature_cc"] = True
        if (
            effect["category"] == "buff"
            and effect["label"] == "Energy"
            and gen._effect_is_battle_start_ally_energy(effect)
        ):
            effect_facts["battle_start_energy"] = True
        effects[_effect_key(effect)] = effect_facts
    merged_numeric = {
        _effect_key(effect): effect.get("numeric") for effect in merged_effects
    }
    ultimate_keys = {
        _effect_key(effect)
        for effect in merged_effects
        if effect.get("source_section") == "Ultimate"
    }
    for section, effect in working["section_effects"]:
        if section != "Unlocks at Supreme+":
            continue
        key = _effect_key(effect)
        if key not in ultimate_keys:
            continue
        current = effects.get(key)
        if current is None or effect["category"] != "debuff":
            continue
        if (
            effect.get("numeric") is None
            or effect.get("numeric") != merged_numeric.get(key)
        ):
            continue
        raw = _effect_throughput_score(effect, working, skills)
        if float(raw or 0) > float(current.get("weight") or 0):
            current["weight"] = raw

    named: dict[str, dict[str, Any]] = {}
    for special in working["special_effects"]:
        if special["label"] != "Named ally on team":
            continue
        ids = [
            hero_id
            for name, hero_id in id_by_display.items()
            if gen._named_ally_text_mentions_hero(special["qualitative"], name)
        ]
        key = "|".join(
            (
                special["kind"],
                special["label"],
                hs.to_schema_tier(special["tier"]),
            )
        )
        named[key] = {
            "ids": ids,
            "grants": [list(item) for item in special.get("grants") or []],
        }

    skill_text = gen.provider_skill_text(working)
    scoring = {
        "primary_damage_type": working["damage_type"],
        "behavior_tags": list(bundle["ai"].get("behavior_tags") or []),
        "summon_profile": {
            "is_summoner": (
                "summoner" in (bundle["ai"].get("behavior_tags") or [])
            ),
            "has_ranged_summons": bool(
                (bundle["ai"].get("summon_profile") or {}).get(
                    "has_ranged_summons"
                )
            ),
        },
        "prydwen_tiers": (bundle["source"].get("source") or {}).get(
            "prydwen_tiers"
        )
        or {},
        "effects": effects,
        "skill_effect_magnitudes": skill_effect_magnitudes,
        "named_allies": named,
        "start_of_battle_output": gen.provider_has_start_of_battle_output(
            working
        ),
        "early_battle_energy": gen.provider_early_battle_ally_energy(working),
        "effective_ally_energy": gen._hero_effective_ally_energy_provided(
            working
        ),
        "shield_payoff": gen.receiver_benefits_from_external_shields(working),
        "ally_magic": gen.match_ally_enabled_magic_damage(working),
        "ranged_damage": (
            gen.match_ranged_damage_allies(working, hero_class) is not None
        ),
        "wide_area": bool(
            re.search(
                r"center of the battlefield|across the battlefield|"
                r"all enemy heroes|all enemies within|whole battlefield|"
                r"most enemies|area with the most enemies|"
                r"enemies within range",
                skill_text,
            )
        ),
        "ally_grant_detail": gen._ally_grant_detail(working, "") or None,
        "replacement_damage": gen._hero_damage_profile(
            working,
            {working["title"]: skills},
        ),
        "signature_section": signature_section,
    }
    return _json_value(
        {
            "positional_tile_buff_labels": sorted(
                working["positional_tile_buff_labels"]
            ),
            "proximity_aura_buff_labels": sorted(
                working["proximity_aura_buff_labels"]
            ),
            "proximity_aura_radius": working["proximity_aura_radius"],
            "summary_effect_magnitudes": {
                "effects": [
                    effect["magnitude"] for effect in summary["effects"]
                ],
                "summon_effects": [
                    effect["magnitude"] for effect in summary["summon_effects"]
                ],
            },
            "scoring": scoring,
        }
    )


def _serialize_processed(
    working_records: list[HeroRecord],
    snapshot: Mapping[str, Any],
    behavior_by_id: Mapping[str, Any],
    analyses_by_id: Mapping[str, LocalAnalysis],
    skills_by_id: Mapping[str, list[Any]],
    class_by_id: Mapping[str, str],
) -> dict[str, Any]:
    import heroes_io as io

    seasons = io.load_seasons()
    energy_provider_ids = {
        row["id"] for row in working_records if gen.is_energy_provider(row)
    }
    processed_heroes: dict[str, dict[str, Any]] = {}
    id_by_display = {
        entry["display_name"]: entry["id"]
        for entry in _manifest_entries(snapshot["manifest"])
    }
    for row in working_records:
        hero_id = row["id"]
        bundle = snapshot["bundles"][hero_id]
        analysis = analyses_by_id[hero_id]
        behavior = behavior_by_id[hero_id]
        behavior_dict = dict(behavior)
        behavior_dict.pop("signature_skill_section", None)
        hero_class = class_by_id[hero_id]
        source = bundle["source"].get("source") or {}
        skills = skills_by_id[hero_id]
        default_range = source.get("range")
        if default_range is not None:
            default_range = int(default_range)
        season, season_number = hs.map_date_to_season(
            source.get("release_date"), seasons
        )
        serialized = copy.deepcopy(dict(analysis))
        for key in (
            "id",
            "display_name",
            "signature_calculated",
            "skill_chunks",
            "primary_damage_type",
        ):
            serialized.pop(key, None)
        serialized.update(
            {
                "is_energy_provider": hero_id in energy_provider_ids,
                "is_melee": bh.compute_is_melee(
                    skills,
                    hero_class=hero_class,
                    display_name=analysis["display_name"],
                    default_range=default_range,
                ),
                "is_dual_range": bh.compute_is_dual_range(
                    skills, display_name=analysis["display_name"]
                ),
                "behavior": behavior_dict,
                "season": season,
                "season_number": season_number,
                "damage_magnitudes": {
                    hs.to_schema_damage_type(dt): mag_label
                    for dt, mag_label in (row.get("damage_magnitudes") or {}).items()
                },
            }
        )
        processed_heroes[hero_id] = serialized
    schema_heroes: dict[str, dict[str, Any]] = {}
    local_only = {
        "id",
        "display_name",
        "signature_calculated",
        "skill_chunks",
        "primary_damage_type",
        "positional_tile_buff_labels",
        "proximity_aura_buff_labels",
        "proximity_aura_radius",
    }
    for hero_id, serialized_row in processed_heroes.items():
        schema_heroes[hero_id] = {
            key: value
            for key, value in serialized_row.items()
            if key not in local_only
        }
    hs.validate_processed({"heroes": schema_heroes})
    summaries = [
        _working_record(row["id"], analyses_by_id[row["id"]], stamp_sections=False)
        for row in working_records
    ]
    mag.assign_magnitudes(summaries, dict(skills_by_id))
    summary_by_id = {row["id"]: row for row in summaries}
    for row in working_records:
        processed_heroes[row["id"]].update(
            _extra_analysis_fields(
                row,
                summary_by_id[row["id"]],
                skills=skills_by_id[row["id"]],
                hero_class=class_by_id[row["id"]],
                behavior=behavior_by_id[row["id"]],
                bundle=snapshot["bundles"][row["id"]],
                id_by_display=id_by_display,
            )
        )
    return {"heroes": processed_heroes}

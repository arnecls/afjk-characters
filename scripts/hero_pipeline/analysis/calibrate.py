"""Roster-relative calibration over ID-keyed local analyses."""

from __future__ import annotations

import copy
import re
from typing import Any, Mapping, cast

import heroes_io as io

from ..contracts import (
    AnalysisContext,
    AnalyzedHero,
    LocalAnalysis,
    ProcessedRoster,
    RosterSnapshot,
)
from ..storage import _manifest_entries
from healing_types import is_hp_recovery_label

from . import scoring_facts as gen
from . import behavior as bh
from . import serialize as hs
from . import effects as rs


def _runtime_hero_from_local(
    analysis: Mapping[str, Any],
    *,
    title: str | None = None,
    damage_type: str | None = None,
    stamp_sections: bool = True,
) -> dict[str, Any]:
    """Convert schema-shaped local skills into one runtime scoring mapping."""
    resolved_title = str(
        title
        or analysis.get("long_name")
        or analysis.get("display_name")
        or ""
    )
    resolved_damage = str(
        damage_type
        or analysis.get("damage_type")
        or analysis.get("primary_damage_type")
        or "Physical"
    )
    hero = rs.Hero(title=resolved_title, damage_type=resolved_damage)
    raw_effects: list[Any] = []
    raw_summon: list[Any] = []
    raw_immunities: list[Any] = []
    slices: dict[str, Any] = {}
    category_to_section = {
        category: section
        for section, category in hs._SECTION_TO_CATEGORY.items()
    }
    for skill in (analysis.get("skills") or {}).values():
        category = str(skill.get("category") or "")
        section = category_to_section.get(category, category)
        converted_effects = []
        converted_summon = []
        converted_immunities = []
        for row in skill.get("effects") or []:
            if hs._is_placeholder_schema_effect(row):
                continue
            converted = hs.schema_effect_to_effect(row)
            if stamp_sections:
                converted = hs._stamp_source_section(converted, section)
            if rs.is_cc_immunity(converted):
                converted_immunities.append(converted)
                raw_immunities.append(converted)
            elif row.get("target") in {
                "summon",
                "own_summons",
                "all_summons",
            }:
                converted_summon.append(converted)
                raw_summon.append(converted)
            else:
                converted_effects.append(converted)
                raw_effects.append(converted)
        slices[section] = rs.SkillSlice(
            section=section,
            tier=str(skill.get("tier") or "base"),
            effects=converted_effects,
            summon_effects=converted_summon,
            cc_immunities=converted_immunities,
        )
    profile = analysis.get("synergy_profile") or {}
    special_effects = [
        hs.synergy_mechanic_to_special(item, "provides")
        for item in profile.get("provides") or []
    ]
    special_effects.extend(
        hs.synergy_mechanic_to_special(item, "requires")
        for item in profile.get("requires") or []
    )
    hero["effects"] = hs._merge_effects(
        raw_effects, keep_section_in_key=stamp_sections
    )
    hero["summon_effects"] = hs._merge_effects(
        raw_summon, keep_section_in_key=stamp_sections
    )
    hero["cc_immunities"] = hs._merge_immunities(raw_immunities)
    hero["special_effects"] = hs._merge_special_effects(special_effects)
    hero["damage_entries"] = [
        (hs.to_display_damage_type(row[0]), row[1])
        for row in analysis.get("damage_entries") or []
    ]
    hero["damage_magnitudes"] = {
        hs.to_display_damage_type(dt): mag
        for dt, mag in (analysis.get("damage_magnitudes") or {}).items()
    }
    hero["benefit_stats"] = [
        hs.to_display_stat(stat) for stat in analysis.get("benefit_stats") or []
    ]
    hero["scalar_stat_shares"] = {
        hs.to_display_stat(stat): float(share)
        for stat, share in (analysis.get("scalar_stat_shares") or {}).items()
    }
    hero["skill_chunks"] = [
        tuple(chunk) for chunk in analysis.get("skill_chunks") or []
    ]
    hero["positional_tile_buff_labels"] = frozenset(
        analysis.get("positional_tile_buff_labels") or []
    )
    hero["proximity_aura_buff_labels"] = frozenset(
        analysis.get("proximity_aura_buff_labels") or []
    )
    hero["proximity_aura_radius"] = analysis.get("proximity_aura_radius")
    raw_range = analysis.get("default_range")
    if isinstance(raw_range, (int, float)):
        hero["default_range"] = int(raw_range)
    hero["id"] = analysis.get("id")
    hero["display_name"] = analysis.get("display_name")
    hero["skill_slices"] = slices
    return hero


def calibrate_roster(
    analyses_by_id: Mapping[str, LocalAnalysis],
    snapshot: RosterSnapshot,
) -> tuple[ProcessedRoster, list[AnalyzedHero], AnalysisContext]:
    """Apply roster-wide calibration to ID-keyed local mappings."""
    return _calibrate_roster(
        analyses_by_id,
        snapshot,
    )


def _calibrate_roster(
    analyses_by_id: Mapping[str, LocalAnalysis],
    snapshot: RosterSnapshot,
) -> tuple[ProcessedRoster, list[AnalyzedHero], AnalysisContext]:
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
    heroes = [_runtime_hero_from_local(analysis) for _, analysis in ordered]
    heroes, behavior_by_title, context = calibrate_heroes(
        heroes,
        snapshot,
    )
    processed = serialize_processed(
        heroes,
        snapshot,
        behavior_by_title,
        context,
        analyses_by_id,
    )
    return (
        cast(ProcessedRoster, processed),
        cast(list[AnalyzedHero], heroes),
        cast(AnalysisContext, context),
    )

def _json_value(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: _json_value(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_value(item) for item in value]
    return value


def _source_records(snapshot: Mapping[str, Any]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for entry in _manifest_entries(snapshot["manifest"]):
        source = copy.deepcopy(
            snapshot["bundles"][entry["id"]]["source"]["source"]
        )
        io.normalize_hero_skills(source)
        records.append(source)
    return records


def _display_by_title(snapshot: Mapping[str, Any]) -> dict[str, str]:
    return {
        entry["title"]: entry["display_name"]
        for entry in _manifest_entries(snapshot["manifest"])
    }


def _id_by_display(snapshot: Mapping[str, Any]) -> dict[str, str]:
    return {
        entry["display_name"]: entry["id"]
        for entry in _manifest_entries(snapshot["manifest"])
    }


def _behavior_inputs(
    snapshot: Mapping[str, Any],
    rs: Any,
) -> dict[str, Any]:
    result: dict[str, dict[str, Any]] = {
        "signatures": {},
        "placement": {},
        "movement": {},
        "walk_speeds": {},
        "behavior_tags": {},
        "skill_names": {},
    }
    for entry in _manifest_entries(snapshot["manifest"]):
        bundle = snapshot["bundles"][entry["id"]]
        source_doc = bundle["source"]
        ai = bundle["ai"]
        overrides = bundle["overrides"]
        local = (bundle.get("analysis") or {}).get("local") or {}
        curated = rs.curated_display_name(entry["display_name"])
        signature: dict[str, Any] = {}
        if local.get("signature_calculated"):
            signature["signature_calculated"] = local["signature_calculated"]
        signature.update(overrides.get("signature") or {})
        if signature:
            result["signatures"][curated] = signature
        if overrides.get("placement_constraints"):
            result["placement"][curated] = copy.deepcopy(
                overrides["placement_constraints"]
            )
        if overrides.get("movement"):
            result["movement"][curated] = copy.deepcopy(
                overrides["movement"]
            )
        walk_speed = (source_doc.get("external") or {}).get("walk_speed")
        if walk_speed is not None:
            result["walk_speeds"][entry["id"]] = walk_speed
        result["behavior_tags"][curated] = list(
            ai.get("behavior_tags") or []
        )
        names: dict[str, str] = {}
        for skill in (source_doc.get("source") or {}).get("skills") or []:
            category = bh.SECTION_TO_SKILL_CATEGORY.get(
                skill.get("section", "")
            )
            if category and skill.get("name"):
                names[category] = skill["name"]
        result["skill_names"][curated] = names
    return result


def analyze_bundles(
    snapshot: Mapping[str, Any],
) -> list[Any]:
    """Run hero-local analysis for every bundle."""
    heroes = []
    for record in _source_records(snapshot):
        hero = rs.hero_from_record(copy.deepcopy(record))
        rs.analyze_hero(hero)
        heroes.append(hero)
    return heroes


def calibrate_heroes(
    heroes: list[Any],
    snapshot: Mapping[str, Any],
) -> tuple[list[Any], dict[str, Any], dict[str, Any]]:
    """Apply roster-wide magnitude and behavior calibration."""
    from .effects import prime_curated_cache

    prime_curated_cache(snapshot)
    records = _source_records(snapshot)
    data_by_title = {record["title"]: record for record in records}
    block_by_title = {
        record["title"]: io.render_hero_block(record)
        for record in records
    }
    behavior_inputs = _behavior_inputs(snapshot, rs)
    skills_by_title = rs.load_skills_by_title_from_records(records)
    rs.assign_magnitudes(heroes, skills_by_title)
    hero_class_by_title = {
        record["title"]: record.get("class") or ""
        for record in records
    }
    display_by_title = _display_by_title(snapshot)
    behavior_by_title = bh.build_behavior_for_heroes(
        heroes,
        display_by_title,
        hero_class_by_title=hero_class_by_title,
        skills_by_title_input=skills_by_title,
        block_by_title_input=block_by_title,
        signature_by_display_input=behavior_inputs["signatures"],
        placement_overrides_input=behavior_inputs["placement"],
        movement_overrides_input=behavior_inputs["movement"],
        walk_speeds_input=behavior_inputs["walk_speeds"],
        behavior_tags_input=behavior_inputs["behavior_tags"],
        skill_names_by_display_input=behavior_inputs["skill_names"],
    )
    return heroes, behavior_by_title, {
        "skills_by_title": skills_by_title,
        "hero_class_by_title": hero_class_by_title,
        "data_by_title": data_by_title,
        "display_by_title": display_by_title,
        "behavior_by_title": behavior_by_title,
    }


def _extra_analysis_fields(
    hero: Any,
    summary_hero: Any,
    *,
    skills: list[Any],
    hero_class: str,
    behavior: Any,
    bundle: Mapping[str, Any],
    id_by_display: Mapping[str, str],
) -> dict[str, Any]:
    def section_token(section: str | None) -> str:
        return {
            "Ultimate": "ultimate",
            "Skill1": "skill1",
            "Skill2": "skill2",
            "Unlocks at Legendary+": "skill3",
            "Ex. Skill": "skill4",
            "Unlocks at Supreme+": "skill5",
        }.get(section or "", "passive")

    def effect_key(effect: Any) -> str:
        section = section_token(effect["source_section"])
        parts: tuple[Any, ...]
        if (
            effect["category"] == "buff"
            and is_hp_recovery_label(effect["label"])
        ):
            parts = (effect["category"], effect["label"], section)
        elif effect["category"] == "buff":
            bucket = "self" if effect["targeting"] == "Self" else "ally"
            parts = (effect["category"], effect["label"], bucket)
        elif effect["category"] in {"cc", "debuff"}:
            parts = (effect["category"], effect["label"], effect["targeting"])
        else:
            parts = (effect["category"], effect["label"])
        return "|".join(parts)

    effects: dict[str, dict[str, Any]] = {}
    skill_effect_magnitudes: dict[str, str] = {}
    for skill_slice in hero["skill_slices"].values():
        for effect in (
            list(skill_slice["effects"]) + list(skill_slice["summon_effects"])
        ):
            key = "|".join(
                (
                    section_token(effect["source_section"]),
                    effect["category"],
                    effect["label"],
                    effect["targeting"],
                )
            )
            skill_effect_magnitudes[key] = effect["magnitude"]
    merged_effects = list(hero["effects"]) + list(hero["summon_effects"])
    signature_section = behavior["signature_skill_section"]
    signature_name = behavior["signature_skill_name"]
    for effect in merged_effects:
        raw = rs._effect_throughput_score(effect, hero, skills)
        effect_facts = {
            "magnitude": effect["magnitude"],
            "weight": raw,
        }
        if effect["category"] == "cc" and gen._cc_effect_in_signature(
                effect,
                hero,
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
        effects[effect_key(effect)] = effect_facts
    merged_numeric = {
        effect_key(effect): effect.get("numeric")
        for effect in merged_effects
    }
    ultimate_keys = {
        effect_key(effect)
        for effect in merged_effects
        if effect.get("source_section") == "Ultimate"
    }
    for skill_slice in hero["skill_slices"].values():
        section = skill_slice.get("section") or ""
        if section != "Unlocks at Supreme+":
            continue
        for effect in (
            list(skill_slice["effects"]) + list(skill_slice["summon_effects"])
        ):
            key = effect_key(effect)
            if key not in ultimate_keys:
                continue
            current = effects.get(key)
            if current is None:
                continue
            if effect["category"] != "debuff":
                continue
            if (
                effect.get("numeric") is None
                or effect.get("numeric") != merged_numeric.get(key)
            ):
                continue
            raw = rs._effect_throughput_score(effect, hero, skills)
            if float(raw or 0) > float(current.get("weight") or 0):
                current["weight"] = raw

    named: dict[str, dict[str, Any]] = {}
    for special in hero["special_effects"]:
        if special["label"] != "Named ally on team":
            continue
        ids = [
            hero_id
            for name, hero_id in id_by_display.items()
            if gen._named_ally_text_mentions_hero(
                special["qualitative"],
                name,
            )
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

    skill_text = gen.provider_skill_text(hero)
    scoring = {
        "primary_damage_type": hero["damage_type"],
        "behavior_tags": list(
            bundle["ai"].get("behavior_tags") or []
        ),
        "summon_profile": {
            "is_summoner": (
                "summoner"
                in (bundle["ai"].get("behavior_tags") or [])
            ),
            "has_ranged_summons": bool(
                (bundle["ai"].get("summon_profile") or {}).get(
                    "has_ranged_summons"
                )
            ),
        },
        "prydwen_tiers": (
            bundle["source"].get("source") or {}
        ).get("prydwen_tiers") or {},
        "effects": effects,
        "skill_effect_magnitudes": skill_effect_magnitudes,
        "named_allies": named,
        "start_of_battle_output": (
            gen.provider_has_start_of_battle_output(hero)
        ),
        "early_battle_energy": gen.provider_early_battle_ally_energy(hero),
        "effective_ally_energy": (
            gen._hero_effective_ally_energy_provided(hero)
        ),
        "shield_payoff": gen.receiver_benefits_from_external_shields(hero),
        "ally_magic": gen.match_ally_enabled_magic_damage(hero),
        "ranged_damage": (
            gen.match_ranged_damage_allies(hero, hero_class) is not None
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
        "ally_grant_detail": gen._ally_grant_detail(hero, "") or None,
        "replacement_damage": gen._hero_damage_profile(
            hero,
            {hero["title"]: skills},
        ),
        "signature_section": signature_section,
    }
    return _json_value({
        "positional_tile_buff_labels": sorted(
            hero["positional_tile_buff_labels"]
        ),
        "proximity_aura_buff_labels": sorted(hero["proximity_aura_buff_labels"]),
        "proximity_aura_radius": hero["proximity_aura_radius"],
        "summary_effect_magnitudes": {
            "effects": [
                effect["magnitude"] for effect in summary_hero["effects"]
            ],
            "summon_effects": [
                effect["magnitude"] for effect in summary_hero["summon_effects"]
            ],
        },
        "scoring": scoring,
    })


def serialize_processed(
    heroes: list[Any],
    snapshot: Mapping[str, Any],
    behavior_by_title: Mapping[str, Any],
    context: Mapping[str, Any],
    analyses_by_id: Mapping[str, LocalAnalysis],
) -> dict[str, Any]:
    """Calibrate ID-keyed local mappings in memory."""
    from . import scoring_facts as facts

    seasons = io.load_seasons()
    energy_provider_titles = {
        hero["title"] for hero in heroes if facts.is_energy_provider(hero)
    }
    processed_heroes: dict[str, dict[str, Any]] = {}
    data_by_title = context["data_by_title"]
    skills_by_title = context["skills_by_title"]
    hero_class_by_title = context["hero_class_by_title"]
    display_by_title = context["display_by_title"]
    id_by_display = _id_by_display(snapshot)
    for hero in heroes:
        behavior = behavior_by_title[hero["title"]]
        bundle = snapshot["bundles"][id_by_display[
            display_by_title[hero["title"]]
        ]]
        hero_record = data_by_title[hero["title"]]
        behavior_dict = dict(behavior)
        behavior_dict.pop("signature_skill_section", None)
        short = display_by_title[hero["title"]]
        hero_id = id_by_display[short]
        hero_class = hero_class_by_title[hero["title"]]
        skills = skills_by_title[hero["title"]]
        default_range = hero_record.get("range")
        if default_range is not None:
            default_range = int(default_range)
        season, season_number = hs.map_date_to_season(
            hero_record.get("release_date"), seasons
        )
        serialized = copy.deepcopy(dict(analyses_by_id[hero_id]))
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
                "is_energy_provider": hero["title"] in energy_provider_titles,
                "is_melee": bh.compute_is_melee(
                    skills,
                    hero_class=hero_class,
                    display_name=short,
                    default_range=default_range,
                ),
                "is_dual_range": bh.compute_is_dual_range(
                    skills, display_name=short
                ),
                "behavior": behavior_dict,
                "season": season,
                "season_number": season_number,
                "damage_magnitudes": {
                    hs.to_schema_damage_type(dt): mag
                    for dt, mag in (
                        hero.get("damage_magnitudes") or {}
                    ).items()
                },
            }
        )
        processed_heroes[hero_id] = serialized
    result = {"heroes": processed_heroes}
    schema_heroes = {}
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
    for hero_id, row in processed_heroes.items():
        schema_heroes[hero_id] = {
            key: value for key, value in row.items() if key not in local_only
        }
    hs.validate_processed({"heroes": schema_heroes})
    summary_by_title = {
        hero["title"]: _runtime_hero_from_local(
            processed_heroes[id_by_display[display_by_title[hero["title"]]]],
            title=hero["title"],
            damage_type=(
                data_by_title[hero["title"]].get("damage_type") or "Physical"
            ),
            stamp_sections=False,
        )
        for hero in heroes
    }
    rs.assign_magnitudes(
        list(summary_by_title.values()),
        skills_by_title,
    )
    for hero in heroes:
        short = display_by_title[hero["title"]]
        behavior = behavior_by_title[hero["title"]]
        bundle = snapshot["bundles"][id_by_display[short]]
        processed_heroes[id_by_display[short]].update(
            _extra_analysis_fields(
                hero,
                summary_by_title[hero["title"]],
                skills=skills_by_title[hero["title"]],
                hero_class=hero_class_by_title[hero["title"]],
                behavior=behavior,
                bundle=bundle,
                id_by_display=id_by_display,
            )
        )
    return result

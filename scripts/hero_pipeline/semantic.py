"""Bundle-native analysis and ID-aware scoring over the shared engine."""

from __future__ import annotations

import copy
import re
from dataclasses import asdict
from typing import Any, Mapping

import hero_schema as hs
import heroes_io as io

from .analysis.policy import policy_scope
from .engine import overview, rewrite_summaries
from .storage import _manifest_entries


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
            snapshot["bundles"][entry["id"]]["generated"]["source"]
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
        generated = bundle["generated"]
        ai = bundle["ai"]
        overrides = bundle["overrides"]
        curated = rs.curated_display_name(entry["display_name"])
        signature: dict[str, Any] = {}
        calculated = (generated.get("derived") or {}).get(
            "signature_calculated"
        )
        if calculated:
            signature["signature_calculated"] = calculated
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
        walk_speed = (generated.get("external") or {}).get("walk_speed")
        if walk_speed is not None:
            result["walk_speeds"][curated] = walk_speed
        result["behavior_tags"][curated] = list(
            ai.get("behavior_tags") or []
        )
        names: dict[str, str] = {}
        for skill in (generated.get("source") or {}).get("skills") or []:
            category = rs.SECTION_TO_SKILL_CATEGORY.get(
                skill.get("section", "")
            )
            if category and skill.get("name"):
                names[category] = skill["name"]
        result["skill_names"][curated] = names
    return result
def analyze_bundles(
    snapshot: Mapping[str, Any],
    policy: Mapping[str, Any],
) -> list[Any]:
    """Run hero-local analysis for every bundle."""
    rs = rewrite_summaries()
    heroes = []
    with policy_scope(policy):
        for record in _source_records(snapshot):
            hero = rs.hero_from_record(copy.deepcopy(record))
            rs.analyze_hero(hero)
            heroes.append(hero)
    return heroes


def calibrate_heroes(
    heroes: list[Any],
    snapshot: Mapping[str, Any],
    policy: Mapping[str, Any],
) -> tuple[list[Any], dict[str, Any], dict[str, Any]]:
    """Apply roster-wide magnitude and behavior calibration."""
    rs = rewrite_summaries()
    records = _source_records(snapshot)
    data_by_title = {record["title"]: record for record in records}
    block_by_title = {
        record["title"]: io.render_hero_block(record)
        for record in records
    }
    behavior_inputs = _behavior_inputs(snapshot, rs)
    with policy_scope(policy):
        skills_by_title = rs.load_skills_by_title_from_records(records)
        rs.assign_magnitudes(heroes, skills_by_title)
        hero_class_by_title = {
            record["title"]: record.get("class") or ""
            for record in records
        }
        display_by_title = _display_by_title(snapshot)
        behavior_by_title = rs.build_behavior_for_heroes(
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
    rs = rewrite_summaries()
    gen = overview()

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
        section = section_token(effect.source_section)
        parts: tuple[Any, ...]
        if (
            effect.category == "buff"
            and gen.is_hp_recovery_label(effect.label)
        ):
            parts = (effect.category, effect.label, section)
        elif effect.category == "buff":
            bucket = "self" if effect.targeting == "Self" else "ally"
            parts = (effect.category, effect.label, bucket)
        elif effect.category in {"cc", "debuff"}:
            parts = (effect.category, effect.label, effect.targeting)
        else:
            parts = (effect.category, effect.label)
        return "|".join(parts)

    effects: dict[str, dict[str, Any]] = {}
    skill_effect_magnitudes: dict[str, str] = {}
    for skill_slice in hero.skill_slices.values():
        for effect in (
            list(skill_slice.effects) + list(skill_slice.summon_effects)
        ):
            key = "|".join(
                (
                    section_token(effect.source_section),
                    effect.category,
                    effect.label,
                    effect.targeting,
                )
            )
            skill_effect_magnitudes[key] = effect.magnitude
    all_effects = list(hero.effects) + list(hero.summon_effects)
    signature_section = behavior.signature_skill_section
    signature_name = behavior.signature_skill_name
    for effect in all_effects:
        raw = rs._effect_throughput_score(effect, hero, skills)
        effect_facts = {
            "magnitude": effect.magnitude,
            "weight": raw,
        }
        if effect.category == "cc" and gen._cc_effect_in_signature(
                effect,
                hero,
                signature_section,
                signature_name,
        ):
            effect_facts["signature_cc"] = True
        if (
            effect.category == "buff"
            and effect.label == "Energy"
            and gen._effect_is_battle_start_ally_energy(effect)
        ):
            effect_facts["battle_start_energy"] = True
        effects[effect_key(effect)] = effect_facts

    named: dict[str, dict[str, Any]] = {}
    for special in hero.special_effects:
        if special.label != "Named ally on team":
            continue
        ids = [
            hero_id
            for name, hero_id in id_by_display.items()
            if gen._named_ally_text_mentions_hero(
                special.qualitative,
                name,
            )
        ]
        key = "|".join(
            (
                special.kind,
                special.label,
                hs.to_schema_tier(special.tier),
            )
        )
        named[key] = {
            "ids": ids,
            "grants": [list(item) for item in special.grants],
        }

    skill_text = gen.provider_skill_text(hero)
    scoring = {
        "primary_damage_type": hero.damage_type,
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
            bundle["generated"].get("source") or {}
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
            {hero.title: skills},
        ),
        "signature_section": signature_section,
    }
    return _json_value({
        "positional_tile_buff_labels": sorted(
            hero.positional_tile_buff_labels
        ),
        "proximity_aura_buff_labels": sorted(hero.proximity_aura_buff_labels),
        "proximity_aura_radius": hero.proximity_aura_radius,
        "summary_effect_magnitudes": {
            "effects": [
                effect.magnitude for effect in summary_hero.effects
            ],
            "summon_effects": [
                effect.magnitude for effect in summary_hero.summon_effects
            ],
        },
        "scoring": scoring,
    })


def serialize_processed(
    heroes: list[Any],
    snapshot: Mapping[str, Any],
    behavior_by_title: Mapping[str, Any],
    context: Mapping[str, Any],
) -> dict[str, Any]:
    """Serialize calibrated heroes to the generated analysis mapping."""
    rs = rewrite_summaries()
    gen = overview()
    seasons = io.load_seasons()
    energy_provider_titles = {
        hero.title for hero in heroes if gen.is_energy_provider(hero)
    }
    processed_heroes: dict[str, dict[str, Any]] = {}
    data_by_title = context["data_by_title"]
    skills_by_title = context["skills_by_title"]
    hero_class_by_title = context["hero_class_by_title"]
    display_by_title = context["display_by_title"]
    id_by_display = _id_by_display(snapshot)
    for hero in heroes:
        behavior = behavior_by_title[hero.title]
        bundle = snapshot["bundles"][id_by_display[
            display_by_title[hero.title]
        ]]
        hero_record = data_by_title[hero.title]
        behavior_dict = asdict(behavior)
        behavior_dict.pop("signature_skill_section", None)
        short = display_by_title[hero.title]
        hero_class = hero_class_by_title[hero.title]
        skills = skills_by_title[hero.title]
        default_range = hero_record.get("range")
        if default_range is not None:
            default_range = int(default_range)
        season, season_number = hs.map_date_to_season(
            hero_record.get("release_date"), seasons
        )
        serialized = hs.serialize_processed_hero(
            hero,
            hero_record,
            is_energy_provider=hero.title in energy_provider_titles,
            is_melee=rs.compute_is_melee(
                skills,
                hero_class=hero_class,
                display_name=short,
                default_range=default_range,
            ),
            is_dual_range=rs.compute_is_dual_range(
                skills, display_name=short
            ),
            behavior=behavior_dict,
            season=season,
            season_number=season_number,
        )
        processed_heroes[id_by_display[short]] = serialized
    result = {"heroes": processed_heroes}
    hs.validate_processed(result)
    summary_by_title = {
        hero.title: hs.deserialize_hero(
            hero.title,
            processed_heroes[id_by_display[display_by_title[hero.title]]],
            data_by_title[hero.title].get("damage_type") or "Physical",
        )
        for hero in heroes
    }
    rs.assign_magnitudes(
        list(summary_by_title.values()),
        skills_by_title,
    )
    for hero in heroes:
        short = display_by_title[hero.title]
        behavior = behavior_by_title[hero.title]
        bundle = snapshot["bundles"][id_by_display[short]]
        processed_heroes[id_by_display[short]].update(
            _extra_analysis_fields(
                hero,
                summary_by_title[hero.title],
                skills=skills_by_title[hero.title],
                hero_class=hero_class_by_title[hero.title],
                behavior=behavior,
                bundle=bundle,
                id_by_display=id_by_display,
            )
        )
    return result

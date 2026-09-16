"""Bundle-native analysis and ID-aware scoring over the shared engine."""

from __future__ import annotations

import copy
from dataclasses import asdict
from typing import Any, Mapping

import hero_schema as hs
import heroes_io as io

from .analysis.policy import policy_scope
from .engine import overview, rewrite_summaries
from .storage import _manifest_entries


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
    gen = overview()
    records = _source_records(snapshot)
    data_by_title = {record["title"]: record for record in records}
    with policy_scope(policy):
        skills_by_title = rs.load_skills_by_title_from_records(records)
        rs.assign_magnitudes(heroes, skills_by_title)
        raw = {
            "heroes": records,
            "heroes_header": (snapshot["manifest"].get("headers") or {}).get(
                "heroes_header",
                "",
            ),
        }
        heroes_text = io.reconstruct_heroes_md(raw)
        behavior_text = io.reconstruct_heroes2_md(raw)
        block_by_title = {
            record["title"]: io.render_hero_block(record) for record in records
        }
        hero_class_by_title = {
            hero.title: gen._parse_hero_class(block_by_title[hero.title])
            for hero in heroes
        }
        display_by_title = _display_by_title(snapshot)
        behavior_by_title = rs.build_behavior_for_heroes(
            heroes,
            display_by_title,
            heroes2_text=behavior_text,
            heroes_text=heroes_text,
            hero_class_by_title=hero_class_by_title,
        )
    return heroes, behavior_by_title, {
        "skills_by_title": skills_by_title,
        "hero_class_by_title": hero_class_by_title,
        "data_by_title": data_by_title,
        "display_by_title": display_by_title,
        "behavior_by_title": behavior_by_title,
    }


def _extra_analysis_fields(hero: Any) -> dict[str, Any]:
    return {
        "positional_tile_buff_labels": sorted(
            hero.positional_tile_buff_labels
        ),
        "proximity_aura_buff_labels": sorted(hero.proximity_aura_buff_labels),
        "proximity_aura_radius": hero.proximity_aura_radius,
    }


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
    for hero in heroes:
        behavior = behavior_by_title[hero.title]
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
        processed_heroes[short] = serialized
    result = {"heroes": processed_heroes}
    hs.validate_processed(result)
    for hero in heroes:
        short = display_by_title[hero.title]
        processed_heroes[short].update(_extra_analysis_fields(hero))
    return result


def score_heroes(
    heroes: list[Any],
    processed: Mapping[str, Any],
    snapshot: Mapping[str, Any],
    context: Mapping[str, Any],
    policy: Mapping[str, Any],
) -> dict[str, Any]:
    """Score synergies from calibrated heroes without a second roster parse."""
    gen = overview()
    rs = rewrite_summaries()
    display_by_title = context["display_by_title"]
    hero_class_by_title = context["hero_class_by_title"]
    skills_by_title = context["skills_by_title"]
    with policy_scope(policy):
        role_category_by_title = hs.role_category_by_title_from_processed(
            heroes, dict(processed), gen.short_name
        )
        behavior_by_title = context["behavior_by_title"]
        enabler_matchers = gen._make_enabler_matchers(hero_class_by_title)
        synergy_entries_by_receiver = gen.build_synergy_entries_by_receiver(
            heroes,
            enabler_matchers,
            behavior_by_title,
            role_category_by_title=role_category_by_title,
        )
        beneficiaries_index = gen.build_beneficiaries_index(
            heroes,
            enabler_matchers,
            behavior_by_title,
            synergy_entries_by_receiver=synergy_entries_by_receiver,
            role_category_by_title=role_category_by_title,
        )
        faction_by_title = {
            hero.title: processed["heroes"][gen.short_name(hero.title)][
                "faction"
            ]
            for hero in heroes
        }
        is_melee_by_title = {
            hero.title: processed["heroes"][gen.short_name(hero.title)][
                "is_melee"
            ]
            for hero in heroes
        }
        replacements_index = gen.compute_replacement_scores(
            heroes,
            behavior_by_title,
            faction_by_title,
            role_category_by_title,
            skills_by_title,
            is_melee_by_title,
        )
        from .synergy.replacements import sanitize_replacements

        synergy_heroes: dict[str, dict[str, Any]] = {}
        for hero in heroes:
            benefited = beneficiaries_index.get(hero.title, [])
            synergy_heroes[gen.short_name(hero.title)] = {
                "synergies": gen.format_synergy_entries(
                    synergy_entries_by_receiver[hero.title]
                ),
                "beneficiaries": [
                    {"score": score, "name": name}
                    for score, name in benefited
                ],
                "beneficiary_overflow_reasons": (
                    gen._beneficiary_overflow_reasons(hero)
                ),
                "replacements": sanitize_replacements(
                    replacements_index.get(hero.title, {})
                ),
            }
        result = {"heroes": synergy_heroes}
        hs.validate_synergies(result)
        return result


def analyze_and_score(
    snapshot: Mapping[str, Any],
    policy: Mapping[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Run local analysis, calibration, and scoring from one snapshot."""
    heroes = analyze_bundles(snapshot, policy)
    heroes, behavior_by_title, context = calibrate_heroes(
        heroes, snapshot, policy
    )
    processed = serialize_processed(
        heroes, snapshot, behavior_by_title, context
    )
    synergies = score_heroes(
        heroes, processed, snapshot, context, policy
    )
    return processed, synergies

"""Hero-local analysis: one bundle to one JSON-compatible mapping."""

from __future__ import annotations

import copy
from dataclasses import asdict
from typing import Any, Mapping, cast

import skill_effects_store as skill_effects

from ..contracts import HeroBundle, HeroManifestEntry, LocalAnalysis
from . import serialize as hs
from . import text as rs
from .policy import LocalPolicy, make_policy, thaw_policy

ALGORITHM_VERSION = "local-analysis-v4"


def algorithm_hash() -> str:
    from ..storage import canonical_hash

    return canonical_hash({"algorithm": ALGORITHM_VERSION})


def _apply_local_policy(local_policy: Mapping[str, Any]) -> None:
    rs.ENERGY_FILL_RATE = local_policy["energy_fill_rate"]
    rs.ULT_ENERGY_CAPACITY = local_policy["ult_energy_capacity"]
    rs.INITIAL_CD_SKILL_WEIGHT = local_policy["initial_cd_skill_weight"]
    rs.INITIAL_CD_CAP = local_policy["initial_cd_cap"]
    rs.MIN_CYCLE_SECONDS = local_policy["min_cycle_seconds"]
    rs.PASSIVE_REFERENCE_CYCLE_SECONDS = local_policy[
        "passive_reference_cycle_seconds"
    ]
    rs.CONDITION_FREQUENT_SCORE = local_policy["condition_frequent_score"]
    rs.CONDITION_COOLDOWN_REFERENCE_SECONDS = local_policy[
        "condition_cooldown_reference_seconds"
    ]
    rs.CONDITION_COOLDOWN_FLOOR_MULT = local_policy[
        "condition_cooldown_floor_mult"
    ]
    rs.CONDITION_RARE_DOWNGRADE_STEPS = local_policy[
        "condition_rare_downgrade_steps"
    ]
    rs.MELEE_MAX_RANGE = local_policy["melee_max_range"]
    rs.NON_MELEE_MELEE_MAX_RANGE = local_policy["non_melee_melee_max_range"]


def _json_mapping(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: _json_mapping(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, frozenset, set)):
        return [_json_mapping(item) for item in value]
    return value


def analyze_local(
    entry: HeroManifestEntry,
    bundle: HeroBundle,
    local_policy: LocalPolicy,
) -> LocalAnalysis:
    """Analyze one bundle and return a schema-shaped mapping."""
    _apply_local_policy(local_policy)
    source = dict(copy.deepcopy(bundle["source"]["source"]))
    from heroes_io import normalize_hero_skills

    normalize_hero_skills(source)
    sidecar = bundle["ai"].get("skill_effects")
    if sidecar is None:
        raise FileNotFoundError(
            f"missing skill effects for hero {entry['id']!r}"
        )
    hero = rs.hero_from_record(copy.deepcopy(source))
    skill_effects.apply_sidecar_to_hero(hero, copy.deepcopy(sidecar))
    rs._postprocess_analyzed_hero(hero, hero.damage_type or "Physical")
    from . import overview_facts as gen
    import heroes_io as io

    skills = rs.load_skills_by_title_from_records([source])[hero.title]
    raw_range = source.get("range")
    default_range = (
        int(raw_range) if isinstance(raw_range, (int, float)) else None
    )
    release_date = source.get("release_date")
    season, season_number = hs.map_date_to_season(
        release_date if isinstance(release_date, str) else None,
        io.load_seasons(),
    )
    hero_class = source.get("class")
    analysis = hs.serialize_processed_hero(
        hero,
        source,
        is_energy_provider=gen.is_energy_provider(hero),
        is_melee=rs.compute_is_melee(
            skills,
            hero_class=hero_class if isinstance(hero_class, str) else "",
            display_name=entry["display_name"],
            default_range=default_range,
        ),
        is_dual_range=rs.compute_is_dual_range(
            skills,
            display_name=entry["display_name"],
        ),
        behavior={},
        season=season,
        season_number=season_number,
    )
    analysis.update(
        {
            "id": entry["id"],
            "display_name": entry["display_name"],
            "positional_tile_buff_labels": sorted(
                hero.positional_tile_buff_labels
            ),
            "proximity_aura_buff_labels": sorted(
                hero.proximity_aura_buff_labels
            ),
            "proximity_aura_radius": hero.proximity_aura_radius,
            "signature_calculated": rs.infer_signature_calculated(
                source, entry["id"]
            ),
            "hero": _json_mapping(asdict(hero)),
        }
    )
    return cast(LocalAnalysis, analysis)

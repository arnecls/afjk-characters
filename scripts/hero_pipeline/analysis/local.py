"""Hero-local analysis: one bundle to one JSON-compatible mapping."""

from __future__ import annotations

import copy
from typing import Any, Mapping, cast

import skill_effects_store as skill_effects

from ..contracts import HeroBundle, HeroManifestEntry, LocalAnalysis
from . import behavior as bh
from . import serialize as hs
from .postprocess import _postprocess_analyzed_hero
from .skill_chunks import hero_from_record, load_skills_by_title_from_records

ALGORITHM_VERSION = "local-analysis-v10"


def algorithm_hash() -> str:
    from ..storage import canonical_hash
    from .policy import effective_defaults

    return canonical_hash(
        {
            "algorithm": ALGORITHM_VERSION,
            "schema_version": 2,
            "local_policy": dict(effective_defaults()["local"]),
        }
    )


def _json_mapping(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: _json_mapping(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, frozenset, set)):
        return [_json_mapping(item) for item in value]
    return value


def analyze_local(
    entry: HeroManifestEntry,
    bundle: HeroBundle,
) -> LocalAnalysis:
    """Analyze one bundle and return a schema-shaped mapping."""
    return _analyze_local_bundle(entry, bundle)


def _analyze_local_bundle(
    entry: HeroManifestEntry,
    bundle: HeroBundle,
) -> LocalAnalysis:
    source = dict(copy.deepcopy(bundle["source"]["source"]))
    from heroes_io import normalize_hero_skills

    normalize_hero_skills(source)
    sidecar = bundle["ai"].get("skill_effects")
    if sidecar is None:
        raise FileNotFoundError(
            f"missing skill effects for hero {entry['id']!r}"
        )
    hero: dict[str, Any] = hero_from_record(copy.deepcopy(source))
    skill_effects.apply_sidecar_to_hero(hero, copy.deepcopy(sidecar))
    from .skill_corrections import spec_from_overrides

    hero["skill_corrections"] = spec_from_overrides(bundle.get("overrides"))
    _postprocess_analyzed_hero(hero, hero["damage_type"] or "Physical")
    from . import scoring_facts as gen
    import heroes_io as io

    skills = load_skills_by_title_from_records([source])[hero["title"]]
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
        is_melee=bh.compute_is_melee(
            skills,
            hero_class=hero_class if isinstance(hero_class, str) else "",
            display_name=entry["display_name"],
            default_range=default_range,
        ),
        is_dual_range=bh.compute_is_dual_range(
            skills,
            display_name=entry["display_name"],
        ),
        behavior={},
        season=season,
        season_number=season_number,
    )
    analysis.pop("hero", None)
    analysis.pop("behavior", None)
    analysis.pop("damage_magnitudes", None)
    analysis.update(
        {
            "id": entry["id"],
            "display_name": entry["display_name"],
            "positional_tile_buff_labels": sorted(
                hero["positional_tile_buff_labels"]
            ),
            "proximity_aura_buff_labels": sorted(
                hero["proximity_aura_buff_labels"]
            ),
            "proximity_aura_radius": hero["proximity_aura_radius"],
            "primary_damage_type": hero["damage_type"]
            or source.get("damage_type")
            or "Physical",
            "signature_calculated": bh.infer_signature_calculated(
                source, entry["id"]
            ),
            "skill_chunks": _json_mapping(hero["skill_chunks"]),
        }
    )
    return cast(LocalAnalysis, analysis)

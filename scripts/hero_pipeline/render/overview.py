"""Overview Markdown and CSV output adapter."""

from __future__ import annotations

import csv
import io
from typing import Any, Mapping

import hero_schema as hs
from character_stat_ranks import build_slug_ranks_map, hero_slug

from ..engine import overview_csv, rewrite_summaries
from ..presentation.format import build_overview_markdown
from ..storage import legacy_synergies


def _summary_heroes(view: Mapping[str, Any]) -> dict[str, Any]:
    heroes: dict[str, Any] = {}
    for hero in view["heroes"]:
        analysis = hero["analysis"]
        damage_type = hero["source"].get("damage_type") or "Physical"
        long_name = analysis["long_name"]
        obj = hs.deserialize_hero(long_name, analysis, damage_type)
        labels = analysis.get("positional_tile_buff_labels")
        if labels is not None:
            obj.positional_tile_buff_labels = frozenset(labels)
        prox = analysis.get("proximity_aura_buff_labels")
        if prox is not None:
            obj.proximity_aura_buff_labels = frozenset(prox)
        if "proximity_aura_radius" in analysis:
            obj.proximity_aura_radius = analysis.get("proximity_aura_radius")
        heroes[long_name] = obj
    return heroes


def _name_synergies(view: Mapping[str, Any]) -> dict[str, Any]:
    manifest = view["manifest"]
    bundles = {
        hero["id"]: {"generated": {"synergies": hero["synergies"]}}
        for hero in view["heroes"]
    }
    sample = (view["heroes"][0]["synergies"] if view["heroes"] else {}) or {}
    rows = sample.get("synergies") or []
    if rows and "provider" in (rows[0] or {}):
        return {
            "heroes": {
                hero["display_name"]: hero["synergies"]
                for hero in view["heroes"]
            }
        }
    return legacy_synergies(manifest, bundles)


def render_overview(
    view: Mapping[str, Any],
    config: Mapping[str, Any],
) -> tuple[str, str]:
    """Render overview Markdown and its CSV projection."""
    limits = (view.get("policy") or {}).get("presentation") or {}
    if not limits:
        limits = config.get("display_limits") or {}
    max_syn = int(limits.get("max_synergies", 6))
    max_ben = int(limits.get("max_beneficiaries_display", 4))
    obvious = int(limits.get("obvious_provider_threshold", 20))
    max_rep = int(
        ((view.get("policy") or {}).get("replacement") or {}).get(
            "max_replacements",
            (config.get("replacement_scoring") or {}).get("max_replacements", 3),
        )
    )
    summary_heroes = _summary_heroes(view)
    name_synergies = _name_synergies(view)
    slug_by_name = {
        hero["display_name"]: hero.get("slug") or hero_slug(hero["display_name"])
        for hero in view["heroes"]
    }
    ranks = {
        hero["slug"]: hero["curated"].get("stat_ranks")
        for hero in view["heroes"]
        if hero["curated"].get("stat_ranks") is not None
    }
    slug_ranks = ranks or build_slug_ranks_map(
        {"characters": {}}, set(slug_by_name.values())
    )
    markdown = build_overview_markdown(
        view,
        summary_heroes=summary_heroes,
        max_synergies=max_syn,
        max_beneficiaries=max_ben,
        obvious_threshold=obvious,
        max_replacements=max_rep,
        name_synergies=name_synergies,
        slug_ranks=slug_ranks,
    )
    csv_mod = overview_csv()
    energy_providers = frozenset(
        hero["display_name"]
        for hero in view["heroes"]
        if hero["analysis"].get("is_energy_provider")
    )
    hero_meta = {
        hero["display_name"]: (
            hero["source"].get("faction") or "",
            hero["source"].get("class") or "",
        )
        for hero in view["heroes"]
    }
    hero_tiers = {
        hero["display_name"]: hero["source"].get("prydwen_tiers") or {}
        for hero in view["heroes"]
    }
    hero_roles = {
        hero["display_name"]: hero["analysis"].get("role_category") or ""
        for hero in view["heroes"]
    }
    analyzed = {
        hero["display_name"]: summary_heroes[hero["analysis"]["long_name"]]
        for hero in view["heroes"]
    }
    rows = csv_mod.convert(
        markdown,
        energy_providers,
        hero_meta,
        hero_tiers,
        hero_roles,
        analyzed_heroes=analyzed,
    )
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(csv_mod.COLUMNS)
    writer.writerows(rows)
    return markdown, output.getvalue()

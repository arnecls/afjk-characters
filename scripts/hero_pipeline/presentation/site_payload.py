"""Site JSON payload built from the presentation model."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Mapping

from character_stat_ranks import hero_slug

from ..engine import rewrite_summaries
from ..render.overview import _name_synergies, _summary_heroes


def build_site_payload(
    view: Mapping[str, Any],
    config: Mapping[str, Any],
    *,
    generated_at: str | None = None,
) -> dict[str, Any]:
    """Return site hero documents without reading data files."""
    import render_site as legacy

    rs = rewrite_summaries()
    limits = (view.get("policy") or {}).get("presentation") or {}
    if not limits:
        limits = config.get("display_limits") or {}
    max_syn = int(limits.get("max_synergies", 6))
    max_ben = int(limits.get("max_beneficiaries_display", 4))
    obvious = int(limits.get("obvious_provider_threshold", 20))
    max_rep = int(
        (config.get("replacement_scoring") or {}).get("max_replacements", 3)
    )
    name_synergies = _name_synergies(view)
    summary_heroes = _summary_heroes(view)
    provider_beneficiary_count = {
        short: len(payload.get("beneficiaries") or [])
        for short, payload in name_synergies["heroes"].items()
    }
    slug_by_name = {
        hero["display_name"]: hero.get("slug") or hero_slug(hero["display_name"])
        for hero in view["heroes"]
    }
    heroes_out: list[dict[str, Any]] = []
    for hero in sorted(view["heroes"], key=lambda item: item["display_name"]):
        short = hero["display_name"]
        p = {
            **hero["analysis"],
            **name_synergies["heroes"][short],
        }
        long_name = p["long_name"]
        analyzed = summary_heroes[long_name]
        behavior = rs.HeroBehavior(**p["behavior"])
        meta = hero["source"]
        skill_summaries = hero["curated"].get("skill_summaries") or {}
        hero_categories = {s["category"] for s in p["skills"].values()}
        prydwen_tiers = legacy._normalize_prydwen_tiers(
            meta.get("prydwen_tiers")
        )
        behavior_md = "\n".join(
            rs.format_behavior_section(
                short,
                behavior,
                skill_summaries=skill_summaries,
                hero_categories=hero_categories,
                include_skill_summaries=False,
                include_stats_overview=False,
                prydwen_tiers=prydwen_tiers,
                hero=analyzed,
                behavior_tags=sorted(
                    hero["curated"].get("behavior_tags") or []
                ),
                play_overview=hero["curated"].get("play_overview"),
                counter_overview=hero["curated"].get("counter_overview"),
            )
        ).strip()
        damage_types = rs._hero_skill_overview_damage_types(behavior, analyzed)
        skill_card_tags_by_category: dict[str, list[str]] = {}
        for skill_data in p.get("skills", {}).values():
            category = skill_data.get("category")
            tags = skill_data.get("skill_card_tags")
            if category and tags is not None:
                skill_card_tags_by_category[category] = tags
        skill_cards = rs.format_skill_cards(
            analyzed,
            skill_summaries,
            hero_categories,
            [],
            source_skills=meta.get("skills", []),
            skill_card_tags_by_category=skill_card_tags_by_category or None,
        )
        summary_md = rs.format_summary(analyzed, short).strip()
        synergy = legacy._build_synergy_sections(
            short,
            p,
            analyzed,
            max_syn,
            max_ben,
            provider_beneficiary_count,
            obvious,
            slug_by_name,
            name_synergies,
        )
        replacements = legacy._build_replacements(
            short, p.get("replacements", {}), max_rep, slug_by_name
        )
        sig_category = rs.signature_skill_category(short, behavior)
        signature_skill = None
        if behavior.signature_skill_name and sig_category:
            signature_skill = {
                "name": behavior.signature_skill_name,
                "category": sig_category,
            }
        stats_overview = hero["curated"].get("stat_ranks")
        sections: dict[str, Any] = {
            "behavior": behavior_md,
            "damageTypes": damage_types,
            "skillCards": skill_cards,
            "benefits_from": synergy,
            "replacements": replacements,
            "summary": summary_md,
        }
        if stats_overview:
            sections["statsOverview"] = stats_overview
        heroes_out.append(
            {
                "name": short,
                "slug": slug_by_name[short],
                "title": meta.get("title", long_name),
                "faction": meta.get("faction"),
                "class": meta.get("class"),
                "roleCategory": p.get("role_category"),
                "damage_type": meta.get("damage_type"),
                "defaultRange": p.get("default_range"),
                "releaseDate": p.get("release_date"),
                "season": p.get("season"),
                "seasonNumber": p.get("season_number"),
                "description": meta.get("description", ""),
                "portrait": f"assets/portraits/{short}.png",
                "signatureSkill": signature_skill,
                "prydwenTiers": prydwen_tiers,
                "sections": sections,
            }
        )
    timestamp = generated_at or datetime.now(timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    return {
        "meta": {
            "generated": timestamp,
            "hero_count": len(heroes_out),
        },
        "heroes": heroes_out,
    }

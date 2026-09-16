"""Format overview Markdown from a resolved presentation model."""

from __future__ import annotations

from typing import Any, Mapping

from character_stat_ranks import stats_overview_for_short

from ..engine import overview, rewrite_summaries


def overview_header(max_synergies: int) -> list[str]:
    return [
        "# Heroes Overview",
        "",
        "Per-hero synergy picks and summaries derived from skill text in",
        "[Heroes.md](Heroes.md). [Heroes.md](Heroes.md) has skills only.",
        "Synergy: stat buff tags under **Units improving X**, and",
        "enabler partners matching **Requires** special effects.",
        f"Up to {max_synergies} partners by combined score. Omitted: "
        "ATK-only, Max HP",
        "buff-only, and Shield-only (unless the hero benefits from shields).",
        "Rare conditional buffs score lower.",
        "Meta tiers from "
        "[Prydwen tier list](https://www.prydwen.gg/afk-journey/tier-list).",
        "Regenerate: `python3 scripts/generate-heroes-overview.py`.",
        "",
    ]


def _display_synergies(hero: Mapping[str, Any]) -> dict[str, Any]:
    stored = hero.get("synergies") or {}
    if stored.get("synergies") and stored["synergies"] and "provider" in (
        stored["synergies"][0] or {}
    ):
        return dict(stored)
    manifest = {
        "heroes": [
            {
                "id": hero["id"],
                "display_name": hero["display_name"],
                "title": hero["source"].get("title") or "",
                "order": 0,
            }
        ]
    }
    # Identity conversion needs the full roster; callers pass converted rows.
    return dict(stored)


def build_overview_markdown(
    view: Mapping[str, Any],
    *,
    summary_heroes: dict[str, Any],
    max_synergies: int,
    max_beneficiaries: int,
    obvious_threshold: int,
    max_replacements: int,
    name_synergies: Mapping[str, Any],
    slug_ranks: Mapping[str, Any],
) -> str:
    rs = rewrite_summaries()
    gen = overview()
    from render_overview import (
        REPLACEMENT_CATEGORY_LABELS,
        _format_replacement_line,
        _format_synergies,
    )

    provider_beneficiary_count = {
        hero["display_name"]: len(
            (hero.get("synergies") or {}).get("beneficiaries") or []
        )
        for hero in view["heroes"]
    }
    parts = overview_header(max_synergies)
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
        syn_lines = _format_synergies(
            short,
            p,
            analyzed,
            max_synergies,
            max_beneficiaries,
            provider_beneficiary_count,
            obvious_threshold,
            dict(name_synergies),
        )
        summary = rs.format_summary(analyzed, short).rstrip()
        parts.append(f"## {short}")
        parts.append("")
        parts.extend(
            rs.format_behavior_section(
                short,
                behavior,
                skill_summaries=skill_summaries,
                hero_categories=hero_categories,
                prydwen_tiers=meta.get("prydwen_tiers"),
                hero=analyzed,
                behavior_tags=sorted(hero["curated"].get("behavior_tags") or []),
                play_overview=hero["curated"].get("play_overview"),
                counter_overview=hero["curated"].get("counter_overview"),
                stats_overview=stats_overview_for_short(short, dict(slug_ranks)),
            )
        )
        parts.append(f"### Units improving {short}")
        parts.append("")
        parts.extend(syn_lines)
        replacements = p.get("replacements", {})
        if isinstance(replacements, dict) and any(replacements.values()):
            parts.append("")
            parts.append(
                f"### Units that can act as a replacement for {short}"
            )
            parts.append("")
            for key in gen.REPLACEMENT_CATEGORY_ORDER:
                label = REPLACEMENT_CATEGORY_LABELS.get(key)
                if not label:
                    continue
                entries = replacements.get(key, [])
                if not entries:
                    continue
                parts.append(f"**{label}**")
                parts.append("")
                for entry in entries[:max_replacements]:
                    parts.append(
                        _format_replacement_line(
                            entry,
                            show_tags=(key != "energy"),
                            show_score=(key != "energy"),
                        )
                    )
                parts.append("")
        parts.append(summary)
        parts.append("")
    return "\n".join(parts).rstrip() + "\n"

#!/usr/bin/env python3
"""Render heroes-overview.md and heroes-overview.csv.

Pure view over ``heroes_data.json`` (identity / damage type),
``heroes_data_processed.json`` (derived effects, behaviour), and
``heroes_data_synergies.json`` (synergies, beneficiaries, replacements).
Rehydrates hero objects from processed JSON; does not re-run skill-text
detection. Display thresholds (top-N synergies / beneficiaries) come from
``heroes_config.json``.
"""

from __future__ import annotations

import csv
import importlib.util
import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import heroes_io as io
import hero_schema as hs

OVERVIEW_MD = io.ROOT / "heroes-overview.md"
OVERVIEW_CSV = io.ROOT / "heroes-overview.csv"


def _receiver_synergies(beneficiary_short: str, synergies: dict) -> list[dict]:
    return synergies["heroes"].get(beneficiary_short, {}).get("synergies", [])


def _format_replacement_line(
    entry: dict,
    *,
    show_tags: bool = True,
    show_score: bool = True,
) -> str:
    if not show_score:
        return f"- {entry['name']}"
    pct = int(entry["score"] * 100)
    match_list = entry.get("matches", [])[:5] if show_tags else []
    tags = " ".join(f"`{tag}`" for tag in match_list)
    if tags:
        return f"- {entry['name']} ({pct}% {tags})"
    return f"- {entry['name']} ({pct}%)"


OVERVIEW_HEADER = [
    "# Heroes Overview",
    "",
    "Per-hero synergy picks and summaries derived from skill text in",
    "[Heroes.md](Heroes.md). [Heroes.md](Heroes.md) has skills only.",
    "Synergy: stat buff tags under **Units improving X**, and",
    "enabler partners matching **Requires** special effects.",
    "Up to five partners by combined score. Omitted: ATK-only, Max HP",
    "buff-only, and Shield-only (unless the hero benefits from shields).",
    "Rare conditional buffs score lower.",
    "Meta tiers from "
    "[Prydwen tier list](https://www.prydwen.gg/afk-journey/tier-list).",
    "Regenerate: `python3 scripts/generate-heroes-overview.py`.",
    "",
]


def _load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


rs = _load_module("rewrite_summaries", "rewrite-summaries.py")
gen = _load_module("gen_overview", "generate-heroes-overview.py")
csv_mod = _load_module("overview_to_csv", "overview-to-csv.py")

REPLACEMENT_CATEGORY_LABELS = {
    "overall": "Best overall replacement",
    **gen.REPLACEMENT_CATEGORY_DISPLAY,
}


def _format_benefit_stat_tags(benefit_stats: list[str]) -> list[str]:
    stats = benefit_stats[:5]
    has_atk_spd = "ATK SPD" in stats
    tags: list[str] = []
    for stat in stats:
        if stat == "Haste" and has_atk_spd:
            continue
        if stat == "ATK SPD":
            tags.append("ATK SPD / Haste")
        else:
            tags.append(stat)
    return tags


def _join_names(names: list[str]) -> str:
    bold = [f"**{name}**" for name in names]
    if len(bold) == 1:
        return bold[0]
    if len(bold) == 2:
        return f"{bold[0]} or {bold[1]}"
    return f"{bold[0]}, {bold[1]}, or {bold[2]}"


def load_summary_heroes(
    data: dict, processed: dict
) -> tuple[dict[str, rs.Hero], dict[str, list]]:
    """Rebuild analyzed heroes from processed JSON (no skill-text detection)."""
    hero_records = data["heroes"]
    data_by_title = {h["title"]: h for h in hero_records}
    skills_by_title = rs.load_skills_by_title_from_records(hero_records)
    summary_heroes: dict[str, rs.Hero] = {}
    for short, p in processed["heroes"].items():
        long_name = p["long_name"]
        meta = data_by_title.get(long_name, {})
        damage_type = meta.get("damage_type", "Physical") or "Physical"
        summary_heroes[long_name] = hs.deserialize_hero(long_name, p, damage_type)
    summary_list = list(summary_heroes.values())
    rs.assign_magnitudes(summary_list, skills_by_title)
    return summary_heroes, skills_by_title


def summary_heroes_by_short(summary_heroes: dict[str, rs.Hero]) -> dict[str, rs.Hero]:
    """Map display short name -> hero for CSV export."""
    return {gen.short_name(title): hero for title, hero in summary_heroes.items()}


def _format_synergies(
    short: str,
    p: dict,
    hero,
    max_syn: int,
    max_ben: int,
    provider_beneficiary_count: dict[str, int],
    obvious_threshold: int,
    synergies: dict,
) -> list[str]:
    lines: list[str] = []
    benefit_stats = [
        hs.to_display_stat(s) for s in p.get("benefit_stats", [])
    ]
    if benefit_stats:
        stat_tags = " ".join(
            f"`{tag}`" for tag in _format_benefit_stat_tags(benefit_stats)
        )
        excluded = gen.common_stat_buffer_names(
            p["synergies"],
            provider_beneficiary_count,
            obvious_threshold,
        )
        look_line = f"Look for units providing: {stat_tags}"
        if excluded:
            look_line += "  "
        lines.append(look_line)
        if excluded:
            lines.append(f"Common buffers are {_join_names(excluded)}.")
        lines.append("")

    requires_lines = gen.format_synergy_requires_markdown(hero, short)
    if requires_lines:
        lines.extend(requires_lines)

    filtered = gen.filter_synergy_picks_for_display(
        p["synergies"],
        provider_beneficiary_count,
        obvious_threshold,
        max_syn,
    )
    picks = filtered
    if picks:
        for pick in picks:
            lines.append(f"- **{gen.short_name(pick['provider'])}**")
            for reason in pick["reasons"]:
                lines.append(f"  - {gen.format_reason_for_display(reason)}")
    else:
        lines.append("_No synergy partners matched stat buffs or enablers._")

    benefited = p["beneficiaries"]
    buffs_intro = rs.format_buffs_provided_intro(hero, short)
    if benefited or buffs_intro:
        lines.append("")
        lines.append(f"### Units benefitting most from {short}")
        lines.append("")
        if buffs_intro:
            lines.append(buffs_intro)
            lines.append("")
        total = len(benefited)
        if benefited and total > max_ben:
            lines.append(
                f"**{total}** units include this provider among their "
                f"top {max_syn} synergy partners. Why the match is common:"
            )
            lines.append("")
            for reason in p["beneficiary_overflow_reasons"]:
                lines.append(f"- {reason}")
            lines.append("")
            lines.append(f"These are the **{max_ben}** strongest pairings: ")
            lines.append("")
            display = benefited[:max_ben]
        elif benefited:
            display = benefited
        else:
            display = []
        if display:
            display = sorted(
                display,
                key=lambda b: (
                    -gen.beneficiary_rating_out_of_five(
                        b["score"],
                        _receiver_synergies(b["name"], synergies),
                    ),
                    b["name"],
                ),
            )
            for b in display:
                receiver_synergies = _receiver_synergies(b["name"], synergies)
                lines.append(
                    f"- {b['name']} ({gen.format_beneficiary_rating_markdown(b['score'], receiver_synergies)})"
                )
    return lines


def build_overview(
    data: dict, processed: dict, synergies: dict, config: dict
) -> tuple[str, dict[str, rs.Hero]]:
    limits = config.get("display_limits", {})
    max_syn = limits.get("max_synergies", 10)
    max_ben = limits.get("max_beneficiaries_display", 10)
    obvious_threshold = limits.get("obvious_provider_threshold", 20)
    rep_scoring = config.get("replacement_scoring", {})
    max_rep = rep_scoring.get("max_replacements", 3)
    provider_beneficiary_count = {
        short: len(s["beneficiaries"])
        for short, s in synergies["heroes"].items()
    }

    data_by_title = {h["title"]: h for h in data["heroes"]}
    parts = list(OVERVIEW_HEADER)

    summary_heroes, _skills_by_title = load_summary_heroes(data, processed)
    behavior_tags_map = gen._load_behavior_tags()
    play_overviews = rs._load_play_overviews()

    for short in sorted(processed["heroes"]):
        p = {
            **processed["heroes"][short],
            **synergies["heroes"][short],
        }
        long_name = p["long_name"]
        hero = summary_heroes[long_name]
        behavior = rs.HeroBehavior(**p["behavior"])
        meta = data_by_title.get(long_name, {})
        skill_summaries = rs._load_skill_summaries().get(short, {})
        hero_categories = {s["category"] for s in p["skills"].values()}

        syn_lines = _format_synergies(
            short,
            p,
            hero,
            max_syn,
            max_ben,
            provider_beneficiary_count,
            obvious_threshold,
            synergies,
        )
        summary = rs.format_summary(hero, short).rstrip()

        parts.append(f"## {short}")
        parts.append("")
        parts.extend(
            rs.format_behavior_section(
                short,
                behavior,
                skill_summaries=skill_summaries,
                hero_categories=hero_categories,
                prydwen_tiers=meta.get("prydwen_tiers"),
                hero=hero,
                behavior_tags=sorted(behavior_tags_map.get(short, ())),
                play_overview=play_overviews.get(short),
            )
        )
        parts.append(f"### Units improving {short}")
        parts.append("")
        parts.extend(syn_lines)
        replacements = p.get("replacements", {})
        if isinstance(replacements, dict) and any(replacements.values()):
            parts.append("")
            parts.append(f"### Units that can act as a replacement for {short}")
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
                for entry in entries[:max_rep]:
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

    return "\n".join(parts).rstrip() + "\n", summary_heroes


def write_csv(
    overview_text: str,
    energy_providers: frozenset[str],
    *,
    analyzed_heroes: dict[str, rs.Hero] | None = None,
) -> int:
    hero_meta = csv_mod._load_hero_faction_class()
    hero_tiers = csv_mod._load_hero_prydwen_tiers()
    hero_roles = csv_mod._load_hero_role_categories()
    rows = csv_mod.convert(
        overview_text,
        energy_providers,
        hero_meta,
        hero_tiers,
        hero_roles,
        analyzed_heroes=analyzed_heroes,
    )
    with OVERVIEW_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(csv_mod.COLUMNS)
        writer.writerows(rows)
    csv_mod.LIST_COLUMNS_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    csv_mod.LIST_COLUMNS_OUTPUT.write_text(
        json.dumps(csv_mod.LIST_COLUMNS, indent=2) + "\n",
        encoding="utf-8",
    )
    return len(rows)


def main() -> None:
    data = io.load_heroes_data()
    processed = io.load_processed()
    synergies = io.load_synergies()
    config = io.load_config()

    content, summary_heroes = build_overview(data, processed, synergies, config)
    OVERVIEW_MD.write_text(content, encoding="utf-8")
    print(
        f"Wrote {OVERVIEW_MD.relative_to(io.ROOT)} ({len(content.splitlines())} lines)"
    )

    energy_providers = frozenset(
        short
        for short, p in processed["heroes"].items()
        if p.get("is_energy_provider")
    )
    n = write_csv(
        content,
        energy_providers,
        analyzed_heroes=summary_heroes_by_short(summary_heroes),
    )
    print(
        f"Wrote {OVERVIEW_CSV.relative_to(io.ROOT)} "
        f"({n} heroes × {len(csv_mod.COLUMNS)} columns)"
    )


if __name__ == "__main__":
    main()

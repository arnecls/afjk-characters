#!/usr/bin/env python3
"""Render heroes-overview.md and heroes-overview.csv.

Pure view over ``heroes_data.json`` (identity / damage type),
``heroes_data_processed.json`` (derived effects, behaviour), and
``heroes_data_synergies.json`` (synergies, beneficiaries, replacements).
No analysis is performed here; display thresholds (top-N synergies /
beneficiaries) come from ``heroes_config.json``.
"""

from __future__ import annotations

import csv
import importlib.util
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import heroes_io as io
import hero_schema as hs

OVERVIEW_MD = io.ROOT / "heroes-overview.md"
OVERVIEW_CSV = io.ROOT / "heroes-overview.csv"

REPLACEMENT_CATEGORY_LABELS = {
    "buff": "Buffs on allies",
    "energy": "Energy provider",
    "similar_skills": "Similar Skills",
    "damage": "Damage",
    "debuff": "Debuffs on enemies",
    "cc": "Crowd Control",
}


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
    "Synergy: stat buff tags under **Units X benefits from**, and",
    "enabler partners matching **Requires** special effects.",
    "Up to five partners by combined score. Omitted: ATK-only, Max HP",
    "buff-only, and Shield-only (unless the hero benefits from Max HP/",
    "shields). Rare conditional buffs score lower.",
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


def _format_synergies(
    short: str,
    p: dict,
    max_syn: int,
    max_ben: int,
    provider_beneficiary_count: dict[str, int],
    obvious_threshold: int,
) -> list[str]:
    lines: list[str] = []
    benefit_stats = [
        hs.to_display_stat(s) for s in p.get("benefit_stats", [])
    ]
    if benefit_stats:
        stat_tags = " ".join(
            f"`{tag}`" for tag in _format_benefit_stat_tags(benefit_stats)
        )
        excluded = [
            gen.short_name(pick["provider"])
            for pick in p["synergies"]
            if provider_beneficiary_count.get(pick["provider"], 0)
            > obvious_threshold
        ][:3]
        look_line = f"Look for units providing: {stat_tags}"
        if excluded:
            look_line += "  "
        lines.append(look_line)
        if excluded:
            lines.append(f"Common buffers are {_join_names(excluded)}.")
        lines.append("")

    filtered = [
        pick
        for pick in p["synergies"]
        if provider_beneficiary_count.get(pick["provider"], 0) <= obvious_threshold
    ]
    picks = filtered[:max_syn]
    if picks:
        for pick in picks:
            lines.append(f"- **{gen.short_name(pick['provider'])}**")
            for reason in pick["reasons"]:
                lines.append(f"  - {gen.format_reason_for_display(reason)}")
    else:
        lines.append("_No synergy partners matched stat buffs or enablers._")

    benefited = p["beneficiaries"]
    if benefited:
        lines.append("")
        lines.append(f"### Units benefitting from {short}")
        lines.append("")
        total = len(benefited)
        if total > max_ben:
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
        else:
            display = benefited
        for b in display:
            lines.append(f"- {b['name']}")
    return lines


def build_overview(
    data: dict, processed: dict, synergies: dict, config: dict
) -> str:
    limits = config.get("display_limits", {})
    max_syn = limits.get("max_synergies", 5)
    max_ben = limits.get("max_beneficiaries_display", 10)
    obvious_threshold = limits.get("obvious_provider_threshold", 20)
    rep_scoring = config.get("replacement_scoring", {})
    max_rep = rep_scoring.get("max_replacements", 3)
    provider_beneficiary_count = {
        title: len(s["beneficiaries"])
        for title, s in synergies["heroes"].items()
    }

    data_by_title = {h["title"]: h for h in data["heroes"]}
    parts = list(OVERVIEW_HEADER)

    heroes_by_title: dict[str, rs.Hero] = {}
    for title in sorted(processed["heroes"]):
        damage_type = data_by_title.get(title, {}).get("damage_type")
        heroes_by_title[title] = hs.deserialize_hero(
            title, processed["heroes"][title], damage_type or ""
        )
    rs.assign_magnitudes(list(heroes_by_title.values()))

    for title in sorted(processed["heroes"]):
        p = {
            **processed["heroes"][title],
            **synergies["heroes"][title],
        }
        short = gen.short_name(title)
        hero = heroes_by_title[title]
        behavior = rs.HeroBehavior(**p["behavior"])

        syn_lines = _format_synergies(
            short,
            p,
            max_syn,
            max_ben,
            provider_beneficiary_count,
            obvious_threshold,
        )
        summary = rs.format_summary(hero, short).rstrip()

        parts.append(f"## {short}")
        parts.append("")
        parts.extend(rs.format_behavior_section(short, behavior))
        parts.append(f"### Units {short} benefits from")
        parts.append("")
        parts.extend(syn_lines)
        replacements = p.get("replacements", {})
        if isinstance(replacements, dict) and any(replacements.values()):
            parts.append("")
            parts.append(f"### Units that can act as a replacement for {short}")
            parts.append("")
            for key, label in REPLACEMENT_CATEGORY_LABELS.items():
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

    return "\n".join(parts).rstrip() + "\n"


def write_csv(overview_text: str, energy_providers: frozenset[str]) -> int:
    rows = csv_mod.convert(overview_text, energy_providers)
    with OVERVIEW_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(csv_mod.COLUMNS)
        writer.writerows(rows)
    return len(rows)


def main() -> None:
    data = io.load_heroes_data()
    processed = io.load_processed()
    synergies = io.load_synergies()
    config = io.load_config()

    content = build_overview(data, processed, synergies, config)
    OVERVIEW_MD.write_text(content, encoding="utf-8")
    print(
        f"Wrote {OVERVIEW_MD.relative_to(io.ROOT)} ({len(content.splitlines())} lines)"
    )

    energy_providers = frozenset(
        gen.short_name(title)
        for title, p in processed["heroes"].items()
        if p.get("is_energy_provider")
    )
    n = write_csv(content, energy_providers)
    print(
        f"Wrote {OVERVIEW_CSV.relative_to(io.ROOT)} "
        f"({n} heroes × {len(csv_mod.COLUMNS)} columns)"
    )


if __name__ == "__main__":
    main()

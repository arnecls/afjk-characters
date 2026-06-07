#!/usr/bin/env python3
"""Render heroes-overview.md and heroes-overview.csv.

Pure view over ``heroes_data.json`` (identity / damage type) and
``heroes_data_processed.json`` (derived effects, behaviour, synergies,
beneficiaries). No analysis is performed here; display thresholds (top-N
synergies / beneficiaries) come from ``heroes_config.json``.
"""

from __future__ import annotations

import csv
import importlib.util
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import heroes_io as io

OVERVIEW_MD = io.ROOT / "heroes-overview.md"
OVERVIEW_CSV = io.ROOT / "heroes-overview.csv"

OVERVIEW_HEADER = [
    "# Heroes Overview",
    "",
    "Per-hero synergy picks and summaries derived from skill text in",
    "[Heroes.md](Heroes.md). [Heroes.md](Heroes.md) has skills only.",
    "Synergy: stat buffs matching **Stats the unit benefits from**, and",
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


def _rebuild_hero(title: str, damage_type: str, p: dict):
    hero = rs.Hero(title=title, damage_type=damage_type or "")
    hero.effects = [rs.Effect(**e) for e in p["effects"]]
    hero.summon_effects = [rs.Effect(**e) for e in p["summon_effects"]]
    hero.cc_immunities = [rs.CcImmunity(**c) for c in p["cc_immunities"]]
    hero.special_effects = [rs.SpecialEffect(**s) for s in p["special_effects"]]
    hero.damage_entries = [tuple(d) for d in p["damage_entries"]]
    hero.damage_magnitudes = p["damage_magnitudes"]
    hero.benefit_stats = p["benefit_stats"]
    return hero


def _format_synergies(short: str, p: dict, max_syn: int, max_ben: int) -> list[str]:
    lines: list[str] = []
    picks = p["synergies"][:max_syn]
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
                f"_**{total}** units include this provider among their "
                f"top {max_syn} synergy partners. Only the "
                f"**{max_ben}** strongest pairings "
                f"are listed below. Why the match is common:_"
            )
            for reason in p["beneficiary_overflow_reasons"]:
                lines.append(f"- {reason}")
            lines.append("")
            display = benefited[:max_ben]
        else:
            display = benefited
        for b in display:
            lines.append(f"- {b['name']}")
    return lines


def build_overview(data: dict, processed: dict, config: dict) -> str:
    limits = config.get("display_limits", {})
    max_syn = limits.get("max_synergies", 5)
    max_ben = limits.get("max_beneficiaries_display", 10)

    data_by_title = {h["title"]: h for h in data["heroes"]}
    parts = list(OVERVIEW_HEADER)

    for title in processed["order"]:
        p = processed["heroes"][title]
        short = gen.short_name(title)
        damage_type = data_by_title.get(title, {}).get("damage_type")
        hero = _rebuild_hero(title, damage_type, p)
        behavior = rs.HeroBehavior(**p["behavior"])

        syn_lines = _format_synergies(short, p, max_syn, max_ben)
        summary = rs.format_summary(hero, short).rstrip()

        parts.append(f"## {short}")
        parts.append("")
        parts.extend(rs.format_behavior_section(short, behavior))
        parts.append(f"### Units {short} benefits from")
        parts.append("")
        parts.extend(syn_lines)
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
    config = io.load_config()

    content = build_overview(data, processed, config)
    OVERVIEW_MD.write_text(content, encoding="utf-8")
    print(
        f"Wrote {OVERVIEW_MD.relative_to(io.ROOT)} ({len(content.splitlines())} lines)"
    )

    energy_providers = frozenset(processed.get("energy_providers", []))
    n = write_csv(content, energy_providers)
    print(
        f"Wrote {OVERVIEW_CSV.relative_to(io.ROOT)} "
        f"({n} heroes × {len(csv_mod.COLUMNS)} columns)"
    )


if __name__ == "__main__":
    main()

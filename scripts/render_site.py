#!/usr/bin/env python3
"""Build site/data/heroes.json for the static hero browser.

Uses the same processed data and formatters as render_overview.py so JSON
content stays in sync with heroes-overview.md.
"""

from __future__ import annotations

import importlib.util
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import hero_schema as hs
import heroes_io as io
from render_overview import (
    REPLACEMENT_CATEGORY_LABELS,
    _format_benefit_stat_tags,
    _format_replacement_line,
    _join_names,
    _load_module,
)

SITE_DIR = io.ROOT / "site"
SITE_DATA = SITE_DIR / "data" / "heroes.json"
OVERVIEW_CSV = io.ROOT / "heroes-overview.csv"
SITE_CSV = SITE_DIR / "data" / "heroes-overview.csv"

rs = _load_module("rewrite_summaries", "rewrite-summaries.py")
gen = _load_module("gen_overview", "generate-heroes-overview.py")


def hero_slug(name: str) -> str:
    """URL slug from a hero display name."""
    slug = name.lower().strip()
    slug = slug.replace("&", "and")
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def _hero_ref(name: str, slug_by_name: dict[str, str]) -> dict[str, str]:
    return {"name": name, "slug": slug_by_name[name]}


def _parse_replacement_detail(line: str, name: str) -> str:
    """Strip leading '- Name (...)' to keep the parenthetical detail."""
    prefix = f"- {name}"
    if line.startswith(prefix):
        rest = line[len(prefix) :].strip()
        if rest.startswith("(") and rest.endswith(")"):
            return rest[1:-1]
        return rest
    return ""


def _build_synergy_sections(
    short: str,
    p: dict,
    max_syn: int,
    max_ben: int,
    provider_beneficiary_count: dict[str, int],
    obvious_threshold: int,
    slug_by_name: dict[str, str],
) -> dict:
    benefit_stats = [hs.to_display_stat(s) for s in p.get("benefit_stats", [])]
    intro_lines: list[str] = []
    common_buffers: list[dict[str, str]] = []

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
        intro_lines.append(f"Look for units providing: {stat_tags}")
        if excluded:
            intro_lines.append(f"Common buffers are {_join_names(excluded)}.")
            common_buffers = [
                _hero_ref(n, slug_by_name) for n in excluded if n in slug_by_name
            ]

    filtered = [
        pick
        for pick in p["synergies"]
        if provider_beneficiary_count.get(pick["provider"], 0) <= obvious_threshold
    ]
    picks = filtered[:max_syn]
    partners: list[dict] = []
    if picks:
        for pick in picks:
            pname = gen.short_name(pick["provider"])
            partners.append(
                {
                    "name": pname,
                    "slug": slug_by_name.get(pname, hero_slug(pname)),
                    "reasons": [
                        gen.format_reason_for_display(r) for r in pick["reasons"]
                    ],
                }
            )

    benefited_by: dict = {"intro": None, "overflow_reasons": [], "heroes": []}
    benefited = p["beneficiaries"]
    if benefited:
        total = len(benefited)
        if total > max_ben:
            benefited_by["intro"] = (
                f"**{total}** units include this provider among their "
                f"top {max_syn} synergy partners. Why the match is common:"
            )
            benefited_by["overflow_reasons"] = list(
                p.get("beneficiary_overflow_reasons", [])
            )
            benefited_by["strongest_note"] = (
                f"These are the **{max_ben}** strongest pairings:"
            )
            display = benefited[:max_ben]
        else:
            display = benefited
        benefited_by["heroes"] = [
            _hero_ref(b["name"], slug_by_name)
            for b in display
            if b["name"] in slug_by_name
        ]

    return {
        "intro": "\n".join(intro_lines) if intro_lines else None,
        "common_buffers": common_buffers,
        "partners": partners,
        "benefited_by": benefited_by if benefited else None,
    }


def _build_replacements(
    short: str,
    replacements: dict,
    max_rep: int,
    slug_by_name: dict[str, str],
) -> list[dict]:
    out: list[dict] = []
    if not isinstance(replacements, dict) or not any(replacements.values()):
        return out
    for key, label in REPLACEMENT_CATEGORY_LABELS.items():
        entries = replacements.get(key, [])
        if not entries:
            continue
        category_entries: list[dict] = []
        for entry in entries[:max_rep]:
            name = entry["name"]
            line = _format_replacement_line(
                entry,
                show_tags=(key != "energy"),
                show_score=(key != "energy"),
            )
            category_entries.append(
                {
                    "name": name,
                    "slug": slug_by_name.get(name, hero_slug(name)),
                    "detail": _parse_replacement_detail(line, name),
                }
            )
        out.append({"category": label, "entries": category_entries})
    return out


def build_site_data(
    data: dict, processed: dict, synergies: dict, config: dict
) -> dict:
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

    slug_by_name: dict[str, str] = {}
    for title in sorted(processed["heroes"]):
        short = gen.short_name(title)
        slug_by_name[short] = hero_slug(short)

    heroes_text = io.reconstruct_heroes_md(data)
    import re

    blocks = [b for b in re.split(r"\n(?=## )", heroes_text) if b.startswith("## ")]
    skills_by_title = rs.load_skills_by_title_from_blocks(blocks)
    summary_heroes: dict[str, rs.Hero] = {}
    for block in blocks:
        hero = rs.parse_hero_block(block)
        rs.analyze_hero(hero)
        summary_heroes[hero.title] = hero
    rs.assign_magnitudes(list(summary_heroes.values()), skills_by_title)

    heroes_out: list[dict] = []
    for title in sorted(processed["heroes"]):
        p = {
            **processed["heroes"][title],
            **synergies["heroes"][title],
        }
        short = gen.short_name(title)
        hero = summary_heroes[title]
        behavior = rs.HeroBehavior(**p["behavior"])
        meta = data_by_title.get(title, {})

        skill_summaries = rs._load_skill_summaries().get(short, {})
        hero_categories = {s["category"] for s in p["skills"].values()}
        hero_skills = skills_by_title.get(title, [])
        prydwen_tiers = meta.get("prydwen_tiers")
        behavior_md = "\n".join(
            rs.format_behavior_section(
                short,
                behavior,
                skill_summaries=skill_summaries,
                hero_categories=hero_categories,
                include_skill_summaries=False,
                prydwen_tiers=prydwen_tiers,
            )
        ).strip()
        skill_cards = rs.format_skill_cards(
            hero,
            skill_summaries,
            hero_categories,
            hero_skills,
        )
        summary_md = rs.format_summary(hero, short).strip()
        synergy = _build_synergy_sections(
            short,
            p,
            max_syn,
            max_ben,
            provider_beneficiary_count,
            obvious_threshold,
            slug_by_name,
        )
        replacements = _build_replacements(
            short, p.get("replacements", {}), max_rep, slug_by_name
        )
        sig_category = rs.signature_skill_category(short, behavior)
        signature_skill = None
        if behavior.signature_skill_name and sig_category:
            signature_skill = {
                "name": behavior.signature_skill_name,
                "category": sig_category,
            }

        heroes_out.append(
            {
                "name": short,
                "slug": slug_by_name[short],
                "title": meta.get("title", title),
                "faction": meta.get("faction"),
                "class": meta.get("class"),
                "damage_type": meta.get("damage_type"),
                "description": meta.get("description", ""),
                "portrait": f"assets/portraits/{short}.png",
                "signatureSkill": signature_skill,
                "prydwenTiers": prydwen_tiers,
                "sections": {
                    "behavior": behavior_md,
                    "skillCards": skill_cards,
                    "benefits_from": synergy,
                    "replacements": replacements,
                    "summary": summary_md,
                },
            }
        )

    return {
        "meta": {
            "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "hero_count": len(heroes_out),
        },
        "heroes": heroes_out,
    }


def main() -> None:
    data = io.load_heroes_data()
    processed = io.load_processed()
    synergies = io.load_synergies()
    config = io.load_config()

    payload = build_site_data(data, processed, synergies, config)
    encoded = json.dumps(payload, ensure_ascii=False)
    SITE_DATA.parent.mkdir(parents=True, exist_ok=True)
    SITE_DATA.write_text(encoded + "\n", encoding="utf-8")
    print(
        f"Wrote {SITE_DATA.relative_to(io.ROOT)} "
        f"({payload['meta']['hero_count']} heroes)"
    )

    if OVERVIEW_CSV.is_file():
        csv_text = OVERVIEW_CSV.read_text(encoding="utf-8")
        SITE_CSV.write_text(csv_text, encoding="utf-8")
        print(f"Wrote {SITE_CSV.relative_to(io.ROOT)}")
    else:
        print(
            f"Warning: {OVERVIEW_CSV.name} missing; "
            "run render-overview before render-site"
        )


if __name__ == "__main__":
    main()

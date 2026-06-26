#!/usr/bin/env python3
"""Build site/data/heroes.json for the static hero browser.

Uses the same processed data and formatters as render_overview.py so JSON
content stays in sync with heroes-overview.md. Rehydrates hero objects from
processed JSON; does not re-run skill-text detection.
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
    _receiver_synergies,
    load_summary_heroes,
)

SITE_DIR = io.ROOT / "site"
SITE_DATA = SITE_DIR / "data" / "heroes.json"
MIX_SYNERGY_INDEX = SITE_DIR / "data" / "mix-synergy-index.json"
MIX_CONFIG = SITE_DIR / "data" / "mix-config.json"
MIX_ROLE_PROMINENCE = SITE_DIR / "data" / "mix-role-prominence.json"
OVERVIEW_CSV = io.ROOT / "heroes-overview.csv"
SITE_CSV = SITE_DIR / "data" / "heroes-overview.csv"

rs = _load_module("rewrite_summaries", "rewrite-summaries.py")
gen = _load_module("gen_overview", "generate-heroes-overview.py")

_PRYDWEN_TIER_KEYS = (
    "afk_stages",
    "dream_realm",
    "dream_realm_endless",
    "pvp",
)


def _normalize_prydwen_tiers(tiers: dict | None) -> dict[str, str]:
    """Ensure all Prydwen modes are present; missing ratings become ``?``."""
    out: dict[str, str] = {}
    source = tiers or {}
    for key in _PRYDWEN_TIER_KEYS:
        value = source.get(key)
        if value is None:
            out[key] = "?"
            continue
        text = str(value).strip()
        out[key] = text if text else "?"
    return out


def hero_slug(name: str) -> str:
    """URL slug from a hero display name."""
    slug = name.lower().strip()
    slug = slug.replace("&", "and")
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def _hero_ref(name: str, slug_by_name: dict[str, str]) -> dict[str, str]:
    return {"name": name, "slug": slug_by_name[name]}


def _provider_synergy_reasons(
    beneficiary_short: str,
    provider_short: str,
    synergies: dict,
) -> list[str]:
    """Why *beneficiary_short* pairs with *provider_short* (receiver view)."""
    for pick in _receiver_synergies(beneficiary_short, synergies):
        if pick.get("provider") == provider_short:
            return [
                gen.format_reason_for_display(r)
                for r in pick.get("reasons", [])
            ]
    return []


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
    hero,
    max_syn: int,
    max_ben: int,
    provider_beneficiary_count: dict[str, int],
    obvious_threshold: int,
    slug_by_name: dict[str, str],
    synergies: dict,
) -> dict:
    benefit_stats = [hs.to_display_stat(s) for s in p.get("benefit_stats", [])]
    intro_lines: list[str] = []
    common_buffers: list[dict[str, str]] = []

    if benefit_stats:
        stat_tags = " ".join(
            f"`{tag}`" for tag in _format_benefit_stat_tags(benefit_stats)
        )
        excluded = gen.common_stat_buffer_names(
            p["synergies"],
            provider_beneficiary_count,
            obvious_threshold,
        )
        intro_lines.append(f"Look for units providing: {stat_tags}")
        if excluded:
            intro_lines.append(f"Common buffers are {_join_names(excluded)}.")
            common_buffers = [
                _hero_ref(n, slug_by_name) for n in excluded if n in slug_by_name
            ]

    ranked = gen.rank_synergy_picks_for_display(
        p["synergies"],
        provider_beneficiary_count,
        obvious_threshold,
    )
    picks = ranked[:max_syn]
    overflow_picks = ranked[max_syn:]
    receiver_synergies = _receiver_synergies(short, synergies)
    partners: list[dict] = []
    if picks:
        for pick in picks:
            pname = gen.short_name(pick["provider"])
            score = pick["score"]
            partners.append(
                {
                    "name": pname,
                    "slug": slug_by_name.get(pname, hero_slug(pname)),
                    "reasons": [
                        gen.format_reason_for_display(r) for r in pick["reasons"]
                    ],
                    "score": score,
                    "scoreRating": gen.beneficiary_rating_out_of_five(
                        score, receiver_synergies
                    ),
                    "scoreDisplay": gen.format_beneficiary_rating_display(
                        score, receiver_synergies
                    ),
                }
            )
        partners.sort(key=lambda partner: (-partner["scoreRating"], partner["name"]))

    more_partners: list[dict] = []
    for pick in overflow_picks:
        pname = gen.short_name(pick["provider"])
        score = pick["score"]
        more_partners.append(
            {
                "name": pname,
                "slug": slug_by_name.get(pname, hero_slug(pname)),
                "score": score,
                "scoreRating": gen.beneficiary_rating_out_of_five(
                    score, receiver_synergies
                ),
            }
        )
    more_partners.sort(
        key=lambda ref: (-ref["scoreRating"], ref["name"].lower())
    )

    benefited_by: dict = {
        "buffs_provided": rs.format_buffs_provided_data(hero, short),
        "intro": None,
        "overflow_reasons": [],
        "heroes": [],
    }
    benefited = p["beneficiaries"]
    if benefited or benefited_by["buffs_provided"]:
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
        benefited_by["heroes"] = []
        for b in display:
            if b["name"] not in slug_by_name:
                continue
            receiver_synergies = _receiver_synergies(b["name"], synergies)
            rating = gen.beneficiary_rating_out_of_five(
                b["score"], receiver_synergies
            )
            benefited_by["heroes"].append(
                {
                    **_hero_ref(b["name"], slug_by_name),
                    "score": b["score"],
                    "scoreRating": rating,
                    "scoreDisplay": gen.format_beneficiary_rating_display(
                        b["score"], receiver_synergies
                    ),
                    "reasons": _provider_synergy_reasons(
                        b["name"], short, synergies
                    ),
                }
            )
        benefited_by["heroes"].sort(
            key=lambda hero: (-hero["scoreRating"], hero["name"])
        )

    return {
        "intro": "\n".join(intro_lines) if intro_lines else None,
        "requires": gen.format_synergy_requires_json(hero, short),
        "common_buffers": common_buffers,
        "partners": partners,
        "more_partners": more_partners,
        "benefited_by": benefited_by
        if (benefited or benefited_by["buffs_provided"])
        else None,
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
    for key in gen.REPLACEMENT_CATEGORY_ORDER:
        label = REPLACEMENT_CATEGORY_LABELS.get(key)
        if not label:
            continue
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


def build_mix_synergy_index(
    synergies: dict, slug_by_name: dict[str, str]
) -> dict:
    """Provider scores keyed by receiver slug then provider slug."""
    by_receiver: dict[str, dict[str, float]] = {}
    for receiver_short, hero_data in synergies["heroes"].items():
        receiver_slug = slug_by_name.get(receiver_short, hero_slug(receiver_short))
        providers: dict[str, float] = {}
        for pick in hero_data.get("synergies", []):
            provider_name = gen.short_name(pick["provider"])
            provider_slug = slug_by_name.get(provider_name, hero_slug(provider_name))
            providers[provider_slug] = round(float(pick["score"]), 4)
        if providers:
            by_receiver[receiver_slug] = providers
    return {"byReceiver": by_receiver}


def build_mix_config(config: dict) -> dict:
    """Subset of heroes_config.json for mix-mode scoring in the browser."""
    mix = config.get("mix_mode", {})
    synergy = config.get("synergy_weights", {})
    return {
        "factionBonus": mix.get("faction_bonus", 3.0),
        "focusTags": mix.get("focus_tags", {}),
        "ccTargetingWeight": mix.get(
            "cc_targeting_weight",
            synergy.get("targeting_weight", {}),
        ),
        "roleProminenceTierWeight": mix.get("role_prominence_tier_weight", 7),
        "markSynergyMultiplier": mix.get("mark_synergy_multiplier", 2.0),
    }


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
        short: len(s["beneficiaries"])
        for short, s in synergies["heroes"].items()
    }

    data_by_title = {h["title"]: h for h in data["heroes"]}

    slug_by_name: dict[str, str] = {}
    for short in sorted(processed["heroes"]):
        slug_by_name[short] = hero_slug(short)

    summary_heroes, skills_by_title = load_summary_heroes(data, processed)

    heroes_out: list[dict] = []
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
        hero_skills = skills_by_title.get(long_name, [])
        prydwen_tiers = _normalize_prydwen_tiers(meta.get("prydwen_tiers"))
        behavior_md = "\n".join(
            rs.format_behavior_section(
                short,
                behavior,
                skill_summaries=skill_summaries,
                hero_categories=hero_categories,
                include_skill_summaries=False,
                prydwen_tiers=prydwen_tiers,
                hero=hero,
                behavior_tags=sorted(behavior_tags_map.get(short, ())),
                play_overview=play_overviews.get(short),
            )
        ).strip()
        damage_types = rs._hero_skill_overview_damage_types(behavior, hero)
        skill_card_tags_by_category: dict[str, list[str]] = {}
        for skill_data in p.get("skills", {}).values():
            category = skill_data.get("category")
            tags = skill_data.get("skill_card_tags")
            if category and tags is not None:
                skill_card_tags_by_category[category] = tags
        skill_cards = rs.format_skill_cards(
            hero,
            skill_summaries,
            hero_categories,
            hero_skills,
            source_skills=meta.get("skills", []),
            skill_card_tags_by_category=skill_card_tags_by_category or None,
        )
        summary_md = rs.format_summary(hero, short).strip()
        synergy = _build_synergy_sections(
            short,
            p,
            hero,
            max_syn,
            max_ben,
            provider_beneficiary_count,
            obvious_threshold,
            slug_by_name,
            synergies,
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
                "title": meta.get("title", long_name),
                "faction": meta.get("faction"),
                "class": meta.get("class"),
                "roleCategory": p.get("role_category"),
                "damage_type": meta.get("damage_type"),
                "description": meta.get("description", ""),
                "portrait": f"assets/portraits/{short}.png",
                "signatureSkill": signature_skill,
                "prydwenTiers": prydwen_tiers,
                "sections": {
                    "behavior": behavior_md,
                    "damageTypes": damage_types,
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

    slug_by_name: dict[str, str] = {}
    for short in sorted(processed["heroes"]):
        slug_by_name[short] = hero_slug(short)

    summary_heroes, skills_by_title = load_summary_heroes(data, processed)
    mix_role_prominence = gen.build_mix_role_prominence_index(
        summary_heroes, skills_by_title, slug_by_name
    )

    payload = build_site_data(data, processed, synergies, config)
    mix_index = build_mix_synergy_index(synergies, slug_by_name)
    mix_config = build_mix_config(config)

    encoded = json.dumps(payload, ensure_ascii=False)
    SITE_DATA.parent.mkdir(parents=True, exist_ok=True)
    SITE_DATA.write_text(encoded + "\n", encoding="utf-8")
    print(
        f"Wrote {SITE_DATA.relative_to(io.ROOT)} "
        f"({payload['meta']['hero_count']} heroes)"
    )

    MIX_SYNERGY_INDEX.write_text(
        json.dumps(mix_index, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {MIX_SYNERGY_INDEX.relative_to(io.ROOT)}")

    MIX_CONFIG.write_text(
        json.dumps(mix_config, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {MIX_CONFIG.relative_to(io.ROOT)}")

    MIX_ROLE_PROMINENCE.write_text(
        json.dumps(mix_role_prominence, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {MIX_ROLE_PROMINENCE.relative_to(io.ROOT)}")

    if OVERVIEW_CSV.is_file():
        csv_text = OVERVIEW_CSV.read_text(encoding="utf-8")
        SITE_CSV.write_text(csv_text, encoding="utf-8")
        print(f"Wrote {SITE_CSV.relative_to(io.ROOT)}")
        list_columns_src = io.ROOT / "site" / "data" / "list-columns.json"
        list_columns_dst = SITE_DIR / "data" / "list-columns.json"
        if list_columns_src.is_file():
            list_columns_dst.write_text(
                list_columns_src.read_text(encoding="utf-8"),
                encoding="utf-8",
            )
            print(f"Wrote {list_columns_dst.relative_to(io.ROOT)}")
    else:
        print(
            f"Warning: {OVERVIEW_CSV.name} missing; "
            "run render-overview before render-site"
        )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Audit skill-card tags for missing targeting suffixes or chip-render gaps."""

from __future__ import annotations

import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

import heroes_io as io
from test_helpers import tag_labels

TIER_SUFFIX_RE = re.compile(
    r"\s*\((Legendary\+|Mythic\+|Supreme\+|EX\+\d+)\)\s*$",
    re.I,
)
TARGETING_BEFORE_TIER_RE = re.compile(
    r"\s*(?:—|–)\s*"
    r"(All units|Area|Arc|Multiple targets|Single target|path|Self|Summons|Owned)"
    r"\s*\(",
    re.I,
)


def _load_rs():
    spec = importlib.util.spec_from_file_location(
        "rewrite_summaries", SCRIPTS / "rewrite-summaries.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["rewrite_summaries"] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def _parse_targeting_from_tag(label: str) -> str:
    work = label.strip()
    tier_match = TIER_SUFFIX_RE.search(work)
    if tier_match:
        work = work[: tier_match.start()].strip()
    match = re.search(
        r"\s*(?:—|–)\s*"
        r"(All units|Area|Arc|Multiple targets|Single target|path|Self|Summons|Owned)\s*$",
        work,
        re.I,
    )
    return match.group(1).strip() if match else ""


def audit_live_tags(rs_mod) -> list[str]:
    issues: list[str] = []
    data = io.load_heroes_data()
    for record in data["heroes"]:
        hero = rs_mod.hero_from_record(record)
        rs_mod.analyze_hero(hero)
        title = hero.title.split(" - ")[0]
        for category in ("ultimate", "skill1", "skill2", "skill3", "skill4", "skill5"):
            section = rs_mod.CATEGORY_TO_SECTION.get(category)
            sl = hero.skill_slices.get(section)
            if not sl:
                continue
            disambiguate_groups, disambiguate_labels = rs_mod._skill_card_disambiguate_keys(
                sl
            )
            live = tag_labels(rs_mod.format_skill_card_tags(hero, category))
            for effect in sl.effects:
                if effect.category not in ("buff", "debuff", "cc"):
                    continue
                targeting = rs_mod._skill_card_targeting_label(effect)
                if targeting in ("Single target", ""):
                    continue
                expected = rs_mod._skill_card_tag_with_tier(
                    effect.label,
                    targeting,
                    effect.tier,
                    category,
                    is_cc=effect.category == "cc",
                    explicit_targeting=rs_mod._skill_card_use_explicit_targeting(
                        effect,
                        category=effect.category,
                        group_keys=disambiguate_groups,
                        label_keys=disambiguate_labels,
                    ),
                )
                if expected in live:
                    continue
                related = [
                    tag
                    for tag in live
                    if rs_mod._skill_card_tag_label(effect.label) in tag
                ]
                if related and any(
                    targeting.lower() in tag.lower()
                    or (targeting == "path" and "path" in tag.lower())
                    for tag in related
                ):
                    continue
                issues.append(
                    f"{title}/{category}: {effect.label} wants {targeting}, "
                    f"have {related}"
                )
    return issues


def audit_stored_tags_with_suffix() -> list[str]:
    """Tags with — Targeting (Tier) that fail tier-first targeting parse."""
    issues: list[str] = []
    heroes = json.loads((ROOT / "site" / "data" / "heroes.json").read_text())
    for hero in heroes.get("heroes", []):
        slug = hero.get("slug", "")
        for card in hero.get("sections", {}).get("skillCards", []):
            for tag in card.get("tags", []):
                label = tag.get("label") if isinstance(tag, dict) else tag
                if not label or not TARGETING_BEFORE_TIER_RE.search(label):
                    continue
                if not _parse_targeting_from_tag(label):
                    issues.append(f"{slug}/{card.get('label')}: {label}")
    return issues


def main() -> int:
    rs_mod = _load_rs()
    live_issues = audit_live_tags(rs_mod)
    stored_issues = audit_stored_tags_with_suffix()
    chip_proc = subprocess.run(
        ["node", str(SCRIPTS / "test_skill_card_chips.js")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    failed = False
    if live_issues:
        failed = True
        print(f"live tag mismatches: {len(live_issues)}")
        for line in live_issues[:20]:
            print(" ", line)
    if stored_issues:
        failed = True
        print(f"stored tags with tier-after-targeting parse gap: {len(stored_issues)}")
        for line in stored_issues[:20]:
            print(" ", line)
    if chip_proc.returncode != 0:
        failed = True
        print(chip_proc.stdout)
        print(chip_proc.stderr, file=sys.stderr)
    if failed:
        return 1
    print("OK: skill-card targeting audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

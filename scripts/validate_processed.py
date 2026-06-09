#!/usr/bin/env python3
"""Validate heroes_data_processed.json against Heroes.md skill text.

Assumes a fully ascended roster: numeric checks compare processed values to
the strongest parseable number across all skill levels and ascension tiers,
not base unlock values.

Checks:
- Heroes.md matches reconstruct_heroes_md(heroes_data.json)
- Re-analysis output matches committed processed JSON
- JSON Schema validation
- Semantic issues: passive_only misuse, wiki markup, (scaled) gaps, CC gaps
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

import hero_schema as hs
import heroes_io as io

HEROES_MD = ROOT / "Heroes.md"
PROCESSED = io.HEROES_DATA_PROCESSED

_CC_KEYWORDS: dict[str, str] = {
    "stun": r"\bstun(?:s|ned|ning)?\b",
    "knock_back": r"\bknock(?:s|ing)? (?:them |the enemy |enemies )?back\b",
    "silence": r"(?<! of )silenc(?:e|es|ed|ing)",
    "blind": r"\bblind(?:ing|s|ed)?\b",
    "bind": r"\bbind(?:ing|s)?\b",
    "pin": r"\bimmobiliz",
    "freeze": r"\bfreez(?:e|es|ed|ing)\b",
}


def _load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def _rebuild_processed() -> dict[str, Any]:
    rs = _load_module("rewrite_summaries", "rewrite-summaries.py")
    gen = _load_module("gen_overview", "generate-heroes-overview.py")
    from process_heroes import build_processed

    data = io.load_heroes_data()
    return build_processed(data)


def check_md_parity() -> list[str]:
    data = io.load_heroes_data()
    recon = io.reconstruct_heroes_md(data)
    md = HEROES_MD.read_text(encoding="utf-8")
    if md == recon:
        return []
    md_blocks = [b for b in re.split(r"\n(?=## )", md) if b.startswith("## ")]
    recon_blocks = [
        b for b in re.split(r"\n(?=## )", recon) if b.startswith("## ")
    ]
    errors = []
    md_titles = {b.split("\n", 1)[0][3:].strip() for b in md_blocks}
    recon_titles = {b.split("\n", 1)[0][3:].strip() for b in recon_blocks}
    for title in sorted(md_titles ^ recon_titles):
        errors.append(f"hero roster mismatch: {title}")
    for title in sorted(md_titles & recon_titles):
        mb = next(b for b in md_blocks if b.startswith(f"## {title}"))
        rb = next(b for b in recon_blocks if b.startswith(f"## {title}"))
        if mb != rb:
            errors.append(f"Heroes.md block differs from heroes_data: {title}")
    return errors


def check_reanalysis_parity(stored: dict[str, Any], fresh: dict[str, Any]) -> list[str]:
    if stored == fresh:
        return []
    errors = []
    for title in sorted(set(stored["heroes"]) | set(fresh["heroes"])):
        if stored["heroes"].get(title) != fresh["heroes"].get(title):
            errors.append(f"processed drift: {title}")
    return errors[:20]


def _cc_types(effects: list[dict[str, Any]]) -> set[str]:
    out: set[str] = set()
    for eff in effects:
        if eff.get("type") == "crowd_control":
            cc = eff.get("cc-type")
            if cc:
                out.add(cc)
    return out


def check_semantic(processed: dict[str, Any]) -> dict[str, list[str]]:
    issues: dict[str, list[str]] = defaultdict(list)
    wiki_re = re.compile(r"\[[^\]]+\][^\[]+\[/\]")

    for title, hero in processed["heroes"].items():
        for skill_name, skill in hero.get("skills", {}).items():
            desc = skill.get("description", "")
            effects = skill.get("effects", [])
            passive = skill.get("passive_only", False)

            if wiki_re.search(desc):
                issues["wiki_markup"].append(f"{title} / {skill_name}")

            if "(scaled)" in desc.lower():
                issues["scaled_placeholder"].append(f"{title} / {skill_name}")

            if passive and effects:
                issues["passive_only_with_effects"].append(
                    f"{title} / {skill_name}"
                )
            if not passive and not effects:
                issues["empty_effects"].append(f"{title} / {skill_name}")

            if hs._is_placeholder_schema_effect(effects[0]) if len(effects) == 1 else False:
                issues["placeholder_damage"].append(f"{title} / {skill_name}")

            text = desc.lower()
            for cc, pat in _CC_KEYWORDS.items():
                if re.search(pat, text):
                    mapped = "move" if cc == "knock_back" else cc
                    if mapped not in _cc_types(effects):
                        issues["cc_missing"].append(
                            f"{title} / {skill_name}: {cc}"
                        )

            for eff in effects:
                if eff.get("name") == "Marked target (focus fire)":
                    val = hs._numeric_from_value(eff.get("value"))
                    if val is not None and val < 10:
                        issues["duration_as_debuff"].append(
                            f"{title} / {skill_name}: marked={val}"
                        )

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--fail-on",
        nargs="*",
        default=["md_parity", "reanalysis", "schema", "semantic"],
        help="Check groups that cause a non-zero exit when failing",
    )
    parser.add_argument(
        "--max-semantic",
        type=int,
        default=0,
        help="Max semantic issues per category before exit 1 (0 = report only)",
    )
    args = parser.parse_args()
    fail_on = set(args.fail_on)

    errors: list[str] = []
    warnings: dict[str, list[str]] = {}

    if "md_parity" in fail_on:
        md_errors = check_md_parity()
        if md_errors:
            errors.extend(md_errors)
        else:
            print("OK: Heroes.md matches heroes_data.json")
    else:
        md_errors = check_md_parity()
        print(
            f"info: Heroes.md parity — {len(md_errors)} issue(s)"
            if md_errors
            else "OK: Heroes.md matches heroes_data.json"
        )

    stored = json.loads(PROCESSED.read_text(encoding="utf-8"))
    fresh = _rebuild_processed()

    if "reanalysis" in fail_on:
        drift = check_reanalysis_parity(stored, fresh)
        if drift:
            errors.extend(drift)
        else:
            print("OK: processed JSON matches re-analysis")
    else:
        drift = check_reanalysis_parity(stored, fresh)
        print(
            f"info: re-analysis drift — {len(drift)} hero(s)"
            if drift
            else "OK: processed JSON matches re-analysis"
        )

    if "schema" in fail_on:
        try:
            hs.validate_processed(stored)
            print("OK: schema validation")
        except Exception as exc:
            errors.append(f"schema validation failed: {exc}")
    else:
        try:
            hs.validate_processed(stored)
            print("OK: schema validation")
        except Exception as exc:
            print(f"warn: schema validation: {exc}")

    semantic = check_semantic(stored)
    warnings = dict(semantic)
    for category, items in sorted(semantic.items()):
        print(f"semantic [{category}]: {len(items)}")
        for item in items[:5]:
            print(f"  - {item}")
        if len(items) > 5:
            print(f"  ... and {len(items) - 5} more")

    if "semantic" in fail_on and args.max_semantic >= 0:
        for category, items in semantic.items():
            if args.max_semantic == 0:
                continue
            if len(items) > args.max_semantic:
                errors.append(
                    f"semantic {category}: {len(items)} > {args.max_semantic}"
                )

    if errors:
        print("\nFAILED:", file=sys.stderr)
        for err in errors:
            print(f"  {err}", file=sys.stderr)
        return 1

    print("\nValidation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

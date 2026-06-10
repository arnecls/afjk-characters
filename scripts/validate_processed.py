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
SKILL_SUMMARY = ROOT / "data" / "heroes_data_skill_summary.json"
SKILL_SUMMARY_SCHEMA = ROOT / "data" / "schema" / "skill_summary.schema.json"

_CC_KEYWORDS: dict[str, str] = {
    "stun": r"\bstun(?:s|ned|ning)?\b",
    "knock_back": (
        r"\bknock(?:s|ing)? (?:them |the enemy |enemies )?(?:\d+ tiles? )?back\b"
    ),
    "knock_down": r"\bknock(?:s|ing)? (?:the enemy|an enemy|them) down\b",
    "knock_up": r"\bknock(?:s|ing)? .{0,25}?(?:in(?:to)?) the air\b",
    "frighten": r"\bfrighten(?:ing|ed|s)?\b",
    "silence": r"(?<! of )silenc(?:e|es|ed|ing)",
    "charm": r"\bcharm(?:ed|s|ing)?\b",
    "sleep": r"\b(?:asleep|hypnotiz)",
    "displace": r"\b(?:pull(?:ing|s)? (?:in |them|the)|teleport)\b",
    "interrupt": r"\binterrupt\b",
    "taunt": r"\btaunt\b",
    "blind": r"\bblind(?:ing|s|ed)?\b",
    "bind": r"\b(?:bind(?:ing|s)?|immobiliz|entangl|imprison)\b",
    "freeze": r"\bfreez(?:e|es|ed|ing) (?!time itself)(?!and defeats)\b",
}

_CC_SCHEMA_MAP: dict[str, str] = {
    "freeze": "bind",
}

_ANTI_CC_KEYWORDS: dict[str, str] = {
    "unaffected": (
        r"(?:becomes?|is|remain|making|grants?|granted|linked).{0,60}unaffected|"
        r"unaffected (?:while|when|for|during)"
    ),
    "steadfast": r"(?:becomes?|is|grants?|granted).{0,40}steadfast",
    "immune": r"\bimmune to (?:damage and )?control\b",
    "untargetable": (
        r"(?:becomes?|is|making|grants?|granted).{0,60}untargetable|"
        r"cannot be targeted by enemies"
    ),
    "cleanse": r"removes? all dispellable debuffs",
}

_UNTARGETABLE_SKIP_RE = re.compile(
    r"defeated or becomes? untargetable|"
    r"if (?:the |that )?enemy becomes? untargetable|"
    r"first enemy affected.{0,60}becomes? untargetable|"
    r"marked enemy is defeated or becomes? untargetable|"
    r"(?:stitchy|shadow).{0,40}cannot be targeted"
)

_FREEZE_SKIP_RE = re.compile(
    r"freez(?:e|es|ing|ed) (?:time itself|and defeats)"
)


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


def _immunity_types(effects: list[dict[str, Any]]) -> set[str]:
    out: set[str] = set()
    for eff in effects:
        if eff.get("type") == "immunity":
            imm = eff.get("immunity_type")
            if imm:
                out.add(imm)
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
            cc_found = _cc_types(effects)
            if not passive:
                for cc, pat in _CC_KEYWORDS.items():
                    if cc == "freeze" and _FREEZE_SKIP_RE.search(text):
                        continue
                    if cc == "displace" and re.search(
                        r"pull(?:s|ing)? (?:the |a )?"
                        r"(?:rearmost|weakest|nearest|frontmost)? ?ally\b",
                        text,
                    ):
                        continue
                    if not re.search(pat, text):
                        continue
                    mapped = _CC_SCHEMA_MAP.get(cc, cc)
                    if mapped not in cc_found:
                        issues["cc_missing"].append(
                            f"{title} / {skill_name}: {cc}"
                        )

            imm_found = _immunity_types(effects)
            for imm, pat in _ANTI_CC_KEYWORDS.items():
                if imm == "unaffected" and re.search(
                    r"(?:who are|if they are|enemies who are|unaffected enemies|"
                    r"ineffective against) unaffected",
                    text,
                ):
                    continue
                if imm == "untargetable" and _UNTARGETABLE_SKIP_RE.search(text):
                    continue
                if re.search(pat, text) and imm not in imm_found:
                    issues["anti_cc_missing"].append(
                        f"{title} / {skill_name}: {imm}"
                    )

            for eff in effects:
                if eff.get("name") == "Marked target (focus fire)":
                    val = hs._numeric_from_value(eff.get("value"))
                    if val is not None and val < 10:
                        issues["duration_as_debuff"].append(
                            f"{title} / {skill_name}: marked={val}"
                        )

    return issues


def check_skill_summaries(processed: dict[str, Any]) -> list[str]:
    """Validate heroes_data_skill_summary.json coverage and basic lint."""
    errors: list[str] = []
    gen = _load_module("gen_overview", "generate-heroes-overview.py")

    if not SKILL_SUMMARY.exists():
        errors.append("missing heroes_data_skill_summary.json")
        return errors

    try:
        summaries = json.loads(SKILL_SUMMARY.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"skill summary JSON parse error: {exc}"]

    if jsonschema_available():
        try:
            schema = json.loads(SKILL_SUMMARY_SCHEMA.read_text(encoding="utf-8"))
            import jsonschema

            # Pre-load all sibling schema files into the resolver's store
            # so relative $ref URIs are served locally instead of over
            # the network (all schema $ids use the afkj.local fake host).
            store: dict[str, object] = {}
            for sibling in SKILL_SUMMARY_SCHEMA.parent.glob("*.schema.json"):
                sibling_schema = json.loads(sibling.read_text(encoding="utf-8"))
                sid = sibling_schema.get("$id")
                if sid:
                    store[sid] = sibling_schema
            schema_dir = SKILL_SUMMARY_SCHEMA.parent.resolve().as_uri() + "/"
            resolver = jsonschema.RefResolver(schema_dir, schema, store=store)
            jsonschema.validate(summaries, schema, resolver=resolver)
        except Exception as exc:
            errors.append(f"skill summary schema validation failed: {exc}")

    expected: dict[str, set[str]] = {}
    skill_names: dict[str, dict[str, str]] = {}
    for title, hero in processed["heroes"].items():
        short = gen.short_name(title)
        categories = {s["category"] for s in hero["skills"].values()}
        expected[short] = categories
        skill_names[short] = {
            s["category"]: name for name, s in hero["skills"].items()
        }

    for short, categories in sorted(expected.items()):
        hero_summaries = summaries.get(short)
        if not hero_summaries:
            errors.append(f"skill summary missing hero: {short}")
            continue
        for category in categories:
            if category not in hero_summaries:
                errors.append(
                    f"skill summary missing {short} / {category}"
                )
        extra = set(hero_summaries) - categories
        for category in sorted(extra):
            errors.append(
                f"skill summary extra category {short} / {category}"
            )

    for short, hero_summaries in summaries.items():
        if short not in expected:
            errors.append(f"skill summary unknown hero: {short}")
            continue
        for category, text in hero_summaries.items():
            if not isinstance(text, str) or not text.strip():
                errors.append(f"skill summary empty {short} / {category}")
                continue
            if re.search(r"\d", text):
                errors.append(
                    f"skill summary contains digit {short} / {category}: {text!r}"
                )
            skill_name = skill_names.get(short, {}).get(category, "")
            if skill_name and skill_name.lower() in text.lower():
                errors.append(
                    f"skill summary contains skill name {short} / {category}: "
                    f"{text!r}"
                )
            if short.lower() in text.lower():
                errors.append(
                    f"skill summary contains hero name {short} / {category}: "
                    f"{text!r}"
                )

    return errors


def jsonschema_available() -> bool:
    try:
        import jsonschema  # noqa: F401

        return True
    except ImportError:
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--fail-on",
        nargs="*",
        default=["md_parity", "reanalysis", "schema", "skill_summary", "semantic"],
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
        if md_errors:
            warnings["md_parity"] = md_errors

    stored = json.loads(PROCESSED.read_text(encoding="utf-8"))
    fresh = _rebuild_processed()

    if "reanalysis" in fail_on:
        drift = check_reanalysis_parity(stored, fresh)
        if drift:
            errors.extend(drift)
        else:
            print("OK: processed JSON matches re-analysis output")
    else:
        drift = check_reanalysis_parity(stored, fresh)
        if drift:
            warnings["reanalysis"] = drift

    if "schema" in fail_on:
        try:
            hs.validate_processed(fresh)
            print("OK: processed JSON validates against schema")
        except Exception as exc:
            errors.append(f"schema validation failed: {exc}")
    else:
        try:
            hs.validate_processed(fresh)
        except Exception as exc:
            warnings["schema"] = [str(exc)]

    if "skill_summary" in fail_on:
        summary_errors = check_skill_summaries(stored)
        if summary_errors:
            errors.extend(summary_errors)
        else:
            print("OK: skill summaries complete and valid")
    else:
        summary_errors = check_skill_summaries(stored)
        if summary_errors:
            warnings["skill_summary"] = summary_errors

    semantic = check_semantic(fresh)
    for category, items in sorted(semantic.items()):
        if items:
            print(f"semantic [{category}]: {len(items)}")
            for item in items[:10]:
                print(f"  - {item}")
            if len(items) > 10:
                print(f"  ... and {len(items) - 10} more")
        if category in fail_on and args.max_semantic >= 0:
            if len(items) > args.max_semantic:
                errors.append(
                    f"semantic {category}: {len(items)} issues "
                    f"(max {args.max_semantic})"
                )

    if warnings:
        for key, items in warnings.items():
            print(f"warning [{key}]: {len(items)}", file=sys.stderr)

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Convert heroes-overview.md into a wide CSV table of summary categories."""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from healing_types import (
    DIRECT_HEALING_LABEL,
    HEALING_OVER_TIME_LABEL,
    normalize_healing_label,
)

from effect_labels import BUFF_EFFECT_TYPES, DEBUFF_EFFECT_TYPES, build_list_columns

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent
DEFAULT_INPUT = ROOT / "heroes-overview.md"
DEFAULT_OUTPUT = ROOT / "heroes-overview.csv"
LIST_COLUMNS_OUTPUT = ROOT / "site" / "data" / "list-columns.json"

DAMAGE_TYPES: list[tuple[str, str]] = [
    ("Magic", "Magic DMG"),
    ("Physical", "Physical DMG"),
    ("True damage", "True DMG"),
    ("HP loss", "HP Loss DMG"),
    ("Max HP-based damage", "Max HP DMG"),
]

CC_TYPES: list[str] = [
    "Stun",
    "Knock down",
    "Knock up",
    "Knock back",
    "Frighten",
    "Silence",
    "Charm",
    "Sleep",
    "Displace",
    "Bind",
    "Interrupt",
    "Taunt",
    "Blind",
]

ANTI_CC_TYPES: list[str] = [
    "Unaffected",
    "Steadfast",
    "Immune",
    "Untargetable",
    "Cleanse",
]

LIST_COLUMNS = build_list_columns()
BUFF_COLUMN_BY_LABEL = {
    col["label"]: col["id"] for col in LIST_COLUMNS if col["group"] == "buff"
}
DEBUFF_COLUMN_BY_LABEL = {
    col["label"]: col["id"] for col in LIST_COLUMNS if col["group"] == "debuff"
}

BUFF_TYPES: list[str] = [col["id"] for col in LIST_COLUMNS if col["group"] == "buff"]
DEBUFF_TYPES: list[str] = [
    col["id"] for col in LIST_COLUMNS if col["group"] == "debuff"
]

DAMAGE_LABEL_TO_COLUMN = {label: col for label, col in DAMAGE_TYPES}
CC_COLUMN_SET = frozenset(CC_TYPES)
ANTI_CC_COLUMN_SET = frozenset(ANTI_CC_TYPES)
BUFF_COLUMN_SET = frozenset(BUFF_COLUMN_BY_LABEL)
DEBUFF_COLUMN_SET = frozenset(DEBUFF_COLUMN_BY_LABEL)

ROLE_CATEGORY_LABELS: dict[str, str] = {
    "damage_dealer": "Damage dealer",
    "specialist": "Specialist",
    "support": "Support",
    "tank": "Tank",
}

COLUMNS: list[str] = (
    [
        "Name",
        "Faction",
        "Class",
        "Role",
        "AFK Stages tier",
        "Dream Realm tier",
        "Dream Realm Endless tier",
        "PVP tier",
        "Movement",
        "Behavior tags",
        "Signature skill speed",
        "Non-ultimate speed",
        "DoT",
        "HoT",
        "Summons",
        "Energy provider",
    ]
    + [col for _, col in DAMAGE_TYPES]
    + ["Healing", "Shields"]
    + CC_TYPES
    + ANTI_CC_TYPES
    + BUFF_TYPES
    + DEBUFF_TYPES
)

SUMMARY_RE = re.compile(r"^### Summary for ", re.M)
HERO_RE = re.compile(r"^## ([^\n]+)$", re.M)
_BOLD_LABEL = r"(?:\*\*)?"
_BOLD_LABEL_END = r"(?:\*\*)?"
MOVEMENT_RE = re.compile(
    rf"^- {_BOLD_LABEL}Movement{_BOLD_LABEL_END}: ([^\n]+)$", re.M
)
BEHAVIOR_TAGS_RE = re.compile(
    rf"^- {_BOLD_LABEL}Behavior tags{_BOLD_LABEL_END}: ([^\n]+)$", re.M
)
CASTING_SPEED_RE = re.compile(r"^- Casting speed: (\w+)$", re.M)
DEFINING_SKILL_SPEED_RE = re.compile(
    rf"^- {_BOLD_LABEL}Signature skill speed{_BOLD_LABEL_END}: (\w+)$", re.M
)
NON_ULT_SPEED_RE = re.compile(
    rf"^- {_BOLD_LABEL}Non-ultimate speed{_BOLD_LABEL_END}: (\w+)$", re.M
)
SKILL_OVERVIEW_SIG_SPEED_RE = re.compile(
    rf"^- {_BOLD_LABEL}Signature skill(?: \(ultimate\))?{_BOLD_LABEL_END}:"
    r".*?\bspeed `(slow|average|fast)`",
    re.M,
)
SKILL_OVERVIEW_NON_ULT_SPEED_RE = re.compile(
    rf"^- {_BOLD_LABEL}Non-ultimate{_BOLD_LABEL_END}:.*?"
    r"\bspeed `(slow|average|fast)`",
    re.M,
)
SECTION_RE = re.compile(r"^#### (.+)$", re.M)
BULLET_RE = re.compile(r"^- (.+)$", re.M)
MAGNITUDE_RE = re.compile(r"`(high|average|low)`")
PRIMARY_DAMAGE_RE = re.compile(r"^Primary damage type")
TIER_SUFFIX_RE = re.compile(r" \([^)]+\)$")


@dataclass
class HeroRow:
    name: str
    faction: str = ""
    class_name: str = ""
    role: str = ""
    afk_stages_tier: str = ""
    dream_realm_tier: str = ""
    dream_realm_endless_tier: str = ""
    pvp_tier: str = ""
    movement: str = ""
    behavior_tags: str = ""
    signature_skill_speed: str = ""
    non_ult_speed: str = ""
    energy_provider: bool = False
    flags: dict[str, bool] = field(default_factory=dict)
    cells: dict[str, list[str]] = field(default_factory=lambda: defaultdict(list))


def normalize_bullet(text: str) -> str:
    """Strip backticks from magnitude markers; keep the rest of the line."""
    return MAGNITUDE_RE.sub(r"\1", text.strip())


def parse_bullet_parts(text: str) -> tuple[str, str, str]:
    """Return (label, targeting, trailing) from a summary bullet."""
    parts = [p.strip() for p in text.split(" — ")]
    if len(parts) == 1:
        return parts[0], "", ""
    if len(parts) == 2:
        return parts[0], parts[1], ""
    return parts[0], parts[1], " — ".join(parts[2:])


def base_label(label: str) -> str:
    """Drop unlock-tier suffix, e.g. 'Stun (Mythic+)' -> 'Stun'."""
    return TIER_SUFFIX_RE.sub("", label).strip()


def format_cell_value(targeting: str, trailing: str) -> str:
    """Quality/timing + targeting for a single effect entry."""
    trailing = normalize_bullet(trailing)
    if targeting and trailing:
        return f"{targeting} — {trailing}"
    return targeting or trailing


def cc_column_name(label: str) -> str | None:
    base = base_label(label)
    if base.endswith(" immunity"):
        return base[: -len(" immunity")]
    if base in CC_COLUMN_SET:
        return base
    if base in ANTI_CC_COLUMN_SET:
        return base
    return None


def add_cell(row: HeroRow, column: str, value: str) -> None:
    if value:
        row.cells[column].append(value)


def apply_buff_effect_to_row(row: HeroRow, effect) -> None:
    label = (
        f"{effect.label} ({effect.tier})"
        if effect.tier and effect.tier != "base"
        else effect.label
    )
    trailing = effect.magnitude
    if effect.conditional:
        trailing = f"{effect.magnitude} — conditional ({effect.conditional})"
    value = format_cell_value(effect.targeting, trailing)
    buff_label = base_label(label)
    norm = normalize_healing_label(buff_label)
    if norm == HEALING_OVER_TIME_LABEL:
        row.flags["HoT"] = True
        return
    if norm == DIRECT_HEALING_LABEL:
        add_cell(row, "Healing", value)
    elif buff_label == "Shield":
        add_cell(row, "Shields", value)
    elif buff_label in BUFF_COLUMN_SET:
        add_cell(row, BUFF_COLUMN_BY_LABEL[buff_label], value)


def _load_rewrite_summaries():
    spec = importlib.util.spec_from_file_location(
        "rewrite_summaries_csv", SCRIPTS / "rewrite-summaries.py"
    )
    rs = importlib.util.module_from_spec(spec)
    sys.modules["rewrite_summaries_csv"] = rs
    assert spec.loader is not None
    spec.loader.exec_module(rs)
    return rs


def _load_role_category_by_title(
    rs,
    gen,
    records: list[dict],
) -> dict[str, str]:
    """Map hero title -> role_category for magnitude assignment."""
    processed_path = ROOT / "data" / "heroes_data_processed.json"
    by_short: dict[str, str] = {}
    if processed_path.is_file():
        payload = json.loads(processed_path.read_text(encoding="utf-8"))
        for short, record in payload.get("heroes", {}).items():
            by_short[short] = record.get("role_category", "damage_dealer")
    out: dict[str, str] = {}
    for record in records:
        hero = rs.hero_from_record(record)
        short = gen.short_name(hero.title)
        out[hero.title] = by_short.get(
            short, record.get("role_category", "damage_dealer")
        )
    return out


def _load_analyzed_heroes_by_short() -> dict[str, object]:
    rs = _load_rewrite_summaries()
    spec = importlib.util.spec_from_file_location(
        "heroes_io_csv", SCRIPTS / "heroes_io.py"
    )
    io = importlib.util.module_from_spec(spec)
    sys.modules["heroes_io_csv"] = io
    assert spec.loader is not None
    spec.loader.exec_module(io)

    gen = _load_gen_overview()

    records = io.load_heroes_data()["heroes"]
    heroes = []
    for record in records:
        hero = rs.hero_from_record(record)
        rs.analyze_hero(hero)
        heroes.append(hero)
    skills_by_title = rs.load_skills_by_title_from_records(records)
    role_category_by_title = _load_role_category_by_title(rs, gen, records)
    rs.assign_magnitudes(heroes, skills_by_title, role_category_by_title)
    out: dict[str, object] = {}
    for hero in heroes:
        out[gen.short_name(hero.title)] = hero
    return out


def section_kind(heading: str, hero_name: str) -> str | None:
    if heading.startswith("Damage types dealt by "):
        return "damage"
    if heading.startswith("Debuffs provided by "):
        return "debuffs"
    if heading.startswith("Crowd Control provided by "):
        return "cc"
    if heading == f"{hero_name} Provides":
        return "provides"
    return None


def parse_behavior(block: str) -> tuple[str, str, str, str]:
    """Return movement, behavior tags, signature skill speed, non-ult speed."""
    movement = ""
    behavior_tags = ""
    defining_skill_speed = ""  # local name kept for legacy fallback logic
    non_ult_speed = ""
    if m := MOVEMENT_RE.search(block):
        # "stationary (no finite attack range)" -> "stationary"
        movement = m.group(1).split(" (", 1)[0].strip()
    if m := BEHAVIOR_TAGS_RE.search(block):
        tags = re.findall(r"`([^`]+)`", m.group(1))
        behavior_tags = "; ".join(sorted(tags))
    if m := SKILL_OVERVIEW_SIG_SPEED_RE.search(block):
        defining_skill_speed = m.group(1).strip()
    if m := SKILL_OVERVIEW_NON_ULT_SPEED_RE.search(block):
        non_ult_speed = m.group(1).strip()
    if m := DEFINING_SKILL_SPEED_RE.search(block):
        defining_skill_speed = m.group(1).strip()
    if m := NON_ULT_SPEED_RE.search(block):
        non_ult_speed = m.group(1).strip()
    # Legacy single casting-speed line (pre-signature-skill overview).
    if not defining_skill_speed and (m := CASTING_SPEED_RE.search(block)):
        defining_skill_speed = m.group(1).strip()
    return movement, behavior_tags, defining_skill_speed, non_ult_speed


def _load_heroes_data_by_short_name() -> dict[str, dict]:
    """Map overview short name -> hero record from heroes_data.json."""
    spec = importlib.util.spec_from_file_location(
        "gen_overview", SCRIPTS / "generate-heroes-overview.py"
    )
    gen = importlib.util.module_from_spec(spec)
    sys.modules["gen_overview_meta"] = gen
    assert spec.loader is not None
    spec.loader.exec_module(gen)

    data_path = ROOT / "data" / "heroes_data.json"
    payload = json.loads(data_path.read_text(encoding="utf-8"))
    out: dict[str, dict] = {}
    for hero in payload.get("heroes", []):
        title = hero.get("title", "")
        short = gen.short_name(title)
        out[short] = hero
    return out


def _load_hero_faction_class() -> dict[str, tuple[str, str]]:
    """Map overview short name -> (faction, class) from heroes_data.json."""
    out: dict[str, tuple[str, str]] = {}
    for short, hero in _load_heroes_data_by_short_name().items():
        out[short] = (
            hero.get("faction", "") or "",
            hero.get("class", "") or "",
        )
    return out


def _load_hero_prydwen_tiers() -> dict[str, dict[str, str]]:
    """Map overview short name -> prydwen_tiers from heroes_data.json."""
    out: dict[str, dict[str, str]] = {}
    for short, hero in _load_heroes_data_by_short_name().items():
        tiers = hero.get("prydwen_tiers")
        if tiers:
            out[short] = tiers
    return out


def _load_gen_overview():
    spec = importlib.util.spec_from_file_location(
        "gen_overview_roles", SCRIPTS / "generate-heroes-overview.py"
    )
    gen = importlib.util.module_from_spec(spec)
    sys.modules["gen_overview_roles"] = gen
    assert spec.loader is not None
    spec.loader.exec_module(gen)
    return gen


def _load_hero_role_categories() -> dict[str, str]:
    """Map overview short name -> Prydwen role label from processed data."""
    path = ROOT / "data" / "heroes_data_processed.json"
    if not path.is_file():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    out: dict[str, str] = {}
    for short, record in payload.get("heroes", {}).items():
        role = record.get("role_category", "")
        out[short] = ROLE_CATEGORY_LABELS.get(role, "")
    return out


def _load_energy_provider_names() -> frozenset[str]:
    """Short names of heroes that grant ally Energy (shared synergy logic)."""
    spec = importlib.util.spec_from_file_location(
        "rewrite_summaries", SCRIPTS / "rewrite-summaries.py"
    )
    rs = importlib.util.module_from_spec(spec)
    sys.modules["rewrite_summaries"] = rs
    assert spec.loader is not None
    spec.loader.exec_module(rs)

    spec = importlib.util.spec_from_file_location(
        "gen_overview", SCRIPTS / "generate-heroes-overview.py"
    )
    gen = importlib.util.module_from_spec(spec)
    sys.modules["gen_overview"] = gen
    assert spec.loader is not None
    spec.loader.exec_module(gen)

    text = (ROOT / "Heroes.md").read_text(encoding="utf-8")
    blocks = [
        b if b.startswith("## ") else "## " + b
        for b in text.split("\n## ")
        if b.strip()
    ]
    names: set[str] = set()
    for block in blocks:
        if not block.startswith("## "):
            continue
        hero = rs.parse_hero_block(block)
        if gen.is_energy_provider(hero):
            names.add(gen.short_name(hero.title))
    return frozenset(names)


def parse_hero_block(
    name: str,
    block: str,
    energy_providers: frozenset[str],
    hero_meta: dict[str, tuple[str, str]],
    hero_tiers: dict[str, dict[str, str]] | None = None,
    hero_roles: dict[str, str] | None = None,
    analyzed_heroes: dict[str, object] | None = None,
) -> HeroRow | None:
    summary_match = SUMMARY_RE.search(block)
    if not summary_match:
        return None

    movement, behavior_tags, signature_skill_speed, non_ult_speed = parse_behavior(
        block
    )
    faction, class_name = hero_meta.get(name, ("", ""))
    tiers = (hero_tiers or {}).get(name, {})
    row = HeroRow(
        name=name,
        faction=faction,
        class_name=class_name,
        role=(hero_roles or {}).get(name, ""),
        afk_stages_tier=tiers.get("afk_stages", ""),
        dream_realm_tier=tiers.get("dream_realm", ""),
        dream_realm_endless_tier=tiers.get("dream_realm_endless", ""),
        pvp_tier=tiers.get("pvp", ""),
        movement=movement,
        behavior_tags=behavior_tags,
        signature_skill_speed=signature_skill_speed,
        non_ult_speed=non_ult_speed,
        energy_provider=name in energy_providers,
    )
    summary = block[summary_match.start() :]

    section_iter = list(SECTION_RE.finditer(summary))
    for idx, match in enumerate(section_iter):
        heading = match.group(1)
        kind = section_kind(heading, name)
        if kind is None:
            continue

        start = match.end()
        end = section_iter[idx + 1].start() if idx + 1 < len(section_iter) else len(summary)
        body = summary[start:end]

        for bullet_match in BULLET_RE.finditer(body):
            raw = bullet_match.group(1)
            label, targeting, trailing = parse_bullet_parts(raw)
            value = format_cell_value(targeting, trailing)

            if kind == "damage":
                if PRIMARY_DAMAGE_RE.match(raw):
                    continue
                dmg_label = base_label(label)
                if dmg_label == "DoT":
                    row.flags["DoT"] = True
                    continue
                column = DAMAGE_LABEL_TO_COLUMN.get(dmg_label)
                if column:
                    add_cell(row, column, value)
            elif kind == "buffs":
                buff_label = base_label(label)
                norm = normalize_healing_label(buff_label)
                if norm == HEALING_OVER_TIME_LABEL:
                    row.flags["HoT"] = True
                    continue
                if norm == DIRECT_HEALING_LABEL:
                    add_cell(row, "Healing", value)
                elif buff_label == "Shield":
                    add_cell(row, "Shields", value)
                elif buff_label in BUFF_COLUMN_SET:
                    add_cell(row, BUFF_COLUMN_BY_LABEL[buff_label], value)
            elif kind == "debuffs":
                debuff_label = base_label(label)
                column = DEBUFF_COLUMN_BY_LABEL.get(debuff_label)
                if column:
                    add_cell(row, column, value)
            elif kind == "cc":
                column = cc_column_name(label)
                if column:
                    add_cell(row, column, value)
            elif kind == "provides" and base_label(label).startswith("Summoning"):
                row.flags["Summons"] = True

    hero_obj = (analyzed_heroes or {}).get(name)
    if hero_obj is not None:
        rs = _load_rewrite_summaries()
        for effect in rs.collect_hero_buff_effects(hero_obj):
            apply_buff_effect_to_row(row, effect)

    return row


def parse_overview(
    text: str,
    energy_providers: frozenset[str],
    hero_meta: dict[str, tuple[str, str]],
    hero_tiers: dict[str, dict[str, str]] | None = None,
    hero_roles: dict[str, str] | None = None,
    *,
    analyzed_heroes: dict[str, object] | None = None,
) -> list[HeroRow]:
    heroes: list[HeroRow] = []
    if analyzed_heroes is None:
        analyzed_heroes = _load_analyzed_heroes_by_short()
    hero_matches = list(HERO_RE.finditer(text))
    for idx, match in enumerate(hero_matches):
        name = match.group(1).strip()
        start = match.end()
        end = hero_matches[idx + 1].start() if idx + 1 < len(hero_matches) else len(text)
        block = text[start:end]
        row = parse_hero_block(
            name,
            block,
            energy_providers,
            hero_meta,
            hero_tiers,
            hero_roles,
            analyzed_heroes,
        )
        if row is not None:
            heroes.append(row)
    return heroes


def format_flag(value: bool) -> str:
    return "yes" if value else ""


def join_cell(values: list[str]) -> str:
    return "; ".join(values)


def row_to_csv(row: HeroRow) -> list[str]:
    out = [
        row.name,
        row.faction,
        row.class_name,
        row.role,
        row.afk_stages_tier,
        row.dream_realm_tier,
        row.dream_realm_endless_tier,
        row.pvp_tier,
        row.movement,
        row.behavior_tags,
        row.signature_skill_speed,
        row.non_ult_speed,
    ]
    for flag in ("DoT", "HoT", "Summons"):
        out.append(format_flag(row.flags.get(flag, False)))
    out.append(format_flag(row.energy_provider))
    for _, col in DAMAGE_TYPES:
        out.append(join_cell(row.cells.get(col, [])))
    out.append(join_cell(row.cells.get("Healing", [])))
    out.append(join_cell(row.cells.get("Shields", [])))
    for col in CC_TYPES + ANTI_CC_TYPES + BUFF_TYPES + DEBUFF_TYPES:
        out.append(join_cell(row.cells.get(col, [])))
    return out


def convert(
    text: str,
    energy_providers: frozenset[str],
    hero_meta: dict[str, tuple[str, str]],
    hero_tiers: dict[str, dict[str, str]] | None = None,
    hero_roles: dict[str, str] | None = None,
    *,
    analyzed_heroes: dict[str, object] | None = None,
) -> list[list[str]]:
    rows = parse_overview(
        text,
        energy_providers,
        hero_meta,
        hero_tiers,
        hero_roles,
        analyzed_heroes=analyzed_heroes,
    )
    return [row_to_csv(row) for row in rows]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert heroes-overview.md into a wide CSV summary table."
    )
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        default=DEFAULT_INPUT,
        help=f"Input markdown file (default: {DEFAULT_INPUT.name})",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output CSV file (default: {DEFAULT_OUTPUT.name})",
    )
    args = parser.parse_args()

    text = args.input.read_text(encoding="utf-8")
    energy_providers = _load_energy_provider_names()
    hero_meta = _load_hero_faction_class()
    hero_tiers = _load_hero_prydwen_tiers()
    hero_roles = _load_hero_role_categories()
    data = convert(text, energy_providers, hero_meta, hero_tiers, hero_roles)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(COLUMNS)
        writer.writerows(data)

    LIST_COLUMNS_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    LIST_COLUMNS_OUTPUT.write_text(
        json.dumps(LIST_COLUMNS, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Wrote {len(data)} heroes × {len(COLUMNS)} columns to {args.output}")
    print(f"Wrote list column registry to {LIST_COLUMNS_OUTPUT}")


if __name__ == "__main__":
    main()

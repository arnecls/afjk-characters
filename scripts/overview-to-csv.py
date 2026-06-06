#!/usr/bin/env python3
"""Convert heroes-overview.md into a wide CSV table of summary categories."""

from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = ROOT / "heroes-overview.md"
DEFAULT_OUTPUT = ROOT / "heroes-overview.csv"

DAMAGE_TYPES: list[tuple[str, str]] = [
    ("Normal", "Normal DMG"),
    ("Melee", "Melee DMG"),
    ("Magic", "Magic DMG"),
    ("Ranged", "Ranged DMG"),
    ("Physical", "Physical DMG"),
    ("True damage", "True DMG"),
    ("HP loss", "HP Loss DMG"),
    ("Max HP-based damage", "Max HP DMG"),
]

CC_TYPES: list[str] = [
    "Stun",
    "Knock down",
    "Frighten",
    "Silence",
    "Charm",
    "Sleep",
    "Move",
    "Pin",
    "Interrupt",
    "Freeze",
    "Taunt",
]

ANTI_CC_TYPES: list[str] = [
    "Unaffected",
    "Steadfast",
    "Immune",
    "Cleanse",
    "Resilience",
]

BUFF_TYPES: list[str] = [
    "ATK buff",
    "ATK SPD buff",
    "Haste buff",
    "Crit buff",
    "DEF Penetration buff",
    "DEF buff",
    "Damage taken reduction",
    "Energy recovery",
    "Execution buff",
    "Fatal blow immunity",
    "Invincible",
    "Lifedrain buff",
    "Max HP buff",
    "Summon damage buff",
    "Ally empower buff",
    "Attack range buff",
    "Healing stat buff",
]

DEBUFF_TYPES: list[str] = [
    "ATK debuff",
    "Blind HP loss debuff",
    "Burn debuff",
    "Damage taken debuff",
    "Energy drain",
    "Execution debuff",
    "Haste debuff",
    "Magic DEF debuff",
    "Max HP debuff",
    "Movement speed debuff",
    "Phys DEF debuff",
    "Vitality debuff",
]

DAMAGE_LABEL_TO_COLUMN = {label: col for label, col in DAMAGE_TYPES}
CC_COLUMN_SET = frozenset(CC_TYPES)
ANTI_CC_COLUMN_SET = frozenset(ANTI_CC_TYPES)
BUFF_COLUMN_SET = frozenset(BUFF_TYPES)
DEBUFF_COLUMN_SET = frozenset(DEBUFF_TYPES)

COLUMNS: list[str] = (
    ["Name", "Movement", "Defining skill speed", "Non-ultimate speed", "DoT", "HoT", "Summons"]
    + [col for _, col in DAMAGE_TYPES]
    + ["Healing", "Shields"]
    + CC_TYPES
    + ANTI_CC_TYPES
    + BUFF_TYPES
    + DEBUFF_TYPES
)

SUMMARY_RE = re.compile(r"^### Summary for ", re.M)
HERO_RE = re.compile(r"^## ([^\n]+)$", re.M)
MOVEMENT_RE = re.compile(r"^- Movement: ([^\n]+)$", re.M)
CASTING_SPEED_RE = re.compile(r"^- Casting speed: (\w+)$", re.M)
DEFINING_SKILL_SPEED_RE = re.compile(r"^- Defining skill speed: (\w+)$", re.M)
NON_ULT_SPEED_RE = re.compile(r"^- Non-ultimate speed: (\w+)$", re.M)
SECTION_RE = re.compile(r"^#### (.+)$", re.M)
BULLET_RE = re.compile(r"^- (.+)$", re.M)
MAGNITUDE_RE = re.compile(r"`(high|medium|low)`")
PRIMARY_DAMAGE_RE = re.compile(r"^Primary damage type")
TIER_SUFFIX_RE = re.compile(r" \([^)]+\)$")


@dataclass
class HeroRow:
    name: str
    movement: str = ""
    defining_skill_speed: str = ""
    non_ult_speed: str = ""
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
    return None


def add_cell(row: HeroRow, column: str, value: str) -> None:
    if value:
        row.cells[column].append(value)


def section_kind(heading: str, hero_name: str) -> str | None:
    if heading.startswith("Damage types dealt by "):
        return "damage"
    if heading.startswith("Buffs provided by "):
        return "buffs"
    if heading.startswith("Debuffs provided by "):
        return "debuffs"
    if heading.startswith("Crowd Control provided by "):
        return "cc"
    if heading == f"{hero_name} Provides":
        return "provides"
    return None


def parse_behavior(block: str) -> tuple[str, str, str]:
    """Return movement, defining skill speed, non-ultimate speed."""
    movement = ""
    defining_skill_speed = ""
    non_ult_speed = ""
    if m := MOVEMENT_RE.search(block):
        # "stationary (no finite attack range)" -> "stationary"
        movement = m.group(1).split(" (", 1)[0].strip()
    if m := DEFINING_SKILL_SPEED_RE.search(block):
        defining_skill_speed = m.group(1).strip()
    if m := NON_ULT_SPEED_RE.search(block):
        non_ult_speed = m.group(1).strip()
    # Legacy single casting-speed line (pre-defining-skill overview).
    if not defining_skill_speed and (m := CASTING_SPEED_RE.search(block)):
        defining_skill_speed = m.group(1).strip()
    return movement, defining_skill_speed, non_ult_speed


def parse_hero_block(name: str, block: str) -> HeroRow | None:
    summary_match = SUMMARY_RE.search(block)
    if not summary_match:
        return None

    movement, defining_skill_speed, non_ult_speed = parse_behavior(block)
    row = HeroRow(
        name=name,
        movement=movement,
        defining_skill_speed=defining_skill_speed,
        non_ult_speed=non_ult_speed,
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
                if buff_label == "Healing over time":
                    row.flags["HoT"] = True
                    continue
                if buff_label == "Healing":
                    add_cell(row, "Healing", value)
                elif buff_label == "Shield":
                    add_cell(row, "Shields", value)
                elif buff_label in BUFF_COLUMN_SET:
                    add_cell(row, buff_label, value)
            elif kind == "debuffs":
                debuff_label = base_label(label)
                if debuff_label in DEBUFF_COLUMN_SET:
                    add_cell(row, debuff_label, value)
            elif kind == "cc":
                column = cc_column_name(label)
                if column:
                    add_cell(row, column, value)
            elif kind == "provides" and base_label(label).startswith("Summoning"):
                row.flags["Summons"] = True

    return row


def parse_overview(text: str) -> list[HeroRow]:
    heroes: list[HeroRow] = []
    hero_matches = list(HERO_RE.finditer(text))
    for idx, match in enumerate(hero_matches):
        name = match.group(1).strip()
        start = match.end()
        end = hero_matches[idx + 1].start() if idx + 1 < len(hero_matches) else len(text)
        block = text[start:end]
        row = parse_hero_block(name, block)
        if row is not None:
            heroes.append(row)
    return heroes


def format_flag(value: bool) -> str:
    return "yes" if value else ""


def join_cell(values: list[str]) -> str:
    return "; ".join(values)


def row_to_csv(row: HeroRow) -> list[str]:
    out = [row.name, row.movement, row.defining_skill_speed, row.non_ult_speed]
    for flag in ("DoT", "HoT", "Summons"):
        out.append(format_flag(row.flags.get(flag, False)))
    for _, col in DAMAGE_TYPES:
        out.append(join_cell(row.cells.get(col, [])))
    out.append(join_cell(row.cells.get("Healing", [])))
    out.append(join_cell(row.cells.get("Shields", [])))
    for col in CC_TYPES + ANTI_CC_TYPES + BUFF_TYPES + DEBUFF_TYPES:
        out.append(join_cell(row.cells.get(col, [])))
    return out


def convert(text: str) -> list[list[str]]:
    rows = parse_overview(text)
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
    data = convert(text)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(COLUMNS)
        writer.writerows(data)

    print(f"Wrote {len(data)} heroes × {len(COLUMNS)} columns to {args.output}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Shared I/O for the AFK Journey hero data pipeline.

Defines the ``heroes_data.json`` schema and provides:

- parsers that read the legacy ``Heroes.md`` (Yaphalla) and ``heroes2.md``
  (fandom) markdown into structured hero records,
- a merge that combines both sources into one record list,
- reconstructors that rebuild the Yaphalla / fandom markdown blocks from a
  record (used both to render ``heroes.md`` and to feed the existing
  markdown-based analysis without changing it),
- helpers to load/save the JSON artefacts.

The schema deliberately keeps the per-source skill text because the synergy
analysis is sensitive to exact wording (Yaphalla text) while the behaviour
analysis reads fandom skill ranges / energy. Storing both lets the render and
process steps reproduce the current outputs byte-for-byte.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent

HEROES_MD = ROOT / "Heroes.md"
HEROES2_MD = ROOT / "heroes2.md"

DATA = ROOT / "data"

HEROES_DATA = DATA / "heroes_data.json"
HEROES_DATA_PROCESSED = DATA / "heroes_data_processed.json"
HEROES_DATA_SYNERGIES = DATA / "heroes_data_synergies.json"
HEROES_CONFIG = DATA / "heroes_config.json"

# Section headings, in the order they appear in a hero block.
SECTION_ORDER = [
    "Ultimate",
    "Skill1",
    "Skill2",
    "Unlocks at Legendary+",
    "Ex. Skill",
    "Unlocks at Supreme+",
]

# Metadata bullet labels, in render order.
META_LABELS = ["Cooldown", "Initial Cooldown", "Skill Range", "Initial Energy"]

_HEROES_MD_HEADER = (
    "# AFK Journey Heroes\n"
    "\n"
    "Skill data sourced from [Yaphalla Heroes](https://www.yaphalla.com/heroes).\n"
    "Summaries live in [heroes-overview.md](heroes-overview.md) "
    "(see `scripts/generate-heroes-overview.py`).\n"
)

_LEVEL_RE = re.compile(r"^Level (\d+)(?: — (.+))?$")


# ---------------------------------------------------------------------------
# JSON load / save
# ---------------------------------------------------------------------------


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: Any) -> None:
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def load_heroes_data() -> list[dict]:
    return load_json(HEROES_DATA)


def load_processed() -> dict:
    return load_json(HEROES_DATA_PROCESSED)


def load_synergies() -> dict:
    return load_json(HEROES_DATA_SYNERGIES)


def load_config() -> dict:
    return load_json(HEROES_CONFIG)


# ---------------------------------------------------------------------------
# Markdown parsing
# ---------------------------------------------------------------------------


def split_hero_blocks(text: str) -> list[str]:
    """Return the per-hero markdown blocks (starting at ``## ``)."""
    return [b for b in re.split(r"\n(?=## )", text) if b.startswith("## ")]


def _parse_level_entry(entry_lines: list[str]) -> dict:
    """Parse one ``- Level ...`` entry (possibly multi-line) into a record.

    ``entry_lines`` is the ``- Level`` line plus any continuation / interior
    blank lines that belong to it. The text may therefore contain newlines.
    """
    body = entry_lines[0][2:]  # strip leading "- "
    text = "\n".join([body] + entry_lines[1:])
    label_part, sep, value = body.partition(": ")
    m = _LEVEL_RE.match(label_part)
    if not m or not sep:
        return {"level": None, "unlock": None, "text": text, "raw": True}
    value = "\n".join([value] + entry_lines[1:])
    return {"level": m.group(1), "unlock": m.group(2), "text": value}


def _parse_skill_block(part: str) -> dict:
    """Parse a single ``### <section>`` chunk into a skill record."""
    lines = part.split("\n")
    section = lines[0][4:].strip()
    skill: dict[str, Any] = {
        "section": section,
        "name": None,
        "unlock": None,
        "meta": {},
        "description": "",
        "levels": [],
    }
    body: list[str] = []
    in_header = True
    for ln in lines[1:]:
        if in_header:
            if ln == "":
                continue
            m_name = re.match(r"^\*\*(.*)\*\*$", ln)
            if m_name and skill["name"] is None:
                skill["name"] = m_name.group(1)
                continue
            m_unlock = re.match(r"^\*(.+)\*$", ln)
            if m_unlock and skill["unlock"] is None:
                skill["unlock"] = m_unlock.group(1)
                continue
            m_meta = re.match(
                r"^- (Cooldown|Initial Cooldown|Skill Range|Initial Energy): (.+)$",
                ln,
            )
            if m_meta:
                skill["meta"][m_meta.group(1)] = m_meta.group(2)
                continue
            in_header = False
        body.append(ln)

    # Split body into the description block and the level-upgrade block.
    first_level = next(
        (i for i, ln in enumerate(body) if ln.startswith("- Level ")), len(body)
    )
    desc_lines = body[:first_level]
    level_region = body[first_level:]

    while desc_lines and desc_lines[0] == "":
        desc_lines.pop(0)
    while desc_lines and desc_lines[-1] == "":
        desc_lines.pop()
    skill["description"] = "\n".join(desc_lines)

    # Drop the single trailing blank that separates the block from the next
    # section; interior blanks stay attached to their level entry.
    while level_region and level_region[-1] == "":
        level_region.pop()

    entries: list[list[str]] = []
    for ln in level_region:
        if ln.startswith("- Level "):
            entries.append([ln])
        elif entries:
            entries[-1].append(ln)
    skill["levels"] = [_parse_level_entry(e) for e in entries]
    return skill


def parse_hero_block(block: str) -> dict:
    """Parse one hero markdown block into a structured record."""
    head, _, rest = block.partition("\n### ")
    head_lines = head.split("\n")
    title = head_lines[0][3:].strip()

    tags = None
    description_lines: list[str] = []
    in_header = True
    for ln in head_lines[1:]:
        if in_header:
            if ln == "":
                continue
            m_tags = re.match(r"^\*(.+)\*$", ln)
            if m_tags and tags is None:
                tags = m_tags.group(1)
                continue
            in_header = False
        description_lines.append(ln)
    while description_lines and description_lines[0] == "":
        description_lines.pop(0)
    while description_lines and description_lines[-1] == "":
        description_lines.pop()

    skills: list[dict] = []
    if rest:
        for part in re.split(r"(?=^### )", "### " + rest, flags=re.MULTILINE):
            if part.startswith("### "):
                skills.append(_parse_skill_block(part.rstrip("\n")))

    faction = hero_class = damage = None
    if tags:
        parts = [p.strip() for p in tags.split("·")]
        if len(parts) >= 1:
            faction = parts[0]
        if len(parts) >= 2:
            hero_class = parts[1]
        if len(parts) >= 3:
            damage = parts[2]

    return {
        "title": title,
        "name": title.split(" - ", 1)[0].strip(),
        "tags": tags,
        "faction": faction,
        "class": hero_class,
        "damage_type": damage,
        "description": "\n".join(description_lines),
        "skills": skills,
    }


def parse_md(text: str) -> list[dict]:
    """Parse a Heroes.md / heroes2.md document into hero records."""
    return [parse_hero_block(b) for b in split_hero_blocks(text)]


# ---------------------------------------------------------------------------
# Source merge
# ---------------------------------------------------------------------------

# Display name -> fandom hero name, for heroes named differently per source.
NAME_ALIASES: dict[str, str] = {
    "Twins": "Elijah & Lailah",
    "Gala": "Galahad",
}


def _gapfill_identity(record: dict, fandom_hero: dict) -> None:
    """Fill missing Yaphalla identity fields from the fandom baseline.

    No-op when the Yaphalla record is already complete (the markdown path), so
    this only affects the live web download where Yaphalla no longer exposes
    faction / class / damage.
    """
    for key in ("faction", "class", "damage_type"):
        if not record.get(key) and fandom_hero.get(key):
            record[key] = fandom_hero[key]
    if not record.get("description") and fandom_hero.get("description"):
        record["description"] = fandom_hero["description"]
    if " - " not in record.get("title", "") and fandom_hero.get("title"):
        record["title"] = fandom_hero["title"]
    if not record.get("tags"):
        tags = " · ".join(
            t for t in (record.get("faction"), record.get("class"),
                        record.get("damage_type")) if t
        )
        record["tags"] = tags or None

    # Per-skill gap-fill: Yaphalla's current site no longer exposes level
    # upgrades, so borrow level text (and empty descriptions) from fandom.
    fandom_skills = {s["section"]: s for s in fandom_hero.get("skills", [])}
    for skill in record.get("skills", []):
        fskill = fandom_skills.get(skill["section"])
        if not fskill:
            continue
        if not skill.get("levels") and fskill.get("levels"):
            skill["levels"] = fskill["levels"]
        if not skill.get("description") and fskill.get("description"):
            skill["description"] = fskill["description"]
        if not skill.get("name") and fskill.get("name"):
            skill["name"] = fskill["name"]


def merge_sources(
    yaphalla: list[dict],
    fandom: list[dict],
    yaphalla_header: str = _HEROES_MD_HEADER,
    fandom_header: str = "",
    gapfill: bool = False,
) -> dict:
    """Merge Yaphalla (baseline text) + fandom (metadata) into one document.

    The Yaphalla record drives ``heroes.md`` and the synergy/summary analysis
    (which is sensitive to exact wording); the fandom record supplies Skill
    Range / Initial Energy and the behaviour skill text. Both are retained so
    the render/process steps reproduce the current outputs.
    """
    fandom_by_name = {h["name"]: h for h in fandom}

    heroes: list[dict] = []
    for hero in yaphalla:
        name = hero["name"]
        fandom_hero = fandom_by_name.get(name)
        if fandom_hero is None and name in NAME_ALIASES:
            fandom_hero = fandom_by_name.get(NAME_ALIASES[name])
        record = dict(hero)
        if gapfill and fandom_hero:
            _gapfill_identity(record, fandom_hero)
        record["fandom"] = fandom_hero
        heroes.append(record)

    return {
        "yaphalla_header": yaphalla_header,
        "fandom_header": fandom_header,
        "heroes": heroes,
    }


# ---------------------------------------------------------------------------
# Document reconstruction (for feeding the existing analysis unchanged)
# ---------------------------------------------------------------------------


def reconstruct_heroes_md(data: dict) -> str:
    """Rebuild the Yaphalla document (== Heroes.md) from heroes_data."""
    return render_md(data["heroes"], header=data["yaphalla_header"])


def reconstruct_heroes2_md(data: dict) -> str:
    """Rebuild the fandom document (behaviour source) from heroes_data."""
    fandom = [h["fandom"] for h in data["heroes"] if h.get("fandom")]
    header = data.get("fandom_header") or ""
    # Match heroes2.md spacing: a blank line trails each hero block.
    parts = [header.rstrip("\n"), ""]
    for hero in fandom:
        parts.append(render_hero_block(hero) + "\n")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Markdown reconstruction
# ---------------------------------------------------------------------------


def _level_line(level: dict) -> str:
    if level.get("raw"):
        return f"- {level['text']}"
    if level.get("unlock"):
        label = f"Level {level['level']} — {level['unlock']}"
    else:
        label = f"Level {level['level']}"
    return f"- {label}: {level['text']}"


def render_skill_block(skill: dict) -> str:
    lines = [f"### {skill['section']}", ""]
    if skill.get("name") is not None:
        lines.append(f"**{skill['name']}**")
    if skill.get("unlock") is not None:
        lines.append(f"*{skill['unlock']}*")
    lines.append("")

    meta = skill.get("meta") or {}
    meta_lines = [f"- {label}: {meta[label]}" for label in META_LABELS if label in meta]
    if meta_lines:
        lines.extend(meta_lines)
        lines.append("")

    lines.append(skill.get("description") or "_No description._")
    lines.append("")

    for level in skill.get("levels", []):
        lines.append(_level_line(level))
    if skill.get("levels"):
        lines.append("")

    return "\n".join(lines)


def render_hero_block(hero: dict) -> str:
    lines = [f"## {hero['title']}", ""]
    if hero.get("tags"):
        lines.append(f"*{hero['tags']}*")
        lines.append("")
    if hero.get("description"):
        lines.append(hero["description"])
        lines.append("")
    for skill in hero.get("skills", []):
        lines.append(render_skill_block(skill))
    return "\n".join(lines)


def render_md(heroes: list[dict], header: str = _HEROES_MD_HEADER) -> str:
    parts = [header.rstrip("\n"), ""]
    for hero in heroes:
        parts.append(render_hero_block(hero))
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Self-test: round-trip the committed markdown files.
# ---------------------------------------------------------------------------


def _extract_header(text: str) -> str:
    """Everything before the first hero block (``## ``)."""
    m = re.search(r"\n## ", text)
    return text[: m.start()] if m else text


def _roundtrip_report(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    heroes = parse_md(original)
    rebuilt = render_md(heroes, header=_extract_header(original))
    if rebuilt == original:
        print(f"OK  {path.name}: round-trip byte-identical ({len(heroes)} heroes)")
        return True
    import difflib

    o_lines = original.split("\n")
    r_lines = rebuilt.split("\n")
    sm = difflib.SequenceMatcher(a=o_lines, b=r_lines, autojunk=False)
    blocks = [b for b in sm.get_opcodes() if b[0] != "equal"]
    print(
        f"DIFF {path.name}: {len(o_lines)} vs {len(r_lines)} lines, "
        f"{len(heroes)} heroes, {len(blocks)} differing region(s)"
    )
    for tag, i1, i2, j1, j2 in blocks[:12]:
        print(f"  [{tag}] orig {i1 + 1}-{i2} / new {j1 + 1}-{j2}")
        for ln in o_lines[i1:i2][:2]:
            print(f"    - {ln!r}")
        for ln in r_lines[j1:j2][:2]:
            print(f"    + {ln!r}")
    return False


if __name__ == "__main__":
    for path in (HEROES_MD, HEROES2_MD):
        if path.exists():
            _roundtrip_report(path)
        else:
            print(f"skip {path.name}: not present")

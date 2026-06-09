#!/usr/bin/env python3
"""Shared I/O for the AFK Journey hero data pipeline.

Defines the ``heroes_data.json`` schema and provides:

- parsers that read ``Heroes.md`` / ``heroes2.md`` markdown into structured
  hero records,
- a merge that uses the Fandom wiki as baseline and fills gaps from Yaphalla,
- reconstructors that rebuild markdown blocks from a record for render and
  analysis,
- helpers to load/save the JSON artefacts.

The Fandom wiki supplies translated skill text plus Skill Range and Initial
Energy. Yaphalla is consulted only when Fandom fields are missing, and
untranslated Yaphalla strings (CJK / ``不用翻译`` markers) are skipped.
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
    "Skill data sourced from "
    "[AFK Journey Wiki](https://afk-journey.fandom.com/wiki/Hero/List), "
    "with gaps filled from [Yaphalla Heroes](https://www.yaphalla.com/heroes).\n"
    "Summaries live in [heroes-overview.md](heroes-overview.md) "
    "(see `scripts/generate-heroes-overview.py`).\n"
)

_CJK_RE = re.compile(r"[\u4e00-\u9fff\u3400-\u4dbf]")

_LEVEL_RE = re.compile(r"^Level (\d+)(?: — (.+))?$")
_WIKI_TAG_RE = re.compile(r"\[([^\]]+)\]([^\[]+)\[/\]")


def normalize_skill_text(text: str) -> str:
    """Strip fandom/wiki highlight tags so analysis sees plain words."""
    if not text:
        return text
    return _WIKI_TAG_RE.sub(lambda m: m.group(2), text)


def normalize_hero_skills(hero: dict) -> None:
    """Normalize skill description and level text in a hero record (in place)."""
    for skill in hero.get("skills", []):
        if skill.get("description"):
            skill["description"] = normalize_skill_text(skill["description"])
        for level in skill.get("levels", []):
            if level.get("text"):
                level["text"] = normalize_skill_text(level["text"])


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

# Fandom roster name -> Yaphalla page name when they differ.
YAPHALLA_NAME_ALIASES: dict[str, str] = {
    "Elijah & Lailah": "Twins",
    "Galahad": "Gala",
}

# Legacy: Yaphalla display name -> Fandom name (old merge direction).
NAME_ALIASES: dict[str, str] = {
    "Twins": "Elijah & Lailah",
}


def _has_text(text: str | None) -> bool:
    return bool(text and str(text).strip())


def is_usable_yaphalla_text(text: str | None) -> bool:
    """True when Yaphalla text is safe to use (translated, non-empty)."""
    if not _has_text(text):
        return False
    s = str(text)
    if "不用翻译" in s:
        return False
    return _CJK_RE.search(s) is None


def _lookup_yaphalla(name: str, yaphalla_by_name: dict[str, dict]) -> dict | None:
    hero = yaphalla_by_name.get(name)
    if hero is not None:
        return hero
    alias = YAPHALLA_NAME_ALIASES.get(name)
    if alias:
        return yaphalla_by_name.get(alias)
    return None


def _gapfill_from_yaphalla(record: dict, yaphalla_hero: dict) -> None:
    """Fill gaps in a Fandom baseline record from translated Yaphalla data."""
    for key in ("faction", "class", "damage_type", "tags"):
        if not record.get(key) and yaphalla_hero.get(key):
            record[key] = yaphalla_hero[key]
    if not record.get("description") and is_usable_yaphalla_text(
        yaphalla_hero.get("description")
    ):
        record["description"] = yaphalla_hero["description"]
    if " - " not in record.get("title", "") and is_usable_yaphalla_text(
        yaphalla_hero.get("title")
    ):
        record["title"] = yaphalla_hero["title"]
    if not record.get("tags"):
        tags = " · ".join(
            t
            for t in (
                record.get("faction"),
                record.get("class"),
                record.get("damage_type"),
            )
            if t
        )
        record["tags"] = tags or None

    yaphalla_skills = {s["section"]: s for s in yaphalla_hero.get("skills", [])}
    for skill in record.get("skills", []):
        yskill = yaphalla_skills.get(skill["section"])
        if not yskill:
            continue
        meta = skill.setdefault("meta", {})
        for label in ("Cooldown", "Initial Cooldown"):
            if label not in meta and yskill.get("meta", {}).get(label):
                meta[label] = yskill["meta"][label]
        if not _has_text(skill.get("name")) and is_usable_yaphalla_text(
            yskill.get("name")
        ):
            skill["name"] = yskill["name"]
        if not _has_text(skill.get("description")) and is_usable_yaphalla_text(
            yskill.get("description")
        ):
            skill["description"] = yskill["description"]
        if not skill.get("levels"):
            ylevels = yskill.get("levels", [])
            if ylevels and all(
                is_usable_yaphalla_text(level.get("text")) for level in ylevels
            ):
                skill["levels"] = ylevels


def merge_sources(
    fandom: list[dict],
    yaphalla: list[dict],
    heroes_header: str = _HEROES_MD_HEADER,
    fandom_header: str = "",
    gapfill: bool = False,
    *,
    yaphalla_header: str | None = None,
) -> dict:
    """Merge Fandom (baseline) + Yaphalla (gap-fill) into one document.

    Each hero record is the Fandom wiki entry (Skill Range, Initial Energy,
    translated text). When ``gapfill`` is true, missing identity or skill
    fields are filled from Yaphalla only if that text is translated.
    """
    yaphalla_by_name = {h["name"]: h for h in yaphalla}
    header = yaphalla_header if yaphalla_header is not None else heroes_header

    heroes: list[dict] = []
    for hero in fandom:
        record = dict(hero)
        yaphalla_hero = _lookup_yaphalla(hero["name"], yaphalla_by_name)
        if gapfill and yaphalla_hero:
            _gapfill_from_yaphalla(record, yaphalla_hero)
        normalize_hero_skills(record)
        heroes.append(record)

    return {
        "heroes_header": header,
        "yaphalla_header": header,
        "fandom_header": fandom_header,
        "heroes": heroes,
    }


# ---------------------------------------------------------------------------
# Document reconstruction (for feeding the existing analysis unchanged)
# ---------------------------------------------------------------------------


def _heroes_document_header(data: dict) -> str:
    return (
        data.get("heroes_header")
        or data.get("yaphalla_header")
        or _HEROES_MD_HEADER
    )


def _behavior_hero_records(data: dict) -> list[dict]:
    """Hero records for behaviour analysis (ranges / energy)."""
    records: list[dict] = []
    for hero in data["heroes"]:
        if hero.get("fandom"):
            records.append(hero["fandom"])
        else:
            records.append(hero)
    return records


def reconstruct_heroes_md(data: dict) -> str:
    """Rebuild Heroes.md from heroes_data (Fandom baseline + Yaphalla gaps)."""
    return render_md(data["heroes"], header=_heroes_document_header(data))


def reconstruct_heroes2_md(data: dict) -> str:
    """Rebuild the behaviour-source document from heroes_data."""
    heroes = _behavior_hero_records(data)
    header = data.get("fandom_header") or _heroes_document_header(data)
    parts = [header.rstrip("\n"), ""]
    for hero in heroes:
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

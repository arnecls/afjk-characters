"""Skill text chunking and hero-record construction."""

from __future__ import annotations

import json
import re
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any, Mapping

from healing_types import (
    DIRECT_HEALING_LABEL,
    HEALING_OVER_TIME_LABEL,
    HEALING_STAT_BUFF_LABEL,
    HP_RECOVERY_LABELS,
    is_hp_recovery_label,
)

from effect_labels import (
    DEBUFF_EFFECT_TYPES,
    canonical_effect_label,
    canonical_effect_name,
    display_effect_name,
)

from .records import (
    Hero,
    HeroRecord,
    SkillMeta,
    SkillMetaRecord,
)
from .detector_common import EX_TIER_RE, SECTION_TIERS
def parse_level_tier(line: str, section: str) -> str:
    ex = EX_TIER_RE.search(line)
    if ex:
        return f"EX+{ex.group(1)}"
    if section == "Unlocks at Legendary+":
        return "Legendary+"
    if section == "Unlocks at Supreme+":
        return "Supreme+"
    return SECTION_TIERS.get(section, "base")

def _split_passive_active_chunk(text: str) -> list[str]:
    """Split merged Passive./Active. prose from Heroes.md skill buffers."""
    if not re.search(r"\bActive\.\s+", text, re.I):
        return [text]
    parts = re.split(r"\bActive\.\s+", text, maxsplit=1, flags=re.I)
    out: list[str] = []
    head = parts[0].strip()
    head = re.sub(r"\bPassive\.\s*$", "", head, flags=re.I).strip()
    if head:
        out.append(head)
    if len(parts) > 1 and parts[1].strip():
        out.append(parts[1].strip())
    return out or [text]

def parse_hero_block(block: str) -> HeroRecord:
    lines = block.splitlines()
    title = lines[0].replace("## ", "").strip()
    dmg = ""
    fm = re.search(r"·\s*(\w+)\s*\*", block[:500])
    if fm:
        dmg = fm.group(1)
    hero = Hero(title=title, damage_type=dmg)
    current_section: str | None = None
    buffer: list[str] = []

    def flush_buffer():
        nonlocal buffer
        if current_section and buffer:
            text = " ".join(buffer).strip()
            if text:
                from heroes_io import normalize_skill_text

                text = normalize_skill_text(text)
                tier = SECTION_TIERS.get(current_section, "base")
                for chunk in _split_passive_active_chunk(text):
                    hero["skill_chunks"].append((tier, chunk, current_section))
        buffer = []

    for ln in lines[1:]:
        if ln.startswith("### Summary"):
            flush_buffer()
            break
        if ln.startswith("### "):
            flush_buffer()
            sec = ln[4:].strip()
            current_section = sec if sec in SECTION_TIERS else None
            continue
        if (
            current_section
            and ln.startswith("**")
            and ln.endswith("**")
            and ln.count("**") == 2
        ):
            skill_name = ln.strip("*").strip()
            if skill_name:
                hero["skill_name_to_section"][skill_name] = current_section
            continue
        if not current_section:
            continue
        if ln.startswith("**") or ln.startswith("*Unlocks"):
            continue
        if ln.startswith("- Cooldown") or ln.startswith("- Initial Cooldown"):
            rest = re.sub(r"^- (?:Initial )?Cooldown:.*?(?=\w)", "", ln).strip()
            if rest:
                buffer.append(rest)
            continue
        if ln.startswith("- Level"):
            flush_buffer()
            tier = parse_level_tier(ln, current_section)
            text = ln.split(":", 1)[-1].strip() if ":" in ln else ln
            from heroes_io import normalize_skill_text

            text = normalize_skill_text(text)
            hero["skill_chunks"].append((tier, text, current_section or ""))
            continue
        if ln.strip():
            buffer.append(ln.strip())
    flush_buffer()
    return hero

def _upgrade_tier(level: dict, section: str) -> str:
    if level.get("raw"):
        return SECTION_TIERS.get(section, "base")
    line = f"Level {level.get('level') or ''}"
    if level.get("unlock"):
        line += f" — {level['unlock']}"
    text = level.get("text") or ""
    line += f": {text}"
    return parse_level_tier(line, section)

def skill_chunks_from_skill(skill: dict) -> list[tuple[str, str, str]]:
    """Build analysis chunks from a structured heroes_data skill record."""
    from heroes_io import (
        _skip_phase_marker_sentence,
        is_structured_description,
        merge_unique_sentences,
        normalize_phase_text,
        normalize_skill_description,
        skill_upgrades,
        split_passive_active,
    )

    if not is_structured_description(skill.get("description")):
        normalize_skill_description(skill)
    section = skill["section"]
    base_tier = SECTION_TIERS.get(section, "base")
    chunks: list[tuple[str, str, str]] = []
    desc = skill["description"]
    passive_sents = normalize_phase_text(desc.get("passive"))
    active_sents = normalize_phase_text(desc.get("active"))
    raw = (desc.get("raw") or "").strip()
    if raw:
        split_passive, split_active = split_passive_active(raw)
        passive_sents = merge_unique_sentences(
            normalize_phase_text(split_passive), passive_sents
        )
        active_sents = merge_unique_sentences(
            normalize_phase_text(split_active), active_sents
        )
    for sent in passive_sents:
        if _skip_phase_marker_sentence(sent):
            continue
        chunks.append((base_tier, sent, section))
    for sent in active_sents:
        if _skip_phase_marker_sentence(sent):
            continue
        chunks.append((base_tier, sent, section))
    if not passive_sents and not active_sents:
        raw = (desc.get("raw") or "").strip()
        if raw:
            for sent in normalize_phase_text(raw):
                chunks.append((base_tier, sent, section))
    for level in skill_upgrades(skill):
        tier = _upgrade_tier(level, section)
        for sent in normalize_phase_text(level.get("text")):
            if _skip_phase_marker_sentence(sent):
                continue
            chunks.append((tier, sent, section))
    return chunks

def hero_from_record(hero_record: dict) -> HeroRecord:
    """Build an analysis Hero directly from a heroes_data.json record."""
    from heroes_io import normalize_skill_description

    title = hero_record["title"]
    tags = hero_record.get("tags") or ""
    dmg = hero_record.get("damage_type") or ""
    if not dmg and tags:
        parts = [p.strip() for p in tags.split("·")]
        if len(parts) >= 3:
            dmg = parts[2]
    hero = Hero(title=title, damage_type=dmg or "")
    raw_range = hero_record.get("range")
    if raw_range is not None:
        hero["default_range"] = int(raw_range)
    for skill in hero_record.get("skills", []):
        normalize_skill_description(skill)
        name = (skill.get("name") or "").strip()
        section = skill.get("section") or ""
        if name and section:
            hero["skill_name_to_section"][name] = section
        hero["skill_chunks"].extend(skill_chunks_from_skill(skill))
    return hero

def load_skills_by_title_from_records(
    heroes: list[dict],
) -> dict[str, list[SkillMetaRecord]]:
    from heroes_io import render_hero_block
    from .skill_meta import load_skill_meta

    skills_by_title: dict[str, list[SkillMetaRecord]] = {}
    for hero in heroes:
        block = render_hero_block(hero)
        skills_by_title[hero["title"]] = load_skill_meta(block)
    return skills_by_title

def load_skills_by_title_from_blocks(
    blocks: list[str],
) -> dict[str, list[SkillMetaRecord]]:
    skills_by_title: dict[str, list[SkillMetaRecord]] = {}
    from .skill_meta import load_skill_meta

    for block in blocks:
        title = block.splitlines()[0].replace("## ", "").strip()
        skills_by_title[title] = load_skill_meta(block)
    return skills_by_title

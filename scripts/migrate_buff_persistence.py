#!/usr/bin/env python3
"""Assign persistence to positive stat buffs in skill effect sidecars."""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

import buff_persistence as bp
import heroes_io as io
import skill_effects_store as ses

CONSUMER_REQUIRE_LABEL = "Temporary ally stat buffs"
OLD_REQUIRE_LABEL = "Ally stat buffs"

# Manual persistence for ally stat buffs the text classifier cannot resolve.
PERSISTENCE_OVERRIDES: dict[tuple[str, str, str, str], str] = {
    ("Aliceth", "Skill1", "base", "Attack range"): "permanent",
    ("Dunlingr", "Ex. Skill", "ex+5", "ATK"): "temporary",
    ("Dunlingr", "Ex. Skill", "ex+15", "Haste"): "temporary",
    ("Gunnar", "Unlocks at Legendary+", "legendary+", "Ranged DEF"): "permanent",
    ("Gunnar", "Unlocks at Legendary+", "legendary+", "Vitality"): "permanent",
    ("Gwyneth", "Ultimate", "base", "ATK"): "permanent",
    ("Gwyneth", "Ex. Skill", "mythic+", "ATK"): "temporary",
    ("Himmel", "Skill2", "base", "Basic stats"): "permanent",
    ("Isabella", "Ultimate", "base", "Phys DEF"): "temporary",
    ("Isabella", "Ultimate", "base", "Magic DEF"): "temporary",
    ("Isabella", "Ultimate", "base", "ATK SPD"): "temporary",
    ("Isabella", "Ultimate", "base", "Haste"): "temporary",
    ("Isabella", "Ultimate", "base", "Vitality"): "temporary",
    ("Kazim", "Ex. Skill", "mythic+", "ATK"): "permanent",
    ("Lamentis", "Unlocks at Legendary+", "legendary+", "ATK SPD"): "permanent",
    ("Lucca", "Ex. Skill", "mythic+", "ATK"): "permanent",
    ("Marilee", "Ex. Skill", "ex+10", "ATK"): "permanent",
    ("Mikola", "Ex. Skill", "ex+10", "Vitality"): "temporary",
    ("Phraesto", "Skill2", "base", "Max HP"): "temporary",
    ("Ravion", "Skill1", "base", "ATK"): "temporary",
    ("Solise", "Skill1", "base", "ATK"): "permanent",
    ("Solise", "Ex. Skill", "mythic+", "DEF"): "permanent",
    ("Solise", "Ex. Skill", "mythic+", "Magic DEF"): "permanent",
    ("Twins", "Ex. Skill", "mythic+", "Vitality"): "permanent",
    ("Dunlingr", "Ultimate", "supreme+", "ATK SPD"): "temporary",
    ("Dunlingr", "Ultimate", "supreme+", "Lifedrain"): "temporary",
    ("Hepler", "Skill1", "base", "Haste"): "temporary",
    ("Kazim", "Skill2", "base", "Haste"): "temporary",
    ("Mikola", "Ultimate", "base", "Haste"): "temporary",
}


def _skill_text(skill: dict) -> str:
    desc = ses.canonical_skill_description(skill)
    return json.dumps(desc, ensure_ascii=False)


def _rename_consumer_requires(doc: dict) -> bool:
    changed = False
    for entry in doc.get("skills", {}).values():
        for tier_data in entry.get("tiers", {}).values():
            for req in tier_data.get("special_requires", []):
                if req.get("label") == OLD_REQUIRE_LABEL:
                    req["label"] = CONSUMER_REQUIRE_LABEL
                    changed = True
    return changed


def migrate_sidecar(doc: dict, hero_record: dict) -> bool:
    hero_short = ses.short_name(hero_record["title"])
    skills_by_section = {
        skill["section"]: skill for skill in hero_record.get("skills", [])
    }
    changed = _rename_consumer_requires(doc)

    for section, entry in doc.get("skills", {}).items():
        skill = skills_by_section.get(section)
        text = _skill_text(skill) if skill else ""
        tiers = entry.get("tiers", {})
        for tier_key, tier_data in tiers.items():
            for bucket in ("effects", "summon_effects"):
                for effect in tier_data.get(bucket, []):
                    label = effect.get("label") or ""
                    if label not in bp.POSITIVE_STAT_BUFF_LABELS and effect.get(
                        "type"
                    ) != "stat_mod":
                        continue
                    if bp.is_positive_stat_buff_effect(effect):
                        key = (
                            hero_short,
                            section,
                            tier_key,
                            (effect.get("name") or ""),
                        )
                        override = PERSISTENCE_OVERRIDES.get(key)
                        classified = (
                            override
                            if override
                            else bp.classify_persistence(effect, text)
                        )
                    else:
                        classified = "permanent"
                    if effect.get("persistence") != classified:
                        effect["persistence"] = classified
                        changed = True
        before = json.dumps(tiers, sort_keys=True)
        bp.inherit_persistence_in_section(tiers)
        if json.dumps(tiers, sort_keys=True) != before:
            changed = True

    return changed


def main() -> int:
    raw = io.load_heroes_data()
    heroes_by_short = {
        ses.short_name(h["title"]): h for h in raw["heroes"]
    }
    updated = 0
    for path in sorted(ses.SKILL_EFFECTS_DIR.glob("*.json")):
        doc = json.loads(path.read_text(encoding="utf-8"))
        hero_short = path.stem
        record = heroes_by_short.get(hero_short)
        if record is None and hero_short == "Twins":
            record = next(
                h for h in raw["heroes"] if h["title"].startswith("Elijah")
            )
        if record is None:
            print(f"skip {hero_short}: no heroes_data record")
            continue
        if migrate_sidecar(doc, record):
            ses.save_sidecar(record["title"], doc)
            updated += 1
            print(f"updated {hero_short}")
    print(f"done: {updated} sidecars updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

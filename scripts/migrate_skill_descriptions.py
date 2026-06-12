#!/usr/bin/env python3
"""One-shot migration: flat skill descriptions -> structured objects."""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import heroes_io as io


def migrate_document(data: dict) -> int:
    count = 0
    for hero in data.get("heroes", []):
        for skill in hero.get("skills", []):
            before = skill.get("description")
            io.normalize_skill_description(skill)
            if before != skill.get("description"):
                count += 1
    return count


def main() -> int:
    data = io.load_json(io.HEROES_DATA)
    before_md = io.reconstruct_heroes_md(data)
    changed = migrate_document(data)
    after_md = io.reconstruct_heroes_md(data)
    if before_md != after_md:
        print("ERROR: Heroes.md would change after migration", file=sys.stderr)
        return 1
    io.save_json(io.HEROES_DATA, data)
    print(
        f"Migrated {changed} skills in {io.HEROES_DATA.relative_to(io.ROOT)} "
        f"(Heroes.md unchanged)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

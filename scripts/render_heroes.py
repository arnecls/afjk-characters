#!/usr/bin/env python3
"""Render Heroes.md from heroes_data.json.

Pure view: re-emits the Yaphalla skill document (skills only, no summaries).
No analysis happens here.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import heroes_io as io

HEROES_OUT = io.HEROES_MD


def main() -> None:
    data = io.load_heroes_data()
    content = io.reconstruct_heroes_md(data)
    HEROES_OUT.write_text(content, encoding="utf-8")
    print(
        f"Wrote {HEROES_OUT.relative_to(io.ROOT)} "
        f"({len(content.splitlines())} lines, {len(data['heroes'])} heroes)"
    )


if __name__ == "__main__":
    main()

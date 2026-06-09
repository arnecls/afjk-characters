#!/usr/bin/env python3
"""Download hero portraits and faction/class icons from Yaphalla into site/assets/."""

from __future__ import annotations

import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import heroes_io as io

# Display name -> Yaphalla hex image filename (without .png).
YAPHALLA_PORTRAIT_NAMES: dict[str, str] = {
    "Twins": "Elijah & Lailah",
    "Galahad": "Gala",
}

YAPHALLA_BASE = "https://www.yaphalla.com"
PORTRAITS_DIR = io.ROOT / "site" / "assets" / "portraits"
ICONS_DIR = io.ROOT / "site" / "assets" / "icons"
HEROES_JSON = io.ROOT / "site" / "data" / "heroes.json"


def _http_get(url: str) -> bytes | None:
    req = urllib.request.Request(
        url, headers={"User-Agent": "afkj-heroes-site/1.0"}
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.read()
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return None
        raise


def _yaphalla_url(path: str) -> str:
    return YAPHALLA_BASE + path


def _portrait_path(name: str) -> str:
    encoded = urllib.parse.quote(name, safe="")
    return f"/assets/images/hexes/unit/{encoded}.png"


def download_file(url: str, dest: Path) -> bool:
    if dest.exists():
        return False
    data = _http_get(url)
    if data is None:
        print(f"  missing {url}")
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    print(f"  saved {dest.relative_to(io.ROOT)}")
    return True


def _icon_filename(value: str) -> str:
    return value.lower().replace(" ", "")


def main() -> None:
    if not HEROES_JSON.exists():
        print(f"Run render_site.py first ({HEROES_JSON.name} missing)")
        sys.exit(1)

    payload = json.loads(HEROES_JSON.read_text(encoding="utf-8"))
    heroes = payload.get("heroes", [])
    downloaded = 0
    skipped = 0

    factions: set[str] = set()
    classes: set[str] = set()

    for hero in heroes:
        name = hero["name"]
        yaphalla_name = YAPHALLA_PORTRAIT_NAMES.get(name, name)
        dest = PORTRAITS_DIR / f"{name}.png"
        url = _yaphalla_url(_portrait_path(yaphalla_name))
        if download_file(url, dest):
            downloaded += 1
        else:
            if dest.exists():
                skipped += 1
        if hero.get("faction"):
            factions.add(hero["faction"])
        if hero.get("class"):
            classes.add(hero["class"])

    for faction in sorted(factions):
        fname = _icon_filename(faction)
        dest = ICONS_DIR / "factions" / f"{fname}.png"
        url = _yaphalla_url(f"/assets/images/factions/{fname}.png")
        if download_file(url, dest):
            downloaded += 1
        elif dest.exists():
            skipped += 1

    for cls in sorted(classes):
        fname = _icon_filename(cls)
        dest = ICONS_DIR / "class" / f"{fname}.png"
        url = _yaphalla_url(f"/assets/images/class/{fname}.png")
        if download_file(url, dest):
            downloaded += 1
        elif dest.exists():
            skipped += 1

    print(
        f"Portraits/icons: {downloaded} downloaded, "
        f"{skipped} already cached ({len(heroes)} heroes)"
    )


if __name__ == "__main__":
    main()

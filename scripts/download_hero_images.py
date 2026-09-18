#!/usr/bin/env python3
"""Download shared icons and hero portraits into site/assets/.

Portraits are resolved from each hero's Fandom gallery combat icon. The
gallery API may return WebP bytes for an asset whose site path ends in
``.png``; both PNG and WebP are valid browser assets here.
"""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import heroes_io as io

YAPHALLA_BASE = "https://www.yaphalla.com"
FANDOM_API = "https://afk-journey.fandom.com/api.php"
ICONS_DIR = io.ROOT / "site" / "assets" / "icons"
PORTRAITS_DIR = io.ROOT / "site" / "assets" / "portraits"
HEROES_JSON = io.ROOT / "site" / "data" / "heroes.json"
ROSTER_JSON = io.ROOT / "data" / "roster.json"

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
JPEG_SIGNATURE = b"\xff\xd8\xff"
WEBP_SIGNATURE = b"RIFF"


def _http_get(
    url: str,
    user_agent: str = "afkj-heroes-site/1.0",
) -> bytes | None:
    req = urllib.request.Request(
        url, headers={"User-Agent": user_agent}
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


def _fandom_api_url(params: dict[str, str]) -> str:
    query = urllib.parse.urlencode({"format": "json", **params})
    return f"{FANDOM_API}?{query}"


def _normalise_asset_name(value: str) -> str:
    return "".join(char.lower() for char in value if char.isalnum())


def _is_image_asset(data: bytes) -> bool:
    if data.startswith(PNG_SIGNATURE) or data.startswith(JPEG_SIGNATURE):
        return True
    return (
        data.startswith(WEBP_SIGNATURE)
        and len(data) >= 12
        and data[8:12] == b"WEBP"
    )


def _portrait_title_matches(title: str, names: list[str]) -> bool:
    filename = title.rsplit(":", 1)[-1].rsplit("/", 1)[-1]
    stem = filename.rsplit(".", 1)[0]
    wanted = {
        "hero" + _normalise_asset_name(name)
        for name in names
        if name
    }
    return _normalise_asset_name(stem) in wanted


def _gallery_image_title(
    page_payload: dict,
    names: list[str],
) -> str | None:
    pages = (page_payload.get("query") or {}).get("pages") or {}
    for page in pages.values():
        for image in page.get("images") or []:
            title = image.get("title")
            if isinstance(title, str) and _portrait_title_matches(title, names):
                return title
    return None


def _add_original_format(url: str) -> str:
    parts = urllib.parse.urlsplit(url)
    query = urllib.parse.parse_qsl(parts.query, keep_blank_values=True)
    query = [(key, value) for key, value in query if key != "format"]
    query.append(("format", "original"))
    return urllib.parse.urlunsplit(
        parts._replace(query=urllib.parse.urlencode(query))
    )


def _fandom_portrait_url(
    display_name: str,
    aliases: list[str] | None = None,
) -> str | None:
    names = [display_name, *(aliases or [])]
    for name in names:
        page = f"{name}/Gallery"
        payload = json.loads(
            _http_get(
                _fandom_api_url(
                    {
                        "action": "query",
                        "titles": page,
                        "prop": "images",
                        "imlimit": "max",
                    }
                ),
                user_agent="afkj-heroes-site/1.0",
            )
            or b"{}"
        )
        title = _gallery_image_title(payload, names)
        if not title:
            continue
        image_payload = json.loads(
            _http_get(
                _fandom_api_url(
                    {
                        "action": "query",
                        "titles": title,
                        "prop": "imageinfo",
                        "iiprop": "url|mime",
                    }
                ),
                user_agent="afkj-heroes-site/1.0",
            )
            or b"{}"
        )
        pages = (image_payload.get("query") or {}).get("pages") or {}
        for image_page in pages.values():
            imageinfo = image_page.get("imageinfo") or []
            if imageinfo and isinstance(imageinfo[0].get("url"), str):
                return _add_original_format(imageinfo[0]["url"])
    return None


def portrait_path(display_name: str, portraits_dir: Path = PORTRAITS_DIR) -> Path:
    return portraits_dir / f"{display_name}.png"


def portrait_is_valid(
    display_name: str,
    portraits_dir: Path = PORTRAITS_DIR,
) -> bool:
    path = portrait_path(display_name, portraits_dir)
    return path.is_file() and _is_image_asset(path.read_bytes())


def validate_portraits(
    display_names: list[str],
    portraits_dir: Path = PORTRAITS_DIR,
) -> list[str]:
    """Return display names whose portrait asset is missing or invalid."""
    return [
        display_name
        for display_name in display_names
        if not portrait_is_valid(display_name, portraits_dir)
    ]


def download_portrait(
    display_name: str,
    aliases: list[str] | None = None,
    portraits_dir: Path = PORTRAITS_DIR,
) -> str:
    """Ensure one portrait exists and return its asset status."""
    dest = portrait_path(display_name, portraits_dir)
    if portrait_is_valid(display_name, portraits_dir):
        return "cached"

    try:
        url = _fandom_portrait_url(display_name, aliases)
    except OSError as exc:
        print(f"  unavailable Fandom portrait for {display_name}: {exc}")
        return "missing"
    if url is None:
        print(f"  missing Fandom portrait for {display_name}")
        return "missing"

    try:
        data = _http_get(url, user_agent="afkj-heroes-site/1.0")
    except OSError as exc:
        print(f"  unavailable Fandom portrait for {display_name}: {exc}")
        return "missing"
    if data is None or not _is_image_asset(data):
        print(f"  invalid Fandom portrait for {display_name}")
        return "missing"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    try:
        shown_path = dest.relative_to(io.ROOT)
    except ValueError:
        shown_path = dest
    print(f"  saved {shown_path}")
    return "downloaded"


def _roster_aliases() -> dict[str, list[str]]:
    if not ROSTER_JSON.is_file():
        return {}
    payload = json.loads(ROSTER_JSON.read_text(encoding="utf-8"))
    return {
        entry["display_name"]: list(entry.get("aliases") or [])
        for entry in payload.get("heroes") or []
        if isinstance(entry.get("display_name"), str)
    }


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
        print(f"Run just views first ({HEROES_JSON.name} missing)")
        sys.exit(1)

    payload = json.loads(HEROES_JSON.read_text(encoding="utf-8"))
    heroes = payload.get("heroes", [])
    downloaded = 0
    skipped = 0
    missing_portraits: list[str] = []
    aliases_by_name = _roster_aliases()

    for hero in heroes:
        display_name = hero.get("name")
        if not isinstance(display_name, str) or not display_name:
            continue
        result = download_portrait(
            display_name,
            aliases_by_name.get(display_name),
        )
        if result == "downloaded":
            downloaded += 1
        elif result == "cached":
            skipped += 1
        else:
            missing_portraits.append(display_name)

    factions: set[str] = set()
    classes: set[str] = set()

    for hero in heroes:
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
        f"Assets: {downloaded} downloaded, "
        f"{skipped} already cached ({len(heroes)} heroes)"
    )
    if missing_portraits:
        print(
            "Missing or invalid portraits: "
            + ", ".join(missing_portraits),
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()

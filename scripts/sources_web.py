#!/usr/bin/env python3
"""Live downloaders for hero data sources (stdlib only).

- ``fetch_fandom()`` reads wikitext from the AFK Journey fandom MediaWiki API
  (https://afk-journey.fandom.com/api.php). This is the baseline: translated
  skill text plus Skill Range and Initial Energy.
- ``fetch_yaphalla()`` scrapes hero pages from https://www.yaphalla.com/heroes.
  Used only to fill gaps in the Fandom record during ``heroes_io.merge_sources``.
- ``fetch_prydwen_tiers()`` scrapes meta tiers from Prydwen character pages
  (https://www.prydwen.gg/afk-journey/characters), aligned with their tier list.

Both hero fetchers return records in the same structure as ``heroes_io.parse_md``
so the results can be merged by ``heroes_io.merge_sources``.

These are Python ports of the former ``scripts/generate-heroes2-md.js`` and
``scripts/generate-heroes-md.js``. Network access is required.
"""

from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

FANDOM_API = "https://afk-journey.fandom.com/api.php"
YAPHALLA_BASE = "https://www.yaphalla.com/heroes"
PRYDWEN_BASE = "https://www.prydwen.gg/afk-journey/characters"
PRYDWEN_TIER_LIST_URL = "https://www.prydwen.gg/afk-journey/tier-list"
CONCURRENCY = 4

PRYDWEN_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

# Fandom roster name -> Prydwen URL slug when they differ.
PRYDWEN_SLUG_ALIASES: dict[str, str] = {
    "Elijah & Lailah": "elijah-and-lailah",
}

_PRYDWEN_RATING_RE = re.compile(
    r'<div class="rating-box[^"]*">\s*([^<]+)</div></span><p>([^<]+)</p>',
    re.I,
)

_PRYDWEN_MODE_KEYS = {
    "afk stages": "afk_stages",
    "dream realm": "dream_realm",
    "dream realm (endless)": "dream_realm_endless",
    "pvp": "pvp",
}

FANDOM_HEADER = (
    "# AFK Journey Heroes\n"
    "\n"
    "Skill data sourced from "
    "[AFK Journey Wiki](https://afk-journey.fandom.com/wiki/Hero/List).\n"
    "Summaries live in [heroes-overview.md](heroes-overview.md) "
    "(see `scripts/generate-heroes-overview.py`).\n"
)

# Playable heroes from Category:Playable_Heroes (alphabetical).
HERO_NAMES = [
    "Aliceth", "Alna", "Alsa", "Antandra", "Arden", "Atalanta", "Athalia",
    "Aurora", "Baelran", "Berial", "Bonnie", "Brutus", "Bryon", "Callan",
    "Carolina", "Cassadee", "Cecia", "Chippy", "Contess", "Cryonaia", "Cyran",
    "Daimon", "Damian", "Dionel", "Dunlingr", "Eironn", "Elijah & Lailah",
    "Evie", "Faramor", "Fay", "Florabelle", "Frieren", "Galahad", "Gerda",
    "Granny Dahnie", "Gunnar", "Gwyneth", "Hammie", "Harak", "Hepler",
    "Hewynn", "Himmel", "Hodgkin", "Hugin", "Igor", "Indris", "Isabella",
    "Kafra", "Koko", "Kordan", "Korin", "Kruger", "Kulu", "Laios", "Lenya",
    "Lily May", "Lorsan", "Lucca", "Lucius", "Lucy", "Ludovic", "Lumont",
    "Lyca", "Marcille", "Marilee", "Mehira", "Mikola", "Mirael", "Nara",
    "Natsu", "Nazrik", "Nerion", "Niru", "Odie", "Pandora", "Pang", "Parisa",
    "Perseus", "Phraesto", "Pippa", "Ravion", "Reinier", "Rhys", "Rowan",
    "Saida", "Salazer", "Satrana", "Scarlita", "Seth", "Shadewing", "Shakir",
    "Shemira", "Silven", "Silvina", "Sinbad", "Smokey & Meerky", "Solise",
    "Sonja", "Soren", "Sylphira", "Talene", "Tasi", "Temesia", "Thador",
    "Thoran", "Tilaya", "Ulmus", "Vala", "Valen", "Valka", "Velara",
    "Viperian", "Walker", "Zandrok", "Zanie", "Zorya",
]

SKILL_TYPE_MAP = {
    "Ultimate": ("Ultimate", "Unlocks at Level 1"),
    "Skill I": ("Skill1", "Unlocks at Level 11"),
    "Skill II": ("Skill2", "Unlocks at Level 31"),
    "Hero Focus": ("Unlocks at Legendary+", "Unlocks at Legendary+"),
    "Exclusive Skill": ("Ex. Skill", "Unlocks at Mythic+"),
    "Enhance Force": ("Unlocks at Supreme+", "Unlocks at Supreme+"),
}


def _http_get(url: str, user_agent: str, *, retries: int = 1) -> str:
    headers = {"User-Agent": user_agent, "Accept": "text/html"}
    last_err: OSError | None = None
    for attempt in range(retries):
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            last_err = exc
            if exc.code in (403, 429) and attempt + 1 < retries:
                time.sleep(1.5 * (attempt + 1))
                continue
            raise
        except OSError as exc:
            last_err = exc
            if attempt + 1 < retries:
                time.sleep(1.5 * (attempt + 1))
                continue
            raise
    assert last_err is not None
    raise last_err


def _map_pool(items, fn):
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as pool:
        return list(pool.map(fn, items))


# ---------------------------------------------------------------------------
# Fandom (MediaWiki wikitext)
# ---------------------------------------------------------------------------


def process_wikitext(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"'''([^']+)'''", r"\1", text)
    text = re.sub(r"''([^']+)''", r"\1", text)
    text = re.sub(r"\{\{b\|([^}]+)\}\}", r"\1", text)
    text = re.sub(r"\{\{ATK\|([^}]+)\}\}", r"\1 (ATK-based)", text)
    text = re.sub(r"\{\{HP\|([^}]+)\}\}", r"\1 (HP-based)", text)
    text = re.sub(r"\{\{PWR\|([^|}]+)(?:\|[^}]*)?\}\}", r"\1", text)
    text = re.sub(r"\{\{e\|([^}]+)\}\}", r"\1", text)
    text = re.sub(r"\{\{([A-Z][A-Za-z0-9-]+)\}\}", r"\1", text)
    text = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)
    text = re.sub(r"\[\[(?:File|Image):[^\]]+\]\]", "", text)
    text = re.sub(r"\{\{[^}]+\}\}", "", text)
    text = re.sub(r"<br\s*/?>", " ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _normalise_cd(cd: str | None) -> str | None:
    if not cd:
        return None
    s = cd.strip()
    return f"{s}s" if re.fullmatch(r"\d+(\.\d+)?", s) else s


def _format_range(rng: str | None) -> str | None:
    if not rng:
        return None
    s = rng.strip()
    if re.fullmatch(r"\d+", s):
        return "1 tile" if s == "1" else f"{s} tiles"
    return s


def _extract_templates(wikitext: str, template_name: str) -> list[str]:
    results: list[str] = []
    open_str = "{{" + template_name + "\n"
    pos = 0
    while pos < len(wikitext):
        start = wikitext.find(open_str, pos)
        if start == -1:
            break
        depth = 0
        i = start
        while i < len(wikitext) - 1:
            if wikitext[i] == "{" and wikitext[i + 1] == "{":
                depth += 1
                i += 2
            elif wikitext[i] == "}" and wikitext[i + 1] == "}":
                depth -= 1
                i += 2
                if depth == 0:
                    break
            else:
                i += 1
        inner_start = start + len(open_str)
        results.append(wikitext[inner_start : i - 2])
        pos = i
    return results


def _parse_fields(inner: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    current_key: str | None = None
    current_lines: list[str] = []
    for line in inner.split("\n"):
        if line.startswith("|"):
            if current_key is not None:
                fields[current_key] = "\n".join(current_lines).strip()
            eq = line.find("=")
            if eq != -1:
                current_key = line[1:eq].strip()
                current_lines = [line[eq + 1 :].strip()]
            else:
                current_key = line[1:].strip()
                current_lines = []
        elif current_key is not None:
            current_lines.append(line)
    if current_key is not None:
        fields[current_key] = "\n".join(current_lines).strip()
    return fields


def _parse_level_upgrades(buffs_text: str) -> list[dict]:
    if not buffs_text:
        return []
    lines = [
        ln.strip()
        for ln in buffs_text.split("\n")
        if ln.strip().startswith("*") or ln.strip().startswith("#")
    ]
    out: list[dict] = []
    for i, line in enumerate(lines):
        raw = re.sub(r"^[*#]+\s*", "", line)
        seq = i + 2
        m = re.match(r"^Unlocks at Level (\d+):\s*([\s\S]+)$", raw)
        if m:
            out.append(
                {"level": str(seq), "unlock": f"Unlocks at Level {m.group(1)}",
                 "text": process_wikitext(m.group(2))}
            )
            continue
        m = re.match(r"^Unlocks at Exclusive Weapon Level (\d+):\s*([\s\S]+)$", raw)
        if m:
            out.append(
                {"level": str(seq), "unlock": f"Unlocks at EX. +{m.group(1)}",
                 "text": process_wikitext(m.group(2))}
            )
            continue
        m = re.match(r"^Unlocks at Exclusive Equipment Refine (\d+):\s*([\s\S]+)$", raw)
        if m:
            out.append(
                {"level": str(seq), "unlock": f"Unlocks at R{m.group(1)}",
                 "text": process_wikitext(m.group(2))}
            )
            continue
        m = re.match(r"^Level (\d+):\s*([\s\S]+)$", raw)
        if m:
            out.append(
                {"level": m.group(1), "unlock": None,
                 "text": process_wikitext(m.group(2))}
            )
            continue
        out.append({"level": str(seq), "unlock": None, "text": process_wikitext(raw)})
    return out


def _parse_fandom_hero(wikitext: str, hero_name: str) -> dict:
    infoboxes = _extract_templates(wikitext, "Character Infobox")
    infobox = _parse_fields(infoboxes[0]) if infoboxes else {}

    name = (infobox.get("name") or hero_name).strip()
    subtitle = (infobox.get("title") or "").strip()
    faction = (infobox.get("faction") or "").strip()
    hero_class = (infobox.get("class") or "").strip()
    damage = (infobox.get("damage") or "").strip()
    description = (
        process_wikitext(infobox["description"]) if infobox.get("description") else ""
    )

    skills: list[dict] = []
    for inner in _extract_templates(wikitext, "Skill"):
        fields = _parse_fields(inner)
        skill_type = (fields.get("type") or "").strip()
        type_info = SKILL_TYPE_MAP.get(skill_type)
        if not type_info:
            continue
        section, unlock = type_info

        meta: dict[str, str] = {}
        cd = _normalise_cd(fields.get("cd"))
        if cd and float(re.match(r"[\d.]+", cd).group()) > 0:
            meta["Cooldown"] = cd
        icd = _normalise_cd(fields.get("icd"))
        if icd and float(re.match(r"[\d.]+", icd).group()) > 0:
            meta["Initial Cooldown"] = icd
        rng = _format_range(fields.get("range"))
        if rng:
            meta["Skill Range"] = rng
        if "energy" in fields:
            raw_energy = (fields.get("energy") or "").strip()
            if raw_energy != "":
                meta["Initial Energy"] = raw_energy

        def _skill_desc(raw: str) -> str:
            if not raw:
                return ""
            return re.sub(
                r" {2,}", " ", re.sub(r"\n+", " ", process_wikitext(raw))
            ).strip()

        skill_description = _skill_desc(fields.get("full", ""))
        skill_description_lite = _skill_desc(fields.get("lite", ""))
        skill_record: dict = {
            "section": section,
            "name": (fields.get("name") or skill_type).strip(),
            "unlock": unlock,
            "meta": meta,
            "description": skill_description,
            "levels": _parse_level_upgrades(fields.get("buffs", "")),
        }
        if skill_description_lite and skill_description_lite != skill_description:
            skill_record["description_lite"] = skill_description_lite

        skills.append(skill_record)

    title = f"{name} - {subtitle}" if subtitle else name
    tags = " · ".join([t for t in (faction, hero_class, damage) if t]) or None
    return {
        "title": title,
        "name": name,
        "tags": tags,
        "faction": faction or None,
        "class": hero_class or None,
        "damage_type": damage or None,
        "description": description,
        "skills": skills,
    }


def _fetch_fandom_wikitext(hero_name: str) -> str:
    page = hero_name.replace(" ", "_")
    url = (
        f"{FANDOM_API}?action=parse&page={urllib.parse.quote(page)}"
        f"&prop=wikitext&format=json"
    )
    data = json.loads(_http_get(url, "afkj-heroes-fandom/1.0"))
    if data.get("error"):
        raise RuntimeError(data["error"].get("info", data["error"].get("code")))
    return data.get("parse", {}).get("wikitext", {}).get("*", "")


def fetch_fandom() -> list[dict]:
    def one(name: str) -> dict:
        try:
            wikitext = _fetch_fandom_wikitext(name)
            hero = _parse_fandom_hero(wikitext, name)
            print(f"  fandom ✓ {name} ({len(hero['skills'])} skills)")
            return hero
        except Exception as err:  # noqa: BLE001
            print(f"  fandom ✗ {name}: {err}")
            return {
                "title": name, "name": name, "tags": None, "faction": None,
                "class": None, "damage_type": None, "description": "", "skills": [],
            }

    return _map_pool(HERO_NAMES, one)


# ---------------------------------------------------------------------------
# Yaphalla (HTML + RSC payload)
# ---------------------------------------------------------------------------

_YAPHALLA_SLOTS = [
    ("ultimate", "Ultimate"),
    ("skill1", "Skill1"),
    ("skill2", "Skill2"),
    ("legendary", "Unlocks at Legendary+"),
    ("ex", "Ex. Skill"),
    ("supreme", "Unlocks at Supreme+"),
]


def _decode_entities(s: str) -> str:
    return (
        s.replace("&#x27;", "'")
        .replace("&amp;", "&")
        .replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("&quot;", '"')
    )


def _html_fragment_to_text(html: str) -> str:
    html = re.sub(r"<script[\s\S]*?</script>", "", html, flags=re.I)
    html = re.sub(r"<style[\s\S]*?</style>", "", html, flags=re.I)
    html = re.sub(r"<br\s*/?>", " ", html, flags=re.I)
    html = re.sub(r"<[^>]+>", " ", html)
    html = re.sub(r"\s+", " ", html)
    return _decode_entities(html.strip())


def _clean_rendered_text(raw: str) -> str:
    raw = re.sub(r"Lite\s*Full", "", raw, flags=re.I)
    raw = re.sub(
        r"A value determined by the caster's ATK\.?", "(ATK-based)", raw, flags=re.I
    )
    raw = re.sub(
        r"A value determined by the caster's HP\.?", "(HP-based)", raw, flags=re.I
    )
    raw = re.sub(
        r"Increase in this stat with each point of (?:Ultimate|Skill) Power gained\.?",
        "", raw, flags=re.I,
    )
    return re.sub(r"\s+", " ", raw).strip()


def _simplify_rsc_text(text: str) -> str:
    text = re.sub(r"</?ATK>", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\{[^}]+\}", "(scaled)", text)
    return text


def _escape_re(s: str) -> str:
    return re.sub(r"[.*+?^${}()|[\]\\]", lambda m: "\\" + m.group(), s)


def _fetch_yaphalla_hero(name: str) -> dict:
    url = f"{YAPHALLA_BASE}/{urllib.parse.quote(name)}"
    html = _http_get(url, "Mozilla/5.0 (afkj-heroes-yaphalla/1.0)")

    title_m = re.search(r"<h[12][^>]*>([^<]+ - [^<]+)</h[12]>", html)
    title = _decode_entities(title_m.group(1).strip()) if title_m else name
    desc_m = re.search(r'<meta name="description" content="([^"]*)"', html)
    description = _decode_entities(desc_m.group(1)) if desc_m else ""

    block_re = re.compile(
        r'<div class="container-primary flex flex-col size-full">'
        r"([\s\S]*?)</div>\s*</div>\s*</div>"
    )
    blocks = [m.group(1) for m in block_re.finditer(html) if "<h3>" in m.group(1)]

    skills: list[dict] = []
    for i, (_, section) in enumerate(_YAPHALLA_SLOTS):
        if i >= len(blocks):
            break
        fragment = blocks[i]
        name_m = re.search(r"<h3>([^<]+)</h3>", fragment)
        skill_name = _decode_entities(name_m.group(1).strip()) if name_m else ""
        full = _clean_rendered_text(_html_fragment_to_text(fragment))
        full = re.sub(
            r"^(?:Ultimate|Skill\s*[12]|EX\.\s*Skill)\s*-\s*Unlocks at\s+Level\s+\d+\s*",
            "", full, flags=re.I,
        )
        full = re.sub(r"^Unlocks at\s+(?:Legendary\+|Mythic\+|Supreme\+)\s*", "", full, flags=re.I)
        if skill_name:
            full = re.sub(rf"^{_escape_re(skill_name)}\s*", "", full, flags=re.I).strip()

        meta_d: dict[str, str] = {}
        cd = re.search(r"Cooldown:\s*(\d+)\s*s", full, re.I)
        icd = re.search(r"Initial Cooldown:\s*(\d+)\s*s", full, re.I)
        if cd:
            meta_d["Cooldown"] = f"{cd.group(1)}s"
            full = re.sub(r"Cooldown:\s*\d+\s*s", "", full, flags=re.I).strip()
        if icd:
            meta_d["Initial Cooldown"] = f"{icd.group(1)}s"
            full = re.sub(r"Initial Cooldown:\s*\d+\s*s", "", full, flags=re.I).strip()

        skills.append(
            {
                "section": section,
                "name": skill_name,
                "unlock": _yaphalla_unlock_label(section),
                "meta": meta_d,
                "description": _simplify_rsc_text(full),
                "levels": [],
            }
        )

    # Faction / class / damage are no longer exposed by Yaphalla as JSON; they
    # come from the Fandom baseline during merge. Yaphalla only gap-fills when
    # Fandom fields are missing.
    return {
        "title": title,
        "name": name,
        "tags": None,
        "faction": None,
        "class": None,
        "damage_type": None,
        "description": description,
        "skills": skills,
    }


def _yaphalla_unlock_label(section: str) -> str:
    return {
        "Ultimate": "Unlocks at Level 1",
        "Skill1": "Unlocks at Level 11",
        "Skill2": "Unlocks at Level 31",
        "Unlocks at Legendary+": "Unlocks at Legendary+",
        "Ex. Skill": "Unlocks at Mythic+",
        "Unlocks at Supreme+": "Unlocks at Supreme+",
    }.get(section, section)


def _yaphalla_hero_names() -> list[str]:
    """Scrape the hero roster from the /heroes index page."""
    html = _http_get(YAPHALLA_BASE, "Mozilla/5.0 (afkj-heroes-yaphalla/1.0)")
    names = re.findall(r'href="/heroes/([^"/?]+)"', html)
    skip = {"Elijah", "Lailah", "Phraesto Clone", "Zanie Turret"}
    seen: list[str] = []
    for raw in names:
        name = urllib.parse.unquote(raw)
        if name not in skip and name not in seen:
            seen.append(name)
    return sorted(seen)


def fetch_yaphalla() -> list[dict]:
    names = _yaphalla_hero_names()

    def one(name: str) -> dict:
        try:
            hero = _fetch_yaphalla_hero(name)
            print(f"  yaphalla ✓ {name} ({len(hero['skills'])} skills)")
            return hero
        except Exception as err:  # noqa: BLE001
            print(f"  yaphalla ✗ {name}: {err}")
            return {
                "title": name, "name": name, "tags": None, "faction": None,
                "class": None, "damage_type": None, "description": "", "skills": [],
            }

    return _map_pool(names, one)


# ---------------------------------------------------------------------------
# Prydwen (meta tier ratings)
# ---------------------------------------------------------------------------


def _prydwen_slug(name: str) -> str:
    alias = PRYDWEN_SLUG_ALIASES.get(name)
    if alias:
        return alias
    slug = name.lower().strip().replace("&", "and")
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def _normalize_prydwen_tier(text: str) -> str:
    tier = text.strip()
    tier = tier.replace("-plus", "+").replace("-minus", "-")
    return tier


def _parse_prydwen_ratings(html: str) -> dict[str, str] | None:
    """Parse General Ratings from a Prydwen character page."""
    if "General Ratings" not in html:
        return None
    ratings: dict[str, str] = {}
    for tier_raw, mode in _PRYDWEN_RATING_RE.findall(html):
        key = _PRYDWEN_MODE_KEYS.get(mode.strip().lower())
        if key:
            ratings[key] = _normalize_prydwen_tier(tier_raw)
    if len(ratings) != 4:
        return None
    return ratings


def _fetch_prydwen_hero_tiers(name: str) -> tuple[str, dict[str, str] | None]:
    slug = _prydwen_slug(name)
    url = f"{PRYDWEN_BASE}/{slug}"
    try:
        html = _http_get(url, PRYDWEN_USER_AGENT, retries=4)
    except OSError:
        return name, None
    return name, _parse_prydwen_ratings(html)


def fetch_prydwen_tiers(hero_names: list[str]) -> dict[str, dict[str, str]]:
    """Return meta tier ratings keyed by hero display name."""
    tiers_by_name: dict[str, dict[str, str]] = {}
    missing = list(hero_names)
    for round_idx in range(3):
        if not missing:
            break
        if round_idx:
            time.sleep(2.0 * round_idx)
        batch_missing: list[str] = []
        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(_fetch_prydwen_hero_tiers, missing))
        for name, tiers in results:
            if tiers:
                tiers_by_name[name] = tiers
            else:
                batch_missing.append(name)
        missing = batch_missing
    return tiers_by_name


if __name__ == "__main__":
    import sys

    which = sys.argv[1] if len(sys.argv) > 1 else "both"
    if which in ("fandom", "both"):
        f = fetch_fandom()
        print(f"fandom: {len(f)} heroes")
    if which in ("yaphalla", "both"):
        y = fetch_yaphalla()
        print(f"yaphalla: {len(y)} heroes")

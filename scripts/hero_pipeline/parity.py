"""Independent presentation-contract comparison for the pipeline rewrite.

Fixtures are frozen from hero-split ``b7d7ed2``. Relationship sections may
differ; numeric leaves and structurally compared text must match.
"""

from __future__ import annotations

import json
import math
import re
import unicodedata
from pathlib import Path
from typing import Any, Mapping

from .repository import Repository, current_repository

FIXTURE_DIR = Path(__file__).resolve().parent.parent / "fixtures" / "hero_split_b7d7ed2"
CONTRACT_NAME = "presentation-contract.json"

RELATIONSHIP_MARKDOWN_HEADINGS = (
    "Units improving",
    "Units benefitting most from",
    "Best overall replacement",
    "Buffs on allies",
    "Energy provider",
    "Healing",
    "Similar Skills",
    "Damage",
    "Debuffs on enemies",
    "Crowd Control",
)

SITE_RELATIONSHIP_KEYS = frozenset({"benefits_from", "replacements"})


def _plain(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _plain(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_plain(item) for item in value]
    return value


def normalize_text(value: str) -> str:
    """NFC, LF newlines, strip trailing spaces, keep wording exact."""
    text = unicodedata.normalize("NFC", value).replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.split("\n")]
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines) + ("\n" if value.endswith("\n") else "")


def _drop_relationship_markdown(markdown: str) -> str:
    lines = markdown.split("\n")
    kept: list[str] = []
    skipping = False
    for line in lines:
        if line.startswith("### ") or line.startswith("#### "):
            title = line.lstrip("#").strip()
            skipping = any(
                title.startswith(prefix)
                for prefix in RELATIONSHIP_MARKDOWN_HEADINGS
            )
        if skipping:
            continue
        kept.append(line)
    return normalize_text("\n".join(kept))


def _drop_site_relationships(payload: Any) -> Any:
    if not isinstance(payload, dict):
        return payload
    result = dict(payload)
    meta = dict(result.get("meta") or {})
    meta.pop("generated", None)
    result["meta"] = meta
    heroes = []
    for hero in result.get("heroes") or []:
        item = dict(hero)
        sections = dict(item.get("sections") or {})
        for key in SITE_RELATIONSHIP_KEYS:
            sections.pop(key, None)
        item["sections"] = sections
        heroes.append(item)
    result["heroes"] = heroes
    return result


def contract_hero(hero: Mapping[str, Any]) -> dict[str, Any]:
    """Return one hero's view-facing facts without relationship lists."""
    analysis = dict(hero.get("analysis") or {})
    analysis.pop("scoring", None)
    return {
        "id": hero["id"],
        "display_name": hero["display_name"],
        "slug": hero["slug"],
        "source": _plain(hero.get("source") or {}),
        "display": _plain(hero.get("display") or {}),
        "curated": _plain(hero.get("curated") or {}),
        "analysis": _plain(analysis),
    }


def contract_from_view(
    view: Mapping[str, Any],
    *,
    heroes_md: str,
    overview_md: str,
    overview_csv: str,
    site_heroes: Mapping[str, Any],
) -> dict[str, Any]:
    """Build the frozen presentation contract from rendered outputs."""
    return {
        "schema_version": 1,
        "heroes": [
            contract_hero(hero)
            for hero in sorted(view["heroes"], key=lambda item: item["id"])
        ],
        "heroes_md": normalize_text(heroes_md),
        "overview_md": _drop_relationship_markdown(overview_md),
        "overview_csv": normalize_text(overview_csv),
        "site_heroes": _drop_site_relationships(site_heroes),
    }


def load_contract(path: Path | None = None) -> dict[str, Any]:
    fixture = path or (FIXTURE_DIR / CONTRACT_NAME)
    return json.loads(fixture.read_text(encoding="utf-8"))


def write_contract(contract: Mapping[str, Any], path: Path | None = None) -> Path:
    fixture = path or (FIXTURE_DIR / CONTRACT_NAME)
    fixture.parent.mkdir(parents=True, exist_ok=True)
    fixture.write_text(
        json.dumps(contract, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return fixture


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _walk_numbers(value: Any, prefix: str = "") -> dict[str, float]:
    if _is_number(value):
        number = float(value)
        if math.isnan(number) or math.isinf(number):
            raise ValueError(f"non-finite numeric value at {prefix}")
        return {prefix: number}
    if isinstance(value, Mapping):
        items: dict[str, float] = {}
        for key, item in value.items():
            path = f"{prefix}.{key}" if prefix else str(key)
            items.update(_walk_numbers(item, path))
        return items
    if isinstance(value, list):
        items = {}
        for index, item in enumerate(value):
            items.update(_walk_numbers(item, f"{prefix}[{index}]"))
        return items
    return {}


def _walk_strings(value: Any, prefix: str = "") -> dict[str, str]:
    if isinstance(value, str):
        return {prefix: normalize_text(value)}
    if isinstance(value, Mapping):
        items: dict[str, str] = {}
        for key, item in value.items():
            path = f"{prefix}.{key}" if prefix else str(key)
            items.update(_walk_strings(item, path))
        return items
    if isinstance(value, list):
        items = {}
        for index, item in enumerate(value):
            items.update(_walk_strings(item, f"{prefix}[{index}]"))
        return items
    return {}


def compare_numbers(baseline: Any, current: Any, *, prefix: str = "") -> list[str]:
    before = _walk_numbers(baseline, prefix)
    after = _walk_numbers(current, prefix)
    errors: list[str] = []
    for key in sorted(set(before) - set(after)):
        errors.append(f"missing number {key}")
    for key in sorted(set(after) - set(before)):
        errors.append(f"added number {key}")
    for key in sorted(set(before) & set(after)):
        if before[key] != after[key]:
            errors.append(
                f"changed number {key}: {before[key]!r} -> {after[key]!r}"
            )
    return errors


def compare_strings(baseline: Any, current: Any, *, prefix: str = "") -> list[str]:
    before = _walk_strings(baseline, prefix)
    after = _walk_strings(current, prefix)
    errors: list[str] = []
    for key in sorted(set(before) - set(after)):
        errors.append(f"missing text {key}")
    for key in sorted(set(after) - set(before)):
        errors.append(f"added text {key}")
    for key in sorted(set(before) & set(after)):
        if before[key] != after[key]:
            errors.append(f"changed text {key}")
    return errors


_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_CODE_RE = re.compile(r"`([^`]+)`")


def markdown_structure(text: str) -> list[str]:
    """Ordered structural tokens for Markdown comparison."""
    tokens: list[str] = []
    for raw in normalize_text(text).split("\n"):
        line = raw.strip()
        if not line:
            continue
        heading = _HEADING_RE.match(line)
        if heading:
            tokens.append(f"h{len(heading.group(1))}:{heading.group(2)}")
            continue
        if line.startswith("- ") or line.startswith("* "):
            body = line[2:]
            tokens.append(f"li:{body}")
        else:
            tokens.append(f"p:{line}")
        for match in _LINK_RE.finditer(line):
            tokens.append(f"link:{match.group(1)}|{match.group(2)}")
        for match in _CODE_RE.finditer(line):
            tokens.append(f"code:{match.group(1)}")
    return tokens


def compare_markdown(baseline: str, current: str, *, label: str) -> list[str]:
    before = markdown_structure(_drop_relationship_markdown(baseline))
    after = markdown_structure(_drop_relationship_markdown(current))
    if before == after:
        return []
    errors = [f"{label} structure differs"]
    for index, (left, right) in enumerate(zip(before, after)):
        if left != right:
            errors.append(f"{label}[{index}]: {left} -> {right}")
            break
    if len(before) != len(after):
        errors.append(
            f"{label} token count {len(before)} -> {len(after)}"
        )
    return errors


def compare_contracts(
    baseline: Mapping[str, Any],
    current: Mapping[str, Any],
) -> list[str]:
    """Return errors when the presentation contract regresses."""
    errors: list[str] = []
    before_ids = [hero["id"] for hero in baseline["heroes"]]
    after_ids = [hero["id"] for hero in current["heroes"]]
    if before_ids != after_ids:
        errors.append(
            f"hero identity order changed: {before_ids} -> {after_ids}"
        )
        return errors
    after_by_id = {hero["id"]: hero for hero in current["heroes"]}
    for hero in baseline["heroes"]:
        other = after_by_id[hero["id"]]
        prefix = hero["id"]
        errors.extend(compare_numbers(hero, other, prefix=prefix))
        errors.extend(compare_strings(hero, other, prefix=prefix))
    errors.extend(
        compare_markdown(
            baseline["heroes_md"],
            current["heroes_md"],
            label="Heroes.md",
        )
    )
    errors.extend(
        compare_markdown(
            baseline["overview_md"],
            current["overview_md"],
            label="heroes-overview.md",
        )
    )
    if normalize_text(baseline["overview_csv"]) != normalize_text(
        current["overview_csv"]
    ):
        errors.append("heroes-overview.csv differs")
    errors.extend(
        compare_numbers(
            baseline["site_heroes"],
            current["site_heroes"],
            prefix="site",
        )
    )
    errors.extend(
        compare_strings(
            baseline["site_heroes"],
            current["site_heroes"],
            prefix="site",
        )
    )
    return errors


def relationship_invariant_errors(view: Mapping[str, Any]) -> list[str]:
    """Validate relationship lists without constraining membership."""
    known = {hero["id"] for hero in view["heroes"]}
    errors: list[str] = []
    for hero in view["heroes"]:
        hero_id = hero["id"]
        refs = hero.get("references") or {}
        rows = list(refs.get("synergies") or [])
        previous: float | None = None
        seen: list[str] = []
        for row in rows:
            provider = row.get("id") or row.get("provider_id")
            if provider not in known:
                errors.append(f"{hero_id}: unknown synergy provider {provider}")
            if provider == hero_id:
                errors.append(f"{hero_id}: self synergy")
            score = float(row.get("score", 0))
            if previous is not None and score > previous:
                errors.append(f"{hero_id}: synergy scores are not ordered")
            previous = score
            seen.append(str(provider))
        if len(seen) != len(set(seen)):
            errors.append(f"{hero_id}: duplicate synergy providers")
        for row in refs.get("beneficiaries") or []:
            other = row.get("id") or row.get("hero_id")
            if other not in known:
                errors.append(f"{hero_id}: unknown beneficiary {other}")
        for rows in (refs.get("replacements") or {}).values():
            for row in rows:
                other = row.get("id") or row.get("hero_id")
                if other not in known:
                    errors.append(f"{hero_id}: unknown replacement {other}")
    return errors


def snapshot_views(repository: Repository | None = None) -> dict[str, str]:
    """Read committed public view files as text."""
    repo = repository or current_repository()
    views: dict[str, str] = {}
    for relpath in (
        "Heroes.md",
        "heroes-overview.md",
        "heroes-overview.csv",
        "site/data/heroes.json",
    ):
        path = repo.root / relpath
        if path.is_file():
            views[relpath] = path.read_text(encoding="utf-8")
    return views

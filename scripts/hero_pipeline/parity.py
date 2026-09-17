"""Independent presentation-contract comparison for the pipeline rewrite.

Fixtures are frozen from hero-split ``b7d7ed2``. Compare displayed
semantics, including relationship membership, scores, and reasons.
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
SITE_FIXTURE_DIR = FIXTURE_DIR / "site" / "data"


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


def site_without_timestamp(payload: Mapping[str, Any] | Any) -> Any:
    """Drop only dynamic generation metadata from a site heroes document."""
    if not isinstance(payload, dict):
        return payload
    result = dict(payload)
    meta = dict(result.get("meta") or {})
    meta.pop("generated", None)
    result["meta"] = meta
    return result


def list_column_semantics(columns: Any) -> list[dict[str, Any]]:
    rows = columns if isinstance(columns, list) else []
    return [
        {
            "label": row.get("label"),
            "polarity": row.get("polarity"),
            "group": row.get("group"),
        }
        for row in rows
        if isinstance(row, Mapping)
    ]


def load_fixture_artifacts() -> dict[str, Any]:
    """Load the expanded b7d7ed2 public-view artifacts."""
    def read_text(name: str) -> str:
        return (FIXTURE_DIR / name).read_text(encoding="utf-8")

    def read_site(name: str) -> Any:
        path = SITE_FIXTURE_DIR / name
        if name.endswith(".json"):
            return json.loads(path.read_text(encoding="utf-8"))
        return path.read_text(encoding="utf-8")

    return {
        "heroes_md": normalize_text(read_text("Heroes.md")),
        "overview_md": normalize_text(read_text("heroes-overview.md")),
        "overview_csv": normalize_text(read_text("heroes-overview.csv")),
        "site_heroes": site_without_timestamp(read_site("heroes.json")),
        "site_csv": normalize_text(read_site("heroes-overview.csv")),
        "mix_synergy_index": read_site("mix-synergy-index.json"),
        "mix_config": read_site("mix-config.json"),
        "mix_role_prominence": read_site("mix-role-prominence.json"),
        "list_columns": list_column_semantics(read_site("list-columns.json")),
        "counter_filter_combos": read_site("counter_filter_combos.json"),
    }


def contract_hero(hero: Mapping[str, Any]) -> dict[str, Any]:
    """Return one hero's view-facing facts without internal scoring facts."""
    analysis = dict(hero.get("analysis") or {})
    analysis.pop("scoring", None)
    profile = dict(analysis.get("synergy_profile") or {})
    if profile:
        analysis["synergy_profile"] = {
            kind: [
                {
                    key: value
                    for key, value in dict(item).items()
                    if key != "grants"
                }
                for item in (profile.get(kind) or [])
            ]
            for kind in ("provides", "requires")
            if kind in profile
        }
    return {
        "id": hero["id"],
        "display_name": hero["display_name"],
        "slug": hero["slug"],
        "source": _plain(hero.get("source") or {}),
        "display": _plain(hero.get("display") or {}),
        "curated": _plain(hero.get("curated") or {}),
        "analysis": _plain(analysis),
        "references": _plain(hero.get("references") or {}),
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
        "overview_md": normalize_text(overview_md),
        "overview_csv": normalize_text(overview_csv),
        "site_heroes": site_without_timestamp(site_heroes),
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


def _list_key(item: Any, index: int) -> str:
    if isinstance(item, Mapping):
        for key in ("slug", "id", "provider_id", "hero_id", "category"):
            value = item.get(key)
            if value not in (None, ""):
                return f"[{key}={value}]"
    return f"[{index}]"


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
            items.update(_walk_numbers(item, f"{prefix}{_list_key(item, index)}"))
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
            items.update(_walk_strings(item, f"{prefix}{_list_key(item, index)}"))
        return items
    return {}


def _list_identity(item: Any) -> Any:
    if isinstance(item, Mapping):
        for key in ("slug", "id", "provider_id", "hero_id"):
            value = item.get(key)
            if value not in (None, ""):
                return value
    return None


def compare_list_order(baseline: Any, current: Any, *, prefix: str = "") -> list[str]:
    errors: list[str] = []
    if isinstance(baseline, Mapping) and isinstance(current, Mapping):
        for key in sorted(set(baseline) & set(current)):
            path = f"{prefix}.{key}" if prefix else str(key)
            errors.extend(compare_list_order(baseline[key], current[key], prefix=path))
        return errors
    if isinstance(baseline, list) and isinstance(current, list):
        before = [_list_identity(item) for item in baseline]
        after = [_list_identity(item) for item in current]
        if before and after and all(value is not None for value in before + after):
            if before != after:
                errors.append(f"changed order {prefix}: {before} -> {after}")
        for item_before, item_after in zip(baseline, current):
            errors.extend(
                compare_list_order(item_before, item_after, prefix=prefix)
            )
    return errors


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
    before = markdown_structure(baseline)
    after = markdown_structure(current)
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
    """Return errors when hero-level presentation facts regress."""
    errors: list[str] = []
    before_ids = [hero["id"] for hero in baseline["heroes"]]
    after_ids = [hero["id"] for hero in current["heroes"]]
    if before_ids != after_ids:
        errors.append(
            f"hero identity order changed: {before_ids} -> {after_ids}"
        )
        return errors
    after_by_id = {hero["id"]: hero for hero in current["heroes"]}
    skip_keys = {"references"}
    for hero in baseline["heroes"]:
        other = after_by_id[hero["id"]]
        prefix = hero["id"]
        left = {key: value for key, value in hero.items() if key not in skip_keys}
        right = {key: value for key, value in other.items() if key not in skip_keys}
        errors.extend(compare_numbers(left, right, prefix=prefix))
        errors.extend(compare_strings(left, right, prefix=prefix))
    return errors


def compare_view_artifacts(
    baseline: Mapping[str, Any],
    current: Mapping[str, Any],
) -> list[str]:
    """Compare every browser-visible generated artifact."""
    errors: list[str] = []
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
    if normalize_text(str(baseline.get("site_csv", ""))) != normalize_text(
        str(current.get("site_csv", ""))
    ):
        errors.append("site/data/heroes-overview.csv differs")
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
    errors.extend(
        compare_list_order(
            baseline["site_heroes"],
            current["site_heroes"],
            prefix="site",
        )
    )
    for name in ("mix_synergy_index", "mix_config", "mix_role_prominence"):
        errors.extend(
            compare_numbers(baseline[name], current[name], prefix=name)
        )
        errors.extend(
            compare_strings(baseline[name], current[name], prefix=name)
        )
    if baseline["list_columns"] != current["list_columns"]:
        errors.append("list-columns display semantics differ")
    errors.extend(
        compare_strings(
            baseline["counter_filter_combos"],
            current["counter_filter_combos"],
            prefix="counter_filter",
        )
    )
    return errors


def relationship_invariant_errors(view: Mapping[str, Any]) -> list[str]:
    """Validate relationship lists and referential integrity."""
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
        "site/data/heroes-overview.csv",
        "site/data/mix-synergy-index.json",
        "site/data/mix-config.json",
        "site/data/mix-role-prominence.json",
        "site/data/list-columns.json",
        "site/data/counter_filter_combos.json",
    ):
        path = repo.root / relpath
        if path.is_file():
            views[relpath] = path.read_text(encoding="utf-8")
    return views

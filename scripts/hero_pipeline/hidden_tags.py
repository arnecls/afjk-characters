"""Behavior tags that stay in data but are hidden from rendered views.

The hidden set is global: ``hidden_behavior_tags`` in
``data/heroes_config.json`` lists tags hidden for every hero. Scoring reads
every tag. Rendered outputs (overview markdown and CSV, site payload) use
``visible_behavior_tags`` instead.
"""

from __future__ import annotations

import json
from functools import lru_cache
from typing import Iterable

from .repository import current_repository


@lru_cache(maxsize=8)
def _load_hidden(config_path: str) -> frozenset[str]:
    with open(config_path, encoding="utf-8") as handle:
        config = json.load(handle)
    return frozenset(config.get("hidden_behavior_tags") or ())


def hidden_behavior_tags() -> frozenset[str]:
    """Tags hidden for all heroes, from the active repository's config."""
    path = current_repository().config_path
    if not path.is_file():
        return frozenset()
    return _load_hidden(str(path))


def visible_behavior_tags(tags: Iterable[str]) -> list[str]:
    """Return ``tags`` without globally hidden ones, keeping order."""
    hidden = hidden_behavior_tags()
    return [tag for tag in tags if tag not in hidden]

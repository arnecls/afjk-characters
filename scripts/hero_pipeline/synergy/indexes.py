"""Structured reverse indexes over scored synergy mappings."""

from __future__ import annotations

from collections import defaultdict
from typing import Any, Mapping


def build_beneficiary_index(
    synergies: Mapping[str, Any],
) -> dict[str, list[dict[str, Any]]]:
    """Return provider ID/name to receiver rows from receiver rankings."""
    result: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for receiver, payload in (synergies.get("heroes") or {}).items():
        for row in payload.get("synergies") or []:
            provider = row.get("provider_id") or row.get("provider")
            if provider is None:
                continue
            result[provider].append(
                {
                    "receiver_id": receiver,
                    "score": row.get("score", 0),
                    "reasons": list(row.get("reasons") or []),
                }
            )
    return dict(result)

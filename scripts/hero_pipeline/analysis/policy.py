"""Explicit immutable analysis policy loaded from the global config."""

from __future__ import annotations

from types import MappingProxyType
from typing import Any, Mapping


def _freeze(value: Any) -> Any:
    if isinstance(value, dict):
        return MappingProxyType(
            {key: _freeze(item) for key, item in value.items()}
        )
    if isinstance(value, list):
        return tuple(_freeze(item) for item in value)
    return value


def make_policy(config: Mapping[str, Any]) -> Mapping[str, Any]:
    """Return a read-only policy snapshot for one pipeline run."""
    return _freeze(dict(config))


def thaw_policy(policy: Mapping[str, Any]) -> dict[str, Any]:
    """Adapt an immutable policy at the legacy implementation seam."""
    def thaw(value: Any) -> Any:
        if isinstance(value, Mapping):
            return {key: thaw(item) for key, item in value.items()}
        if isinstance(value, tuple):
            return [thaw(item) for item in value]
        return value

    return thaw(policy)

"""Load hyphenated analysis libraries once for the whole process."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType
from typing import Any

SCRIPTS = Path(__file__).resolve().parent.parent

_RS: ModuleType | None = None
_GEN: ModuleType | None = None
_CSV: ModuleType | None = None


def _load(name: str, filename: str) -> ModuleType:
    existing = sys.modules.get(name)
    path = SCRIPTS / filename
    if existing is not None:
        loaded_from = getattr(existing, "__file__", None)
        if loaded_from and Path(loaded_from).resolve() == path.resolve():
            return existing
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def rewrite_summaries() -> Any:
    """Return the shared rewrite-summaries implementation."""
    global _RS
    if _RS is None:
        overview()
        _RS = sys.modules["rewrite_summaries"]
    return _RS


def overview() -> Any:
    """Return the shared synergy and overview implementation."""
    global _GEN
    if _GEN is None:
        _GEN = _load("gen_overview", "generate-heroes-overview.py")
        global _RS
        _RS = _GEN._rs
    return _GEN


def overview_csv() -> Any:
    """Return the shared CSV column helpers."""
    global _CSV
    if _CSV is None:
        _CSV = _load("overview_to_csv", "overview-to-csv.py")
    return _CSV

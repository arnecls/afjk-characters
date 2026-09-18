"""Injectable filesystem roots for the per-hero storage seam."""

from __future__ import annotations

from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

SCRIPTS = Path(__file__).resolve().parent.parent
DEFAULT_ROOT = SCRIPTS.parent


@dataclass(frozen=True)
class Repository:
    """Filesystem locations for one roster checkout."""

    root: Path

    @property
    def data(self) -> Path:
        return self.root / "data"

    @property
    def heroes_dir(self) -> Path:
        return self.data / "heroes"

    @property
    def manifest_path(self) -> Path:
        return self.data / "roster.json"

    @property
    def schema_dir(self) -> Path:
        return self.data / "schema"

    @property
    def config_path(self) -> Path:
        return self.data / "heroes_config.json"

    @property
    def seasons_path(self) -> Path:
        return self.data / "seasons.json"

    @property
    def tmp_dir(self) -> Path:
        return self.root / "tmp"

    @property
    def heroes_md(self) -> Path:
        return self.root / "Heroes.md"

    @property
    def overview_md(self) -> Path:
        return self.root / "heroes-overview.md"

    @property
    def overview_csv(self) -> Path:
        return self.root / "heroes-overview.csv"

    @property
    def site_data(self) -> Path:
        return self.root / "site" / "data"


DEFAULT_REPOSITORY = Repository(DEFAULT_ROOT)
_CURRENT: ContextVar[Repository] = ContextVar(
    "hero_pipeline_repository",
    default=DEFAULT_REPOSITORY,
)


def current_repository() -> Repository:
    """Return the repository for this execution context."""
    return _CURRENT.get()


@contextmanager
def repository_scope(repository: Repository) -> Iterator[Repository]:
    """Use ``repository`` for storage, analysis, and render I/O."""
    token = _CURRENT.set(repository)
    try:
        yield repository
    finally:
        _CURRENT.reset(token)

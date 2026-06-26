# ADR 0002: Canonical effect names (no buff/debuff suffixes)

## Status

Accepted (2026-06-25)

## Context

Combat-effect labels were stored with redundant polarity suffixes (`ATK buff`,
`Damage taken reduction`, `Energy recovery debuff`, …). The web UI stripped
suffixes at render time; CSV headers duplicated semantics in header text;
asymmetric pairs (`Damage taken reduction` vs `Damage taken debuff`) shared no
common stem. Processed JSON already had canonical `name` + `type`, but parallel
paths (skill tags, overview CSV, `TAG_DEFINITIONS`) still used suffixed strings.

## Decision

1. **Storage** — all effect labels are canonical stems (`ATK`, `Damage taken`,
   `Energy`, …). Polarity lives in `type` / category / column metadata only.
2. **Asymmetric pairs** — map legacy buff/debuff names to one stem (e.g.
   `Damage taken reduction` and `Damage taken debuff` → `Damage taken`).
3. **List view CSV** — headers use unique column ids (`atk_buff`, `atk_debuff`);
   `site/data/list-columns.json` carries display label + polarity.
4. **Web** — remove suffix stripping and suffix-based polarity inference; pass
   explicit polarity from tag objects or column registry.
5. **Migration** — single atomic pipeline regen (`just views`) with code changes.

## Consequences

- **Breaking for CSV consumers** — header row ids change from `"ATK buff"` to
  `atk_buff`; display label remains `ATK`.
- **Skill card tags** — `{label, polarity?}` objects replace plain strings where
  buff/debuff share a stem.
- **Synergy schema** — enum values `Stacking buff` → `Stacking`, `Artifact buff`
  → `Artifact`.
- **Hard to reverse** — touches detection rules, schema, site JS, overview
  generators, and all derived JSON/MD/CSV artifacts.
- **Surprising without context** — grep for `"ATK buff"` in committed data no
  longer matches; polarity must be read from `type` or column group.

## Alternatives considered

- **Render-time stripping only** — rejected; suffixes remained in JSON, CSV, and
  tests; asymmetric pairs stayed inconsistent with AGENTS.md display guidance.

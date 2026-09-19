# AFK Journey Hero Reference

**Start here: [Web-view](https://arnecls.github.io/afjk-characters)** — per-hero synergies, combat
behavior, structured skill summaries, and replacement suggestions for the full
roster.

This repository collects and analyzes hero skill data for [AFK Journey](https://afk-journey.fandom.com/wiki/AFK_Journey). Skill text is sourced primarily from the [AFK Journey Fandom wiki](https://afk-journey.fandom.com/wiki/Hero/List), with gaps filled from [Yaphalla](https://www.yaphalla.com/heroes). Meta tier ratings (S+, S, A, etc. per game mode) come from the [Prydwen tier list](https://www.prydwen.gg/afk-journey/tier-list). Skill text is parsed to extract buffs, debuffs, crowd control, damage types, and team synergies. Character play overview and counter propsals are AI generated from available data with additional input coming from community videos by [Puzzle](https://www.youtube.com/@PuzzleAFKJ) and [Elfe](https://www.youtube.com/@ElfeYT).

## Content warning

Most of the data and all of the code in this repository is AI generated.  
Due to the amount of data, only a couple of characters have been reviewed.  
If you spot any issues, please report them.

## What is in this repository

| File / folder | Purpose |
| --- | --- |
| **[heroes-overview.md](heroes-overview.md)** | Main reference: synergy partners, behavior, and parsed summaries per hero |
| **[heroes-overview.csv](heroes-overview.csv)** | Same roster data in spreadsheet form (damage, CC, buffs, movement, etc.) |
| **[Heroes.md](Heroes.md)** | Raw skill descriptions only — no summaries |
| **[`data/`](data/)** | Per-hero source, AI data, generated analysis, and schemas — see [data/README.md](data/README.md) |
| **[`scripts/`](scripts/)** | Python pipeline: download, analyze, validate, and render views |
| **[`site/`](site/)** | Static web viewer (GitHub Pages) — hero grid with synergy details |
| **[`docs/`](docs/)** | Pipeline overview, algorithm write-ups, and validation snapshots — see [docs/README.md](docs/README.md) |
| **[`.cursor/AGENTS.md`](.cursor/AGENTS.md)** | Detailed rules for parsing skills, scoring synergies, and editing summaries |

### What each hero entry contains

Each section in [heroes-overview.md](heroes-overview.md) includes:

- **Behavior** — Prydwen meta tiers, movement pattern, signature skill, behavior tags, placement constraints, damage-type overview
- **Play overview** — short playstyle blurb (setup, strengths, weaknesses) from each hero's `ai.json`
- **Skill overview** — signature / ultimate / non-ultimate metrics plus per-skill mechanic summaries
- **Units improving X** — up to five ranked synergy partners (stat buffs, enablers, summon support)
- **Units benefitting most from X** — reverse index of heroes who synergize with this unit
- **Replacements** — similar heroes grouped by role (damage, crowd control, buffs, etc.)
- **Summary** — structured breakdown of stats benefited, damage types, buffs, debuffs, crowd control, and special effects

Magnitude labels (`high`, `average`, `low`) rank an effect against the full roster (same effect label), not same-role peers only. See [`.cursor/AGENTS.md`](.cursor/AGENTS.md) for the full taxonomy.

## How to use it

### Browse the reference

Open [heroes-overview.md](heroes-overview.md) and jump to a hero by name. Use your editor's outline or search (`Ctrl/Cmd+F`) to navigate.

For filtering or pivot tables, open [heroes-overview.csv](heroes-overview.csv) in a spreadsheet application.

For verbatim skill wording (levels, cooldowns, unlock tiers), see [Heroes.md](Heroes.md).

### Web viewer

Browse the roster in a browser at **[https://arnecls.github.io/afjk-characters/](https://arnecls.github.io/afjk-characters/)** (deployed from the [`site/`](site/) directory via GitHub Pages).

Each hero has a shareable URL, e.g. `/hero/aliceth`. Synergy partners link to their own pages.

Character portraits in the web viewer are from the AFK Journey Fandom wiki. Faction/class icons are from [Yaphalla](https://www.yaphalla.com/heroes).

Rebuild site data locally:

```bash
just render-site
```

This refreshes `heroes-overview.md` / `heroes-overview.csv`, copies the CSV into `site/data/`, writes `site/data/heroes.json`, and downloads any missing faction/class icons from Yaphalla into `site/assets/icons/`. Running `just views` also refreshes the site data.

Skill-card chip tags on the character sheet come from the same analysis pass as
each hero's generated analysis (`skill_card_tags` per skill). After changing
detection logic, run `just views` so generated and site data stay aligned.

Preview locally (required — the site loads data via `fetch`):

```bash
cd site && python3 -m http.server
```

Then open `http://localhost:8000/` in your browser.

Enable GitHub Pages once in the repository settings: source **Deploy from a branch**, branch **`gh-pages`**, folder **`/` (root)**. Pushes to `main` or `webview` trigger [`.github/workflows/deploy-pages.yml`](.github/workflows/deploy-pages.yml), which rebuilds site data from committed JSON and publishes `site/`.

### Regenerate the views

The ordered `data/roster.json` manifest and the four files under each
`data/heroes/<hero-id>/` directory (`source.json`, `ai.json`,
`overrides.json`, `analysis.json`) are the source of truth. Views are rebuilt
from them with [just](https://github.com/casey/just).

**One-time setup:**

```bash
just setup
```

**Regenerate from committed data (no network):**

```bash
just views
```

This runs analysis and writes generated analysis/synergy fields inside each
hero directory, then renders `Heroes.md`, `heroes-overview.md`,
`heroes-overview.csv`, and the site data.

**Full refresh from live sources (requires network):**

```bash
just all
```

Downloads merged data from Yaphalla and the Fandom wiki, then runs the full pipeline.
`just download` alone marks existing generated analysis stale; run `just analyze`
before rendering.

**Validate processed data against schemas and cache freshness:**

```bash
just validate
```

Broader content and detection checks:

```bash
just validate-semantics
```

Run `just` (or `just --list`) to see all available recipes.

**Tests** (after `just setup`):

```bash
PYTHONPATH=scripts .venv/bin/python -m unittest discover -s scripts -p 'test_*.py'
```

### Pipeline overview

```
download  →  data/heroes/<hero-id>/source.json
analyze   →  data/heroes/<hero-id>/analysis.json (hero-local cache)
views     →  Heroes.md
             heroes-overview.md
             heroes-overview.csv
             site/data/heroes.json  (skillCards read from processed skill_card_tags)
```

| Step | Script(s) | Role |
| --- | --- | --- |
| Download | `scripts/hero_pipeline_cli.py download` | Merge Fandom, Yaphalla, and Prydwen into hero-local `source.json` |
| Analyze | `scripts/hero_pipeline_cli.py analyze` | Refresh stale local analysis caches |
| Views | `scripts/hero_pipeline_cli.py views` | Calibrate, score relationships in memory, render Markdown/CSV/site |
| Local analysis | `scripts/hero_pipeline/analysis/` | Detection, behavior, and hero-local facts |
| Relationships | `scripts/hero_pipeline/relationships/` | Synergy and replacement scoring |

Configuration for analysis, synergy scoring, and display limits lives in
`data/heroes_config.json`. AI-authored data and typed overrides live beside
each hero; see [data/README.md](data/README.md) and
[docs/ai-generated-data.md](docs/ai-generated-data.md).

## Requirements

- Python 3.12+
- [just](https://github.com/casey/just) (optional, for convenience recipes)
- Dependencies: `jsonschema` (installed into `.venv` by `just setup`)

---

<sup>*This repository and its contents were generated with the assistance of AI.*</sup>

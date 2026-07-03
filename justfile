# AFK Journey hero data pipeline.
# Run `just` (or `just -l`) to list recipes.
#
# Pipeline: download -> analyze -> render
#   download : data/heroes_data.json          (Fandom baseline + Yaphalla gaps)
#   analyze  : merges data/skill_effects/*.json sidecars into
#              data/heroes_data_processed.json + heroes_data_synergies.json
#   render   : Heroes.md, heroes-overview.md, heroes-overview.csv, site data

default:
    @just --list

# Create .venv and install requirements.txt (jsonschema for schema validation).
setup:
    python3 -m venv .venv
    .venv/bin/pip install -r requirements.txt

# Ensure .venv exists before recipes that validate JSON schemas.
ensure-venv:
    #!/usr/bin/env bash
    set -euo pipefail
    if [[ ! -x .venv/bin/python ]]; then
      python3 -m venv .venv
      .venv/bin/pip install -q -r requirements.txt
    fi

# Refresh data/heroes_data.json from live sources (Fandom, Yaphalla, Prydwen).
download:
    python3 scripts/download_heroes.py

# Validate processed JSON vs Heroes.md and pipeline parity.
validate: ensure-venv
    .venv/bin/python scripts/validate_processed.py

# Parallel pytest (~2–3 min after caching). Uses -n auto when peak RSS ≤ 1.5 GB.
test: ensure-venv
    #!/usr/bin/env bash
    set -euo pipefail
    workers="$(.venv/bin/python scripts/test_parallel_workers.py)"
    .venv/bin/python -m pytest scripts/ -n "$workers"

# Stream one line per test (serial, ~4–5 min with cache). For debugging failures.
test-serial: ensure-venv
    .venv/bin/python -m unittest discover -s scripts -p 'test_*.py' -v

# Merge AI skill-effect sidecars into processed + synergies JSON.
analyze: ensure-venv
    .venv/bin/python scripts/process_heroes.py
    .venv/bin/python scripts/process_synergies.py

# Recompute roster-wide synergies from existing processed data.
analyze-synergies: ensure-venv
    .venv/bin/python scripts/process_synergies.py

# Render Heroes.md from data/heroes_data.json.
render-heroes:
    python3 scripts/render_heroes.py

# Render heroes-overview.md + heroes-overview.csv.
render-overview:
    python3 scripts/render_overview.py

# Build site/data from overview views and cache missing portraits, and bundle JS assets.
render-site: render-overview
    python3 scripts/render_site.py
    python3 scripts/download_hero_images.py
    python3 scripts/bundle_js.py


# Render all view files.
render: render-heroes render-site

# Regenerate views from the committed data/heroes_data.json (no network).
views: analyze render

# Full pipeline: refresh data from the web, then regenerate views.
all: download analyze render

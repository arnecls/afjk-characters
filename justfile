# AFK Journey hero data pipeline.
# Run `just` (or `just -l`) to list recipes.
#
# Pipeline: download -> analyze -> views
#   download : data/roster.json + data/heroes/*/source.json
#   analyze  : data/heroes/*/analysis.json (hero-local cache)
#   views    : calibrate + relationships in memory; Heroes.md, overview, CSV, site

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

# Refresh per-hero source files from live sources.
download:
    python3 scripts/hero_pipeline_cli.py download

# Validate processed JSON vs Heroes.md and pipeline parity.
validate: ensure-venv
    .venv/bin/python scripts/hero_pipeline_cli.py validate

# Content and semantic checks against local caches and AI sidecars.
validate-semantics: ensure-venv
    .venv/bin/python scripts/validate_processed.py

# Strict types for the schema-first pipeline package only.
typecheck: ensure-venv
    .venv/bin/python -m mypy --config-file mypy.ini scripts/hero_pipeline

# Parallel pytest (~2–3 min after caching). Uses -n auto when peak RSS ≤ 1.5 GB.
test: ensure-venv
    #!/usr/bin/env bash
    set -euo pipefail
    workers="$(.venv/bin/python scripts/test_parallel_workers.py)"
    .venv/bin/python -m pytest scripts/ -n "$workers"

# Stream one line per test (serial, ~4–5 min with cache). For debugging failures.
test-serial: ensure-venv
    .venv/bin/python -m unittest discover -s scripts -p 'test_*.py' -v

# Refresh stale local analysis caches.
analyze: ensure-venv
    .venv/bin/python scripts/hero_pipeline_cli.py analyze

# Recompute roster-wide relationships in memory and publish views.
analyze-synergies: ensure-venv
    .venv/bin/python scripts/hero_pipeline_cli.py views

# Render Heroes.md, overview, CSV, and browser-visible files.
render-heroes: ensure-venv
    .venv/bin/python scripts/hero_pipeline_cli.py views

# Render views, then fail if committed outputs drifted besides the timestamp.
assert-rendered-outputs: ensure-venv
    .venv/bin/python scripts/assert_rendered_outputs.py

# Render heroes-overview.md + heroes-overview.csv (same views command).
render-overview: render-heroes

# Build site/data from overview views, cache faction/class icons, bundle JS.
render-site: render-overview
    python3 scripts/download_hero_images.py
    python3 scripts/bundle_js.py

# Render all view files.
render: render-site

# Regenerate views from committed hero bundles (no network).
views: render

# Full pipeline: refresh data from the web, then regenerate views.
all: download analyze render

# Serve the site locally.
serve:
    python3 -m http.server 8000 --directory site
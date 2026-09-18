#!/usr/bin/env python3
"""Command-line entry point for the schema-first hero pipeline."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from hero_pipeline.pipeline import analyze, download, init, validate, views


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    init_p = sub.add_parser("init", help="create a four-file hero bundle")
    init_p.add_argument("id")
    init_p.add_argument("--display-name", required=True)
    init_p.add_argument("--title", required=True)
    init_p.add_argument("--alias", action="append", default=[])

    download_p = sub.add_parser("download", help="refresh downloaded source")
    download_p.add_argument("--hero")

    analyze_p = sub.add_parser("analyze", help="refresh stale local caches")
    analyze_p.add_argument("--hero")
    analyze_p.add_argument(
        "--force",
        action="store_true",
        help="recompute even when inputs are fresh (detector bumps)",
    )

    views_p = sub.add_parser(
        "views",
        help="calibrate, score, and render the full roster",
    )

    validate_p = sub.add_parser("validate", help="validate bundles and caches")
    validate_p.add_argument("--hero")

    args = parser.parse_args()
    if args.command == "init":
        init(
            args.id,
            args.display_name,
            args.title,
            args.alias or None,
        )
        print(f"Initialized {args.id}")
        return
    if args.command == "download":
        count = download(hero_id=args.hero)
        scope = args.hero or "roster"
        print(f"Downloaded source for {scope} ({count} web records)")
        return
    if args.command == "analyze":
        count = analyze(hero_id=args.hero, force=args.force)
        print(f"Refreshed {count} local analysis caches")
        return
    if args.command == "views":
        heroes, scored = views()
        print(f"Rendered views for {heroes} heroes ({scored} scored)")
        return
    if args.command == "validate":
        errors = validate(hero_id=args.hero)
        if errors:
            print("\n".join(errors), file=sys.stderr)
            raise SystemExit(1)
        print("OK")


if __name__ == "__main__":
    main()

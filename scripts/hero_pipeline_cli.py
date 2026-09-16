#!/usr/bin/env python3
"""Command-line entry point for the schema-first hero pipeline."""

from __future__ import annotations

import argparse

from hero_pipeline.pipeline import analyze


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("analyze",))
    args = parser.parse_args()
    if args.command == "analyze":
        processed, synergies = analyze()
        print(
            f"Analyzed {len(processed['heroes'])} heroes and "
            f"scored {len(synergies['heroes'])} heroes"
        )


if __name__ == "__main__":
    main()

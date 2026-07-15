#!/usr/bin/env python3
"""Bundle and minify JS modular source files from site/js/src/ to site/js/app.js.

Uses rjsmin for minification as configured in the project's requirements.txt.
"""

import sys
from pathlib import Path

# Try importing rjsmin
try:
    import rjsmin
except ImportError:
    # Fallback to importing through venv
    SCRIPTS_DIR = Path(__file__).resolve().parent
    VENV_SITE_PACKAGES = SCRIPTS_DIR.parent / ".venv" / "lib"
    # Find site-packages dynamically
    site_packages = list(VENV_SITE_PACKAGES.glob("python*/site-packages"))
    if site_packages:
        sys.path.insert(0, str(site_packages[0]))
        import rjsmin
    else:
        print("Error: rjsmin not found. Please run 'just setup' or install rjsmin.")
        sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "site" / "js" / "src"
DIST_FILE = ROOT / "site" / "js" / "app.js"  # site/js/app.js

# List of source files in exact dependency resolution order
SRC_FILES = [
    "namespace.js",
    "config.js",
    "theme.js",
    "utils.js",
    "state.js",
    "chips.js",
    "tiers.js",
    "markdown.js",
    "skills.js",
    "ui-widgets.js",
    "views-grid.js",
    "views-list.js",
    "views-mix.js",
    "views-detail.js",
    "router.js",
    "main.js",
]


def bundle_and_minify(debug: bool = False) -> None:
    print(f"Bundling JS from {SRC_DIR.relative_to(ROOT)}...")

    missing_files = []
    contents = []

    # Wrap the entire bundle in an IIFE to keep the window namespace clean except for AFKJ
    contents.append("(function() {\n'use strict';\n")

    for f_name in SRC_FILES:
        f_path = SRC_DIR / f_name
        if not f_path.exists():
            missing_files.append(f_name)
            continue

        file_content = f_path.read_text(encoding="utf-8")
        # Ensure there is a trailing newline and wrap each file in comments for clarity
        contents.append(f"\n/* --- START FILE: {f_name} --- */\n")
        contents.append(file_content)
        contents.append(f"\n/* --- END FILE: {f_name} --- */\n")

    contents.append("\n})();\n")

    if missing_files:
        print(f"Error: Missing source files: {', '.join(missing_files)}")
        sys.exit(1)

    full_js = "".join(contents)

    if debug:
        print(f"Writing unminified JS to {DIST_FILE.relative_to(ROOT)}...")
        DIST_FILE.write_text(full_js, encoding="utf-8")
    else:
        print(f"Minifying and writing to {DIST_FILE.relative_to(ROOT)}...")
        minified = rjsmin.jsmin(full_js)
        DIST_FILE.write_text(minified, encoding="utf-8")

    print("JS Bundling complete!")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Bundle site JS")
    parser.add_argument("--debug", action="store_true", help="Do not minify output")
    args = parser.parse_args()
    bundle_and_minify(debug=args.debug)

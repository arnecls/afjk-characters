# Module Breakdown (site/js/src/)

The monolithic site/js/app.js has been broken down into 15 organized modules, each wrapped in an IIFE and exporting functions/constants onto a unified window.AFKJ namespace:

- `namespace.js:` Initializes standard global namespaces (window.AFKJ.state, window.AFKJ.config, window.AFKJ.utils, etc.).
- `config.js:` Houses all static metadata configurations (TAG_DEFINITIONS, ROLE_CATEGORY_META, etc.).
- `utils.js:` Houses generalized utilities like HTML escaping, base path resolution, asset URL builders, and viewport collision detection.
- `state.js:` Declares a Centralized State Object (window.AFKJ.state) containing all mutable app variables and structured DOM caching (window.AFKJ.state.dom).
- `chips.js:` Handles effect label parsing and polarity-aware styling (buff vs. debuff) for interactive status chips.
- `tiers.js:` Encapsulates Prydwen tier ranking comparisons, mappings, and cell-augmentation helpers.
markdown.js:` Contains the custom markdown parser and inline compiler for skills.
- `skills.js:` Manages interactive skill description overlays, tag matching, and card rendering.
- `ui-widgets.js:` Drives foundational UI behaviors like the welcome/warning banner, mobile filter menu collapsibles, custom tooltips, and floating skill card popovers.
- `views-grid.js:` Implements individual hero grid renders, faction/class icon grids, and card title fitting animations.
- `views-list.js:` Manages the spreadsheet list view, headers, custom sorters, and multi-filter column panels.
- `views-mix.js:` Implements the synergy scoring sandbox, hero drag-and-drop slots, and context menus.
- `views-detail.js:` Controls the dedicated single-hero detail profiles (behavior breakdown, synergy options, and replacement suggestions).
- `router.js:` Facilitates path-safe location routing, navigation, state history, and search filters.
- `main.js:` Serves as the application bootstrap; caches DOM elements on DOM-ready, initializes widgets, binds event listeners, and routes the initial view.

The separate files are compiled to a minified app.js via just `render-site`.
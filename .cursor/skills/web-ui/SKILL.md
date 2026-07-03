---
name: web-ui
description: >-
  Fixes and changes for the static hero browser in site/ — chip/pill rendering,
  skill cards, list/grid views, synergy sections, layout, and display wording.
  Use when the user reports wrong pills, chips, cards, columns, filters,
  colors, layout, or web-UI labels; or asks to change how heroes.json content
  appears in the browser.
---

# Web UI (site viewer)

The browser lives in `site/`. JavaScript source files live in
`site/js/src/`; bundled/minified output is `site/js/app.js`. Styles:
`site/css/styles.css`. Data: `site/data/heroes.json` and
`site/data/heroes-overview.csv`.

**Never hand-edit `site/js/app.js`.** Make JavaScript changes in
`site/js/src/**`, then rebuild `site/js/app.js` with
`python3 scripts/bundle_js.py` or `just render-site`.

Read `.cursor/AGENTS.md` for skill-card tag rules and magnitude vocabulary.

## Workflow

```markdown
Task progress:
- [ ] 1. Reproduce — which view, which hero/section, expected vs actual
- [ ] 2. Classify — data, detection, or display-only (see below)
- [ ] 3. Trace — stored tag/text vs rendered HTML
- [ ] 4. Fix — minimal change in the right layer
- [ ] 5. Verify — node chip test and/or local preview; run tests if Python touched
- [ ] 6. Regenerate site data only when detection or render_site inputs changed
```

### 1. Classify the bug

| Symptom | Likely layer | Where to fix |
| --- | --- | --- |
| Wrong effect **missing or extra** on skill card | Sidecar extraction | `data/skill_effects/<hero>.json` → `just views` |
| Tag string correct in JSON but **wrong chip** on screen | Display | `site/js/src/` (`TAG_DEFINITIONS`, chip helpers) → bundle |
| Synergy/summary **wording** wrong in markdown and web | Generation | `scripts/generate-heroes-overview.py` / `rewrite-summaries.py` → `just render-site` |
| **Layout, color, filter, column** behavior | CSS / JS view code | `site/css/styles.css`, `site/js/src/` → bundle |
| List view column **content** wrong | CSV pipeline | `scripts/overview-to-csv.py` → `just render-site` |

**Skill cards:** tags are computed during `just analyze` and stored as
`skill_card_tags` on each skill in `heroes_data_processed.json`.
`scripts/render_site.py` copies them into `site/data/heroes.json` →
`sections.skillCards[].tags`. It does **not** re-derive tags.

After changing skill effects in `data/skill_effects/<hero>.json`, run
**`just views`** (analyze + render), not `just analyze` alone.

Display-only chip fixes need **no** data regen — rebuild the JS bundle after
editing `site/js/src/**`, then reload the page.

### 2. Trace skill-card issues

```bash
# Tags stored for a hero (example: Eironn Legendary+ = skill3)
node -e "
const h = require('./site/data/heroes.json').heroes.find(x => x.slug === 'eironn');
console.log(h.sections.skillCards.find(c => c.label === 'Legendary+'));
"
```

If `tags` are correct but pills look wrong → display layer in `site/js/src/`.

Key render path:

1. `renderSkillCards` → `renderSkillCardTags`
2. `chipifySkillCardTag` → `parseSkillCardTag` (strips `— Self`)
3. `skillCardEffectLabel` / `parseBuffEffectLabel` / `parseDebuffEffectLabel`
4. `resolveLeadingChip` → `TAG_DEFINITIONS` + prefix match on stat/CC keys
5. `mergeEffectWithTargeting` for self-targeted merged pills

Canonical dedup keys: `skillCardChipKey` (JS) and
`_canonical_skill_card_chip_key` (Python). **Stat keys must be checked
before damage keys** so labels like `Ranged DEF buff` do not match
`Ranged` damage.

### 3. Chip / pill system (`site/js/src/`)

**Registry:** `TAG_DEFINITIONS` — emoji + CSS class per label.

| `cls` suffix | Role | Examples |
| --- | --- | --- |
| `chip-damage` | Damage types | Physical, Magic, Ranged, True damage |
| `chip-stat` | Stats / defensive | ATK, Physical DEF, Ranged DEF, Shield |
| `chip-debuff` | Debuffs | Haste debuff, Magic DEF debuff |
| `chip-heal` | Healing | Direct healing, HoT |
| `chip-cc` | Crowd control | Stun, Bind, Silence |
| `chip-quality` | Magnitude | high, average, low |
| `chip-target` | Targeting | Self, Area, Arc |
| `chip-behavior-tag` | Behavior tags | aoe-damage, summoner |

**Merged pill layout** (`chip chip-merged`): effect on the left, modifier on
the right, separated by `|`. Used for:

- Quality: `Haste buff | high`
- Self on skill cards: `Ranged DEF | Self`
- CC duration: `Stun | long` (not raw `(low)` text)

Helpers: `formatMergedIndicator`, `mergeEffectWithQuality`,
`mergeEffectWithTargeting`, `renderMergedEffectPill`,
`renderBuffProvidedEntry`.

**Polarity:** buff vs debuff affects which suffix is stripped and which chip
class applies. Debuffs must not reuse buff chip paths (e.g. Energy recovery
**debuff** on Contess skill 2).

### 4. UI surfaces → code

| Surface | Data source | Render entry |
| --- | --- | --- |
| Grid hero cards | `heroes.json` metadata | `renderGrid` |
| Character sheet — behavior | `sections.behavior` markdown | `renderInline`, `renderBehaviorTagsLine` |
| Skill overview pills | behavior markdown metrics | `renderSkillOverviewMetric` |
| Skill cards | `sections.skillCards` | `renderSkillCards`, skill popover |
| Synergy — improving | `sections.synergy` markdown | `renderBuffProvidedEntry`, `chipifyEffectName` |
| Replacement options | `sections.replacements` | replacement section renderers |
| List view table | `heroes-overview.csv` | `buildListBodyHtml`, column chip helpers |
| Column filters | CSV cell atoms | `columnFilter*`, `buildColumnFilterOptions` |
| Welcome warning | localStorage | `initWelcomeWarning` |

List view and detail sheet **share** chip helpers — fix both when changing
pill rules (historical bugs: text outside pills in table cells).

### 5. Display wording (web-UI only)

Use these in `site/js/src/` / `chipDisplayLabel`, not in detection JSON:

| Prefer | Not in web UI |
| --- | --- |
| `average` | `medium`, `normal` (magnitude and speed) |
| `Max HP damage` | `Max HP-based damage` |
| `HoT` | `Healing over time` (skill cards only; summaries may differ) |
| `Ranged DEF` | `Ranged` (when meaning defensive stat, not damage type) |

Magnitude in data/markdown uses backticks: `` `high` ``, `` `average` ``.

### 6. CSS conventions

- Chip colors: `.chip-damage`, `.chip-stat`, `.chip-debuff`, etc. in
  `styles.css`
- Merged pills: `.chip-merged`, `.chip-merged-left`, `.chip-merged-right`
- Skill cards: `.skill-card-tags` (smaller font)
- List table: `.heroes-table`, sticky headers, column width lock
- Replacement sections: per-category background tints
- Responsive: mobile toolbar wraps below search (`@media` in `styles.css`)

### 7. Verify

**Local preview** (required — `fetch` needs a server):

```bash
cd site && python3 -m http.server
# open http://localhost:8000/#hero/eironn
```

**Chip logic smoke test** (no browser):

```bash
node -e "
const fs = require('fs');
const src = fs.readFileSync('site/js/app.js', 'utf8');
const start = src.indexOf('const QUALITY_CLASS');
const end = src.indexOf('function stripSkillSummarySubsections');
const extra = src.slice(src.indexOf('function parseDebuffEffectLabel'),
  src.indexOf('function parseEffectColumnLabel'));
const buff = src.slice(src.indexOf('function parseBuffEffectLabel'),
  src.indexOf('function renderBuffTargetingChip'));
const fns = eval('(function(){ function escapeHtml(s){return s;} '
  + src.slice(start, end) + extra + buff
  + ' return { renderSkillCardTags }; })()');
console.log(fns.renderSkillCardTags(['Ranged DEF buff — Self'])
  .replace(/<[^>]+>/g,' ').replace(/\\s+/g,' ').trim());
"
```

**Python** (if detection or canonical keys changed):

```bash
PYTHONPATH=scripts .venv/bin/python -m unittest \
  scripts.test_hero_schema.SkillOverviewTests.test_processed_skill_card_tags_match_live_analysis \
  scripts.test_hero_schema.SkillOverviewTests.test_eironn_legendary_skill_card_ranged_def_tags -v
```

### 8. Regenerate commands

| Change | Command |
| --- | --- |
| Detection / skill_card_tags | `just views` |
| Overview markdown / synergies only | `just render-site` |
| CSV columns | `just render-overview` (includes CSV) |
| `site/js/src/` / `styles.css` only | `python3 scripts/bundle_js.py`, then reload browser — no data regen |

## When to touch Python vs JS

- **New effect label** on skill cards → detection (`format_skill_card_tags`)
  **and** display (`TAG_DEFINITIONS`, `_SKILL_CARD_STAT_KEYS` or debuff keys)
- **Wrong chip icon/color for existing label** → JS (+ CSS) only
- **New list column** → `overview-to-csv.py`, `render_site.py`, `site/js/src/`
  headers + `buildListBodyHtml`
- **Play overview length** on character sheet → `data/hero_play_overviews.json`
  and `just render-site`

## Reporting

Summarize for the user:

1. **Layer** — data, detection, or display
2. **Files changed** — especially whether `heroes.json` was regenerated
3. **How to verify** — hero URL hash and what pills/sections to check

Do not regenerate overview or site data unless the fix requires it.

## Examples

See [pitfalls.md](pitfalls.md) for past fixes from agent sessions (wrong
pills, list view, replacements, layout, wording).

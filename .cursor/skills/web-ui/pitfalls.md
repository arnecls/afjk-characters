# Web UI pitfalls

Past fixes from agent sessions. Use as patterns, not exhaustive rules.

## Skill cards — data vs display

### Kazim still showed Max HP damage (d580e830)

**Symptom:** Skill cards out of sync with updated detection.

**Cause:** Tags were computed separately from `skill_slices`; processed JSON
and `heroes.json` could drift.

**Fix pattern:** Unify on `format_skill_card_tags()` during analyze; store
`skill_card_tags` per skill; `render_site.py` reads stored tags. Test:
`test_processed_skill_card_tags_match_live_analysis`.

**Display policy:** `_apply_skill_card_damage_display_policy()` may hide
implicit max-HP chips on cards while detection still records them.

### Eironn Legendary+ showed Ranged instead of Ranged DEF (c7e477b3)

**Symptom:** `Ranged DEF buff — Self` rendered as damage-type Ranged (🏹).

**Cause:** `Ranged DEF` missing from stat chips; prefix matching could treat
`ranged def buff` as damage `Ranged`; buff suffix not stripped before
`resolveLeadingChip`.

**Fix pattern:**

- Add `Ranged DEF` to `TAG_DEFINITIONS` (`chip-stat`) and
  `_SKILL_CARD_STAT_KEYS`
- `skillCardEffectLabel()` — strip `buff` only for qualified `* DEF buff`
  labels
- Check stat keys before damage keys in `skillCardChipKey` and
  `_canonical_skill_card_chip_key`

**Verify:** tags in JSON unchanged; rendered pill is `🛡️ Ranged DEF | Self`.

### Self-targeted skill cards (c4f5813f, aed4f41)

**Symptom:** Self effects did not use merged pill layout.

**Fix:** Tags suffixed `— Self` in Python (`_skill_card_tag_for_effect`);
`parseSkillCardTag` + `mergeEffectWithTargeting` in JS; `effectChipRemainder`
hides trailing `buff`/`debuff` after stat match.

### Contess energy recovery shown as buff (87cdaf8e)

**Symptom:** Debuff rendered with buff styling.

**Fix:** Ensure label is `Energy recovery debuff` in detection; polarity from
` debuff` suffix in `chipifySkillCardTag`; separate canonical keys for buff
vs debuff (`test_contess_skill2_skill_card_energy_recovery_debuff`).

### HoT never on skill cards (5c5af693)

**Symptom:** Only generic Healing chip, not HoT.

**Fix:** Detection labels + `_skill_card_tag_label` maps healing-over-time to
`HoT` on cards; broader healing taxonomy in schema is separate from card
display shorthand.

## Synergy / summary pills

### Nerion CC pills showed `(low)` as text (6b217c43)

**Symptom:** Units improving section showed `(average)` instead of merged
quality chip.

**Fix:** Route through `renderMergedEffectPill` / `mergeEffectWithQuality`,
not plain parentheses in markdown parsing.

### Saida Energy drain split chip (4294f970)

**Symptom:** Energy pill + word `drain` instead of one debuff chip.

**Fix:** `resolveLeadingChip` / debuff label parsing — full label
`Energy drain` as debuff, not stat `Energy` + remainder.

### Max HP-based damage in list cells (87cdaf8e)

**Symptom:** `( ❤️ Max HP | low ) DMG` — text outside pills; overflow.

**Fix:** Use shared `chipifyEffectName` path for table cells;
`chipDisplayLabel`: `Max HP-based damage` → `Max HP damage`; column width
lock so filtering does not resize columns.

## List view

### Pills broken in table (87cdaf8e)

Examples of broken cells:

- `Magic DMG` with no pill
- `Conditional` with no pill
- Magnitude/targeting outside merged layout

**Fix:** Build filter atoms from chip HTML, not raw strings; reuse
`renderMergedEffectPill` for effect stacks.

### Filters: match-all vs match-one (b694cf6b)

**Symptom:** Multi-select within a column used AND instead of OR.

**Fix:** Per-column OR; AND across columns.

### Filter dropdown groups (b694cf6b)

**Symptom:** All combinations listed; user wanted `medium or high and global`.

**Fix:** List atomic values in dropdown; combine selected atoms when
filtering.

### Reload loses list view (b694cf6b)

**Fix:** Persist `viewMode` in `localStorage` (`readStoredViewMode`).

### Healing column width (b694cf6b)

Too wide → skills on one line; too narrow → clipped. Tune
`measureEffectStackCellWidth` and column min-widths.

### Behavior tags column (d580e830)

**Fix:** Add column in `overview-to-csv.py`, copy CSV in `render_site.py`,
render with `behaviorTagChip` in `buildListBodyHtml`.

## Wording and indicators

### medium / normal → average (4294f970, 358aedc)

**Scope:** Web UI only — `QUALITY_CLASS`, `SPEED_CLASS`, speed tooltips,
`parseSkillOverviewMetricEntry`. Data pipeline already uses `average`.

### Speed vs magnitude average icons (4294f970)

User chose: speed average 🚶 (`SPEED_EMOJI.average`), magnitude average ⚖️
(`QUALITY_EMOJI.average`).

### Missing Prydwen tiers break tier row (87cdaf8e)

**Symptom:** Kazim with no tiers hid entire tier visualization.

**Fix:** `_normalize_prydwen_tiers` fills missing modes with `?` (same as
partial tiers for Gwyneth).

## Layout and chrome

### Collapsible filters broke toolbar alignment (87cdaf8e)

**Symptom:** Collapse button wrong side; grid/list toggle misplaced.

**Fix:** `setFiltersCollapsed` + CSS grid areas; right-align collapse when
open; keep view toggle left of search.

### Mobile toolbar overflow (8c486ad8)

**Fix:** Wrap controls below search only in mobile `@media`.

### Welcome warning blocks interaction (4294f970)

`initWelcomeWarning` — backdrop blur, intercept clicks until dismissed;
`localStorage` flag.

## Replacement section

### Section rename and disclaimer (f6fc0d6e)

- Rename to **Potential replacement options**
- Warning-styled intro with link to `docs/replacement-algorithm.md`
  (`target="_blank"`)

### Visual grouping (d580e830)

- Fading background per replacement category
- Icons on subsection headings
- Orange tier label for one-step downgrade
- Distinct color for Similar Skills vs Damage replacements

### Behavior tag pills beige + label icon (d580e830)

CSS for filter tag chips; use `behaviorTagDefinition` emoji, not generic 🏷️.

## Play overviews on character sheet (42bdda45)

**Source:** `data/hero_play_overviews.json` → `sections` via `render_site.py`.

**Length:** ~5–6 lines in UI; target under ~900 characters per hero.
Regenerate with `just render-site` after JSON edits.

## Common mistake: fixing only one layer

| User report | Wrong fix | Right fix |
| --- | --- | --- |
| Wrong pill label | Edit `heroes.json` by hand | Fix detection or `app.js` |
| Missing skill card tag | Only `app.js` | `rewrite-summaries.py` + `just views` |
| List column wrong | Only `app.js` | `overview-to-csv.py` + render pipeline |
| Chip color | `heroes.json` | `styles.css` or `TAG_DEFINITIONS.cls` |

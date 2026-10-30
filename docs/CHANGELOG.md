# Changelog

## 2026-10-30

### New Features

- Added Baden (Graveborn · Rogue · Physical), The Abomination.
- Added the Level 2 Enhance Force upgrade for 41 heroes. It unlocks at
  Supreme+ with 100 Shadow Essence. The hero pages show its text and
  chips as "Supreme+ Lv2".
- Synergy: the Supreme+ Lv2 tier scores like the strongest defining tier,
  with a multiplier of 1.8.

### Fixed

- The Level 2 Enhance Force text was empty for 38 heroes. It now shows the
  full text.
- Vala now shows her Level 2 Enhance Force text, which uses a different
  wiki format.

### Character changes

| Character | What changed |
|---|---|
| baden | - Added as new hero |
| marene | - Added as new hero |
| alsa, antandra, atalanta, berial, bryon, callan, cassadee, cecia, cryonaia, damian, dionel, dunlingr, florabelle, gerda, granny-dahnie, harak, hodgkin, indris, isabella, lenya, lorsan, lucca, lumont, lyca, mirael, nara, niru, parisa, rhys, rowan, salazer, satrana, scarlita, silvina, soren, temesia, vala, valen, valka, viperian, walker | - Added the Level 2 Enhance Force text<br>- Added the Level 2 effects, except for Parisa and Satrana, which have no numeric effect |
| lyca, valen, cecia | - Added the tag `high-initial-energy` |
| niru, rowan | - Added the tag `temporary-stat-buffer` |
| harak | - Added the tag `battle-start-burst` |
| walker, viperian | - Added the tag `life-drain` |
| dunlingr | - Added the tag `energy-inhibitor` |
| nara | - Added the tag `enemy-debuffer` |
| alsa | - Added the tags `aoe-damage` and `enemy-debuffer` |
| atalanta, nara, lenya, cryonaia, harak, temesia | - Updated the counter text for the Level 2 upgrade |
| 126 heroes (most of the roster) | - Rewrote the first sentences of the counter text<br>- The new opening names the main PVP threat or the window to stop the hero<br>- The opening no longer repeats the play overview |
| aster, athalia, faramor, lenya, lily-may, salazer, seth, shadewing, silvina, sinbad, soren, sylphira, walker | - Refreshed relative stat ranks |

### Implementation changes

- `sources_web.py`: `_normalize_infobox_inner` now splits fields only
  outside nested templates. Before, `{{Item|Shadow Essence|x=100}}` cut the
  Level 2 text.
- `sources_web.py`: `_parse_level_upgrades` reads both the
  `Level 2 (Unlocks with ...)` format and the `Unlock {{Item|...}}` format.
  The unlock label is "Unlocks at Supreme+ (100 Shadow Essence)".
- Added the tier `supreme+_2`, shown as `Supreme+ Lv2`. It sorts after
  `Supreme+` and has a defining-tier multiplier of 1.8. The change covers
  `serialize.py`, `project.py`, `scoring.py`, `scoring_facts.py`,
  `policy.py`, `game_properties.schema.json` and the site chips.
- `skill_chunks.py`: a Supreme+ upgrade that needs Shadow Essence gets the
  tier `Supreme+ Lv2`.
- `crowd_control.py`: the CC check now skips text such as "hitting an enemy
  with Arcane Binding". The text names a skill and does not apply CC.
- Added the season Veil of Memories (2026-09-23) to `seasons.json`.
- Added tests for both wiki formats and for the tier mapping.
- `download` also changed other skill texts and the order of `roster.json`.
  Only the Level 2 upgrades were kept. The wiki text for Harak Skill1 was
  cut, so the earlier text stays.

## 2026-10-12

### New Features

- Synergy: added the rearmost buff penalty. Pandora and Ravion give buffs to
  the rearmost allies. A hero with an ally directly behind it is rarely
  rearmost. That hero now gets 10% of the rearmost part of the score.
- Rearmost buff special cases:
  - Receivers with a penalty: Gunnar, Hugin, Thador, Thoran, Daimon and
    Lucca.
  - Faramor, Niru, Cassadee and Galahad get no penalty. They can pick an
    ally in front.
  - Evie gets no penalty. Her quill moves to the ally with the highest
    damage after 3s.
  - The penalty applies only to the rearmost buffs. Other effects of the
    provider keep their score.
  - Dunlingr is not modelled yet.
- Added two behavior tags, `ally-behind-placer` and `ally-adjacent-placer`.
  The list `hidden_behavior_tags` in `heroes_config.json` hides tags for all
  heroes. Hidden tags stay in the data and in scoring. They do not show in
  the overview, the CSV or the site.
- Synergy: added the Protection path. A hero that gives an ally
  invincibility or cheat death now scores for strong, fragile carries.
  Examples of providers: Gunnar, Alna, Aliceth, Ravion, Hepler. Examples of
  carries: Gwyneth, Frieren.
- Protection score inputs:
  - The damage percentile of the receiver. Tanks and supports are not
    counted.
  - The fragility of the receiver (0.7x to 1.3x). It comes from HP and DEF
    percentiles across the roster.
  - The protection tier. A one-time save counts half.
- Protection special cases:
  - Gunnar gives no credit to moving receivers.
  - A receiver that protects itself gets half.
  - Pandora is excluded, because her protected ally cannot act.
  - Revives and spirit forms do not count.
  - Only the best effect per pair scores.
- The reason text reads `Protection via <label> (<targeting>, recurring|once)`.
- Mix mode counts only the best protected receiver of a protector.
- Mix mode: a static-tile buff (Gunnar, Hugin) reaches only the ally 1 tile
  behind the buffer. Mix mode now picks the best placement of these buffs
  for the team. A candidate gets the gain it adds to that placement, not its
  tile buff once for each teammate. Gunnar's protection is part of his tile
  buff. The Mix index carries `tileBuff` and `tileBuffers`.
- Synergy: added buff zones. A provider can place a zone, for example
  Estrilda's Pennon of Valor. The position of the receiver decides how much
  of the zone it stands in. An enemy-backline zone reaches a frontline
  receiver at 0.75.
- Synergy: Perseus and Orion need temporary ally stat buffs. They now value
  providers of temporary ally buffs. The list of qualifying stats is wider.
  It includes Movement speed and rivalry DMG Boost / DMG Reduction.
- Temporary buff score:
  - It grows with the number of different buff labels.
  - It grows with how often the buffs apply.
  - A `distinct_allies` requirement needs buffs from that many allies.
- Synergy: Mix mode adds a zone grouping bonus when the team has an
  enemy-grouping hero. A second temporary-buff provider gets a 1.5x bonus.
- Synergy: ATK buffs now scale with how much the skills of a hero depend on
  ATK. The multiplier is 1.0x to 2.0x. It replaces the old fixed 1.75x.
  ATK buffs now score for every hero with ATK-scaled skills.
- Synergy: Haste now scores for every receiver at weight 1.0x (was 1.25x).
  Haste is no longer a penalty for implicit fuel. A receiver with a fast
  signature skill and no ATK SPD matches Haste only.
- Synergy: Frieren, Marcille and Shemira keep ally Energy above Haste. The
  0.45x implicit-fuel penalty does not apply to them.
- Gunnar now appears for Gwyneth. Alna now appears for Frieren and Sylphira.

### Fixed

- Damage replacement: the old score checked only if a candidate has true
  damage. It ignored the amount. Silven (3 true damage) matched Aster (40
  true damage) almost fully. The score now compares the amounts.
- Damage replacement: a candidate that hits fewer enemies than the source
  now scores lower. Silven (single target) no longer replaces Aster (area).
- Senea: the damage detector now finds her true damage. It missed two
  texts.
- Ravion: EX+10 now provides `Fatal blow save`.
- Evie: the reveal text no longer counts as an ally provide.
- The synergy tooltip works again with character pills.

### Character changes

#### Rearmost buffs

| Character | What changed |
|---|---|
| gunnar, hugin | - Score from Pandora and Ravion is 10% of the rearmost part |
| thador, thoran, daimon, lucca | - Added tag `ally-behind-placer`<br>- Score from Pandora and Ravion is 10% of the rearmost part |
| faramor, niru, cassadee, galahad | - Added tag `ally-adjacent-placer`<br>- Scores do not change |

Examples of new scores: Thador from Ravion 13.62 to 1.36. Hugin from Ravion
16.86 to 1.69. Gunnar from Pandora 16.52 to 8.42. Gunnar keeps more score
because his other effects are not rearmost buffs. No other pair score
changes.

#### Buff zones and requirements

| Character | What changed |
|---|---|
| estrilda | - Added buff zone anchor (enemy backline) |
| hugin | - Added buff zone anchor (fixed tile) |
| kordan | - Added buff zone anchor (enemy target)<br>- Position set to frontline |
| mikola | - Added buff zone anchor (caster) |
| perseus | - Added buff zone anchor (caster)<br>- Requires buffs from 2 distinct allies |
| orion | - Requires buffs from 2 distinct allies |
| shakir | - Added buff zone anchor (caster) |
| smokey-meerky | - Added buff zone anchor (caster) |
| damian | - Added buff zone anchor (summon) |
| peggy | - Added buff zone anchor (summon) |
| berial, harak, igor, temesia | - Position set to roaming |
| chippy, gerda, himmel, kafra, lenya, seth, sinbad, soren | - Position set to frontline |
| lily-may, nara, niru | - Position set to ally backline |

#### Damage replacements

Aster: the damage replacements change from Sylphira, Lamentis and Silven to
Frieren, Cyran and Faramor. The Damage lists of 64 other heroes also change.
Senea does not appear for Aster. Her score is 0.45, which is below the
minimum of 0.5. She has no DoT.

| Character | What changed |
|---|---|
| silven | - Score as Aster replacement 0.99 to 0.10 |
| senea | - True damage is now detected (42.8, was 0) |

### Implementation changes

- Added `REARMOST_BUFF_LABELS`, `REARMOST_UNLIKELY_TAGS` and
  `REARMOST_UNLIKELY_FACTOR` (0.1) to `scoring.py`. A label applies to all
  skills of the provider, as with `STATIC_TILE_BUFF_LABELS`.
- `score_combined_synergy` scores the provider with and without its
  rearmost buffs. The result is the score without them plus 0.1 times the
  difference. `temp_buff_score` uses the same split.
- Added `scripts/hero_pipeline/hidden_tags.py`. It reads
  `hidden_behavior_tags` from the config. The projection step removes hidden
  tags from the views. The replacement scoring ignores them for Similar
  Skills.
- Added `scripts/test_rearmost_penalty.py`.
- The Protection path is automatic. It needs no `special_requires` entry.
- The constant `PROTECTION_BASE_MULT` is 16.
- The Mix index has the new fields `protection`, `groupingUplift`,
  `tempBuff` and `distinctAllies`. The pick field is `protection_score`.
- The synergies schema allows the new `protection` field.
- The new scoring fact `atk_dependency` sums the `N% (ATK-based)` values in
  the base skill text. It multiplies them by explicit hit counts. The
  multiplier is `1 + min(1, atk_dependency / 1500)`.
- Max HP keeps its share-based boost.
- Zone buffs score through the stat path. The reach of the zone scales the
  score (`BUFF_ZONE_REACH_WEIGHT`). A presence credit covers buffs that the
  stat path did not credit.
- The code reads the persistence of a buff from the skill text.
- The afkj-data exporter now writes `roster_percentiles` into `source.json`.
- Added the per-hero override `battlefield_position` (frontline, ally
  backline or roaming).
- Added the fields `zone_anchor` and `distinct_allies` to `ai.json` and to
  the schemas.
- Added `scripts/test_protection_synergy.py`.
- Extended `scripts/test_mix_synergy_index.py`.
- Fixed `scripts/test_synergy_overflow.js`. It failed because `heroByName`
  was missing from the test setup.
- Documented the new paths in `docs/synergy-algorithm.md`,
  `.cursor/AGENTS.md` and `.cursor/GLOSSARY.md`.
- Documented buff zones, temporary stat buffs and ATK dependency in
  `docs/synergy-algorithm.md` and `.cursor/MECHANICS.md`.
- Regenerated `heroes-overview.md` and the site data.
- Damage replacement: `_damage_replacement_coverage` in `scoring.py` now
  takes the damage profiles and the reach of both heroes. The score is
  `0.5 * type match + 0.5 * throughput`, multiplied by the reach ratio. The
  ratio is 1 when the candidate reaches as far as the source.
- The type match covers True damage, HP loss, DoT, Max HP-based damage and
  Lost HP-based damage. It compares amounts per type. The throughput part
  compares each damage type separately, so Physical cannot replace Magic.
- Added `SPECIAL_DAMAGE_TYPES` and `REPLACEMENT_DAMAGE_TYPE_BLEND` (0.5).
  Removed `REPLACEMENT_TRUE_DAMAGE_BLEND` (0.65).
- `_text_has_max_hp_damage` ignores a trailing "and inflict ..." clause.
  `_chunk_deals_enemy_damage` accepts "each <summon> deals N% (ATK-based)
  true damage".
- `ALGORITHM_VERSION` is now `local-analysis-v15`.
- Added tests in `test_replacement.py`, `test_detector_seams.py` and
  `test_pipeline_regressions.py`.
- Documented the new score in `docs/replacement-algorithm.md` and
  `.cursor/AGENTS.md`.

#### Summoner tag fix

Spectral spectators (Senea) and Stars (Aster) are not battle units. Summon
buffs, for example Peggy's, cannot target them. Both heroes lose the
`summoner` tag and their `summon_profile`.

| Character | What changed |
|---|---|
| senea | - Removed summoner tag (spectators are not battle units) |
| aster | - Removed summoner tag (Stars are not battle units) |

## 2026-10-11

### New Features

- The "score higher than" tooltip in "Units improving <hero>" now shows
  character pills (portrait and name).
- The score shows as `x/5`. It has one decimal and no trailing `.0`.
- Pills in the tooltip are clickable. They open the hero page.
- The tooltip stays open when the mouse moves into it.
- A click on the trigger text pins the tooltip. A click outside closes it.

### Fixed

- Melee and ranged detection is more accurate. It follows the new
  definition in `.cursor/MECHANICS.md`.
- Reclassified after review:
  - Lily May is now ranged (jump-and-retreat).
  - Lucy, Mehira and Damian are now melee.
  - Tasi is now melee and dual-range.
  - Taichi & Agumon is now melee and dual-range.
- Replacement lists changed for heroes with a new melee or ranged role.

### Character changes

| Character | What changed |
|---|---|
| damian | - Now classified as melee |
| lily-may | - Now classified as ranged |
| lucy | - Now classified as melee |
| mehira | - Now classified as melee |
| taichi-agumon | - Now classified as melee and dual-range |
| tasi | - Now classified as melee and dual-range |

### Implementation changes

- `is_melee` no longer uses the hero class. The rules are:
  - A default attack range of 2 or less is melee.
  - A range of 4 or more is ranged.
  - A summoner off the battlefield takes the type of its summon.
  - For range 3, the shortest skill range decides.
- Per-hero overrides cover the cases that text cannot show.
- Removed the Berial (`is_melee`) and Vala (`is_dual_range`) overrides.
  Detection gives the same result.
- Added the Map and Positioning sections to `.cursor/MECHANICS.md`. They
  cover the hex grid, tile numbering, front and rear, range, movement
  patterns and melee rules.
- Updated the counter skill and the glossary for the melee overrides.
- Regenerated the replacement lists in `heroes-overview.md`.

## 2026-10-02

### New Features

- Added Aster (Hypogean · Mage · Magic), Chaos Observer.
- Added Senea (Graveborn · Marksman · Magic), Deathless Songstress.
- Added Estrilda (Lightbearer · Rogue · Physical), Knight of Valor.
- Each new hero has a full skill analysis, a roster entry and a portrait.
- Estrilda: skill texts, upgrade tiers and release date (2026-10-09) come
  from the live wiki. Prydwen tiers are not published yet.

### Fixed

- Character portraits now download without errors.
- Updated the Karma play texts.
- Synced the Prydwen meta tiers with the live Prydwen pages.
  - Corrected stale ratings for 21 heroes.
  - Added the missing ratings for Karma.
  - Chippy, Hammie, Taichi & Agumon and Yamato & Gabumon have no Prydwen
    rating yet. They stay unrated.

### Character changes

| Character | What changed |
|---|---|
| aster | - Added as new hero |
| estrilda | - Added as new hero |
| senea | - Added as new hero |
| callan | - Refreshed relative stat ranks |
| contess | - Refreshed relative stat ranks |
| daimon | - Refreshed relative stat ranks |
| dunlingr | - Refreshed relative stat ranks |
| granny-dahnie | - Refreshed relative stat ranks |
| hewynn | - Refreshed relative stat ranks |
| ludovic | - Refreshed relative stat ranks |
| lumont | - Refreshed relative stat ranks |
| mikola | - Refreshed relative stat ranks |
| phraesto | - Refreshed relative stat ranks |
| reinier | - Refreshed relative stat ranks |
| solise | - Refreshed relative stat ranks |
| temesia | - Refreshed relative stat ranks |
| thador | - Refreshed relative stat ranks |
| ulmus | - Refreshed relative stat ranks |
| velara | - Refreshed relative stat ranks |

### Implementation changes

- Added Estrilda to the hero list of the downloader.
- Fixed pipeline issues that made portrait downloads fail.

## 2026-09-24

### New Features

- Merged and renamed damage types in the list view and in CSV exports.
  Filtering by damage type is now easier.

### Fixed

- Repaired skill data and values for almost every character. The wiki skill
  texts were sometimes incomplete or incorrect.
- Repaired the detection of the "stats steal" mechanic.
- Fixed the detection of HP-loss, max-HP, lost-HP and true damage. These
  damage types were often confused.
- Updated the Karma portrait image.

### Character changes

| Character | What changed |
|---|---|
| aliceth | - Refreshed skill effects to match text; reclassified damage types |
| alna | - Fixed confirmed skill-effect gaps against skill text |
| alsa | - Gated Swift Evasion shield on 7s re-trigger |
| antandra | - Refreshed skill effects to match text |
| arden | - Refreshed skill effects to match text |
| athalia | - Refreshed skill effects to match text |
| aurora | - Deduped Ultimate 320% Magic damage to single text-backed row |
| baelran | - Fixed Ultimate to 10% HP AoE; removed unsupported 400% |
| bonnie | - Refreshed skill effects to match text |
| brutus | - Refreshed skill effects to match text |
| bryon | - Removed spurious Haste; added Tacit Strike 200% heal + 40% HoT; fixed Ult storm DoT |
| callan | - Refreshed skill effects to match text |
| carolina | - Refreshed skill effects to match text |
| cassadee | - Refreshed skill effects to match text |
| cecia | - Fixed DoT to 140% + summon to 60% |
| contess | - Reclassified damage types; refreshed counters/behavior |
| cryonaia | - Removed unsupported 77% value |
| cyran | - Refreshed skill effects to match text |
| daimon | - Refreshed skill effects; reclassified damage types |
| damian | - Refreshed skill effects to match text |
| dionel | - Refreshed skill effects to match text |
| dunlingr | - Refreshed skill effects to match text |
| eironn | - Split slash 125% / stab 250% |
| eryndor | - Refreshed skill effects to match text |
| evie | - Refreshed skill effects; reclassified damage types |
| faramor | - Fixed Skill2 ATK 15% and Exclusive self ATK 10% |
| fay | - Added Skill2 160 damage + DEF; fixed Exclusive Vitality 25 |
| florabelle | - Fixed summon duration to 10s |
| frieren | - Fixed Ult to True 1800; rebuilt Skill1/2 rows; removed spurious DoT |
| galahad | - Fixed Ult/max damage, Skill1 AoE strikes, shield-expiry damage |
| gerda | - Fixed damage 180 / 260 / 150 + HoT and 400 shield rows |
| granny-dahnie | - Fixed Energy 40 + durations; added Haste/damage; Vitality 19; reclassified damage |
| gunnar | - Rebuilt Ult 640 / meteor 550 / DoT; fixed Skill1 80 and Invincible ally row |
| gwyneth | - Fixed 280 damage, periodic DoT, ATK SPD, DEF Pen 60 |
| hammie | - Fixed ATK duration to 5s |
| harak | - Moved devour to Skill2; dropped unsupported Skill1 invincibility; reclassified damage |
| hepler | - Added Haste 90, deduped HoT, rebuilt Exclusive invincible/cheat-death/buff rows |
| hewynn | - Fixed damage 300 and Damage taken 36% |
| himmel | - Added Skill1 unaffected + Skill2/Ex heals; moved party require |
| hodgkin | - Dropped unsupported heal-inhibitor tag |
| hugin | - Fixed Haste 10s, shields 8s, defensive rows |
| igor | - Fixed Ult 270 / Skill1 170; rebuilt heal + cheat-death + lifedrain |
| indris | - Fixed Ult to True-only + 8s silence; fixed durations; reclassified damage |
| isabella | - Fixed ATK debuff 75% 5s and Exclusive 8s |
| kafra | - Fixed Haste 5s and Supreme+ 520 |
| karma | - Portrait + audit sidecar refresh (clean in audit) |
| kazim | - Rebuilt Ult arc + Skill1/2 values; fixed Exclusive; reclassified damage |
| koko | - Added Damage taken + spear rows; fixed shield 7s |
| kordan | - Fixed confirmed skill effects against text |
| korin | - Fixed area 2, True 220, Damage taken 25%; deduped Max HP; reclassified damage |
| kruger | - Rebuilt DEF / Damage taken / shield / ATK rows |
| kulu | - Added Ex doom-bomb max-HP rider |
| laios | - Rebuilt DEF/stun, heals 500/560, summon rows |
| lamentis | - Added Max HP debuff + ATK SPD; fixed Max HP 20% |
| lenya | - Fixed Single 480 / Single 260 + Area 390 / crit + stun rows |
| lily-may | - Fixed Ult 240; rebuilt invincible / ATK-stack / True damage rows |
| lorsan | - Fixed Haste 5s, HoT 120, immunity scope |
| lucca | - Fixed Ult 240; rebuilt shield 400 + damage 150 |
| lucius | - Fixed shields 520 / 320 / 3% and damage 70 |
| lucy | - Corrected fully-ascended shield 450 -> 550; damage reclass |
| ludovic | - Corrected Ex berry heal 130 -> 150; reclassified damage |
| lumont | - Fixed taunt 4s, shield/DEF rows; removed spurious stun |
| lyca | - Added Energy/duration rows; fixed DEF debuff; fixed Focus tier |
| marcille | - Added Area blind + heal 300; fixed once-per-battle + energy rows |
| marilee | - Fixed conditions and ATK-stack conditions; fixed Focus tier |
| mehira | - Fixed Ex Skill, Skill1, Ultimate sidecar gaps |
| mikola | - Fixed sphere 12s, heal count, HoT 12%/s |
| mirael | - Fixed Area 3 and DoT 14s + conditions |
| nara | - Fixed Energy Self 750, HP-loss 5%, Physical 80, ATK 20% |
| natsu | - Added Crit 5 + Crit DMG 5 |
| nazrik | - Refreshed skill effects to match text (audit-clean) |
| nerion | - Fixed ATK buff 30% 12s and spear 220 Area |
| niru | - Refreshed skill effects to match text (audit-clean) |
| odie | - Fixed Exclusive energy target to Self |
| orion | - Refreshed skill effects (audit-clean) |
| pandora | - Triage fix + damage reclassification |
| pang | - Refreshed skill effects to match text |
| parisa | - Fixed durations to 10s |
| peggy | - Refreshed skill effects to match text |
| perseus | - Refreshed skill effects to match text |
| phraesto | - Refreshed skill effects; reclassified damage |
| pippa | - Triage fix + damage reclassification |
| ravion | - Fixed Supreme+ sidecar gaps |
| reinier | - Corrected Ex max damage to 300% per text |
| rhys | - Triage-corrected stale expectations |
| rolan | - Refreshed skill effects; damage reclass |
| rowan | - Refreshed skill effects to match text |
| saida | - Fixed DoT, removed stale Energy 240, removed spurious immunity |
| salazer | - Added missing stat-steal Self 12% permanent; fixed label/target |
| satrana | - Fixed Exclusive Self/ally splits + Energy 200 |
| scarlita | - Refreshed skill effects to match text |
| seth | - Refreshed skill effects (audit-clean) |
| shadewing | - Added missing Legendary+ Hero Focus ATK buff |
| shakir | - Triage-corrected stale expectations |
| shemira | - Fixed to True-only delivery; reclassified damage |
| silven | - Fixed to True-only; corrected Exclusive ATK |
| silvina | - Refreshed skill effects (audit-clean) |
| sinbad | - Moved mark provider to correct location |
| smokey-meerky | - Triage fix + damage reclassification |
| solise | - Removed duplicate Magic DEF; fixed values 30 / ATK 15 |
| sonja | - Fixed Ult 672 and Lifedrain row |
| soren | - Removed spurious Supreme rows; fixed value 90 |
| sylphira | - Corrected skill effects against skill text |
| taichi-agumon | - Added Max HP + 330 rows; damage reclass |
| talene | - Rebuilt Ultimate / Skill1 / Skill2 rows |
| tasi | - Refreshed skill effects (audit-clean) |
| temesia | - Removed spurious Damage-dealt buff |
| thador | - Rebuilt Ultimate rows; fixed shield 8s |
| thoran | - Captured pact recovery; triage fix |
| tilaya | - Refreshed skill effects (audit-clean) |
| twins | - Refreshed skill effects to match text |
| ulmus | - Fixed Max-HP formula + 260 value |
| vala | - Fixed buff Self + lost-HP 12% |
| valen | - Refreshed skill effects (audit-clean) |
| valka | - Removed spurious shield; fixed to True damage; reclassified damage |
| velara | - Fixed durations; removed stale Haste; fixed tier selection |
| viperian | - Fixed confirmed discrepancies; reclassified damage |
| voracia | - Refreshed skill effects (audit-clean) |
| walker | - Fixed lost-HP and mark rows |
| yamato-gabumon | - Fixed to True damage + energy; reclassified damage |
| zandrok | - Fixed Max HP target to Self |
| zanie | - Refreshed skill effects (audit-clean) |
| zorya | - Fixed ATK-stack extraction |
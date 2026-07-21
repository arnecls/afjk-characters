# AFK Journey context

## Temporary files

When generating ephemeral files only required for a single agent run, create
these files in the directory called `tmp`.

## Factions

- Wilders
- Maulers
- Graveborn
- Lightbearer
- Celestials
- Hypogeans
- Dimensional

**Celestial–Hypogean pairing** — for faction-bonus counting, Celestial
and Hypogean heroes are treated as one faction (in-game dimensional
bonus). Does not merge the separate **Dimensional** roster tag used
for crossover units.

## Classes

- Tank
- Support
- Marksman
- Mage
- Rogue
- Warrior

## Artifacts

[Artifacts](https://afk-journey.fandom.com/wiki/Artifact) are equippable items
selected before battle. They grant team stat buffs and cast **Assistance**
skills during combat — a core mechanic separate from hero kits.

**Skill text naming:** when a skill mentions **Magister Merlin**, that is the
story name for the **player** (the protagonist), not a roster hero.
**Magister Merlin's skills** means the **Artifact currently enabled** for
that fight — i.e. its Assistance effects, not any hero's abilities.

- **Starter Story artifacts** — unlocked through Main Quests; remain permanently
  available and effective in every season.
- **Seasonal artifacts** — unlock per season and apply only for that season;
  the roster rotates roughly every three months.

## Damage types

- Normal damage types
  - Physical
  - Magic
  - Ranged
- True damage tyes
  - True damage (classic, no HP scaling in the phrase)
  - HP loss — extra/true damage scaling on **the target's lost HP**
  - Max HP-based damage — damage scaling on **the target's max HP**
- Damage over time (DoT)

Damage over time needs to derived from text by look for indicators like "deals
damage for 2s".

True damage types ignore defensive stats and shields.

**Hierarchy:** Max HP-based damage and HP loss are specialized forms of true
damage. When both a generic `True damage` label and a concrete subtype apply
to the same scaling phrase, keep the subtype and drop generic True. Never
drop Max HP-based damage or HP loss in favor of generic True damage—the
subtype labels are more precise (including `plus extra true damage equal to …
max HP` riders).

## Targeting

- Self
- Single target
- Multiple targets
- Arc
- Area
- All units

To detect these targeting types, the text needs to be searched for wordings like
"In an arc", "all", etc. This needs to be done by the Agent, as text are too
fuzzy to define clear rules. **Per clause:** do not copy Area or All units
reach from splash/AoE wording onto a primary-target or capped multi-target
effect in the same sentence (e.g. silence on the target vs splash stun).

## Crowd Control

- Stun (unable to move or act)
- Bind (immobilize, entangle, imprison; cannot move but may still act)
- Knock down (unable to move or act)
- Knock up (unable to move or act)
- Knock back (unable to move briefly; forced reposition backward)
- Frighten (run around in panic, no casting)
- Silence (no spell casting)
- Charm (attacks their own allies)
- Sleep (hypnotized; cannot move or act)
- Displace (force new position; pull/teleport without knock immobility)
- Blind (cannot use normal attacks)
- Disarm (prevents normal attacks; an abnormal status in-game; skills unaffected)
- Interrupt (stop ultimates)
- Taunt (force attack on caster)

Enemy freeze/frozen/freezing text maps to **Bind** (often paired with damage in
the same skill). Battle-time pause and freeze-and-defeat execute are special
mechanics, not standalone CC types.

These types need to be derived from the text.
For example:

- "knocking them back" -> Knock back
- "knocking them into the air" -> Knock up
- "knocking them down" / "knocks the enemy down" -> Knock down
- "hypnotizing all enemies" -> Sleep
- "stunning them" -> Stun
- "unable to move" / "immobilize" / "bind" -> Bind
- "freezing them" / "freeze enemies" -> Bind
- "pulling in enemies" -> Displace

This needs to be done by the Agent, as text are too
fuzzy to define clear rules.

## Buffs (summary lines)

Buff lines use `{label} ({tier}) — {targeting} — {magnitude}`.

Optional suffix: `— conditional (frequent)` or `— conditional (rare)`.

- **conditional (frequent)** — gated but usually applies often in a fight
  (e.g. on cast, on kill, first proc). Magnitude is not reduced.
- **conditional (rare)** — not every battle or hard to proc (e.g. enemy
  monsters, ingredients, once per battle). Magnitude is lowered by two steps
  (`high`→`low`, `average`→`low`).

Synergy picks in `heroes-overview.md` skip rare conditional ally buffs.

## Fully ascended comparison

Synergy ranking and roster-wide magnitude bands assume every hero is **fully
ascended**: all skill slots unlock (Ultimate through Supreme+ / EX tiers), and
numeric comparison uses the **strongest parseable value** per effect label
across skill level lines — not the base unlock value. This is implemented in
`_merge_effects_from_list()` in `rewrite-summaries.py` (max numeric wins).
Processed JSON may set `is_max_known: false` when higher tiers still
use `(scaled)` placeholders in source text.

## Quality indicators

Summary lines mark relative strength with **`high`**, **`average`**, or
**`low`** (backticks in output). These rank an effect against the **full
roster** (same effect label), not same-role peers only.

- **Buffs / debuffs** — parsed % compared within the same label across
  all heroes (quantiles when enough data); debuffs also reward
  `all enemies` reach. `assign_magnitudes()` in `rewrite-summaries.py`.
- **Crowd control** — duration-based (≥5s → high, ≥2s → average).
- **HP loss / max-HP / true damage** — composite score from %, targeting, and
  frequency; roster-wide quantiles in `assign_damage_magnitudes()`.

**Tier** in parentheses (`Mythic+`, `Level 3`, …) is unlock level, not
strength. **Conditional (rare)** lowers magnitude by two steps; some labels
(Invincible, Fatal blow immunity) are always high.

## Meta tiers (Prydwen)

Per-mode strength ratings (`S+`, `S`, `A+`, `A`, `B`, `C`, `?`) are stored on
each hero in `heroes_data.json` as `prydwen_tiers` (`afk_stages`, `dream_realm`,
`dream_realm_endless`, `pvp`). Sourced from the
[Prydwen tier list](https://www.prydwen.gg/afk-journey/tier-list) via character
pages during `just download`. Shown at the top of each hero's behavior section
in `heroes-overview.md` (comma-separated text) and the site viewer (tier boxes).
Do not confuse these with ascension unlock tiers in skill summaries.

Synergy scoring weights magnitude (high > average > low). When auditing,
compare heroes with the same buff/debuff label — wrong targeting or clause
parsing often yields wrong indicators.

## Hero docs

- **Heroes.md** — skill text from Yaphalla (and manual edits). No `### Summary`
  sections.
- **heroes-overview.md** — generated synergies plus `### Summary` per hero.

Regenerate overview (and strip stray summaries from Heroes.md if present):

`python3 scripts/generate-heroes-overview.py`

Summary/synergy rules live in `scripts/rewrite-summaries.py` (library).

## Behavior (movement & casting speed)

Each hero in `heroes-overview.md` starts with `### <name>'s behavior`:

- **Movement** — `stationary`, `mostly stationary`, `moving`,
  `high movement`, or `moving / stationary` (dual units). Derived from
  per-skill `Skill Range`, cooldown-weighted attack ranges, and
  repositioning phrases in skill text. Special cases in
  `compute_movement()` in `rewrite-summaries.py`: off-battlefield heroes
  (Damian), summon controllers (Bryon), dual units (Twins), constant
  movers (Rhys), dormant/rooted cycles (Zorya, Ulmus), explicit hero
  repositioning (Rowan), brief aerial reposition (Scarlita), pull-to-self
  (Nara), normal-attack range priority (Walker). Range uses
  Ultimate/Skill1/Skill2 only (not Ex). Summon/companion movement and
  dormant sentences are excluded before range and repositioning analysis.
  Data from
  [heroes2.md](heroes2.md); falls back to [Heroes.md](Heroes.md) (aliases:
  Twins → Elijah & Lailah).
- **Signature skill** — the one skill that most characterises how the
  hero is played. Stored in `data/signature_skills.json` (key =
  display name from `heroes-overview.md`). Each entry has
  `signature_calculated` (best repeatable, buffable skill by category:
  `ultimate`, `skill1`, `skill2`, `skill4`) and optional
  `signature_override` when the curated identity skill differs.
  Effective signature = `signature_override ?? signature_calculated`.
  Optional `speed_override` applies to the effective signature.
  Skill names resolve from `heroes_data.json`; shown in the behavior
  block as `**Signature skill**: {name} [(ultimate)]`.
  Often the Ultimate, but not always. Pick the skill that defines the
  unit's identity in combat.
  **Indicators:** enhanced by Ex / Supreme+ (`Enhance Force`); unique
  mechanic few others share; exceptional damage or buff; battle-start or
  formation setup.
  **Synergy fuel fallback** — when the effective signature is a
  non-buffable **Ultimate** that is still slow (not fast/battle-start),
  `signature_calculated` drives `synergy_signature_speed` instead.
  Non-ultimate signatures (e.g. Bonnie's Skill1) keep primary speed so
  fuel targets identity, not a side ult.
- **Placement constraints** — optional top-block bullets when skill text
  ties ally buffs to grid placement or auto-selected allies:
  **Ally composition** (`ally_placement` + `ally_composition` kinds) and
  **Self placement** (`self_placement`). Detected in
  `detect_placement_constraints()`; stored in
  `behavior.placement_constraints`. Overrides in
  `data/placement_constraint_overrides.json`.
- **Skill overview** — `#### Skill overview` subsection with rows for
  **Signature skill** (labeled **Signature skill (ult)** when the
  ultimate row is omitted), **Ultimate** (only when signature is not the
  ultimate), and **Non-ultimate**. Each row lists only non-`none`
  indicators among `speed`, `first cast speed`, `heal`, `buffs`, `debuffs`,
  `damage` (damage last; `high` / `average` / `low`; speed `slow` / `average`
  / `fast`). **First cast speed** is shown when the opener applies at battle
  start or battle preparation while recurring cast speed is slower (e.g.
  Cassadee's Tidal Strength blesses at battle start). For **Ultimates**,
  `fast` first cast speed aligns with `high-initial-energy` (effective IE ≥
  500 at full build and first cast within ~5s) or a free/guaranteed early
  ultimate cast (`battle-start-ult`); passive battle-start setup alone does
  not count.
  When any tier deals **HP loss**, **Max HP-based damage**, or **True
  damage**, a final `- **True damage**: {type} \`{mag}\`, …` line lists types
  (peak per type across tiers; p75 for non-ultimate).
  Computed in `compute_skill_overview()` in
  `rewrite-summaries.py`; stored in `behavior.skill_overview`. Speed uses
  `compute_per_skill_speeds()` roster-wide quantiles. Damage scores per skill
  section from chunk text (roster-wide quantiles). Heal/buffs/debuffs peak
  magnitudes from `skill_slices` effects. Non-ultimate row aggregates
  Skill1/Skill2/Ex with **p75** per metric type. Synergy fuel still uses
  `signature_skill_speed` / `synergy_signature_speed` in processed JSON
  (not shown in the markdown block).
  After the metric rows (and optional True damage line), **per-category
  summaries** appear as `##### {slot}` headers with a short paragraph
  underneath. Summaries come from `data/heroes_data_skill_summary.json`
  (key = display name, then `category` from processed JSON:
  `ultimate`, `skill1`–`skill5`). Labels: Ultimate, Skill 1, Skill 2,
  Legendary+, Ex. Skill, Supreme+.

**Skill cards** (site character sheet) — chip tags under each skill summary
in `site/data/heroes.json` → `sections.skillCards`. Tags are computed during
`just analyze` from the same `analyze_hero()` pass as processed JSON:

- **Damage chips** — labels from `skill_slices[section].effects` (category
  `damage`), not a second pass over raw skill text.
- **Buff / debuff / CC / immunity chips** — same `skill_slices` effects.

Stored on each skill as `skill_card_tags` in `heroes_data_processed.json`.
`render_site.py` reads those tags (does not re-derive). After changing
effects in `data/skill_effects/<short_name>.json`, run `just views`
(analyze + render) so processed JSON and the site stay aligned.

**Skill effect extraction** (AI-authored sidecar, not regex):

- Source of truth: `data/skill_effects/<short_name>.json` per hero.
- `analyze_hero()` loads sidecar via `scripts/skill_effects_store.py`.
- Each skill entry stores `source_hash`; stale hash fails `just validate`.
- To fix detection: re-extract with the extract-skill-effects skill — do not
  edit regex rule tables (removed from `rewrite-summaries.py`).

**Skill summary authoring** (AI-generated, not scripted):

- Read fully ascended `description` from `heroes_data_processed.json`.
- Cross-check against `description_lite` in `heroes_data.json` for each
  skill slot — it is the preferred source for validating mechanics and
  catching missing or invented effects.
- Write a **short mechanic summary** using **generalized game vocabulary**
  from `data/schema/game_properties.schema.json` (damage types, CC,
  stats, immunities, battle phases) and effect labels in
  `data/schema/skills.schema.json`.
- **No numbers** (no `%`, tile counts, cooldowns, energy values).
- **No hero-specific wording** — no hero names, skill names, companion
  or grant names, or skill-only imagery (feather, lance, dark cloud,
  winged form, intel, party, etc.). Use generic terms instead:
  transformation, companion, summon, mark, ally grant, DoT zone,
  HP-loss, observation stacks, formation, bond, channeling.
- Use schema vocabulary in **display form**: `HP-loss`, `knock down`,
  `knock back`, `knock up` — not enum tokens like `hp_loss` or
  `knock_down`.
- Prefer established game terms over flavor nouns: **circular area** or
  **zone** (not magic circle), **melee buff state** (not combat stance),
  **area with most enemies** (not dense group), **counterattack** (not
  retaliate), **channel then single-target magic damage** (not charged
  fireball), **sequential single-target shots** (not artillery salvo),
  **line AoE** (not piercing stun line), **untargetable aerial AoE
  damage** (not repeated spear thrusts), **AoE zone** (not storm centered),
  **mobile aura zone follows caster** (not empowerment sphere follows),
  **removed from battlefield** (not separate dimension), **clone** (not
  illusion copy).
- Describe **what happens** (mechanics/effects), not ascension tier
  labels or flavor nouns tied to one hero.
- **Punctuation conventions** (avoid ambiguous phrasing):
  - **Passive / active:** prefix `Passive:` and `Active:` when both
    appear, or split into two sentences.
  - **Participial phrases:** comma before `-ing` clauses that describe
    the caster's action (`enemy, dealing …` not `enemy dealing …`).
  - **CC types:** separate CC from follow-up with comma or `then`
    (`knock back, then stun` not `knock back stun`).
  - **Abbreviations:** expand `regeneration` (not `regen`), `trigger` /
    `bonus effects` (not `proc`), `normal attacks` (not `normals`),
    `alternate form` (not `alt form`); keep ATK/DEF/HP/AoE/DoT.
  - **HP wording:** use **HP-loss** for the damage type; **max HP
    reduction** for cap penalties; **ally losing HP** for heal triggers.
  - **Lists:** Oxford commas for stat/effect lists (`HP drain, haste
    reduction, and vitality reduction`).
- Validate with `just validate` (`skill_summary` check group).
- Run tests with `just test` (parallel pytest via pytest-xdist; ~2–3 min with
  roster cache). Use `just test-serial` for serial unittest output when
  debugging a failure (~4–5 min). Avoid piping `pytest -q` to `tail` — output
  is block-buffered and looks hung in agents.

Regenerate: `python3 scripts/generate-heroes-overview.py` (or `just overview`).

## Behavior tags

Curated combat-role tags live in `data/hero_behavior_tags.json`; allowed values
are enumerated in `data/schema/tags.schema.json`. Tags drive **Similar Skills**
replacement scoring (Jaccard overlap on shared tags in
`generate-heroes-overview.py`). Any hero pair with at least one shared tag can
appear; more shared tags score higher. Other replacement categories still use
the global minimum score from `heroes_config.json`. **Chip magnitudes**
(`assign_magnitudes()`) use **roster-wide per-label quantile bands**;
**replacement profiles** (buff, healing, damage, debuff, cc) use **global raw
throughput, numeric, or duration scores** so substitutes compare on absolute
kit strength rather than percentile labels.
**Replacement ranking** sorts by kit similarity first (coverage / Jaccard);
Prydwen tier breaks ties only. For tier comparison, `dream_realm` and
`dream_realm_endless` are merged to the **max** of both (three modes:
afk_stages, dream_realm, pvp). Candidates **without any Prydwen tiers** are
excluded; candidates **2+ tiers below the source on every overlapping mode**
are excluded. Synergy ranking is unchanged. **Buff/debuff/CC replacement
profiles keep full targeting weights** (area, all units, etc.) so substitutes
compare on maximum kit reach; synergy stat-buff scoring does not.
Assign a small set
(typically three to five) that describe how the hero is played, not every minor
skill effect.

- ally-buffer: Grants meaningful offensive or defensive stat buffs to allies.
- ally-healer: Restores ally HP directly or via healing over time as a core role.
- ally-shielder: Grants shields to allies as a significant part of the kit.
- aoe-damage: Deals substantial multi-target or area damage on a regular basis.
- aoe-healing: Heals multiple allies or wide ally groups, not only single-target sustain.
- assassin: Selectively attacks a chosen enemy by **non-positional** combat
  criteria (weakest, marked, highest energy, isolated, role marks, etc.) so
  the pick can be any row. Not rear/far/highest-damage selectors (use
  `backline-assassin` / `backline-inhibit` instead).
- backline-assassin: Enemy-facing pressure that **selects rear/far/highest-
  damage** (or equivalent) and can kill that target within ~10s via
  substantial damage. Qualifies: explicit rearmost/farthest/greatest-distance
  or highest cumulative damage dealer; forcing allies to attack such a target;
  teleport/dash self or an ally onto that target or into the backline. If the
  skill does not teleport/dash-to-target, Skill Range must be **Global or
  > 5 tiles**. Not soft poke, DoT-only (unless the kit can still delete a
  backliner in ~10s), self-retreat to allied backline, taunt, prefer-only AI
  without explicit select, or melee walk/charge without teleport.
- backline-inhibit: Same **target selectors** as `backline-assassin`, but the
  effect slows or softens that unit (CC, Haste/slow, DEF cuts, damage-taken
  amp, DoT, etc.). Damage plus inhibit on the same clause → both tags.
- battle-start-burst: Deals damage to one or more units in the first ~2–3s of
  battle. Primary signal: skill text with "when a battle starts" / "at battle
  start" combined with damage dealt (e.g. Gerda Skill 1, Nerion Mythic+,
  Walker grenades). Also qualifies when a skill auto-casts at battle start or
  with a short initial cooldown so damage reliably lands in the opening seconds
  (e.g. Marcille's early channeled flash, Atalanta Mythic+ double Sweet
  Encounter at battle start). Not buffs, shields, debuffs, energy, or summons
  alone without immediate damage; not sequential battle-start cycles where
  non-damage effects run before the first hit (Cyran Mythic+).
- battle-start-ult: Casts ultimate or reaches full energy unusually early in the fight.
- battlefield-modification: Adds physical obstacles or transforms the map layout; buff or debuff zones alone do not count.
- cc-immunity: Grants self or allies immunity to crowd control as a defining mechanic.
- cheat-death: Survives a would-be defeat or critical HP threshold via
  self-recovery (delayed resurrect, drain-seed revival, low-HP retreat/root,
  etc.).
- counterattack: Punishes enemies for attacking the hero with reactive damage or effects.
- interrupt: Applies hard shutdown effects such as Silence or Interrupt beyond routine CC.
- dot-specialist: Relies on damage over time or recurring tick damage as a primary pattern.
- enemy-debuffer: Applies meaningful stat or combat debuffs to enemies as a core output.
- enemy-grouping: Pulls, pushes, or clusters enemies to set up follow-up damage or CC.
  Providers with this tag satisfy receiver **Enemy grouping** requires when
  their displacement or area control is strong enough (`match_enemy_grouping`
  in `generate-heroes-overview.py`). Zone anchors such as Faramor use the
  require label; they are not tagged as groupers themselves.
- energy-provider: Grants Energy to allies or routinely accelerates ally ultimates.
- execute: Finishes low-HP enemies or scales damage strongly on wounded targets.
- high-damage-ult: Ultimate is the main damage spike and a large share of total output.
- high-initial-energy: Ultimate starts with **≥ 500 effective Initial Energy**
  when fully built (Ultimate `Initial Energy` meta plus the highest ascension
  bonus such as "Gains extra N initial Energy"). Aligns with fast ult fill
  (~≤ 5s at 100 energy/s). Not the same as `battle-start-ult` (free or
  guaranteed early cast without relying on IE fill).
- hp-scaling: Damage, survivability, or effects scale strongly with HP values.
- invincibility: Grants damage and/or control immunity windows to self or allies.
- life-drain: Sustains through lifesteal or HP recovery tied to dealing damage.
- mark-target: Marks or designates units so allies or self can focus amplified damage.
- mass-cc: Applies crowd control to multiple enemies or wide areas reliably.
- non-ult-utility: Delivers meaningful combat value from non-ultimate skills
  without relying on the ultimate. Path A: at least two `high` effect
  categories across qualifying Skill1/Skill2/Ex sections. Path B (when Path A
  misses): strong non-ult attacks (Lily May), opening burst mages with debuff
  focus (Bonnie), or hp-scaling shield damage (Daimon) — see
  `scripts/audit_non_ult_utility.py`. Not `high-damage-ult` or
  `battle-start-ult`; not start-of-battle ultimate text (e.g. Alna); exclude
  ultimate-support sections from scoring.
- revive: Brings defeated allies back to the fight (e.g. Marcille); not
  self-survival.
- self-repositioner: Regularly moves self across the grid via jumps, dashes, or teleports.
- static-tile-buffer: Buffs an ally only while they remain on a specific placement tile.
- stealth: Enters hidden or untargetable states to avoid focus or enable picks.
- summoner: Fields battlefield summons — independently acting combat units
  placed on or remaining on the battlefield beyond the cast animation.
  Timed or untargetable fighters qualify; transient attacks/effects (e.g.
  Marcille Sky Fish) and passive objects (e.g. Pandora's box) do not. Curated
  roster and source skills live in `data/hero_summon_profiles.json`.
- taunt: Forces enemies to attack the hero or redirects enemy focus onto them.
- temporary-stat-buffer: Grants at least one **temporary** ally stat buff
  (`persistence: temporary` on an ally-targeted positive stat effect in the
  skill-effects sidecar). Self-only and summon-only buffs do not qualify.
  `just validate` cross-checks ally `target` against source skill text and
  rejects summon-only/self-only mislabels; not inferred from `ally-buffer`
  alone.
- ultimate-cancel: Cancels or interrupts enemy ultimates when they begin casting.
- untargetable: Routinely becomes untargetable by enemy skills during normal gameplay.

## Detecting synergies between units

Synergy is **provider → receiver**: one hero supplies what another needs.
Automated ranking lives in `scripts/generate-heroes-overview.py`; when
reviewing or fixing matches, work through both heroes in this order.

1. **Summarize each hero** from `Heroes.md` skill text (see `### Summary` in
   `heroes-overview.md` or run `rewrite-summaries.py`). Extract:
   - **Stats the unit benefits from** — stats they self-buff or scale on
   - **Ally buffs** — buffs that hit allies (`Single target` through
     `All units`; not `Self`)
   - **Summon buffs** — buffs on allied summons only
   - **Requires** — partner-enabled special effects (not self-setup)

2. **Match provider → receiver** on three paths:
   - **Stat buffs** — ally buff label maps to a receiver benefit stat
     (e.g. `Haste buff` → Haste or ATK SPD; `Shield` → Shield only, not Max HP)
   - **Summon buffs** — summon buffs for heroes who field summons
   - **Enablers** — provider satisfies a receiver **Requires** label
     (DoT on enemies, magic damage from allies, party composition,
     **Enemy grouping** for zone receivers, etc.)

3. **Score and rank** — broader targeting and higher magnitude win; skip
   **rare conditional** ally buffs; sum stat + summon + enabler scores; keep
   the top five partners per receiver. Drop weak-only picks (generic ATK,
   Max HP / Shield when the receiver does not value those stats). Shields do not
   count toward Max HP scaling needs.
   **Defining-tier enablers:** requirements from Ex-Skills (`Mythic+`,
   `EX+n`) and `Supreme+` skills are unit-defining and score higher via
   `DEFINING_TIER_SCORE_MULT` in `generate-heroes-overview.py`.
   **Early-battle energy:** providers that grant ally Energy at or right
   after battle start score extra when the hero's **curated signature is a
   slow Ultimate** or when **`signature_first_cast_needs_energy`** is set
   (`receiver_wants_early_battle_energy` in `generate-heroes-overview.py`).
   The first-cast flag covers slow-opening ultimates whose recurring cast
   speed is fast after post-ult Haste (e.g. Tasi). Units whose identity is
   a battle-start Skill1/Skill2 (Bonnie, Kulu, etc.) are excluded even if
   their side ultimate is slow. First-cast receivers use the slow early-battle
   multiplier even when `ult_speed` is fast. Early-battle Energy scoring uses
   flat single-target reach for all providers; lieutenant grants parse their
   numeric amount (e.g. Thador EX+10: 350 Energy) so focused batteries can
   outrank diluted team-wide grants. Display keeps early-battle Energy picks
   visible even when the provider is a roster-wide common buffer.
   **Signature-skill fuel:** Haste/ATK SPD ally buffs are boosted by the
   receiver's effective synergy signature speed (`SIGNATURE_FUEL_SPEED_MULT`:
   slow 1.6×, average 1.2×, fast 1.0×). Energy recovery uses a lighter
   `SIGNATURE_FUEL_ENERGY_MULT` (slow 1.3×) plus `ENERGY_SYNERGY_SCORE_MULT`
   (0.72×) so batteries do not dominate lists. **High-damage ultimate
   carries:** receivers tagged `high-damage-ult` without `high-initial-energy`
   or `battle-start-ult` get `HIGH_DAMAGE_ULT_ENERGY_PREF_MULT` (2.25×) on
   ally Energy (ongoing and battle-start) so comparable batteries outrank
   Haste. Slow/average effective speeds
   also implicitly value Energy and ATK SPD at `IMPLICIT_FUEL_BASE` (0.45×)
   when not in benefit stats.    Buffability
   is detected from skill text (`NON_BUFFABLE_SIGNATURE_RES` in
   `rewrite-summaries.py`).
   **Proximity aura buffs:** provider-attached auras/circles (e.g. Shakir's
   Lupine Aura) and **provider-anchored ground zones** (e.g. Perseus fertile
   ground — allies standing on ground within N tiles of the provider) are
   detected in `rewrite-summaries.py` (`PROVIDER_PROXIMITY_AURA_PATTERNS`).
   Ally buffs tied to those zones only score for receivers whose **weighted
   attack range** is melee-close enough to stand in the zone (`receiver_can_reach_proximity_aura` in
   `generate-heroes-overview.py`; tunables in `heroes_config.json` →
   `proximity_synergy`). Global buffs (Twins dance, etc.) are unaffected.
   Complements the existing rule that skips **positional tile** buffs and
   **`static-tile-buffer`** providers for **moving/high-movement** receivers
   (both `score_synergy` and ally-stat-buff enabler scoring).

**Units benefitting most from** at the end of each Synergies block is the reverse index:
heroes who list this unit among their top five synergy partners. When
more than ten such heroes exist, only the ten strongest pairings (by
score) are listed, with a short note on why the provider matches widely.

**Parsing pitfalls** (bad summaries → false synergies): resolve targeting from
the **same sentence/clause** as the buff; do not treat self energy or self
stats as ally buffs; enemy debuffs are not benefit stats; situational ally
buffs (monster fights, ingredients, once per battle) should not rank.
**Own-skill state gates** are not partner requires: e.g. Zandrok's extra max HP
while **Rallying Roar** temp buffs are active is self-setup, not
`Temporary ally stat buffs`. **Self-applied named debuffs/DoTs** (Crimson
Venom tick text, Bonnie's Aging) are not generic `Debuff on target` requires.

Regenerate: `python3 scripts/generate-heroes-overview.py`

## Synergies (`heroes-overview.md`)

Generated by `scripts/generate-heroes-overview.py`. Up to five allies per hero, ranked by
combined score. **Units benefitting most from** (end of Synergies) lists heroes who
include this unit in their top five. Display (`render_overview.py` /
`render_site.py`) drops roster-wide **stat-buffer-only** partners
(`obvious_provider_threshold`) but keeps **Enabler** matches (damage type,
DoT, CC, etc.); top picks are then sorted by score for display. When every
pick would be filtered as an obvious buffer, the **common-buffer** names are
promoted into the partner list instead (no duplicate common-buffer row).

1. **Stat buffs** — provider buffs match the hero's **Stats the unit benefits
   from** (magnitude, conditional weighting). Ally-buff **reach** (single vs
   multiple allies, area, etc.) does **not** change synergy score — Units
   improving scores one specific receiver. **Replacements** still use full
   targeting weights for maximum kit strength (see behavior-tags section).
   Omitted when that is the only value: ATK-only buffs, Max HP buff-only,
   Shield-only (unless the hero benefits from shields). Shields extend
   survivability but do not affect Max HP scaling. Rare conditional buffs
   score lower.
   **Haste vs ATK SPD:** Haste also increases attack speed. For heroes that
   benefit from **ATK SPD**, ally **Haste buff** counts toward that need and
   is scored above **ATK SPD buff** at equal magnitude (see
   `HASTE_FOR_ATK_SPD_SCORE_MULT` in `generate-heroes-overview.py`).
   **Healing need:** heroes who **consume or lose their own max HP** during
   skills (e.g. Talene's Ultimate channel) get **Healing** in benefit stats
   and match ally healers and **Lifedrain buff** providers. Ally healers do
   **not** get **Healing** in benefit stats — they provide sustain, they do
   not seek it. **Life Drain** is not a separate benefit stat; treat it as
   sustain for the same HP-cost heroes via the **Healing** matcher.
   **Wide magic for Bonnie:** providers with **Magic**
   damage and battlefield-wide patterns (`center of the battlefield`, `all
   enemies`, etc.) score higher for Bonnie's *Magic damage from allies*
   enabler. **Indirect ally magic:** providers that grant a combat token or
   blessing so **allied hits** apply magic damage, burn, or ignite on enemies
   (e.g. Satrana's Sparks) also match that enabler — often with higher weight
   than self-only magic dealers because physical allies count too.
2. **Enablers** — provider satisfies the hero's **Requires** special effects
   (e.g. magic damage from allies for Bonnie, DoT on enemies for Shadewing,
   Mage/Tank/Support for Himmel's party composition, ally stat buffs for
   Perseus/Silven). Self-setup labels (Debuff on target (Aging), form/stance,
   boss gates, etc.) are skipped; **Debuff on target** is also omitted when
   the hero applies that debuff in their own kit (Bonnie casts Aging at battle
   start — partners need magic damage to stack it, not separate debuffs). Requirements on Ex/Supreme+ tiers get a
   defining-tier multiplier (`DEFINING_TIER_SCORE_MULT`). Synergy text uses
   `Enables {label} via {detail}`. Ally-stat-buff enabler scoring uses the
   same movement / static-tile rules as stat-buff synergy lines.

Matchers and skip lists live in `scripts/generate-heroes-overview.py`.
`main()` prints an enabler pattern scan for skill phrases not yet matched by
synergy enablers.

## Special effects (summary lines)

Notable mechanics outside buff/debuff/CC stat lines. Summary section order:
Stats the unit benefits from → Damage (includes primary damage type) →
Buffs → Debuffs → Crowd Control → Special Effects. Under `#### Special Effects`, use separate `##### Provides`
and `##### Requires` subsections.
Line format (no Provides/Requires prefix on each bullet):

`{label} ({tier}) — {targeting}`

- **Provides** — use descriptive labels (not skill names): e.g. instant defeat,
  invincibility, cheat death (self-survival after defeat or critical HP),
  revive ally (fallen allied hero), summoning (includes named companions),
  marked target (focus fire), ally empower, DoT conversion, dispel,
  fatal-blow save, stat steal,
  ally positioning link, ally blessing, sleep (area), spirit form protection.
  **Ally empower:** when the empowered ally receives conditional immunity
  (e.g. Alna grants the Winter Warrior the same immunity effects), also list
  `Damage and control immunity` in the **Buffs** section (always `high`).
  **Marked target (focus fire):** also list in the **Debuffs** section so
  synergy matching can see which heroes debuff via marking (always `average`).
  **Ally grants:** phrasing like `grants Sparks to allies` or `grants an ally
  Brightfeather` adds `Ally grant (name)`; when allies with that grant can
  inflict DoT or debuffs on enemies in the same skill text, also list
  `Ally DoT on enemies` / `Ally Vitality debuff on enemies` (stored in the
  hero's skill effects sidecar under `special_provides`).
- **Requires** — e.g. continuous damage on enemies, magic damage from allies,
  debuff on target (Aging), form or stance active, ally blessing active,
  passive with internal cooldown, enemy not CC-immune, party composition,
  **Temporary ally stat buffs** (needs temporary stat buffs from allies;
  matched only by providers whose ally stat effects have
  `persistence: temporary`; start-of-battle preferred; see
  `match_ally_stat_buffs` in `generate-heroes-overview.py`). Encode
  persistence on every positive stat buff in sidecars (`temporary`,
  `permanent`, or `unknown`; ally `unknown` fails validation).
  **Continuous damage on enemies** providers are matched **only** from
  structured sidecar data: enemy-targeted `dot` effects, recurring enemy
  HP-loss/max-HP rows with `tick`/`duration`, burn-style debuffs, persistent
  damaging zones, and `Ally DoT on enemies` special provides. Raw skill text
  (`damage … each time`, cooldown wording, channels, periodic attacks) must
  not drive `match_dot_damage()`.

Special provides/requires are extracted into the skill effects sidecar
(`special_provides` / `special_requires` per tier). When merging buffs from
several skill tiers, ally-wide targeting is kept over self-only. Regenerate
`heroes-overview.md` after changing sidecar data.

## Healing

Some units can _heal_ other units and/or provide shields.
Healing effects are extracted into the skill effects sidecar as `heal` /
`dot` with `healing_type`. Do not confuse with the **Healing** stat column.

## Stats the unit benefits from

Listed in each hero summary for synergy matching. Derived from self-buffs
and explicit self-scaling in skill text (`refine_benefit_stats` in
`rewrite-summaries.py`). Omitted as noise: **ATK** from `(ATK-based)` damage
only, companion-only **Max HP**, **Healing** that only
restores a summon, ally-healer kits that output healing (they do not seek
**Healing** partners), standalone **Life Drain** (folded into **Healing**
need for HP-cost heroes only), and one-off **Initial Energy** lines.

## Stats

Hero stats can be buffed (increased) or debuffed (decreased). Grouping follows
[Hero Stats](https://afk-journey.fandom.com/wiki/Hero_Stats) on the Fandom wiki.

### Basic

- **HP** — health pool; a unit is defeated at zero.
- **ATK** — increases damage dealt.
- **Phys DEF** — reduces physical damage received.
- **Magic DEF** — reduces magic damage received.

### Offensive

- **ATK SPD** — +1% normal attack frequency and attack animation speed per point.
- **Crit** — crit *rate* when dealing damage; each point above the target's
  Crit Resist adds 1% crit rate (not crit damage — see Crit DMG Boost).
- **Haste** — +1% normal attack and skill frequency, and attack animation
  speed, per point. Also affects ATK SPD
- **DEF Penetration** — ignores 1% of the target's Phys DEF and Magic DEF per
  point when dealing damage.
- **Execution** — +1% damage vs targets below 50% HP per point.
- **Crit DMG Boost** — crit damage multiplier when dealing crits; default 150%,
  adjusted ±1% per point vs target Crit DMG DEF (range 120%–300%).

### Defensive

- **Vitality** — +1% effectiveness of received shields and healing (including
  self-heals) per point.
- **Life Drain** — restores HP equal to 1% of actual damage dealt per point.
- **Crit Resist** — reduces incoming crit rate; each point above the attacker's
  Crit subtracts 1% from their crit rate.
- **Ranged DEF** — reduces damage from non-adjacent enemies by 1% per point.
- **Crit DMG DEF** — reduces incoming crit damage multiplier; each point above
  the attacker's Crit DMG Boost lowers the multiplier by 1%.

### Other

- **Healing** — +1% effectiveness of shields and healing *provided by* the unit
  per point (distinct from heal/shield skill effects; see **Healing** above).
- **Assistance** — +1% duration of most buffs the unit provides per point.
- **Energy Regen on Hit** — +1% Energy recovered when the unit takes damage per
  point.
- **Debuff Focus** — +1% duration of most debuffs the unit inflicts per point.
- **Resilience** — −1% duration of most debuffs inflicted on the unit per point.
- **Proficiency** — when lower than enemy level, some skill effects are weakened.

### Rivalry-only stats

These appear on rivalry builds and in rivalry-mode tooltips; omit from normal
hero summaries unless skill text names them explicitly.

- **DMG Boost** / **DMG Reduction** — damage dealt/taken multiplier (100%
  base; ±1% per point of difference).
- **Energy Regen Reduction** — reduces Energy recovered by targets when they
  take damage from the unit.

### Not roster stats (skill effects)

Do not list these as hero stat types; detect them as buffs, debuffs, or special
effects instead.

- **Damage taken** — combat modifier, not a character-sheet stat. Store and
  parse as **Damage taken** with `type` buff (reduction) or debuff
  (vulnerability). List view uses separate column ids (`damage_taken_buff`,
  `damage_taken_debuff`) with the same display label.
- **Magic damage** — store and parse as **Magic damage** with `type` buff
  (reduction / mitigation) or debuff (amplification / vulnerability). Same
  display label in summaries; polarity from section or metadata.
- **Max HP** — scaling phrase in skills (`max HP`, `% of max HP`); not a
  separate wiki stat column (use **HP** for the health pool).
- **Dodge chance** — skill-granted avoidance (e.g. Eironn's shield), not a base
  stat.
- **Movement speed** — repositioning / slow effects in skill text, not a base
  stat.

When looking for stat effects in skill text, wording is often indirect. For
example, "reducing their Magic DEF" is a **Magic DEF** debuff; "increasing her
Crit DMG Boost" is an offensive buff; "Crit" alone refers to crit rate.

## Anti Crowd-control

- Unaffected (immune to _all_ control effects, including silence)
- Steadfast (immune to knock down/up/back and displacement)
- Dispell ("removes all their dispellable debuffs"; summaries label **Cleanse**)
- Untargetable (cannot be targeted by spells)
- Immune ("immune to control effects")
- Invincible (immune to damage and cc, untargetable)

Summary lines use `{type} ({tier}) — {targeting} — {timing}` (e.g. Unaffected,
Immune, Steadfast, Cleanse — no extra "immunity" suffix).
Timing labels:

- Start of battle
- Permanent
- Once (e.g. once per battle, first time only)
- Form (while in a named form or mode)
- On ultimate
- On skill
- Conditional

## Ascension

- Epic
- Epic+
- Legendary
- Legendary+ (new skill)
- Mythic
- Mythic+ (new skill)
- Supreme
- Supreme+ (new skill)
- Paragon 1
- Paragon 2
- Paragon 3
- Paragon 4

## Ex-Weapon levels

New exlusive skills are unlocked at the following levels:

- Ex5
- Ex10
- Ex15
- Ex20
- Ex25
- R2 (Paragon 2)
- R4 (Paragon 4)

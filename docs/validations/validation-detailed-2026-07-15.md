# Detailed validation — 2026-07-15

Scope: manual comparison of targeting, geometry, duration, tick interval,
persistence, numeric value/unit, and strongest fully-ascended tier merge for
all existing effect rows. Label existence and type are covered by
[the high-level pass](validation-high-level-2026-07-15.md).

Roster: **119 heroes**, **708 skills**. **159 skills (22.5%)** have at least
one detailed discrepancy, comprising **253 effect-level finding rows**.

Baseline: [validation-detailed-2026-06-16.md](validation-detailed-2026-06-16.md).
Unlike that delta report, this pass re-read every skill.

## Pre-scan results

| Pre-scan | Start | End after fixes |
| --- | ---: | ---: |
| Ally-target self-effect candidates | 3 | 3 |
| Self-target ally-buff candidates | 0 | 0 |
| Self-debuff | 0 | 0 |
| Spurious immunity | 0 | 0 |
| Artifact Silence CC | 0 | 0 |
| True + Max HP double-label | 1 | 0 |
| Heal `value: 0` | 0 | 0 |
| DoT tick 1s with 0.25s/0.5s text | 10 | 0 |
| Knock down `duration: 0` | 0 | 0 |

The three remaining ally-target candidates were manually confirmed valid:
Contess Detention Pass grants its heal and shield to the Exemption ally, and
Smokey & Meerky Special Aroma heals allies.

## Common failure patterns

1. **Placeholder targeting** — `target_count: 3` appears where text says one,
   two, all, or a variable number of units.
2. **Default periodic metadata** — explicit 0.25s, 0.5s, 1.5s, 3s, or ongoing
   effects retain `tick: 1` and/or `duration: 2`.
3. **Self/ally inversion** — ally heals, shields, immunities, and stat buffs
   are stored as Self; reactive self buffs are stored as ally effects.
4. **Single/area collapse** — zones, arcs, paths, walls, and all-unit effects
   remain Single target.
5. **Tier-merge and scalar bleed** — stronger upgrade values are missed, or a
   trigger threshold / neighboring effect scalar replaces the effect value.
6. **Flag effects carry bogus values/persistence** — Invincible and similar
   windows inherit damage percentages or become permanent.
7. **Multi-phase rows collapse** — per-tick damage, ending burst, heal wave,
   and state effects are represented by one row with incompatible metadata.

## Findings

Format: `Character (Skill): found -> expected`.

### Batch 1 — Aliceth–Florabelle

31 heroes, 183 skills; **22 skills**, **43 effect-level findings**.

- Aliceth (Guiding Light): Attack range 500% -> +5 tiles flat.
- Aliceth (Aegis Wings): heal Self -> saved self/Brightfeather ally; blind
  damage 330%/1s/single -> 40% HP/s for 3s on adjacent blinded enemies.
- Aliceth (Sealed Fate): target_count 3 -> 1 farthest marked enemy.
- Alna (Winter Anthem): frost enemy -> all units except Alna; DoT tick 1s ->
  0.5s; direct Self heal 55% -> 10s HoT for Alna and Winter Warrior.
- Alna (Shared Resolve): heal Self -> Alna + Winter Warrior.
- Antandra (Shield Assault): heal 20% -> 20%+5% SP plus 8%+2% SP per hit.
- Arden (Entangling Vines): target_count 3 -> 2.
- Arden (Force of Nature): tick 1s -> 2s.
- Berial (Scared Swamp): tick 1s -> 0.25s.
- Bonnie (Deathmark Arrow): Single target -> all enemies, twice each.
- Contess (Detention Pass): enemy DoT 666% -> ally max-HP loss 2.5%/s; heal
  missing +66% SP.
- Contess (Mandatory Civility): target_count 3 -> 2; ATK debuff duration ->
  6s.
- Contess (Quiet Period): target_count 3 -> 2; Energy debuff duration -> 6s.
- Cryonaia (Icicle Tempest): tick 1s -> 0.5s; split path and adjacent damage.
- Cyran (Gravitic Requiem): tick 1s/value 600% -> 0.25s center/edge rows with
  their per-tick values.
- Daimon (Guardian Howl): Frighten duration -> 2s; max-HP row single/instant ->
  3-tile area, every 0.5s for 2s.
- Damian (Inventor's Will): single/tc3/40/no duration -> 2-tile radius,
  55 Haste, 10s.
- Dunlingr (Grand Resonance): single Haste/no duration -> frontal area ATK SPD
  -60 for 4s.
- Evie (Foretold Favor): direct 60% -> 120%/s HoT on carrier ally.
- Faramor (Sanctified Circle): 250%/1s -> 55% every 0.5s while active.
- Fay (Healing Gemstones): Self 50%/2s -> weakest ally, 65%/s for
  4+1.5 SP seconds.
- Bryon (Tacit Strike): Stun duration missing -> 3s.

### Batch 2 — Frieren–Lucius

30 heroes, 177 skills; **44 skills**, **62 effect-level findings**.

- Frieren (Hellfire: Vollzanbel): tick 1s -> 0.5s; Vitality Single -> Area.
- Granny Dahnie (Threshold of Jade): Single -> radius-2 Area; Bind -> 3s.
- Granny Dahnie (Seed Cannon): Haste duration missing -> 6s.
- Gunnar (Annihilation Directive): range 550% -> +3 tiles; DoT Single -> Area.
- Gunnar (Fire Suppression): Invincible Self/permanent/1400% -> ally,
  conditional window without scalar; ally ATK -> 45%.
- Gunnar (Hero Focus): missing flat Ranged DEF/Vitality tier values.
- Gwyneth (Flare Arrow): tick 1s -> 0.25s.
- Gwyneth (Hailing Arrows): ATK scaling 0.1% -> 0.1 flat per point.
- Gerda (Spring Therapy): HoT Self/Single/2s -> ally Area for field uptime.
- Gerda (Hero Focus): Damage taken value missing -> 20% max tier.
- Harak (Vicious Bite): Knock down duration missing.
- Harak (Flesh Feast): Haste/Crit durations missing -> 12s.
- Harak (Tidal Assault): Invincible permanent/250% -> brief dive window.
- Hewynn (Rain Prayer): HoT Self -> all allies for 9s.
- Hewynn (Healing Wave): 280% -> 300%.
- Hewynn (Tranquility): Damage taken value missing -> 36%; permanent -> while
  Rain Prayer is active.
- Hepler (Extra Credit): HoT Self -> weakest/three weakest allies.
- Hepler (Fur-ious Rescue): Invincible Self -> protected ally for 3s.
- Himmel (Heroic Dash): target_count 3 -> 2.
- Himmel (Heroic Slash): area width unset -> 3 tiles.
- Hodgkin (Phantom Respite): HoT duration 2s -> 8+0.5 SP seconds.
- Hugin (Unstoppable!): ATK/Haste durations missing -> 10s.
- Hugin (Titan's Aegis): Shield duration -> 8s; Energy permanent -> trigger.
- Hugin (Steelbound Kinship): target_count 3 -> 2.
- Igor (Specter Guard): heal 3% generic -> HP-based 3%+0.8% SP per jump.
- Isabella (Hexward): ATK debuff duration -> 5s; Unaffected -> 2.5+0.25 SP s.
- Kafra (Sylvan Banishment): Haste duration missing -> 5s.
- Koko (Fulfilling Feast): heal Self/350% -> ally/260%.
- Koko (Full Energy): Damage taken value missing -> 55%; Lifedrain tc3 -> all
  allies.
- Kordan (Dominance Ring): Life Drain 40 -> 55 flat.
- Kordan (Fury Slash): Shield duration missing -> 15s.
- Kordan (Sundering Strike): Knock down duration missing.
- Kruger (Vital Strike): Damage taken value missing -> 40%.
- Kulu (Boomboom Bash!): Movement speed duration missing -> 3s.
- Laios (Dungeon Gourmet): meal HoT/DEF/Haste Self -> allies in 2-tile Area.
- Lamentis (Malevolent Gaze): Stun All units -> per-apostle targets.
- Lenya (Winning Resolve): Crit DMG Boost 20 -> 65 flat.
- Lorsan (Whispering Tempest): tick 1s -> 0.5s; duration missing -> 5s.
- Lorsan (Zephyr's Embrace): HoT Self -> weakest ally; Unaffected Self ->
  protected ally.
- Lorsan (Turbulent Resurgence): target_count 3 -> 2; heal -> 400%.
- Lucca (Quake Slam): Knock down duration missing.
- Lucius (Divine Light Aegis): Shield duration missing -> 10s.
- Lucius (Divine Light Blessing): heal Self -> weakest ally.
- Lucius (Sacred Beam): ATK debuff 8%/no duration -> 12% for 4s; EX shield
  metadata missing.

### Batch 3 — Lucy–Scarlita

30 heroes, 180 skills; **49 skills**, **83 effect-level findings**.

- Lucy (Celestial Spirit Summon): Stun/Knock up Single -> 1-tile Area.
- Lucy (Star Dress: Aquarius Form): Stun/Knock up Single -> 1-tile Area.
- Lucy (Water Barrier): Shield 450%/no duration -> 550% for 8s.
- Ludovic (Eternal Serenity): single 2s HoT/direct 150% -> field HoT plus
  separate 110% wave heal.
- Ludovic (Ephemeral Berries): 130%/tc3 -> 150%, all allies in range.
- Lumont (Totem Ward): Shield 50 -> 450%+40% SP; DEF target_count 3 -> 2.
- Lumont (Totem Slam): ATK debuff/Physical Single -> 1/2/3-tile Areas.
- Lumont (Enhance Force): HoT duration 2s -> while shielded.
- Lyca (Empyrean Blessing): Energy 25 -> 120; ATK SPD duration -> 8s.
- Marcille (Magical Flash): Blind/Magic Single -> nearby-enemy Area.
- Marcille (Ancient Magic): heal Self -> revived ally.
- Marilee (Mid-Air Shot): target_count 3 -> 2.
- Mehira (Euphoric Rush): Charm Single -> Area blast victims.
- Mehira (Total Devotion): tick 1s/duration 2s -> 1.5s summon cadence.
- Mikola (Dauntless Hymn): tc3/Single -> allies in 2-tile sphere.
- Mirael (Winged Flame): Single -> 3-tile wall Area.
- Nara (Crimson Vengeance): peak branches/cross-skill max-HP/Energy rows ->
  preserve conditional branches and battle-start 750 Energy.
- Nara (Eerie Execution): heal Self/15% -> allies in 2-tile Area at 8%.
- Nara (Killer Kick): collapsed 175% -> kick plus three follow-up hits.
- Natsu (Fiery Ties): Crit DMG Boost 30 -> 5.
- Natsu ("Salamander" Natsu): tick 1s/duration 2s -> 0.5s sustained drain.
- Natsu (Enhance Force): tick 1s -> 0.5s.
- Nazrik (Staggering Strike): healing debuff 300%/3s -> flat 90 for 15s.
- Nerion (Abyssal Embrace): tick 1s/value 600% -> 0.5s/60% per tick.
- Niru (Soul Reaping): HP-loss 0.45 -> 0.4× lost-HP multiplier.
- Niru (Enhance Force): DEF buffs Self/no duration -> ally for 8s.
- Odie (Corrosive Dart): 250%/2s -> 30%/s until defeated.
- Pandora (Panic Projection): tick 1s -> 0.5s; ATK debuff Single -> all units.
- Pandora (Boxed Blessing): Invincible 50% -> no scalar; Energy Self -> ally.
- Parisa (Floral Inspiration): two buff rows target_count 3 -> 2.
- Peggy (Royal Scroll): summon HoT duration 2s -> 8s.
- Peggy (Royal Barrage): target_count 3 -> 2.
- Perseus (Spear-Shield Combo): one 250% row -> separate spear/shield strikes.
- Perseus (Fertile Ground): Max HP 40% trigger value -> 60%+6% SP buff.
- Perseus (Divine Grace): Unaffected ally/tc3 -> Self.
- Phraesto (Vicious Sting): DoT 50 -> max-HP percentage per second for 6s.
- Pippa (Wild Shift): Bind/Displace target_count 3 -> 2.
- Pippa (Enhance Force): Displace/max-HP target_count 3 -> 2.
- Ravion (Designated Duty): ATK/Energy target_count 3 -> 2.
- Ravion (Enhance Force): Unaffected Self -> accepting ally for 5s.
- Reinier (Mutual Reflection): Displace/damage target_count 3 -> 1.
- Reinier (Dynamic Balance): heal 50% -> 45% of damage taken.
- Rowan (Great Bargain): Self Max HP 70% -> ally super-potion heal.
- Saida (Revenant Sprout): heal 4% -> 10%+1% SP.
- Saida (Deepening Roots): tick 1s/duration 2s -> periodic trap over 45s.
- Saida (Enhance Force): Shield target_count 3 -> 2.
- Satrana (Fiery Dance): Invincible 300% -> no scalar; Charm Single -> Area.
- Scarlita (Sanctified Verdict): Invincible 220% -> no scalar; Energy 150 lump
  -> 40/s plus separate late 150.
- Scarlita (Valkyrie Spirit): Supreme+-only/no duration -> base shield for 3s.

### Batch 4 — Seth–Zorya

28 heroes, 168 skills; **44 skills**, **65 effect-level findings**.

- Seth (Predator's Lunge): Phys DEF debuff duration missing -> 6s.
- Shadewing (Razor Talons): DoT duration 2s -> 5s.
- Shadewing (Withering Curse): DEF debuffs Single -> all enemies.
- Shakir (Ravaging Claws): ally Damage taken permanent -> temporary.
- Shakir (Wolf's Will): Lifedrain 30 -> 40+SP.
- Silven (Tempered Field): Ranged DEF 3% -> 48 flat.
- Silvina (Shadow Slayer): Energy debuff 200 -> 300.
- Sinbad (Adaptive Prowess): three debuff target_counts 3 -> 1.
- Sinbad (Tracker's Instincts): Damage taken value missing -> 40%.
- Smokey & Meerky (Special Aroma): HoT 170%/2s -> 31%/s while channeling.
- Solise (Lifebloom Buds): tick 1s -> 3s.
- Solise (Floral Favor): target_count 3 -> 2.
- Sonja (Crimson Covenant): buff target_counts 3 -> 2.
- Sonja (Stunning Reception): Stun/Physical Single -> radius-1 Area.
- Soren (Whirlwind Swing): Stun target_count 3 -> variable collision victims.
- Soren (Repel Sweep): damage/Stun target_count 3 -> 1.
- Soren (Deflecting Swing): Damage taken/Shield ally -> Self.
- Soren (Hero Focus): Haste ally -> Self.
- Soren (Dusk Rejuvenation): Haste 60 -> 80.
- Sylphira (Punishing Rhythm): Energy debuff 120 -> 150.
- Sylphira (Harmonic Refrain): target_count all -> nearest 2.
- Tasi (Shimmering Dust): Damage taken permanent/no duration -> temporary 5s.
- Talene (Enhance Force): HoT duration 2s -> ongoing.
- Temesia (Iron Heel): Damage dealt duration missing -> 5s.
- Temesia (Invincible Fury): HoT duration 2s -> ongoing.
- Thador (Darkmoon Pact): Shield target_count 3 -> 2.
- Thador (Umbral Descent): battlefield effects Single -> all enemies; tick 1s
  -> 0.5s; duration 2s -> 6s; per-tick 560% -> 80%, separate fade burst.
- Thador (Enhance Force): HoT duration 2s -> ongoing.
- Thoran (Hero Focus): Energy 40 flat -> 40% Energy Recovery.
- Thoran (Enhance Force): HP-loss target_count 3 -> variable marked enemies.
- Tilaya (Verdant Growth): Max HP buff 120% -> 40%.
- Ulmus (Way of the Forest): HoT 3.5% -> 5%; Energy value -> 36+4.
- Ulmus (Prowling Roots): Physical 80% -> 120%.
- Valen (Eternal Thunder): Physical 1% placeholder -> normal-attack damage.
- Valka (Spectral Bulwark): ATK SPD target_count 3 -> variable nearby allies.
- Valka (Soulshock Riposte): Energy 250 -> 350; Lifedrain value -> 60.
- Velara (Ruthless Rite): heal 70% -> 80%; target_count 3 -> variable Area.
- Velara (Sinbound Shackles): three debuff durations missing -> 5s.
- Velara (Enhance Force): Unaffected target_count 3 -> all allies.
- Walker (Aerial Thunder): Crit Resist Single -> Arc.
- Zandrok (Rallying Roar): Max HP buff target_count 3 -> variable wedge allies.
- Zorya (Guardian's Ring): HoT duration 2s -> ongoing.
- Zorya (Gargoyle Rampart): Damage taken permanent/no duration -> temporary 10s.
- Zorya (Devouring Strike): Single/area_count 2 -> radius-2 Area.

## Spot-checked confirmations

- Twins Stellar Bond heal/Energy values and linked-ally targeting are merged.
- Atalanta Wild Sniper uses path geometry and a 2s Stun.
- Bonnie Decay's Reach retains 180% DoT at 1s with a 2s max-stack duration.
- Florabelle Overgrowth retains flat Lifedrain 100 and max-tier Haste 66.
- Korin Defiance Charge retains max-tier Shield/True values and ally targeting.
- Indris Arcane Binding retains 5s Bind and radius-2 Knock back.
- Nara Phantom Chains retains per-tile HP loss and single-target Displace.
- Ravion Killer Flush retains lost-HP scaling and card-by-card physical hits.
- Scarlita Divine Quake retains 2s Stun and all-unit Knock back.
- Thoran Resurrection retains 60% heal and 500 Energy at max tier.
- Valka Phantom Slasher retains max-tier 20% Max HP-based damage.
- Vala Night Maneuver retains 120 Haste for 10s.

## Relation to high-level

- Labels are correct but details remain wrong for Alna Winter Anthem, Faramor
  Sanctified Circle, Lorsan Whispering Tempest, Hewynn Rain Prayer, Soren
  Hero Focus, Niru Enhance Force, and Thador Umbral Descent.
- Several high-level findings have no valid row yet and therefore cannot have
  detailed metadata fixed until extraction adds the missing effect.
- Cross-skill tier bleed appears in both passes (Alna, Granny Dahnie, Nara,
  Mehira, Seth), so sidecar corrections must preserve skill ownership before
  adjusting values.

## Fix order

1. Ally/self targeting and fixed-three target-count placeholders.
2. Periodic tick/duration defaults.
3. Heal values and wrong scalar/unit merges.
4. Area/single geometry.
5. Timed persistence and flag-effect scalar cleanup.
6. Complex multi-phase row splitting.

## Fixes applied in this run

- Corrected all ten explicit 0.25s/0.5s periodic rows. Seven sidecars needed
  edits; Alna, Berial, and Natsu were already correct at source.
- Preserved explicit sidecar tick and HoT duration metadata through the
  schema-to-analysis round trip. This closed the processed-output tick scan.
- Corrected 22 confident Self/ally target inversions across 15 sidecars.
  Soren's misplaced shield row remains a label/ownership finding rather than
  receiving a target-only patch.
- Moved Nara's Mythic+ max-HP shockwave from Crimson Vengeance to Eerie
  Execution and corrected the fully ascended value to 15%.
- Added Niru's `temporary-stat-buffer` tag after its DEF buffs were correctly
  recognized as temporary ally buffs.
- Added focused positive and negative regressions for ticks, targeting, skill
  ownership, and processed round-trip preservation.

The findings above remain the start-of-pass baseline. Rows covered by these
fixes are resolved; the other findings remain prioritized follow-up work.

## Verification

- `just views` regenerated processed data, synergies, overview outputs, and
  site data for all 119 heroes.
- `just validate` passes. It still reports six semantic candidates already
  represented in the findings: five anti-CC phrases and Lenya's missing Stun.
- Final pre-scans are zero for self-debuff, spurious immunity,
  artifact-Silence, True + Max HP double-label, heal value zero, explicit
  short-interval tick mismatch, and zero-duration knock down.
- The three ally-target candidates are confirmed legitimate.
- `just test` passes: **342 tests**, with 17 jsonschema deprecation warnings.
- Processed spot checks confirm 0.25s/0.5s ticks, corrected ally/self targets,
  and Nara's Physical + conditional True ultimate versus Max HP-based Eerie
  Execution.

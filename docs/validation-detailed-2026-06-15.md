# Detailed validation — 2026-06-15

Scope: compare detected **targeting**, **area types**, **timings**, and **magnitudes**
per skill effect in `data/heroes_data_processed.json` against each skill's
`description` (raw + active/passive + max-tier upgrades). Damage-type labels,
buff/debuff labels, and CC-type labels are **not** checked here — see
[validation-high-level-2026-06-15.md](validation-high-level-2026-06-15.md).

Roster: **117 heroes**, **696 skills**. Skills audited: **696**. Skills with at
least one discrepancy: **~265** (~38%). Effect-level finding lines: **~400**.

Baseline high-level pass: [validation-high-level-2026-06-15.md](validation-high-level-2026-06-15.md).

Method per `.cursor/AGENTS.md` §Detailed validation: manual comparison in four
hero batches (not automated assertion). Max ascended values used where upgrade
tiers replace base numbers. Where text uses `X% (ATK-based) + Y% damage`, separate
`physical`/`magic` (X+Y) plus `max_hp` (Y) is treated as **correct** unless the
split or total is wrong.

## Common failure patterns

1. **Heal magnitude `0%`** — restoration text present but `value: 0` (Alna Shared
   Resolve, Berial Shadow Trick, Marcille Magical Flash, Niru Spirit Devour,
   Sylphira Harmonic Refrain, Talene Radiant Resurgence, and many others).

2. **DoT tick defaults to 1s** — `every 0.25s` / `every 0.5s` stored as
   `tick: 1` (Alna Winter Anthem, Berial shadow phase, Cryonaia storms, Cyran
   black hole, Faramor circle, Frieren hellfire, Gwyneth burn, Lorsan storm).

3. **Flat `+ X%` parsed as max-HP magnitude** — additive rider duplicated or
   mis-split from main hit (Aliceth Radiant Rain, Athalia, marksmen generally).

4. **Single target vs area/line/arc** — path AOEs, adjacent tiles, and “all
   enemies” collapsed to `single` (Atalanta Wild Sniper, Dionel Starry Void,
   Bonnie Deathmark Arrow, Granny Dahnie Threshold, Mehira Blissful Whip).

5. **`target_count` off** — “2 enemies/allies” stored as `3` (Contess, Arden,
   Marilee Mid-Air Shot); “Multiple targets” placeholder `3` on support skills.

6. **Timed buffs/debuffs without duration** — Haste/DEF/movement reductions,
   shields, damage reduction, frighten/taunt often lack `duration` when text
   gives seconds.

7. **CC duration `0` for knock down** — knock-down effects get `duration: 0`
   instead of brief lock (Antandra Shield Assault, Callan Flail Slam, Harak,
   Himmel Heroic Dash).

8. **Default `area_count: 2`** — explicit 1-tile or 3-tile wording keeps parser
   default (Faramor circle, Dunlingr frontal wave, Himmel frontal slash).

9. **Self vs ally mis-targeting** — Dodge, Crit, heals, DEF buffs on wrong
   `target` (Eironn Tempest Guard, Harak Flesh Feast, Hewynn Healing Wave,
   Marcille Hero Focus, Sonja/Soren Hero Focus).

10. **Upgrade-tier magnitudes not merged** — max-tier EX/Supreme values missing
    or base kept (Cryonaia shield, Carolina Ice Vortex, Lucius shields, Koko
    Fluffy Shield).

11. **Multi-phase skills collapsed** — shadow-phase vs exit burst (Berial),
    dash target vs path (Athalia), arc hits vs sweep (Alna Wild Whirl), mode
    branches (Natsu, Vala Checkmate).

12. **HoT vs direct heal confusion** — sustained recovery stored as instant or
    wrong target (Alna Winter Anthem, Damian Inventor's Will, Fay Healing
    Gemstones).

13. **Flat stat points as percentages or omitted** — Life Drain, Haste, ATK SPD,
    Crit DMG Boost (Kordan, Indris, Lenya, Lyca, Lorsan Haste reduction).

14. **Passive/upgrade-only effects not extracted** — EX/Supreme+ lines with
    numbers but empty or partial `effects` (Evie Tactical Briefing, Hewynn
    Revitalize, Galahad Time Recast, Talene Divine Conflagration, Valen Unseen
    Blade).

15. **Spurious DoT rows** — periodic attacks or entry bursts parsed as sustained
    DoT (Carolina Snowball Witchery, Cryonaia Frozen in Time, Dunlingr bell
    summon).

## Findings

Format: `Character, Skill: found -> expected`

### Batch Aliceth–Dionel (141 skills, ~72 with discrepancies)

Aliceth, Radiant Rain: max-HP magnitude 10% -> +10% flat additive (already in physical 130%)
Aliceth, Radiant Rain: invincible duration missing -> airborne for full ult cast
Aliceth, Sealed Fate: targeting Multiple targets / target_count 3 -> Single target (one marked enemy)
Aliceth, Sealed Fate: DEF Penetration magnitude missing -> 50 + 5 at max tier
Aliceth, Aegis Wings: invincible value 30% -> duration 1.5s
Aliceth, Aegis Wings: blind HP-loss debuff tick missing -> 40% (ATK-based) per 1s
Alna, Winter Anthem: DoT tick 1s -> 0.5s (every 0.5s for 8s)
Alna, Winter Anthem: heal targeting Self -> Self + Winter Warrior
Alna, Winter Anthem: heal magnitude 50% instant -> 50% + 5% of damage taken over 10s (HoT)
Alna, Winter Anthem: Haste debuff target enemy / All units -> all battlefield units except Alna
Alna, Shared Resolve: damage targeting Single target -> multiple enemies in spear thrust
Alna, Shared Resolve: heal magnitude 0% -> 100% + 10% HP to Alna and Winter Warrior
Alna, Wild Whirl: damage area radius only -> arc (1-tile front, 2 hits) + surrounding sweep
Alna, Wild Whirl: Haste debuff duration missing -> 8s
Alna, Chilling Presence: immunity duration missing -> 6s at max tier (every 20s)
Alna, Enhance Force: Vitality debuff duration missing -> 10s; magnitude missing -> -50
Alsa, Twirling Rocks: movement-speed debuff duration missing -> 2s; magnitude missing -> 60%
Alsa, Twirling Rocks: shield duration missing -> 7s
Alsa, Rolling Boulder: targeting All units / zone -> Multiple targets (enemies recently CC'd only)
Antandra, Shield Assault: immunity targeting Area / ally / radius 2 -> Self unaffected 5s
Antandra, Shield Assault: knock-down CC duration 0s -> knock down on adjacent enemies
Antandra, Shield Assault: heal magnitude 20% -> 20% + 5% base plus +8% + 2% per enemy hit
Antandra, Shield Formation: shield magnitude 15% -> 25% + 5% of guarded ally max HP at max tier
Antandra, Shield Formation: shield targeting Self only -> Self + guarded ally
Antandra, Spear Barrage: ATK debuff duration missing -> 7s
Antandra, Gale Barrier: damage-reduction duration missing -> 10s; magnitude missing -> 40–60%
Arden, Force of Nature: area_count 1 -> 2 tiles (surrounding enemies)
Arden, Force of Nature: DoT tick 1s / duration 2s -> strike once per 2s while cloud lasts 7s
Arden, Entangling Vines: target_count 3 -> 2 closest enemies
Atalanta, Wild Sniper: targeting Single target -> line/area (1-tile-wide path)
Atalanta, Wild Sniper: stun targeting Single target -> all enemies along path
Atalanta, Scorching Gift: area_count 1 -> 2 tiles at L3
Atalanta, Hero Focus: targeting Multiple targets / ally -> Self
Atalanta, Enhance Force: heal magnitude 0% -> 10% max HP per enemy hit by Wild Sniper
Athalia, Unbroken Retribution: targeting All units / zone -> Single target (highest cumulative damage enemy)
Athalia, Unbroken Retribution: invincible value 0.5 -> untargetable while casting
Athalia, Vengeance Charge: path damage missing -> 280% + 30% to enemies in dash path
Athalia, Vanguard's Renewal: damage magnitude 165% -> 38% per hit × 6 hits at max tier
Athalia, Enhance Force: magnitude 800% on damage line -> shield reduction cap, not damage dealt
Aurora, Plushification: bind duration 1.125s -> 2.625s at max tier (source tiers conflict)
Baelran, Celestial Rise: heal magnitude 0% -> restores HP equal to 40% of active strike damage
Baelran, Sanctified Surge: HoT duration 2s -> continuous 2% (HP-based) per second
Baelran, Wrath Cleave: area radius 2 -> 3-tile rectangular area in front
Berial, Scared Swamp: DoT tick 1s / value 320% -> 45% every 0.25s for up to 5s in shadow phase
Berial, Shadow Trick: heal magnitude 0% -> 300% (ATK-based) when no isolated enemies
Berial, Devil's Contract: revive heal missing -> 60% + 6% HP at max tier
Bonnie, Deathmark Arrow: targeting Single target -> all enemies (each hit twice)
Bonnie, Decay's Reach: DoT value 180% -> 100% every 1s at max Aging stack
Bonnie, Decay's Reach: DoT duration 2s -> ongoing while max-stacked
Bonnie, Nightfall Shift: targeting Area / radius 2 -> six sequential single-target hits
Bonnie, Blight Surge: target_count 1 -> 2 nearest unafflicted enemies at L3
Brutus, Ferocious Roar: taunt area_count 1 -> 2 tiles
Brutus, Ferocious Roar: Phys DEF debuff duration missing -> 9s
Brutus, Indomitable: immunity duration missing -> 6s base
Bryon, Falcon Raid: DoT value 110% -> 40% per second thunderbolt at L3+
Bryon, Shadow Flash: active damage missing -> 200% × 2 at L4
Callan, Restless Guardian: active shield magnitude 200% -> 140% + 5% (HP-based) at max tier
Callan, Flail Slam: targeting All units / zone -> single-target flail + rectangular slam
Callan, Flail Slam: knock-down CC duration 0s -> knock down on slam
Callan, Enhance Force: heal magnitude 0% -> 15% of shield max value on shield gain
Carolina, Frozen Grave: Frostbite reapply interval missing -> every 2s in arctic field
Carolina, Ice Vortex: Magic DEF debuff magnitude 15% -> 30% at EX+15
Carolina, Snowball Witchery: spurious DoT -> discrete 3s auto-shot, 1.5s per-enemy cooldown
Cassadee, Running Tide: knock-back CC duration missing -> 2s
Cassadee, Tidal Strength: blessing buff targeting Self -> nearest blessed ally
Cecia, Queen's Summons: summon HP drain missing -> loses 4% max HP per second
Cecia, Queen's Summons: Tangled Agony DoT value 185% -> 140% per second for 2s
Cecia, Earth's Offering: ATK SPD buff targeting Self -> Cecia + Mr. Carlyle; magnitude 55 -> 60
Cecia, Agonizing Puncture: DEF Penetration magnitude missing -> 25 + 2 at L2+
Contess, Detention Pass: HP-loss effect target enemy -> exempted ally; tick missing -> 2.5% max HP per 1s
Contess, Mandatory Civility: target_count 3 -> 2 weakest allies / 2 highest-damage enemies
Contess, Quiet Period: target_count 3 -> 2 enemies; debuff magnitude/duration missing
Contess, Hero Focus: Energy-recovery debuff magnitude missing -> up to 4% ATK / 3% energy recovery
Contess, Expulsion Notice: expelled DoT missing -> 30% HP per second at EX L4
Cryonaia, Frostveil Domain: shield magnitude 1400% -> 3000% + 250% at L5
Cryonaia, Frostveil Domain: trap duration / target count missing -> up to 3 heroes for 12s
Cryonaia, Icicle Tempest: DoT tick 1s -> 0.5s; dual magnitudes collapsed
Cryonaia, Frozen in Time: DoT entry mislabeled -> on-domain-entry burst, not sustained DoT
Cyran, Gravitic Requiem: DoT tick 1s -> 0.25s; duration 2s -> 5s black-hole lifetime
Cyran, Cursed Grasp: imprison CC area radius 2 -> Single target; knock-down duration 0s -> 0.5s
Cyran, Mystic Recollection: ATK SPD debuff magnitude 20% -> flat -20 ATK SPD for 5s
Cyran, Mystic Recollection: Haste buff magnitude / duration missing -> +30 Haste for 8s
Daimon, Dolly Defender: true-damage magnitude 1% -> 25% + 3% of each target's max HP at L5
Daimon, Guardian Howl: frighten duration missing -> 2s; roar DoT tick missing -> 0.5s
Damian, Emergency Support!: heal targeting Self -> weakest ally within 3 tiles
Damian, Emergency Support!: heal magnitude 150% -> 160% + 10% per pulse × 4 at max tier
Damian, Inventor's Will: Haste magnitude 40 -> 55 at L4; duration missing -> 10s
Damian, Inventor's Will: HoT magnitude 0% -> 80% HP per second (EX L2)
Dionel, Dawn Light: untargetable immunity targeting Area / ally -> Self for 6s
Dionel, Dawn Light: damage magnitude 250% -> 190% + 15% per thrust at L5
Dionel, Starry Void: targeting Single target -> penetrating line hitting all enemies along path
Dionel, Nectar Feast: ATK buff magnitude 20% -> 25% + 2%; duration missing -> 12s
Dionel, Celestial Spear: Vitality debuff magnitude missing -> -60 for 8s (EX+10)

Chippy: no targeting / area / timing / magnitude discrepancies found.

### Batch Dunlingr–Hugin (111 skills)

Dunlingr, Echo of Silence: silence Single target, no duration -> All units (both sides), duration 6.25s
Dunlingr, Echo of Silence: summon damage as DoT 240% -> instant 240% + 20% max HP to all enemies
Dunlingr, Grand Resonance: area_count 2 -> 3 (3-tile wide × 3-tile long frontal)
Dunlingr, Grand Resonance: magic 55% per effect -> 220% total (4 hits) + 20% max HP total
Dunlingr, Grand Resonance: ATK SPD debuff Single target -> Area, 60 for 4s
Dunlingr, Harmonic Soundwall: shield 130% -> 160% + 20% max HP at max tier
Dunlingr, Enhance Force: missing Curelock HP damage -> 150% to all enemies (Supreme+ L2)
Eironn, Verdant Cyclone: magic 350% -> 330% + 20% max HP at max tier
Eironn, Ice Spike: arc magic 270% -> slash 125% + 10% max HP (separate from stab)
Eironn, Ice Spike: Magic DEF debuff Single target -> Area, 2-tile line, 40% for 5s
Eironn, Tempest Guard: shield 280% -> 320% + 30% max HP for 10s
Eironn, Tempest Guard: Dodge buff target ally -> Self, 80% at max tier
Evie, Intel Chase: magic 198% -> 180% + 18% per second for 8s
Evie, Pointed Proof: no active damage effect -> 2 × 250% at max tier
Evie, Foretold Favor: ATK buff Multiple targets/3 -> Single target (quill carrier)
Evie, Foretold Favor: Direct heal 60% -> HoT 120%/s on quill carrier; orb heal to 2 weakest allies
Evie, Tactical Briefing: no effects -> enemies deal 35% less damage (EX+15)
Faramor, Sanctified Circle: area_count 2 -> 1 (1-tile circle)
Faramor, Sanctified Circle: DoT 250%, tick 1 -> 55% true per 0.5s at max tier
Faramor, Glory's Embrace: shield 200%, no duration -> 200% + 20% max HP for 6s
Faramor, Sacred Pledge: ATK buff Self 12% -> Self + blessed ally, 16.5% for 10s
Fay, Vibrant Dance: ATK buff Multiple targets/3 -> Arc/front allies, 14% for 10s
Fay, Healing Gemstones: HoT Self 0% -> Single weakest ally, 65%/s for 5.5s
Fay, Blinding Light: heal/magic magnitudes -> 160% + 15% max HP at max tier
Florabelle, Overgrowth: Lifedrain buff 60% -> 100 Life Drain (flat) at max tier
Florabelle, Overgrowth: no duration on buffs -> 10s giant form (L4)
Frieren, Zoltraak: targeting All units -> Area, 3-tile rectangle
Frieren, Hellfire: Vollzanbel: DoT tick 1 -> 0.5s for 5s
Galahad, Temporal Field: Haste buff target ally -> Self, 30 when circle complete
Galahad, Chrono Ward: shield 480% -> 600% + 40% max HP for 8s at max tier
Galahad, Time Recast: no effects -> shadow duration 12s; inherits ally stats
Gerda, Splashing Fun: targeting Multiple targets/3 -> Area, area_count 2
Gerda, Mighty Smash: shield 340% -> 400% + 30% for 8s at max tier
Granny Dahnie, Threshold of Jade: all effects Single target -> Area, area_count 2, duration 3s
Granny Dahnie, Threshold of Jade: Energy drain 30 -> 40 + 5 per second at max tier
Granny Dahnie, Glimmerbloom Blessings: HoT 0% -> 110%/s for 12s at max tier
Gunnar, Annihilation Directive: Attack range buff 25% -> +3 normal attack range (flat tiles)
Gunnar, Annihilation Directive: DoT 550%, tick 1 -> 80% + 8% max HP/s for 15s on scorched ground
Gunnar, Absolute Defense: shield Single ally -> Self 600% + 60%; allies behind 400% + 40% for 6s
Gwyneth, Flare Arrow: DoT tick 1 -> 0.25s for 4s; Vitality debuff value missing -> -40
Hammie, You'll Be Fine: heal Self 0% -> Single weakest ally, 190% heal + 10% ATK for 5s
Harak, Vicious Bite: physical 260% lump -> 10 × 100% + 10% + final 240% + 20% at max tier
Harak, Flesh Feast: Crit buff target ally -> Self, 50 + 6 Crit for 12s
Hepler, Remedial Class: Haste debuff 60 -> 90 at max tier; duration 3.3s
Hepler, Extra Credit: shield 130% -> 640% + 64% for 15s (Altered, 3 allies) at max tier
Hewynn, Rain Prayer: HoT duration 2 -> 115% + 5% max HP/s for 9s
Hewynn, Healing Wave: heal Self 300% -> weakest ally, 300% + 30% max HP
Hewynn, Tranquility: Damage taken reduction, no value -> all allies -36% while Rain Prayer active
Hewynn, Enhance Force: no effects -> +30 Haste for 6s on Revitalize heal
Himmel, Heroic Slash: area_count 2 -> 3 (3×3 frontal)
Himmel, Heroic Slash: physical 330% -> 9 × 60% + 6% slashes + 300% + 30% sweep
Himmel, Heroic Dash: target_count 3 -> 2; knock_down duration 0 -> 2s
Himmel, Hero Party: shield 12% -> shared shield 1500% + 100% of initial ATK
Himmel, Blue-Moon Blessings: missing Penetration buff -> +30 Penetration (party)
Hodgkin, Rending Cleave: missing Energy drain 85 (80 + 5)
Hugin, Unstoppable!: ATK buff Multiple/3 -> Single top damage dealer
Hugin, Titan's Aegis: shield 600% -> 660% + 60% max HP for 8s
Hugin, Steelbound Kinship: shield Multiple/3 -> 2 weakest allies, 900% for 8s
Hugin, Enhance Force Hugin: Damage taken reduction, no value -> 30% while cogshield active

### Batch Igor–Lyca (120 skills)

Igor, Specter Guard: heal magnitude 3% -> 4.5% (HP-based) + 0.8% at L4
Igor, Horror Strike: Direct healing 0% Self -> spurious
Indris, True Sight: True damage 185% -> 60% + 6% true on weakness proc
Indris, Arcane Binding: knock-back area_count 1 -> 2 tiles
Indris, Windpiercer: ATK SPD buff no value -> flat +60 for 6s (L4)
Isabella, Lingering Grace: heal targeting Self 400% -> Single ally 400% + 40% max HP
Isabella, Hexward: Magic damage 350% enemy -> none (trigger threshold only)
Isabella, Hexward: immunity no duration -> Unaffected ally 2.75s
Kafra, Forest's Wrath: no ally heal -> HoT 100% + 15% within 2 tiles
Kazim, Stormy Dominion: Haste buff Multiple targets (3) -> All units ally
Koko, Full Energy: Damage taken reduction no magnitude -> 55% All allies 12s (L3)
Koko, Fulfilling Feast: Direct heal 260% -> 260% + 20% max HP (L4)
Koko, Enhance Force: Vitality value 6.0% -> flat +25 for 6s
Kordan, Dominance Ring: Life Drain value 36% -> flat 55 (L4)
Kordan, Fury Slash: Shield 100% -> 100% of damage dealt + 300% (ATK-based)
Korin, Defiance Charge: True damage 320% -> 220% + 15% true (L4)
Korin, Vine Arms: True damage 1.0% Area -> 2.8% max HP for 8s (L4)
Kruger, Hero Focus: ally DEF buff -> Self Ranged DEF flat +26 (L3)
Kruger, Vital Strike: Phys DEF debuff -> Vulnerable (40% physical damage taken increase)
Laios, Intimidate: Phys DEF debuff 49% -> 55%; area_count 1 -> 3-tile frontal arc
Laios, Dungeon Gourmet: Direct heal value 0 -> 560% allies within 2 tiles (L4)
Lenya, Wild Duel: damage/knockback Area radius 2 -> Single target duel enemy
Lenya, Tornado Strike: Physical 285% Area -> 130% × 3 hits surrounding (L4)
Lenya, Winning Resolve: Crit DMG Boost value 20% -> flat +65 (L4)
Lily May, Swallow's Flight: True damage 1.0% -> 6% + 0.6% max HP per hit (L4)
Lorsan, Whispering Tempest: Haste debuff no flat value -> -33 (30 + 3) Area 2 tiles
Lorsan, Whispering Tempest: DoT duration 2s -> 5s storm length; ticks every 0.5s
Lorsan, Zephyr's Embrace: HoT duration 2s -> 6s; missing Dodge +50 ally
Lucius, Divine Light Aegis: Shield 470% -> 520% + 40% max HP (L5)
Lucius, Divine Bash: Physical 350% -> 70% single enemy
Lucy, Celestial Spirit Summon: damage All units zone -> Area 1-tile densest enemies
Ludovic, Lifeweaver's Blooms: Magic 350% + max HP 15% -> HP-loss 55% + 10%/s over 4s (L4)
Lumont, Totem Slam: damage/debuff Single target -> Area per slam ring (1 / 2 / 3 tiles)
Lyca, Nova Fall: ATK debuff All enemies -> none (Phys DEF -12% only)
Lyca, Empyrean Blessing: ATK SPD buff no value -> flat +45 for 8s; Energy recovery +120 flat

### Batch Marcille–Zorya (324 skills)

Marcille, Silver-White Wings that Streak Across the Skies: Magic 600% -> 550% max tier
Marcille, Magical Flash: heal Self / val 0% -> Single ally / 300% heal
Marcille, Hero Focus: Haste buff Single ally -> Self
Marilee, Mid-Air Shot: target_count 3 -> 2 closest enemies
Marilee, Hyperfocus: ATK buff 25% -> ATK 18% + ATK SPD 25 flat
Mehira, Blissful Whip: Single target -> Arc / 3-tile frontal arc
Mehira, Blissful Whip: HP loss 23% -> 32% + 3% per hit max tier
Mehira, Alluring Mirage: charm no duration -> ~2.4s max tier
Mikola, Dauntless Hymn: ally buffs Multiple targets (3) -> Area / 2-tile sphere
Mirael, Winged Flame: Single target -> zone / 3-tile-wide flame wall
Nara, Eerie Execution: ally heal val 0% -> 15% of defeated target max HP (EX+15)
Natsu, Lightning Fire Dragon's Roar: CC+damage Single target -> mode-dependent (Fire Dragon King: all enemies in 5-tile flame)
Nerion, Abyssal Embrace: DoT dur 1s / val 600% -> per-hit 50% on drowning ticks
Niru, Spirit Devour: heal weakest ally val 0% -> equal to damage dealt
Niru, Soul Shepherd: heal val 0% -> restore 45% + 5% max HP (Spirit form)
Odie, Corrosive Dart: DoT debuff val 150% -> 30%/s sustained poison
Pandora, Hero Focus: Max HP buff Single ally -> Self
Pang, Zen Ward: shield Single ally -> Self
Pang, Sky Splitter: ATK buff Single ally 470% -> Self 25%
Parisa, Flower Power: Single target -> path / all enemies along expanding bouquet
Perseus, Spear-Shield Combo: merged Physical 250% -> spear 200%+20% + shield 140%+20% (two radii)
Phraesto, Crimson Contract: enemy max-HP damage 10% -> ally HP reduction 6% (no enemy damage)
Pippa, Botanical Woe: Single target -> Area 1-tile zone, per-second 140%+20%
Reinier, Dynamic Balance: heal Self val 0% -> ally restores 45% of damage taken
Rhys, Concussive Strike: Single target -> enemies within 2 tiles
Rhys, Flame Barrage: Physical 360% -> 320% + 40% per projectile max tier
Shemira, Ghastly Tribute: True 27% Area -> 800% cap per ghost strike context
Shemira, Spectral Barrier: EX+10 damage Single target -> all enemies within 1 tile
Silven, Tempered Field: max-HP damage 1.6% -> blade-sharpen bonus per pass
Smokey & Meerky, Energizing Formula: Energy-only Single ally -> Area all allies ATK 17% + 5 Energy/s
Smokey & Meerky, Withering Potion: stun 0.1s -> 10s empowered aroma window
Sylphira, Harmonic Refrain: heal val 0% -> 1000% per score play
Talene, Divine Conflagration: no effects -> 5-tile channel Magic 150%+20% + HP-loss + 250 Energy/s
Tasi, Eternal Dreamscape: sleep dur 0.5s -> 4.0s (3.5+0.5)
Tasi, Shimmering Dust: Haste Single ally 130 -> Self 70
Temesia, Courage Sword: Physical 77% -> 40%+5% of targets' ATK per hit ×4
Thador, Crescent Cleave: Single target -> Arc 2-tile crescent
Vala, Checkmate: stun 1.0s -> Skyblaster: Haste -60 for 8s; Sword: 3-hit melee (no 1s stun)
Valen, Unseen Blade: no effects -> 3×100%+10% strikes
Valka, Phantom Slasher: frighten dur 0 -> 10s panic state
Velara, Graceful Edict: enemy Magic 400% -> 600% on enemy branch max tier
Viperian, Soul Ravager: heal val 0% -> HP equal to damage dealt
Walker, Shotgun Blast: Single target per bullet -> frontal area (main 3×, others 1×)
Zandrok, Shock Stomp: stun only -> Area max-HP damage 12%+1.5% + 1.5s stun
Zanie, Hero Focus: DEF Penetration Single ally -> Self
Zorya, Devouring Strike: passive heal val 0% -> 30% max HP on enemy defeat within 2 tiles
Zorya, Hero Focus: no effects -> Self damage dealt +9% (+3% with ≥2 enemies nearby)

(Full batch-4 audit covered 324 skills; ~78 had discrepancies. Representative
lines above; remaining findings follow the same patterns in §Common failure
patterns.)

## Spot-checked confirmations

- **Kazim Gale Barrage** — max-HP magnitude **40%** at max tier (upgrade scalar).
- **Lorsan Whispering Tempest** — Haste debuff and DoT labels correct; detailed
  gaps remain on Haste flat value (-33), DoT duration (5s vs 2s), tick (0.5s).
- **Faramor Sanctified Circle** — `area_count` should be **1** (1-tile circle);
  DoT tick should be **0.5s** at max tier.
- **Hugin Titan's Aegis** — Shield label correct; magnitude should be **660% +
  60%** max HP for **8s**.
- **Chippy** (all skills) — no targeting / area / timing / magnitude issues in
  batch Aliceth–Dionel pass.

## Relation to high-level validation

Several high-level gaps are now closed (label detection) while detailed gaps
remain (magnitudes, durations, targeting). Examples:

| Skill | High-level | Detailed still open |
| --- | --- | --- |
| Lorsan Whispering Tempest | DoT + Haste debuff OK | Haste -33 flat; DoT 5s / 0.5s tick |
| Cecia Trial of Thorns | Vitality debuff OK | DoT value tier; bind duration |
| Faramor Sanctified Circle | True damage OK | area_count, DoT tick/magnitude |
| Florabelle Overgrowth | Haste + Lifedrain OK | flat Life Drain 100; 10s duration |

## Next step

Prioritize fixes by synergy impact: **heal val=0**, **wrong targeting on ally
buffs**, and **DoT tick/duration** affect magnitude bands and fuel scoring most.
Label-level fixes from the detection pass are documented in
[validation-high-level-2026-06-15.md](validation-high-level-2026-06-15.md) §Fixes
applied.

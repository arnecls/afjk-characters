# Heroes Overview

Per-hero synergy picks and summaries derived from skill text in
[Heroes.md](Heroes.md). [Heroes.md](Heroes.md) has skills only.
Synergy: stat buff tags under **Units improving X**, and
enabler partners matching **Requires** special effects.
Up to five partners by combined score. Omitted: ATK-only, Max HP
buff-only, and Shield-only (unless the hero benefits from shields).
Rare conditional buffs score lower.
Meta tiers from [Prydwen tier list](https://www.prydwen.gg/afk-journey/tier-list).
Regenerate: `python3 scripts/generate-heroes-overview.py`.

## Aliceth

### Aliceth's behavior

`AFK Stages [B]`, `Dream Realm [B]`, `Dream Realm (Endless) [S+]`, `PVP [S]`

- **Signature skill**: Radiant Rain (ultimate)
- **Movement**: stationary (avg attack range 8.0 tiles)
- **Behavior tags**: `ally-buffer` `cheat-death` `execute` `hp-scaling` `mark-target` `non-ult-utility` `temporary-stat-buffer`
- **Ally composition**: grants Brightfeather to nearest ally in her row
- **Damage types**: Physical `high`, DoT `low`, HP loss `average`

#### Play overview

Aliceth **bonds one ally at battle start**, empowering their strikes so follow-up attacks land after a set number of hits. Her active skill delivers a **heavy strike with knockback and stun** on a focused target when activated. She marks the **farthest enemy**, and she and bonded allies **prioritize that target** until it falls, then her battle ATK climbs for the rest of the fight. Her ultimate fires **arrow volleys** at a single foe, growing heavier when her partner meets feather thresholds. She also blocks the **first fatal blow** on herself or her bonded ally. Against **spread formations**, the mark and focus fire fail to concentrate damage. If the bonded ally dies early, much of her buffing and ultimate scaling is lost entirely.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `low`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

fly up and fire arrow volley at single target

##### Skill 1

Passive: empower an ally with follow-up strike after set hits; Active: heavy strike, knocking back and stunning target

##### Skill 2

mark farthest enemy; caster and bonded allies prioritize that target

##### Legendary+

battle ATK grows after first marked target falls

##### Mythic+

prevent first fatal blow for caster or bonded ally

##### Supreme+

bonded ally feather threshold enhances ultimate with additional arrow volleys

### Units improving Aliceth

Look for units providing: `ATK`  
Common buffers are **Ravion**, **Pandora**, **Contess**, or **Evie**.

- **Ravion**
  - ATK (multiple targets, high)
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Pang**
  - ATK (multiple targets, average)
- **Thador**
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Phraesto**
  - Energy via Energy recovery speed (contract ally, start of battle) `signature fuel`

### Units benefitting most from Aliceth

Aliceth provides Attack range to single targets `high`, DEF Penetration to multiple targets `high`, ATK (Legendary+) to multiple targets `average`, and Fatal blow immunity (Mythic+) to single targets `high` — conditional (rare).

**11** units include this provider among their top 6 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **4** strongest pairings: 

- Nerion (4.6 / 5)
- Carolina (3.7 / 5)
- Kordan (3.4 / 5)
- Lily May (3.0 / 5)

### Units that can act as a replacement for Aliceth

**Similar Skills**

- Scarlita (48% `execute` `hp-scaling` `non-ult-utility`)
- Parisa (45% `ally-buffer` `mark-target` `temporary-stat-buffer`)
- Kordan (40% `ally-buffer` `hp-scaling` `temporary-stat-buffer`)

**Damage**

- Athalia (100% `Physical`)
- Nara (100% `Physical`)
- Faramor (93% `Physical` `DoT` `HP loss`)

**Crowd Control**

- Twins (93% `Blind` `Knock back`)
- Hepler (91% `Blind` `Stun`)
- Damian (91% `Blind` `Stun`)

### Summary for Aliceth

#### Aliceth Provides

- Ally grant (Brightfeather) — Single target
- Instant defeat — Single target
- Invincibility — Self
- Marked target (focus fire) — Multiple targets
- Marked target (focus fire) — Single target
- Fatal blow save (Mythic+) — Single target
- Invincibility (Mythic+) — Single target

#### Damage types dealt by Aliceth

- Physical — Area, Single target
- DoT — Single target — conditional (on blind)
- HP loss — Single target — `average`

#### Buffs provided by Aliceth

- Attack range — Single target — `high`
- DEF Penetration — Multiple targets — `high`
- ATK (Legendary+) — Multiple targets — `average`
- Fatal blow immunity (Mythic+) — Single target — `high` — conditional (rare)

#### Debuffs provided by Aliceth

- Execution — Single target — `low`
- Marked target (focus fire) — Multiple targets — `average`

#### Crowd Control provided by Aliceth

- Unaffected — Self — On ultimate
- Knock back — Single target — `low`
- Stun — Single target — `average`
- Blind (EX+15) — Area — `average`

## Alna

### Alna's behavior

`AFK Stages [S+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S+]`

- **Signature skill**: Shared Resolve (Skill 1)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-buffer` `aoe-damage` `cc-immunity` `invincibility` `temporary-stat-buffer`
- **Ally composition**: place ally in same row at battle prep (Winter Warrior buffs)
- **Damage types**: Physical `high`, DoT `high`

#### Play overview

Before battle, Alna **requires a Winter Warrior in her row**, chosen during prep, who gains extra max HP and shared healing while resisting her opening frost. At fight start she blankets the field in frost, **cutting Haste and attack range** for nearly everyone, then cycles **damage and control immunity** windows that can extend to her partner as well. Her blizzard strips enemy Haste buffs and deals steady damage over time. Damage she or the Winter Warrior takes is then converted into **delayed healing**. Against **targets immune to Haste or range reduction**, much of her control is wasted while allies still suffer the frost penalty. She also needs **sustained fight time** to reapply her ultimate and periodic immunity cycles.

#### Skill overview

- **Signature skill**: speed `average`, first cast speed `fast`, heal `average`, buffs `average`, damage `average`
- **Ultimate**: speed `slow`, heal `average`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `average`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

AoE blizzard reduces enemy haste and deals DoT

##### Skill 1

appoint a companion, granting them buffs

##### Skill 2

multi-hit arc sweep, applying haste reduction

##### Legendary+

battle damage reduction scales over time

##### Mythic+

immunity to damage and control effects

##### Supreme+

shared stat buff; first immunity exit freezes nearby enemies

### Units improving Alna

Look for units providing: `Max HP`  
Common buffers are **Twins**, **Smokey & Meerky**, **Ravion**, or **Lorsan**.

- **Zandrok**
  - Max HP (multiple targets, low)
  - ATK SPD via Haste (area, average, conditional (frequent)) `signature fuel`
- **Hewynn**
  - ATK SPD via Haste (single target, average) `signature fuel`
- **Mehira**
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
- **Shakir**
  - ATK SPD via Haste (area, average) `signature fuel`
- **Damian**
  - ATK SPD via Haste (multiple targets, average, conditional (frequent)) `signature fuel`
- **Isabella**
  - ATK SPD via Haste (single target, low) `signature fuel`

### Units benefitting most from Alna

Alna provides Max HP to single targets `high` and Basic stats (Supreme+) to single targets `low`.

- Zandrok (5.0 / 5)
- Shadewing (4.1 / 5)
- Carolina (3.7 / 5)

### Units that can act as a replacement for Alna

**Buffs on allies**

- Tilaya (79% `Max HP`)

**Similar Skills**

- Dunlingr (61% `ally-buffer` `aoe-damage` `temporary-stat-buffer`)
- Sonja (60% `ally-buffer` `aoe-damage` `temporary-stat-buffer`)
- Perseus (60% `ally-buffer` `aoe-damage` `temporary-stat-buffer`)

**Damage**

- Gwyneth (100% `DoT` `Physical`)
- Thador (100% `DoT` `Physical`)
- Faramor (100% `DoT` `Physical`)

**Debuffs on enemies**

- Lorsan (72% `Haste`)

**Crowd Control**

- Gwyneth (100% `Bind`)
- Evie (100% `Bind`)
- Eironn (100% `Bind`)

### Summary for Alna

#### Alna Provides

- Ally empower — Single target
- DMG+CC immunity (Mythic+) — Self
- DMG+CC immunity (EX+15) — Single target

#### Damage types dealt by Alna

- Physical — Area, Single target
- DoT — All units

#### Buffs provided by Alna

- Max HP — Single target — `high`
- Basic stats (Supreme+) — Single target — `low`

#### Debuffs provided by Alna

- Haste — All units — `low`
- Haste — Area — `average`
- Vitality (Supreme+) — Area — `low`

#### Crowd Control provided by Alna

- Immune (Mythic+) — Self — Start of battle
- Bind (Supreme+) — Area — `average`

## Alsa

### Alsa's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Twirling Rocks (ultimate)
- **Movement**: mostly stationary (avg attack range 6.0 tiles)
- **Behavior tags**: `battlefield-modification` `self-repositioner`
- **Damage types**: Magic `high`

#### Play overview

Alsa enters a **combat stance** that boosts damage and dodge, then fights from that posture for the rest of the fight. Her ultimate curls into a ball, **damaging nearby enemies** and creating terrain obstacles that reshape paths across the field. She punishes **recently controlled foes** with AoE strikes and gains haste as the battle wears on. In stance she slams for extra hits and **evades incoming blows**, rolling away with a shield when pressed. Bonus damage also lands on **multiply-controlled targets**, rewarding teams that chain crowd control together. Terrain obstacles can block enemy movement and funnel foes into follow-up strikes. Against **immune or ungrouped targets**, her control payoff and obstacle value shrink sharply. Her habit of **rolling out of position** also leaves her exposed when enemies focus her down.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `high`

##### Ultimate

enter combat stance with enhanced damage and dodge

##### Skill 1

deal damage to target, creating terrain obstacles on the field

##### Skill 2

AoE damage on enemies recently affected by control

##### Legendary+

battle haste increase

##### Mythic+

enhanced combat capabilities while in combat stance

##### Supreme+

bonus damage against multiply-controlled targets

### Units improving Alsa

Look for units providing: `ATK` `Haste` `Max HP` `Shield`  
Common buffers are **Ravion**, **Smokey & Meerky**, **Twins**, or **Kazim**.

- **Ravion**
  - ATK (multiple targets, high)
  - Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Max HP (single target, low)
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Zandrok**
  - Haste (area, average, conditional (frequent)) `signature fuel`
  - Max HP (multiple targets, low)
  - ATK SPD via Haste (area, average, conditional (frequent)) `signature fuel`
- **Hewynn**
  - Haste (single target, average) `signature fuel`
  - ATK SPD via Haste (single target, average) `signature fuel`
- **Mehira**
  - Haste (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
- **Damian**
  - Haste (multiple targets, average, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste (multiple targets, average, conditional (frequent)) `signature fuel`

### Units benefitting most from Alsa

- Niru (5.0 / 5)
- Bonnie (3.5 / 5)
- Vala (2.1 / 5)

### Units that can act as a replacement for Alsa

**Best overall replacement**

- Galahad (77% `Damage` `Debuffs on enemies`)
- Zorya (64% `Damage` `Debuffs on enemies` `Crowd Control`)
- Natsu (58% `Damage` `Crowd Control`)

**Similar Skills**

- Kulu (100% `battlefield-modification` `self-repositioner`)
- Rhys (48% `self-repositioner`)
- Marilee (40% `self-repositioner`)

**Damage**

- Frieren (100% `Magic`)
- Saida (100% `Magic`)
- Silven (100% `Magic`)

**Debuffs on enemies**

- Galahad (100% `Movement speed`)
- Kulu (100% `Movement speed`)
- Zorya (100% `Movement speed`)

**Crowd Control**

- Aliceth (100% `Stun` `Knock back`)
- Perseus (100% `Stun` `Knock back`)
- Scarlita (100% `Stun` `Knock back`)

### Summary for Alsa

#### Alsa Provides

- Enhanced form — Single target

#### Damage types dealt by Alsa

- Magic — All units, Area, Single target

#### Debuffs provided by Alsa

- Movement speed — Area — `low`

#### Crowd Control provided by Alsa

- Immune — Self — Conditional
- Knock back — Single target — `low`
- Stun — Single target — `average`

## Antandra

### Antandra's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Shield Assault (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-shielder` `aoe-damage` `mass-cc` `taunt`
- **Ally composition**: frontmost ally becomes guarded ally (shared shields)
- **Damage types**: Physical `high`

#### Play overview

Antandra guards one ally with **shields and damage reduction**, then rushes to their side when they are threatened. Her ultimate first **cuts incoming damage**, then stuns surrounding enemies and swings for damage and self-heal that scales with foes hit. Repeated frontal strikes **lower enemy ATK** while her battle max HP grows over time. Landing ultimate hits also **raises her Phys DEF** permanently for the rest of the fight. She works best as a **secondary frontliner** beside another tank who can hold primary aggro and absorb burst. Her shield skill has a **long cooldown**, so mistimed casts leave allies exposed. Without a partner to guard or **dense enemy clusters**, her stun swing and heal scaling underdeliver.

#### Skill overview

- **Signature skill (ult)**: speed `average`, heal `average`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `low`

##### Ultimate

damage reduction, then stun surrounding enemies, striking for damage and self-heal

##### Skill 1

grant shield to selected ally and herself

##### Skill 2

repeated frontal area attacks, reducing targets' ATK

##### Legendary+

battle max HP increase

##### Mythic+

rush to guarded ally, granting them damage reduction

##### Supreme+

hitting with ultimate boosts own Phys DEF

### Units improving Antandra

Look for units providing: `Max HP` `Energy` `Physical DEF`  
Common buffers are **Rowan**, **Pandora**, **Twins**, or **Thador**.

- **Rowan**
  - Energy (area, high) `signature fuel`
  - Phys DEF (single target, average)
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Pandora**
  - Max HP (single target, low)
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Tilaya**
  - Max HP (area, high)
  - DEF (area, high)
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Ravion**
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Lyca**
  - Energy (all units, low) `signature fuel`
  - ATK SPD (all units, low) `signature fuel`
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`

### Units benefitting most from Antandra

Antandra provides Damage taken (Mythic+) to single targets `low` — conditional (frequent).

- Carolina (3.7 / 5)

### Units that can act as a replacement for Antandra

**Best overall replacement**

- Lumont (75% `Crowd Control` `Damage` `Debuffs on enemies`)
- Hepler (61% `Crowd Control` `Damage`)
- Phraesto (60% `Buffs on allies` `Crowd Control`)

**Buffs on allies**

- Hugin (100% `Damage taken`)
- Phraesto (100% `Damage taken`)
- Reinier (100% `Damage taken`)

**Similar Skills**

- Valen (50% `aoe-damage` `mass-cc`)
- Galahad (48% `ally-shielder` `aoe-damage`)
- Brutus (41% `aoe-damage` `taunt`)

**Damage**

- Gwyneth (100% `Physical`)
- Baelran (100% `Physical`)
- Alna (100% `Physical`)

**Debuffs on enemies**

- Bonnie (100% `ATK`)
- Lumont (100% `ATK`)
- Lyca (95% `ATK`)

**Crowd Control**

- Hepler (100% `Stun` `Taunt`)
- Callan (90% `Stun` `Knock down`)
- Lucca (90% `Stun` `Knock down`)

### Summary for Antandra

#### Antandra Provides

- Stacking (Supreme+) — Single target

#### Damage types dealt by Antandra

- Physical — Arc, Area

#### Buffs provided by Antandra

- Damage taken (Mythic+) — Single target — `low` — conditional (frequent)

#### Debuffs provided by Antandra

- ATK — Arc — `average`

#### Crowd Control provided by Antandra

- Unaffected — Self — On skill
- Knock down — Area — `low`
- Stun — Area — `average`
- Taunt — Area — `low`

## Arden

### Arden's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Force of Nature (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `aoe-damage` `dot-specialist` `mass-cc`
- **Damage types**: Magic `average`, DoT `average`

#### Play overview

Arden builds damage around **crowd control on himself or allies**, cycling energy whenever enemies are controlled. His roots bind multiple foes with **continuous damage**, feeding faster skill use in control-heavy teams. His ultimate drops a **persistent lightning zone** that strikes controlled enemies more often than free targets. After casting, he can **bind every target** under the dark cloud at once for a chained lockdown. Strike intervals also **tighten on repeat hits** within the zone, letting damage tick up fast over the full duration. He needs **consistent control sources** from himself or teammates to fuel his rotation and keep the zone active. Against **control-immune or fast-cleansing teams**, his energy loop and lightning ticks never ramp up meaningfully. Pair him with allies who can chain stuns or roots to maximize lightning ticks.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `high`

##### Ultimate

place persistent lightning AoE zone; controlled enemies struck more frequently

##### Skill 1

bind multiple enemies, dealing continuous damage

##### Skill 2

recover energy whenever enemies are controlled

##### Legendary+

battle ATK increase

##### Mythic+

post-ultimate bind all targets under dark cloud simultaneously

##### Supreme+

reduce lightning strike interval for same target within AoE zone

### Units improving Arden

Look for units providing: `ATK` `Energy`  
Common buffers are **Ravion**, **Smokey & Meerky**, **Kazim**, or **Mikola**.

- **Ravion**
  - ATK (multiple targets, high)
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Lyca**
  - Energy (all units, low) `signature fuel`
  - ATK SPD (all units, low) `signature fuel`
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`
- **Aliceth**
  - ATK (multiple targets, average)

### Units benefitting most from Arden

- Carolina (3.7 / 5)
- Nerion (3.2 / 5)
- Bonnie (2.6 / 5)

### Units that can act as a replacement for Arden

**Best overall replacement**

- Gwyneth (59% `Damage` `Similar Skills` `Crowd Control`)
- Frieren (57% `Damage`)
- Faramor (55% `Damage`)

**Similar Skills**

- Viperian (80% `aoe-damage` `dot-specialist`)
- Valen (80% `aoe-damage` `mass-cc`)
- Natsu (72% `aoe-damage` `dot-specialist` `mass-cc`)

**Damage**

- Frieren (100% `DoT` `Magic`)
- Faramor (100% `DoT`)
- Cyran (100% `DoT` `Magic`)

**Crowd Control**

- Eironn (100% `Bind`)
- Evie (85% `Bind`)
- Laios (85% `Bind`)

### Summary for Arden

#### Damage types dealt by Arden

- Magic — Area
- DoT — Multiple targets, Single target

#### Crowd Control provided by Arden

- Bind — Multiple targets — `average`
- Bind (Mythic+) — Area — `average`

## Atalanta

### Atalanta's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Wild Sniper (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `aoe-damage` `battle-start-burst` `self-repositioner`
- **Damage types**: Physical `high`

#### Play overview

Atalanta opens with **rapid chained casts** of her knockback and explosive shots before settling into normal pacing. Her ultimate dashes forward, then fires a **penetrating line shot** that can clip several foes. Hitting different enemies **raises her haste**, rewarding wide target access early. A direct ultimate hit also **heals herself**. Splash from her explosives only carries **partial damage**, so grouped hits feel weaker than the main strike. She struggles when **frontlines block her line** or when burst windows end before she can line up a clean shot.

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

dash forward, then fire a penetrative line shot

##### Skill 1

knock back target, chaining effects to a second enemy behind

##### Skill 2

explosive shot with area splash damage

##### Legendary+

haste grows from hitting multiple different foes

##### Mythic+

skill can be cast multiple times in a row at battle start

##### Supreme+

direct ultimate hit heals self

### Units improving Atalanta

Look for units providing: `ATK` `Haste` `Physical DEF`  
Common buffers are **Ravion**, **Mikola**, **Smokey & Meerky**, or **Kazim**.

- **Ravion**
  - ATK (multiple targets, high)
  - Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Rowan**
  - Phys DEF (single target, average)
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Perseus**
  - ATK (multiple targets, average)
  - Phys DEF (multiple targets, low)
- **Isabella**
  - ATK (single target, low, conditional (frequent))
  - Haste (single target, low) `signature fuel`
  - Phys DEF (single target, low)
  - ATK SPD via Haste (single target, low) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`

### Units benefitting most from Atalanta

- Carolina (3.7 / 5)
- Nerion (3.2 / 5)
- Zorya (2.0 / 5)

### Units that can act as a replacement for Atalanta

**Best overall replacement**

- Perseus (77% `Damage` `Crowd Control`)
- Gwyneth (70% `Damage`)
- Valen (61% `Damage` `Crowd Control`)

**Similar Skills**

- Rhys (80% `aoe-damage` `self-repositioner`)
- Dionel (60% `aoe-damage` `self-repositioner`)
- Himmel (50% `aoe-damage` `self-repositioner`)

**Damage**

- Gwyneth (100% `Physical`)
- Baelran (100% `Physical`)
- Aliceth (100% `Physical`)

**Debuffs on enemies**

- Zanie (100% `Phys DEF` `ATK`)
- Lyca (96% `Phys DEF` `ATK`)
- Ravion (92% `Phys DEF` `ATK`)

**Crowd Control**

- Perseus (97% `Stun` `Knock back`)
- Valen (82% `Stun`)
- Lucca (68% `Stun`)

### Summary for Atalanta

#### Atalanta Provides

- Reposition enemies — Single target
- Start-of-battle cast (Mythic+) — Single target
- Stat steal (EX+10) — Single target

#### Damage types dealt by Atalanta

- Physical — Area, Single target

#### Debuffs provided by Atalanta

- ATK (EX+10) — Single target — `low`
- Phys DEF (EX+10) — Single target — `high`

#### Crowd Control provided by Atalanta

- Unaffected (Supreme+) — Self — On skill
- Bind — Single target — `average`
- Knock back — Single target — `low`
- Stun — Area — `average`

## Athalia

### Athalia's behavior

`AFK Stages [A+]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Unbroken Retribution (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `hp-scaling` `non-ult-utility` `self-repositioner`
- **Damage types**: Physical `high`, True damage `high`

#### Play overview

Athalia **dives behind the highest damage dealer**, slashing foes in her path while healing herself. Her ultimate deals **massive true damage** to whoever has dealt the most cumulative damage. Repeated dashes trigger **extra area slashes** that also **strip enemy shields**. She excels at **bursting isolated carries** but offers little when fights demand sustained pressure.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `high`

##### Ultimate

deal massive true damage to the highest cumulative damage dealer

##### Skill 1

dash behind highest damage dealer, dealing damage to target and enemies in path

##### Skill 2

deal damage to adjacent enemies and self-heal

##### Legendary+

battle crit increase

##### Mythic+

consecutive dashes trigger additional area slashes

##### Supreme+

charge and slashes also reduce enemy shield values

### Units improving Athalia

Look for units providing: `Max HP` `CRIT` `Execution`  
Common buffers are **Pandora**, **Thador**, **Rowan**, or **Ravion**.

- **Pandora**
  - Max HP (single target, low)
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Crit (single target, average)
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Ravion**
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Phraesto**
  - Energy via Energy recovery speed (contract ally, start of battle) `signature fuel`
- **Lyca**
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`

### Units benefitting most from Athalia

- Niru (4.2 / 5)
- Vala (1.9 / 5)
- Carolina (1.5 / 5)

### Units that can act as a replacement for Athalia

**Best overall replacement**

- Baelran (64% `Damage` `Crowd Control`)
- Nara (63% `Damage` `Crowd Control`)
- Faramor (55% `Damage`)

**Similar Skills**

- Marilee (80% `hp-scaling` `self-repositioner`)
- Lily May (50% `hp-scaling` `non-ult-utility` `self-repositioner`)
- Silven (48% `hp-scaling` `non-ult-utility`)

**Damage**

- Faramor (100% `True damage` `Physical`)
- Nara (100% `Physical` `True damage`)
- Baelran (81% `True damage` `Physical`)

**Crowd Control**

- Frieren (100% `Knock down`)
- Himmel (100% `Knock down`)
- Baelran (100% `Knock down`)

### Summary for Athalia

#### Athalia Provides

- Cheat death — Self
- Invincibility — Self
- Transformation — Self

#### Damage types dealt by Athalia

- Physical — Area, Single target
- HP loss — Single target
- True damage — Single target — `high`

#### Crowd Control provided by Athalia

- Unaffected — Self — On ultimate
- Knock down — Single target — `low`

## Aurora

### Aurora's behavior

`AFK Stages [A+]`, `Dream Realm [A+]`, `Dream Realm (Endless) [S+]`, `PVP [B]`

- **Signature skill**: Starlit Slumber (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `invincibility` `mark-target` `summoner`
- **Damage types**: Magic `high`

#### Play overview

Aurora summons a companion that **attacks and detonates for AoE damage**, then falls asleep to become **invincible** while buffing allied summons. Nearby enemies who linger are **transformed into harmless forms**, and her ATK scales with **summon variety** on the field. While asleep, allied summons are **enhanced** and her companion becomes unaffected. She shines beside **summon-heavy teams** but adds little when allies field few bodies or fights end before her sleep cycle.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, buffs `average`, debuffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `high`

##### Ultimate

fall asleep and become invincible, summoning companion to buff allied summons and attack enemies

##### Skill 1

summon companion that attacks enemies, detonating for AoE damage on expiry

##### Skill 2

nearby enemies lingering too long are transformed into harmless form

##### Legendary+

ATK scales with variety of allied summons on field

##### Mythic+

while asleep, allied summons enhanced and companion becomes unaffected

##### Supreme+

high energy during sleep expands transformation field radius

### Units improving Aurora

Look for units providing: `ATK` `Haste`  
Common buffers are **Ravion**, **Kazim**, **Mikola**, or **Smokey & Meerky**.

- **Peggy**
  - ATK (all summons, high)
  - DEF via DEF (all summons, high)
- **Ravion**
  - ATK (multiple targets, high)
  - Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Florabelle**
  - Shield (all summons, average)
- **Aliceth**
  - ATK (multiple targets, average)
- **Pang**
  - ATK (multiple targets, average)

### Units benefitting most from Aurora

Aurora provides Haste to all summons `high`, Damage dealt (Mythic+) to all summons `average`, and Damage taken (Mythic+) to all summons `low`.

**14** units include this provider among their top 6 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **4** strongest pairings: 

- Berial (5.0 / 5)
- Cecia (5.0 / 5)
- Daimon (5.0 / 5)
- Bryon (4.4 / 5)

### Units that can act as a replacement for Aurora

**Similar Skills**

- Zanie (33% `summoner`)
- Florabelle (25% `summoner`)
- Nazrik (25% `mark-target`)

**Damage**

- Saida (100% `Magic`)
- Galahad (100% `Magic`)
- Sylphira (100% `Magic`)

**Debuffs on enemies**

- Alna (100% `Haste`)
- Galahad (100% `Haste`)
- Velara (100% `Haste`)

**Crowd Control**

- Gwyneth (100% `Bind`)
- Saida (100% `Bind`)
- Alna (100% `Bind`)

### Summary for Aurora

#### Aurora Provides

- Dream sleep (transformation) — Self
- Invincibility — Self
- Summoning — Single target

#### Damage types dealt by Aurora

- Magic — Area, Single target

#### Buffs provided by Aurora

- Haste — All summons — `high`
- Damage dealt (Mythic+) — All summons — `average`
- Damage taken (Mythic+) — All summons — `low`

#### Debuffs provided by Aurora

- Haste — Single target — `low`

#### Crowd Control provided by Aurora

- Unaffected (Mythic+) — Self — On skill
- Bind — Area — `low`

## Baelran

### Baelran's behavior

`AFK Stages [S]`, `Dream Realm [A]`, `Dream Realm (Endless) [S]`, `PVP [A+]`

- **Signature skill**: Celestial Rise (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `hp-scaling`
- **Damage types**: Physical `high`, True damage `average`

#### Play overview

Baelran leans on a **massive HP pool** and passive regeneration, then transforms when shields decay or bonus HP triggers. In enhanced form he gains **unaffected status** and his ultimate deals **frontal true damage** with HP restore. Each form shift raises haste over time. His hits also **permanently shave enemy max HP** while transformed. He needs **reliable single-target healing** to cycle forms safely.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, heal `average`, damage `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `high`

##### Ultimate

decaying shield and bonus HP trigger transformation; active frontal true damage and HP restore

##### Skill 1

passive HP regeneration; transformation adds true damage per hit

##### Skill 2

knock up single enemy, then knock down all enemies in frontal area

##### Legendary+

haste grows with each form transition

##### Mythic+

repeat max HP restore enters enhanced form with permanent unaffected and ultimate true damage

##### Supreme+

true damage per hit also reduces enemy max HP permanently

### Units improving Baelran

Look for units providing: `ATK` `Haste` `Shield`  
Common buffers are **Ravion**, **Kazim**, **Mikola**, or **Smokey & Meerky**.

- **Ravion**
  - ATK (multiple targets, high)
  - Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Phraesto**
  - Energy via Energy recovery speed (contract ally, start of battle) `signature fuel`
- **Lyca**
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`

### Units benefitting most from Baelran

- Niru (4.2 / 5)
- Carolina (3.7 / 5)
- Nerion (3.2 / 5)

### Units that can act as a replacement for Baelran

**Best overall replacement**

- Sylphira (51% `Debuffs on enemies` `Crowd Control` `Damage`)

**Similar Skills**

- Zorya (60% `hp-scaling`)
- Shemira (50% `hp-scaling`)
- Athalia (40% `hp-scaling`)

**Damage**

- Faramor (100% `True damage` `Physical`)
- Athalia (100% `True damage` `Physical`)
- Dionel (100% `True damage` `Physical`)

**Debuffs on enemies**

- Sylphira (100% `Max HP`)
- Shemira (100% `Max HP`)

**Crowd Control**

- Sylphira (100% `Knock down`)
- Zorya (75% `Knock down`)
- Callan (52% `Knock down`)

### Summary for Baelran

#### Baelran Provides

- Enhanced form (Mythic+) — Area
- Dispel debuffs (EX+15) — Self

#### Damage types dealt by Baelran

- Physical — Area
- True damage — Arc, Area, Single target — `high`

#### Debuffs provided by Baelran

- Max HP (Supreme+) — Single target — `low`

#### Crowd Control provided by Baelran

- Unaffected — Self — Form
- Knock down — Area — `average`
- Knock up — Single target — `low`

## Berial

### Berial's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Scared Swamp (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `assassin` `cheat-death` `stealth` `summoner`
- **Damage types**: Magic `high`

#### Play overview

Berial hunts **isolated enemies** with no allies within one tile, bouncing in stealth to drain energy and frighten nearby foes. If no one is isolated, he **heals and retreats** instead of pressing the attack. He can **revive from a newly defeated enemy** after his own death, and stealth duration **extends after he falls**. Isolated targets also suffer **penalized damage dealt and taken**, and may spawn decaying decoy summons. He dominates **scattered backlines** but does little when enemies stay **packed together**. Teams that protect rear targets or deny isolated picks waste his assassin kit.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, debuffs `average`, damage `low`

##### Ultimate

enter invincible stealth on target, draining their energy, then leap to damage and frighten adjacent enemies

##### Skill 1

enter stealth; hunt isolated targets or heal and return

##### Skill 2

revive from a newly-defeated enemy after own defeat

##### Legendary+

penalize isolated enemy damage dealt and taken

##### Mythic+

isolated enemies spawn decaying decoy summons

##### Supreme+

extend stealth duration after own defeat

### Units improving Berial

- **Aurora**
  - Haste (all summons, high)
  - Damage dealt via Damage dealt (all summons, average)
  - Damage taken via Damage taken (all summons, low)
- **Peggy**
  - ATK (all summons, high)
  - DEF via DEF (all summons, high)
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Ravion**
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Florabelle**
  - Shield (all summons, average)

### Units benefitting most from Berial

- Carolina (3.7 / 5)
- Nerion (3.2 / 5)
- Bonnie (2.6 / 5)

### Units that can act as a replacement for Berial

**Best overall replacement**

- Cryonaia (55% `Damage`)
- Saida (54% `Debuffs on enemies`)
- Dunlingr (50% `Damage` `Debuffs on enemies`)

**Similar Skills**

- Bryon (40% `cheat-death` `summoner`)
- Zanie (25% `summoner`)
- Florabelle (24% `summoner`)

**Damage**

- Frieren (100% `DoT` `Magic`)
- Cyran (100% `DoT` `Magic`)
- Cryonaia (100% `DoT` `Magic`)

**Debuffs on enemies**

- Saida (100% `Energy` `Damage dealt`)
- Pippa (100% `Energy`)
- Silvina (100% `Energy`)

**Crowd Control**

- Silvina (100% `Frighten`)

### Summary for Berial

#### Berial Provides

- Cheat death — Self
- Invincibility — Self
- Summoning (Mythic+) — Single target

#### Damage types dealt by Berial

- Magic — Area, Single target

#### Debuffs provided by Berial

- Energy — Single target — `high`
- Damage dealt (Legendary+) — Single target — `low`
- Damage taken (Legendary+) — Single target — `low`

#### Crowd Control provided by Berial

- Frighten — Area — `average`

## Bonnie

### Bonnie's behavior

`AFK Stages [A]`, `Dream Realm [A]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Decay's Reach (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `aoe-damage` `battle-start-burst` `enemy-debuffer` `non-ult-utility`
- **Damage types**: Magic `average`

#### Play overview

Bonnie opens by placing an **Aging debuff** on the rearmost enemy, slowing haste and stacking when allies deal magic damage to that target. Her ultimate hits AoE for **bonus damage and stun** against debuffed targets. She can **turn to mist and reposition** when threatened, and the debuff **spreads on max stack or death**. Max-stack victims also take **increased magic damage**, making magic dealers ideal partners. Battle ATK growth adds steady personal damage over time. She deals **less raw damage** than top burst dealers but excels when debuffs can spread across multiple targets. Against **immune or cleanse-heavy lines**, her debuff chain and ultimate payoff never build.

#### Skill overview

- **Signature skill**: speed `fast`, debuffs `average`, damage `low`
- **Ultimate**: speed `fast`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

AoE damage; bonus damage and stun against debuffed targets

##### Skill 1

apply haste-reducing debuff to rearmost enemy; ally magic damage further stacks the debuff

##### Skill 2

transform into mist and reposition to safety

##### Legendary+

battle ATK increase

##### Mythic+

debuff spreads to new targets on max stack or debuffed unit death

##### Supreme+

max-stack debuffed targets suffer increased magic damage

### Units improving Bonnie

Look for units providing: `ATK`  
Common buffers are **Parisa**, **Dunlingr**, **Twins**, or **Contess**.

Bonnie also requires units **dealing magic damage**

- **Solise**
  - ATK (single target, low)
  - Enables Magic damage from allies via Magic damage + wide area + all enemies (All units)
- **Galahad**
  - Enables Magic damage from allies via Magic damage + wide area + all enemies (All units)
- **Lamentis**
  - Enables Magic damage from allies via Magic damage + wide area + all enemies (All units)
- **Lucy**
  - Enables Magic damage from allies via Magic damage + wide area + all enemies (All units)
- **Marcille**
  - Enables Magic damage from allies via Magic damage + wide area + all enemies (All units)
- **Niru**
  - Enables Magic damage from allies via Magic damage + early battle + all enemies (All units)

### Units benefitting most from Bonnie

- Niru (4.2 / 5)
- Carolina (2.0 / 5)
- Nerion (1.8 / 5)

### Units that can act as a replacement for Bonnie

**Best overall replacement**

- Nerion (51% `Damage` `Crowd Control`)

**Similar Skills**

- Nerion (57% `battle-start-burst` `enemy-debuffer`)
- Cassadee (48% `aoe-damage` `enemy-debuffer`)
- Kazim (36% `aoe-damage` `battle-start-burst` `non-ult-utility`)

**Damage**

- Frieren (100% `Magic`)
- Saida (100% `Magic`)
- Silven (100% `Magic`)

**Debuffs on enemies**

- Lorsan (56% `Haste`)

**Crowd Control**

- Phraesto (100% `Stun`)
- Callan (100% `Stun`)
- Ludovic (100% `Stun`)

### Summary for Bonnie

#### Bonnie Provides

- Invincibility — Self
- Transformation — Self

#### Damage types dealt by Bonnie

- Magic — Area, Single target
- DoT — Single target

#### Debuffs provided by Bonnie

- ATK — Single target — `high`
- Haste — Single target — `low`
- Magic damage (Supreme+) — Single target — `low`

#### Crowd Control provided by Bonnie

- Stun — Single target — `average`

## Brutus

### Brutus's behavior

`AFK Stages [A]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Indomitable (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `aoe-damage` `cheat-death` `invincibility` `life-drain` `taunt`
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Play overview

Brutus taunts nearby enemies while **shredding their Phys DEF**, then spins for sustained damage to adjacent foes. He **survives the first fatal blow** and gains temporary immunity, with extended immunity when triggered. Life drain rises during his spin, and taking **adjacent physical hits** feeds more drain after his frontal cleave. His ultimate spin also grants **brief invincibility** while active. His kit is built to **stall and soften frontlines** while he absorbs pressure. He adds little when enemies **ignore taunt** or burst him before Indomitable triggers. Without **melee traffic** around him, his spin and drain scaling stay flat.

#### Skill overview

- **Signature skill**: speed `fast`, buffs `average`
- **Ultimate**: speed `slow`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

spin, dealing sustained damage to adjacent enemies

##### Skill 1

taunt nearby enemies, reducing their Phys DEF

##### Skill 2

survive first fatal blow then gain temporary immunity

##### Legendary+

battle life drain elevated during spin

##### Mythic+

cleave enemies in front; gain life drain after taking physical hits from adjacent enemies

##### Supreme+

extend immunity duration

### Units improving Brutus

_No synergy partners matched stat buffs or enablers._

### Units benefitting most from Brutus

- Niru (4.2 / 5)
- Vala (1.9 / 5)
- Indris (1.3 / 5)

### Units that can act as a replacement for Brutus

**Best overall replacement**

- Lumont (54% `Crowd Control`)
- Hepler (51% `Crowd Control`)

**Similar Skills**

- Igor (42% `aoe-damage` `cheat-death` `life-drain`)
- Antandra (41% `aoe-damage` `taunt`)
- Thoran (40% `cheat-death` `life-drain`)

**Damage**

- Gunnar (100% `Physical` `DoT`)
- Himmel (100% `Physical`)
- Valka (100% `Physical`)

**Debuffs on enemies**

- Laios (100% `Phys DEF`)
- Kafra (87% `Phys DEF`)
- Atalanta (65% `Phys DEF`)

**Crowd Control**

- Phraesto (100% `Taunt`)
- Hepler (100% `Taunt`)
- Lumont (100% `Taunt`)

### Summary for Brutus

#### Damage types dealt by Brutus

- Physical — Arc, Area
- Max HP-based damage — Arc — `high`

#### Debuffs provided by Brutus

- Phys DEF — Area — `average`

#### Crowd Control provided by Brutus

- Immune — Self — On skill
- Unaffected — Self — On skill
- Taunt — Area — `average`

## Bryon

### Bryon's behavior

`AFK Stages [A+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Shadow Flash (Skill 2)
- **Movement**: stationary (summon moves)
- **Behavior tags**: `battle-start-ult` `cheat-death` `high-initial-energy` `summoner`
- **Damage types**: Magic `high`, DoT `average`

#### Play overview

Bryon opens with a **battle-start companion summon** that fights beside him and gains haste while she remains on the field. His projectiles **drain enemy energy** on hit, and his companion **counterattacks and stuns** when he is controlled or struck hard, also blocking fatal blows. Casting his projectile skill also **spawns leaves near the companion** for extra pressure. He deals strong **multi-target magic damage** when enemies are grouped. He underperforms when the companion **dies early** or when foes are **spread beyond projectile reach**.

#### Skill overview

- **Signature skill**: speed `slow`, debuffs `average`
- **Ultimate**: speed `fast`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, debuffs `average`, damage `average`

##### Ultimate

summon companion to deal damage and assist in battle

##### Skill 1

launch multiple magic projectiles at target

##### Skill 2

Passive: drain enemy energy on each hit; Active: two-hit strike

##### Legendary+

haste scales while companion is on battlefield

##### Mythic+

companion counterattacks and stuns when owner is controlled or struck hard, also blocking fatal blows

##### Supreme+

casting projectile skill also spawns leaves near companion

### Units improving Bryon

Look for units providing: `Haste` `Energy`  
Common buffers are **Hugin**, **Smokey & Meerky**, **Lorsan**, or **Ravion**.

- **Peggy**
  - ATK (all summons, high)
  - DEF via DEF (all summons, high)
  - Ranged damage via Ranged damage (all summons, low)
- **Aurora**
  - Haste (all summons, high)
  - Damage dealt via Damage dealt (all summons, average)
  - Damage taken via Damage taken (all summons, low)
- **Hewynn**
  - Haste (single target, average) `signature fuel`
  - ATK SPD via Haste (single target, average) `signature fuel`
- **Mehira**
  - Haste (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
- **Damian**
  - Haste (multiple targets, average, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste (multiple targets, average, conditional (frequent)) `signature fuel`
- **Zandrok**
  - Haste (area, average, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste (area, average, conditional (frequent)) `signature fuel`

### Units benefitting most from Bryon

- Shadewing (3.4 / 5)
- Indris (2.4 / 5)
- Bonnie (1.6 / 5)

### Units that can act as a replacement for Bryon

**Best overall replacement**

- Natsu (69% `Damage` `Crowd Control` `Debuffs on enemies`)
- Galahad (52% `Damage` `Debuffs on enemies`)
- Lucy (51% `Damage` `Crowd Control`)

**Similar Skills**

- Saida (40% `cheat-death` `high-initial-energy`)
- Berial (40% `cheat-death` `summoner`)
- Lucy (33% `high-initial-energy` `summoner`)

**Damage**

- Cyran (100% `Magic` `DoT`)
- Cryonaia (100% `Magic` `DoT`)
- Frieren (97% `Magic` `DoT`)

**Debuffs on enemies**

- Dunlingr (100% `Haste` `Energy`)
- Pandora (100% `Haste` `Energy`)
- Vala (100% `Haste` `Energy`)

**Crowd Control**

- Contess (100% `Stun`)
- Gwyneth (100% `Stun`)
- Aliceth (100% `Stun`)

### Summary for Bryon

#### Bryon Provides

- Summoning — Single target
- Cheat death (EX+5) — Self
- Counterattack (EX+10) — Single target

#### Damage types dealt by Bryon

- Magic — Single target
- DoT — Area

#### Debuffs provided by Bryon

- Energy — Single target — `low`
- Haste — Area — `low`

#### Crowd Control provided by Bryon

- Stun (Mythic+) — Single target — `low`

## Callan

### Callan's behavior

`AFK Stages [A+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Restless Guardian (ultimate)
- **Movement**: moving (inactive while ultimate is running)
- **Behavior tags**: `ally-shielder` `cc-immunity`
- **Damage types**: Magic `average`

#### Play overview

Callan grants **shields at battle start and on ultimate cast**, absorbing damage meant for nearby allies at the opening of fights. His multi-hit skill **knocks down** the target and nearby enemies, while absorbed damage is **stored for a burst release** on his second skill. Once per battle, low HP triggers an **AoE burst and stun** on nearby foes. He also heals whenever he gains any shield, and battle vitality **grows over time** to keep him standing through long engagements. He is a **strong opening protector** but offers weak retaliation compared to dedicated counter tanks. His stored burst also **underwhelms against heavily armored targets** that shrug off the release. He provides no offensive buffs for allies once shields fall. Fights that **bypass or strip shields** leave him with little damage and no team buffs to contribute once his protection windows end.

#### Skill overview

- **Signature skill (ult)**: speed `fast`
- **Non-ultimate**: speed `fast`, damage `average`

##### Ultimate

grant a shield at battle start and on cast, absorbing damage for allies

##### Skill 1

multi-hit on target, knocking target and nearby enemies down

##### Skill 2

convert absorbed damage to stored burst release

##### Legendary+

battle vitality increase

##### Mythic+

once per battle, low HP triggers AoE burst damage and stun on nearby enemies

##### Supreme+

heal when gaining any shield

### Units improving Callan

Look for units providing: `Shield`  
Common buffers are **Thador**, **Pandora**, **Contess**, or **Rowan**.

- **Thador**
  - Shield (multiple targets, high)
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Pandora**
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Saida**
  - Shield (multiple targets, high)
- **Rowan**
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Ravion**
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Phraesto**
  - Energy via Energy recovery speed (contract ally, start of battle) `signature fuel`

### Units benefitting most from Callan

- Niru (5.0 / 5)
- Carolina (4.3 / 5)
- Nerion (3.8 / 5)
- Bonnie (3.5 / 5)

### Units that can act as a replacement for Callan

**Best overall replacement**

- Zorya (52% `Crowd Control` `Damage`)

**Similar Skills**

- Korin (33% `ally-shielder`)
- Hepler (30% `ally-shielder`)
- Lucca (30% `ally-shielder`)

**Damage**

- Frieren (100% `Magic`)
- Saida (100% `Magic`)
- Silven (100% `Magic`)

**Crowd Control**

- Zorya (100% `Stun` `Knock down`)
- Antandra (96% `Stun` `Knock down`)
- Lucca (96% `Stun` `Knock down`)

### Summary for Callan

#### Callan Provides

- Damage absorption (allies) — Area
- Damage absorption (allies) — Multiple targets
- Stored damage release — Self
- Stored damage release — Area
- Stored damage release — Single target

#### Damage types dealt by Callan

- Magic — All units

#### Crowd Control provided by Callan

- Unaffected — Self — Start of battle
- Knock down — All units — `low`
- Stun (Mythic+) — All units — `average`
- Stun (EX+10) — Single target — `average`

## Carolina

### Carolina's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Frozen Grave (ultimate)
- **Movement**: mostly stationary (avg attack range 4.0 tiles)
- **Behavior tags**: `dot-specialist` `enemy-debuffer`
- **Damage types**: Magic `average`

#### Play overview

Carolina stacks **DoT on area hits**, then freezes a target and lays an **arctic field** that keeps burning foes inside. Orbiting projectiles **auto-attack controlled enemies**, and repeated casts widen projectile AoE while **shaving Magic DEF**. Stacking projectiles also **apply DoT on impact**, and her crit grows with cast count over long fights. She peaks when **allies supply steady control** and magic damage can exploit lowered defenses. Her freeze and field reward extended engagements where stacks can compound. Against **control-immune targets**, her orbiting damage and freeze setup never activate. Short fights that end **before DoT and cast stacks** build also waste her kit entirely.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, debuffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, debuffs `average`, damage `average`

##### Ultimate

deal damage and freeze target, creating an arctic field that inflicts DoT

##### Skill 1

area damage applies DoT stacks to targets

##### Skill 2

orbiting projectiles automatically attack controlled enemies

##### Legendary+

crit scales with repeated use count

##### Mythic+

repeated casts stack projectile AoE damage and reduce Magic DEF

##### Supreme+

stacking projectiles also apply DoT on impact

### Units improving Carolina

Look for units providing: `CRIT`  
Common buffers are **Lorsan**, **Twins**, **Pandora**, or **Smokey & Meerky**.

Carolina also requires units **applying crowd control** to enemies

- **Hepler**
  - Enables CC on enemies via Blind (area, high)
- **Lorsan**
  - ATK SPD via Haste (single target, high) `signature fuel`
  - Enables CC on enemies via Stun (multiple targets, high)
- **Callan**
  - Enables CC on enemies via Stun (all units, average)
- **Tasi**
  - Enables CC on enemies via Sleep (all units, average)
- **Twins**
  - Energy (multiple targets, low) `signature fuel`
  - ATK SPD via Haste (all units, average) `signature fuel`
  - Enables CC on enemies via Blind (area, average)
- **Damian**
  - ATK SPD via Haste (multiple targets, average, conditional (frequent)) `signature fuel`
  - Enables CC on enemies via Blind (area, average)

### Units benefitting most from Carolina

- Bonnie (3.4 / 5)
- Indris (2.4 / 5)
- Nerion (2.3 / 5)

### Units that can act as a replacement for Carolina

**Best overall replacement**

- Shadewing (55% `Similar Skills`)
- Nerion (53% `Similar Skills` `Damage`)
- Eironn (51% `Damage` `Debuffs on enemies` `Crowd Control`)

**Similar Skills**

- Shadewing (100% `dot-specialist` `enemy-debuffer`)
- Nerion (96% `dot-specialist` `enemy-debuffer`)
- Mirael (50% `dot-specialist`)

**Damage**

- Frieren (100% `Magic`)
- Saida (100% `Magic`)
- Silven (100% `Magic`)

**Debuffs on enemies**

- Eironn (100% `Haste` `Magic DEF`)
- Bonnie (100% `Haste`)
- Zorya (100% `Haste`)

**Crowd Control**

- Evie (100% `Bind`)
- Eironn (100% `Bind`)
- Arden (100% `Bind`)

### Summary for Carolina

#### Carolina Provides

- Stacking — Area

#### Damage types dealt by Carolina

- Magic — Area, Single target

#### Debuffs provided by Carolina

- Haste — Area — `low`
- Magic DEF (Mythic+) — Area — `low`
- Haste (Supreme+) — Single target — `low`

#### Crowd Control provided by Carolina

- Bind — Single target — `high`

## Cassadee

### Cassadee's behavior

`AFK Stages [C]`, `Dream Realm [A]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Tidal Strength (Skill 2)
- **Movement**: stationary (avg attack range 10.0 tiles)
- **Behavior tags**: `ally-buffer` `aoe-damage` `enemy-debuffer`
- **Ally composition**: nearest ally auto-selected at battle start; prioritizes ally behind
- **Damage types**: Magic `high`

#### Play overview

Cassadee blesses one ally so their attacks **deal bonus magic damage** to struck enemies, keeping haste high while that ally lives. Her heavy single-target strike adds direct pressure, and her ultimate **knocks back foes in a line** while temporarily blessing allies it touches. The ultimate path also **lowers enemy Magic DEF** for a window after impact. She blends **damage, soft control, and ally amplification** in one slot. She falters when the **blessed ally dies early** or when enemies **dodge the line attack**. Without a **partner who attacks often**, her blessing contributes little sustained value over the fight. Her haste growth rewards keeping the blessed ally alive through sustained exchanges.

#### Skill overview

- **Signature skill**: speed `average`, first cast speed `fast`, damage `low`
- **Ultimate**: speed `slow`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, damage `average`

##### Ultimate

knock back and damage enemies in a straight line

##### Skill 1

deal heavy single-target damage

##### Skill 2

bless one ally, dealing bonus damage to enemies hit by their normal attacks

##### Legendary+

haste grows while first blessed ally remains alive

##### Mythic+

ultimate path blesses all hit allies temporarily

##### Supreme+

ultimate reduces enemies' Magic DEF for a while

### Units improving Cassadee

Look for units providing: `Haste`  
Common buffers are **Hugin**, **Smokey & Meerky**, **Lorsan**, or **Ravion**.

- **Hewynn**
  - Haste (single target, average) `signature fuel`
  - ATK SPD via Haste (single target, average) `signature fuel`
- **Mehira**
  - Haste (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
- **Damian**
  - Haste (multiple targets, average, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste (multiple targets, average, conditional (frequent)) `signature fuel`
- **Zandrok**
  - Haste (area, average, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste (area, average, conditional (frequent)) `signature fuel`
- **Isabella**
  - Haste (single target, low) `signature fuel`
  - ATK SPD via Haste (single target, low) `signature fuel`
- **Gunnar**
  - ATK SPD (single target, low) `signature fuel`

### Units benefitting most from Cassadee

- Kazim (2.8 / 5)

### Units that can act as a replacement for Cassadee

**Similar Skills**

- Sonja (60% `ally-buffer` `aoe-damage`)
- Perseus (60% `ally-buffer` `aoe-damage`)
- Hodgkin (60% `aoe-damage` `enemy-debuffer`)

**Damage**

- Frieren (100% `Magic`)
- Saida (100% `Magic`)
- Silven (100% `Magic`)

**Debuffs on enemies**

- Thador (100% `Magic DEF`)
- Evie (100% `Magic DEF`)
- Eironn (100% `Magic DEF`)

**Crowd Control**

- Scarlita (94% `Knock back` `Knock up` `Stun`)
- Lumont (60% `Knock back` `Stun` `Knock up`)
- Perseus (60% `Knock back` `Stun`)

### Summary for Cassadee

#### Cassadee Provides

- Ally blessing — Single target
- Ally blessing — All units

#### Damage types dealt by Cassadee

- Magic — Area, Single target

#### Debuffs provided by Cassadee

- Magic DEF (Supreme+) — Area — `low`

#### Crowd Control provided by Cassadee

- Knock back — Area — `average`
- Knock up — Single target — `low`
- Stun — Single target — `low`
- Knock up (EX+10) — Multiple targets — `low`
- Stun (EX+10) — Multiple targets — `low`

## Cecia

### Cecia's behavior

`AFK Stages [B]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Queen's Summons (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Behavior tags**: `enemy-debuffer` `mass-cc` `summoner`
- **Damage types**: Physical `high`, DoT `average`

#### Play overview

Cecia fights alongside a **permanent companion**, raising both their attack speeds and landing periodic **enhanced heavy strikes**. She binds an enemy to **drain their stats**, and attack speed scales while the companion stays on the field. Her ultimate **re-summons the companion** for another burst of pressure. She is a **solid carry** with bind and steady DPS but struggles against **tanky single targets** that resist bind.

#### Skill overview

- **Signature skill (ult)**: speed `average`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

summon companion to assist in battle

##### Skill 1

increase own and companion ATK speed

##### Skill 2

periodic enhanced normal attack dealing heavy damage

##### Legendary+

ATK speed scales with companion presence on battlefield

##### Mythic+

bind an enemy and drain their stats

##### Supreme+

reduce normal attacks needed to trigger enhanced attack

### Units improving Cecia

Look for units providing: `ATK SPD / Haste` `DEF Penetration` `Physical DEF` `Magic DEF`  
Common buffers are **Rowan**, **Mikola**, **Ravion**, or **Pandora**.

- **Aurora**
  - Haste (all summons, high)
  - Damage dealt via Damage dealt (all summons, average)
  - Damage taken via Damage taken (all summons, low)
- **Peggy**
  - ATK (all summons, high)
  - DEF via DEF (all summons, high)
- **Rowan**
  - Phys DEF (single target, average)
  - Magic DEF (single target, average)
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Niru**
  - Phys DEF (single target, high)
  - Magic DEF (single target, high)
- **Tilaya**
  - DEF (area, high)
  - DEF (area, high)
- **Ravion**
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`

### Units benefitting most from Cecia

- Carolina (3.7 / 5)
- Shadewing (3.4 / 5)
- Nerion (3.2 / 5)

### Units that can act as a replacement for Cecia

**Best overall replacement**

- Gwyneth (82% `Damage` `Crowd Control` `Debuffs on enemies`)
- Alna (58% `Damage` `Crowd Control`)
- Faramor (52% `Damage`)

**Similar Skills**

- Hodgkin (60% `enemy-debuffer` `summoner`)
- Pandora (50% `enemy-debuffer` `mass-cc`)
- Lucy (40% `mass-cc` `summoner`)

**Damage**

- Gwyneth (100% `Physical` `DoT`)
- Alna (100% `Physical` `DoT`)
- Faramor (100% `Physical` `DoT`)

**Debuffs on enemies**

- Isabella (100% `Magic DEF` `Phys DEF` `Vitality`)
- Sinbad (100% `Magic DEF` `Phys DEF` `Vitality`)
- Gwyneth (80% `Phys DEF` `Vitality`)

**Crowd Control**

- Gwyneth (100% `Bind`)
- Alna (100% `Bind`)
- Evie (100% `Bind`)

### Summary for Cecia

#### Cecia Provides

- Summoning — Single target

#### Damage types dealt by Cecia

- Physical — Arc, Single target
- DoT — Area, Single target

#### Debuffs provided by Cecia

- Magic DEF (Mythic+) — Single target — `low`
- Phys DEF (Mythic+) — Single target — `low`
- Vitality (EX+5) — Single target — `low`

#### Crowd Control provided by Cecia

- Bind — Area — `average`
- Bind (Mythic+) — Single target — `average`

## Chippy

### Chippy's behavior

- **Signature skill**: Brothers-in-arms (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `self-repositioner`
- **Damage types**: Physical `high`

#### Play overview

Chippy **summons two companions** at battle start to fight beside him, then leaps at a single target for direct damage. His normal attacks have a **rare chance to spike** into massive single-hit damage when luck lands. He is a **lightweight early summon** who adds bodies and occasional burst. Without **companions surviving** or fights long enough for crit spikes, his output stays modest. He offers little when enemies **wipe his summons immediately** or outscale his basic damage.

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `average`
- **Non-ultimate**: speed `average`, damage `high`

##### Ultimate

summon two companion units to join the battle

##### Skill 1

leap at single target, dealing damage

##### Skill 2

rare chance for massive single normal attack damage

### Units improving Chippy

- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Ravion**
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Lyca**
  - Energy (all units, low) `signature fuel`
  - ATK SPD (all units, low) `signature fuel`
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`
- **Phraesto**
  - Energy via Energy recovery speed (contract ally, start of battle) `signature fuel`

### Units benefitting most from Chippy

- Himmel (2.2 / 5)

### Units that can act as a replacement for Chippy

**Similar Skills**

- Marilee (60% `self-repositioner`)
- Alsa (50% `self-repositioner`)
- Kulu (50% `self-repositioner`)

**Damage**

- Alna (100% `Physical`)
- Antandra (100% `Physical`)
- Athalia (100% `Physical`)

### Summary for Chippy

#### Damage types dealt by Chippy

- Physical — Single target

## Contess

### Contess's behavior

`AFK Stages [A+]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S+]`, `PVP [S+]`

- **Signature skill**: Detention Pass (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-healer` `ally-shielder` `enemy-debuffer` `stealth` `temporary-stat-buffer` `untargetable`
- **Damage types**: Magic `low`

#### Play overview

Contess starts **hidden while recovering energy**, then emerges to heal an ally, grant rule immunity, and **convert their HP into shield**. She punishes foes who deal **large HP or shield loss**, healing weakest allies and cutting high-damage enemies' ATK. She also **slows ultimate casters' energy recovery** and stacks permanent ATK and energy penalties on repeat violations. Severe violations can trigger **permanent silence** and increased HP-loss effects that bypass unaffected. She needs **long fights** to cycle rules and punishments. Teams that **burst her before she emerges** or ignore her conduct rules see little from her kit.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, heal `average`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, heal `average`, debuffs `average`

##### Ultimate

Passive: start hidden recovering energy; Active: heal ally, grant rule immunity, ally converts HP to shield

##### Skill 1

Passive: penalize units causing large HP or shield loss; Active: heal weakest allies and reduce high-damage enemies' ATK

##### Skill 2

penalize ultimate casters by reducing energy recovery

##### Legendary+

violations permanently stack ATK and energy reduction

##### Mythic+

repeated violations lead to permanent silence and increased HP-loss, bypassing unaffected

##### Supreme+

violations trigger stun or silence based on rule type

### Units improving Contess

Look for units providing: `Energy`  
Common buffers are **Pandora**, **Thador**, **Rowan**, or **Ravion**.

- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Ravion**
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Lyca**
  - Energy (all units, low) `signature fuel`
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`
- **Phraesto**
  - Energy via Energy recovery speed (contract ally, start of battle) `signature fuel`

### Units benefitting most from Contess

Contess provides ATK to single targets `high`, Direct healing to multiple targets `high`, and Shield to single targets `average`.

**45** units include this provider among their top 6 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **4** strongest pairings: 

- Talene (4.7 / 5)
- Indris (4.3 / 5)
- Himmel (4.2 / 5)
- Shadewing (3.8 / 5)

### Units that can act as a replacement for Contess

**Best overall replacement**

- Evie (61% `Healing` `Crowd Control`)

**Buffs on allies**

- Hugin (100% `Shield` `ATK`)
- Saida (100% `Shield`)
- Thador (90% `Shield`)

**Healing**

- Solise (100% `Direct healing` `Healing`)
- Evie (100% `Direct healing` `Healing`)
- Smokey & Meerky (100% `Direct healing` `Healing`)

**Similar Skills**

- Velara (51% `ally-healer` `ally-shielder` `temporary-stat-buffer`)
- Evie (51% `ally-healer` `stealth` `temporary-stat-buffer`)
- Twins (45% `ally-healer` `ally-shielder` `temporary-stat-buffer`)

**Damage**

- Aliceth (100% `HP loss`)
- Faramor (100% `HP loss`)
- Ravion (100% `HP loss`)

**Crowd Control**

- Evie (90% `Silence`)

### Summary for Contess

#### Contess Provides

- Ally empower — Single target
- Damage absorption (allies) — Single target
- Debuff application — Enemies
- DoT conversion (EX+15) — Allies

#### Damage types dealt by Contess

- DoT — Single target

#### Buffs provided by Contess

- ATK — Single target — `high`
- Direct healing — Multiple targets — `high`
- Shield — Single target — `average`

#### Debuffs provided by Contess

- ATK — Multiple targets — `high`
- Energy — Multiple targets — `low`
- Max HP — Single target — `low`
- ATK (Legendary+) — Single target — `low`
- Energy (Legendary+) — Single target — `low`
- HP loss (Mythic+) — Single target — `average`

#### Crowd Control provided by Contess

- Untargetable — Self — On skill
- Silence (Mythic+) — Single target — `high`
- Stun (Supreme+) — Single target — `average`

## Cryonaia

### Cryonaia's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [B]`, `PVP [S]`

- **Signature skill**: Frostveil Domain (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Behavior tags**: `battlefield-modification` `cc-immunity` `execute` `high-damage-ult` `invincibility`
- **Damage types**: Magic `high`, DoT `high`

#### Play overview

Cryonaia traps several enemies in a **separate winter domain**, gaining shields, control immunity, haste, and attack while it lasts. Only she can cast her ultimate inside, and **weakened foes inside can be instantly defeated**. Enemies entering the domain take **massive damage**, while her sweeping AoE crosses the entire battlefield and her projectiles chip priority targets. Her attack **grows the longer her shield holds**, rewarding teams that help her survive the setup phase. She is devastating once the domain is up but **vulnerable until her first ultimate** lands. Teams must **protect her during the wind-up** or she never reaches her peak. Fights that **break her shield quickly** or deny grouping end the domain before her execute can trigger. Once inside, she alone controls the pace and can chain ultimates while enemies are trapped.

#### Skill overview

- **Signature skill (ult)**: speed `slow`
- **Non-ultimate**: speed `fast`, debuffs `average`, damage `high`

##### Ultimate

trap several enemies in a separate domain, granting self various boosts

##### Skill 1

sweeping AoE damage crosses the entire battlefield

##### Skill 2

fire multiple projectiles at target, dealing damage

##### Legendary+

ATK grows the longer shield stays active

##### Mythic+

deal massive damage each time enemies enter domain; only self can cast ultimate within

##### Supreme+

instantly defeat weakened enemies inside domain

### Units improving Cryonaia

Look for units providing: `ATK` `Shield`  
Common buffers are **Ravion**, **Pandora**, **Thador**, or **Rowan**.

- **Ravion**
  - ATK (multiple targets, high)
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Lyca**
  - Energy (all units, low) `signature fuel`
  - ATK SPD (all units, low) `signature fuel`
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`
- **Phraesto**
  - Energy via Energy recovery speed (contract ally, start of battle) `signature fuel`

### Units benefitting most from Cryonaia

- Shadewing (3.4 / 5)
- Bonnie (3.4 / 5)
- Himmel (2.2 / 5)

### Units that can act as a replacement for Cryonaia

**Similar Skills**

- Alna (25% `cc-immunity` `invincibility`)
- Lily May (22% `cc-immunity` `invincibility`)
- Harak (20% `execute`)

**Damage**

- Frieren (84% `DoT` `Magic`)
- Cyran (72% `DoT` `Magic`)
- Saida (64% `Magic` `DoT`)

**Debuffs on enemies**

- Himmel (100% `Damage taken`)
- Mehira (100% `Damage taken`)
- Kulu (100% `Damage taken`)

### Summary for Cryonaia

#### Cryonaia Provides

- Enemy isolation (domain) — Single target
- Battle time pause (EX+15) — Self
- Battle time pause (EX+15) — Single target
- Instant defeat (Supreme+) — Self

#### Damage types dealt by Cryonaia

- Magic — Area, Single target
- DoT — Area

#### Debuffs provided by Cryonaia

- Damage taken (EX+5) — Single target — `low`

#### Crowd Control provided by Cryonaia

- Immune — Self — Conditional

## Cyran

### Cyran's behavior

`AFK Stages [S]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Gravitic Requiem (ultimate)
- **Movement**: mostly stationary (avg attack range 6.0 tiles)
- **Behavior tags**: `aoe-damage` `enemy-grouping` `execute` `high-initial-energy`
- **Damage types**: Magic `high`, DoT `high`, True damage `average`

#### Play overview

Cyran opens with **sequential battle-start spells** and a large initial energy bonus for fast ultimate access. His orbs chip multiple foes, and he **throws the nearest enemy** into the densest cluster to set up AoE follow-through. His ultimate places a **pull zone** that damages and executes low-HP enemies at the center. Battle crit growth rewards repeated casts on grouped targets. He excels at **disrupting clustered lines** and finishing wounded foes. His opening spell chain gives him **immediate board impact** before enemies can spread out. He adds little when enemies **stay spread** or resist grouping and execute thresholds.

#### Skill overview

- **Signature skill (ult)**: speed `average`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `low`

##### Ultimate

place AoE pull zone dealing damage; execute low-HP enemies at center

##### Skill 1

launch multiple magic orbs at enemies

##### Skill 2

lift nearest enemy and throw at area with most enemies

##### Legendary+

battle crit increase

##### Mythic+

cast sequential opening spells at battle start

##### Supreme+

gain large initial energy bonus

### Units improving Cyran

Look for units providing: `ATK` `ATK SPD / Haste` `CRIT`  
Common buffers are **Ravion**, **Smokey & Meerky**, **Kazim**, or **Mikola**.

- **Aliceth**
  - ATK (multiple targets, average)
- **Pang**
  - ATK (multiple targets, average)
- **Hewynn**
  - ATK SPD via Haste (single target, average) `signature fuel`
- **Mehira**
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
- **Isabella**
  - ATK (single target, low, conditional (frequent))
  - ATK SPD via Haste (single target, low) `signature fuel`
- **Gunnar**
  - ATK (single target, low)
  - ATK SPD (single target, low) `signature fuel`

### Units benefitting most from Cyran

- Bonnie (3.4 / 5)
- Faramor (3.2 / 5)
- Indris (2.8 / 5)

### Units that can act as a replacement for Cyran

**Similar Skills**

- Nara (40% `execute` `high-initial-energy`)
- Eironn (34% `aoe-damage` `enemy-grouping`)
- Scarlita (34% `aoe-damage` `execute`)

**Damage**

- Korin (96% `True damage`)
- Temesia (93% `True damage`)
- Frieren (93% `DoT` `Magic` `True damage`)

**Crowd Control**

- Eironn (73% `Bind` `Displace`)
- Pippa (65% `Bind` `Displace` `Knock down`)
- Saida (50% `Bind` `Displace`)

### Summary for Cyran

#### Cyran Provides

- Artifact mimic (Mythic+) — Self
- Artifact block (EX+10) — Single target

#### Damage types dealt by Cyran

- Magic — Area, Single target
- DoT — Area
- True damage — All units — `average`

#### Debuffs provided by Cyran

- Execution — Single target — `low`
- ATK SPD (Mythic+) — All units — `low`

#### Crowd Control provided by Cyran

- Unaffected (Mythic+) — Self — Start of battle
- Bind — Area — `low`
- Displace — All units — `low`
- Displace — Area — `low`
- Knock down — Area — `low`
- Bind (Mythic+) — Single target — `low`

## Daimon

### Daimon's behavior

`AFK Stages [A+]`, `Dream Realm [B]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Buddy Barrier (Skill 2)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-shielder` `hp-scaling` `non-ult-utility` `summoner` `temporary-stat-buffer`
- **Ally composition**: place ally directly behind at battle prep (shield share, Life Drain, and ATK bond)
- **Damage types**: Magic `low`, Max HP-based damage `high`

#### Play overview

Daimon fights with an **untargetable companion** named Stitchy that frightens nearby enemies and joins his ultimate for true damage based on enemy HP. At battle start the companion attacks alongside him, dealing damage with basic attacks. He converts **enemy HP-loss into personal shield**, shares a portion of received shield with a **bonded ally**, and gains damage reduction while shielded. Excess shield value also **converts to HP** when overflowing, turning overheal into sustain. He blends **tanking, shielding, and sub-DPS** in one slot. He struggles as a **solo frontliner** without enough shield generation or a dedicated healer beside him. Teams that **deny HP-loss triggers** or kill his companion early blunt his sustain loop entirely. He pairs best with allies who generate frequent shields or trigger steady HP-loss on enemies.

#### Skill overview

- **Signature skill**: speed `fast`, buffs `average`
- **Ultimate**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `low`

##### Ultimate

summon companion to fight alongside

##### Skill 1

convert enemy HP-loss into a personal shield

##### Skill 2

share a portion of received shield with bonded ally

##### Legendary+

damage reduction grows while shielded

##### Mythic+

companion frightens nearby enemies

##### Supreme+

excess shield value converts to HP

### Units improving Daimon

Look for units providing: `Max HP` `Shield`  
Common buffers are **Contess**, **Hugin**, or **Thador**.

- **Aurora**
  - Haste (all summons, high)
  - Damage dealt via Damage dealt (all summons, average)
  - Damage taken via Damage taken (all summons, low)
- **Peggy**
  - ATK (all summons, high)
  - DEF via DEF (all summons, high)
- **Niru**
  - Named ally grant: Phys DEF (high)
  - Named ally grant: Magic DEF (high)
- **Florabelle**
  - Shield (all summons, average)
- **Saida**
  - Shield (multiple targets, high)
- **Korin**
  - Shield (single target, average)

### Units benefitting most from Daimon

Daimon provides Lifedrain to single targets `low`.

- Shadewing (3.4 / 5)
- Carolina (2.3 / 5)
- Nerion (2.1 / 5)

### Units that can act as a replacement for Daimon

**Buffs on allies**

- Kordan (100% `Healing`)
- Dunlingr (100% `Healing`)
- Zandrok (100% `Healing`)

**Similar Skills**

- Scarlita (42% `ally-shielder` `hp-scaling` `non-ult-utility`)
- Korin (40% `ally-shielder` `hp-scaling`)
- Gunnar (34% `ally-shielder` `temporary-stat-buffer`)

**Damage**

- Ludovic (100% `Magic` `Max HP-based damage`)
- Brutus (100% `Max HP-based damage`)
- Nara (100% `Max HP-based damage`)

**Crowd Control**

- Pandora (100% `Frighten`)
- Berial (100% `Frighten`)
- Silvina (100% `Frighten`)

### Summary for Daimon

#### Daimon Provides

- Summoning — Self

#### Damage types dealt by Daimon

- Magic — Single target
- DoT — Area
- Max HP-based damage — Area — `high`

#### Buffs provided by Daimon

- Lifedrain — Single target — `low`

#### Crowd Control provided by Daimon

- Frighten (Mythic+) — Area — `low`

## Damian

### Damian's behavior

`AFK Stages [C]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Inventor's Will (Mythic+)
- **Movement**: stationary (off battlefield)
- **Behavior tags**: `ally-buffer` `ally-healer` `summoner` `temporary-stat-buffer`
- **Damage types**: Magic `high`

#### Play overview

Damian summons toys that **heal weakest allies, restore energy, stun distant foes, and blind enemies** from a chariot he can control. His summon aura grants **haste to adjacent allies**, and battle ATK rises over time. Blinds last longer while **summon health stays above half**. He mixes **healing, buffing, and soft control** through multiple summons. Fights that **focus and kill his toys early** remove his healing, control, and blind extension.

#### Skill overview

- **Signature skill**: speed `fast`, buffs `average`
- **Ultimate**: speed `average`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `low`

##### Ultimate

summon or control toy chariot to blind enemies

##### Skill 1

summon heals weakest nearby ally or restores energy

##### Skill 2

control toy plane to stun the farthest enemy

##### Legendary+

battle ATK increase

##### Mythic+

summon aura inspires adjacent allies with haste

##### Supreme+

blind extends while summon health is above half

### Units improving Damian

Look for units providing: `ATK` `Haste` `Energy`  
Common buffers are **Ravion**, **Kazim**, **Mikola**, or **Smokey & Meerky**.

- **Aurora**
  - Haste (all summons, high)
  - Damage dealt via Damage dealt (all summons, average)
  - Damage taken via Damage taken (all summons, low)
- **Peggy**
  - ATK (all summons, high)
  - DEF via DEF (all summons, high)
- **Florabelle**
  - Shield (all summons, average)
- **Aliceth**
  - ATK (multiple targets, average)
- **Pang**
  - ATK (multiple targets, average)
- **Isabella**
  - ATK (single target, low, conditional (frequent))
  - Haste (single target, low) `signature fuel`

### Units benefitting most from Damian

Damian provides Direct healing to single targets `average` and Haste (Mythic+) to multiple targets `high` — conditional (frequent).

- Carolina (4.0 / 5)
- Nerion (3.9 / 5)
- Dunlingr (3.3 / 5)
- Lamentis (2.3 / 5)

### Units that can act as a replacement for Damian

**Best overall replacement**

- Twins (91% `Buffs on allies` `Healing` `Crowd Control` `Similar Skills`)
- Smokey & Meerky (81% `Buffs on allies` `Healing`)
- Lorsan (71% `Buffs on allies` `Healing`)

**Buffs on allies**

- Twins (100% `Haste`)
- Hugin (100% `Haste`)
- Smokey & Meerky (100% `Haste`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Twins (100% `Direct healing` `Healing`)

**Similar Skills**

- Koko (90% `ally-buffer` `ally-healer` `temporary-stat-buffer`)
- Isabella (90% `ally-buffer` `ally-healer` `temporary-stat-buffer`)
- Laios (80% `ally-buffer` `ally-healer` `summoner` `temporary-stat-buffer`)

**Damage**

- Frieren (100% `Magic`)
- Saida (100% `Magic`)
- Silven (100% `Magic`)

**Crowd Control**

- Hepler (100% `Blind` `Stun`)
- Aliceth (80% `Blind` `Stun`)
- Twins (73% `Blind`)

### Summary for Damian

#### Damian Provides

- Summoning — Single target

#### Damage types dealt by Damian

- Magic — Area, Single target

#### Buffs provided by Damian

- Direct healing — Single target — `average`
- Haste (Mythic+) — Multiple targets — `high` — conditional (frequent)

#### Crowd Control provided by Damian

- Blind — Area — `average`
- Stun — Single target — `high`
- Blind (Supreme+) — Single target — `high`

## Dionel

### Dionel's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Dawn Light (ultimate)
- **Movement**: moving (avg attack range 0.0 tiles)
- **Behavior tags**: `aoe-damage` `self-repositioner` `untargetable`
- **Damage types**: Physical `average`, True damage `average`

#### Play overview

Dionel's normal attacks become **long-range penetrating lines**, and he permanently gains attack speed with each strike. He stacks buffs from **allied boosts**, then spikes ATK and attack speed on active sip; at max stacks he unleashes a **true damage burst**. His ultimate soars untargetable, raining AoE hits that end with **bonus damage and knock-up**. Execution bonuses rise while his active buff is live. He needs **frequent ally buffs** to reach peak stacks and cycle his sip cleanly. Teams built around **continuous buffing** unlock his full damage ceiling. His attack speed snowballs over time, so longer fights favor his scaling pattern. Without buff support or **grouped enemies**, his line attacks and aerial burst underperform over the course of a long fight.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

soar into the air, dealing AoE damage; final hit deals bonus damage and knocks up

##### Skill 1

normal attack becomes long-range penetrating line

##### Skill 2

Passive: gain stacking buffs from allied boosts; Active: increase ATK and ATK SPD

##### Legendary+

ATK speed permanently rises with each normal attack

##### Mythic+

true damage burst available at max buff stacks

##### Supreme+

execution bonus increases while active buff is in effect

### Units improving Dionel

Look for units providing: `ATK` `ATK SPD / Haste` `Shield` `Execution`  
Common buffers are **Mikola**, **Ravion**, **Smokey & Meerky**, or **Dunlingr**.

Dionel also requires units **buffing them**

- **Isabella**
  - ATK (single target, low, conditional (frequent))
  - ATK SPD via Haste (single target, low) `signature fuel`
  - Grants 6 distinct temporary stat buffs to Dionel
- **Ravion**
  - ATK (multiple targets, high)
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
  - Grants 1 distinct temporary stat buff to Dionel
- **Perseus**
  - ATK (multiple targets, average)
  - Grants 3 distinct temporary stat buffs to Dionel
- **Lyca**
  - ATK SPD (all units, low) `signature fuel`
  - Energy (all units, low) `signature fuel`
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`
  - Grants 1 distinct temporary stat buff to Dionel
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
  - Grants 1 distinct temporary stat buff to Dionel
- **Hewynn**
  - ATK SPD via Haste (single target, average) `signature fuel`
  - Grants 1 distinct temporary stat buff to Dionel

### Units benefitting most from Dionel

- Niru (4.2 / 5)
- Kazim (2.3 / 5)
- Vala (1.9 / 5)

### Units that can act as a replacement for Dionel

**Best overall replacement**

- Frieren (89% `Damage` `Debuffs on enemies` `Crowd Control`)
- Faramor (69% `Damage` `Debuffs on enemies`)
- Nara (69% `Damage` `Debuffs on enemies` `Crowd Control`)

**Similar Skills**

- Rhys (80% `aoe-damage` `self-repositioner`)
- Igor (60% `aoe-damage` `self-repositioner` `untargetable`)
- Atalanta (60% `aoe-damage` `self-repositioner`)

**Damage**

- Frieren (100% `True damage`)
- Baelran (100% `True damage` `Physical`)
- Faramor (100% `True damage` `Physical`)

**Debuffs on enemies**

- Frieren (100% `Vitality`)
- Gunnar (100% `Vitality`)
- Gwyneth (100% `Vitality`)

**Crowd Control**

- Frieren (100% `Knock up`)
- Baelran (100% `Knock up`)
- Kordan (100% `Knock up`)

### Summary for Dionel

#### Dionel Provides

- Stacking — Single target
- Execution scaling (Supreme+) — Single target

#### Damage types dealt by Dionel

- Physical — Area
- True damage — All units — `average`

#### Debuffs provided by Dionel

- Vitality (Mythic+) — Single target — `low`

#### Crowd Control provided by Dionel

- Untargetable — Self — On skill
- Knock up — Single target — `low`

## Dunlingr

### Dunlingr's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S+]`

- **Signature skill**: Echo of Silence (ultimate)
- **Movement**: moving (melee class)
- **Behavior tags**: `ally-buffer` `aoe-damage` `battle-start-burst` `interrupt` `temporary-stat-buffer`
- **Damage types**: Magic `average`, HP loss `low`

#### Play overview

Before battle, Dunlingr **chooses a field rule** that blocks all healing or all ultimates for both sides. A bell enforces the rule at start, and casting his ultimate **extends the order** for more duration. He gains shields when order conditions are met and can **shield one ally from the rule** while granting allies attack speed or life drain at rule start. Frontal multi-hits add **rule-based bonus effects** on top of damage. Battle damage taken reduction keeps him standing while the order is active. He is oppressive against **heal-reliant or ultimate-reliant teams** but **handicaps his own side** with the same restriction. Enemies that **ignore the order** or burst teams that end fights inside the window waste his setup entirely. Choosing the right rule before battle is essential, since both options hurt allies too.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

pre-battle set a battlefield rule; Active: re-enforce the rule for additional duration

##### Skill 1

frontal area multi-hit with rule-based bonus effect

##### Skill 2

gain shield whenever order conditions are met

##### Legendary+

battle damage taken reduction

##### Mythic+

protect one ally from the imposed rule

##### Supreme+

rule start grants allies ATK speed or life drain

### Units improving Dunlingr

Look for units providing: `ATK SPD / Haste` `Max HP` `Shield` `Healing`  
Common buffers are **Pandora**, **Lorsan**, **Smokey & Meerky**, or **Twins**.

- **Pandora**
  - Max HP (single target, low)
  - Direct healing (single target, high)
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Hewynn**
  - ATK SPD via Haste (single target, average) `signature fuel`
  - Healing over time (all units, high)
- **Damian**
  - ATK SPD via Haste (multiple targets, average, conditional (frequent)) `signature fuel`
  - Direct healing (single target, high)
- **Zandrok**
  - ATK SPD via Haste (area, average, conditional (frequent)) `signature fuel`
  - Max HP (multiple targets, low)
  - Lifedrain (area, average, conditional (frequent))
- **Ravion**
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Isabella**
  - ATK SPD via Haste (single target, low) `signature fuel`
  - Direct healing (single target, high)

### Units benefitting most from Dunlingr

Dunlingr provides ATK (EX+5) to single targets `low`, Haste (EX+15) to single targets `average`, ATK SPD (Supreme+) to all units `low`, and Lifedrain (Supreme+) to all units `low`.

**42** units include this provider among their top 6 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight

These are the **4** strongest pairings: 

- Indris (5.0 / 5)
- Bonnie (3.9 / 5)
- Dionel (3.7 / 5)
- Vala (3.6 / 5)

### Units that can act as a replacement for Dunlingr

**Buffs on allies**

- Zandrok (70% `Healing` `Haste`)
- Kordan (52% `Healing` `ATK`)

**Similar Skills**

- Alna (61% `ally-buffer` `aoe-damage` `temporary-stat-buffer`)
- Sonja (60% `ally-buffer` `aoe-damage` `temporary-stat-buffer`)
- Perseus (60% `ally-buffer` `aoe-damage` `temporary-stat-buffer`)

**Damage**

- Faramor (100% `DoT` `HP loss`)

**Debuffs on enemies**

- Saida (88% `Energy`)
- Lily May (88% `Energy`)
- Pippa (70% `Energy`)

**Crowd Control**

- Contess (100% `Silence`)
- Gwyneth (100% `Silence`)
- Sylphira (100% `Silence`)

### Summary for Dunlingr

#### Dunlingr Provides

- Heal lock (Curelock) — All units
- Ultimate lock (Spellbind) — All units

#### Damage types dealt by Dunlingr

- Magic — All units, Area
- HP loss — Single target — `low`

#### Buffs provided by Dunlingr

- ATK (EX+5) — Single target — `low`
- Haste (EX+15) — Single target — `average`
- ATK SPD (Supreme+) — All units — `low`
- Lifedrain (Supreme+) — All units — `low`

#### Debuffs provided by Dunlingr

- Haste — Single target — `low`
- Energy (Supreme+) — All units — `average`
- Haste (Supreme+) — All units — `low`
- Vitality (Supreme+) — All units — `low`

#### Crowd Control provided by Dunlingr

- Silence — Single target — `low`

## Eironn

### Eironn's behavior

`AFK Stages [S]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Verdant Cyclone (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `aoe-damage` `battle-start-burst` `battle-start-ult` `enemy-grouping` `mass-cc`
- **Damage types**: Magic `high`

#### Play overview

Eironn can **cast his ultimate on any tile at battle start**, pulling nearby enemies to the center for damage and immobilization. His dual-sword sweep **reduces enemy haste and Magic DEF**, and he shields himself with high dodge when pressed. Ranged defense **scales up at low HP**, and immobilized targets take **extra Magic DEF reduction**. He is a premier **opener for control and magic damage teams**. His value drops against **pull-immune or unaffected targets**.

#### Skill overview

- **Signature skill (ult)**: speed `average`, first cast speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

pull nearby enemies to center, dealing damage and immobilizing

##### Skill 1

AoE dual-sword attack reducing enemy haste and magic DEF

##### Skill 2

large personal shield, granting high dodge rate

##### Legendary+

ranged DEF scales up when health is low

##### Mythic+

cast ultimate on any tile at battle start

##### Supreme+

extra magic DEF reduction on immobilized targets

### Units improving Eironn

Look for units providing: `Shield` `Physical DEF`  
Common buffers are **Mikola**, **Rowan**, **Twins**, or **Smokey & Meerky**.

- **Niru**
  - Phys DEF (single target, high)
- **Tilaya**
  - DEF (area, high)
- **Isabella**
  - Phys DEF (single target, low)
  - ATK SPD via Haste (single target, low) `signature fuel`
- **Hewynn**
  - ATK SPD via Haste (single target, average) `signature fuel`
- **Mehira**
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
- **Shakir**
  - ATK SPD via Haste (area, average) `signature fuel`

### Units benefitting most from Eironn

- Faramor (3.5 / 5)

### Units that can act as a replacement for Eironn

**Similar Skills**

- Walker (51% `aoe-damage` `battle-start-burst` `mass-cc`)
- Mehira (45% `aoe-damage` `enemy-grouping` `mass-cc`)
- Tasi (41% `aoe-damage` `mass-cc`)

**Damage**

- Frieren (100% `Magic`)
- Saida (100% `Magic`)
- Silven (100% `Magic`)

**Debuffs on enemies**

- Lorsan (100% `Haste`)
- Carolina (90% `Haste` `Magic DEF`)
- Kafra (88% `Haste`)

**Crowd Control**

- Arden (90% `Bind`)
- Carolina (90% `Bind`)
- Evie (84% `Bind` `Displace`)

### Summary for Eironn

#### Damage types dealt by Eironn

- Magic — Arc, Area

#### Debuffs provided by Eironn

- Haste — Arc — `average`
- Magic DEF — Single target — `high`

#### Crowd Control provided by Eironn

- Bind — Area — `average`
- Displace — Area — `low`
- Bind (EX+10) — Single target — `high`

## Evie

### Evie's behavior

`AFK Stages [B]`, `Dream Realm [A+]`, `Dream Realm (Endless) [B]`, `PVP [S]`

- **Signature skill**: Intel Chase (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-healer` `self-repositioner` `stealth` `temporary-stat-buffer`
- **Ally composition**: rearmost ally starts with healing quill; tracks highest damage dealer
- **Damage types**: Magic `average`

#### Play overview

Evie begins **concealed on the enemy side**, gathering intel on nearby foes to reduce their Magic DEF and fuel her ultimate. She sends a quill to **follow an ally for buffs and healing**, and full intel on all enemies **inflicts debuffs** across the line. A completed investigation can **silence her immobilize target** and spawn an extra support quill. Battle healing growth keeps her sustain relevant over long fights. She loses intel when **allies cast ultimates**, slowing her setup considerably. She works best when enemies cluster so she can investigate most of the line quickly. Spread enemy lines or **fast burst** that ends fights before intel completes waste her debuff package entirely. She offers broad utility but lacks a single standout specialty.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

Passive: start concealed on enemy side gathering intel; Active: immobilize enemy, also silencing if intel gathered

##### Skill 1

Passive: observation stacks reduce target magic DEF; Active: multi-strike

##### Skill 2

send a quill to follow an ally, buffing and healing them

##### Legendary+

battle healing stat increase

##### Mythic+

gathering intel on all enemies inflicts debuffs on them

##### Supreme+

full intel spawns an extra ally support quill

### Units improving Evie

Look for units providing: `ATK` `Energy`  
Common buffers are **Ravion**, **Pandora**, **Contess**, or **Kazim**.

- **Ravion**
  - ATK (multiple targets, high)
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Aliceth**
  - ATK (multiple targets, average)
- **Pang**
  - ATK (multiple targets, average)

### Units benefitting most from Evie

Evie provides ATK to single targets `average` and Direct healing to single targets `low`.

**33** units include this provider among their top 6 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **4** strongest pairings: 

- Indris (4.9 / 5)
- Talene (4.7 / 5)
- Himmel (4.2 / 5)
- Aurora (2.8 / 5)

### Units that can act as a replacement for Evie

**Best overall replacement**

- Contess (55% `Healing`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Smokey & Meerky (100% `Direct healing` `Healing`)

**Similar Skills**

- Fay (57% `ally-healer` `temporary-stat-buffer`)
- Contess (51% `ally-healer` `stealth` `temporary-stat-buffer`)
- Smokey & Meerky (48% `ally-healer` `temporary-stat-buffer`)

**Damage**

- Frieren (100% `Magic`)
- Saida (100% `Magic`)
- Silven (100% `Magic`)

**Debuffs on enemies**

- Thador (72% `Magic DEF`)

**Crowd Control**

- Eironn (52% `Bind` `Displace`)

### Summary for Evie

#### Evie Provides

- Invincibility — Self
- Invincibility — All units

#### Damage types dealt by Evie

- Magic — Single target

#### Buffs provided by Evie

- ATK — Single target — `average`
- Direct healing — Single target — `low`

#### Debuffs provided by Evie

- Magic DEF — Single target — `low`
- Magic DEF — All units — `average`
- Damage dealt (Mythic+) — Single target — `average`
- Debuff duration (Mythic+) — Multiple targets — `average`
- Debuff duration (EX+5) — Single target — `average`

#### Crowd Control provided by Evie

- Bind — Single target — `high`
- Displace — Single target — `low`
- Silence — Single target — `high`

## Faramor

### Faramor's behavior

`AFK Stages [S]`, `Dream Realm [S]`, `Dream Realm (Endless) [A+]`, `PVP [B]`

- **Signature skill**: Sanctified Circle (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-buffer` `aoe-damage` `dot-specialist` `hp-scaling`
- **Ally composition**: bless adjacent ally at battle prep; prioritizes tile behind
- **Damage types**: Physical `high`, DoT `high`, HP loss `high`, True damage `high`

#### Play overview

Faramor drops a **circular zone that blocks healing** and deals sustained true damage to enemies inside. He shields on strike, blesses an ally to **boost both their ATK**, then stuns nearby foes around each of them. While the circle is active he **enhances his own skills** and grants allies bonus true damage inside. Enemies revived within the zone also suffer **reduced vitality**. Battle haste growth keeps his rotation moving through longer fights. He needs **survival time** to maintain the circle and energy to sustain it. **High burst teams** that kill him early or enemies that **never enter the zone** negate his anti-heal and true damage payoff. Allies who fight inside his circle gain the most from his true damage amplification.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `high`

##### Ultimate

circular area blocks healing and deals sustained true damage

##### Skill 1

gain shield and deal damage to current target

##### Skill 2

bless an ally, boosting ATK for both, then stun nearby enemies around each

##### Legendary+

battle haste increase

##### Mythic+

active circle enhances own abilities and grants allies bonus true damage inside

##### Supreme+

reduce vitality of enemies revived inside circular area

### Units improving Faramor

Look for units providing: `ATK` `Haste` `Shield`  
Common buffers are **Mikola**, **Ravion**, **Smokey & Meerky**, or **Dunlingr**.

Faramor also requires units **grouping enemies** and/or units **buffing them**

- **Isabella**
  - ATK (single target, low, conditional (frequent))
  - Haste (single target, low) `signature fuel`
  - Grants 6 distinct temporary stat buffs to Faramor
- **Mehira**
  - Haste (multiple targets, average) `signature fuel`
  - Enables Enemy grouping via Displace (all units, low)
  - Grants 1 distinct temporary stat buff to Faramor
- **Ravion**
  - ATK (multiple targets, high)
  - Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
  - Grants 1 distinct temporary stat buff to Faramor
- **Eironn**
  - Enables Enemy grouping via Displace (area, low), battle start
- **Perseus**
  - ATK (multiple targets, average)
  - Grants 3 distinct temporary stat buffs to Faramor
- **Cyran**
  - Enables Enemy grouping via Displace (all units, low)

### Units benefitting most from Faramor

- Shadewing (3.4 / 5)

### Units that can act as a replacement for Faramor

**Best overall replacement**

- Nazrik (61% `Debuffs on enemies` `Crowd Control`)
- Frieren (60% `Damage` `Debuffs on enemies`)
- Nara (56% `Damage` `Debuffs on enemies`)

**Similar Skills**

- Viperian (60% `aoe-damage` `dot-specialist`)
- Arden (57% `aoe-damage` `dot-specialist`)
- Perseus (48% `ally-buffer` `aoe-damage`)

**Damage**

- Athalia (100% `True damage` `Physical`)
- Nara (99% `True damage` `Physical`)
- Frieren (67% `True damage` `DoT`)

**Debuffs on enemies**

- Frieren (100% `Vitality`)
- Gunnar (100% `Vitality`)
- Gwyneth (100% `Vitality`)

**Crowd Control**

- Contess (100% `Stun`)
- Gwyneth (100% `Stun`)
- Aliceth (100% `Stun`)

### Summary for Faramor

#### Damage types dealt by Faramor

- Physical — Area, Single target
- DoT — Area
- HP loss — Area — `high`
- True damage — Area — `high`

#### Debuffs provided by Faramor

- Vitality (Supreme+) — Single target — `low`

#### Crowd Control provided by Faramor

- Stun — Area — `low`

## Fay

### Fay's behavior

`AFK Stages [C]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [C]`

- **Signature skill**: Vibrant Dance (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Behavior tags**: `ally-healer` `aoe-healing` `temporary-stat-buffer`
- **Damage types**: Magic `average`

#### Play overview

Fay heals and buffs **allies within ultimate range**, with steady single-target healing and an AoE burst that damages foes while healing friends. She opens battle by **healing and buffing the ally in front of her tile**, and combat max HP rises over time. Low-HP allies also trigger an **emergency heal** for clutch saves. She is a **reliable early support** when stronger healers are unavailable. Her healing output and buffs are **modest compared to top supports**.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, heal `average`, buffs `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `average`

##### Ultimate

heal and buff allies within range

##### Skill 1

heal one ally over time

##### Skill 2

AoE burst damages foes and heals allies

##### Legendary+

combat max HP increase

##### Mythic+

battle-start heal and buff the ally on tile in front

##### Supreme+

low HP ally triggers emergency heal

### Units improving Fay

Look for units providing: `ATK` `ATK SPD / Haste`  
Common buffers are **Ravion**, **Smokey & Meerky**, **Mikola**, or **Kazim**.

- **Ravion**
  - ATK (multiple targets, high)
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Lyca**
  - ATK SPD (all units, low) `signature fuel`
  - Energy (all units, low) `signature fuel`
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Hewynn**
  - ATK SPD via Haste (single target, average) `signature fuel`
- **Mehira**
  - ATK SPD via Haste (multiple targets, average) `signature fuel`

### Units benefitting most from Fay

Fay provides ATK to arc `low`, Direct healing to arc `high`, Healing over time to single targets `average`, and Vitality (EX+5) to single targets `low`.

- Bonnie (3.1 / 5)
- Himmel (2.9 / 5)
- Vala (2.2 / 5)

### Units that can act as a replacement for Fay

**Best overall replacement**

- Evie (77% `Healing` `Buffs on allies`)
- Smokey & Meerky (76% `Healing` `Buffs on allies` `Similar Skills`)
- Isabella (75% `Healing` `Buffs on allies` `Similar Skills`)

**Buffs on allies**

- Twins (100% `ATK` `Vitality`)
- Koko (100% `ATK` `Vitality`)
- Mikola (100% `ATK` `Vitality`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing over time` `Healing`)
- Evie (100% `Direct healing` `Healing`)

**Similar Skills**

- Smokey & Meerky (100% `ally-healer` `aoe-healing` `temporary-stat-buffer`)
- Hewynn (100% `ally-healer` `aoe-healing` `temporary-stat-buffer`)
- Velara (90% `ally-healer` `aoe-healing` `temporary-stat-buffer`)

**Damage**

- Frieren (100% `Magic`)
- Saida (100% `Magic`)
- Silven (100% `Magic`)

### Summary for Fay

#### Damage types dealt by Fay

- Magic — Area

#### Buffs provided by Fay

- ATK — Arc — `low`
- Direct healing — Arc — `high`
- Healing over time — Single target — `average`
- Vitality (EX+5) — Single target — `low`

## Florabelle

### Florabelle's behavior

`AFK Stages [A]`, `Dream Realm [A+]`, `Dream Realm (Endless) [S]`, `PVP [C]`

- **Signature skill**: Pounding Blow (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `aoe-damage` `summoner`
- **Damage types**: Physical `high`

#### Play overview

Florabelle opens with a **battle-start tank summon**, then smashes adjacent tiles on ultimate while buffing ally summons with **haste and life drain**. She can summon a **ranged ally**, and combat ATK rises with multiple summons on the field. Each allied summon gains a **permanent shield on entry**, and large summons gain **control immunity and ATK boost**. She peaks in **summon-heavy compositions** that keep bodies on the board. Against teams that **wipe her critters early**, her scaling and shields never build.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `low`

##### Ultimate

Passive: battle-start tank summon; Active: cast is adjacent AoE smash

##### Skill 1

grant growth buff to ally summon, boosting haste and life drain

##### Skill 2

summon a ranged ally

##### Legendary+

combat ATK bonus with multiple summons on field

##### Mythic+

grant permanent shield to each allied summon when they enter battle

##### Supreme+

large summons gain control immunity and ATK boost

### Units improving Florabelle

Look for units providing: `ATK` `Haste`  
Common buffers are **Ravion**, **Kazim**, **Mikola**, or **Smokey & Meerky**.

- **Peggy**
  - ATK (all summons, high)
  - DEF via DEF (all summons, high)
  - Ranged damage via Ranged damage (all summons, low)
- **Aurora**
  - Haste (all summons, high)
  - Damage dealt via Damage dealt (all summons, average)
  - Damage taken via Damage taken (all summons, low)
- **Ravion**
  - ATK (multiple targets, high)
  - Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Aliceth**
  - ATK (multiple targets, average)
- **Pang**
  - ATK (multiple targets, average)

### Units benefitting most from Florabelle

Florabelle provides Shield (Mythic+) to all summons `average`.

**6** units include this provider among their top 6 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **4** strongest pairings: 

- Kazim (4.5 / 5)
- Berial (2.3 / 5)
- Daimon (2.3 / 5)
- Lamentis (2.0 / 5)

### Units that can act as a replacement for Florabelle

**Best overall replacement**

- Kazim (56% `Damage` `Crowd Control`)
- Pang (55% `Damage`)
- Perseus (53% `Damage`)

**Similar Skills**

- Galahad (80% `aoe-damage` `summoner`)
- Hodgkin (66% `aoe-damage` `summoner`)
- Zanie (50% `summoner`)

**Damage**

- Gwyneth (100% `Physical`)
- Athalia (100% `Physical`)
- Kulu (100% `Physical`)

**Crowd Control**

- Zandrok (100% `Knock up`)
- Nerion (100% `Knock up`)
- Scarlita (100% `Knock up`)

### Summary for Florabelle

#### Florabelle Provides

- Summoning — Single target

#### Damage types dealt by Florabelle

- Physical — Area, Multiple targets

#### Buffs provided by Florabelle

- Shield (Mythic+) — All summons — `average`

#### Crowd Control provided by Florabelle

- Immune (Supreme+) — Owned summons — Form
- Knock up — Area — `low`

## Frieren

### Frieren's behavior

`AFK Stages [S+]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S+]`, `PVP [S+]`

- **Signature skill**: Zoltraak (ultimate)
- **Movement**: stationary (avg attack range 7.0 tiles)
- **Behavior tags**: `aoe-damage` `dot-specialist` `high-damage-ult` `self-repositioner`
- **Ally composition**: frontmost ally shares damage reduction with this hero
- **Damage types**: Magic `high`, DoT `high`, True damage `high`

#### Play overview

Frieren begins **concealed and low-priority**, then needs about 15 seconds to **amplify her magic**. With **Himmel adjacent**, she skips the wait and gains a permanent ATK bonus from his stats. After ramping, her damage jumps from enhanced normal attacks and a **vitality-reducing burn**. Her rectangle ultimate adds **split true damage**. She shines in **long fights**, with damage reduction for herself and the frontmost ally buying time to cast. **Burst before amplification** shuts her down early, and **short fights** never develop her burn or ultimate.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

deal heavy damage to enemies in a rectangular area

##### Skill 1

conceal magic then amplify, replacing normal attacks with enhanced attacks that can stun

##### Skill 2

area burn applies vitality reduction

##### Legendary+

battle ATK increase

##### Mythic+

reduce damage taken for self and frontmost ally

##### Supreme+

knock up then knock down the highest cumulative damage dealer

### Units improving Frieren

Look for units providing: `ATK` `Haste`  
Common buffers are **Ravion**, **Pandora**, **Kazim**, or **Mikola**.

Frieren also requires specific **named allies**

- **Ravion**
  - ATK (multiple targets, high)
  - Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Himmel**
  - Enables Named ally on team via Himmel named in skill text
  - Named ally grant: Penetration (average)
- **Thador**
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Phraesto**
  - Energy via Energy recovery speed (contract ally, start of battle) `signature fuel`

### Units benefitting most from Frieren

- Himmel (4.8 / 5)
- Shadewing (4.1 / 5)

### Units that can act as a replacement for Frieren

**Best overall replacement**

- Faramor (50% `Damage`)

**Similar Skills**

- Himmel (48% `aoe-damage` `self-repositioner`)
- Marcille (41% `aoe-damage` `high-damage-ult`)
- Faramor (40% `aoe-damage` `dot-specialist`)

**Damage**

- Faramor (87% `True damage` `DoT`)
- Athalia (80% `True damage`)
- Sylphira (79% `Magic` `True damage`)

**Crowd Control**

- Baelran (85% `Knock down` `Knock up`)
- Himmel (68% `Knock down`)
- Silven (68% `Knock down`)

### Summary for Frieren

#### Damage types dealt by Frieren

- Magic — Area, Single target
- DoT — All units, Area
- True damage — All units — `high`

#### Debuffs provided by Frieren

- DoT — Area — `low`
- Vitality — Single target — `low`

#### Crowd Control provided by Frieren

- Stun — Single target — `low`
- Knock down (Supreme+) — Single target — `average`
- Knock up (Supreme+) — Single target — `low`

## Galahad

### Galahad's behavior

`AFK Stages [S]`, `Dream Realm [A+]`, `Dream Realm (Endless) [S+]`, `PVP [B]`

- **Signature skill**: Time Recast (Mythic+)
- **Movement**: stationary (avg attack range 10.0 tiles)
- **Behavior tags**: `ally-shielder` `aoe-damage` `summoner`
- **Ally composition**: nearest ally auto-selected at battle start; prioritizes ally behind
- **Damage types**: Magic `high`

#### Play overview

Galahad needs her **circular zone to fill** with energy before clones and enhanced casts come online, so early timing matters. Her ultimate immobilizes the **top cumulative damage dealer** with HP-loss tied to healing received, then lashes a wider area. Weakest allies gain **exploding shields** that detonate for area damage on expiry. Once the zone completes, a **shadow duplicate** of an ally fights beside her while battle ATK climbs. External buffs grant **sustained energy and steadfast** status to keep the zone growing. She excels in **long attrition fights** where energy-fed clones stack pressure. **Early burst** that kills her before the zone matures, or teams that cannot protect the circle while it charges, blunt her payoff.

#### Skill overview

- **Signature skill**: speed `fast`
- **Ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, damage `average`

##### Ultimate

AoE damage then create energy-consuming zone; when full, gain buff and skill casts spawn shadow duplicates

##### Skill 1

immobilize top attacker, causing HP-loss based on healing received, then AoE in wider range

##### Skill 2

shield weakest ally; explodes on expiry, dealing area damage

##### Legendary+

ATK grows after circular zone fully forms

##### Mythic+

once zone fully forms, summon temporary shadow of an ally to fight alongside

##### Supreme+

external buff grants sustained energy and steadfast state

### Units improving Galahad

Look for units providing: `ATK` `Haste` `Energy`  
Common buffers are **Ravion**, **Kazim**, **Mikola**, or **Smokey & Meerky**.

- **Aurora**
  - Haste (all summons, high)
  - Damage dealt via Damage dealt (all summons, average)
  - Damage taken via Damage taken (all summons, low)
- **Peggy**
  - ATK (all summons, high)
  - DEF via DEF (all summons, high)
- **Florabelle**
  - Shield (all summons, average)
- **Aliceth**
  - ATK (multiple targets, average)
- **Pang**
  - ATK (multiple targets, average)
- **Isabella**
  - ATK (single target, low, conditional (frequent))
  - Haste (single target, low) `signature fuel`

### Units benefitting most from Galahad

- Niru (5.0 / 5)
- Bonnie (4.6 / 5)

### Units that can act as a replacement for Galahad

**Best overall replacement**

- Saida (55% `Damage` `Crowd Control`)
- Natsu (52% `Damage`)
- Marcille (50% `Damage`)

**Similar Skills**

- Florabelle (80% `aoe-damage` `summoner`)
- Phraesto (60% `ally-shielder` `aoe-damage` `summoner`)
- Ulmus (50% `ally-shielder` `aoe-damage`)

**Damage**

- Saida (100% `Magic`)
- Sylphira (100% `Magic`)
- Cryonaia (100% `Magic`)

**Debuffs on enemies**

- Zorya (64% `Movement speed` `Haste`)

**Crowd Control**

- Gwyneth (100% `Bind`)
- Alna (100% `Bind`)
- Velara (100% `Bind`)

### Summary for Galahad

#### Galahad Provides

- Summoning (Mythic+) — Single target
- Artifact (EX+10) — Single target

#### Damage types dealt by Galahad

- Magic — All units, Area, Single target

#### Debuffs provided by Galahad

- Haste — Area — `average`
- Movement speed — Area — `average`

#### Crowd Control provided by Galahad

- Steadfast (Supreme+) — Self — On skill
- Bind — Single target — `average`

## Gerda

### Gerda's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Spring Therapy (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-healer` `ally-shielder` `aoe-healing` `battle-start-burst` `mass-cc` `self-repositioner`
- **Damage types**: Physical `high`

#### Play overview

Gerda opens with a **battle-start leap** that interrupts nearby enemies and drops a **healing zone** where she lands. Her ultimate sleeps foes in range while **healing allies**, turning clustered lines into a stall window. A stun skill adds a personal shield, and battle damage taken reduction keeps her standing through the opener. Enhanced zone healing and **cooldown reduction on zone heals** keep her rotation moving as allies stand inside. At higher tiers the opening leap **stuns instead of interrupting**, tightening control on grouped targets. She is a **strong early tank-healer** when enemies bunch up and can be caught in the zone. **Spread formations** and foes immune to sleep or interrupt waste her leap and zone value entirely.

#### Skill overview

- **Signature skill**: speed `fast`, heal `average`, damage `average`
- **Ultimate**: speed `average`, heal `average`, damage `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `average`

##### Ultimate

AoE sleep nearby enemies and heal allies

##### Skill 1

leap forward at battle start, interrupting nearby enemies and creating a healing zone

##### Skill 2

stun an enemy while gaining a shield

##### Legendary+

battle damage taken reduction

##### Mythic+

enhance healing zone healing; reduce skill cooldown whenever ally is healed by zone

##### Supreme+

battle-start leap stuns enemies instead of interrupting

### Units improving Gerda

Look for units providing: `Max HP` `Shield`

_No synergy partners matched stat buffs or enablers._

### Units benefitting most from Gerda

Gerda provides Direct healing in an area `average` and Healing over time to single targets `average`.

- Niru (4.2 / 5)
- Carolina (2.0 / 5)
- Nerion (1.8 / 5)

### Units that can act as a replacement for Gerda

**Best overall replacement**

- Hepler (59% `Damage` `Healing`)

**Healing**

- Solise (100% `Direct healing` `Healing over time` `Healing`)
- Ludovic (100% `Direct healing` `Healing over time` `Healing`)
- Smokey & Meerky (100% `Direct healing` `Healing over time` `Healing`)

**Similar Skills**

- Solise (50% `ally-healer` `ally-shielder` `aoe-healing`)
- Velara (42% `ally-healer` `ally-shielder` `aoe-healing`)
- Hepler (41% `ally-healer` `ally-shielder`)

**Damage**

- Gunnar (100% `Physical`)
- Gwyneth (100% `Physical`)
- Himmel (100% `Physical`)

**Crowd Control**

- Lucca (54% `Stun` `Interrupt`)

### Summary for Gerda

#### Damage types dealt by Gerda

- Physical — Area, Single target

#### Buffs provided by Gerda

- Direct healing — Area — `average`
- Healing over time — Single target — `average`

#### Crowd Control provided by Gerda

- Unaffected — Self — On skill
- Bind — Single target — `low`
- Interrupt — Area — `low`
- Sleep — Single target — `low`
- Stun — Single target — `average`
- Interrupt (Supreme+) — Single target — `low`

## Granny Dahnie

### Granny Dahnie's behavior

`AFK Stages [C]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Threshold of Jade (ultimate)
- **Movement**: moving (melee class)
- **Behavior tags**: `hp-scaling` `taunt`
- **Damage types**: Physical `low`, DoT `low`

#### Play overview

Granny Dahnie taunts a foe and **recovers HP**, then retaliates with projectiles when damage thresholds are crossed, slowing attacker haste. Her ultimate immobilizes nearby enemies while **draining HP and energy**, staying unaffected during the channel. Low HP triggers **Phys and Magic DEF boosts** plus recovery, and triggered shots grant instant self-heals. Vitality scales with **ultimate casting** over longer fights. She stalls **melee-heavy lines** that keep feeding her retaliations and taunt cycles. **Burst before her ultimate** lands, or taunt-immune targets, leave her as a slow frontliner with modest team utility.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, debuffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `low`

##### Ultimate

immobilize enemies in range, draining their HP and energy, unaffected by control during effect

##### Skill 1

trigger retaliatory projectile at damage threshold, reducing attacker haste

##### Skill 2

taunt an enemy and recover HP

##### Legendary+

battle vitality scales with ultimate casting

##### Mythic+

low HP triggers Phys and Magic DEF boost and HP recovery

##### Supreme+

triggered projectiles grant instant self HP recovery

### Units improving Granny Dahnie

Look for units providing: `Haste` `Energy` `Physical DEF` `Magic DEF`  
Common buffers are **Rowan**, **Mikola**, **Pandora**, or **Ravion**.

- **Rowan**
  - Energy (area, high) `signature fuel`
  - Phys DEF (single target, average)
  - Magic DEF (single target, average)
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Niru**
  - Phys DEF (single target, high)
  - Magic DEF (single target, high)
- **Tilaya**
  - DEF (area, high)
  - DEF (area, high)
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Ravion**
  - Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`

### Units benefitting most from Granny Dahnie

- Himmel (2.2 / 5)
- Shadewing (1.9 / 5)
- Indris (1.5 / 5)

### Units that can act as a replacement for Granny Dahnie

**Best overall replacement**

- Hepler (52% `Crowd Control` `Damage` `Debuffs on enemies`)
- Brutus (51% `Crowd Control` `Damage`)

**Similar Skills**

- Baelran (50% `hp-scaling`)
- Pippa (40% `hp-scaling`)
- Shemira (33% `hp-scaling`)

**Damage**

- Gunnar (100% `Physical` `DoT`)
- Gwyneth (100% `Physical` `DoT`)
- Alna (100% `Physical` `DoT`)

**Debuffs on enemies**

- Vala (88% `Haste` `Energy`)
- Dunlingr (84% `Haste` `Energy`)
- Alna (80% `Haste`)

**Crowd Control**

- Phraesto (90% `Taunt`)
- Brutus (90% `Taunt`)
- Hepler (90% `Taunt`)

### Summary for Granny Dahnie

#### Damage types dealt by Granny Dahnie

- Physical — Single target
- DoT — Single target

#### Debuffs provided by Granny Dahnie

- Energy — Single target — `low`
- Haste — Single target — `high`

#### Crowd Control provided by Granny Dahnie

- Unaffected — Self — On skill
- Bind — Single target — `low`
- Taunt — Single target — `average`

## Gunnar

### Gunnar's behavior

`AFK Stages [S+]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S+]`, `PVP [S+]`

- **Signature skill**: Annihilation Directive (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-shielder` `aoe-damage` `static-tile-buffer` `temporary-stat-buffer`
- **Ally composition**: place ally 1 tile behind at battle start (Doomfield buffs and coordinated attacks)
- **Damage types**: Physical `high`, DoT `low`

#### Play overview

Gunnar anchors a **rear ally on a passive field** that empowers their range and ATK, then shields everyone behind himself on active cast. Cannon volleys pepper targeted areas, and his **scorched ultimate** deals massive AoE while denying heals and shields inside the burn. Ranged DEF and vitality **scale with allied positioning**, and ally damage thresholds trigger **self-healing missiles** when the line takes pressure. He wants a protected rear partner and enemies walking into sustained fire across multiple casts. **Anti-shield or heal-immune foes** shrug off his zone denial entirely. Without **clustered enemies** in cannon and burn range, his damage and suppression stay modest for the slot.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, buffs `average`, debuffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `high`

##### Ultimate

Passive: summon field on rear ally's tile, enhancing them; Active: massive AoE damage, setting area on fire

##### Skill 1

fire cannons multiple times, dealing damage to enemies in targeted areas

##### Skill 2

shield self and all allies behind, also empowering the field ally

##### Legendary+

ranged DEF and vitality scale with allied positioning

##### Mythic+

ally damage threshold triggers missile with self-heal

##### Supreme+

scorched area enemies cannot heal or gain shields

### Units improving Gunnar

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Pandora**, **Ravion**, **Hugin**, or **Lorsan**.

- **Pandora**
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Ravion**
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Lyca**
  - ATK SPD (all units, low) `signature fuel`
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`
- **Thador**
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Hewynn**
  - ATK SPD via Haste (single target, average) `signature fuel`

### Units benefitting most from Gunnar

Gunnar provides ATK to single targets `high`, ATK SPD to single targets `low`, Attack range to single targets `high`, Ranged DEF (Legendary+) to single targets `low`, Vitality (Legendary+) to single targets `low`, and Invincible (EX+15) to single targets `high`.

- Niru (5.0 / 5)

### Units that can act as a replacement for Gunnar

**Similar Skills**

- Hugin (50% `ally-shielder` `static-tile-buffer` `temporary-stat-buffer`)
- Galahad (40% `ally-shielder` `aoe-damage`)
- Thador (40% `ally-shielder` `temporary-stat-buffer`)

**Damage**

- Gwyneth (100% `Physical` `DoT`)
- Himmel (98% `Physical`)

**Crowd Control**

- Frieren (100% `Stun`)
- Contess (100% `Stun`)
- Gwyneth (100% `Stun`)

### Summary for Gunnar

#### Gunnar Provides

- Invincibility (EX+15) — Single target

#### Damage types dealt by Gunnar

- Physical — All units, Area, Single target
- DoT — Single target
- Max HP-based damage — Single target

#### Buffs provided by Gunnar

- ATK — Single target — `high`
- ATK SPD — Single target — `low`
- Attack range — Single target — `high`
- Ranged DEF (Legendary+) — Single target — `low`
- Vitality (Legendary+) — Single target — `low`
- Invincible (EX+15) — Single target — `high`

#### Debuffs provided by Gunnar

- Vitality — Single target — `low`
- Healing (Supreme+) — Area — `low`

#### Crowd Control provided by Gunnar

- Stun — Single target — `low`

## Gwyneth

### Gwyneth's behavior

`AFK Stages [A]`, `Dream Realm [S+]`, `Dream Realm (Endless) [?]`, `PVP [S+]`

- **Signature skill**: Hailing Arrows (ultimate)
- **Movement**: stationary (avg attack range 8.0 tiles)
- **Behavior tags**: `dot-specialist` `mass-cc` `non-ult-utility`
- **Damage types**: Physical `high`, DoT `high`, Max HP-based damage `low`

#### Play overview

Gwyneth alternates **splash CC arrows** and **high-damage burn shots**, then fires both at once so every effect lands together on priority targets. Her ultimate rains arrows across range, and **empty nearby tiles** raise her attack speed while also tightening normal attack intervals when foes cannot close. Burn DoT and control stack on targets over time rather than in one burst, rewarding safe spacing throughout the fight. She peaks when **enemies cannot reach her** and she keeps casting from a protected rear tile without interruption. **Melee rush** or cleanse-heavy lines shut down her burn and CC chain before damage ramps meaningfully. Her kit relies on **sustained casting rhythm**, not a single opening burst window. Against **spread formations** her splash and rain cover too little area to justify the slot. She needs safe rear spacing to cycle both arrow types.

#### Skill overview

- **Signature skill (ult)**: speed `average`, buffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

rain arrows on enemies within range, dealing damage

##### Skill 1

fire arrow dealing splash damage and applying CC to nearby enemies

##### Skill 2

fire arrow dealing high damage and applying burn DoT to target

##### Legendary+

ATK speed grows higher when no nearby enemies present

##### Mythic+

simultaneously fire both arrows, applying all effects of each at once

##### Supreme+

no nearby enemies reduces normal attack interval further

### Units improving Gwyneth

Look for units providing: `ATK` `ATK SPD / Haste`  
Common buffers are **Ravion**, **Smokey & Meerky**, **Kazim**, or **Mikola**.

- **Ravion**
  - ATK (multiple targets, high)
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Lyca**
  - ATK SPD (all units, low) `signature fuel`
  - Energy (all units, low) `signature fuel`
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Aliceth**
  - ATK (multiple targets, average)

### Units benefitting most from Gwyneth

- Niru (4.2 / 5)
- Carolina (3.7 / 5)
- Nerion (3.2 / 5)

### Units that can act as a replacement for Gwyneth

**Similar Skills**

- Arden (60% `dot-specialist` `mass-cc`)
- Natsu (40% `dot-specialist` `mass-cc`)
- Odie (30% `dot-specialist`)

**Damage**

- Shemira (78% `Max HP-based damage`)

**Debuffs on enemies**

- Cecia (100% `Phys DEF` `Vitality`)
- Sinbad (100% `Phys DEF` `Vitality`)
- Frieren (60% `Vitality`)

**Crowd Control**

- Evie (99% `Bind` `Silence`)
- Arden (83% `Bind`)
- Cecia (83% `Bind`)

### Summary for Gwyneth

#### Damage types dealt by Gwyneth

- Physical — Area, Single target
- DoT — Single target
- Max HP-based damage — Single target — `low`

#### Debuffs provided by Gwyneth

- Vitality — Single target — `low`
- Phys DEF (Mythic+) — Single target — `low`

#### Crowd Control provided by Gwyneth

- Bind — Area — `average`
- Silence — Single target — `low`
- Stun — Area — `low`

## Hammie

### Hammie's behavior

- **Signature skill**: Pretty Fireball (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Behavior tags**: `ally-buffer` `ally-healer` `temporary-stat-buffer`
- **Damage types**: Magic `average`

#### Play overview

Hammie **heals the weakest ally** and buffs them, then sustains herself with a simple self-heal skill. Her ultimate is a **single-target fireball** for modest burst damage. She is an **early support** who keeps fragile allies alive with light healing and buffs. Her numbers stay **modest compared to top healers**, and she brings little beyond sustain. Fights that need **strong shields, damage reduction, or teamwide healing** leave her underwhelming.

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `average`
- **Non-ultimate**: speed `average`, heal `average`, buffs `average`

##### Ultimate

single-target fireball dealing damage

##### Skill 1

heal weakest ally and buff them

##### Skill 2

self-heal

### Units improving Hammie

Look for units providing: `ATK`  
Common buffers are **Ravion**, **Kazim**, **Mikola**, or **Smokey & Meerky**.

- **Ravion**
  - ATK (multiple targets, high)
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Aliceth**
  - ATK (multiple targets, average)
- **Pang**
  - ATK (multiple targets, average)

### Units benefitting most from Hammie

Hammie provides ATK to single targets `low`.

- Himmel (2.9 / 5)
- Bonnie (2.0 / 5)
- Lily May (2.0 / 5)

### Units that can act as a replacement for Hammie

**Best overall replacement**

- Fay (55% `Buffs on allies` `Similar Skills`)
- Isabella (55% `Buffs on allies` `Similar Skills`)
- Koko (55% `Buffs on allies` `Similar Skills`)

**Buffs on allies**

- Aliceth (100% `ATK`)
- Contess (100% `ATK`)
- Dunlingr (100% `ATK`)

**Similar Skills**

- Isabella (100% `ally-buffer` `ally-healer` `temporary-stat-buffer`)
- Koko (100% `ally-buffer` `ally-healer` `temporary-stat-buffer`)
- Damian (90% `ally-buffer` `ally-healer` `temporary-stat-buffer`)

**Damage**

- Alsa (100% `Magic`)
- Aurora (100% `Magic`)
- Berial (100% `Magic`)

### Summary for Hammie

#### Damage types dealt by Hammie

- Magic — Single target

#### Buffs provided by Hammie

- ATK — Single target — `low`

## Harak

### Harak's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [A+]`, `PVP [B]`

- **Signature skill**: Flesh Feast (Skill 2)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `assassin` `execute` `life-drain`
- **Damage types**: Physical `low`, HP loss `average`

#### Play overview

Harak enters an **enhanced battle-start state** that extends with assists and defeats, then devours a non-summoned unit when the state ends. He dashes to the **weakest enemy**, knocks them up, and his ultimate blocks **target HP recovery** with sustained multi-strikes. Life drain and **ATK plus max HP** grow with each takedown across the fight. Enough assists or defeats also **refund ultimate energy** for another execute window. He snowballs hardest in **chaotic multi-kill fights** where bodies feed his ramp and devour timing. **Single-target stalls** or teams that deny assists keep him from growing or force bad devour targets on allies.

#### Skill overview

- **Signature skill**: speed `fast`, buffs `average`, debuffs `average`
- **Ultimate**: speed `slow`, debuffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `low`

##### Ultimate

sustained multi-strike preventing target HP recovery

##### Skill 1

dash to weakest enemy, dealing damage and knocking them up

##### Skill 2

battle-start enhanced state extended by assists or defeats; on exit, uncontrolled devour a non-summoned unit

##### Legendary+

life drain increases with assists and defeats

##### Mythic+

gain ATK and max HP on assist or defeat

##### Supreme+

after enough assists or defeats, ultimate recovers energy on cast

### Units improving Harak

Look for units providing: `Haste` `Max HP` `CRIT` `Energy`  
Common buffers are **Twins**, **Thador**, **Smokey & Meerky**, or **Ravion**.

- **Zandrok**
  - Haste (area, average, conditional (frequent)) `signature fuel`
  - Max HP (multiple targets, low)
- **Hewynn**
  - Haste (single target, average) `signature fuel`
- **Mehira**
  - Haste (multiple targets, average) `signature fuel`
- **Shakir**
  - Haste (area, average) `signature fuel`
- **Damian**
  - Haste (multiple targets, average, conditional (frequent)) `signature fuel`
- **Isabella**
  - Haste (single target, low) `signature fuel`

### Units benefitting most from Harak

- Niru (3.7 / 5)
- Vala (1.7 / 5)
- Indris (1.5 / 5)

### Units that can act as a replacement for Harak

**Best overall replacement**

- Seth (77% `Damage` `Similar Skills`)
- Nara (75% `Damage` `Crowd Control`)
- Athalia (65% `Damage` `Crowd Control`)

**Similar Skills**

- Seth (80% `assassin` `life-drain`)
- Nara (40% `assassin` `execute`)
- Odie (30% `execute`)

**Damage**

- Himmel (100% `Physical`)
- Aliceth (100% `Physical` `HP loss`)
- Faramor (100% `Physical` `HP loss`)

**Debuffs on enemies**

- Gunnar (60% `Healing`)
- Nazrik (60% `Healing`)
- Odie (60% `Execution`)

**Crowd Control**

- Frieren (100% `Knock down`)
- Himmel (100% `Knock down`)
- Baelran (100% `Knock down`)

### Summary for Harak

#### Harak Provides

- Instant defeat — Single target
- Invincibility — Self

#### Damage types dealt by Harak

- Physical — Single target
- HP loss — Single target — `average`

#### Debuffs provided by Harak

- Execution — Single target — `low`
- Healing — Single target — `low`

#### Crowd Control provided by Harak

- Unaffected — Self — On skill
- Knock down — Single target — `low`

## Hepler

### Hepler's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Form Shift (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-healer` `ally-shielder` `high-initial-energy`
- **Ally composition**: frontmost adjacent ally gets fatal-blow protection
- **Damage types**: Physical `high`

#### Play overview

Hepler toggles between **true-form offense** and an alternate **taunt form** that heals and shields multiple allies. His ultimate consumes taunt stacks for **AoE damage and blind** on revert. Charge spending **permanently stacks DEF** and damage reduction over the fight. He can **block a fatal blow** on the frontmost ally by transforming to safety. Alternate form also carries **higher damage taken reduction** than his human stance. **Fast burst** that skips his charge cycle leaves little defensive value.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

alternate form taunt consumes stacks; revert deals AoE damage and blind

##### Skill 1

true form: single target damage and haste reduction; alternate form: AoE damage and stun

##### Skill 2

base form heal single ally; alternate form heal multiple and shield

##### Legendary+

battle damage taken reduction higher in alternate form

##### Mythic+

protect frontmost ally from fatal blow; transform to safety

##### Supreme+

charge spending permanently stacks DEF and damage reduction

### Units improving Hepler

Look for units providing: `ATK` `Haste` `Max HP` `Physical DEF` `Magic DEF`  
Common buffers are **Mikola**, **Twins**, **Ravion**, or **Kazim**.

- **Tilaya**
  - Max HP (area, high)
  - DEF (area, high)
  - DEF (area, high)
- **Niru**
  - Phys DEF (single target, high)
  - Magic DEF (single target, high)
- **Perseus**
  - ATK (multiple targets, average)
  - Phys DEF (multiple targets, low)
  - Magic DEF (multiple targets, low)
- **Isabella**
  - ATK (single target, low, conditional (frequent))
  - Haste (single target, low) `signature fuel`
  - Phys DEF (single target, low)
  - Magic DEF (single target, low)
- **Solise**
  - ATK (single target, low)
  - DEF (single target, low)
  - DEF (single target, low)
- **Aliceth**
  - ATK (multiple targets, average)

### Units benefitting most from Hepler

Hepler provides Healing over time to single targets `high` and Invincible (Mythic+) to single targets `high`.

- Carolina (5.0 / 5)
- Nerion (4.4 / 5)

### Units that can act as a replacement for Hepler

**Buffs on allies**

- Gunnar (100% `Invincible`)
- Pandora (62% `Invincible`)

**Healing**

- Smokey & Meerky (100% `Healing over time` `Healing`)
- Hewynn (100% `Healing over time` `Healing`)
- Solise (76% `Healing over time` `Healing`)

**Similar Skills**

- Lucca (60% `ally-shielder` `high-initial-energy`)
- Solise (50% `ally-healer` `ally-shielder`)
- Saida (50% `ally-shielder` `high-initial-energy`)

**Damage**

- Gwyneth (100% `Physical`)
- Baelran (100% `Physical`)
- Alna (100% `Physical`)

**Debuffs on enemies**

- Alna (100% `Haste`)
- Galahad (100% `Haste`)
- Velara (100% `Haste`)

### Summary for Hepler

#### Hepler Provides

- Invincibility (Mythic+) — Single target

#### Damage types dealt by Hepler

- Physical — Area

#### Buffs provided by Hepler

- Healing over time — Single target — `high`
- Invincible (Mythic+) — Single target — `high`

#### Debuffs provided by Hepler

- Haste — Single target — `high`

#### Crowd Control provided by Hepler

- Blind — Area — `high`
- Stun — Area — `average`
- Taunt — Area — `high`

## Hewynn

### Hewynn's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Rain Prayer (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-healer` `aoe-healing` `temporary-stat-buffer`
- **Damage types**: Magic `low`

#### Play overview

Hewynn sustains allies with **single-target heals** and a cleanse that strips dispellable debuffs from multiple friends. Her ultimate delivers **AoE heal over time** while she stays unaffected and all allies gain **damage reduction** during the channel. Battle ATK rises after her **first ultimate**, and cleansed allies receive a **haste boost** for quicker rotations through the rest of the fight. She is a reliable healer when stronger options are unavailable on the roster. Output is **modest next to top supports** and she offers little beyond healing. Fights needing **shields or hard mitigation** rather than steady regeneration underuse her kit.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, heal `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`

##### Ultimate

sustained AoE heal over time for all allies

##### Skill 1

heal a single ally

##### Skill 2

heal allies, cleansing dispellable debuffs

##### Legendary+

ATK scales after first ultimate cast

##### Mythic+

unaffected during ultimate; all allies reduce damage taken

##### Supreme+

haste boost for ally when cleansed

### Units improving Hewynn

Look for units providing: `ATK`  
Common buffers are **Ravion**, **Kazim**, **Mikola**, or **Smokey & Meerky**.

- **Ravion**
  - ATK (multiple targets, high)
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Aliceth**
  - ATK (multiple targets, average)
- **Pang**
  - ATK (multiple targets, average)

### Units benefitting most from Hewynn

Hewynn provides Direct healing to single targets `high`, Healing over time to all units `high`, Damage taken (Mythic+) to all units `low`, and Haste (Supreme+) to single targets `average`.

**13** units include this provider among their top 6 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight

These are the **4** strongest pairings: 

- Lumont (3.5 / 5)
- Mehira (3.5 / 5)
- Dunlingr (3.4 / 5)
- Lamentis (2.4 / 5)

### Units that can act as a replacement for Hewynn

**Best overall replacement**

- Smokey & Meerky (71% `Healing` `Similar Skills`)

**Buffs on allies**

- Shakir (100% `Damage taken` `Haste`)
- Hugin (75% `Haste` `Damage taken`)
- Damian (68% `Haste`)

**Healing**

- Solise (100% `Direct healing` `Healing over time` `Healing`)
- Smokey & Meerky (100% `Healing over time` `Direct healing` `Healing`)

**Similar Skills**

- Velara (100% `ally-healer` `aoe-healing` `temporary-stat-buffer`)
- Smokey & Meerky (100% `ally-healer` `aoe-healing` `temporary-stat-buffer`)
- Fay (100% `ally-healer` `aoe-healing` `temporary-stat-buffer`)

### Summary for Hewynn

#### Buffs provided by Hewynn

- Direct healing — Single target — `high`
- Healing over time — All units — `high`
- Damage taken (Mythic+) — All units — `low`
- Haste (Supreme+) — Single target — `average`

#### Crowd Control provided by Hewynn

- Unaffected (Mythic+) — Self — On skill

## Himmel

### Himmel's behavior

`AFK Stages [S]`, `Dream Realm [S+]`, `Dream Realm (Endless) [A+]`, `PVP [A+]`

- **Signature skill**: Hero Party (Skill 2)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-buffer` `aoe-damage` `self-repositioner`
- **Ally composition**: place Mage, Tank, and Support within 1 tile at battle start (Hero Party)
- **Damage types**: Physical `high`

#### Play overview

Himmel opens with a **battle-start formation** beside allies, granting petals that bless everyone on the field with sustained bonuses. He dashes to two high-damage foes, knocks them down, then slashes in a **repeated frontal ultimate** with a massive finishing sweep across the line. Formation strikes add **extra HP-loss on boss targets**, and battle haste keeps his rotation brisk through long fights. He pairs strongly with **Frieren adjacent** so she skips her ramp wait and shares ATK from his stats for the whole fight. He offers **soft buffs and line pressure**, not standalone carry damage or hard mitigation. **Spread lines** or burst that ends before formation and petal value builds waste his setup entirely. Without **adjacent allies** in formation, his petals and HP-loss bonuses contribute far less to the team.

#### Skill overview

- **Signature skill**: speed `slow`, first cast speed `fast`, buffs `average`, damage `average`
- **Ultimate**: speed `fast`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `high`

##### Ultimate

repeated frontal slashes finishing with a massive sweep

##### Skill 1

dash to two enemies, striking and knocking them down

##### Skill 2

Passive: battle-start formation with allies; Active: deal damage to frontal enemies

##### Legendary+

battle haste increase

##### Mythic+

battle-start petals grant blessings to battlefield allies

##### Supreme+

formation deals extra HP-loss on boss targets

### Units improving Himmel

Look for units providing: `ATK` `Haste` `Max HP`  
Common buffers are **Twins**, **Mikola**, **Smokey & Meerky**, or **Contess**.

Himmel also requires a party **with the right composition** and/or specific **named allies**

- **Twins**
  - ATK (multiple targets, average)
  - Haste (all units, average) `signature fuel`
  - Max HP (multiple targets, average)
  - Enables Party composition via Support (party slot)
- **Mikola**
  - ATK (all units, high)
  - Haste (multiple targets, average) `signature fuel`
  - Enables Party composition via Support (party slot)
- **Frieren**
  - Enables Party composition via Mage (party slot)
  - Enables Named ally on team via Frieren named in skill text
- **Smokey & Meerky**
  - ATK (area, average)
  - Haste (area, high) `signature fuel`
  - Enables Party composition via Support (party slot)
- **Contess**
  - ATK (single target, high)
  - Enables Party composition via Support (party slot)
- **Evie**
  - ATK (single target, high)
  - Enables Party composition via Support (party slot)

### Units benefitting most from Himmel

Himmel provides Basic stats to single targets `low`.

- Niru (5.0 / 5)
- Frieren (3.2 / 5)

### Units that can act as a replacement for Himmel

**Buffs on allies**

- Alna (100% `Basic stats`)
- Velara (100% `Basic stats`)

**Similar Skills**

- Dionel (50% `aoe-damage` `self-repositioner`)
- Perseus (50% `ally-buffer` `aoe-damage`)
- Frieren (48% `aoe-damage` `self-repositioner`)

**Damage**

- Faramor (81% `Physical`)
- Athalia (81% `Physical`)
- Gwyneth (67% `Physical`)

**Debuffs on enemies**

- Mehira (100% `Damage taken`)
- Kulu (100% `Damage taken`)
- Cryonaia (100% `Damage taken`)

**Crowd Control**

- Frieren (100% `Knock down`)
- Baelran (100% `Knock down`)
- Silven (100% `Knock down`)

### Summary for Himmel

#### Himmel Provides

- Named ally on team (Mythic+) — Allies

#### Damage types dealt by Himmel

- Physical — All units, Multiple targets, Single target
- HP loss — Single target
- Max HP-based damage — All units

#### Buffs provided by Himmel

- Basic stats — Single target — `low`

#### Debuffs provided by Himmel

- Damage taken (Supreme+) — Single target — `low`

#### Crowd Control provided by Himmel

- Knock down — Multiple targets — `low`

## Hodgkin

### Hodgkin's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Cannon Fire (ultimate)
- **Movement**: moving (avg attack range 3.0 tiles)
- **Behavior tags**: `aoe-damage` `enemy-debuffer` `summoner`
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Play overview

Hodgkin phases **physically immune** with sustained regeneration, then fires cannons for **AoE damage** while ATK climbs during intangibility. Arc strikes **steal enemy energy**, and defeated minions **explode for AoE** while draining more energy from nearby foes. Cannon hits also **shave Phys DEF** on targets, softening them for follow-up physical damage from allies. Summoned bodies give him **extra detonation points** across the field when they fall in clusters. During intangible phase his ATK climbs higher, making cannon windows the main damage spike. He shines when enemies bunch for cannon fire and minion pops chain together. **Magic damage** or teams that kill minions before they explode blunt his energy drain and DEF shred loop.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, debuffs `average`, damage `average`

##### Ultimate

fire cannons dealing AoE damage to enemies

##### Skill 1

intangible phase grants physical immunity with sustained HP regeneration

##### Skill 2

arc damage stealing enemy energy

##### Legendary+

ATK grows higher during intangible phase

##### Mythic+

summon minions; on defeat, they deal AoE damage and reduce enemy energy

##### Supreme+

cannon hits reduce target Phys DEF

### Units improving Hodgkin

Look for units providing: `ATK` `Energy`  
Common buffers are **Ravion**, **Pandora**, **Contess**, or **Evie**.

- **Aurora**
  - Haste (all summons, high)
  - Damage dealt via Damage dealt (all summons, average)
  - Damage taken via Damage taken (all summons, low)
- **Peggy**
  - ATK (all summons, high)
  - DEF via DEF (all summons, high)
- **Ravion**
  - ATK (multiple targets, high)
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`

### Units benefitting most from Hodgkin

- Niru (4.2 / 5)
- Vala (1.9 / 5)
- Indris (1.8 / 5)

### Units that can act as a replacement for Hodgkin

**Similar Skills**

- Florabelle (66% `aoe-damage` `summoner`)
- Cassadee (60% `aoe-damage` `enemy-debuffer`)
- Cecia (60% `enemy-debuffer` `summoner`)

**Damage**

- Himmel (100% `Physical`)
- Brutus (100% `Physical` `Max HP-based damage`)
- Valka (100% `Physical`)

**Debuffs on enemies**

- Saida (100% `Energy`)
- Lily May (100% `Energy`)
- Silvina (100% `Energy` `Vitality`)

### Summary for Hodgkin

#### Hodgkin Provides

- Summoning (Mythic+) — Single target
- Stacking (Supreme+) — Single target

#### Damage types dealt by Hodgkin

- Physical — Arc, Area
- Max HP-based damage — Area — `high`

#### Debuffs provided by Hodgkin

- Energy — Arc — `low`
- Energy (Mythic+) — Single target — `high`
- Phys DEF (Supreme+) — Single target — `low`
- Vitality (Supreme+) — Single target — `low`

## Hugin

### Hugin's behavior

`AFK Stages [S+]`, `Dream Realm [A+]`, `Dream Realm (Endless) [S]`, `PVP [A]`

- **Signature skill**: Mechanized Bond (Skill 2)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-shielder` `energy-provider` `high-initial-energy` `static-tile-buffer` `temporary-stat-buffer`
- **Self placement**: stays anchored to battle-prep tile; returns after displacement
- **Ally composition**: put one ally 1 tile behind him (ATK bonus; buff ends if they leave the sigil)
- **Damage types**: Physical `low`

#### Play overview

Hugin shields the **weakest ally** with large barriers, then boosts the **highest cumulative damage dealer's ATK and Haste** on ultimate. The ally directly behind gains **ATK**, and recovers energy whenever he shields anyone on the field. Shielded allies also **reduce damage taken**, and his ultimate adds shields to weak targets alongside the buff. He is a **strong buffer for a rear carry** positioned behind him on the board. Value drops when the **rear partner dies** or when no ally clearly leads damage dealt. He adds **little personal damage** if buff targets are misaligned or the top dealer changes mid-fight.

#### Skill overview

- **Signature skill**: speed `fast`, buffs `average`
- **Ultimate**: speed `slow`, first cast speed `fast`, buffs `average`
- **Non-ultimate**: speed `fast`, buffs `average`

##### Ultimate

boost ATK and Haste of the ally with highest cumulative damage

##### Skill 1

large shield granted to weakest ally

##### Skill 2

boost ATK of ally directly behind; that ally recovers energy when caster shields

##### Legendary+

battle haste increase

##### Mythic+

ultimate also grants shields to weakest allies

##### Supreme+

shielded allies reduce their damage taken

### Units improving Hugin

Look for units providing: `Haste` `Energy`  
Common buffers are **Smokey & Meerky**, **Ravion**, **Lorsan**, or **Twins**.

- **Hewynn**
  - Haste (single target, average) `signature fuel`
- **Mehira**
  - Haste (multiple targets, average) `signature fuel`
- **Damian**
  - Haste (multiple targets, average, conditional (frequent)) `signature fuel`
- **Zandrok**
  - Haste (area, average, conditional (frequent)) `signature fuel`
- **Isabella**
  - Haste (single target, low) `signature fuel`

### Units benefitting most from Hugin

Hugin provides ATK to multiple targets `low`, Energy to single targets `average` — conditional (frequent), Haste to multiple targets `high`, Shield to multiple targets `high`, and Damage taken (Supreme+) to single targets `low`.

**28** units include this provider among their top 6 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight
- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner

These are the **4** strongest pairings: 

- Koko (5.0 / 5)
- Alsa (4.0 / 5)
- Bryon (3.6 / 5)
- Silven (3.2 / 5)

### Units that can act as a replacement for Hugin

**Buffs on allies**

- Saida (86% `Shield`)
- Thador (54% `Shield` `Energy`)

**Similar Skills**

- Pang (60% `ally-shielder` `high-initial-energy` `temporary-stat-buffer`)
- Twins (51% `ally-shielder` `energy-provider` `temporary-stat-buffer`)
- Gunnar (50% `ally-shielder` `static-tile-buffer` `temporary-stat-buffer`)

### Summary for Hugin

#### Buffs provided by Hugin

- ATK — Multiple targets — `low`
- Energy — Single target — `average` — conditional (frequent)
- Haste — Multiple targets — `high`
- Shield — Multiple targets — `high`
- Damage taken (Supreme+) — Single target — `low`

## Igor

### Igor's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Funereal Ring (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `aoe-damage` `cheat-death` `life-drain` `self-repositioner` `untargetable`
- **Damage types**: Physical `high`

#### Play overview

Igor places **battle-start markers** and leaps to them for **AoE explosions**, with an extra marker from his opening ultimate cast. Fatal blows trigger a **dodge leap** with HP recovery, and life drain rises after the first dodge proc. High HP ratio **widens explosion range**, letting him kite through danger while staying aggressive. His ultimate hits **all enemies** once markers are spent in sequence. He excels as a **mobile opener** that survives focus fire through repositioning. **Immobilize or marker denial** before he leaps leaves him exposed with modest sustained output.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `average`
- **Non-ultimate**: speed `fast`, heal `average`, debuffs `average`, damage `high`

##### Ultimate

deal damage to all enemies

##### Skill 1

leap to an active marker, dealing area damage, then deactivate it

##### Skill 2

dodge fatal blows by leaping to markers with HP recovery

##### Legendary+

life drain elevated after first fatal blow dodge trigger

##### Mythic+

extend leap-explosion range when HP ratio is high

##### Supreme+

battle-start ultimate summons an extra marker

### Units improving Igor

- **Pandora**
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Ravion**
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Phraesto**
  - Energy via Energy recovery speed (contract ally, start of battle) `signature fuel`
- **Lyca**
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`

### Units benefitting most from Igor

- Niru (5.0 / 5)
- Vala (2.1 / 5)
- Indris (1.3 / 5)

### Units that can act as a replacement for Igor

**Similar Skills**

- Dionel (60% `aoe-damage` `self-repositioner` `untargetable`)
- Tasi (60% `aoe-damage` `cheat-death` `self-repositioner`)
- Mehira (45% `aoe-damage` `life-drain` `untargetable`)

**Damage**

- Gwyneth (100% `Physical`)
- Athalia (100% `Physical`)
- Kulu (100% `Physical`)

**Debuffs on enemies**

- Gunnar (100% `Healing`)
- Nazrik (100% `Healing`)
- Niru (100% `Healing`)

### Summary for Igor

#### Damage types dealt by Igor

- Physical — All units, Area

#### Debuffs provided by Igor

- Healing (Mythic+) — Single target — `low`

## Indris

### Indris's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Spellbane Shot (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `enemy-debuffer` `interrupt`
- **Damage types**: Physical `low`, Max HP-based damage `low`, True damage `low`

#### Play overview

Indris opens **exposed weakness** windows with penetrating normal attacks that add **true damage** on marked foes. She pushes back close enemies, immobilizes the nearest, then fires a **silencing arrow** that blocks stat gains and permanently cuts DEF. ATK and **attack speed spike** whenever weakness bonuses trigger during the fight. Immobilize also grants a **no-cooldown weakness window** for rapid follow-up on chained targets. She dismantles **buff-reliant carries** over sustained engagements where DEF shred compounds. **Silence-immune or ungrouped targets** deny her DEF shred and speed ramp before she snowballs. Penetrating attacks prioritize multiple foes, but isolated single targets take less bonus from her weakness triggers.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, debuffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `low`

##### Ultimate

fire silencing arrow, preventing stat gains and permanently reducing target DEF

##### Skill 1

three-hit penetrating normal attack; extra true damage on exposed

##### Skill 2

push back all close enemies then immobilize nearest

##### Legendary+

ATK grows while an enemy has exposed weakness

##### Mythic+

ATK speed burst each time exposed weakness bonus triggers

##### Supreme+

immobilize opens a window with no-cooldown weakness trigger

### Units improving Indris

Look for units providing: `ATK` `ATK SPD / Haste`  
Common buffers are **Dunlingr**, **Evie**, **Contess**, or **Ravion**.

Indris also requires units **putting multiple debuffs** on enemies

- **Dunlingr**
  - ATK (single target, low)
  - ATK SPD via Haste (single target, average) `signature fuel`
  - Enables Multiple debuffs on target via 3 debuff types
- **Evie**
  - ATK (single target, high)
  - Enables Multiple debuffs on target via 3 debuff types
- **Sinbad**
  - Enables Multiple debuffs on target via 7 debuff types
- **Velara**
  - Enables Multiple debuffs on target via 4 debuff types
- **Contess**
  - ATK (single target, high)
  - Enables Multiple debuffs on target via 4 debuff types
- **Ravion**
  - ATK (multiple targets, high)
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
  - Enables Multiple debuffs on target via 2 debuff types

### Units benefitting most from Indris

- Carolina (2.5 / 5)
- Nerion (2.3 / 5)

### Units that can act as a replacement for Indris

**Best overall replacement**

- Korin (53% `Damage` `Crowd Control`)
- Pippa (50% `Damage` `Crowd Control`)

**Similar Skills**

- Temesia (40% `enemy-debuffer` `interrupt`)
- Salazer (40% `interrupt`)
- Shadewing (33% `enemy-debuffer`)

**Damage**

- Nara (100% `Physical` `True damage` `Max HP-based damage`)
- Korin (98% `Physical` `True damage` `Max HP-based damage`)
- Pippa (94% `True damage`)

**Debuffs on enemies**

- Thador (100% `Magic DEF` `Phys DEF`)
- Velara (100% `Magic DEF` `Phys DEF`)
- Laios (100% `Magic DEF` `Phys DEF`)

**Crowd Control**

- Kordan (100% `Bind` `Knock back`)
- Korin (100% `Bind` `Knock back`)
- Arden (93% `Bind`)

### Summary for Indris

#### Damage types dealt by Indris

- Physical — Single target
- Max HP-based damage — Single target — `low`
- True damage — Single target — `average`

#### Debuffs provided by Indris

- Magic DEF — Single target — `low`
- Phys DEF — Single target — `average`

#### Crowd Control provided by Indris

- Bind — Single target — `high`
- Knock back — Area — `low`

## Isabella

### Isabella's behavior

`AFK Stages [C]`, `Dream Realm [B]`, `Dream Realm (Endless) [A+]`, `PVP [C]`

- **Signature skill**: Grimoire Pact (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-buffer` `ally-healer` `temporary-stat-buffer`
- **Ally composition**: frontmost ally becomes companion (stat stacks and ult buffs)
- **Damage types**: Magic `low`

#### Play overview

Isabella bonds the **frontmost ally as companion**, buffing them heavily whenever she casts ultimate on that partner. She heals the companion while **damaging adjacent foes**, and makes them **unaffected after control** when they take a disabling hit. Companion damage taken **cuts attacker ATK**, and large buffs add **extra debuff stacks** on enemies during ultimate. Battle assistance stat growth rewards long support play beside a durable frontliner. She needs a **tanky front partner** to justify the bond and survive her setup phase. If the companion **dies early**, her healing and buff package collapses quickly. Her ultimate also debuffs an enemy hero on cast when buff stacks are large enough to add soft control.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, buffs `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`

##### Ultimate

select frontmost ally as companion, granting them powerful buffs on ultimate cast

##### Skill 1

heal companion and deal damage to adjacent foes

##### Skill 2

make companion unaffected after control; reduce attacker ATK when companion takes damage

##### Legendary+

battle assistance stat increase

##### Mythic+

debuff an enemy hero when casting ultimate

##### Supreme+

large enough buff grants extra debuff stack

### Units improving Isabella

Look for units providing: `ATK` `ATK SPD / Haste` `Energy`  
Common buffers are **Ravion**, **Smokey & Meerky**, **Mikola**, or **Kazim**.

- **Ravion**
  - ATK (multiple targets, high)
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Lyca**
  - ATK SPD (all units, low) `signature fuel`
  - Energy (all units, low) `signature fuel`
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`
- **Aliceth**
  - ATK (multiple targets, average)

### Units benefitting most from Isabella

Isabella provides ATK to single targets `low` — conditional (frequent), ATK SPD to single targets `low`, Direct healing to single targets `high`, Haste to single targets `low`, Magic DEF to single targets `low`, Phys DEF to single targets `low`, and Vitality to single targets `low`.

**11** units include this provider among their top 6 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **4** strongest pairings: 

- Lily May (5.0 / 5)
- Silven (5.0 / 5)
- Perseus (4.6 / 5)
- Dionel (4.6 / 5)

### Units that can act as a replacement for Isabella

**Best overall replacement**

- Smokey & Meerky (58% `Healing` `Similar Skills`)
- Fay (57% `Healing` `Similar Skills`)
- Twins (55% `Buffs on allies` `Similar Skills`)

**Buffs on allies**

- Twins (99% `ATK` `Haste` `Magic DEF` `Physical DEF` `Vitality`)
- Mikola (79% `ATK` `Haste` `Magic DEF` `Vitality`)
- Dunlingr (50% `ATK` `ATK SPD` `Haste`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Evie (100% `Direct healing` `Healing`)

**Similar Skills**

- Koko (100% `ally-buffer` `ally-healer` `temporary-stat-buffer`)
- Damian (90% `ally-buffer` `ally-healer` `temporary-stat-buffer`)
- Twins (72% `ally-buffer` `ally-healer` `temporary-stat-buffer`)

**Debuffs on enemies**

- Sinbad (83% `ATK` `ATK SPD` `Magic DEF` `Phys DEF` `Vitality`)
- Velara (60% `Haste` `Magic DEF` `Phys DEF`)
- Pandora (60% `ATK` `Haste` `Vitality`)

### Summary for Isabella

#### Damage types dealt by Isabella

- Magic — Area

#### Buffs provided by Isabella

- ATK — Single target — `low` — conditional (frequent)
- ATK SPD — Single target — `low`
- Direct healing — Single target — `high`
- Haste — Single target — `low`
- Magic DEF — Single target — `low`
- Phys DEF — Single target — `low`
- Vitality — Single target — `low`

#### Debuffs provided by Isabella

- ATK — Single target — `low`
- ATK SPD (Mythic+) — Single target — `low`
- Haste (Mythic+) — Single target — `low`
- Magic DEF (Mythic+) — Single target — `low`
- Phys DEF (Mythic+) — Single target — `low`
- Vitality (Mythic+) — Single target — `low`

#### Crowd Control provided by Isabella

- Unaffected — Single target — Conditional

## Kafra

### Kafra's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Gale Thrust (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `assassin` `enemy-debuffer` `mark-target` `non-ult-utility` `self-repositioner`
- **Damage types**: Physical `high`

#### Play overview

Kafra marks an enemy, then **charges out-of-range targets** to stun them on approach for a reliable pick. Marks **shave Phys DEF**, and defeating a marked foe grants **self buffs** that keep his momentum going through the fight. His ultimate knocks back and reapplies the mark, while he **interrupts heals** on anyone treating the marked target. First battle charge greatly **boosts damage** for an opening assassination window against backliners. He excels at **hunting marked targets** in melee-heavy teams that can follow his picks. **Immune or heavily shielded marks** waste his charge, and spread lines deny follow-up kills on secondary targets. In melee-oriented teams with frequent picks, his mark-and-charge loop sustains pressure and can match support healing when marked foes die near grouped allies.

#### Skill overview

- **Signature skill (ult)**: speed `average`, debuffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, debuffs `average`, damage `high`

##### Ultimate

knock back an enemy and apply mark

##### Skill 1

charge out-of-range marked enemy, stunning them

##### Skill 2

mark reduces enemy Phys DEF; defeating marked enemy grants self buffs

##### Legendary+

battle ATK increase

##### Mythic+

interrupt enemies healing the marked target

##### Supreme+

first battle charge greatly boosts damage

### Units improving Kafra

Look for units providing: `ATK` `Shield`  
Common buffers are **Ravion**, **Kazim**, **Mikola**, or **Smokey & Meerky**.

- **Ravion**
  - ATK (multiple targets, high)
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Aliceth**
  - ATK (multiple targets, average)
- **Pang**
  - ATK (multiple targets, average)

### Units benefitting most from Kafra

- Carolina (2.0 / 5)
- Nerion (1.8 / 5)
- Indris (1.8 / 5)

### Units that can act as a replacement for Kafra

**Similar Skills**

- Sinbad (72% `assassin` `enemy-debuffer` `mark-target`)
- Lenya (40% `assassin` `self-repositioner`)
- Bonnie (34% `enemy-debuffer` `non-ult-utility`)

**Damage**

- Gwyneth (100% `Physical`)
- Baelran (100% `Physical`)
- Alna (100% `Physical`)

**Debuffs on enemies**

- Eironn (97% `Haste`)
- Lorsan (97% `Haste`)
- Bonnie (81% `Haste`)

**Crowd Control**

- Aliceth (100% `Stun` `Knock back`)
- Perseus (100% `Stun` `Knock back`)
- Scarlita (100% `Stun` `Knock back`)

### Summary for Kafra

#### Kafra Provides

- Marked target (focus fire) — Single target
- Marked target (focus fire) — Area

#### Damage types dealt by Kafra

- Physical — Single target

#### Debuffs provided by Kafra

- Marked target (focus fire) — Single target — `average`
- Phys DEF — Single target — `average`
- Haste (Mythic+) — Single target — `low`

#### Crowd Control provided by Kafra

- Unaffected (Mythic+) — Self — On skill
- Knock back — Single target — `low`
- Stun — Single target — `average`

## Kazim

### Kazim's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Soaring Falcon (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-buffer` `aoe-damage` `battle-start-burst` `high-initial-energy` `invincibility` `mark-target` `mass-cc` `non-ult-utility` `temporary-stat-buffer`
- **Damage types**: Physical `high`, Max HP-based damage `average`

#### Play overview

Kazim opens **invincible in Soaring**, diving at airborne enemies to **mark prey** and stunning them after he lands. His ultimate chains **arc knock-ups** into sustained volleys that scale with attack speed. Marked prey takes **bonus normal-attack damage** and periodic max-HP true damage with knock-up. Allies in his zone gain **haste stacks from prey marks**, which he can absorb doubled after his aerial phase. He shines when **enemies can be kept airborne or marked** for follow-up focus. Fights with **grounded, spread, or knock-up-immune targets** deny his mark loop and aerial payoff.

#### Skill overview

- **Signature skill**: speed `fast`, buffs `average`, debuffs `average`, damage `average`
- **Ultimate**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

Passive: extend knock up and fire tracking shots; Active: arc AoE knock up, then sustained volleys scaling with ATK SPD

##### Skill 1

Passive: battle-start Soaring (invincible); dives at airborne enemies to mark prey; stuns marked prey after landing

##### Skill 2

Passive: zone ally haste stacks on prey marks; self absorbs doubled haste after aerial phase; Active: line AoE knock up

##### Legendary+

battle ATK SPD increase

##### Mythic+

normal attacks bonus damage on marked prey; periodic max HP-based true damage with knock up

##### Supreme+

knock up stationary rearmost enemy after aerial start; ATK SPD and Energy on prey marks or defeats

### Units improving Kazim

Look for units providing: `ATK SPD / Haste` `Energy`  
Common buffers are **Smokey & Meerky**, **Ravion**, **Lorsan**, or **Twins**.

Kazim also requires units **providing knock up**

- **Zandrok**
  - ATK SPD via Haste (area, average, conditional (frequent)) `signature fuel`
  - Enables Knock up from allies via Knock up + early battle (area)
- **Florabelle**
  - Enables Knock up from allies via Knock up + wide area (area)
- **Nerion**
  - Enables Knock up from allies via Knock up + wide area (area)
- **Ulmus**
  - Enables Knock up from allies via Knock up + wide area (area)
- **Lucca**
  - Enables Knock up from allies via Knock up (area)
- **Scarlita**
  - Enables Knock up from allies via Knock up (area)

### Units benefitting most from Kazim

Kazim provides Haste to multiple targets `average` and ATK (Mythic+) to single targets `high`.

**66** units include this provider among their top 6 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **4** strongest pairings: 

- Vala (4.1 / 5)
- Alsa (4.1 / 5)
- Nerion (4.1 / 5)
- Dionel (3.6 / 5)

### Units that can act as a replacement for Kazim

**Best overall replacement**

- Zandrok (52% `Crowd Control` `Damage` `Buffs on allies`)

**Buffs on allies**

- Twins (100% `Haste` `ATK`)
- Ravion (100% `Haste` `ATK`)
- Smokey & Meerky (100% `Haste` `ATK`)

**Similar Skills**

- Walker (66% `aoe-damage` `battle-start-burst` `mark-target` `mass-cc` `non-ult-utility`)
- Parisa (53% `ally-buffer` `aoe-damage` `mark-target` `temporary-stat-buffer`)
- Alna (40% `ally-buffer` `aoe-damage` `invincibility` `temporary-stat-buffer`)

**Damage**

- Valka (100% `Physical`)
- Nara (100% `Physical` `Max HP-based damage`)
- Hodgkin (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Aliceth (100% `Marked target (focus fire)`)
- Vala (100% `Marked target (focus fire)`)
- Kafra (100% `Marked target (focus fire)`)

**Crowd Control**

- Zandrok (100% `Stun` `Knock up`)
- Scarlita (100% `Stun` `Knock up`)
- Lucca (100% `Stun` `Knock up`)

### Summary for Kazim

#### Kazim Provides

- Invincibility — Self
- Stacking — Multiple targets
- Stacking — Single target

#### Damage types dealt by Kazim

- Physical — Area, Single target
- Max HP-based damage — Single target — `average`

#### Buffs provided by Kazim

- Haste — Multiple targets — `average`
- ATK (Mythic+) — Single target — `high`

#### Debuffs provided by Kazim

- Marked target (focus fire) — Single target — `average`

#### Crowd Control provided by Kazim

- Knock up — Area — `low`
- Stun — Single target — `average`
- Knock up (EX+10) — Single target — `low`

## Koko

### Koko's behavior

`AFK Stages [A]`, `Dream Realm [B]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Full Energy (ultimate)
- **Movement**: mostly stationary (avg attack range 4.0 tiles)
- **Behavior tags**: `ally-buffer` `ally-healer` `temporary-stat-buffer`
- **Damage types**: Physical `average`

#### Play overview

Koko feeds allies or herself to **recover HP and raise stats**, then inspires everyone with **damage reduction and buffs** on ultimate. Her strike skill deals heavy damage with debuffs, and fed allies gain a **temporary vitality boost** after each meal. Ultimate also grants her an **extra shield**, and battle haste keeps casts flowing. She blends **healing, buffing, and soft offense** in one slot. Healing is **modest compared to top supports**. Fights that **burst her before ultimate** see little team-wide value. She needs fight length for her ultimate to matter.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, buffs `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

inspire all allies with damage reduction and stat buffs

##### Skill 1

feed an ally or herself, recovering HP and increasing stats

##### Skill 2

deal high damage and apply debuffs to enemy

##### Legendary+

battle haste increase

##### Mythic+

gain extra shield when casting ultimate

##### Supreme+

ally fed by heal gains temporary vitality boost

### Units improving Koko

Look for units providing: `Haste` `Shield` `Resilience` `Energy`  
Common buffers are **Ravion**, **Hugin**, **Smokey & Meerky**, or **Lorsan**.

- **Ravion**
  - Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Hewynn**
  - Haste (single target, average) `signature fuel`
  - ATK SPD via Haste (single target, average) `signature fuel`
- **Mehira**
  - Haste (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`

### Units benefitting most from Koko

Koko provides ATK to all units `low`, Damage taken to all units `low`, Direct healing to single targets `high`, Lifedrain to multiple targets `average`, Shield (Mythic+) to all units `low`, and Vitality (Supreme+) to single targets `high`.

- Carolina (3.7 / 5)
- Nerion (3.6 / 5)
- Lily May (2.6 / 5)

### Units that can act as a replacement for Koko

**Best overall replacement**

- Mikola (78% `Healing` `Buffs on allies` `Similar Skills`)
- Damian (62% `Healing` `Similar Skills` `Crowd Control`)
- Smokey & Meerky (58% `Healing` `Similar Skills`)

**Buffs on allies**

- Mikola (74% `Vitality` `ATK`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Twins (100% `Direct healing` `Healing`)

**Similar Skills**

- Isabella (100% `ally-buffer` `ally-healer` `temporary-stat-buffer`)
- Damian (90% `ally-buffer` `ally-healer` `temporary-stat-buffer`)
- Twins (72% `ally-buffer` `ally-healer` `temporary-stat-buffer`)

**Damage**

- Gunnar (100% `Physical`)
- Gwyneth (100% `Physical`)
- Himmel (100% `Physical`)

**Debuffs on enemies**

- Himmel (100% `Damage taken`)
- Mehira (100% `Damage taken`)
- Kulu (100% `Damage taken`)

**Crowd Control**

- Hepler (100% `Stun`)
- Scarlita (100% `Stun`)
- Lorsan (100% `Stun`)

### Summary for Koko

#### Koko Provides

- Dispel debuffs (EX+10) — All units

#### Damage types dealt by Koko

- Physical — Area

#### Buffs provided by Koko

- ATK — All units — `low`
- Damage taken — All units — `low`
- Direct healing — Single target — `high`
- Lifedrain — Multiple targets — `average`
- Shield (Mythic+) — All units — `low`
- Vitality (Supreme+) — Single target — `high`

#### Debuffs provided by Koko

- Damage taken — Single target — `low`

#### Crowd Control provided by Koko

- Stun — Area — `average`

## Kordan

### Kordan's behavior

`AFK Stages [A]`, `Dream Realm [A]`, `Dream Realm (Endless) [S]`, `PVP [A]`

- **Signature skill**: Dominance Ring (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-buffer` `high-initial-energy` `hp-scaling` `self-repositioner` `temporary-stat-buffer`
- **Damage types**: Physical `high`

#### Play overview

Kordan drops a **hunting zone** that cuts damage taken and outside healing while allies inside gain **ATK and life drain**. His slash grants a **proportional self-shield**, and knockdown strikes add direct pressure on isolated targets. First takedown inside the circle **permanently enhances skills**, and further kills **reposition the zone** to chase new prey across the field. He wants **melee allies** fighting inside his ring for the full buff package. His circle denies outside healing to enemies beyond the ring when the zone stays active. **Enemies that never enter the zone** or burst that ends before enhancements trigger waste his setup entirely. Ranged foes outside the circle avoid his damage reduction and healing denial. He needs committed melee allies inside the ring for the full payoff.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, first cast speed `fast`, buffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `high`

##### Ultimate

hunting zone reduces damage taken and outside healing; allies inside gain ATK and life drain

##### Skill 1

powerful slash with proportional self-shield

##### Skill 2

knock down an enemy, dealing damage

##### Legendary+

battle ATK increase

##### Mythic+

first assist or defeat inside hunting circle permanently enhances skills

##### Supreme+

assist or defeat inside zone repositions caster and circle to new target

### Units improving Kordan

Look for units providing: `ATK` `Shield` `DEF Penetration` `Physical DEF` `Magic DEF`  
Common buffers are **Mikola**, **Ravion**, **Rowan**, or **Twins**.

- **Ravion**
  - ATK (multiple targets, high)
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Rowan**
  - Phys DEF (single target, average)
  - Magic DEF (single target, average)
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Aliceth**
  - ATK (multiple targets, average)
  - DEF Penetration (multiple targets, high)
- **Niru**
  - Phys DEF (single target, high)
  - Magic DEF (single target, high)
- **Tilaya**
  - DEF (area, high)
  - DEF (area, high)
- **Perseus**
  - ATK (multiple targets, average)
  - Phys DEF (multiple targets, low)
  - Magic DEF (multiple targets, low)

### Units benefitting most from Kordan

Kordan provides ATK in an area `low`, Lifedrain in an area `average`, and DEF Penetration (Supreme+) in an area `high`.

- Lily May (3.3 / 5)
- Silven (2.8 / 5)

### Units that can act as a replacement for Kordan

**Buffs on allies**

- Aliceth (72% `DEF Penetration` `ATK`)

**Similar Skills**

- Laios (42% `ally-buffer` `high-initial-energy` `temporary-stat-buffer`)
- Zandrok (41% `hp-scaling` `temporary-stat-buffer`)
- Marilee (40% `hp-scaling` `self-repositioner`)

**Damage**

- Baelran (100% `Physical`)
- Aliceth (100% `Physical` `HP loss`)
- Alna (100% `Physical`)

**Crowd Control**

- Indris (79% `Bind` `Knock back`)
- Eironn (62% `Bind`)
- Carolina (62% `Bind`)

### Summary for Kordan

#### Damage types dealt by Kordan

- Physical — Area, Single target

#### Buffs provided by Kordan

- ATK — Area — `low`
- Lifedrain — Area — `average`
- DEF Penetration (Supreme+) — Area — `high`

#### Crowd Control provided by Kordan

- Bind — Single target — `high`
- Knock back — Area — `low`
- Knock down — Single target — `low`
- Knock up (Mythic+) — Single target — `low`

## Korin

### Korin's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Demonseal Spear (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-shielder` `hp-scaling`
- **Damage types**: Physical `low`, Max HP-based damage `low`, True damage `average`

#### Play overview

Korin jumps to an ally, **shielding them** while dealing **true damage** to nearby enemies on landing. His ultimate sweeps adjacent foes with **immobilize and knockback**, disrupting packed frontlines. Distant targets eat guaranteed crits on his strike skill for reliable burst. Accumulated team ultimates trigger a **true damage buff** that spikes his follow-up hits. He also **reduces incoming ranged damage** for safer positioning in the back half. He is a flexible **front-to-back protector** with burst true damage. Value falls when **no ally needs a jump shield** or enemies stay outside sweep range. Team ultimate accumulation turns his jump-and-sweep combo into reliable burst against large HP targets when allies cast often.

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `average`

##### Ultimate

arc sweep immobilize and knock back adjacent enemies

##### Skill 1

jump to an ally, granting them a shield and dealing true damage to nearby enemies

##### Skill 2

guaranteed critical strike on distant targets

##### Legendary+

battle haste increase

##### Mythic+

accumulated team ultimates trigger true damage buff

##### Supreme+

reduce incoming ranged damage taken

### Units improving Korin

Look for units providing: `ATK SPD / Haste` `Max HP`  
Common buffers are **Pandora**, **Ravion**, **Twins**, or **Smokey & Meerky**.

- **Pandora**
  - Max HP (single target, low)
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Ravion**
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Lyca**
  - ATK SPD (all units, low) `signature fuel`
  - Energy (all units, low) `signature fuel`
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste (area, average, conditional (frequent)) `signature fuel`
  - Max HP (multiple targets, low)

### Units benefitting most from Korin

Korin provides Shield to single targets `average`.

- Callan (2.4 / 5)
- Daimon (1.7 / 5)

### Units that can act as a replacement for Korin

**Buffs on allies**

- Contess (100% `Shield`)
- Hugin (100% `Shield`)
- Saida (100% `Shield`)

**Similar Skills**

- Baelran (60% `hp-scaling`)
- Scarlita (48% `ally-shielder` `hp-scaling`)
- Daimon (40% `ally-shielder` `hp-scaling`)

**Damage**

- Nara (100% `True damage` `Physical` `Max HP-based damage`)
- Temesia (100% `Physical` `True damage`)
- Baelran (96% `True damage` `Physical`)

**Crowd Control**

- Kordan (100% `Bind` `Knock back`)
- Indris (95% `Bind` `Knock back`)
- Gwyneth (80% `Bind`)

### Summary for Korin

#### Damage types dealt by Korin

- Physical — Area
- Max HP-based damage — Area — `low`
- True damage — Single target — `average`

#### Buffs provided by Korin

- Shield — Single target — `average`

#### Crowd Control provided by Korin

- Bind — Area — `average`
- Knock back — Area — `low`

## Kruger

### Kruger's behavior

`AFK Stages [C]`, `Dream Realm [A+]`, `Dream Realm (Endless) [A]`, `PVP [C]`

- **Signature skill**: Devastating Axe (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `enemy-debuffer` `life-drain`
- **Damage types**: Physical `high`

#### Play overview

Kruger shreds **Phys DEF** on single-target hits, then slashes to knock down foes and cut DEF further on ultimate. Low-DEF enemies take **Vulnerable** with increased physical damage and life drain on follow-up strikes. Isolated positioning grants a **battle-start shield** and extra drain for safer opening trades. Killing vulnerable foes **permanently stacks ATK** across the fight. He softens targets for **physical damage dealers** better than anyone in his niche. **Magic-heavy teams** gain little from his DEF shred, and **spread lines** deny his vulnerable execute chain. His battle ranged DEF increase helps him survive at distance while stacking vulnerable kills for permanent ATK.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

slash to knock down an enemy and reduce their Phys DEF

##### Skill 1

deal damage to a single enemy, reducing their Phys DEF

##### Skill 2

strike enemies with low Phys DEF, inflicting Vulnerable, increasing physical damage taken with life drain

##### Legendary+

battle ranged DEF increase

##### Mythic+

isolated positioning grants battle-start shield and life drain

##### Supreme+

permanent ATK boost stacks on vulnerable enemy kills

### Units improving Kruger

Look for units providing: `Shield` `Physical DEF`  
Common buffers are **Pandora**, **Rowan**, **Thador**, or **Ravion**.

- **Pandora**
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Rowan**
  - Phys DEF (single target, average)
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Niru**
  - Phys DEF (single target, high)
- **Tilaya**
  - DEF (area, high)
- **Thador**
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Ravion**
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`

### Units benefitting most from Kruger

- Niru (4.2 / 5)
- Indris (3.2 / 5)
- Vala (1.9 / 5)

### Units that can act as a replacement for Kruger

**Similar Skills**

- Shakir (48% `life-drain`)
- Shadewing (40% `enemy-debuffer`)
- Zorya (40% `life-drain`)

**Damage**

- Gwyneth (100% `Physical`)
- Kazim (63% `Physical`)

**Debuffs on enemies**

- Sinbad (56% `Phys DEF` `Damage taken`)
- Ravion (50% `Phys DEF`)
- Zanie (50% `Phys DEF`)

**Crowd Control**

- Frieren (100% `Knock down`)
- Himmel (100% `Knock down`)
- Baelran (100% `Knock down`)

### Summary for Kruger

#### Kruger Provides

- Stacking — Single target

#### Damage types dealt by Kruger

- Physical — Area, Single target

#### Debuffs provided by Kruger

- Damage taken — Single target — `low`
- Phys DEF — Single target — `low`
- Phys DEF — Area — `low`
- Vulnerable — Area — `low`

#### Crowd Control provided by Kruger

- Knock down — Single target — `low`

## Kulu

### Kulu's behavior

`AFK Stages [A+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S+]`

- **Signature skill**: Demolition Zone (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `battlefield-modification` `self-repositioner`
- **Damage types**: Physical `high`

#### Play overview

Kulu opens by **blocking enemy lanes with debris**, then uses skills that **splash to both sides**—allies take reduced friendly-fire damage, but tight formations still suffer. Her ultimate bombards the enemy half with random strikes. Defeated foes can leave **explosive traps**, and her ATK climbs as she damages enemies. She shines when **enemies cluster on their side** and movement paths are contested. **Low raw multipliers** and a modest damage-taken debuff make her a weak pure DPS pick. **Single-target races** or splash-intolerant teams underperform badly.

#### Skill overview

- **Signature skill**: speed `slow`, first cast speed `fast`, buffs `average`, damage `low`
- **Ultimate**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

Passive: all skills deal friendly fire damage; Active: relentlessly bombard enemy side

##### Skill 1

battle-start bomb enemy border tiles, creating movement-blocking debris; Active: knock up an enemy

##### Skill 2

devour frontmost enemies and deliver them to enemy side, triggering bouncing explosions

##### Legendary+

battle ATK stacks from dealing damage to enemies

##### Mythic+

enemies gain explosive debuff; defeated become detonation traps

##### Supreme+

ATK speed and Ranged DEF scale with enemy count on own half

### Units improving Kulu

Look for units providing: `ATK` `ATK SPD / Haste` `DEF Penetration`  
Common buffers are **Ravion**, **Kazim**, **Mikola**, or **Smokey & Meerky**.

- **Aliceth**
  - ATK (multiple targets, average)
  - DEF Penetration (multiple targets, high)
- **Pang**
  - ATK (multiple targets, average)
- **Kordan**
  - DEF Penetration (area, high)
- **Isabella**
  - ATK (single target, low, conditional (frequent))
  - ATK SPD via Haste (single target, low) `signature fuel`
- **Hewynn**
  - ATK SPD via Haste (single target, average) `signature fuel`
- **Mehira**
  - ATK SPD via Haste (multiple targets, average) `signature fuel`

### Units benefitting most from Kulu

Kulu provides ATK (Legendary+) to single targets `low`.

- Niru (5.0 / 5)

### Units that can act as a replacement for Kulu

**Best overall replacement**

- Kordan (50% `Buffs on allies` `Crowd Control` `Damage`)

**Buffs on allies**

- Gunnar (100% `ATK`)
- Contess (100% `ATK`)
- Solise (100% `ATK`)

**Similar Skills**

- Alsa (100% `battlefield-modification` `self-repositioner`)
- Soren (40% `self-repositioner`)
- Marilee (33% `self-repositioner`)

**Damage**

- Gwyneth (100% `Physical`)
- Athalia (100% `Physical`)
- Kruger (100% `Physical`)

**Debuffs on enemies**

- Zorya (53% `Movement speed`)
- Reinier (50% `Damage taken`)

**Crowd Control**

- Kordan (100% `Knock back` `Knock up`)
- Scarlita (100% `Knock back` `Knock up`)
- Ulmus (100% `Knock back` `Knock up`)

### Summary for Kulu

#### Kulu Provides

- Invincibility — Self
- Enhanced form (EX+15) — Single target

#### Damage types dealt by Kulu

- Physical — All units, Area, Single target

#### Buffs provided by Kulu

- ATK (Legendary+) — Single target — `low`

#### Debuffs provided by Kulu

- Movement speed — Area — `low`
- Damage taken (Mythic+) — All units — `low`

#### Crowd Control provided by Kulu

- Unaffected — Self — On ultimate
- Knock back — Single target — `low`
- Knock up — Single target — `low`

## Laios

### Laios's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Dungeon Gourmet (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-buffer` `ally-healer` `high-initial-energy` `summoner` `temporary-stat-buffer`
- **Damage types**: Physical `low`

#### Play overview

Laios summons a **self-regenerating armor construct** on ultimate and confuses enemies in a frontal area to open space. Defeated foes drop **ingredients** that buff allies, with battle-start analysis raising drop rates on early kills. Each ingredient also **permanently grows max HP** over the fight for scaling durability. He blends **summon pressure, debuff, and stacking buffs** in one tank slot. He peaks when **enemies die often** inside his ingredient loop. **Slow fights with few defeats** never stack HP or buffs, and burst that kills the construct early removes his frontline.

#### Skill overview

- **Signature skill**: speed `slow`, heal `average`, buffs `average`
- **Ultimate**: speed `fast`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`

##### Ultimate

summon armor construct that self-regenerates after defeat

##### Skill 1

confuse enemies in frontal area

##### Skill 2

collect ingredients from defeated enemies to grant ally buffs

##### Legendary+

battle ATK increase

##### Mythic+

battle-start analysis makes enemies drop more ingredients on defeat

##### Supreme+

max HP permanently grows with each ingredient collected

### Units improving Laios

Look for units providing: `ATK` `ATK SPD / Haste` `Max HP` `Energy`  
Common buffers are **Mikola**, **Twins**, **Ravion**, or **Smokey & Meerky**.

- **Aurora**
  - Haste (all summons, high)
  - Damage dealt via Damage dealt (all summons, average)
  - Damage taken via Damage taken (all summons, low)
- **Peggy**
  - ATK (all summons, high)
  - DEF via DEF (all summons, high)
- **Tilaya**
  - Max HP (area, high)
  - DEF (area, high)
  - DEF (area, high)
- **Niru**
  - Phys DEF (single target, high)
  - Magic DEF (single target, high)
- **Perseus**
  - ATK (multiple targets, average)
  - Phys DEF (multiple targets, low)
  - Magic DEF (multiple targets, low)
- **Isabella**
  - ATK (single target, low, conditional (frequent))
  - ATK SPD via Haste (single target, low) `signature fuel`
  - Phys DEF (single target, low)
  - Magic DEF (single target, low)

### Units benefitting most from Laios

Laios provides ATK to multiple targets `low` — conditional (rare), Haste in an area `low` — conditional (rare), Healing over time in an area `low` — conditional (rare), Magic DEF in an area `low` — conditional (rare), and Phys DEF in an area `low` — conditional (rare).

- Marcille (2.4 / 5)

### Units that can act as a replacement for Laios

**Similar Skills**

- Damian (80% `ally-buffer` `ally-healer` `summoner` `temporary-stat-buffer`)
- Koko (60% `ally-buffer` `ally-healer` `temporary-stat-buffer`)
- Isabella (60% `ally-buffer` `ally-healer` `temporary-stat-buffer`)

**Crowd Control**

- Evie (100% `Bind`)
- Eironn (100% `Bind`)
- Arden (100% `Bind`)

### Summary for Laios

#### Laios Provides

- Summoning — Single target
- Stacking (EX+10) — Single target

#### Buffs provided by Laios

- ATK — Multiple targets — `low` — conditional (rare)
- Haste — Area — `low` — conditional (rare)
- Healing over time — Area — `low` — conditional (rare)
- Magic DEF — Area — `low` — conditional (rare)
- Phys DEF — Area — `low` — conditional (rare)

#### Debuffs provided by Laios

- Magic DEF — Area — `low`
- Phys DEF — Area — `high`

#### Crowd Control provided by Laios

- Bind — Area — `average`

## Lamentis

### Lamentis's behavior

- **Signature skill**: Omnisight (Mythic+)
- **Movement**: moving (avg attack range 0.0 tiles)
- **Behavior tags**: `aoe-damage` `high-initial-energy` `hp-scaling` `mass-cc` `summoner`
- **Damage types**: Magic `high`, True damage `average`

#### Play overview

Lamentis fights through **apostle summons** that inherit his stats, attack his target, and feed a **Growth stack loop** that eventually unlocks Six Eyes for free apostle waves and stronger Starcrusher hits. His ultimate **stuns front targets** and deals heavy **AoE magic damage** while shaving max HP on controlled foes. Apostles extend his reach but **die easily** and need uninterrupted uptime to reach full ramp; stuns on apostles stall Growth gains. He struggles when **no targets are available** to attack or when burst kills him before Six Eyes activates. The kit peaks in **long fights with summon support** that buys time for apostle stacking and merge healing.

#### Skill overview

- **Signature skill**: speed `fast`, heal `average`, buffs `average`, damage `average`
- **Ultimate**: speed `slow`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `average`

##### Ultimate

apostles stun front enemies, then AoE magic damage and max HP reduction on stunned foes; gain ATK SPD

##### Skill 1

every third normal attack deals bonus max-HP-scaling magic damage

##### Skill 2

sacrifice max HP to create apostles that inherit stats and copy enhanced normals; merge heals caster

##### Legendary+

ATK SPD for self and apostles scales with apostle count on field

##### Mythic+

apostle attacks stack Growth on merge; max stacks unlock Six Eyes, free apostles, and enhanced true damage

##### Supreme+

caster receives a portion of ally buffs applied to apostles

### Units improving Lamentis

Look for units providing: `ATK SPD / Haste` `Healing` `Energy`  
Common buffers are **Smokey & Meerky**, **Lorsan**, **Twins**, or **Mikola**.

- **Peggy**
  - Healing over time (multiple targets, average)
  - ATK (all summons, high)
  - DEF via DEF (all summons, high)
  - Ranged damage via Ranged damage (all summons, low)
- **Aurora**
  - Haste (all summons, high)
  - Damage dealt via Damage dealt (all summons, average)
  - Damage taken via Damage taken (all summons, low)
- **Hewynn**
  - ATK SPD via Haste (single target, average) `signature fuel`
  - Healing over time (all units, high)
- **Damian**
  - ATK SPD via Haste (multiple targets, average, conditional (frequent)) `signature fuel`
  - Direct healing (single target, high)
- **Isabella**
  - ATK SPD via Haste (single target, low) `signature fuel`
  - Direct healing (single target, high)
- **Florabelle**
  - Shield (all summons, average)

### Units benefitting most from Lamentis

- Bonnie (4.6 / 5)

### Units that can act as a replacement for Lamentis

**Similar Skills**

- Lucy (60% `high-initial-energy` `mass-cc` `summoner`)
- Natsu (42% `aoe-damage` `high-initial-energy` `mass-cc`)
- Florabelle (40% `aoe-damage` `summoner`)

**Damage**

- Sylphira (94% `Magic` `True damage`)
- Nara (85% `True damage`)
- Korin (83% `True damage`)

**Debuffs on enemies**

- Lorsan (100% `Max HP`)
- Nara (100% `Max HP`)
- Natsu (100% `Max HP`)

**Crowd Control**

- Hepler (100% `Stun`)
- Koko (100% `Stun`)
- Lorsan (100% `Stun`)

### Summary for Lamentis

#### Lamentis Provides

- Summoning — Self
- Stacking (Mythic+) — Single target

#### Damage types dealt by Lamentis

- Magic — All units, Single target
- Max HP-based damage — Single target
- True damage — Single target — `average`

#### Debuffs provided by Lamentis

- Max HP — Multiple targets — `low`

#### Crowd Control provided by Lamentis

- Stun — Multiple targets — `average`

## Lenya

### Lenya's behavior

`AFK Stages [C]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Wild Duel (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `assassin` `counterattack` `self-repositioner`
- **Damage types**: Physical `average`

#### Play overview

Lenya dodges normal attacks, then **counter-kicks** surrounding foes for AoE damage when pressured. Crits trigger a **power kick with stun**, and her ultimate isolates the **top attacker in a duel**. During the duel she gains **stat boosts and enhanced kicks**, while non-duel opponents deal **reduced damage** to her. Battle haste keeps her rotation quick through repeated counters. She shuts down **high-damage carries** locked in the duel. **Duel-immune targets** or teams that focus her outside the duel waste her isolation payoff.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `average`

##### Ultimate

isolate top attacker in one-on-one combat

##### Skill 1

dodge normal attacks, then counter with an AoE kick

##### Skill 2

crit triggers follow-up power kick with stun

##### Legendary+

battle haste increase

##### Mythic+

gain stat boost and enhanced kick ability during duel

##### Supreme+

reduce damage taken from non-duel opponents

### Units improving Lenya

Look for units providing: `ATK` `Haste` `Max HP` `Shield` `CRIT`  
Common buffers are **Ravion**, **Smokey & Meerky**, **Twins**, or **Kazim**.

- **Ravion**
  - ATK (multiple targets, high)
  - Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Thador**
  - Crit (single target, average)
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Pandora**
  - Max HP (single target, low)
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Zandrok**
  - Haste (area, average, conditional (frequent)) `signature fuel`
  - Max HP (multiple targets, low)
  - ATK SPD via Haste (area, average, conditional (frequent)) `signature fuel`
- **Hewynn**
  - Haste (single target, average) `signature fuel`
  - ATK SPD via Haste (single target, average) `signature fuel`

### Units benefitting most from Lenya

- Niru (4.2 / 5)
- Carolina (2.3 / 5)
- Nerion (2.1 / 5)

### Units that can act as a replacement for Lenya

**Best overall replacement**

- Soren (83% `Damage` `Similar Skills` `Crowd Control`)
- Kafra (80% `Damage` `Crowd Control`)
- Perseus (77% `Damage` `Crowd Control`)

**Similar Skills**

- Soren (66% `counterattack` `self-repositioner`)
- Kafra (40% `assassin` `self-repositioner`)
- Marilee (30% `self-repositioner`)

**Damage**

- Gunnar (100% `Physical`)
- Gwyneth (100% `Physical`)
- Himmel (100% `Physical`)

**Crowd Control**

- Perseus (100% `Knock back` `Stun`)
- Scarlita (100% `Knock back` `Stun`)
- Cassadee (100% `Knock back` `Stun`)

### Summary for Lenya

#### Damage types dealt by Lenya

- Physical — Area, Single target

#### Crowd Control provided by Lenya

- Unaffected — Self — Once
- Knock back — Area — `low`
- Stun — Single target — `average`

## Lily May

### Lily May's behavior

`AFK Stages [A]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Tempest Shot (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `cc-immunity` `hp-scaling` `invincibility` `non-ult-utility` `self-repositioner` `ultimate-cancel`
- **Damage types**: Magic `low`

#### Play overview

Lily May enters a **defensive ultimate** that interrupts the enemy's cast, draining extra energy on the first stop. She strikes multiple times while **invincible**, then grows stronger in stages that **raise ATK and hit count** on each growth. Ally buffs trigger growth and **expand enhanced attacks** for wider pressure across the line. Battle penetration rises over time so later hits bite harder on armored targets. She counters **enemy ultimate timing** and scales into a carry role. **Interrupt-immune casts** or burst that kills her before growth cycles complete blunt her entire kit.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, buffs `average`, debuffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `low`

##### Ultimate

enter defensive state and interrupt the enemy's ultimate

##### Skill 1

deal multiple attacks while invincible

##### Skill 2

progressively grow stronger, each growth boosting ATK and enhancing attacks

##### Legendary+

battle penetration increase

##### Mythic+

ally buff triggers growth, expanding enhanced hit count

##### Supreme+

first ultimate interrupt drains extra energy from target

### Units improving Lily May

Look for units providing: `ATK` `DEF Penetration`  
Common buffers are **Mikola**, **Sonja**, **Parisa**, or **Dunlingr**.

Lily May also requires units **buffing them**

- **Isabella**
  - ATK (single target, low, conditional (frequent))
  - Grants 6 distinct temporary stat buffs to Lily May
- **Perseus**
  - ATK (multiple targets, average)
  - Grants 3 distinct temporary stat buffs to Lily May
- **Kordan**
  - ATK (area, low)
  - DEF Penetration (area, high)
  - Grants 2 distinct temporary stat buffs to Lily May
- **Ravion**
  - ATK (multiple targets, high)
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
  - Grants 1 distinct temporary stat buff to Lily May
- **Aliceth**
  - ATK (multiple targets, average)
  - DEF Penetration (multiple targets, high)
  - Grants 1 distinct temporary stat buff to Lily May
- **Niru**
  - Grants 2 distinct temporary stat buffs to Lily May (start of battle)

### Units benefitting most from Lily May

- Bonnie (1.6 / 5)
- Indris (1.3 / 5)

### Units that can act as a replacement for Lily May

**Similar Skills**

- Athalia (50% `hp-scaling` `non-ult-utility` `self-repositioner`)
- Marilee (33% `hp-scaling` `self-repositioner`)
- Kafra (32% `non-ult-utility` `self-repositioner`)

**Damage**

- Silven (100% `Magic`)
- Sylphira (100% `Magic`)
- Shemira (100% `Magic`)

**Debuffs on enemies**

- Saida (100% `Energy`)
- Dunlingr (50% `Energy`)

**Crowd Control**

- Saida (100% `Interrupt`)
- Sylphira (100% `Interrupt`)
- Marcille (100% `Interrupt`)

### Summary for Lily May

#### Lily May Provides

- Invincibility — Single target

#### Damage types dealt by Lily May

- Magic — Single target
- Max HP-based damage — Single target

#### Debuffs provided by Lily May

- Energy — Single target — `high`

#### Crowd Control provided by Lily May

- Unaffected — Self — Conditional
- Interrupt — Single target — `low`

## Lorsan

### Lorsan's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Whispering Tempest (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `aoe-damage` `dot-specialist` `temporary-stat-buffer`
- **Damage types**: Magic `low`, DoT `high`

#### Play overview

Lorsan links the **nearest and farthest enemy** at battle start, forcing shared damage and control across opposite ends of the line. He then summons a storm that **cuts Haste** and deals sustained damage to everyone within range. Breaking the chain **heals allies** and can reset for another cast within the same fight, rewarding repeated disruption. He shields the weakest ally with **dodge, haste, and regeneration**, and at higher tiers they also gain unaffected status during the protection window. ATK scales after the **first chain break**, so each successful unlink raises his damage ceiling. He mixes **control, healing, and AoE pressure** across a long engagement where the storm can tick for full duration. **Immune or unlinked targets** deny chain payoff entirely, and short fights end before storm damage ramps. Spread enemy lines unlock the full chain-and-storm payoff.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`

##### Ultimate

summon storm dealing sustained damage and reducing Haste to enemies within range

##### Skill 1

battle-start link nearest and farthest enemy heroes with a chain

##### Skill 2

protect weakest ally with dodge, haste, and sustained HP regeneration

##### Legendary+

ATK scales after damage-link chain breaks the first time

##### Mythic+

chain break heals allies; resets for multiple casts per battle

##### Supreme+

protected ally also gains unaffected status

### Units improving Lorsan

Look for units providing: `ATK`  
Common buffers are **Ravion**, **Kazim**, **Mikola**, or **Smokey & Meerky**.

- **Ravion**
  - ATK (multiple targets, high)
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Aliceth**
  - ATK (multiple targets, average)
- **Pang**
  - ATK (multiple targets, average)

### Units benefitting most from Lorsan

Lorsan provides Haste to single targets `average` and Healing over time to single targets `average`.

**42** units include this provider among their top 6 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **4** strongest pairings: 

- Nerion (4.8 / 5)
- Carolina (4.7 / 5)
- Indris (3.8 / 5)
- Alsa (3.2 / 5)

### Units that can act as a replacement for Lorsan

**Buffs on allies**

- Smokey & Meerky (100% `Haste`)
- Shakir (100% `Haste`)
- Twins (90% `Haste`)

**Healing**

- Solise (100% `Healing over time` `Healing`)
- Smokey & Meerky (100% `Healing over time` `Healing`)
- Hepler (100% `Healing over time` `Healing`)

**Similar Skills**

- Tilaya (80% `aoe-damage` `temporary-stat-buffer`)
- Viperian (66% `aoe-damage` `dot-specialist`)
- Arden (60% `aoe-damage` `dot-specialist`)

**Damage**

- Frieren (100% `DoT` `Magic`)
- Faramor (100% `DoT`)
- Cyran (100% `DoT` `Magic`)

**Debuffs on enemies**

- Alna (97% `Haste`)

**Crowd Control**

- Scarlita (100% `Stun`)
- Hepler (88% `Stun`)
- Koko (80% `Stun`)

### Summary for Lorsan

#### Damage types dealt by Lorsan

- DoT — Area

#### Buffs provided by Lorsan

- Haste — Single target — `average`
- Healing over time — Single target — `average`

#### Debuffs provided by Lorsan

- Haste — Area — `low`
- Max HP (Supreme+) — Single target — `average`

#### Crowd Control provided by Lorsan

- Unaffected (Supreme+) — Single target — On skill
- Stun (Mythic+) — Multiple targets — `high`

## Lucca

### Lucca's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Quake Slam (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-shielder` `high-initial-energy` `interrupt`
- **Ally composition**: place adjacent allies behind at battle prep (DEF buff)
- **Ally composition**: place allies on adjacent tiles behind at battle start (shields and ATK boost)
- **Damage types**: Physical `high`

#### Play overview

Lucca gains a shield, then **interrupts and disarms** an enemy while cleansing her own debuffs for brief **damage reduction**. Her ultimate slams a target to origin or **stuns adjacent tiles** when they cannot be returned. She stays steadfast and stacks **shields for each ally behind** her in formation. Cleansing also **recovers HP**, and battle max HP grows over time for durability. She is a **durable disruptor** for packed frontlines that need control. **Disarm-immune foes** or enemies that never cluster for the slam see limited control value. Her cleanse skill also recovers HP when used, giving her a self-sustain loop between disruption casts on the frontline. Steadfast status protects her while stacking shields behind allies.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `low`

##### Ultimate

slam target to origin tile or slam adjacent area, stunning

##### Skill 1

gain shield, then interrupt and disarm an enemy

##### Skill 2

cleanse own debuffs and reduce damage taken briefly

##### Legendary+

battle max HP increase

##### Mythic+

remain steadfast; gain shield for each ally behind

##### Supreme+

recover HP when casting cleanse skill

### Units improving Lucca

Look for units providing: `Max HP` `Shield`

_No synergy partners matched stat buffs or enablers._

### Units benefitting most from Lucca

Lucca provides ATK (Mythic+) to single targets `low` and Magic DEF (Supreme+) in an area `low`.

- Kazim (3.4 / 5)

### Units that can act as a replacement for Lucca

**Best overall replacement**

- Perseus (55% `Buffs on allies` `Damage`)

**Buffs on allies**

- Rowan (100% `Magic DEF`)
- Mikola (100% `Magic DEF` `ATK`)
- Sonja (100% `Magic DEF` `ATK`)

**Similar Skills**

- Hepler (60% `ally-shielder` `high-initial-energy`)
- Saida (50% `ally-shielder` `high-initial-energy`)
- Pang (50% `ally-shielder` `high-initial-energy`)

**Damage**

- Gwyneth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Crowd Control**

- Scarlita (63% `Stun` `Knock up` `Knock down`)
- Callan (61% `Stun` `Knock down`)
- Antandra (61% `Stun` `Knock down`)

### Summary for Lucca

#### Damage types dealt by Lucca

- Physical — Area, Single target

#### Buffs provided by Lucca

- ATK (Mythic+) — Single target — `low`
- Magic DEF (Supreme+) — Area — `low`

#### Crowd Control provided by Lucca

- Immune — Self — On skill
- Steadfast (Mythic+) — Self — Permanent
- Disarm — Single target — `average`
- Interrupt — Single target — `low`
- Knock down — Area — `low`
- Knock up — Area — `low`
- Stun — Area — `average`

## Lucius

### Lucius's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Divine Light Aegis (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-healer` `ally-shielder` `aoe-damage` `enemy-debuffer`
- **Damage types**: Physical `low`

#### Play overview

Lucius knocks back melee foes for a **personal shield**, then heals an ally whenever he gains any shield. His ultimate grants **AoE shields** around a chosen tile for team protection. Frontal strikes deal damage while **cutting enemy ATK**, and battle healing stat rises over time. Each cast **heals one extra ally** beyond the primary target. He mixes **shielding, healing, and soft debuff** in one tank slot. Output is **modest next to dedicated healers** when shield triggers are sparse.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, buffs `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `low`

##### Ultimate

AoE shield granted to allies around selected tile

##### Skill 1

melee knock back, gaining a personal shield

##### Skill 2

heal an ally whenever gaining a shield

##### Legendary+

battle healing stat increase

##### Mythic+

frontal AoE deals damage and reduces enemy ATK

##### Supreme+

heal one extra ally per cast

### Units improving Lucius

Look for units providing: `Shield`  
Common buffers are **Thador**, **Pandora**, **Ravion**, or **Rowan**.

- **Thador**
  - Shield (multiple targets, high)
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Ravion**
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Lyca**
  - Energy (all units, low) `signature fuel`
  - ATK SPD (all units, low) `signature fuel`
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`
- **Saida**
  - Shield (multiple targets, high)

### Units benefitting most from Lucius

Lucius provides Direct healing to multiple targets `average` and Shield in an area `high`.

- Niru (4.2 / 5)
- Himmel (2.2 / 5)
- Vala (1.9 / 5)

### Units that can act as a replacement for Lucius

**Best overall replacement**

- Lumont (79% `Crowd Control` `Damage` `Debuffs on enemies`)
- Antandra (64% `Damage` `Debuffs on enemies` `Crowd Control`)
- Gerda (62% `Healing` `Damage` `Crowd Control`)

**Buffs on allies**

- Hugin (100% `Shield`)
- Saida (100% `Shield`)
- Thador (100% `Shield`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Evie (100% `Direct healing` `Healing`)

**Similar Skills**

- Hepler (48% `ally-healer` `ally-shielder`)
- Cassadee (48% `aoe-damage` `enemy-debuffer`)
- Contess (42% `ally-healer` `ally-shielder` `enemy-debuffer`)

**Damage**

- Gunnar (100% `Physical`)
- Gwyneth (100% `Physical`)
- Himmel (100% `Physical`)

**Debuffs on enemies**

- Contess (100% `ATK`)
- Zanie (100% `ATK`)
- Bonnie (100% `ATK`)

**Crowd Control**

- Aliceth (100% `Knock back` `Stun`)
- Perseus (100% `Knock back` `Stun`)
- Scarlita (100% `Knock back` `Stun`)

### Summary for Lucius

#### Damage types dealt by Lucius

- Physical — Area, Single target

#### Buffs provided by Lucius

- Direct healing — Multiple targets — `average`
- Shield — Area — `high`

#### Debuffs provided by Lucius

- ATK (Mythic+) — Area — `low`
- ATK (EX+10) — Single target — `average`

#### Crowd Control provided by Lucius

- Knock back — Single target — `low`
- Stun — Single target — `low`

## Lucy

### Lucy's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Star Dress: Aquarius Form (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-shielder` `high-initial-energy` `mass-cc` `summoner`
- **Damage types**: Magic `high`

#### Play overview

Lucy stuns the **highest cumulative damage dealer**, then summons a companion whose ultimate triggers **AoE knock-up and stun** across the field. The companion **shields the weakest ally** with a large barrier while active on the board. Max energy during companion uptime **boosts companion attack speed** for faster follow-up. Ultimate also drives **transformation swirls** for extra AoE between casts. Battle haste keeps her rotation moving through control cycles. She blends **control and protection** around her summon. **Burst that kills her companion early** removes shields and stun follow-up. Reaching max energy while the companion is active accelerates stun and shield cycles for the weakest ally under pressure.

#### Skill overview

- **Signature skill**: speed `fast`, damage `high`
- **Ultimate**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `high`

##### Ultimate

summon companion; AoE knock up and stun

##### Skill 1

strike the highest cumulative damage dealer, stunning them

##### Skill 2

ultimate triggers transformation with AoE swirl attacks

##### Legendary+

battle haste increase

##### Mythic+

companion shields weakest ally with large barrier

##### Supreme+

reaching max energy while companion is active boosts companion ATK speed

### Units improving Lucy

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Smokey & Meerky**, **Lorsan**, **Dunlingr**, or **Twins**.

- **Peggy**
  - ATK (all summons, high)
  - DEF via DEF (all summons, high)
  - Ranged damage via Ranged damage (all summons, low)
- **Aurora**
  - Haste (all summons, high)
  - Damage dealt via Damage dealt (all summons, average)
  - Damage taken via Damage taken (all summons, low)
- **Florabelle**
  - Shield (all summons, average)
- **Hewynn**
  - ATK SPD via Haste (single target, average) `signature fuel`
- **Mehira**
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
- **Shakir**
  - ATK SPD via Haste (area, average) `signature fuel`

### Units benefitting most from Lucy

Lucy provides Shield (Mythic+) to single targets `average`.

- Bonnie (4.6 / 5)
- Callan (2.4 / 5)
- Daimon (1.7 / 5)

### Units that can act as a replacement for Lucy

**Buffs on allies**

- Contess (100% `Shield`)
- Hugin (100% `Shield`)
- Saida (100% `Shield`)

**Similar Skills**

- Saida (48% `ally-shielder` `high-initial-energy`)
- Galahad (40% `ally-shielder` `summoner`)
- Hepler (40% `ally-shielder` `high-initial-energy`)

**Damage**

- Saida (100% `Magic`)
- Sylphira (100% `Magic`)
- Marcille (100% `Magic`)

**Crowd Control**

- Zandrok (100% `Stun` `Knock up`)
- Nerion (100% `Stun` `Knock up`)
- Scarlita (100% `Stun` `Knock up`)

### Summary for Lucy

#### Lucy Provides

- Summoning — Single target

#### Damage types dealt by Lucy

- Magic — All units, Single target

#### Buffs provided by Lucy

- Shield (Mythic+) — Single target — `average`

#### Crowd Control provided by Lucy

- Unaffected — Self — On skill
- Knock up — Single target — `low`
- Stun — Single target — `average`

## Ludovic

### Ludovic's behavior

`AFK Stages [A]`, `Dream Realm [B]`, `Dream Realm (Endless) [A]`, `PVP [A]`

- **Signature skill**: Eternal Serenity (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-healer` `aoe-healing`
- **Damage types**: Magic `high`, Max HP-based damage `average`

#### Play overview

Ludovic anchors a **movable healing field** that restores HP for allies inside and damages or stuns **enemies who enter** the zone. He shifts the field to allies or **absorbs nearby enemy HP** to refill stored healing when the pool runs low. Damage skills targeting the top attacker add **HP-loss pressure** alongside the field's passive refill when foes lose HP. Stored healing **scales his battle healing stat**, while periodic berries **explode for damage and ally heals** in range. Field healing restores when enemies lose HP, so sustained enemy damage keeps his pool topped. He excels in **long attrition fights** with steady enemy traffic through the field. Burst that skips the field or enemies that never step inside waste his heal-damage loop. Enemies entering the field take damage and stun, punishing anyone who walks through his shifted zone.

#### Skill overview

- **Signature skill (ult)**: speed `average`, heal `average`
- **Non-ultimate**: speed `average`, heal `average`, damage `high`

##### Ultimate

move healing field to designated tile, restoring HP for allies within range

##### Skill 1

Passive: field healing restored when enemies lose HP; Active: deal damage and HP-loss to top attacker

##### Skill 2

move field to selected ally's position, absorbing nearby enemy HP to restore field healing

##### Legendary+

battle healing stat scales with field total healing stored

##### Mythic+

field periodically produces berries that explode, damaging enemies and healing allies within range

##### Supreme+

enemies entering field take damage and are stunned

### Units improving Ludovic

- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Ravion**
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Lyca**
  - Energy (all units, low) `signature fuel`
  - ATK SPD (all units, low) `signature fuel`
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`
- **Phraesto**
  - Energy via Energy recovery speed (contract ally, start of battle) `signature fuel`

### Units benefitting most from Ludovic

Ludovic provides Direct healing to multiple targets `average` and Healing over time to single targets `high`.

- Niru (5.0 / 5)

### Units that can act as a replacement for Ludovic

**Best overall replacement**

- Smokey & Meerky (50% `Healing` `Similar Skills`)
- Contess (50% `Healing` `Crowd Control`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing over time` `Healing`)
- Evie (100% `Direct healing` `Healing`)

**Similar Skills**

- Solise (80% `ally-healer` `aoe-healing`)
- Smokey & Meerky (80% `ally-healer` `aoe-healing`)
- Fay (80% `ally-healer` `aoe-healing`)

**Damage**

- Shemira (100% `Magic` `Max HP-based damage`)
- Sylphira (99% `Magic`)
- Natsu (99% `Magic`)

**Crowd Control**

- Phraesto (100% `Stun`)
- Bonnie (100% `Stun`)
- Callan (100% `Stun`)

### Summary for Ludovic

#### Damage types dealt by Ludovic

- Magic — All units, Single target
- DoT — Single target
- Max HP-based damage — Single target — `average`

#### Buffs provided by Ludovic

- Direct healing — Multiple targets — `average`
- Healing over time — Single target — `high`

#### Crowd Control provided by Ludovic

- Unaffected — Self — On skill
- Stun (Supreme+) — Single target — `average`

## Lumont

### Lumont's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Lumont's Charge (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `enemy-debuffer` `non-ult-utility` `taunt` `temporary-stat-buffer`
- **Damage types**: Physical `high`

#### Play overview

Lumont charges in a line, **knocking enemies back** toward a chosen tile while building **large shields that grow per adjacent foe**. His stomp adds AoE damage, and **battle haste scales with nearby enemy count** so he swings faster the more bodies crowd him. Sustained damage taken triggers **multi-ring slams** that slash ATK from surrounding enemies, while shielded moments **regenerate HP each second** to stretch his frontline time. He excels as a **tank that thickens with crowd pressure**, punishing swarms that sit on him and feed his haste loop. Against **sparse lines or burst that breaks shields fast**, his regen, counter-slam scaling, and haste buildup never fully ramp.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `average`
- **Non-ultimate**: speed `average`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

charge in line, dealing damage and knocking enemies back toward selected tile

##### Skill 1

large shield growing per adjacent enemy

##### Skill 2

stomp dealing AoE damage

##### Legendary+

battle haste grows with nearby enemy count

##### Mythic+

sustained damage taken triggers multi-ring slam with ATK reduction

##### Supreme+

regenerate HP each second while shielded

### Units improving Lumont

Look for units providing: `Haste` `Shield`  
Common buffers are **Ravion**, **Smokey & Meerky**, **Lorsan**, or **Thador**.

- **Ravion**
  - Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Thador**
  - Shield (multiple targets, high)
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Hewynn**
  - Haste (single target, average) `signature fuel`
  - ATK SPD via Haste (single target, average) `signature fuel`
- **Mehira**
  - Haste (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
- **Damian**
  - Haste (multiple targets, average, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste (multiple targets, average, conditional (frequent)) `signature fuel`

### Units benefitting most from Lumont

Lumont provides Phys DEF to multiple targets `low`.

- Niru (4.2 / 5)
- Carolina (2.3 / 5)
- Nerion (2.1 / 5)

### Units that can act as a replacement for Lumont

**Best overall replacement**

- Hepler (55% `Crowd Control` `Damage`)
- Perseus (55% `Buffs on allies` `Damage`)
- Antandra (52% `Damage`)

**Buffs on allies**

- Niru (100% `Physical DEF`)
- Rowan (100% `Physical DEF`)
- Perseus (100% `Physical DEF`)

**Similar Skills**

- Thador (40% `enemy-debuffer` `temporary-stat-buffer`)
- Daimon (34% `non-ult-utility` `temporary-stat-buffer`)
- Bonnie (33% `enemy-debuffer` `non-ult-utility`)

**Damage**

- Gwyneth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Debuffs on enemies**

- Bonnie (100% `ATK`)
- Antandra (60% `ATK`)

**Crowd Control**

- Hepler (100% `Taunt` `Stun`)
- Phraesto (62% `Taunt` `Stun`)
- Antandra (57% `Stun` `Taunt`)

### Summary for Lumont

#### Damage types dealt by Lumont

- Physical — Area, Single target

#### Buffs provided by Lumont

- Phys DEF — Multiple targets — `low`

#### Debuffs provided by Lumont

- ATK (Mythic+) — Single target — `high`

#### Crowd Control provided by Lumont

- Unaffected — Self — On skill
- Knock back — Area — `low`
- Stun — Area — `low`
- Taunt — Area — `average`
- Knock up (Mythic+) — Single target — `low`
- Stun (Supreme+) — Single target — `low`

## Lyca

### Lyca's behavior

`AFK Stages [C]`, `Dream Realm [A]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Comet Archery (ultimate)
- **Movement**: stationary (avg attack range 11.0 tiles)
- **Behavior tags**: `ally-buffer` `energy-provider` `temporary-stat-buffer`
- **Damage types**: Physical `average`

#### Play overview

Lyca opens by **buffing all allies' attack speed** and fueling the first cast with bonus energy for quick tempo. Her line shot lets nearby allies **summon meteors on normal attacks**, stacking area pressure alongside her ultimate volleys. AoE meteor rain also **shaves enemy Phys DEF**, and passive meteors assist throughout the fight while battle haste keeps her rotation moving. Ultimate hits **deepen the DEF shred**, letting dealers exploit softened targets over time. She shines when **allies stay within ultimate range** and attack often enough to proc meteors on every cycle. Spread formations or **allies outside her line** waste her attack-speed package and meteor summons.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, debuffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

fire line shot; allies within range summon meteors with normal attacks

##### Skill 1

buff all allies ATK speed; grant energy on the first cast

##### Skill 2

AoE meteor rain reduces enemy Phys DEF

##### Legendary+

battle ATK speed increase

##### Mythic+

summon meteors to assist in battle

##### Supreme+

ultimate hit reduces target Phys DEF

### Units improving Lyca

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Ravion**, **Hugin**, **Smokey & Meerky**, or **Lorsan**.

- **Ravion**
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Hewynn**
  - ATK SPD via Haste (single target, average) `signature fuel`
- **Mehira**
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`

### Units benefitting most from Lyca

Lyca provides ATK SPD to all units `low` and Energy to all units `low`.

**30** units include this provider among their top 6 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight
- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **4** strongest pairings: 

- Indris (3.8 / 5)
- Zorya (3.5 / 5)
- Shemira (3.3 / 5)
- Vala (2.9 / 5)

### Units that can act as a replacement for Lyca

**Best overall replacement**

- Ravion (53% `Buffs on allies` `Debuffs on enemies` `Damage`)

**Buffs on allies**

- Ravion (97% `Energy`)
- Thador (81% `Energy`)
- Twins (67% `Energy`)

**Similar Skills**

- Twins (60% `ally-buffer` `energy-provider` `temporary-stat-buffer`)
- Ravion (57% `energy-provider` `temporary-stat-buffer`)
- Parisa (57% `ally-buffer` `temporary-stat-buffer`)

**Damage**

- Gunnar (100% `Physical`)
- Gwyneth (100% `Physical`)
- Himmel (100% `Physical`)

**Debuffs on enemies**

- Zanie (92% `Phys DEF` `ATK`)
- Ravion (88% `Phys DEF` `ATK`)
- Kafra (70% `Phys DEF`)

**Crowd Control**

- Phraesto (100% `Stun`)
- Callan (100% `Stun`)
- Zandrok (100% `Stun`)

### Summary for Lyca

#### Damage types dealt by Lyca

- Physical — All units, Area, Single target

#### Buffs provided by Lyca

- ATK SPD — All units — `low`
- Energy — All units — `low`

#### Debuffs provided by Lyca

- ATK — All units — `low`
- Phys DEF — All units — `low`
- Phys DEF (Supreme+) — Single target — `average`

#### Crowd Control provided by Lyca

- Stun (EX+10) — Single target — `average`

## Marcille

### Marcille's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Silver-White Wings that Streak Across the Skies (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-healer` `aoe-damage` `battle-start-burst` `high-damage-ult` `revive`
- **Ally composition**: place ally 1 tile in front at battle prep (revive target)
- **Damage types**: Magic `high`

#### Play overview

Marcille must **channel every skill**, trading instant casts for heavy payoff once each completes without interruption. Her ultimate **continuously summons companions** while active, and channeled AoE blasts and blinds **heal allies** mid-fight when channels land cleanly. Channeling the ultimate also **raises battle haste**, and she can **revive one fallen ally** after a completed cast. She needs **protection and time** so channels finish before control cancels them. Fights that **interrupt her setup** leave much of her heal and summon value unrealized.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, damage `high`

##### Ultimate

Passive: all skills require channeling to cast; Active: continuously summon companions to attack enemies

##### Skill 1

AoE explosion after channeling completes

##### Skill 2

AoE blind and ally heal after channeling

##### Legendary+

battle haste increase with extra bonus while channeling ultimate

##### Mythic+

revive a fallen ally after channeling completes

##### Supreme+

recover extra energy while buffed by allies

### Units improving Marcille

Look for units providing: `ATK SPD / Haste` `Energy`  
Common buffers are **Pandora**, **Thador**, **Rowan**, or **Ravion**.

Marcille also requires specific **named allies**

- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Ravion**
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Lyca**
  - ATK SPD (all units, low) `signature fuel`
  - Energy (all units, low) `signature fuel`
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`
- **Phraesto**
  - Energy via Energy recovery speed (contract ally, start of battle) `signature fuel`

### Units benefitting most from Marcille

Marcille provides Direct healing (Mythic+) to single targets `high`.

- Niru (5.0 / 5)
- Bonnie (4.6 / 5)

### Units that can act as a replacement for Marcille

**Best overall replacement**

- Natsu (63% `Damage`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Evie (100% `Direct healing` `Healing`)

**Similar Skills**

- Frieren (41% `aoe-damage` `high-damage-ult`)
- Atalanta (40% `aoe-damage` `battle-start-burst`)
- Natsu (36% `aoe-damage` `high-damage-ult`)

**Damage**

- Saida (100% `Magic`)
- Natsu (100% `Magic`)
- Sylphira (92% `Magic`)

**Crowd Control**

- Twins (81% `Blind`)
- Aliceth (81% `Blind`)
- Hepler (81% `Blind`)

### Summary for Marcille

#### Marcille Provides

- Revive ally (Mythic+) — Single target
- Stacking (Supreme+) — Single target

#### Damage types dealt by Marcille

- Magic — All units, Area, Single target

#### Buffs provided by Marcille

- Direct healing (Mythic+) — Single target — `high`

#### Crowd Control provided by Marcille

- Unaffected (Supreme+) — Self — On skill
- Blind — Single target — `average`
- Interrupt (Mythic+) — Single target — `low`

## Marilee

### Marilee's behavior

`AFK Stages [B]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Mid-Air Shot (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `hp-scaling` `self-repositioner`
- **Damage types**: Physical `low`, True damage `low`

#### Play overview

Marilee **leaps to distant tiles** while firing on targets, then strings **stunning enhanced shots** every few normal attacks for steady control from range. She gains ATK and attack speed **when no enemy sits adjacent**, rewarding rear or isolated placement away from melee pressure. Each ally ultimate **stacks her ATK**, culminating in **true damage at max stacks** that spikes her burst window late. Battle crit damage climbs over time, and easier bonus-attack triggers **keep her DPS scaling** through longer engagements. She falters when **enemies close distance** or when few allies cycle ultimates to feed her stacks.

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `low`

##### Ultimate

leap to far location while shooting targets

##### Skill 1

enhanced normal attack every few hits with brief stun

##### Skill 2

ATK and ATK speed increase when no close enemy present

##### Legendary+

battle crit damage boost

##### Mythic+

ATK stacks from each ally ultimate; true damage at max stacks

##### Supreme+

trigger ATK speed bonus condition more easily

### Units improving Marilee

Look for units providing: `ATK` `ATK SPD / Haste` `CRIT`  
Common buffers are **Ravion**, **Smokey & Meerky**, **Kazim**, or **Mikola**.

- **Ravion**
  - ATK (multiple targets, high)
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Thador**
  - Crit (single target, average)
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Lyca**
  - ATK SPD (all units, low) `signature fuel`
  - Energy (all units, low) `signature fuel`
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Aliceth**
  - ATK (multiple targets, average)

### Units benefitting most from Marilee

Marilee provides ATK (EX+10) to single targets `low`.

- Niru (3.4 / 5)
- Vala (2.0 / 5)
- Nerion (1.8 / 5)

### Units that can act as a replacement for Marilee

**Best overall replacement**

- Vala (90% `Damage` `Crowd Control`)
- Nazrik (73% `Damage` `Crowd Control`)
- Faramor (70% `Damage` `Crowd Control`)

**Buffs on allies**

- Gunnar (100% `ATK`)
- Contess (100% `ATK`)
- Solise (100% `ATK`)

**Similar Skills**

- Athalia (80% `hp-scaling` `self-repositioner`)
- Vala (57% `hp-scaling` `self-repositioner`)
- Baelran (50% `hp-scaling`)

**Damage**

- Baelran (100% `Physical` `True damage`)
- Faramor (100% `Physical` `True damage`)
- Athalia (100% `Physical` `True damage`)

**Crowd Control**

- Frieren (100% `Stun`)
- Gunnar (100% `Stun`)
- Contess (100% `Stun`)

### Summary for Marilee

#### Marilee Provides

- DoT conversion (Mythic+) — Self
- Stacking (Mythic+) — Multiple targets

#### Damage types dealt by Marilee

- Physical — Multiple targets, Single target
- True damage — Self — `low`

#### Buffs provided by Marilee

- ATK (EX+10) — Single target — `low`

#### Crowd Control provided by Marilee

- Stun — Single target — `low`

## Mehira

### Mehira's behavior

`AFK Stages [S+]`, `Dream Realm [B]`, `Dream Realm (Endless) [A+]`, `PVP [S]`

- **Signature skill**: Euphoric Rush (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `aoe-damage` `enemy-grouping` `life-drain` `mass-cc` `temporary-stat-buffer` `untargetable`
- **Damage types**: Magic `low`

#### Play overview

Mehira charms an area with **multi-hit AoE**, then whips a frontal arc that **costs HP from all units** but grants allies haste when caught in the lash. She **pulls enemies to a tile**, drains life while scaling ATK from healing received, and summons **voidlings that attack for her**. In danger she can **sacrifice a summon to become untargetable** and heal, while charmed foes take increased damage. She peaks against **clustered targets** that absorb whip pulls and charm setups. Teams that **kill voidlings early** or spread lines blunt her drain payoff.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `low`

##### Ultimate

multi-hit AoE dealing damage and charming all enemies in target area

##### Skill 1

frontal arc whip causes HP-loss to all units; allies hit gain haste

##### Skill 2

pull all enemies toward a designated position

##### Legendary+

life drain and ATK scale with received healing

##### Mythic+

summon voidlings that attack enemies; sacrifice one when in danger to become untargetable and recover HP

##### Supreme+

charmed or bewitched enemies take increased damage

### Units improving Mehira

Look for units providing: `Haste` `Max HP`  
Common buffers are **Ravion**, **Smokey & Meerky**, **Lorsan**, or **Twins**.

- **Ravion**
  - Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Max HP (single target, low)
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Zandrok**
  - Haste (area, average, conditional (frequent)) `signature fuel`
  - Max HP (multiple targets, low)
  - ATK SPD via Haste (area, average, conditional (frequent)) `signature fuel`
- **Hewynn**
  - Haste (single target, average) `signature fuel`
  - ATK SPD via Haste (single target, average) `signature fuel`
- **Shakir**
  - Haste (area, average) `signature fuel`
  - ATK SPD via Haste (area, average) `signature fuel`
- **Damian**
  - Haste (multiple targets, average, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste (multiple targets, average, conditional (frequent)) `signature fuel`

### Units benefitting most from Mehira

Mehira provides Haste to multiple targets `average`.

**14** units include this provider among their top 6 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **4** strongest pairings: 

- Faramor (4.1 / 5)
- Lumont (3.5 / 5)
- Koko (3.2 / 5)
- Bryon (2.4 / 5)

### Units that can act as a replacement for Mehira

**Buffs on allies**

- Twins (100% `Haste`)
- Hugin (100% `Haste`)
- Ravion (100% `Haste`)

**Similar Skills**

- Eironn (45% `aoe-damage` `enemy-grouping` `mass-cc`)
- Gunnar (30% `aoe-damage` `temporary-stat-buffer`)
- Cyran (30% `aoe-damage` `enemy-grouping`)

**Damage**

- Dunlingr (100% `DoT` `Magic`)
- Shadewing (100% `Magic` `DoT`)
- Zorya (99% `Magic`)

**Debuffs on enemies**

- Himmel (100% `Damage taken`)
- Kulu (100% `Damage taken`)
- Cryonaia (100% `Damage taken`)

**Crowd Control**

- Cyran (60% `Displace`)

### Summary for Mehira

#### Mehira Provides

- HP threshold strike (Mythic+) — Single target

#### Damage types dealt by Mehira

- Magic — Area, Single target
- HP loss — Single target

#### Buffs provided by Mehira

- Haste — Multiple targets — `average`

#### Debuffs provided by Mehira

- Damage taken (Supreme+) — Single target — `low`

#### Crowd Control provided by Mehira

- Untargetable (Mythic+) — Self — On skill
- Charm — Single target — `average`
- Charm — All units — `low`
- Displace — All units — `low`

## Mikola

### Mikola's behavior

`AFK Stages [B]`, `Dream Realm [B]`, `Dream Realm (Endless) [A]`, `PVP [B]`

- **Signature skill**: Dauntless Hymn (ultimate)
- **Movement**: moving (avg attack range 2.0 tiles)
- **Behavior tags**: `ally-buffer` `aoe-healing` `temporary-stat-buffer`
- **Damage types**: Physical `low`

#### Play overview

Mikola generates a **Courage Sphere** that buffs nearby allies and **heals everyone in range** once damage thresholds trip during the fight. She places a **central zone** that empowers allies while her side controls it, and heals two weakest allies with DEF boosts to keep fragile carries standing. The sphere grows over time, dealing **continuous DoT to enemies** adjacent to buffed allies, and zone control **freezes aura duration** so the buff window does not decay early. She needs **map control and grouped allies** inside Courage range to maximize healing, DoT aura, and zone bonuses. Fights that **deny zone ownership** or keep allies scattered shrink her buff and sustain impact.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, heal `average`, buffs `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`

##### Ultimate

generate Courage Sphere buffing nearby allies; damage threshold triggers heal for all in-range allies

##### Skill 1

create arena in center; buff all allies when own side controls it

##### Skill 2

heal self and two weakest allies with DEF boost

##### Legendary+

battle ATK increase

##### Mythic+

Courage Sphere enhances over time, dealing continuous DoT to enemies adjacent to in-range allies

##### Supreme+

aura duration frozen when own side controls arena

### Units improving Mikola

Look for units providing: `ATK` `Haste`  
Common buffers are **Ravion**, **Smokey & Meerky**, **Kazim**, or **Twins**.

- **Ravion**
  - ATK (multiple targets, high)
  - Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Hewynn**
  - Haste (single target, average) `signature fuel`
  - ATK SPD via Haste (single target, average) `signature fuel`
- **Mehira**
  - Haste (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
- **Shakir**
  - Haste (area, average) `signature fuel`
  - ATK SPD via Haste (area, average) `signature fuel`
- **Damian**
  - Haste (multiple targets, average, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste (multiple targets, average, conditional (frequent)) `signature fuel`

### Units benefitting most from Mikola

Mikola provides ATK to all units `low`, DEF to multiple targets `average`, Direct healing to multiple targets `average`, Haste to multiple targets `high`, Magic DEF to multiple targets `average`, and Vitality (EX+10) to multiple targets `high`.

**74** units include this provider among their top 6 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight

These are the **4** strongest pairings: 

- Dionel (5.0 / 5)
- Perseus (5.0 / 5)
- Lily May (4.6 / 5)
- Silven (4.3 / 5)

### Units that can act as a replacement for Mikola

**Best overall replacement**

- Smokey & Meerky (64% `Healing` `Similar Skills`)
- Koko (52% `Healing` `Similar Skills`)
- Evie (51% `Healing`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Evie (100% `Direct healing` `Healing`)

**Similar Skills**

- Smokey & Meerky (72% `aoe-healing` `temporary-stat-buffer`)
- Koko (72% `ally-buffer` `temporary-stat-buffer`)
- Sonja (60% `ally-buffer` `temporary-stat-buffer`)

### Summary for Mikola

#### Mikola Provides

- Ally DoT on enemies (Mythic+) — Area

#### Buffs provided by Mikola

- ATK — All units — `low`
- DEF — Multiple targets — `average`
- Direct healing — Multiple targets — `average`
- Haste — Multiple targets — `high`
- Magic DEF — Multiple targets — `average`
- Vitality (EX+10) — Multiple targets — `high`

#### Crowd Control provided by Mikola

- Unaffected (Supreme+) — Self — Conditional

## Mirael

### Mirael's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Winged Flame (ultimate)
- **Movement**: stationary (avg attack range 10.1 tiles)
- **Behavior tags**: `dot-specialist`
- **Damage types**: Magic `high`, DoT `low`

#### Play overview

Mirael lays a **wide frontal burn line** that hits harder on already burning foes, then maintains **sustained single-target burn** between ultimates to keep pressure on priority marks. Magic burst adds **adjacent splash**, battle attack speed rises, and after the first ultimate her **normal attacks become area fireballs** permanently for the rest of the fight. She also **extends burn DoT duration** so flames linger longer on targets her team keeps controlled. Her kit rewards **grouped enemies** where splash, fireball normals, and burn bonuses chain together every cycle. Against **spread or cleanse-heavy lines**, burns fail to stack and her transformed attack pattern underdelivers for much of the fight.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, damage `high`

##### Ultimate

wide frontal line AoE burn damage; extra damage to burning targets

##### Skill 1

apply single sustained burn DoT to one target

##### Skill 2

magic burst with adjacent splash damage

##### Legendary+

battle ATK speed increase

##### Mythic+

after first ultimate, area fireball becomes the normal attack permanently

##### Supreme+

extend burn DoT duration

### Units improving Mirael

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Pandora**, **Ravion**, **Hugin**, or **Lorsan**.

- **Pandora**
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Ravion**
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Lyca**
  - ATK SPD (all units, low) `signature fuel`
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`
- **Thador**
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Hewynn**
  - ATK SPD via Haste (single target, average) `signature fuel`

### Units benefitting most from Mirael

- Niru (4.2 / 5)
- Bonnie (2.6 / 5)
- Vala (1.9 / 5)

### Units that can act as a replacement for Mirael

**Best overall replacement**

- Frieren (53% `Damage`)
- Silven (50% `Damage`)

**Similar Skills**

- Odie (60% `dot-specialist`)
- Viperian (60% `dot-specialist`)
- Shadewing (50% `dot-specialist`)

**Damage**

- Frieren (100% `Magic` `DoT`)
- Saida (100% `Magic` `DoT`)
- Silven (100% `Magic`)

### Summary for Mirael

#### Damage types dealt by Mirael

- Magic — Area, Single target
- DoT — Single target

## Nara

### Nara's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Phantom Chains (Skill 1)
- **Movement**: mostly stationary (pulls enemies; moves on failed pull)
- **Behavior tags**: `ally-healer` `assassin` `execute` `high-initial-energy`
- **Damage types**: Physical `high`, Max HP-based damage `average`, True damage `high`

#### Play overview

Nara strikes a hero for **scaling damage against low HP ratios**, then yanks out-of-range foes **into melee** for a knock-up combo and rapid follow-up attacks. Each assist or defeat **grows her ATK**, and an ultimate kill **releases a shockwave** that damages enemies and heals allies while refunding energy on the finisher. She blends **assassin burst with team sustain** when fights produce kills and wounded targets she can reach. Pulling isolated carries and chaining knock-up strikes define her win condition against backline-heavy formations that leave squishy targets exposed. She needs **access to wounded or isolated targets** and enough energy to cycle her pull-strike loop repeatedly through the fight. **Tanky frontlines or foes that stay in range** deny her execute angle, shockwave value, and the energy refund that keeps her assassin tempo alive through longer trades.

#### Skill overview

- **Signature skill**: speed `fast`, debuffs `average`
- **Ultimate**: speed `fast`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, debuffs `average`, damage `low`

##### Ultimate

strike an enemy hero, dealing more damage to lower HP ratio targets

##### Skill 1

pull enemy hero outside attack range toward self

##### Skill 2

strike knock up then rapid follow-up attacks

##### Legendary+

ATK grows after each assist or defeat

##### Mythic+

ultimate kill releases shockwave damaging enemies and healing allies

##### Supreme+

recover energy after defeating enemy with ultimate

### Units improving Nara

Look for units providing: `ATK` `Energy`  
Common buffers are **Ravion**, **Contess**, **Evie**, or **Kazim**.

- **Aliceth**
  - ATK (multiple targets, average)
- **Pang**
  - ATK (multiple targets, average)
- **Perseus**
  - ATK (multiple targets, average)
- **Fay**
  - ATK (arc, low)
- **Gunnar**
  - ATK (single target, low)
- **Hammie**
  - ATK (single target, low)

### Units benefitting most from Nara

Nara provides Direct healing (Mythic+) in an area `low`.

- Kazim (2.3 / 5)
- Carolina (2.0 / 5)
- Nerion (1.8 / 5)

### Units that can act as a replacement for Nara

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Twins (100% `Direct healing` `Healing`)

**Similar Skills**

- Harak (40% `assassin` `execute`)
- Hepler (40% `ally-healer` `high-initial-energy`)
- Cyran (40% `execute` `high-initial-energy`)

**Damage**

- Faramor (88% `True damage` `Physical`)
- Valka (81% `True damage` `Physical`)
- Athalia (74% `Physical` `True damage`)

**Debuffs on enemies**

- Lorsan (80% `Max HP`)
- Nazrik (66% `Max HP` `Vitality`)
- Natsu (66% `Max HP`)

**Crowd Control**

- Baelran (90% `Knock down` `Knock up`)
- Cyran (90% `Knock down` `Displace`)
- Scarlita (90% `Knock down` `Knock up`)

### Summary for Nara

#### Damage types dealt by Nara

- Physical — Single target
- HP loss — Single target
- Max HP-based damage — Area — `average`
- True damage — Single target — `high`

#### Buffs provided by Nara

- Direct healing (Mythic+) — Area — `low`

#### Debuffs provided by Nara

- Max HP (Supreme+) — Single target — `average`
- Vitality (Supreme+) — Single target — `low`

#### Crowd Control provided by Nara

- Unaffected (Supreme+) — Self — Permanent
- Displace — Single target — `low`
- Knock down — Single target — `average`
- Knock up — Single target — `low`

## Natsu

### Natsu's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Lightning Fire Dragon's Roar/Fire Dragon King's Roar (ultimate)
- **Movement**: moving (avg attack range 3.0 tiles)
- **Behavior tags**: `aoe-damage` `dot-specialist` `high-damage-ult` `high-initial-energy` `mass-cc`
- **Damage types**: Magic `high`

#### Play overview

Natsu chooses modes between **stun-heavy frontal AoE** or **greater raw damage**, adapting each cast to the fight state. The first ally defeat **boosts his ATK and DEF**, with extra crit if a bonded ally falls, while every damage tick also **shaves target max HP**. Sustained burns apply when foes lose HP from **non-normal sources**, feeding his combat scaling. He peaks in **long fights with ally casualties** that unlock his spikes. Early burst or **lines that deny mode setup** leave his burn package thin.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

mode choice: frontal AoE with stun, or frontal AoE with greater damage

##### Skill 1

mode choice: haste debuff strike on top damage dealer, or knock down adjacent enemy

##### Skill 2

first ally defeat boosts ATK and DEF; specific ally's defeat additionally boosts crit

##### Legendary+

mode-dependent haste or ATK boost in combat

##### Mythic+

each damage instance also reduces target max HP

##### Supreme+

sustained burn applied when target loses HP from non-normal sources

### Units improving Natsu

Look for units providing: `ATK` `Haste` `CRIT` `CRIT DMG Boost` `Physical DEF`  
Common buffers are **Mikola**, **Twins**, **Kazim**, or **Ravion**.

Natsu also requires specific **named allies**

- **Niru**
  - Phys DEF (single target, high)
  - Magic DEF (single target, high)
- **Tilaya**
  - DEF (area, high)
  - DEF (area, high)
- **Perseus**
  - ATK (multiple targets, average)
  - Phys DEF (multiple targets, low)
  - Magic DEF (multiple targets, low)
- **Lucy**
  - Enables Named ally on team via Lucy named in skill text
- **Isabella**
  - ATK (single target, low, conditional (frequent))
  - Haste (single target, low) `signature fuel`
  - Phys DEF (single target, low)
  - Magic DEF (single target, low)
- **Solise**
  - ATK (single target, low)
  - DEF (single target, low)
  - DEF (single target, low)

### Units benefitting most from Natsu

- Carolina (3.0 / 5)
- Bonnie (2.8 / 5)
- Nerion (2.7 / 5)

### Units that can act as a replacement for Natsu

**Best overall replacement**

- Sylphira (62% `Damage`)

**Similar Skills**

- Frieren (72% `aoe-damage` `dot-specialist` `high-damage-ult`)
- Arden (72% `aoe-damage` `dot-specialist` `mass-cc`)
- Viperian (48% `aoe-damage` `dot-specialist`)

**Damage**

- Sylphira (100% `Magic`)
- Silven (88% `Magic`)

**Debuffs on enemies**

- Lorsan (72% `Haste` `Max HP`)
- Galahad (65% `Haste`)
- Pandora (61% `Haste`)

**Crowd Control**

- Callan (100% `Stun` `Knock down`)
- Scarlita (100% `Stun` `Knock down`)
- Valen (100% `Stun`)

### Summary for Natsu

#### Natsu Provides

- Form or stance active — Self

#### Damage types dealt by Natsu

- Magic — Arc, Single target
- DoT — Single target
- Max HP-based damage — Single target

#### Debuffs provided by Natsu

- Haste — Single target — `high`
- Max HP (Mythic+) — Single target — `average`

#### Crowd Control provided by Natsu

- Knock down — Single target — `low`
- Stun — Arc — `average`

## Nazrik

### Nazrik's behavior

`AFK Stages [A]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [B]`

- **Signature skill**: Rend Rupture (ultimate)
- **Movement**: stationary (avg attack range 10.0 tiles)
- **Behavior tags**: `hp-scaling` `mark-target`
- **Damage types**: Physical `high`, True damage `high`

#### Play overview

Nazrik marks prey and **detonates all Rend stacks** with a spear throw, while crit throws **apply Rend that ticks when prey casts ultimate**. He stuns the **highest healer** with anti-heal, grows crit from accumulated debuff stacks, and lets **allies add Rend on prey damage** so the whole team feeds the detonation. Each critical hit also **raises crit damage** for snowballing finishes once stacks are high. He needs **time to stack Rend** and allies who can proc it reliably before the spear detonates. **Cleanse or prey targets that never ult** waste his mark-and-detonate loop and stall his crit growth.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, debuffs `average`, damage `average`

##### Ultimate

mark enemy as Prey; throw spear to detonate all Rend stacks

##### Skill 1

crit spear throws apply Rend; Rend deals damage when afflicted enemy casts ultimate

##### Skill 2

target highest healer with damage, stun, and anti-heal

##### Legendary+

crit stat grows after accumulating debuff stacks

##### Mythic+

allies can apply Rend stacks to Prey on dealing damage

##### Supreme+

each critical hit gains increased crit DMG boost

### Units improving Nazrik

Look for units providing: `CRIT`  
Common buffers are **Pandora**, **Thador**, **Rowan**, or **Ravion**.

- **Pandora**
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Crit (single target, average)
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Ravion**
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Phraesto**
  - Energy via Energy recovery speed (contract ally, start of battle) `signature fuel`
- **Lyca**
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`

### Units benefitting most from Nazrik

- Indris (2.4 / 5)
- Carolina (2.0 / 5)
- Nerion (1.8 / 5)

### Units that can act as a replacement for Nazrik

**Best overall replacement**

- Vala (65% `Damage` `Crowd Control`)
- Faramor (58% `Damage`)
- Athalia (52% `Damage`)

**Similar Skills**

- Silven (60% `hp-scaling` `mark-target`)
- Baelran (50% `hp-scaling`)
- Vala (48% `hp-scaling` `mark-target`)

**Damage**

- Frieren (100% `True damage`)
- Faramor (100% `True damage` `Physical`)
- Athalia (100% `True damage` `Physical`)

**Crowd Control**

- Phraesto (100% `Stun`)
- Bonnie (100% `Stun`)
- Callan (100% `Stun`)

### Summary for Nazrik

#### Nazrik Provides

- Stacking — Single target

#### Damage types dealt by Nazrik

- Physical — Single target
- True damage — Single target — `high`

#### Debuffs provided by Nazrik

- Healing — Single target — `average`
- Max HP — Single target — `low`
- Crit Resist (Mythic+) — Single target — `low`
- Damage taken (EX+10) — Single target — `low`
- Vitality (EX+10) — Single target — `low`

#### Crowd Control provided by Nazrik

- Stun — Single target — `average`

## Nerion

### Nerion's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Drowning Doom (ultimate)
- **Movement**: mostly stationary (avg attack range 4.0 tiles)
- **Behavior tags**: `battle-start-burst` `dot-specialist` `enemy-debuffer`
- **Damage types**: Magic `average`, DoT `high`

#### Play overview

Nerion applies **drowning DoT to controlled enemies**, then bounces attacks between drowning targets after an ATK boost on ultimate for chained magic pressure. Enhanced normals **knock back and stun**, projectiles erupt with **delayed knock-up**, and battle start **drowns the rearmost foe** with ATK and haste cuts before control even lands. When every non-summon enemy drowns he gains **permanent empowerment and penetration**, spiking his damage for the rest of the fight. He excels beside **consistent control** that keeps drowning active across multiple targets. **Control-immune or fast-moving lines** never feed his bounce damage or empowerment spike.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

Passive: drowning DoT on controlled enemies; Active: ATK boost; attacks bounce between drowning targets

##### Skill 1

enhanced attack every few normal attacks with knock back and stun

##### Skill 2

projectile then delayed water eruption knock up

##### Legendary+

battle ATK speed increase

##### Mythic+

battle-start apply drowning to rearmost enemy, reducing ATK and Haste; drowning enemies take DoT while controlled

##### Supreme+

all non-summon enemies drowning grants permanent empowerment and penetration increase

### Units improving Nerion

Look for units providing: `ATK` `ATK SPD / Haste` `Shield` `Energy` `DEF Penetration`  
Common buffers are **Twins**, **Lorsan**, **Smokey & Meerky**, or **Ravion**.

Nerion also requires units **applying crowd control** to enemies

- **Twins**
  - ATK (multiple targets, average)
  - ATK SPD via Haste (all units, average) `signature fuel`
  - Energy (multiple targets, low) `signature fuel`
  - Enables CC on enemies via Blind (area, average)
- **Lorsan**
  - ATK SPD via Haste (single target, high) `signature fuel`
  - Enables CC on enemies via Stun (multiple targets, high)
- **Aliceth**
  - ATK (multiple targets, average)
  - DEF Penetration (multiple targets, high)
  - Enables CC on enemies via Blind (area, average)
- **Hepler**
  - Enables CC on enemies via Blind (area, high)
- **Smokey & Meerky**
  - ATK (area, average)
  - ATK SPD via Haste (area, high) `signature fuel`
  - Energy (area, low) `signature fuel`
  - Enables CC on enemies via Stun (area, low)
- **Ravion**
  - ATK (multiple targets, high)
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
  - Enables CC on enemies via Knock down (single target, low)

### Units benefitting most from Nerion

- Kazim (4.5 / 5)

### Units that can act as a replacement for Nerion

**Similar Skills**

- Shadewing (96% `dot-specialist` `enemy-debuffer`)
- Carolina (96% `dot-specialist` `enemy-debuffer`)
- Bonnie (57% `battle-start-burst` `enemy-debuffer`)

**Damage**

- Frieren (100% `DoT` `Magic`)
- Cyran (100% `DoT` `Magic`)
- Cryonaia (100% `DoT` `Magic`)

**Debuffs on enemies**

- Bonnie (100% `Haste` `ATK`)
- Pandora (100% `Haste` `ATK`)
- Zorya (100% `Haste`)

**Crowd Control**

- Zandrok (100% `Knock up` `Stun`)
- Scarlita (100% `Knock up` `Stun`)
- Cassadee (100% `Knock up` `Stun`)

### Summary for Nerion

#### Nerion Provides

- Enhanced form (Supreme+) — Single target

#### Damage types dealt by Nerion

- Magic — Area, Single target
- DoT — Single target

#### Debuffs provided by Nerion

- ATK (Mythic+) — Single target — `low`
- Haste (Mythic+) — Single target — `low`

#### Crowd Control provided by Nerion

- Knock up — Area — `low`
- Stun — Single target — `average`

## Niru

### Niru's behavior

`AFK Stages [A+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Soul Shepherd (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-healer` `battle-start-ult` `hp-scaling` `temporary-stat-buffer`
- **Ally composition**: nearest ally auto-selected at battle start; prioritizes ally behind
- **Damage types**: Magic `high`, HP loss `low`

#### Play overview

Niru stores an ally soul at battle start so they **keep fighting in spirit form** after a fatal blow, preserving output from a key carry. She strikes the weakest foe for **bonus damage at low HP**, drains enemy HP to **heal the weakest ally**, and grows battle max HP to stay relevant on the field. Her opening ultimate **costs no energy**, letting the spirit safeguard trigger immediately. Attacks also briefly **block target healing**, adding soft anti-sustain on her pressure target. She is a **battle-start safety net** for one ally with drain-based sustain for the team. Without a **worthy soul target** or fights that end before spirit triggers, much of her protection sits idle.

#### Skill overview

- **Signature skill (ult)**: speed `fast`
- **Non-ultimate**: speed `fast`, damage `average`

##### Ultimate

store one ally's soul; they continue fighting in spirit form after fatal blow

##### Skill 1

attack weakest enemy, dealing more damage the lower their HP

##### Skill 2

drain all enemies' HP to heal the weakest ally

##### Legendary+

battle max HP increase

##### Mythic+

cast ultimate at battle start without consuming energy

##### Supreme+

attack briefly prevents target from recovering HP

### Units improving Niru

Niru also requires enemies **to be defeated**

- **Alsa**
  - Enables Enemy defeat via AoE magic (kills)
- **Callan**
  - Enables Enemy defeat via AoE magic (kills)
- **Dunlingr**
  - Enables Enemy defeat via AoE magic (kills)
- **Galahad**
  - Enables Enemy defeat via AoE magic (kills)
- **Gunnar**
  - Enables Enemy defeat via AoE physical (kills)
- **Himmel**
  - Enables Enemy defeat via AoE physical (kills)

### Units benefitting most from Niru

Niru provides Magic DEF (Supreme+) to single targets `high` and Phys DEF (Supreme+) to single targets `high`.

**13** units include this provider among their top 6 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **4** strongest pairings: 

- Bonnie (4.3 / 5)
- Silven (3.3 / 5)
- Cecia (3.0 / 5)
- Daimon (3.0 / 5)

### Units that can act as a replacement for Niru

**Buffs on allies**

- Rowan (80% `Magic DEF` `Physical DEF`)
- Mikola (60% `Magic DEF`)
- Sonja (56% `Magic DEF`)

**Similar Skills**

- Isabella (57% `ally-healer` `temporary-stat-buffer`)
- Smokey & Meerky (48% `ally-healer` `temporary-stat-buffer`)
- Koko (48% `ally-healer` `temporary-stat-buffer`)

**Damage**

- Dunlingr (100% `Magic` `HP loss`)
- Shadewing (100% `Magic` `HP loss`)
- Zorya (100% `Magic` `HP loss`)

**Debuffs on enemies**

- Gunnar (100% `Healing`)
- Nazrik (100% `Healing`)
- Harak (100% `Healing`)

### Summary for Niru

#### Niru Provides

- Spirit form protection — Single target
- Start-of-battle cast (Mythic+) — Self
- Spirit form protection (EX+5) — All units
- Named ally on team (Supreme+) — Allies

#### Damage types dealt by Niru

- Magic — All units, Single target
- HP loss — Single target — `low`

#### Buffs provided by Niru

- Magic DEF (Supreme+) — Single target — `high`
- Phys DEF (Supreme+) — Single target — `high`

#### Debuffs provided by Niru

- Healing (Supreme+) — Single target — `low`

## Odie

### Odie's behavior

`AFK Stages [A]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Heart Crusher (Mythic+)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Behavior tags**: `dot-specialist` `execute`
- **Damage types**: Magic `average`, DoT `low`

#### Play overview

Odie plants a **persistent DoT** with his ultimate, then triple-shot normals that **stack poison base damage** on already poisoned targets for escalating tick pressure. Battle attack speed rises, and he can **instantly defeat poisoned foes below a HP threshold** once the venom has softened them enough. Bonus damage also lands on **poisoned triple-shots**, rewarding repeated focus on a single marked victim. He needs **time to layer poison** and enough shots on the same mark to reach execute range. **Cleanse or spread targets** that slip the threshold kill waste his execute angle and poison stacking loop.

#### Skill overview

- **Signature skill**: speed `fast`, debuffs `average`
- **Ultimate**: speed `average`, damage `average`
- **Non-ultimate**: speed `fast`, debuffs `average`, damage `low`

##### Ultimate

apply persistent DoT to a target

##### Skill 1

triple-shot normal attack sequence

##### Skill 2

normal attacks on poisoned targets stack DoT base damage

##### Legendary+

battle ATK speed increase

##### Mythic+

instantly defeat poisoned enemies below HP threshold

##### Supreme+

triple-shot deals bonus damage against poisoned targets

### Units improving Odie

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Hugin**, **Smokey & Meerky**, **Lorsan**, or **Dunlingr**.

- **Hewynn**
  - ATK SPD via Haste (single target, average) `signature fuel`
- **Mehira**
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
- **Damian**
  - ATK SPD via Haste (multiple targets, average, conditional (frequent)) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste (area, average, conditional (frequent)) `signature fuel`
- **Isabella**
  - ATK SPD via Haste (single target, low) `signature fuel`
- **Gunnar**
  - ATK SPD (single target, low) `signature fuel`

### Units benefitting most from Odie

- Niru (3.7 / 5)
- Vala (1.7 / 5)
- Bonnie (1.6 / 5)

### Units that can act as a replacement for Odie

**Best overall replacement**

- Frieren (64% `Damage` `Debuffs on enemies`)
- Mirael (60% `Damage` `Similar Skills`)
- Arden (53% `Damage`)

**Similar Skills**

- Mirael (60% `dot-specialist`)
- Viperian (40% `dot-specialist`)
- Salazer (40% `execute`)

**Damage**

- Frieren (100% `Magic` `DoT`)
- Saida (100% `Magic` `DoT`)
- Silven (100% `Magic`)

**Debuffs on enemies**

- Frieren (82% `DoT`)

### Summary for Odie

#### Odie Provides

- Debuff application — Single target
- Instant defeat (Mythic+) — Single target
- Execution scaling (Supreme+) — Single target

#### Damage types dealt by Odie

- Magic — Single target
- DoT — Single target

#### Debuffs provided by Odie

- DoT — Single target — `average`
- Execution (Mythic+) — Single target — `low`

## Pandora

### Pandora's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [A]`, `PVP [A+]`

- **Signature skill**: Boxed Blessing (Skill 1)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `enemy-debuffer` `energy-provider` `mass-cc`
- **Ally composition**: rearmost ally enters invincible box, then gains Energy and ATK
- **Damage types**: Magic `high`, DoT `average`

#### Play overview

Pandora's ultimate **CCs every unit except herself**, freezing the entire field while she alone keeps acting, while at battle start she **pulls an ally into her box** and restores their energy for an early tempo spike. Corruption stacks **drive debuffs on enemies** as the fight wears on, battle max HP grows especially after box corruption, and the **indestructible box persists** even after she falls to keep her setup alive. Allies inside the box **ignore her ultimate**, turning the global pause into a controlled window for one protected partner. She demands careful **ally selection for the box** and patience to build corruption before debuffs peak on the enemy line. Teams that **punish her before corruption ramps** or exploit the global CC window blunt her upside, box value, and late-fight max HP scaling.

#### Skill overview

- **Signature skill**: speed `fast`, buffs `average`
- **Ultimate**: speed `slow`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`

##### Ultimate

AoE CC on all units, friend and foe; caster alone is unaffected

##### Skill 1

at battle start, pull an ally into the box and restore their energy

##### Skill 2

inflict enemy debuffs based on accumulated Corruption stacks

##### Legendary+

max HP grows during battle, increased further after box corruption

##### Mythic+

box remains on battlefield and is indestructible after caster defeat

##### Supreme+

ally inside the box is unaffected by caster ultimate

### Units improving Pandora

Look for units providing: `Energy`

- **Rowan**
  - Energy (area, high) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
- **Ravion**
  - Energy (multiple targets, average) `signature fuel`
- **Hugin**
  - Energy (single target, average, conditional (frequent)) `signature fuel`

### Units benefitting most from Pandora

Pandora provides Direct healing to single targets `high`, Energy to single targets `low`, Invincible to single targets `high`, and Max HP (Legendary+) to single targets `low`.

**68** units include this provider among their top 6 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **4** strongest pairings: 

- Marcille (5.0 / 5)
- Shemira (5.0 / 5)
- Cryonaia (4.5 / 5)
- Carolina (4.0 / 5)

### Units that can act as a replacement for Pandora

**Best overall replacement**

- Hepler (51% `Buffs on allies` `Healing`)

**Buffs on allies**

- Gunnar (93% `Invincible`)
- Hepler (93% `Invincible`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Evie (100% `Direct healing` `Healing`)

**Similar Skills**

- Cecia (50% `enemy-debuffer` `mass-cc`)
- Thador (40% `enemy-debuffer` `energy-provider`)
- Temesia (33% `enemy-debuffer` `mass-cc`)

**Damage**

- Frieren (100% `DoT`)
- Gwyneth (100% `DoT`)
- Alna (100% `DoT`)

**Debuffs on enemies**

- Alna (58% `Haste` `Vitality`)
- Dunlingr (53% `Haste` `Vitality` `Energy`)

**Crowd Control**

- Berial (100% `Frighten`)
- Silvina (100% `Frighten`)
- Daimon (80% `Frighten`)

### Summary for Pandora

#### Pandora Provides

- Invincibility — Single target

#### Damage types dealt by Pandora

- DoT — All units

#### Buffs provided by Pandora

- Direct healing — Single target — `high`
- Energy — Single target — `low`
- Invincible — Single target — `high`
- Max HP (Legendary+) — Single target — `low`

#### Debuffs provided by Pandora

- ATK — Single target — `low`
- Damage taken — Single target — `low`
- Energy — Single target — `low`
- Haste — Single target — `average`
- Vitality — Single target — `average`

#### Crowd Control provided by Pandora

- Frighten — All units — `low`

## Pang

### Pang's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Sky Splitter (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-shielder` `high-initial-energy` `temporary-stat-buffer`
- **Damage types**: Physical `high`

#### Play overview

Pang channels then **bursts AoE**, entering a stance with ATK and haste where strikes **block enemy energy recovery** to stall opposing ultimates across the field. Heavy single-target hits add direct pressure, a shield keeps him **unaffected while active**, and shield break or expiry deals retaliation damage to punish focus fire on his frontline slot. Any shielded ally gains **ATK from his passive**, and entering the buff state **instantly grants shield and penetration** for an immediate power spike before the stance fully settles. Battle ATK rises over time, blending **burst damage with energy denial** once stance is online and retaliation triggers are armed. Fights that **break shields before stance** or deny melee access cut his retaliation loop, energy denial, and team ATK sharing.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, buffs `average`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `average`

##### Ultimate

channel then AoE burst; enter stance with ATK and haste, strikes block enemy energy recovery

##### Skill 1

deal heavy damage to a single enemy

##### Skill 2

gain shield, remaining unaffected while active; shield expiry, break, or reapplication deals damage

##### Legendary+

battle ATK increase

##### Mythic+

shield grants ATK boost to any shielded unit

##### Supreme+

entering buff state immediately grants shield and penetration

### Units improving Pang

Look for units providing: `ATK` `Haste` `Shield` `Energy` `DEF Penetration`  
Common buffers are **Ravion**, **Kazim**, **Mikola**, or **Smokey & Meerky**.

- **Aliceth**
  - ATK (multiple targets, average)
  - DEF Penetration (multiple targets, high)
- **Kordan**
  - ATK (area, low)
  - DEF Penetration (area, high)
- **Perseus**
  - ATK (multiple targets, average)
- **Isabella**
  - ATK (single target, low, conditional (frequent))
  - Haste (single target, low) `signature fuel`
- **Hewynn**
  - Haste (single target, average) `signature fuel`
- **Mehira**
  - Haste (multiple targets, average) `signature fuel`

### Units benefitting most from Pang

Pang provides ATK (Mythic+) to multiple targets `average`.

- Aliceth (2.8 / 5)

### Units that can act as a replacement for Pang

**Best overall replacement**

- Perseus (92% `Damage` `Crowd Control` `Buffs on allies`)
- Kafra (77% `Damage` `Crowd Control`)
- Lucca (75% `Damage` `Crowd Control` `Similar Skills`)

**Buffs on allies**

- Contess (100% `ATK`)
- Twins (100% `ATK`)
- Ravion (100% `ATK`)

**Similar Skills**

- Hugin (60% `ally-shielder` `high-initial-energy` `temporary-stat-buffer`)
- Saida (50% `ally-shielder` `high-initial-energy`)
- Hepler (50% `ally-shielder` `high-initial-energy`)

**Damage**

- Gwyneth (100% `Physical`)
- Alna (100% `Physical`)
- Faramor (100% `Physical`)

**Debuffs on enemies**

- Contess (100% `Energy`)
- Saida (100% `Energy`)
- Sylphira (100% `Energy`)

**Crowd Control**

- Contess (100% `Stun`)
- Gwyneth (100% `Stun`)
- Aliceth (100% `Stun`)

### Summary for Pang

#### Pang Provides

- Transformation — Self

#### Damage types dealt by Pang

- Physical — Area, Single target

#### Buffs provided by Pang

- ATK (Mythic+) — Multiple targets — `average`

#### Debuffs provided by Pang

- Energy — Single target — `low`

#### Crowd Control provided by Pang

- Unaffected — Self — On skill
- Stun — Single target — `low`

## Parisa

### Parisa's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Floral Splendor (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Behavior tags**: `ally-buffer` `aoe-damage` `mark-target` `temporary-stat-buffer`
- **Self placement**: nearest symmetrical enemy at battle start (Falling Blossom / First Strike openers)
- **Damage types**: Magic `high`

#### Play overview

Parisa marks with flowers for **AoE ultimate damage**, then boosts **attack speed and normal attack damage** for herself and one ally to accelerate their output together. Periodic line attacks sweep after several normals, battle ATK climbs, and marks at start let normals **hit extra targets after enough stacks** accumulate on the field. Fewer normals are needed to **trigger the line attack** at higher tiers, tightening her proc rhythm in longer fights. She shines beside **another high-attack ally** who can share her speed buff. Without **frequent normal attacks** or clustered marks, her line procs stay flat.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `average`

##### Ultimate

mark target with flower and deal AoE damage

##### Skill 1

boost ATK speed and normal attack damage for herself and an ally

##### Skill 2

periodic line attack hitting enemies along path after several normal attacks

##### Legendary+

battle ATK increase

##### Mythic+

mark at start; normal attacks hit extra targets after accumulating marks

##### Supreme+

fewer normal attacks needed to trigger periodic line attack

### Units improving Parisa

Look for units providing: `ATK` `ATK SPD / Haste` `Energy`  
Common buffers are **Ravion**, **Smokey & Meerky**, **Kazim**, or **Mikola**.

- **Ravion**
  - ATK (multiple targets, high)
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Lyca**
  - ATK SPD (all units, low) `signature fuel`
  - Energy (all units, low) `signature fuel`
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`
- **Aliceth**
  - ATK (multiple targets, average)

### Units benefitting most from Parisa

Parisa provides ATK to multiple targets `high` and ATK SPD to multiple targets `low`.

**46** units include this provider among their top 6 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **4** strongest pairings: 

- Bonnie (3.9 / 5)
- Perseus (3.6 / 5)
- Dionel (3.5 / 5)
- Lily May (3.4 / 5)

### Units that can act as a replacement for Parisa

**Buffs on allies**

- Ravion (69% `ATK`)
- Evie (50% `ATK`)
- Smokey & Meerky (50% `ATK`)

**Similar Skills**

- Sonja (75% `ally-buffer` `aoe-damage` `temporary-stat-buffer`)
- Perseus (75% `ally-buffer` `aoe-damage` `temporary-stat-buffer`)
- Tilaya (60% `aoe-damage` `temporary-stat-buffer`)

**Damage**

- Saida (100% `Magic`)
- Galahad (100% `Magic`)
- Sylphira (100% `Magic`)

### Summary for Parisa

#### Parisa Provides

- Marked target (focus fire) — Area
- Marked target (focus fire) (Mythic+) — Single target

#### Damage types dealt by Parisa

- Magic — Area

#### Buffs provided by Parisa

- ATK — Multiple targets — `high`
- ATK SPD — Multiple targets — `low`

## Peggy

### Peggy's behavior

- **Signature skill**: Princess Rally (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-buffer` `ally-healer` `ally-shielder` `high-initial-energy` `summoner`
- **Damage types**: Physical `average`

#### Play overview

Peggy opens with **two royal guards** and reaches her ultimate quickly thanks to high starting energy. Her ultimate **heals guards to full** then routes most ally damage through them while **reducing HP-loss damage** they take, giving broad protection once it lands. Royal Scroll provides **strong healing over time** on guards and the weakest allies, while Royal Barrage adds a marksman that **amplifies ranged damage** on front targets and boosts summon output. Ex aura and Supreme buffs also make her a **summon-team amplifier** beside her protector role. Protection **depends on the ultimate window** and living guards — burst that kills her or denies the cast leaves allies exposed.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, first cast speed `fast`, heal `average`, buffs `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

Passive: battle-start summon guards; Active: heal guards, refill guard, then guards absorb ally damage

##### Skill 1

healing over time on guards and two weakest allies

##### Skill 2

summon ranged marksman; armor-piercing shots increase ranged damage taken and amplify allied summon ranged damage

##### Legendary+

haste bonus rises when two guards remain on field

##### Mythic+

during ultimate, guards alternate AoE slashes that grant shield; aura boosts nearby melee damage, extra for summons

##### Supreme+

when enough allied summons from different allies are alive, buff all summons ATK and Phys and Magic DEF

### Units improving Peggy

Look for units providing: `ATK` `Haste` `Shield`  
Common buffers are **Kazim**, **Mikola**, **Ravion**, or **Smokey & Meerky**.

- **Aurora**
  - Haste (all summons, high)
  - Damage dealt via Damage dealt (all summons, average)
  - Damage taken via Damage taken (all summons, low)
- **Florabelle**
  - Shield (all summons, average)
- **Aliceth**
  - ATK (multiple targets, average)
- **Pang**
  - ATK (multiple targets, average)
- **Isabella**
  - ATK (single target, low, conditional (frequent))
  - Haste (single target, low) `signature fuel`
- **Hewynn**
  - Haste (single target, average) `signature fuel`

### Units benefitting most from Peggy

Peggy provides Healing over time to multiple targets `high`, Ranged damage to all summons `low`, Damage dealt (EX+10) to multiple targets `low`, ATK (Supreme+) to all summons `high`, and DEF (Supreme+) to all summons `average`.

**14** units include this provider among their top 6 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **4** strongest pairings: 

- Bryon (5.0 / 5)
- Florabelle (5.0 / 5)
- Lamentis (5.0 / 5)
- Lucy (5.0 / 5)

### Units that can act as a replacement for Peggy

**Healing**

- Hepler (100% `Healing over time` `Healing`)
- Hewynn (100% `Healing over time` `Healing`)
- Lorsan (100% `Healing over time` `Healing`)

**Similar Skills**

- Laios (66% `ally-buffer` `ally-healer` `high-initial-energy` `summoner`)
- Hepler (60% `ally-healer` `ally-shielder` `high-initial-energy`)
- Lucy (60% `ally-shielder` `high-initial-energy` `summoner`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

### Summary for Peggy

#### Peggy Provides

- Damage absorption (allies) — All units
- Summoning — Single target

#### Damage types dealt by Peggy

- Physical — Area, Multiple targets

#### Buffs provided by Peggy

- Healing over time — Multiple targets — `high`
- Ranged damage — All summons — `low`
- Damage dealt (EX+10) — Multiple targets — `low`
- ATK (Supreme+) — All summons — `high`
- DEF (Supreme+) — All summons — `average`

#### Debuffs provided by Peggy

- Ranged damage — Single target — `average`

## Perseus

### Perseus's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Divine Rend (ultimate)
- **Movement**: moving (avg attack range 2.9 tiles)
- **Behavior tags**: `ally-buffer` `aoe-damage` `temporary-stat-buffer`
- **Damage types**: Physical `high`

#### Play overview

Perseus **marches through packed frontlines**, dealing repeated AoE hits, knockback, and a finishing stun while he stays unaffected. Before heavy damage lands, he turns nearby tiles **fertile**, buffing allies who stand on them with ATK and DEF until the ground withers. He also **amplifies temporary ally buffs** into extra ATK for himself, then gains a one-time max HP surge and heal once he drops below 40% HP. Against **isolated or spread targets**, his march and tile buffs fail to connect. Teams that burst him early or **keep allies off his fertile ground** get little value from his kit.

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `high`

##### Ultimate

continuously march forward, dealing damage with repeated spear swings

##### Skill 1

swing spear and shield, dealing damage to nearby enemies

##### Skill 2

grant buffs to allies standing on terrain zone tiles

##### Legendary+

ATK boost grows with temporary ally buffs active

##### Mythic+

amplify effects of all temporary stat buffs received

##### Supreme+

expand ally terrain buff area by one tile

### Units improving Perseus

Look for units providing: `ATK` `ATK SPD / Haste` `Max HP` `Shield`  
Common buffers are **Mikola**, **Ravion**, **Smokey & Meerky**, or **Twins**.

Perseus also requires units **buffing them**

- **Isabella**
  - ATK (single target, low, conditional (frequent))
  - ATK SPD via Haste (single target, low) `signature fuel`
  - Grants 6 distinct temporary stat buffs to Perseus
- **Ravion**
  - ATK (multiple targets, high)
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
  - Grants 1 distinct temporary stat buff to Perseus
- **Pandora**
  - Max HP (single target, low)
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
  - Grants 1 distinct temporary stat buff to Perseus
- **Zandrok**
  - ATK SPD via Haste (area, average, conditional (frequent)) `signature fuel`
  - Max HP (multiple targets, low)
  - Grants 1 distinct temporary stat buff to Perseus (start of battle)
- **Koko**
  - ATK (all units, low)
  - Grants 2 distinct temporary stat buffs to Perseus

### Units benefitting most from Perseus

Perseus provides ATK to multiple targets `low`, Magic DEF to multiple targets `low`, and Phys DEF to multiple targets `low`.

**6** units include this provider among their top 6 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **4** strongest pairings: 

- Lily May (3.6 / 5)
- Faramor (3.5 / 5)
- Dionel (3.2 / 5)
- Silven (2.8 / 5)

### Units that can act as a replacement for Perseus

**Best overall replacement**

- Sonja (69% `Similar Skills` `Buffs on allies`)
- Pang (64% `Damage`)
- Lucca (63% `Damage` `Crowd Control`)

**Buffs on allies**

- Sonja (85% `ATK` `Magic DEF`)
- Twins (71% `ATK` `Magic DEF` `Physical DEF`)
- Mikola (71% `ATK` `Magic DEF`)

**Similar Skills**

- Sonja (100% `ally-buffer` `aoe-damage` `temporary-stat-buffer`)
- Parisa (75% `ally-buffer` `aoe-damage` `temporary-stat-buffer`)
- Tilaya (66% `aoe-damage` `temporary-stat-buffer`)

**Damage**

- Gwyneth (100% `Physical`)
- Athalia (100% `Physical`)
- Kulu (100% `Physical`)

**Crowd Control**

- Scarlita (100% `Stun` `Knock back`)
- Atalanta (100% `Stun` `Knock back`)
- Valen (96% `Stun`)

### Summary for Perseus

#### Damage types dealt by Perseus

- Physical — Area

#### Buffs provided by Perseus

- ATK — Multiple targets — `low`
- Magic DEF — Multiple targets — `low`
- Phys DEF — Multiple targets — `low`

#### Crowd Control provided by Perseus

- Unaffected — Self — On skill
- Knock back — Area — `low`
- Stun — Area — `average`

## Phraesto

### Phraesto's behavior

`AFK Stages [A+]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Crimson Contract (Skill 1)
- **Movement**: moving (avg attack range 1.8 tiles)
- **Behavior tags**: `ally-buffer` `ally-shielder` `aoe-damage` `energy-provider` `summoner`
- **Ally composition**: place allies 1 tile behind this hero and the Illusion for contract buffs
- **Self placement**: keep this hero and Illusion in the same row (damage reduction and battle-start shields)
- **Damage types**: Magic `high`

#### Play overview

Phraesto sacrifices max HP to **summon an Illusion that casts all his skills**, duplicating his kit while his active ultimate **heals per nearby hit** to recover the cost over time. He and the clone **grant rear allies stat contracts**, apply DoT and reductions on strike, share DEF and cross-transfer energy on damage so both bodies stay fueled through the fight. Row allies start with **shields at battle open**, and if the Illusion dies first he **damages and stuns an enemy** for a punish window. He needs **HP to feed the clone** and allies behind him positioned to honor contracts and benefit from rear buffs. Losing the Illusion early or **denying rear positioning** shrinks his buff, duplication value, and sustain loop across the fight.

#### Skill overview

- **Signature skill**: speed `slow`, first cast speed `fast`, buffs `average`, damage `low`
- **Ultimate**: speed `average`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

Passive: sacrifice max HP to summon an Illusion that uses all skills; Active: AoE damage nearby, recovering HP per hit

##### Skill 1

Passive: clone and self grant rear allies stat contracts; Active: frontal multi-strike

##### Skill 2

apply DoT and stat reduction to target

##### Legendary+

DEF boost shared with clone; energy cross-transfers on damage

##### Mythic+

if Illusion is defeated first, deal damage to an enemy and stun them

##### Supreme+

both in same row gain initial shield at battle start

### Units improving Phraesto

Look for units providing: `Healing` `Energy` `Magic DEF`  
Common buffers are **Rowan**, **Mikola**, **Twins**, or **Pandora**.

- **Peggy**
  - Healing over time (multiple targets, average)
  - ATK (all summons, high)
  - DEF via DEF (all summons, high)
- **Aurora**
  - Haste (all summons, high)
  - Damage dealt via Damage dealt (all summons, average)
  - Damage taken via Damage taken (all summons, low)
- **Florabelle**
  - Shield (all summons, average)
- **Isabella**
  - Direct healing (single target, high)
  - Magic DEF (single target, low)
- **Solise**
  - Direct healing (all units, high)
  - DEF (single target, low)
- **Damian**
  - Direct healing (single target, high)

### Units benefitting most from Phraesto

Phraesto provides Damage taken to single targets `low`.

**16** units include this provider among their top 6 synergy partners. Why the match is common:

- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **4** strongest pairings: 

- Marcille (2.6 / 5)
- Callan (2.5 / 5)
- Shemira (2.5 / 5)
- Athalia (2.5 / 5)

### Units that can act as a replacement for Phraesto

**Best overall replacement**

- Antandra (64% `Crowd Control` `Buffs on allies`)
- Satrana (54% `Buffs on allies` `Debuffs on enemies` `Damage`)

**Buffs on allies**

- Hugin (100% `Damage taken`)
- Reinier (100% `Damage taken`)
- Koko (100% `Damage taken`)

**Similar Skills**

- Galahad (60% `ally-shielder` `aoe-damage` `summoner`)
- Twins (42% `ally-buffer` `ally-shielder` `energy-provider`)
- Gunnar (41% `ally-shielder` `aoe-damage`)

**Damage**

- Frieren (100% `Magic`)
- Saida (100% `Magic`)
- Silven (100% `Magic`)

**Debuffs on enemies**

- Frieren (100% `Vitality`)
- Gunnar (100% `Vitality`)
- Gwyneth (100% `Vitality`)

**Crowd Control**

- Hepler (100% `Stun` `Taunt`)
- Antandra (95% `Stun` `Taunt`)
- Callan (60% `Stun`)

### Summary for Phraesto

#### Phraesto Provides

- Summoning — Self

#### Damage types dealt by Phraesto

- Magic — Area, Single target
- DoT — Single target

#### Buffs provided by Phraesto

- Damage taken — Single target — `low`

#### Debuffs provided by Phraesto

- Vitality — Single target — `low`

#### Crowd Control provided by Phraesto

- Stun (Mythic+) — Single target — `average`
- Taunt (Mythic+) — Single target — `average`

## Pippa

### Pippa's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Wild Shift (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `enemy-grouping` `hp-scaling`
- **Damage types**: Magic `high`, Max HP-based damage `average`, True damage `low`

#### Play overview

Pippa **immobilizes and teleports enemies** on ultimate, then sprays **rapid magic missiles** and seeds magical growth on **the densest enemy cluster** to damage and drain energy. Consecutive casts **scale battle haste**, random mutations can surprise on skill use, and teleported foes **take extra portal fall damage** after repositioning. She excels when **enemies group** for growth, teleport setups, and missile volleys. Sparse lines or **RNG mutations that miss** leave her damage inconsistent.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, debuffs `average`, damage `low`

##### Ultimate

immobilize and teleport enemies

##### Skill 1

fire magic missiles at enemies in quick succession

##### Skill 2

magical growth on area with most enemies, dealing damage and draining energy

##### Legendary+

battle haste scales with controlled consecutive casts

##### Mythic+

skill casts may randomly trigger mutation

##### Supreme+

teleported targets fall through portals, taking additional damage

### Units improving Pippa

Look for units providing: `Haste`  
Common buffers are **Pandora**, **Ravion**, **Lorsan**, or **Smokey & Meerky**.

- **Pandora**
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Ravion**
  - Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Thador**
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Phraesto**
  - Energy via Energy recovery speed (contract ally, start of battle) `signature fuel`
- **Lyca**
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`

### Units benefitting most from Pippa

- Carolina (3.7 / 5)
- Bonnie (3.4 / 5)
- Nerion (3.2 / 5)

### Units that can act as a replacement for Pippa

**Best overall replacement**

- Sylphira (51% `Damage`)

**Similar Skills**

- Baelran (50% `hp-scaling`)
- Shemira (40% `hp-scaling`)
- Nazrik (40% `hp-scaling`)

**Damage**

- Sylphira (100% `Magic` `True damage`)
- Indris (93% `True damage`)
- Frieren (81% `Magic` `True damage`)

**Debuffs on enemies**

- Saida (100% `Energy`)
- Dunlingr (100% `Energy`)
- Lily May (100% `Energy`)

**Crowd Control**

- Eironn (100% `Bind` `Displace`)
- Arden (92% `Bind`)
- Indris (86% `Bind`)

### Summary for Pippa

#### Damage types dealt by Pippa

- Magic — Area, Single target
- DoT — Area
- Max HP-based damage — Multiple targets — `average`
- True damage — Area — `average`

#### Debuffs provided by Pippa

- Energy — Area — `average`

#### Crowd Control provided by Pippa

- Unaffected — Self — On skill
- Bind — Multiple targets — `low`
- Displace — Multiple targets — `low`
- Knock down — Single target — `low`
- Bind (Mythic+) — Area — `average`
- Bind (Supreme+) — Single target — `low`

## Ravion

### Ravion's behavior

`AFK Stages [A+]`, `Dream Realm [A+]`, `Dream Realm (Endless) [A]`, `PVP [A+]`

- **Signature skill**: Killer Flush (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-shielder` `energy-provider` `self-repositioner` `temporary-stat-buffer`
- **Ally composition**: Objectives go to the 2 rearmost allies; backline heroes receive ATK and Energy on completion
- **Damage types**: Physical `low`, HP loss `average`

#### Play overview

Ravion assigns **objectives to allies**; completing them grants energy, ATK, and unlocks a knock-down strike for coordinated burst windows across the fight. His ultimate **scales with target HP-loss** across multi-hits, while repeated teleports **deal early jump damage** then reposition away from foes to stay safe through longer engagements. First enhanced strike **activates ATK bonus**, and unlocking it permanently **grants haste and ATK to self and allies** for a lasting team spike. Assigned tasks also give brief ATK boost and unaffected state while allies work objectives across the board. He needs **allies who finish objectives** and room to teleport safely through longer engagements. **Static teams or burst that pins him** before enhanced strikes land waste his coordination package and team buffs.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

multi-hit single target, dealing extra damage scaling with target's HP-loss

##### Skill 1

assign objectives to allies; completion grants energy and ATK and unlocks knock down strike

##### Skill 2

repeated teleports, dealing area damage on early jumps, then repositioning away from enemies

##### Legendary+

ATK bonus activates after first enhanced strike

##### Mythic+

enhanced strike unlocks permanent haste and ATK for self and allies

##### Supreme+

assigned ally tasks grant brief ATK boost and unaffected state

### Units improving Ravion

Look for units providing: `ATK` `Haste` `Energy`  
Common buffers are **Kazim**, **Mikola**, **Smokey & Meerky**, or **Twins**.

- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Aliceth**
  - ATK (multiple targets, average)
- **Pang**
  - ATK (multiple targets, average)
- **Perseus**
  - ATK (multiple targets, average)

### Units benefitting most from Ravion

Ravion provides ATK to multiple targets `high`, Energy to multiple targets `average`, Haste (Mythic+) to multiple targets `average`, and Lifedrain (EX+10) to single targets `low` — conditional (rare).

**102** units include this provider among their top 6 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight
- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **4** strongest pairings: 

- Vala (5.0 / 5)
- Zorya (4.7 / 5)
- Indris (4.3 / 5)
- Nerion (4.2 / 5)

### Units that can act as a replacement for Ravion

**Best overall replacement**

- Lyca (53% `Debuffs on enemies` `Energy provider`)
- Thador (52% `Similar Skills` `Buffs on allies` `Energy provider`)

**Buffs on allies**

- Thador (90% `Energy`)
- Rowan (75% `Energy`)

**Similar Skills**

- Thador (72% `ally-shielder` `energy-provider` `temporary-stat-buffer`)
- Lyca (57% `energy-provider` `temporary-stat-buffer`)
- Twins (50% `ally-shielder` `energy-provider` `temporary-stat-buffer`)

**Damage**

- Aliceth (100% `Physical` `HP loss`)
- Faramor (100% `Physical` `HP loss`)
- Himmel (98% `Physical`)

**Debuffs on enemies**

- Zanie (100% `Phys DEF` `ATK`)
- Lyca (100% `Phys DEF` `ATK`)
- Kruger (80% `Phys DEF`)

**Crowd Control**

- Cyran (100% `Displace` `Knock down`)
- Eironn (100% `Displace`)
- Mehira (87% `Displace`)

### Summary for Ravion

#### Damage types dealt by Ravion

- Physical — Area, Single target
- HP loss — Single target — `average`

#### Buffs provided by Ravion

- ATK — Multiple targets — `high`
- Energy — Multiple targets — `average`
- Haste (Mythic+) — Multiple targets — `average`
- Lifedrain (EX+10) — Single target — `low` — conditional (rare)

#### Debuffs provided by Ravion

- ATK — Single target — `low`
- Phys DEF — Single target — `average`

#### Crowd Control provided by Ravion

- Unaffected — Self — On skill
- Displace — Single target — `low`
- Displace — Area — `low`
- Knock down — Single target — `low`

## Reinier

### Reinier's behavior

`AFK Stages [B]`, `Dream Realm [S]`, `Dream Realm (Endless) [A]`, `PVP [B]`

- **Signature skill**: Dynamic Balance (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `enemy-grouping` `interrupt`
- **Ally composition**: symmetrical ally-enemy tile pairs at battle start for Dynamic Balance swaps
- **Damage types**: Magic `average`

#### Play overview

Reinier swaps **symmetrical ally-enemy positions at battle start**, disrupting enemy lines before the first cast, then can **remove himself and one foe** from the field with his ultimate dimension trip for a temporary duel outside the main fight. Multi-hit attacks **knock targets airborne**, swaps **boost ally ATK or cut enemy ATK**, wound swapped enemies to take more damage, and grant damage reduction to a swapped ally for survivability. Symmetrical allies also gain **ATK while holding position**, rewarding clean mirror setups when enemy layout matches yours across the board. He is devastating when **enemy layout mirrors yours** for clean swaps, wound chains, and dimension removal on a high-value target. Misaligned formations or **targets immune to displacement** negate his opener, wound setups, and the dimension removal that defines his late-fight control.

#### Skill overview

- **Signature skill**: speed `fast`, heal `average`
- **Ultimate**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

teleport with an enemy to another dimension, removing both from battlefield

##### Skill 1

battle-start swap symmetrical ally-enemy positions

##### Skill 2

multi-hit attack knocking target into the air

##### Legendary+

position swap boosts ally ATK or reduces enemy ATK

##### Mythic+

position swap wounds enemy to take more damage, while reducing an ally's damage taken

##### Supreme+

symmetrical ally gains ATK boost while in position

### Units improving Reinier

_No synergy partners matched stat buffs or enablers._

### Units benefitting most from Reinier

Reinier provides Direct healing to single targets `low` and Damage taken (EX+10) to single targets `low`.

- Faramor (2.8 / 5)
- Bonnie (2.2 / 5)
- Himmel (2.2 / 5)

### Units that can act as a replacement for Reinier

**Best overall replacement**

- Koko (76% `Buffs on allies` `Healing`)
- Hewynn (73% `Buffs on allies` `Healing`)

**Buffs on allies**

- Koko (100% `Damage taken`)
- Shakir (100% `Damage taken`)
- Hewynn (100% `Damage taken`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Twins (100% `Direct healing` `Healing`)

**Similar Skills**

- Indris (33% `interrupt`)
- Pippa (33% `enemy-grouping`)
- Salazer (33% `interrupt`)

**Damage**

- Frieren (100% `Magic`)
- Mehira (100% `Magic`)
- Saida (100% `Magic`)

**Debuffs on enemies**

- Kulu (81% `Damage taken`)
- Pandora (64% `ATK` `Damage taken`)
- Sinbad (54% `ATK` `Damage taken`)

**Crowd Control**

- Ravion (60% `Displace` `Knock down`)
- Cyran (60% `Displace` `Knock down`)
- Lucca (60% `Interrupt` `Knock down` `Knock up`)

### Summary for Reinier

#### Damage types dealt by Reinier

- Magic — Multiple targets, Single target

#### Buffs provided by Reinier

- Direct healing — Single target — `low`
- Damage taken (EX+10) — Single target — `low`

#### Debuffs provided by Reinier

- ATK (Legendary+) — Single target — `average`
- Damage taken (Mythic+) — Single target — `average`

#### Crowd Control provided by Reinier

- Steadfast — Self — Conditional
- Unaffected — Self — Conditional
- Displace — Multiple targets — `low`
- Interrupt — Single target — `low`
- Knock up — Single target — `low`
- Knock down (Mythic+) — Single target — `low`

## Rhys

### Rhys's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Flame Barrage (ultimate)
- **Movement**: high movement (moves while attacking)
- **Behavior tags**: `aoe-damage` `self-repositioner`
- **Damage types**: Physical `high`

#### Play overview

Rhys **moves while attacking**, loading **Blast Ammo** on ultimate to enhance follow-up normals into area shots that hit multiple tiles across the field. Control immunity and crit **trigger when he takes CC**, knockback clears nearby foes, and crit damage **scales with equipped splash shots** as he kites away from melee pressure on the board. Movement loads splash shots for enhanced area attacks, and immunity skill **cooldown drops** for faster recovery between control windows so he can re-engage safely. He needs **space to kite** and time to load ammo between bursts for maximum splash output on grouped targets throughout the fight. **Pinned melee lines** or fights without movement deny his splash scaling, crit ramp, and the ammo-enhanced normals that carry his sustained damage through longer trades on the field.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `average`

##### Ultimate

Passive: move while attacking; Active: fire at enemies, loading Blast Ammo to enhance follow-up normal attacks

##### Skill 1

increase Crit and gain control immunity when taking CC

##### Skill 2

knock back nearby enemies, dealing damage

##### Legendary+

battle crit damage boost scales with splash shots equipped

##### Mythic+

movement loads splash shots for enhanced area attacks

##### Supreme+

control immunity skill cooldown reduced

### Units improving Rhys

Look for units providing: `ATK SPD / Haste` `CRIT` `CRIT DMG Boost`  
Common buffers are **Ravion**, **Smokey & Meerky**, **Thador**, or **Lorsan**.

- **Ravion**
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Thador**
  - Crit (single target, average)
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Lyca**
  - ATK SPD (all units, low) `signature fuel`
  - Energy (all units, low) `signature fuel`
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`
- **Hewynn**
  - ATK SPD via Haste (single target, average) `signature fuel`
- **Mehira**
  - ATK SPD via Haste (multiple targets, average) `signature fuel`

### Units benefitting most from Rhys

- Niru (5.0 / 5)
- Vala (2.1 / 5)
- Carolina (1.5 / 5)

### Units that can act as a replacement for Rhys

**Best overall replacement**

- Atalanta (83% `Damage` `Similar Skills` `Crowd Control`)
- Soren (73% `Damage` `Crowd Control`)
- Perseus (71% `Damage` `Crowd Control`)

**Similar Skills**

- Dionel (80% `aoe-damage` `self-repositioner`)
- Atalanta (80% `aoe-damage` `self-repositioner`)
- Himmel (66% `aoe-damage` `self-repositioner`)

**Damage**

- Gunnar (100% `Physical`)
- Gwyneth (100% `Physical`)
- Himmel (100% `Physical`)

**Crowd Control**

- Twins (100% `Knock back`)
- Aliceth (100% `Knock back`)
- Kordan (100% `Knock back`)

### Summary for Rhys

#### Damage types dealt by Rhys

- Physical — All units, Single target

#### Crowd Control provided by Rhys

- Immune — Self — Conditional
- Knock back — Single target — `low`

## Rowan

### Rowan's behavior

`AFK Stages [A]`, `Dream Realm [B]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Fatal Greed (ultimate)
- **Movement**: moving (repositions on cast)
- **Behavior tags**: `ally-healer` `energy-provider`
- **Damage types**: Magic `high`

#### Play overview

Rowan restores **energy to surrounding allies** on ultimate and places **consumable heals** that trigger when ally HP drops low for passive safety. His companion **drains enemy energy** while attacks restock heals when depleted, battle haste bonuses apply before first heal restock, and a **super heal permanently raises Phys and Magic DEF** on one ally. He places one extra heal at battle start for early protection. He is a **steady sustain and energy battery** for grouped teams that stay near his consumables. **Spread allies** or enemies that **burn heals before triggers** waste his consumable package.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, buffs `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

restore energy to surrounding allies

##### Skill 1

place consumable heals triggered when ally HP drops low

##### Skill 2

companion attacks draining energy; replenishes heals when depleted

##### Legendary+

battle haste bonus before first heal restock

##### Mythic+

place a super heal that recovers HP and permanently increases the ally's Phys and Magic DEF

##### Supreme+

place one extra heal at battle start

### Units improving Rowan

Look for units providing: `ATK` `Haste` `Max HP` `Energy`  
Common buffers are **Ravion**, **Twins**, **Kazim**, or **Mikola**.

- **Ravion**
  - ATK (multiple targets, high)
  - Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Max HP (single target, low)
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Aliceth**
  - ATK (multiple targets, average)
- **Pang**
  - ATK (multiple targets, average)
- **Perseus**
  - ATK (multiple targets, average)

### Units benefitting most from Rowan

Rowan provides Direct healing in an area `low`, Energy in an area `high`, Magic DEF (Mythic+) to single targets `average`, and Phys DEF (Mythic+) to single targets `average`.

**46** units include this provider among their top 6 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **4** strongest pairings: 

- Shemira (4.7 / 5)
- Marcille (4.4 / 5)
- Cryonaia (3.5 / 5)
- Zorya (3.3 / 5)

### Units that can act as a replacement for Rowan

**Buffs on allies**

- Thador (94% `Energy`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Twins (100% `Direct healing` `Healing`)

**Similar Skills**

- Twins (48% `ally-healer` `energy-provider`)
- Ludovic (40% `ally-healer`)
- Fay (36% `ally-healer`)

**Damage**

- Frieren (100% `Magic`)
- Saida (100% `Magic`)
- Silven (100% `Magic`)

**Debuffs on enemies**

- Saida (100% `Energy`)
- Dunlingr (100% `Energy`)
- Lily May (100% `Energy`)

### Summary for Rowan

#### Rowan Provides

- Energy steal — Single target
- Named ally on team (Supreme+) — Allies

#### Damage types dealt by Rowan

- Magic — Single target

#### Buffs provided by Rowan

- Direct healing — Area — `low`
- Energy — Area — `high`
- Magic DEF (Mythic+) — Single target — `average`
- Phys DEF (Mythic+) — Single target — `average`

#### Debuffs provided by Rowan

- Energy — Single target — `low`

## Saida

### Saida's behavior

`AFK Stages [S+]`, `Dream Realm [A]`, `Dream Realm (Endless) [A]`, `PVP [S]`

- **Signature skill**: Seed Siphon (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-shielder` `cheat-death` `high-initial-energy`
- **Damage types**: Magic `high`, DoT `average`

#### Play overview

Saida teleports to an enemy, planting a **marker that deals periodic damage and drains energy** to soften and stall the target over time. Damage dealt **heals her with excess becoming shield**, strikes **trigger nearby markers on the target**, and she can **consume a marker to revive** after defeat for a second life in longer fights on the board. Damage reduction grows with active markers, each ultimate **shortens marker DoT interval**, and battle start plants markers on nearby allies to seed the field early. She blends sustain, **energy drain, and cheat-death** when markers stay live across the fight and allies keep hers planted on the board. Teams that **clear markers or burst her before planting** deny her shield loop, revival safety, and the damage reduction scaling that keeps her standing through focused burst damage.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, debuffs `average`, damage `high`

##### Ultimate

teleport to enemy, plant marker that deals periodic damage and drains energy

##### Skill 1

Passive: heal on damage dealt, excess becomes shield; Active: damage triggers nearby markers on target

##### Skill 2

consume a planted marker to revive after defeat

##### Legendary+

damage reduction grows per active marker count

##### Mythic+

each ultimate cast shortens marker DoT interval

##### Supreme+

battle-start plant markers in nearby allies

### Units improving Saida

Look for units providing: `Max HP`

_No synergy partners matched stat buffs or enablers._

### Units benefitting most from Saida

Saida provides Shield (Supreme+) to multiple targets `high`.

**5** units include this provider among their top 6 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **4** strongest pairings: 

- Niru (5.0 / 5)
- Callan (3.0 / 5)
- Lucius (2.7 / 5)
- Daimon (2.0 / 5)

### Units that can act as a replacement for Saida

**Buffs on allies**

- Hugin (100% `Shield`)
- Thador (55% `Shield`)

**Similar Skills**

- Hepler (50% `ally-shielder` `high-initial-energy`)
- Valka (48% `ally-shielder` `high-initial-energy`)
- Hugin (33% `ally-shielder` `high-initial-energy`)

**Damage**

- Marcille (73% `Magic`)
- Sylphira (67% `Magic`)
- Cryonaia (60% `Magic` `DoT`)

**Debuffs on enemies**

- Lily May (62% `Energy`)

**Crowd Control**

- Eironn (97% `Bind` `Displace`)
- Cyran (82% `Bind` `Displace`)
- Evie (81% `Bind` `Displace`)

### Summary for Saida

#### Saida Provides

- Cheat death — Self

#### Damage types dealt by Saida

- Magic — All units, Area, Single target
- DoT — Single target

#### Buffs provided by Saida

- Shield (Supreme+) — Multiple targets — `high`

#### Debuffs provided by Saida

- Energy — Single target — `high`
- Damage dealt (Mythic+) — Single target — `low`

#### Crowd Control provided by Saida

- Unaffected — Self — On skill
- Bind — Single target — `low`
- Displace — Single target — `low`
- Interrupt — Single target — `low`
- Bind (EX+15) — All units — `low`

## Salazer

### Salazer's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Spirit Shackles (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `execute` `interrupt`
- **Damage types**: Physical `high`

#### Play overview

Salazer summons **flying swords** on ultimate while arc strikes **add bonus hits on low-HP targets** for finisher pressure against wounded marks. He deals **massive damage and imprisons** very low foes, gains battle damage reduction, and at battle start or after imprison **arc skill has no cooldown** with a guaranteed extra use for chained finishers. Imprisoning also **heals himself**, keeping him in the fight through execute windows when victims are caged. He is a **finisher who chains arcs** once a victim is imprisoned and the team has softened HP totals across the line. Without **wounded targets** or early imprison windows, his reset loop, bonus hits, and self-heal on cage never activate.

#### Skill overview

- **Signature skill**: speed `fast`, damage `average`
- **Ultimate**: speed `fast`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `high`

##### Ultimate

summon flying swords to deal damage to an enemy

##### Skill 1

arc strike; extra hit when target is low HP

##### Skill 2

deal massive damage to low-HP enemy and imprison them

##### Legendary+

battle damage taken reduction

##### Mythic+

arc skill has no cooldown at battle start or after imprisoning an enemy, with guaranteed extra use

##### Supreme+

heal self after imprisoning an enemy

### Units improving Salazer

Look for units providing: `Max HP` `Shield`

_No synergy partners matched stat buffs or enablers._

### Units benefitting most from Salazer

- Niru (3.4 / 5)
- Carolina (2.5 / 5)
- Nerion (2.3 / 5)

### Units that can act as a replacement for Salazer

**Best overall replacement**

- Cecia (73% `Damage` `Crowd Control`)
- Nara (62% `Damage`)
- Silvina (61% `Damage`)

**Similar Skills**

- Odie (40% `execute`)
- Indris (40% `interrupt`)
- Reinier (33% `interrupt`)

**Damage**

- Gwyneth (100% `Physical`)
- Himmel (100% `Physical`)
- Baelran (100% `Physical`)

**Crowd Control**

- Evie (100% `Bind`)
- Eironn (100% `Bind`)
- Arden (100% `Bind`)

### Summary for Salazer

#### Damage types dealt by Salazer

- Physical — Arc, Single target

#### Crowd Control provided by Salazer

- Bind — Single target — `high`

## Satrana

### Satrana's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Fiery Dance (ultimate)
- **Movement**: moving (avg attack range 1.5 tiles)
- **Behavior tags**: `dot-specialist` `hp-scaling` `invincibility` `life-drain`
- **Ally composition**: place allies within 2 tiles at battle start (Sparks grant)
- **Damage types**: Magic `high`

#### Play overview

Satrana goes **invincible during ultimate** while dealing continuous AoE, then arc attacks with **life drain** and Sparks that **ignite enemies for Vitality cuts and DoT** shared with allies. Battle damage reduction helps her stand through the burn setup, ignited foes **lower magic damage taken** for her team, and when all enemies burn her strike **has no cooldown limit**. She peaks once **ignites spread across the line** and her team can exploit the magic mitigation. **Cleanse or short fights** before full ignite leave her cooldown relief inactive.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `low`

##### Ultimate

invincible while dealing continuous AoE damage

##### Skill 1

arc attack gaining Life Drain

##### Skill 2

Sparks buff shared with allies ignites enemies, reducing their Vitality and dealing DoT

##### Legendary+

battle damage taken reduction

##### Mythic+

ignite enemies to reduce magic damage taken for self and allies

##### Supreme+

strike has no cooldown limit when all enemies are ignited

### Units improving Satrana

Look for units providing: `Max HP`  
Common buffers are **Pandora**, **Thador**, **Rowan**, or **Ravion**.

- **Pandora**
  - Max HP (single target, low)
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Ravion**
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Phraesto**
  - Energy via Energy recovery speed (contract ally, start of battle) `signature fuel`
- **Lyca**
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`

### Units benefitting most from Satrana

Satrana provides Magic damage (Mythic+) to single targets `average` and Damage taken (EX+10) to single targets `low`.

- Bonnie (3.4 / 5)
- Carolina (2.0 / 5)
- Nerion (1.8 / 5)

### Units that can act as a replacement for Satrana

**Similar Skills**

- Zorya (60% `hp-scaling` `life-drain`)
- Brutus (34% `invincibility` `life-drain`)
- Faramor (33% `dot-specialist` `hp-scaling`)

**Damage**

- Silven (100% `Magic`)
- Sylphira (100% `Magic`)
- Shemira (100% `Magic`)

**Debuffs on enemies**

- Alna (100% `Vitality`)
- Dunlingr (100% `Vitality`)
- Pandora (100% `Vitality`)

**Crowd Control**

- Mehira (100% `Charm`)

### Summary for Satrana

#### Satrana Provides

- Ally DoT on enemies — Area
- Ally grant (Sparks) — Area
- Invincibility — Self

#### Damage types dealt by Satrana

- Magic — Area, Single target
- Max HP-based damage — Single target

#### Buffs provided by Satrana

- Magic damage (Mythic+) — Single target — `average`
- Damage taken (EX+10) — Single target — `low`

#### Debuffs provided by Satrana

- Vitality — Multiple targets — `low`

#### Crowd Control provided by Satrana

- Charm — Single target — `average`

## Scarlita

### Scarlita's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Divine Wrath (Mythic+)
- **Movement**: moving (brief reposition)
- **Behavior tags**: `ally-shielder` `aoe-damage` `execute` `hp-scaling` `non-ult-utility`
- **Damage types**: Physical `high`

#### Play overview

Scarlita slashes the ground to **send a wave that knocks foes to the edge**, then charges to **knock down survivors** for a two-step displacement combo across the battlefield. Airborne charges **build power for landing AoE stun**, weakest allies gain shields while she is airborne, and each shield sent **stacks execution potential** for later burst. Enough living allies let her **deal true damage**, and shielded allies also gain Phys and Magic DEF from her protection during air time. She needs **clustered enemies for the wave** and air time to charge before landing on grouped targets across the battlefield. **Sparse formations or burst that grounds her early** waste her knockdown follow-through, execution stacks, and true damage payoff.

#### Skill overview

- **Signature skill**: speed `fast`
- **Ultimate**: speed `average`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `high`

##### Ultimate

slash ground to create wide wave knocking enemies to edge, then charge to knock down targets

##### Skill 1

charge power while airborne, then descend to deal AoE damage and stun

##### Skill 2

grant weakest ally a shield while airborne, deal AoE damage on landing

##### Legendary+

gain execution stacks for each shield sent while airborne

##### Mythic+

deal true damage when enough allied heroes are alive

##### Supreme+

shielding an ally also increases their Phys and Magic DEF

### Units improving Scarlita

Look for units providing: `ATK` `Execution` `Energy`  
Common buffers are **Ravion**, **Contess**, **Evie**, or **Mikola**.

- **Aliceth**
  - ATK (multiple targets, average)
- **Pang**
  - ATK (multiple targets, average)
- **Perseus**
  - ATK (multiple targets, average)
- **Fay**
  - ATK (arc, low)
- **Hammie**
  - ATK (single target, low)
- **Koko**
  - ATK (all units, low)

### Units benefitting most from Scarlita

Scarlita provides Shield (Supreme+) to single targets `low`.

- Kazim (3.4 / 5)

### Units that can act as a replacement for Scarlita

**Buffs on allies**

- Contess (100% `Shield`)
- Hugin (100% `Shield`)
- Saida (100% `Shield`)

**Similar Skills**

- Korin (48% `ally-shielder` `hp-scaling`)
- Aliceth (48% `execute` `hp-scaling` `non-ult-utility`)
- Daimon (42% `ally-shielder` `hp-scaling` `non-ult-utility`)

**Damage**

- Gwyneth (100% `Physical`)
- Himmel (100% `Physical`)
- Baelran (100% `Physical`)

**Crowd Control**

- Lorsan (64% `Stun`)
- Lucca (53% `Stun` `Knock up` `Knock down`)

### Summary for Scarlita

#### Scarlita Provides

- Invincibility — Self

#### Damage types dealt by Scarlita

- Physical — All units, Arc, Area

#### Buffs provided by Scarlita

- Shield (Supreme+) — Single target — `low`

#### Crowd Control provided by Scarlita

- Unaffected — Self — Conditional
- Knock back — All units — `low`
- Knock down — Arc — `low`
- Knock up — Area — `low`
- Stun — Arc — `average`
- Stun — Area — `average`

## Seth

### Seth's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Shadow Strike (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `assassin` `life-drain`
- **Damage types**: Physical `average`, HP loss `high`

#### Play overview

Seth flashes to a foe for **multi-hit ultimate damage**, then pounces on the **weakest nearby enemy** for repeated assassin pressure between casts. Low enemy HP **grants stat bonuses**, battle ATK rises, and each non-summon defeat **resets pounce cooldown and refunds energy** to chain kills across the fight. Pounce also **shreds extra Phys DEF** when he carries a specific buff, opening tankier targets for follow-up from allies. He chains **assassin resets** in fights with frequent kills and accessible weak marks on the board. Without **finishes or accessible weak targets**, his pounce loop and stat spikes stall out before he can snowball through the enemy line in longer fights.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, heal `average`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

flash to an enemy and deal multiple attacks

##### Skill 1

pounce on weakest nearby enemy, dealing damage

##### Skill 2

gain stat bonuses when an enemy HP is low

##### Legendary+

battle ATK increase

##### Mythic+

reset pounce cooldown and recover energy on each non-summoned enemy defeat

##### Supreme+

pounce reduces extra Phys DEF when carrying specific buff

### Units improving Seth

Look for units providing: `ATK` `Haste` `CRIT` `Energy` `Physical DEF`  
Common buffers are **Mikola**, **Ravion**, **Rowan**, or **Twins**.

- **Ravion**
  - ATK (multiple targets, high)
  - Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Phys DEF (single target, average)
  - Magic DEF (single target, average)
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Thador**
  - Crit (single target, average)
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Niru**
  - Phys DEF (single target, high)
  - Magic DEF (single target, high)
- **Tilaya**
  - DEF (area, high)
  - DEF (area, high)
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Seth

- Carolina (1.5 / 5)
- Nerion (1.4 / 5)
- Indris (1.3 / 5)

### Units that can act as a replacement for Seth

**Best overall replacement**

- Harak (68% `Damage` `Similar Skills`)
- Faramor (55% `Damage`)
- Athalia (52% `Damage`)

**Similar Skills**

- Harak (80% `assassin` `life-drain`)
- Shakir (40% `life-drain`)
- Kruger (40% `life-drain`)

**Damage**

- Himmel (100% `Physical`)
- Faramor (100% `Physical` `HP loss`)
- Athalia (100% `Physical`)

**Debuffs on enemies**

- Gwyneth (100% `Phys DEF`)
- Thador (100% `Phys DEF`)
- Velara (100% `Phys DEF`)

**Crowd Control**

- Gwyneth (100% `Bind`)
- Saida (100% `Bind`)
- Alna (100% `Bind`)

### Summary for Seth

#### Seth Provides

- Invincibility — Single target
- Stacking — Single target

#### Damage types dealt by Seth

- Physical — Single target
- HP loss — Single target — `high`

#### Debuffs provided by Seth

- Phys DEF (Supreme+) — Single target — `low`

#### Crowd Control provided by Seth

- Bind — Single target — `low`

## Shadewing

### Shadewing's behavior

`AFK Stages [A+]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Withering Curse (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `dot-specialist` `enemy-debuffer`
- **Damage types**: Magic `low`, DoT `low`, HP loss `low`

#### Play overview

Shadewing applies **sustained DoT scaling on target lost HP** with his ultimate, then dual strikes plus **wound DoT** while converting enemy damage taken into **curse value for a heavy lash** at threshold. Battle ATK climbs, trigger hits **build energy and permanent damage**, and at start he **drains ally HP for lasting ATK and shield** to front-load his scaling. He needs **allies willing to pay the opening HP cost** and sustained damage across the team to fill curse quickly enough for the lash to land on priority targets in longer fights. **Short fights or allies that cannot spare HP** blunt his scaling lash, energy buildup, and self-buff loop across longer fights on the board.

#### Skill overview

- **Signature skill**: speed `fast`, buffs `average`, debuffs `average`
- **Ultimate**: speed `slow`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `low`

##### Ultimate

sustained DoT per second scaling on target lost HP

##### Skill 1

dual strike then sustained wound DoT

##### Skill 2

convert continuous damage taken by enemies into curse value; at threshold, lash out for heavy damage

##### Legendary+

battle ATK increase

##### Mythic+

trigger hits build energy and permanent damage boost

##### Supreme+

drain ally HP at start for lasting ATK boost and shield

### Units improving Shadewing

Look for units providing: `ATK` `Shield` `Energy`  
Common buffers are **Smokey & Meerky**, **Pandora**, **Mikola**, or **Contess**.

Shadewing also requires units **dealing continuous damage** to enemies

- **Smokey & Meerky**
  - ATK (area, average)
  - Energy (area, low) `signature fuel`
  - Enables Continuous damage on enemies via DoT
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Enables Continuous damage on enemies via persistent zone
- **Alna**
  - Enables Continuous damage on enemies via persistent zone
- **Frieren**
  - Enables Continuous damage on enemies via DoT + Burn
- **Tasi**
  - Enables Continuous damage on enemies via DoT
- **Viperian**
  - Enables Continuous damage on enemies via persistent zone

### Units benefitting most from Shadewing

- Bonnie (1.6 / 5)
- Indris (1.5 / 5)

### Units that can act as a replacement for Shadewing

**Similar Skills**

- Nerion (96% `dot-specialist` `enemy-debuffer`)
- Kruger (40% `enemy-debuffer`)
- Odie (33% `dot-specialist`)

**Damage**

- Mehira (100% `Magic` `DoT`)
- Dunlingr (100% `Magic` `DoT` `HP loss`)
- Niru (100% `Magic` `HP loss`)

**Debuffs on enemies**

- Thador (100% `Magic DEF` `Phys DEF`)
- Eironn (100% `Magic DEF`)
- Cassadee (100% `Magic DEF`)

### Summary for Shadewing

#### Shadewing Provides

- Debuff application — Single target
- DoT conversion — Single target
- Invincibility — Self
- Damage leech from allies (Supreme+) — Single target

#### Damage types dealt by Shadewing

- Magic — Single target
- DoT — Single target
- HP loss — Single target — `low`

#### Debuffs provided by Shadewing

- Magic DEF — Single target — `low`
- Phys DEF — Single target — `low`

## Shakir

### Shakir's behavior

`AFK Stages [A]`, `Dream Realm [B]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Ravaging Claws (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `life-drain` `temporary-stat-buffer`
- **Damage types**: Physical `high`

#### Play overview

Shakir **transforms into Wolf Form** to reshape his combat kit, trading single-target strikes for **frontal AoE cleaves** and sustained pressure. In form he gains **Ranged DEF and Life Drain**, helping him survive ranged fire while staying on enemies. His **damage reduction scales with aura allies**, so he peaks when teammates cluster inside his influence zone. A lower **energy threshold sustains transformation** longer, keeping wolf pressure online through extended fights. Third hit also **shaves enemy vitality**, softening targets for follow-up damage. Against **spread lines** or teams that deny his landing zone, wolf uptime and aura scaling stall out.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `low`

##### Ultimate

transform into wolf form, enhancing combat capabilities

##### Skill 1

three consecutive AoE strikes while in Wolf Form

##### Skill 2

gain Ranged DEF and Life Drain while in Wolf Form

##### Legendary+

battle damage taken reduction grows with aura allies

##### Mythic+

transformation sustained at lower energy threshold

##### Supreme+

third hit reduces target vitality

### Units improving Shakir

Look for units providing: `Haste` `Max HP`  
Common buffers are **Pandora**, **Ravion**, **Twins**, or **Smokey & Meerky**.

- **Pandora**
  - Max HP (single target, low)
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Ravion**
  - Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Thador**
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Zandrok**
  - Haste (area, average, conditional (frequent)) `signature fuel`
  - Max HP (multiple targets, low)
- **Phraesto**
  - Energy via Energy recovery speed (contract ally, start of battle) `signature fuel`

### Units benefitting most from Shakir

Shakir provides Damage taken in an area `low` and Haste in an area `average`.

- Mehira (3.5 / 5)
- Dionel (2.4 / 5)
- Lenya (2.4 / 5)

### Units that can act as a replacement for Shakir

**Best overall replacement**

- Nara (61% `Damage` `Debuffs on enemies` `Crowd Control`)
- Kordan (56% `Crowd Control` `Damage`)
- Kazim (50% `Damage` `Crowd Control`)

**Buffs on allies**

- Smokey & Meerky (63% `Haste`)
- Lorsan (63% `Haste`)
- Twins (52% `Haste`)

**Similar Skills**

- Kruger (48% `life-drain`)
- Mehira (40% `life-drain` `temporary-stat-buffer`)
- Zorya (40% `life-drain`)

**Damage**

- Gwyneth (100% `Physical`)
- Baelran (100% `Physical`)
- Aliceth (100% `Physical`)

**Debuffs on enemies**

- Frieren (100% `Vitality`)
- Gunnar (100% `Vitality`)
- Gwyneth (100% `Vitality`)

**Crowd Control**

- Frieren (100% `Knock up`)
- Baelran (100% `Knock up`)
- Kordan (100% `Knock up`)

### Summary for Shakir

#### Shakir Provides

- Transformation — Self

#### Damage types dealt by Shakir

- Physical — Area, Single target

#### Buffs provided by Shakir

- Damage taken — Area — `low`
- Haste — Area — `average`

#### Debuffs provided by Shakir

- Vitality (Supreme+) — Single target — `low`

#### Crowd Control provided by Shakir

- Unaffected — Self — Form
- Knock up — Single target — `low`

## Shemira

### Shemira's behavior

`AFK Stages [A+]`, `Dream Realm [A]`, `Dream Realm (Endless) [A]`, `PVP [A]`

- **Signature skill**: Phantom Procession (ultimate)
- **Movement**: mostly stationary (avg attack range 4.0 tiles)
- **Behavior tags**: `high-damage-ult` `hp-scaling`
- **Damage types**: Magic `high`, Max HP-based damage `low`

#### Play overview

Shemira **sacrifices HP to fuel damage**, firing orb lines and AoE bursts as her health pool shrinks. She **summons ghosts** to bombard random enemies, and each hero defeat **spawns an extra summon** to widen pressure. Energy recovery from attacks **scales with summon count**, rewarding teams that keep bodies on the field. When summons expire, **remaining power converts to all-enemy damage** for a closing burst. She needs **healing to cycle sacrifices** safely. Without sustain or summons, her HP costs leave her exposed quickly.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, debuffs `average`, damage `high`

##### Ultimate

summon ghosts to bombard random enemies

##### Skill 1

HP sacrifice fires orb line, dealing area damage

##### Skill 2

sacrifice HP to deal damage; sacrifice summons for extra AoE damage

##### Legendary+

battle energy recovery from attacks grows with summon count

##### Mythic+

summon expiry converts remaining power to all-enemy damage

##### Supreme+

each hero defeat spawns an extra summon

### Units improving Shemira

Look for units providing: `Shield` `Energy`  
Common buffers are **Pandora**, **Thador**, **Rowan**, or **Ravion**.

- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Ravion**
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Lyca**
  - Energy (all units, low) `signature fuel`
  - ATK SPD (all units, low) `signature fuel`
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`
- **Niru**
  - Named ally grant: Phys DEF (high)
  - Named ally grant: Magic DEF (high)

### Units benefitting most from Shemira

- Niru (4.2 / 5)
- Bonnie (2.6 / 5)
- Vala (1.9 / 5)

### Units that can act as a replacement for Shemira

**Best overall replacement**

- Natsu (69% `Damage` `Debuffs on enemies`)
- Sylphira (64% `Damage` `Debuffs on enemies`)
- Silven (51% `Damage`)

**Similar Skills**

- Baelran (50% `hp-scaling`)
- Nazrik (40% `hp-scaling`)
- Zorya (40% `hp-scaling`)

**Damage**

- Silven (100% `Magic`)
- Sylphira (100% `Magic`)
- Ludovic (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Baelran (100% `Max HP`)
- Sylphira (100% `Max HP`)
- Nazrik (100% `Max HP`)

### Summary for Shemira

#### Damage types dealt by Shemira

- Magic — Area, Single target
- Max HP-based damage — Area, Single target — `low`

#### Debuffs provided by Shemira

- Max HP (EX+10) — Single target — `low`

## Silven

### Silven's behavior

`AFK Stages [S]`, `Dream Realm [S]`, `Dream Realm (Endless) [A+]`, `PVP [A+]`

- **Signature skill**: Gravity Collapse (Skill 1)
- **Movement**: stationary (avg attack range 12.0 tiles)
- **Behavior tags**: `high-initial-energy` `hp-scaling` `mark-target` `non-ult-utility`
- **Damage types**: Magic `high`

#### Play overview

Silven builds damage around **flying blade summons** and marks that detonate when she knocks foes down. Her ultimate launches **blade volleys** at enemies, while a field skill **enhances blade output** for sustained AoE pressure. Receiving ally buffs grants her **energy, penetration, and ATK SPD**, so she rewards supportive teammates. She deals **bonus damage to high-HP-ratio targets**, making her strong against bulky frontliners. Battle **ATK speed growth** adds steady personal scaling over long fights. Against **immune or unmarked targets**, her detonation chain and blade field underdeliver.

#### Skill overview

- **Signature skill**: speed `fast`, damage `high`
- **Ultimate**: speed `fast`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `high`

##### Ultimate

summon flying blades to attack enemies

##### Skill 1

knock down enemy and detonate marks on them

##### Skill 2

set up a field that enhances flying blades

##### Legendary+

battle ATK speed increase

##### Mythic+

receiving ally buff grants energy, penetration, and ATK SPD

##### Supreme+

deal bonus damage to enemies with high HP ratio

### Units improving Silven

Look for units providing: `ATK SPD / Haste` `Energy` `DEF Penetration` `Physical DEF`  
Common buffers are **Mikola**, **Dunlingr**, **Hugin**, or **Smokey & Meerky**.

Silven also requires units **buffing them**

- **Isabella**
  - ATK SPD via Haste (single target, low) `signature fuel`
  - Phys DEF (single target, low)
  - Grants 6 distinct temporary stat buffs to Silven
- **Niru**
  - Phys DEF (single target, high)
  - Grants 2 distinct temporary stat buffs to Silven (start of battle)
- **Kordan**
  - DEF Penetration (area, high)
  - Grants 2 distinct temporary stat buffs to Silven
- **Perseus**
  - Grants 3 distinct temporary stat buffs to Silven
- **Aliceth**
  - DEF Penetration (multiple targets, high)
  - Grants 1 distinct temporary stat buff to Silven
- **Koko**
  - Grants 2 distinct temporary stat buffs to Silven

### Units benefitting most from Silven

- Carolina (2.0 / 5)
- Nerion (1.8 / 5)
- Bonnie (1.6 / 5)

### Units that can act as a replacement for Silven

**Best overall replacement**

- Sylphira (68% `Damage` `Crowd Control`)

**Similar Skills**

- Athalia (48% `hp-scaling` `non-ult-utility`)
- Aliceth (37% `hp-scaling` `mark-target` `non-ult-utility`)
- Kordan (28% `high-initial-energy` `hp-scaling`)

**Damage**

- Sylphira (100% `Magic`)
- Shemira (100% `Magic`)
- Ludovic (100% `Magic`)

**Crowd Control**

- Frieren (100% `Knock down`)
- Himmel (100% `Knock down`)
- Baelran (100% `Knock down`)

### Summary for Silven

#### Damage types dealt by Silven

- Magic — Single target
- Max HP-based damage — Single target

#### Crowd Control provided by Silven

- Knock down — Single target — `average`

## Silvina

### Silvina's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: First Strike (Skill 1)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `assassin` `battle-start-burst` `interrupt` `mark-target`
- **Self placement**: nearest symmetrical enemy at battle start (Falling Blossom / First Strike openers)
- **Damage types**: Physical `average`

#### Play overview

Silvina opens by **dashing to the closest symmetrical enemy**, landing burst damage before normal pacing resumes. At battle start she swaps to **rapid strikes** briefly and gains a shield for early survivability. Her ultimate strikes the **highest-energy enemy**, dealing damage and **draining their energy** to disrupt casters before they can fire. Battle crit growth adds finishing pressure, and rapid hits **reduce target vitality** for softer kills. She excels as an **opening assassin** who punishes backline energy hoarders and symmetrical formations. She falters when symmetrical targets are absent, when burst windows end before she reaches priority foes, or when enemies deny her opening dash entirely.

#### Skill overview

- **Signature skill**: speed `fast`, damage `average`
- **Ultimate**: speed `fast`, debuffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, damage `average`

##### Ultimate

strike the highest-energy enemy, dealing damage and reducing their energy

##### Skill 1

dash to closest symmetrical enemy at battle start, dealing damage

##### Skill 2

normal attacks replaced by rapid strikes briefly at battle start

##### Legendary+

battle crit increase

##### Mythic+

gain a shield at battle start

##### Supreme+

rapid attack hits also reduce target vitality

### Units improving Silvina

Look for units providing: `Shield` `CRIT`

- **Thador**
  - Crit (single target, average)

### Units benefitting most from Silvina

- Carolina (3.7 / 5)
- Nerion (3.2 / 5)
- Indris (1.5 / 5)

### Units that can act as a replacement for Silvina

**Best overall replacement**

- Salazer (74% `Damage`)
- Hodgkin (73% `Damage` `Debuffs on enemies`)
- Perseus (62% `Damage`)

**Similar Skills**

- Sinbad (40% `assassin` `mark-target`)
- Salazer (28% `interrupt`)
- Dunlingr (28% `battle-start-burst` `interrupt`)

**Damage**

- Gunnar (100% `Physical`)
- Gwyneth (100% `Physical`)
- Himmel (100% `Physical`)

**Debuffs on enemies**

- Dunlingr (100% `Energy` `Vitality`)
- Pippa (100% `Energy`)
- Hodgkin (96% `Energy` `Vitality`)

**Crowd Control**

- Berial (81% `Frighten`)

### Summary for Silvina

#### Silvina Provides

- Marked target (focus fire) — Single target
- Marked target (focus fire) (EX+10) — Area

#### Damage types dealt by Silvina

- Physical — Single target

#### Debuffs provided by Silvina

- Energy — Single target — `high`
- Vitality (Supreme+) — Single target — `low`

#### Crowd Control provided by Silvina

- Stun — Single target — `high`
- Frighten (EX+10) — Area — `average`

## Sinbad

### Sinbad's behavior

`AFK Stages [B]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Whizzing Edge (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `assassin` `enemy-debuffer` `mark-target`
- **Damage types**: Physical `high`

#### Play overview

Sinbad **marks the top attacker and top damage-taker**, then focuses fire on those roles with **enhanced damage against marked roles**. His ultimate delivers **multiple rapid hits** to a single target for concentrated burst pressure. A skill attacks the target twice, and his debuff **adapts to enemy combat role** for flexible disruption on each mark. Battle **ATK speed growth** keeps his rotation moving through longer fights. He is a **role-targeting specialist** who shines when enemy teams have clear carries to isolate. Against evenly distributed damage or mark-immune lines, his priority targeting adds little value.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `average`
- **Non-ultimate**: speed `fast`, debuffs `average`, damage `high`

##### Ultimate

deal multiple rapid damage hits to the enemy

##### Skill 1

mark the top attacker and top damage-taker as priority targets

##### Skill 2

attack target twice

##### Legendary+

battle ATK speed increase

##### Mythic+

debuff adapts to enemy combat role

##### Supreme+

enhanced damage against marked enemy roles

### Units improving Sinbad

Look for units providing: `ATK SPD / Haste` `Energy`  
Common buffers are **Ravion**, **Pandora**, **Thador**, or **Rowan**.

- **Ravion**
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Lyca**
  - ATK SPD (all units, low) `signature fuel`
  - Energy (all units, low) `signature fuel`
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`
- **Hewynn**
  - ATK SPD via Haste (single target, average) `signature fuel`

### Units benefitting most from Sinbad

- Indris (4.8 / 5)

### Units that can act as a replacement for Sinbad

**Similar Skills**

- Kafra (72% `assassin` `enemy-debuffer` `mark-target`)
- Silvina (40% `assassin` `mark-target`)
- Shadewing (30% `enemy-debuffer`)

**Damage**

- Gwyneth (100% `Physical`)
- Himmel (100% `Physical`)
- Baelran (100% `Physical`)

**Debuffs on enemies**

- Cassadee (54% `Magic DEF`)
- Shadewing (54% `Magic DEF` `Phys DEF`)
- Evie (51% `Magic DEF`)

### Summary for Sinbad

#### Sinbad Provides

- Marked target (focus fire) — Single target

#### Damage types dealt by Sinbad

- Physical — Single target

#### Debuffs provided by Sinbad

- Damage taken — Single target — `low`
- ATK SPD (Mythic+) — Single target — `low`
- Energy (Mythic+) — Single target — `low`
- Magic DEF (Mythic+) — Multiple targets — `average`
- Phys DEF (Mythic+) — Multiple targets — `low`
- Vitality (Mythic+) — Multiple targets — `low`
- ATK (EX+10) — Single target — `low`

#### Crowd Control provided by Sinbad

- Unaffected — Self — Conditional

## Smokey & Meerky

### Smokey & Meerky's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [S]`, `PVP [C]`

- **Signature skill**: Special Aroma (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-healer` `aoe-healing` `temporary-stat-buffer`
- **Damage types**: Magic `low`

#### Play overview

Smokey and Meerky anchor fights with a **continuous healing aura** that levels up with each active cast, deepening recovery over time. Allies inside gain **ATK and energy recovery**, while a separate skill **instant-heals everyone** within the zone on demand. ATK boost **grows with ally count inside the aura**, rewarding clustered formations that stay in range. The third aura upgrade also **increases damage dealt to enemies**, blending offense with sustain in one slot. Extra healing on each aura use **stacks recovery** over repeated casts. They underperform when allies **cannot stay inside the zone** or when fights end before aroma levels build.

#### Skill overview

- **Signature skill (ult)**: speed `average`, heal `average`, buffs `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`

##### Ultimate

create continuous healing aura, each active cast leveling up the aroma

##### Skill 1

boost ATK and recover energy for allies within the aura

##### Skill 2

instant heal all allies inside aura

##### Legendary+

ATK boost grows with more allies inside aura

##### Mythic+

third aura upgrade increases damage dealt to enemies

##### Supreme+

extra healing on each aura use

### Units improving Smokey & Meerky

Look for units providing: `ATK` `Energy`  
Common buffers are **Ravion**, **Pandora**, **Contess**, or **Evie**.

- **Ravion**
  - ATK (multiple targets, high)
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Aliceth**
  - ATK (multiple targets, average)
- **Pang**
  - ATK (multiple targets, average)

### Units benefitting most from Smokey & Meerky

Smokey & Meerky provides ATK in an area `average`, Direct healing in an area `high`, Energy in an area `low`, Haste in an area `average`, and Healing over time in an area `high`.

**92** units include this provider among their top 6 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight
- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner

These are the **4** strongest pairings: 

- Zorya (5.0 / 5)
- Nerion (4.3 / 5)
- Dionel (4.2 / 5)
- Perseus (4.0 / 5)

### Units that can act as a replacement for Smokey & Meerky

**Buffs on allies**

- Twins (63% `Haste` `ATK` `Energy`)

**Healing**

- Solise (100% `Direct healing` `Healing over time` `Healing`)
- Hewynn (71% `Healing over time` `Direct healing` `Healing`)

**Similar Skills**

- Fay (100% `ally-healer` `aoe-healing` `temporary-stat-buffer`)
- Hewynn (100% `ally-healer` `aoe-healing` `temporary-stat-buffer`)
- Velara (90% `ally-healer` `aoe-healing` `temporary-stat-buffer`)

**Crowd Control**

- Frieren (100% `Stun`)
- Gunnar (100% `Stun`)
- Contess (100% `Stun`)

### Summary for Smokey & Meerky

#### Damage types dealt by Smokey & Meerky

- DoT — Area

#### Buffs provided by Smokey & Meerky

- ATK — Area — `average`
- Direct healing — Area — `high`
- Energy — Area — `low`
- Haste — Area — `average`
- Healing over time — Area — `high`

#### Crowd Control provided by Smokey & Meerky

- Stun (Mythic+) — Area — `low`

## Solise

### Solise's behavior

`AFK Stages [S]`, `Dream Realm [S]`, `Dream Realm (Endless) [S]`, `PVP [S]`

- **Signature skill**: Life's Embrace (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-healer` `ally-shielder` `aoe-healing`
- **Damage types**: Magic `low`

#### Play overview

Solise attaches **healing companions** to each non-summoned ally, then blooms them into **enhanced forms** for extra pressure. Her ultimate **continuously heals all allies** while companions deal **damage to all enemies**. Weakest allies receive direct heals and shields when a companion is present on them. Excess healing is **absorbed by companions** to unlock additional buffs for their hosts. Companion damage **scales on stored excess healing**, turning overheal into offense. She needs **clustered allies and fight time**; spread lines or early burst waste her companion setup.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, heal `average`, damage `low`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`

##### Ultimate

continuously heal all allies; companions deal damage to all enemies

##### Skill 1

attach healing companion to each non-summoned ally, which can bloom into enhanced form

##### Skill 2

heal weakest allies; grant shield if companion is present

##### Legendary+

ATK increased further when companion present

##### Mythic+

companion absorbs excess healing to unlock additional buffs for host

##### Supreme+

companion damage scales on stored excess healing

### Units improving Solise

Look for units providing: `ATK`  
Common buffers are **Ravion**, **Contess**, **Evie**, or **Kazim**.

- **Ravion**
  - ATK (multiple targets, high)
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Aliceth**
  - ATK (multiple targets, average)
- **Pang**
  - ATK (multiple targets, average)
- **Thador**
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`

### Units benefitting most from Solise

Solise provides ATK to single targets `low`, Direct healing to all units `high`, Healing over time to single targets `average`, DEF (Mythic+) to single targets `low`, and Magic DEF (Mythic+) to single targets `low`.

- Bonnie (5.0 / 5)
- Niru (5.0 / 5)
- Phraesto (2.1 / 5)

### Units that can act as a replacement for Solise

**Buffs on allies**

- Twins (85% `ATK` `Magic DEF`)
- Isabella (85% `ATK` `Magic DEF`)
- Perseus (71% `ATK` `Magic DEF`)

**Healing**

- Smokey & Meerky (83% `Direct healing` `Healing over time` `Healing`)

**Similar Skills**

- Velara (100% `ally-healer` `ally-shielder` `aoe-healing`)
- Smokey & Meerky (60% `ally-healer` `aoe-healing`)
- Hepler (50% `ally-healer` `ally-shielder`)

**Damage**

- Frieren (100% `Magic`)
- Mehira (100% `Magic`)
- Twins (100% `Magic`)

### Summary for Solise

#### Solise Provides

- Ally blessing (Mythic+) — Single target

#### Damage types dealt by Solise

- Magic — All units

#### Buffs provided by Solise

- ATK — Single target — `low`
- Direct healing — All units — `high`
- Healing over time — Single target — `average`
- DEF (Mythic+) — Single target — `low`
- Magic DEF (Mythic+) — Single target — `low`

#### Crowd Control provided by Solise

- Unaffected — Self — On skill

## Sonja

### Sonja's behavior

`AFK Stages [B]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [B]`

- **Signature skill**: Crimson Covenant (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-buffer` `aoe-damage` `temporary-stat-buffer`
- **Ally composition**: place allies on left and right at battle start (Crimson Covenant buffs; prioritizes front row)
- **Damage types**: Physical `average`

#### Play overview

Sonja forms a **pact with left and right allies at battle start**, continuously raising their stats while all three remain alive. Her ultimate delivers **multi-hit damage** then charges through a frontal area, converting a portion of damage dealt to **self-healing**. She also **stuns nearby enemies twice** with her area skill for soft control at the front. Enhanced bond accumulates bonuses over time while partners survive, and battle **haste growth** keeps her rotation fluid. She is a **frontline buffer** who needs flanking allies to realize her pact value. Without adjacent partners or dense enemy clusters, her buffs and stun swings underwhelm.

#### Skill overview

- **Signature skill**: speed `fast`, buffs `average`
- **Ultimate**: speed `fast`, buffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `low`

##### Ultimate

multi-hit then charge through frontal area

##### Skill 1

form pact with left and right allies at battle start, continuously increasing their stats

##### Skill 2

deal damage and stun nearby enemies twice

##### Legendary+

battle haste increase

##### Mythic+

enhanced bond continuously accumulates bonuses while partners live

##### Supreme+

ultimate converts portion of damage dealt to self-healing

### Units improving Sonja

Look for units providing: `ATK` `Haste` `Max HP`  
Common buffers are **Twins**, **Mikola**, **Ravion**, or **Kazim**.

- **Aliceth**
  - ATK (multiple targets, average)
- **Pang**
  - ATK (multiple targets, average)
- **Perseus**
  - ATK (multiple targets, average)
- **Zandrok**
  - Haste (area, average, conditional (frequent)) `signature fuel`
  - Max HP (multiple targets, low)
- **Isabella**
  - ATK (single target, low, conditional (frequent))
  - Haste (single target, low) `signature fuel`
- **Hewynn**
  - Haste (single target, average) `signature fuel`

### Units benefitting most from Sonja

Sonja provides ATK to multiple targets `average` and Magic DEF to multiple targets `low`.

**32** units include this provider among their top 6 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **4** strongest pairings: 

- Lily May (3.4 / 5)
- Perseus (3.3 / 5)
- Dionel (3.1 / 5)
- Vala (3.0 / 5)

### Units that can act as a replacement for Sonja

**Best overall replacement**

- Perseus (66% `Similar Skills` `Crowd Control`)
- Mikola (55% `Buffs on allies` `Similar Skills`)

**Buffs on allies**

- Mikola (100% `Magic DEF` `ATK`)
- Niru (68% `Magic DEF`)
- Evie (62% `ATK`)

**Similar Skills**

- Perseus (100% `ally-buffer` `aoe-damage` `temporary-stat-buffer`)
- Parisa (75% `ally-buffer` `aoe-damage` `temporary-stat-buffer`)
- Tilaya (66% `aoe-damage` `temporary-stat-buffer`)

**Damage**

- Gunnar (100% `Physical`)
- Gwyneth (100% `Physical`)
- Himmel (100% `Physical`)

**Crowd Control**

- Contess (100% `Stun`)
- Gwyneth (100% `Stun`)
- Aliceth (100% `Stun`)

### Summary for Sonja

#### Damage types dealt by Sonja

- Physical — Area, Single target

#### Buffs provided by Sonja

- ATK — Multiple targets — `average`
- Magic DEF — Multiple targets — `low`

#### Crowd Control provided by Sonja

- Stun — Single target — `low`

## Soren

### Soren's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Whirlwind Swing (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `counterattack` `self-repositioner`
- **Damage types**: Physical `high`

#### Play overview

Soren rushes targets with **knockback and stun on collision**, using melee strikes to shove enemies into walls or allies for extra damage and control. His block skill **absorbs a powerful incoming attack** and resets knockback cooldown, enabling repeated displacement chains through the fight. Low HP triggers a **haste boost plus HP and energy recovery**, helping him recover after heavy trades and stay in the brawl longer. When block triggers, his next melee skill gains **extended knockback and bonus damage** for a punishing follow-up strike on clustered foes. Battle **haste growth** keeps his repositioning active through longer engagements without slowing down. He struggles against **knockback-immune targets** or enemies who burst him down before his block cycle can activate and reset his knockback pressure entirely.

#### Skill overview

- **Signature skill (ult)**: speed `average`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `average`

##### Ultimate

rush to target, knocking back nearby enemies and stunning them on collision

##### Skill 1

melee knock back; collision deals extra damage and stuns

##### Skill 2

block a powerful attack, resetting the knock back skill cooldown

##### Legendary+

combat haste increase

##### Mythic+

low HP triggers haste boost and HP and energy recovery

##### Supreme+

extended knock back on next melee skill when block triggers, dealing extra damage

### Units improving Soren

Look for units providing: `Haste` `Max HP` `Energy`  
Common buffers are **Ravion**, **Pandora**, **Twins**, or **Smokey & Meerky**.

- **Ravion**
  - Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Max HP (single target, low)
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Zandrok**
  - Haste (area, average, conditional (frequent)) `signature fuel`
  - Max HP (multiple targets, low)
  - ATK SPD via Haste (area, average, conditional (frequent)) `signature fuel`
- **Hewynn**
  - Haste (single target, average) `signature fuel`
  - ATK SPD via Haste (single target, average) `signature fuel`

### Units benefitting most from Soren

Soren provides Shield (Supreme+) to single targets `low`.

- Niru (4.2 / 5)
- Carolina (3.0 / 5)
- Nerion (2.7 / 5)

### Units that can act as a replacement for Soren

**Best overall replacement**

- Scarlita (50% `Crowd Control` `Damage`)

**Buffs on allies**

- Contess (100% `Shield`)
- Hugin (100% `Shield`)
- Saida (100% `Shield`)

**Similar Skills**

- Lenya (66% `counterattack` `self-repositioner`)
- Kulu (40% `self-repositioner`)
- Alsa (40% `self-repositioner`)

**Damage**

- Gwyneth (100% `Physical`)
- Himmel (100% `Physical`)
- Baelran (100% `Physical`)

**Crowd Control**

- Perseus (100% `Stun` `Knock back`)
- Scarlita (100% `Stun` `Knock back`)
- Lumont (93% `Stun` `Knock back`)

### Summary for Soren

#### Damage types dealt by Soren

- Physical — Area, Multiple targets

#### Buffs provided by Soren

- Shield (Supreme+) — Single target — `low`

#### Crowd Control provided by Soren

- Knock back — Area — `low`
- Knock back — Single target — `low`
- Stun — Multiple targets — `average`

## Sylphira

### Sylphira's behavior

`AFK Stages [A]`, `Dream Realm [A+]`, `Dream Realm (Endless) [?]`, `PVP [S+]`

- **Signature skill**: Grand Finale (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `high-initial-energy` `interrupt` `life-drain` `mass-cc`
- **Damage types**: Magic `high`, Max HP-based damage `average`, True damage `low`

#### Play overview

Sylphira builds an **active score** that raises ATK and Haste, then unleashes a **silencing domain** followed by multi-hit strikes on her target. Her three-hit skill **drains enemy energy** on each connect, and a separate skill chains **control into area knockdown** for crowd disruption across grouped foes. Once score activates, auto-play **cleanses debuffs and recovers HP and energy**, keeping her self-sufficient through extended fights without external support. Enhanced attacks also deal **true damage life drain** for sustained personal pressure between ultimate windows. She blends control, silence, and self-sustain in one slot for attrition-heavy teams. Against **unaffected or silence-immune foes**, her domain, energy drain, and knockdown chain lose much of their disruptive value.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, buffs `average`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

Passive: active score increases ATK and Haste; Active: create silencing domain, then multi-hit target

##### Skill 1

three-hit strike dealing damage and draining enemy energy

##### Skill 2

control then area knock down burst

##### Legendary+

battle haste increase

##### Mythic+

once score activates, auto-play cleanses debuffs and recovers HP and energy

##### Supreme+

enhanced attacks true damage life drain

### Units improving Sylphira

Look for units providing: `ATK` `Haste`  
Common buffers are **Kazim**, **Mikola**, **Ravion**, or **Smokey & Meerky**.

- **Aliceth**
  - ATK (multiple targets, average)
- **Pang**
  - ATK (multiple targets, average)
- **Perseus**
  - ATK (multiple targets, average)
- **Isabella**
  - ATK (single target, low, conditional (frequent))
  - Haste (single target, low) `signature fuel`
- **Hewynn**
  - Haste (single target, average) `signature fuel`
- **Mehira**
  - Haste (multiple targets, average) `signature fuel`

### Units benefitting most from Sylphira

- Carolina (3.7 / 5)
- Bonnie (3.4 / 5)
- Nerion (3.2 / 5)

### Units that can act as a replacement for Sylphira

**Best overall replacement**

- Pippa (53% `Damage` `Debuffs on enemies`)
- Natsu (50% `Damage`)

**Similar Skills**

- Lucca (40% `high-initial-energy` `interrupt`)
- Natsu (34% `high-initial-energy` `mass-cc`)
- Lucy (33% `high-initial-energy` `mass-cc`)

**Damage**

- Natsu (95% `Magic`)
- Pippa (89% `Magic` `True damage`)
- Nara (79% `True damage`)

**Debuffs on enemies**

- Dunlingr (100% `Energy`)
- Vala (100% `Energy`)
- Pippa (100% `Energy`)

**Crowd Control**

- Baelran (87% `Knock down`)
- Lucca (50% `Knock down` `Interrupt`)

### Summary for Sylphira

#### Sylphira Provides

- Dispel debuffs (Mythic+) — Self
- Stacking (Mythic+) — Single target

#### Damage types dealt by Sylphira

- Magic — Area, Single target
- Max HP-based damage — Single target — `average`
- True damage — Area — `average`

#### Debuffs provided by Sylphira

- Energy — Single target — `average`
- Max HP — Single target — `low`

#### Crowd Control provided by Sylphira

- Immune — Self — On skill
- Unaffected — Self — On skill
- Cleanse (Mythic+) — Self — On skill
- Interrupt — Single target — `low`
- Knock down — Area — `average`
- Silence — Single target — `low`

## Talene

### Talene's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [A]`, `PVP [B]`

- **Signature skill**: Divine Conflagration (ultimate)
- **Movement**: moving (avg attack range 3.0 tiles)
- **Behavior tags**: `ally-healer` `aoe-damage` `cheat-death`
- **Ally composition**: frontmost ally carries Pyre of Renewal (AoE damage and healing)
- **Damage types**: Magic `high`

#### Play overview

Talene **consumes HP to shoot flames** at enemies, and her ATK **scales with cumulative HP spent** over the course of the fight. HP loss passively **heals allies while damaging enemies**, turning her self-harm into team-wide value whenever she trades health for offense. On defeat she **transforms and regenerates to resurrect**, with faster recovery on the first fall to rejoin the battle quickly. She also **enhances the frontmost ally** to deal sustained damage to adjacent enemies, extending her sacrifice into allied pressure over long engagements where she can cycle flame bursts multiple times. She is a **self-sacrificing specialist** who needs reliable healing to survive her own HP consumption safely across repeated flame cycles. Without sustain or enough fight time to trigger resurrection, her flame scaling and ally enhancement never reach their peak.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `high`

##### Ultimate

consume HP to shoot flames at enemies

##### Skill 1

Passive: HP-loss heals allies, being healed damages enemies; Active: deal damage to enemies

##### Skill 2

transformation on defeat; regeneration to resurrect

##### Legendary+

ATK scales with cumulative HP consumed

##### Mythic+

enhance frontmost ally to deal sustained damage to adjacent enemies

##### Supreme+

regeneration rate increased when defeated for the first time

### Units improving Talene

Look for units providing: `ATK` `Max HP` `Healing`  
Common buffers are **Pandora**, **Contess**, **Evie**, or **Ravion**.

- **Pandora**
  - Max HP (single target, low)
  - Direct healing (single target, high)
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Ravion**
  - ATK (multiple targets, high)
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Fay**
  - ATK (arc, low)
  - Direct healing (arc, high)
- **Solise**
  - ATK (single target, low)
  - Direct healing (all units, high)
- **Isabella**
  - ATK (single target, low, conditional (frequent))
  - Direct healing (single target, high)
- **Koko**
  - ATK (all units, low)
  - Direct healing (single target, average)

### Units benefitting most from Talene

- Bonnie (3.4 / 5)
- Carolina (2.3 / 5)
- Nerion (2.1 / 5)

### Units that can act as a replacement for Talene

**Similar Skills**

- Ulmus (60% `aoe-damage` `cheat-death`)
- Tasi (48% `aoe-damage` `cheat-death`)
- Lucius (40% `ally-healer` `aoe-damage`)

**Damage**

- Frieren (100% `Magic`)
- Saida (100% `Magic`)
- Silven (100% `Magic`)

**Crowd Control**

- Twins (100% `Knock back`)
- Kordan (100% `Knock back`)
- Perseus (100% `Knock back`)

### Summary for Talene

#### Talene Provides

- Cheat death — Self
- Transformation — Self
- Ally DoT on enemies (Mythic+) — Area
- Stacking (Mythic+) — Single target

#### Damage types dealt by Talene

- Magic — Area

#### Crowd Control provided by Talene

- Knock back — Area — `low`

## Tasi

### Tasi's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Eternal Dreamscape (ultimate)
- **Movement**: stationary (avg attack range 10.0 tiles)
- **Behavior tags**: `aoe-damage` `cheat-death` `mass-cc` `self-repositioner`
- **Damage types**: Magic `average`, DoT `average`

#### Play overview

Tasi opens with **AoE sleep** that damages all enemies, then leaps to a distant foe to **deal damage and stun again**. HP sacrifice triggers **transformation that recovers HP** while damaging nearby enemies in her alternate form. ATK **grows after sleep casts**, and post-ultimate haste **tightens her rotation** between cycles. She gains **extra secondary form uses** on assists or kills for extended pressure windows. Against **sleep-immune targets**, her control package stalls before forms can cycle.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `low`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `average`

##### Ultimate

AoE sleep all enemies with sustained damage

##### Skill 1

consume HP to stun nearby enemies, then leap to distant enemy to deal damage and stun again

##### Skill 2

transform on HP-loss threshold, recovering HP while dealing damage to nearby enemies

##### Legendary+

ATK grows after sleep cast is active

##### Mythic+

post-ultimate haste and damage reduction, with reduced cooldown on HP-sacrifice skill

##### Supreme+

extra secondary form use gained per assist or kill

### Units improving Tasi

Look for units providing: `ATK` `Haste` `Max HP`  
Common buffers are **Ravion**, **Twins**, **Mikola**, or **Kazim**.

- **Ravion**
  - ATK (multiple targets, high)
  - Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Max HP (single target, low)
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Aliceth**
  - ATK (multiple targets, average)
- **Pang**
  - ATK (multiple targets, average)
- **Thador**
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Zandrok**
  - Haste (area, average, conditional (frequent)) `signature fuel`
  - Max HP (multiple targets, low)

### Units benefitting most from Tasi

- Carolina (4.3 / 5)
- Shadewing (4.1 / 5)
- Nerion (3.8 / 5)

### Units that can act as a replacement for Tasi

**Similar Skills**

- Igor (60% `aoe-damage` `cheat-death` `self-repositioner`)
- Temesia (60% `aoe-damage` `mass-cc` `self-repositioner`)
- Ulmus (57% `aoe-damage` `cheat-death`)

**Damage**

- Frieren (100% `DoT` `Magic`)
- Cyran (100% `DoT` `Magic`)
- Dunlingr (100% `DoT` `Magic`)

### Summary for Tasi

#### Tasi Provides

- Invincibility — Self
- Sleep (area) — All units
- Transformation — Self

#### Damage types dealt by Tasi

- Magic — Area
- DoT — All units, Area

#### Crowd Control provided by Tasi

- Sleep — All units — `average`
- Stun — Area — `low`

## Temesia

### Temesia's behavior

`AFK Stages [C]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Knight's Heart (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `aoe-damage` `enemy-debuffer` `interrupt` `mass-cc` `self-repositioner`
- **Damage types**: Physical `high`, Max HP-based damage `high`, True damage `low`

#### Play overview

Temesia charges through the field, dealing **path damage passively** and **knocking down enemies** on her mounted leap ultimate. Direction changes trigger **interrupting kicks** that weaken foes in her path. Sword attacks on adjacent tiles **scale on target ATK**, punishing high-damage frontliners. After repeated charges she gains **unaffected status and true damage**, and charge hits shave enemy Phys DEF. Battle ATK **grows after first ultimate**, adding scaling through longer fights. She underperforms when **charge paths are blocked** or enemies resist knockdown and displacement.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, buffs `average`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, debuffs `average`, damage `low`

##### Ultimate

Passive: charge path damage; Active: mount leap knock down and charge speed boost

##### Skill 1

kick interrupts and weakens when charge direction changes

##### Skill 2

sword attacks adjacent scaling on target ATK

##### Legendary+

battle ATK grows after first ultimate activation

##### Mythic+

permanent unaffected and true damage after repeated charges

##### Supreme+

charge hits reduce target Phys DEF

### Units improving Temesia

Look for units providing: `ATK` `ATK SPD / Haste` `Energy`  
Common buffers are **Ravion**, **Smokey & Meerky**, **Kazim**, or **Mikola**.

- **Ravion**
  - ATK (multiple targets, high)
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Lyca**
  - ATK SPD (all units, low) `signature fuel`
  - Energy (all units, low) `signature fuel`
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`
- **Aliceth**
  - ATK (multiple targets, average)

### Units benefitting most from Temesia

- Indris (2.4 / 5)
- Carolina (2.3 / 5)
- Nerion (2.1 / 5)

### Units that can act as a replacement for Temesia

**Similar Skills**

- Tasi (60% `aoe-damage` `mass-cc` `self-repositioner`)
- Valen (48% `aoe-damage` `mass-cc`)
- Cassadee (48% `aoe-damage` `enemy-debuffer`)

**Damage**

- Nara (100% `Physical` `True damage`)
- Korin (100% `Physical` `True damage`)
- Valka (97% `Physical` `True damage`)

**Debuffs on enemies**

- Evie (100% `Damage dealt`)
- Vala (100% `Damage dealt`)
- Saida (67% `Damage dealt`)

**Crowd Control**

- Sylphira (100% `Knock down` `Interrupt`)
- Cyran (100% `Knock down`)
- Lucca (100% `Knock down` `Interrupt`)

### Summary for Temesia

#### Temesia Provides

- Stacking — Single target
- Execution scaling (Mythic+) — Self

#### Damage types dealt by Temesia

- Physical — Area, Single target
- Max HP-based damage — Single target — `high`
- True damage — Area — `low`

#### Debuffs provided by Temesia

- Damage dealt — Single target — `low`
- Phys DEF (Supreme+) — Area — `low`
- Phys DEF (Supreme+) — Single target — `low`

#### Crowd Control provided by Temesia

- Unaffected (Mythic+) — Self — Permanent
- Interrupt — Single target — `low`
- Knock down — Area — `low`

## Thador

### Thador's behavior

`AFK Stages [S]`, `Dream Realm [A+]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Darkmoon Pact (Skill 1)
- **Movement**: moving (avg attack range 0.2 tiles)
- **Behavior tags**: `ally-shielder` `enemy-debuffer` `energy-provider` `temporary-stat-buffer`
- **Ally composition**: place lieutenant 1 tile behind at battle prep (Crit + shared shields)
- **Damage types**: Physical `average`, DoT `high`

#### Play overview

Thador designates a **rear ally bond** that grants crit, then shields both partners when his active skill fires at the start of engagements. His ultimate deals **AoE damage and ritual debuffs** on affected enemies, layering disruption across the whole line. A frontal arc skill **knocks down** nearby foes, and battle **damage taken reduction** keeps him standing as a durable frontliner through sustained trades. When the bonded ally casts ultimate, he triggers **AoE damage plus Phys and Magic DEF reduction** on all enemies, amplifying team follow-up. Passive **HP regeneration** continues while the bonded ally lives, giving both partners staying power. He needs a **reliable rear partner** in formation; if the bond target dies early, much of his shielding, crit grant, and debuff payoff is lost for the rest of the fight.

#### Skill overview

- **Signature skill**: speed `average`, first cast speed `fast`, buffs `average`
- **Ultimate**: speed `slow`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

AoE damage and perform ritual inflicting debuffs on affected enemies

##### Skill 1

Passive: designate rear ally bond granting crit; Active: shield both

##### Skill 2

frontal arc knock down

##### Legendary+

battle damage taken reduction

##### Mythic+

bonded ally casting ultimate triggers AoE damage and Phys and Magic DEF reduction on all enemies

##### Supreme+

passive HP regeneration while bonded ally is alive

### Units improving Thador

Look for units providing: `Max HP` `CRIT`  
Common buffers are **Twins**, **Smokey & Meerky**, **Ravion**, or **Lorsan**.

- **Zandrok**
  - Max HP (multiple targets, low)
  - ATK SPD via Haste (area, average, conditional (frequent)) `signature fuel`
- **Hewynn**
  - ATK SPD via Haste (single target, average) `signature fuel`
- **Mehira**
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
- **Shakir**
  - ATK SPD via Haste (area, average) `signature fuel`
- **Damian**
  - ATK SPD via Haste (multiple targets, average, conditional (frequent)) `signature fuel`
- **Isabella**
  - ATK SPD via Haste (single target, low) `signature fuel`

### Units benefitting most from Thador

Thador provides Crit to single targets `low`, Shield to multiple targets `average`, and Energy (EX+10) to single targets `high`.

**50** units include this provider among their top 6 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **4** strongest pairings: 

- Shemira (4.9 / 5)
- Marcille (4.5 / 5)
- Cryonaia (3.7 / 5)
- Vala (3.1 / 5)

### Units that can act as a replacement for Thador

**Similar Skills**

- Ravion (72% `ally-shielder` `energy-provider` `temporary-stat-buffer`)
- Twins (50% `ally-shielder` `energy-provider` `temporary-stat-buffer`)
- Hugin (50% `ally-shielder` `energy-provider` `temporary-stat-buffer`)

**Damage**

- Gwyneth (100% `DoT` `Physical`)
- Alna (100% `DoT` `Physical`)
- Faramor (100% `DoT` `Physical`)

**Crowd Control**

- Frieren (100% `Knock down`)
- Himmel (100% `Knock down`)
- Baelran (100% `Knock down`)

### Summary for Thador

#### Damage types dealt by Thador

- Physical — Area, Single target
- DoT — Single target

#### Buffs provided by Thador

- Crit — Single target — `low`
- Shield — Multiple targets — `average`
- Energy (EX+10) — Single target — `high`

#### Debuffs provided by Thador

- Magic DEF (Mythic+) — Single target — `high`
- Phys DEF (Mythic+) — Single target — `low`

#### Crowd Control provided by Thador

- Knock down — Single target — `low`

## Thoran

### Thoran's behavior

`AFK Stages [B]`, `Dream Realm [A+]`, `Dream Realm (Endless) [A]`, `PVP [B]`

- **Signature skill**: Resurrection (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `cheat-death` `counterattack` `life-drain`
- **Ally composition**: place ally 1 tile behind at battle prep (Soul Pact damage share and revive)
- **Damage types**: Physical `average`

#### Play overview

Thoran **charges up a slash** that adds a portion of damage taken during the charge, then gains **life drain** on the release for sustain. He drains HP from the **highest-HP enemy** to swell his own pool, and **revives once at partial HP** after his first defeat. Energy recovery from attacks is **higher before revive triggers**, fueling faster early ultimates while he still has his first life. He absorbs a portion of damage for a bonded ally, and on defeat the ally can sacrifice HP to revive him. His ultimate also **drains HP from enemies** on impact. He is a **durable frontliner** but offers weak output when enemies deny his drain targets and burst him before revive can matter.

#### Skill overview

- **Signature skill**: speed `fast`, heal `average`, buffs `average`
- **Ultimate**: speed `fast`, buffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`

##### Ultimate

charge up, slash in range for damage plus a portion of damage taken during charge, gaining life drain

##### Skill 1

drain HP from highest HP enemy, increasing own HP

##### Skill 2

revive once at partial HP after defeat

##### Legendary+

energy recovery from attacks; higher before revive triggers

##### Mythic+

absorb a portion of damage for bonded ally; on defeat, bonded ally sacrifices HP to revive self

##### Supreme+

ultimate additionally drains HP from enemy

### Units improving Thoran

Look for units providing: `Max HP` `Energy`

- **Twins**
  - Max HP (multiple targets, average)
  - Energy (multiple targets, low) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
- **Pandora**
  - Max HP (single target, low)
  - Energy (single target, low) `signature fuel`

### Units benefitting most from Thoran

- Niru (4.2 / 5)
- Himmel (2.2 / 5)
- Vala (1.9 / 5)

### Units that can act as a replacement for Thoran

**Similar Skills**

- Brutus (40% `cheat-death` `life-drain`)
- Igor (40% `cheat-death` `life-drain`)
- Zorya (30% `life-drain`)

**Damage**

- Himmel (100% `Physical`)
- Aliceth (100% `Physical`)
- Faramor (100% `Physical`)

**Debuffs on enemies**

- Kulu (100% `Damage taken`)
- Reinier (100% `Damage taken`)
- Himmel (97% `Damage taken`)

### Summary for Thoran

#### Thoran Provides

- Cheat death — Self
- Ally positioning link (Mythic+) — Single target
- Cheat death (Mythic+) — Single target

#### Damage types dealt by Thoran

- Physical — Area
- HP loss — Multiple targets, Single target

#### Debuffs provided by Thoran

- Damage taken — Single target — `low`

#### Crowd Control provided by Thoran

- Unaffected — Self — On skill

## Tilaya

### Tilaya's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Wrath of the Wilds (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `aoe-damage` `temporary-stat-buffer`
- **Damage types**: Physical `average`

#### Play overview

Tilaya fights behind an **auto-regenerating shield** that fuels both defense and offense throughout the fight. Her ultimate delivers **repeated frontal greatsword attacks**, and shield regeneration **speeds up while casting** to keep her barrier topped. A powerful strike **restores shield value**, while normal attacks gain extra damage proportional to current shield for scaling burst. First shield break **permanently increases shield recovery**, and battle vitality growth keeps her standing through long frontline trades. She is a **shield-scaling tank** who peaks when allowed to maintain and rebuild her barrier repeatedly. Fights that **strip or bypass shields** leave her damage scaling and sustain flat.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, heal `average`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `average`

##### Ultimate

Passive: gain auto-regenerating shield; Active: repeated frontal greatsword attacks

##### Skill 1

powerful strike that also restores shield value

##### Skill 2

attacks gain extra damage proportional to current shield value

##### Legendary+

battle vitality increase

##### Mythic+

first shield break permanently increases shield recovery amount

##### Supreme+

shield regeneration speed increases while casting ultimate

### Units improving Tilaya

Look for units providing: `ATK` `Max HP` `Shield`  
Common buffers are **Ravion**, **Pandora**, **Twins**, or **Contess**.

- **Ravion**
  - ATK (multiple targets, high)
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Max HP (single target, low)
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Aliceth**
  - ATK (multiple targets, average)
- **Pang**
  - ATK (multiple targets, average)
- **Perseus**
  - ATK (multiple targets, average)

### Units benefitting most from Tilaya

Tilaya provides DEF (EX+10) in an area `high` and Max HP (EX+10) in an area `high`.

**11** units include this provider among their top 6 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **4** strongest pairings: 

- Antandra (4.7 / 5)
- Hepler (4.2 / 5)
- Laios (3.7 / 5)
- Cecia (3.0 / 5)

### Units that can act as a replacement for Tilaya

**Buffs on allies**

- Alna (80% `Max HP`)

**Similar Skills**

- Lorsan (80% `aoe-damage` `temporary-stat-buffer`)
- Sonja (66% `aoe-damage` `temporary-stat-buffer`)
- Perseus (66% `aoe-damage` `temporary-stat-buffer`)

**Damage**

- Gunnar (100% `Physical`)
- Gwyneth (100% `Physical`)
- Himmel (100% `Physical`)

### Summary for Tilaya

#### Tilaya Provides

- Damage absorption (allies) — Self
- Form or stance active — Self

#### Damage types dealt by Tilaya

- Physical — Arc, Single target

#### Buffs provided by Tilaya

- DEF (EX+10) — Area — `high`
- Max HP (EX+10) — Area — `high`

#### Crowd Control provided by Tilaya

- Unaffected — Self — Conditional

## Twins

### Twins's behavior

`AFK Stages [S]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S+]`, `PVP [A+]`

- **Signature skill**: Starlight Waltz (ultimate)
- **Movement**: moving / stationary (two units)
- **Behavior tags**: `ally-buffer` `ally-healer` `ally-shielder` `energy-provider` `temporary-stat-buffer`
- **Ally composition**: place allies on the Stellar Bond line between Elijah and Lailah
- **Damage types**: Magic `low`

#### Play overview

The Twins inspire allied **haste through a linked duo performance**, and linked allies become **unaffected** during the ultimate. They form **line links** that recover linked allies' energy and HP over sustained casts. One twin **shields allies** while the other **damages and blinds** nearby enemies in the same beat. Linked allies **borrow best stats from each other**, and haste grows with each repeated performance. They need **multiple linked partners** in formation; sparse lineups waste their buff and healing channels.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, buffs `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `low`

##### Ultimate

linked duo performance inspires allied haste; linked allies become unaffected

##### Skill 1

form line link channeling blessings to recover linked allies' energy and HP

##### Skill 2

one twin shields allies; the other damages and blinds nearby enemies

##### Legendary+

haste grows each time the performance is repeated

##### Mythic+

same-faction link strengthens bond; permanently enhanced when all linked allies cast ultimate

##### Supreme+

linked allies borrow best stats from each other

### Units improving Twins

Look for units providing: `Haste` `Energy`  
Common buffers are **Ravion**, **Hugin**, **Smokey & Meerky**, or **Lorsan**.

- **Ravion**
  - Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Hewynn**
  - Haste (single target, average) `signature fuel`
  - ATK SPD via Haste (single target, average) `signature fuel`
- **Mehira**
  - Haste (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`

### Units benefitting most from Twins

Twins provides ATK to multiple targets `high`, Direct healing to multiple targets `average`, Energy to multiple targets `low`, Haste to all units `high`, Max HP to multiple targets `average`, Vitality (Mythic+) to multiple targets `low`, Magic DEF (Supreme+) to single targets `low`, and Phys DEF (Supreme+) to single targets `low`.

**94** units include this provider among their top 6 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight
- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner

These are the **4** strongest pairings: 

- Nerion (5.0 / 5)
- Zorya (4.6 / 5)
- Carolina (4.2 / 5)
- Vala (3.9 / 5)

### Units that can act as a replacement for Twins

**Best overall replacement**

- Smokey & Meerky (50% `Healing` `Buffs on allies`)

**Buffs on allies**

- Hugin (64% `Haste` `Energy` `ATK`)
- Smokey & Meerky (61% `Haste` `ATK` `Energy`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Evie (100% `Direct healing` `Healing`)

**Similar Skills**

- Koko (72% `ally-buffer` `ally-healer` `temporary-stat-buffer`)
- Velara (60% `ally-healer` `ally-shielder` `temporary-stat-buffer`)
- Hugin (51% `ally-shielder` `energy-provider` `temporary-stat-buffer`)

**Damage**

- Frieren (100% `Magic`)
- Mehira (100% `Magic`)
- Solise (100% `Magic`)

**Crowd Control**

- Hepler (81% `Blind`)
- Aliceth (75% `Blind` `Knock back`)

### Summary for Twins

#### Twins Provides

- Ally positioning link — Multiple targets
- Ally positioning link — Single target
- Ally positioning link — Area
- Shared HP and Energy — Single target
- Ally positioning link (Legendary+) — All units

#### Damage types dealt by Twins

- Magic — Area

#### Buffs provided by Twins

- ATK — Multiple targets — `high`
- Direct healing — Multiple targets — `average`
- Energy — Multiple targets — `low`
- Haste — All units — `high`
- Max HP — Multiple targets — `average`
- Vitality (Mythic+) — Multiple targets — `low`
- Magic DEF (Supreme+) — Single target — `low`
- Phys DEF (Supreme+) — Single target — `low`

#### Crowd Control provided by Twins

- Unaffected — Self — On skill
- Blind — Area — `average`
- Knock back — Area — `low`

## Ulmus

### Ulmus's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Way of the Forest (Skill 2)
- **Movement**: moving (stationary when rooted)
- **Behavior tags**: `ally-shielder` `aoe-damage` `cheat-death`
- **Ally composition**: when rooted, shields frontmost ally instead of self
- **Damage types**: Physical `high`

#### Play overview

Ulmus gains a **shield that damages surrounding enemies when it breaks**, and retreats to **take root at low HP** for survival when pressured. While rooted he shifts to energy regeneration instead of HP regen, and grants **shield to the frontmost ally** after his own shield breaks. His ultimate **knocks up a target and adjacent enemies**, and displacement **extends knockdown duration with bonus damage**. Battle max HP growth adds durability over time, and shield break knocks back adjacent foes for extra control. He blends **tanking, control, and ally protection** in one slot. He struggles when enemies **focus him before rooting** or deny displacement setups entirely.

#### Skill overview

- **Signature skill**: speed `fast`, heal `average`, buffs `average`
- **Ultimate**: speed `fast`, heal `average`, damage `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `average`

##### Ultimate

Passive: retreat to initial tile and take root when HP is low; Active: knock up target and adjacent enemies

##### Skill 1

gain shield that damages surrounding enemies when it breaks; after rooting, grant shield to frontmost ally instead

##### Skill 2

passive HP regeneration; energy regeneration when rooted instead

##### Legendary+

battle max HP increase

##### Mythic+

displacement extends knock down duration with bonus damage

##### Supreme+

shield break knock back adjacent enemies

### Units improving Ulmus

Look for units providing: `Shield` `Energy`

- **Rowan**
  - Energy (area, high) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
- **Ravion**
  - Energy (multiple targets, average) `signature fuel`
- **Twins**
  - Energy (multiple targets, low) `signature fuel`

### Units benefitting most from Ulmus

- Kazim (4.5 / 5)

### Units that can act as a replacement for Ulmus

**Best overall replacement**

- Scarlita (51% `Damage` `Crowd Control`)

**Similar Skills**

- Saida (60% `ally-shielder` `cheat-death`)
- Talene (60% `aoe-damage` `cheat-death`)
- Tasi (57% `aoe-damage` `cheat-death`)

**Damage**

- Gunnar (100% `Physical`)
- Gwyneth (100% `Physical`)
- Himmel (100% `Physical`)

**Crowd Control**

- Scarlita (100% `Knock back` `Knock up`)
- Kordan (88% `Knock back` `Bind` `Knock up`)
- Cassadee (88% `Knock back` `Knock up`)

### Summary for Ulmus

#### Ulmus Provides

- Cheat death — Self

#### Damage types dealt by Ulmus

- Physical — Area, Single target

#### Crowd Control provided by Ulmus

- Unaffected — Self — Conditional
- Knock up — Area — `low`
- Bind (Mythic+) — Single target — `low`
- Knock back (Supreme+) — Area — `low`

## Vala

### Vala's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Swift Shift (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `hp-scaling` `mark-target` `self-repositioner` `stealth` `untargetable`
- **Damage types**: Physical `average`, True damage `average`

#### Play overview

Vala **marks an enemy** and prioritizes them, **absorbing their energy** on each focused attack to starve their rotation. Her ultimate switches between **ranged stun mode** and **melee true damage mode** depending on positioning needs in the fight. Mode-based skills either reduce enemy haste or deliver multi-hit burst for flexible offense. ATK **grows with each non-summoned enemy defeated**, and marked enemy defeat boosts her movement speed and haste. She deals **bonus damage to marked targets** for reliable focus fire on priority carries. Against **mark-immune or stealth-heavy lines**, her energy drain and mode switching add little sustained pressure.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

switch to ranged mode dealing damage and stun, or melee mode dealing true damage

##### Skill 1

mark an enemy, prioritizing attacks on them and absorbing their energy

##### Skill 2

mode-based: damage and haste reduction, or multi-hit attack

##### Legendary+

ATK grows with each non-summoned enemy defeated

##### Mythic+

marked enemy defeat increases movement speed and haste

##### Supreme+

deal bonus damage to marked enemy

### Units improving Vala

Look for units providing: `ATK` `Haste` `Energy`  
Common buffers are **Ravion**, **Kazim**, **Twins**, or **Smokey & Meerky**.

Vala also requires enemies **to be defeated**

- **Ravion**
  - ATK (multiple targets, high)
  - Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
  - Enables Enemy defeat via AoE physical (kills)
- **Kazim**
  - ATK (single target, high)
  - Haste (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Enables Enemy defeat via AoE physical (kills)
- **Twins**
  - ATK (multiple targets, average)
  - Haste (all units, average) `signature fuel`
  - Energy (multiple targets, low) `signature fuel`
  - ATK SPD via Haste (all units, average) `signature fuel`
  - Enables Enemy defeat via AoE magic (kills)
- **Dunlingr**
  - ATK (single target, low)
  - Haste (single target, average) `signature fuel`
  - ATK SPD via Haste (single target, average) `signature fuel`
  - Enables Enemy defeat via AoE magic (kills)
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
  - Enables Enemy defeat via AoE physical (kills)
- **Sonja**
  - ATK (multiple targets, high)
  - Enables Enemy defeat via AoE physical (kills)

### Units benefitting most from Vala

- Indris (2.1 / 5)
- Carolina (2.0 / 5)
- Nerion (1.8 / 5)

### Units that can act as a replacement for Vala

**Best overall replacement**

- Nazrik (70% `Damage` `Crowd Control`)
- Marilee (58% `Damage`)
- Faramor (55% `Damage`)

**Similar Skills**

- Marilee (57% `hp-scaling` `self-repositioner`)
- Nazrik (48% `hp-scaling` `mark-target`)
- Silven (41% `hp-scaling` `mark-target`)

**Damage**

- Frieren (100% `True damage`)
- Faramor (100% `True damage` `Physical` `HP loss`)
- Athalia (100% `True damage` `Physical`)

**Debuffs on enemies**

- Berial (78% `Energy` `Damage dealt`)
- Dunlingr (76% `Energy` `Haste`)
- Rowan (72% `Energy`)

**Crowd Control**

- Phraesto (100% `Stun`)
- Callan (100% `Stun`)
- Zandrok (100% `Stun`)

### Summary for Vala

#### Vala Provides

- Form or stance active — Self
- Marked target (focus fire) — Single target
- Marked target (focus fire) (Mythic+) — Self

#### Damage types dealt by Vala

- Physical — Single target
- True damage — Single target — `average`

#### Debuffs provided by Vala

- Energy — Single target — `average`
- Haste — Single target — `high`
- Marked target (focus fire) — Single target — `average`
- Damage dealt (Supreme+) — Single target — `average`

#### Crowd Control provided by Vala

- Untargetable (Mythic+) — Self — Conditional
- Stun — Single target — `average`

## Valen

### Valen's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Thunder Swordwork (ultimate)
- **Movement**: moving (avg attack range 1.4 tiles)
- **Behavior tags**: `aoe-damage` `mass-cc`
- **Damage types**: Physical `average`

#### Play overview

Valen launches **multiple strikes within range** and enters a permanent **Invigoration buff state** that defines his entire rotation. Three-hit consecutive strikes **chain lightning to nearby foes** while buffed, and a separate skill delivers **AoE lightning burst** only during the buff window for spread damage. Buff activations **stack ATK bonus** over repeated casts, compounding personal damage through the fight, and lightning AoE also stuns enemies for control alongside raw burst output. He is a buff-gated damage dealer who needs Invigoration uptime to access his best skills. Without **grouped enemies for chain lightning**, his burst and stun payoff shrink sharply.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, damage `average`

##### Ultimate

launch multiple strikes within range and gain Invigoration buff state

##### Skill 1

three-hit consecutive strikes; chain lightning to nearby during buff

##### Skill 2

AoE lightning burst available only while buffed

##### Legendary+

battle ATK increase

##### Mythic+

permanent buff state; buff activations stack ATK bonus

##### Supreme+

lightning AoE also stuns enemies

### Units improving Valen

Look for units providing: `ATK` `Energy`  
Common buffers are **Ravion**, **Smokey & Meerky**, **Kazim**, or **Mikola**.

- **Ravion**
  - ATK (multiple targets, high)
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Lyca**
  - Energy (all units, low) `signature fuel`
  - ATK SPD (all units, low) `signature fuel`
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`
- **Aliceth**
  - ATK (multiple targets, average)

### Units benefitting most from Valen

- Niru (4.2 / 5)
- Carolina (3.7 / 5)
- Nerion (3.2 / 5)

### Units that can act as a replacement for Valen

**Best overall replacement**

- Perseus (94% `Damage` `Crowd Control`)
- Atalanta (78% `Damage` `Crowd Control`)
- Antandra (72% `Damage` `Similar Skills` `Crowd Control`)

**Similar Skills**

- Arden (80% `aoe-damage` `mass-cc`)
- Tasi (50% `aoe-damage` `mass-cc`)
- Antandra (50% `aoe-damage` `mass-cc`)

**Damage**

- Gunnar (100% `Physical`)
- Gwyneth (100% `Physical`)
- Himmel (100% `Physical`)

**Crowd Control**

- Koko (100% `Stun`)
- Hepler (100% `Stun`)
- Scarlita (100% `Stun`)

### Summary for Valen

#### Valen Provides

- Form or stance active — Self
- Invincibility — Self
- Stacking (Mythic+) — Self

#### Damage types dealt by Valen

- Physical — Area, Single target

#### Crowd Control provided by Valen

- Stun (Supreme+) — Area — `average`

## Valka

### Valka's behavior

`AFK Stages [C]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [B]`

- **Signature skill**: Phantom Slasher (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-buffer` `ally-shielder` `counterattack` `high-initial-energy`
- **Damage types**: Physical `high`

#### Play overview

Valka applies **Panic stacks through normal attacks**, then slashes panicked targets for **damage and self-healing** on ultimate for sustain at the front. She wields **multiple sword techniques** at appropriate range, each costing energy for flexible offense across melee and mid-range. At battle start she gains a **shield and raises ally ATK SPD**, supporting nearby partners while she pressures enemies. Battle ATK speed growth keeps her rotation fluid, and she **counters incoming ultimate damage** with a free parry counter when threatened. While shielded she gains **bonus energy from normal attacks**, fueling faster technique use. She underperforms when enemies **never accumulate Panic** or burst her before stacks complete.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `high`

##### Ultimate

Passive: normal attacks apply Panic stacks to target; Active: slash panicked target, dealing damage and self-healing

##### Skill 1

multiple sword techniques at appropriate range cost energy

##### Skill 2

gain a shield and increase ally ATK SPD at battle start

##### Legendary+

battle ATK speed increase

##### Mythic+

counter incoming ultimate damage with free parry counter

##### Supreme+

while shielded gain bonus energy from normal attacks

### Units improving Valka

Look for units providing: `ATK SPD / Haste` `Shield` `Energy`  
Common buffers are **Thador**, **Smokey & Meerky**, **Ravion**, or **Lorsan**.

- **Saida**
  - Shield (multiple targets, high)
- **Hewynn**
  - ATK SPD via Haste (single target, average) `signature fuel`
- **Mehira**
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
- **Shakir**
  - ATK SPD via Haste (area, average) `signature fuel`
- **Damian**
  - ATK SPD via Haste (multiple targets, average, conditional (frequent)) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste (area, average, conditional (frequent)) `signature fuel`

### Units benefitting most from Valka

Valka provides ATK SPD to multiple targets `low`.

- Carolina (2.5 / 5)
- Nerion (2.5 / 5)
- Vala (2.0 / 5)

### Units that can act as a replacement for Valka

**Buffs on allies**

- Dunlingr (100% `ATK SPD`)
- Lyca (100% `ATK SPD`)
- Parisa (100% `ATK SPD`)

**Similar Skills**

- Saida (48% `ally-shielder` `high-initial-energy`)
- Hepler (40% `ally-shielder` `high-initial-energy`)
- Lucca (40% `ally-shielder` `high-initial-energy`)

**Damage**

- Nara (100% `True damage` `Physical`)
- Temesia (100% `Physical` `True damage`)
- Hodgkin (100% `Physical`)

**Debuffs on enemies**

- Alna (100% `Haste`)
- Galahad (100% `Haste`)
- Velara (100% `Haste`)

**Crowd Control**

- Callan (100% `Knock down` `Stun`)
- Zorya (100% `Knock down` `Stun`)
- Antandra (100% `Knock down` `Stun`)

### Summary for Valka

#### Damage types dealt by Valka

- Physical — Area
- Max HP-based damage — Single target

#### Buffs provided by Valka

- ATK SPD — Multiple targets — `low`

#### Debuffs provided by Valka

- Haste — Single target — `low`

#### Crowd Control provided by Valka

- Unaffected — Self — On skill
- Knock down — Single target — `low`
- Knock down — Area — `low`
- Stun — Single target — `low`

## Velara

### Velara's behavior

`AFK Stages [S+]`, `Dream Realm [S]`, `Dream Realm (Endless) [S]`, `PVP [B]`

- **Signature skill**: Ruthless Rite (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-healer` `ally-shielder` `aoe-healing` `temporary-stat-buffer`
- **Damage types**: Magic `average`

#### Play overview

Velara summons **magic circles** that awaken to affect nearby units, extending to the **entire battlefield** once all circles are active across the field. She **immobilizes the highest cumulative damage dealer** and reduces their stats, blunting the enemy's main damage source early. One circle **awakens immediately at battle start**, and nearby debuffed enemies **charge circle energy** for faster full activation. Haste **grows with awakened circle count**, and awakened circles periodically buff weakest allies with healing and protection. Full awakening makes allies unaffected and boosts their damage on subsequent ultimate casts. She needs **fight time and enemy clustering** near circles to reach full coverage; fast burst that ends fights before all circles awaken wastes her scaling and team-wide buff package.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, heal `average`, buffs `average`, debuffs `average`
- **Non-ultimate**: speed `fast`, debuffs `average`, damage `average`

##### Ultimate

summon magic circles that awaken to affect nearby units; all circles awakened extends effects to entire battlefield

##### Skill 1

immobilize the highest cumulative damage dealer and reduce their stats

##### Skill 2

awaken one magic circle at battle start; nearby enemies with stat reductions charge circle energy

##### Legendary+

battle haste grows with awakened circle count

##### Mythic+

awakened circles periodically apply effects to the weakest units

##### Supreme+

all circles awakened extends battlefield coverage; subsequent casts make allies unaffected and boost their damage

### Units improving Velara

Look for units providing: `Haste` `Shield` `Energy`  
Common buffers are **Pandora**, **Ravion**, **Thador**, or **Rowan**.

- **Pandora**
  - Energy (single target, low) `signature fuel`
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Ravion**
  - Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Thador**
  - Energy (single target, high) `signature fuel`
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Lyca**
  - Energy (all units, low) `signature fuel`
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`
- **Phraesto**
  - Energy via Energy recovery speed (contract ally, start of battle) `signature fuel`

### Units benefitting most from Velara

Velara provides Basic stats to all units `average` and Direct healing to multiple targets `average`.

- Indris (4.6 / 5)

### Units that can act as a replacement for Velara

**Best overall replacement**

- Evie (63% `Healing` `Crowd Control`)
- Solise (60% `Healing` `Similar Skills`)
- Hewynn (60% `Healing` `Similar Skills`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Twins (100% `Direct healing` `Healing`)

**Similar Skills**

- Solise (100% `ally-healer` `ally-shielder` `aoe-healing`)
- Hewynn (100% `ally-healer` `aoe-healing` `temporary-stat-buffer`)
- Smokey & Meerky (90% `ally-healer` `aoe-healing` `temporary-stat-buffer`)

**Damage**

- Frieren (100% `Magic`)
- Saida (100% `Magic`)
- Silven (100% `Magic`)

**Debuffs on enemies**

- Eironn (63% `Haste` `Magic DEF`)
- Carolina (52% `Haste` `Magic DEF`)

**Crowd Control**

- Gwyneth (100% `Bind`)
- Alna (100% `Bind`)
- Evie (100% `Bind`)

### Summary for Velara

#### Damage types dealt by Velara

- Magic — Single target

#### Buffs provided by Velara

- Basic stats — All units — `average`
- Direct healing — Multiple targets — `average`

#### Debuffs provided by Velara

- Basic stats — All units — `average`
- Haste — Area — `low`
- Haste — Multiple targets — `average`
- Haste — Single target — `average`
- Magic DEF — Single target — `high`
- Phys DEF — Single target — `low`

#### Crowd Control provided by Velara

- Unaffected (Supreme+) — Multiple targets — On skill
- Bind — Single target — `high`

## Viperian

### Viperian's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Crimson Waltz (Mythic+)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Behavior tags**: `aoe-damage` `dot-specialist`
- **Damage types**: Magic `average`

#### Play overview

Viperian **spends HP to send possessing summons** onto all enemies, spreading pressure across the entire enemy line at once. She drains HP from the **healthiest foe** to refill herself, and possessed summons **periodically damage their hosts** for sustained DoT attrition. A high HP threshold triggers a **large AoE damage burst**, punishing healthy enemy formations. Battle **haste growth** keeps her rotation moving between possession cycles and drain windows, and when possessed enemies fall, summons **return to restore her HP and energy** for the next wave. She is a **DoT and life-drain specialist** who needs healing to cycle HP costs safely. Without sustain or long fights, her possession loop and burst threshold never fully activate.

#### Skill overview

- **Signature skill**: speed `slow`, damage `average`
- **Ultimate**: speed `fast`, damage `average`
- **Non-ultimate**: speed `average`, debuffs `average`, damage `average`

##### Ultimate

spend HP to send possessing summons onto all enemies

##### Skill 1

drain HP from the healthiest enemy

##### Skill 2

possessed summons periodically deal damage to their hosts

##### Legendary+

battle haste increase

##### Mythic+

high HP threshold triggers large AoE damage burst

##### Supreme+

summons return on possessed enemy defeat, restoring HP and energy

### Units improving Viperian

Look for units providing: `Haste`  
Common buffers are **Hugin**, **Smokey & Meerky**, **Lorsan**, or **Ravion**.

- **Hewynn**
  - Haste (single target, average) `signature fuel`
  - ATK SPD via Haste (single target, average) `signature fuel`
- **Mehira**
  - Haste (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
- **Damian**
  - Haste (multiple targets, average, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste (multiple targets, average, conditional (frequent)) `signature fuel`
- **Zandrok**
  - Haste (area, average, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste (area, average, conditional (frequent)) `signature fuel`
- **Isabella**
  - Haste (single target, low) `signature fuel`
  - ATK SPD via Haste (single target, low) `signature fuel`
- **Gunnar**
  - ATK SPD (single target, low) `signature fuel`

### Units benefitting most from Viperian

- Shadewing (4.1 / 5)

### Units that can act as a replacement for Viperian

**Best overall replacement**

- Berial (64% `Damage` `Debuffs on enemies`)
- Pippa (64% `Damage` `Debuffs on enemies`)
- Frieren (60% `Damage` `Similar Skills`)

**Similar Skills**

- Arden (80% `aoe-damage` `dot-specialist`)
- Lorsan (66% `aoe-damage` `dot-specialist`)
- Frieren (60% `aoe-damage` `dot-specialist`)

**Damage**

- Frieren (100% `Magic`)
- Saida (100% `Magic`)
- Silven (100% `Magic`)

**Debuffs on enemies**

- Saida (100% `Energy`)
- Dunlingr (100% `Energy`)
- Lily May (100% `Energy`)

### Summary for Viperian

#### Damage types dealt by Viperian

- Magic — All units, Single target
- DoT — All units

#### Debuffs provided by Viperian

- Energy — Single target — `average`

#### Crowd Control provided by Viperian

- Unaffected — Self — On skill

## Walker

### Walker's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Six-Shot (ultimate)
- **Movement**: moving (avg attack range 2.0 tiles)
- **Behavior tags**: `aoe-damage` `battle-start-burst` `mark-target` `mass-cc` `non-ult-utility`
- **Damage types**: Physical `average`

#### Play overview

Walker fires **sequential frontal shots** that stun each target hit, and his normal attacks deal **AoE damage** for spread pressure. He **prioritizes the highest-damage-dealt enemy**, gaining a buff on focus, and throws **grenades at battle start** for AoE damage and stun. Battle **crit damage growth** adds scaling over time, and first hit against the marked target grants a shield for survivability. He excels as a **battle-start burst specialist** with sustained stun pressure on priority targets. Against **stun-immune targets** or lines that deny his opening grenade angles, his control chain stalls early.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `average`

##### Ultimate

fire sequential shots at frontal enemies, stunning each

##### Skill 1

normal attacks deal AoE damage

##### Skill 2

prioritize attacking highest-damage-dealt enemy, gaining a buff

##### Legendary+

battle crit damage boost

##### Mythic+

throw grenades at battle start, dealing AoE damage and stunning enemies

##### Supreme+

gain a shield on first hit against the marked target

### Units improving Walker

Look for units providing: `Max HP` `Shield` `CRIT`  
Common buffers are **Pandora**, **Thador**, **Rowan**, or **Ravion**.

- **Pandora**
  - Max HP (single target, low)
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Crit (single target, average)
  - Energy via Energy recovery (350 at battle start, lieutenant) `signature fuel`
- **Rowan**
  - Energy via Energy recovery (energy potion, start of battle) `signature fuel`
- **Ravion**
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Phraesto**
  - Energy via Energy recovery speed (contract ally, start of battle) `signature fuel`
- **Lyca**
  - Energy via Energy recovery (120 at battle start, all units) `signature fuel`

### Units benefitting most from Walker

- Niru (3.4 / 5)
- Carolina (3.0 / 5)
- Nerion (2.7 / 5)

### Units that can act as a replacement for Walker

**Similar Skills**

- Kazim (66% `aoe-damage` `battle-start-burst` `mark-target` `mass-cc` `non-ult-utility`)
- Bonnie (60% `aoe-damage` `battle-start-burst` `non-ult-utility`)
- Eironn (51% `aoe-damage` `battle-start-burst` `mass-cc`)

**Damage**

- Gunnar (100% `Physical`)
- Gwyneth (100% `Physical`)
- Himmel (100% `Physical`)

**Debuffs on enemies**

- Nazrik (100% `Crit Resist`)

**Crowd Control**

- Phraesto (100% `Stun`)
- Callan (100% `Stun`)
- Zandrok (100% `Stun`)

### Summary for Walker

#### Damage types dealt by Walker

- Physical — Arc, Single target
- Max HP-based damage — Single target

#### Debuffs provided by Walker

- Crit Resist (Mythic+) — Single target — `low`

#### Crowd Control provided by Walker

- Stun — Single target — `average`
- Stun (Mythic+) — Arc — `average`

## Zandrok

### Zandrok's behavior

`AFK Stages [A+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Rallying Roar (Skill 1)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `aoe-damage` `battlefield-modification` `hp-scaling` `temporary-stat-buffer`
- **Damage types**: Physical `low`

#### Play overview

At battle start, Zandrok sends **illusions charging forward** that **destroy obstacles** in their path and **inspire passing allies** with extra max HP, **Life Drain**, and **Haste**. His axe slam **clears leftover obstacles** near the target while dealing **HP-based area damage**. A ground stomp hits **adjacent enemies** with damage that **scales on max HP**, and his max HP **grows over the fight**, especially while his inspire buffs are active. Normal attacks add **bonus damage from max HP**, and excess healing **converts to permanent max HP**, so sustain feeds his scaling loop. He is a **max HP specialist** who peaks on obstacle-heavy fields with healing support. On **open boards without obstacles**, much of his terrain value and illusion pathing is wasted.

#### Skill overview

- **Signature skill**: speed `fast`, buffs `average`
- **Ultimate**: speed `average`
- **Non-ultimate**: speed `fast`, buffs `average`

##### Ultimate

slam axe down, destroying all obstacles in the area

##### Skill 1

summon illusions that destroy obstacles in their path

##### Skill 2

stomp the ground to strike nearby enemies

##### Legendary+

battle max HP increase, further boosted while buff state is active

##### Mythic+

normal attacks deal bonus damage scaling on max HP

##### Supreme+

excess healing converts to permanent max HP gain

### Units improving Zandrok

Look for units providing: `Max HP`  
Common buffers are **Twins** or **Pandora**.

- **Alna**
  - Max HP (single target, high)
- **Tilaya**
  - Max HP (area, high)

### Units benefitting most from Zandrok

Zandrok provides Haste in an area `average` — conditional (frequent), Lifedrain in an area `high` — conditional (frequent), and Max HP to multiple targets `low`.

**10** units include this provider among their top 6 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **4** strongest pairings: 

- Kazim (5.0 / 5)
- Mehira (3.6 / 5)
- Dunlingr (3.1 / 5)
- Zorya (2.9 / 5)

### Units that can act as a replacement for Zandrok

**Similar Skills**

- Tilaya (50% `aoe-damage` `temporary-stat-buffer`)
- Lorsan (48% `aoe-damage` `temporary-stat-buffer`)
- Kordan (41% `hp-scaling` `temporary-stat-buffer`)

**Crowd Control**

- Scarlita (100% `Stun` `Knock up`)
- Kazim (100% `Stun` `Knock up`)
- Lucca (100% `Stun` `Knock up`)

### Summary for Zandrok

#### Zandrok Provides

- Start-of-battle cast — Allies
- Stacking (Supreme+) — Self

#### Damage types dealt by Zandrok

- Physical — Area
- Max HP-based damage — Area

#### Buffs provided by Zandrok

- Haste — Area — `average` — conditional (frequent)
- Lifedrain — Area — `high` — conditional (frequent)
- Max HP — Multiple targets — `low`

#### Crowd Control provided by Zandrok

- Knock up — Area — `low`
- Stun — Area — `low`

## Zanie

### Zanie's behavior

`AFK Stages [A+]`, `Dream Realm [A+]`, `Dream Realm (Endless) [A+]`, `PVP [B]`

- **Signature skill**: Vein Pulse (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `summoner`
- **Damage types**: Physical `low`

#### Play overview

Zanie **deploys laser turrets at reduced max HP**, then boosts **ATK and ATK speed** for herself and her turrets on ultimate. A gun turret **targets enemies near laser turrets** at battle start, and she **repairs turrets** to restore HP and grant shields to keep them on the field. One turret can be upgraded for more power, and laser attacks apply burn to enemies hit for steady pressure. Battle penetration growth helps her damage pierce defenses over time. She is a **summon-dependent specialist** who needs turrets alive to realize her kit. Fights that **destroy turrets early** or deny her setup window leave her weakened.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, buffs `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`

##### Ultimate

Passive: reduce max HP to deploy laser turrets; Active: boost ATK and ATK speed for self and turrets

##### Skill 1

battle-start deploy gun turret that targets enemies near laser turrets

##### Skill 2

repair turrets restoring HP and granting shields

##### Legendary+

battle penetration increase

##### Mythic+

upgrade a turret to make it more powerful

##### Supreme+

laser turret attacks apply burn to enemies hit

### Units improving Zanie

Look for units providing: `ATK` `ATK SPD / Haste` `DEF Penetration`  
Common buffers are **Ravion**, **Kazim**, **Mikola**, or **Smokey & Meerky**.

- **Peggy**
  - ATK (all summons, high)
  - DEF via DEF (all summons, high)
  - Ranged damage via Ranged damage (all summons, low)
- **Aurora**
  - Haste (all summons, high)
  - Damage dealt via Damage dealt (all summons, average)
  - Damage taken via Damage taken (all summons, low)
- **Ravion**
  - ATK (multiple targets, high)
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Energy via Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Aliceth**
  - ATK (multiple targets, average)
  - DEF Penetration (multiple targets, high)
- **Pandora**
  - Energy via Energy recovery (1000 at battle start, single target) `signature fuel`
- **Kordan**
  - ATK (area, low)
  - DEF Penetration (area, high)

### Units benefitting most from Zanie

- Shadewing (1.9 / 5)
- Indris (1.5 / 5)
- Carolina (1.5 / 5)

### Units that can act as a replacement for Zanie

**Similar Skills**

- Florabelle (50% `summoner`)
- Hodgkin (40% `summoner`)
- Galahad (33% `summoner`)

**Debuffs on enemies**

- Lyca (100% `Phys DEF` `ATK`)
- Ravion (96% `Phys DEF` `ATK`)
- Atalanta (96% `Phys DEF` `ATK`)

**Crowd Control**

- Aliceth (100% `Knock back` `Stun`)
- Perseus (100% `Knock back` `Stun`)
- Scarlita (100% `Knock back` `Stun`)

### Summary for Zanie

#### Zanie Provides

- Summoning — Self
- Summoning — Single target

#### Damage types dealt by Zanie

- Physical — Single target
- DoT — Single target

#### Debuffs provided by Zanie

- ATK (Supreme+) — Single target — `average`
- Phys DEF (Supreme+) — Single target — `average`

#### Crowd Control provided by Zanie

- Knock back — Single target — `low`
- Stun — Single target — `low`

## Zorya

### Zorya's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Guardian's Ring (ultimate)
- **Movement**: moving (inactive while dormant)
- **Behavior tags**: `hp-scaling` `life-drain`
- **Damage types**: Magic `high`, HP loss `high`

#### Play overview

Zorya cycles **dormant and awake states**, jumping to nearby enemies for **AoE damage** on each awakening. While awake she gains **life drain and damage reduction**, and her aura **slows enemy haste** while boosting her own. Damage dealt **scales with nearby enemy count**, rewarding clustered foes. A fatal blow **forces immediate dormancy**, ending her active window. She needs **clustered enemies**; spread lines waste her cycles.

#### Skill overview

- **Signature skill (ult)**: speed `average`, heal `average`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`

##### Ultimate

alternate dormant and awake states; each awakening jumps to nearby enemies, dealing damage

##### Skill 1

Passive: reduce damage taken on awaken; Active: knock down enemies in front

##### Skill 2

Passive: awaken increases life drain; Active: deal multiple hits to nearby enemies

##### Legendary+

battle damage dealt grows with surrounding enemy count

##### Mythic+

awaken creates aura reducing enemy haste and movement speed, boosting own haste

##### Supreme+

fatal blow triggers immediate transition to dormant state

### Units improving Zorya

Look for units providing: `ATK` `Haste` `Max HP` `Energy`  
Common buffers are **Smokey & Meerky**, **Ravion**, **Twins**, or **Lyca**.

Zorya also requires allies **casting ultimates**

- **Smokey & Meerky**
  - ATK (area, average)
  - Haste (area, high) `signature fuel`
  - Energy (area, low) `signature fuel`
  - ATK SPD via Haste (area, high) `signature fuel`
  - Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
- **Ravion**
  - ATK (multiple targets, high)
  - Haste (multiple targets, average) `signature fuel`
  - Energy (multiple targets, average) `signature fuel`
  - ATK SPD via Haste (multiple targets, average) `signature fuel`
  - Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
- **Twins**
  - ATK (multiple targets, average)
  - Haste (all units, average) `signature fuel`
  - Max HP (multiple targets, average)
  - Energy (multiple targets, low) `signature fuel`
  - ATK SPD via Haste (all units, average) `signature fuel`
  - Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
- **Lyca**
  - Energy (all units, low) `signature fuel`
  - ATK SPD (all units, low) `signature fuel`
  - Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
- **Rowan**
  - Energy (area, high) `signature fuel`
  - Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
- **Zandrok**
  - Haste (area, average, conditional (frequent)) `signature fuel`
  - Max HP (multiple targets, low)
  - ATK SPD via Haste (area, average, conditional (frequent)) `signature fuel`
  - Enables Ally Ultimate casts via Start-of-battle Ultimate

### Units benefitting most from Zorya

- Carolina (3.7 / 5)
- Bonnie (3.4 / 5)
- Nerion (3.2 / 5)

### Units that can act as a replacement for Zorya

**Similar Skills**

- Baelran (60% `hp-scaling`)
- Satrana (60% `hp-scaling` `life-drain`)
- Shemira (40% `hp-scaling`)

**Damage**

- Dunlingr (100% `Magic` `HP loss`)
- Shadewing (100% `Magic` `HP loss`)
- Niru (100% `Magic` `HP loss`)

**Debuffs on enemies**

- Galahad (100% `Movement speed` `Haste`)
- Bonnie (61% `Haste`)
- Lorsan (51% `Haste`)

**Crowd Control**

- Callan (100% `Stun` `Knock down`)
- Scarlita (94% `Stun` `Knock down`)
- Antandra (85% `Stun` `Knock down`)

### Summary for Zorya

#### Zorya Provides

- Cheat death — Self
- Invincibility — Self

#### Damage types dealt by Zorya

- Magic — Arc, Area, Single target
- HP loss — Single target — `high`

#### Debuffs provided by Zorya

- Haste (Mythic+) — Area — `high`
- Movement speed (Mythic+) — Area — `average`

#### Crowd Control provided by Zorya

- Steadfast — Self — On skill
- Unaffected (EX+10) — Self — Conditional
- Knock down — Arc — `average`
- Stun — Area — `average`

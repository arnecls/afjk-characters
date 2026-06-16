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
- **Behavior tags**: `ally-buffer` `cheat-death` `execute` `hp-scaling` `mark-target`
- **Ally composition**: grants Brightfeather to nearest ally in her row
- **Damage types**: Physical `high`, HP loss `low`, Max HP-based damage `high`

#### Play overview

Aliceth **bonds one ally at battle start**, empowering their strikes so follow-up attacks land after a set number of hits. Her active skill delivers a **heavy strike with knockback and stun** on a focused target when activated. She marks the **farthest enemy**, and she and bonded allies **prioritize that target** until it falls, then her battle ATK climbs for the rest of the fight. Her ultimate fires **arrow volleys** at a single foe, growing heavier when her partner meets feather thresholds. She also blocks the **first fatal blow** on herself or her bonded ally. Against **spread formations**, the mark and focus fire fail to concentrate damage. If the bonded ally dies early, much of her buffing and ultimate scaling is lost entirely.

#### Skill overview

- **Signature skill (ult)**: speed `average`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `high`

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

Look for units providing: `ATK` `Healing` `DEF Penetration`  
Common buffers are **Twins**, **Solise**, or **Hugin**.

- **Contess**
  - ATK buff (single target, high)
  - Direct healing (single target, high)
- **Himmel**
  - ATK buff (single target, high)
  - Direct healing (single target, low)
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
- **Velara**
  - Direct healing (area, low)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, average) `signature fuel`

### Units benefitting most from Aliceth

Aliceth provides Ally empower buff to single targets `high`, Attack range buff to single targets `high`, DEF Penetration buff to multiple targets `high`, ATK buff (Legendary+) to multiple targets `low`, and Fatal blow immunity (Mythic+) to single targets `high` — conditional (rare).

- Lily May (3.2 / 5)
- Nerion (3.0 / 5)
- Kulu (2.9 / 5)
- Kordan (2.7 / 5)

### Units that can act as a replacement for Aliceth

**Best overall replacement**

- Athalia (60% `Damage`)
- Vala (51% `Damage`)

**Similar Skills**

- Silven (48% `hp-scaling` `mark-target`)
- Nazrik (48% `hp-scaling` `mark-target`)
- Faramor (34% `ally-buffer` `hp-scaling`)

**Damage**

- Athalia (100% `Physical` `Max HP-based damage` `HP loss`)
- Nara (100% `Physical` `Max HP-based damage` `HP loss`)
- Vala (95% `Physical` `Max HP-based damage` `HP loss`)

**Crowd Control**

- Twins (93% `Blind` `Knock back`)
- Damian (91% `Blind` `Stun`)
- Hepler (91% `Blind` `Stun`)

### Summary for Aliceth

#### Aliceth Provides

- Ally grant (Brightfeather) — Single target
- Instant defeat — Single target
- Invincibility — Single target
- Marked target (focus fire) — Single target
- Reposition enemies — Single target
- Fatal blow save (Mythic+) — Single target

#### Damage types dealt by Aliceth

- Physical — Area, Single target
- HP loss — Single target — `low`
- Max HP-based damage — Single target — `average`

#### Debuffs provided by Aliceth

- Execution — Single target — `low`
- Marked target (focus fire) — Multiple targets — `average`
- Blind HP loss (EX+15) — Single target — `low`

#### Crowd Control provided by Aliceth

- Knock back — Single target — `low`
- Stun — Single target — `average`
- Blind (EX+15) — Area — `average`

## Alna

### Alna's behavior

`AFK Stages [S+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S+]`

- **Signature skill**: Shared Resolve (Skill 1)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-buffer` `aoe-damage` `cc-immunity` `invincibility`
- **Ally composition**: place ally in same row at battle prep (Winter Warrior buffs)
- **Damage types**: Physical `high`, DoT `high`, Max HP-based damage `high`

#### Play overview

Before battle, Alna **requires a Winter Warrior in her row**, chosen during prep, who gains extra max HP and shared healing while resisting her opening frost. At fight start she blankets the field in frost, **cutting Haste and attack range** for nearly everyone, then cycles **damage and control immunity** windows that can extend to her partner as well. Her blizzard strips enemy Haste buffs and deals steady damage over time. Damage she or the Winter Warrior takes is then converted into **delayed healing**. Against **targets immune to Haste or range reduction**, much of her control is wasted while allies still suffer the frost penalty. She also needs **sustained fight time** to reapply her ultimate and periodic immunity cycles.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `average`
- **Ultimate**: speed `slow`, first cast speed `fast`, heal `average`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `high`

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

Look for units providing: `Max HP` `Healing`  
Common buffers are **Solise**, **Twins**, or **Smokey & Meerky**.

- **Zanie**
  - Max HP buff (single target, high)
  - Direct healing (single target, high)
- **Contess**
  - Direct healing (single target, high)
- **Velara**
  - Direct healing (area, low)
- **Himmel**
  - Direct healing (single target, low)
- **Hewynn**
  - Healing over time (all units, high)

### Units benefitting most from Alna

Alna provides Ally empower buff to single targets `high`, Max HP buff to single targets `high`, Dmg and CC immunity (EX+15) to single targets `high`, and ATK buff (Supreme+) to single targets `average`.

- Shadewing (3.3 / 5)

### Units that can act as a replacement for Alna

**Similar Skills**

- Perseus (50% `ally-buffer` `aoe-damage`)
- Dunlingr (48% `ally-buffer` `aoe-damage`)
- Himmel (40% `ally-buffer` `aoe-damage`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage` `DoT`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Thador (100% `DoT` `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Lorsan (95% `Haste debuff` `Max HP debuff`)

**Crowd Control**

- Eironn (100% `Bind`)
- Kordan (100% `Bind`)
- Evie (100% `Bind`)

### Summary for Alna

#### Alna Provides

- Ally empower — Single target
- Dmg and CC immunity (Mythic+) — Self
- Dmg and CC immunity (ally) (EX+15) — Single target

#### Damage types dealt by Alna

- Physical — Arc, Area, Single target
- DoT — All units
- Max HP-based damage — All units, Area, Single target — `high`

#### Debuffs provided by Alna

- Haste — All units — `average`
- Max HP — Single target — `low`
- Vitality (Supreme+) — Area — `low`

#### Crowd Control provided by Alna

- Immune (Mythic+) — Self — Start of battle
- Bind (Supreme+) — Area — `average`

## Alsa

### Alsa's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Twirling Rocks (ultimate)
- **Movement**: mostly stationary (avg attack range 6.0 tiles)
- **Behavior tags**: `battlefield-modification` `self-repositioner` `transformation`
- **Damage types**: Magic `average`, Max HP-based damage `average`

#### Play overview

Alsa enters a **combat stance** that boosts damage and dodge, then fights from that posture for the rest of the fight. Her ultimate curls into a ball, **damaging nearby enemies** and creating terrain obstacles that reshape paths across the field. She punishes **recently controlled foes** with AoE strikes and gains haste as the battle wears on. In stance she slams for extra hits and **evades incoming blows**, rolling away with a shield when pressed. Bonus damage also lands on **multiply-controlled targets**, rewarding teams that chain crowd control together. Terrain obstacles can block enemy movement and funnel foes into follow-up strikes. Against **immune or ungrouped targets**, her control payoff and obstacle value shrink sharply. Her habit of **rolling out of position** also leaves her exposed when enemies focus her down.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, buffs `average`, debuffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, damage `average`

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

Look for units providing: `Haste` `Shield`  
Common buffers are **Twins**, **Hugin**, or **Damian**.

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Shield (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Tasi**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Alsa

- Bonnie (2.6 / 5)
- Carolina (1.8 / 5)
- Indris (1.6 / 5)

### Units that can act as a replacement for Alsa

**Best overall replacement**

- Galahad (77% `Damage` `Debuffs on enemies`)
- Zorya (65% `Damage` `Debuffs on enemies` `Crowd Control`)
- Natsu (63% `Damage` `Crowd Control`)

**Similar Skills**

- Kulu (66% `battlefield-modification` `self-repositioner`)
- Athalia (60% `self-repositioner` `transformation`)
- Tasi (40% `self-repositioner` `transformation`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Galahad (100% `Movement speed debuff`)
- Kulu (100% `Movement speed debuff`)
- Zorya (100% `Movement speed debuff`)

**Crowd Control**

- Perseus (100% `Stun` `Knock back`)
- Scarlita (100% `Stun` `Knock back`)
- Lenya (100% `Stun` `Knock back`)

### Summary for Alsa

#### Alsa Provides

- Enhanced form — Single target

#### Damage types dealt by Alsa

- Magic — All units, Area, Single target
- Max HP-based damage — Single target — `average`

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
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `low`

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

Look for units providing: `Max HP` `Shield` `Healing` `Energy`  
Common buffers are **Twins**, **Smokey & Meerky**, or **Hugin**.

- **Hepler**
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Koko**
  - Shield (all units, low)
  - Direct healing (all units, average)
- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
  - Direct healing (single target, high)
- **Marcille**
  - Direct healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Ludovic**
  - Direct healing (multiple targets, high)

### Units benefitting most from Antandra

Antandra provides DEF buff (Supreme+) to single targets `low`.

- Carolina (3.1 / 5)
- Shadewing (2.6 / 5)
- Nerion (2.3 / 5)

### Units that can act as a replacement for Antandra

**Best overall replacement**

- Lumont (100% `Buffs on allies` `Damage` `Debuffs on enemies`)
- Lucca (80% `Buffs on allies` `Crowd Control` `Damage`)
- Scarlita (62% `Buffs on allies` `Crowd Control` `Damage`)

**Buffs on allies**

- Twins (100% `Magic DEF` `Physical DEF`)
- Tilaya (100% `Magic DEF` `Physical DEF`)
- Scarlita (100% `Magic DEF` `Physical DEF`)

**Similar Skills**

- Galahad (48% `ally-shielder` `aoe-damage`)
- Brutus (41% `aoe-damage` `taunt`)
- Scarlita (40% `ally-shielder` `aoe-damage`)

**Damage**

- Baelran (100% `Physical`)
- Himmel (100% `Physical`)
- Alna (100% `Physical`)

**Debuffs on enemies**

- Bonnie (100% `ATK debuff`)
- Lumont (100% `ATK debuff`)
- Lyca (95% `ATK debuff`)

**Crowd Control**

- Hepler (100% `Stun` `Taunt`)
- Lucca (90% `Stun` `Knock down`)
- Callan (75% `Stun` `Knock down`)

### Summary for Antandra

#### Antandra Provides

- Stacking buff (Supreme+) — Single target

#### Damage types dealt by Antandra

- Physical — Arc, Area

#### Debuffs provided by Antandra

- ATK — Arc — `average`

#### Crowd Control provided by Antandra

- Unaffected — Area — On skill
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
Common buffers are **Twins**, **Rowan**, or **Ravion**.

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Pandora**
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Arden

- Carolina (3.6 / 5)
- Nerion (2.6 / 5)
- Shadewing (1.7 / 5)

### Units that can act as a replacement for Arden

**Best overall replacement**

- Frieren (57% `Damage`)
- Faramor (55% `Damage`)
- Lorsan (55% `Damage` `Similar Skills`)

**Similar Skills**

- Lorsan (80% `aoe-damage` `dot-specialist`)
- Gwyneth (60% `dot-specialist` `mass-cc`)
- Natsu (60% `aoe-damage` `dot-specialist` `mass-cc`)

**Damage**

- Frieren (100% `DoT` `Magic`)
- Faramor (100% `DoT`)
- Cyran (100% `DoT` `Magic`)

**Crowd Control**

- Eironn (100% `Bind`)
- Kordan (100% `Bind`)
- Evie (100% `Bind`)

### Summary for Arden

#### Damage types dealt by Arden

- Magic — Area
- DoT — Multiple targets, Single target

#### Crowd Control provided by Arden

- Bind — All units — `average`

## Atalanta

### Atalanta's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Wild Sniper (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `aoe-damage` `battle-start-burst` `self-repositioner`
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Play overview

Atalanta opens with **rapid chained casts** of her knockback and explosive shots before settling into normal pacing. Her ultimate dashes forward, then fires a **penetrating line shot** that can clip several foes. Hitting different enemies **raises her haste**, rewarding wide target access early. A direct ultimate hit also **heals herself**. Splash from her explosives only carries **partial damage**, so grouped hits feel weaker than the main strike. She struggles when **frontlines block her line** or when burst windows end before she can line up a clean shot.

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, damage `average`

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

Look for units providing: `Haste` `Healing` `Physical DEF`  
Common buffers are **Twins**, **Damian**, or **Hugin**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Hewynn**
  - Healing over time (all units, high)
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
  - Direct healing (all units, low)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Tilaya**
  - DEF buff (area, high)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Atalanta

- Carolina (3.1 / 5)
- Nerion (2.3 / 5)
- Shadewing (2.2 / 5)

### Units that can act as a replacement for Atalanta

**Best overall replacement**

- Perseus (80% `Damage` `Crowd Control`)
- Gwyneth (67% `Damage`)
- Kafra (61% `Damage` `Debuffs on enemies`)

**Similar Skills**

- Dionel (60% `aoe-damage` `self-repositioner`)
- Rhys (60% `aoe-damage` `self-repositioner`)
- Himmel (50% `aoe-damage` `self-repositioner`)

**Damage**

- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)
- Aliceth (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Brutus (100% `Phys DEF debuff`)
- Lyca (100% `Phys DEF debuff`)
- Laios (100% `Phys DEF debuff`)

**Crowd Control**

- Perseus (100% `Stun` `Knock back`)
- Lucca (80% `Stun`)
- Scarlita (75% `Stun` `Knock back`)

### Summary for Atalanta

#### Atalanta Provides

- Reposition enemies — Single target
- Stat steal (EX+10) — Single target

#### Damage types dealt by Atalanta

- Physical — Area, Single target
- Max HP-based damage — Area — `average`

#### Debuffs provided by Atalanta

- Phys DEF (Supreme+) — Single target — `average`

#### Crowd Control provided by Atalanta

- Bind — Single target — `average`
- Knock back — Single target — `low`
- Stun — Area — `average`

## Athalia

### Athalia's behavior

`AFK Stages [A+]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Unbroken Retribution (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `hp-scaling` `self-repositioner` `transformation`
- **Damage types**: Physical `high`, HP loss `high`, Max HP-based damage `high`, True damage `average`

#### Play overview

Athalia **dives behind the highest damage dealer**, slashing foes in her path while healing herself. Her ultimate deals **massive true damage** to whoever has dealt the most cumulative damage. Repeated dashes trigger **extra area slashes** that also **strip enemy shields**. She excels at **bursting isolated carries** but offers little when fights demand sustained pressure.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, buffs `average`, damage `high`
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

Look for units providing: `Max HP` `CRIT` `Execution` `Healing`  
Common buffers are **Solise**, **Twins**, or **Smokey & Meerky**.

- **Zanie**
  - Max HP buff (single target, high)
  - Direct healing (single target, high)
- **Contess**
  - Direct healing (single target, high)
- **Velara**
  - Direct healing (area, low)
- **Himmel**
  - Direct healing (single target, low)
- **Hewynn**
  - Healing over time (all units, high)

### Units benefitting most from Athalia

- Shadewing (1.7 / 5)
- Carolina (1.4 / 5)
- Nerion (1.2 / 5)

### Units that can act as a replacement for Athalia

**Best overall replacement**

- Baelran (80% `Damage` `Similar Skills` `Crowd Control`)
- Sylphira (63% `Crowd Control`)
- Nara (62% `Damage` `Crowd Control`)

**Similar Skills**

- Baelran (80% `hp-scaling` `transformation`)
- Marilee (80% `hp-scaling` `self-repositioner`)
- Lily May (60% `hp-scaling` `self-repositioner` `transformation`)

**Damage**

- Nara (100% `Physical` `True damage` `Max HP-based damage` `HP loss`)
- Faramor (98% `True damage` `Physical` `HP loss`)
- Baelran (94% `True damage` `Physical` `Max HP-based damage`)

**Crowd Control**

- Frieren (100% `Knock down`)
- Baelran (100% `Knock down`)
- Himmel (100% `Knock down`)

### Summary for Athalia

#### Athalia Provides

- Invincibility — Single target
- Transformation — Self

#### Damage types dealt by Athalia

- Physical — All units, Area, Single target
- HP loss — All units — `high`
- Max HP-based damage — Area — `high`
- True damage — All units, Single target — `average`

#### Crowd Control provided by Athalia

- Unaffected — Self — On skill
- Knock down — Single target — `low`

## Aurora

### Aurora's behavior

`AFK Stages [A+]`, `Dream Realm [A+]`, `Dream Realm (Endless) [S+]`, `PVP [B]`

- **Signature skill**: Starlit Slumber (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `invincibility` `mark-target` `summoner`
- **Damage types**: Magic `high`, Max HP-based damage `high`

#### Play overview

Aurora summons a companion that **attacks and detonates for AoE damage**, then falls asleep to become **invincible** while buffing allied summons. Nearby enemies who linger are **transformed into harmless forms**, and her ATK scales with **summon variety** on the field. While asleep, allied summons are **enhanced** and her companion becomes unaffected. She shines beside **summon-heavy teams** but adds little when allies field few bodies or fights end before her sleep cycle.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `average`
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
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Galahad**
  - Haste buff (single target, average) `signature fuel`
- **Mehira**
  - Haste buff (single target, low) `signature fuel`
- **Velara**
  - Haste buff (single target, low) `signature fuel`
- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)
- **Kazim**
  - ATK buff (single target, high)
  - Haste buff (multiple targets, average) `signature fuel`

### Units benefitting most from Aurora

Aurora provides Haste buff to summons `high` and Summon damage buff (Mythic+) to summons `low`.

- Florabelle (3.7 / 5)
- Zanie (3.3 / 5)
- Cecia (3.1 / 5)
- Dunlingr (2.8 / 5)
- Phraesto (2.7 / 5)
- Mehira (2.1 / 5)

### Units that can act as a replacement for Aurora

**Similar Skills**

- Silven (25% `mark-target`)
- Zanie (25% `summoner`)
- Florabelle (25% `summoner`)

**Damage**

- Galahad (100% `Magic` `Max HP-based damage`)
- Twins (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Galahad (100% `Haste debuff`)
- Velara (100% `Haste debuff`)
- Alna (100% `Haste debuff`)

**Crowd Control**

- Galahad (100% `Bind`)
- Saida (100% `Bind`)
- Velara (100% `Bind`)

### Summary for Aurora

#### Aurora Provides

- Dream sleep (transformation) — Self
- Invincibility — Self
- Summoning — Single target

#### Damage types dealt by Aurora

- Magic — Area, Single target
- Max HP-based damage — Area, Single target — `high`

#### Debuffs provided by Aurora

- Haste — Single target — `average`

#### Crowd Control provided by Aurora

- Unaffected — Self — On skill
- Bind — Area — `low`

## Baelran

### Baelran's behavior

`AFK Stages [S]`, `Dream Realm [A]`, `Dream Realm (Endless) [S]`, `PVP [S]`

- **Signature skill**: Celestial Rise (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `hp-scaling` `transformation`
- **Damage types**: Physical `high`, Max HP-based damage `high`, True damage `average`

#### Play overview

Baelran leans on a **massive HP pool** and passive regeneration, then transforms when shields decay or bonus HP triggers. In enhanced form he gains **unaffected status** and his ultimate deals **frontal true damage** with HP restore. Each form shift raises haste over time. His hits also **permanently shave enemy max HP** while transformed. He needs **reliable single-target healing** to cycle forms safely.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, damage `high`
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

Look for units providing: `ATK` `Haste` `Shield` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Solise**.

- **Contess**
  - ATK buff (single target, high)
  - Shield (single target, average)
  - Direct healing (single target, high)
- **Himmel**
  - ATK buff (single target, high)
  - Shield (single target, average)
  - Direct healing (single target, low)
- **Gunnar**
  - ATK buff (single target, high)
  - Shield (single target, average)
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - Shield (single target, average)
- **Velara**
  - Haste buff (single target, low) `signature fuel`
  - Direct healing (area, low)

### Units benefitting most from Baelran

- Carolina (3.1 / 5)
- Nerion (2.3 / 5)
- Kazim (2.0 / 5)

### Units that can act as a replacement for Baelran

**Best overall replacement**

- Sylphira (68% `Crowd Control` `Debuffs on enemies` `Damage`)

**Similar Skills**

- Athalia (80% `hp-scaling` `transformation`)
- Silven (33% `hp-scaling`)
- Lily May (33% `hp-scaling` `transformation`)

**Damage**

- Himmel (100% `True damage` `Physical` `Max HP-based damage`)
- Athalia (100% `True damage` `Physical` `Max HP-based damage`)
- Sylphira (98% `Max HP-based damage` `True damage`)

**Debuffs on enemies**

- Shemira (100% `Max HP debuff`)
- Alna (100% `Max HP debuff`)
- Sylphira (100% `Max HP debuff`)

**Crowd Control**

- Sylphira (100% `Knock down`)
- Callan (63% `Knock down`)
- Zorya (63% `Knock down`)

### Summary for Baelran

#### Baelran Provides

- Enhanced form (Mythic+) — Area
- Dispel debuffs (EX+15) — Self

#### Damage types dealt by Baelran

- Physical — Area, Single target
- Max HP-based damage — Area — `high`
- True damage — Arc, Area, Single target — `average`

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
- **Behavior tags**: `assassin` `cheat-death` `clone` `stealth`
- **Damage types**: Magic `average`, DoT `average`, Max HP-based damage `average`

#### Play overview

Berial hunts **isolated enemies** with no allies within one tile, bouncing in stealth to drain energy and frighten nearby foes. If no one is isolated, he **heals and retreats** instead of pressing the attack. He can **revive from a newly defeated enemy** after his own death, and stealth duration **extends after he falls**. Isolated targets also suffer **penalized damage dealt and taken**, and may spawn decaying decoy summons. He dominates **scattered backlines** but does little when enemies stay **packed together**. Teams that protect rear targets or deny isolated picks waste his assassin kit.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, buffs `average`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `low`

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

Look for units providing: `Healing`  
Common buffers are **Solise**, **Rowan**, or **Twins**.

- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)
- **Hewynn**
  - Healing over time (all units, high)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Pandora**
  - Direct healing (single target, average)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Berial

- Carolina (3.1 / 5)
- Nerion (2.3 / 5)
- Shadewing (2.2 / 5)

### Units that can act as a replacement for Berial

**Best overall replacement**

- Saida (87% `Damage` `Debuffs on enemies`)
- Silvina (76% `Damage` `Debuffs on enemies` `Crowd Control`)
- Lily May (58% `Damage` `Debuffs on enemies`)

**Similar Skills**

- Seth (24% `assassin`)
- Saida (24% `cheat-death`)
- Harak (24% `assassin`)

**Damage**

- Frieren (100% `DoT` `Magic` `Max HP-based damage`)
- Mehira (100% `DoT` `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `DoT` `Max HP-based damage`)

**Debuffs on enemies**

- Saida (100% `Energy drain` `Damage dealt debuff`)
- Lily May (100% `Energy drain`)
- Silvina (100% `Energy drain`)

**Crowd Control**

- Silvina (80% `Frighten`)

### Summary for Berial

#### Berial Provides

- Cheat death — Self
- Invincibility — Self
- Summoning (Mythic+) — Single target

#### Damage types dealt by Berial

- Magic — Area, Single target
- DoT — Single target
- Max HP-based damage — Area, Single target — `average`

#### Debuffs provided by Berial

- Energy drain — Single target — `average`
- Damage dealt (Legendary+) — Single target — `low`
- Damage taken (Legendary+) — Single target — `low`

#### Crowd Control provided by Berial

- Frighten — Area — `average`

## Bonnie

### Bonnie's behavior

`AFK Stages [A]`, `Dream Realm [A]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Decay's Reach (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `aoe-damage` `battle-start-burst` `enemy-debuffer` `transformation`
- **Damage types**: Magic `average`

#### Play overview

Bonnie opens by placing an **Aging debuff** on the rearmost enemy, slowing haste and stacking when allies deal magic damage to that target. Her ultimate hits AoE for **bonus damage and stun** against debuffed targets. She can **turn to mist and reposition** when threatened, and the debuff **spreads on max stack or death**. Max-stack victims also take **increased magic damage**, making magic dealers ideal partners. Battle ATK growth adds steady personal damage over time. She deals **less raw damage** than top burst dealers but excels when debuffs can spread across multiple targets. Against **immune or cleanse-heavy lines**, her debuff chain and ultimate payoff never build.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, debuffs `average`, damage `low`
- **Ultimate**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `average`

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
Common buffers are **Ravion**, **Twins**, or **Solise**.

Bonnie also requires units **dealing magic damage** and/or units **putting debuffs** on enemies

- **Cyran**
  - Enables Debuff on target via ATK SPD debuff (all units)
  - Enables Magic damage from allies via Magic damage + wide area (area)
- **Dunlingr**
  - ATK buff (single target, low)
  - Enables Debuff on target via Haste debuff (all units)
  - Enables Magic damage from allies via Magic damage (area)
- **Kulu**
  - ATK buff (single target, low)
  - Enables Debuff on target via Damage taken debuff (all units)
- **Evie**
  - ATK buff (multiple targets, high)
  - Enables Debuff on target via Magic DEF debuff (all units)
  - Enables Magic damage from allies via Magic damage (single target)
- **Frieren**
  - ATK buff (single target, high)
  - Enables Debuff on target via DoT (area)
  - Enables Magic damage from allies via Magic damage (area)

### Units benefitting most from Bonnie

- Shadewing (2.4 / 5)
- Indris (1.9 / 5)
- Carolina (1.8 / 5)

### Units that can act as a replacement for Bonnie

**Best overall replacement**

- Nerion (50% `Damage` `Crowd Control`)

**Similar Skills**

- Nerion (57% `battle-start-burst` `enemy-debuffer`)
- Cassadee (48% `aoe-damage` `enemy-debuffer`)
- Cyran (40% `aoe-damage` `battle-start-burst`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Lorsan (56% `Haste debuff`)

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

- ATK — Single target — `average`
- Haste — Single target — `average`
- Magic damage amplification (Supreme+) — Single target — `low`

#### Crowd Control provided by Bonnie

- Stun — Single target — `average`

## Brutus

### Brutus's behavior

`AFK Stages [A]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Indomitable (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `aoe-damage` `cheat-death` `invincibility` `life-drain` `taunt`
- **Damage types**: Physical `high`, DoT `average`, Max HP-based damage `average`

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

Look for units providing: `Life Drain`

- **Dunlingr**
  - Lifedrain buff (all units, average)
- **Koko**
  - Lifedrain buff (multiple targets, average)
- **Zandrok**
  - Lifedrain buff (area, low, conditional (frequent))
- **Daimon**
  - Lifedrain buff (single target, average)
- **Kordan**
  - Lifedrain buff (multiple targets, low)

### Units benefitting most from Brutus

Brutus provides Lifedrain buff to single targets `average`.

- Satrana (2.2 / 5)

### Units that can act as a replacement for Brutus

**Best overall replacement**

- Lumont (71% `Crowd Control` `Damage`)
- Hepler (67% `Crowd Control` `Damage`)

**Buffs on allies**

- Dunlingr (100% `Life Drain`)
- Kordan (100% `Life Drain`)
- Shakir (100% `Life Drain`)

**Similar Skills**

- Igor (42% `aoe-damage` `cheat-death` `life-drain`)
- Antandra (41% `aoe-damage` `taunt`)
- Thoran (40% `cheat-death` `life-drain`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage` `DoT`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Lyca (100% `Phys DEF debuff`)
- Laios (100% `Phys DEF debuff`)
- Kafra (87% `Phys DEF debuff`)

**Crowd Control**

- Phraesto (100% `Taunt`)
- Hepler (100% `Taunt`)
- Antandra (100% `Taunt`)

### Summary for Brutus

#### Damage types dealt by Brutus

- Physical — Arc, Single target
- DoT — Area
- Max HP-based damage — Arc, Area, Single target — `average`

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
- **Behavior tags**: `battle-start-ult` `cheat-death` `summoner`
- **Damage types**: Magic `high`, DoT `average`

#### Play overview

Bryon opens with a **battle-start companion summon** that fights beside him and gains haste while she remains on the field. His projectiles **drain enemy energy** on hit, and his companion **counterattacks and stuns** when he is controlled or struck hard, also blocking fatal blows. Casting his projectile skill also **spawns leaves near the companion** for extra pressure. He deals strong **multi-target magic damage** when enemies are grouped. He underperforms when the companion **dies early** or when foes are **spread beyond projectile reach**.

#### Skill overview

- **Signature skill**: speed `slow`, debuffs `average`
- **Ultimate**: speed `fast`, first cast speed `fast`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, debuffs `average`, damage `average`

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

Look for units providing: `Haste` `Healing` `Energy`  
Common buffers are **Twins**, **Smokey & Meerky**, or **Damian**.

- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Marcille**
  - Haste buff (single target, low) `signature fuel`
  - Direct healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Tasi**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Bryon

- Bonnie (2.5 / 5)
- Shadewing (2.3 / 5)
- Indris (2.2 / 5)

### Units that can act as a replacement for Bryon

**Best overall replacement**

- Natsu (66% `Damage` `Crowd Control` `Debuffs on enemies`)
- Saida (50% `Damage`)

**Similar Skills**

- Florabelle (36% `summoner`)
- Zanie (25% `summoner`)
- Saida (24% `cheat-death`)

**Damage**

- Saida (100% `Magic` `DoT`)
- Cyran (100% `Magic` `DoT`)
- Cryonaia (100% `Magic` `DoT`)

**Debuffs on enemies**

- Dunlingr (100% `Haste debuff` `Energy drain`)
- Vala (100% `Haste debuff` `Energy drain`)
- Granny Dahnie (100% `Haste debuff` `Energy drain`)

**Crowd Control**

- Contess (100% `Stun`)
- Aliceth (100% `Stun`)
- Faramor (100% `Stun`)

### Summary for Bryon

#### Bryon Provides

- Summoning — Single target
- Cheat death (EX+5) — Self
- Counterattack (EX+10) — Single target

#### Damage types dealt by Bryon

- Magic — Single target
- DoT — Area

#### Debuffs provided by Bryon

- Energy drain — Single target — `low`
- Haste — Area — `low`

#### Crowd Control provided by Bryon

- Stun (Mythic+) — Single target — `low`

## Callan

### Callan's behavior

`AFK Stages [A+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Restless Guardian (ultimate)
- **Movement**: moving (inactive while ultimate is running)
- **Behavior tags**: `ally-shielder` `cc-immunity`
- **Damage types**: Magic `high`

#### Play overview

Callan grants **shields at battle start and on ultimate cast**, absorbing damage meant for nearby allies at the opening of fights. His multi-hit skill **knocks down** the target and nearby enemies, while absorbed damage is **stored for a burst release** on his second skill. Once per battle, low HP triggers an **AoE burst and stun** on nearby foes. He also heals whenever he gains any shield, and battle vitality **grows over time** to keep him standing through long engagements. He is a **strong opening protector** but offers weak retaliation compared to dedicated counter tanks. His stored burst also **underwhelms against heavily armored targets** that shrug off the release. He provides no offensive buffs for allies once shields fall. Fights that **bypass or strip shields** leave him with little damage and no team buffs to contribute once his protection windows end.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, first cast speed `fast`, buffs `average`
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

Look for units providing: `Shield` `Healing`  
Common buffers are **Solise**, **Smokey & Meerky**, or **Hugin**.

- **Koko**
  - Shield (all units, low)
  - Direct healing (all units, average)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)
- **Contess**
  - Shield (single target, average)
  - Direct healing (single target, high)

### Units benefitting most from Callan

Callan provides Shield to single targets `low`.

- Carolina (3.6 / 5)
- Nerion (2.7 / 5)
- Bonnie (1.8 / 5)

### Units that can act as a replacement for Callan

**Best overall replacement**

- Phraesto (68% `Buffs on allies` `Damage`)
- Hepler (60% `Buffs on allies` `Crowd Control`)
- Zorya (57% `Crowd Control` `Damage`)

**Buffs on allies**

- Gunnar (100% `Shield`)
- Contess (100% `Shield`)
- Galahad (100% `Shield`)

**Similar Skills**

- Lucca (40% `ally-shielder`)
- Daimon (36% `ally-shielder`)
- Pang (33% `ally-shielder`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Crowd Control**

- Zorya (100% `Stun` `Knock down`)
- Antandra (100% `Stun` `Knock down`)
- Lucca (100% `Stun` `Knock down`)

### Summary for Callan

#### Callan Provides

- Damage absorption (allies) — Multiple targets
- Stored damage release — Self

#### Damage types dealt by Callan

- Magic — All units, Single target

#### Crowd Control provided by Callan

- Unaffected — Self — Start of battle
- Knock down — All units — `low`
- Stun (Mythic+) — All units — `average`

## Carolina

### Carolina's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Frozen Grave (ultimate)
- **Movement**: mostly stationary (avg attack range 4.0 tiles)
- **Behavior tags**: `dot-specialist` `enemy-debuffer`
- **Damage types**: Magic `high`

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
Common buffers are **Damian**, **Twins**, or **Rowan**.

Carolina also requires units **applying crowd control** to enemies

- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Enables CC on enemies via Blind (area, high)
- **Eironn**
  - Enables CC on enemies via Bind (area, high)
- **Kordan**
  - Enables CC on enemies via Bind (area, high)
- **Lorsan**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
  - Enables CC on enemies via Stun (multiple targets, high)
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
  - Enables CC on enemies via Stun (single target, average)

### Units benefitting most from Carolina

- Bonnie (2.8 / 5)
- Shadewing (2.3 / 5)
- Indris (2.2 / 5)

### Units that can act as a replacement for Carolina

**Best overall replacement**

- Shadewing (54% `Similar Skills`)
- Eironn (51% `Damage` `Debuffs on enemies` `Crowd Control`)

**Similar Skills**

- Shadewing (100% `dot-specialist` `enemy-debuffer`)
- Nerion (96% `dot-specialist` `enemy-debuffer`)
- Kruger (40% `enemy-debuffer`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Bonnie (100% `Haste debuff`)
- Eironn (100% `Haste debuff` `Magic DEF debuff`)
- Zorya (100% `Haste debuff`)

**Crowd Control**

- Eironn (100% `Bind`)
- Kordan (100% `Bind`)
- Evie (100% `Bind`)

### Summary for Carolina

#### Carolina Provides

- Stacking buff — Area

#### Damage types dealt by Carolina

- Magic — Area, Single target

#### Debuffs provided by Carolina

- Haste — Area — `low`
- Magic DEF (Mythic+) — Area — `low`

#### Crowd Control provided by Carolina

- Bind — Single target — `high`

## Cassadee

### Cassadee's behavior

`AFK Stages [C]`, `Dream Realm [A]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Tidal Strength (Skill 2)
- **Movement**: stationary (avg attack range 10.0 tiles)
- **Behavior tags**: `ally-buffer` `aoe-damage` `enemy-debuffer`
- **Ally composition**: nearest ally auto-selected at battle start; prioritizes ally behind
- **Damage types**: Magic `high`, Max HP-based damage `high`

#### Play overview

Cassadee blesses one ally so their attacks **deal bonus magic damage** to struck enemies, keeping haste high while that ally lives. Her heavy single-target strike adds direct pressure, and her ultimate **knocks back foes in a line** while temporarily blessing allies it touches. The ultimate path also **lowers enemy Magic DEF** for a window after impact. She blends **damage, soft control, and ally amplification** in one slot. She falters when the **blessed ally dies early** or when enemies **dodge the line attack**. Without a **partner who attacks often**, her blessing contributes little sustained value over the fight. Her haste growth rewards keeping the blessed ally alive through sustained exchanges.

#### Skill overview

- **Signature skill**: speed `average`, first cast speed `fast`, buffs `average`, damage `low`
- **Ultimate**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `average`

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
Common buffers are **Twins**, **Hugin**, or **Damian**.

Cassadee also requires a unit **to bless**

- **Tasi**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Dunlingr**
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD via Haste buff (single target, average) `signature fuel`

### Units benefitting most from Cassadee

Cassadee provides Tidal Strength buff (Legendary+) to all units `low`.

- Carolina (2.3 / 5)
- Bonnie (2.1 / 5)
- Nerion (1.8 / 5)

### Units that can act as a replacement for Cassadee

**Similar Skills**

- Perseus (80% `ally-buffer` `aoe-damage`)
- Sonja (60% `ally-buffer` `aoe-damage`)
- Parisa (60% `ally-buffer` `aoe-damage`)

**Damage**

- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)
- Silven (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Velara (100% `Magic DEF debuff`)
- Thador (100% `Magic DEF debuff`)
- Shadewing (100% `Magic DEF debuff`)

**Crowd Control**

- Perseus (100% `Knock back` `Stun`)
- Scarlita (100% `Knock back` `Stun` `Knock up`)
- Soren (100% `Knock back` `Stun`)

### Summary for Cassadee

#### Cassadee Provides

- Ally blessing — Self

#### Damage types dealt by Cassadee

- Magic — All units, Single target
- Max HP-based damage — All units — `high`

#### Debuffs provided by Cassadee

- Magic DEF (Supreme+) — Single target — `low`

#### Crowd Control provided by Cassadee

- Knock back — All units — `low`
- Knock up — Single target — `low`
- Stun — Single target — `low`

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

- **Signature skill (ult)**: speed `average`, buffs `average`, damage `average`
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
Common buffers are **Twins**, **Hugin**, or **Solise**.

- **Tilaya**
  - DEF buff (area, high)
  - DEF buff (area, high)
- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)
- **Lucca**
  - DEF buff (area, average)
  - DEF buff (area, average)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Aliceth**
  - DEF Penetration buff (multiple targets, high)

### Units benefitting most from Cecia

Cecia provides DEF Penetration buff to single targets `low`, Lifedrain buff in an area `low`, and Max HP buff to single targets `high`.

- Nerion (2.4 / 5)
- Lily May (1.8 / 5)
- Silven (1.8 / 5)

### Units that can act as a replacement for Cecia

**Best overall replacement**

- Gwyneth (67% `Damage` `Debuffs on enemies`)
- Alna (58% `Damage` `Crowd Control` `Buffs on allies`)
- Faramor (52% `Damage`)

**Buffs on allies**

- Alna (87% `Max HP`)
- Tilaya (60% `Max HP`)

**Similar Skills**

- Hodgkin (60% `enemy-debuffer` `summoner`)
- Pandora (50% `enemy-debuffer` `mass-cc`)
- Temesia (33% `enemy-debuffer` `mass-cc`)

**Damage**

- Alna (100% `Physical` `DoT`)
- Faramor (100% `Physical` `DoT`)
- Gwyneth (100% `Physical` `DoT`)

**Debuffs on enemies**

- Sinbad (100% `Magic DEF debuff` `Phys DEF debuff` `Vitality debuff`)
- Shadewing (80% `Magic DEF debuff` `Phys DEF debuff`)
- Gwyneth (80% `Phys DEF debuff` `Vitality debuff`)

**Crowd Control**

- Eironn (100% `Bind`)
- Kordan (100% `Bind`)
- Evie (100% `Bind`)

### Summary for Cecia

#### Damage types dealt by Cecia

- Physical — Arc, Area, Single target
- DoT — Area, Single target

#### Debuffs provided by Cecia

- Magic DEF (Mythic+) — Single target — `low`
- Phys DEF (Mythic+) — Single target — `low`
- Vitality (EX+5) — Single target — `low`

#### Crowd Control provided by Cecia

- Bind — Area — `average`

## Chippy

### Chippy's behavior

- **Signature skill**: Brothers-in-arms (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `self-repositioner` `summoner`
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

- **Lyca**
  - Energy recovery (all units, low) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
- **Kazim**
  - ATK SPD via Haste buff (multiple targets, average) `signature fuel`
- **Lorsan**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Tasi**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Chippy

- Himmel (1.5 / 5)

### Units that can act as a replacement for Chippy

**Similar Skills**

- Marilee (40% `self-repositioner`)
- Zanie (40% `summoner`)
- Florabelle (33% `summoner`)

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
- **Behavior tags**: `ally-healer` `ally-shielder` `stealth` `untargetable`
- **Damage types**: Magic `low`, HP loss `low`

#### Play overview

Contess starts **hidden while recovering energy**, then emerges to heal an ally, grant rule immunity, and **convert their HP into shield**. She punishes foes who deal **large HP or shield loss**, healing weakest allies and cutting high-damage enemies' ATK. She also **slows ultimate casters' energy recovery** and stacks permanent ATK and energy penalties on repeat violations. Severe violations can trigger **permanent silence** and increased HP-loss effects that bypass unaffected. She needs **long fights** to cycle rules and punishments. Teams that **burst her before she emerges** or ignore her conduct rules see little from her kit.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, damage `low`
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
Common buffers are **Rowan**, **Smokey & Meerky**, or **Ravion**.

- **Lyca**
  - Energy recovery (all units, low) `signature fuel`
- **Seth**
  - Energy recovery (single target, average) `signature fuel`
- **Thoran**
  - Energy recovery (single target, average) `signature fuel`
- **Pandora**
  - Energy recovery (single target, low) `signature fuel`
- **Thador**
  - Energy recovery (single target, low) `signature fuel`

### Units benefitting most from Contess

Contess provides ATK buff to single targets `high`, Direct healing to multiple targets `high`, Exemption buff to single targets `high`, and Shield to single targets `average`.

**16** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Baelran (2.8 / 5)
- Evie (2.7 / 5)
- Aliceth (2.5 / 5)
- Faramor (2.5 / 5)
- Himmel (2.5 / 5)
- Alna (2.2 / 5)
- Athalia (2.2 / 5)
- Silven (2.2 / 5)
- Shemira (2.2 / 5)
- Sylphira (1.8 / 5)

### Units that can act as a replacement for Contess

**Healing**

- Solise (100% `Direct healing` `Healing`)
- Ludovic (100% `Direct healing` `Healing`)
- Smokey & Meerky (100% `Direct healing` `Healing`)

**Similar Skills**

- Solise (48% `ally-healer` `ally-shielder`)
- Velara (48% `ally-healer` `ally-shielder`)
- Twins (40% `ally-healer` `ally-shielder`)

**Damage**

- Mehira (100% `HP loss`)
- Aliceth (100% `HP loss`)
- Faramor (100% `HP loss`)

**Debuffs on enemies**

- Reinier (62% `Damage taken debuff` `ATK debuff`)

**Crowd Control**

- Gwyneth (50% `Silence` `Stun`)

### Summary for Contess

#### Damage types dealt by Contess

- HP loss — Single target — `low`

#### Debuffs provided by Contess

- ATK — Multiple targets — `low`
- Energy recovery — Multiple targets — `low`
- Max HP — Single target — `low`
- Damage taken (Mythic+) — Single target — `low`

#### Crowd Control provided by Contess

- Untargetable — Single target — On skill
- Silence (Mythic+) — Single target — `high`
- Stun (Supreme+) — Single target — `average`

## Cryonaia

### Cryonaia's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [B]`, `PVP [S]`

- **Signature skill**: Frostveil Domain (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Behavior tags**: `battlefield-modification` `cc-immunity` `invincibility`
- **Damage types**: Magic `high`, DoT `high`, Max HP-based damage `low`

#### Play overview

Cryonaia traps several enemies in a **separate winter domain**, gaining shields, control immunity, haste, and attack while it lasts. Only she can cast her ultimate inside, and **weakened foes inside can be instantly defeated**. Enemies entering the domain take **massive damage**, while her sweeping AoE crosses the entire battlefield and her projectiles chip priority targets. Her attack **grows the longer her shield holds**, rewarding teams that help her survive the setup phase. She is devastating once the domain is up but **vulnerable until her first ultimate** lands. Teams must **protect her during the wind-up** or she never reaches her peak. Fights that **break her shield quickly** or deny grouping end the domain before her execute can trigger. Once inside, she alone controls the pace and can chain ultimates while enemies are trapped.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, buffs `average`
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
Common buffers are **Hugin**, **Twins**, or **Mikola**.

- **Saida**
  - Shield (multiple targets, high)
- **Gunnar**
  - ATK buff (single target, high)
  - Shield (single target, average)
  - ATK SPD buff (single target, low) `signature fuel`
- **Pandora**
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Contess**
  - ATK buff (single target, high)
  - Shield (single target, average)
- **Himmel**
  - ATK buff (single target, high)
  - Shield (single target, average)

### Units benefitting most from Cryonaia

- Bonnie (2.5 / 5)
- Shadewing (1.9 / 5)
- Himmel (1.5 / 5)

### Units that can act as a replacement for Cryonaia

**Best overall replacement**

- Berial (66% `Damage` `Debuffs on enemies`)
- Mehira (50% `Damage` `Debuffs on enemies`)

**Similar Skills**

- Alna (40% `cc-immunity` `invincibility`)
- Lily May (34% `cc-immunity` `invincibility`)
- Kulu (30% `battlefield-modification`)

**Damage**

- Frieren (100% `DoT` `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `DoT` `Max HP-based damage`)
- Berial (100% `DoT` `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Contess (100% `Damage taken debuff`)
- Himmel (100% `Damage taken debuff`)
- Mehira (100% `Damage taken debuff`)

### Summary for Cryonaia

#### Cryonaia Provides

- Enemy isolation (domain) — Single target
- Battle time pause (EX+15) — Self
- Instant defeat (Supreme+) — Self

#### Damage types dealt by Cryonaia

- Magic — All units, Area, Single target
- DoT — All units, Single target
- Max HP-based damage — Single target — `low`

#### Debuffs provided by Cryonaia

- Damage taken (EX+5) — Single target — `low`

#### Crowd Control provided by Cryonaia

- Immune — Self — Conditional

## Cyran

### Cyran's behavior

`AFK Stages [S]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Gravitic Requiem (ultimate)
- **Movement**: mostly stationary (avg attack range 6.0 tiles)
- **Behavior tags**: `aoe-damage` `battle-start-burst` `enemy-grouping` `execute`
- **Damage types**: Magic `high`, DoT `high`, True damage `average`

#### Play overview

Cyran opens with **sequential battle-start spells** and a large initial energy bonus for fast ultimate access. His orbs chip multiple foes, and he **throws the nearest enemy** into the densest cluster to set up AoE follow-through. His ultimate places a **pull zone** that damages and executes low-HP enemies at the center. Battle crit growth rewards repeated casts on grouped targets. He excels at **disrupting clustered lines** and finishing wounded foes. His opening spell chain gives him **immediate board impact** before enemies can spread out. He adds little when enemies **stay spread** or resist grouping and execute thresholds.

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `average`

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
Common buffers are **Twins**, **Hugin**, or **Ravion**.

- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, average) `signature fuel`
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Velara**
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Cyran

- Bonnie (5.0 / 5)

### Units that can act as a replacement for Cyran

**Similar Skills**

- Eironn (60% `aoe-damage` `battle-start-burst` `enemy-grouping`)
- Atalanta (48% `aoe-damage` `battle-start-burst`)
- Walker (41% `aoe-damage` `battle-start-burst`)

**Damage**

- Korin (97% `True damage` `Max HP-based damage`)
- Temesia (93% `Max HP-based damage` `True damage`)
- Frieren (93% `DoT` `Magic` `True damage` `Max HP-based damage`)

**Debuffs on enemies**

- Sinbad (100% `ATK SPD debuff`)

**Crowd Control**

- Eironn (82% `Bind` `Displace`)
- Pippa (60% `Bind` `Displace` `Knock down`)
- Evie (56% `Bind` `Displace`)

### Summary for Cyran

#### Cyran Provides

- Artifact mimic (Mythic+) — Self
- Artifact block (EX+10) — Single target

#### Damage types dealt by Cyran

- Magic — Area, Single target
- DoT — Area
- True damage — All units — `average`

#### Debuffs provided by Cyran

- ATK SPD (Mythic+) — All units — `average`

#### Crowd Control provided by Cyran

- Unaffected (Mythic+) — Self — Start of battle
- Bind — Area — `low`
- Displace — All units — `low`
- Knock down — Area — `low`

## Daimon

### Daimon's behavior

`AFK Stages [A+]`, `Dream Realm [B]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Buddy Barrier (Skill 2)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-shielder` `hp-scaling` `summoner`
- **Ally composition**: place ally directly behind at battle prep (shield share, Life Drain, and ATK bond)
- **Damage types**: Magic `low`, Max HP-based damage `high`

#### Play overview

Daimon fights with an **untargetable companion** named Stitchy that frightens nearby enemies and joins his ultimate for true damage based on enemy HP. At battle start the companion attacks alongside him, dealing damage with basic attacks. He converts **enemy HP-loss into personal shield**, shares a portion of received shield with a **bonded ally**, and gains damage reduction while shielded. Excess shield value also **converts to HP** when overflowing, turning overheal into sustain. He blends **tanking, shielding, and sub-DPS** in one slot. He struggles as a **solo frontliner** without enough shield generation or a dedicated healer beside him. Teams that **deny HP-loss triggers** or kill his companion early blunt his sustain loop entirely. He pairs best with allies who generate frequent shields or trigger steady HP-loss on enemies.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `average`
- **Ultimate**: speed `slow`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `low`

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
Common buffers are **Twins** or **Hugin**.

- **Saida**
  - Shield (multiple targets, high)
- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
- **Phraesto**
  - Max HP buff (single target, low)
  - Shield (single target, average)
- **Contess**
  - Shield (single target, average)
- **Galahad**
  - Shield (single target, average)

### Units benefitting most from Daimon

Daimon provides Lifedrain buff to single targets `low` and Shield to multiple targets `low`.

- Brutus (2.2 / 5)
- Satrana (2.2 / 5)

### Units that can act as a replacement for Daimon

**Best overall replacement**

- Silvina (54% `Crowd Control` `Damage`)

**Buffs on allies**

- Gunnar (100% `Shield`)
- Hepler (100% `Shield`)
- Lucius (100% `Shield`)

**Similar Skills**

- Korin (66% `ally-shielder` `hp-scaling`)
- Scarlita (50% `ally-shielder` `hp-scaling`)
- Callan (36% `ally-shielder`)

**Damage**

- Gunnar (100% `Max HP-based damage`)
- Frieren (100% `Max HP-based damage` `Magic`)
- Baelran (100% `Max HP-based damage`)

**Crowd Control**

- Pandora (100% `Frighten`)
- Berial (100% `Frighten`)
- Silvina (100% `Frighten`)

### Summary for Daimon

#### Damage types dealt by Daimon

- Magic — Single target
- Max HP-based damage — Area, Single target — `high`

#### Crowd Control provided by Daimon

- Frighten (Mythic+) — Area — `low`

## Damian

### Damian's behavior

`AFK Stages [C]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Inventor's Will (Mythic+)
- **Movement**: stationary (off battlefield)
- **Behavior tags**: `ally-buffer` `ally-healer` `summoner`
- **Damage types**: Magic `high`

#### Play overview

Damian summons toys that **heal weakest allies, restore energy, stun distant foes, and blind enemies** from a chariot he can control. His summon aura grants **haste to adjacent allies**, and battle ATK rises over time. Blinds last longer while **summon health stays above half**. He mixes **healing, buffing, and soft control** through multiple summons. Fights that **focus and kill his toys early** remove his healing, control, and blind extension.

#### Skill overview

- **Signature skill**: speed `fast`, heal `average`, buffs `average`
- **Ultimate**: speed `average`, first cast speed `fast`, buffs `average`, damage `high`
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

Look for units providing: `ATK` `Haste` `Healing` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Solise**.

- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
- **Marcille**
  - Haste buff (single target, low) `signature fuel`
  - Direct healing (multiple targets, high)

### Units benefitting most from Damian

Damian provides Haste buff (Mythic+) to multiple targets `average` — conditional (frequent).

**25** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Carolina (5.0 / 5)
- Viperian (3.2 / 5)
- Atalanta (3.2 / 5)
- Lumont (3.2 / 5)
- Bryon (3.1 / 5)
- Lorsan (2.9 / 5)
- Fay (2.9 / 5)
- Alsa (2.9 / 5)
- Soren (2.8 / 5)
- Tasi (2.6 / 5)

### Units that can act as a replacement for Damian

**Best overall replacement**

- Twins (77% `Buffs on allies` `Healing`)
- Lorsan (64% `Buffs on allies` `Healing`)
- Mikola (60% `Healing` `Buffs on allies`)

**Buffs on allies**

- Twins (100% `Haste`)
- Hugin (100% `Haste`)
- Shakir (100% `Haste`)

**Healing**

- Solise (100% `Healing over time` `Healing`)
- Ludovic (100% `Healing over time` `Healing`)
- Mikola (100% `Healing over time` `Healing`)

**Similar Skills**

- Laios (100% `ally-buffer` `ally-healer` `summoner`)
- Koko (80% `ally-buffer` `ally-healer`)
- Isabella (80% `ally-buffer` `ally-healer`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Crowd Control**

- Hepler (100% `Blind` `Stun`)
- Twins (59% `Blind`)

### Summary for Damian

#### Damian Provides

- Summoning — Single target

#### Damage types dealt by Damian

- Magic — Area, Single target

#### Crowd Control provided by Damian

- Blind — Area — `high`
- Stun — Single target — `high`

## Dionel

### Dionel's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S]`

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
Common buffers are **Twins**, **Mikola**, or **Hugin**.

Dionel also requires units **buffing them**

- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
  - Grants 3 distinct stat buffs to Dionel
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
  - Shield (single target, average)
  - Grants 6 distinct stat buffs to Dionel (start of battle)
- **Koko**
  - Shield (all units, low)
  - Grants 5 distinct stat buffs to Dionel
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
  - Grants 4 distinct stat buffs to Dionel
- **Pandora**
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
  - Grants 4 distinct stat buffs to Dionel (start of battle)

### Units benefitting most from Dionel

Dionel provides ATK buff to single targets `average`.

- Kazim (2.0 / 5)
- Bonnie (1.5 / 5)
- Indris (1.4 / 5)

### Units that can act as a replacement for Dionel

**Best overall replacement**

- Frieren (92% `Damage` `Debuffs on enemies` `Crowd Control` `Buffs on allies`)
- Faramor (69% `Damage` `Debuffs on enemies`)
- Nazrik (64% `Damage` `Debuffs on enemies`)

**Buffs on allies**

- Gunnar (100% `ATK`)
- Contess (100% `ATK`)
- Frieren (100% `ATK`)

**Similar Skills**

- Igor (60% `aoe-damage` `self-repositioner` `untargetable`)
- Rhys (60% `aoe-damage` `self-repositioner`)
- Atalanta (60% `aoe-damage` `self-repositioner`)

**Damage**

- Frieren (100% `True damage`)
- Baelran (100% `True damage` `Physical`)
- Himmel (100% `True damage` `Physical`)

**Debuffs on enemies**

- Gunnar (100% `Vitality debuff`)
- Frieren (100% `Vitality debuff`)
- Alna (100% `Vitality debuff`)

**Crowd Control**

- Kulu (100% `Knock up`)
- Florabelle (100% `Knock up`)
- Zandrok (100% `Knock up`)

### Summary for Dionel

#### Dionel Provides

- Stacking buff — Single target
- Execution scaling (Supreme+) — Single target

#### Damage types dealt by Dionel

- Physical — Area, Single target
- True damage — All units, Single target — `average`

#### Debuffs provided by Dionel

- Vitality (Mythic+) — Single target — `low`

#### Crowd Control provided by Dionel

- Untargetable — Area — On skill
- Knock up — Single target — `low`

## Dunlingr

### Dunlingr's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S+]`

- **Signature skill**: Echo of Silence (ultimate)
- **Movement**: moving (melee class)
- **Behavior tags**: `ally-buffer` `aoe-damage` `battle-start-burst` `disabler`
- **Damage types**: Magic `average`, DoT `average`, HP loss `low`, Max HP-based damage `average`

#### Play overview

Before battle, Dunlingr **chooses a field rule** that blocks all healing or all ultimates for both sides. A bell enforces the rule at start, and casting his ultimate **extends the order** for more duration. He gains shields when order conditions are met and can **shield one ally from the rule** while granting allies attack speed or life drain at rule start. Frontal multi-hits add **rule-based bonus effects** on top of damage. Battle damage taken reduction keeps him standing while the order is active. He is oppressive against **heal-reliant or ultimate-reliant teams** but **handicaps his own side** with the same restriction. Enemies that **ignore the order** or burst teams that end fights inside the window waste his setup entirely. Choosing the right rule before battle is essential, since both options hurt allies too.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, first cast speed `fast`, heal `average`, damage `average`
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
Common buffers are **Twins**, **Solise**, or **Hugin**.

- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)
  - Shield (summons only, low)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
  - Direct healing (single target, high)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)

### Units benefitting most from Dunlingr

Dunlingr provides ATK buff (EX+5) to single targets `low`, Haste buff (EX+15) to single targets `average`, ATK SPD buff (Supreme+) to all units `low`, and Lifedrain buff (Supreme+) to all units `average`.

**13** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Brutus (5.0 / 5)
- Satrana (5.0 / 5)
- Bonnie (4.9 / 5)
- Indris (4.8 / 5)
- Kruger (4.3 / 5)
- Igor (3.5 / 5)
- Walker (3.3 / 5)
- Zandrok (2.9 / 5)
- Harak (2.8 / 5)
- Cyran (2.5 / 5)

### Units that can act as a replacement for Dunlingr

**Best overall replacement**

- Sylphira (53% `Crowd Control` `Damage`)

**Similar Skills**

- Perseus (50% `ally-buffer` `aoe-damage`)
- Alna (48% `ally-buffer` `aoe-damage`)
- Himmel (40% `ally-buffer` `aoe-damage`)

**Damage**

- Mehira (100% `DoT` `Magic` `Max HP-based damage` `HP loss`)
- Zorya (100% `Magic` `Max HP-based damage` `HP loss`)
- Athalia (96% `Max HP-based damage` `HP loss`)

**Debuffs on enemies**

- Saida (88% `Energy drain`)
- Lily May (88% `Energy drain`)

**Crowd Control**

- Contess (100% `Silence`)
- Gwyneth (100% `Silence`)
- Sylphira (100% `Silence`)

### Summary for Dunlingr

#### Dunlingr Provides

- Summoning — Single target
- Ultimate lock (Spellbind) — Single target

#### Damage types dealt by Dunlingr

- Magic — Area
- DoT — All units
- HP loss — Single target — `low`
- Max HP-based damage — All units — `low`

#### Debuffs provided by Dunlingr

- Haste — All units — `low`
- Energy drain (Supreme+) — All units — `average`
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

- **Signature skill (ult)**: speed `average`, damage `high`
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
Common buffers are **Hugin**, **Twins**, or **Ravion**.

- **Saida**
  - Shield (multiple targets, high)
- **Galahad**
  - Shield (single target, average)
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Gunnar**
  - Shield (single target, average)
  - ATK SPD buff (single target, low) `signature fuel`
- **Contess**
  - Shield (single target, average)
- **Daimon**
  - Shield (multiple targets, low)

### Units benefitting most from Eironn

Eironn provides Dodge chance buff to single targets `high`.

- Carolina (4.1 / 5)
- Nerion (2.9 / 5)

### Units that can act as a replacement for Eironn

**Similar Skills**

- Cyran (60% `aoe-damage` `battle-start-burst` `enemy-grouping`)
- Mehira (51% `aoe-damage` `enemy-grouping` `mass-cc`)
- Walker (51% `aoe-damage` `battle-start-burst` `mass-cc`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Lorsan (100% `Haste debuff`)
- Carolina (90% `Haste debuff` `Magic DEF debuff`)
- Kafra (88% `Haste debuff`)

**Crowd Control**

- Kordan (96% `Bind`)
- Korin (96% `Bind`)
- Carolina (72% `Bind`)

### Summary for Eironn

#### Damage types dealt by Eironn

- Magic — Arc, Area, Single target

#### Debuffs provided by Eironn

- Haste — Arc — `high`
- Magic DEF — Single target — `average`

#### Crowd Control provided by Eironn

- Bind — Area — `high`
- Displace — Area — `low`

## Evie

### Evie's behavior

`AFK Stages [B]`, `Dream Realm [A+]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Intel Chase (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-healer` `self-repositioner` `stealth`
- **Ally composition**: rearmost ally starts with healing quill; tracks highest damage dealer
- **Damage types**: Magic `average`

#### Play overview

Evie begins **concealed on the enemy side**, gathering intel on nearby foes to reduce their Magic DEF and fuel her ultimate. She sends a quill to **follow an ally for buffs and healing**, and full intel on all enemies **inflicts debuffs** across the line. A completed investigation can **silence her immobilize target** and spawn an extra support quill. Battle healing growth keeps her sustain relevant over long fights. She loses intel when **allies cast ultimates**, slowing her setup considerably. She works best when enemies cluster so she can investigate most of the line quickly. Spread enemy lines or **fast burst** that ends fights before intel completes waste her debuff package entirely. She offers broad utility but lacks a single standout specialty.

#### Skill overview

- **Signature skill (ult)**: speed `average`, first cast speed `fast`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `average`

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

Look for units providing: `ATK` `Healing` `Energy`  
Common buffers are **Solise**, **Ravion**, or **Twins**.

- **Contess**
  - ATK buff (single target, high)
  - Direct healing (single target, high)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Himmel**
  - ATK buff (single target, high)
  - Direct healing (single target, low)
- **Zanie**
  - ATK buff (single target, low)
  - Direct healing (single target, high)
- **Velara**
  - Direct healing (area, low)

### Units benefitting most from Evie

Evie provides ATK buff to multiple targets `high` and Direct healing to single targets `low`.

- Bonnie (3.9 / 5)
- Smokey & Meerky (3.7 / 5)
- Talene (3.7 / 5)

### Units that can act as a replacement for Evie

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Ludovic (100% `Direct healing` `Healing`)

**Similar Skills**

- Contess (48% `ally-healer` `stealth`)
- Rowan (36% `ally-healer`)
- Fay (36% `ally-healer`)

**Damage**

- Frieren (100% `Magic`)
- Galahad (100% `Magic`)
- Saida (100% `Magic`)

**Debuffs on enemies**

- Velara (100% `Magic DEF debuff`)
- Thador (100% `Magic DEF debuff`)
- Shadewing (100% `Magic DEF debuff`)

**Crowd Control**

- Korin (56% `Bind`)
- Eironn (52% `Bind` `Displace`)

### Summary for Evie

#### Evie Provides

- Invincibility — Self

#### Damage types dealt by Evie

- Magic — Single target

#### Debuffs provided by Evie

- Magic DEF — All units — `low`

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
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `high`

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
Common buffers are **Twins**, **Hugin**, or **Solise**.

Faramor also requires units **buffing them**

- **Gunnar**
  - ATK buff (single target, high)
  - Shield (single target, average)
  - Grants 6 distinct stat buffs to Faramor (start of battle)
- **Contess**
  - ATK buff (single target, high)
  - Shield (single target, average)
  - Grants 4 distinct stat buffs to Faramor
- **Saida**
  - Shield (multiple targets, high)
  - Grants 1 distinct stat buff to Faramor
- **Himmel**
  - ATK buff (single target, high)
  - Shield (single target, average)
  - Grants 3 distinct stat buffs to Faramor
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - Shield (single target, average)
  - Grants 2 distinct stat buffs to Faramor

### Units benefitting most from Faramor

- Carolina (2.0 / 5)
- Shadewing (1.9 / 5)
- Nerion (1.6 / 5)

### Units that can act as a replacement for Faramor

**Best overall replacement**

- Nazrik (62% `Debuffs on enemies` `Crowd Control`)
- Frieren (60% `Damage` `Debuffs on enemies`)
- Nara (56% `Damage` `Debuffs on enemies`)

**Similar Skills**

- Perseus (60% `ally-buffer` `aoe-damage`)
- Lorsan (60% `aoe-damage` `dot-specialist`)
- Arden (57% `aoe-damage` `dot-specialist`)

**Damage**

- Athalia (100% `True damage` `Physical` `HP loss`)
- Nara (99% `True damage` `Physical` `HP loss`)
- Vala (83% `True damage` `Physical` `HP loss`)

**Debuffs on enemies**

- Gunnar (100% `Vitality debuff`)
- Frieren (100% `Vitality debuff`)
- Alna (100% `Vitality debuff`)

**Crowd Control**

- Contess (100% `Stun`)
- Aliceth (100% `Stun`)
- Gwyneth (100% `Stun`)

### Summary for Faramor

#### Damage types dealt by Faramor

- Physical — Area, Single target
- DoT — Area
- HP loss — Area — `high`
- True damage — Area, Single target — `high`

#### Debuffs provided by Faramor

- Vitality (Supreme+) — Single target — `low`

#### Crowd Control provided by Faramor

- Stun — Area — `low`

## Fay

### Fay's behavior

`AFK Stages [C]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [C]`

- **Signature skill**: Vibrant Dance (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Behavior tags**: `ally-healer` `aoe-healing`
- **Damage types**: Magic `high`

#### Play overview

Fay heals and buffs **allies within ultimate range**, with steady single-target healing and an AoE burst that damages foes while healing friends. She opens battle by **healing and buffing the ally in front of her tile**, and combat max HP rises over time. Low-HP allies also trigger an **emergency heal** for clutch saves. She is a **reliable early support** when stronger healers are unavailable. Her healing output and buffs are **modest compared to top supports**.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, heal `average`, buffs `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, damage `average`

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

Look for units providing: `ATK` `ATK SPD / Haste` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
- **Marcille**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Direct healing (multiple targets, high)
- **Pandora**
  - Direct healing (single target, average)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Fay

Fay provides ATK SPD buff to multiple targets `low`, ATK buff to multiple targets `low`, Direct healing to arc `high`, and Vitality buff (EX+5) to single targets `low`.

- Lily May (2.2 / 5)
- Silven (2.1 / 5)
- Dionel (2.1 / 5)

### Units that can act as a replacement for Fay

**Best overall replacement**

- Evie (64% `Healing`)
- Ludovic (55% `Healing` `Similar Skills`)
- Smokey & Meerky (55% `Healing` `Similar Skills`)

**Buffs on allies**

- Gunnar (78% `ATK` `ATK SPD` `Vitality buff`)
- Twins (67% `ATK` `Vitality buff`)
- Mikola (67% `ATK` `Vitality buff`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Evie (100% `Direct healing` `Healing`)

**Similar Skills**

- Ludovic (100% `ally-healer` `aoe-healing`)
- Smokey & Meerky (100% `ally-healer` `aoe-healing`)
- Hewynn (100% `ally-healer` `aoe-healing`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

### Summary for Fay

#### Damage types dealt by Fay

- Magic — Area

## Florabelle

### Florabelle's behavior

`AFK Stages [A]`, `Dream Realm [A+]`, `Dream Realm (Endless) [S]`, `PVP [C]`

- **Signature skill**: Pounding Blow (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `aoe-damage` `summoner`
- **Damage types**: Physical `high`, Max HP-based damage `low`

#### Play overview

Florabelle opens with a **battle-start tank summon**, then smashes adjacent tiles on ultimate while buffing ally summons with **haste and life drain**. She can summon a **ranged ally**, and combat ATK rises with multiple summons on the field. Each allied summon gains a **permanent shield on entry**, and large summons gain **control immunity and ATK boost**. She peaks in **summon-heavy compositions** that keep bodies on the board. Against teams that **wipe her critters early**, her scaling and shields never build.

#### Skill overview

- **Signature skill (ult)**: speed `average`, first cast speed `fast`, damage `high`
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
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
- **Mehira**
  - Haste buff (single target, low) `signature fuel`
- **Velara**
  - Haste buff (single target, low) `signature fuel`
- **Kazim**
  - ATK buff (single target, high)
  - Haste buff (multiple targets, average) `signature fuel`

### Units benefitting most from Florabelle

Florabelle provides Haste buff to summons `high`, Lifedrain buff to summons `high`, Shield (Mythic+) to summons `low`, and Summon damage buff (Supreme+) to summons `average`.

- Berial (4.3 / 5)
- Hodgkin (4.3 / 5)
- Kazim (3.8 / 5)
- Damian (3.6 / 5)
- Cecia (3.6 / 5)
- Dunlingr (3.5 / 5)
- Phraesto (3.5 / 5)

### Units that can act as a replacement for Florabelle

**Best overall replacement**

- Perseus (66% `Damage`)
- Pang (66% `Damage`)
- Hodgkin (62% `Damage` `Similar Skills`)

**Similar Skills**

- Hodgkin (66% `aoe-damage` `summoner`)
- Tilaya (60% `aoe-damage`)
- Marcille (40% `aoe-damage` `summoner`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Crowd Control**

- Lucca (100% `Knock up`)
- Ulmus (80% `Knock up`)
- Zandrok (66% `Knock up`)

### Summary for Florabelle

#### Florabelle Provides

- Summoning — Single target

#### Damage types dealt by Florabelle

- Physical — Area, Single target
- Max HP-based damage — Single target — `low`

#### Crowd Control provided by Florabelle

- Immune (Supreme+) — Self — Form
- Knock up — Area — `low`

## Frieren

### Frieren's behavior

`AFK Stages [S]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S+]`, `PVP [S]`

- **Signature skill**: Zoltraak (ultimate)
- **Movement**: stationary (avg attack range 7.0 tiles)
- **Behavior tags**: `aoe-damage` `dot-specialist` `high-damage-ult` `self-repositioner`
- **Ally composition**: frontmost ally shares damage reduction with this hero
- **Damage types**: Magic `high`, DoT `high`, Max HP-based damage `high`, True damage `high`

#### Play overview

Frieren begins **concealed and low-priority**, then needs about 15 seconds to **amplify her magic**. With **Himmel adjacent**, she skips the wait and gains a permanent ATK bonus from his stats. After ramping, her damage jumps from enhanced normal attacks and a **vitality-reducing burn**. Her rectangle ultimate adds **split true damage**. She shines in **long fights**, with damage reduction for herself and the frontmost ally buying time to cast. **Burst before amplification** shuts her down early, and **short fights** never develop her burn or ultimate.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `high`

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
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Kazim**
  - ATK buff (single target, high)
  - Haste buff (multiple targets, average) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, low)
  - Haste buff (single target, average) `signature fuel`
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
- **Tasi**
  - Haste buff (single target, high) `signature fuel`
- **Vala**
  - Haste buff (single target, high) `signature fuel`

### Units benefitting most from Frieren

Frieren provides ATK buff to single targets `high`.

- Bonnie (3.9 / 5)
- Shadewing (3.3 / 5)
- Himmel (2.0 / 5)

### Units that can act as a replacement for Frieren

**Best overall replacement**

- Himmel (57% `Damage` `Crowd Control` `Buffs on allies`)

**Buffs on allies**

- Contess (100% `ATK`)
- Ravion (100% `ATK`)
- Gunnar (88% `ATK`)

**Similar Skills**

- Himmel (48% `aoe-damage` `self-repositioner`)
- Dionel (48% `aoe-damage` `self-repositioner`)
- Faramor (40% `aoe-damage` `dot-specialist`)

**Damage**

- Himmel (79% `True damage` `Max HP-based damage`)
- Athalia (79% `True damage` `Max HP-based damage`)
- Sylphira (78% `Magic` `Max HP-based damage` `True damage`)

**Crowd Control**

- Baelran (85% `Knock down` `Knock up`)
- Callan (71% `Knock down` `Stun`)
- Zorya (71% `Knock down` `Stun`)

### Summary for Frieren

#### Damage types dealt by Frieren

- Magic — Area, Single target
- DoT — All units, Area
- Max HP-based damage — Area — `high`
- True damage — All units — `high`

#### Debuffs provided by Frieren

- DoT — Area — `average`
- Vitality — Single target — `low`

#### Crowd Control provided by Frieren

- Stun — Single target — `low`
- Knock down (Supreme+) — Single target — `average`
- Knock up (Supreme+) — Single target — `low`

## Galahad

### Galahad's behavior

`AFK Stages [S]`, `Dream Realm [A+]`, `Dream Realm (Endless) [S+]`, `PVP [A+]`

- **Signature skill**: Time Recast (Mythic+)
- **Movement**: stationary (avg attack range 10.0 tiles)
- **Behavior tags**: `ally-shielder` `aoe-damage` `clone`
- **Ally composition**: nearest ally auto-selected at battle start; prioritizes ally behind
- **Damage types**: Magic `high`, Max HP-based damage `high`

#### Play overview

Galahad needs her **circular zone to fill** with energy before clones and enhanced casts come online, so early timing matters. Her ultimate immobilizes the **top cumulative damage dealer** with HP-loss tied to healing received, then lashes a wider area. Weakest allies gain **exploding shields** that detonate for area damage on expiry. Once the zone completes, a **shadow duplicate** of an ally fights beside her while battle ATK climbs. External buffs grant **sustained energy and steadfast** status to keep the zone growing. She excels in **long attrition fights** where energy-fed clones stack pressure. **Early burst** that kills her before the zone matures, or teams that cannot protect the circle while it charges, blunt her payoff.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`
- **Ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `average`

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
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Velara**
  - Haste buff (single target, low) `signature fuel`
- **Kazim**
  - ATK buff (single target, high)
  - Haste buff (multiple targets, average) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, low)
  - Haste buff (single target, average) `signature fuel`
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
- **Tasi**
  - Haste buff (single target, high) `signature fuel`

### Units benefitting most from Galahad

Galahad provides Haste buff to single targets `average` and Shield to single targets `average`.

- Eironn (2.3 / 5)
- Velara (2.3 / 5)
- Gwyneth (1.8 / 5)
- Hugin (1.7 / 5)
- Zanie (1.6 / 5)
- Aurora (1.6 / 5)
- Florabelle (1.6 / 5)
- Ravion (1.5 / 5)

### Units that can act as a replacement for Galahad

**Best overall replacement**

- Saida (77% `Damage` `Crowd Control` `Buffs on allies`)
- Alna (51% `Damage` `Crowd Control`)

**Buffs on allies**

- Hugin (100% `Shield` `Haste`)
- Saida (100% `Shield`)
- Hepler (100% `Shield` `Haste`)

**Similar Skills**

- Phraesto (50% `ally-shielder` `aoe-damage` `clone`)
- Scarlita (50% `ally-shielder` `aoe-damage`)
- Gunnar (40% `ally-shielder` `aoe-damage`)

**Damage**

- Saida (100% `Magic` `Max HP-based damage`)
- Cryonaia (100% `Magic` `Max HP-based damage`)
- Marcille (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Zorya (64% `Movement speed debuff` `Haste debuff`)

**Crowd Control**

- Saida (100% `Bind`)
- Velara (100% `Bind`)
- Alna (100% `Bind`)

### Summary for Galahad

#### Galahad Provides

- Artifact buff (EX+10) — Single target

#### Damage types dealt by Galahad

- Magic — All units, Area, Single target
- Max HP-based damage — All units, Single target — `high`

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
- **Damage types**: Physical `average`

#### Play overview

Gerda opens with a **battle-start leap** that interrupts nearby enemies and drops a **healing zone** where she lands. Her ultimate sleeps foes in range while **healing allies**, turning clustered lines into a stall window. A stun skill adds a personal shield, and battle damage taken reduction keeps her standing through the opener. Enhanced zone healing and **cooldown reduction on zone heals** keep her rotation moving as allies stand inside. At higher tiers the opening leap **stuns instead of interrupting**, tightening control on grouped targets. She is a **strong early tank-healer** when enemies bunch up and can be caught in the zone. **Spread formations** and foes immune to sleep or interrupt waste her leap and zone value entirely.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, heal `average`, damage `high`
- **Ultimate**: speed `average`, heal `average`, damage `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, damage `high`

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
Common buffers are **Twins** or **Hugin**.

- **Hepler**
  - Shield (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)
- **Lucius**
  - Shield (area, average)
- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
- **Koko**
  - Shield (all units, low)

### Units benefitting most from Gerda

Gerda provides Direct healing to multiple targets `high` and Healing over time in an area `average`.

- Lily May (2.0 / 5)
- Silven (2.0 / 5)
- Dionel (1.7 / 5)

### Units that can act as a replacement for Gerda

**Best overall replacement**

- Hepler (57% `Damage` `Healing`)

**Healing**

- Solise (100% `Direct healing` `Healing over time` `Healing`)
- Ludovic (100% `Direct healing` `Healing over time` `Healing`)
- Smokey & Meerky (100% `Direct healing` `Healing`)

**Similar Skills**

- Solise (50% `ally-healer` `ally-shielder` `aoe-healing`)
- Velara (50% `ally-healer` `ally-shielder` `aoe-healing`)
- Hepler (41% `ally-healer` `ally-shielder`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

### Summary for Gerda

#### Damage types dealt by Gerda

- Physical — Area, Multiple targets, Single target

#### Crowd Control provided by Gerda

- Unaffected — Self — On skill
- Bind — Single target — `low`
- Interrupt — Area — `low`
- Sleep — Single target — `low`
- Stun — Single target — `average`

## Granny Dahnie

### Granny Dahnie's behavior

`AFK Stages [C]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Threshold of Jade (ultimate)
- **Movement**: moving (avg attack range 2.0 tiles)
- **Behavior tags**: `hp-scaling` `taunt`
- **Damage types**: Physical `low`, DoT `low`

#### Play overview

Granny Dahnie taunts a foe and **recovers HP**, then retaliates with projectiles when damage thresholds are crossed, slowing attacker haste. Her ultimate immobilizes nearby enemies while **draining HP and energy**, staying unaffected during the channel. Low HP triggers **Phys and Magic DEF boosts** plus recovery, and triggered shots grant instant self-heals. Vitality scales with **ultimate casting** over longer fights. She stalls **melee-heavy lines** that keep feeding her retaliations and taunt cycles. **Burst before her ultimate** lands, or taunt-immune targets, leave her as a slow frontliner with modest team utility.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, heal `average`, debuffs `average`, damage `low`
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

Look for units providing: `Haste` `Healing` `Energy` `Physical DEF` `Magic DEF`  
Common buffers are **Twins**, **Smokey & Meerky**, or **Solise**.

- **Tilaya**
  - DEF buff (area, high)
  - DEF buff (area, high)
- **Lucca**
  - DEF buff (area, average)
  - DEF buff (area, average)
- **Hewynn**
  - Healing over time (all units, high)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
- **Marcille**
  - Haste buff (single target, low) `signature fuel`
  - Direct healing (multiple targets, high)

### Units benefitting most from Granny Dahnie

- Shadewing (2.2 / 5)
- Indris (1.6 / 5)
- Himmel (1.5 / 5)

### Units that can act as a replacement for Granny Dahnie

**Similar Skills**

- Baelran (40% `hp-scaling`)
- Pippa (40% `hp-scaling`)
- Lumont (40% `taunt`)

**Damage**

- Gunnar (100% `Physical` `DoT`)
- Alna (100% `Physical` `DoT`)
- Thador (100% `Physical` `DoT`)

**Debuffs on enemies**

- Vala (88% `Haste debuff` `Energy drain`)
- Dunlingr (84% `Haste debuff` `Energy drain`)
- Velara (80% `Haste debuff`)

**Crowd Control**

- Phraesto (80% `Taunt`)
- Brutus (80% `Taunt`)
- Hepler (80% `Taunt`)

### Summary for Granny Dahnie

#### Damage types dealt by Granny Dahnie

- Physical — Single target
- DoT — Single target

#### Debuffs provided by Granny Dahnie

- Energy drain — Single target — `average`
- Haste — Single target — `average`

#### Crowd Control provided by Granny Dahnie

- Unaffected — Self — On skill
- Bind — Single target — `low`
- Taunt — Single target — `average`

## Gunnar

### Gunnar's behavior

`AFK Stages [S+]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S+]`, `PVP [S+]`

- **Signature skill**: Annihilation Directive (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-shielder` `aoe-damage` `fire-attack` `static-tile-buffer`
- **Ally composition**: place ally 1 tile behind at battle start (Doomfield buffs and coordinated attacks)
- **Damage types**: Physical `high`, DoT `low`, Max HP-based damage `average`

#### Play overview

Gunnar anchors a **rear ally on a passive field** that empowers their range and ATK, then shields everyone behind himself on active cast. Cannon volleys pepper targeted areas, and his **scorched ultimate** deals massive AoE while denying heals and shields inside the burn. Ranged DEF and vitality **scale with allied positioning**, and ally damage thresholds trigger **self-healing missiles** when the line takes pressure. He wants a protected rear partner and enemies walking into sustained fire across multiple casts. **Anti-shield or heal-immune foes** shrug off his zone denial entirely. Without **clustered enemies** in cannon and burn range, his damage and suppression stay modest for the slot.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `average`
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

Look for units providing: `ATK SPD / Haste` `Shield` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Solise**.

- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
- **Hewynn**
  - Healing over time (all units, high)
- **Koko**
  - Shield (all units, low)
  - Direct healing (all units, average)
- **Marcille**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Direct healing (multiple targets, high)
- **Lorsan**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
  - Direct healing (all units, low)

### Units benefitting most from Gunnar

Gunnar provides ATK SPD buff to single targets `low`, ATK buff to single targets `high`, Attack range buff to single targets `high`, Shield to single targets `average`, Ranged DEF buff (Legendary+) to single targets `low`, and Vitality buff (Legendary+) to single targets `low`.

- Shadewing (3.0 / 5)
- Faramor (2.9 / 5)
- Silven (2.7 / 5)
- Perseus (2.6 / 5)
- Eironn (2.0 / 5)
- Kulu (2.0 / 5)
- Zanie (2.0 / 5)
- Cyran (1.9 / 5)
- Velara (1.6 / 5)
- Twins (1.2 / 5)

### Units that can act as a replacement for Gunnar

**Best overall replacement**

- Perseus (53% `Crowd Control` `Damage`)
- Contess (50% `Crowd Control` `Buffs on allies`)

**Buffs on allies**

- Contess (82% `Shield` `ATK`)
- Hugin (54% `Shield` `ATK`)

**Similar Skills**

- Galahad (40% `ally-shielder` `aoe-damage`)
- Hugin (40% `ally-shielder` `static-tile-buffer`)
- Florabelle (20% `aoe-damage`)

**Damage**

- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)
- Saida (100% `Max HP-based damage` `DoT`)

**Crowd Control**

- Contess (100% `Stun`)
- Frieren (100% `Stun`)
- Aliceth (100% `Stun`)

### Summary for Gunnar

#### Gunnar Provides

- Invincibility (EX+15) — Single target

#### Damage types dealt by Gunnar

- Physical — All units, Area, Single target
- DoT — Single target
- Max HP-based damage — Area, Single target — `average`

#### Debuffs provided by Gunnar

- Vitality — Single target — `low`
- Healing (Supreme+) — Area — `low`

#### Crowd Control provided by Gunnar

- Stun — Single target — `low`

## Gwyneth

### Gwyneth's behavior

`AFK Stages [A]`, `Dream Realm [S+]`, `Dream Realm (Endless) [?]`, `PVP [B]`

- **Signature skill**: Hailing Arrows (ultimate)
- **Movement**: stationary (avg attack range 8.0 tiles)
- **Behavior tags**: `dot-specialist` `fire-attack` `mass-cc`
- **Damage types**: Physical `high`, DoT `high`, Max HP-based damage `average`

#### Play overview

Gwyneth alternates **splash CC arrows** and **high-damage burn shots**, then fires both at once so every effect lands together on priority targets. Her ultimate rains arrows across range, and **empty nearby tiles** raise her attack speed while also tightening normal attack intervals when foes cannot close. Burn DoT and control stack on targets over time rather than in one burst, rewarding safe spacing throughout the fight. She peaks when **enemies cannot reach her** and she keeps casting from a protected rear tile without interruption. **Melee rush** or cleanse-heavy lines shut down her burn and CC chain before damage ramps meaningfully. Her kit relies on **sustained casting rhythm**, not a single opening burst window. Against **spread formations** her splash and rain cover too little area to justify the slot. She needs safe rear spacing to cycle both arrow types.

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `average`
- **Non-ultimate**: speed `fast`, debuffs `average`, damage `high`

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

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Twins**, **Hugin**, or **Ravion**.

- **Galahad**
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Velara**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, low) `signature fuel`
- **Thador**
  - Energy recovery (single target, low) `signature fuel`

### Units benefitting most from Gwyneth

- Carolina (2.0 / 5)
- Shadewing (1.9 / 5)
- Nerion (1.6 / 5)

### Units that can act as a replacement for Gwyneth

**Best overall replacement**

- Atalanta (62% `Damage` `Crowd Control` `Debuffs on enemies`)
- Frieren (60% `Damage` `Debuffs on enemies`)
- Mirael (58% `Damage` `Similar Skills`)

**Similar Skills**

- Mirael (96% `dot-specialist` `fire-attack`)
- Arden (60% `dot-specialist` `mass-cc`)
- Natsu (60% `dot-specialist` `fire-attack` `mass-cc`)

**Damage**

- Frieren (100% `DoT` `Max HP-based damage`)
- Perseus (97% `Physical` `Max HP-based damage`)
- Atalanta (97% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Sinbad (100% `Phys DEF debuff` `Vitality debuff`)
- Cecia (100% `Phys DEF debuff` `Vitality debuff`)
- Hodgkin (100% `Phys DEF debuff` `Vitality debuff`)

**Crowd Control**

- Evie (97% `Bind` `Silence`)
- Atalanta (89% `Bind` `Stun`)
- Contess (57% `Silence` `Stun`)

### Summary for Gwyneth

#### Damage types dealt by Gwyneth

- Physical — Area, Single target
- DoT — Single target
- Max HP-based damage — Single target — `average`

#### Debuffs provided by Gwyneth

- Vitality — Single target — `low`
- Phys DEF (Mythic+) — Single target — `low`

#### Crowd Control provided by Gwyneth

- Bind — Single target — `average`
- Silence — Area — `low`
- Stun — Area — `low`

## Hammie

### Hammie's behavior

- **Signature skill**: Pretty Fireball (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Behavior tags**: `ally-buffer` `ally-healer`
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

Look for units providing: `ATK` `Healing`  
Common buffers are **Mikola**, **Twins**, or **Smokey & Meerky**.

- **Hewynn**
  - Healing over time (all units, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Fay**
  - ATK buff (multiple targets, low)
  - Direct healing (arc, average)
  - ATK SPD buff (multiple targets, low) `signature fuel`
- **Hepler**
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Marcille**
  - Direct healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Hammie

Hammie provides ATK buff to multiple targets `high`.

- Bonnie (2.9 / 5)
- Himmel (2.6 / 5)
- Silven (1.7 / 5)

### Units that can act as a replacement for Hammie

**Best overall replacement**

- Evie (94% `Buffs on allies` `Healing`)
- Contess (77% `Buffs on allies` `Healing`)
- Mikola (62% `Healing` `Buffs on allies`)

**Buffs on allies**

- Contess (100% `ATK`)
- Evie (100% `ATK`)
- Pang (100% `ATK`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Evie (100% `Direct healing` `Healing`)
- Fay (100% `Direct healing` `Healing`)

**Similar Skills**

- Isabella (100% `ally-buffer` `ally-healer`)
- Koko (100% `ally-buffer` `ally-healer`)
- Damian (80% `ally-buffer` `ally-healer`)

**Damage**

- Alsa (100% `Magic`)
- Aurora (100% `Magic`)
- Berial (100% `Magic`)

### Summary for Hammie

#### Damage types dealt by Hammie

- Magic — Single target

## Harak

### Harak's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [A+]`, `PVP [B]`

- **Signature skill**: Flesh Feast (Skill 2)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `assassin` `execute` `life-drain`
- **Damage types**: Physical `low`, HP loss `low`

#### Play overview

Harak enters an **enhanced battle-start state** that extends with assists and defeats, then devours a non-summoned unit when the state ends. He dashes to the **weakest enemy**, knocks them up, and his ultimate blocks **target HP recovery** with sustained multi-strikes. Life drain and **ATK plus max HP** grow with each takedown across the fight. Enough assists or defeats also **refund ultimate energy** for another execute window. He snowballs hardest in **chaotic multi-kill fights** where bodies feed his ramp and devour timing. **Single-target stalls** or teams that deny assists keep him from growing or force bad devour targets on allies.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`
- **Ultimate**: speed `slow`, debuffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `low`

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

Look for units providing: `Haste` `Max HP` `CRIT` `Healing` `Energy`  
Common buffers are **Twins**, **Smokey & Meerky**, or **Solise**.

- **Koko**
  - Direct healing (all units, average)
  - Lifedrain buff (multiple targets, average)
- **Dunlingr**
  - Haste buff (single target, average) `signature fuel`
  - Lifedrain buff (all units, average)
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, average)
  - Lifedrain buff (area, low, conditional (frequent))
- **Marcille**
  - Haste buff (single target, low) `signature fuel`
  - Direct healing (multiple targets, high)
- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - Lifedrain buff (single target, low)

### Units benefitting most from Harak

Harak provides Crit buff to single targets `low` and Lifedrain buff (Legendary+) to single targets `low`.

- Nazrik (5.0 / 5)

### Units that can act as a replacement for Harak

**Best overall replacement**

- Nara (78% `Damage` `Crowd Control` `Similar Skills`)
- Seth (77% `Damage` `Similar Skills`)
- Athalia (72% `Damage` `Crowd Control`)

**Buffs on allies**

- Rhys (92% `Crit`)
- Walker (61% `Crit`)

**Similar Skills**

- Seth (80% `assassin` `life-drain`)
- Salazer (60% `execute` `life-drain`)
- Nara (50% `assassin` `execute`)

**Damage**

- Mehira (100% `Max HP-based damage` `HP loss`)
- Aliceth (100% `Physical` `Max HP-based damage` `HP loss`)
- Faramor (100% `Physical` `HP loss`)

**Debuffs on enemies**

- Gunnar (60% `Healing debuff`)
- Aliceth (60% `Execution debuff`)
- Nazrik (60% `Healing debuff`)

**Crowd Control**

- Frieren (100% `Knock down`)
- Baelran (100% `Knock down`)
- Himmel (100% `Knock down`)

### Summary for Harak

#### Harak Provides

- Instant defeat — Single target
- Invincibility — Self

#### Damage types dealt by Harak

- Physical — Single target
- HP loss — Single target — `low`

#### Debuffs provided by Harak

- Execution — Single target — `low`
- Healing — Single target — `low`

#### Crowd Control provided by Harak

- Unaffected — Self — On skill
- Knock down — Single target — `low`

## Hepler

### Hepler's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Form Shift (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-healer` `ally-shielder` `transformation`
- **Ally composition**: frontmost adjacent ally gets fatal-blow protection
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Play overview

Hepler toggles between **true-form offense** and an alternate **taunt form** that heals and shields multiple allies. His ultimate consumes taunt stacks for **AoE damage and blind** on revert. Charge spending **permanently stacks DEF** and damage reduction over the fight. He can **block a fatal blow** on the frontmost ally by transforming to safety. Alternate form also carries **higher damage taken reduction** than his human stance. **Fast burst** that skips his charge cycle leaves little defensive value.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `high`

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
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Tilaya**
  - Max HP buff (area, average)
  - DEF buff (area, high)
  - DEF buff (area, high)
- **Sonja**
  - ATK buff (multiple targets, average)
  - DEF buff (multiple targets, low)
  - DEF buff (multiple targets, low)
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, average)
- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
- **Alna**
  - ATK buff (single target, low)
  - Max HP buff (single target, high)

### Units benefitting most from Hepler

Hepler provides Haste buff to single targets `low`, Healing over time to multiple targets `high`, and Shield to multiple targets `average`.

**13** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Lucius (4.9 / 5)
- Salazer (4.4 / 5)
- Ulmus (4.4 / 5)
- Gunnar (4.4 / 5)
- Carolina (4.3 / 5)
- Antandra (3.9 / 5)
- Temesia (3.5 / 5)
- Lumont (3.5 / 5)
- Lucca (3.2 / 5)
- Kafra (2.9 / 5)

### Units that can act as a replacement for Hepler

**Buffs on allies**

- Hugin (100% `Shield` `Haste`)
- Saida (99% `Shield`)
- Salazer (93% `Shield`)

**Healing**

- Hewynn (100% `Healing over time` `Healing`)
- Smokey & Meerky (78% `Healing`)
- Solise (70% `Healing over time` `Healing`)

**Similar Skills**

- Pang (66% `ally-shielder` `transformation`)
- Solise (50% `ally-healer` `ally-shielder`)
- Velara (50% `ally-healer` `ally-shielder`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Galahad (100% `Haste debuff`)
- Velara (100% `Haste debuff`)
- Alna (100% `Haste debuff`)

**Crowd Control**

- Lumont (57% `Taunt` `Stun`)

### Summary for Hepler

#### Hepler Provides

- Invincibility (Mythic+) — Single target

#### Damage types dealt by Hepler

- Physical — Area, Single target
- Max HP-based damage — Area, Single target — `high`

#### Debuffs provided by Hepler

- Haste — Single target — `average`

#### Crowd Control provided by Hepler

- Blind — Area — `high`
- Stun — Area — `average`
- Taunt — Area — `high`

## Hewynn

### Hewynn's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Rain Prayer (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-healer` `aoe-healing`
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
Common buffers are **Twins**, **Mikola**, or **Ravion**.

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Pandora**
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Hewynn

Hewynn provides Direct healing to single targets `average`, Healing over time to all units `high`, and Damage taken (Mythic+) to multiple targets `low`.

- Hodgkin (3.9 / 5)
- Salazer (3.9 / 5)
- Gunnar (3.6 / 5)
- Granny Dahnie (3.5 / 5)
- Hammie (3.5 / 5)

### Units that can act as a replacement for Hewynn

**Best overall replacement**

- Koko (50% `Buffs on allies`)

**Buffs on allies**

- Koko (100% `Damage taken reduction`)
- Shakir (100% `Damage taken reduction`)
- Hugin (60% `Damage taken reduction`)

**Healing**

- Solise (100% `Direct healing` `Healing over time` `Healing`)
- Smokey & Meerky (77% `Direct healing` `Healing`)
- Hepler (67% `Healing over time` `Healing`)

**Similar Skills**

- Ludovic (100% `ally-healer` `aoe-healing`)
- Smokey & Meerky (100% `ally-healer` `aoe-healing`)
- Fay (100% `ally-healer` `aoe-healing`)

### Summary for Hewynn

#### Crowd Control provided by Hewynn

- Unaffected (Mythic+) — Self — On skill

## Himmel

### Himmel's behavior

`AFK Stages [S]`, `Dream Realm [S+]`, `Dream Realm (Endless) [A+]`, `PVP [A+]`

- **Signature skill**: Hero Party (Skill 2)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-buffer` `aoe-damage` `self-repositioner`
- **Ally composition**: place Mage, Tank, and Support within 1 tile at battle start (Hero Party)
- **Damage types**: Physical `high`, Max HP-based damage `high`, True damage `high`

#### Play overview

Himmel opens with a **battle-start formation** beside allies, granting petals that bless everyone on the field with sustained bonuses. He dashes to two high-damage foes, knocks them down, then slashes in a **repeated frontal ultimate** with a massive finishing sweep across the line. Formation strikes add **extra HP-loss on boss targets**, and battle haste keeps his rotation brisk through long fights. He pairs strongly with **Frieren adjacent** so she skips her ramp wait and shares ATK from his stats for the whole fight. He offers **soft buffs and line pressure**, not standalone carry damage or hard mitigation. **Spread lines** or burst that ends before formation and petal value builds waste his setup entirely. Without **adjacent allies** in formation, his petals and HP-loss bonuses contribute far less to the team.

#### Skill overview

- **Signature skill**: speed `slow`, first cast speed `fast`, heal `average`, buffs `average`, damage `average`
- **Ultimate**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, damage `high`

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

Look for units providing: `ATK` `Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Solise**, or **Mikola**.

Himmel also requires a party **with the right composition**

- **Contess**
  - ATK buff (single target, high)
  - Direct healing (single target, high)
  - Enables Party composition via Support (party slot)
- **Velara**
  - Haste buff (single target, low) `signature fuel`
  - Direct healing (area, low)
  - Enables Party composition via Support (party slot)
- **Frieren**
  - ATK buff (single target, high)
  - Enables Party composition via Mage (party slot)
- **Gunnar**
  - ATK buff (single target, high)
  - Enables Party composition via Tank (party slot)
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - Enables Party composition via Mage (party slot)

### Units benefitting most from Himmel

Himmel provides ATK buff to single targets `high` and Shield to single targets `low`.

- Baelran (2.4 / 5)
- Aliceth (2.0 / 5)
- Velara (1.6 / 5)
- Saida (1.4 / 5)

### Units that can act as a replacement for Himmel

**Best overall replacement**

- Contess (83% `Buffs on allies` `Healing` `Debuffs on enemies`)
- Mikola (72% `Healing` `Buffs on allies`)
- Evie (59% `Healing` `Buffs on allies`)

**Buffs on allies**

- Gunnar (100% `ATK` `Shield`)
- Contess (100% `ATK` `Shield`)
- Hugin (100% `Shield` `ATK`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Twins (100% `Direct healing` `Healing`)

**Similar Skills**

- Perseus (66% `ally-buffer` `aoe-damage`)
- Kordan (50% `ally-buffer` `self-repositioner`)
- Dionel (50% `aoe-damage` `self-repositioner`)

**Damage**

- Frieren (100% `True damage` `Max HP-based damage`)
- Baelran (100% `True damage` `Physical` `Max HP-based damage`)
- Athalia (100% `Physical` `True damage` `Max HP-based damage`)

**Debuffs on enemies**

- Contess (100% `Damage taken debuff`)
- Mehira (100% `Damage taken debuff`)
- Kulu (100% `Damage taken debuff`)

**Crowd Control**

- Frieren (100% `Knock down`)
- Baelran (100% `Knock down`)
- Silven (100% `Knock down`)

### Summary for Himmel

#### Damage types dealt by Himmel

- Physical — All units, Area, Multiple targets, Single target
- Max HP-based damage — All units, Multiple targets, Single target — `high`
- True damage — All units — `high`

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

Look for units providing: `ATK` `Healing` `Energy`  
Common buffers are **Solise**, **Smokey & Meerky**, or **Mikola**.

- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)
- **Hewynn**
  - Healing over time (all units, high)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Koko**
  - Direct healing (all units, average)

### Units benefitting most from Hodgkin

- Indris (1.7 / 5)
- Bonnie (1.6 / 5)
- Shadewing (1.4 / 5)

### Units that can act as a replacement for Hodgkin

**Similar Skills**

- Florabelle (66% `aoe-damage` `summoner`)
- Cassadee (60% `aoe-damage` `enemy-debuffer`)
- Cecia (60% `enemy-debuffer` `summoner`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Silvina (100% `Energy drain` `Vitality debuff`)
- Dunlingr (95% `Energy drain` `Vitality debuff`)
- Saida (90% `Energy drain`)

### Summary for Hodgkin

#### Hodgkin Provides

- Summoning (Mythic+) — Single target
- Stacking buff (Supreme+) — Single target

#### Damage types dealt by Hodgkin

- Physical — Arc, Area, Single target
- Max HP-based damage — Arc, Area, Single target — `high`

#### Debuffs provided by Hodgkin

- Energy drain (Mythic+) — Single target — `average`
- Phys DEF (Supreme+) — Single target — `low`
- Vitality (Supreme+) — Single target — `low`

## Hugin

### Hugin's behavior

`AFK Stages [S+]`, `Dream Realm [A+]`, `Dream Realm (Endless) [S]`, `PVP [A]`

- **Signature skill**: Mechanized Bond (Skill 2)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-shielder` `energy-provider` `static-tile-buffer`
- **Self placement**: stays anchored to battle-prep tile; returns after displacement
- **Ally composition**: put one ally 1 tile behind him (ATK bonus; buff ends if they leave the sigil)
- **Damage types**: Physical `low`

#### Play overview

Hugin shields the **weakest ally** with large barriers, then boosts the **highest cumulative damage dealer's ATK and Haste** on ultimate. The ally directly behind gains **ATK**, and recovers energy whenever he shields anyone on the field. Shielded allies also **reduce damage taken**, and his ultimate adds shields to weak targets alongside the buff. He is a **strong buffer for a rear carry** positioned behind him on the board. Value drops when the **rear partner dies** or when no ally clearly leads damage dealt. He adds **little personal damage** if buff targets are misaligned or the top dealer changes mid-fight.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `average`
- **Ultimate**: speed `average`, first cast speed `fast`, buffs `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`

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
Common buffers are **Twins**, **Rowan**, or **Smokey & Meerky**.

- **Galahad**
  - Haste buff (single target, average) `signature fuel`
- **Velara**
  - Haste buff (single target, low) `signature fuel`
- **Kazim**
  - Haste buff (multiple targets, average) `signature fuel`
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
- **Tasi**
  - Haste buff (single target, high) `signature fuel`

### Units benefitting most from Hugin

Hugin provides ATK buff to multiple targets `high`, Haste buff to multiple targets `high`, Shield to multiple targets `high`, and Damage taken (Supreme+) to single targets `low`.

**75** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Faramor (4.2 / 5)
- Alsa (4.1 / 5)
- Koko (4.0 / 5)
- Dionel (4.0 / 5)
- Perseus (3.7 / 5)
- Lenya (3.6 / 5)
- Lily May (3.6 / 5)
- Silven (3.4 / 5)
- Lorsan (3.4 / 5)
- Mikola (3.2 / 5)

### Units that can act as a replacement for Hugin

**Buffs on allies**

- Saida (88% `Shield`)
- Hepler (83% `Shield` `Haste`)

**Similar Skills**

- Thador (50% `ally-shielder` `energy-provider`)
- Ravion (50% `ally-shielder` `energy-provider`)
- Twins (48% `ally-shielder` `energy-provider`)

### Summary for Hugin

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

- **Signature skill (ult)**: speed `fast`, first cast speed `fast`, damage `average`
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

Look for units providing: `Healing` `Life Drain`  
Common buffers are **Solise**, **Smokey & Meerky**, or **Mikola**.

- **Koko**
  - Direct healing (all units, average)
  - Lifedrain buff (multiple targets, average)
- **Dunlingr**
  - Lifedrain buff (all units, average)
- **Hepler**
  - Healing over time (multiple targets, high)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)

### Units benefitting most from Igor

- Shadewing (1.9 / 5)
- Indris (1.3 / 5)
- Bonnie (1.3 / 5)

### Units that can act as a replacement for Igor

**Similar Skills**

- Dionel (60% `aoe-damage` `self-repositioner` `untargetable`)
- Mehira (51% `aoe-damage` `life-drain` `untargetable`)
- Brutus (42% `aoe-damage` `cheat-death` `life-drain`)

**Damage**

- Athalia (100% `Physical` `Max HP-based damage`)
- Kulu (100% `Physical`)
- Kruger (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Gunnar (100% `Healing debuff`)
- Nazrik (100% `Healing debuff`)
- Niru (100% `Healing debuff`)

### Summary for Igor

#### Damage types dealt by Igor

- Physical — All units, Area

#### Debuffs provided by Igor

- Healing (Mythic+) — Single target — `low`

## Indris

### Indris's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Spellbane Shot (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `disabler` `enemy-debuffer`
- **Damage types**: Physical `low`, True damage `average`

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
Common buffers are **Twins**, **Mikola**, or **Ravion**.

Indris also requires units **putting debuffs** on enemies and/or units **putting multiple debuffs** on enemies

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via ATK debuff (all units)
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
  - Enables Multiple debuffs on target via 3 debuff types
  - Enables Debuff on target via Haste debuff (all units)
- **Lorsan**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via Haste debuff (area)
- **Kulu**
  - ATK buff (single target, low)
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via Damage taken debuff (all units)
- **Alna**
  - ATK buff (single target, low)
  - Enables Multiple debuffs on target via 3 debuff types
  - Enables Debuff on target via Haste debuff (all units)

### Units benefitting most from Indris

- Carolina (2.2 / 5)
- Nerion (1.7 / 5)
- Bonnie (1.6 / 5)

### Units that can act as a replacement for Indris

**Best overall replacement**

- Faramor (54% `Damage`)
- Korin (53% `Damage` `Crowd Control`)
- Pippa (51% `Damage` `Crowd Control`)

**Similar Skills**

- Temesia (40% `disabler` `enemy-debuffer`)
- Shadewing (33% `enemy-debuffer`)
- Reinier (33% `disabler`)

**Damage**

- Baelran (100% `Physical` `True damage` `Max HP-based damage`)
- Himmel (100% `Physical` `True damage` `Max HP-based damage`)
- Faramor (100% `Physical` `True damage`)

**Debuffs on enemies**

- Sinbad (80% `Phys DEF debuff` `Magic DEF debuff` `Damage taken debuff`)
- Laios (61% `Phys DEF debuff` `Magic DEF debuff`)
- Kruger (57% `Phys DEF debuff` `Damage taken debuff`)

**Crowd Control**

- Kordan (100% `Bind` `Knock back`)
- Korin (100% `Bind` `Knock back`)
- Arden (93% `Bind`)

### Summary for Indris

#### Damage types dealt by Indris

- Physical — Single target
- True damage — Single target — `average`

#### Debuffs provided by Indris

- Damage taken — Multiple targets — `low`
- Magic DEF — Single target — `average`
- Phys DEF — Single target — `average`

#### Crowd Control provided by Indris

- Bind — Single target — `high`
- Knock back — Area — `low`

## Isabella

### Isabella's behavior

`AFK Stages [C]`, `Dream Realm [B]`, `Dream Realm (Endless) [A+]`, `PVP [C]`

- **Signature skill**: Grimoire Pact (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-buffer` `ally-healer`
- **Ally composition**: frontmost ally becomes companion (stat stacks and ult buffs)
- **Damage types**: Magic `low`

#### Play overview

Isabella bonds the **frontmost ally as companion**, buffing them heavily whenever she casts ultimate on that partner. She heals the companion while **damaging adjacent foes**, and makes them **unaffected after control** when they take a disabling hit. Companion damage taken **cuts attacker ATK**, and large buffs add **extra debuff stacks** on enemies during ultimate. Battle assistance stat growth rewards long support play beside a durable frontliner. She needs a **tanky front partner** to justify the bond and survive her setup phase. If the companion **dies early**, her healing and buff package collapses quickly. Her ultimate also debuffs an enemy hero on cast when buff stacks are large enough to add soft control.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, first cast speed `fast`, buffs `average`
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

Look for units providing: `ATK` `ATK SPD / Haste` `Healing` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Smokey & Meerky**.

- **Tilaya**
  - DEF buff (area, high)
  - DEF buff (area, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Sonja**
  - ATK buff (multiple targets, average)
  - DEF buff (multiple targets, low)
  - DEF buff (multiple targets, low)
- **Marcille**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Direct healing (multiple targets, high)
- **Koko**
  - Direct healing (all units, average)

### Units benefitting most from Isabella

Isabella provides ATK buff to single targets `low` — conditional (frequent) and DEF buff to single targets `low`.

- Bonnie (2.1 / 5)
- Himmel (1.7 / 5)
- Silven (1.3 / 5)

### Units that can act as a replacement for Isabella

**Buffs on allies**

- Twins (100% `Magic DEF` `Physical DEF` `ATK`)
- Sonja (100% `Magic DEF` `Physical DEF` `ATK`)
- Contess (58% `ATK`)

**Similar Skills**

- Koko (100% `ally-buffer` `ally-healer`)
- Damian (80% `ally-buffer` `ally-healer`)
- Laios (66% `ally-buffer` `ally-healer`)

**Debuffs on enemies**

- Ravion (100% `ATK debuff`)
- Bonnie (100% `ATK debuff`)
- Zanie (100% `ATK debuff`)

### Summary for Isabella

#### Damage types dealt by Isabella

- Magic — Area, Single target

#### Debuffs provided by Isabella

- ATK — Single target — `low`

#### Crowd Control provided by Isabella

- Unaffected — Single target — On skill

## Kafra

### Kafra's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Gale Thrust (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `assassin` `enemy-debuffer` `mark-target` `self-repositioner`
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Play overview

Kafra marks an enemy, then **charges out-of-range targets** to stun them on approach for a reliable pick. Marks **shave Phys DEF**, and defeating a marked foe grants **self buffs** that keep his momentum going through the fight. His ultimate knocks back and reapplies the mark, while he **interrupts heals** on anyone treating the marked target. First battle charge greatly **boosts damage** for an opening assassination window against backliners. He excels at **hunting marked targets** in melee-heavy teams that can follow his picks. **Immune or heavily shielded marks** waste his charge, and spread lines deny follow-up kills on secondary targets. In melee-oriented teams with frequent picks, his mark-and-charge loop sustains pressure and can match support healing when marked foes die near grouped allies.

#### Skill overview

- **Signature skill (ult)**: speed `average`, debuffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`

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
Common buffers are **Hugin**, **Mikola**, or **Twins**.

- **Hepler**
  - Shield (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Saida**
  - Shield (multiple targets, high)
- **Gunnar**
  - ATK buff (single target, high)
  - Shield (single target, average)
  - ATK SPD buff (single target, low) `signature fuel`
- **Lucius**
  - Shield (area, average)
- **Contess**
  - ATK buff (single target, high)
  - Shield (single target, average)

### Units benefitting most from Kafra

- Shadewing (2.4 / 5)
- Indris (1.9 / 5)
- Bonnie (1.9 / 5)

### Units that can act as a replacement for Kafra

**Best overall replacement**

- Lenya (52% `Crowd Control` `Damage`)

**Similar Skills**

- Sinbad (90% `assassin` `enemy-debuffer` `mark-target`)
- Lenya (48% `assassin` `self-repositioner`)
- Temesia (34% `enemy-debuffer` `self-repositioner`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Eironn (97% `Haste debuff`)
- Lorsan (97% `Haste debuff`)
- Bonnie (81% `Haste debuff`)

**Crowd Control**

- Perseus (100% `Stun` `Knock back`)
- Scarlita (100% `Stun` `Knock back`)
- Cassadee (100% `Stun` `Knock back`)

### Summary for Kafra

#### Kafra Provides

- Marked target (focus fire) — Single target

#### Damage types dealt by Kafra

- Physical — Single target
- Max HP-based damage — Single target — `average`

#### Debuffs provided by Kafra

- Marked target (focus fire) — Single target — `average`
- Phys DEF — Single target — `average`
- Haste (Mythic+) — Single target — `average`

#### Crowd Control provided by Kafra

- Unaffected (Mythic+) — Self — On skill
- Knock back — Single target — `low`
- Stun — Single target — `average`

## Kazim

### Kazim's behavior

- **Signature skill**: Soaring Falcon (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-buffer` `aoe-damage` `battle-start-burst` `invincibility` `mark-target` `mass-cc`
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Play overview

Kazim opens **invincible in Soaring**, diving at airborne enemies to **mark prey** and stunning them after he lands. His ultimate chains **arc knock-ups** into sustained volleys that scale with attack speed. Marked prey takes **bonus normal-attack damage** and periodic max-HP true damage with knock-up. Allies in his zone gain **haste stacks from prey marks**, which he can absorb doubled after his aerial phase. He shines when **enemies can be kept airborne or marked** for follow-up focus. Fights with **grounded, spread, or knock-up-immune targets** deny his mark loop and aerial payoff.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `average`
- **Ultimate**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `high`

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
Common buffers are **Twins**, **Hugin**, or **Damian**.

Kazim also requires units **providing knock up**

- **Florabelle**
  - Enables Knock up from allies via Knock up + wide area (area)
- **Nerion**
  - Enables Knock up from allies via Knock up + wide area (area)
- **Ulmus**
  - Enables Knock up from allies via Knock up + wide area (area)
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Enables Knock up from allies via Knock up (area)
- **Lucca**
  - Enables Knock up from allies via Knock up (area)

### Units benefitting most from Kazim

Kazim provides Haste buff to multiple targets `high` and ATK buff (Mythic+) to single targets `high`.

- Frieren (3.0 / 5)

### Units that can act as a replacement for Kazim

**Buffs on allies**

- Evie (89% `ATK`)
- Ravion (85% `ATK`)
- Pang (83% `ATK`)

**Similar Skills**

- Walker (68% `aoe-damage` `battle-start-burst` `mark-target` `mass-cc`)
- Parisa (60% `ally-buffer` `aoe-damage` `mark-target`)
- Eironn (45% `aoe-damage` `battle-start-burst` `mass-cc`)

**Damage**

- Kordan (100% `Physical` `Max HP-based damage`)
- Kruger (100% `Physical` `Max HP-based damage`)
- Nara (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Aliceth (100% `Marked target (focus fire)`)
- Kafra (100% `Marked target (focus fire)`)
- Vala (100% `Marked target (focus fire)`)

**Crowd Control**

- Lucca (100% `Stun` `Knock up`)
- Scarlita (100% `Stun` `Knock up`)
- Zandrok (100% `Stun` `Knock up`)

### Summary for Kazim

#### Kazim Provides

- Invincibility — Self
- Stacking buff — Multiple targets

#### Damage types dealt by Kazim

- Physical — Area, Single target
- Max HP-based damage — Area, Single target — `high`

#### Debuffs provided by Kazim

- Marked target (focus fire) — Single target — `average`

#### Crowd Control provided by Kazim

- Knock up — Area — `low`
- Stun — Single target — `average`

## Koko

### Koko's behavior

`AFK Stages [A]`, `Dream Realm [B]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Full Energy (ultimate)
- **Movement**: mostly stationary (avg attack range 4.0 tiles)
- **Behavior tags**: `ally-buffer` `ally-healer`
- **Damage types**: Physical `low`

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

Look for units providing: `Haste` `Shield` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - Shield (single target, average)
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Saida**
  - Shield (multiple targets, high)
- **Pandora**
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Dunlingr**
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Koko

Koko provides Damage taken to all units `low`, Direct healing to all units `high`, Lifedrain buff to multiple targets `average`, Shield (Mythic+) to all units `low`, and Vitality buff (Supreme+) to single targets `low`.

**20** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Igor (5.0 / 5)
- Salazer (5.0 / 5)
- Ulmus (5.0 / 5)
- Callan (4.3 / 5)
- Talene (4.2 / 5)
- Zandrok (3.4 / 5)
- Antandra (3.3 / 5)
- Harak (3.2 / 5)
- Lily May (3.1 / 5)
- Perseus (2.6 / 5)

### Units that can act as a replacement for Koko

**Best overall replacement**

- Contess (72% `Healing` `Buffs on allies` `Debuffs on enemies`)
- Hepler (65% `Healing` `Buffs on allies` `Crowd Control`)
- Smokey & Meerky (51% `Healing`)

**Buffs on allies**

- Salazer (70% `Shield` `Life Drain`)
- Hugin (69% `Shield` `Damage taken reduction`)
- Soren (69% `Shield` `Damage taken reduction`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Evie (100% `Direct healing` `Healing`)

**Similar Skills**

- Isabella (100% `ally-buffer` `ally-healer`)
- Damian (80% `ally-buffer` `ally-healer`)
- Laios (66% `ally-buffer` `ally-healer`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Contess (100% `Damage taken debuff`)
- Himmel (100% `Damage taken debuff`)
- Mehira (100% `Damage taken debuff`)

**Crowd Control**

- Perseus (100% `Stun`)
- Scarlita (100% `Stun`)
- Hepler (100% `Stun`)

### Summary for Koko

#### Damage types dealt by Koko

- Physical — Area, Single target

#### Debuffs provided by Koko

- Damage taken — Single target — `low`

#### Crowd Control provided by Koko

- Stun — Area — `average`

## Kordan

### Kordan's behavior

`AFK Stages [A]`, `Dream Realm [A]`, `Dream Realm (Endless) [S]`, `PVP [B]`

- **Signature skill**: Dominance Ring (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-buffer` `hp-scaling` `self-repositioner`
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Play overview

Kordan drops a **hunting zone** that cuts damage taken and outside healing while allies inside gain **ATK and life drain**. His slash grants a **proportional self-shield**, and knockdown strikes add direct pressure on isolated targets. First takedown inside the circle **permanently enhances skills**, and further kills **reposition the zone** to chase new prey across the field. He wants **melee allies** fighting inside his ring for the full buff package. His circle denies outside healing to enemies beyond the ring when the zone stays active. **Enemies that never enter the zone** or burst that ends before enhancements trigger waste his setup entirely. Ranged foes outside the circle avoid his damage reduction and healing denial. He needs committed melee allies inside the ring for the full payoff.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, buffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `high`

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

Look for units providing: `ATK` `Shield` `Healing` `DEF Penetration` `Physical DEF`  
Common buffers are **Twins**, **Hugin**, or **Ravion**.

- **Aliceth**
  - ATK buff (multiple targets, low)
  - DEF Penetration buff (multiple targets, high)
- **Contess**
  - ATK buff (single target, high)
  - Shield (single target, average)
  - Direct healing (single target, high)
- **Zanie**
  - ATK buff (single target, low)
  - Shield (single target, average)
  - Direct healing (single target, high)
  - DEF Penetration buff (single target, average)
- **Himmel**
  - ATK buff (single target, high)
  - Shield (single target, average)
  - Direct healing (single target, low)
- **Saida**
  - Shield (multiple targets, high)

### Units benefitting most from Kordan

Kordan provides ATK buff to multiple targets `high`, Lifedrain buff to multiple targets `average`, and DEF Penetration buff (Supreme+) to multiple targets `low`.

- Carolina (4.1 / 5)
- Nerion (2.9 / 5)
- Brutus (2.2 / 5)

### Units that can act as a replacement for Kordan

**Similar Skills**

- Marilee (66% `hp-scaling` `self-repositioner`)
- Himmel (50% `ally-buffer` `self-repositioner`)
- Athalia (50% `hp-scaling` `self-repositioner`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Crowd Control**

- Korin (92% `Bind` `Knock back`)
- Eironn (73% `Bind`)
- Carolina (55% `Bind`)

### Summary for Kordan

#### Damage types dealt by Kordan

- Physical — Area, Single target
- Max HP-based damage — Single target — `average`

#### Crowd Control provided by Kordan

- Bind — Area — `high`
- Knock back — Area — `low`
- Knock down — Single target — `low`
- Knock up (Mythic+) — Single target — `low`

## Korin

### Korin's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Demonseal Spear (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-shielder` `hp-scaling`
- **Damage types**: Physical `low`, True damage `average`

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
Common buffers are **Twins**, **Hugin**, or **Damian**.

- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, average)
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, average) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (all units, low) `signature fuel`
- **Lorsan**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Korin

Korin provides Shield to single targets `average`.

- Carolina (3.1 / 5)
- Nerion (2.5 / 5)
- Dionel (1.3 / 5)

### Units that can act as a replacement for Korin

**Best overall replacement**

- Scarlita (53% `Similar Skills` `Buffs on allies`)

**Buffs on allies**

- Gunnar (100% `Shield`)
- Contess (100% `Shield`)
- Galahad (100% `Shield`)

**Similar Skills**

- Scarlita (80% `ally-shielder` `hp-scaling`)
- Daimon (66% `ally-shielder` `hp-scaling`)
- Silven (40% `hp-scaling`)

**Damage**

- Baelran (100% `True damage` `Physical` `Max HP-based damage`)
- Himmel (100% `True damage` `Physical` `Max HP-based damage`)
- Faramor (100% `True damage` `Physical`)

**Crowd Control**

- Kordan (100% `Bind` `Knock back`)
- Eironn (96% `Bind`)
- Evie (72% `Bind`)

### Summary for Korin

#### Damage types dealt by Korin

- Physical — Area
- True damage — Single target — `high`

#### Crowd Control provided by Korin

- Bind — Area — `average`
- Knock back — Area — `low`

## Kruger

### Kruger's behavior

`AFK Stages [C]`, `Dream Realm [A+]`, `Dream Realm (Endless) [A]`, `PVP [C]`

- **Signature skill**: Devastating Axe (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `enemy-debuffer` `life-drain`
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Play overview

Kruger shreds **Phys DEF** on single-target hits, then slashes to knock down foes and cut DEF further on ultimate. Low-DEF enemies take **Vulnerable** with increased physical damage and life drain on follow-up strikes. Isolated positioning grants a **battle-start shield** and extra drain for safer opening trades. Killing vulnerable foes **permanently stacks ATK** across the fight. He softens targets for **physical damage dealers** better than anyone in his niche. **Magic-heavy teams** gain little from his DEF shred, and **spread lines** deny his vulnerable execute chain. His battle ranged DEF increase helps him survive at distance while stacking vulnerable kills for permanent ATK.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `high`

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

Look for units providing: `Shield` `Life Drain` `Physical DEF`  
Common buffers are **Hugin** or **Twins**.

- **Tilaya**
  - DEF buff (area, high)
- **Koko**
  - Shield (all units, low)
  - Lifedrain buff (multiple targets, average)
- **Dunlingr**
  - Lifedrain buff (all units, average)
- **Saida**
  - Shield (multiple targets, high)
- **Daimon**
  - Shield (multiple targets, low)
  - Lifedrain buff (single target, average)

### Units benefitting most from Kruger

- Indris (2.5 / 5)
- Bonnie (1.8 / 5)
- Shadewing (1.6 / 5)

### Units that can act as a replacement for Kruger

**Similar Skills**

- Shakir (48% `life-drain`)
- Shadewing (40% `enemy-debuffer`)
- Zorya (40% `life-drain`)

**Damage**

- Kordan (100% `Physical` `Max HP-based damage`)
- Brutus (100% `Physical` `Max HP-based damage`)
- Satrana (100% `Max HP-based damage`)

**Debuffs on enemies**

- Brutus (59% `Phys DEF debuff`)
- Lyca (59% `Phys DEF debuff`)
- Kafra (59% `Phys DEF debuff`)

**Crowd Control**

- Baelran (100% `Knock down`)
- Silven (100% `Knock down`)
- Sylphira (100% `Knock down`)

### Summary for Kruger

#### Kruger Provides

- Stacking buff — Single target

#### Damage types dealt by Kruger

- Physical — Area, Single target
- Max HP-based damage — Area, Single target — `high`

#### Debuffs provided by Kruger

- Damage taken — Single target — `low`
- Phys DEF — Area — `low`
- Vulnerable — Area — `low`

#### Crowd Control provided by Kruger

- Knock down — Single target — `low`

## Kulu

### Kulu's behavior

`AFK Stages [A+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Demolition Zone (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `battlefield-modification` `self-repositioner`
- **Damage types**: Physical `high`

#### Play overview

Kulu opens by **blocking enemy lanes with debris**, then uses skills that **splash to both sides**—allies take reduced friendly-fire damage, but tight formations still suffer. Her ultimate bombards the enemy half with random strikes. Defeated foes can leave **explosive traps**, and her ATK climbs as she damages enemies. She shines when **enemies cluster on their side** and movement paths are contested. **Low raw multipliers** and a modest damage-taken debuff make her a weak pure DPS pick. **Single-target races** or splash-intolerant teams underperform badly.

#### Skill overview

- **Signature skill**: speed `slow`, first cast speed `fast`, buffs `average`, damage `low`
- **Ultimate**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `average`

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
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Aliceth**
  - ATK buff (multiple targets, low)
  - DEF Penetration buff (multiple targets, high)
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
- **Zanie**
  - ATK buff (single target, low)
  - DEF Penetration buff (single target, average)
- **Galahad**
  - ATK SPD via Haste buff (single target, average) `signature fuel`

### Units benefitting most from Kulu

Kulu provides ATK buff (Legendary+) to single targets `low` and DEF Penetration buff (EX+15) to single targets `low`.

- Bonnie (4.2 / 5)
- Indris (3.7 / 5)

### Units that can act as a replacement for Kulu

**Buffs on allies**

- Aliceth (100% `DEF Penetration` `ATK`)
- Kordan (100% `DEF Penetration` `ATK`)
- Zanie (100% `DEF Penetration` `ATK`)

**Similar Skills**

- Alsa (66% `battlefield-modification` `self-repositioner`)
- Soren (40% `self-repositioner`)
- Marilee (33% `self-repositioner`)

**Damage**

- Athalia (100% `Physical`)
- Kruger (100% `Physical`)
- Valka (100% `Physical`)

**Debuffs on enemies**

- Zorya (53% `Movement speed debuff`)

**Crowd Control**

- Scarlita (80% `Knock back` `Knock up`)
- Ulmus (80% `Knock back` `Knock up`)
- Kordan (66% `Knock back` `Knock up`)

### Summary for Kulu

#### Kulu Provides

- Invincibility — Self
- Enhanced form (EX+15) — Single target

#### Damage types dealt by Kulu

- Physical — All units, Area, Single target

#### Debuffs provided by Kulu

- Movement speed — Area — `low`
- Damage taken (Mythic+) — All units — `low`

#### Crowd Control provided by Kulu

- Unaffected — Self — On ultimate
- Displace — Single target — `low`
- Knock back — Single target — `low`
- Knock up — Single target — `low`

## Laios

### Laios's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Dungeon Gourmet (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-buffer` `ally-healer` `summoner`
- **Damage types**: Physical `low`

#### Play overview

Laios summons a **self-regenerating armor construct** on ultimate and confuses enemies in a frontal area to open space. Defeated foes drop **ingredients** that buff allies, with battle-start analysis raising drop rates on early kills. Each ingredient also **permanently grows max HP** over the fight for scaling durability. He blends **summon pressure, debuff, and stacking buffs** in one tank slot. He peaks when **enemies die often** inside his ingredient loop. **Slow fights with few defeats** never stack HP or buffs, and burst that kills the construct early removes his frontline.

#### Skill overview

- **Signature skill**: speed `slow`, heal `average`, buffs `average`
- **Ultimate**: speed `fast`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`

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

Look for units providing: `ATK` `ATK SPD / Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Solise**.

- **Tilaya**
  - Max HP buff (area, average)
  - DEF buff (area, high)
  - DEF buff (area, high)
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)
- **Lucca**
  - DEF buff (area, average)
  - DEF buff (area, average)
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, average) `signature fuel`

### Units benefitting most from Laios

Laios provides ATK buff to multiple targets `low` — conditional (rare).

- Carolina (3.1 / 5)
- Shadewing (2.9 / 5)
- Indris (2.6 / 5)

### Units that can act as a replacement for Laios

**Similar Skills**

- Damian (100% `ally-buffer` `ally-healer` `summoner`)
- Koko (66% `ally-buffer` `ally-healer`)
- Isabella (66% `ally-buffer` `ally-healer`)

**Debuffs on enemies**

- Lyca (55% `Phys DEF debuff`)

**Crowd Control**

- Eironn (100% `Bind`)
- Kordan (100% `Bind`)
- Evie (100% `Bind`)

### Summary for Laios

#### Laios Provides

- Summoning — Single target
- Stacking buff (EX+10) — Single target

#### Debuffs provided by Laios

- Magic DEF — Area — `low`
- Phys DEF — Area — `average`

#### Crowd Control provided by Laios

- Bind — Area — `average`

## Lenya

### Lenya's behavior

`AFK Stages [C]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Wild Duel (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `assassin` `counterattack` `self-repositioner`
- **Damage types**: Physical `average`, Max HP-based damage `average`

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
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, average)
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Shield (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Pandora**
  - Max HP buff (single target, average)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Lenya

- Carolina (2.0 / 5)
- Nerion (1.6 / 5)

### Units that can act as a replacement for Lenya

**Best overall replacement**

- Soren (82% `Damage` `Similar Skills` `Crowd Control`)
- Kafra (79% `Damage` `Crowd Control`)
- Perseus (77% `Damage` `Crowd Control`)

**Similar Skills**

- Soren (66% `counterattack` `self-repositioner`)
- Kafra (48% `assassin` `self-repositioner`)
- Marilee (30% `self-repositioner`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Crowd Control**

- Perseus (100% `Knock back` `Stun`)
- Soren (100% `Knock back` `Stun`)
- Scarlita (90% `Knock back` `Stun`)

### Summary for Lenya

#### Damage types dealt by Lenya

- Physical — Area, Single target
- Max HP-based damage — Single target — `average`

#### Crowd Control provided by Lenya

- Unaffected — Self — Once
- Knock back — Area — `low`
- Stun — Single target — `average`

## Lily May

### Lily May's behavior

`AFK Stages [A]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Tempest Shot (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `cc-immunity` `hp-scaling` `invincibility` `self-repositioner` `transformation` `ultimate-cancel`
- **Damage types**: Magic `low`, Max HP-based damage `low`

#### Play overview

Lily May enters a **defensive ultimate** that interrupts the enemy's cast, draining extra energy on the first stop. She strikes multiple times while **invincible**, then grows stronger in stages that **raise ATK and hit count** on each growth. Ally buffs trigger growth and **expand enhanced attacks** for wider pressure across the line. Battle penetration rises over time so later hits bite harder on armored targets. She counters **enemy ultimate timing** and scales into a carry role. **Interrupt-immune casts** or burst that kills her before growth cycles complete blunt her entire kit.

#### Skill overview

- **Signature skill (ult)**: speed `average`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `low`
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
Common buffers are **Twins**, **Mikola**, or **Hugin**.

Lily May also requires units **buffing them**

- **Aliceth**
  - ATK buff (multiple targets, low)
  - DEF Penetration buff (multiple targets, high)
  - Grants 4 distinct stat buffs to Lily May
- **Koko**
  - Grants 5 distinct stat buffs to Lily May
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
  - Grants 6 distinct stat buffs to Lily May (start of battle)
- **Kordan**
  - ATK buff (multiple targets, high)
  - DEF Penetration buff (multiple targets, low)
  - Grants 3 distinct stat buffs to Lily May
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
  - Grants 4 distinct stat buffs to Lily May

### Units benefitting most from Lily May

Lily May provides DEF Penetration buff (Legendary+) to single targets `low`.

- Bonnie (2.6 / 5)
- Indris (1.7 / 5)
- Shadewing (1.7 / 5)

### Units that can act as a replacement for Lily May

**Best overall replacement**

- Saida (92% `Damage` `Debuffs on enemies` `Crowd Control`)
- Sylphira (82% `Damage` `Crowd Control`)
- Pippa (63% `Damage`)

**Buffs on allies**

- Aliceth (100% `DEF Penetration`)
- Silven (100% `DEF Penetration`)
- Kordan (100% `DEF Penetration`)

**Similar Skills**

- Athalia (60% `hp-scaling` `self-repositioner` `transformation`)
- Marilee (40% `hp-scaling` `self-repositioner`)
- Vala (40% `hp-scaling` `self-repositioner` `transformation`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Mehira (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Saida (100% `Energy drain`)
- Dunlingr (50% `Energy drain`)

**Crowd Control**

- Sylphira (100% `Interrupt`)
- Smokey & Meerky (100% `Interrupt`)
- Gerda (100% `Interrupt`)

### Summary for Lily May

#### Lily May Provides

- Invincibility — Single target

#### Damage types dealt by Lily May

- Magic — Single target
- Max HP-based damage — Single target — `low`

#### Debuffs provided by Lily May

- Energy drain — Single target — `high`

#### Crowd Control provided by Lily May

- Unaffected — Self — Conditional
- Interrupt — Single target — `low`

## Lorsan

### Lorsan's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Whispering Tempest (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `aoe-damage` `dot-specialist`
- **Damage types**: Magic `low`, DoT `high`

#### Play overview

Lorsan links the **nearest and farthest enemy** at battle start, forcing shared damage and control across opposite ends of the line. He then summons a storm that **cuts Haste** and deals sustained damage to everyone within range. Breaking the chain **heals allies** and can reset for another cast within the same fight, rewarding repeated disruption. He shields the weakest ally with **dodge, haste, and regeneration**, and at higher tiers they also gain unaffected status during the protection window. ATK scales after the **first chain break**, so each successful unlink raises his damage ceiling. He mixes **control, healing, and AoE pressure** across a long engagement where the storm can tick for full duration. **Immune or unlinked targets** deny chain payoff entirely, and short fights end before storm damage ramps. Spread enemy lines unlock the full chain-and-storm payoff.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`

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

Look for units providing: `ATK` `Haste` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Hewynn**
  - Healing over time (all units, high)
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Marcille**
  - Haste buff (single target, low) `signature fuel`
  - Direct healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Lorsan

Lorsan provides Haste buff to single targets `high`.

- Indris (3.8 / 5)
- Pippa (2.2 / 5)

### Units that can act as a replacement for Lorsan

**Buffs on allies**

- Tasi (100% `Haste`)
- Twins (90% `Haste`)
- Hugin (72% `Haste`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Twins (100% `Direct healing` `Healing`)

**Similar Skills**

- Arden (80% `aoe-damage` `dot-specialist`)
- Viperian (66% `aoe-damage` `dot-specialist`)
- Faramor (60% `aoe-damage` `dot-specialist`)

**Damage**

- Frieren (100% `DoT` `Magic`)
- Faramor (100% `DoT`)
- Cyran (100% `DoT` `Magic`)

**Debuffs on enemies**

- Alna (66% `Haste debuff` `Max HP debuff`)

**Crowd Control**

- Scarlita (100% `Stun`)
- Zorya (96% `Stun`)
- Soren (90% `Stun`)

### Summary for Lorsan

#### Damage types dealt by Lorsan

- DoT — Area

#### Debuffs provided by Lorsan

- Haste — Area — `average`
- Max HP (Supreme+) — Single target — `average`

#### Crowd Control provided by Lorsan

- Unaffected (Supreme+) — Self — On skill
- Stun (Mythic+) — Multiple targets — `high`

## Lucca

### Lucca's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Quake Slam (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-shielder` `disabler`
- **Ally composition**: place adjacent allies behind at battle prep (DEF buff)
- **Ally composition**: place allies on adjacent tiles behind at battle start (shields and ATK boost)
- **Damage types**: Physical `high`

#### Play overview

Lucca gains a shield, then **interrupts and disarms** an enemy while cleansing her own debuffs for brief **damage reduction**. Her ultimate slams a target to origin or **stuns adjacent tiles** when they cannot be returned. She stays steadfast and stacks **shields for each ally behind** her in formation. Cleansing also **recovers HP**, and battle max HP grows over time for durability. She is a **durable disruptor** for packed frontlines that need control. **Disarm-immune foes** or enemies that never cluster for the slam see limited control value. Her cleanse skill also recovers HP when used, giving her a self-sustain loop between disruption casts on the frontline. Steadfast status protects her while stacking shields behind allies.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `low`

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

Look for units providing: `Max HP` `Shield` `Healing` `Physical DEF` `Magic DEF`  
Common buffers are **Twins**, **Solise**, or **Smokey & Meerky**.

- **Tilaya**
  - Max HP buff (area, average)
  - DEF buff (area, high)
  - DEF buff (area, high)
- **Hepler**
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
- **Koko**
  - Shield (all units, low)
  - Direct healing (all units, average)
- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
  - Direct healing (single target, high)
- **Ludovic**
  - Direct healing (multiple targets, high)

### Units benefitting most from Lucca

Lucca provides DEF buff in an area `low`.

- Granny Dahnie (3.7 / 5)
- Natsu (3.7 / 5)
- Cecia (3.4 / 5)

### Units that can act as a replacement for Lucca

**Best overall replacement**

- Antandra (58% `Crowd Control` `Damage`)
- Lumont (50% `Buffs on allies` `Damage`)

**Buffs on allies**

- Tilaya (100% `Magic DEF` `Physical DEF`)
- Sonja (100% `Magic DEF` `Physical DEF`)
- Lumont (90% `Magic DEF` `Physical DEF`)

**Similar Skills**

- Callan (40% `ally-shielder`)
- Korin (40% `ally-shielder`)
- Reinier (33% `disabler`)

**Damage**

- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)
- Alna (100% `Physical` `Max HP-based damage`)

**Crowd Control**

- Antandra (84% `Stun` `Knock down`)
- Scarlita (74% `Stun` `Knock up` `Knock down`)
- Callan (70% `Stun` `Knock down`)

### Summary for Lucca

#### Damage types dealt by Lucca

- Physical — Area, Single target

#### Crowd Control provided by Lucca

- Immune — Self — On skill
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

Look for units providing: `Shield` `Healing`  
Common buffers are **Rowan**, **Twins**, or **Hugin**.

- **Hepler**
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Koko**
  - Shield (all units, low)
  - Direct healing (all units, average)
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Pandora**
  - Direct healing (single target, average)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Marcille**
  - Direct healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Lucius

Lucius provides Shield in an area `high`.

- Silvina (4.6 / 5)
- Gerda (4.0 / 5)

### Units that can act as a replacement for Lucius

**Best overall replacement**

- Hepler (74% `Buffs on allies` `Damage` `Crowd Control`)
- Scarlita (65% `Crowd Control` `Damage`)
- Antandra (64% `Damage` `Debuffs on enemies` `Crowd Control`)

**Buffs on allies**

- Hugin (100% `Shield`)
- Saida (100% `Shield`)
- Hepler (100% `Shield`)

**Similar Skills**

- Thador (48% `ally-shielder` `enemy-debuffer`)
- Hepler (48% `ally-healer` `ally-shielder`)
- Cassadee (48% `aoe-damage` `enemy-debuffer`)

**Damage**

- Gunnar (100% `Physical`)
- Baelran (100% `Physical`)
- Himmel (100% `Physical`)

**Debuffs on enemies**

- Bonnie (100% `ATK debuff`)
- Zanie (100% `ATK debuff`)
- Lyca (100% `ATK debuff`)

**Crowd Control**

- Aliceth (100% `Knock back` `Stun`)
- Perseus (100% `Knock back` `Stun`)
- Scarlita (100% `Knock back` `Stun`)

### Summary for Lucius

#### Damage types dealt by Lucius

- Physical — Area, Single target

#### Debuffs provided by Lucius

- ATK (Mythic+) — Area — `low`

#### Crowd Control provided by Lucius

- Knock back — Single target — `low`
- Stun — Single target — `low`

## Lucy

### Lucy's behavior

- **Signature skill**: Star Dress: Aquarius Form (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-shielder` `mass-cc`
- **Damage types**: Magic `high`, Max HP-based damage `high`

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
Common buffers are **Twins**, **Hugin**, or **Damian**.

- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, average) `signature fuel`
- **Kazim**
  - ATK SPD via Haste buff (multiple targets, average) `signature fuel`
- **Lorsan**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Tasi**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Lucy

Lucy provides Shield (Mythic+) to single targets `high`.

- Nerion (1.8 / 5)
- Faramor (1.6 / 5)
- Dionel (1.4 / 5)

### Units that can act as a replacement for Lucy

**Best overall replacement**

- Hepler (50% `Buffs on allies` `Crowd Control` `Damage`)

**Buffs on allies**

- Hepler (100% `Shield`)
- Hugin (100% `Shield`)
- Lucius (100% `Shield`)

**Similar Skills**

- Antandra (50% `ally-shielder` `mass-cc`)
- Korin (40% `ally-shielder`)
- Callan (33% `ally-shielder`)

**Damage**

- Marcille (100% `Magic` `Max HP-based damage`)
- Natsu (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Crowd Control**

- Lucca (100% `Stun` `Knock up`)
- Scarlita (100% `Stun` `Knock up`)
- Zandrok (100% `Stun` `Knock up`)

### Summary for Lucy

#### Damage types dealt by Lucy

- Magic — All units, Single target
- Max HP-based damage — All units, Single target — `high`

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

Look for units providing: `Healing`  
Common buffers are **Solise**, **Twins**, or **Hugin**.

- **Velara**
  - Direct healing (area, low)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Contess**
  - Direct healing (single target, high)
- **Evie**
  - Direct healing (single target, high)
- **Zanie**
  - Direct healing (single target, high)
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Ludovic

Ludovic provides Direct healing in an area `average` and Healing over time to single targets `high`.

- Callan (3.0 / 5)
- Evie (2.7 / 5)
- Niru (2.5 / 5)

### Units that can act as a replacement for Ludovic

**Best overall replacement**

- Smokey & Meerky (54% `Healing` `Similar Skills`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing over time` `Healing`)
- Evie (100% `Direct healing` `Healing`)

**Similar Skills**

- Smokey & Meerky (100% `ally-healer` `aoe-healing`)
- Fay (100% `ally-healer` `aoe-healing`)
- Hewynn (100% `ally-healer` `aoe-healing`)

**Damage**

- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)
- Shemira (100% `Magic` `Max HP-based damage`)

**Crowd Control**

- Bonnie (100% `Stun`)
- Phraesto (100% `Stun`)
- Callan (100% `Stun`)

### Summary for Ludovic

#### Damage types dealt by Ludovic

- Magic — All units, Single target
- Max HP-based damage — Single target — `average`

#### Crowd Control provided by Ludovic

- Unaffected — Self — On skill
- Stun (Supreme+) — Single target — `average`

## Lumont

### Lumont's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Lumont's Charge (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `enemy-debuffer` `taunt`
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Play overview

Lumont charges in a line, **knocking enemies back** toward a chosen tile while building **large shields that grow per adjacent foe**. His stomp adds AoE damage, and **battle haste scales with nearby enemy count** so he swings faster the more bodies crowd him. Sustained damage taken triggers **multi-ring slams** that slash ATK from surrounding enemies, while shielded moments **regenerate HP each second** to stretch his frontline time. He excels as a **tank that thickens with crowd pressure**, punishing swarms that sit on him and feed his haste loop. Against **sparse lines or burst that breaks shields fast**, his regen, counter-slam scaling, and haste buildup never fully ramp.

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`

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

Look for units providing: `Haste` `Shield` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Damian**.

- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Hewynn**
  - Healing over time (all units, high)
- **Koko**
  - Shield (all units, low)
  - Direct healing (all units, average)
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
  - Direct healing (all units, low)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Marcille**
  - Haste buff (single target, low) `signature fuel`
  - Direct healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Lumont

Lumont provides DEF buff to multiple targets `low`.

- Shadewing (2.2 / 5)
- Carolina (2.0 / 5)
- Nerion (1.6 / 5)

### Units that can act as a replacement for Lumont

**Best overall replacement**

- Hepler (66% `Crowd Control` `Damage`)
- Antandra (54% `Buffs on allies`)

**Buffs on allies**

- Tilaya (100% `Magic DEF` `Physical DEF`)
- Sonja (100% `Magic DEF` `Physical DEF`)
- Lucca (100% `Magic DEF` `Physical DEF`)

**Similar Skills**

- Kruger (40% `enemy-debuffer`)
- Granny Dahnie (40% `taunt`)
- Shadewing (33% `enemy-debuffer`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Bonnie (100% `ATK debuff`)
- Antandra (60% `ATK debuff`)

**Crowd Control**

- Hepler (100% `Taunt` `Stun`)
- Antandra (51% `Taunt` `Stun`)

### Summary for Lumont

#### Damage types dealt by Lumont

- Physical — Area, Single target
- Max HP-based damage — Area — `average`

#### Debuffs provided by Lumont

- ATK (Mythic+) — Single target — `average`

#### Crowd Control provided by Lumont

- Unaffected — Self — On skill
- Stun — Area — `low`
- Taunt — Area — `average`
- Knock up (Mythic+) — Single target — `low`

## Lyca

### Lyca's behavior

`AFK Stages [C]`, `Dream Realm [A]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Comet Archery (ultimate)
- **Movement**: stationary (avg attack range 11.0 tiles)
- **Behavior tags**: `ally-buffer` `energy-provider`
- **Damage types**: Physical `average`

#### Play overview

Lyca opens by **buffing all allies' attack speed** and fueling the first cast with bonus energy for quick tempo. Her line shot lets nearby allies **summon meteors on normal attacks**, stacking area pressure alongside her ultimate volleys. AoE meteor rain also **shaves enemy Phys DEF**, and passive meteors assist throughout the fight while battle haste keeps her rotation moving. Ultimate hits **deepen the DEF shred**, letting dealers exploit softened targets over time. She shines when **allies stay within ultimate range** and attack often enough to proc meteors on every cycle. Spread formations or **allies outside her line** waste her attack-speed package and meteor summons.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `average`

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
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Lyca**
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Tasi**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Pandora**
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Lyca

Lyca provides ATK SPD buff to all units `low` and Energy recovery to all units `low`.

- Indris (5.0 / 5)
- Hewynn (3.7 / 5)
- Arden (3.5 / 5)
- Valen (3.5 / 5)
- Rhys (3.4 / 5)
- Contess (2.7 / 5)
- Chippy (2.6 / 5)
- Mirael (2.3 / 5)

### Units that can act as a replacement for Lyca

**Buffs on allies**

- Ravion (72% `Energy`)
- Twins (50% `Energy`)
- Dunlingr (50% `ATK SPD`)

**Similar Skills**

- Twins (50% `ally-buffer` `energy-provider`)
- Ravion (36% `energy-provider`)
- Parisa (36% `ally-buffer`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Laios (71% `Phys DEF debuff`)
- Kafra (55% `Phys DEF debuff`)
- Zanie (51% `Phys DEF debuff` `ATK debuff`)

**Crowd Control**

- Phraesto (100% `Stun`)
- Callan (100% `Stun`)
- Zandrok (100% `Stun`)

### Summary for Lyca

#### Damage types dealt by Lyca

- Physical — All units, Area, Single target

#### Debuffs provided by Lyca

- ATK — All units — `low`
- Phys DEF — All units — `average`

#### Crowd Control provided by Lyca

- Stun (EX+10) — Single target — `average`

## Marcille

### Marcille's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Silver-White Wings that Streak Across the Skies (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-healer` `aoe-damage` `battle-start-burst` `high-damage-ult` `revive` `summoner`
- **Ally composition**: place ally 1 tile in front at battle prep (revive target)
- **Damage types**: Magic `high`, Max HP-based damage `high`

#### Play overview

Marcille must **channel every skill**, trading instant casts for heavy payoff once each completes without interruption. Her ultimate **continuously summons companions** while active, and channeled AoE blasts and blinds **heal allies** mid-fight when channels land cleanly. Channeling the ultimate also **raises battle haste**, and she can **revive one fallen ally** after a completed cast. She needs **protection and time** so channels finish before control cancels them. Fights that **interrupt her setup** leave much of her heal and summon value unrealized.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, damage `high`

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

Look for units providing: `ATK SPD / Haste` `Healing` `Energy`  
Common buffers are **Twins**, **Smokey & Meerky**, or **Solise**.

- **Koko**
  - Direct healing (all units, average)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, average) `signature fuel`
- **Velara**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Direct healing (area, low)
- **Contess**
  - Direct healing (single target, high)

### Units benefitting most from Marcille

Marcille provides Haste buff (Legendary+) to single targets `low` and Direct healing (Mythic+) to multiple targets `high`.

- Rowan (2.3 / 5)

### Units that can act as a replacement for Marcille

**Best overall replacement**

- Natsu (61% `Damage`)
- Galahad (54% `Damage` `Buffs on allies`)

**Buffs on allies**

- Galahad (100% `Haste`)
- Twins (100% `Haste`)
- Hugin (100% `Haste`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Evie (100% `Direct healing` `Healing`)

**Similar Skills**

- Florabelle (40% `aoe-damage` `summoner`)
- Frieren (36% `aoe-damage` `high-damage-ult`)
- Laios (34% `ally-healer` `summoner`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Crowd Control**

- Aliceth (97% `Blind`)
- Twins (81% `Blind`)
- Damian (81% `Blind`)

### Summary for Marcille

#### Marcille Provides

- Revive ally (Mythic+) — Single target
- Stacking buff (Supreme+) — Single target

#### Damage types dealt by Marcille

- Magic — All units, Area, Single target
- Max HP-based damage — All units, Area, Single target — `high`

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
- **Damage types**: Physical `average`, True damage `low`

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

Look for units providing: `ATK` `ATK SPD / Haste` `CRIT` `CRIT DMG Boost`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (all units, low) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
- **Tasi**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`

### Units benefitting most from Marilee

Marilee provides ATK buff (EX+10) to single targets `low`.

- Carolina (1.4 / 5)
- Nerion (1.2 / 5)
- Silven (1.1 / 5)

### Units that can act as a replacement for Marilee

**Best overall replacement**

- Vala (88% `Damage` `Crowd Control`)
- Nazrik (73% `Damage` `Crowd Control`)
- Faramor (68% `Damage` `Crowd Control`)

**Buffs on allies**

- Gunnar (100% `ATK`)
- Contess (100% `ATK`)
- Frieren (100% `ATK`)

**Similar Skills**

- Athalia (80% `hp-scaling` `self-repositioner`)
- Kordan (66% `hp-scaling` `self-repositioner`)
- Silven (48% `hp-scaling`)

**Damage**

- Baelran (100% `Physical` `Max HP-based damage` `True damage`)
- Himmel (100% `Physical` `Max HP-based damage` `True damage`)
- Faramor (100% `Physical` `True damage`)

**Crowd Control**

- Gunnar (100% `Stun`)
- Contess (100% `Stun`)
- Frieren (100% `Stun`)

### Summary for Marilee

#### Marilee Provides

- Stacking buff (Mythic+) — Multiple targets

#### Damage types dealt by Marilee

- Physical — Multiple targets, Single target
- True damage — Single target — `low`

#### Crowd Control provided by Marilee

- Stun — Single target — `low`

## Mehira

### Mehira's behavior

`AFK Stages [S+]`, `Dream Realm [B]`, `Dream Realm (Endless) [A+]`, `PVP [A+]`

- **Signature skill**: Euphoric Rush (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `aoe-damage` `enemy-grouping` `life-drain` `mass-cc` `untargetable`
- **Damage types**: Magic `low`, DoT `average`, HP loss `average`, Max HP-based damage `average`

#### Play overview

Mehira charms an area with **multi-hit AoE**, then whips a frontal arc that **costs HP from all units** but grants allies haste when caught in the lash. She **pulls enemies to a tile**, drains life while scaling ATK from healing received, and summons **voidlings that attack for her**. In danger she can **sacrifice a summon to become untargetable** and heal, while charmed foes take increased damage. She peaks against **clustered targets** that absorb whip pulls and charm setups. Teams that **kill voidlings early** or spread lines blunt her drain payoff.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, damage `low`

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

Look for units providing: `Haste` `Max HP` `Healing` `Life Drain`  
Common buffers are **Twins**, **Hugin**, or **Solise**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Velara**
  - Haste buff (single target, low) `signature fuel`
  - Direct healing (area, low)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Contess**
  - Direct healing (single target, high)
- **Himmel**
  - Direct healing (single target, low)

### Units benefitting most from Mehira

Mehira provides Haste buff to single targets `average`.

- Gwyneth (1.4 / 5)
- Aurora (1.3 / 5)
- Florabelle (1.3 / 5)
- Ravion (1.3 / 5)

### Units that can act as a replacement for Mehira

**Buffs on allies**

- Galahad (100% `Haste`)
- Twins (100% `Haste`)
- Hugin (100% `Haste`)

**Similar Skills**

- Eironn (51% `aoe-damage` `enemy-grouping` `mass-cc`)
- Igor (51% `aoe-damage` `life-drain` `untargetable`)
- Cyran (34% `aoe-damage` `enemy-grouping`)

**Damage**

- Dunlingr (100% `DoT` `Magic` `Max HP-based damage` `HP loss`)
- Zorya (100% `Magic` `Max HP-based damage` `HP loss`)
- Ravion (97% `Max HP-based damage` `HP loss`)

**Debuffs on enemies**

- Contess (100% `Damage taken debuff`)
- Himmel (100% `Damage taken debuff`)
- Kulu (100% `Damage taken debuff`)

**Crowd Control**

- Satrana (51% `Charm`)
- Cyran (51% `Displace`)
- Eironn (51% `Displace`)

### Summary for Mehira

#### Mehira Provides

- HP threshold strike (Mythic+) — Single target
- Summoning (Mythic+) — Single target

#### Damage types dealt by Mehira

- Magic — Area, Single target
- DoT — Single target
- HP loss — Single target — `average`
- Max HP-based damage — Single target — `average`

#### Debuffs provided by Mehira

- Damage taken (Supreme+) — Single target — `low`

#### Crowd Control provided by Mehira

- Untargetable (Mythic+) — Self — On skill
- Charm — Single target — `average`
- Displace — All units — `low`

## Mikola

### Mikola's behavior

`AFK Stages [B]`, `Dream Realm [B]`, `Dream Realm (Endless) [A]`, `PVP [A]`

- **Signature skill**: Dauntless Hymn (ultimate)
- **Movement**: moving (avg attack range 2.0 tiles)
- **Behavior tags**: `ally-buffer` `aoe-healing`
- **Damage types**: Physical `low`

#### Play overview

Mikola generates a **Courage Sphere** that buffs nearby allies and **heals everyone in range** once damage thresholds trip during the fight. She places a **central zone** that empowers allies while her side controls it, and heals two weakest allies with DEF boosts to keep fragile carries standing. The sphere grows over time, dealing **continuous DoT to enemies** adjacent to buffed allies, and zone control **freezes aura duration** so the buff window does not decay early. She needs **map control and grouped allies** inside Courage range to maximize healing, DoT aura, and zone bonuses. Fights that **deny zone ownership** or keep allies scattered shrink her buff and sustain impact.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, heal `average`, buffs `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`

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

Look for units providing: `ATK` `Haste` `Healing` `Physical DEF` `Magic DEF`  
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Marcille**
  - Haste buff (single target, low) `signature fuel`
  - Direct healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Pandora**
  - Direct healing (single target, average)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Koko**
  - Direct healing (all units, average)

### Units benefitting most from Mikola

Mikola provides ATK buff to all units `average`, Direct healing to multiple targets `low`, Haste buff to multiple targets `average`, and Vitality buff (EX+10) to multiple targets `high`.

**45** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Lily May (4.8 / 5)
- Dionel (4.2 / 5)
- Fay (4.2 / 5)
- Perseus (4.0 / 5)
- Seth (3.9 / 5)
- Lorsan (3.9 / 5)
- Vala (3.8 / 5)
- Tasi (3.5 / 5)
- Laios (3.4 / 5)
- Zorya (3.1 / 5)

### Units that can act as a replacement for Mikola

**Best overall replacement**

- Contess (53% `Healing` `Buffs on allies`)
- Evie (53% `Healing` `Buffs on allies`)

**Buffs on allies**

- Contess (63% `ATK`)
- Evie (63% `ATK`)
- Gunnar (55% `ATK` `Vitality buff`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing over time` `Healing`)
- Twins (100% `Direct healing` `Healing`)

**Similar Skills**

- Smokey & Meerky (48% `aoe-healing`)
- Koko (48% `ally-buffer`)
- Ludovic (40% `aoe-healing`)

### Summary for Mikola

#### Crowd Control provided by Mikola

- Unaffected (Supreme+) — Self — Conditional

## Mirael

### Mirael's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Winged Flame (ultimate)
- **Movement**: stationary (avg attack range 10.1 tiles)
- **Behavior tags**: `dot-specialist` `fire-attack`
- **Damage types**: Magic `high`, DoT `low`, Max HP-based damage `high`

#### Play overview

Mirael lays a **wide frontal burn line** that hits harder on already burning foes, then maintains **sustained single-target burn** between ultimates to keep pressure on priority marks. Magic burst adds **adjacent splash**, battle attack speed rises, and after the first ultimate her **normal attacks become area fireballs** permanently for the rest of the fight. She also **extends burn DoT duration** so flames linger longer on targets her team keeps controlled. Her kit rewards **grouped enemies** where splash, fireball normals, and burn bonuses chain together every cycle. Against **spread or cleanse-heavy lines**, burns fail to stack and her transformed attack pattern underdelivers for much of the fight.

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `high`
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
Common buffers are **Twins**, **Hugin**, or **Damian**.

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (all units, low) `signature fuel`
- **Lorsan**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Tasi**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Mirael

- Shadewing (1.7 / 5)
- Bonnie (1.7 / 5)
- Himmel (1.5 / 5)

### Units that can act as a replacement for Mirael

**Best overall replacement**

- Gwyneth (60% `Damage` `Similar Skills`)
- Natsu (54% `Damage`)
- Silven (53% `Damage`)

**Similar Skills**

- Gwyneth (96% `dot-specialist` `fire-attack`)
- Satrana (40% `dot-specialist` `fire-attack`)
- Zanie (40% `fire-attack`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage` `DoT`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage` `DoT`)

### Summary for Mirael

#### Damage types dealt by Mirael

- Magic — Area, Single target
- DoT — Single target
- Max HP-based damage — Area, Single target — `average`

## Nara

### Nara's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Phantom Chains (Skill 1)
- **Movement**: mostly stationary (pulls enemies; moves on failed pull)
- **Behavior tags**: `ally-healer` `assassin` `execute`
- **Damage types**: Physical `high`, HP loss `average`, Max HP-based damage `high`, True damage `high`

#### Play overview

Nara strikes a hero for **scaling damage against low HP ratios**, then yanks out-of-range foes **into melee** for a knock-up combo and rapid follow-up attacks. Each assist or defeat **grows her ATK**, and an ultimate kill **releases a shockwave** that damages enemies and heals allies while refunding energy on the finisher. She blends **assassin burst with team sustain** when fights produce kills and wounded targets she can reach. Pulling isolated carries and chaining knock-up strikes define her win condition against backline-heavy formations that leave squishy targets exposed. She needs **access to wounded or isolated targets** and enough energy to cycle her pull-strike loop repeatedly through the fight. **Tanky frontlines or foes that stay in range** deny her execute angle, shockwave value, and the energy refund that keeps her assassin tempo alive through longer trades.

#### Skill overview

- **Signature skill**: speed `average`, damage `low`
- **Ultimate**: speed `fast`, first cast speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, damage `low`

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
Common buffers are **Mikola**, **Twins**, or **Ravion**.

- **Lyca**
  - Energy recovery (all units, low) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Nara

Nara provides Direct healing (Mythic+) in an area `low`.

- Carolina (1.8 / 5)
- Indris (1.6 / 5)
- Lily May (1.3 / 5)

### Units that can act as a replacement for Nara

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Twins (100% `Direct healing` `Healing`)

**Similar Skills**

- Harak (50% `assassin` `execute`)
- Ludovic (30% `ally-healer`)
- Isabella (30% `ally-healer`)

**Damage**

- Athalia (100% `Physical` `True damage` `Max HP-based damage` `HP loss`)
- Faramor (84% `True damage` `Physical` `HP loss`)
- Himmel (81% `True damage` `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Lorsan (80% `Max HP debuff`)
- Alna (66% `Max HP debuff` `Vitality debuff`)
- Nazrik (66% `Max HP debuff` `Vitality debuff`)

**Crowd Control**

- Cyran (93% `Knock down` `Displace`)
- Scarlita (80% `Knock down` `Knock up`)
- Reinier (77% `Displace` `Knock down` `Knock up`)

### Summary for Nara

#### Damage types dealt by Nara

- Physical — Single target
- HP loss — Single target — `average`
- Max HP-based damage — Area, Single target — `high`
- True damage — Single target — `high`

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

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Lightning Fire Dragon's Roar/Fire Dragon King's Roar (ultimate)
- **Movement**: moving (avg attack range 3.0 tiles)
- **Behavior tags**: `aoe-damage` `dot-specialist` `fire-attack` `high-damage-ult` `mass-cc` `transformation`
- **Damage types**: Magic `high`, Max HP-based damage `high`

#### Play overview

Natsu chooses modes between **stun-heavy frontal AoE** or **greater raw damage**, adapting each cast to the fight state. The first ally defeat **boosts his ATK and DEF**, with extra crit if a bonded ally falls, while every damage tick also **shaves target max HP**. Sustained burns apply when foes lose HP from **non-normal sources**, feeding his combat scaling. He peaks in **long fights with ally casualties** that unlock his spikes. Early burst or **lines that deny mode setup** leave his burn package thin.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, first cast speed `fast`, damage `high`
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
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Tilaya**
  - DEF buff (area, high)
  - DEF buff (area, high)
- **Lucca**
  - DEF buff (area, average)
  - DEF buff (area, average)
- **Sonja**
  - ATK buff (multiple targets, average)
  - DEF buff (multiple targets, low)
  - DEF buff (multiple targets, low)
- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
- **Antandra**
  - DEF buff (single target, average)
  - DEF buff (single target, average)

### Units benefitting most from Natsu

Natsu provides Magic DEF buff to single targets `average` and Phys DEF buff to single targets `average`.

- Bonnie (2.6 / 5)
- Shadewing (2.2 / 5)
- Lily May (1.4 / 5)

### Units that can act as a replacement for Natsu

**Best overall replacement**

- Perseus (69% `Damage` `Crowd Control` `Buffs on allies`)
- Frieren (61% `Damage`)
- Zorya (61% `Damage` `Crowd Control` `Debuffs on enemies`)

**Buffs on allies**

- Perseus (100% `Magic DEF buff` `Phys DEF buff`)

**Similar Skills**

- Frieren (61% `aoe-damage` `dot-specialist` `high-damage-ult`)
- Gwyneth (60% `dot-specialist` `fire-attack` `mass-cc`)
- Arden (60% `aoe-damage` `dot-specialist` `mass-cc`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Lorsan (72% `Haste debuff` `Max HP debuff`)
- Galahad (65% `Haste debuff`)
- Alna (63% `Haste debuff` `Max HP debuff`)

**Crowd Control**

- Callan (100% `Stun` `Knock down`)
- Scarlita (100% `Stun` `Knock down`)
- Zorya (100% `Stun` `Knock down`)

### Summary for Natsu

#### Damage types dealt by Natsu

- Magic — Single target
- DoT — Single target
- Max HP-based damage — Area, Single target — `high`

#### Debuffs provided by Natsu

- Haste — Single target — `average`
- Max HP (Mythic+) — Single target — `average`

#### Crowd Control provided by Natsu

- Knock down — Area — `low`
- Stun — Single target — `average`

## Nazrik

### Nazrik's behavior

`AFK Stages [A]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [B]`

- **Signature skill**: Rend Rupture (ultimate)
- **Movement**: stationary (avg attack range 10.0 tiles)
- **Behavior tags**: `hp-scaling` `mark-target`
- **Damage types**: Physical `high`, Max HP-based damage `average`, True damage `high`

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

- **Harak**
  - Crit buff (single target, low)
- **Rhys**
  - Crit buff (single target, low)
- **Walker**
  - Crit buff (single target, low)

### Units benefitting most from Nazrik

- Shadewing (1.9 / 5)
- Indris (1.8 / 5)
- Carolina (1.8 / 5)

### Units that can act as a replacement for Nazrik

**Best overall replacement**

- Vala (63% `Damage` `Crowd Control`)
- Athalia (52% `Damage`)

**Similar Skills**

- Silven (100% `hp-scaling` `mark-target`)
- Aliceth (48% `hp-scaling` `mark-target`)
- Marilee (40% `hp-scaling`)

**Damage**

- Frieren (100% `True damage` `Max HP-based damage`)
- Himmel (100% `True damage` `Physical` `Max HP-based damage`)
- Athalia (100% `True damage` `Physical` `Max HP-based damage`)

**Crowd Control**

- Aliceth (100% `Stun`)
- Bonnie (100% `Stun`)
- Phraesto (100% `Stun`)

### Summary for Nazrik

#### Nazrik Provides

- Stacking buff — Single target

#### Damage types dealt by Nazrik

- Physical — Single target
- Max HP-based damage — Single target — `low`
- True damage — Single target — `high`

#### Debuffs provided by Nazrik

- Healing — Single target — `low`
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
- **Damage types**: Magic `high`, DoT `average`, Max HP-based damage `high`

#### Play overview

Nerion applies **drowning DoT to controlled enemies**, then bounces attacks between drowning targets after an ATK boost on ultimate for chained magic pressure. Enhanced normals **knock back and stun**, projectiles erupt with **delayed knock-up**, and battle start **drowns the rearmost foe** with ATK and haste cuts before control even lands. When every non-summon enemy drowns he gains **permanent empowerment and penetration**, spiking his damage for the rest of the fight. He excels beside **consistent control** that keeps drowning active across multiple targets. **Control-immune or fast-moving lines** never feed his bounce damage or empowerment spike.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `high`

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

Look for units providing: `ATK SPD / Haste` `Shield` `Energy` `DEF Penetration`  
Common buffers are **Twins**, **Hugin**, or **Rowan**.

Nerion also requires units **applying crowd control** to enemies

- **Aliceth**
  - DEF Penetration buff (multiple targets, high)
  - Enables CC on enemies via Blind (area, average)
- **Eironn**
  - Enables CC on enemies via Bind (area, high)
- **Kordan**
  - Enables CC on enemies via Bind (area, high)
- **Callan**
  - Shield (single target, low)
  - Enables CC on enemies via Stun (all units, average)
- **Koko**
  - Shield (all units, low)
  - Enables CC on enemies via Stun (area, average)

### Units benefitting most from Nerion

- Kazim (3.8 / 5)

### Units that can act as a replacement for Nerion

**Similar Skills**

- Shadewing (96% `dot-specialist` `enemy-debuffer`)
- Carolina (96% `dot-specialist` `enemy-debuffer`)
- Bonnie (57% `battle-start-burst` `enemy-debuffer`)

**Damage**

- Frieren (100% `DoT` `Magic` `Max HP-based damage`)
- Zorya (100% `Magic` `Max HP-based damage`)
- Cryonaia (98% `DoT` `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Ravion (100% `ATK debuff`)
- Bonnie (100% `ATK debuff`)
- Zanie (100% `ATK debuff`)

**Crowd Control**

- Zandrok (100% `Knock up` `Stun`)
- Scarlita (100% `Knock up` `Stun`)
- Lucca (100% `Knock up` `Stun`)

### Summary for Nerion

#### Nerion Provides

- Enhanced form (Supreme+) — Single target

#### Damage types dealt by Nerion

- Magic — Area, Single target
- DoT — Single target
- Max HP-based damage — Area, Single target — `high`

#### Debuffs provided by Nerion

- ATK (Mythic+) — Single target — `low`

#### Crowd Control provided by Nerion

- Knock up — Area — `low`
- Stun — Single target — `average`

## Niru

### Niru's behavior

`AFK Stages [A+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Soul Shepherd (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-healer` `battle-start-ult` `hp-scaling`
- **Ally composition**: nearest ally auto-selected at battle start; prioritizes ally behind
- **Damage types**: Magic `high`, HP loss `low`

#### Play overview

Niru stores an ally soul at battle start so they **keep fighting in spirit form** after a fatal blow, preserving output from a key carry. She strikes the weakest foe for **bonus damage at low HP**, drains enemy HP to **heal the weakest ally**, and grows battle max HP to stay relevant on the field. Her opening ultimate **costs no energy**, letting the spirit safeguard trigger immediately. Attacks also briefly **block target healing**, adding soft anti-sustain on her pressure target. She is a **battle-start safety net** for one ally with drain-based sustain for the team. Without a **worthy soul target** or fights that end before spirit triggers, much of her protection sits idle.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, first cast speed `fast`, heal `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, damage `high`

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

Look for units providing: `Healing` `Physical DEF` `Magic DEF`  
Common buffers are **Solise**, **Smokey & Meerky**, or **Twins**.

Niru also requires a unit **to bless** and/or enemies **to be defeated**

- **Tilaya**
  - DEF buff (area, high)
  - DEF buff (area, high)
- **Koko**
  - Direct healing (all units, average)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)
- **Sonja**
  - DEF buff (multiple targets, low)
  - DEF buff (multiple targets, low)

### Units benefitting most from Niru

- Bonnie (2.4 / 5)
- Shadewing (1.9 / 5)
- Zorya (1.4 / 5)

### Units that can act as a replacement for Niru

**Similar Skills**

- Ludovic (36% `ally-healer`)
- Isabella (36% `ally-healer`)
- Smokey & Meerky (30% `ally-healer`)

**Damage**

- Zorya (100% `Magic` `HP loss`)
- Shadewing (90% `Magic` `HP loss`)
- Dunlingr (90% `Magic` `HP loss`)

**Debuffs on enemies**

- Gunnar (100% `Healing debuff`)
- Nazrik (100% `Healing debuff`)
- Harak (100% `Healing debuff`)

### Summary for Niru

#### Niru Provides

- Spirit form protection — Single target
- Start-of-battle cast (Mythic+) — Self

#### Damage types dealt by Niru

- Magic — All units, Single target
- HP loss — Single target — `low`

#### Debuffs provided by Niru

- Healing (Supreme+) — Single target — `low`

## Odie

### Odie's behavior

`AFK Stages [A]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Heart Crusher (Mythic+)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Behavior tags**: `dot-specialist` `execute`
- **Damage types**: Magic `low`, DoT `low`

#### Play overview

Odie plants a **persistent DoT** with his ultimate, then triple-shot normals that **stack poison base damage** on already poisoned targets for escalating tick pressure. Battle attack speed rises, and he can **instantly defeat poisoned foes below a HP threshold** once the venom has softened them enough. Bonus damage also lands on **poisoned triple-shots**, rewarding repeated focus on a single marked victim. He needs **time to layer poison** and enough shots on the same mark to reach execute range. **Cleanse or spread targets** that slip the threshold kill waste his execute angle and poison stacking loop.

#### Skill overview

- **Signature skill**: speed `fast`, debuffs `average`
- **Ultimate**: speed `average`, debuffs `average`, damage `average`
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
Common buffers are **Twins**, **Hugin**, or **Damian**.

- **Tasi**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, average) `signature fuel`

### Units benefitting most from Odie

- Bonnie (2.3 / 5)
- Shadewing (2.2 / 5)
- Indris (1.6 / 5)

### Units that can act as a replacement for Odie

**Best overall replacement**

- Frieren (68% `Damage` `Debuffs on enemies`)
- Mirael (55% `Damage`)
- Galahad (50% `Damage`)

**Similar Skills**

- Mirael (40% `dot-specialist`)
- Shadewing (33% `dot-specialist`)
- Carolina (33% `dot-specialist`)

**Damage**

- Frieren (100% `Magic` `DoT` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `DoT` `Max HP-based damage`)

**Debuffs on enemies**

- Frieren (100% `DoT`)

### Summary for Odie

#### Damage types dealt by Odie

- Magic — Single target
- DoT — Single target

#### Debuffs provided by Odie

- DoT — Single target — `average`
- Poison — Single target — `low`

## Pandora

### Pandora's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [A]`, `PVP [A+]`

- **Signature skill**: Boxed Blessing (Skill 1)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `enemy-debuffer` `energy-provider` `mass-cc`
- **Ally composition**: rearmost ally enters invincible box, then gains Energy and ATK
- **Damage types**: Magic `high`, DoT `average`, HP loss `low`

#### Play overview

Pandora's ultimate **CCs every unit except herself**, freezing the entire field while she alone keeps acting, while at battle start she **pulls an ally into her box** and restores their energy for an early tempo spike. Corruption stacks **drive debuffs on enemies** as the fight wears on, battle max HP grows especially after box corruption, and the **indestructible box persists** even after she falls to keep her setup alive. Allies inside the box **ignore her ultimate**, turning the global pause into a controlled window for one protected partner. She demands careful **ally selection for the box** and patience to build corruption before debuffs peak on the enemy line. Teams that **punish her before corruption ramps** or exploit the global CC window blunt her upside, box value, and late-fight max HP scaling.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `average`
- **Ultimate**: speed `slow`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`

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
Common buffers are **Rowan**, **Smokey & Meerky**, or **Ravion**.

- **Thoran**
  - Energy recovery (single target, average) `signature fuel`
- **Thador**
  - Energy recovery (single target, low) `signature fuel`
- **Lyca**
  - Energy recovery (all units, low) `signature fuel`
- **Seth**
  - Energy recovery (single target, average) `signature fuel`

### Units benefitting most from Pandora

Pandora provides Direct healing to single targets `high`, Energy recovery to single targets `low`, Invincible to single targets `high`, and Max HP buff (Legendary+) to single targets `average`.

- Lily May (2.3 / 5)
- Dionel (2.2 / 5)
- Silven (2.2 / 5)

### Units that can act as a replacement for Pandora

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Evie (100% `Direct healing` `Healing`)

**Similar Skills**

- Thador (50% `enemy-debuffer` `energy-provider`)
- Cecia (50% `enemy-debuffer` `mass-cc`)
- Temesia (33% `enemy-debuffer` `mass-cc`)

**Damage**

- Faramor (100% `DoT` `HP loss`)
- Dunlingr (79% `DoT` `HP loss`)
- Contess (78% `HP loss`)

**Debuffs on enemies**

- Alna (62% `Haste debuff` `Vitality debuff`)
- Velara (50% `Haste debuff`)
- Natsu (50% `Haste debuff`)

**Crowd Control**

- Berial (100% `Frighten`)
- Silvina (100% `Frighten`)
- Daimon (80% `Frighten`)

### Summary for Pandora

#### Pandora Provides

- Invincibility — Single target

#### Damage types dealt by Pandora

- DoT — All units, Single target
- HP loss — All units — `low`

#### Debuffs provided by Pandora

- ATK — Single target — `low`
- Damage taken — Single target — `low`
- Haste — Single target — `average`
- Vitality — Single target — `average`

#### Crowd Control provided by Pandora

- Frighten — All units — `low`

## Pang

### Pang's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Sky Splitter (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-shielder` `transformation`
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Play overview

Pang channels then **bursts AoE**, entering a stance with ATK and haste where strikes **block enemy energy recovery** to stall opposing ultimates across the field. Heavy single-target hits add direct pressure, a shield keeps him **unaffected while active**, and shield break or expiry deals retaliation damage to punish focus fire on his frontline slot. Any shielded ally gains **ATK from his passive**, and entering the buff state **instantly grants shield and penetration** for an immediate power spike before the stance fully settles. Battle ATK rises over time, blending **burst damage with energy denial** once stance is online and retaliation triggers are armed. Fights that **break shields before stance** or deny melee access cut his retaliation loop, energy denial, and team ATK sharing.

#### Skill overview

- **Signature skill (ult)**: speed `average`, buffs `average`, debuffs `average`, damage `high`
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

Look for units providing: `ATK` `Haste` `Energy` `DEF Penetration`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Aliceth**
  - ATK buff (multiple targets, low)
  - DEF Penetration buff (multiple targets, high)
- **Kordan**
  - ATK buff (multiple targets, high)
  - DEF Penetration buff (multiple targets, low)
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Tasi**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Pang

Pang provides ATK buff to single targets `high`, Shield to single targets `average`, and DEF Penetration buff (Supreme+) to single targets `low`.

- Faramor (2.0 / 5)
- Lily May (2.0 / 5)
- Dionel (1.8 / 5)

### Units that can act as a replacement for Pang

**Best overall replacement**

- Hepler (83% `Damage` `Similar Skills` `Crowd Control`)
- Perseus (77% `Damage` `Crowd Control`)
- Lenya (76% `Damage` `Crowd Control`)

**Buffs on allies**

- Contess (93% `ATK` `Shield`)
- Gunnar (66% `Shield` `ATK`)
- Ravion (61% `ATK`)

**Similar Skills**

- Hepler (66% `ally-shielder` `transformation`)
- Ulmus (60% `ally-shielder` `transformation`)
- Baelran (33% `transformation`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Contess (100% `Energy recovery debuff`)
- Sinbad (100% `Energy recovery debuff`)

**Crowd Control**

- Aliceth (100% `Stun`)
- Bonnie (100% `Stun`)
- Phraesto (100% `Stun`)

### Summary for Pang

#### Pang Provides

- Transformation — Self

#### Damage types dealt by Pang

- Physical — Area, Single target
- Max HP-based damage — Area, Single target — `high`

#### Debuffs provided by Pang

- Energy recovery — Single target — `low`

#### Crowd Control provided by Pang

- Unaffected — Self — On skill
- Stun — Single target — `low`

## Parisa

### Parisa's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Floral Splendor (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Behavior tags**: `ally-buffer` `aoe-damage` `mark-target`
- **Damage types**: Magic `high`

#### Play overview

Parisa marks with flowers for **AoE ultimate damage**, then boosts **attack speed and normal attack damage** for herself and one ally to accelerate their output together. Periodic line attacks sweep after several normals, battle ATK climbs, and marks at start let normals **hit extra targets after enough stacks** accumulate on the field. Fewer normals are needed to **trigger the line attack** at higher tiers, tightening her proc rhythm in longer fights. She shines beside **another high-attack ally** who can share her speed buff. Without **frequent normal attacks** or clustered marks, her line procs stay flat.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `high`

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
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (all units, low) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
- **Lorsan**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Parisa

- Bonnie (1.7 / 5)
- Niru (1.6 / 5)
- Himmel (1.5 / 5)

### Units that can act as a replacement for Parisa

**Similar Skills**

- Perseus (66% `ally-buffer` `aoe-damage`)
- Cassadee (60% `ally-buffer` `aoe-damage`)
- Himmel (50% `ally-buffer` `aoe-damage`)

**Damage**

- Galahad (100% `Magic`)
- Saida (100% `Magic`)
- Cyran (100% `Magic`)

### Summary for Parisa

#### Parisa Provides

- Marked target (focus fire) — Area

#### Damage types dealt by Parisa

- Magic — Area

## Perseus

### Perseus's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Divine Rend (ultimate)
- **Movement**: moving (avg attack range 2.9 tiles)
- **Behavior tags**: `ally-buffer` `aoe-damage`
- **Damage types**: Physical `high`, Max HP-based damage `high`

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
Common buffers are **Twins**, **Mikola**, or **Hugin**.

Perseus also requires units **buffing them**

- **Koko**
  - Shield (all units, low)
  - Grants 5 distinct stat buffs to Perseus
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
  - Shield (single target, average)
  - Grants 6 distinct stat buffs to Perseus (start of battle)
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
  - Grants 3 distinct stat buffs to Perseus
- **Alna**
  - ATK buff (single target, low)
  - Max HP buff (single target, high)
  - Grants 4 distinct stat buffs to Perseus (start of battle)
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
  - Grants 4 distinct stat buffs to Perseus

### Units benefitting most from Perseus

Perseus provides ATK buff to multiple targets `high`, Magic DEF buff to multiple targets `average`, and Phys DEF buff to multiple targets `average`.

- Carolina (3.1 / 5)
- Shadewing (2.6 / 5)
- Silven (2.5 / 5)

### Units that can act as a replacement for Perseus

**Best overall replacement**

- Atalanta (72% `Damage` `Crowd Control`)
- Himmel (67% `Damage` `Similar Skills`)
- Florabelle (63% `Damage`)

**Similar Skills**

- Sonja (80% `ally-buffer` `aoe-damage`)
- Cassadee (80% `ally-buffer` `aoe-damage`)
- Himmel (66% `ally-buffer` `aoe-damage`)

**Damage**

- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)
- Aliceth (100% `Physical` `Max HP-based damage`)

**Crowd Control**

- Atalanta (100% `Stun` `Knock back`)
- Soren (95% `Stun` `Knock back`)
- Scarlita (94% `Stun` `Knock back`)

### Summary for Perseus

#### Damage types dealt by Perseus

- Physical — Area, Single target
- Max HP-based damage — Area, Single target — `average`

#### Crowd Control provided by Perseus

- Unaffected — Self — On skill
- Knock back — Area — `low`
- Stun — Area — `average`

## Phraesto

### Phraesto's behavior

`AFK Stages [A+]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Crimson Contract (Skill 1)
- **Movement**: moving (avg attack range 1.8 tiles)
- **Behavior tags**: `ally-buffer` `ally-shielder` `aoe-damage` `clone` `energy-provider` `summoner`
- **Ally composition**: place allies 1 tile behind this hero and the Illusion for contract buffs
- **Self placement**: keep this hero and Illusion in the same row (damage reduction and battle-start shields)
- **Damage types**: Magic `high`

#### Play overview

Phraesto sacrifices max HP to **summon an Illusion that casts all his skills**, duplicating his kit while his active ultimate **heals per nearby hit** to recover the cost over time. He and the clone **grant rear allies stat contracts**, apply DoT and reductions on strike, share DEF and cross-transfer energy on damage so both bodies stay fueled through the fight. Row allies start with **shields at battle open**, and if the Illusion dies first he **damages and stuns an enemy** for a punish window. He needs **HP to feed the clone** and allies behind him positioned to honor contracts and benefit from rear buffs. Losing the Illusion early or **denying rear positioning** shrinks his buff, duplication value, and sustain loop across the fight.

#### Skill overview

- **Signature skill**: speed `slow`, first cast speed `fast`, buffs `average`, damage `low`
- **Ultimate**: speed `average`, damage `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `high`

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

Look for units providing: `Shield` `Healing` `Energy` `Physical DEF` `Magic DEF`  
Common buffers are **Solise**, **Twins**, or **Hugin**.

- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)
  - Shield (summons only, low)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Saida**
  - Shield (multiple targets, high)
- **Contess**
  - Shield (single target, average)
  - Direct healing (single target, high)
- **Zanie**
  - Shield (single target, average)
  - Direct healing (single target, high)

### Units benefitting most from Phraesto

Phraesto provides Damage taken to single targets `low`, Max HP buff to single targets `low`, and Shield to single targets `average`.

- Daimon (2.7 / 5)

### Units that can act as a replacement for Phraesto

**Best overall replacement**

- Hepler (65% `Crowd Control` `Buffs on allies`)
- Gunnar (61% `Buffs on allies` `Debuffs on enemies`)

**Buffs on allies**

- Gunnar (100% `Shield`)
- Contess (100% `Shield`)
- Saida (100% `Shield`)

**Similar Skills**

- Galahad (50% `ally-shielder` `aoe-damage` `clone`)
- Twins (42% `ally-buffer` `ally-shielder` `energy-provider`)
- Gunnar (36% `ally-shielder` `aoe-damage`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Gunnar (100% `Vitality debuff`)
- Frieren (100% `Vitality debuff`)
- Alna (100% `Vitality debuff`)

**Crowd Control**

- Hepler (100% `Stun` `Taunt`)
- Antandra (100% `Stun` `Taunt`)
- Callan (60% `Stun`)

### Summary for Phraesto

#### Phraesto Provides

- Summoning — Self

#### Damage types dealt by Phraesto

- Magic — Area, Single target
- DoT — Single target

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
- **Damage types**: Magic `average`, Max HP-based damage `high`, True damage `low`

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
Common buffers are **Twins**, **Hugin**, or **Damian**.

- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
- **Tasi**
  - Haste buff (single target, high) `signature fuel`
- **Vala**
  - Haste buff (single target, high) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Dunlingr**
  - Haste buff (single target, average) `signature fuel`

### Units benefitting most from Pippa

- Carolina (3.1 / 5)
- Nerion (2.3 / 5)
- Shadewing (1.9 / 5)

### Units that can act as a replacement for Pippa

**Best overall replacement**

- Saida (63% `Damage` `Debuffs on enemies` `Crowd Control`)
- Sylphira (58% `Damage`)
- Lily May (50% `Debuffs on enemies`)

**Similar Skills**

- Silven (40% `hp-scaling`)
- Nazrik (40% `hp-scaling`)
- Marilee (40% `hp-scaling`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage` `True damage`)
- Sylphira (100% `Magic` `Max HP-based damage` `True damage`)
- Athalia (84% `Max HP-based damage` `True damage`)

**Debuffs on enemies**

- Saida (100% `Energy drain`)
- Dunlingr (100% `Energy drain`)
- Lily May (100% `Energy drain`)

**Crowd Control**

- Eironn (98% `Bind` `Displace`)
- Saida (93% `Bind` `Displace`)
- Arden (92% `Bind`)

### Summary for Pippa

#### Damage types dealt by Pippa

- Magic — Single target
- Max HP-based damage — Single target — `high`
- True damage — Area — `low`

#### Debuffs provided by Pippa

- Energy drain — Single target — `average`

#### Crowd Control provided by Pippa

- Unaffected — Self — On skill
- Bind — Area — `average`
- Displace — Single target — `low`
- Knock down — Single target — `low`

## Ravion

### Ravion's behavior

`AFK Stages [A+]`, `Dream Realm [A+]`, `Dream Realm (Endless) [A]`, `PVP [A]`

- **Signature skill**: Killer Flush (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-shielder` `energy-provider` `self-repositioner`
- **Ally composition**: Objectives go to the 2 rearmost allies; backline heroes receive ATK and Energy on completion
- **Damage types**: Physical `low`, HP loss `low`, Max HP-based damage `average`

#### Play overview

Ravion assigns **objectives to allies**; completing them grants energy, ATK, and unlocks a knock-down strike for coordinated burst windows across the fight. His ultimate **scales with target HP-loss** across multi-hits, while repeated teleports **deal early jump damage** then reposition away from foes to stay safe through longer engagements. First enhanced strike **activates ATK bonus**, and unlocking it permanently **grants haste and ATK to self and allies** for a lasting team spike. Assigned tasks also give brief ATK boost and unaffected state while allies work objectives across the board. He needs **allies who finish objectives** and room to teleport safely through longer engagements. **Static teams or burst that pins him** before enhanced strikes land waste his coordination package and team buffs.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `average`

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
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Galahad**
  - Haste buff (single target, average) `signature fuel`
- **Mehira**
  - Haste buff (single target, low) `signature fuel`
- **Velara**
  - Haste buff (single target, low) `signature fuel`
- **Thador**
  - Energy recovery (single target, low) `signature fuel`
- **Kazim**
  - ATK buff (single target, high)
  - Haste buff (multiple targets, average) `signature fuel`

### Units benefitting most from Ravion

Ravion provides ATK buff to multiple targets `high`, Energy recovery to multiple targets `average`, Lifedrain buff (EX+10) to single targets `low` — conditional (rare), and Shield (EX+10) to single targets `low` — conditional (rare).

**22** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Arden (4.9 / 5)
- Valen (4.9 / 5)
- Hewynn (4.6 / 5)
- Cryonaia (4.2 / 5)
- Nara (3.8 / 5)
- Kordan (3.6 / 5)
- Shadewing (3.4 / 5)
- Dionel (2.7 / 5)
- Sylphira (2.5 / 5)
- Mikola (2.5 / 5)

### Units that can act as a replacement for Ravion

**Buffs on allies**

- Pang (68% `ATK`)
- Contess (57% `ATK`)
- Evie (57% `ATK`)

**Similar Skills**

- Thador (60% `ally-shielder` `energy-provider`)
- Hugin (50% `ally-shielder` `energy-provider`)
- Twins (40% `ally-shielder` `energy-provider`)

**Damage**

- Mehira (100% `Max HP-based damage` `HP loss`)
- Athalia (100% `Physical` `Max HP-based damage` `HP loss`)
- Zorya (100% `Max HP-based damage` `HP loss`)

**Debuffs on enemies**

- Zanie (100% `Phys DEF debuff` `ATK debuff`)
- Lyca (100% `Phys DEF debuff` `ATK debuff`)
- Kruger (90% `Phys DEF debuff`)

**Crowd Control**

- Cyran (100% `Displace` `Knock down`)
- Eironn (100% `Displace`)
- Mehira (87% `Displace`)

### Summary for Ravion

#### Damage types dealt by Ravion

- Physical — Area, Single target
- HP loss — Single target — `low`
- Max HP-based damage — Single target — `average`

#### Debuffs provided by Ravion

- ATK — Single target — `low`
- Phys DEF — Single target — `high`

#### Crowd Control provided by Ravion

- Unaffected — Self — On skill
- Displace — Area — `low`
- Knock down — Single target — `low`

## Reinier

### Reinier's behavior

`AFK Stages [B]`, `Dream Realm [S]`, `Dream Realm (Endless) [A]`, `PVP [B]`

- **Signature skill**: Dynamic Balance (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `disabler` `enemy-grouping`
- **Ally composition**: symmetrical ally-enemy tile pairs at battle start for Dynamic Balance swaps
- **Damage types**: Magic `average`

#### Play overview

Reinier swaps **symmetrical ally-enemy positions at battle start**, disrupting enemy lines before the first cast, then can **remove himself and one foe** from the field with his ultimate dimension trip for a temporary duel outside the main fight. Multi-hit attacks **knock targets airborne**, swaps **boost ally ATK or cut enemy ATK**, wound swapped enemies to take more damage, and grant damage reduction to a swapped ally for survivability. Symmetrical allies also gain **ATK while holding position**, rewarding clean mirror setups when enemy layout matches yours across the board. He is devastating when **enemy layout mirrors yours** for clean swaps, wound chains, and dimension removal on a high-value target. Misaligned formations or **targets immune to displacement** negate his opener, wound setups, and the dimension removal that defines his late-fight control.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, heal `average`
- **Ultimate**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, debuffs `average`, damage `average`

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

Look for units providing: `Healing`  
Common buffers are **Solise**, **Twins**, or **Smokey & Meerky**.

- **Contess**
  - Direct healing (single target, high)
- **Zanie**
  - Direct healing (single target, high)
- **Velara**
  - Direct healing (area, low)
- **Himmel**
  - Direct healing (single target, low)
- **Hewynn**
  - Healing over time (all units, high)

### Units benefitting most from Reinier

Reinier provides ATK buff (Legendary+) to single targets `low`.

- Bonnie (2.2 / 5)
- Himmel (1.7 / 5)
- Indris (1.6 / 5)

### Units that can act as a replacement for Reinier

**Best overall replacement**

- Contess (53% `Buffs on allies` `Debuffs on enemies`)

**Buffs on allies**

- Gunnar (100% `ATK`)
- Contess (100% `ATK`)
- Frieren (100% `ATK`)

**Similar Skills**

- Lucca (33% `disabler`)
- Pippa (33% `enemy-grouping`)
- Indris (33% `disabler`)

**Damage**

- Frieren (100% `Magic`)
- Galahad (100% `Magic`)
- Mehira (100% `Magic`)

**Debuffs on enemies**

- Contess (100% `Damage taken debuff` `ATK debuff`)
- Pandora (100% `ATK debuff` `Damage taken debuff`)
- Sinbad (90% `ATK debuff` `Damage taken debuff`)

**Crowd Control**

- Nara (70% `Displace` `Knock down` `Knock up`)
- Saida (60% `Displace` `Interrupt`)
- Ravion (60% `Displace` `Knock down`)

### Summary for Reinier

#### Damage types dealt by Reinier

- Magic — Multiple targets, Single target

#### Debuffs provided by Reinier

- ATK (Legendary+) — Single target — `low`
- Damage taken (Mythic+) — Single target — `low`

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
- **Behavior tags**: `aoe-damage` `fire-attack` `self-repositioner`
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Play overview

Rhys **moves while attacking**, loading **Blast Ammo** on ultimate to enhance follow-up normals into area shots that hit multiple tiles across the field. Control immunity and crit **trigger when he takes CC**, knockback clears nearby foes, and crit damage **scales with equipped splash shots** as he kites away from melee pressure on the board. Movement loads splash shots for enhanced area attacks, and immunity skill **cooldown drops** for faster recovery between control windows so he can re-engage safely. He needs **space to kite** and time to load ammo between bursts for maximum splash output on grouped targets throughout the fight. **Pinned melee lines** or fights without movement deny his splash scaling, crit ramp, and the ammo-enhanced normals that carry his sustained damage through longer trades on the field.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `average`

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
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Lorsan**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Tasi**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Pandora**
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Rhys

Rhys provides Crit buff to single targets `low` and Movement speed buff (Mythic+) to single targets `high`.

- Nazrik (5.0 / 5)

### Units that can act as a replacement for Rhys

**Best overall replacement**

- Atalanta (78% `Damage` `Crowd Control` `Similar Skills`)
- Perseus (71% `Damage` `Crowd Control`)
- Soren (69% `Damage` `Crowd Control`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Himmel (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)

**Similar Skills**

- Dionel (60% `aoe-damage` `self-repositioner`)
- Atalanta (60% `aoe-damage` `self-repositioner`)
- Himmel (50% `aoe-damage` `self-repositioner`)

**Damage**

- Baelran (100% `Physical` `Max HP-based damage`)
- Galahad (100% `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Crowd Control**

- Twins (100% `Knock back`)
- Aliceth (100% `Knock back`)
- Kordan (100% `Knock back`)

### Summary for Rhys

#### Damage types dealt by Rhys

- Physical — All units, Arc, Single target
- Max HP-based damage — All units — `high`

#### Crowd Control provided by Rhys

- Immune — Single target — Conditional
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
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `high`

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

Look for units providing: `Haste` `Max HP` `Healing` `Energy` `Physical DEF`  
Common buffers are **Twins**, **Smokey & Meerky**, or **Solise**.

- **Marcille**
  - Haste buff (single target, low) `signature fuel`
  - Direct healing (multiple targets, high)
- **Koko**
  - Direct healing (all units, average)
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, average)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Zanie**
  - Max HP buff (single target, high)
  - Direct healing (single target, high)

### Units benefitting most from Rowan

Rowan provides Direct healing in an area `low` and Energy recovery in an area `high`.

**27** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Arden (5.0 / 5)
- Valen (5.0 / 5)
- Berial (4.8 / 5)
- Vala (3.1 / 5)
- Koko (3.1 / 5)
- Soren (3.0 / 5)
- Fay (3.0 / 5)
- Lorsan (2.7 / 5)
- Zorya (2.6 / 5)
- Lenya (2.6 / 5)

### Units that can act as a replacement for Rowan

**Best overall replacement**

- Pandora (55% `Healing` `Energy provider`)
- Fay (51% `Healing`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Twins (100% `Direct healing` `Healing`)

**Similar Skills**

- Twins (60% `ally-healer` `energy-provider`)
- Fay (48% `ally-healer`)
- Ludovic (40% `ally-healer`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Saida (100% `Energy drain`)
- Dunlingr (100% `Energy drain`)
- Lily May (100% `Energy drain`)

### Summary for Rowan

#### Rowan Provides

- Energy steal — Single target

#### Damage types dealt by Rowan

- Magic — Single target

#### Debuffs provided by Rowan

- Energy drain — Single target — `average`

## Saida

### Saida's behavior

`AFK Stages [S+]`, `Dream Realm [A]`, `Dream Realm (Endless) [A]`, `PVP [S]`

- **Signature skill**: Seed Siphon (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-shielder` `cheat-death` `life-drain`
- **Damage types**: Magic `high`, DoT `low`, Max HP-based damage `high`

#### Play overview

Saida teleports to an enemy, planting a **marker that deals periodic damage and drains energy** to soften and stall the target over time. Damage dealt **heals her with excess becoming shield**, strikes **trigger nearby markers on the target**, and she can **consume a marker to revive** after defeat for a second life in longer fights on the board. Damage reduction grows with active markers, each ultimate **shortens marker DoT interval**, and battle start plants markers on nearby allies to seed the field early. She blends sustain, **energy drain, and cheat-death** when markers stay live across the fight and allies keep hers planted on the board. Teams that **clear markers or burst her before planting** deny her shield loop, revival safety, and the damage reduction scaling that keeps her standing through focused burst damage.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `high`

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

Look for units providing: `Max HP` `Healing`  
Common buffers are **Solise**, **Twins**, or **Smokey & Meerky**.

- **Contess**
  - Direct healing (single target, high)
- **Velara**
  - Direct healing (area, low)
- **Himmel**
  - Direct healing (single target, low)
- **Hewynn**
  - Healing over time (all units, high)
- **Koko**
  - Direct healing (all units, average)

### Units benefitting most from Saida

Saida provides Shield to multiple targets `high`.

- Silvina (5.0 / 5)
- Daimon (4.4 / 5)
- Gerda (4.4 / 5)
- Kruger (4.0 / 5)
- Eironn (3.4 / 5)
- Shadewing (3.2 / 5)
- Thador (3.0 / 5)
- Shemira (2.4 / 5)

### Units that can act as a replacement for Saida

**Best overall replacement**

- Galahad (54% `Damage` `Crowd Control`)
- Lily May (51% `Damage` `Debuffs on enemies`)

**Similar Skills**

- Thoran (50% `cheat-death` `life-drain`)
- Brutus (33% `cheat-death` `life-drain`)
- Harak (28% `life-drain`)

**Damage**

- Galahad (100% `Magic` `Max HP-based damage`)
- Sylphira (100% `Magic` `Max HP-based damage`)
- Cryonaia (100% `Magic` `DoT` `Max HP-based damage`)

**Debuffs on enemies**

- Lily May (62% `Energy drain`)

**Crowd Control**

- Eironn (86% `Bind` `Displace`)
- Evie (86% `Bind` `Displace`)
- Cecia (80% `Bind`)

### Summary for Saida

#### Saida Provides

- Cheat death — Self

#### Damage types dealt by Saida

- Magic — All units, Area, Single target
- DoT — Single target
- Max HP-based damage — Single target — `high`

#### Debuffs provided by Saida

- Energy drain — Single target — `high`
- Damage dealt (Mythic+) — Single target — `low`

#### Crowd Control provided by Saida

- Unaffected — Self — On skill
- Bind — All units — `low`
- Displace — Single target — `low`
- Interrupt — Single target — `low`

## Salazer

### Salazer's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Spirit Shackles (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `disabler` `execute` `life-drain`
- **Damage types**: Physical `high`

#### Play overview

Salazer summons **flying swords** on ultimate while arc strikes **add bonus hits on low-HP targets** for finisher pressure against wounded marks. He deals **massive damage and imprisons** very low foes, gains battle damage reduction, and at battle start or after imprison **arc skill has no cooldown** with a guaranteed extra use for chained finishers. Imprisoning also **heals himself**, keeping him in the fight through execute windows when victims are caged. He is a **finisher who chains arcs** once a victim is imprisoned and the team has softened HP totals across the line. Without **wounded targets** or early imprison windows, his reset loop, bonus hits, and self-heal on cage never activate.

#### Skill overview

- **Signature skill**: speed `fast`, damage `average`
- **Ultimate**: speed `average`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `high`

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

Look for units providing: `Max HP` `Shield` `Healing` `Life Drain`  
Common buffers are **Solise**, **Twins**, or **Smokey & Meerky**.

- **Koko**
  - Shield (all units, low)
  - Direct healing (all units, average)
  - Lifedrain buff (multiple targets, average)
- **Hepler**
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
- **Hewynn**
  - Healing over time (all units, high)
- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
  - Direct healing (single target, high)
- **Dunlingr**
  - Lifedrain buff (all units, average)

### Units benefitting most from Salazer

Salazer provides Lifedrain buff to single targets `average` and Shield (Supreme+) to single targets `high` — conditional (frequent).

- Shadewing (2.4 / 5)
- Nerion (2.0 / 5)
- Dionel (1.6 / 5)

### Units that can act as a replacement for Salazer

**Best overall replacement**

- Cecia (75% `Damage` `Crowd Control`)
- Kordan (64% `Damage` `Crowd Control`)
- Nara (62% `Damage`)

**Buffs on allies**

- Saida (100% `Shield`)
- Hugin (96% `Shield`)
- Hepler (96% `Shield`)

**Similar Skills**

- Harak (60% `execute` `life-drain`)
- Sylphira (48% `disabler` `life-drain`)
- Odie (30% `execute`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Crowd Control**

- Eironn (100% `Bind`)
- Kordan (100% `Bind`)
- Evie (100% `Bind`)

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
- **Behavior tags**: `dot-specialist` `fire-attack` `hp-scaling` `invincibility` `life-drain`
- **Damage types**: Magic `high`, Max HP-based damage `low`

#### Play overview

Satrana goes **invincible during ultimate** while dealing continuous AoE, then arc attacks with **life drain** and Sparks that **ignite enemies for Vitality cuts and DoT** shared with allies. Battle damage reduction helps her stand through the burn setup, ignited foes **lower magic damage taken** for her team, and when all enemies burn her strike **has no cooldown limit**. She peaks once **ignites spread across the line** and her team can exploit the magic mitigation. **Cleanse or short fights** before full ignite leave her cooldown relief inactive.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `low`

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

Look for units providing: `Max HP` `Life Drain`

- **Dunlingr**
  - Lifedrain buff (all units, average)
- **Zandrok**
  - Max HP buff (multiple targets, average)
  - Lifedrain buff (area, low, conditional (frequent))
- **Koko**
  - Lifedrain buff (multiple targets, average)
- **Brutus**
  - Lifedrain buff (single target, average)
- **Daimon**
  - Lifedrain buff (single target, average)

### Units benefitting most from Satrana

Satrana provides Magic damage amplification (Mythic+) to single targets `average` and Damage taken (EX+10) to single targets `low`.

- Bonnie (2.6 / 5)
- Shadewing (2.2 / 5)
- Indris (1.9 / 5)

### Units that can act as a replacement for Satrana

**Similar Skills**

- Zorya (48% `hp-scaling` `life-drain`)
- Mirael (40% `dot-specialist` `fire-attack`)
- Shemira (33% `hp-scaling` `life-drain`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Mehira (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Sinbad (73% `Vitality debuff`)
- Frieren (69% `DoT` `Vitality debuff`)
- Alna (60% `Vitality debuff`)

**Crowd Control**

- Mehira (100% `Charm`)

### Summary for Satrana

#### Satrana Provides

- Ally grant (Sparks) — Area
- Invincibility — Self

#### Damage types dealt by Satrana

- Magic — Area, Single target
- Max HP-based damage — Single target — `low`

#### Debuffs provided by Satrana

- DoT — Multiple targets — `low`
- Vitality — Multiple targets — `low`

#### Crowd Control provided by Satrana

- Charm — Single target — `average`

## Scarlita

### Scarlita's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Divine Wrath (Mythic+)
- **Movement**: moving (brief reposition)
- **Behavior tags**: `ally-shielder` `aoe-damage` `hp-scaling`
- **Damage types**: Physical `high`

#### Play overview

Scarlita slashes the ground to **send a wave that knocks foes to the edge**, then charges to **knock down survivors** for a two-step displacement combo across the battlefield. Airborne charges **build power for landing AoE stun**, weakest allies gain shields while she is airborne, and each shield sent **stacks execution potential** for later burst. Enough living allies let her **deal true damage**, and shielded allies also gain Phys and Magic DEF from her protection during air time. She needs **clustered enemies for the wave** and air time to charge before landing on grouped targets across the battlefield. **Sparse formations or burst that grounds her early** waste her knockdown follow-through, execution stacks, and true damage payoff.

#### Skill overview

- **Signature skill**: speed `fast`
- **Ultimate**: speed `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `high`

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
Common buffers are **Ravion**, **Rowan**, or **Smokey & Meerky**.

- **Thoran**
  - Energy recovery (single target, average) `signature fuel`
- **Pandora**
  - Energy recovery (single target, low) `signature fuel`
- **Thador**
  - Energy recovery (single target, low) `signature fuel`
- **Lyca**
  - Energy recovery (all units, low) `signature fuel`
- **Seth**
  - Energy recovery (single target, average) `signature fuel`

### Units benefitting most from Scarlita

Scarlita provides Shield to single targets `low` and DEF buff (Supreme+) to single targets `low`.

- Carolina (3.1 / 5)
- Kazim (2.9 / 5)
- Nerion (2.5 / 5)

### Units that can act as a replacement for Scarlita

**Best overall replacement**

- Korin (58% `Similar Skills` `Buffs on allies`)

**Buffs on allies**

- Zanie (100% `Shield`)
- Korin (100% `Shield`)
- Gunnar (96% `Shield`)

**Similar Skills**

- Korin (80% `ally-shielder` `hp-scaling`)
- Zandrok (60% `aoe-damage` `hp-scaling`)
- Galahad (50% `ally-shielder` `aoe-damage`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Crowd Control**

- Soren (69% `Stun` `Knock back`)
- Lucca (67% `Stun` `Knock up` `Knock down`)
- Zorya (64% `Stun` `Knock down`)

### Summary for Scarlita

#### Scarlita Provides

- Invincibility — Self

#### Damage types dealt by Scarlita

- Physical — All units, Arc, Area

#### Crowd Control provided by Scarlita

- Unaffected — Self — Conditional
- Knock back — All units — `low`
- Knock down — Arc — `low`
- Knock up — Area — `low`
- Stun — Area — `average`

## Seth

### Seth's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Shadow Strike (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `assassin` `life-drain`
- **Damage types**: Physical `average`, HP loss `average`

#### Play overview

Seth flashes to a foe for **multi-hit ultimate damage**, then pounces on the **weakest nearby enemy** for repeated assassin pressure between casts. Low enemy HP **grants stat bonuses**, battle ATK rises, and each non-summon defeat **resets pounce cooldown and refunds energy** to chain kills across the fight. Pounce also **shreds extra Phys DEF** when he carries a specific buff, opening tankier targets for follow-up from allies. He chains **assassin resets** in fights with frequent kills and accessible weak marks on the board. Without **finishes or accessible weak targets**, his pounce loop and stat spikes stall out before he can snowball through the enemy line in longer fights.

#### Skill overview

- **Signature skill (ult)**: speed `average`, heal `average`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `average`

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

Look for units providing: `ATK` `Haste` `CRIT` `Healing` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Tilaya**
  - DEF buff (area, high)
  - DEF buff (area, high)
- **Dunlingr**
  - ATK buff (single target, low)
  - Haste buff (single target, average) `signature fuel`
  - Lifedrain buff (all units, average)
  - ATK SPD buff (all units, low) `signature fuel`
- **Koko**
  - Direct healing (all units, average)
  - Lifedrain buff (multiple targets, average)
- **Lucca**
  - DEF buff (area, average)
  - DEF buff (area, average)
- **Hewynn**
  - Healing over time (all units, high)

### Units benefitting most from Seth

Seth provides Energy recovery (EX+10) to single targets `average`.

- Nerion (1.5 / 5)
- Zorya (1.4 / 5)
- Silven (1.3 / 5)

### Units that can act as a replacement for Seth

**Best overall replacement**

- Ravion (74% `Damage` `Debuffs on enemies` `Buffs on allies` `Energy provider`)
- Harak (68% `Damage` `Similar Skills`)
- Athalia (55% `Damage`)

**Buffs on allies**

- Ravion (100% `Energy`)
- Smokey & Meerky (100% `Energy`)
- Rowan (100% `Energy`)

**Similar Skills**

- Harak (80% `assassin` `life-drain`)
- Shakir (40% `life-drain`)
- Kruger (40% `life-drain`)

**Damage**

- Aliceth (100% `Physical` `Max HP-based damage` `HP loss`)
- Faramor (100% `Physical` `HP loss`)
- Athalia (100% `Physical` `HP loss` `Max HP-based damage`)

**Debuffs on enemies**

- Velara (100% `Phys DEF debuff`)
- Thador (100% `Phys DEF debuff`)
- Shadewing (100% `Phys DEF debuff`)

**Crowd Control**

- Galahad (100% `Bind`)
- Saida (100% `Bind`)
- Velara (100% `Bind`)

### Summary for Seth

#### Seth Provides

- Invincibility — Single target
- Stacking buff — Single target

#### Damage types dealt by Seth

- Physical — Single target
- HP loss — Single target — `average`

#### Debuffs provided by Seth

- Phys DEF (Supreme+) — Single target — `low`

#### Crowd Control provided by Seth

- Bind — Single target — `low`

## Shadewing

### Shadewing's behavior

`AFK Stages [A+]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [S]`

- **Signature skill**: Withering Curse (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `dot-specialist` `enemy-debuffer`
- **Damage types**: Magic `low`, DoT `low`, HP loss `low`

#### Play overview

Shadewing applies **sustained DoT scaling on target lost HP** with his ultimate, then dual strikes plus **wound DoT** while converting enemy damage taken into **curse value for a heavy lash** at threshold. Battle ATK climbs, trigger hits **build energy and permanent damage**, and at start he **drains ally HP for lasting ATK and shield** to front-load his scaling. He needs **allies willing to pay the opening HP cost** and sustained damage across the team to fill curse quickly enough for the lash to land on priority targets in longer fights. **Short fights or allies that cannot spare HP** blunt his scaling lash, energy buildup, and self-buff loop across longer fights on the board.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`
- **Ultimate**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `low`

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

Look for units providing: `ATK` `Shield` `Energy` `Life Drain`  
Common buffers are **Ravion**, **Hugin**, or **Twins**.

Shadewing also requires units **dealing continuous damage** to enemies and/or units **putting debuffs** on enemies

- **Alna**
  - ATK buff (single target, low)
  - Enables Debuff on target via Haste debuff (all units)
  - Enables Continuous damage on enemies via DoT
- **Frieren**
  - ATK buff (single target, high)
  - Enables Debuff on target via DoT (area)
  - Enables Continuous damage on enemies via DoT + Burn
- **Saida**
  - Shield (multiple targets, high)
  - Enables Debuff on target via Energy drain (single target)
  - Enables Continuous damage on enemies via DoT
- **Gunnar**
  - ATK buff (single target, high)
  - Shield (single target, average)
  - Enables Debuff on target via Healing debuff (area)
  - Enables Continuous damage on enemies via DoT
- **Aliceth**
  - ATK buff (multiple targets, low)
  - Enables Debuff on target via Marked target (focus fire) (multiple targets)
  - Enables Continuous damage on enemies via tick damage

### Units benefitting most from Shadewing

- Bonnie (2.3 / 5)
- Indris (1.6 / 5)

### Units that can act as a replacement for Shadewing

**Similar Skills**

- Nerion (96% `dot-specialist` `enemy-debuffer`)
- Kruger (40% `enemy-debuffer`)
- Odie (33% `dot-specialist`)

**Damage**

- Mehira (100% `Magic` `DoT` `HP loss`)
- Dunlingr (100% `Magic` `DoT` `HP loss`)
- Niru (100% `Magic` `HP loss`)

**Debuffs on enemies**

- Thador (100% `Magic DEF debuff` `Phys DEF debuff`)
- Eironn (100% `Magic DEF debuff`)
- Sinbad (100% `Magic DEF debuff` `Phys DEF debuff`)

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

- Magic DEF — Single target — `average`
- Phys DEF — Single target — `low`

## Shakir

### Shakir's behavior

`AFK Stages [A]`, `Dream Realm [B]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Ravaging Claws (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `life-drain` `transformation`
- **Damage types**: Physical `high`

#### Play overview

Shakir **transforms into Wolf Form** to reshape his combat kit, trading single-target strikes for **frontal AoE cleaves** and sustained pressure. In form he gains **Ranged DEF and Life Drain**, helping him survive ranged fire while staying on enemies. His **damage reduction scales with aura allies**, so he peaks when teammates cluster inside his influence zone. A lower **energy threshold sustains transformation** longer, keeping wolf pressure online through extended fights. Third hit also **shaves enemy vitality**, softening targets for follow-up damage. Against **spread lines** or teams that deny his landing zone, wolf uptime and aura scaling stall out.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, buffs `average`, debuffs `average`, damage `high`
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
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, average)
- **Dunlingr**
  - Haste buff (single target, average) `signature fuel`
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
- **Marcille**
  - Haste buff (single target, low) `signature fuel`
- **Mehira**
  - Haste buff (single target, low) `signature fuel`

### Units benefitting most from Shakir

Shakir provides Damage taken to multiple targets `average`, Haste buff to multiple targets `average`, and Lifedrain buff to single targets `low`.

- Lucy (3.4 / 5)
- Sinbad (3.2 / 5)
- Atalanta (3.0 / 5)
- Pang (2.9 / 5)
- Mikola (2.8 / 5)
- Dionel (2.7 / 5)
- Korin (2.7 / 5)
- Lenya (2.6 / 5)
- Sonja (2.2 / 5)

### Units that can act as a replacement for Shakir

**Buffs on allies**

- Zandrok (58% `Haste` `Life Drain`)
- Tasi (50% `Haste`)
- Lorsan (50% `Haste`)

**Similar Skills**

- Sylphira (50% `life-drain` `transformation`)
- Kruger (48% `life-drain`)
- Zorya (40% `life-drain`)

**Damage**

- Baelran (100% `Physical`)
- Himmel (100% `Physical`)
- Aliceth (100% `Physical`)

**Debuffs on enemies**

- Alna (100% `Haste debuff` `Vitality debuff`)
- Dunlingr (100% `Haste debuff` `Vitality debuff`)
- Pandora (100% `Haste debuff` `Vitality debuff`)

### Summary for Shakir

#### Shakir Provides

- Transformation — Self

#### Damage types dealt by Shakir

- Physical — Area, Single target

#### Debuffs provided by Shakir

- Haste — Multiple targets — `low`
- Vitality (Supreme+) — Single target — `low`

#### Crowd Control provided by Shakir

- Unaffected — Self — Form

## Shemira

### Shemira's behavior

`AFK Stages [A+]`, `Dream Realm [S+]`, `Dream Realm (Endless) [A]`, `PVP [A+]`

- **Signature skill**: Phantom Procession (ultimate)
- **Movement**: mostly stationary (avg attack range 4.0 tiles)
- **Behavior tags**: `high-damage-ult` `hp-scaling` `life-drain`
- **Damage types**: Magic `high`, Max HP-based damage `high`

#### Play overview

Shemira **sacrifices HP to fuel damage**, firing orb lines and AoE bursts as her health pool shrinks. She **summons ghosts** to bombard random enemies, and each hero defeat **spawns an extra summon** to widen pressure. Energy recovery from attacks **scales with summon count**, rewarding teams that keep bodies on the field. When summons expire, **remaining power converts to all-enemy damage** for a closing burst. She needs **healing to cycle sacrifices** safely. Without sustain or summons, her HP costs leave her exposed quickly.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, heal `average`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`

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

Look for units providing: `Shield` `Healing` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Solise**.

- **Saida**
  - Shield (multiple targets, high)
- **Contess**
  - Shield (single target, average)
  - Direct healing (single target, high)
- **Galahad**
  - Shield (single target, average)
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Velara**
  - Direct healing (area, low)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Himmel**
  - Shield (single target, average)
  - Direct healing (single target, low)

### Units benefitting most from Shemira

- Bonnie (2.0 / 5)
- Shadewing (1.9 / 5)
- Himmel (1.5 / 5)

### Units that can act as a replacement for Shemira

**Best overall replacement**

- Sylphira (68% `Damage` `Debuffs on enemies`)
- Zorya (62% `Damage` `Similar Skills`)
- Nazrik (56% `Damage` `Debuffs on enemies`)

**Similar Skills**

- Zorya (80% `hp-scaling` `life-drain`)
- Satrana (33% `hp-scaling` `life-drain`)
- Silven (30% `hp-scaling`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Baelran (100% `Max HP debuff`)
- Alna (100% `Max HP debuff`)
- Sylphira (100% `Max HP debuff`)

### Summary for Shemira

#### Damage types dealt by Shemira

- Magic — Area, Single target
- Max HP-based damage — Area, Single target — `high`

#### Debuffs provided by Shemira

- Max HP (EX+10) — Single target — `low`

## Silven

### Silven's behavior

`AFK Stages [S]`, `Dream Realm [S]`, `Dream Realm (Endless) [A+]`, `PVP [A]`

- **Signature skill**: Gravity Collapse (Skill 1)
- **Movement**: stationary (avg attack range 12.0 tiles)
- **Behavior tags**: `hp-scaling` `mark-target`
- **Damage types**: Magic `high`, Max HP-based damage `high`

#### Play overview

Silven builds damage around **flying blade summons** and marks that detonate when she knocks foes down. Her ultimate launches **blade volleys** at enemies, while a field skill **enhances blade output** for sustained AoE pressure. Receiving ally buffs grants her **energy, penetration, and ATK SPD**, so she rewards supportive teammates. She deals **bonus damage to high-HP-ratio targets**, making her strong against bulky frontliners. Battle **ATK speed growth** adds steady personal scaling over long fights. Against **immune or unmarked targets**, her detonation chain and blade field underdeliver.

#### Skill overview

- **Signature skill**: speed `fast`, damage `high`
- **Ultimate**: speed `fast`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `high`

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
Common buffers are **Twins**, **Hugin**, or **Solise**.

Silven also requires units **buffing them**

- **Gunnar**
  - ATK SPD buff (single target, low) `signature fuel`
  - Grants 6 distinct stat buffs to Silven (start of battle)
- **Contess**
  - Grants 4 distinct stat buffs to Silven
- **Himmel**
  - Grants 3 distinct stat buffs to Silven
- **Saida**
  - Grants 1 distinct stat buff to Silven
- **Galahad**
  - ATK SPD via Haste buff (single target, average) `signature fuel`
  - Grants 2 distinct stat buffs to Silven

### Units benefitting most from Silven

Silven provides DEF Penetration buff (Mythic+) to single targets `low`.

- Carolina (1.8 / 5)
- Bonnie (1.7 / 5)
- Nerion (1.6 / 5)

### Units that can act as a replacement for Silven

**Best overall replacement**

- Sylphira (63% `Damage` `Crowd Control`)
- Zorya (58% `Damage` `Crowd Control`)
- Nazrik (58% `Damage` `Similar Skills`)

**Buffs on allies**

- Aliceth (100% `DEF Penetration`)
- Kordan (100% `DEF Penetration`)
- Kulu (100% `DEF Penetration`)

**Similar Skills**

- Nazrik (100% `hp-scaling` `mark-target`)
- Aliceth (48% `hp-scaling` `mark-target`)
- Vala (48% `hp-scaling` `mark-target`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Crowd Control**

- Baelran (100% `Knock down`)
- Sylphira (100% `Knock down`)
- Cyran (100% `Knock down`)

### Summary for Silven

#### Damage types dealt by Silven

- Magic — Single target
- Max HP-based damage — Single target — `high`

#### Crowd Control provided by Silven

- Knock down — Single target — `average`

## Silvina

### Silvina's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: First Strike (Skill 1)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `assassin` `battle-start-burst` `disabler` `mark-target`
- **Damage types**: Physical `average`, Max HP-based damage `high`

#### Play overview

Silvina opens by **dashing to the closest symmetrical enemy**, landing burst damage before normal pacing resumes. At battle start she swaps to **rapid strikes** briefly and gains a shield for early survivability. Her ultimate strikes the **highest-energy enemy**, dealing damage and **draining their energy** to disrupt casters before they can fire. Battle crit growth adds finishing pressure, and rapid hits **reduce target vitality** for softer kills. She excels as an **opening assassin** who punishes backline energy hoarders and symmetrical formations. She falters when symmetrical targets are absent, when burst windows end before she reaches priority foes, or when enemies deny her opening dash entirely.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, damage `average`
- **Ultimate**: speed `fast`, debuffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `average`

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
Common buffers are **Hugin** or **Twins**.

- **Hepler**
  - Shield (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)
- **Lucius**
  - Shield (area, average)
- **Koko**
  - Shield (all units, low)
- **Contess**
  - Shield (single target, average)

### Units benefitting most from Silvina

- Carolina (3.1 / 5)
- Nerion (2.3 / 5)
- Indris (1.6 / 5)

### Units that can act as a replacement for Silvina

**Best overall replacement**

- Hodgkin (73% `Damage` `Debuffs on enemies`)
- Berial (71% `Damage` `Debuffs on enemies` `Crowd Control`)
- Perseus (64% `Damage`)

**Similar Skills**

- Sinbad (40% `assassin` `mark-target`)
- Dunlingr (33% `battle-start-burst` `disabler`)
- Kafra (33% `assassin` `mark-target`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Saida (100% `Energy drain`)
- Dunlingr (100% `Energy drain` `Vitality debuff`)
- Lily May (100% `Energy drain`)

**Crowd Control**

- Berial (70% `Frighten`)

### Summary for Silvina

#### Silvina Provides

- Marked target (focus fire) — Single target

#### Damage types dealt by Silvina

- Physical — Single target
- Max HP-based damage — Single target — `average`

#### Debuffs provided by Silvina

- Energy drain — Single target — `average`
- Vitality (Supreme+) — Single target — `low`

#### Crowd Control provided by Silvina

- Stun — Single target — `high`
- Frighten (EX+10) — Area — `average`

## Sinbad

### Sinbad's behavior

`AFK Stages [B]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [B]`

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
Common buffers are **Twins**, **Hugin**, or **Damian**.

- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (all units, low) `signature fuel`
- **Tasi**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Sinbad

- Indris (3.6 / 5)
- Bonnie (2.2 / 5)
- Shadewing (1.9 / 5)

### Units that can act as a replacement for Sinbad

**Best overall replacement**

- Kafra (53% `Similar Skills` `Damage`)

**Similar Skills**

- Kafra (90% `assassin` `enemy-debuffer` `mark-target`)
- Silvina (40% `assassin` `mark-target`)
- Silven (30% `mark-target`)

**Damage**

- Gunnar (100% `Physical`)
- Baelran (100% `Physical`)
- Himmel (100% `Physical`)

### Summary for Sinbad

#### Sinbad Provides

- Marked target (focus fire) — Single target

#### Damage types dealt by Sinbad

- Physical — Single target

#### Debuffs provided by Sinbad

- Damage taken — Single target — `low`
- ATK SPD (Mythic+) — Single target — `average`
- Energy recovery (Mythic+) — Single target — `average`
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
- **Behavior tags**: `ally-healer` `aoe-healing`
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

Look for units providing: `ATK` `Healing` `Energy`  
Common buffers are **Mikola**, **Solise**, or **Ravion**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Koko**
  - Direct healing (all units, average)
- **Contess**
  - ATK buff (single target, high)
  - Direct healing (single target, high)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)

### Units benefitting most from Smokey & Meerky

Smokey & Meerky provides Direct healing in an area `average` and Energy recovery in an area `low`.

**30** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner

These are the **10** strongest pairings: 

- Twins (5.0 / 5)
- Granny Dahnie (4.4 / 5)
- Antandra (4.3 / 5)
- Damian (4.2 / 5)
- Harak (3.8 / 5)
- Bryon (3.1 / 5)
- Zorya (3.1 / 5)
- Seth (3.0 / 5)
- Vala (2.9 / 5)
- Soren (2.8 / 5)

### Units that can act as a replacement for Smokey & Meerky

**Best overall replacement**

- Rowan (59% `Buffs on allies` `Energy provider`)

**Buffs on allies**

- Rowan (100% `Energy`)
- Seth (64% `Energy`)
- Ravion (61% `Energy`)

**Healing**

- Solise (100% `Direct healing` `Healing`)
- Hewynn (87% `Direct healing` `Healing`)
- Ludovic (68% `Direct healing` `Healing`)

**Similar Skills**

- Ludovic (100% `ally-healer` `aoe-healing`)
- Fay (100% `ally-healer` `aoe-healing`)
- Hewynn (100% `ally-healer` `aoe-healing`)

**Crowd Control**

- Gerda (100% `Interrupt` `Stun`)
- Sylphira (93% `Interrupt`)
- Lily May (93% `Interrupt`)

### Summary for Smokey & Meerky

#### Damage types dealt by Smokey & Meerky

- DoT — Single target

#### Crowd Control provided by Smokey & Meerky

- Interrupt — Single target — `low`
- Stun (Mythic+) — Single target — `low`

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
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`

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

_No synergy partners matched stat buffs or enablers._

### Units benefitting most from Solise

Solise provides ATK buff to summons `low`, Direct healing to all units `average`, Healing over time to single targets `high`, Shield to summons `average`, and DEF buff (Mythic+) to summons `low`.

**39** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Berial (5.0 / 5)
- Hodgkin (5.0 / 5)
- Phraesto (5.0 / 5)
- Dunlingr (4.3 / 5)
- Damian (4.2 / 5)
- Himmel (3.1 / 5)
- Laios (3.0 / 5)
- Bryon (2.9 / 5)
- Mehira (2.7 / 5)
- Silven (2.4 / 5)

### Units that can act as a replacement for Solise

**Healing**

- Smokey & Meerky (51% `Direct healing` `Healing`)

**Similar Skills**

- Velara (100% `ally-healer` `ally-shielder` `aoe-healing`)
- Smokey & Meerky (80% `ally-healer` `aoe-healing`)
- Contess (48% `ally-healer` `ally-shielder`)

**Damage**

- Frieren (100% `Magic`)
- Galahad (100% `Magic`)
- Twins (100% `Magic`)

### Summary for Solise

#### Solise Provides

- Ally blessing (Mythic+) — Single target

#### Damage types dealt by Solise

- Magic — All units

#### Crowd Control provided by Solise

- Unaffected — Self — On skill

## Sonja

### Sonja's behavior

`AFK Stages [B]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [B]`

- **Signature skill**: Crimson Covenant (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-buffer` `aoe-damage` `life-drain`
- **Ally composition**: place allies on left and right at battle start (Crimson Covenant buffs; prioritizes front row)
- **Damage types**: Physical `average`

#### Play overview

Sonja forms a **pact with left and right allies at battle start**, continuously raising their stats while all three remain alive. Her ultimate delivers **multi-hit damage** then charges through a frontal area, converting a portion of damage dealt to **self-healing**. She also **stuns nearby enemies twice** with her area skill for soft control at the front. Enhanced bond accumulates bonuses over time while partners survive, and battle **haste growth** keeps her rotation fluid. She is a **frontline buffer** who needs flanking allies to realize her pact value. Without adjacent partners or dense enemy clusters, her buffs and stun swings underwhelm.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `average`
- **Ultimate**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `low`

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
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, average)
- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
- **Alna**
  - ATK buff (single target, low)
  - Max HP buff (single target, high)
- **Zanie**
  - ATK buff (single target, low)
  - Max HP buff (single target, high)
- **Dunlingr**
  - ATK buff (single target, low)
  - Haste buff (single target, average) `signature fuel`

### Units benefitting most from Sonja

Sonja provides ATK buff to multiple targets `average` and DEF buff to multiple targets `low`.

- Hepler (2.5 / 5)

### Units that can act as a replacement for Sonja

**Best overall replacement**

- Perseus (59% `Buffs on allies` `Crowd Control` `Similar Skills`)

**Buffs on allies**

- Hugin (74% `ATK`)
- Evie (74% `ATK`)
- Twins (70% `ATK` `Magic DEF` `Physical DEF`)

**Similar Skills**

- Perseus (80% `ally-buffer` `aoe-damage`)
- Himmel (60% `ally-buffer` `aoe-damage`)
- Cassadee (60% `ally-buffer` `aoe-damage`)

**Damage**

- Gunnar (100% `Physical`)
- Baelran (100% `Physical`)
- Himmel (100% `Physical`)

**Crowd Control**

- Contess (100% `Stun`)
- Aliceth (100% `Stun`)
- Bonnie (100% `Stun`)

### Summary for Sonja

#### Damage types dealt by Sonja

- Physical — Area, Single target

#### Crowd Control provided by Sonja

- Stun — Single target — `low`

## Soren

### Soren's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Whirlwind Swing (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `counterattack` `self-repositioner`
- **Damage types**: Physical `high`, Max HP-based damage `average`

#### Play overview

Soren rushes targets with **knockback and stun on collision**, using melee strikes to shove enemies into walls or allies for extra damage and control. His block skill **absorbs a powerful incoming attack** and resets knockback cooldown, enabling repeated displacement chains through the fight. Low HP triggers a **haste boost plus HP and energy recovery**, helping him recover after heavy trades and stay in the brawl longer. When block triggers, his next melee skill gains **extended knockback and bonus damage** for a punishing follow-up strike on clustered foes. Battle **haste growth** keeps his repositioning active through longer engagements without slowing down. He struggles against **knockback-immune targets** or enemies who burst him down before his block cycle can activate and reset his knockback pressure entirely.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `average`

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

Look for units providing: `Haste` `Max HP` `Healing` `Energy`  
Common buffers are **Twins**, **Rowan**, or **Smokey & Meerky**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
  - Direct healing (all units, low)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Hewynn**
  - Healing over time (all units, high)
- **Pandora**
  - Max HP buff (single target, average)
  - Direct healing (single target, average)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, average)
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Soren

Soren provides Damage taken to single targets `low`, Haste buff (Legendary+) to single targets `low`, and Shield (Supreme+) to single targets `low`.

- Carolina (2.7 / 5)
- Nerion (2.3 / 5)
- Dionel (1.4 / 5)

### Units that can act as a replacement for Soren

**Best overall replacement**

- Hepler (51% `Damage` `Buffs on allies` `Crowd Control`)

**Buffs on allies**

- Galahad (100% `Shield` `Haste`)
- Hugin (100% `Shield` `Haste` `Damage taken reduction`)
- Hepler (100% `Shield` `Haste`)

**Similar Skills**

- Lenya (66% `counterattack` `self-repositioner`)
- Kulu (40% `self-repositioner`)
- Kordan (36% `self-repositioner`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Crowd Control**

- Perseus (100% `Stun` `Knock back`)
- Scarlita (100% `Stun` `Knock back`)
- Koko (78% `Stun`)

### Summary for Soren

#### Damage types dealt by Soren

- Physical — Area, Multiple targets, Single target
- Max HP-based damage — Single target — `low`

#### Crowd Control provided by Soren

- Knock back — Area — `low`
- Stun — Multiple targets — `average`

## Sylphira

### Sylphira's behavior

`AFK Stages [A]`, `Dream Realm [A+]`, `Dream Realm (Endless) [?]`, `PVP [A+]`

- **Signature skill**: Grand Finale (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `disabler` `life-drain` `mass-cc` `transformation`
- **Damage types**: Magic `high`, Max HP-based damage `high`, True damage `low`

#### Play overview

Sylphira builds an **active score** that raises ATK and Haste, then unleashes a **silencing domain** followed by multi-hit strikes on her target. Her three-hit skill **drains enemy energy** on each connect, and a separate skill chains **control into area knockdown** for crowd disruption across grouped foes. Once score activates, auto-play **cleanses debuffs and recovers HP and energy**, keeping her self-sufficient through extended fights without external support. Enhanced attacks also deal **true damage life drain** for sustained personal pressure between ultimate windows. She blends control, silence, and self-sustain in one slot for attrition-heavy teams. Against **unaffected or silence-immune foes**, her domain, energy drain, and knockdown chain lose much of their disruptive value.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, buffs `average`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `average`

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

Look for units providing: `ATK` `Haste` `Healing` `Life Drain`  
Common buffers are **Twins**, **Hugin**, or **Ravion**.

- **Contess**
  - ATK buff (single target, high)
  - Direct healing (single target, high)
- **Velara**
  - Haste buff (single target, low) `signature fuel`
  - Direct healing (area, low)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Himmel**
  - ATK buff (single target, high)
  - Direct healing (single target, low)
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`

### Units benefitting most from Sylphira

- Carolina (3.1 / 5)
- Bonnie (2.3 / 5)
- Nerion (2.3 / 5)

### Units that can act as a replacement for Sylphira

**Best overall replacement**

- Saida (63% `Damage` `Debuffs on enemies`)
- Baelran (63% `Damage` `Crowd Control`)
- Pippa (62% `Damage` `Debuffs on enemies`)

**Similar Skills**

- Shakir (50% `life-drain` `transformation`)
- Tasi (33% `mass-cc` `transformation`)
- Natsu (30% `mass-cc` `transformation`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage` `True damage`)
- Baelran (100% `Max HP-based damage` `True damage`)
- Athalia (100% `Max HP-based damage` `True damage`)

**Debuffs on enemies**

- Saida (100% `Energy drain`)
- Dunlingr (100% `Energy drain`)
- Lily May (100% `Energy drain`)

**Crowd Control**

- Baelran (76% `Knock down`)
- Lucca (60% `Knock down` `Interrupt`)

### Summary for Sylphira

#### Sylphira Provides

- Dispel debuffs (Mythic+) — Self
- Stacking buff (Mythic+) — Single target

#### Damage types dealt by Sylphira

- Magic — Area, Single target
- Max HP-based damage — Area, Single target — `average`
- True damage — Area — `low`

#### Debuffs provided by Sylphira

- Energy drain — Single target — `low`
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
- **Behavior tags**: `ally-healer` `aoe-damage` `cheat-death` `fire-attack` `transformation`
- **Ally composition**: frontmost ally carries Pyre of Renewal (AoE damage and healing)
- **Damage types**: Magic `high`

#### Play overview

Talene **consumes HP to shoot flames** at enemies, and her ATK **scales with cumulative HP spent** over the course of the fight. HP loss passively **heals allies while damaging enemies**, turning her self-harm into team-wide value whenever she trades health for offense. On defeat she **transforms and regenerates to resurrect**, with faster recovery on the first fall to rejoin the battle quickly. She also **enhances the frontmost ally** to deal sustained damage to adjacent enemies, extending her sacrifice into allied pressure over long engagements where she can cycle flame bursts multiple times. She is a **self-sacrificing specialist** who needs reliable healing to survive her own HP consumption safely across repeated flame cycles. Without sustain or enough fight time to trigger resurrection, her flame scaling and ally enhancement never reach their peak.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `high`

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

Look for units providing: `ATK` `Max HP` `Healing` `Life Drain`  
Common buffers are **Mikola**, **Twins**, or **Solise**.

- **Koko**
  - Direct healing (all units, average)
  - Lifedrain buff (multiple targets, average)
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Kordan**
  - ATK buff (multiple targets, high)
  - Lifedrain buff (multiple targets, low)
- **Dunlingr**
  - ATK buff (single target, low)
  - Lifedrain buff (all units, average)
- **Zanie**
  - ATK buff (single target, low)
  - Max HP buff (single target, high)
  - Direct healing (single target, high)

### Units benefitting most from Talene

Talene provides ATK buff (EX+5) in an area `high`.

- Bonnie (3.6 / 5)
- Shadewing (2.9 / 5)
- Silven (1.8 / 5)

### Units that can act as a replacement for Talene

**Buffs on allies**

- Gunnar (100% `ATK`)
- Contess (100% `ATK`)
- Frieren (100% `ATK`)

**Similar Skills**

- Ulmus (60% `aoe-damage` `cheat-death` `transformation`)
- Natsu (37% `aoe-damage` `fire-attack` `transformation`)
- Bonnie (34% `aoe-damage` `transformation`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Crowd Control**

- Twins (100% `Knock back`)
- Kordan (100% `Knock back`)
- Perseus (100% `Knock back`)

### Summary for Talene

#### Talene Provides

- Cheat death — Self
- Transformation — Self
- Stacking buff (Mythic+) — Single target

#### Damage types dealt by Talene

- Magic — Area, Single target

#### Crowd Control provided by Talene

- Knock back — Area — `low`

## Tasi

### Tasi's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Eternal Dreamscape (ultimate)
- **Movement**: stationary (avg attack range 10.0 tiles)
- **Behavior tags**: `aoe-damage` `mass-cc` `self-repositioner` `transformation`
- **Damage types**: Magic `average`, DoT `average`

#### Play overview

Tasi opens with **AoE sleep** that damages all enemies, then leaps to a distant foe to **deal damage and stun again**. HP sacrifice triggers **transformation that recovers HP** while damaging nearby enemies in her alternate form. ATK **grows after sleep casts**, and post-ultimate haste **tightens her rotation** between cycles. She gains **extra secondary form uses** on assists or kills for extended pressure windows. Against **sleep-immune targets**, her control package stalls before forms can cycle.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `low`
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

Look for units providing: `ATK` `Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, average)
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Pandora**
  - Max HP buff (single target, average)
  - Direct healing (single target, average)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Tasi

Tasi provides Haste buff (EX+5) to single targets `high`.

- Odie (2.2 / 5)
- Cassadee (2.2 / 5)

### Units that can act as a replacement for Tasi

**Buffs on allies**

- Twins (100% `Haste`)
- Lorsan (100% `Haste`)
- Hugin (82% `Haste`)

**Similar Skills**

- Valen (75% `aoe-damage` `mass-cc` `transformation`)
- Temesia (60% `aoe-damage` `mass-cc` `self-repositioner`)
- Arden (48% `aoe-damage` `mass-cc`)

**Damage**

- Frieren (100% `DoT` `Magic`)
- Cyran (100% `DoT` `Magic`)
- Cryonaia (100% `DoT` `Magic`)

**Crowd Control**

- Gerda (62% `Stun` `Bind` `Sleep`)
- Gwyneth (53% `Bind` `Stun`)
- Atalanta (53% `Bind` `Stun`)

### Summary for Tasi

#### Tasi Provides

- Invincibility — Area
- Sleep (area) — All units
- Transformation — Self

#### Damage types dealt by Tasi

- Magic — Area
- DoT — Area, Single target

#### Crowd Control provided by Tasi

- Bind — Single target — `low`
- Sleep — All units — `low`
- Stun — Area — `low`

## Temesia

### Temesia's behavior

`AFK Stages [C]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Knight's Heart (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `aoe-damage` `disabler` `enemy-debuffer` `mass-cc` `self-repositioner`
- **Damage types**: Physical `high`, Max HP-based damage `low`, True damage `low`

#### Play overview

Temesia charges through the field, dealing **path damage passively** and **knocking down enemies** on her mounted leap ultimate. Direction changes trigger **interrupting kicks** that weaken foes in her path. Sword attacks on adjacent tiles **scale on target ATK**, punishing high-damage frontliners. After repeated charges she gains **unaffected status and true damage**, and charge hits shave enemy Phys DEF. Battle ATK **grows after first ultimate**, adding scaling through longer fights. She underperforms when **charge paths are blocked** or enemies resist knockdown and displacement.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, buffs `average`, damage `high`
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

Look for units providing: `ATK` `ATK SPD / Haste` `Shield` `Healing` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
- **Hewynn**
  - Healing over time (all units, high)
- **Koko**
  - Shield (all units, low)
  - Direct healing (all units, average)
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Contess**
  - ATK buff (single target, high)
  - Shield (single target, average)
  - Direct healing (single target, high)

### Units benefitting most from Temesia

- Carolina (2.0 / 5)
- Nerion (1.6 / 5)
- Indris (1.4 / 5)

### Units that can act as a replacement for Temesia

**Similar Skills**

- Tasi (60% `aoe-damage` `mass-cc` `self-repositioner`)
- Cassadee (48% `aoe-damage` `enemy-debuffer`)
- Indris (40% `disabler` `enemy-debuffer`)

**Damage**

- Baelran (100% `Physical` `Max HP-based damage` `True damage`)
- Himmel (100% `Physical` `Max HP-based damage` `True damage`)
- Athalia (100% `Physical` `Max HP-based damage` `True damage`)

**Debuffs on enemies**

- Saida (90% `Damage dealt debuff`)
- Berial (90% `Damage dealt debuff`)

**Crowd Control**

- Sylphira (100% `Knock down` `Interrupt`)
- Lucca (100% `Knock down` `Interrupt`)
- Zorya (96% `Knock down`)

### Summary for Temesia

#### Temesia Provides

- Stacking buff — Single target

#### Damage types dealt by Temesia

- Physical — All units, Area, Single target
- Max HP-based damage — Single target — `average`
- True damage — Single target — `low`

#### Debuffs provided by Temesia

- Damage dealt — Single target — `low`
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
- **Behavior tags**: `ally-shielder` `enemy-debuffer` `energy-provider`
- **Ally composition**: place lieutenant 1 tile behind at battle prep (Crit + shared shields)
- **Damage types**: Physical `average`, DoT `high`, Max HP-based damage `average`

#### Play overview

Thador designates a **rear ally bond** that grants crit, then shields both partners when his active skill fires at the start of engagements. His ultimate deals **AoE damage and ritual debuffs** on affected enemies, layering disruption across the whole line. A frontal arc skill **knocks down** nearby foes, and battle **damage taken reduction** keeps him standing as a durable frontliner through sustained trades. When the bonded ally casts ultimate, he triggers **AoE damage plus Phys and Magic DEF reduction** on all enemies, amplifying team follow-up. Passive **HP regeneration** continues while the bonded ally lives, giving both partners staying power. He needs a **reliable rear partner** in formation; if the bond target dies early, much of his shielding, crit grant, and debuff payoff is lost for the rest of the fight.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `average`
- **Ultimate**: speed `slow`, damage `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `high`

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

Look for units providing: `Max HP` `Shield` `CRIT` `Healing`  
Common buffers are **Solise**, **Twins**, or **Hugin**.

- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
  - Direct healing (single target, high)
- **Saida**
  - Shield (multiple targets, high)
- **Contess**
  - Shield (single target, average)
  - Direct healing (single target, high)
- **Himmel**
  - Shield (single target, average)
  - Direct healing (single target, low)
- **Velara**
  - Direct healing (area, low)

### Units benefitting most from Thador

Thador provides Energy recovery (EX+10) to single targets `low`.

- Shadewing (2.3 / 5)
- Carolina (2.0 / 5)
- Indris (2.0 / 5)

### Units that can act as a replacement for Thador

**Best overall replacement**

- Ravion (77% `Buffs on allies` `Crowd Control` `Damage` `Similar Skills`)
- Baelran (53% `Crowd Control` `Damage`)

**Buffs on allies**

- Twins (100% `Energy`)
- Ravion (100% `Energy`)
- Pandora (100% `Energy`)

**Similar Skills**

- Ravion (60% `ally-shielder` `energy-provider`)
- Hugin (50% `ally-shielder` `energy-provider`)
- Pandora (50% `enemy-debuffer` `energy-provider`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage` `DoT`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Alna (100% `DoT` `Physical` `Max HP-based damage`)

**Crowd Control**

- Frieren (100% `Knock down`)
- Baelran (100% `Knock down`)
- Himmel (100% `Knock down`)

### Summary for Thador

#### Damage types dealt by Thador

- Physical — Area, Single target
- DoT — Single target
- Max HP-based damage — Area, Single target — `average`

#### Debuffs provided by Thador

- Magic DEF (Mythic+) — Single target — `average`
- Phys DEF (Mythic+) — Single target — `low`

#### Crowd Control provided by Thador

- Knock down — Single target — `low`

## Thoran

### Thoran's behavior

`AFK Stages [B]`, `Dream Realm [A+]`, `Dream Realm (Endless) [A]`, `PVP [A]`

- **Signature skill**: Resurrection (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `cheat-death` `counterattack` `life-drain`
- **Ally composition**: place ally 1 tile behind at battle prep (Soul Pact damage share and revive)
- **Damage types**: Physical `low`

#### Play overview

Thoran **charges up a slash** that adds a portion of damage taken during the charge, then gains **life drain** on the release for sustain. He drains HP from the **highest-HP enemy** to swell his own pool, and **revives once at partial HP** after his first defeat. Energy recovery from attacks is **higher before revive triggers**, fueling faster early ultimates while he still has his first life. He absorbs a portion of damage for a bonded ally, and on defeat the ally can sacrifice HP to revive him. His ultimate also **drains HP from enemies** on impact. He is a **durable frontliner** but offers weak output when enemies deny his drain targets and burst him before revive can matter.

#### Skill overview

- **Signature skill**: speed `fast`
- **Ultimate**: speed `fast`, buffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`

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

Look for units providing: `Max HP` `Healing` `Energy`  
Common buffers are **Solise**, **Twins**, or **Ravion**.

- **Zanie**
  - Max HP buff (single target, high)
  - Direct healing (single target, high)
- **Contess**
  - Direct healing (single target, high)
- **Velara**
  - Direct healing (area, low)
- **Himmel**
  - Direct healing (single target, low)
- **Thador**
  - Energy recovery (single target, low) `signature fuel`

### Units benefitting most from Thoran

Thoran provides Lifedrain buff to single targets `low` and Energy recovery (Legendary+) to single targets `average`.

- Pandora (2.0 / 5)
- Scarlita (1.6 / 5)

### Units that can act as a replacement for Thoran

**Best overall replacement**

- Gerda (57% `Crowd Control` `Damage`)
- Lucca (57% `Crowd Control` `Damage`)

**Buffs on allies**

- Twins (80% `Energy`)
- Ravion (80% `Energy`)
- Smokey & Meerky (80% `Energy`)

**Similar Skills**

- Saida (50% `cheat-death` `life-drain`)
- Brutus (40% `cheat-death` `life-drain`)
- Igor (40% `cheat-death` `life-drain`)

**Damage**

- Gunnar (100% `Physical`)
- Baelran (100% `Physical`)
- Himmel (100% `Physical`)

**Crowd Control**

- Saida (100% `Interrupt`)
- Sylphira (100% `Interrupt`)
- Lily May (100% `Interrupt`)

### Summary for Thoran

#### Thoran Provides

- Cheat death — Self

#### Damage types dealt by Thoran

- Physical — Single target

#### Crowd Control provided by Thoran

- Unaffected — Self — On skill
- Interrupt — Single target — `low`

## Tilaya

### Tilaya's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Wrath of the Wilds (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `aoe-damage`
- **Damage types**: Physical `average`

#### Play overview

Tilaya fights behind an **auto-regenerating shield** that fuels both defense and offense throughout the fight. Her ultimate delivers **repeated frontal greatsword attacks**, and shield regeneration **speeds up while casting** to keep her barrier topped. A powerful strike **restores shield value**, while normal attacks gain extra damage proportional to current shield for scaling burst. First shield break **permanently increases shield recovery**, and battle vitality growth keeps her standing through long frontline trades. She is a **shield-scaling tank** who peaks when allowed to maintain and rebuild her barrier repeatedly. Fights that **strip or bypass shields** leave her damage scaling and sustain flat.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, damage `low`
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

Look for units providing: `Max HP` `Shield` `Healing`  
Common buffers are **Solise**, **Twins**, or **Smokey & Meerky**.

- **Koko**
  - Shield (all units, low)
  - Direct healing (all units, average)
- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
  - Direct healing (single target, high)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)

### Units benefitting most from Tilaya

Tilaya provides DEF buff (EX+10) in an area `high` and Max HP buff (EX+10) in an area `average`.

- Granny Dahnie (5.0 / 5)
- Kruger (5.0 / 5)
- Lucca (5.0 / 5)
- Natsu (5.0 / 5)
- Niru (5.0 / 5)
- Hepler (4.9 / 5)
- Cecia (4.6 / 5)
- Isabella (3.9 / 5)
- Laios (3.4 / 5)
- Seth (3.3 / 5)

### Units that can act as a replacement for Tilaya

**Buffs on allies**

- Alna (68% `Max HP`)
- Cecia (57% `Max HP`)

**Similar Skills**

- Florabelle (60% `aoe-damage`)
- Lorsan (60% `aoe-damage`)
- Perseus (50% `aoe-damage`)

**Damage**

- Gunnar (100% `Physical`)
- Baelran (100% `Physical`)
- Himmel (100% `Physical`)

### Summary for Tilaya

#### Damage types dealt by Tilaya

- Physical — Single target

#### Crowd Control provided by Tilaya

- Unaffected — Single target — On skill

## Twins

### Twins's behavior

`AFK Stages [S]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S+]`, `PVP [A+]`

- **Signature skill**: Starlight Waltz (ultimate)
- **Movement**: moving / stationary (two units)
- **Behavior tags**: `ally-buffer` `ally-healer` `ally-shielder` `energy-provider`
- **Ally composition**: place allies on the Stellar Bond line between Elijah and Lailah
- **Damage types**: Magic `low`, Max HP-based damage `low`

#### Play overview

The Twins inspire allied **haste through a linked duo performance**, and linked allies become **unaffected** during the ultimate. They form **line links** that recover linked allies' energy and HP over sustained casts. One twin **shields allies** while the other **damages and blinds** nearby enemies in the same beat. Linked allies **borrow best stats from each other**, and haste grows with each repeated performance. They need **multiple linked partners** in formation; sparse lineups waste their buff and healing channels.

#### Skill overview

- **Signature skill (ult)**: speed `average`, buffs `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, damage `low`

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

Look for units providing: `Haste` `Healing` `Energy`  
Common buffers are **Smokey & Meerky**, **Damian**, or **Hugin**.

- **Contess**
  - Direct healing (single target, high)
- **Gunnar**
  - ATK SPD buff (single target, low) `signature fuel`
- **Hewynn**
  - Healing over time (all units, high)
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
  - Direct healing (all units, low)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Twins

Twins provides ATK buff to multiple targets `average`, Direct healing to multiple targets `low`, Energy recovery to multiple targets `low`, Haste buff to all units `high`, Max HP buff to multiple targets `high`, Shield to single targets `low`, Vitality buff (Mythic+) to multiple targets `low`, and DEF buff (Supreme+) to single targets `low`.

**103** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight
- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner

These are the **10** strongest pairings: 

- Dionel (5.0 / 5)
- Faramor (5.0 / 5)
- Laios (5.0 / 5)
- Lenya (5.0 / 5)
- Lily May (5.0 / 5)
- Perseus (5.0 / 5)
- Silven (5.0 / 5)
- Soren (5.0 / 5)
- Tasi (5.0 / 5)
- Zorya (5.0 / 5)

### Units that can act as a replacement for Twins

**Best overall replacement**

- Smokey & Meerky (60% `Healing` `Energy provider`)
- Pandora (57% `Healing` `Energy provider`)
- Rowan (56% `Energy provider` `Healing` `Similar Skills`)

**Buffs on allies**

- Hugin (63% `Haste` `Shield` `ATK`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Zanie (100% `Direct healing` `Healing`)

**Similar Skills**

- Koko (60% `ally-buffer` `ally-healer`)
- Rowan (60% `ally-healer` `energy-provider`)
- Solise (48% `ally-healer` `ally-shielder`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Mehira (100% `Magic` `Max HP-based damage`)

**Crowd Control**

- Damian (97% `Blind`)
- Hepler (81% `Blind`)
- Aliceth (75% `Blind` `Knock back`)

### Summary for Twins

#### Twins Provides

- Ally positioning link — Multiple targets
- Shared HP and Energy — Single target

#### Damage types dealt by Twins

- Magic — Area, Single target
- Max HP-based damage — Single target — `low`

#### Crowd Control provided by Twins

- Unaffected — Single target — On skill
- Blind — Area — `average`
- Knock back — Area — `low`

## Ulmus

### Ulmus's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Way of the Forest (Skill 2)
- **Movement**: moving (stationary when rooted)
- **Behavior tags**: `ally-shielder` `aoe-damage` `cheat-death` `transformation`
- **Ally composition**: when rooted, shields frontmost ally instead of self
- **Damage types**: Physical `average`

#### Play overview

Ulmus gains a **shield that damages surrounding enemies when it breaks**, and retreats to **take root at low HP** for survival when pressured. While rooted he shifts to energy regeneration instead of HP regen, and grants **shield to the frontmost ally** after his own shield breaks. His ultimate **knocks up a target and adjacent enemies**, and displacement **extends knockdown duration with bonus damage**. Battle max HP growth adds durability over time, and shield break knocks back adjacent foes for extra control. He blends **tanking, control, and ally protection** in one slot. He struggles when enemies **focus him before rooting** or deny displacement setups entirely.

#### Skill overview

- **Signature skill**: speed `fast`, heal `average`, buffs `average`
- **Ultimate**: speed `fast`, heal `average`, damage `high`
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

Look for units providing: `Max HP` `Shield` `Healing` `Energy` `Life Drain`  
Common buffers are **Smokey & Meerky**, **Twins**, or **Solise**.

- **Koko**
  - Shield (all units, low)
  - Direct healing (all units, average)
  - Lifedrain buff (multiple targets, average)
- **Hepler**
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
  - Direct healing (single target, high)
- **Dunlingr**
  - Lifedrain buff (all units, average)
- **Zandrok**
  - Max HP buff (multiple targets, average)
  - Lifedrain buff (area, low, conditional (frequent))

### Units benefitting most from Ulmus

- Kazim (3.8 / 5)

### Units that can act as a replacement for Ulmus

**Best overall replacement**

- Scarlita (74% `Buffs on allies` `Damage` `Crowd Control`)
- Pang (61% `Buffs on allies` `Similar Skills` `Damage`)

**Buffs on allies**

- Gunnar (100% `Shield`)
- Contess (100% `Shield`)
- Galahad (100% `Shield`)

**Similar Skills**

- Talene (60% `aoe-damage` `cheat-death` `transformation`)
- Pang (60% `ally-shielder` `transformation`)
- Scarlita (48% `ally-shielder` `aoe-damage`)

**Damage**

- Gunnar (100% `Physical`)
- Baelran (100% `Physical`)
- Himmel (100% `Physical`)

**Crowd Control**

- Scarlita (100% `Knock back` `Knock up`)
- Kordan (88% `Knock back` `Bind` `Knock up`)
- Cassadee (69% `Knock back` `Knock up`)

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
- **Behavior tags**: `hp-scaling` `mark-target` `self-repositioner` `stealth` `transformation` `untargetable`
- **Damage types**: Physical `average`, HP loss `average`, Max HP-based damage `average`, True damage `average`

#### Play overview

Vala **marks an enemy** and prioritizes them, **absorbing their energy** on each focused attack to starve their rotation. Her ultimate switches between **ranged stun mode** and **melee true damage mode** depending on positioning needs in the fight. Mode-based skills either reduce enemy haste or deliver multi-hit burst for flexible offense. ATK **grows with each non-summoned enemy defeated**, and marked enemy defeat boosts her movement speed and haste. She deals **bonus damage to marked targets** for reliable focus fire on priority carries. Against **mark-immune or stealth-heavy lines**, her energy drain and mode switching add little sustained pressure.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, damage `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `average`

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

Look for units providing: `ATK` `Haste` `Healing` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

Vala also requires enemies **to be defeated**

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Marcille**
  - Haste buff (single target, low) `signature fuel`
  - Direct healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Pandora**
  - Direct healing (single target, average)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Vala

Vala provides Haste buff (Mythic+) to single targets `high`.

- Indris (2.4 / 5)
- Nerion (2.2 / 5)
- Dionel (1.7 / 5)

### Units that can act as a replacement for Vala

**Best overall replacement**

- Athalia (60% `Damage` `Similar Skills`)
- Nazrik (54% `Damage` `Crowd Control`)
- Silvina (50% `Crowd Control` `Debuffs on enemies`)

**Buffs on allies**

- Twins (100% `Haste`)
- Hugin (100% `Haste`)
- Shakir (100% `Haste`)

**Similar Skills**

- Athalia (60% `hp-scaling` `self-repositioner` `transformation`)
- Silven (48% `hp-scaling` `mark-target`)
- Marilee (48% `hp-scaling` `self-repositioner`)

**Damage**

- Athalia (100% `True damage` `Physical` `Max HP-based damage` `HP loss`)
- Nara (100% `True damage` `Physical` `Max HP-based damage` `HP loss`)
- Nazrik (93% `True damage` `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Dunlingr (83% `Energy drain` `Haste debuff`)
- Saida (75% `Energy drain`)
- Lily May (75% `Energy drain`)

**Crowd Control**

- Callan (100% `Stun`)
- Koko (100% `Stun`)
- Perseus (100% `Stun`)

### Summary for Vala

#### Vala Provides

- Marked target (focus fire) — Single target

#### Damage types dealt by Vala

- Physical — Single target
- HP loss — Single target — `average`
- Max HP-based damage — Single target — `low`
- True damage — Single target — `average`

#### Debuffs provided by Vala

- Energy drain — Single target — `low`
- Haste — Single target — `average`
- Marked target (focus fire) — Single target — `average`

#### Crowd Control provided by Vala

- Untargetable (Mythic+) — Multiple targets — Conditional
- Stun — Single target — `average`

## Valen

### Valen's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Thunder Swordwork (ultimate)
- **Movement**: moving (avg attack range 1.4 tiles)
- **Behavior tags**: `aoe-damage` `mass-cc` `transformation`
- **Damage types**: Physical `average`

#### Play overview

Valen launches **multiple strikes within range** and enters a permanent **Invigoration buff state** that defines his entire rotation. Three-hit consecutive strikes **chain lightning to nearby foes** while buffed, and a separate skill delivers **AoE lightning burst** only during the buff window for spread damage. Buff activations **stack ATK bonus** over repeated casts, compounding personal damage through the fight, and lightning AoE also stuns enemies for control alongside raw burst output. He is a buff-gated damage dealer who needs Invigoration uptime to access his best skills. Without **grouped enemies for chain lightning**, his burst and stun payoff shrink sharply.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `average`

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
Common buffers are **Twins**, **Rowan**, or **Ravion**.

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Pandora**
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`

### Units benefitting most from Valen

Valen provides ATK buff (Mythic+) to single targets `low`.

- Bonnie (1.8 / 5)
- Carolina (1.8 / 5)
- Indris (1.7 / 5)

### Units that can act as a replacement for Valen

**Best overall replacement**

- Perseus (100% `Damage` `Crowd Control` `Buffs on allies`)
- Pang (91% `Damage` `Crowd Control` `Buffs on allies`)
- Atalanta (84% `Damage` `Crowd Control`)

**Buffs on allies**

- Gunnar (100% `ATK`)
- Contess (100% `ATK`)
- Frieren (100% `ATK`)

**Similar Skills**

- Tasi (75% `aoe-damage` `mass-cc` `transformation`)
- Arden (60% `aoe-damage` `mass-cc`)
- Natsu (60% `aoe-damage` `mass-cc` `transformation`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Galahad (100% `Haste debuff` `Movement speed debuff`)
- Zorya (100% `Haste debuff` `Movement speed debuff`)
- Vala (96% `Haste debuff`)

**Crowd Control**

- Aliceth (100% `Stun`)
- Bonnie (100% `Stun`)
- Phraesto (100% `Stun`)

### Summary for Valen

#### Valen Provides

- Invincibility — Self
- Stacking buff (Mythic+) — Single target

#### Damage types dealt by Valen

- Physical — Area, Single target

#### Debuffs provided by Valen

- Haste (Supreme+) — Single target — `average`
- Movement speed (Supreme+) — Single target — `low`

#### Crowd Control provided by Valen

- Stun (Supreme+) — Single target — `average`

## Valka

### Valka's behavior

`AFK Stages [C]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [B]`

- **Signature skill**: Phantom Slasher (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-buffer` `ally-shielder` `counterattack`
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Play overview

Valka applies **Panic stacks through normal attacks**, then slashes panicked targets for **damage and self-healing** on ultimate for sustain at the front. She wields **multiple sword techniques** at appropriate range, each costing energy for flexible offense across melee and mid-range. At battle start she gains a **shield and raises ally ATK SPD**, supporting nearby partners while she pressures enemies. Battle ATK speed growth keeps her rotation fluid, and she **counters incoming ultimate damage** with a free parry counter when threatened. While shielded she gains **bonus energy from normal attacks**, fueling faster technique use. She underperforms when enemies **never accumulate Panic** or burst her before stacks complete.

#### Skill overview

- **Signature skill (ult)**: speed `fast`, first cast speed `fast`, heal `average`, debuffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `high`

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

Look for units providing: `ATK SPD / Haste` `Shield` `Healing` `Energy`  
Common buffers are **Twins**, **Smokey & Meerky**, or **Hugin**.

- **Koko**
  - Shield (all units, low)
  - Direct healing (all units, average)
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Marcille**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Direct healing (multiple targets, high)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)

### Units benefitting most from Valka

Valka provides ATK SPD buff to multiple targets `low` and Lifedrain buff (EX+10) to single targets `low`.

- Carolina (2.3 / 5)
- Shadewing (2.1 / 5)
- Nerion (2.0 / 5)

### Units that can act as a replacement for Valka

**Best overall replacement**

- Zorya (65% `Debuffs on enemies` `Crowd Control` `Damage`)
- Dunlingr (51% `Buffs on allies` `Debuffs on enemies` `Damage`)

**Buffs on allies**

- Dunlingr (100% `ATK SPD` `Life Drain`)
- Lyca (80% `ATK SPD`)
- Fay (66% `ATK SPD`)

**Similar Skills**

- Twins (40% `ally-buffer` `ally-shielder`)
- Callan (30% `ally-shielder`)
- Isabella (30% `ally-buffer`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Galahad (100% `Haste debuff`)
- Velara (100% `Haste debuff`)
- Alna (100% `Haste debuff`)

**Crowd Control**

- Callan (100% `Knock down` `Stun`)
- Scarlita (100% `Knock down` `Stun`)
- Zorya (100% `Knock down` `Stun`)

### Summary for Valka

#### Damage types dealt by Valka

- Physical — Area
- Max HP-based damage — Single target — `average`

#### Debuffs provided by Valka

- Haste — Single target — `low`

#### Crowd Control provided by Valka

- Unaffected — Self — On skill
- Knock down — Area — `low`
- Stun — Single target — `low`

## Velara

### Velara's behavior

`AFK Stages [S+]`, `Dream Realm [S]`, `Dream Realm (Endless) [S]`, `PVP [A]`

- **Signature skill**: Ruthless Rite (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-healer` `ally-shielder` `aoe-healing`
- **Damage types**: Magic `average`

#### Play overview

Velara summons **magic circles** that awaken to affect nearby units, extending to the **entire battlefield** once all circles are active across the field. She **immobilizes the highest cumulative damage dealer** and reduces their stats, blunting the enemy's main damage source early. One circle **awakens immediately at battle start**, and nearby debuffed enemies **charge circle energy** for faster full activation. Haste **grows with awakened circle count**, and awakened circles periodically buff weakest allies with healing and protection. Full awakening makes allies unaffected and boosts their damage on subsequent ultimate casts. She needs **fight time and enemy clustering** near circles to reach full coverage; fast burst that ends fights before all circles awaken wastes her scaling and team-wide buff package.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, first cast speed `fast`, heal `average`, debuffs `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `average`

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
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - Shield (single target, average)
- **Contess**
  - Shield (single target, average)
- **Gunnar**
  - Shield (single target, average)
- **Himmel**
  - Shield (single target, average)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Shield (multiple targets, high)

### Units benefitting most from Velara

Velara provides Direct healing in an area `low` and Haste buff to single targets `low`.

**12** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Ludovic (2.2 / 5)
- Himmel (2.1 / 5)
- Alna (2.1 / 5)
- Athalia (2.1 / 5)
- Reinier (2.1 / 5)
- Saida (2.1 / 5)
- Mehira (1.6 / 5)
- Gwyneth (1.4 / 5)
- Aurora (1.3 / 5)
- Galahad (1.3 / 5)

### Units that can act as a replacement for Velara

**Best overall replacement**

- Twins (81% `Buffs on allies` `Healing`)
- Mikola (77% `Buffs on allies` `Healing`)
- Solise (66% `Healing` `Similar Skills`)

**Buffs on allies**

- Galahad (100% `Haste`)
- Twins (100% `Haste`)
- Hugin (100% `Haste`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Twins (100% `Direct healing` `Healing`)

**Similar Skills**

- Solise (100% `ally-healer` `ally-shielder` `aoe-healing`)
- Ludovic (80% `ally-healer` `aoe-healing`)
- Smokey & Meerky (80% `ally-healer` `aoe-healing`)

**Damage**

- Frieren (100% `Magic`)
- Galahad (100% `Magic`)
- Saida (100% `Magic`)

**Debuffs on enemies**

- Eironn (100% `Haste debuff` `Magic DEF debuff`)
- Galahad (69% `Haste debuff`)
- Alna (69% `Haste debuff`)

**Crowd Control**

- Saida (100% `Bind`)
- Alna (100% `Bind`)
- Eironn (100% `Bind`)

### Summary for Velara

#### Damage types dealt by Velara

- Magic — Single target

#### Debuffs provided by Velara

- Haste — Area — `average`
- Magic DEF — Single target — `average`
- Phys DEF — Single target — `low`

#### Crowd Control provided by Velara

- Bind — Single target — `high`

## Viperian

### Viperian's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Crimson Waltz (Mythic+)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Behavior tags**: `aoe-damage` `dot-specialist` `life-drain`
- **Damage types**: Magic `average`

#### Play overview

Viperian **spends HP to send possessing summons** onto all enemies, spreading pressure across the entire enemy line at once. She drains HP from the **healthiest foe** to refill herself, and possessed summons **periodically damage their hosts** for sustained DoT attrition. A high HP threshold triggers a **large AoE damage burst**, punishing healthy enemy formations. Battle **haste growth** keeps her rotation moving between possession cycles and drain windows, and when possessed enemies fall, summons **return to restore her HP and energy** for the next wave. She is a **DoT and life-drain specialist** who needs healing to cycle HP costs safely. Without sustain or long fights, her possession loop and burst threshold never fully activate.

#### Skill overview

- **Signature skill**: speed `slow`, damage `average`
- **Ultimate**: speed `fast`, first cast speed `fast`, heal `average`, damage `average`
- **Non-ultimate**: speed `average`, heal `average`, debuffs `average`, damage `average`

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

Look for units providing: `Haste` `Healing`  
Common buffers are **Twins**, **Damian**, or **Hugin**.

- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
  - Direct healing (all units, low)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Hewynn**
  - Healing over time (all units, high)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Marcille**
  - Haste buff (single target, low) `signature fuel`
  - Direct healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Tasi**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Viperian

- Bonnie (2.4 / 5)
- Shadewing (2.2 / 5)
- Indris (1.5 / 5)

### Units that can act as a replacement for Viperian

**Best overall replacement**

- Saida (70% `Damage` `Debuffs on enemies`)
- Berial (64% `Damage` `Debuffs on enemies`)
- Pippa (64% `Damage` `Debuffs on enemies`)

**Similar Skills**

- Lorsan (66% `aoe-damage` `dot-specialist`)
- Arden (60% `aoe-damage` `dot-specialist`)
- Sonja (50% `aoe-damage` `life-drain`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Saida (100% `Energy drain`)
- Dunlingr (100% `Energy drain`)
- Lily May (100% `Energy drain`)

### Summary for Viperian

#### Damage types dealt by Viperian

- Magic — All units, Single target

#### Debuffs provided by Viperian

- Energy drain — Single target — `low`

#### Crowd Control provided by Viperian

- Unaffected — Self — On skill

## Walker

### Walker's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Six-Shot (ultimate)
- **Movement**: moving (avg attack range 2.0 tiles)
- **Behavior tags**: `aoe-damage` `battle-start-burst` `life-drain` `mark-target` `mass-cc`
- **Damage types**: Physical `low`, Max HP-based damage `low`

#### Play overview

Walker fires **sequential frontal shots** that stun each target hit, and his normal attacks deal **AoE damage** for spread pressure. He **prioritizes the highest-damage-dealt enemy**, gaining a buff on focus, and throws **grenades at battle start** for AoE damage and stun. Battle **crit damage growth** adds scaling over time, and first hit against the marked target grants a shield for survivability. He excels as a **battle-start burst specialist** with sustained stun pressure on priority targets. Against **stun-immune targets** or lines that deny his opening grenade angles, his control chain stalls early.

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `average`

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

Look for units providing: `Max HP` `Shield` `CRIT` `CRIT DMG Boost` `Life Drain`  
Common buffers are **Twins**, **Hugin**, or **Damian**.

- **Dunlingr**
  - Lifedrain buff (all units, average)
  - ATK SPD buff (all units, low) `signature fuel`
- **Zandrok**
  - Max HP buff (multiple targets, average)
  - Lifedrain buff (area, low, conditional (frequent))
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Koko**
  - Shield (all units, low)
  - Lifedrain buff (multiple targets, average)
- **Hepler**
  - Shield (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Saida**
  - Shield (multiple targets, high)

### Units benefitting most from Walker

Walker provides Crit buff to single targets `low`.

- Nazrik (5.0 / 5)

### Units that can act as a replacement for Walker

**Buffs on allies**

- Harak (100% `Crit`)
- Rhys (100% `Crit`)

**Similar Skills**

- Mehira (51% `aoe-damage` `life-drain` `mass-cc`)
- Eironn (51% `aoe-damage` `battle-start-burst` `mass-cc`)
- Cyran (41% `aoe-damage` `battle-start-burst`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Nazrik (100% `Crit Resist debuff`)

**Crowd Control**

- Callan (100% `Stun`)
- Koko (100% `Stun`)
- Perseus (100% `Stun`)

### Summary for Walker

#### Damage types dealt by Walker

- Physical — Arc, Single target
- Max HP-based damage — Single target — `low`

#### Debuffs provided by Walker

- Crit Resist (Mythic+) — Single target — `low`

#### Crowd Control provided by Walker

- Stun — Arc — `average`

## Zandrok

### Zandrok's behavior

`AFK Stages [A+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Rallying Roar (Skill 1)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `aoe-damage` `battlefield-modification` `hp-scaling`
- **Damage types**: Physical `low`

#### Play overview

At battle start, Zandrok sends **illusions charging forward** that **destroy obstacles** in their path and **inspire passing allies** with extra max HP, **Life Drain**, and **Haste**. His axe slam **clears leftover obstacles** near the target while dealing **HP-based area damage**. A ground stomp hits **adjacent enemies** with damage that **scales on max HP**, and his max HP **grows over the fight**, especially while his inspire buffs are active. Normal attacks add **bonus damage from max HP**, and excess healing **converts to permanent max HP**, so sustain feeds his scaling loop. He is a **max HP specialist** who peaks on obstacle-heavy fields with healing support. On **open boards without obstacles**, much of his terrain value and illusion pathing is wasted.

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `average`
- **Ultimate**: speed `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`

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

Look for units providing: `Haste` `Max HP` `Healing` `Life Drain`  
Common buffers are **Twins**, **Solise**, or **Smokey & Meerky**.

- **Koko**
  - Direct healing (all units, average)
  - Lifedrain buff (multiple targets, average)
- **Dunlingr**
  - Haste buff (single target, average) `signature fuel`
  - Lifedrain buff (all units, average)
- **Marcille**
  - Haste buff (single target, low) `signature fuel`
  - Direct healing (multiple targets, high)
- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - Lifedrain buff (single target, low)
- **Ludovic**
  - Direct healing (multiple targets, high)

### Units benefitting most from Zandrok

Zandrok provides Haste buff in an area `low` — conditional (frequent), Lifedrain buff in an area `low` — conditional (frequent), and Max HP buff to multiple targets `average`.

- Satrana (4.8 / 5)
- Kazim (3.7 / 5)
- Walker (3.2 / 5)
- Shakir (2.6 / 5)
- Korin (2.4 / 5)
- Brutus (2.4 / 5)
- Sonja (2.3 / 5)

### Units that can act as a replacement for Zandrok

**Buffs on allies**

- Shakir (96% `Haste` `Life Drain`)
- Twins (77% `Haste` `Max HP`)
- Cecia (55% `Max HP` `Life Drain`)

**Similar Skills**

- Scarlita (60% `aoe-damage` `hp-scaling`)
- Faramor (40% `aoe-damage` `hp-scaling`)
- Tilaya (33% `aoe-damage`)

**Crowd Control**

- Scarlita (100% `Stun` `Knock up`)
- Lucca (100% `Stun` `Knock up`)
- Soren (86% `Stun`)

### Summary for Zandrok

#### Crowd Control provided by Zandrok

- Knock up — Area — `low`
- Stun — Area — `low`

## Zanie

### Zanie's behavior

`AFK Stages [A+]`, `Dream Realm [A+]`, `Dream Realm (Endless) [A+]`, `PVP [B]`

- **Signature skill**: Vein Pulse (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `fire-attack` `summoner`
- **Damage types**: Physical `low`

#### Play overview

Zanie **deploys laser turrets at reduced max HP**, then boosts **ATK and ATK speed** for herself and her turrets on ultimate. A gun turret **targets enemies near laser turrets** at battle start, and she **repairs turrets** to restore HP and grant shields to keep them on the field. One turret can be upgraded for more power, and laser attacks apply burn to enemies hit for steady pressure. Battle penetration growth helps her damage pierce defenses over time. She is a **summon-dependent specialist** who needs turrets alive to realize her kit. Fights that **destroy turrets early** or deny her setup window leave her weakened.

#### Skill overview

- **Signature skill (ult)**: speed `slow`, first cast speed `fast`, buffs `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`

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

Look for units providing: `ATK` `ATK SPD / Haste`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Velara**
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Zanie

Zanie provides Direct healing to single targets `high`, Shield to single targets `high`, DEF Penetration buff (Legendary+) to single targets `average`, ATK buff (Mythic+) to single targets `high`, and Max HP buff (Mythic+) to single targets `high`.

- Daimon (3.9 / 5)
- Thador (3.7 / 5)
- Tilaya (3.7 / 5)
- Alna (3.4 / 5)
- Athalia (3.4 / 5)
- Thoran (2.7 / 5)
- Reinier (2.2 / 5)

### Units that can act as a replacement for Zanie

**Buffs on allies**

- Hugin (100% `Shield` `ATK`)
- Lucius (100% `Shield`)
- Korin (100% `Shield`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Twins (100% `Direct healing` `Healing`)

**Similar Skills**

- Mirael (40% `fire-attack`)
- Florabelle (33% `summoner`)
- Gwyneth (30% `fire-attack`)

**Debuffs on enemies**

- Lyca (100% `Phys DEF debuff` `ATK debuff`)
- Ravion (96% `Phys DEF debuff` `ATK debuff`)
- Sinbad (86% `Phys DEF debuff` `ATK debuff`)

**Crowd Control**

- Aliceth (100% `Knock back` `Stun`)
- Perseus (100% `Knock back` `Stun`)
- Scarlita (100% `Knock back` `Stun`)

### Summary for Zanie

#### Damage types dealt by Zanie

- Physical — Single target
- DoT — Single target

#### Debuffs provided by Zanie

- ATK (Supreme+) — Single target — `average`
- Phys DEF (Supreme+) — Single target — `high`

#### Crowd Control provided by Zanie

- Knock back — Single target — `low`
- Stun — Single target — `low`

## Zorya

### Zorya's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Guardian's Ring (ultimate)
- **Movement**: moving (inactive while dormant)
- **Behavior tags**: `hp-scaling` `life-drain`
- **Damage types**: Magic `high`, HP loss `high`, Max HP-based damage `high`

#### Play overview

Zorya cycles **dormant and awake states**, jumping to nearby enemies for **AoE damage** on each awakening. While awake she gains **life drain and damage reduction**, and her aura **slows enemy haste** while boosting her own. Damage dealt **scales with nearby enemy count**, rewarding clustered foes. A fatal blow **forces immediate dormancy**, ending her active window. She needs **clustered enemies**; spread lines waste her cycles.

#### Skill overview

- **Signature skill (ult)**: speed `average`, first cast speed `fast`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `high`

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

Look for units providing: `ATK` `Haste` `Max HP` `Healing` `Energy`  
Common buffers are **Twins**, **Smokey & Meerky**, or **Mikola**.

Zorya also requires allies **casting ultimates**

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - Lifedrain buff (single target, low)
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Lyca**
  - Energy recovery (all units, low) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
  - Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
- **Dunlingr**
  - ATK buff (single target, low)
  - Haste buff (single target, average) `signature fuel`
  - Lifedrain buff (all units, average)
  - ATK SPD buff (all units, low) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, average)
  - Lifedrain buff (area, low, conditional (frequent))
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Koko**
  - Direct healing (all units, average)
  - Lifedrain buff (multiple targets, average)

### Units benefitting most from Zorya

Zorya provides Haste buff (EX+5) to single targets `low`.

- Bonnie (4.4 / 5)
- Indris (3.3 / 5)
- Nerion (2.5 / 5)

### Units that can act as a replacement for Zorya

**Buffs on allies**

- Galahad (100% `Haste`)
- Twins (100% `Haste`)
- Hugin (100% `Haste`)

**Similar Skills**

- Shemira (80% `hp-scaling` `life-drain`)
- Satrana (48% `hp-scaling` `life-drain`)
- Shakir (40% `life-drain`)

**Damage**

- Mehira (100% `Magic` `Max HP-based damage` `HP loss`)
- Dunlingr (100% `Magic` `Max HP-based damage` `HP loss`)
- Nara (100% `Max HP-based damage` `HP loss`)

**Debuffs on enemies**

- Galahad (100% `Movement speed debuff` `Haste debuff`)
- Bonnie (61% `Haste debuff`)
- Lorsan (51% `Haste debuff`)

**Crowd Control**

- Callan (100% `Stun` `Knock down`)
- Scarlita (100% `Stun` `Knock down`)
- Antandra (100% `Stun` `Knock down`)

### Summary for Zorya

#### Zorya Provides

- Invincibility — Single target

#### Damage types dealt by Zorya

- Magic — Arc, Area, Single target
- HP loss — Single target — `high`
- Max HP-based damage — Arc, Single target — `high`

#### Debuffs provided by Zorya

- Haste (Mythic+) — Area — `high`
- Movement speed (Mythic+) — Area — `average`

#### Crowd Control provided by Zorya

- Steadfast — Self — On skill
- Unaffected (EX+10) — Self — On skill
- Knock down — Arc — `average`
- Stun — Area — `average`

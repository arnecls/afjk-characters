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
- **Behavior tags**: `ally-buffer` `execute` `hp-scaling` `invincibility` `mark-target`
- **Ally composition**: nearest ally in same row receives Brightfeather at battle start
- **Damage types**: Physical `high`, HP loss `low`, Max HP-based damage `high`

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
Common buffers are **Solise**, **Twins**, or **Mikola**.

Aliceth also requires units **putting debuffs** on enemies

- **Velara**
  - Direct healing (area, low)
  - Enables Debuff on target via Haste debuff (area)
- **Galahad**
  - ATK SPD via Haste buff (single target, average) `signature fuel`
  - Enables Debuff on target via Movement speed debuff (area)
- **Contess**
  - ATK buff (single target, high)
  - Direct healing (multiple targets, low)
  - Enables Debuff on target via ATK debuff (multiple targets)
- **Frieren**
  - Enables Debuff on target via DoT (area)
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
  - Enables Debuff on target via Healing debuff (area)

### Units benefitting most from Aliceth

Aliceth provides Ally empower buff to single targets `high`, Attack range buff to single targets `high`, DEF Penetration buff to multiple targets `high`, ATK buff (Legendary+) to multiple targets `average`, and Fatal blow immunity (Mythic+) to single targets `high` — conditional (rare).

- Lily May (4.1 / 5)
- Nerion (3.7 / 5)
- Kulu (3.7 / 5)
- Pang (3.3 / 5)
- Shadewing (2.6 / 5)
- Kordan (2.3 / 5)

### Units that can act as a replacement for Aliceth

**Similar Skills**

- Aurora (60% `ally-buffer` `invincibility` `mark-target`)
- Silven (48% `hp-scaling` `mark-target`)
- Nazrik (48% `hp-scaling` `mark-target`)

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
- Marked target (focus fire) — Single target — `average`
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
- **Behavior tags**: `ally-buffer` `aoe-damage` `cc-immunity` `dot-specialist` `invincibility` `summoner`
- **Ally composition**: place ally in same row at battle prep (Winter Warrior buffs)
- **Damage types**: Physical `high`, DoT `high`, Max HP-based damage `high`

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
Common buffers are **Solise**, **Twins**, or **Mikola**.

- **Zanie**
  - Max HP buff (single target, high)
  - Direct healing (single target, high)
- **Velara**
  - Direct healing (area, low)
- **Contess**
  - Direct healing (multiple targets, low)
- **Himmel**
  - Direct healing (single target, low)
- **Hewynn**
  - Healing over time (all units, high)

### Units benefitting most from Alna

Alna provides Ally empower buff to single targets `high`, Max HP buff to single targets `high`, Dmg and CC immunity (EX+15) to single targets `high`, and ATK buff (Supreme+) to single targets `low`.

- Indris (3.6 / 5)
- Shadewing (3.2 / 5)

### Units that can act as a replacement for Alna

**Similar Skills**

- Aurora (51% `ally-buffer` `invincibility` `summoner`)
- Faramor (42% `ally-buffer` `aoe-damage` `dot-specialist`)
- Laios (34% `ally-buffer` `summoner`)

**Damage**

- Baelran (100% `Physical` `Max HP-based damage`)
- Thador (100% `DoT` `Physical` `Max HP-based damage`)
- Dunlingr (100% `DoT` `Max HP-based damage`)

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
Common buffers are **Twins**, **Rowan**, or **Mikola**.

- **Atalanta**
  - Haste buff (multiple targets, high, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) `signature fuel`
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
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - Shield (single target, average)
  - ATK SPD via Haste buff (single target, average) `signature fuel`

### Units benefitting most from Alsa

- Bonnie (2.5 / 5)
- Nerion (1.8 / 5)
- Indris (1.6 / 5)

### Units that can act as a replacement for Alsa

**Similar Skills**

- Athalia (60% `self-repositioner` `transformation`)
- Kulu (50% `battlefield-modification` `self-repositioner`)
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
Common buffers are **Twins**, **Smokey & Meerky**, or **Mikola**.

- **Hepler**
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
  - Direct healing (single target, high)
- **Zandrok**
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Hugin**
  - Shield (multiple targets, high)
- **Ludovic**
  - Direct healing (multiple targets, high)

### Units benefitting most from Antandra

Antandra provides DEF buff (Supreme+) to single targets `low`.

- Carolina (3.4 / 5)
- Nerion (3.1 / 5)
- Shadewing (2.5 / 5)

### Units that can act as a replacement for Antandra

**Buffs on allies**

- Eironn (100% `Magic DEF` `Physical DEF`)
- Kordan (100% `Magic DEF` `Physical DEF`)
- Mikola (100% `Magic DEF` `Physical DEF`)

**Similar Skills**

- Ulmus (50% `ally-shielder` `aoe-damage` `mass-cc`)
- Galahad (48% `ally-shielder` `aoe-damage`)
- Lucca (48% `ally-shielder` `mass-cc`)

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
Common buffers are **Rowan**, **Mikola**, or **Smokey & Meerky**.

- **Ravion**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, average) `signature fuel`
  - Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, high)
  - ATK SPD buff (all units, low) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, average, conditional (frequent))
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Pandora**
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Arden

Arden provides Energy recovery to single targets `low`.

- Carolina (2.9 / 5)
- Nerion (2.7 / 5)
- Shadewing (1.8 / 5)

### Units that can act as a replacement for Arden

**Buffs on allies**

- Twins (100% `Energy`)
- Ravion (100% `Energy`)
- Smokey & Meerky (100% `Energy`)

**Similar Skills**

- Lorsan (80% `aoe-damage` `dot-specialist`)
- Gwyneth (60% `dot-specialist` `mass-cc`)
- Viperian (60% `aoe-damage` `dot-specialist`)

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

- Bind — Multiple targets — `average`

## Atalanta

### Atalanta's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Wild Sniper (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `aoe-damage` `battle-start-burst` `self-repositioner`
- **Damage types**: Physical `high`, Max HP-based damage `high`

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
Common buffers are **Mikola**, **Twins**, or **Smokey & Meerky**.

- **Hewynn**
  - Healing over time (all units, high)
- **Fay**
  - Direct healing (arc, average)
  - DEF buff (multiple targets, average)
  - ATK SPD buff (multiple targets, low) `signature fuel`
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
  - Direct healing (all units, low)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
  - DEF buff (single target, low)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Lucca**
  - DEF buff (area, high)

### Units benefitting most from Atalanta

Atalanta provides Haste buff (Legendary+) to multiple targets `high` — conditional (frequent).

- Lucy (4.1 / 5)
- Mirael (3.9 / 5)
- Alsa (3.8 / 5)
- Chippy (3.7 / 5)
- Hugin (3.5 / 5)
- Frieren (3.2 / 5)
- Korin (2.8 / 5)

### Units that can act as a replacement for Atalanta

**Buffs on allies**

- Twins (100% `Haste`)
- Lorsan (100% `Haste`)
- Shakir (69% `Haste`)

**Similar Skills**

- Himmel (60% `aoe-damage` `battle-start-burst` `self-repositioner`)
- Florabelle (60% `aoe-damage` `battle-start-burst`)
- Dionel (60% `aoe-damage` `self-repositioner`)

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
- **Damage types**: Physical `high`, HP loss `high`, Max HP-based damage `high`, True damage `high`

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
Common buffers are **Solise**, **Twins**, or **Mikola**.

- **Zanie**
  - Max HP buff (single target, high)
  - Direct healing (single target, high)
- **Velara**
  - Direct healing (area, low)
- **Contess**
  - Direct healing (multiple targets, low)
- **Himmel**
  - Direct healing (single target, low)
- **Hewynn**
  - Healing over time (all units, high)

### Units benefitting most from Athalia

- Shadewing (1.7 / 5)
- Carolina (1.5 / 5)
- Nerion (1.4 / 5)

### Units that can act as a replacement for Athalia

**Similar Skills**

- Baelran (80% `hp-scaling` `transformation`)
- Pippa (80% `hp-scaling` `self-repositioner`)
- Kordan (66% `hp-scaling` `self-repositioner`)

**Damage**

- Nara (95% `Physical` `True damage` `Max HP-based damage` `HP loss`)
- Vala (90% `True damage` `Physical` `Max HP-based damage` `HP loss`)
- Nazrik (83% `True damage` `Physical` `Max HP-based damage`)

**Crowd Control**

- Frieren (100% `Knock down`)
- Baelran (100% `Knock down`)
- Himmel (100% `Knock down`)

### Summary for Athalia

#### Athalia Provides

- Invincibility — Self
- Transformation — Self

#### Damage types dealt by Athalia

- Physical — All units, Area, Single target
- HP loss — All units — `high`
- Max HP-based damage — Area — `high`
- True damage — All units, Single target — `high`

#### Crowd Control provided by Athalia

- Unaffected — Self — On skill
- Knock down — Single target — `low`

## Aurora

### Aurora's behavior

`AFK Stages [A+]`, `Dream Realm [A+]`, `Dream Realm (Endless) [S+]`, `PVP [B]`

- **Signature skill**: Starlit Slumber (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `ally-buffer` `invincibility` `mark-target` `summoner`
- **Damage types**: Magic `high`, Max HP-based damage `high`

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
Common buffers are **Twins** or **Mikola**.

- **Galahad**
  - Haste buff (single target, average) `signature fuel`
- **Mehira**
  - Haste buff (single target, low) `signature fuel`
- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)
- **Kazim**
  - ATK buff (single target, average)
  - Haste buff (multiple targets, average) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, average, conditional (frequent))
  - Haste buff (multiple targets, low) `signature fuel`

### Units benefitting most from Aurora

Aurora provides Haste buff to summons `high`, Invincible to single targets `high`, and Summon damage buff (Mythic+) to summons `low`.

- Florabelle (3.7 / 5)
- Zanie (3.5 / 5)
- Dunlingr (3.2 / 5)
- Phraesto (2.9 / 5)
- Mehira (2.5 / 5)

### Units that can act as a replacement for Aurora

**Buffs on allies**

- Pandora (89% `Invincible`)
- Harak (60% `Invincible`)

**Similar Skills**

- Aliceth (60% `ally-buffer` `invincibility` `mark-target`)
- Alna (51% `ally-buffer` `invincibility` `summoner`)
- Damian (48% `ally-buffer` `summoner`)

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
- Velara (100% `Bind`)
- Alna (100% `Bind`)

### Summary for Aurora

#### Aurora Provides

- Dream sleep (transformation) — Self
- Invincibility — Single target
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
- **Damage types**: Physical `high`, Max HP-based damage `high`, True damage `high`

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
Common buffers are **Twins**, **Solise**, or **Mikola**.

- **Hugin**
  - ATK buff (multiple targets, high)
  - Shield (multiple targets, high)
- **Contess**
  - ATK buff (single target, high)
  - Shield (single target, average)
  - Direct healing (multiple targets, low)
- **Himmel**
  - ATK buff (multiple targets, low)
  - Shield (single target, average)
  - Direct healing (single target, low)
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - Shield (single target, average)
- **Velara**
  - Direct healing (area, low)

### Units benefitting most from Baelran

- Carolina (3.4 / 5)
- Nerion (3.1 / 5)
- Kazim (2.4 / 5)

### Units that can act as a replacement for Baelran

**Similar Skills**

- Athalia (80% `hp-scaling` `transformation`)
- Silven (33% `hp-scaling`)
- Kordan (33% `hp-scaling`)

**Damage**

- Athalia (100% `True damage` `Physical` `Max HP-based damage`)
- Frieren (85% `True damage` `Max HP-based damage`)
- Sylphira (82% `Max HP-based damage` `True damage`)

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
Common buffers are **Mikola**, **Rowan**, or **Solise**.

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
  - Direct healing (single target, high)
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Berial

- Carolina (3.4 / 5)
- Nerion (3.1 / 5)
- Shadewing (2.1 / 5)

### Units that can act as a replacement for Berial

**Similar Skills**

- Seth (24% `assassin`)
- Saida (24% `cheat-death`)
- Harak (24% `assassin`)

**Damage**

- Frieren (100% `DoT` `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `DoT` `Max HP-based damage`)
- Gwyneth (100% `DoT` `Max HP-based damage`)

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
- **Behavior tags**: `aoe-damage` `battle-start-burst` `enemy-debuffer` `mass-cc` `transformation`
- **Damage types**: Magic `average`

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
Common buffers are **Solise**, **Twins**, or **Smokey & Meerky**.

Bonnie also requires units **dealing magic damage** and/or units **putting debuffs** on enemies

- **Dunlingr**
  - ATK buff (single target, high)
  - Enables Debuff on target via Haste debuff (all units)
  - Enables Magic damage from allies via Magic damage (area)
- **Cyran**
  - Enables Debuff on target via ATK SPD debuff (all units)
  - Enables Magic damage from allies via Magic damage + wide area (area)
- **Kulu**
  - Enables Debuff on target via Damage taken debuff (all units)
- **Galahad**
  - Enables Debuff on target via Movement speed debuff (area)
  - Enables Magic damage from allies via Magic damage + wide area + all enemies (all units)
- **Frieren**
  - Enables Debuff on target via DoT (area)
  - Enables Magic damage from allies via Magic damage (area)

### Units benefitting most from Bonnie

- Shadewing (2.3 / 5)
- Indris (1.9 / 5)
- Nerion (1.8 / 5)

### Units that can act as a replacement for Bonnie

**Similar Skills**

- Tasi (60% `aoe-damage` `mass-cc` `transformation`)
- Ulmus (51% `aoe-damage` `mass-cc` `transformation`)
- Temesia (51% `aoe-damage` `enemy-debuffer` `mass-cc`)

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
- Haste — Single target — `high`
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
Common buffers are **Koko**.

- **Dunlingr**
  - Lifedrain buff (all units, average)
- **Zandrok**
  - Lifedrain buff (area, low, conditional (frequent))
- **Daimon**
  - Lifedrain buff (single target, average)
- **Kordan**
  - Lifedrain buff (multiple targets, low)
- **Shakir**
  - Lifedrain buff (single target, low)

### Units benefitting most from Brutus

- Shadewing (2.8 / 5)
- Aliceth (2.4 / 5)
- Indris (2.1 / 5)

### Units that can act as a replacement for Brutus

**Similar Skills**

- Antandra (41% `aoe-damage` `taunt`)
- Thoran (40% `cheat-death` `life-drain`)
- Saida (33% `cheat-death` `life-drain`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage` `DoT`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Alna (100% `Physical` `DoT` `Max HP-based damage`)

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
- **Behavior tags**: `battle-start-burst` `battle-start-ult` `summoner` `untargetable`
- **Damage types**: Magic `high`, DoT `average`

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
Common buffers are **Twins**, **Mikola**, or **Smokey & Meerky**.

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
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)

### Units benefitting most from Bryon

- Bonnie (2.4 / 5)
- Shadewing (2.2 / 5)
- Indris (2.2 / 5)

### Units that can act as a replacement for Bryon

**Similar Skills**

- Florabelle (57% `battle-start-burst` `summoner`)
- Dunlingr (50% `battle-start-burst` `summoner`)
- Igor (28% `battle-start-burst` `untargetable`)

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
- **Movement**: moving (avg attack range 1.7 tiles)
- **Behavior tags**: `ally-shielder` `battle-start-burst` `cc-immunity`
- **Damage types**: Magic `high`

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
Common buffers are **Koko**, **Mikola**, or **Solise**.

- **Hugin**
  - Shield (multiple targets, high)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)
- **Zanie**
  - Shield (single target, average)
  - Direct healing (single target, high)

### Units benefitting most from Callan

- Nerion (3.6 / 5)

### Units that can act as a replacement for Callan

**Similar Skills**

- Gerda (34% `ally-shielder` `battle-start-burst`)
- Himmel (33% `ally-shielder` `battle-start-burst`)
- Dunlingr (30% `battle-start-burst`)

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
- **Behavior tags**: `dot-specialist` `enemy-debuffer` `mass-cc`
- **Damage types**: Magic `high`

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
Common buffers are **Twins**, **Koko**, or **Rowan**.

Carolina also requires units **applying crowd control** to enemies

- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Enables CC on enemies via Blind (area, high)
- **Damian**
  - Enables CC on enemies via Blind (area, high)
- **Eironn**
  - Enables CC on enemies via Bind (area, high)
- **Kordan**
  - Enables CC on enemies via Bind (area, high)
- **Lorsan**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
  - Enables CC on enemies via Stun (multiple targets, high)

### Units benefitting most from Carolina

- Shadewing (2.2 / 5)
- Indris (2.2 / 5)
- Nerion (2.2 / 5)

### Units that can act as a replacement for Carolina

**Similar Skills**

- Shadewing (96% `dot-specialist` `enemy-debuffer`)
- Nerion (72% `dot-specialist` `enemy-debuffer`)
- Cecia (60% `enemy-debuffer` `mass-cc`)

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
Common buffers are **Twins**, **Mikola**, or **Solise**.

Cassadee also requires a unit **to bless**

- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Dunlingr**
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Isabella**
  - Haste buff (multiple targets, low) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Lyca**
  - Energy recovery (all units, low) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Cassadee

Cassadee provides Tidal Strength buff to all units `high`.

- Nerion (2.3 / 5)
- Silven (2.3 / 5)
- Perseus (2.2 / 5)

### Units that can act as a replacement for Cassadee

**Similar Skills**

- Perseus (80% `ally-buffer` `aoe-damage`)
- Parisa (60% `ally-buffer` `aoe-damage`)
- Hodgkin (60% `aoe-damage` `enemy-debuffer`)

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
Common buffers are **Mikola**, **Twins**, or **Rowan**.

- **Lucca**
  - DEF buff (area, high)
  - DEF buff (area, high)
- **Sonja**
  - DEF buff (multiple targets, high)
  - DEF buff (multiple targets, high)
- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)
- **Fay**
  - ATK SPD buff (multiple targets, low) `signature fuel`
  - DEF buff (multiple targets, average)
  - DEF buff (multiple targets, average)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)

### Units benefitting most from Cecia

Cecia provides DEF Penetration buff to single targets `average`, Lifedrain buff in an area `low`, and Max HP buff to single targets `high`.

- Carolina (3.4 / 5)
- Nerion (3.3 / 5)
- Silven (1.8 / 5)

### Units that can act as a replacement for Cecia

**Buffs on allies**

- Phraesto (90% `Max HP`)
- Alna (79% `Max HP`)

**Similar Skills**

- Carolina (60% `enemy-debuffer` `mass-cc`)
- Hodgkin (60% `enemy-debuffer` `summoner`)
- Pandora (50% `enemy-debuffer` `mass-cc`)

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

- **Atalanta**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) `signature fuel`
- **Lyca**
  - Energy recovery (all units, low) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
- **Kazim**
  - ATK SPD via Haste buff (multiple targets, average) `signature fuel`
- **Valka**
  - ATK SPD buff (multiple targets, average) `signature fuel`
- **Lorsan**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Chippy

- Himmel (1.5 / 5)

### Units that can act as a replacement for Chippy

**Similar Skills**

- Dunlingr (40% `summoner`)
- Zanie (40% `summoner`)
- Kordan (33% `self-repositioner`)

**Damage**

- Athalia (100% `Physical`)
- Igor (100% `Physical`)
- Kruger (100% `Physical`)

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

Look for units providing: `Healing` `Energy`  
Common buffers are **Smokey & Meerky**, **Mikola**, or **Solise**.

- **Hewynn**
  - Healing over time (all units, high)
- **Hepler**
  - Healing over time (multiple targets, high)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)
- **Gerda**
  - Healing over time (area, average)

### Units benefitting most from Contess

Contess provides ATK buff to single targets `high`, Direct healing to multiple targets `low`, Exemption buff to single targets `high`, and Shield to single targets `average`.

**14** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Faramor (2.4 / 5)
- Aliceth (2.4 / 5)
- Himmel (2.2 / 5)
- Baelran (2.2 / 5)
- Daimon (2.1 / 5)
- Shemira (1.9 / 5)
- Silven (1.9 / 5)
- Alna (1.8 / 5)
- Athalia (1.8 / 5)
- Sylphira (1.7 / 5)

### Units that can act as a replacement for Contess

**Buffs on allies**

- Hugin (56% `ATK` `Shield`)

**Healing**

- Solise (100% `Direct healing` `Healing`)
- Ludovic (100% `Direct healing` `Healing`)
- Marcille (100% `Direct healing` `Healing`)

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

- Cyran (75% `Silence`)
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
Common buffers are **Mikola**, **Rowan**, or **Twins**.

- **Hugin**
  - ATK buff (multiple targets, high)
  - Shield (multiple targets, high)
- **Ravion**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, average) `signature fuel`
  - Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Saida**
  - Shield (multiple targets, high)
- **Dunlingr**
  - ATK buff (single target, high)
  - ATK SPD buff (all units, low) `signature fuel`
- **Pandora**
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Cryonaia

- Bonnie (2.4 / 5)
- Shadewing (1.9 / 5)
- Himmel (1.5 / 5)

### Units that can act as a replacement for Cryonaia

**Similar Skills**

- Lily May (34% `cc-immunity` `invincibility`)
- Alna (28% `cc-immunity` `invincibility`)
- Kulu (24% `battlefield-modification`)

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
- **Damage types**: Magic `high`, DoT `high`, True damage `low`

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `low`

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
Common buffers are **Twins**, **Mikola**, or **Smokey & Meerky**.

- **Dunlingr**
  - ATK buff (single target, high)
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, average) `signature fuel`
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
- **Ravion**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, average) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Cyran

- Bonnie (4.7 / 5)

### Units that can act as a replacement for Cyran

**Similar Skills**

- Atalanta (48% `aoe-damage` `battle-start-burst`)
- Walker (41% `aoe-damage` `battle-start-burst`)
- Florabelle (40% `aoe-damage` `battle-start-burst`)

**Damage**

- Korin (97% `True damage` `Max HP-based damage`)
- Frieren (93% `DoT` `Magic` `True damage` `Max HP-based damage`)
- Faramor (83% `DoT` `True damage`)

**Debuffs on enemies**

- Sinbad (100% `ATK SPD debuff`)

**Crowd Control**

- Evie (82% `Silence` `Bind` `Displace`)

### Summary for Cyran

#### Cyran Provides

- Artifact mimic (Mythic+) — Self
- Artifact block (EX+10) — Single target

#### Damage types dealt by Cyran

- Magic — Area, Single target
- DoT — Area
- True damage — All units — `average`

#### Debuffs provided by Cyran

- ATK SPD (Mythic+) — All units — `high`

#### Crowd Control provided by Cyran

- Steadfast — Single target — Conditional
- Unaffected — Self — Start of battle
- Bind — Area — `low`
- Displace — All units — `low`
- Knock down — Area — `low`
- Silence (EX+10) — Single target — `high`

## Daimon

### Daimon's behavior

`AFK Stages [A+]`, `Dream Realm [B]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Buddy Barrier (Skill 2)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-shielder` `hp-scaling` `life-drain` `summoner`
- **Ally composition**: place ally directly behind at battle prep (shield share, Life Drain, and ATK bond)
- **Damage types**: Magic `low`, Max HP-based damage `high`, True damage `average`

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
Common buffers are **Twins** or **Koko**.

- **Hugin**
  - Shield (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)
- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
- **Contess**
  - Shield (single target, average)
- **Galahad**
  - Shield (single target, average)

### Units benefitting most from Daimon

Daimon provides Lifedrain buff to single targets `average` and Shield to multiple targets `average`.

- Kruger (4.0 / 5)
- Silvina (3.7 / 5)
- Brutus (2.2 / 5)
- Eironn (2.0 / 5)
- Satrana (2.0 / 5)

### Units that can act as a replacement for Daimon

**Buffs on allies**

- Hepler (100% `Shield`)
- Lucius (100% `Shield`)
- Salazer (100% `Shield`)

**Similar Skills**

- Shemira (72% `hp-scaling` `life-drain` `summoner`)
- Zorya (60% `hp-scaling` `life-drain`)
- Koko (50% `ally-shielder` `life-drain`)

**Damage**

- Frieren (100% `Max HP-based damage` `Magic` `True damage`)
- Baelran (100% `Max HP-based damage` `True damage`)
- Shemira (100% `Max HP-based damage` `Magic` `True damage`)

**Crowd Control**

- Pandora (100% `Frighten`)
- Berial (100% `Frighten`)
- Silvina (100% `Frighten`)

### Summary for Daimon

#### Damage types dealt by Daimon

- Magic — Single target
- Max HP-based damage — Area, Single target — `high`
- True damage — Area — `low`

#### Crowd Control provided by Daimon

- Frighten (Mythic+) — Area — `low`

## Damian

### Damian's behavior

`AFK Stages [C]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Inventor's Will (Mythic+)
- **Movement**: stationary (off battlefield)
- **Behavior tags**: `ally-buffer` `ally-healer` `summoner`
- **Damage types**: Magic `high`

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
Common buffers are **Mikola**, **Smokey & Meerky**, or **Twins**.

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
- **Fay**
  - ATK buff (multiple targets, low)
  - Direct healing (arc, average)

### Units benefitting most from Damian

Damian provides Healing over time (EX+5) in an area `low`.

- Carolina (4.7 / 5)

### Units that can act as a replacement for Damian

**Healing**

- Solise (100% `Healing over time` `Healing`)
- Ludovic (100% `Healing over time` `Healing`)
- Mikola (100% `Healing over time` `Healing`)

**Similar Skills**

- Laios (100% `ally-buffer` `ally-healer` `summoner`)
- Isabella (60% `ally-buffer` `ally-healer`)
- Twins (48% `ally-buffer` `ally-healer`)

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
- **Damage types**: Physical `average`, True damage `high`

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

Look for units providing: `ATK SPD / Haste` `Shield` `Execution`  
Common buffers are **Twins**, **Rowan**, or **Mikola**.

- **Shakir**
  - ATK SPD via Haste buff (multiple targets, average) `signature fuel`
- **Valka**
  - ATK SPD buff (multiple targets, average) `signature fuel`
- **Ravion**
  - Energy recovery (multiple targets, average) `signature fuel`
  - Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, average) `signature fuel`
  - Shield (single target, average)
- **Hugin**
  - Shield (multiple targets, high)

### Units benefitting most from Dionel

Dionel provides ATK buff to single targets `average`.

- Kazim (2.4 / 5)
- Indris (1.5 / 5)
- Nerion (1.4 / 5)

### Units that can act as a replacement for Dionel

**Buffs on allies**

- Gunnar (100% `ATK`)
- Hugin (100% `ATK`)
- Aliceth (100% `ATK`)

**Similar Skills**

- Igor (60% `aoe-damage` `self-repositioner` `untargetable`)
- Rhys (60% `aoe-damage` `self-repositioner`)
- Atalanta (60% `aoe-damage` `self-repositioner`)

**Damage**

- Frieren (100% `True damage`)
- Baelran (100% `True damage` `Physical`)
- Faramor (100% `True damage` `Physical`)

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
- True damage — All units, Single target — `high`

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
- **Behavior tags**: `battle-start-burst` `summoner`
- **Damage types**: Magic `average`, DoT `average`, HP loss `low`, Max HP-based damage `average`

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
Common buffers are **Twins**, **Solise**, or **Mikola**.

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
- **Hugin**
  - Shield (multiple targets, high)
- **Ludovic**
  - Direct healing (multiple targets, high)

### Units benefitting most from Dunlingr

Dunlingr provides ATK buff (EX+5) to single targets `high`, Haste buff (EX+15) to single targets `average`, ATK SPD buff (Supreme+) to all units `low`, and Lifedrain buff (Supreme+) to all units `average`.

**20** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Bonnie (5.0 / 5)
- Brutus (5.0 / 5)
- Indris (5.0 / 5)
- Kruger (4.3 / 5)
- Walker (3.8 / 5)
- Igor (3.5 / 5)
- Zandrok (3.4 / 5)
- Cyran (3.4 / 5)
- Seth (3.0 / 5)
- Marilee (2.8 / 5)

### Units that can act as a replacement for Dunlingr

**Buffs on allies**

- Twins (71% `ATK` `Haste`)
- Kordan (69% `ATK` `Life Drain`)
- Gunnar (66% `ATK` `ATK SPD`)

**Similar Skills**

- Florabelle (66% `battle-start-burst` `summoner`)
- Bryon (50% `battle-start-burst` `summoner`)
- Zanie (33% `summoner`)

**Damage**

- Zorya (85% `Magic` `Max HP-based damage` `HP loss`)
- Mehira (85% `DoT` `Magic` `Max HP-based damage` `HP loss`)
- Aliceth (80% `Max HP-based damage` `HP loss`)

**Debuffs on enemies**

- Saida (88% `Energy drain`)
- Lily May (88% `Energy drain`)

**Crowd Control**

- Contess (100% `Silence`)
- Gwyneth (100% `Silence`)
- Sylphira (100% `Silence`)

### Summary for Dunlingr

#### Dunlingr Provides

- Summoning — Self
- Ultimate lock (Spellbind) — Single target

#### Damage types dealt by Dunlingr

- Magic — Area
- DoT — All units
- HP loss — Single target — `low`
- Max HP-based damage — All units — `low`

#### Debuffs provided by Dunlingr

- Haste — All units — `high`
- Energy drain (Supreme+) — All units — `high`
- Vitality (Supreme+) — All units — `high`

#### Crowd Control provided by Dunlingr

- Silence — Single target — `low`

## Eironn

### Eironn's behavior

`AFK Stages [S]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Verdant Cyclone (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `aoe-damage` `battle-start-ult` `enemy-grouping` `mass-cc`
- **Damage types**: Magic `high`

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

Look for units providing: `Shield` `Physical DEF` `Magic DEF`  
Common buffers are **Twins**, **Mikola**, or **Rowan**.

- **Hugin**
  - Shield (multiple targets, high)
- **Kordan**
  - DEF buff (single target, high)
  - DEF buff (single target, high)
- **Saida**
  - Shield (multiple targets, high)
- **Daimon**
  - Shield (multiple targets, average)
- **Galahad**
  - Shield (single target, average)
  - ATK SPD via Haste buff (single target, average) `signature fuel`

### Units benefitting most from Eironn

Eironn provides Dodge chance buff to single targets `high` and DEF buff (Legendary+) to single targets `high`.

- Carolina (4.7 / 5)
- Nerion (4.1 / 5)

### Units that can act as a replacement for Eironn

**Similar Skills**

- Mehira (51% `aoe-damage` `enemy-grouping` `mass-cc`)
- Arden (48% `aoe-damage` `mass-cc`)
- Tasi (48% `aoe-damage` `mass-cc`)

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

- Haste — Arc — `average`
- Magic DEF — Single target — `average`

#### Crowd Control provided by Eironn

- Bind — Area — `high`
- Displace — Area — `low`

## Evie

### Evie's behavior

`AFK Stages [B]`, `Dream Realm [A+]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Intel Chase (ultimate)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `invincibility` `self-repositioner` `stealth`
- **Ally composition**: rearmost ally starts with healing quill; tracks highest damage dealer
- **Damage types**: Magic `average`

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

Look for units providing: `Healing` `Energy`  
Common buffers are **Solise**, **Twins**, or **Smokey & Meerky**.

- **Ludovic**
  - Direct healing (multiple targets, high)
- **Zanie**
  - Direct healing (single target, high)
- **Ravion**
  - Energy recovery (multiple targets, average) `signature fuel`
- **Velara**
  - Direct healing (area, low)
- **Contess**
  - Direct healing (multiple targets, low)

### Units benefitting most from Evie

Evie provides ATK buff to multiple targets `high` and Direct healing to single targets `high`.

- Smokey & Meerky (2.8 / 5)
- Ludovic (1.9 / 5)

### Units that can act as a replacement for Evie

**Healing**

- Solise (100% `Direct healing` `Healing`)
- Ludovic (100% `Direct healing` `Healing`)
- Smokey & Meerky (100% `Direct healing` `Healing`)

**Similar Skills**

- Vala (34% `self-repositioner` `stealth`)
- Igor (33% `invincibility` `self-repositioner`)
- Lily May (28% `invincibility` `self-repositioner`)

**Damage**

- Frieren (100% `Magic`)
- Galahad (100% `Magic`)
- Saida (100% `Magic`)

**Debuffs on enemies**

- Velara (100% `Magic DEF debuff`)
- Thador (100% `Magic DEF debuff`)
- Shadewing (100% `Magic DEF debuff`)

**Crowd Control**

- Cyran (63% `Silence` `Bind` `Displace`)
- Korin (56% `Bind`)
- Eironn (52% `Bind` `Displace`)

### Summary for Evie

#### Evie Provides

- Invincibility — Self

#### Damage types dealt by Evie

- Magic — Single target

#### Debuffs provided by Evie

- Magic DEF — Single target — `low`

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
- **Damage types**: Physical `high`, DoT `high`, HP loss `high`, True damage `average`

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
Common buffers are **Twins**, **Mikola**, or **Koko**.

- **Hugin**
  - ATK buff (multiple targets, high)
  - Shield (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)
- **Contess**
  - ATK buff (single target, high)
  - Shield (single target, average)
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - Shield (single target, average)
- **Himmel**
  - ATK buff (multiple targets, low)
  - Shield (single target, average)

### Units benefitting most from Faramor

- Carolina (2.2 / 5)
- Nerion (2.0 / 5)
- Shadewing (1.9 / 5)

### Units that can act as a replacement for Faramor

**Similar Skills**

- Perseus (60% `ally-buffer` `aoe-damage`)
- Lorsan (60% `aoe-damage` `dot-specialist`)
- Arden (57% `aoe-damage` `dot-specialist`)

**Damage**

- Athalia (90% `Physical` `True damage` `HP loss`)
- Vala (85% `True damage` `Physical` `HP loss`)
- Nara (73% `Physical` `True damage` `HP loss`)

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
- True damage — Area, Single target — `average`

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

#### Skill overview

- **Signature skill (ult)**: speed `slow`, heal `average`, buffs `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `average`

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

Look for units providing: `ATK SPD / Haste` `Healing`  
Common buffers are **Mikola**, **Twins**, or **Rowan**.

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Pandora**
  - Direct healing (single target, high)
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
- **Valka**
  - ATK SPD buff (multiple targets, average) `signature fuel`
- **Ravion**
  - Energy recovery (multiple targets, average) `signature fuel`
  - Energy recovery (150 early objective, multiple targets) `signature fuel`

### Units benefitting most from Fay

Fay provides ATK SPD buff to multiple targets `low`, ATK buff to multiple targets `low`, DEF buff to multiple targets `average`, Direct healing to arc `average`, Direct healing to multiple targets `average`, and Vitality buff (EX+5) to single targets `high`.

- Granny Dahnie (3.7 / 5)
- Lucca (3.7 / 5)
- Hepler (2.8 / 5)
- Natsu (2.8 / 5)

### Units that can act as a replacement for Fay

**Buffs on allies**

- Mikola (100% `Magic DEF` `Physical DEF` `ATK` `Vitality buff`)
- Sonja (100% `Magic DEF` `Physical DEF` `ATK`)
- Kordan (88% `Magic DEF` `Physical DEF` `ATK`)

**Healing**

- Solise (100% `Direct healing` `Healing`)
- Evie (100% `Direct healing` `Healing`)
- Ludovic (100% `Direct healing` `Healing`)

**Similar Skills**

- Ludovic (100% `ally-healer` `aoe-healing`)
- Smokey & Meerky (100% `ally-healer` `aoe-healing`)
- Hewynn (100% `ally-healer` `aoe-healing`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Sinbad (100% `Magic DEF debuff` `Phys DEF debuff`)
- Laios (100% `Magic DEF debuff` `Phys DEF debuff`)
- Velara (87% `Magic DEF debuff` `Phys DEF debuff`)

### Summary for Fay

#### Damage types dealt by Fay

- Magic — Area

#### Debuffs provided by Fay

- Magic DEF — Multiple targets — `low`
- Phys DEF — Multiple targets — `low`

## Florabelle

### Florabelle's behavior

`AFK Stages [A]`, `Dream Realm [A+]`, `Dream Realm (Endless) [S]`, `PVP [C]`

- **Signature skill**: Pounding Blow (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `aoe-damage` `battle-start-burst` `summoner`
- **Damage types**: Physical `high`, Max HP-based damage `low`

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
Common buffers are **Twins** or **Mikola**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
- **Mehira**
  - Haste buff (single target, low) `signature fuel`
- **Kazim**
  - ATK buff (single target, average)
  - Haste buff (multiple targets, average) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, average, conditional (frequent))
  - Haste buff (multiple targets, low) `signature fuel`

### Units benefitting most from Florabelle

Florabelle provides Haste buff to summons `high`, Lifedrain buff to summons `high`, Shield (Mythic+) to summons `low`, and Summon damage buff (Supreme+) to summons `average`.

- Kazim (4.7 / 5)
- Berial (4.4 / 5)
- Aurora (4.3 / 5)
- Dunlingr (4.1 / 5)
- Cecia (3.9 / 5)
- Phraesto (3.7 / 5)
- Hodgkin (3.3 / 5)
- Bryon (3.2 / 5)
- Damian (2.9 / 5)

### Units that can act as a replacement for Florabelle

**Similar Skills**

- Dunlingr (66% `battle-start-burst` `summoner`)
- Atalanta (60% `aoe-damage` `battle-start-burst`)
- Bryon (57% `battle-start-burst` `summoner`)

**Damage**

- Himmel (100% `Physical` `Max HP-based damage`)
- Aliceth (100% `Physical` `Max HP-based damage`)
- Thador (100% `Physical` `Max HP-based damage`)

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

#### Skill overview

- **Signature skill (ult)**: speed `average`, damage `high`
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
Common buffers are **Mikola**, **Twins**, or **Smokey & Meerky**.

- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
- **Atalanta**
  - Haste buff (multiple targets, high, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) `signature fuel`
- **Kazim**
  - ATK buff (single target, average)
  - Haste buff (multiple targets, average) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, average) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, high)
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, average, conditional (frequent))
  - Haste buff (multiple targets, low) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`

### Units benefitting most from Frieren

- Bonnie (3.1 / 5)
- Shadewing (2.8 / 5)

### Units that can act as a replacement for Frieren

**Similar Skills**

- Dionel (48% `aoe-damage` `self-repositioner`)
- Marcille (41% `aoe-damage` `high-damage-ult`)
- Faramor (40% `aoe-damage` `dot-specialist`)

**Damage**

- Athalia (79% `True damage` `Max HP-based damage`)
- Sylphira (78% `Magic` `Max HP-based damage` `True damage`)
- Shemira (78% `Magic` `Max HP-based damage` `True damage`)

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
Common buffers are **Twins**, **Mikola**, or **Smokey & Meerky**.

- **Kazim**
  - ATK buff (single target, average)
  - Haste buff (multiple targets, average) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, average, conditional (frequent))
  - Haste buff (multiple targets, low) `signature fuel`
- **Atalanta**
  - Haste buff (multiple targets, high, conditional (frequent)) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, high)
  - Haste buff (single target, average) `signature fuel`
- **Ravion**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, average) `signature fuel`

### Units benefitting most from Galahad

Galahad provides Haste buff to single targets `average` and Shield to single targets `average`.

**15** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Bonnie (3.6 / 5)
- Velara (2.8 / 5)
- Aliceth (2.6 / 5)
- Faramor (2.1 / 5)
- Gwyneth (2.1 / 5)
- Mehira (1.8 / 5)
- Cyran (1.8 / 5)
- Sylphira (1.7 / 5)
- Kulu (1.7 / 5)
- Zanie (1.7 / 5)

### Units that can act as a replacement for Galahad

**Buffs on allies**

- Saida (100% `Shield`)
- Hepler (100% `Shield` `Haste`)
- Contess (89% `Shield`)

**Similar Skills**

- Phraesto (60% `ally-shielder` `aoe-damage` `clone`)
- Scarlita (50% `ally-shielder` `aoe-damage`)
- Gunnar (40% `ally-shielder` `aoe-damage`)

**Damage**

- Saida (100% `Magic` `Max HP-based damage`)
- Cryonaia (100% `Magic` `Max HP-based damage`)
- Marcille (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Zorya (64% `Movement speed debuff` `Haste debuff`)

**Crowd Control**

- Velara (100% `Bind`)
- Alna (100% `Bind`)
- Cyran (100% `Bind`)

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
Common buffers are **Twins** or **Koko**.

- **Hepler**
  - Shield (multiple targets, high)
- **Hugin**
  - Shield (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)
- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
- **Daimon**
  - Shield (multiple targets, average)

### Units benefitting most from Gerda

Gerda provides Direct healing to multiple targets `average`, Healing over time in an area `average`, and Direct healing (Mythic+) to single targets `low`.

- Himmel (2.3 / 5)
- Silven (1.8 / 5)
- Perseus (1.8 / 5)

### Units that can act as a replacement for Gerda

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

Look for units providing: `Healing` `Energy` `Physical DEF` `Magic DEF`  
Common buffers are **Mikola**, **Smokey & Meerky**, or **Rowan**.

- **Lucca**
  - DEF buff (area, high)
  - DEF buff (area, high)
- **Fay**
  - Direct healing (arc, average)
  - DEF buff (multiple targets, average)
  - DEF buff (multiple targets, average)
- **Sonja**
  - DEF buff (multiple targets, high)
  - DEF buff (multiple targets, high)
- **Hewynn**
  - Healing over time (all units, high)
- **Hepler**
  - Healing over time (multiple targets, high)
  - DEF buff (single target, low)
  - DEF buff (single target, low)

### Units benefitting most from Granny Dahnie

Granny Dahnie provides Haste buff (Supreme+) to single targets `low`.

- Shadewing (2.1 / 5)
- Indris (1.8 / 5)
- Nerion (1.6 / 5)

### Units that can act as a replacement for Granny Dahnie

**Buffs on allies**

- Galahad (100% `Haste`)
- Twins (100% `Haste`)
- Mehira (100% `Haste`)

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
Common buffers are **Mikola**, **Twins**, or **Koko**.

- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
- **Hewynn**
  - Healing over time (all units, high)
- **Lorsan**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
  - Direct healing (all units, low)
- **Atalanta**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) `signature fuel`
- **Fay**
  - ATK SPD buff (multiple targets, low) `signature fuel`
  - Direct healing (arc, average)

### Units benefitting most from Gunnar

Gunnar provides ATK SPD buff to single targets `low`, ATK buff to single targets `high`, Attack range buff to single targets `high`, Ranged DEF buff (Legendary+) to single targets `high`, and Vitality buff (Legendary+) to single targets `high`.

- Silven (2.7 / 5)
- Kulu (2.1 / 5)
- Zanie (2.1 / 5)
- Cyran (2.0 / 5)
- Himmel (1.9 / 5)
- Frieren (1.8 / 5)
- Gwyneth (1.4 / 5)
- Twins (1.1 / 5)

### Units that can act as a replacement for Gunnar

**Similar Skills**

- Galahad (40% `ally-shielder` `aoe-damage`)
- Hugin (40% `ally-shielder` `static-tile-buffer`)
- Himmel (28% `ally-shielder` `aoe-damage`)

**Damage**

- Baelran (100% `Physical` `Max HP-based damage`)
- Alna (100% `Physical` `Max HP-based damage` `DoT`)
- Thador (100% `Physical` `Max HP-based damage` `DoT`)

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
Common buffers are **Twins**, **Mikola**, or **Rowan**.

- **Galahad**
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Ravion**
  - Energy recovery (multiple targets, average) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, low) `signature fuel`
- **Thador**
  - Energy recovery (single target, low) `signature fuel`

### Units benefitting most from Gwyneth

- Carolina (2.2 / 5)
- Nerion (2.0 / 5)
- Shadewing (1.9 / 5)

### Units that can act as a replacement for Gwyneth

**Similar Skills**

- Mirael (96% `dot-specialist` `fire-attack`)
- Arden (60% `dot-specialist` `mass-cc`)
- Satrana (50% `dot-specialist` `fire-attack`)

**Damage**

- Frieren (100% `DoT` `Max HP-based damage`)
- Perseus (97% `Physical` `Max HP-based damage`)
- Atalanta (97% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Sinbad (100% `Phys DEF debuff` `Vitality debuff`)
- Cecia (100% `Phys DEF debuff` `Vitality debuff`)
- Hodgkin (100% `Phys DEF debuff` `Vitality debuff`)

**Crowd Control**

- Cyran (97% `Bind` `Silence`)
- Evie (97% `Bind` `Silence`)
- Atalanta (89% `Bind` `Stun`)

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
Common buffers are **Mikola**, **Smokey & Meerky**, or **Solise**.

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
- **Ludovic**
  - Direct healing (multiple targets, high)

### Units benefitting most from Hammie

Hammie provides ATK buff to multiple targets `average` and Direct healing to single targets `average`.

- Bonnie (2.4 / 5)
- Himmel (2.4 / 5)
- Silven (1.5 / 5)

### Units that can act as a replacement for Hammie

**Buffs on allies**

- Aliceth (100% `ATK`)
- Contess (100% `ATK`)
- Evie (100% `ATK`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Evie (100% `Direct healing` `Healing`)
- Fay (100% `Direct healing` `Healing`)

**Similar Skills**

- Damian (80% `ally-buffer` `ally-healer`)
- Isabella (80% `ally-buffer` `ally-healer`)
- Laios (66% `ally-buffer` `ally-healer`)

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
Common buffers are **Twins**, **Mikola**, or **Smokey & Meerky**.

- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, high)
  - Lifedrain buff (area, low, conditional (frequent))
- **Dunlingr**
  - Haste buff (single target, average) `signature fuel`
  - Lifedrain buff (all units, average)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)
- **Zanie**
  - Max HP buff (single target, high)
  - Direct healing (single target, high)

### Units benefitting most from Harak

Harak provides Invincible to single targets `high`.

- Indris (1.4 / 5)
- Silven (1.3 / 5)
- Perseus (1.3 / 5)

### Units that can act as a replacement for Harak

**Buffs on allies**

- Aurora (100% `Invincible`)
- Pandora (100% `Invincible`)

**Similar Skills**

- Seth (80% `assassin` `life-drain`)
- Salazer (60% `execute` `life-drain`)
- Nara (50% `assassin` `execute`)

**Damage**

- Aliceth (100% `Physical` `Max HP-based damage` `HP loss`)
- Faramor (100% `Physical` `HP loss`)
- Athalia (100% `Physical` `Max HP-based damage` `HP loss`)

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
- Invincibility — Single target

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
Common buffers are **Mikola**, **Twins**, or **Rowan**.

- **Sonja**
  - ATK buff (multiple targets, average)
  - DEF buff (multiple targets, high)
  - DEF buff (multiple targets, high)
- **Tilaya**
  - Max HP buff (area, average)
  - DEF buff (area, low)
  - DEF buff (area, low)
- **Fay**
  - ATK buff (multiple targets, low)
  - DEF buff (multiple targets, average)
  - DEF buff (multiple targets, average)
- **Kordan**
  - ATK buff (multiple targets, average)
  - DEF buff (single target, high)
  - DEF buff (single target, high)
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, high)

### Units benefitting most from Hepler

Hepler provides Haste buff to single targets `low`, Healing over time to multiple targets `high`, Shield to multiple targets `high`, and DEF buff (Supreme+) to single targets `low`.

**14** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Carolina (4.9 / 5)
- Lucius (4.8 / 5)
- Gunnar (4.5 / 5)
- Salazer (4.4 / 5)
- Ulmus (4.4 / 5)
- Antandra (4.4 / 5)
- Lumont (4.2 / 5)
- Lucca (4.1 / 5)
- Velara (4.1 / 5)
- Temesia (3.1 / 5)

### Units that can act as a replacement for Hepler

**Buffs on allies**

- Hugin (99% `Shield`)
- Saida (99% `Shield`)
- Salazer (92% `Shield`)

**Healing**

- Mikola (100% `Healing over time` `Healing`)
- Hewynn (100% `Healing over time` `Healing`)
- Solise (79% `Healing over time` `Healing`)

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
- Velara (100% `Haste debuff` `Magic DEF debuff`)
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
- Magic DEF (Supreme+) — Single target — `low`

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
Common buffers are **Mikola**, **Rowan**, or **Twins**.

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Ravion**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, average) `signature fuel`
  - Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, high)
  - ATK SPD buff (all units, low) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, average, conditional (frequent))
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Pandora**
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Hewynn

Hewynn provides Direct healing to single targets `high`, Healing over time to all units `high`, and Damage taken (Mythic+) to multiple targets `low`.

- Contess (3.9 / 5)
- Salazer (3.9 / 5)
- Gunnar (3.7 / 5)
- Lumont (3.3 / 5)
- Twins (3.3 / 5)
- Hodgkin (3.0 / 5)
- Viperian (3.0 / 5)
- Atalanta (2.9 / 5)
- Hammie (2.8 / 5)
- Lorsan (2.3 / 5)

### Units that can act as a replacement for Hewynn

**Buffs on allies**

- Koko (100% `Damage taken reduction`)
- Shakir (100% `Damage taken reduction`)
- Hugin (60% `Damage taken reduction`)

**Healing**

- Solise (100% `Healing over time` `Direct healing` `Healing`)

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
- **Behavior tags**: `ally-buffer` `ally-shielder` `aoe-damage` `battle-start-burst` `self-repositioner`
- **Damage types**: Physical `high`, Max HP-based damage `high`

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
  - Direct healing (multiple targets, low)
  - Enables Party composition via Support (party slot)
- **Gunnar**
  - ATK buff (single target, high)
  - Enables Party composition via Tank (party slot)
- **Velara**
  - Direct healing (area, low)
  - Enables Party composition via Support (party slot)
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - Enables Party composition via Mage (party slot)
- **Frieren**
  - Enables Party composition via Mage (party slot)

### Units benefitting most from Himmel

Himmel provides ATK buff to multiple targets `low`, Direct healing to single targets `low`, and Shield to single targets `average`.

- Velara (1.9 / 5)
- Baelran (1.8 / 5)
- Saida (1.4 / 5)

### Units that can act as a replacement for Himmel

**Buffs on allies**

- Contess (100% `ATK` `Shield`)
- Hugin (100% `ATK` `Shield`)
- Twins (84% `ATK` `Shield`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Twins (100% `Direct healing` `Healing`)

**Similar Skills**

- Igor (42% `aoe-damage` `battle-start-burst` `self-repositioner`)
- Perseus (40% `ally-buffer` `aoe-damage`)
- Gerda (37% `ally-shielder` `battle-start-burst` `self-repositioner`)

**Damage**

- Athalia (99% `Physical` `Max HP-based damage`)
- Perseus (97% `Physical` `Max HP-based damage`)
- Alna (94% `Physical` `Max HP-based damage`)

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
Common buffers are **Mikola**, **Smokey & Meerky**, or **Solise**.

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
- **Fay**
  - ATK buff (multiple targets, low)
  - Direct healing (arc, average)

### Units benefitting most from Hodgkin

- Indris (1.7 / 5)
- Bonnie (1.6 / 5)
- Aliceth (1.5 / 5)

### Units that can act as a replacement for Hodgkin

**Similar Skills**

- Cassadee (60% `aoe-damage` `enemy-debuffer`)
- Cecia (60% `enemy-debuffer` `summoner`)
- Florabelle (50% `aoe-damage` `summoner`)

**Damage**

- Himmel (100% `Physical` `Max HP-based damage`)
- Alna (100% `Physical` `Max HP-based damage`)
- Athalia (100% `Physical` `Max HP-based damage`)

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
- **Atalanta**
  - Haste buff (multiple targets, high, conditional (frequent)) `signature fuel`
- **Kazim**
  - Haste buff (multiple targets, average) `signature fuel`
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
- **Ravion**
  - Energy recovery (multiple targets, average) `signature fuel`

### Units benefitting most from Hugin

Hugin provides ATK buff to multiple targets `high`, Shield to multiple targets `high`, and Damage taken (Supreme+) to single targets `average`.

**18** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Kafra (4.8 / 5)
- Cryonaia (4.5 / 5)
- Faramor (4.4 / 5)
- Baelran (3.0 / 5)
- Callan (3.0 / 5)
- Temesia (2.9 / 5)
- Perseus (2.9 / 5)
- Lenya (2.7 / 5)
- Kordan (2.5 / 5)
- Silven (2.3 / 5)

### Units that can act as a replacement for Hugin

**Buffs on allies**

- Saida (59% `Shield`)
- Evie (57% `ATK`)
- Hepler (53% `Shield`)

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
- **Behavior tags**: `aoe-damage` `battle-start-burst` `invincibility` `self-repositioner` `untargetable`
- **Damage types**: Physical `high`

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
Common buffers are **Koko**, **Mikola**, or **Solise**.

- **Dunlingr**
  - Lifedrain buff (all units, average)
- **Hepler**
  - Healing over time (multiple targets, high)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)
- **Gerda**
  - Healing over time (area, average)

### Units benefitting most from Igor

- Shadewing (1.9 / 5)
- Indris (1.3 / 5)
- Aliceth (1.3 / 5)

### Units that can act as a replacement for Igor

**Similar Skills**

- Dionel (60% `aoe-damage` `self-repositioner` `untargetable`)
- Atalanta (60% `aoe-damage` `battle-start-burst` `self-repositioner`)
- Himmel (42% `aoe-damage` `battle-start-burst` `self-repositioner`)

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
Common buffers are **Mikola**, **Twins**, or **Rowan**.

Indris also requires units **putting debuffs** on enemies and/or units **putting multiple debuffs** on enemies

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via ATK debuff (all units)
- **Dunlingr**
  - ATK buff (single target, high)
  - ATK SPD buff (all units, low) `signature fuel`
  - Enables Multiple debuffs on target via 3 debuff types
  - Enables Debuff on target via Haste debuff (all units)
- **Lorsan**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via Haste debuff (area)
- **Alna**
  - ATK buff (single target, low)
  - Enables Multiple debuffs on target via 3 debuff types
  - Enables Debuff on target via Haste debuff (all units)
- **Kulu**
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via Damage taken debuff (all units)

### Units benefitting most from Indris

- Carolina (2.4 / 5)
- Nerion (2.2 / 5)
- Aliceth (1.5 / 5)

### Units that can act as a replacement for Indris

**Similar Skills**

- Temesia (40% `disabler` `enemy-debuffer`)
- Shadewing (33% `enemy-debuffer`)
- Reinier (33% `disabler`)

**Damage**

- Baelran (100% `Physical` `True damage` `Max HP-based damage`)
- Faramor (100% `Physical` `True damage`)
- Athalia (100% `Physical` `True damage` `Max HP-based damage`)

**Debuffs on enemies**

- Sinbad (80% `Phys DEF debuff` `Magic DEF debuff` `Damage taken debuff`)
- Fay (61% `Phys DEF debuff` `Magic DEF debuff`)
- Laios (61% `Phys DEF debuff` `Magic DEF debuff`)

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
- **Behavior tags**: `ally-buffer` `ally-healer` `life-drain`
- **Ally composition**: frontmost ally becomes companion (stat stacks and ult buffs)
- **Damage types**: Magic `low`

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
Common buffers are **Mikola**, **Smokey & Meerky**, or **Twins**.

- **Sonja**
  - ATK buff (multiple targets, average)
  - DEF buff (multiple targets, high)
  - DEF buff (multiple targets, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Dunlingr**
  - ATK buff (single target, high)
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, average) `signature fuel`
- **Eironn**
  - DEF buff (single target, high)
  - DEF buff (single target, high)
- **Kordan**
  - DEF buff (single target, high)
  - DEF buff (single target, high)

### Units benefitting most from Isabella

Isabella provides ATK buff to multiple targets `average` — conditional (frequent) and Haste buff (Supreme+) to multiple targets `low`.

- Marilee (2.6 / 5)
- Parisa (2.6 / 5)

### Units that can act as a replacement for Isabella

**Buffs on allies**

- Hugin (100% `ATK`)
- Evie (100% `ATK`)
- Mikola (100% `ATK` `Haste`)

**Similar Skills**

- Damian (60% `ally-buffer` `ally-healer`)
- Laios (50% `ally-buffer` `ally-healer`)
- Twins (48% `ally-buffer` `ally-healer`)

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
Common buffers are **Mikola**, **Twins**, or **Smokey & Meerky**.

- **Hugin**
  - ATK buff (multiple targets, high)
  - Shield (multiple targets, high)
- **Hepler**
  - Shield (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Saida**
  - Shield (multiple targets, high)
- **Contess**
  - ATK buff (single target, high)
  - Shield (single target, average)
- **Dunlingr**
  - ATK buff (single target, high)
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Kafra

- Shadewing (2.3 / 5)
- Indris (2.1 / 5)
- Nerion (1.8 / 5)

### Units that can act as a replacement for Kafra

**Similar Skills**

- Sinbad (90% `assassin` `enemy-debuffer` `mark-target`)
- Lenya (48% `assassin` `self-repositioner`)
- Silvina (40% `assassin` `mark-target`)

**Damage**

- Himmel (100% `Physical` `Max HP-based damage`)
- Thador (100% `Physical` `Max HP-based damage`)
- Athalia (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Eironn (91% `Haste debuff`)
- Lorsan (91% `Haste debuff`)
- Bonnie (83% `Haste debuff` `ATK debuff`)

**Crowd Control**

- Perseus (100% `Stun` `Knock back`)
- Scarlita (100% `Stun` `Knock back`)
- Cassadee (100% `Stun` `Knock back`)

### Summary for Kafra

#### Kafra Provides

- Marked target (focus fire) — Single target

#### Damage types dealt by Kafra

- Physical — Single target
- Max HP-based damage — Single target — `high`

#### Debuffs provided by Kafra

- Marked target (focus fire) — Single target — `average`
- Phys DEF — Single target — `high`
- ATK (Mythic+) — Single target — `low`
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
Common buffers are **Twins**, **Rowan**, or **Smokey & Meerky**.

Kazim also requires units **providing knock up**

- **Ulmus**
  - Energy recovery (single target, low) `signature fuel`
  - Enables Knock up from allies via Knock up + wide area (area)
- **Florabelle**
  - Enables Knock up from allies via Knock up + wide area (area)
- **Nerion**
  - Enables Knock up from allies via Knock up + wide area (area)
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Enables Knock up from allies via Knock up (area)
- **Lucca**
  - Enables Knock up from allies via Knock up (area)

### Units benefitting most from Kazim

Kazim provides Haste buff to multiple targets `average` and ATK buff (Mythic+) to single targets `average`.

- Lucy (3.4 / 5)
- Frieren (3.2 / 5)
- Galahad (2.7 / 5)

### Units that can act as a replacement for Kazim

**Buffs on allies**

- Aliceth (100% `ATK`)
- Kordan (100% `ATK`)
- Mikola (100% `ATK` `Haste`)

**Similar Skills**

- Sonja (57% `ally-buffer` `aoe-damage` `battle-start-burst` `mass-cc`)
- Walker (57% `aoe-damage` `battle-start-burst` `mark-target` `mass-cc`)
- Parisa (50% `ally-buffer` `aoe-damage` `mark-target`)

**Damage**

- Athalia (100% `Physical` `Max HP-based damage`)
- Galahad (100% `Max HP-based damage`)
- Kruger (100% `Physical` `Max HP-based damage`)

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
- Stacking buff — Single target

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
- **Behavior tags**: `ally-shielder` `life-drain`
- **Damage types**: Physical `low`

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
Common buffers are **Twins**, **Rowan**, or **Mikola**.

- **Ravion**
  - Energy recovery (multiple targets, average) `signature fuel`
  - Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - Shield (single target, average)
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Hugin**
  - Shield (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Koko

Koko provides Damage taken to all units `average`, Direct healing to all units `average`, Lifedrain buff to multiple targets `average`, Shield (Mythic+) to all units `low`, and Vitality buff (Supreme+) to single targets `low`.

**21** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Igor (5.0 / 5)
- Salazer (5.0 / 5)
- Ulmus (5.0 / 5)
- Callan (4.3 / 5)
- Zandrok (3.9 / 5)
- Gunnar (3.7 / 5)
- Harak (3.6 / 5)
- Talene (3.1 / 5)
- Perseus (3.1 / 5)
- Seth (2.6 / 5)

### Units that can act as a replacement for Koko

**Buffs on allies**

- Hugin (70% `Shield` `Damage taken reduction`)
- Twins (66% `Shield` `Vitality buff`)
- Daimon (62% `Shield` `Life Drain`)

**Healing**

- Solise (100% `Direct healing` `Healing`)
- Evie (100% `Direct healing` `Healing`)
- Ludovic (100% `Direct healing` `Healing`)

**Similar Skills**

- Saida (66% `ally-shielder` `life-drain`)
- Daimon (50% `ally-shielder` `life-drain`)
- Shakir (40% `life-drain`)

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
- **Behavior tags**: `hp-scaling` `self-repositioner`
- **Damage types**: Physical `high`, Max HP-based damage `high`

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
Common buffers are **Twins**, **Solise**, or **Mikola**.

- **Hugin**
  - ATK buff (multiple targets, high)
  - Shield (multiple targets, high)
- **Aliceth**
  - ATK buff (multiple targets, average)
  - DEF Penetration buff (multiple targets, high)
- **Ravion**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, average) `signature fuel`
  - Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Contess**
  - ATK buff (single target, high)
  - Shield (single target, average)
  - Direct healing (multiple targets, low)
- **Zanie**
  - Shield (single target, average)
  - Direct healing (single target, high)
  - DEF Penetration buff (single target, average)

### Units benefitting most from Kordan

Kordan provides ATK buff to multiple targets `average`, Lifedrain buff to multiple targets `low`, DEF buff (EX+10) to single targets `high`, and DEF Penetration buff (Supreme+) to multiple targets `low`.

- Carolina (4.7 / 5)
- Nerion (4.1 / 5)
- Lily May (2.9 / 5)
- Eironn (2.5 / 5)
- Brutus (2.2 / 5)
- Satrana (2.0 / 5)

### Units that can act as a replacement for Kordan

**Buffs on allies**

- Mikola (100% `ATK` `Magic DEF` `Physical DEF`)
- Talene (68% `ATK`)
- Sonja (68% `ATK` `Magic DEF` `Physical DEF`)

**Similar Skills**

- Pippa (100% `hp-scaling` `self-repositioner`)
- Athalia (66% `hp-scaling` `self-repositioner`)
- Marilee (66% `hp-scaling` `self-repositioner`)

**Damage**

- Athalia (100% `Physical` `Max HP-based damage` `HP loss`)
- Brutus (100% `Physical` `Max HP-based damage`)
- Nazrik (100% `Physical` `Max HP-based damage`)

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
Common buffers are **Twins**, **Mikola**, or **Rowan**.

- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, high)
- **Atalanta**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, average) `signature fuel`
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, average) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (all units, low) `signature fuel`

### Units benefitting most from Korin

Korin provides Shield to single targets `average`.

- Carolina (3.4 / 5)
- Nerion (3.3 / 5)
- Perseus (1.3 / 5)

### Units that can act as a replacement for Korin

**Buffs on allies**

- Contess (100% `Shield`)
- Galahad (100% `Shield`)
- Hugin (100% `Shield`)

**Similar Skills**

- Scarlita (80% `ally-shielder` `hp-scaling`)
- Daimon (50% `ally-shielder` `hp-scaling`)
- Silven (40% `hp-scaling`)

**Damage**

- Baelran (100% `True damage` `Physical` `Max HP-based damage`)
- Athalia (100% `True damage` `Physical` `Max HP-based damage`)
- Cyran (100% `True damage` `Max HP-based damage`)

**Crowd Control**

- Kordan (100% `Bind` `Knock back`)
- Eironn (96% `Bind`)
- Evie (72% `Bind`)

### Summary for Korin

#### Damage types dealt by Korin

- Physical — Area
- True damage — Single target — `average`

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
Common buffers are **Koko**, **Mikola**, or **Twins**.

- **Dunlingr**
  - Lifedrain buff (all units, average)
- **Daimon**
  - Shield (multiple targets, average)
  - Lifedrain buff (single target, average)
- **Hugin**
  - Shield (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)
- **Sonja**
  - DEF buff (multiple targets, high)

### Units benefitting most from Kruger

Kruger provides DEF buff (Legendary+) to single targets `average`.

- Indris (2.5 / 5)
- Aliceth (1.7 / 5)
- Silven (1.4 / 5)

### Units that can act as a replacement for Kruger

**Buffs on allies**

- Eironn (100% `Magic DEF` `Physical DEF`)
- Kordan (100% `Magic DEF` `Physical DEF`)
- Mikola (100% `Magic DEF` `Physical DEF`)

**Similar Skills**

- Shakir (48% `life-drain`)
- Shadewing (40% `enemy-debuffer`)
- Koko (40% `life-drain`)

**Damage**

- Kordan (100% `Physical` `Max HP-based damage`)
- Soren (100% `Physical` `Max HP-based damage`)
- Satrana (93% `Max HP-based damage`)

**Debuffs on enemies**

- Sinbad (56% `Phys DEF debuff` `Damage taken debuff`)

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
- Phys DEF — Single target — `low`
- Vulnerable — Area — `low`

#### Crowd Control provided by Kruger

- Knock down — Single target — `low`

## Kulu

### Kulu's behavior

`AFK Stages [A+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Demolition Zone (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `battle-start-burst` `battlefield-modification` `self-repositioner`
- **Damage types**: Physical `high`

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
Common buffers are **Twins** or **Mikola**.

- **Aliceth**
  - ATK buff (multiple targets, average)
  - DEF Penetration buff (multiple targets, high)
- **Dunlingr**
  - ATK buff (single target, high)
  - ATK SPD buff (all units, low) `signature fuel`
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Zanie**
  - DEF Penetration buff (single target, average)

### Units benefitting most from Kulu

Kulu provides DEF Penetration buff (EX+15) to single targets `low`.

- Bonnie (3.8 / 5)
- Indris (3.6 / 5)

### Units that can act as a replacement for Kulu

**Buffs on allies**

- Aliceth (100% `DEF Penetration`)
- Silven (100% `DEF Penetration`)
- Kordan (100% `DEF Penetration`)

**Similar Skills**

- Alsa (50% `battlefield-modification` `self-repositioner`)
- Atalanta (50% `battle-start-burst` `self-repositioner`)
- Zandrok (48% `battle-start-burst` `battlefield-modification`)

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
- Damage taken (Mythic+) — All units — `high`

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
Common buffers are **Mikola**, **Twins**, or **Smokey & Meerky**.

- **Dunlingr**
  - ATK buff (single target, high)
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, average) `signature fuel`
- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, high)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`
  - Direct healing (arc, average)

### Units benefitting most from Laios

Laios provides ATK buff to multiple targets `low` — conditional (rare) and DEF buff to single targets `low` — conditional (rare).

- Nerion (3.1 / 5)
- Shadewing (2.8 / 5)
- Indris (2.6 / 5)

### Units that can act as a replacement for Laios

**Similar Skills**

- Damian (100% `ally-buffer` `ally-healer` `summoner`)
- Isabella (50% `ally-buffer` `ally-healer`)
- Twins (40% `ally-buffer` `ally-healer`)

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
Common buffers are **Twins**, **Mikola**, or **Rowan**.

- **Hugin**
  - ATK buff (multiple targets, high)
  - Shield (multiple targets, high)
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Ravion**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, average) `signature fuel`
  - Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Shakir**
  - Haste buff (multiple targets, average) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, average) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`

### Units benefitting most from Lenya

- Carolina (2.2 / 5)
- Nerion (2.0 / 5)

### Units that can act as a replacement for Lenya

**Similar Skills**

- Soren (66% `counterattack` `self-repositioner`)
- Kafra (48% `assassin` `self-repositioner`)
- Pippa (36% `self-repositioner`)

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

#### Skill overview

- **Signature skill (ult)**: speed `average`, first cast speed `fast`, debuffs `average`, damage `average`
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
Common buffers are **Mikola**, **Twins**, or **Smokey & Meerky**.

- **Aliceth**
  - ATK buff (multiple targets, average)
  - DEF Penetration buff (multiple targets, high)
- **Kordan**
  - ATK buff (multiple targets, average)
  - DEF Penetration buff (multiple targets, low)
- **Dunlingr**
  - ATK buff (single target, high)
  - ATK SPD buff (all units, low) `signature fuel`
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
- **Ravion**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, average) `signature fuel`

### Units benefitting most from Lily May

Lily May provides DEF Penetration buff (Legendary+) to single targets `low`.

- Bonnie (2.5 / 5)
- Aliceth (2.0 / 5)
- Indris (1.7 / 5)

### Units that can act as a replacement for Lily May

**Buffs on allies**

- Aliceth (100% `DEF Penetration`)
- Silven (100% `DEF Penetration`)
- Kordan (100% `DEF Penetration`)

**Similar Skills**

- Athalia (60% `hp-scaling` `self-repositioner` `transformation`)
- Pippa (48% `hp-scaling` `self-repositioner`)
- Vala (40% `hp-scaling` `self-repositioner` `transformation`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

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
Common buffers are **Mikola**, **Twins**, or **Smokey & Meerky**.

- **Hewynn**
  - Healing over time (all units, high)
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Dunlingr**
  - ATK buff (single target, high)
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Lorsan

Lorsan provides Haste buff to single targets `high` and Direct healing (Mythic+) to all units `low`.

- Indris (3.8 / 5)
- Viperian (3.2 / 5)
- Pippa (2.8 / 5)

### Units that can act as a replacement for Lorsan

**Buffs on allies**

- Twins (90% `Haste`)
- Atalanta (81% `Haste`)
- Shakir (68% `Haste`)

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

- Haste — Area — `high`
- Max HP (Supreme+) — Single target — `average`

#### Crowd Control provided by Lorsan

- Unaffected (Supreme+) — Self — On skill
- Stun (Mythic+) — Multiple targets — `high`

## Lucca

### Lucca's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Quake Slam (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `ally-shielder` `disabler` `mass-cc`
- **Ally composition**: place adjacent allies behind at battle prep (DEF buff)
- **Ally composition**: place allies on adjacent tiles behind at battle start (shields and ATK boost)
- **Damage types**: Physical `high`

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
Common buffers are **Mikola**, **Twins**, or **Koko**.

- **Hepler**
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
  - DEF buff (single target, low)
  - DEF buff (single target, low)
- **Fay**
  - Direct healing (arc, average)
  - DEF buff (multiple targets, average)
  - DEF buff (multiple targets, average)
- **Sonja**
  - DEF buff (multiple targets, high)
  - DEF buff (multiple targets, high)
- **Tilaya**
  - Max HP buff (area, average)
  - DEF buff (area, low)
  - DEF buff (area, low)
- **Scarlita**
  - Shield (single target, average)
  - DEF buff (single target, high)
  - DEF buff (single target, high)

### Units benefitting most from Lucca

Lucca provides DEF buff in an area `high`.

- Cecia (5.0 / 5)
- Granny Dahnie (4.6 / 5)
- Natsu (3.9 / 5)

### Units that can act as a replacement for Lucca

**Similar Skills**

- Antandra (48% `ally-shielder` `mass-cc`)
- Sylphira (40% `disabler` `mass-cc`)
- Temesia (40% `disabler` `mass-cc`)

**Damage**

- Himmel (100% `Physical` `Max HP-based damage`)
- Alna (100% `Physical` `Max HP-based damage`)
- Athalia (100% `Physical` `Max HP-based damage`)

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
Common buffers are **Mikola**, **Rowan**, or **Smokey & Meerky**.

- **Hepler**
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Pandora**
  - Direct healing (single target, high)
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Ravion**
  - Energy recovery (multiple targets, average) `signature fuel`
  - Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Hugin**
  - Shield (multiple targets, high)

### Units benefitting most from Lucius

Lucius provides Shield in an area `low`.

- Shadewing (1.9 / 5)
- Nerion (1.7 / 5)
- Perseus (1.4 / 5)

### Units that can act as a replacement for Lucius

**Buffs on allies**

- Hugin (100% `Shield`)
- Saida (100% `Shield`)
- Daimon (100% `Shield`)

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
Common buffers are **Twins** or **Mikola**.

- **Atalanta**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, average) `signature fuel`
- **Kazim**
  - ATK SPD via Haste buff (multiple targets, average) `signature fuel`
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, average) `signature fuel`
- **Valka**
  - ATK SPD buff (multiple targets, average) `signature fuel`

### Units benefitting most from Lucy

Lucy provides Shield (Mythic+) to single targets `high` and DEF buff (EX+10) to single targets `high`.

- Nerion (2.1 / 5)
- Silven (1.9 / 5)
- Perseus (1.7 / 5)

### Units that can act as a replacement for Lucy

**Buffs on allies**

- Scarlita (62% `Shield` `Magic DEF` `Physical DEF`)
- Kordan (52% `Magic DEF` `Physical DEF`)
- Hepler (50% `Shield` `Magic DEF` `Physical DEF`)

**Similar Skills**

- Lucca (66% `ally-shielder` `mass-cc`)
- Antandra (50% `ally-shielder` `mass-cc`)
- Ulmus (48% `ally-shielder` `mass-cc`)

**Damage**

- Marcille (100% `Magic` `Max HP-based damage`)
- Galahad (99% `Magic` `Max HP-based damage`)
- Saida (98% `Magic` `Max HP-based damage`)

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
Common buffers are **Solise**, **Twins**, or **Mikola**.

- **Evie**
  - Direct healing (single target, high)
- **Zanie**
  - Direct healing (single target, high)
- **Velara**
  - Direct healing (area, low)
- **Contess**
  - Direct healing (multiple targets, low)
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Ludovic

Ludovic provides Direct healing in an area `low`, Healing over time to single targets `high`, Direct healing (Mythic+) to multiple targets `high`, and Healing over time (EX+10) to single targets `low`.

- Evie (2.7 / 5)

### Units that can act as a replacement for Ludovic

**Healing**

- Solise (100% `Direct healing` `Healing over time` `Healing`)
- Evie (100% `Direct healing` `Healing`)
- Smokey & Meerky (100% `Direct healing` `Healing`)

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
Common buffers are **Mikola**, **Twins**, or **Smokey & Meerky**.

- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Hewynn**
  - Healing over time (all units, high)
- **Atalanta**
  - Haste buff (multiple targets, high, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) `signature fuel`
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
  - Direct healing (all units, low)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Hugin**
  - Shield (multiple targets, high)

### Units benefitting most from Lumont

Lumont provides DEF buff to multiple targets `average`.

- Cecia (3.0 / 5)
- Nerion (2.0 / 5)
- Silven (1.8 / 5)

### Units that can act as a replacement for Lumont

**Buffs on allies**

- Kordan (100% `Magic DEF` `Physical DEF`)
- Mikola (100% `Magic DEF` `Physical DEF`)
- Sonja (100% `Magic DEF` `Physical DEF`)

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
- **Behavior tags**: `ally-buffer` `battle-start-burst` `energy-provider`
- **Damage types**: Physical `average`

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
Common buffers are **Twins**, **Rowan**, or **Mikola**.

- **Lyca**
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Valka**
  - ATK SPD buff (multiple targets, average) `signature fuel`
- **Ravion**
  - Energy recovery (multiple targets, average) `signature fuel`
  - Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
- **Pandora**
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Lyca

Lyca provides ATK SPD buff to all units `low` and Energy recovery to all units `low`.

**12** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight
- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Indris (5.0 / 5)
- Rhys (4.5 / 5)
- Hewynn (3.8 / 5)
- Fay (3.8 / 5)
- Sinbad (3.3 / 5)
- Alsa (3.0 / 5)
- Lyca (3.0 / 5)
- Mirael (2.9 / 5)
- Zorya (2.9 / 5)
- Odie (2.6 / 5)

### Units that can act as a replacement for Lyca

**Buffs on allies**

- Ravion (72% `Energy`)
- Smokey & Meerky (50% `Energy`)
- Rowan (50% `Energy`)

**Similar Skills**

- Twins (40% `ally-buffer` `energy-provider`)
- Himmel (33% `ally-buffer` `battle-start-burst`)
- Sonja (33% `ally-buffer` `battle-start-burst`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Laios (71% `Phys DEF debuff`)
- Kafra (67% `Phys DEF debuff` `ATK debuff`)
- Zanie (51% `Phys DEF debuff` `ATK debuff`)

**Crowd Control**

- Phraesto (100% `Stun`)
- Callan (100% `Stun`)
- Zandrok (100% `Stun`)

### Summary for Lyca

#### Damage types dealt by Lyca

- Physical — All units, Area, Single target

#### Debuffs provided by Lyca

- ATK — All units — `high`
- Phys DEF — All units — `average`

#### Crowd Control provided by Lyca

- Stun (EX+10) — Single target — `average`

## Marcille

### Marcille's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Silver-White Wings that Streak Across the Skies (ultimate)
- **Movement**: stationary (no finite attack range)
- **Behavior tags**: `ally-healer` `aoe-damage` `high-damage-ult` `revive` `summoner`
- **Ally composition**: place ally 1 tile in front at battle prep (revive target)
- **Damage types**: Magic `high`, Max HP-based damage `high`

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
Common buffers are **Mikola**, **Smokey & Meerky**, or **Twins**.

- **Ludovic**
  - Direct healing (multiple targets, high)
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, average) `signature fuel`
- **Evie**
  - Direct healing (single target, high)
- **Pandora**
  - Direct healing (single target, high)
- **Zanie**
  - Direct healing (single target, high)

### Units benefitting most from Marcille

Marcille provides Direct healing (Mythic+) to multiple targets `high`.

- Himmel (2.4 / 5)
- Silven (1.5 / 5)
- Perseus (1.5 / 5)

### Units that can act as a replacement for Marcille

**Healing**

- Solise (100% `Direct healing` `Healing`)
- Evie (100% `Direct healing` `Healing`)
- Smokey & Meerky (100% `Direct healing` `Healing`)

**Similar Skills**

- Frieren (41% `aoe-damage` `high-damage-ult`)
- Florabelle (40% `aoe-damage` `summoner`)
- Laios (40% `ally-healer` `summoner`)

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
- **Behavior tags**: `hp-scaling` `mass-cc` `self-repositioner`
- **Damage types**: Physical `average`, True damage `low`

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
Common buffers are **Mikola**, **Twins**, or **Smokey & Meerky**.

- **Dunlingr**
  - ATK buff (single target, high)
  - ATK SPD buff (all units, low) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, average, conditional (frequent))
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (all units, low) `signature fuel`
- **Valka**
  - ATK SPD buff (multiple targets, average) `signature fuel`
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`

### Units benefitting most from Marilee

- Carolina (1.5 / 5)
- Nerion (1.4 / 5)

### Units that can act as a replacement for Marilee

**Similar Skills**

- Pippa (80% `hp-scaling` `self-repositioner`)
- Kordan (66% `hp-scaling` `self-repositioner`)
- Athalia (60% `hp-scaling` `self-repositioner`)

**Damage**

- Baelran (100% `Physical` `Max HP-based damage` `True damage`)
- Faramor (100% `Physical` `True damage`)
- Athalia (100% `Physical` `Max HP-based damage` `True damage`)

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
- **Behavior tags**: `aoe-damage` `enemy-grouping` `life-drain` `mass-cc` `summoner` `untargetable`
- **Damage types**: Magic `low`, DoT `average`, HP loss `average`, Max HP-based damage `average`

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
Common buffers are **Twins**, **Solise**, or **Mikola**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Velara**
  - Direct healing (area, low)
- **Contess**
  - Direct healing (multiple targets, low)
- **Himmel**
  - Direct healing (single target, low)

### Units benefitting most from Mehira

Mehira provides Haste buff to single targets `low`.

- Gwyneth (1.6 / 5)
- Zanie (1.3 / 5)
- Aurora (1.3 / 5)
- Florabelle (1.3 / 5)
- Ravion (1.3 / 5)

### Units that can act as a replacement for Mehira

**Buffs on allies**

- Galahad (100% `Haste`)
- Twins (100% `Haste`)
- Dunlingr (100% `Haste`)

**Similar Skills**

- Eironn (51% `aoe-damage` `enemy-grouping` `mass-cc`)
- Sonja (37% `aoe-damage` `life-drain` `mass-cc`)
- Cyran (30% `aoe-damage` `enemy-grouping`)

**Damage**

- Zorya (100% `Magic` `Max HP-based damage` `HP loss`)
- Dunlingr (98% `DoT` `Magic` `Max HP-based damage` `HP loss`)
- Ravion (81% `Max HP-based damage` `HP loss`)

**Debuffs on enemies**

- Contess (100% `Damage taken debuff`)
- Himmel (100% `Damage taken debuff`)
- Kulu (100% `Damage taken debuff`)

**Crowd Control**

- Satrana (90% `Charm`)

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

## Mikola

### Mikola's behavior

`AFK Stages [B]`, `Dream Realm [B]`, `Dream Realm (Endless) [A]`, `PVP [A]`

- **Signature skill**: Dauntless Hymn (ultimate)
- **Movement**: moving (avg attack range 2.0 tiles)
- **Behavior tags**: `ally-buffer` `aoe-healing`
- **Damage types**: Physical `low`

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

Look for units providing: `ATK` `Haste` `Healing`  
Common buffers are **Twins**, **Smokey & Meerky**, or **Rowan**.

- **Shakir**
  - Haste buff (multiple targets, average) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, average) `signature fuel`
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Dunlingr**
  - ATK buff (single target, high)
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
- **Ravion**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, average) `signature fuel`
  - Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Pandora**
  - Direct healing (single target, high)
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Mikola

Mikola provides ATK buff to all units `high`, DEF buff to multiple targets `average`, Direct healing to multiple targets `low`, Haste buff to multiple targets `average`, Healing over time to all units `high`, and Vitality buff (EX+10) to multiple targets `high`.

**70** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Damian (5.0 / 5)
- Hammie (5.0 / 5)
- Isabella (5.0 / 5)
- Laios (5.0 / 5)
- Lorsan (5.0 / 5)
- Perseus (5.0 / 5)
- Seth (5.0 / 5)
- Tasi (5.0 / 5)
- Temesia (5.0 / 5)
- Vala (5.0 / 5)

### Units that can act as a replacement for Mikola

**Buffs on allies**

- Evie (95% `ATK`)
- Hugin (60% `ATK`)
- Talene (56% `ATK`)

**Healing**

- Solise (100% `Healing over time` `Direct healing` `Healing`)
- Hepler (100% `Healing over time` `Healing`)
- Hewynn (100% `Healing over time` `Direct healing` `Healing`)

**Similar Skills**

- Smokey & Meerky (48% `aoe-healing`)
- Ludovic (40% `aoe-healing`)
- Fay (40% `aoe-healing`)

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
Common buffers are **Twins**, **Mikola**, or **Rowan**.

- **Atalanta**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (all units, low) `signature fuel`
- **Valka**
  - ATK SPD buff (multiple targets, average) `signature fuel`
- **Lorsan**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Mirael

- Shadewing (1.7 / 5)
- Bonnie (1.6 / 5)
- Himmel (1.5 / 5)

### Units that can act as a replacement for Mirael

**Similar Skills**

- Gwyneth (96% `dot-specialist` `fire-attack`)
- Satrana (66% `dot-specialist` `fire-attack`)
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

#### Skill overview

- **Signature skill**: speed `fast`, damage `low`
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
Common buffers are **Smokey & Meerky**, **Rowan**, or **Twins**.

- **Ravion**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, average) `signature fuel`
- **Lyca**
  - Energy recovery (all units, low) `signature fuel`
- **Thoran**
  - Energy recovery (single target, average) `signature fuel`
- **Arden**
  - Energy recovery (single target, low) `signature fuel`
- **Thador**
  - Energy recovery (single target, low) `signature fuel`

### Units benefitting most from Nara

Nara provides Direct healing (Mythic+) in an area `low`.

- Aliceth (2.0 / 5)
- Nerion (1.8 / 5)
- Indris (1.6 / 5)

### Units that can act as a replacement for Nara

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Twins (100% `Direct healing` `Healing`)

**Similar Skills**

- Harak (50% `assassin` `execute`)
- Ludovic (30% `ally-healer`)
- Smokey & Meerky (25% `ally-healer`)

**Damage**

- Valka (95% `True damage` `Physical` `Max HP-based damage`)
- Athalia (84% `Physical` `True damage` `Max HP-based damage` `HP loss`)
- Vala (71% `True damage` `Physical` `Max HP-based damage` `HP loss`)

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

- **Signature skill**: Lightning Fire Dragon's Roar/Fire Dragon King's Roar (ultimate)
- **Movement**: moving (avg attack range 3.0 tiles)
- **Behavior tags**: `aoe-damage` `dot-specialist` `fire-attack` `high-damage-ult` `mass-cc` `transformation`
- **Damage types**: Magic `high`, Max HP-based damage `high`

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
Common buffers are **Mikola**, **Twins**, or **Rowan**.

- **Lucca**
  - DEF buff (area, high)
  - DEF buff (area, high)
- **Sonja**
  - ATK buff (multiple targets, average)
  - DEF buff (multiple targets, high)
  - DEF buff (multiple targets, high)
- **Fay**
  - ATK buff (multiple targets, low)
  - DEF buff (multiple targets, average)
  - DEF buff (multiple targets, average)
- **Kordan**
  - ATK buff (multiple targets, average)
  - DEF buff (single target, high)
  - DEF buff (single target, high)
- **Lumont**
  - DEF buff (multiple targets, average)
  - DEF buff (multiple targets, average)

### Units benefitting most from Natsu

- Bonnie (2.5 / 5)
- Shadewing (2.1 / 5)
- Nerion (2.0 / 5)

### Units that can act as a replacement for Natsu

**Similar Skills**

- Frieren (61% `aoe-damage` `dot-specialist` `high-damage-ult`)
- Arden (60% `aoe-damage` `dot-specialist` `mass-cc`)
- Gwyneth (60% `dot-specialist` `fire-attack` `mass-cc`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Marcille (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Lorsan (72% `Haste debuff` `Max HP debuff`)
- Galahad (65% `Haste debuff`)
- Alna (63% `Haste debuff` `Max HP debuff`)

**Crowd Control**

- Antandra (100% `Stun` `Knock down`)
- Callan (100% `Stun` `Knock down`)
- Lucca (100% `Stun` `Knock down`)

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

- **Seth**
  - Crit buff (single target, low)

### Units benefitting most from Nazrik

- Shadewing (1.9 / 5)
- Indris (1.8 / 5)
- Nerion (1.8 / 5)

### Units that can act as a replacement for Nazrik

**Similar Skills**

- Silven (100% `hp-scaling` `mark-target`)
- Aliceth (48% `hp-scaling` `mark-target`)
- Kordan (40% `hp-scaling`)

**Damage**

- Frieren (100% `True damage` `Max HP-based damage`)
- Athalia (100% `True damage` `Physical` `Max HP-based damage`)
- Valka (100% `True damage` `Physical` `Max HP-based damage`)

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
Common buffers are **Twins**, **Koko**, or **Rowan**.

Nerion also requires units **applying crowd control** to enemies

- **Eironn**
  - Enables CC on enemies via Bind (area, high)
- **Kordan**
  - Enables CC on enemies via Bind (area, high)
- **Aliceth**
  - DEF Penetration buff (multiple targets, high)
  - Enables CC on enemies via Blind (area, average)
- **Callan**
  - Enables CC on enemies via Stun (all units, average)
- **Alna**
  - Enables CC on enemies via Bind (area, average)

### Units benefitting most from Nerion

- Kazim (4.7 / 5)

### Units that can act as a replacement for Nerion

**Similar Skills**

- Shadewing (96% `dot-specialist` `enemy-debuffer`)
- Carolina (72% `dot-specialist` `enemy-debuffer`)
- Bonnie (48% `battle-start-burst` `enemy-debuffer`)

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
Common buffers are **Mikola**, **Solise**, or **Smokey & Meerky**.

Niru also requires a unit **to bless** and/or enemies **to be defeated**

- **Sonja**
  - DEF buff (multiple targets, high)
  - DEF buff (multiple targets, high)
- **Eironn**
  - DEF buff (single target, high)
  - DEF buff (single target, high)
- **Kordan**
  - DEF buff (single target, high)
  - DEF buff (single target, high)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)

### Units benefitting most from Niru

- Bonnie (2.3 / 5)
- Shadewing (1.9 / 5)
- Zorya (1.6 / 5)

### Units that can act as a replacement for Niru

**Similar Skills**

- Ludovic (36% `ally-healer`)
- Smokey & Meerky (30% `ally-healer`)
- Rowan (30% `ally-healer`)

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

#### Skill overview

- **Signature skill**: speed `fast`, debuffs `average`
- **Ultimate**: speed `average`, debuffs `average`, damage `low`
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
Common buffers are **Twins** or **Mikola**.

- **Valka**
  - ATK SPD buff (multiple targets, average) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, average) `signature fuel`

### Units benefitting most from Odie

- Bonnie (2.2 / 5)
- Shadewing (2.1 / 5)
- Indris (1.6 / 5)

### Units that can act as a replacement for Odie

**Similar Skills**

- Mirael (40% `dot-specialist`)
- Shadewing (33% `dot-specialist`)
- Lorsan (33% `dot-specialist`)

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
Common buffers are **Rowan**, **Smokey & Meerky**, or **Twins**.

- **Ravion**
  - Energy recovery (multiple targets, average) `signature fuel`
- **Thoran**
  - Energy recovery (single target, average) `signature fuel`
- **Thador**
  - Energy recovery (single target, low) `signature fuel`
- **Lyca**
  - Energy recovery (all units, low) `signature fuel`
- **Arden**
  - Energy recovery (single target, low) `signature fuel`

### Units benefitting most from Pandora

Pandora provides Direct healing to single targets `high`, Invincible to single targets `high`, and Max HP buff (Legendary+) to single targets `average`.

- Nerion (2.8 / 5)
- Indris (2.4 / 5)
- Silven (2.0 / 5)

### Units that can act as a replacement for Pandora

**Buffs on allies**

- Aurora (100% `Invincible`)
- Harak (80% `Invincible`)

**Healing**

- Solise (100% `Direct healing` `Healing`)
- Evie (100% `Direct healing` `Healing`)
- Ludovic (100% `Direct healing` `Healing`)

**Similar Skills**

- Thador (50% `enemy-debuffer` `energy-provider`)
- Cecia (50% `enemy-debuffer` `mass-cc`)
- Carolina (50% `enemy-debuffer` `mass-cc`)

**Damage**

- Faramor (100% `DoT` `HP loss`)
- Dunlingr (79% `DoT` `HP loss`)
- Contess (78% `HP loss`)

**Debuffs on enemies**

- Alna (62% `Haste debuff` `Vitality debuff`)
- Velara (50% `Haste debuff`)
- Dunlingr (50% `Haste debuff` `Vitality debuff`)

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
Common buffers are **Mikola**, **Twins**, or **Smokey & Meerky**.

- **Aliceth**
  - ATK buff (multiple targets, average)
  - DEF Penetration buff (multiple targets, high)
- **Shakir**
  - Haste buff (multiple targets, average) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, average) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, high)
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, average, conditional (frequent))
  - Haste buff (multiple targets, low) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Kordan**
  - ATK buff (multiple targets, average)
  - DEF Penetration buff (multiple targets, low)

### Units benefitting most from Pang

Pang provides Shield to single targets `average` and DEF Penetration buff (Supreme+) to single targets `low`.

- Nerion (1.7 / 5)
- Perseus (1.4 / 5)
- Silven (1.3 / 5)

### Units that can act as a replacement for Pang

**Buffs on allies**

- Galahad (100% `Shield`)
- Saida (100% `Shield`)
- Zanie (100% `Shield` `DEF Penetration`)

**Similar Skills**

- Hepler (66% `ally-shielder` `transformation`)
- Ulmus (48% `ally-shielder` `transformation`)
- Baelran (33% `transformation`)

**Damage**

- Himmel (100% `Physical` `Max HP-based damage`)
- Aliceth (100% `Physical` `Max HP-based damage`)
- Athalia (100% `Physical` `Max HP-based damage`)

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

#### Skill overview

- **Signature skill (ult)**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `average`

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
Common buffers are **Mikola**, **Twins**, or **Smokey & Meerky**.

- **Dunlingr**
  - ATK buff (single target, high)
  - ATK SPD buff (all units, low) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, average, conditional (frequent))
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (all units, low) `signature fuel`
- **Ravion**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, average) `signature fuel`
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`

### Units benefitting most from Parisa

- Bonnie (1.6 / 5)
- Niru (1.5 / 5)
- Himmel (1.5 / 5)

### Units that can act as a replacement for Parisa

**Similar Skills**

- Perseus (66% `ally-buffer` `aoe-damage`)
- Cassadee (60% `ally-buffer` `aoe-damage`)
- Faramor (48% `ally-buffer` `aoe-damage`)

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
Common buffers are **Mikola**, **Twins**, or **Smokey & Meerky**.

Perseus also requires units **buffing them**

- **Hugin**
  - ATK buff (multiple targets, high)
  - Shield (multiple targets, high)
  - Grants 3 distinct stat buffs to Perseus
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
  - Grants 5 distinct stat buffs to Perseus (start of battle)
- **Dunlingr**
  - ATK buff (single target, high)
  - ATK SPD buff (all units, low) `signature fuel`
  - Grants 4 distinct stat buffs to Perseus
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, high)
  - Grants 3 distinct stat buffs to Perseus
- **Alna**
  - ATK buff (single target, low)
  - Max HP buff (single target, high)
  - Grants 4 distinct stat buffs to Perseus (start of battle)

### Units benefitting most from Perseus

Perseus provides ATK buff to multiple targets `low`.

- Carolina (3.4 / 5)
- Nerion (3.1 / 5)
- Shadewing (1.9 / 5)

### Units that can act as a replacement for Perseus

**Buffs on allies**

- Gunnar (100% `ATK`)
- Contess (100% `ATK`)
- Himmel (100% `ATK`)

**Similar Skills**

- Cassadee (80% `ally-buffer` `aoe-damage`)
- Parisa (66% `ally-buffer` `aoe-damage`)
- Faramor (60% `ally-buffer` `aoe-damage`)

**Damage**

- Aliceth (100% `Physical` `Max HP-based damage`)
- Athalia (100% `Physical` `Max HP-based damage`)
- Gwyneth (100% `Physical` `Max HP-based damage`)

**Crowd Control**

- Atalanta (100% `Stun` `Knock back`)
- Soren (95% `Stun` `Knock back`)
- Scarlita (94% `Stun` `Knock back`)

### Summary for Perseus

#### Damage types dealt by Perseus

- Physical — Area, Single target
- Max HP-based damage — Area, Single target — `average`

#### Crowd Control provided by Perseus

- Unaffected — Single target — On skill
- Knock back — Area — `low`
- Stun — Area — `average`

## Phraesto

### Phraesto's behavior

`AFK Stages [A+]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Crimson Contract (Skill 1)
- **Movement**: moving (avg attack range 1.8 tiles)
- **Behavior tags**: `ally-shielder` `aoe-damage` `clone` `energy-provider` `summoner`
- **Ally composition**: place allies 1 tile behind this hero and the Illusion for contract buffs
- **Self placement**: keep this hero and Illusion in the same row (damage reduction and battle-start shields)
- **Damage types**: Magic `high`

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
Common buffers are **Solise**, **Twins**, or **Mikola**.

- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)
  - Shield (summons only, low)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Hugin**
  - Shield (multiple targets, high)
- **Kordan**
  - DEF buff (single target, high)
  - DEF buff (single target, high)
- **Saida**
  - Shield (multiple targets, high)

### Units benefitting most from Phraesto

Phraesto provides Damage taken to single targets `low` and Max HP buff to single targets `high`.

- Nerion (2.0 / 5)
- Himmel (1.9 / 5)
- Shadewing (1.9 / 5)

### Units that can act as a replacement for Phraesto

**Similar Skills**

- Galahad (60% `ally-shielder` `aoe-damage` `clone`)
- Gunnar (41% `ally-shielder` `aoe-damage`)
- Thador (40% `ally-shielder` `energy-provider`)

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
- **Behavior tags**: `hp-scaling` `self-repositioner`
- **Damage types**: Magic `average`, Max HP-based damage `high`, True damage `low`

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
Common buffers are **Twins** or **Mikola**.

- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Dunlingr**
  - Haste buff (single target, average) `signature fuel`
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
- **Isabella**
  - Haste buff (multiple targets, low) `signature fuel`

### Units benefitting most from Pippa

- Carolina (3.4 / 5)
- Nerion (3.1 / 5)
- Shadewing (1.9 / 5)

### Units that can act as a replacement for Pippa

**Similar Skills**

- Kordan (100% `hp-scaling` `self-repositioner`)
- Athalia (80% `hp-scaling` `self-repositioner`)
- Marilee (80% `hp-scaling` `self-repositioner`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage` `True damage`)
- Shemira (100% `Magic` `Max HP-based damage` `True damage`)
- Sylphira (100% `Magic` `Max HP-based damage` `True damage`)

**Debuffs on enemies**

- Saida (100% `Energy drain`)
- Dunlingr (100% `Energy drain`)
- Lily May (100% `Energy drain`)

**Crowd Control**

- Eironn (98% `Bind` `Displace`)
- Arden (92% `Bind`)
- Indris (86% `Bind`)

### Summary for Pippa

#### Damage types dealt by Pippa

- Magic — Single target
- Max HP-based damage — Single target — `average`
- True damage — Area — `low`

#### Debuffs provided by Pippa

- Energy drain — Single target — `low`

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
Common buffers are **Twins**, **Mikola**, or **Smokey & Meerky**.

- **Galahad**
  - Haste buff (single target, average) `signature fuel`
- **Mehira**
  - Haste buff (single target, low) `signature fuel`
- **Thador**
  - Energy recovery (single target, low) `signature fuel`
- **Kazim**
  - ATK buff (single target, average)
  - Haste buff (multiple targets, average) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, average, conditional (frequent))
  - Haste buff (multiple targets, low) `signature fuel`

### Units benefitting most from Ravion

Ravion provides ATK buff to multiple targets `low`, Energy recovery to multiple targets `average`, Lifedrain buff (EX+10) to single targets `low` — conditional (rare), and Shield (EX+10) to single targets `low` — conditional (rare).

**16** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Arden (3.8 / 5)
- Valen (3.8 / 5)
- Cryonaia (3.4 / 5)
- Hewynn (3.4 / 5)
- Nara (3.0 / 5)
- Shadewing (2.7 / 5)
- Koko (2.7 / 5)
- Vala (2.4 / 5)
- Sylphira (2.1 / 5)
- Kordan (2.1 / 5)

### Units that can act as a replacement for Ravion

**Buffs on allies**

- Smokey & Meerky (100% `ATK` `Energy`)
- Kordan (68% `ATK`)
- Talene (68% `ATK`)

**Similar Skills**

- Thador (60% `ally-shielder` `energy-provider`)
- Hugin (50% `ally-shielder` `energy-provider`)
- Twins (40% `ally-shielder` `energy-provider`)

**Damage**

- Athalia (100% `Physical` `Max HP-based damage` `HP loss`)
- Nara (100% `Physical` `Max HP-based damage` `HP loss`)
- Vala (100% `Physical` `Max HP-based damage` `HP loss`)

**Debuffs on enemies**

- Zanie (100% `Phys DEF debuff` `ATK debuff`)
- Lyca (100% `Phys DEF debuff` `ATK debuff`)
- Sinbad (90% `Phys DEF debuff` `ATK debuff`)

**Crowd Control**

- Cyran (100% `Displace` `Knock down`)
- Reinier (100% `Displace` `Knock down`)
- Nara (100% `Displace` `Knock down`)

### Summary for Ravion

#### Damage types dealt by Ravion

- Physical — Area, Single target
- HP loss — Single target — `low`
- Max HP-based damage — Single target — `average`

#### Debuffs provided by Ravion

- ATK — Single target — `low`
- Phys DEF — Single target — `average`

#### Crowd Control provided by Ravion

- Unaffected — Self — On skill
- Displace — Single target — `low`
- Knock down — Single target — `low`

## Reinier

### Reinier's behavior

`AFK Stages [B]`, `Dream Realm [S]`, `Dream Realm (Endless) [A]`, `PVP [B]`

- **Signature skill**: Dynamic Balance (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Behavior tags**: `battle-start-burst` `disabler`
- **Damage types**: Magic `average`

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
Common buffers are **Solise**, **Twins**, or **Mikola**.

- **Zanie**
  - Direct healing (single target, high)
- **Velara**
  - Direct healing (area, low)
- **Contess**
  - Direct healing (multiple targets, low)
- **Himmel**
  - Direct healing (single target, low)
- **Hewynn**
  - Healing over time (all units, high)

### Units benefitting most from Reinier

Reinier provides ATK buff (Legendary+) to single targets `average`.

- Bonnie (2.3 / 5)
- Himmel (1.8 / 5)
- Indris (1.7 / 5)

### Units that can act as a replacement for Reinier

**Buffs on allies**

- Gunnar (100% `ATK`)
- Contess (100% `ATK`)
- Himmel (100% `ATK`)

**Similar Skills**

- Dunlingr (33% `battle-start-burst`)
- Indris (33% `disabler`)
- Kulu (30% `battle-start-burst`)

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
- Cyran (60% `Displace` `Knock down`)

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
Common buffers are **Twins**, **Rowan**, or **Mikola**.

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Valka**
  - ATK SPD buff (multiple targets, average) `signature fuel`
- **Ravion**
  - Energy recovery (multiple targets, average) `signature fuel`
  - Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Lorsan**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Rhys

Rhys provides Direct healing to single targets `low`.

- Carolina (1.5 / 5)
- Nerion (1.4 / 5)
- Perseus (1.1 / 5)

### Units that can act as a replacement for Rhys

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Himmel (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)

**Similar Skills**

- Dionel (60% `aoe-damage` `self-repositioner`)
- Atalanta (60% `aoe-damage` `self-repositioner`)
- Frieren (48% `aoe-damage` `self-repositioner`)

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

Look for units providing: `Haste` `Healing` `Energy`  
Common buffers are **Mikola**, **Smokey & Meerky**, or **Twins**.

- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)
- **Evie**
  - Direct healing (single target, high)
- **Pandora**
  - Direct healing (single target, high)
- **Zanie**
  - Direct healing (single target, high)

### Units benefitting most from Rowan

Rowan provides Direct healing in an area `low`, Energy recovery in an area `high`, DEF buff (Mythic+) to single targets `average`, and Max HP buff (Mythic+) to single targets `high`.

**35** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Arden (5.0 / 5)
- Valen (5.0 / 5)
- Berial (4.9 / 5)
- Soren (4.1 / 5)
- Koko (4.0 / 5)
- Fay (3.9 / 5)
- Zorya (3.6 / 5)
- Lenya (3.6 / 5)
- Vala (3.3 / 5)
- Tasi (3.2 / 5)

### Units that can act as a replacement for Rowan

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
Common buffers are **Solise**, **Twins**, or **Mikola**.

- **Velara**
  - Direct healing (area, low)
- **Contess**
  - Direct healing (multiple targets, low)
- **Himmel**
  - Direct healing (single target, low)
- **Hewynn**
  - Healing over time (all units, high)
- **Hepler**
  - Healing over time (multiple targets, high)

### Units benefitting most from Saida

Saida provides Shield to multiple targets `high`.

- Silvina (5.0 / 5)
- Daimon (4.4 / 5)
- Gerda (4.4 / 5)
- Kruger (4.0 / 5)
- Shadewing (3.1 / 5)
- Thador (3.0 / 5)
- Faramor (2.7 / 5)
- Eironn (2.5 / 5)
- Shemira (2.4 / 5)

### Units that can act as a replacement for Saida

**Similar Skills**

- Koko (66% `ally-shielder` `life-drain`)
- Thoran (50% `cheat-death` `life-drain`)
- Daimon (40% `ally-shielder` `life-drain`)

**Damage**

- Galahad (100% `Magic` `Max HP-based damage`)
- Cryonaia (100% `Magic` `DoT` `Max HP-based damage`)
- Marcille (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Lily May (62% `Energy drain`)

**Crowd Control**

- Cyran (75% `Bind` `Displace`)
- Eironn (75% `Bind` `Displace`)
- Evie (75% `Bind` `Displace`)

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
- Bind — Single target — `low`
- Displace — Single target — `low`
- Interrupt — Single target — `low`

## Salazer

### Salazer's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Spirit Shackles (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `disabler` `execute` `life-drain`
- **Damage types**: Physical `high`

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
Common buffers are **Koko**, **Mikola**, or **Solise**.

- **Hepler**
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
- **Hewynn**
  - Healing over time (all units, high)
- **Zandrok**
  - Max HP buff (multiple targets, high)
  - Lifedrain buff (area, low, conditional (frequent))
- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
  - Direct healing (single target, high)
- **Dunlingr**
  - Lifedrain buff (all units, average)

### Units benefitting most from Salazer

Salazer provides Shield (Supreme+) to single targets `high` — conditional (frequent).

- Nerion (2.5 / 5)
- Shadewing (2.0 / 5)
- Perseus (1.4 / 5)

### Units that can act as a replacement for Salazer

**Buffs on allies**

- Hugin (100% `Shield`)
- Saida (100% `Shield`)
- Hepler (100% `Shield`)

**Similar Skills**

- Harak (60% `execute` `life-drain`)
- Sylphira (48% `disabler` `life-drain`)
- Odie (30% `execute`)

**Damage**

- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)
- Aliceth (100% `Physical` `Max HP-based damage`)

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
- **Behavior tags**: `dot-specialist` `fire-attack` `hp-scaling`
- **Damage types**: Magic `high`, Max HP-based damage `low`

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
Common buffers are **Koko**.

- **Zandrok**
  - Max HP buff (multiple targets, high)
  - Lifedrain buff (area, low, conditional (frequent))
- **Dunlingr**
  - Lifedrain buff (all units, average)
- **Daimon**
  - Lifedrain buff (single target, average)
- **Kordan**
  - Lifedrain buff (multiple targets, low)
- **Shakir**
  - Lifedrain buff (single target, low)

### Units benefitting most from Satrana

Satrana provides Magic damage amplification (Mythic+) to single targets `high`.

- Bonnie (2.5 / 5)
- Shadewing (2.1 / 5)
- Indris (1.9 / 5)

### Units that can act as a replacement for Satrana

**Similar Skills**

- Mirael (66% `dot-specialist` `fire-attack`)
- Gwyneth (50% `dot-specialist` `fire-attack`)
- Faramor (40% `dot-specialist` `hp-scaling`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage`)
- Galahad (100% `Magic` `Max HP-based damage`)
- Saida (100% `Magic` `Max HP-based damage`)

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

Look for units providing: `Execution` `Energy`  
Common buffers are **Rowan**, **Smokey & Meerky**, or **Twins**.

- **Ravion**
  - Energy recovery (multiple targets, average) `signature fuel`
- **Thoran**
  - Energy recovery (single target, average) `signature fuel`
- **Thador**
  - Energy recovery (single target, low) `signature fuel`
- **Lyca**
  - Energy recovery (all units, low) `signature fuel`
- **Arden**
  - Energy recovery (single target, low) `signature fuel`

### Units benefitting most from Scarlita

Scarlita provides Shield to single targets `average` and DEF buff (Supreme+) to single targets `high`.

- Carolina (3.4 / 5)
- Nerion (3.3 / 5)
- Silven (1.8 / 5)

### Units that can act as a replacement for Scarlita

**Buffs on allies**

- Hepler (85% `Shield` `Magic DEF` `Physical DEF`)
- Contess (84% `Shield`)
- Galahad (84% `Shield`)

**Similar Skills**

- Korin (80% `ally-shielder` `hp-scaling`)
- Galahad (50% `ally-shielder` `aoe-damage`)
- Zandrok (48% `aoe-damage` `hp-scaling`)

**Damage**

- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)
- Aliceth (100% `Physical` `Max HP-based damage`)

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
Common buffers are **Mikola**, **Smokey & Meerky**, or **Twins**.

- **Dunlingr**
  - ATK buff (single target, high)
  - Haste buff (single target, average) `signature fuel`
  - Lifedrain buff (all units, average)
  - ATK SPD buff (all units, low) `signature fuel`
- **Hewynn**
  - Healing over time (all units, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
  - Direct healing (all units, low)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Seth

Seth provides Crit buff to single targets `low`.

- Nazrik (5.0 / 5)

### Units that can act as a replacement for Seth

**Similar Skills**

- Harak (80% `assassin` `life-drain`)
- Koko (40% `life-drain`)
- Shakir (40% `life-drain`)

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
Common buffers are **Twins**, **Mikola**, or **Smokey & Meerky**.

Shadewing also requires units **dealing continuous damage** to enemies and/or units **putting debuffs** on enemies

- **Alna**
  - ATK buff (single target, low)
  - Enables Debuff on target via Haste debuff (all units)
  - Enables Continuous damage on enemies via DoT
- **Saida**
  - Shield (multiple targets, high)
  - Enables Debuff on target via Energy drain (single target)
  - Enables Continuous damage on enemies via DoT
- **Frieren**
  - Enables Debuff on target via DoT (area)
  - Enables Continuous damage on enemies via DoT + Burn
- **Ravion**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, average) `signature fuel`
  - Enables Debuff on target via Phys DEF debuff (single target)
  - Enables Continuous damage on enemies via tick damage
- **Aliceth**
  - ATK buff (multiple targets, average)
  - Enables Debuff on target via Marked target (focus fire) (single target)
  - Enables Continuous damage on enemies via tick damage

### Units benefitting most from Shadewing

- Bonnie (2.2 / 5)
- Indris (1.6 / 5)
- Aliceth (1.5 / 5)

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

Look for units providing: `Haste`  
Common buffers are **Twins** or **Mikola**.

- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Dunlingr**
  - Haste buff (single target, average) `signature fuel`
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
- **Mehira**
  - Haste buff (single target, low) `signature fuel`
- **Atalanta**
  - Haste buff (multiple targets, high, conditional (frequent)) `signature fuel`

### Units benefitting most from Shakir

Shakir provides Damage taken to multiple targets `average`, Haste buff to multiple targets `average`, and Lifedrain buff to single targets `low`.

- Dionel (3.1 / 5)
- Mikola (2.9 / 5)
- Pang (2.7 / 5)
- Sonja (2.3 / 5)

### Units that can act as a replacement for Shakir

**Buffs on allies**

- Zandrok (58% `Haste` `Life Drain`)
- Lorsan (50% `Haste`)

**Similar Skills**

- Sylphira (50% `life-drain` `transformation`)
- Kruger (48% `life-drain`)
- Koko (40% `life-drain`)

**Damage**

- Himmel (100% `Physical`)
- Aliceth (100% `Physical`)
- Alna (100% `Physical`)

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
- **Behavior tags**: `high-damage-ult` `hp-scaling` `life-drain` `summoner`
- **Damage types**: Magic `high`, Max HP-based damage `high`, True damage `low`

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
Common buffers are **Twins**, **Solise**, or **Rowan**.

- **Hugin**
  - Shield (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)
- **Contess**
  - Shield (single target, average)
  - Direct healing (multiple targets, low)
- **Galahad**
  - Shield (single target, average)
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Himmel**
  - Shield (single target, average)
  - Direct healing (single target, low)

### Units benefitting most from Shemira

- Bonnie (1.9 / 5)
- Shadewing (1.9 / 5)
- Himmel (1.5 / 5)

### Units that can act as a replacement for Shemira

**Similar Skills**

- Daimon (72% `hp-scaling` `life-drain` `summoner`)
- Zorya (60% `hp-scaling` `life-drain`)
- Marcille (34% `high-damage-ult` `summoner`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage` `True damage`)
- Sylphira (100% `Magic` `Max HP-based damage` `True damage`)
- Daimon (85% `Max HP-based damage` `Magic` `True damage`)

**Debuffs on enemies**

- Baelran (100% `Max HP debuff`)
- Alna (100% `Max HP debuff`)
- Sylphira (100% `Max HP debuff`)

### Summary for Shemira

#### Damage types dealt by Shemira

- Magic — Area, Single target
- Max HP-based damage — Area, Single target — `high`
- True damage — Area, Single target — `average`

#### Debuffs provided by Shemira

- Max HP (EX+10) — Single target — `low`

## Silven

### Silven's behavior

`AFK Stages [S]`, `Dream Realm [S]`, `Dream Realm (Endless) [A+]`, `PVP [A]`

- **Signature skill**: Gravity Collapse (Skill 1)
- **Movement**: stationary (avg attack range 12.0 tiles)
- **Behavior tags**: `hp-scaling` `mark-target`
- **Damage types**: Magic `high`, Max HP-based damage `high`

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

Look for units providing: `ATK SPD / Haste` `Energy` `DEF Penetration` `Physical DEF` `Magic DEF`  
Common buffers are **Twins**, **Solise**, or **Mikola**.

Silven also requires units **buffing them**

- **Gunnar**
  - ATK SPD buff (single target, low) `signature fuel`
  - Grants 5 distinct stat buffs to Silven (start of battle)
- **Hugin**
  - Grants 3 distinct stat buffs to Silven
- **Contess**
  - Grants 4 distinct stat buffs to Silven
- **Saida**
  - Grants 1 distinct stat buff to Silven
- **Galahad**
  - ATK SPD via Haste buff (single target, average) `signature fuel`
  - Grants 2 distinct stat buffs to Silven

### Units benefitting most from Silven

Silven provides DEF Penetration buff (Mythic+) to single targets `low`.

- Carolina (1.9 / 5)
- Nerion (1.9 / 5)
- Bonnie (1.6 / 5)

### Units that can act as a replacement for Silven

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
- **Behavior tags**: `assassin` `disabler` `mark-target`
- **Damage types**: Physical `average`, Max HP-based damage `high`

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
Common buffers are **Koko** or **Twins**.

- **Hepler**
  - Shield (multiple targets, high)
- **Hugin**
  - Shield (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)
- **Daimon**
  - Shield (multiple targets, average)
- **Lucius**
  - Shield (area, low)

### Units benefitting most from Silvina

- Carolina (3.4 / 5)
- Nerion (3.1 / 5)
- Indris (1.6 / 5)

### Units that can act as a replacement for Silvina

**Similar Skills**

- Sinbad (50% `assassin` `mark-target`)
- Kafra (40% `assassin` `mark-target`)
- Silven (30% `mark-target`)

**Damage**

- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)
- Shemira (100% `Max HP-based damage`)

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
Common buffers are **Twins**, **Rowan**, or **Smokey & Meerky**.

- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (all units, low) `signature fuel`
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, average) `signature fuel`
- **Valka**
  - ATK SPD buff (multiple targets, average) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
- **Ravion**
  - Energy recovery (multiple targets, average) `signature fuel`

### Units benefitting most from Sinbad

- Indris (3.6 / 5)
- Bonnie (2.1 / 5)
- Aliceth (2.1 / 5)

### Units that can act as a replacement for Sinbad

**Similar Skills**

- Kafra (90% `assassin` `enemy-debuffer` `mark-target`)
- Silvina (50% `assassin` `mark-target`)
- Silven (30% `mark-target`)

**Damage**

- Baelran (100% `Physical`)
- Himmel (100% `Physical`)
- Aliceth (100% `Physical`)

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
Common buffers are **Mikola**, **Solise**, or **Rowan**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)
- **Contess**
  - ATK buff (single target, high)
  - Direct healing (multiple targets, low)
- **Ravion**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, average) `signature fuel`

### Units benefitting most from Smokey & Meerky

Smokey & Meerky provides Direct healing in an area `high`, Direct healing to multiple targets `average`, Energy recovery in an area `high`, ATK buff (Legendary+) to multiple targets `average`, and Direct healing (Supreme+) to single targets `low`.

**50** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner

These are the **10** strongest pairings: 

- Hodgkin (4.6 / 5)
- Bryon (4.0 / 5)
- Damian (4.0 / 5)
- Zorya (3.9 / 5)
- Temesia (3.8 / 5)
- Laios (3.8 / 5)
- Seth (3.6 / 5)
- Vala (3.6 / 5)
- Isabella (3.2 / 5)
- Perseus (3.1 / 5)

### Units that can act as a replacement for Smokey & Meerky

**Buffs on allies**

- Ravion (79% `ATK` `Energy`)
- Rowan (65% `Energy`)
- Mikola (65% `ATK`)

**Healing**

- Solise (100% `Direct healing` `Healing`)
- Hewynn (88% `Direct healing` `Healing`)
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

Solise provides ATK buff to summons `low`, Direct healing to all units `high`, Direct healing to multiple targets `average`, Healing over time to single targets `high`, Shield to summons `average`, and DEF buff (Mythic+) to summons `low`.

**39** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Phraesto (5.0 / 5)
- Dunlingr (4.7 / 5)
- Berial (4.5 / 5)
- Niru (3.8 / 5)
- Hodgkin (3.4 / 5)
- Bryon (3.3 / 5)
- Damian (3.0 / 5)
- Himmel (3.0 / 5)
- Laios (2.7 / 5)
- Silven (2.2 / 5)

### Units that can act as a replacement for Solise

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
- **Behavior tags**: `ally-buffer` `aoe-damage` `battle-start-burst` `life-drain` `mass-cc`
- **Ally composition**: place allies on left and right at battle start (Crimson Covenant buffs; prioritizes front row)
- **Damage types**: Physical `average`

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

Look for units providing: `Haste` `Max HP`  
Common buffers are **Twins** or **Mikola**.

- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, high)
- **Shakir**
  - Haste buff (multiple targets, average) `signature fuel`
- **Dunlingr**
  - Haste buff (single target, average) `signature fuel`
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
- **Mehira**
  - Haste buff (single target, low) `signature fuel`

### Units benefitting most from Sonja

Sonja provides ATK buff to multiple targets `average` and DEF buff to multiple targets `high`.

- Cecia (4.0 / 5)
- Hepler (3.9 / 5)
- Natsu (3.9 / 5)
- Lucca (3.7 / 5)
- Niru (3.7 / 5)
- Isabella (2.9 / 5)

### Units that can act as a replacement for Sonja

**Buffs on allies**

- Kordan (100% `ATK` `Magic DEF` `Physical DEF`)
- Mikola (100% `ATK` `Magic DEF` `Physical DEF`)
- Fay (100% `Magic DEF` `Physical DEF` `ATK`)

**Similar Skills**

- Walker (80% `aoe-damage` `battle-start-burst` `life-drain` `mass-cc`)
- Himmel (51% `ally-buffer` `aoe-damage` `battle-start-burst`)
- Perseus (48% `ally-buffer` `aoe-damage`)

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
Common buffers are **Twins**, **Rowan**, or **Mikola**.

- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
  - Direct healing (all units, low)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Pandora**
  - Max HP buff (single target, average)
  - Direct healing (single target, high)
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Shakir**
  - Haste buff (multiple targets, average) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, average) `signature fuel`
- **Hewynn**
  - Healing over time (all units, high)

### Units benefitting most from Soren

Soren provides Shield (Supreme+) to single targets `low`.

- Carolina (2.8 / 5)
- Nerion (2.7 / 5)
- Shadewing (1.8 / 5)

### Units that can act as a replacement for Soren

**Buffs on allies**

- Contess (100% `Shield`)
- Galahad (100% `Shield`)
- Himmel (100% `Shield`)

**Similar Skills**

- Lenya (66% `counterattack` `self-repositioner`)
- Kordan (48% `self-repositioner`)
- Pippa (33% `self-repositioner`)

**Damage**

- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)
- Aliceth (100% `Physical` `Max HP-based damage`)

**Crowd Control**

- Perseus (100% `Stun` `Knock back`)
- Scarlita (100% `Stun` `Knock back`)
- Koko (78% `Stun`)

### Summary for Soren

#### Damage types dealt by Soren

- Physical — Area, Multiple targets, Single target
- Max HP-based damage — Single target — `average`

#### Crowd Control provided by Soren

- Knock back — Area — `low`
- Stun — Multiple targets — `average`

## Sylphira

### Sylphira's behavior

`AFK Stages [A]`, `Dream Realm [A+]`, `Dream Realm (Endless) [?]`, `PVP [A+]`

- **Signature skill**: Grand Finale (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `disabler` `life-drain` `mass-cc` `transformation`
- **Damage types**: Magic `high`, Max HP-based damage `high`, True damage `average`

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
Common buffers are **Twins**, **Solise**, or **Mikola**.

- **Ravion**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, average) `signature fuel`
  - Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD via Haste buff (single target, average) `signature fuel`
- **Contess**
  - ATK buff (single target, high)
  - Direct healing (multiple targets, low)
- **Gunnar**
  - ATK buff (single target, high)
  - ATK SPD buff (single target, low) `signature fuel`
- **Thador**
  - Energy recovery (lieutenant, start of battle) `signature fuel`

### Units benefitting most from Sylphira

- Carolina (3.4 / 5)
- Nerion (3.1 / 5)
- Bonnie (2.2 / 5)

### Units that can act as a replacement for Sylphira

**Similar Skills**

- Shakir (50% `life-drain` `transformation`)
- Lucca (40% `disabler` `mass-cc`)
- Tasi (33% `mass-cc` `transformation`)

**Damage**

- Frieren (100% `Magic` `Max HP-based damage` `True damage`)
- Shemira (100% `Magic` `Max HP-based damage` `True damage`)
- Athalia (100% `Max HP-based damage` `True damage`)

**Debuffs on enemies**

- Saida (100% `Energy drain`)
- Dunlingr (100% `Energy drain`)
- Lily May (100% `Energy drain`)

**Crowd Control**

- Baelran (76% `Knock down`)
- Lucca (60% `Knock down` `Interrupt`)
- Cyran (50% `Knock down` `Silence`)

### Summary for Sylphira

#### Sylphira Provides

- Dispel debuffs (Mythic+) — Self
- Stacking buff (Mythic+) — Single target

#### Damage types dealt by Sylphira

- Magic — Area, Single target
- Max HP-based damage — Area, Single target — `average`
- True damage — Area — `average`

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
Common buffers are **Mikola**, **Smokey & Meerky**, or **Koko**.

- **Dunlingr**
  - ATK buff (single target, high)
  - Lifedrain buff (all units, average)
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Zandrok**
  - Max HP buff (multiple targets, high)
  - Lifedrain buff (area, low, conditional (frequent))
- **Kordan**
  - ATK buff (multiple targets, average)
  - Lifedrain buff (multiple targets, low)
- **Ludovic**
  - Direct healing (multiple targets, high)

### Units benefitting most from Talene

Talene provides ATK buff (Legendary+) in an area `high`.

- Bonnie (3.4 / 5)
- Shadewing (2.8 / 5)
- Silven (1.7 / 5)

### Units that can act as a replacement for Talene

**Buffs on allies**

- Evie (100% `ATK`)
- Mikola (100% `ATK`)
- Hugin (90% `ATK`)

**Similar Skills**

- Ulmus (51% `aoe-damage` `cheat-death` `transformation`)
- Tasi (34% `aoe-damage` `transformation`)
- Hepler (33% `ally-healer` `transformation`)

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
Common buffers are **Mikola**, **Twins**, or **Rowan**.

- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, high)
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Pandora**
  - Max HP buff (single target, average)
  - Direct healing (single target, high)
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Dunlingr**
  - ATK buff (single target, high)
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Tasi

- Carolina (2.5 / 5)
- Nerion (2.3 / 5)
- Shadewing (1.7 / 5)

### Units that can act as a replacement for Tasi

**Similar Skills**

- Valen (75% `aoe-damage` `mass-cc` `transformation`)
- Ulmus (72% `aoe-damage` `mass-cc` `transformation`)
- Bonnie (60% `aoe-damage` `mass-cc` `transformation`)

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
- Sleep (area) — Single target
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
- **Damage types**: Physical `high`, Max HP-based damage `average`

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
Common buffers are **Mikola**, **Smokey & Meerky**, or **Twins**.

- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
- **Hugin**
  - ATK buff (multiple targets, high)
  - Shield (multiple targets, high)
- **Hewynn**
  - Healing over time (all units, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`
  - Direct healing (arc, average)

### Units benefitting most from Temesia

- Carolina (2.2 / 5)
- Nerion (2.0 / 5)
- Indris (1.4 / 5)

### Units that can act as a replacement for Temesia

**Similar Skills**

- Tasi (60% `aoe-damage` `mass-cc` `self-repositioner`)
- Bonnie (51% `aoe-damage` `enemy-debuffer` `mass-cc`)
- Cassadee (48% `aoe-damage` `enemy-debuffer`)

**Damage**

- Himmel (100% `Physical` `Max HP-based damage`)
- Aliceth (100% `Physical` `Max HP-based damage`)
- Alna (100% `Physical` `Max HP-based damage`)

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
Common buffers are **Solise**, **Twins**, or **Koko**.

- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
  - Direct healing (single target, high)
- **Hugin**
  - Shield (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)
- **Contess**
  - Shield (single target, average)
  - Direct healing (multiple targets, low)
- **Himmel**
  - Shield (single target, average)
  - Direct healing (single target, low)

### Units benefitting most from Thador

Thador provides Energy recovery (EX+10) to single targets `low`.

- Ravion (1.2 / 5)

### Units that can act as a replacement for Thador

**Buffs on allies**

- Twins (100% `Energy`)
- Ravion (100% `Energy`)
- Smokey & Meerky (100% `Energy`)

**Similar Skills**

- Ravion (60% `ally-shielder` `energy-provider`)
- Hugin (50% `ally-shielder` `energy-provider`)
- Pandora (50% `enemy-debuffer` `energy-provider`)

**Damage**

- Alna (100% `DoT` `Physical` `Max HP-based damage`)
- Gwyneth (99% `DoT` `Physical` `Max HP-based damage`)
- Brutus (97% `Physical` `DoT` `Max HP-based damage`)

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
Common buffers are **Solise**, **Twins**, or **Smokey & Meerky**.

- **Zanie**
  - Max HP buff (single target, high)
  - Direct healing (single target, high)
- **Ravion**
  - Energy recovery (multiple targets, average) `signature fuel`
- **Velara**
  - Direct healing (area, low)
- **Contess**
  - Direct healing (multiple targets, low)
- **Himmel**
  - Direct healing (single target, low)

### Units benefitting most from Thoran

Thoran provides Lifedrain buff to single targets `low` and Energy recovery (Legendary+) to single targets `average`.

- Pandora (2.0 / 5)
- Scarlita (2.0 / 5)

### Units that can act as a replacement for Thoran

**Buffs on allies**

- Twins (80% `Energy`)
- Ravion (80% `Energy`)
- Smokey & Meerky (80% `Energy`)

**Similar Skills**

- Saida (50% `cheat-death` `life-drain`)
- Brutus (40% `cheat-death` `life-drain`)
- Zorya (30% `life-drain`)

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
Common buffers are **Koko**, **Mikola**, or **Solise**.

- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
  - Direct healing (single target, high)
- **Hugin**
  - Shield (multiple targets, high)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)

### Units benefitting most from Tilaya

Tilaya provides DEF buff (EX+10) in an area `low` and Max HP buff (EX+10) in an area `average`.

- Hepler (2.9 / 5)

### Units that can act as a replacement for Tilaya

**Buffs on allies**

- Alna (60% `Max HP`)
- Phraesto (60% `Max HP`)
- Lucca (60% `Magic DEF` `Physical DEF`)

**Similar Skills**

- Lorsan (60% `aoe-damage`)
- Perseus (50% `aoe-damage`)
- Florabelle (40% `aoe-damage`)

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
- **Damage types**: Magic `low`, Max HP-based damage `low`

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
Common buffers are **Mikola**, **Smokey & Meerky**, or **Solise**.

Twins also requires units **positioned on their link**

- **Contess**
  - Direct healing (multiple targets, low)
- **Gunnar**
  - ATK SPD buff (single target, low) `signature fuel`
- **Hewynn**
  - Healing over time (all units, high)
- **Atalanta**
  - Haste buff (multiple targets, high, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) `signature fuel`
- **Lorsan**
  - Haste buff (single target, high) `signature fuel`
  - Direct healing (all units, low)
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Twins

Twins provides ATK buff to multiple targets `low`, Direct healing to multiple targets `low`, Energy recovery to multiple targets `low`, Haste buff to all units `average`, Max HP buff to multiple targets `high`, Shield to single targets `low`, Vitality buff (Mythic+) to multiple targets `low`, and DEF buff (Supreme+) to single targets `low`.

**97** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight
- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner

These are the **10** strongest pairings: 

- Lenya (5.0 / 5)
- Mehira (5.0 / 5)
- Soren (5.0 / 5)
- Zorya (5.0 / 5)
- Nerion (4.8 / 5)
- Tasi (4.7 / 5)
- Laios (4.6 / 5)
- Perseus (4.0 / 5)
- Vala (4.0 / 5)
- Silven (3.7 / 5)

### Units that can act as a replacement for Twins

**Buffs on allies**

- Contess (52% `ATK` `Shield`)
- Himmel (52% `ATK` `Shield`)
- Hugin (52% `ATK` `Shield`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Zanie (100% `Direct healing` `Healing`)

**Similar Skills**

- Rowan (60% `ally-healer` `energy-provider`)
- Solise (48% `ally-healer` `ally-shielder`)
- Hugin (48% `ally-shielder` `energy-provider`)

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

- Ally positioning link — Single target
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
- **Behavior tags**: `ally-shielder` `aoe-damage` `cheat-death` `mass-cc` `transformation`
- **Ally composition**: when rooted, shields frontmost ally instead of self
- **Damage types**: Physical `average`

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

Look for units providing: `Max HP` `Shield` `Healing` `Energy` `Life Drain`  
Common buffers are **Koko**, **Smokey & Meerky**, or **Rowan**.

- **Hepler**
  - Shield (multiple targets, high)
  - Healing over time (multiple targets, high)
- **Zandrok**
  - Max HP buff (multiple targets, high)
  - Lifedrain buff (area, low, conditional (frequent))
- **Zanie**
  - Max HP buff (single target, high)
  - Shield (single target, average)
  - Direct healing (single target, high)
- **Dunlingr**
  - Lifedrain buff (all units, average)
- **Daimon**
  - Shield (multiple targets, average)
  - Lifedrain buff (single target, average)

### Units benefitting most from Ulmus

Ulmus provides Energy recovery to single targets `low`.

- Kazim (5.0 / 5)

### Units that can act as a replacement for Ulmus

**Buffs on allies**

- Twins (100% `Energy`)
- Ravion (100% `Energy`)
- Smokey & Meerky (100% `Energy`)

**Similar Skills**

- Tasi (72% `aoe-damage` `mass-cc` `transformation`)
- Valen (60% `aoe-damage` `mass-cc` `transformation`)
- Bonnie (51% `aoe-damage` `mass-cc` `transformation`)

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
Common buffers are **Mikola**, **Twins**, or **Smokey & Meerky**.

Vala also requires enemies **to be defeated**

- **Ravion**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, average) `signature fuel`
  - Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Evie**
  - ATK buff (multiple targets, high)
  - Direct healing (single target, high)
- **Dunlingr**
  - ATK buff (single target, high)
  - Haste buff (single target, average) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing over time (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Vala

- Carolina (1.9 / 5)
- Nerion (1.8 / 5)
- Indris (1.7 / 5)

### Units that can act as a replacement for Vala

**Similar Skills**

- Athalia (60% `hp-scaling` `self-repositioner` `transformation`)
- Silven (48% `hp-scaling` `mark-target`)
- Marilee (41% `hp-scaling` `self-repositioner`)

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

- Marked target (focus fire) — Self

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
Common buffers are **Rowan**, **Mikola**, or **Smokey & Meerky**.

- **Ravion**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, average) `signature fuel`
  - Energy recovery (150 early objective, multiple targets) `signature fuel`
- **Lyca**
  - ATK SPD buff (all units, low) `signature fuel`
  - Energy recovery (120 at battle start, all units) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, high)
  - ATK SPD buff (all units, low) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, average, conditional (frequent))
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Pandora**
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Valen

- Carolina (1.9 / 5)
- Nerion (1.8 / 5)
- Indris (1.6 / 5)

### Units that can act as a replacement for Valen

**Similar Skills**

- Tasi (75% `aoe-damage` `mass-cc` `transformation`)
- Bonnie (60% `aoe-damage` `mass-cc` `transformation`)
- Ulmus (60% `aoe-damage` `mass-cc` `transformation`)

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
- **Damage types**: Physical `high`, Max HP-based damage `high`, True damage `average`

#### Skill overview

- **Signature skill (ult)**: speed `fast`, first cast speed `fast`, heal `average`, debuffs `average`, damage `high`
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
Common buffers are **Mikola**, **Smokey & Meerky**, or **Twins**.

- **Hugin**
  - Shield (multiple targets, high)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)
- **Saida**
  - Shield (multiple targets, high)
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, average) `signature fuel`

### Units benefitting most from Valka

Valka provides ATK SPD buff to multiple targets `average` and Lifedrain buff (EX+10) to single targets `low`.

- Odie (2.9 / 5)
- Lyca (2.8 / 5)
- Rhys (2.8 / 5)
- Mirael (2.8 / 5)
- Dionel (2.7 / 5)

### Units that can act as a replacement for Valka

**Buffs on allies**

- Lyca (100% `ATK SPD`)
- Dunlingr (61% `ATK SPD` `Life Drain`)

**Similar Skills**

- Twins (40% `ally-buffer` `ally-shielder`)
- Himmel (33% `ally-buffer` `ally-shielder`)
- Soren (30% `counterattack`)

**Damage**

- Nara (100% `True damage` `Physical` `Max HP-based damage`)
- Athalia (93% `True damage` `Physical` `Max HP-based damage`)
- Nazrik (91% `True damage` `Physical` `Max HP-based damage`)

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
- True damage — Single target — `high`

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
Common buffers are **Twins**, **Rowan**, or **Smokey & Meerky**.

- **Galahad**
  - Haste buff (single target, average) `signature fuel`
  - Shield (single target, average)
- **Contess**
  - Shield (single target, average)
- **Himmel**
  - Shield (single target, average)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Shield (multiple targets, high)
- **Hugin**
  - Shield (multiple targets, high)

### Units benefitting most from Velara

Velara provides Direct healing in an area `low`.

- Aliceth (2.9 / 5)
- Alna (2.1 / 5)
- Athalia (2.1 / 5)
- Reinier (2.1 / 5)
- Saida (2.1 / 5)
- Himmel (1.9 / 5)
- Ludovic (1.8 / 5)
- Thoran (1.8 / 5)
- Mehira (1.4 / 5)

### Units that can act as a replacement for Velara

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

- Alna (100% `Bind`)
- Eironn (100% `Bind`)
- Kordan (100% `Bind`)

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
Common buffers are **Mikola**, **Twins**, or **Smokey & Meerky**.

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
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)

### Units benefitting most from Viperian

- Bonnie (2.3 / 5)
- Shadewing (2.1 / 5)
- Indris (1.5 / 5)

### Units that can act as a replacement for Viperian

**Similar Skills**

- Lorsan (66% `aoe-damage` `dot-specialist`)
- Arden (60% `aoe-damage` `dot-specialist`)
- Frieren (48% `aoe-damage` `dot-specialist`)

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

- Energy drain — Single target — `average`

#### Crowd Control provided by Viperian

- Unaffected — Self — On skill

## Walker

### Walker's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Six-Shot (ultimate)
- **Movement**: moving (avg attack range 2.0 tiles)
- **Behavior tags**: `aoe-damage` `battle-start-burst` `life-drain` `mark-target` `mass-cc`
- **Damage types**: Physical `low`, Max HP-based damage `low`

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
Common buffers are **Twins**, **Koko**, or **Rowan**.

- **Zandrok**
  - Max HP buff (multiple targets, high)
  - Lifedrain buff (area, low, conditional (frequent))
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Dunlingr**
  - Lifedrain buff (all units, average)
  - ATK SPD buff (all units, low) `signature fuel`
- **Hepler**
  - Shield (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Daimon**
  - Shield (multiple targets, average)
  - Lifedrain buff (single target, average)
- **Hugin**
  - Shield (multiple targets, high)

### Units benefitting most from Walker

- Carolina (1.9 / 5)
- Nerion (1.8 / 5)
- Indris (1.3 / 5)

### Units that can act as a replacement for Walker

**Similar Skills**

- Sonja (80% `aoe-damage` `battle-start-burst` `life-drain` `mass-cc`)
- Bonnie (51% `aoe-damage` `battle-start-burst` `mass-cc`)
- Mehira (45% `aoe-damage` `life-drain` `mass-cc`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Baelran (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Nazrik (100% `Crit Resist debuff`)

**Crowd Control**

- Bonnie (100% `Stun`)
- Phraesto (100% `Stun`)
- Callan (100% `Stun`)

### Summary for Walker

#### Damage types dealt by Walker

- Physical — Arc, Single target
- Max HP-based damage — Single target — `low`

#### Debuffs provided by Walker

- Crit Resist (Mythic+) — Single target — `low`

#### Crowd Control provided by Walker

- Stun — Single target — `average`

## Zandrok

### Zandrok's behavior

`AFK Stages [A+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Rallying Roar (Skill 1)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Behavior tags**: `aoe-damage` `battle-start-burst` `battlefield-modification` `hp-scaling`
- **Damage types**: Physical `low`

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
Common buffers are **Twins**, **Mikola**, or **Koko**.

- **Dunlingr**
  - Haste buff (single target, average) `signature fuel`
  - Lifedrain buff (all units, average)
- **Ludovic**
  - Direct healing (multiple targets, high)
- **Marcille**
  - Direct healing (multiple targets, high)
- **Zanie**
  - Max HP buff (single target, high)
  - Direct healing (single target, high)
- **Pandora**
  - Max HP buff (single target, average)
  - Direct healing (single target, high)

### Units benefitting most from Zandrok

Zandrok provides Haste buff in an area `low` — conditional (frequent), Lifedrain buff in an area `low` — conditional (frequent), and Max HP buff to multiple targets `high`.

**12** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Satrana (5.0 / 5)
- Kazim (4.7 / 5)
- Walker (4.2 / 5)
- Sonja (3.6 / 5)
- Korin (3.3 / 5)
- Soren (2.8 / 5)
- Lenya (2.7 / 5)
- Tasi (2.6 / 5)
- Brutus (2.4 / 5)
- Cassadee (2.3 / 5)

### Units that can act as a replacement for Zandrok

**Buffs on allies**

- Twins (90% `Max HP` `Haste`)
- Cecia (80% `Max HP` `Life Drain`)
- Alna (71% `Max HP`)

**Similar Skills**

- Kulu (48% `battle-start-burst` `battlefield-modification`)
- Scarlita (48% `aoe-damage` `hp-scaling`)
- Florabelle (40% `aoe-damage` `battle-start-burst`)

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
Common buffers are **Twins** or **Mikola**.

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
- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, high)

### Units benefitting most from Zanie

Zanie provides Direct healing to single targets `high`, Shield to single targets `average`, DEF Penetration buff (Legendary+) to single targets `average`, and Max HP buff (Mythic+) to single targets `high`.

- Daimon (3.9 / 5)
- Gerda (3.9 / 5)
- Thador (3.7 / 5)
- Alna (3.4 / 5)
- Athalia (3.4 / 5)
- Dunlingr (2.8 / 5)
- Thoran (2.7 / 5)
- Reinier (2.2 / 5)
- Ludovic (1.9 / 5)
- Evie (1.9 / 5)

### Units that can act as a replacement for Zanie

**Buffs on allies**

- Hugin (100% `Shield`)
- Scarlita (100% `Shield`)
- Lucius (100% `Shield`)

**Healing**

- Contess (100% `Direct healing` `Healing`)
- Solise (100% `Direct healing` `Healing`)
- Twins (100% `Direct healing` `Healing`)

**Similar Skills**

- Mirael (40% `fire-attack`)
- Dunlingr (33% `summoner`)
- Gwyneth (30% `fire-attack`)

**Debuffs on enemies**

- Lyca (100% `Phys DEF debuff` `ATK debuff`)
- Ravion (96% `Phys DEF debuff` `ATK debuff`)
- Kafra (96% `Phys DEF debuff` `ATK debuff`)

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
- **Damage types**: Magic `high`, HP loss `high`, Max HP-based damage `high`

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

Look for units providing: `Haste` `Max HP` `Healing` `Energy` `Life Drain`  
Common buffers are **Twins**, **Smokey & Meerky**, or **Rowan**.

Zorya also requires allies **casting ultimates**

- **Lyca**
  - Energy recovery (all units, low) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
  - Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, high)
  - Lifedrain buff (area, low, conditional (frequent))
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Dunlingr**
  - Haste buff (single target, average) `signature fuel`
  - Lifedrain buff (all units, average)
  - ATK SPD buff (all units, low) `signature fuel`
- **Shakir**
  - Haste buff (multiple targets, average) `signature fuel`
  - Lifedrain buff (single target, low)
  - ATK SPD via Haste buff (multiple targets, average) `signature fuel`
- **Ravion**
  - Energy recovery (multiple targets, average) `signature fuel`
  - Enables Ally Ultimate casts via Energy recovery (Ultimate pace)

### Units benefitting most from Zorya

- Bonnie (4.2 / 5)
- Nerion (3.1 / 5)
- Indris (3.1 / 5)

### Units that can act as a replacement for Zorya

**Similar Skills**

- Shemira (60% `hp-scaling` `life-drain`)
- Daimon (60% `hp-scaling` `life-drain`)
- Kordan (40% `hp-scaling`)

**Damage**

- Nara (100% `Max HP-based damage` `HP loss`)
- Mehira (92% `Magic` `Max HP-based damage` `HP loss`)
- Dunlingr (85% `Magic` `Max HP-based damage` `HP loss`)

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

- Haste (Mythic+) — Area — `average`
- Movement speed (Mythic+) — Area — `high`

#### Crowd Control provided by Zorya

- Steadfast — Self — On skill
- Unaffected (EX+10) — Single target — On skill
- Knock down — Arc — `average`
- Stun — Area — `average`

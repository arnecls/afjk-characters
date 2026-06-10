# Heroes Overview

Per-hero synergy picks and summaries derived from skill text in
[Heroes.md](Heroes.md). [Heroes.md](Heroes.md) has skills only.
Synergy: stat buff tags under **Units X benefits from**, and
enabler partners matching **Requires** special effects.
Up to five partners by combined score. Omitted: ATK-only, Max HP
buff-only, and Shield-only (unless the hero benefits from Max HP/
shields). Rare conditional buffs score lower.
Meta tiers from [Prydwen tier list](https://www.prydwen.gg/afk-journey/tier-list).
Regenerate: `python3 scripts/generate-heroes-overview.py`.

## Aliceth

### Aliceth's behavior

`AFK Stages [B]`, `Dream Realm [B]`, `Dream Realm (Endless) [S+]`, `PVP [S]`

- **Signature skill**: Radiant Rain (ultimate)
- **Movement**: stationary (avg attack range 8.0 tiles)
- **Ally composition**: nearest ally in same row receives Brightfeather at battle start

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `high`
- **True damage**: HP loss `high`

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

### Units Aliceth benefits from

Look for units providing: `ATK` `Healing` `DEF Penetration`  
Common buffers are **Ravion**, **Hugin**, or **Solise**.

- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)
  - Enables Debuff on target via Max HP debuff (multiple targets)
- **Shadewing**
  - Enables Debuff on target via Magic DEF debuff (all units)
- **Sylphira**
  - Enables Debuff on target via Max HP debuff (area)
- **Zanie**
  - Healing (single target, high)
  - DEF Penetration buff (single target, medium)
  - Enables Debuff on target via Phys DEF debuff (single target)
- **Gwyneth**
  - Enables Debuff on target via DoT (single target)

### Units benefitting most from Aliceth

- Kulu
- Lily May

### Units that can act as a replacement for Aliceth

**Damage**

- Faramor (100% `Physical` `HP loss`)
- Kordan (94% `Physical` `HP loss`)
- Ravion (89% `Physical` `HP loss`)

**Crowd Control**

- Twins (60% `Blind` `Knock back`)

### Summary for Aliceth

#### Aliceth Provides

- Ally grant (Brightfeather) — Single target
- Instant defeat — Multiple targets
- Invincibility — Single target
- Marked target (focus fire) — Single target
- Reposition enemies — Single target
- Fatal blow save (Mythic+) — Area

#### Aliceth Requires

- Debuff on target (Legendary+) — Enemies

#### Damage types dealt by Aliceth

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- HP loss — Single target — `high`

#### Buffs provided by Aliceth

- Ally empower buff — Single target — `low`
- Attack range buff — Single target — `low`
- DEF Penetration buff — Multiple targets — `high`
- ATK buff (Legendary+) — Multiple targets — `low`
- Fatal blow immunity (Mythic+) — Single target — `high` — conditional (rare)

#### Debuffs provided by Aliceth

- Execution debuff — Multiple targets — `medium`
- Marked target (focus fire) — Multiple targets — `medium`
- Blind HP loss debuff (EX+15) — Area — `low`

#### Crowd Control provided by Aliceth

- Knock back — Single target — `low`
- Stun — Single target — `low`
- Blind (EX+15) — Area — `medium`

## Alna

### Alna's behavior

`AFK Stages [S+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S+]`

- **Signature skill**: Winter Anthem (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Ally composition**: place ally in same row at battle prep (Winter Warrior buffs)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, heal `medium`, debuffs `medium`, damage `high`
- **Non-ultimate**: speed `slow`, first cast speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `high`

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

### Units Alna benefits from

Look for units providing: `Max HP` `Healing`  
Common buffers are **Solise**, **Hugin**, or **Velara**.

- **Contess**
  - Healing (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
  - Healing (single target, high)
- **Galahad**
  - Max HP via Shield (single target, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)

### Units benefitting most from Alna

- Indris
- Bonnie

### Units that can act as a replacement for Alna

**Damage**

- Athalia (100% `Physical`)
- Gunnar (100% `Physical`)
- Aliceth (96% `Physical`)

**Crowd Control**

- Gwyneth (100% `Bind`)
- Kordan (100% `Bind`)

### Summary for Alna

#### Alna Provides

- Ally empower — Single target
- Start-of-battle cast — All units
- Damage and control immunity (Mythic+) — Self
- Damage and control immunity (ally) (EX+15) — Single target

#### Damage types dealt by Alna

- Primary damage type (unit): **Physical**
- Physical — All units, Arc, Single target

#### Buffs provided by Alna

- Ally empower buff — Single target — `low`
- Max HP buff — Single target — `low`
- Damage and control immunity (EX+15) — Single target — `high`
- ATK buff (Supreme+) — Single target — `medium`

#### Debuffs provided by Alna

- Haste debuff — Area — `high`
- Vitality debuff (Supreme+) — Area — `low`

#### Crowd Control provided by Alna

- Immune (Mythic+) — Self — Start of battle
- Bind (Supreme+) — Area — `medium`

## Alsa

### Alsa's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Twirling Rocks (ultimate)
- **Movement**: mostly stationary (avg attack range 6.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, debuffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, debuffs `medium`, damage `medium`

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

### Units Alsa benefits from

Look for units providing: `Haste` `Max HP`  
Common buffers are **Hugin**, **Twins**, or **Lyca**.

- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - Max HP via Shield (single target, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, low)
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Mehira**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Alsa

- Indris
- Bonnie
- Nerion

### Units that can act as a replacement for Alsa

**Damage**

- Callan (100% `Magic`)
- Cassadee (100% `Magic`)
- Contess (100% `Magic`)

**Debuffs on enemies**

- Kulu (84% `Movement speed debuff`)

**Crowd Control**

- Perseus (100% `Stun` `Knock back`)
- Antandra (98% `Stun`)
- Koko (98% `Stun`)

### Summary for Alsa

#### Alsa Provides

- Enhanced form — Area

#### Damage types dealt by Alsa

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target

#### Debuffs provided by Alsa

- Movement speed debuff — Area — `medium`
- Energy drain (Mythic+) — Single target — `low`

#### Crowd Control provided by Alsa

- Immune — Area — Permanent
- Knock back — Single target — `low`
- Stun — Single target — `high`

## Antandra

### Antandra's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Shield Assault (ultimate)
- **Movement**: high movement (repositioning skills)
- **Ally composition**: frontmost ally becomes guarded ally (shared shields)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, damage `low`

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

### Units Antandra benefits from

Look for units providing: `Max HP` `Healing` `Energy`  
Common buffers are **Rowan**, **Lyca**, or **Smokey & Meerky**.

- **Hepler**
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Pandora**
  - Max HP buff (single target, medium)
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Hewynn**
  - Healing (all units, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)

### Units benefitting most from Antandra

- Nerion
- Carolina
- Perseus

### Units that can act as a replacement for Antandra

**Buffs on allies**

- Contess (100% `Healing`)
- Gerda (100% `Healing`)
- Hepler (100% `Healing`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Atalanta (100% `Physical`)

**Crowd Control**

- Lumont (66% `Stun` `Taunt`)
- Lucca (60% `Stun` `Knock down`)
- Zorya (60% `Stun` `Knock down`)

### Summary for Antandra

#### Antandra Provides

- Stacking buff (Supreme+) — Single target

#### Antandra Requires

- Once per battle (Mythic+) — Allies

#### Damage types dealt by Antandra

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Self, Single target

#### Buffs provided by Antandra

- Healing — Multiple targets — `high`

#### Crowd Control provided by Antandra

- Unaffected — Area — On skill
- Knock down — Area — `medium`
- Stun — Area — `medium`
- Taunt — Area — `low`

## Arden

### Arden's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Force of Nature (ultimate)
- **Movement**: stationary (no finite attack range)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, damage `high`

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

### Units Arden benefits from

Look for units providing: `ATK` `Energy`  
Common buffers are **Rowan**, **Lyca**, or **Ravion**.

- **Pandora**
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
- **Thador**
  - Energy recovery (lieutenant, start of battle) `signature fuel`

### Units benefitting most from Arden

- Nerion
- Carolina
- Bonnie

### Units that can act as a replacement for Arden

**Similar Skills**

- Lorsan (100% `aoe-damage` `dot-specialist`)
- Faramor (80% `aoe-damage` `dot-specialist`)
- Viperian (66% `aoe-damage` `dot-specialist`)

**Damage**

- Alsa (100% `Magic`)
- Aurora (100% `Magic`)
- Berial (100% `Magic`)

**Crowd Control**

- Gwyneth (72% `Bind` `Stun`)
- Indris (60% `Bind`)
- Lorsan (60% `Stun`)

### Summary for Arden

#### Damage types dealt by Arden

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target

#### Crowd Control provided by Arden

- Bind — Multiple targets — `high`
- Stun — Multiple targets — `high`

## Atalanta

### Atalanta's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Wild Sniper (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, damage `medium`

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

### Units Atalanta benefits from

Look for units providing: `Haste` `Healing` `Physical DEF`  
Common buffers are **Rowan**, **Twins**, or **Hugin**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Atalanta

- Nerion
- Carolina
- Indris

### Units that can act as a replacement for Atalanta

**Similar Skills**

- Zandrok (66% `aoe-damage` `battle-start-burst`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Brutus (100% `Phys DEF debuff`)
- Kafra (100% `Phys DEF debuff`)
- Lyca (100% `Phys DEF debuff`)

**Crowd Control**

- Cassadee (90% `Knock back` `Stun`)
- Perseus (90% `Knock back` `Stun`)
- Korin (75% `Knock back` `Bind`)

### Summary for Atalanta

#### Atalanta Provides

- Reposition enemies — Single target
- Stat steal (EX+10) — Single target

#### Damage types dealt by Atalanta

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target

#### Debuffs provided by Atalanta

- Phys DEF debuff (Supreme+) — Single target — `high`

#### Crowd Control provided by Atalanta

- Bind — Single target — `medium`
- Knock back — Single target — `high`
- Stun — Single target — `medium`

## Athalia

### Athalia's behavior

`AFK Stages [S]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [S+]`

- **Signature skill**: Unbroken Retribution (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, buffs `medium`, debuffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `high`
- **True damage**: HP loss `high`, True damage `medium`

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

### Units Athalia benefits from

Look for units providing: `Max HP` `CRIT` `Execution` `Healing`  
Common buffers are **Hugin**, **Solise**, or **Twins**.

- **Contess**
  - Healing (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
  - Healing (single target, high)
- **Galahad**
  - Max HP via Shield (single target, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Athalia

- Indris
- Nerion
- Aliceth

### Units that can act as a replacement for Athalia

**Similar Skills**

- Baelran (80% `hp-scaling` `transformation`)
- Kordan (66% `hp-scaling` `self-repositioner`)

**Damage**

- Faramor (83% `Physical` `HP loss` `True damage`)
- Shadewing (69% `HP loss` `True damage`)

**Debuffs on enemies**

- Ravion (60% `ATK debuff`)

**Crowd Control**

- Baelran (100% `Knock down`)
- Ravion (100% `Knock down`)
- Kordan (60% `Knock down`)

### Summary for Athalia

#### Athalia Provides

- Invincibility — Self
- Transformation — Self

#### Damage types dealt by Athalia

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target
- HP loss — All units — `high`
- True damage — Single target — `medium`

#### Debuffs provided by Athalia

- ATK debuff — All units — `medium`

#### Crowd Control provided by Athalia

- Unaffected — Area — On skill
- Knock down — All units — `low`

## Aurora

### Aurora's behavior

`AFK Stages [A]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S+]`, `PVP [B]`

- **Signature skill**: Starlit Slumber (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, buffs `medium`, debuffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `high`

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

### Units Aurora benefits from

Look for units providing: `ATK` `Haste`  
Common buffers are **Twins**, **Hugin**, or **Velara**.

- **Mehira**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, low) `signature fuel`
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Aurora

- Damian
- Florabelle
- Mehira
- Phraesto
- Zanie
- Shadewing

### Units that can act as a replacement for Aurora

**Damage**

- Contess (100% `Magic`)
- Mehira (100% `Magic`)
- Saida (100% `Magic`)

### Summary for Aurora

#### Aurora Provides

- Invincibility — Multiple targets
- Start-of-battle cast — Multiple targets
- Summoning — Single target

#### Damage types dealt by Aurora

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target

#### Buffs provided by Aurora

- Haste buff — Summons only — `medium`
- Invincible — Single target — `high`
- Summon damage buff (Mythic+) — Summons only — `low`

#### Debuffs provided by Aurora

- Haste debuff — Multiple targets — `low`

#### Crowd Control provided by Aurora

- Unaffected — Self — On skill
- Sleep — Single target — `high`

## Baelran

### Baelran's behavior

`AFK Stages [S]`, `Dream Realm [A]`, `Dream Realm (Endless) [S]`, `PVP [S]`

- **Signature skill**: Celestial Rise (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, heal `medium`, buffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `high`
- **True damage**: True damage `high`

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

### Units Baelran benefits from

Look for units providing: `ATK` `Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Solise**, or **Velara**.

- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
- **Hewynn**
  - Healing (all units, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)

### Units benefitting most from Baelran

- Nerion
- Carolina

### Units that can act as a replacement for Baelran

**Damage**

- Silven (68% `True damage`)

**Debuffs on enemies**

- Contess (100% `Max HP debuff`)

### Summary for Baelran

#### Baelran Provides

- Start-of-battle cast — Arc
- Enhanced form (Mythic+) — Area
- Dispel debuffs (EX+15) — Area

#### Baelran Requires

- Boss encounter (Supreme+) — Enemies

#### Damage types dealt by Baelran

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- True damage — Arc, Area, Single target — `medium`

#### Debuffs provided by Baelran

- Max HP debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Baelran

- Unaffected — Self — Start of battle
- Knock down — Area — `medium`
- Knock up — Area — `high`

## Berial

### Berial's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Scared Swamp (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `low`

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

### Units Berial benefits from

Look for units providing: `Healing`  
Common buffers are **Rowan**, **Lyca**, or **Smokey & Meerky**.

- **Lorsan**
  - Healing (all units, high)
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Damian**
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, medium)

### Units benefitting most from Berial

- Nerion
- Carolina
- Bonnie

### Units that can act as a replacement for Berial

**Damage**

- Aurora (100% `Magic`)
- Bonnie (100% `Magic`)
- Bryon (100% `Magic`)

**Debuffs on enemies**

- Pandora (100% `Damage taken debuff` `Energy drain`)
- Sinbad (100% `Damage taken debuff` `Energy drain`)
- Contess (60% `Energy drain`)

**Crowd Control**

- Silvina (66% `Frighten`)

### Summary for Berial

#### Berial Provides

- Invincibility — Self
- Revive ally — Single target
- Summoning (Mythic+) — Single target

#### Damage types dealt by Berial

- Primary damage type (unit): **Magic**
- Magic — Area, Single target

#### Debuffs provided by Berial

- Damage taken debuff (Legendary+) — Single target — `low`
- Energy drain (Mythic+) — Single target — `low`

#### Crowd Control provided by Berial

- Frighten — Area — `medium`

## Bonnie

### Bonnie's behavior

`AFK Stages [B]`, `Dream Realm [A]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Decay's Reach (Skill 1)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, debuffs `medium`, damage `high`
- **Ultimate**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

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

### Units Bonnie benefits from

Look for units providing: `ATK`  
Common buffers are **Ravion**, **Rowan**, or **Velara**.

- **Lily May**
  - Enables Debuff on target via Energy drain (all units)
  - Enables Magic damage from allies via Magic damage + all enemies (all units)
- **Frieren**
  - Enables Debuff on target via DoT (area)
  - Enables Magic damage from allies via Magic damage + all enemies (all units)
- **Kulu**
  - Enables Debuff on target via Damage taken debuff (all units)
- **Alna**
  - ATK buff (single target, medium)
  - Enables Debuff on target via Haste debuff (area)
- **Shadewing**
  - Enables Debuff on target via Magic DEF debuff (all units)
  - Enables Magic damage from allies via Magic damage + all enemies (all units)

### Units benefitting most from Bonnie

- Indris
- Aliceth
- Shadewing

### Units that can act as a replacement for Bonnie

**Damage**

- Aurora (100% `Magic`)
- Contess (100% `Magic`)
- Cryonaia (100% `Magic`)

**Debuffs on enemies**

- Pandora (85% `ATK debuff` `Haste debuff` `Damage taken debuff`)

**Crowd Control**

- Aliceth (100% `Stun`)
- Contess (100% `Stun`)
- Faramor (100% `Stun`)

### Summary for Bonnie

#### Bonnie Provides

- Invincibility — Self
- Transformation — Self
- Magic damage amplification (Supreme+) — Single target

#### Bonnie Requires

- Debuff on target — Enemies
- Debuff on target (Aging) — Enemies
- Magic damage from allies — Allies

#### Damage types dealt by Bonnie

- Primary damage type (unit): **Magic**
- Magic — Area, Single target

#### Debuffs provided by Bonnie

- ATK debuff — Single target — `high`
- Haste debuff — Single target — `high`
- Damage taken debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Bonnie

- Stun — Single target — `low`

## Brutus

### Brutus's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Whirlwind Wrath (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, debuffs `medium`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`
- **True damage**: Max HP-based damage `high`

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

### Units Brutus benefits from

Look for units providing: `Life Drain`  
Common buffers are **Lyca**, **Rowan**, or **Ravion**.

- **Shakir**
  - Lifedrain buff (single target, medium)
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Valka**
  - Lifedrain buff (single target, high)
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Dunlingr**
  - Lifedrain buff (all units, low)
  - ATK SPD buff (all units, low) `signature fuel`
- **Pandora**
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Zandrok**
  - Lifedrain buff (area, low, conditional (frequent))
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Brutus

- Shadewing
- Indris
- Aliceth

### Units that can act as a replacement for Brutus

**Buffs on allies**

- Daimon (100% `Life Drain`)
- Dunlingr (100% `Life Drain`)
- Koko (100% `Life Drain`)

**Similar Skills**

- Zorya (66% `hp-scaling` `life-drain`)

**Damage**

- Gunnar (100% `Max HP-based damage` `DoT` `Physical`)
- Satrana (97% `Max HP-based damage`)
- Valka (88% `Max HP-based damage` `Physical`)

**Debuffs on enemies**

- Lyca (66% `Phys DEF debuff`)

**Crowd Control**

- Hepler (100% `Taunt`)

### Summary for Brutus

#### Damage types dealt by Brutus

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Self, Single target
- DoT — Area
- Max HP-based damage — Arc, Self — `high`

#### Buffs provided by Brutus

- Lifedrain buff — Single target — `medium`

#### Debuffs provided by Brutus

- DoT — Area — `low`
- Phys DEF debuff — Area — `medium`

#### Crowd Control provided by Brutus

- Immune — Self — On skill
- Unaffected — Self — On skill
- Taunt — Area — `high`

## Bryon

### Bryon's behavior

`AFK Stages [A+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Falcon Raid (ultimate)
- **Movement**: stationary (summon moves)

#### Skill overview

- **Signature skill (ultimate)**: speed `fast`, first cast speed `fast`, debuffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, damage `medium`

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

### Units Bryon benefits from

Look for units providing: `Haste` `Healing`  
Common buffers are **Solise**, **Mikola**, or **Velara**.

- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, medium)
- **Koko**
  - Healing (all units, medium)
- **Contess**
  - Healing (multiple targets, high)
- **Marcille**
  - Healing (multiple targets, high)

### Units benefitting most from Bryon

- Shadewing
- Bonnie
- Indris

### Units that can act as a replacement for Bryon

**Damage**

- Frieren (100% `DoT` `Magic`)
- Shadewing (68% `Magic` `DoT`)
- Eironn (60% `Magic`)

**Debuffs on enemies**

- Alna (100% `Haste debuff`)
- Eironn (60% `Haste debuff`)

**Crowd Control**

- Smokey & Meerky (100% `Interrupt` `Stun`)
- Faramor (60% `Stun`)
- Lenya (60% `Stun`)

### Summary for Bryon

#### Bryon Provides

- Start-of-battle cast — Single target
- Summoning — Self
- Counterattack (EX+10) — Single target

#### Damage types dealt by Bryon

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Area

#### Debuffs provided by Bryon

- Haste debuff — Area — `high`

#### Crowd Control provided by Bryon

- Interrupt — Single target — `low`
- Stun (Mythic+) — Single target — `low`

## Callan

### Callan's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Restless Guardian (ultimate)
- **Movement**: moving (avg attack range 1.7 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, buffs `medium`
- **Non-ultimate**: speed `fast`, damage `high`

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

### Units Callan benefits from

Look for units providing: `Healing`  
Common buffers are **Solise**, **Smokey & Meerky**, or **Mikola**.

- **Koko**
  - Healing (all units, medium)
- **Contess**
  - Healing (multiple targets, high)
- **Evie**
  - Healing (single target, high)
- **Pandora**
  - Healing (single target, high)
- **Zanie**
  - Healing (single target, high)

### Units benefitting most from Callan

- Nerion
- Carolina
- Perseus

### Units that can act as a replacement for Callan

**Buffs on allies**

- Daimon (100% `Max HP`)
- Galahad (100% `Max HP`)
- Hugin (100% `Max HP`)

**Damage**

- Contess (100% `Magic`)
- Cryonaia (100% `Magic`)
- Cyran (100% `Magic`)

**Crowd Control**

- Valka (100% `Knock down` `Stun`)
- Athalia (62% `Knock down`)
- Baelran (62% `Knock down`)

### Summary for Callan

#### Callan Provides

- Damage absorption (allies) — Multiple targets
- Stored damage release — Self

#### Callan Requires

- Stored resource threshold — Enemies

#### Damage types dealt by Callan

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target

#### Buffs provided by Callan

- Shield — Single target — `medium`

#### Crowd Control provided by Callan

- Unaffected — Self — Start of battle
- Knock down — All units — `low`
- Stun (Mythic+) — Single target — `medium`

## Carolina

### Carolina's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Frozen Grave (ultimate)
- **Movement**: mostly stationary (avg attack range 4.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, debuffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, debuffs `medium`, damage `medium`

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

### Units Carolina benefits from

Look for units providing: `CRIT`  
Common buffers are **Ravion**, **Lyca**, or **Twins**.

- **Tasi**
  - Enables CC on enemies via Sleep (all units, high)
- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Enables CC on enemies via Blind (area, high)
- **Baelran**
  - Enables CC on enemies via Knock up (area, high)
- **Indris**
  - Enables CC on enemies via Knock back (area, high)
- **Kordan**
  - Enables CC on enemies via Bind (area, high)

### Units benefitting most from Carolina

- Nerion
- Indris
- Bonnie

### Units that can act as a replacement for Carolina

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Debuffs on enemies**

- Eironn (100% `Haste debuff` `Magic DEF debuff`)
- Bonnie (60% `Haste debuff`)
- Shadewing (60% `Magic DEF debuff`)

**Crowd Control**

- Kordan (100% `Bind`)
- Gwyneth (66% `Bind`)
- Indris (66% `Bind`)

### Summary for Carolina

#### Carolina Provides

- Stacking buff — Area

#### Carolina Requires

- CC on enemies — Allies

#### Damage types dealt by Carolina

- Primary damage type (unit): **Magic**
- Magic — Area, Self, Single target

#### Debuffs provided by Carolina

- Haste debuff — Area — `low`
- Magic DEF debuff (Mythic+) — Area — `low`

#### Crowd Control provided by Carolina

- Bind — Area — `high`

## Cassadee

### Cassadee's behavior

`AFK Stages [C]`, `Dream Realm [A+]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Tidal Strength (Skill 2)
- **Movement**: stationary (avg attack range 10.0 tiles)
- **Ally composition**: nearest ally auto-selected at battle start; prioritizes ally behind

#### Skill overview

- **Signature skill**: speed `slow`, first cast speed `fast`, damage `low`
- **Ultimate**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, damage `medium`

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

### Units Cassadee benefits from

Look for units providing: `Haste`  
Common buffers are **Twins**, **Hugin**, or **Lyca**.

- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Valka**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Isabella**
  - Haste buff (multiple targets, low) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`

### Units benefitting most from Cassadee

- Nerion
- Carolina
- Bonnie

### Units that can act as a replacement for Cassadee

**Damage**

- Callan (100% `Magic`)
- Contess (100% `Magic`)
- Cryonaia (100% `Magic`)

**Debuffs on enemies**

- Eironn (100% `Magic DEF debuff`)
- Shadewing (100% `Magic DEF debuff`)
- Thador (100% `Magic DEF debuff`)

**Crowd Control**

- Perseus (66% `Knock back` `Stun`)
- Scarlita (65% `Knock back` `Knock up` `Stun`)

### Summary for Cassadee

#### Cassadee Provides

- Ally blessing — Single target

#### Cassadee Requires

- Ally blessing active (Supreme+) — Allies

#### Damage types dealt by Cassadee

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Debuffs provided by Cassadee

- Magic DEF debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Cassadee

- Knock back — All units — `medium`
- Knock up — Single target — `high`
- Stun — Single target — `high`

## Cecia

### Cecia's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Queen's Summons (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `low`

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

### Units Cecia benefits from

Look for units providing: `ATK SPD / Haste` `DEF Penetration` `Physical DEF` `Magic DEF`  
Common buffers are **Lyca**, **Rowan**, or **Twins**.

- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Fay**
  - ATK SPD buff (multiple targets, low) `signature fuel`
  - DEF buff (multiple targets, low)
  - DEF buff (multiple targets, low)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, medium)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`

### Units benefitting most from Cecia

- Perseus
- Silven
- Nerion

### Units that can act as a replacement for Cecia

**Similar Skills**

- Viperian (60% `dot-specialist` `life-drain`)

**Damage**

- Brutus (100% `Physical` `DoT`)
- Gunnar (100% `Physical` `DoT`)
- Hodgkin (68% `Physical`)

**Crowd Control**

- Alna (100% `Bind`)
- Arden (100% `Bind`)
- Carolina (100% `Bind`)

### Summary for Cecia

#### Cecia Provides

- Summoning — Self

#### Cecia Requires

- Enemy not CC-immune (Mythic+) — Enemies

#### Damage types dealt by Cecia

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- DoT — Arc, Single target

#### Buffs provided by Cecia

- ATK SPD buff — Single target — `low`
- DEF Penetration buff — Single target — `medium`
- Lifedrain buff — Area — `high`
- Max HP buff — Single target — `high`

#### Crowd Control provided by Cecia

- Bind — Single target — `high`

## Chippy

### Chippy's behavior

- **Signature skill**: Brothers-in-arms (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `normal`, damage `high`

##### Ultimate

summon two companion units to join the battle

##### Skill 1

leap at single target, dealing damage

##### Skill 2

rare chance for massive single normal attack damage

### Units Chippy benefits from

- **Pandora**
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Thador**
  - Energy recovery (lieutenant, start of battle) `signature fuel`
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Chippy

- Himmel

### Units that can act as a replacement for Chippy

**Similar Skills**

- Florabelle (100% `summoner`)
- Zanie (100% `summoner`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

### Summary for Chippy

#### Damage types dealt by Chippy

- Primary damage type (unit): **Physical**
- Physical — Single target

## Contess

### Contess's behavior

`AFK Stages [C]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S+]`, `PVP [S]`

- **Signature skill**: Detention Pass (ultimate)
- **Movement**: stationary (no finite attack range)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, first cast speed `fast`, heal `medium`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, debuffs `medium`, damage `medium`

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

### Units Contess benefits from

Look for units providing: `Max HP` `Healing` `Energy`  
Common buffers are **Solise**, **Velara**, or **Rowan**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Hepler**
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
- **Hewynn**
  - Healing (all units, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)

### Units benefitting most from Contess

**18** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Silven
- Himmel
- Aliceth
- Baelran
- Isabella
- Kordan
- Smokey & Meerky
- Alna
- Athalia
- Callan

### Units that can act as a replacement for Contess

**Buffs on allies**

- Solise (66% `Healing`)

**Damage**

- Saida (100% `Magic`)
- Solise (100% `Magic`)
- Velara (100% `Magic`)

**Debuffs on enemies**

- Sylphira (75% `Max HP debuff` `Energy drain`)

**Crowd Control**

- Gwyneth (93% `Silence` `Stun`)
- Sylphira (60% `Silence`)

### Summary for Contess

#### Contess Provides

- Start-of-battle cast — All units

#### Damage types dealt by Contess

- Primary damage type (unit): **Magic**
- Magic — All units, Multiple targets

#### Buffs provided by Contess

- ATK buff — Single target — `high`
- Healing — Multiple targets — `high`

#### Debuffs provided by Contess

- Energy drain — Single target — `low`
- Max HP debuff — Multiple targets — `low`
- ATK debuff (Legendary+) — Single target — `low`

#### Crowd Control provided by Contess

- Untargetable — Multiple targets — Start of battle
- Silence (Mythic+) — Single target — `high`
- Stun (Supreme+) — Single target — `medium`

## Cryonaia

### Cryonaia's behavior

`AFK Stages [B]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [S]`

- **Signature skill**: Frostveil Domain (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, debuffs `medium`, damage `high`

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

### Units Cryonaia benefits from

Look for units providing: `ATK` `Max HP`  
Common buffers are **Hugin**, **Ravion**, or **Twins**.

- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Galahad**
  - Max HP via Shield (single target, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Alna**
  - ATK buff (single target, medium)
  - Max HP buff (single target, low)
- **Zanie**
  - Max HP via Shield (single target, high)

### Units benefitting most from Cryonaia

- Bonnie
- Himmel
- Niru

### Units that can act as a replacement for Cryonaia

**Similar Skills**

- Alna (75% `battlefield-modification` `cc-immunity` `invincibility`)

**Damage**

- Contess (100% `Magic`)
- Cyran (100% `Magic`)
- Frieren (100% `Magic`)

**Debuffs on enemies**

- Kulu (100% `Damage taken debuff`)
- Mehira (100% `Damage taken debuff`)

### Summary for Cryonaia

#### Cryonaia Provides

- Enemy isolation (domain) — All units
- Battle time pause (EX+15) — Self
- Instant defeat (Supreme+) — Self

#### Cryonaia Requires

- Boss encounter — Enemies

#### Damage types dealt by Cryonaia

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Debuffs provided by Cryonaia

- Damage taken debuff (EX+5) — Single target — `low`

#### Crowd Control provided by Cryonaia

- Immune — Self — Conditional

## Cyran

### Cyran's behavior

`AFK Stages [S]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Gravitic Requiem (ultimate)
- **Movement**: mostly stationary (avg attack range 6.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, debuffs `medium`, damage `low`
- **True damage**: True damage `medium`

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

### Units Cyran benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `CRIT`  
Common buffers are **Hugin**, **Twins**, or **Ravion**.

- **Galahad**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, low) `signature fuel`
- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`

### Units benefitting most from Cyran

- Bonnie
- Nerion
- Indris

### Units that can act as a replacement for Cyran

**Damage**

- Frieren (100% `True damage` `Magic`)
- Sylphira (97% `True damage` `Magic`)
- Silven (86% `Magic` `True damage`)

**Debuffs on enemies**

- Athalia (100% `ATK debuff`)
- Ravion (100% `ATK debuff`)

**Crowd Control**

- Gwyneth (100% `Bind` `Silence`)

### Summary for Cyran

#### Cyran Provides

- Artifact mimic (Mythic+) — All units
- Enemy artifact block (EX+10) — Single target

#### Damage types dealt by Cyran

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- True damage — All units — `medium`

#### Debuffs provided by Cyran

- ATK debuff (Mythic+) — All units — `low`

#### Crowd Control provided by Cyran

- Steadfast — Area — Conditional
- Unaffected — Self — Start of battle
- Bind — Area — `low`
- Silence (EX+10) — Single target — `high`

## Daimon

### Daimon's behavior

`AFK Stages [B]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Buddy Barrier (Skill 2)
- **Movement**: stationary (no finite attack range)
- **Ally composition**: place ally directly behind at battle prep (shield share, Life Drain, and ATK bond)

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `medium`
- **Ultimate**: speed `slow`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, damage `high`
- **True damage**: Max HP-based damage `high`

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

### Units Daimon benefits from

Look for units providing: `Max HP`  
Common buffers are **Hugin**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
- **Galahad**
  - Max HP via Shield (single target, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, medium)

### Units benefitting most from Daimon

- Gerda

### Units that can act as a replacement for Daimon

**Buffs on allies**

- Hugin (66% `Max HP`)
- Saida (66% `Max HP`)

**Similar Skills**

- Shemira (72% `hp-scaling` `life-drain` `summoner`)

**Damage**

- Shadewing (100% `Max HP-based damage` `Magic`)
- Shemira (100% `Max HP-based damage` `Magic`)
- Gunnar (85% `Max HP-based damage`)

### Summary for Daimon

#### Damage types dealt by Daimon

- Primary damage type (unit): **Magic**
- Magic — Area, Self, Single target
- Max HP-based damage — Area — `high`

#### Buffs provided by Daimon

- Lifedrain buff — Single target — `medium`
- Shield — Multiple targets — `medium`

#### Crowd Control provided by Daimon

- Frighten (Mythic+) — Area — `low`

## Damian

### Damian's behavior

`AFK Stages [C]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Inventor's Will (Mythic+)
- **Movement**: stationary (off battlefield)

#### Skill overview

- **Signature skill**: speed `fast`, heal `medium`, buffs `medium`, damage `low`
- **Ultimate**: speed `slow`, first cast speed `fast`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

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

### Units Damian benefits from

Look for units providing: `ATK` `Haste` `Energy`  
Common buffers are **Hugin**, **Mikola**, or **Ravion**.

- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, medium)
- **Galahad**
  - Haste buff (single target, high) `signature fuel`
- **Mehira**
  - Haste buff (single target, high) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Damian

- Viperian
- Natsu
- Odie

### Units that can act as a replacement for Damian

**Buffs on allies**

- Velara (100% `Healing` `Haste`)
- Solise (68% `Healing`)
- Hepler (67% `Healing` `Haste`)

**Similar Skills**

- Laios (66% `ally-healer` `summoner`)
- Florabelle (60% `summoner`)

**Damage**

- Callan (100% `Magic`)
- Cassadee (100% `Magic`)
- Contess (100% `Magic`)

**Crowd Control**

- Hepler (94% `Blind` `Stun`)
- Aliceth (66% `Blind` `Stun`)
- Faramor (60% `Stun`)

### Summary for Damian

#### Damian Provides

- Summoning — All units

#### Damage types dealt by Damian

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Buffs provided by Damian

- Healing — Area — `medium`
- Haste buff (Mythic+) — Multiple targets — `medium` — conditional (frequent)

#### Crowd Control provided by Damian

- Blind — Single target — `high`
- Stun — Single target — `high`

## Dionel

### Dionel's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Dawn Light (ultimate)
- **Movement**: moving (avg attack range 0.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `medium`
- **True damage**: True damage `medium`

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

### Units Dionel benefits from

Look for units providing: `ATK SPD / Haste` `Max HP` `Execution`  
Common buffers are **Hugin**, **Twins**, or **Rowan**.

- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
  - Max HP via Shield (single target, medium)
- **Pandora**
  - Max HP buff (single target, medium)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, low)

### Units benefitting most from Dionel

- Nerion
- Silven
- Aliceth

### Units that can act as a replacement for Dionel

**Buffs on allies**

- Aliceth (100% `DEF Penetration`)
- Kordan (66% `DEF Penetration`)
- Zanie (66% `DEF Penetration`)

**Damage**

- Athalia (100% `Physical` `True damage`)
- Baelran (100% `True damage` `Physical`)
- Sylphira (100% `True damage`)

**Debuffs on enemies**

- Alna (100% `Vitality debuff`)
- Frieren (100% `Vitality debuff`)
- Nazrik (100% `Vitality debuff`)

**Crowd Control**

- Baelran (100% `Knock up`)
- Florabelle (100% `Knock up`)
- Zandrok (66% `Knock up`)

### Summary for Dionel

#### Dionel Provides

- Stacking buff — Single target
- Execution scaling (Supreme+) — Self

#### Damage types dealt by Dionel

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target
- True damage — All units, Single target — `medium`

#### Buffs provided by Dionel

- DEF Penetration buff — Single target — `high`

#### Debuffs provided by Dionel

- Vitality debuff (Mythic+) — Single target — `medium`

#### Crowd Control provided by Dionel

- Untargetable — Area — On skill
- Knock up — Area — `low`

## Dunlingr

### Dunlingr's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S+]`

- **Signature skill**: Echo of Silence (ultimate)
- **Movement**: stationary (avg attack range 6.4 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, heal `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `medium`
- **True damage**: HP loss `medium`

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

### Units Dunlingr benefits from

Look for units providing: `ATK SPD / Haste` `Max HP` `Healing`  
Common buffers are **Solise**, **Hugin**, or **Twins**.

- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
  - Max HP via Shield (summons only, medium)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, medium)
- **Contess**
  - Healing (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
  - Healing (single target, high)

### Units benefitting most from Dunlingr

- Marcille

### Units that can act as a replacement for Dunlingr

**Damage**

- Athalia (100% `HP loss`)
- Aliceth (90% `HP loss`)
- Niru (84% `Magic` `HP loss`)

**Crowd Control**

- Sylphira (96% `Silence`)
- Contess (60% `Silence`)
- Cyran (60% `Silence`)

### Summary for Dunlingr

#### Dunlingr Provides

- Summoning — Self
- Ultimate lock (Spellbind) — All units

#### Damage types dealt by Dunlingr

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target
- HP loss — Area — `medium`

#### Buffs provided by Dunlingr

- ATK buff (EX+5) — Single target — `low`
- Haste buff (EX+15) — Single target — `low`
- ATK SPD buff (Supreme+) — All units — `low`
- Lifedrain buff (Supreme+) — All units — `low`

#### Debuffs provided by Dunlingr

- ATK debuff — Area — `low`
- Energy drain (Supreme+) — All units — `low`

#### Crowd Control provided by Dunlingr

- Silence — All units — `low`

## Eironn

### Eironn's behavior

`AFK Stages [S+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Howling Hurricane (Mythic+)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill**: speed `fast`
- **Ultimate**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `medium`

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

### Units Eironn benefits from

Look for units providing: `Max HP` `Physical DEF`  
Common buffers are **Hugin** or **Rowan**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
- **Galahad**
  - Max HP via Shield (single target, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, medium)

### Units benefitting most from Eironn

- Indris
- Bonnie
- Nerion

### Units that can act as a replacement for Eironn

**Damage**

- Aurora (100% `Magic`)
- Contess (100% `Magic`)
- Cryonaia (100% `Magic`)

**Debuffs on enemies**

- Shadewing (60% `Magic DEF debuff`)

**Crowd Control**

- Ravion (65% `Displace`)

### Summary for Eironn

#### Damage types dealt by Eironn

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Single target

#### Debuffs provided by Eironn

- Haste debuff — Arc — `medium`
- Magic DEF debuff — Arc — `high`

#### Crowd Control provided by Eironn

- Bind — Single target — `high`
- Displace — Area — `medium`

## Twins

### Twins's behavior

`AFK Stages [S]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S+]`, `PVP [A+]`

- **Signature skill**: Starlight Waltz (ultimate)
- **Movement**: moving / stationary (two units)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `medium`, buffs `medium`, damage `low`

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

### Units Twins benefits from

Look for units providing: `Haste` `Healing` `Energy`  
Common buffers are **Solise**, **Rowan**, or **Hugin**.

- **Gunnar**
  - ATK SPD buff (single target, low) `signature fuel`
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Twins

**74** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Perseus
- Silven
- Alsa
- Hepler
- Lenya
- Lumont
- Mehira
- Soren
- Tasi
- Zorya

### Units that can act as a replacement for Twins

**Damage**

- Solise (100% `Magic`)

### Summary for Twins

#### Twins Provides

- Ally positioning link — Single target
- Shared HP and Energy — All units

#### Twins Requires

- Ally on positioning link (Supreme+) — —

#### Damage types dealt by Twins

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target

#### Buffs provided by Twins

- Haste buff — All units — `medium`
- Max HP buff — Multiple targets — `medium`
- Shield — Single target — `low`
- Vitality buff (Mythic+) — Multiple targets — `low`

#### Crowd Control provided by Twins

- Unaffected — Area — On skill
- Blind — Area — `low`
- Knock back — Area — `low`

## Evie

### Evie's behavior

`AFK Stages [B]`, `Dream Realm [B]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Intel Chase (ultimate)
- **Movement**: high movement (repositioning skills)
- **Ally composition**: rearmost ally starts with healing quill; tracks highest damage dealer

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, buffs `medium`, debuffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `medium`, buffs `medium`, damage `high`

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

### Units Evie benefits from

Look for units providing: `Healing`  
Common buffers are **Solise**, **Smokey & Meerky**, or **Mikola**.

- **Koko**
  - Healing (all units, medium)
- **Contess**
  - Healing (multiple targets, high)
- **Pandora**
  - Healing (single target, high)
- **Zanie**
  - Healing (single target, high)
- **Hewynn**
  - Healing (all units, high)

### Units benefitting most from Evie

- Smokey & Meerky

### Units that can act as a replacement for Evie

**Buffs on allies**

- Mikola (100% `ATK` `Healing`)
- Hugin (80% `ATK`)
- Contess (66% `ATK` `Healing`)

**Damage**

- Callan (100% `Magic`)
- Contess (100% `Magic`)
- Cryonaia (100% `Magic`)

**Debuffs on enemies**

- Frieren (100% `DoT`)

**Crowd Control**

- Eironn (63% `Displace` `Bind`)
- Gwyneth (61% `Bind` `Silence`)

### Summary for Evie

#### Evie Provides

- Invincibility — Self
- Start-of-battle cast — All units

#### Evie Requires

- Passive with internal cooldown — Allies

#### Damage types dealt by Evie

- Primary damage type (unit): **Magic**
- Magic — All units, Multiple targets, Single target

#### Buffs provided by Evie

- ATK buff — Multiple targets — `high`
- Healing — Single target — `high`

#### Debuffs provided by Evie

- DoT — All units — `medium`

#### Crowd Control provided by Evie

- Bind — All units — `low`
- Displace — All units — `low`
- Silence — All units — `low`

## Faramor

### Faramor's behavior

`AFK Stages [S]`, `Dream Realm [S]`, `Dream Realm (Endless) [A+]`, `PVP [B]`

- **Signature skill**: Sanctified Circle (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Ally composition**: bless adjacent ally at battle prep; prioritizes tile behind

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, damage `high`
- **True damage**: HP loss `high`, True damage `high`

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

### Units Faramor benefits from

Look for units providing: `ATK` `Haste` `Max HP`  
Common buffers are **Hugin**, **Twins**, or **Velara**.

- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - Max HP via Shield (single target, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Mehira**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Zanie**
  - Max HP via Shield (single target, high)
- **Gunnar**
  - ATK SPD buff (single target, low) `signature fuel`

### Units benefitting most from Faramor

- Nerion
- Carolina
- Indris

### Units that can act as a replacement for Faramor

**Damage**

- Shadewing (70% `HP loss` `True damage`)

**Crowd Control**

- Gunnar (62% `Stun`)

### Summary for Faramor

#### Faramor Provides

- Revive ally (Supreme+) — Single target

#### Faramor Requires

- Once per battle (EX+10) — Enemies

#### Damage types dealt by Faramor

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- HP loss — Single target — `high`
- True damage — Multiple targets — `high`

#### Debuffs provided by Faramor

- Vitality debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Faramor

- Stun — Area — `medium`

## Fay

### Fay's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [B]`, `PVP [B]`

- **Signature skill**: Vibrant Dance (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, buffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `medium`

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

### Units Fay benefits from

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Lyca**, **Twins**, or **Hugin**.

- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Pandora**
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Fay

- Perseus
- Silven
- Indris

### Units that can act as a replacement for Fay

**Buffs on allies**

- Rowan (65% `Healing` `Magic DEF` `Physical DEF`)
- Mikola (63% `Healing` `ATK` `Vitality buff`)

**Similar Skills**

- Ludovic (100% `ally-healer` `aoe-healing`)
- Smokey & Meerky (100% `ally-healer` `aoe-healing`)
- Solise (66% `ally-healer` `aoe-healing`)

**Damage**

- Aurora (100% `Magic`)
- Bonnie (100% `Magic`)
- Bryon (100% `Magic`)

**Debuffs on enemies**

- Indris (75% `Phys DEF debuff` `Magic DEF debuff`)
- Cassadee (60% `Magic DEF debuff`)
- Zanie (60% `Phys DEF debuff`)

### Summary for Fay

#### Damage types dealt by Fay

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Multiple targets, Single target

#### Buffs provided by Fay

- ATK SPD buff — Multiple targets — `low`
- ATK buff — Multiple targets — `low`
- DEF buff — Multiple targets — `low`
- Healing — Arc — `medium` — conditional (frequent)
- Vitality buff (EX+5) — Single target — `low`

#### Debuffs provided by Fay

- Magic DEF debuff — Multiple targets — `low`
- Phys DEF debuff — Multiple targets — `low`

## Florabelle

### Florabelle's behavior

`AFK Stages [B]`, `Dream Realm [S]`, `Dream Realm (Endless) [S]`, `PVP [B]`

- **Signature skill**: Pounding Blow (ultimate)
- **Movement**: stationary (no finite attack range)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `low`

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

### Units Florabelle benefits from

Look for units providing: `ATK` `Haste`  
Common buffers are **Hugin**, **Twins**, or **Velara**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, medium)
- **Galahad**
  - Haste buff (single target, high) `signature fuel`
- **Mehira**
  - Haste buff (single target, high) `signature fuel`
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Vala**
  - Haste buff (single target, high) `signature fuel`

### Units benefitting most from Florabelle

- Dunlingr
- Bryon
- Damian
- Phraesto

### Units that can act as a replacement for Florabelle

**Similar Skills**

- Zanie (100% `summoner`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Crowd Control**

- Baelran (100% `Knock up`)

### Summary for Florabelle

#### Florabelle Provides

- Summoning — Self

#### Damage types dealt by Florabelle

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Florabelle

- Lifedrain buff — Summons only — `high` — conditional (frequent)
- Shield (Mythic+) — Summons only — `medium`
- Haste buff (EX+10) — Summons only — `medium` — conditional (frequent)
- Summon damage buff (Supreme+) — Summons only — `medium`

#### Crowd Control provided by Florabelle

- Immune (Supreme+) — Self — Form
- Knock up — Area — `low`

## Frieren

### Frieren's behavior

`AFK Stages [B]`, `Dream Realm [B]`, `Dream Realm (Endless) [S+]`, `PVP [A+]`

- **Signature skill**: Zoltraak (ultimate)
- **Movement**: stationary (avg attack range 7.0 tiles)
- **Ally composition**: frontmost ally shares damage reduction with this hero

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, debuffs `medium`, damage `high`
- **True damage**: True damage `high`

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

### Units Frieren benefits from

Look for units providing: `ATK` `Haste`  
Common buffers are **Hugin**, **Twins**, or **Ravion**.

- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, low) `signature fuel`
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Vala**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Frieren

- Bonnie

### Units that can act as a replacement for Frieren

**Damage**

- Sylphira (86% `True damage` `Magic`)
- Shadewing (77% `Magic` `DoT` `True damage`)
- Faramor (76% `True damage`)

**Crowd Control**

- Athalia (66% `Knock down`)
- Baelran (66% `Knock down`)
- Kordan (66% `Knock down`)

### Summary for Frieren

#### Damage types dealt by Frieren

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target
- DoT — All units, Single target
- True damage — All units, Single target — `high`

#### Debuffs provided by Frieren

- DoT — Area — `high`
- Vitality debuff — Single target — `high`

#### Crowd Control provided by Frieren

- Stun — Single target — `low`
- Knock down (Supreme+) — Single target — `medium`

## Galahad

### Galahad's behavior

`AFK Stages [S]`, `Dream Realm [B]`, `Dream Realm (Endless) [S+]`, `PVP [A]`

- **Signature skill**: Time Recast (Mythic+)
- **Movement**: stationary (avg attack range 10.0 tiles)
- **Ally composition**: nearest ally auto-selected at battle start; prioritizes ally behind

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`
- **Ultimate**: speed `normal`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, damage `high`

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

### Units Galahad benefits from

Look for units providing: `ATK` `Haste` `Energy`  
Common buffers are **Hugin**, **Twins**, or **Velara**.

- **Mehira**
  - Haste buff (single target, high) `signature fuel`
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Vala**
  - Haste buff (single target, high) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, low)
  - Haste buff (single target, low) `signature fuel`

### Units benefitting most from Galahad

**18** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Alsa
- Lenya
- Faramor
- Cassadee
- Frieren
- Koko
- Ravion
- Cyran
- Pippa
- Rowan

### Units that can act as a replacement for Galahad

**Buffs on allies**

- Hugin (100% `Haste` `Max HP`)
- Twins (80% `Haste` `Max HP`)
- Mehira (60% `Haste`)

**Damage**

- Contess (100% `Magic`)
- Mehira (100% `Magic`)
- Saida (100% `Magic`)

**Crowd Control**

- Gwyneth (100% `Bind`)
- Velara (100% `Bind`)

### Summary for Galahad

#### Galahad Provides

- Artifact amplification (EX+10) — Single target

#### Galahad Requires

- Artifact buffs active (Supreme+) — Self

#### Damage types dealt by Galahad

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Buffs provided by Galahad

- Haste buff — Single target — `high`
- Shield — Single target — `medium`

#### Crowd Control provided by Galahad

- Steadfast (Supreme+) — Self — On skill
- Bind — Single target — `medium`

## Gerda

### Gerda's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Spring Therapy (Skill 1)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, heal `medium`, damage `medium`
- **Ultimate**: speed `slow`, heal `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `medium`, buffs `medium`, damage `medium`

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

### Units Gerda benefits from

Look for units providing: `Max HP`  
Common buffers are **Hugin**.

- **Hepler**
  - Max HP via Shield (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Daimon**
  - Max HP via Shield (multiple targets, medium)
- **Koko**
  - Max HP via Shield (all units, low)
- **Lenya**
  - Max HP via Shield (single target, high)

### Units benefitting most from Gerda

- Perseus
- Silven
- Nerion

### Units that can act as a replacement for Gerda

**Buffs on allies**

- Mikola (98% `Healing`)
- Solise (79% `Healing`)
- Hepler (63% `Healing`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Crowd Control**

- Smokey & Meerky (80% `Interrupt` `Stun`)
- Koko (60% `Stun`)

### Summary for Gerda

#### Damage types dealt by Gerda

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target

#### Buffs provided by Gerda

- Healing — Multiple targets — `high`
- Healing over time — Area — `medium`

#### Crowd Control provided by Gerda

- Unaffected — Self — Start of battle
- Interrupt — Single target — `medium`
- Stun — Single target — `high`

## Granny Dahnie

### Granny Dahnie's behavior

`AFK Stages [C]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Threshold of Jade (ultimate)
- **Movement**: moving (avg attack range 2.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `low`

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

### Units Granny Dahnie benefits from

Look for units providing: `Healing` `Energy` `Physical DEF` `Magic DEF`  
Common buffers are **Rowan**, **Lyca**, or **Smokey & Meerky**.

- **Lorsan**
  - Healing (all units, high)
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Fay**
  - Healing (arc, medium, conditional (frequent))
  - DEF buff (multiple targets, low)
  - DEF buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`
- **Damian**
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Hepler**
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Granny Dahnie

- Nerion
- Indris
- Carolina

### Units that can act as a replacement for Granny Dahnie

**Similar Skills**

- Brutus (66% `hp-scaling` `taunt`)
- Tilaya (60% `hp-scaling`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Debuffs on enemies**

- Bonnie (100% `ATK debuff` `Haste debuff`)
- Pandora (100% `ATK debuff` `Haste debuff`)
- Bryon (60% `Haste debuff`)

**Crowd Control**

- Hepler (80% `Taunt` `Stun`)
- Faramor (68% `Stun`)
- Lorsan (68% `Stun`)

### Summary for Granny Dahnie

#### Damage types dealt by Granny Dahnie

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target

#### Debuffs provided by Granny Dahnie

- Haste debuff — Single target — `medium`
- ATK debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Granny Dahnie

- Unaffected — Self — On skill
- Stun — Area — `low`
- Taunt — Single target — `high`

## Gunnar

### Gunnar's behavior

`AFK Stages [S+]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S+]`, `PVP [S]`

- **Signature skill**: Annihilation Directive (ultimate)
- **Movement**: stationary (no finite attack range)
- **Ally composition**: place ally 1 tile behind at battle start (Doomfield buffs and coordinated attacks)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `medium`
- **True damage**: Max HP-based damage `medium`

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

### Units Gunnar benefits from

Look for units providing: `ATK SPD / Haste` `Max HP` `Healing`  
Common buffers are **Hugin**, **Twins**, or **Lyca**.

- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
- **Hewynn**
  - Healing (all units, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)

### Units benefitting most from Gunnar

- Shadewing
- Gwyneth
- Aurora
- Twins
- Hugin
- Solise

### Units that can act as a replacement for Gunnar

**Buffs on allies**

- Fay (66% `ATK SPD` `Vitality buff`)

**Damage**

- Brutus (96% `Max HP-based damage` `DoT` `Physical`)
- Korin (86% `Max HP-based damage` `Physical`)
- Valka (86% `Max HP-based damage` `Physical`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Arden (100% `Stun`)

### Summary for Gunnar

#### Gunnar Provides

- Invincibility (EX+15) — Single target

#### Damage types dealt by Gunnar

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target
- DoT — Area
- Max HP-based damage — All units — `medium`

#### Buffs provided by Gunnar

- ATK SPD buff — Single target — `low`
- Ranged DEF buff (Legendary+) — Single target — `low`
- Vitality buff (Legendary+) — Single target — `low`

#### Crowd Control provided by Gunnar

- Stun — All units — `low`

## Gwyneth

### Gwyneth's behavior

`AFK Stages [A]`, `Dream Realm [S+]`, `Dream Realm (Endless) [?]`, `PVP [S]`

- **Signature skill**: Hailing Arrows (ultimate)
- **Movement**: stationary (avg attack range 8.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, debuffs `medium`, damage `high`
- **True damage**: Max HP-based damage `low`

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

### Units Gwyneth benefits from

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Twins**, **Velara**, or **Lyca**.

- **Gunnar**
  - ATK SPD buff (single target, low) `signature fuel`
- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Gwyneth

- Nerion
- Carolina
- Shadewing

### Units that can act as a replacement for Gwyneth

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Shadewing (72% `Max HP-based damage`)

### Summary for Gwyneth

#### Damage types dealt by Gwyneth

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- Max HP-based damage — Single target — `low`

#### Debuffs provided by Gwyneth

- DoT — Single target — `high`

#### Crowd Control provided by Gwyneth

- Bind — Area — `medium`
- Silence — Area — `low`
- Stun — Area — `low`

## Hammie

### Hammie's behavior

- **Signature skill**: Pretty Fireball (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `normal`, heal `medium`, buffs `medium`, damage `medium`

##### Ultimate

single-target fireball dealing damage

##### Skill 1

heal weakest ally and buff them

##### Skill 2

self-heal

### Units Hammie benefits from

Look for units providing: `ATK` `Healing`  
Common buffers are **Rowan**, **Mikola**, or **Lyca**.

- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)
- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (single target, high)
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Hammie

- Bonnie
- Himmel
- Perseus

### Units that can act as a replacement for Hammie

**Buffs on allies**

- Aliceth (100% `ATK`)
- Alna (100% `ATK`)
- Contess (100% `ATK`)

**Similar Skills**

- Isabella (66% `ally-buffer` `ally-healer`)
- Laios (66% `ally-buffer` `ally-healer`)
- Perseus (60% `ally-buffer`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

### Summary for Hammie

#### Damage types dealt by Hammie

- Primary damage type (unit): **Magic**
- Magic — Single target

#### Buffs provided by Hammie

- ATK buff — Multiple targets — `low`

## Harak

### Harak's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [A+]`, `PVP [B]`

- **Signature skill**: Flesh Feast (Skill 2)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `medium`, debuffs `medium`
- **Ultimate**: speed `slow`, heal `medium`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `low`
- **True damage**: HP loss `low`

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

### Units Harak benefits from

Look for units providing: `Haste` `Max HP` `CRIT` `Healing` `Energy`  
Common buffers are **Rowan**, **Hugin**, or **Smokey & Meerky**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Contess**
  - Healing (multiple targets, high)
- **Marcille**
  - Healing (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`

### Units benefitting most from Harak

- Perseus
- Silven
- Nerion

### Units that can act as a replacement for Harak

**Buffs on allies**

- Aurora (75% `Invincible`)
- Pandora (75% `Invincible`)

**Damage**

- Aliceth (100% `Physical` `HP loss`)
- Athalia (100% `Physical` `HP loss`)
- Faramor (100% `Physical` `HP loss`)

**Debuffs on enemies**

- Aliceth (100% `Execution debuff`)

**Crowd Control**

- Athalia (100% `Knock down`)
- Baelran (100% `Knock down`)
- Callan (100% `Knock down`)

### Summary for Harak

#### Harak Provides

- Instant defeat — Single target
- Invincibility — Single target

#### Harak Requires

- Boss encounter — Allies

#### Damage types dealt by Harak

- Primary damage type (unit): **Physical**
- Physical — Single target
- HP loss — Single target — `low`

#### Buffs provided by Harak

- Invincible — Single target — `high`
- Lifedrain buff (Legendary+) — Single target — `low`

#### Debuffs provided by Harak

- Execution debuff — Single target — `low`

#### Crowd Control provided by Harak

- Unaffected — Self — Start of battle
- Knock down — Single target — `low`

## Hepler

### Hepler's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Form Shift (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Ally composition**: frontmost adjacent ally gets fatal-blow protection

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `high`

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

### Units Hepler benefits from

Look for units providing: `ATK` `Haste` `Max HP` `Healing`  
Common buffers are **Hugin**, **Twins**, or **Rowan**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Pandora**
  - Max HP buff (single target, medium)
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - Max HP via Shield (single target, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)

### Units benefitting most from Hepler

**19** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Nerion
- Carolina
- Lumont
- Soren
- Tasi
- Gunnar
- Antandra
- Salazer
- Lucca
- Contess

### Units that can act as a replacement for Hepler

**Buffs on allies**

- Koko (86% `Healing` `Max HP`)

**Similar Skills**

- Ulmus (66% `ally-shielder` `transformation`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Debuffs on enemies**

- Alna (100% `Haste debuff`)
- Bonnie (100% `Haste debuff`)
- Bryon (100% `Haste debuff`)

### Summary for Hepler

#### Hepler Provides

- Invincibility (Mythic+) — Area

#### Damage types dealt by Hepler

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target

#### Buffs provided by Hepler

- Haste buff — Single target — `low`
- Healing — Multiple targets — `high`
- Shield — Multiple targets — `high`

#### Debuffs provided by Hepler

- Haste debuff — Area — `low`

#### Crowd Control provided by Hepler

- Blind — Area — `high`
- Stun — Area — `low`
- Taunt — Area — `high`

## Hewynn

### Hewynn's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Rain Prayer (ultimate)
- **Movement**: stationary (no finite attack range)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, damage `low`
- **Non-ultimate**: speed `fast`, heal `medium`, damage `medium`

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

### Units Hewynn benefits from

Look for units providing: `ATK`  
Common buffers are **Lyca**, **Hugin**, or **Rowan**.

- **Pandora**
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
- **Thador**
  - Energy recovery (lieutenant, start of battle) `signature fuel`

### Units benefitting most from Hewynn

- Gunnar
- Lucca
- Lucius
- Saida

### Units that can act as a replacement for Hewynn

**Buffs on allies**

- Lorsan (100% `Healing`)
- Solise (100% `Healing`)
- Smokey & Meerky (80% `Healing`)

**Similar Skills**

- Fay (100% `ally-healer` `aoe-healing`)
- Ludovic (100% `ally-healer` `aoe-healing`)
- Smokey & Meerky (100% `ally-healer` `aoe-healing`)

**Damage**

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Cassadee (100% `Magic`)

### Summary for Hewynn

#### Hewynn Requires

- Passive with internal cooldown — Allies

#### Damage types dealt by Hewynn

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Hewynn

- Healing — All units — `high`

#### Crowd Control provided by Hewynn

- Unaffected (Mythic+) — Self — On skill

## Himmel

### Himmel's behavior

`AFK Stages [B]`, `Dream Realm [A]`, `Dream Realm (Endless) [A+]`, `PVP [A]`

- **Signature skill**: Hero Party (Skill 2)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill**: speed `slow`, first cast speed `fast`, buffs `medium`, damage `medium`
- **Ultimate**: speed `normal`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `medium`, buffs `medium`, damage `medium`
- **True damage**: Max HP-based damage `low`

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

### Units Himmel benefits from

Look for units providing: `ATK` `Haste` `Max HP` `Healing`  
Common buffers are **Hugin**, **Twins**, or **Solise**.

- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)
  - Enables Party composition via Support (party slot)
- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - Max HP via Shield (single target, medium)
  - Enables Party composition via Mage (party slot)
- **Alna**
  - ATK buff (single target, medium)
  - Max HP buff (single target, low)
  - Enables Party composition via Tank (party slot)
- **Mehira**
  - Haste buff (single target, high) `signature fuel`
  - Enables Party composition via Mage (party slot)
- **Saida**
  - Max HP via Shield (multiple targets, high)

### Units benefitting most from Himmel

- Cryonaia

### Units that can act as a replacement for Himmel

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Gwyneth (85% `Physical` `Max HP-based damage`)
- Shadewing (80% `Max HP-based damage`)

### Summary for Himmel

#### Himmel Requires

- Party composition — Allies
- Boss encounter (Supreme+) — —

#### Damage types dealt by Himmel

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Multiple targets, Self, Single target
- Max HP-based damage — All units — `low`

#### Buffs provided by Himmel

- Shield — Single target — `low`
- ATK buff (Mythic+) — Multiple targets — `low`
- Max HP buff (Mythic+) — Multiple targets — `high`

## Hodgkin

### Hodgkin's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Cannon Fire (ultimate)
- **Movement**: moving (avg attack range 3.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, debuffs `medium`, damage `medium`

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

### Units Hodgkin benefits from

Look for units providing: `ATK` `Healing` `Energy`  
Common buffers are **Rowan**, **Smokey & Meerky**, or **Mikola**.

- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)
- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (single target, high)
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Hodgkin

- Indris
- Aliceth
- Bonnie

### Units that can act as a replacement for Hodgkin

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Sinbad (100% `Energy drain` `Vitality debuff` `Phys DEF debuff`)
- Silvina (77% `Energy drain` `Vitality debuff`)

### Summary for Hodgkin

#### Hodgkin Provides

- Summoning (Mythic+) — Area
- Stacking buff (Supreme+) — Single target

#### Damage types dealt by Hodgkin

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target

#### Debuffs provided by Hodgkin

- Energy drain (Mythic+) — Area — `low`
- Phys DEF debuff (Supreme+) — Single target — `low`
- Vitality debuff (Supreme+) — Single target — `medium`

## Hugin

### Hugin's behavior

`AFK Stages [S+]`, `Dream Realm [B]`, `Dream Realm (Endless) [S]`, `PVP [A+]`

- **Signature skill**: Unstoppable! (ultimate)
- **Movement**: stationary (no finite attack range)
- **Self placement**: stays anchored to battle-prep tile; returns after displacement
- **Ally composition**: put one ally 1 tile behind him (ATK bonus; buff ends if they leave the sigil)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, buffs `medium`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, damage `high`

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

### Units Hugin benefits from

Look for units providing: `Haste` `Energy`  
Common buffers are **Twins**, **Velara**, or **Lyca**.

- **Mehira**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, low) `signature fuel`
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Hugin

**83** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Perseus
- Tasi
- Alsa
- Frieren
- Hepler
- Lenya
- Lorsan
- Lumont
- Mehira
- Natsu

### Units that can act as a replacement for Hugin

**Similar Skills**

- Twins (66% `ally-shielder` `energy-provider`)

**Damage**

- Baelran (100% `Physical`)
- Gunnar (100% `Physical`)
- Gwyneth (100% `Physical`)

### Summary for Hugin

#### Damage types dealt by Hugin

- Primary damage type (unit): **Physical**
- Physical — Multiple targets, Single target

#### Buffs provided by Hugin

- ATK buff — Multiple targets — `high`
- Haste buff — Multiple targets — `high`
- Shield (Mythic+) — Multiple targets — `high`

## Igor

### Igor's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Funereal Ring (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, debuffs `medium`, damage `high`

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

### Units Igor benefits from

Look for units providing: `Healing` `Life Drain`  
Common buffers are **Solise**, **Smokey & Meerky**, or **Mikola**.

- **Koko**
  - Healing (all units, medium)
  - Lifedrain buff (multiple targets, low)
- **Contess**
  - Healing (multiple targets, high)
- **Hepler**
  - Healing (multiple targets, high)
- **Marcille**
  - Healing (multiple targets, high)
- **Ludovic**
  - Healing (area, medium)

### Units benefitting most from Igor

- Indris
- Aliceth
- Bonnie

### Units that can act as a replacement for Igor

**Damage**

- Alna (100% `Physical`)
- Athalia (100% `Physical`)
- Dionel (100% `Physical`)

**Debuffs on enemies**

- Nazrik (100% `Healing debuff`)

### Summary for Igor

#### Damage types dealt by Igor

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target

#### Debuffs provided by Igor

- Healing debuff (Mythic+) — Single target — `medium`

## Indris

### Indris's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Spellbane Shot (ultimate)
- **Movement**: stationary (no finite attack range)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, debuffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`
- **True damage**: Max HP-based damage `low`, True damage `high`

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

### Units Indris benefits from

Look for units providing: `ATK` `ATK SPD / Haste`  
Common buffers are **Lyca**, **Ravion**, or **Hugin**.

- **Pandora**
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
  - Enables Multiple debuffs on target via 5 debuff types
  - Enables Debuff on target via ATK debuff (all units)
- **Kulu**
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via Damage taken debuff (all units)
- **Alna**
  - ATK buff (single target, medium)
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via Haste debuff (area)
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via Energy drain (all units)
- **Frieren**
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via DoT (area)

### Units benefitting most from Indris

- Nerion

### Units that can act as a replacement for Indris

**Damage**

- Pippa (100% `True damage` `Max HP-based damage`)
- Sylphira (88% `True damage` `Max HP-based damage`)
- Nara (82% `True damage` `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Kruger (60% `Damage taken debuff` `Phys DEF debuff`)

**Crowd Control**

- Kordan (68% `Bind` `Knock back`)

### Summary for Indris

#### Indris Requires

- Debuff on target — Enemies
- Multiple debuffs on target — Enemies
- Passive with internal cooldown — Enemies

#### Damage types dealt by Indris

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Self, Single target
- Max HP-based damage — Single target — `low`
- True damage — Multiple targets — `high`

#### Debuffs provided by Indris

- Damage taken debuff — Multiple targets — `low`
- Magic DEF debuff — Single target — `low`
- Phys DEF debuff (EX+10) — Single target — `medium`

#### Crowd Control provided by Indris

- Bind — Area — `high`
- Knock back — Area — `high`
- Silence — Single target — `low`

## Isabella

### Isabella's behavior

`AFK Stages [C]`, `Dream Realm [S]`, `Dream Realm (Endless) [A+]`, `PVP [C]`

- **Signature skill**: Grimoire Pact (ultimate)
- **Movement**: stationary (no finite attack range)
- **Ally composition**: frontmost ally becomes companion (stat stacks and ult buffs)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `medium`

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

### Units Isabella benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `Healing` `Energy`  
Common buffers are **Hugin**, **Rowan**, or **Solise**.

- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, low) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Zanie**
  - Healing (single target, high)

### Units benefitting most from Isabella

- Indris
- Bonnie
- Perseus

### Units that can act as a replacement for Isabella

**Buffs on allies**

- Galahad (100% `Haste`)
- Hugin (100% `Haste`)
- Mehira (100% `Haste`)

**Damage**

- Aurora (100% `Magic`)
- Contess (100% `Magic`)
- Cryonaia (100% `Magic`)

**Debuffs on enemies**

- Athalia (100% `ATK debuff`)
- Cyran (100% `ATK debuff`)
- Ravion (100% `ATK debuff`)

### Summary for Isabella

#### Isabella Requires

- Once per battle — Allies

#### Damage types dealt by Isabella

- Primary damage type (unit): **Magic**
- Magic — Area, Single target

#### Buffs provided by Isabella

- Haste buff (Supreme+) — Multiple targets — `low`

#### Debuffs provided by Isabella

- ATK debuff — Single target — `high`

#### Crowd Control provided by Isabella

- Unaffected — Single target — Once

## Kafra

### Kafra's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Gale Thrust (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, debuffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

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

### Units Kafra benefits from

Look for units providing: `ATK` `Max HP`  
Common buffers are **Lyca**, **Rowan**, or **Hugin**.

- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Pandora**
  - Max HP buff (single target, medium)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Hepler**
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`

### Units benefitting most from Kafra

- Nerion
- Indris
- Carolina

### Units that can act as a replacement for Kafra

**Similar Skills**

- Sinbad (66% `enemy-debuffer` `mark-target`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Lyca (65% `ATK debuff` `Phys DEF debuff`)
- Ravion (65% `ATK debuff` `Phys DEF debuff`)

**Crowd Control**

- Atalanta (100% `Stun` `Knock back`)
- Cassadee (100% `Stun` `Knock back`)
- Lenya (100% `Stun` `Knock back`)

### Summary for Kafra

#### Kafra Provides

- Marked target (focus fire) — Single target

#### Damage types dealt by Kafra

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Debuffs provided by Kafra

- Marked target (focus fire) — Single target — `medium`
- Phys DEF debuff — Single target — `high`
- ATK debuff (Mythic+) — Single target — `high`
- Haste debuff (Mythic+) — Single target — `high`

#### Crowd Control provided by Kafra

- Unaffected (Mythic+) — Self — Conditional
- Knock back — Single target — `low`
- Stun — Single target — `high`

## Koko

### Koko's behavior

`AFK Stages [A]`, `Dream Realm [B]`, `Dream Realm (Endless) [B]`, `PVP [B]`

- **Signature skill**: Full Energy (ultimate)
- **Movement**: mostly stationary (avg attack range 4.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `high`

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

### Units Koko benefits from

Look for units providing: `Haste` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Pandora**
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Valka**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Koko

**12** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Perseus
- Talene
- Gunnar
- Harak
- Lucca
- Tilaya
- Ulmus
- Valka
- Igor
- Callan

### Units that can act as a replacement for Koko

**Similar Skills**

- Saida (66% `ally-shielder` `life-drain`)

**Damage**

- Alna (100% `Physical`)
- Athalia (100% `Physical`)
- Gunnar (100% `Physical`)

**Debuffs on enemies**

- Kruger (100% `Damage taken debuff`)
- Kulu (100% `Damage taken debuff`)

**Crowd Control**

- Faramor (100% `Stun`)
- Perseus (100% `Stun`)
- Valka (75% `Stun`)

### Summary for Koko

#### Damage types dealt by Koko

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target

#### Buffs provided by Koko

- Damage taken reduction — All units — `medium`
- Healing — All units — `medium`
- Lifedrain buff — Multiple targets — `low`
- Shield (Mythic+) — All units — `low`
- Vitality buff (Supreme+) — Single target — `low`

#### Debuffs provided by Koko

- Damage taken debuff — Area — `low`

#### Crowd Control provided by Koko

- Stun — Area — `medium`

## Kordan

### Kordan's behavior

`AFK Stages [C]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S]`, `PVP [A]`

- **Signature skill**: Dominance Ring (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `high`
- **True damage**: HP loss `medium`

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

### Units Kordan benefits from

Look for units providing: `ATK` `Max HP` `Healing` `DEF Penetration` `Life Drain`  
Common buffers are **Hugin**, **Ravion**, or **Twins**.

- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)
- **Aliceth**
  - ATK buff (multiple targets, low)
  - DEF Penetration buff (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
  - Healing (single target, high)
  - DEF Penetration buff (single target, medium)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Galahad**
  - Max HP via Shield (single target, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Kordan

- Nerion
- Carolina
- Perseus

### Units that can act as a replacement for Kordan

**Damage**

- Aliceth (100% `Physical` `HP loss`)
- Faramor (100% `Physical` `HP loss`)
- Ravion (93% `Physical` `HP loss`)

### Summary for Kordan

#### Damage types dealt by Kordan

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- HP loss — Single target — `medium`

#### Buffs provided by Kordan

- Lifedrain buff — Multiple targets — `medium`
- DEF Penetration buff (Supreme+) — Multiple targets — `low`

#### Crowd Control provided by Kordan

- Bind — Area — `high`
- Knock back — Area — `low`
- Knock down — Single target — `high`
- Knock up (Mythic+) — Single target — `medium`

## Korin

### Korin's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Demonseal Spear (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `medium`
- **True damage**: Max HP-based damage `medium`, True damage `medium`

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

### Units Korin benefits from

Look for units providing: `ATK SPD / Haste` `Max HP`  
Common buffers are **Lyca**, **Hugin**, or **Twins**.

- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
  - Haste buff (single target, low) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
  - Max HP via Shield (single target, medium)
- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
- **Pandora**
  - Max HP buff (single target, medium)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Korin

- Nerion
- Carolina
- Perseus

### Units that can act as a replacement for Korin

**Buffs on allies**

- Callan (100% `Max HP`)
- Daimon (100% `Max HP`)
- Galahad (100% `Max HP`)

**Similar Skills**

- Scarlita (66% `ally-shielder` `hp-scaling`)
- Lucca (60% `ally-shielder`)
- Silven (60% `hp-scaling`)

**Damage**

- Temesia (100% `Physical` `Max HP-based damage` `True damage`)
- Nara (92% `Max HP-based damage` `True damage` `Physical`)
- Indris (86% `Physical` `True damage` `Max HP-based damage`)

**Crowd Control**

- Indris (100% `Knock back` `Bind`)
- Kordan (100% `Knock back` `Bind`)
- Atalanta (85% `Knock back` `Bind`)

### Summary for Korin

#### Damage types dealt by Korin

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- Max HP-based damage — Area — `medium`
- True damage — Single target — `medium`

#### Buffs provided by Korin

- Shield — Single target — `medium`

#### Crowd Control provided by Korin

- Bind — Single target — `medium`
- Knock back — Area — `low`

## Kruger

### Kruger's behavior

`AFK Stages [C]`, `Dream Realm [S]`, `Dream Realm (Endless) [A]`, `PVP [C]`

- **Signature skill**: Devastating Axe (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, debuffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

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

### Units Kruger benefits from

Look for units providing: `Max HP` `Physical DEF`  
Common buffers are **Hugin**, **Rowan**, or **Twins**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Galahad**
  - Max HP via Shield (single target, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Daimon**
  - Max HP via Shield (multiple targets, medium)
- **Zandrok**
  - Max HP buff (multiple targets, low)
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Zanie**
  - Max HP via Shield (single target, high)

### Units benefitting most from Kruger

- Indris
- Aliceth
- Bonnie

### Units that can act as a replacement for Kruger

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Crowd Control**

- Athalia (100% `Knock down`)
- Baelran (100% `Knock down`)
- Frieren (100% `Knock down`)

### Summary for Kruger

#### Kruger Provides

- Stacking buff — Single target

#### Kruger Requires

- Vulnerable enemy (Mythic+) — Enemies

#### Damage types dealt by Kruger

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Debuffs provided by Kruger

- Damage taken debuff — Area — `low`
- Phys DEF debuff — Single target — `low`
- Vulnerable debuff — Area — `low`

#### Crowd Control provided by Kruger

- Knock down — Single target — `low`

## Kulu

### Kulu's behavior

`AFK Stages [S]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Demolition Zone (Skill 1)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill**: speed `slow`, first cast speed `fast`, buffs `medium`, damage `low`
- **Ultimate**: speed `normal`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

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

### Units Kulu benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `DEF Penetration`  
Common buffers are **Twins**, **Hugin**, or **Velara**.

- **Aliceth**
  - ATK buff (multiple targets, low)
  - DEF Penetration buff (multiple targets, high)
- **Galahad**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Zanie**
  - DEF Penetration buff (single target, medium)
- **Gunnar**
  - ATK SPD buff (single target, low) `signature fuel`

### Units benefitting most from Kulu

- Indris
- Bonnie

### Units that can act as a replacement for Kulu

**Buffs on allies**

- Aliceth (100% `DEF Penetration`)
- Kordan (100% `DEF Penetration`)
- Silven (100% `DEF Penetration`)

**Damage**

- Alna (100% `Physical`)
- Athalia (100% `Physical`)
- Gunnar (100% `Physical`)

**Crowd Control**

- Kordan (66% `Knock back` `Knock up`)

### Summary for Kulu

#### Kulu Provides

- Invincibility — Self
- Enhanced form (EX+15) — Single target

#### Damage types dealt by Kulu

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target

#### Buffs provided by Kulu

- DEF Penetration buff (EX+15) — Single target — `low`

#### Debuffs provided by Kulu

- Movement speed debuff — Area — `medium`
- Damage taken debuff (Mythic+) — All units — `high`

#### Crowd Control provided by Kulu

- Unaffected — Area — On ultimate
- Displace — Single target — `low`
- Knock back — Single target — `low`
- Knock up — Single target — `low`

## Laios

### Laios's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Dungeon Gourmet (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill**: speed `slow`, heal `medium`, buffs `medium`, damage `high`
- **Ultimate**: speed `fast`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `medium`, buffs `medium`, damage `high`

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

### Units Laios benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `Max HP` `Healing`  
Common buffers are **Lyca**, **Hugin**, or **Twins**.

- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
  - Max HP via Shield (summons only, medium)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
  - Haste buff (single target, low) `signature fuel`

### Units benefitting most from Laios

- Nerion
- Carolina

### Units that can act as a replacement for Laios

**Similar Skills**

- Damian (66% `ally-healer` `summoner`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Crowd Control**

- Faramor (100% `Stun`)
- Koko (100% `Stun`)
- Perseus (100% `Stun`)

### Summary for Laios

#### Laios Provides

- Summoning — Single target
- Stacking buff (EX+10) — Single target

#### Laios Requires

- Monster ingredients (Supreme+) — Enemies
- Stacked resource (Supreme+) — Enemies

#### Damage types dealt by Laios

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Laios

- ATK buff — Multiple targets — `low` — conditional (rare)
- DEF buff — Single target — `low` — conditional (rare)

#### Crowd Control provided by Laios

- Stun — Area — `medium`

## Lenya

### Lenya's behavior

`AFK Stages [C]`, `Dream Realm [A+]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Wild Duel (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `high`

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

### Units Lenya benefits from

Look for units providing: `Haste` `Max HP` `CRIT` `CRIT DMG Boost` `Energy`  
Common buffers are **Hugin**, **Twins**, or **Rowan**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - Max HP via Shield (single target, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Pandora**
  - Max HP buff (single target, medium)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, low)
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Mehira**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Lenya

- Nerion
- Perseus
- Silven

### Units that can act as a replacement for Lenya

**Buffs on allies**

- Daimon (100% `Max HP`)
- Hugin (100% `Max HP`)
- Koko (100% `Max HP`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Crowd Control**

- Perseus (100% `Knock back` `Stun`)

### Summary for Lenya

#### Damage types dealt by Lenya

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target

#### Buffs provided by Lenya

- Shield (Supreme+) — Single target — `high`

#### Crowd Control provided by Lenya

- Unaffected — Self — Once
- Knock back — Area — `low`
- Stun — Single target — `medium`

## Lily May

### Lily May's behavior

`AFK Stages [A]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Tempest Shot (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, debuffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `low`
- **True damage**: Max HP-based damage `low`

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

### Units Lily May benefits from

Look for units providing: `ATK` `DEF Penetration`  
Common buffers are **Rowan**, **Ravion**, or **Twins**.

- **Aliceth**
  - ATK buff (multiple targets, low)
  - DEF Penetration buff (multiple targets, high)
- **Pandora**
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
- **Thador**
  - Energy recovery (lieutenant, start of battle) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Lily May

- Bonnie

### Units that can act as a replacement for Lily May

**Buffs on allies**

- Aliceth (100% `DEF Penetration`)
- Kordan (100% `DEF Penetration`)
- Kulu (100% `DEF Penetration`)

**Similar Skills**

- Athalia (60% `hp-scaling` `self-repositioner` `transformation`)

**Damage**

- Shadewing (100% `Magic` `Max HP-based damage`)
- Shemira (100% `Magic` `Max HP-based damage`)
- Daimon (94% `Magic` `Max HP-based damage`)

**Crowd Control**

- Sylphira (80% `Interrupt`)
- Reinier (60% `Interrupt`)

### Summary for Lily May

#### Lily May Provides

- Invincibility — Single target

#### Damage types dealt by Lily May

- Primary damage type (unit): **Magic**
- Magic — All units, Single target
- Max HP-based damage — Self, Single target — `low`

#### Buffs provided by Lily May

- DEF Penetration buff (Legendary+) — Single target — `low`

#### Debuffs provided by Lily May

- Energy drain — All units — `high`

#### Crowd Control provided by Lily May

- Unaffected — Self — Start of battle
- Interrupt — All units — `low`

## Lorsan

### Lorsan's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Whispering Tempest (ultimate)
- **Movement**: stationary (no finite attack range)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `medium`, damage `medium`

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

### Units Lorsan benefits from

Look for units providing: `ATK` `Haste` `Healing`  
Common buffers are **Hugin**, **Mikola**, or **Twins**.

- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (single target, high)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Lorsan

- Berial
- Granny Dahnie
- Lucius

### Units that can act as a replacement for Lorsan

**Buffs on allies**

- Solise (100% `Healing`)
- Smokey & Meerky (80% `Healing`)
- Koko (66% `Healing`)

**Similar Skills**

- Faramor (80% `aoe-damage` `dot-specialist`)

**Damage**

- Callan (100% `Magic`)
- Cassadee (100% `Magic`)
- Contess (100% `Magic`)

**Crowd Control**

- Faramor (100% `Stun`)
- Perseus (100% `Stun`)
- Tasi (100% `Stun`)

### Summary for Lorsan

#### Damage types dealt by Lorsan

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Buffs provided by Lorsan

- Healing (Mythic+) — All units — `high`

#### Crowd Control provided by Lorsan

- Unaffected (Supreme+) — Self — On skill
- Stun (Mythic+) — Multiple targets — `high`

## Lucca

### Lucca's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Quake Slam (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Ally composition**: place adjacent allies behind at battle prep (DEF buff)
- **Ally composition**: place allies on adjacent tiles behind at battle start (shields and ATK boost)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, damage `low`

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

### Units Lucca benefits from

Look for units providing: `Max HP` `Healing` `Physical DEF` `Magic DEF`  
Common buffers are **Rowan**, **Hugin**, or **Solise**.

- **Hepler**
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Hewynn**
  - Healing (all units, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)
- **Fay**
  - Healing (arc, medium, conditional (frequent))
  - DEF buff (multiple targets, low)
  - DEF buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`

### Units benefitting most from Lucca

- Nerion
- Carolina
- Himmel

### Units that can act as a replacement for Lucca

**Similar Skills**

- Hugin (60% `ally-shielder`)
- Korin (60% `ally-shielder`)
- Lucius (60% `ally-shielder`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Antandra (66% `Stun` `Knock down`)
- Zorya (66% `Stun` `Knock down`)

### Summary for Lucca

#### Damage types dealt by Lucca

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Crowd Control provided by Lucca

- Immune — Self — On skill
- Interrupt — Single target — `medium`
- Knock down — Area — `low`
- Knock up — Area — `low`
- Stun — Area — `medium`

## Lucius

### Lucius's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Divine Light Aegis (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `medium`

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

### Units Lucius benefits from

Look for units providing: `Healing`  
Common buffers are **Rowan**, **Lyca**, or **Smokey & Meerky**.

- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Damian**
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Hepler**
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Lucius

- Nerion
- Perseus
- Shadewing

### Units that can act as a replacement for Lucius

**Buffs on allies**

- Hepler (100% `Max HP`)
- Hugin (100% `Max HP`)
- Saida (100% `Max HP`)

**Similar Skills**

- Hepler (66% `ally-healer` `ally-shielder`)
- Solise (66% `ally-healer` `ally-shielder`)
- Twins (66% `ally-healer` `ally-shielder`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Athalia (100% `ATK debuff`)
- Lyca (100% `ATK debuff`)
- Sinbad (90% `ATK debuff`)

**Crowd Control**

- Atalanta (100% `Knock back` `Stun`)
- Cassadee (100% `Knock back` `Stun`)
- Lenya (100% `Knock back` `Stun`)

### Summary for Lucius

#### Damage types dealt by Lucius

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Lucius

- Shield — Area — `medium`

#### Debuffs provided by Lucius

- ATK debuff (Mythic+) — Area — `medium`

#### Crowd Control provided by Lucius

- Knock back — Single target — `high`
- Stun — Single target — `low`

## Lucy

### Lucy's behavior

- **Signature skill**: Star Dress: Aquarius Form (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill**: speed `fast`, damage `high`
- **Ultimate**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `high`

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

### Units Lucy benefits from

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Lyca**, **Twins**, or **Hugin**.

- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
  - Haste buff (single target, low) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, low) `signature fuel`
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Lucy

- Nerion
- Carolina
- Perseus

### Units that can act as a replacement for Lucy

**Buffs on allies**

- Daimon (100% `Max HP`)
- Hepler (100% `Max HP`)
- Hugin (100% `Max HP`)

**Damage**

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Cassadee (100% `Magic`)

### Summary for Lucy

#### Damage types dealt by Lucy

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Lucy

- Shield (Mythic+) — Single target — `high`

#### Crowd Control provided by Lucy

- Unaffected — Self — On skill
- Knock up — All units — `medium`
- Stun — Single target — `high`

## Ludovic

### Ludovic's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [A]`, `PVP [A]`

- **Signature skill**: Eternal Serenity (ultimate)
- **Movement**: stationary (no finite attack range)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, damage `high`

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

### Units Ludovic benefits from

Look for units providing: `Healing`  
Common buffers are **Rowan**, **Smokey & Meerky**, or **Solise**.

- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Koko**
  - Healing (all units, medium)
- **Contess**
  - Healing (multiple targets, high)
- **Marcille**
  - Healing (multiple targets, high)
- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`

### Units benefitting most from Ludovic

- Himmel
- Perseus
- Silven

### Units that can act as a replacement for Ludovic

**Buffs on allies**

- Contess (100% `Healing`)
- Koko (100% `Healing`)
- Marcille (100% `Healing`)

**Similar Skills**

- Smokey & Meerky (100% `ally-healer` `aoe-healing`)
- Solise (66% `ally-healer` `aoe-healing`)

**Damage**

- Callan (100% `Magic`)
- Contess (100% `Magic`)
- Cryonaia (100% `Magic`)

**Crowd Control**

- Callan (100% `Stun`)
- Contess (100% `Stun`)
- Faramor (100% `Stun`)

### Summary for Ludovic

#### Damage types dealt by Ludovic

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target

#### Buffs provided by Ludovic

- Healing — Area — `medium`

#### Crowd Control provided by Ludovic

- Unaffected — Self — On skill
- Stun (Supreme+) — Single target — `medium`

## Lumont

### Lumont's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Lumont's Charge (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

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

### Units Lumont benefits from

Look for units providing: `Haste` `Max HP` `Healing`  
Common buffers are **Hugin**, **Twins**, or **Rowan**.

- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Pandora**
  - Max HP buff (single target, medium)
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Hewynn**
  - Healing (all units, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)

### Units benefitting most from Lumont

- Nerion
- Carolina
- Indris

### Units that can act as a replacement for Lumont

**Buffs on allies**

- Fay (100% `Magic DEF` `Physical DEF`)
- Rowan (100% `Magic DEF` `Physical DEF`)

**Similar Skills**

- Kruger (60% `enemy-debuffer`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Athalia (100% `ATK debuff`)
- Bonnie (100% `ATK debuff`)
- Cyran (100% `ATK debuff`)

**Crowd Control**

- Antandra (100% `Stun` `Taunt`)
- Lucca (75% `Stun` `Knock up`)
- Perseus (66% `Stun`)

### Summary for Lumont

#### Damage types dealt by Lumont

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Lumont

- DEF buff — Multiple targets — `low`

#### Debuffs provided by Lumont

- ATK debuff (Mythic+) — Single target — `high`

#### Crowd Control provided by Lumont

- Unaffected — Self — On skill
- Stun — Area — `high`
- Taunt — Single target — `medium`
- Knock up (Mythic+) — Single target — `low`

## Lyca

### Lyca's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Comet Archery (ultimate)
- **Movement**: stationary (avg attack range 11.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, debuffs `medium`, damage `medium`

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

### Units Lyca benefits from

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Pandora**
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Lyca

**47** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight
- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Indris
- Nerion
- Cecia
- Fay
- Gwyneth
- Korin
- Marilee
- Mirael
- Parisa
- Rhys

### Units that can act as a replacement for Lyca

**Damage**

- Alna (100% `Physical`)
- Athalia (100% `Physical`)
- Dionel (100% `Physical`)

**Crowd Control**

- Callan (100% `Stun`)
- Cassadee (100% `Stun`)
- Contess (100% `Stun`)

### Summary for Lyca

#### Damage types dealt by Lyca

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target

#### Buffs provided by Lyca

- ATK SPD buff — All units — `high`
- Energy recovery — All units — `low`

#### Debuffs provided by Lyca

- ATK debuff — All units — `high`
- Phys DEF debuff — All units — `high`

#### Crowd Control provided by Lyca

- Stun (EX+10) — Single target — `medium`

## Marcille

### Marcille's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Silver-White Wings that Streak Across the Skies (ultimate)
- **Movement**: stationary (no finite attack range)
- **Ally composition**: place ally 1 tile in front at battle prep (revive target)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `medium`, damage `high`

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

### Units Marcille benefits from

Look for units providing: `ATK SPD / Haste` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
  - Haste buff (single target, low) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, low) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Marcille

- Perseus
- Himmel
- Silven

### Units that can act as a replacement for Marcille

**Buffs on allies**

- Contess (100% `Healing`)
- Koko (100% `Healing`)
- Smokey & Meerky (100% `Healing`)

**Damage**

- Callan (100% `Magic`)
- Contess (100% `Magic`)
- Cryonaia (100% `Magic`)

**Crowd Control**

- Lily May (60% `Interrupt`)
- Reinier (60% `Interrupt`)
- Smokey & Meerky (60% `Interrupt`)

### Summary for Marcille

#### Marcille Provides

- Revive ally (Mythic+) — Single target
- Stacking buff (Supreme+) — Single target

#### Marcille Requires

- Once per battle (Mythic+) — Allies

#### Damage types dealt by Marcille

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Multiple targets, Single target

#### Buffs provided by Marcille

- Healing — Multiple targets — `high`

#### Crowd Control provided by Marcille

- Unaffected (Supreme+) — Self — On skill
- Blind — Single target — `medium`
- Interrupt (Mythic+) — Single target — `high`

## Marilee

### Marilee's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Mid-Air Shot (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `low`
- **True damage**: True damage `low`

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

### Units Marilee benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `CRIT` `CRIT DMG Boost`  
Common buffers are **Lyca**, **Twins**, or **Hugin**.

- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Marilee

- Nerion
- Carolina

### Units that can act as a replacement for Marilee

**Similar Skills**

- Kordan (66% `hp-scaling` `self-repositioner`)
- Pippa (66% `hp-scaling` `self-repositioner`)
- Tasi (66% `mass-cc` `self-repositioner`)

**Damage**

- Athalia (100% `Physical` `True damage`)
- Baelran (100% `Physical` `True damage`)
- Dionel (100% `Physical` `True damage`)

**Crowd Control**

- Aliceth (100% `Stun`)
- Alsa (100% `Stun`)
- Antandra (100% `Stun`)

### Summary for Marilee

#### Marilee Provides

- Stacking buff (Mythic+) — Multiple targets

#### Damage types dealt by Marilee

- Primary damage type (unit): **Physical**
- Physical — Multiple targets, Single target
- True damage — Multiple targets — `low`

#### Crowd Control provided by Marilee

- Stun — Single target — `low`

## Mehira

### Mehira's behavior

`AFK Stages [S+]`, `Dream Realm [A]`, `Dream Realm (Endless) [A+]`, `PVP [A+]`

- **Signature skill**: Euphoric Rush (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `medium`, buffs `medium`, damage `low`

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

### Units Mehira benefits from

Look for units providing: `Haste` `Max HP` `Healing`  
Common buffers are **Hugin**, **Twins**, or **Solise**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, medium)
- **Contess**
  - Healing (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Gunnar**
  - ATK SPD buff (single target, low) `signature fuel`
- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`

### Units benefitting most from Mehira

**14** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Aurora
- Cassadee
- Frieren
- Ravion
- Cyran
- Faramor
- Hugin
- Pippa
- Rowan
- Shakir

### Units that can act as a replacement for Mehira

**Buffs on allies**

- Hugin (100% `Haste`)
- Twins (100% `Haste`)
- Velara (100% `Haste`)

**Damage**

- Contess (100% `Magic`)
- Saida (100% `Magic`)
- Shadewing (100% `Magic`)

### Summary for Mehira

#### Mehira Provides

- HP threshold strike (Mythic+) — Self
- Summoning (Mythic+) — Self

#### Damage types dealt by Mehira

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target

#### Buffs provided by Mehira

- Haste buff — Single target — `high`

#### Debuffs provided by Mehira

- Damage taken debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Mehira

- Untargetable (Mythic+) — Self — Start of battle
- Charm — Area — `medium`

## Mikola

### Mikola's behavior

`AFK Stages [C]`, `Dream Realm [A]`, `Dream Realm (Endless) [A]`, `PVP [B]`

- **Signature skill**: Dauntless Hymn (ultimate)
- **Movement**: moving (avg attack range 2.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, buffs `medium`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `medium`, buffs `medium`, damage `low`

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

### Units Mikola benefits from

Look for units providing: `ATK` `Haste`  
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Valka**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Mikola

**26** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Perseus
- Hepler
- Lorsan
- Seth
- Tasi
- Vala
- Laios
- Temesia
- Hammie
- Hodgkin

### Units that can act as a replacement for Mikola

**Damage**

- Alna (100% `Physical`)
- Athalia (100% `Physical`)
- Gunnar (100% `Physical`)

### Summary for Mikola

#### Damage types dealt by Mikola

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Multiple targets, Single target

#### Buffs provided by Mikola

- ATK buff — Multiple targets — `high`
- Haste buff — Multiple targets — `low`
- Healing — Multiple targets — `medium`
- Healing over time — All units — `medium`
- Vitality buff (EX+10) — Multiple targets — `low`

#### Crowd Control provided by Mikola

- Unaffected (Supreme+) — Self — Conditional

## Mirael

### Mirael's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Winged Flame (ultimate)
- **Movement**: stationary (avg attack range 10.1 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, debuffs `medium`, damage `high`

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

### Units Mirael benefits from

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Lyca**, **Twins**, or **Hugin**.

- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Mirael

- Shadewing
- Bonnie
- Himmel

### Units that can act as a replacement for Mirael

**Similar Skills**

- Gwyneth (80% `dot-specialist` `fire-attack`)
- Satrana (66% `dot-specialist` `fire-attack`)

**Damage**

- Bryon (100% `Magic` `DoT`)
- Frieren (100% `Magic` `DoT`)
- Shadewing (100% `Magic` `DoT`)

**Debuffs on enemies**

- Brutus (100% `DoT`)
- Evie (100% `DoT`)
- Frieren (100% `DoT`)

### Summary for Mirael

#### Damage types dealt by Mirael

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Single target

#### Debuffs provided by Mirael

- DoT — Single target — `low`

## Nara

### Nara's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Phantom Chains (Skill 1)
- **Movement**: mostly stationary (pulls enemies)

#### Skill overview

- **Signature skill**: speed `fast`
- **Ultimate**: speed `fast`, first cast speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, damage `low`
- **True damage**: Max HP-based damage `medium`, True damage `high`

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

### Units Nara benefits from

Look for units providing: `ATK` `Energy`  
Common buffers are **Ravion**, **Smokey & Meerky**, or **Rowan**.

- **Pandora**
  - Energy recovery (single target, low) `signature fuel`
- **Thador**
  - Energy recovery (single target, low) `signature fuel`

### Units benefitting most from Nara

- Nerion
- Carolina
- Perseus

### Units that can act as a replacement for Nara

**Buffs on allies**

- Contess (100% `Healing`)
- Evie (100% `Healing`)
- Hepler (100% `Healing`)

**Damage**

- Shadewing (100% `Max HP-based damage` `True damage`)
- Indris (84% `True damage` `Physical` `Max HP-based damage`)
- Nazrik (84% `True damage` `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Alna (100% `Vitality debuff`)
- Dionel (100% `Vitality debuff`)
- Faramor (100% `Vitality debuff`)

**Crowd Control**

- Baelran (100% `Knock down` `Knock up`)
- Kordan (100% `Knock down` `Knock up`)
- Scarlita (80% `Knock down` `Knock up`)

### Summary for Nara

#### Damage types dealt by Nara

- Primary damage type (unit): **Physical**
- Physical — Single target
- Max HP-based damage — Area — `medium`
- True damage — Single target — `high`

#### Buffs provided by Nara

- Healing (Mythic+) — Area — `low`

#### Debuffs provided by Nara

- Vitality debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Nara

- Unaffected (Supreme+) — Self — Permanent
- Knock down — Single target — `high`
- Knock up — Single target — `medium`

## Natsu

### Natsu's behavior

- **Signature skill**: Lightning Fire Dragon's Roar/Fire Dragon King's Roar (ultimate)
- **Movement**: stationary (avg attack range 11.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, first cast speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`
- **True damage**: Max HP-based damage `low`

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

### Units Natsu benefits from

Look for units providing: `ATK` `Haste` `CRIT` `CRIT DMG Boost`  
Common buffers are **Hugin**, **Twins**, or **Mikola**.

- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Valka**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD buff (multiple targets, high) `signature fuel`

### Units benefitting most from Natsu

- Indris
- Shadewing
- Bonnie

### Units that can act as a replacement for Natsu

**Damage**

- Daimon (100% `Magic` `Max HP-based damage`)
- Satrana (100% `Magic` `Max HP-based damage`)
- Shadewing (100% `Magic` `Max HP-based damage`)

**Crowd Control**

- Antandra (100% `Stun` `Knock down`)
- Lucca (100% `Stun` `Knock down`)
- Valka (100% `Stun` `Knock down`)

### Summary for Natsu

#### Damage types dealt by Natsu

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- Max HP-based damage — Area — `low`

#### Debuffs provided by Natsu

- Haste debuff — Area — `medium`
- Max HP debuff (Mythic+) — Single target — `medium`
- DoT (Supreme+) — Single target — `medium`

#### Crowd Control provided by Natsu

- Knock down — Area — `low`
- Stun — Single target — `medium`

## Nazrik

### Nazrik's behavior

`AFK Stages [B]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [B]`

- **Signature skill**: Rend Rupture (ultimate)
- **Movement**: stationary (avg attack range 10.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, damage `high`
- **Non-ultimate**: speed `fast`, debuffs `medium`, damage `medium`
- **True damage**: Max HP-based damage `low`, True damage `high`

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

### Units Nazrik benefits from

Look for units providing: `CRIT`  
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Nazrik

- Indris
- Nerion
- Carolina

### Units that can act as a replacement for Nazrik

**Damage**

- Sylphira (91% `True damage` `Max HP-based damage`)
- Shadewing (78% `Max HP-based damage` `True damage`)
- Silven (71% `True damage`)

**Crowd Control**

- Callan (100% `Stun`)
- Contess (100% `Stun`)
- Faramor (100% `Stun`)

### Summary for Nazrik

#### Nazrik Provides

- Stacking buff — Single target

#### Damage types dealt by Nazrik

- Primary damage type (unit): **Physical**
- Physical — Single target
- Max HP-based damage — Single target — `low`
- True damage — Single target — `high`

#### Debuffs provided by Nazrik

- Healing debuff — Single target — `medium`
- Max HP debuff — Single target — `medium`
- Crit Resist debuff (Mythic+) — Single target — `low`
- Damage taken debuff (EX+10) — Single target — `low`
- Vitality debuff (EX+10) — Single target — `medium`

#### Crowd Control provided by Nazrik

- Stun — Single target — `medium`

## Nerion

### Nerion's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Drowning Doom (ultimate)
- **Movement**: mostly stationary (avg attack range 4.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

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

### Units Nerion benefits from

Look for units providing: `ATK SPD / Haste` `Max HP` `Energy` `DEF Penetration`  
Common buffers are **Lyca**, **Ravion**, or **Twins**.

- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
  - Enables CC on enemies via Blind (area, high)
- **Baelran**
  - Enables CC on enemies via Knock up (area, high)
- **Indris**
  - Enables CC on enemies via Knock back (area, high)
- **Kordan**
  - Enables CC on enemies via Bind (area, high)
- **Aliceth**
  - DEF Penetration buff (multiple targets, high)
  - Enables CC on enemies via Blind (area, medium)

### Units benefitting most from Nerion

- Bonnie
- Carolina
- Indris

### Units that can act as a replacement for Nerion

**Similar Skills**

- Shadewing (100% `dot-specialist` `enemy-debuffer`)

**Damage**

- Aurora (100% `Magic`)
- Bonnie (100% `Magic`)
- Bryon (100% `Magic`)

**Debuffs on enemies**

- Athalia (100% `ATK debuff`)
- Bonnie (100% `ATK debuff`)
- Contess (100% `ATK debuff`)

**Crowd Control**

- Callan (100% `Stun`)
- Cassadee (100% `Stun`)
- Contess (100% `Stun`)

### Summary for Nerion

#### Nerion Provides

- Enhanced form (Supreme+) — Single target

#### Nerion Requires

- CC on enemies (EX+15) — Enemies

#### Damage types dealt by Nerion

- Primary damage type (unit): **Magic**
- Magic — Area, Self, Single target

#### Debuffs provided by Nerion

- ATK debuff (Mythic+) — Single target — `low`

#### Crowd Control provided by Nerion

- Stun — Single target — `medium`

## Niru

### Niru's behavior

`AFK Stages [A+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Soul Shepherd (ultimate)
- **Movement**: stationary (no finite attack range)
- **Ally composition**: nearest ally auto-selected at battle start; prioritizes ally behind

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, heal `medium`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `medium`, damage `medium`
- **True damage**: HP loss `low`

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

### Units Niru benefits from

Look for units providing: `Healing` `Physical DEF` `Magic DEF`  
Common buffers are **Rowan**, **Solise**, or **Velara**.

- **Contess**
  - Healing (multiple targets, high)
- **Mehira**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
  - Enables Enemy defeat via HP threshold strike
- **Aliceth**
  - Enables Enemy defeat via Instant defeat
- **Cryonaia**
  - Enables Enemy defeat via Instant defeat
- **Thador**
  - Energy recovery (lieutenant, start of battle) `signature fuel`

### Units benefitting most from Niru

- Bonnie
- Zorya
- Himmel

### Units that can act as a replacement for Niru

**Damage**

- Dunlingr (100% `Magic` `HP loss`)
- Shadewing (100% `Magic` `HP loss`)
- Aliceth (71% `HP loss`)

### Summary for Niru

#### Niru Provides

- Spirit form protection — Single target
- Start-of-battle cast (Mythic+) — Self

#### Niru Requires

- Ally blessing active — Allies
- Enemy defeat — Allies

#### Damage types dealt by Niru

- Primary damage type (unit): **Magic**
- Magic — All units, Self, Single target
- HP loss — Single target — `low`

## Odie

### Odie's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Heart Crusher (Mythic+)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)

#### Skill overview

- **Signature skill**: speed `fast`, debuffs `medium`
- **Ultimate**: speed `slow`, debuffs `medium`, damage `low`
- **Non-ultimate**: speed `fast`, debuffs `medium`, damage `low`

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

### Units Odie benefits from

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Lyca**, **Twins**, or **Hugin**.

- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Odie

- Shadewing
- Bonnie
- Indris

### Units that can act as a replacement for Odie

**Damage**

- Bryon (100% `DoT` `Magic`)
- Frieren (100% `DoT` `Magic`)
- Shadewing (100% `DoT` `Magic`)

**Debuffs on enemies**

- Brutus (100% `DoT`)
- Evie (100% `DoT`)
- Frieren (100% `DoT`)

### Summary for Odie

#### Damage types dealt by Odie

- Primary damage type (unit): **Magic**
- Magic — Single target
- DoT — Single target

#### Debuffs provided by Odie

- DoT — Single target — `medium`

## Pandora

### Pandora's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [A]`, `PVP [A+]`

- **Signature skill**: Boxed Blessing (Skill 1)
- **Movement**: stationary (no finite attack range)
- **Ally composition**: rearmost ally enters invincible box, then gains Energy and ATK

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `medium`
- **Ultimate**: speed `slow`, debuffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `medium`

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

### Units Pandora benefits from

Look for units providing: `Energy`  
Common buffers are **Rowan**, **Ravion**, or **Smokey & Meerky**.

- **Thador**
  - Energy recovery (single target, low) `signature fuel`

### Units benefitting most from Pandora

- Indris
- Salazer
- Ludovic
- Walker
- Chippy
- Lily May
- Satrana
- Reinier
- Nara
- Scarlita

### Units that can act as a replacement for Pandora

**Buffs on allies**

- Rowan (66% `Healing` `Max HP` `Energy`)

**Damage**

- Contess (100% `Magic`)
- Cryonaia (100% `Magic`)
- Cyran (100% `Magic`)

### Summary for Pandora

#### Pandora Provides

- Invincibility — Single target

#### Damage types dealt by Pandora

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Pandora

- Energy recovery — Single target — `low`
- Healing — Single target — `high`
- Invincible — Single target — `high`
- Max HP buff (Legendary+) — Single target — `medium`

#### Debuffs provided by Pandora

- ATK debuff — All units — `low`
- Damage taken debuff — Single target — `low`
- Energy drain — Single target — `low`
- Haste debuff — Single target — `medium`
- Vitality debuff — Single target — `high`

## Pang

### Pang's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Sky Splitter (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `medium`

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

### Units Pang benefits from

Look for units providing: `ATK` `Haste` `DEF Penetration`  
Common buffers are **Twins**, **Hugin**, or **Lyca**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Aliceth**
  - ATK buff (multiple targets, low)
  - DEF Penetration buff (multiple targets, high)
- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Pang

- Nerion
- Carolina
- Perseus

### Units that can act as a replacement for Pang

**Buffs on allies**

- Zanie (100% `DEF Penetration` `Max HP`)
- Lenya (60% `Max HP`)
- Lily May (60% `DEF Penetration`)

**Similar Skills**

- Ulmus (100% `ally-shielder` `transformation`)
- Hepler (66% `ally-shielder` `transformation`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Crowd Control**

- Faramor (100% `Stun`)
- Koko (100% `Stun`)
- Laios (100% `Stun`)

### Summary for Pang

#### Pang Provides

- Transformation — Self

#### Damage types dealt by Pang

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Pang

- Shield (EX+10) — Single target — `low`
- DEF Penetration buff (Supreme+) — Single target — `low`

#### Crowd Control provided by Pang

- Unaffected — Self — On skill
- Stun — Area — `low`

## Parisa

### Parisa's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Floral Splendor (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, damage `low`

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

### Units Parisa benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `Energy`  
Common buffers are **Lyca**, **Hugin**, or **Rowan**.

- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Parisa

- Bonnie
- Himmel
- Niru

### Units that can act as a replacement for Parisa

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

### Summary for Parisa

#### Parisa Provides

- Marked target (focus fire) — Area

#### Damage types dealt by Parisa

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Self, Single target

## Perseus

### Perseus's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S+]`

- **Signature skill**: Divine Rend (ultimate)
- **Movement**: moving (avg attack range 2.9 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `high`
- **True damage**: True damage `low`

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

### Units Perseus benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `Max HP`  
Common buffers are **Hugin**, **Rowan**, or **Mikola**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Enables Ally stat buffs via 5 ally stat buffs
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
  - Enables Ally stat buffs via 3 ally stat buffs
- **Pandora**
  - Max HP buff (single target, medium)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
  - Enables Ally stat buffs via 4 ally stat buffs (start of battle)
- **Evie**
  - ATK buff (multiple targets, high)
  - Enables Ally stat buffs via 2 ally stat buffs (start of battle)
- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
  - Enables Ally stat buffs via 3 ally stat buffs

### Units benefitting most from Perseus

- Nerion
- Carolina
- Silven

### Units that can act as a replacement for Perseus

**Buffs on allies**

- Evie (100% `ATK`)
- Hugin (100% `ATK`)
- Mikola (100% `ATK`)

**Damage**

- Athalia (100% `Physical` `True damage`)
- Baelran (100% `Physical` `True damage`)
- Faramor (100% `Physical` `True damage`)

### Summary for Perseus

#### Perseus Requires

- Ally stat buffs (EX+10) — —

#### Damage types dealt by Perseus

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- True damage — Multiple targets — `low`

#### Buffs provided by Perseus

- ATK buff — Multiple targets — `medium`

#### Crowd Control provided by Perseus

- Unaffected — Multiple targets — On skill
- Knock back — Area — `low`
- Stun — Area — `medium`

## Phraesto

### Phraesto's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [B]`, `PVP [B]`

- **Signature skill**: Crimson Contract (Skill 1)
- **Movement**: moving (avg attack range 1.8 tiles)
- **Ally composition**: place allies 1 tile behind this hero and the Illusion for contract buffs
- **Self placement**: keep this hero and Illusion in the same row (damage reduction and battle-start shields)

#### Skill overview

- **Signature skill**: speed `slow`, first cast speed `fast`, buffs `medium`, damage `low`
- **Ultimate**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `medium`, buffs `medium`, damage `high`

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

### Units Phraesto benefits from

Look for units providing: `Healing` `Energy`  
Common buffers are **Smokey & Meerky**, **Rowan**, or **Solise**.

- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, medium)
- **Koko**
  - Healing (all units, medium)
- **Contess**
  - Healing (multiple targets, high)
- **Hepler**
  - Healing (multiple targets, high)

### Units benefitting most from Phraesto

- Perseus
- Nerion
- Silven

### Units that can act as a replacement for Phraesto

**Buffs on allies**

- Koko (75% `Max HP` `Damage taken reduction`)
- Zanie (75% `Max HP`)
- Saida (60% `Max HP`)

**Damage**

- Aurora (100% `Magic`)
- Bonnie (100% `Magic`)
- Bryon (100% `Magic`)

**Crowd Control**

- Hepler (100% `Stun` `Taunt`)
- Contess (60% `Stun`)
- Gunnar (60% `Stun`)

### Summary for Phraesto

#### Phraesto Provides

- Summoning — Area

#### Damage types dealt by Phraesto

- Primary damage type (unit): **Magic**
- Magic — Area, Single target

#### Buffs provided by Phraesto

- Damage taken reduction — Single target — `low`
- Max HP buff — Single target — `low`
- Shield — Single target — `medium`

#### Crowd Control provided by Phraesto

- Stun (Mythic+) — Single target — `low`
- Taunt (Mythic+) — Single target — `low`

## Pippa

### Pippa's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Wild Shift (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, damage `medium`
- **Non-ultimate**: speed `fast`, debuffs `medium`, damage `medium`
- **True damage**: True damage `medium`

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

### Units Pippa benefits from

Look for units providing: `Haste`  
Common buffers are **Twins**, **Hugin**, or **Lyca**.

- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Valka**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Isabella**
  - Haste buff (multiple targets, low) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`

### Units benefitting most from Pippa

- Bonnie
- Indris
- Aliceth

### Units that can act as a replacement for Pippa

**Similar Skills**

- Kordan (100% `hp-scaling` `self-repositioner`)
- Athalia (66% `hp-scaling` `self-repositioner`)

**Damage**

- Indris (100% `True damage` `Max HP-based damage`)
- Sylphira (100% `True damage` `Magic` `Max HP-based damage`)
- Shadewing (84% `Magic` `Max HP-based damage` `True damage`)

**Debuffs on enemies**

- Lily May (100% `Energy drain`)
- Dunlingr (62% `Energy drain`)

**Crowd Control**

- Eironn (84% `Bind` `Displace`)
- Ravion (72% `Displace` `Knock down`)
- Evie (70% `Bind` `Displace`)

### Summary for Pippa

#### Damage types dealt by Pippa

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target
- Max HP-based damage — Single target — `low`
- True damage — Area — `medium`

#### Debuffs provided by Pippa

- Energy drain — Area — `medium`

#### Crowd Control provided by Pippa

- Unaffected — Self — On skill
- Bind — Single target — `medium`
- Displace — Single target — `low`
- Knock down — Single target — `low`

## Ravion

### Ravion's behavior

`AFK Stages [A]`, `Dream Realm [S]`, `Dream Realm (Endless) [A]`, `PVP [A+]`

- **Signature skill**: Killer Flush (ultimate)
- **Movement**: high movement (repositioning skills)
- **Ally composition**: Objectives go to the 2 rearmost allies; backline heroes receive ATK and Energy on completion

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, debuffs `medium`, damage `medium`
- **True damage**: HP loss `low`

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

### Units Ravion benefits from

Look for units providing: `ATK` `Haste` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Velara**.

- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, low) `signature fuel`
- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`

### Units benefitting most from Ravion

**27** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Nerion
- Indris
- Carolina
- Aliceth
- Arden
- Hodgkin
- Parisa
- Cryonaia
- Cyran
- Frieren

### Units that can act as a replacement for Ravion

**Similar Skills**

- Hugin (66% `ally-shielder` `energy-provider`)

**Damage**

- Aliceth (100% `Physical` `HP loss`)
- Faramor (100% `Physical` `HP loss`)
- Kordan (100% `Physical` `HP loss`)

### Summary for Ravion

#### Ravion Requires

- Boss encounter — Allies

#### Damage types dealt by Ravion

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- HP loss — Single target — `low`

#### Buffs provided by Ravion

- ATK buff — Multiple targets — `medium`
- Energy recovery — Multiple targets — `medium`
- Lifedrain buff (EX+10) — Single target — `low` — conditional (rare)
- Shield (EX+10) — Single target — `low` — conditional (rare)

#### Debuffs provided by Ravion

- ATK debuff — Multiple targets — `medium`
- Phys DEF debuff — Multiple targets — `medium`

#### Crowd Control provided by Ravion

- Unaffected — Self — Start of battle
- Displace — Multiple targets — `high`
- Knock down — Multiple targets — `high`

## Reinier

### Reinier's behavior

`AFK Stages [B]`, `Dream Realm [A]`, `Dream Realm (Endless) [A]`, `PVP [B]`

- **Signature skill**: Dynamic Balance (Skill 1)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, heal `medium`, damage `high`
- **Ultimate**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `medium`, debuffs `medium`, damage `high`

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

### Units Reinier benefits from

Look for units providing: `Healing`  
Common buffers are **Solise**, **Rowan**, or **Velara**.

- **Contess**
  - Healing (multiple targets, high)
- **Pandora**
  - Healing (single target, high)
- **Zanie**
  - Healing (single target, high)
- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)

### Units benefitting most from Reinier

- Bonnie
- Indris
- Himmel

### Units that can act as a replacement for Reinier

**Buffs on allies**

- Aliceth (100% `ATK`)
- Alna (100% `ATK`)
- Contess (100% `ATK`)

**Damage**

- Contess (100% `Magic`)
- Cryonaia (100% `Magic`)
- Cyran (100% `Magic`)

**Debuffs on enemies**

- Bonnie (100% `ATK debuff` `Damage taken debuff`)
- Pandora (100% `ATK debuff` `Damage taken debuff`)
- Contess (60% `ATK debuff`)

**Crowd Control**

- Ravion (63% `Displace` `Knock down`)

### Summary for Reinier

#### Damage types dealt by Reinier

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Multiple targets, Single target

#### Buffs provided by Reinier

- ATK buff (Legendary+) — Single target — `low`

#### Debuffs provided by Reinier

- ATK debuff (Legendary+) — Single target — `low`
- Damage taken debuff (Mythic+) — Single target — `low`

#### Crowd Control provided by Reinier

- Steadfast — Self — Conditional
- Unaffected — Self — Conditional
- Displace — Multiple targets — `high`
- Interrupt — Single target — `high`
- Knock up — Single target — `low`
- Knock down (Mythic+) — Single target — `low`

## Rhys

### Rhys's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Flame Barrage (ultimate)
- **Movement**: high movement (moves while attacking)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

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

### Units Rhys benefits from

Look for units providing: `ATK SPD / Haste` `CRIT` `CRIT DMG Boost`  
Common buffers are **Lyca**, **Twins**, or **Hugin**.

- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Rhys

- Nerion
- Carolina
- Perseus

### Units that can act as a replacement for Rhys

**Buffs on allies**

- Antandra (80% `Healing`)
- Gerda (80% `Healing`)
- Hepler (80% `Healing`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Atalanta (100% `Knock back`)
- Cassadee (100% `Knock back`)
- Indris (100% `Knock back`)

### Summary for Rhys

#### Damage types dealt by Rhys

- Primary damage type (unit): **Physical**
- Physical — Arc, Single target

#### Buffs provided by Rhys

- Healing — Single target — `medium`
- Movement speed buff (Mythic+) — Single target — `low`

#### Crowd Control provided by Rhys

- Knock back — Single target — `high`

## Rowan

### Rowan's behavior

`AFK Stages [A]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Fatal Greed (ultimate)
- **Movement**: moving (repositions on cast)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `medium`

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

### Units Rowan benefits from

Look for units providing: `Haste` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Velara**.

- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Isabella**
  - Haste buff (multiple targets, low) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Dunlingr**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
- **Thador**
  - Energy recovery (single target, low) `signature fuel`

### Units benefitting most from Rowan

**65** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Perseus
- Granny Dahnie
- Zorya
- Antandra
- Soren
- Temesia
- Niru
- Hodgkin
- Seth
- Twins

### Units that can act as a replacement for Rowan

**Similar Skills**

- Twins (66% `ally-healer` `energy-provider`)

**Damage**

- Aurora (100% `Magic`)
- Contess (100% `Magic`)
- Cryonaia (100% `Magic`)

**Debuffs on enemies**

- Dunlingr (100% `Energy drain`)
- Saida (100% `Energy drain`)
- Sylphira (66% `Energy drain`)

### Summary for Rowan

#### Rowan Provides

- Energy steal — Single target

#### Rowan Requires

- Once per battle (Mythic+) — Allies

#### Damage types dealt by Rowan

- Primary damage type (unit): **Magic**
- Magic — Single target

#### Buffs provided by Rowan

- Energy recovery — Area — `high`
- Healing — Area — `medium`
- DEF buff (Mythic+) — Single target — `high`
- Max HP buff (Mythic+) — Single target — `high`

#### Debuffs provided by Rowan

- Energy drain — Single target — `high`

## Saida

### Saida's behavior

`AFK Stages [S+]`, `Dream Realm [A]`, `Dream Realm (Endless) [A]`, `PVP [S+]`

- **Signature skill**: Seed Siphon (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `fast`, debuffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `high`

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

### Units Saida benefits from

Look for units providing: `Max HP` `Healing`  
Common buffers are **Solise**, **Velara**, or **Rowan**.

- **Contess**
  - Healing (multiple targets, high)
- **Hepler**
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
- **Hewynn**
  - Healing (all units, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)

### Units benefitting most from Saida

**15** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Shadewing
- Silven
- Alna
- Baelran
- Contess
- Cryonaia
- Daimon
- Eironn
- Faramor
- Gerda

### Units that can act as a replacement for Saida

**Damage**

- Contess (100% `Magic`)
- Solise (100% `Magic`)
- Velara (100% `Magic`)

### Summary for Saida

#### Saida Provides

- Revive ally — Single target

#### Saida Requires

- Boss encounter — Enemies

#### Damage types dealt by Saida

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Multiple targets, Single target

#### Buffs provided by Saida

- Shield — Multiple targets — `high`

#### Debuffs provided by Saida

- Energy drain — Single target — `high`

#### Crowd Control provided by Saida

- Unaffected — Self — Conditional
- Displace — Single target — `low`
- Interrupt — Area — `low`

## Salazer

### Salazer's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Rain of Blades (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, damage `medium`

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

### Units Salazer benefits from

Look for units providing: `Max HP` `Healing`  
Common buffers are **Rowan**, **Lyca**, or **Hugin**.

- **Hepler**
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Pandora**
  - Max HP buff (single target, medium)
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Hewynn**
  - Healing (all units, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)

### Units benefitting most from Salazer

- Nerion
- Perseus
- Silven

### Units that can act as a replacement for Salazer

**Buffs on allies**

- Daimon (100% `Life Drain` `Max HP`)
- Koko (100% `Life Drain` `Max HP`)
- Callan (60% `Max HP`)

**Similar Skills**

- Zorya (80% `hp-scaling` `life-drain`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Alna (100% `Bind`)
- Arden (100% `Bind`)
- Atalanta (100% `Bind`)

### Summary for Salazer

#### Damage types dealt by Salazer

- Primary damage type (unit): **Physical**
- Physical — Arc, Single target

#### Buffs provided by Salazer

- Lifedrain buff — Single target — `low`
- Shield (Supreme+) — Single target — `low` — conditional (frequent)

#### Crowd Control provided by Salazer

- Bind — Single target — `low`

## Satrana

### Satrana's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Fiery Dance (ultimate)
- **Movement**: moving (avg attack range 1.5 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, debuffs `medium`, damage `medium`
- **True damage**: Max HP-based damage `high`

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

### Units Satrana benefits from

- **Pandora**
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Thador**
  - Energy recovery (lieutenant, start of battle) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Satrana

- Indris
- Shadewing
- Bonnie

### Units that can act as a replacement for Satrana

**Buffs on allies**

- Koko (100% `Damage taken reduction`)
- Shakir (100% `Damage taken reduction`)

**Damage**

- Daimon (100% `Max HP-based damage` `Magic`)
- Shadewing (100% `Max HP-based damage` `Magic`)
- Shemira (100% `Max HP-based damage` `Magic`)

**Debuffs on enemies**

- Frieren (70% `Vitality debuff` `DoT`)

**Crowd Control**

- Mehira (100% `Charm`)

### Summary for Satrana

#### Satrana Provides

- Ally Vitality debuff on enemies — Area
- Ally grant (Sparks) — Area
- Invincibility — Self

#### Damage types dealt by Satrana

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Single target
- Max HP-based damage — Arc, Area — `high`

#### Buffs provided by Satrana

- Damage taken reduction (Legendary+) — Single target — `medium`

#### Debuffs provided by Satrana

- DoT — Area — `low`
- Vitality debuff — Area — `medium`

#### Crowd Control provided by Satrana

- Charm — Single target — `high`

## Scarlita

### Scarlita's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Divine Wrath (Mythic+)
- **Movement**: moving (brief reposition)

#### Skill overview

- **Signature skill**: speed `fast`, damage `low`
- **Ultimate**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, damage `medium`
- **True damage**: True damage `low`

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

### Units Scarlita benefits from

Look for units providing: `Execution` `Energy`  
Common buffers are **Rowan**, **Smokey & Meerky**, or **Ravion**.

- **Pandora**
  - Energy recovery (single target, low) `signature fuel`
- **Thador**
  - Energy recovery (single target, low) `signature fuel`

### Units benefitting most from Scarlita

- Nerion
- Carolina
- Perseus

### Units that can act as a replacement for Scarlita

**Buffs on allies**

- Callan (100% `Max HP`)
- Daimon (100% `Max HP`)
- Galahad (100% `Max HP`)

**Damage**

- Athalia (100% `Physical` `True damage`)
- Baelran (100% `Physical` `True damage`)
- Dionel (100% `Physical` `True damage`)

**Crowd Control**

- Baelran (69% `Knock up` `Knock down`)
- Cassadee (65% `Knock back` `Knock up` `Stun`)

### Summary for Scarlita

#### Scarlita Provides

- Invincibility — Self

#### Damage types dealt by Scarlita

- Primary damage type (unit): **Physical**
- Physical — All units, Arc, Area, Single target
- True damage — Multiple targets — `low`

#### Buffs provided by Scarlita

- Shield — Single target — `low`

#### Crowd Control provided by Scarlita

- Unaffected — Self — Conditional
- Knock back — All units — `low`
- Knock down — Arc — `low`
- Knock up — Area — `medium`
- Stun — Single target — `medium`

## Seth

### Seth's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Shadow Strike (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, buffs `medium`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `low`

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

### Units Seth benefits from

Look for units providing: `ATK` `Haste` `CRIT` `Healing` `Energy`  
Common buffers are **Rowan**, **Mikola**, or **Twins**.

- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)
- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (single target, high)

### Units benefitting most from Seth

- Nerion
- Perseus
- Carolina

### Units that can act as a replacement for Seth

**Buffs on allies**

- Brutus (60% `Life Drain`)
- Koko (60% `Life Drain`)
- Kordan (60% `Life Drain`)

**Similar Skills**

- Harak (66% `assassin` `life-drain`)

**Damage**

- Aliceth (100% `Physical`)
- Athalia (100% `Physical`)
- Faramor (100% `Physical`)

**Debuffs on enemies**

- Atalanta (100% `Phys DEF debuff`)
- Brutus (100% `Phys DEF debuff`)
- Fay (100% `Phys DEF debuff`)

**Crowd Control**

- Alna (100% `Bind`)
- Arden (100% `Bind`)
- Atalanta (100% `Bind`)

### Summary for Seth

#### Seth Provides

- Invincibility — Single target
- Stacking buff — Self

#### Damage types dealt by Seth

- Primary damage type (unit): **Physical**
- Physical — Self, Single target
- HP loss — Self

#### Buffs provided by Seth

- Crit buff — Single target — `low`
- Lifedrain buff — Single target — `low`

#### Debuffs provided by Seth

- Phys DEF debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Seth

- Bind — Single target — `low`

## Shadewing

### Shadewing's behavior

`AFK Stages [A+]`, `Dream Realm [S]`, `Dream Realm (Endless) [B]`, `PVP [S+]`

- **Signature skill**: Withering Curse (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `medium`, debuffs `medium`, damage `high`
- **Ultimate**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, debuffs `medium`, damage `high`
- **True damage**: HP loss `low`, Max HP-based damage `high`, True damage `low`

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

### Units Shadewing benefits from

Look for units providing: `ATK` `Max HP` `Energy` `Life Drain`  
Common buffers are **Hugin**, **Velara**, or **Lyca**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
  - Enables Debuff on target via Energy drain (single target)
- **Contess**
  - ATK buff (single target, high)
  - Enables Debuff on target via Max HP debuff (multiple targets)
- **Gunnar**
  - Enables Continuous damage on enemies via DoT
- **Aurora**
  - Enables Debuff on target via Haste debuff (multiple targets)
- **Baelran**
  - Enables Debuff on target via Max HP debuff (single target)

### Units benefitting most from Shadewing

- Bonnie
- Aliceth
### Summary for Shadewing

#### Shadewing Provides

- Debuff application — Single target
- DoT conversion — All units
- Invincibility — Self
- Damage leech from allies (Supreme+) — Self

#### Shadewing Requires

- Continuous damage on enemies — Enemies
- Debuff on target — Enemies

#### Damage types dealt by Shadewing

- Primary damage type (unit): **Magic**
- Magic — All units, Single target
- DoT — Single target
- HP loss — Single target — `low`
- Max HP-based damage — All units — `high`
- True damage — Single target — `low`

#### Debuffs provided by Shadewing

- Magic DEF debuff — All units — `medium`

## Shakir

### Shakir's behavior

`AFK Stages [B]`, `Dream Realm [B]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Ravaging Claws (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `medium`

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

### Units Shakir benefits from

Look for units providing: `Haste`  
Common buffers are **Twins**, **Hugin**, or **Velara**.

- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Valka**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Isabella**
  - Haste buff (multiple targets, low) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`

### Units benefitting most from Shakir

**12** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Atalanta
- Hepler
- Lenya
- Mikola
- Pang
- Soren
- Dionel
- Korin
- Sinbad
- Lucy

### Units that can act as a replacement for Shakir

**Buffs on allies**

- Koko (68% `Damage taken reduction` `Life Drain`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Debuffs on enemies**

- Alna (100% `Vitality debuff`)
- Faramor (100% `Vitality debuff`)
- Frieren (100% `Vitality debuff`)

### Summary for Shakir

#### Shakir Provides

- Transformation — Self

#### Damage types dealt by Shakir

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Multiple targets, Single target

#### Buffs provided by Shakir

- Damage taken reduction — Multiple targets — `high`
- Haste buff — Multiple targets — `high`
- Lifedrain buff — Single target — `medium`

#### Debuffs provided by Shakir

- Vitality debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Shakir

- Unaffected — Self — Form

## Shemira

### Shemira's behavior

`AFK Stages [A]`, `Dream Realm [S+]`, `Dream Realm (Endless) [A]`, `PVP [A+]`

- **Signature skill**: Phantom Procession (ultimate)
- **Movement**: mostly stationary (avg attack range 4.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `high`
- **True damage**: Max HP-based damage `high`

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

### Units Shemira benefits from

Look for units providing: `Max HP` `Healing` `Energy`  
Common buffers are **Hugin**, **Twins**, or **Solise**.

- **Contess**
  - Healing (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
  - Healing (single target, high)
- **Galahad**
  - Max HP via Shield (single target, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Shemira

- Bonnie
- Himmel

### Units that can act as a replacement for Shemira

**Damage**

- Shadewing (100% `Max HP-based damage` `Magic`)
- Gunnar (83% `Max HP-based damage`)
- Silven (68% `Magic`)

### Summary for Shemira

#### Damage types dealt by Shemira

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target
- Max HP-based damage — Area, Single target — `high`

## Silven

### Silven's behavior

`AFK Stages [S]`, `Dream Realm [S]`, `Dream Realm (Endless) [A+]`, `PVP [A+]`

- **Signature skill**: Gravity Collapse (Skill 1)
- **Movement**: stationary (avg attack range 12.0 tiles)

#### Skill overview

- **Signature skill**: speed `fast`, damage `high`
- **Ultimate**: speed `fast`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, damage `high`
- **True damage**: True damage `low`

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

### Units Silven benefits from

Look for units providing: `ATK SPD / Haste` `Energy` `DEF Penetration` `Physical DEF`  
Common buffers are **Twins**, **Velara**, or **Solise**.

- **Contess**
  - Enables Ally stat buffs via 2 ally stat buffs (start of battle)
- **Saida**
  - Enables Ally stat buffs via 1 ally stat buff
- **Gunnar**
  - ATK SPD buff (single target, low) `signature fuel`
  - Enables Ally stat buffs via 3 ally stat buffs
- **Koko**
  - Enables Ally stat buffs via 5 ally stat buffs
- **Cecia**
  - ATK SPD buff (single target, low) `signature fuel`
  - DEF Penetration buff (single target, medium)
  - Enables Ally stat buffs via 4 ally stat buffs

### Units benefitting most from Silven

- Nerion
- Carolina
- Bonnie

### Units that can act as a replacement for Silven

**Crowd Control**

- Baelran (100% `Knock down`)

### Summary for Silven

#### Silven Requires

- Ally stat buffs (Mythic+) — Allies

#### Damage types dealt by Silven

- Primary damage type (unit): **Magic**
- Magic — Self, Single target
- Max HP-based damage — Self
- True damage — Single target — `low`

#### Buffs provided by Silven

- DEF Penetration buff (Mythic+) — Single target — `low`

#### Crowd Control provided by Silven

- Knock down — Single target — `medium`

## Silvina

### Silvina's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Shadow Slayer (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, debuffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, damage `medium`

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

### Units Silvina benefits from

Look for units providing: `Max HP` `CRIT`  
Common buffers are **Hugin**, **Twins**, or **Lyca**.

- **Hepler**
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Galahad**
  - Max HP via Shield (single target, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Daimon**
  - Max HP via Shield (multiple targets, medium)

### Units benefitting most from Silvina

- Nerion
- Carolina
- Indris

### Units that can act as a replacement for Silvina

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Debuffs on enemies**

- Sinbad (100% `Energy drain` `Vitality debuff`)
- Dunlingr (75% `Energy drain`)
- Lily May (75% `Energy drain`)

**Crowd Control**

- Berial (64% `Frighten`)

### Summary for Silvina

#### Silvina Provides

- Marked target (focus fire) — Single target

#### Damage types dealt by Silvina

- Primary damage type (unit): **Physical**
- Physical — Single target

#### Debuffs provided by Silvina

- Energy drain — Single target — `high`
- Vitality debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Silvina

- Stun — Single target — `high`
- Frighten (EX+10) — Area — `medium`

## Sinbad

### Sinbad's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Whizzing Edge (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, damage `medium`
- **Non-ultimate**: speed `fast`, debuffs `medium`, damage `medium`

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

### Units Sinbad benefits from

Look for units providing: `ATK SPD / Haste` `Energy`  
Common buffers are **Lyca**, **Twins**, or **Hugin**.

- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Galahad**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Sinbad

- Indris
- Aliceth
- Bonnie

### Units that can act as a replacement for Sinbad

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

### Summary for Sinbad

#### Sinbad Provides

- Marked target (focus fire) — Multiple targets

#### Damage types dealt by Sinbad

- Primary damage type (unit): **Physical**
- Physical — Multiple targets, Self, Single target

#### Debuffs provided by Sinbad

- Damage taken debuff — Multiple targets — `low`
- ATK debuff (Mythic+) — Multiple targets — `medium`
- Energy drain (Mythic+) — Multiple targets — `medium`
- Magic DEF debuff (Mythic+) — Multiple targets — `medium`
- Phys DEF debuff (Mythic+) — Multiple targets — `medium`
- Vitality debuff (Mythic+) — Multiple targets — `high`

#### Crowd Control provided by Sinbad

- Unaffected — Multiple targets — Conditional

## Smokey & Meerky

### Smokey & Meerky's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [S]`, `PVP [C]`

- **Signature skill**: Special Aroma (ultimate)
- **Movement**: stationary (no finite attack range)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, buffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

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

### Units Smokey & Meerky benefits from

Look for units providing: `ATK` `Healing` `Energy`  
Common buffers are **Mikola**, **Rowan**, or **Solise**.

- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (single target, high)
- **Koko**
  - Healing (all units, medium)
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
- **Zanie**
  - Healing (single target, high)

### Units benefitting most from Smokey & Meerky

**23** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner

These are the **10** strongest pairings: 

- Zorya
- Hodgkin
- Seth
- Vala
- Antandra
- Granny Dahnie
- Hammie
- Harak
- Phraesto
- Ulmus

### Units that can act as a replacement for Smokey & Meerky

**Buffs on allies**

- Rowan (69% `Energy` `Healing`)

**Similar Skills**

- Solise (66% `ally-healer` `aoe-healing`)

**Damage**

- Aurora (100% `Magic`)
- Bonnie (100% `Magic`)
- Callan (100% `Magic`)

**Crowd Control**

- Lily May (80% `Interrupt`)
- Sylphira (80% `Interrupt`)
- Reinier (60% `Interrupt`)

### Summary for Smokey & Meerky

#### Damage types dealt by Smokey & Meerky

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target

#### Buffs provided by Smokey & Meerky

- Energy recovery — Area — `medium`
- Healing — Area — `high`
- ATK buff (Legendary+) — Multiple targets — `low`

#### Crowd Control provided by Smokey & Meerky

- Interrupt — Area — `low`
- Stun (Mythic+) — Single target — `low`

## Solise

### Solise's behavior

`AFK Stages [S]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S]`, `PVP [S]`

- **Signature skill**: Life's Embrace (ultimate)
- **Movement**: stationary (no finite attack range)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, heal `medium`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `medium`, buffs `medium`, damage `high`

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

### Units Solise benefits from

Look for units providing: `ATK`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Gunnar**
  - ATK SPD buff (single target, low) `signature fuel`
- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`

### Units benefitting most from Solise

**32** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Silven
- Dunlingr
- Mehira
- Himmel
- Niru
- Aliceth
- Alna
- Athalia
- Baelran
- Berial

### Units that can act as a replacement for Solise

**Damage**

- Twins (80% `Magic`)

### Summary for Solise

#### Solise Provides

- Ally blessing (Mythic+) — Single target

#### Damage types dealt by Solise

- Primary damage type (unit): **Magic**
- Magic — All units, Multiple targets, Single target

#### Buffs provided by Solise

- Healing — All units — `high`
- Healing over time — Single target — `high`
- Shield — Summons only — `medium`

#### Crowd Control provided by Solise

- Unaffected — Self — Start of battle

## Sonja

### Sonja's behavior

`AFK Stages [C]`, `Dream Realm [B]`, `Dream Realm (Endless) [B]`, `PVP [B]`

- **Signature skill**: Crimson Covenant (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Ally composition**: place allies on left and right at battle start (Crimson Covenant buffs; prioritizes front row)

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `medium`
- **Ultimate**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, damage `low`

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

### Units Sonja benefits from

Look for units providing: `Haste` `Max HP`  
Common buffers are **Hugin**, **Twins**, or **Velara**.

- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - Max HP via Shield (single target, medium)
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, low)

### Units benefitting most from Sonja

- Nerion
- Perseus
- Carolina

### Units that can act as a replacement for Sonja

**Buffs on allies**

- Aliceth (100% `ATK`)
- Alna (100% `ATK`)
- Contess (100% `ATK`)

**Similar Skills**

- Perseus (60% `ally-buffer`)
- Silven (60% `hp-scaling`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Crowd Control**

- Cassadee (100% `Stun`)
- Faramor (100% `Stun`)
- Gunnar (100% `Stun`)

### Summary for Sonja

#### Damage types dealt by Sonja

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Sonja

- ATK buff — Multiple targets — `low`

#### Crowd Control provided by Sonja

- Stun — Area — `low`

## Soren

### Soren's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Whirlwind Swing (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

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

### Units Soren benefits from

Look for units providing: `Haste` `Max HP` `Healing` `Energy`  
Common buffers are **Rowan**, **Hugin**, or **Twins**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Pandora**
  - Max HP buff (single target, medium)
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)

### Units benefitting most from Soren

- Nerion
- Perseus
- Silven

### Units that can act as a replacement for Soren

**Buffs on allies**

- Koko (96% `Damage taken reduction` `Max HP`)
- Shakir (96% `Damage taken reduction` `Haste`)

**Similar Skills**

- Lenya (66% `counterattack` `self-repositioner`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Crowd Control**

- Cassadee (100% `Knock back` `Stun`)
- Lenya (100% `Knock back` `Stun`)
- Perseus (100% `Knock back` `Stun`)

### Summary for Soren

#### Damage types dealt by Soren

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target

#### Buffs provided by Soren

- Damage taken reduction — Single target — `high`
- Haste buff (Legendary+) — Single target — `low`
- Shield (Supreme+) — Single target — `low`

#### Crowd Control provided by Soren

- Knock back — Single target — `high`
- Stun — Single target — `medium`

## Sylphira

### Sylphira's behavior

`AFK Stages [A]`, `Dream Realm [A+]`, `Dream Realm (Endless) [?]`, `PVP [S]`

- **Signature skill**: Grand Finale (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, debuffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `high`
- **True damage**: True damage `high`

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

### Units Sylphira benefits from

Look for units providing: `ATK` `Haste` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Velara**.

- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)
- **Mehira**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Zanie**
  - Healing (single target, high)
- **Gunnar**
  - ATK SPD buff (single target, low) `signature fuel`
- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`

### Units benefitting most from Sylphira

- Nerion
- Indris
- Bonnie

### Units that can act as a replacement for Sylphira

**Damage**

- Shadewing (81% `Magic` `Max HP-based damage` `True damage`)
- Silven (71% `Magic` `True damage`)

### Summary for Sylphira

#### Sylphira Provides

- Dispel debuffs (Mythic+) — Self
- Stacking buff (Mythic+) — Self

#### Damage types dealt by Sylphira

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- Max HP-based damage — Single target — `medium`
- True damage — Area — `high`

#### Debuffs provided by Sylphira

- Energy drain — Single target — `medium`
- Max HP debuff — Area — `medium`

#### Crowd Control provided by Sylphira

- Immune — Self — On skill
- Unaffected — Area — Conditional
- Cleanse (Mythic+) — Self — On skill
- Interrupt — Area — `low`
- Knock down — Area — `medium`
- Silence — Area — `low`

## Talene

### Talene's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [A]`, `PVP [B]`

- **Signature skill**: Divine Conflagration (ultimate)
- **Movement**: moving (avg attack range 3.0 tiles)
- **Ally composition**: frontmost ally carries Pyre of Renewal (AoE damage and healing)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `high`
- **True damage**: HP loss `medium`

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

### Units Talene benefits from

Look for units providing: `ATK` `Max HP` `Healing` `Life Drain`  
Common buffers are **Mikola**, **Smokey & Meerky**, or **Solise**.

- **Hepler**
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
  - Lifedrain buff (multiple targets, low)
- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (single target, high)
- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)

### Units benefitting most from Talene

- Nerion
- Perseus
- Silven

### Units that can act as a replacement for Talene

**Buffs on allies**

- Mikola (100% `Healing`)
- Solise (100% `Healing`)

**Damage**

- Athalia (100% `HP loss`)
- Dunlingr (100% `HP loss` `Magic`)
- Zorya (100% `HP loss` `Magic`)

**Crowd Control**

- Cassadee (100% `Knock back`)
- Indris (100% `Knock back`)
- Kordan (100% `Knock back`)

### Summary for Talene

#### Talene Provides

- Transformation — Self
- Stacking buff (Mythic+) — Area

#### Damage types dealt by Talene

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- HP loss — All units — `medium`

#### Buffs provided by Talene

- Healing — Area — `low`
- Healing over time — Area — `low`

#### Crowd Control provided by Talene

- Knock back — Area — `low`

## Tasi

### Tasi's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Eternal Dreamscape (ultimate)
- **Movement**: stationary (avg attack range 10.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

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

### Units Tasi benefits from

Look for units providing: `ATK` `Haste` `Max HP` `Healing`  
Common buffers are **Hugin**, **Twins**, or **Rowan**.

- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Pandora**
  - Max HP buff (single target, medium)
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - Max HP via Shield (single target, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Tasi

- Carolina

### Units that can act as a replacement for Tasi

**Damage**

- Frieren (100% `DoT` `Magic`)
- Bryon (96% `DoT` `Magic`)
- Shadewing (65% `Magic` `DoT`)

### Summary for Tasi

#### Tasi Provides

- Invincibility — Area
- Sleep (area) — Single target
- Transformation — Self

#### Damage types dealt by Tasi

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — All units, Single target

#### Crowd Control provided by Tasi

- Sleep — All units — `high`
- Stun — Area — `high`

## Temesia

### Temesia's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Knight's Heart (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, damage `low`
- **True damage**: True damage `low`

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

### Units Temesia benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `Max HP` `Healing` `Energy`  
Common buffers are **Lyca**, **Rowan**, or **Hugin**.

- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Pandora**
  - Max HP buff (single target, medium)
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Hewynn**
  - Healing (all units, high)

### Units benefitting most from Temesia

- Nerion
- Carolina
- Himmel

### Units that can act as a replacement for Temesia

**Similar Skills**

- Cassadee (60% `aoe-damage` `enemy-debuffer`)

**Damage**

- Korin (100% `Physical` `Max HP-based damage` `True damage`)
- Indris (88% `Physical` `Max HP-based damage` `True damage`)
- Nara (87% `Max HP-based damage` `Physical` `True damage`)

**Debuffs on enemies**

- Atalanta (100% `Phys DEF debuff`)
- Brutus (100% `Phys DEF debuff`)
- Fay (100% `Phys DEF debuff`)

**Crowd Control**

- Lucca (100% `Knock down` `Interrupt`)
- Sylphira (100% `Knock down` `Interrupt`)
- Antandra (83% `Knock down`)

### Summary for Temesia

#### Temesia Provides

- Stacking buff — Single target

#### Damage types dealt by Temesia

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target
- Max HP-based damage — Single target — `high`
- True damage — Single target — `low`

#### Debuffs provided by Temesia

- Phys DEF debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Temesia

- Unaffected (Mythic+) — Self — Permanent
- Interrupt — Single target — `low`
- Knock down — All units — `low`

## Thador

### Thador's behavior

`AFK Stages [S]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Darkmoon Pact (Skill 1)
- **Movement**: moving (avg attack range 0.2 tiles)
- **Ally composition**: place lieutenant 1 tile behind at battle prep (Crit + shared shields)

#### Skill overview

- **Signature skill**: speed `slow`, first cast speed `fast`, buffs `medium`, damage `medium`
- **Ultimate**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

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

### Units Thador benefits from

Look for units providing: `Max HP` `CRIT` `Healing`  
Common buffers are **Rowan**, **Hugin**, or **Twins**.

- **Contess**
  - Healing (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
  - Healing (single target, high)
- **Galahad**
  - Max HP via Shield (single target, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Thador

- Pandora

### Units that can act as a replacement for Thador

**Buffs on allies**

- Ravion (100% `Energy`)
- Rowan (100% `Energy`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Debuffs on enemies**

- Eironn (100% `Magic DEF debuff`)
- Shadewing (100% `Magic DEF debuff`)

**Crowd Control**

- Athalia (100% `Knock down`)
- Baelran (100% `Knock down`)
- Kordan (100% `Knock down`)

### Summary for Thador

#### Damage types dealt by Thador

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target

#### Buffs provided by Thador

- Energy recovery (EX+10) — Single target — `low`

#### Debuffs provided by Thador

- Magic DEF debuff (Mythic+) — Single target — `high`

#### Crowd Control provided by Thador

- Knock down — Single target — `high`

## Thoran

### Thoran's behavior

`AFK Stages [B]`, `Dream Realm [A+]`, `Dream Realm (Endless) [A]`, `PVP [B]`

- **Signature skill**: Resurrection (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Ally composition**: place ally 1 tile behind at battle prep (Soul Pact damage share and revive)

#### Skill overview

- **Signature skill**: speed `fast`
- **Ultimate**: speed `slow`, buffs `medium`, damage `low`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`

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

### Units Thoran benefits from

Look for units providing: `Max HP` `Healing` `Energy`  
Common buffers are **Rowan**, **Solise**, or **Hugin**.

- **Contess**
  - Healing (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
  - Healing (single target, high)
- **Galahad**
  - Max HP via Shield (single target, medium)
- **Thador**
  - Energy recovery (single target, low) `signature fuel`

### Units benefitting most from Thoran

- Himmel
- Perseus
- Silven

### Units that can act as a replacement for Thoran

**Buffs on allies**

- Dunlingr (100% `Life Drain`)
- Kordan (100% `Life Drain`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Crowd Control**

- Saida (100% `Interrupt`)
- Sylphira (100% `Interrupt`)

### Summary for Thoran

#### Thoran Provides

- Revive ally — Self

#### Damage types dealt by Thoran

- Primary damage type (unit): **Physical**
- Physical — Self, Single target

#### Buffs provided by Thoran

- Lifedrain buff — Single target — `low`

#### Crowd Control provided by Thoran

- Unaffected — Self — On skill
- Interrupt — Single target — `low`

## Tilaya

### Tilaya's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Wrath of the Wilds (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, heal `medium`, buffs `medium`, damage `low`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

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

### Units Tilaya benefits from

Look for units providing: `Max HP` `Healing`  
Common buffers are **Solise**, **Rowan**, or **Smokey & Meerky**.

- **Hepler**
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Contess**
  - Healing (multiple targets, high)
- **Gerda**
  - Healing (multiple targets, high)
- **Marcille**
  - Healing (multiple targets, high)

### Units benefitting most from Tilaya

- Perseus
- Silven
- Zorya

### Units that can act as a replacement for Tilaya

**Buffs on allies**

- Himmel (100% `Max HP`)
- Twins (75% `Max HP`)

**Similar Skills**

- Silven (100% `hp-scaling`)
- Pippa (60% `hp-scaling`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

### Summary for Tilaya

#### Tilaya Provides

- Start-of-battle cast — Arc

#### Damage types dealt by Tilaya

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target

#### Buffs provided by Tilaya

- Max HP buff (EX+10) — Area — `medium`

#### Crowd Control provided by Tilaya

- Unaffected — Arc — Start of battle

## Ulmus

### Ulmus's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Way of the Forest (Skill 2)
- **Movement**: moving (stationary when rooted)
- **Ally composition**: when rooted, shields frontmost ally instead of self

#### Skill overview

- **Signature skill**: speed `fast`, heal `medium`
- **Ultimate**: speed `slow`, heal `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

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

### Units Ulmus benefits from

Look for units providing: `Max HP` `Healing` `Energy`  
Common buffers are **Rowan**, **Smokey & Meerky**, or **Solise**.

- **Hepler**
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Contess**
  - Healing (multiple targets, high)
- **Marcille**
  - Healing (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)

### Units benefitting most from Ulmus

- Nerion
- Carolina
- Himmel

### Units that can act as a replacement for Ulmus

**Buffs on allies**

- Lenya (60% `Max HP`)
- Solise (60% `Healing`)

**Similar Skills**

- Hepler (66% `ally-shielder` `transformation`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Crowd Control**

- Kordan (100% `Knock back` `Bind` `Knock down`)
- Indris (94% `Knock back` `Bind`)
- Scarlita (78% `Knock back` `Knock down`)

### Summary for Ulmus

#### Ulmus Requires

- Vulnerable enemy (Mythic+) — Enemies

#### Damage types dealt by Ulmus

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Ulmus

- Healing over time — Single target — `low`
- Shield — Single target — `low`

#### Crowd Control provided by Ulmus

- Unaffected — Self — Conditional
- Bind (Mythic+) — Single target — `low`
- Knock down (Mythic+) — Single target — `low`
- Knock back (Supreme+) — Area — `low`

## Vala

### Vala's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Swift Shift (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `low`
- **True damage**: HP loss `medium`, True damage `medium`

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

### Units Vala benefits from

Look for units providing: `ATK` `Haste` `Healing` `Energy`  
Common buffers are **Rowan**, **Mikola**, or **Twins**.

- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Mehira**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
  - Enables Enemy defeat via HP threshold strike
- **Lorsan**
  - Healing (all units, high)
- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (single target, high)

### Units benefitting most from Vala

- Nerion
- Indris
- Perseus

### Units that can act as a replacement for Vala

**Buffs on allies**

- Damian (100% `Haste`)
- Galahad (100% `Haste`)
- Hugin (100% `Haste`)

**Damage**

- Athalia (100% `HP loss` `True damage` `Physical`)
- Faramor (100% `HP loss` `True damage` `Physical`)
- Shadewing (78% `HP loss` `True damage`)

**Debuffs on enemies**

- Aliceth (66% `Marked target (focus fire)`)

**Crowd Control**

- Cassadee (100% `Stun`)
- Damian (100% `Stun`)
- Faramor (100% `Stun`)

### Summary for Vala

#### Vala Provides

- Marked target (focus fire) — Self

#### Vala Requires

- Enemy defeat (Legendary+) — Enemies

#### Damage types dealt by Vala

- Primary damage type (unit): **Physical**
- Physical — Single target
- HP loss — Single target — `medium`
- True damage — Single target — `medium`

#### Buffs provided by Vala

- Haste buff (Mythic+) — Single target — `high`

#### Debuffs provided by Vala

- Haste debuff — Single target — `low`
- Marked target (focus fire) — Single target — `medium`

#### Crowd Control provided by Vala

- Untargetable (Mythic+) — Multiple targets — Conditional
- Stun — Single target — `medium`

## Valen

### Valen's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Thunder Swordwork (ultimate)
- **Movement**: moving (avg attack range 1.4 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, damage `low`
- **Non-ultimate**: speed `fast`, damage `medium`

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

### Units Valen benefits from

Look for units providing: `ATK`  
Common buffers are **Lyca**, **Rowan**, or **Ravion**.

- **Pandora**
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Valen

- Nerion
- Carolina
- Indris

### Units that can act as a replacement for Valen

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Alna (100% `Haste debuff`)
- Aurora (100% `Haste debuff`)
- Bonnie (100% `Haste debuff`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Arden (100% `Stun`)

### Summary for Valen

#### Valen Provides

- Invincibility — Self
- Stacking buff (Mythic+) — Single target

#### Damage types dealt by Valen

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Debuffs provided by Valen

- Haste debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Valen

- Stun (Supreme+) — Single target — `medium`

## Valka

### Valka's behavior

`AFK Stages [C]`, `Dream Realm [A+]`, `Dream Realm (Endless) [B]`, `PVP [B]`

- **Signature skill**: Phantom Slasher (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `fast`, first cast speed `fast`, heal `medium`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, damage `high`
- **True damage**: Max HP-based damage `medium`

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

### Units Valka benefits from

Look for units providing: `ATK SPD / Haste` `Max HP` `Healing` `Energy`  
Common buffers are **Rowan**, **Hugin**, or **Twins**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Contess**
  - Healing (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
  - Healing (single target, high)

### Units benefitting most from Valka

**12** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Cecia
- Dionel
- Fay
- Lyca
- Mirael
- Rhys
- Marcille
- Brutus
- Sinbad
- Lucy

### Units that can act as a replacement for Valka

**Buffs on allies**

- Dunlingr (73% `ATK SPD` `Life Drain` `Haste`)

**Damage**

- Daimon (100% `Max HP-based damage`)
- Gunnar (100% `Max HP-based damage` `Physical`)
- Shadewing (100% `Max HP-based damage`)

**Crowd Control**

- Callan (84% `Knock down` `Stun`)
- Faramor (60% `Stun`)
- Koko (60% `Stun`)

### Summary for Valka

#### Damage types dealt by Valka

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- Max HP-based damage — Area — `medium`

#### Buffs provided by Valka

- ATK SPD buff — Multiple targets — `high`
- Lifedrain buff (EX+10) — Single target — `high`
- Haste buff (Supreme+) — Single target — `low`

#### Crowd Control provided by Valka

- Unaffected — Self — On skill
- Knock down — Area — `low`
- Stun — Area — `low`

## Velara

### Velara's behavior

`AFK Stages [S+]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S]`, `PVP [B]`

- **Signature skill**: Ruthless Rite (ultimate)
- **Movement**: stationary (no finite attack range)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, heal `medium`, debuffs `medium`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

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

### Units Velara benefits from

Look for units providing: `Haste` `Max HP` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, medium)
- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - Max HP via Shield (single target, medium)
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, low)

### Units benefitting most from Velara

**25** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Silven
- Zorya
- Mehira
- Sylphira
- Viperian
- Himmel
- Dunlingr
- Isabella
- Baelran
- Bryon

### Units that can act as a replacement for Velara

**Buffs on allies**

- Solise (76% `Healing`)

**Similar Skills**

- Solise (90% `ally-healer` `ally-shielder` `aoe-healing`)

**Damage**

- Solise (100% `Magic`)
- Twins (80% `Magic`)

**Crowd Control**

- Gwyneth (100% `Bind`)

### Summary for Velara

#### Velara Provides

- Start-of-battle cast — All units

#### Velara Requires

- Boss encounter — Allies

#### Damage types dealt by Velara

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Multiple targets, Single target

#### Buffs provided by Velara

- Haste buff — Single target — `high`
- Healing — Area — `medium`

#### Debuffs provided by Velara

- Haste debuff — Single target — `low`

#### Crowd Control provided by Velara

- Bind — Single target — `high`

## Viperian

### Viperian's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Crimson Waltz (Mythic+)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)

#### Skill overview

- **Signature skill**: speed `slow`, damage `low`
- **Ultimate**: speed `normal`, first cast speed `fast`, heal `medium`, damage `high`
- **Non-ultimate**: speed `slow`, heal `medium`, debuffs `medium`, damage `medium`

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

### Units Viperian benefits from

Look for units providing: `Haste` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Velara**.

- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Viperian

- Shadewing
- Bonnie
- Indris

### Units that can act as a replacement for Viperian

**Similar Skills**

- Arden (66% `aoe-damage` `dot-specialist`)
- Lorsan (66% `aoe-damage` `dot-specialist`)
- Cecia (60% `dot-specialist` `life-drain`)

**Damage**

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Cassadee (100% `Magic`)

**Debuffs on enemies**

- Dunlingr (100% `Energy drain`)
- Hodgkin (100% `Energy drain`)
- Lily May (100% `Energy drain`)

### Summary for Viperian

#### Damage types dealt by Viperian

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Debuffs provided by Viperian

- Energy drain — Single target — `medium`

#### Crowd Control provided by Viperian

- Unaffected — Self — Start of battle

## Walker

### Walker's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Six-Shot (ultimate)
- **Movement**: moving (avg attack range 2.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`, debuffs `medium`, damage `low`
- **True damage**: HP loss `medium`, Max HP-based damage `low`

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

### Units Walker benefits from

Look for units providing: `Max HP` `CRIT` `CRIT DMG Boost` `Life Drain`  
Common buffers are **Lyca**, **Rowan**, or **Hugin**.

- **Pandora**
  - Max HP buff (single target, medium)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Shakir**
  - Lifedrain buff (single target, medium)
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Valka**
  - Lifedrain buff (single target, high)
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Hepler**
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Zandrok**
  - Max HP buff (multiple targets, low)
  - Lifedrain buff (area, low, conditional (frequent))
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Walker

- Nerion
- Carolina
- Indris

### Units that can act as a replacement for Walker

**Damage**

- Shadewing (75% `HP loss` `Max HP-based damage`)
- Gwyneth (68% `Physical` `Max HP-based damage`)
- Aliceth (62% `Physical` `HP loss`)

**Debuffs on enemies**

- Nazrik (100% `Crit Resist debuff`)

**Crowd Control**

- Cassadee (100% `Stun`)
- Damian (100% `Stun`)
- Faramor (100% `Stun`)

### Summary for Walker

#### Damage types dealt by Walker

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- HP loss — Single target — `medium`
- Max HP-based damage — Single target — `low`

#### Debuffs provided by Walker

- Crit Resist debuff (Mythic+) — Single target — `low`

#### Crowd Control provided by Walker

- Stun — Single target — `medium`

## Zandrok

### Zandrok's behavior

`AFK Stages [A+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Rallying Roar (Skill 1)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `medium`
- **Ultimate**: speed `slow`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `medium`

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

### Units Zandrok benefits from

Look for units providing: `Haste` `Max HP` `Healing` `Life Drain`  
Common buffers are **Hugin**, **Twins**, or **Solise**.

- **Contess**
  - Healing (multiple targets, high)
- **Daimon**
  - Max HP via Shield (multiple targets, medium)
  - Lifedrain buff (single target, medium)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
  - Healing (single target, high)
- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - Max HP via Shield (single target, medium)

### Units benefitting most from Zandrok

- Perseus
- Nerion
- Silven

### Units that can act as a replacement for Zandrok

**Buffs on allies**

- Twins (63% `Haste` `Max HP`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

### Summary for Zandrok

#### Damage types dealt by Zandrok

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Self, Single target

#### Buffs provided by Zandrok

- Haste buff — Area — `low` — conditional (frequent)
- Lifedrain buff — Area — `low` — conditional (frequent)
- Max HP buff — Multiple targets — `low`

#### Crowd Control provided by Zandrok

- Knock up — Area — `low`
- Stun — Area — `low`

## Zanie

### Zanie's behavior

`AFK Stages [A+]`, `Dream Realm [S]`, `Dream Realm (Endless) [A+]`, `PVP [A]`

- **Signature skill**: Vein Pulse (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, buffs `medium`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `medium`, buffs `medium`, damage `medium`

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

### Units Zanie benefits from

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Twins**, **Hugin**, or **Velara**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, medium)
- **Galahad**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, low) `signature fuel`
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))

### Units benefitting most from Zanie

- Alna
- Daimon
- Eironn

### Units that can act as a replacement for Zanie

**Damage**

- Baelran (100% `Physical`)
- Faramor (100% `Physical`)
- Gunnar (100% `Physical`)

**Crowd Control**

- Twins (66% `Knock back`)

### Summary for Zanie

#### Zanie Provides

- Summoning — Self

#### Damage types dealt by Zanie

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target

#### Buffs provided by Zanie

- Healing — Single target — `high`
- Shield — Single target — `high`
- DEF Penetration buff (Legendary+) — Single target — `medium`
- Max HP buff (Mythic+) — Single target — `low`

#### Debuffs provided by Zanie

- ATK debuff (Supreme+) — Single target — `low`
- DoT (Supreme+) — Single target — `low`
- Phys DEF debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Zanie

- Knock back — Single target — `high`
- Stun — Single target — `low`

## Zorya

### Zorya's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Guardian's Ring (ultimate)
- **Movement**: moving (inactive while dormant)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, heal `medium`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `high`
- **True damage**: HP loss `high`

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

### Units Zorya benefits from

Look for units providing: `Haste` `Max HP` `Healing` `Energy`  
Common buffers are **Rowan**, **Hugin**, or **Smokey & Meerky**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Contess**
  - Healing (multiple targets, high)
  - Enables Ally Ultimate casts via Start-of-battle Ultimate
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - Max HP via Shield (single target, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Pandora**
  - Max HP buff (single target, medium)
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Enables Ally Ultimate casts via Energy recovery (Ultimate pace)

### Units benefitting most from Zorya

- Nerion
- Carolina
- Bonnie

### Units that can act as a replacement for Zorya

**Similar Skills**

- Daimon (60% `hp-scaling` `life-drain`)
- Shemira (60% `hp-scaling` `life-drain`)

**Damage**

- Niru (94% `Magic` `HP loss`)
- Shadewing (94% `Magic` `HP loss`)
- Dunlingr (91% `HP loss` `Magic`)

**Crowd Control**

- Perseus (66% `Stun`)
- Valka (66% `Stun` `Knock down`)

### Summary for Zorya

#### Zorya Provides

- Invincibility — Area

#### Zorya Requires

- Ally Ultimate casts (Mythic+) — Allies

#### Damage types dealt by Zorya

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Single target
- HP loss — Area — `high`

#### Crowd Control provided by Zorya

- Steadfast — Self — Start of battle
- Unaffected (EX+10) — Single target — On skill
- Knock down — Arc — `medium`
- Stun — Area — `medium`

# Heroes Overview

Per-hero synergy picks and summaries derived from skill text in
[Heroes.md](Heroes.md). [Heroes.md](Heroes.md) has skills only.
Synergy: stat buff tags under **Units improving X**, and
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
- **Damage types**: Physical `high`, HP loss `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `average`, damage `high`
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
Common buffers are **Twins**, **Ravion**, or **Hugin**.

Aliceth also requires units **putting debuffs** on enemies

- **Zanie**
  - ATK buff (single target, low)
  - Healing (single target, average)
  - DEF Penetration buff (single target, average)
  - Enables Debuff on target via ATK debuff (single target)
- **Velara**
  - Healing (area, low)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Enables Debuff on target via Magic DEF debuff (single target)
- **Gwyneth**
  - Enables Debuff on target via DoT (single target)
- **Gunnar**
  - ATK buff (single target, low)
  - ATK SPD buff (single target, high) `signature fuel`
- **Shadewing**
  - Enables Debuff on target via Magic DEF debuff (single target)

### Units benefitting most from Aliceth

Aliceth provides Ally empower buff to single targets `high`, Attack range buff to single targets `high`, DEF Penetration buff to multiple targets `high`, ATK buff (Legendary+) to multiple targets `average`, and Fatal blow immunity (Mythic+) to single targets `high` — conditional (rare).

- Lily May (3.9 / 5)
- Kulu (3.4 / 5)
- Nerion (3.2 / 5)
- Kordan (2.8 / 5)

### Units that can act as a replacement for Aliceth

**Damage**

- Faramor (100% `Physical` `HP loss`)
- Kordan (94% `Physical` `HP loss`)
- Ravion (94% `Physical` `HP loss`)

**Crowd Control**

- Twins (91% `Blind` `Knock back`)

### Summary for Aliceth

#### Aliceth Provides

- Ally grant (Brightfeather) — Single target
- Instant defeat — Multiple targets
- Invincibility — Single target
- Marked target (focus fire) — Single target
- Reposition enemies — Single target
- Fatal blow save (Mythic+) — Area

#### Damage types dealt by Aliceth

- Physical — Area, Multiple targets, Single target
- HP loss — Single target — `high`

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
- **Ally composition**: place ally in same row at battle prep (Winter Warrior buffs)
- **Damage types**: Physical `high`

#### Skill overview

- **Signature skill**: speed `slow`, first cast speed `fast`, heal `average`, buffs `average`, damage `average`
- **Ultimate**: speed `slow`, first cast speed `fast`, heal `average`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `slow`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `high`

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
Common buffers are **Twins**, **Hugin**, or **Contess**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
  - Healing (single target, average)
- **Velara**
  - Healing (area, low)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, high) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Alna

Alna provides Ally empower buff to single targets `low`, Max HP buff to single targets `low`, Dmg and CC immunity (EX+15) to single targets `high`, and ATK buff (Supreme+) to single targets `average`.

- Bonnie (3.7 / 5)
- Indris (3.4 / 5)

### Units that can act as a replacement for Alna

**Damage**

- Athalia (100% `Physical`)
- Baelran (100% `Physical`)
- Gunnar (100% `Physical`)

**Crowd Control**

- Kordan (100% `Bind`)

### Summary for Alna

#### Alna Provides

- Ally empower — Single target
- Start-of-battle cast — All units
- Dmg and CC immunity (Mythic+) — Self
- Dmg and CC immunity (ally) (EX+15) — Single target

#### Damage types dealt by Alna

- Physical — All units, Arc, Single target

#### Debuffs provided by Alna

- Haste — Area — `high`
- Vitality (Supreme+) — Area — `low`

#### Crowd Control provided by Alna

- Immune (Mythic+) — Self — Start of battle
- Bind (Supreme+) — Area — `average`

## Alsa

### Alsa's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Twirling Rocks (ultimate)
- **Movement**: mostly stationary (avg attack range 6.0 tiles)
- **Damage types**: Magic `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `average`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, debuffs `average`, damage `average`

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

Look for units providing: `Haste` `Max HP`  
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, low)
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Tasi**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Pandora**
  - Max HP buff (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Alsa

- Bonnie (2.5 / 5)
- Indris (2.2 / 5)
- Nerion (1.6 / 5)

### Units that can act as a replacement for Alsa

**Similar Skills**

- Athalia (60% `self-repositioner` `transformation`)

**Damage**

- Callan (100% `Magic`)
- Cassadee (100% `Magic`)
- Cryonaia (100% `Magic`)

**Debuffs on enemies**

- Kulu (72% `Movement speed debuff`)

**Crowd Control**

- Atalanta (100% `Stun` `Knock back`)
- Lenya (100% `Stun` `Knock back`)
- Perseus (100% `Stun` `Knock back`)

### Summary for Alsa

#### Alsa Provides

- Enhanced form — Area

#### Damage types dealt by Alsa

- Magic — All units, Area, Single target

#### Debuffs provided by Alsa

- Movement speed — Area — `low`
- Energy drain (Mythic+) — Single target — `low`

#### Crowd Control provided by Alsa

- Immune — Area — Permanent
- Knock back — Single target — `low`
- Stun — Single target — `average`

## Antandra

### Antandra's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Shield Assault (ultimate)
- **Movement**: high movement (repositioning skills)
- **Ally composition**: frontmost ally becomes guarded ally (shared shields)
- **Damage types**: Physical `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `average`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `low`

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

Look for units providing: `Max HP` `Healing` `Energy`  
Common buffers are **Rowan**, **Twins**, or **Smokey & Meerky**.

- **Hepler**
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, average)
- **Pandora**
  - Max HP buff (single target, average)
  - Healing (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Hewynn**
  - Healing (all units, average)
- **Lorsan**
  - Healing (all units, average)

### Units benefitting most from Antandra

Antandra provides DEF buff (Supreme+) to single targets `low`.

- Carolina (4.1 / 5)

### Units that can act as a replacement for Antandra

**Buffs on allies**

- Carolina (100% `Magic DEF` `Physical DEF`)
- Fay (100% `Magic DEF` `Physical DEF`)
- Hepler (100% `Magic DEF` `Physical DEF`)

**Similar Skills**

- Lucca (60% `ally-shielder`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Atalanta (100% `Physical`)

**Crowd Control**

- Lucca (72% `Stun` `Knock down`)
- Hepler (67% `Stun` `Taunt`)
- Zorya (60% `Stun` `Knock down`)

### Summary for Antandra

#### Antandra Provides

- Stacking buff (Supreme+) — Single target

#### Damage types dealt by Antandra

- Physical — Arc, Area, Single target

#### Crowd Control provided by Antandra

- Unaffected — Area — On skill
- Knock down — Area — `low`
- Stun — Area — `high`
- Taunt — Area — `low`

## Arden

### Arden's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Force of Nature (ultimate)
- **Movement**: stationary (no finite attack range)
- **Damage types**: Magic `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
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

- **Pandora**
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, low, conditional (frequent))
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
- **Gunnar**
  - ATK buff (single target, low)
  - ATK SPD buff (single target, high) `signature fuel`

### Units benefitting most from Arden

Arden provides Energy recovery to single targets `low`.

- Carolina (1.9 / 5)
- Nerion (1.7 / 5)
- Zorya (1.4 / 5)

### Units that can act as a replacement for Arden

**Buffs on allies**

- Lyca (100% `Energy`)
- Ravion (100% `Energy`)
- Rowan (100% `Energy`)

**Similar Skills**

- Lorsan (100% `aoe-damage` `dot-specialist`)
- Faramor (96% `aoe-damage` `dot-specialist`)
- Viperian (80% `aoe-damage` `dot-specialist`)

**Damage**

- Alsa (100% `Magic`)
- Aurora (100% `Magic`)
- Berial (100% `Magic`)

**Crowd Control**

- Alna (100% `Bind`)
- Atalanta (100% `Bind`)
- Carolina (100% `Bind`)

### Summary for Arden

#### Damage types dealt by Arden

- Magic — Area, Multiple targets, Single target

#### Crowd Control provided by Arden

- Bind — Single target — `average`

## Atalanta

### Atalanta's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Wild Sniper (ultimate)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Physical `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `average`
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
Common buffers are **Twins**, **Damian**, or **Rowan**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing (multiple targets, high)
  - DEF buff (single target, low)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Lucca**
  - DEF buff (area, high)
- **Tasi**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Atalanta

- Indris (1.7 / 5)
- Aliceth (1.7 / 5)
- Nerion (1.6 / 5)

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
- Fay (80% `Phys DEF debuff`)

**Crowd Control**

- Gwyneth (100% `Stun` `Bind`)
- Perseus (96% `Stun` `Knock back`)
- Alsa (80% `Stun` `Knock back`)

### Summary for Atalanta

#### Atalanta Provides

- Reposition enemies — Single target
- Stat steal (EX+10) — Single target

#### Damage types dealt by Atalanta

- Physical — Area, Single target

#### Debuffs provided by Atalanta

- Phys DEF (Supreme+) — Single target — `high`

#### Crowd Control provided by Atalanta

- Bind — Single target — `average`
- Knock back — Single target — `low`
- Stun — Single target — `average`

## Athalia

### Athalia's behavior

`AFK Stages [S]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [S+]`

- **Signature skill**: Unbroken Retribution (ultimate)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Physical `high`, True damage `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `average`, buffs `average`, debuffs `average`, damage `average`
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
Common buffers are **Twins**, **Hugin**, or **Contess**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
  - Healing (single target, average)
- **Velara**
  - Healing (area, low)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, high) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Athalia

- Carolina (1.4 / 5)
- Indris (1.3 / 5)
- Nerion (1.3 / 5)

### Units that can act as a replacement for Athalia

**Similar Skills**

- Baelran (80% `hp-scaling` `transformation`)
- Kordan (66% `hp-scaling` `self-repositioner`)

**Damage**

- Baelran (100% `Physical` `True damage`)
- Faramor (100% `Physical` `True damage`)
- Frieren (91% `True damage`)

**Debuffs on enemies**

- Contess (100% `ATK debuff`)
- Ravion (100% `ATK debuff`)
- Zanie (100% `ATK debuff`)

**Crowd Control**

- Baelran (100% `Knock down`)
- Frieren (100% `Knock down`)
- Silven (100% `Knock down`)

### Summary for Athalia

#### Athalia Provides

- Invincibility — Self
- Transformation — Self

#### Damage types dealt by Athalia

- Physical — All units, Area, Single target
- True damage — Single target — `average`

#### Debuffs provided by Athalia

- ATK — Single target — `low`

#### Crowd Control provided by Athalia

- Unaffected — Area — On skill
- Knock down — Single target — `low`

## Aurora

### Aurora's behavior

`AFK Stages [A]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S+]`, `PVP [B]`

- **Signature skill**: Starlit Slumber (ultimate)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Magic `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `average`
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

- **Mehira**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Velara**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, high) `signature fuel`
- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, average, conditional (frequent))
- **Tasi**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Aurora

Aurora provides Haste buff to summons `high`, Invincible to single targets `high`, and Summon damage buff (Mythic+) to summons `low`.

- Zanie (4.0 / 5)
- Florabelle (3.7 / 5)
- Damian (3.5 / 5)
- Phraesto (3.4 / 5)
- Dunlingr (3.1 / 5)
- Mehira (2.2 / 5)

### Units that can act as a replacement for Aurora

**Damage**

- Mehira (100% `Magic`)
- Saida (100% `Magic`)
- Solise (100% `Magic`)

### Summary for Aurora

#### Aurora Provides

- Dream sleep (transformation) — Self
- Invincibility — Multiple targets
- Start-of-battle cast — Multiple targets
- Summoning — Single target

#### Damage types dealt by Aurora

- Magic — Area, Multiple targets, Single target

#### Crowd Control provided by Aurora

- Unaffected — Self — On skill

## Baelran

### Baelran's behavior

`AFK Stages [S]`, `Dream Realm [A]`, `Dream Realm (Endless) [S]`, `PVP [S]`

- **Signature skill**: Celestial Rise (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Damage types**: Physical `high`, True damage `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, heal `average`, buffs `average`, damage `average`
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

Look for units providing: `ATK` `Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Contess**, or **Solise**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Velara**
  - Haste buff (single target, low) `signature fuel`
  - Healing (area, low)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
- **Talene**
  - ATK buff (area, high)
  - Healing (area, low)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, average)

### Units benefitting most from Baelran

- Carolina (3.1 / 5)
- Nerion (2.6 / 5)
- Zorya (1.5 / 5)
### Summary for Baelran

#### Baelran Provides

- Start-of-battle cast — Arc
- Enhanced form (Mythic+) — Area
- Dispel debuffs (EX+15) — Area

#### Damage types dealt by Baelran

- Physical — Arc, Area, Single target
- True damage — Arc, Area — `average`

#### Debuffs provided by Baelran

- Max HP (Supreme+) — Single target — `low`

#### Crowd Control provided by Baelran

- Unaffected — Self — Start of battle
- Knock down — Area — `average`
- Knock up — Single target — `low`

## Berial

### Berial's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Scared Swamp (ultimate)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Magic `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `average`, damage `high`
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
Common buffers are **Rowan**, **Lyca**, or **Twins**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, average, conditional (frequent))
- **Pandora**
  - Healing (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Hepler**
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Koko**
  - Healing (all units, average)

### Units benefitting most from Berial

- Carolina (3.1 / 5)
- Nerion (2.6 / 5)
- Bonnie (1.9 / 5)

### Units that can act as a replacement for Berial

**Damage**

- Aurora (100% `Magic`)
- Bonnie (100% `Magic`)
- Callan (100% `Magic`)

**Debuffs on enemies**

- Pandora (100% `Damage taken debuff` `Energy drain`)
- Cryonaia (72% `Damage taken debuff`)
- Contess (60% `Energy drain`)

**Crowd Control**

- Silvina (80% `Frighten`)
- Daimon (66% `Frighten`)

### Summary for Berial

#### Berial Provides

- Invincibility — Self
- Revive ally — Single target
- Summoning (Mythic+) — Single target

#### Damage types dealt by Berial

- Magic — Area, Single target

#### Debuffs provided by Berial

- Damage taken (Legendary+) — Single target — `low`
- Energy drain (Mythic+) — Single target — `low`

#### Crowd Control provided by Berial

- Frighten — Area — `average`

## Bonnie

### Bonnie's behavior

`AFK Stages [B]`, `Dream Realm [A]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Decay's Reach (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Magic `high`

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, debuffs `average`, damage `high`
- **Ultimate**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `high`

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
Common buffers are **Contess**, **Rowan**, or **Twins**.

Bonnie also requires units **dealing magic damage** and/or units **putting debuffs** on enemies

- **Cyran**
  - Enables Debuff on target via ATK debuff (all units)
  - Enables Magic damage from allies via Magic damage + wide area + all enemies (all units)
- **Frieren**
  - ATK buff (single target, high)
  - Enables Debuff on target via DoT (area)
  - Enables Magic damage from allies via Magic damage + all enemies (all units)
- **Kulu**
  - ATK buff (single target, low)
  - Enables Debuff on target via Damage taken debuff (all units)
- **Alna**
  - ATK buff (single target, average)
  - Enables Debuff on target via Haste debuff (area)
- **Eironn**
  - Enables Debuff on target via Haste debuff (arc)
  - Enables Magic damage from allies via Magic damage (area)

### Units benefitting most from Bonnie

- Indris (2.0 / 5)
- Aliceth (1.7 / 5)
- Nerion (1.6 / 5)

### Units that can act as a replacement for Bonnie

**Damage**

- Aurora (100% `Magic`)
- Cryonaia (100% `Magic`)
- Cyran (100% `Magic`)

**Crowd Control**

- Aliceth (100% `Stun`)
- Contess (100% `Stun`)
- Faramor (100% `Stun`)

### Summary for Bonnie

#### Bonnie Provides

- Invincibility — Self
- Transformation — Self
- Magic damage amplification (Supreme+) — Single target

#### Damage types dealt by Bonnie

- Magic — Area, Single target

#### Debuffs provided by Bonnie

- ATK — Single target — `high`
- Haste — Single target — `high`
- Damage taken (Supreme+) — Single target — `low`

#### Crowd Control provided by Bonnie

- Stun — Single target — `average`

## Brutus

### Brutus's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Indomitable (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Damage types**: Physical `high`, DoT `average`, Max HP-based damage `high`

#### Skill overview

- **Signature skill**: speed `fast`, buffs `average`
- **Ultimate**: speed `slow`, damage `low`
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

- **Kordan**
  - Lifedrain buff (multiple targets, high)
- **Koko**
  - Lifedrain buff (multiple targets, average)
- **Dunlingr**
  - Lifedrain buff (all units, low)
- **Thoran**
  - Lifedrain buff (single target, high)
- **Zandrok**
  - Lifedrain buff (area, low, conditional (frequent))

### Units benefitting most from Brutus

Brutus provides Lifedrain buff to single targets `high`.

- Shadewing (4.2 / 5)
- Aliceth (2.2 / 5)
- Indris (2.1 / 5)

### Units that can act as a replacement for Brutus

**Buffs on allies**

- Dunlingr (100% `Life Drain`)
- Koko (100% `Life Drain`)
- Kordan (100% `Life Drain`)

**Similar Skills**

- Zorya (66% `hp-scaling` `life-drain`)

**Damage**

- Gunnar (100% `Max HP-based damage` `DoT` `Physical`)
- Daimon (96% `Max HP-based damage`)
- Himmel (89% `Max HP-based damage` `Physical`)

**Crowd Control**

- Hepler (100% `Taunt`)

### Summary for Brutus

#### Damage types dealt by Brutus

- Physical — Arc, Single target
- DoT — Area
- Max HP-based damage — Arc, Single target — `high`

#### Debuffs provided by Brutus

- Phys DEF — Area — `average`

#### Crowd Control provided by Brutus

- Immune — Self — On skill
- Unaffected — Self — On skill
- Taunt — Area — `average`

## Bryon

### Bryon's behavior

`AFK Stages [A+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Shadow Flash (Skill 2)
- **Movement**: stationary (summon moves)
- **Damage types**: Magic `high`, DoT `high`

#### Skill overview

- **Signature skill**: speed `slow`, damage `low`
- **Ultimate**: speed `fast`, first cast speed `fast`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, damage `average`

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

Look for units providing: `Haste` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Solise**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, average, conditional (frequent))
- **Koko**
  - Healing (all units, average)
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Velara**
  - Haste buff (single target, low) `signature fuel`
  - Healing (area, low)
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Bryon

- Shadewing (2.8 / 5)
- Bonnie (2.6 / 5)
- Indris (1.6 / 5)

### Units that can act as a replacement for Bryon

**Damage**

- Frieren (100% `DoT` `Magic`)
- Gunnar (72% `DoT`)

**Debuffs on enemies**

- Alna (100% `Haste debuff`)
- Bonnie (100% `Haste debuff`)
- Eironn (100% `Haste debuff`)

**Crowd Control**

- Lily May (100% `Interrupt`)
- Smokey & Meerky (100% `Interrupt`)
- Sylphira (100% `Interrupt`)

### Summary for Bryon

#### Bryon Provides

- Start-of-battle cast — Single target
- Summoning — Self
- Counterattack (EX+10) — Single target

#### Damage types dealt by Bryon

- Magic — Single target
- DoT — Area

#### Debuffs provided by Bryon

- Haste — Area — `low`

#### Crowd Control provided by Bryon

- Interrupt — Single target — `low`

## Callan

### Callan's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Restless Guardian (ultimate)
- **Movement**: moving (avg attack range 1.7 tiles)
- **Damage types**: Magic `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, buffs `average`
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

### Units improving Callan

Look for units providing: `Healing`  
Common buffers are **Smokey & Meerky**, **Mikola**, or **Solise**.

- **Koko**
  - Healing (all units, average)
- **Evie**
  - Healing (single target, high)
- **Velara**
  - Healing (area, low)
- **Pandora**
  - Healing (single target, average)
- **Zanie**
  - Healing (single target, average)

### Units benefitting most from Callan

Callan provides Shield to single targets `average`.

- Carolina (2.3 / 5)
- Nerion (2.2 / 5)
- Perseus (1.4 / 5)

### Units that can act as a replacement for Callan

**Buffs on allies**

- Contess (100% `Max HP`)
- Daimon (100% `Max HP`)
- Galahad (100% `Max HP`)

**Damage**

- Cryonaia (100% `Magic`)
- Cyran (100% `Magic`)
- Daimon (100% `Magic`)

**Crowd Control**

- Baelran (75% `Knock down`)
- Sylphira (62% `Knock down`)

### Summary for Callan

#### Callan Provides

- Damage absorption (allies) — Multiple targets
- Stored damage release — Self

#### Damage types dealt by Callan

- Magic — All units, Single target

#### Crowd Control provided by Callan

- Unaffected — Self — Start of battle
- Knock down — All units — `low`
- Stun (Mythic+) — Single target — `average`

## Carolina

### Carolina's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Frozen Grave (ultimate)
- **Movement**: mostly stationary (avg attack range 4.0 tiles)
- **Damage types**: Magic `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `average`

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
Common buffers are **Twins**, **Lyca**, or **Damian**.

Carolina also requires units **applying crowd control** to enemies

- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Enables CC on enemies via Blind (area, high)
- **Antandra**
  - Enables CC on enemies via Stun (area, high)
- **Kordan**
  - Enables CC on enemies via Bind (area, high)
- **Lorsan**
  - Enables CC on enemies via Stun (multiple targets, high)
- **Aliceth**
  - Enables CC on enemies via Blind (area, average)

### Units benefitting most from Carolina

Carolina provides DEF buff (Mythic+) to single targets `average`.

- Bonnie (2.7 / 5)
- Indris (2.2 / 5)
- Nerion (1.9 / 5)

### Units that can act as a replacement for Carolina

**Buffs on allies**

- Fay (100% `Magic DEF` `Physical DEF`)
- Lucca (100% `Magic DEF` `Physical DEF`)
- Lumont (100% `Magic DEF` `Physical DEF`)

**Similar Skills**

- Kruger (60% `enemy-debuffer`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Debuffs on enemies**

- Eironn (100% `Haste debuff` `Magic DEF debuff`)
- Bonnie (72% `Haste debuff`)
- Kafra (60% `Haste debuff`)

**Crowd Control**

- Alna (100% `Bind`)
- Evie (100% `Bind`)
- Kordan (100% `Bind`)

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

`AFK Stages [C]`, `Dream Realm [A+]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Tidal Strength (Skill 2)
- **Movement**: stationary (avg attack range 10.0 tiles)
- **Ally composition**: nearest ally auto-selected at battle start; prioritizes ally behind
- **Damage types**: Magic `high`

#### Skill overview

- **Signature skill**: speed `slow`, first cast speed `fast`, damage `low`
- **Ultimate**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, damage `average`

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
Common buffers are **Twins**, **Hugin**, or **Galahad**.

Cassadee also requires a unit **to bless**

- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Isabella**
  - Haste buff (multiple targets, low) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Dunlingr**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Marcille**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Cassadee

- Carolina (2.3 / 5)
- Bonnie (2.1 / 5)
- Nerion (2.0 / 5)

### Units that can act as a replacement for Cassadee

**Damage**

- Callan (100% `Magic`)
- Cryonaia (100% `Magic`)
- Cyran (100% `Magic`)

**Debuffs on enemies**

- Eironn (100% `Magic DEF debuff`)
- Indris (100% `Magic DEF debuff`)
- Shadewing (100% `Magic DEF debuff`)

**Crowd Control**

- Scarlita (100% `Knock back` `Knock up` `Stun`)
- Perseus (97% `Knock back` `Stun`)
- Lenya (81% `Knock back` `Stun`)

### Summary for Cassadee

#### Cassadee Provides

- Ally blessing — Single target

#### Damage types dealt by Cassadee

- Magic — All units, Single target

#### Debuffs provided by Cassadee

- Magic DEF (Supreme+) — Single target — `low`

#### Crowd Control provided by Cassadee

- Knock back — All units — `low`
- Knock up — Single target — `low`
- Stun — Single target — `low`

## Cecia

### Cecia's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Queen's Summons (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Damage types**: Physical `average`, DoT `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `low`

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
Common buffers are **Twins**, **Lyca**, or **Rowan**.

- **Lucca**
  - DEF buff (area, high)
  - DEF buff (area, high)
- **Lumont**
  - DEF buff (multiple targets, high)
  - DEF buff (multiple targets, high)
- **Tilaya**
  - DEF buff (area, average)
  - DEF buff (area, average)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, average, conditional (frequent))

### Units benefitting most from Cecia

Cecia provides ATK SPD buff to single targets `high`, DEF Penetration buff to single targets `low`, Lifedrain buff in an area `high`, and Max HP buff to single targets `high`.

- Shadewing (4.2 / 5)
- Silven (3.0 / 5)
- Perseus (2.8 / 5)

### Units that can act as a replacement for Cecia

**Similar Skills**

- Viperian (72% `dot-specialist` `life-drain`)

**Damage**

- Gunnar (100% `Physical` `DoT`)
- Brutus (85% `DoT` `Physical`)
- Aliceth (68% `Physical`)

**Crowd Control**

- Alna (100% `Bind`)
- Arden (100% `Bind`)
- Atalanta (100% `Bind`)

### Summary for Cecia

#### Cecia Provides

- Summoning — Self

#### Damage types dealt by Cecia

- Physical — Arc, Area, Single target
- DoT — Arc, Single target

#### Crowd Control provided by Cecia

- Bind — Single target — `average`

## Chippy

### Chippy's behavior

- **Signature skill**: Brothers-in-arms (ultimate)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Physical `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `average`
- **Non-ultimate**: speed `average`, damage `low`

##### Ultimate

summon two companion units to join the battle

##### Skill 1

leap at single target, dealing damage

##### Skill 2

rare chance for massive single normal attack damage

### Units improving Chippy

- **Pandora**
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Thador**
  - Energy recovery (lieutenant, start of battle) `signature fuel`
- **Tasi**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Chippy

- Himmel (1.6 / 5)

### Units that can act as a replacement for Chippy

**Similar Skills**

- Florabelle (100% `summoner`)
- Zanie (100% `summoner`)
- Dunlingr (60% `summoner`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

### Summary for Chippy

#### Damage types dealt by Chippy

- Physical — Single target

## Contess

### Contess's behavior

`AFK Stages [C]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S+]`, `PVP [S]`

- **Signature skill**: Detention Pass (ultimate)
- **Movement**: stationary (no finite attack range)
- **Damage types**: Magic `low`

#### Skill overview

- **Signature skill (ultimate)**: speed `average`, first cast speed `fast`, heal `average`, buffs `average`
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
Common buffers are **Solise**, **Twins**, or **Smokey & Meerky**.

- **Velara**
  - Healing (area, low)
- **Hewynn**
  - Healing (all units, average)
- **Koko**
  - Healing (all units, average)
- **Lorsan**
  - Healing (all units, average)
- **Hepler**
  - Healing (multiple targets, high)

### Units benefitting most from Contess

Contess provides ATK buff to single targets `high`, Healing to multiple targets `high`, and Shield to single targets `average`.

**27** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Talene (3.6 / 5)
- Himmel (3.5 / 5)
- Baelran (3.2 / 5)
- Smokey & Meerky (3.2 / 5)
- Alna (3.0 / 5)
- Kordan (3.0 / 5)
- Isabella (2.8 / 5)
- Silven (2.7 / 5)
- Aliceth (2.6 / 5)
- Sylphira (2.1 / 5)

### Units that can act as a replacement for Contess

**Buffs on allies**

- Twins (96% `ATK` `Max HP`)

**Healing**

- Solise (100% `Healing`)

**Damage**

- Saida (100% `Magic`)
- Silven (100% `Magic`)
- Solise (100% `Magic`)

**Crowd Control**

- Gwyneth (93% `Silence` `Stun`)

### Summary for Contess

#### Contess Provides

- Start-of-battle cast — All units

#### Debuffs provided by Contess

- Energy drain — Single target — `low`
- ATK (Legendary+) — Single target — `low`

#### Crowd Control provided by Contess

- Untargetable — Multiple targets — Start of battle
- Silence (Mythic+) — Single target — `high`
- Stun (Supreme+) — Single target — `average`

## Cryonaia

### Cryonaia's behavior

`AFK Stages [B]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [S]`

- **Signature skill**: Frostveil Domain (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Damage types**: Magic `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `average`, damage `high`
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

Look for units providing: `ATK` `Max HP`  
Common buffers are **Twins**, **Hugin**, or **Ravion**.

- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - ATK buff (single target, low)
  - Max HP via Shield (single target, high)
- **Gunnar**
  - ATK buff (single target, low)
  - ATK SPD buff (single target, high) `signature fuel`
- **Alna**
  - ATK buff (single target, average)
  - Max HP buff (single target, low)

### Units benefitting most from Cryonaia

- Bonnie (2.4 / 5)
- Niru (1.7 / 5)
- Himmel (1.6 / 5)

### Units that can act as a replacement for Cryonaia

**Similar Skills**

- Alna (75% `battlefield-modification` `cc-immunity` `invincibility`)

**Damage**

- Cyran (100% `Magic`)
- Frieren (100% `Magic`)
- Galahad (100% `Magic`)

**Debuffs on enemies**

- Kulu (100% `Damage taken debuff`)
- Mehira (100% `Damage taken debuff`)

### Summary for Cryonaia

#### Cryonaia Provides

- Enemy isolation (domain) — All units
- Battle time pause (EX+15) — Self
- Instant defeat (Supreme+) — Self

#### Damage types dealt by Cryonaia

- Magic — All units, Area, Single target

#### Debuffs provided by Cryonaia

- Damage taken (EX+5) — Single target — `low`

#### Crowd Control provided by Cryonaia

- Immune — Self — Conditional

## Cyran

### Cyran's behavior

`AFK Stages [S]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Gravitic Requiem (ultimate)
- **Movement**: mostly stationary (avg attack range 6.0 tiles)
- **Damage types**: Magic `high`, True damage `low`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
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
Common buffers are **Twins**, **Hugin**, or **Ravion**.

- **Gunnar**
  - ATK buff (single target, low)
  - ATK SPD buff (single target, high) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Velara**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
- **Tasi**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Cyran

- Bonnie (5.0 / 5)

### Units that can act as a replacement for Cyran

**Damage**

- Frieren (100% `Magic` `True damage`)
- Baelran (80% `True damage`)
- Faramor (80% `True damage`)

### Summary for Cyran

#### Cyran Provides

- Artifact mimic (Mythic+) — All units
- Enemy artifact block (EX+10) — Single target

#### Damage types dealt by Cyran

- Magic — All units, Area, Single target
- True damage — All units — `low`

#### Debuffs provided by Cyran

- ATK (Mythic+) — All units — `high`

#### Crowd Control provided by Cyran

- Steadfast — Area — Conditional
- Unaffected — Self — Start of battle
- Bind — Single target — `low`
- Displace — All units — `low`
- Silence (EX+10) — Single target — `high`

## Daimon

### Daimon's behavior

`AFK Stages [B]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Buddy Barrier (Skill 2)
- **Movement**: stationary (no finite attack range)
- **Ally composition**: place ally directly behind at battle prep (shield share, Life Drain, and ATK bond)
- **Damage types**: Magic `low`, Max HP-based damage `average`

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

Look for units providing: `Max HP`  
Common buffers are **Hugin**, **Galahad**, or **Contess**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
- **Hepler**
  - Max HP via Shield (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, average)
- **Koko**
  - Max HP via Shield (all units, low)

### Units benefitting most from Daimon

Daimon provides Lifedrain buff to single targets `average` and Shield to multiple targets `low`.

- Carolina (3.1 / 5)
- Nerion (2.8 / 5)
- Perseus (1.5 / 5)

### Units that can act as a replacement for Daimon

**Buffs on allies**

- Thoran (72% `Life Drain`)
- Dunlingr (60% `Life Drain`)

**Similar Skills**

- Shemira (72% `hp-scaling` `life-drain` `summoner`)

**Damage**

- Gunnar (100% `Max HP-based damage`)
- Shemira (100% `Max HP-based damage` `Magic`)
- Himmel (86% `Max HP-based damage`)

### Summary for Daimon

#### Damage types dealt by Daimon

- Magic — Area
- Max HP-based damage — Area — `average`

#### Crowd Control provided by Daimon

- Frighten (Mythic+) — Area — `average`

## Damian

### Damian's behavior

`AFK Stages [C]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Inventor's Will (Mythic+)
- **Movement**: stationary (off battlefield)
- **Damage types**: Magic `high`

#### Skill overview

- **Signature skill**: speed `fast`, heal `average`, buffs `average`
- **Ultimate**: speed `slow`, first cast speed `fast`, buffs `average`, damage `high`
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
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, average, conditional (frequent))
- **Isabella**
  - ATK buff (multiple targets, low, conditional (frequent))
  - Haste buff (multiple targets, low) `signature fuel`
- **Tasi**
  - Haste buff (single target, high) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Damian

Damian provides Healing in an area `average` and Haste buff (Mythic+) to multiple targets `high` — conditional (frequent).

**22** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Twins (5.0 / 5)
- Viperian (3.6 / 5)
- Atalanta (3.5 / 5)
- Lorsan (3.3 / 5)
- Lumont (3.3 / 5)
- Soren (3.2 / 5)
- Vala (3.2 / 5)
- Seth (3.1 / 5)
- Tasi (3.0 / 5)
- Laios (2.9 / 5)

### Units that can act as a replacement for Damian

**Buffs on allies**

- Hugin (100% `Haste`)
- Shakir (100% `Haste`)
- Twins (100% `Haste`)

**Healing**

- Contess (100% `Healing`)
- Hepler (100% `Healing`)
- Koko (100% `Healing`)

**Similar Skills**

- Laios (66% `ally-healer` `summoner`)
- Florabelle (60% `summoner`)

**Damage**

- Callan (100% `Magic`)
- Cassadee (100% `Magic`)
- Cryonaia (100% `Magic`)

**Crowd Control**

- Hepler (100% `Blind` `Stun`)
- Aliceth (83% `Blind` `Stun`)
- Koko (60% `Stun`)

### Summary for Damian

#### Damian Provides

- Summoning — All units

#### Damage types dealt by Damian

- Magic — All units, Single target

#### Crowd Control provided by Damian

- Blind — Single target — `high`
- Stun — Single target — `high`

## Dionel

### Dionel's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Dawn Light (ultimate)
- **Movement**: moving (avg attack range 0.0 tiles)
- **Damage types**: Physical `average`, True damage `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `average`
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

Look for units providing: `ATK SPD / Haste` `Max HP` `Execution`  
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Pandora**
  - Max HP buff (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, low)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Dionel

Dionel provides ATK buff to single targets `low`.

- Indris (1.5 / 5)
- Aliceth (1.4 / 5)
- Nerion (1.3 / 5)

### Units that can act as a replacement for Dionel

**Buffs on allies**

- Aliceth (100% `ATK`)
- Alna (100% `ATK`)
- Contess (100% `ATK`)

**Damage**

- Athalia (100% `Physical` `True damage`)
- Baelran (100% `True damage` `Physical`)
- Faramor (100% `True damage` `Physical`)

**Debuffs on enemies**

- Alna (100% `Vitality debuff`)
- Faramor (100% `Vitality debuff`)
- Frieren (100% `Vitality debuff`)

**Crowd Control**

- Florabelle (100% `Knock up`)
- Kulu (100% `Knock up`)
- Zandrok (100% `Knock up`)

### Summary for Dionel

#### Dionel Provides

- Stacking buff — Single target
- Execution scaling (Supreme+) — Self

#### Damage types dealt by Dionel

- Physical — All units, Area, Single target
- True damage — All units — `average`

#### Debuffs provided by Dionel

- Vitality (Mythic+) — Single target — `low`

#### Crowd Control provided by Dionel

- Untargetable — Area — On skill
- Knock up — Single target — `low`

## Dunlingr

### Dunlingr's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S+]`

- **Signature skill**: Echo of Silence (ultimate)
- **Movement**: stationary (avg attack range 6.4 tiles)
- **Damage types**: Magic `average`, HP loss `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, heal `average`, damage `average`
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

Look for units providing: `ATK SPD / Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Solise**, or **Hugin**.

- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, average, conditional (frequent))
  - Max HP via Shield (summons only, average)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
  - Healing (single target, average)
- **Velara**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Healing (area, low)

### Units benefitting most from Dunlingr

Dunlingr provides ATK buff (EX+5) to single targets `low`, Haste buff (EX+15) to single targets `low`, ATK SPD buff (Supreme+) to all units `low`, and Lifedrain buff (Supreme+) to all units `low`.

- Brutus (2.7 / 5)

### Units that can act as a replacement for Dunlingr

**Damage**

- Aliceth (90% `HP loss`)
- Niru (84% `Magic` `HP loss`)
- Faramor (75% `HP loss`)

**Debuffs on enemies**

- Rowan (69% `Energy drain`)

**Crowd Control**

- Contess (66% `Silence`)
- Cyran (66% `Silence`)

### Summary for Dunlingr

#### Dunlingr Provides

- Summoning — Self
- Ultimate lock (Spellbind) — All units

#### Damage types dealt by Dunlingr

- Magic — All units, Area, Single target
- HP loss — Area — `average`

#### Debuffs provided by Dunlingr

- ATK — Single target — `low`
- Energy drain (Supreme+) — All units — `low`

#### Crowd Control provided by Dunlingr

- Silence — Single target — `high`

## Eironn

### Eironn's behavior

`AFK Stages [S+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Verdant Cyclone (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Damage types**: Magic `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `average`
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

Look for units providing: `Max HP` `Physical DEF`  
Common buffers are **Rowan**, **Twins**, or **Hugin**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Thador**
  - Energy recovery (lieutenant, start of battle) `signature fuel`
- **Zanie**
  - Max HP via Shield (single target, high)
- **Velara**
  - DEF buff (single target, average)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Isabella**
  - DEF buff (single target, low)
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`

### Units benefitting most from Eironn

- Bonnie (3.4 / 5)

### Units that can act as a replacement for Eironn

**Damage**

- Aurora (100% `Magic`)
- Cryonaia (100% `Magic`)
- Cyran (100% `Magic`)

**Debuffs on enemies**

- Alna (75% `Haste debuff`)

**Crowd Control**

- Cyran (85% `Displace` `Bind`)

### Summary for Eironn

#### Damage types dealt by Eironn

- Magic — Arc, Area, Single target

#### Debuffs provided by Eironn

- Haste — Arc — `high`
- Magic DEF — Single target — `average`

#### Crowd Control provided by Eironn

- Bind — Single target — `high`
- Displace — Area — `low`

## Evie

### Evie's behavior

`AFK Stages [B]`, `Dream Realm [B]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Intel Chase (ultimate)
- **Movement**: high movement (repositioning skills)
- **Ally composition**: rearmost ally starts with healing quill; tracks highest damage dealer
- **Damage types**: Magic `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, buffs `average`, debuffs `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, damage `high`

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

Look for units providing: `Healing`  
Common buffers are **Smokey & Meerky**, **Mikola**, or **Solise**.

- **Koko**
  - Healing (all units, average)
- **Velara**
  - Healing (area, low)
- **Pandora**
  - Healing (single target, average)
- **Zanie**
  - Healing (single target, average)
- **Hewynn**
  - Healing (all units, average)

### Units benefitting most from Evie

Evie provides ATK buff to multiple targets `high` and Healing to single targets `high`.

- Smokey & Meerky (3.2 / 5)

### Units that can act as a replacement for Evie

**Buffs on allies**

- Hugin (100% `ATK`)
- Kordan (100% `ATK`)
- Mikola (100% `ATK`)

**Healing**

- Contess (100% `Healing`)
- Koko (100% `Healing`)
- Rowan (100% `Healing`)

**Damage**

- Callan (100% `Magic`)
- Cryonaia (100% `Magic`)
- Cyran (100% `Magic`)

**Debuffs on enemies**

- Frieren (100% `DoT`)
- Gwyneth (100% `DoT`)

**Crowd Control**

- Gwyneth (64% `Bind` `Silence`)
- Cyran (62% `Silence` `Displace` `Bind`)

### Summary for Evie

#### Evie Provides

- Invincibility — Self
- Start-of-battle cast — All units

#### Damage types dealt by Evie

- Magic — All units, Single target

#### Debuffs provided by Evie

- DoT — Single target — `average`

#### Crowd Control provided by Evie

- Bind — Single target — `high`
- Displace — Single target — `low`
- Silence — Single target — `high`

## Faramor

### Faramor's behavior

`AFK Stages [S]`, `Dream Realm [S]`, `Dream Realm (Endless) [A+]`, `PVP [B]`

- **Signature skill**: Sanctified Circle (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Ally composition**: bless adjacent ally at battle prep; prioritizes tile behind
- **Damage types**: Physical `high`, HP loss `high`, True damage `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `average`, damage `high`
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

Look for units providing: `ATK` `Haste` `Max HP`  
Common buffers are **Twins**, **Hugin**, or **Galahad**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - ATK buff (single target, low)
  - Max HP via Shield (single target, high)
- **Mehira**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Velara**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, high) `signature fuel`

### Units benefitting most from Faramor

- Carolina (2.0 / 5)
- Nerion (1.8 / 5)
- Indris (1.3 / 5)

### Units that can act as a replacement for Faramor

**Crowd Control**

- Gwyneth (100% `Stun`)
- Contess (75% `Stun`)

### Summary for Faramor

#### Faramor Provides

- Revive ally (Supreme+) — Single target

#### Damage types dealt by Faramor

- Physical — Area, Multiple targets, Single target
- HP loss — Single target — `high`
- True damage — Multiple targets — `high`

#### Debuffs provided by Faramor

- Vitality (Supreme+) — Single target — `low`

#### Crowd Control provided by Faramor

- Stun — Area — `low`

## Fay

### Fay's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [B]`, `PVP [B]`

- **Signature skill**: Vibrant Dance (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Damage types**: Magic `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `average`, buffs `average`
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

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Tasi**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
- **Pandora**
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, high) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Fay

Fay provides ATK SPD buff to multiple targets `low`, ATK buff to multiple targets `low`, DEF buff to multiple targets `low`, Healing to arc `average` — conditional (frequent), and Vitality buff (EX+5) to single targets `low`.

- Indris (2.5 / 5)
- Silven (2.5 / 5)
- Perseus (2.3 / 5)

### Units that can act as a replacement for Fay

**Buffs on allies**

- Sonja (82% `ATK` `Magic DEF` `Physical DEF`)
- Twins (68% `ATK` `Magic DEF` `Physical DEF` `Vitality buff`)

**Healing**

- Contess (100% `Healing`)
- Damian (100% `Healing`)
- Evie (100% `Healing`)

**Similar Skills**

- Ludovic (100% `ally-healer` `aoe-healing`)
- Smokey & Meerky (100% `ally-healer` `aoe-healing`)
- Solise (80% `ally-healer` `aoe-healing`)

**Damage**

- Aurora (100% `Magic`)
- Bonnie (100% `Magic`)
- Callan (100% `Magic`)

**Debuffs on enemies**

- Velara (90% `Magic DEF debuff` `Phys DEF debuff`)
- Indris (75% `Phys DEF debuff` `Magic DEF debuff`)
- Shadewing (75% `Magic DEF debuff` `Phys DEF debuff`)

### Summary for Fay

#### Damage types dealt by Fay

- Magic — Area, Single target

#### Debuffs provided by Fay

- Magic DEF — Multiple targets — `low`
- Phys DEF — Multiple targets — `low`

## Florabelle

### Florabelle's behavior

`AFK Stages [B]`, `Dream Realm [S]`, `Dream Realm (Endless) [S]`, `PVP [B]`

- **Signature skill**: Pounding Blow (ultimate)
- **Movement**: stationary (no finite attack range)
- **Damage types**: Physical `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, damage `high`
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
Common buffers are **Twins**, **Hugin**, or **Galahad**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Mehira**
  - Haste buff (single target, low) `signature fuel`
- **Velara**
  - Haste buff (single target, low) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, low, conditional (frequent))
  - Haste buff (multiple targets, low) `signature fuel`
- **Tasi**
  - Haste buff (single target, high) `signature fuel`

### Units benefitting most from Florabelle

Florabelle provides Lifedrain buff to summons `average` — conditional (frequent), Shield (Mythic+) to summons `average`, Haste buff (EX+10) to summons `average` — conditional (frequent), and Summon damage buff (Supreme+) to summons `average`.

- Dunlingr (3.6 / 5)
- Damian (3.1 / 5)
- Phraesto (3.1 / 5)

### Units that can act as a replacement for Florabelle

**Similar Skills**

- Zanie (100% `summoner`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

### Summary for Florabelle

#### Florabelle Provides

- Summoning — Self

#### Damage types dealt by Florabelle

- Physical — Area, Single target

#### Crowd Control provided by Florabelle

- Immune (Supreme+) — Self — Form
- Knock up — Area — `low`

## Frieren

### Frieren's behavior

`AFK Stages [B]`, `Dream Realm [B]`, `Dream Realm (Endless) [S+]`, `PVP [A+]`

- **Signature skill**: Zoltraak (ultimate)
- **Movement**: stationary (avg attack range 7.0 tiles)
- **Ally composition**: frontmost ally shares damage reduction with this hero
- **Damage types**: Magic `high`, DoT `high`, True damage `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
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
Common buffers are **Twins**, **Hugin**, or **Ravion**.

- **Gunnar**
  - ATK buff (single target, low)
  - ATK SPD buff (single target, high) `signature fuel`
- **Mehira**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Velara**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Tasi**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Frieren

Frieren provides ATK buff to single targets `high`.

- Bonnie (4.7 / 5)
- Indris (3.5 / 5)

### Units that can act as a replacement for Frieren

**Buffs on allies**

- Aliceth (100% `ATK`)
- Contess (100% `ATK`)
- Hugin (100% `ATK`)

**Damage**

- Faramor (91% `True damage`)
- Athalia (82% `True damage`)
- Baelran (74% `True damage`)

**Crowd Control**

- Silven (80% `Knock down`)
- Sylphira (80% `Knock down`)
- Baelran (66% `Knock down`)

### Summary for Frieren

#### Damage types dealt by Frieren

- Magic — All units, Area, Single target
- DoT — All units, Single target
- True damage — All units, Single target — `high`

#### Debuffs provided by Frieren

- DoT — Area — `high`
- Vitality — Single target — `low`

#### Crowd Control provided by Frieren

- Stun — Single target — `low`
- Knock down (Supreme+) — Single target — `average`

## Galahad

### Galahad's behavior

`AFK Stages [S]`, `Dream Realm [B]`, `Dream Realm (Endless) [S+]`, `PVP [A]`

- **Signature skill**: Time Recast (Mythic+)
- **Movement**: stationary (avg attack range 10.0 tiles)
- **Ally composition**: nearest ally auto-selected at battle start; prioritizes ally behind
- **Damage types**: Magic `high`

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`
- **Ultimate**: speed `average`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `high`

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
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Mehira**
  - Haste buff (single target, low) `signature fuel`
- **Velara**
  - Haste buff (single target, low) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, low, conditional (frequent))
  - Haste buff (multiple targets, low) `signature fuel`
- **Tasi**
  - Haste buff (single target, high) `signature fuel`
- **Vala**
  - Haste buff (single target, high) `signature fuel`

### Units benefitting most from Galahad

Galahad provides Haste buff to single targets `high` and Shield to single targets `high`.

**24** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Sonja (2.7 / 5)
- Himmel (2.6 / 5)
- Dionel (2.4 / 5)
- Faramor (2.3 / 5)
- Cassadee (2.2 / 5)
- Koko (2.1 / 5)
- Frieren (2.0 / 5)
- Natsu (2.0 / 5)
- Ravion (2.0 / 5)
- Cyran (2.0 / 5)

### Units that can act as a replacement for Galahad

**Buffs on allies**

- Hugin (100% `Haste` `Max HP`)
- Twins (66% `Haste` `Max HP`)
- Saida (60% `Max HP`)

**Damage**

- Saida (100% `Magic`)
- Shemira (100% `Magic`)
- Solise (100% `Magic`)

**Crowd Control**

- Gwyneth (100% `Bind`)
- Velara (100% `Bind`)

### Summary for Galahad

#### Galahad Provides

- Artifact amplification (EX+10) — Single target

#### Damage types dealt by Galahad

- Magic — All units, Area, Single target

#### Crowd Control provided by Galahad

- Steadfast (Supreme+) — Self — On skill
- Bind — Single target — `average`

## Gerda

### Gerda's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Spring Therapy (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Physical `average`

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, heal `average`, damage `average`
- **Ultimate**: speed `slow`, heal `average`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, damage `average`

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

Look for units providing: `Max HP`  
Common buffers are **Hugin**, **Galahad**, or **Contess**.

- **Hepler**
  - Max HP via Shield (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Koko**
  - Max HP via Shield (all units, low)
- **Lenya**
  - Max HP via Shield (single target, high)
- **Zanie**
  - Max HP via Shield (single target, high)

### Units benefitting most from Gerda

Gerda provides Healing to multiple targets `low` and Healing over time in an area `low`.

- Nerion (1.6 / 5)
- Silven (1.5 / 5)
- Perseus (1.4 / 5)

### Units that can act as a replacement for Gerda

**Healing**

- Mikola (100% `Healing over time` `Healing`)
- Solise (100% `Healing over time` `Healing`)
- Talene (100% `Healing over time` `Healing`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

### Summary for Gerda

#### Damage types dealt by Gerda

- Physical — Area, Multiple targets, Single target

#### Crowd Control provided by Gerda

- Unaffected — Self — Start of battle
- Bind — Single target — `low`
- Interrupt — Area — `low`
- Stun — Single target — `average`

## Granny Dahnie

### Granny Dahnie's behavior

`AFK Stages [C]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Threshold of Jade (ultimate)
- **Movement**: moving (avg attack range 2.0 tiles)
- **Damage types**: Physical `low`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `average`
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
Common buffers are **Rowan**, **Twins**, or **Smokey & Meerky**.

- **Tilaya**
  - DEF buff (area, average)
  - DEF buff (area, average)
- **Hepler**
  - Healing (multiple targets, high)
  - DEF buff (single target, low)
  - DEF buff (single target, low)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Fay**
  - Healing (arc, average, conditional (frequent))
  - DEF buff (multiple targets, low)
  - DEF buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`
- **Sonja**
  - DEF buff (multiple targets, average)
  - DEF buff (multiple targets, average)
- **Velara**
  - Healing (area, low)
  - DEF buff (single target, average)
  - DEF buff (single target, average)
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Granny Dahnie

- Carolina (1.8 / 5)
- Indris (1.6 / 5)
- Nerion (1.6 / 5)

### Units that can act as a replacement for Granny Dahnie

**Similar Skills**

- Brutus (80% `hp-scaling` `taunt`)
- Tilaya (72% `hp-scaling`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Debuffs on enemies**

- Bonnie (100% `Haste debuff` `ATK debuff`)
- Alna (80% `Haste debuff`)
- Bryon (80% `Haste debuff`)

**Crowd Control**

- Alna (72% `Bind`)
- Eironn (72% `Bind`)
- Indris (72% `Bind`)

### Summary for Granny Dahnie

#### Damage types dealt by Granny Dahnie

- Physical — Single target

#### Debuffs provided by Granny Dahnie

- Haste — Single target — `average`
- ATK (Supreme+) — Single target — `low`

#### Crowd Control provided by Granny Dahnie

- Unaffected — Self — On skill
- Bind — Single target — `average`
- Taunt — Single target — `average`

## Gunnar

### Gunnar's behavior

`AFK Stages [S+]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S+]`, `PVP [S]`

- **Signature skill**: Annihilation Directive (ultimate)
- **Movement**: stationary (no finite attack range)
- **Ally composition**: place ally 1 tile behind at battle start (Doomfield buffs and coordinated attacks)
- **Damage types**: Physical `average`, DoT `high`, Max HP-based damage `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, buffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `average`

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

Look for units providing: `ATK SPD / Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Damian**.

- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, average)
- **Hewynn**
  - Healing (all units, average)
- **Lorsan**
  - Healing (all units, average)
- **Cecia**
  - ATK SPD buff (single target, high) `signature fuel`
  - Max HP buff (single target, high)

### Units benefitting most from Gunnar

Gunnar provides ATK SPD buff to single targets `high`, ATK buff to single targets `low`, Ranged DEF buff (Legendary+) to single targets `low`, and Vitality buff (Legendary+) to single targets `low`.

- Silven (2.2 / 5)
- Shadewing (2.0 / 5)
- Zanie (2.0 / 5)
- Cyran (1.9 / 5)
- Gwyneth (1.9 / 5)
- Solise (1.9 / 5)
- Kulu (1.7 / 5)
- Twins (1.5 / 5)
- Frieren (1.4 / 5)
- Aurora (1.3 / 5)

### Units that can act as a replacement for Gunnar

**Buffs on allies**

- Dunlingr (80% `ATK SPD` `ATK`)
- Fay (66% `ATK SPD` `ATK` `Vitality buff`)

**Damage**

- Brutus (100% `Max HP-based damage` `DoT` `Physical`)
- Daimon (93% `Max HP-based damage`)
- Himmel (91% `Max HP-based damage` `Physical`)

**Crowd Control**

- Aliceth (100% `Stun`)
- Alsa (100% `Stun`)
- Antandra (100% `Stun`)

### Summary for Gunnar

#### Gunnar Provides

- Invincibility (EX+15) — Single target

#### Damage types dealt by Gunnar

- Physical — All units, Area, Single target
- DoT — Area
- Max HP-based damage — All units — `average`

#### Crowd Control provided by Gunnar

- Stun — Single target — `low`

## Gwyneth

### Gwyneth's behavior

`AFK Stages [A]`, `Dream Realm [S+]`, `Dream Realm (Endless) [?]`, `PVP [S]`

- **Signature skill**: Hailing Arrows (ultimate)
- **Movement**: stationary (avg attack range 8.0 tiles)
- **Damage types**: Physical `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
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
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Gunnar**
  - ATK SPD buff (single target, high) `signature fuel`
- **Velara**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Tasi**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Gwyneth

- Shadewing (2.9 / 5)
- Nerion (1.8 / 5)
- Indris (1.7 / 5)

### Units that can act as a replacement for Gwyneth

**Damage**

- Gunnar (100% `Physical`)

### Summary for Gwyneth

#### Damage types dealt by Gwyneth

- Physical — Area, Single target

#### Debuffs provided by Gwyneth

- DoT — Single target — `high`

#### Crowd Control provided by Gwyneth

- Bind — Single target — `average`
- Silence — Area — `low`
- Stun — Area — `low`

## Hammie

### Hammie's behavior

- **Signature skill**: Pretty Fireball (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Damage types**: Magic `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `average`
- **Non-ultimate**: speed `average`, heal `average`, buffs `average`

##### Ultimate

single-target fireball dealing damage

##### Skill 1

heal weakest ally and buff them

##### Skill 2

self-heal

### Units improving Hammie

Look for units providing: `ATK` `Healing`  
Common buffers are **Mikola**, **Twins**, or **Rowan**.

- **Talene**
  - ATK buff (area, high)
  - Healing (area, low)
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (single target, high)
- **Pandora**
  - Healing (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Hepler**
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, average, conditional (frequent))
  - ATK SPD buff (multiple targets, low) `signature fuel`

### Units benefitting most from Hammie

Hammie provides ATK buff to multiple targets `low`.

- Bonnie (2.0 / 5)
- Himmel (1.9 / 5)
- Silven (1.2 / 5)

### Units that can act as a replacement for Hammie

**Buffs on allies**

- Aliceth (100% `ATK`)
- Alna (100% `ATK`)
- Contess (100% `ATK`)

**Similar Skills**

- Isabella (80% `ally-buffer` `ally-healer`)
- Laios (66% `ally-buffer` `ally-healer`)
- Perseus (60% `ally-buffer`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

### Summary for Hammie

#### Damage types dealt by Hammie

- Magic — Single target

## Harak

### Harak's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [A+]`, `PVP [B]`

- **Signature skill**: Flesh Feast (Skill 2)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Physical `low`, HP loss `low`

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`
- **Ultimate**: speed `slow`, heal `average`, damage `low`
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
Common buffers are **Twins**, **Hugin**, or **Smokey & Meerky**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, average)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
- **Zanie**
  - Max HP via Shield (single target, high)
  - Healing (single target, average)
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, low)

### Units benefitting most from Harak

Harak provides Invincible to single targets `high` and Lifedrain buff (Legendary+) to single targets `low`.

- Silven (1.4 / 5)
- Perseus (1.4 / 5)
- Nerion (1.3 / 5)

### Units that can act as a replacement for Harak

**Buffs on allies**

- Aurora (75% `Invincible`)
- Pandora (75% `Invincible`)

**Damage**

- Aliceth (100% `Physical` `HP loss`)
- Faramor (100% `Physical` `HP loss`)
- Kordan (100% `Physical` `HP loss`)

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

#### Damage types dealt by Harak

- Physical — Single target
- HP loss — Single target — `low`

#### Debuffs provided by Harak

- Execution — Single target — `low`

#### Crowd Control provided by Harak

- Unaffected — Self — Start of battle
- Knock down — Single target — `low`

## Hepler

### Hepler's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Form Shift (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Ally composition**: frontmost adjacent ally gets fatal-blow protection
- **Damage types**: Physical `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
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

Look for units providing: `ATK` `Haste` `Max HP` `Healing` `Physical DEF`  
Common buffers are **Twins**, **Rowan**, or **Mikola**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Sonja**
  - ATK buff (multiple targets, high)
  - DEF buff (multiple targets, average)
  - DEF buff (multiple targets, average)
- **Talene**
  - ATK buff (area, high)
  - Healing (area, low)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, average)
- **Velara**
  - Haste buff (single target, low) `signature fuel`
  - Healing (area, low)
  - DEF buff (single target, average)
  - DEF buff (single target, average)
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Hepler

Hepler provides Haste buff to single targets `low`, Healing to multiple targets `high`, Shield to multiple targets `high`, and DEF buff (Supreme+) to single targets `low`.

**15** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Saida (5.0 / 5)
- Salazer (5.0 / 5)
- Tilaya (5.0 / 5)
- Lucca (4.7 / 5)
- Carolina (4.3 / 5)
- Nerion (4.2 / 5)
- Talene (3.9 / 5)
- Gunnar (3.9 / 5)
- Antandra (3.5 / 5)
- Lumont (2.8 / 5)

### Units that can act as a replacement for Hepler

**Buffs on allies**

- Hugin (87% `Max HP` `Haste`)
- Saida (75% `Max HP`)
- Galahad (60% `Max HP` `Haste`)

**Healing**

- Contess (100% `Healing`)
- Koko (100% `Healing`)
- Smokey & Meerky (100% `Healing`)

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

- Physical — Area, Single target

#### Debuffs provided by Hepler

- Haste — Single target — `average`

#### Crowd Control provided by Hepler

- Blind — Area — `high`
- Stun — Area — `average`
- Taunt — Area — `high`

## Hewynn

### Hewynn's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Rain Prayer (ultimate)
- **Movement**: stationary (no finite attack range)
- **Damage types**: Magic `low`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `average`
- **Non-ultimate**: speed `fast`, heal `average`

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
Common buffers are **Twins**, **Lyca**, or **Mikola**.

- **Pandora**
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, low, conditional (frequent))
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
- **Gunnar**
  - ATK buff (single target, low)
  - ATK SPD buff (single target, high) `signature fuel`

### Units benefitting most from Hewynn

Hewynn provides Healing to all units `average`.

- Salazer (3.2 / 5)

### Units that can act as a replacement for Hewynn

**Healing**

- Contess (100% `Healing`)
- Damian (100% `Healing`)
- Koko (100% `Healing`)

**Similar Skills**

- Fay (100% `ally-healer` `aoe-healing`)
- Ludovic (100% `ally-healer` `aoe-healing`)
- Smokey & Meerky (100% `ally-healer` `aoe-healing`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

### Summary for Hewynn

#### Crowd Control provided by Hewynn

- Unaffected (Mythic+) — Self — On skill

## Himmel

### Himmel's behavior

`AFK Stages [B]`, `Dream Realm [A]`, `Dream Realm (Endless) [A+]`, `PVP [A]`

- **Signature skill**: Hero Party (Skill 2)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Skill overview

- **Signature skill**: speed `slow`, first cast speed `fast`, buffs `average`, damage `average`
- **Ultimate**: speed `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, damage `average`

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
Common buffers are **Twins**, **Hugin**, or **Contess**.

Himmel also requires a party **with the right composition**

- **Velara**
  - Haste buff (single target, low) `signature fuel`
  - Healing (area, low)
  - Enables Party composition via Support (party slot)
- **Alna**
  - ATK buff (single target, average)
  - Max HP buff (single target, low)
  - Enables Party composition via Tank (party slot)
- **Frieren**
  - ATK buff (single target, high)
  - Enables Party composition via Mage (party slot)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - ATK buff (single target, low)
  - Max HP via Shield (single target, high)
  - Healing (single target, average)

### Units benefitting most from Himmel

Himmel provides Shield to single targets `low`, ATK buff (Mythic+) to multiple targets `low`, and Max HP buff (Mythic+) to multiple targets `high`.

- Cryonaia (2.8 / 5)

### Units that can act as a replacement for Himmel

**Buffs on allies**

- Twins (93% `Max HP` `ATK`)

**Damage**

- Gunnar (91% `Max HP-based damage` `Physical`)
- Shemira (77% `Max HP-based damage`)
- Silven (69% `Max HP-based damage`)

### Summary for Himmel

#### Damage types dealt by Himmel

- Physical — All units, Area, Single target
- Max HP-based damage — All units — `high`

## Hodgkin

### Hodgkin's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Cannon Fire (ultimate)
- **Movement**: moving (avg attack range 3.0 tiles)
- **Damage types**: Physical `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
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
Common buffers are **Mikola**, **Rowan**, or **Twins**.

- **Talene**
  - ATK buff (area, high)
  - Healing (area, low)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (single target, high)
- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, average, conditional (frequent))
- **Pandora**
  - Healing (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Hodgkin

- Indris (1.8 / 5)
- Bonnie (1.6 / 5)
- Aliceth (1.4 / 5)

### Units that can act as a replacement for Hodgkin

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Silvina (90% `Energy drain` `Vitality debuff`)
- Sinbad (60% `Phys DEF debuff` `Vitality debuff`)
- Viperian (60% `Energy drain`)

### Summary for Hodgkin

#### Hodgkin Provides

- Summoning (Mythic+) — Area
- Stacking buff (Supreme+) — Single target

#### Damage types dealt by Hodgkin

- Physical — Arc, Area, Single target

#### Debuffs provided by Hodgkin

- Energy drain (Mythic+) — Single target — `average`
- Phys DEF (Supreme+) — Single target — `low`
- Vitality (Supreme+) — Single target — `low`

## Hugin

### Hugin's behavior

`AFK Stages [S+]`, `Dream Realm [B]`, `Dream Realm (Endless) [S]`, `PVP [A+]`

- **Signature skill**: Mechanized Bond (Skill 2)
- **Movement**: stationary (no finite attack range)
- **Self placement**: stays anchored to battle-prep tile; returns after displacement
- **Ally composition**: put one ally 1 tile behind him (ATK bonus; buff ends if they leave the sigil)
- **Damage types**: Physical `low`

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `average`
- **Ultimate**: speed `slow`, first cast speed `fast`, buffs `average`
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
Common buffers are **Twins**, **Rowan**, or **Damian**.

- **Mehira**
  - Haste buff (single target, low) `signature fuel`
- **Velara**
  - Haste buff (single target, low) `signature fuel`
- **Tasi**
  - Haste buff (single target, high) `signature fuel`
- **Vala**
  - Haste buff (single target, high) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Hugin

Hugin provides ATK buff to multiple targets `high`, Haste buff to multiple targets `high`, and Shield (Mythic+) to multiple targets `high`.

**80** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Tasi (4.0 / 5)
- Alsa (3.8 / 5)
- Frieren (3.8 / 5)
- Natsu (3.8 / 5)
- Perseus (3.7 / 5)
- Lorsan (3.6 / 5)
- Lumont (3.6 / 5)
- Mehira (3.6 / 5)
- Lenya (3.4 / 5)
- Hepler (3.2 / 5)

### Units that can act as a replacement for Hugin

**Buffs on allies**

- Twins (73% `Haste` `ATK` `Max HP`)

**Similar Skills**

- Twins (80% `ally-shielder` `energy-provider`)

**Damage**

- Baelran (100% `Physical`)
- Gunnar (100% `Physical`)
- Gwyneth (100% `Physical`)

### Summary for Hugin

## Igor

### Igor's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Funereal Ring (ultimate)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Physical `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, damage `average`
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
Common buffers are **Smokey & Meerky**, **Mikola**, or **Solise**.

- **Koko**
  - Healing (all units, average)
  - Lifedrain buff (multiple targets, average)
- **Hepler**
  - Healing (multiple targets, high)
- **Dunlingr**
  - Lifedrain buff (all units, low)
- **Brutus**
  - Lifedrain buff (single target, high)
- **Evie**
  - Healing (single target, high)

### Units benefitting most from Igor

- Indris (1.3 / 5)
- Bonnie (1.3 / 5)
- Aliceth (1.2 / 5)

### Units that can act as a replacement for Igor

**Damage**

- Alna (100% `Physical`)
- Athalia (100% `Physical`)
- Dionel (100% `Physical`)

**Debuffs on enemies**

- Nazrik (100% `Healing debuff`)

### Summary for Igor

#### Damage types dealt by Igor

- Physical — All units, Area, Single target

#### Debuffs provided by Igor

- Healing (Mythic+) — Single target — `low`

## Indris

### Indris's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Spellbane Shot (ultimate)
- **Movement**: stationary (no finite attack range)
- **Damage types**: Physical `high`, True damage `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, debuffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`

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
Common buffers are **Lyca**, **Twins**, or **Hugin**.

Indris also requires units **putting debuffs** on enemies and/or units **putting multiple debuffs** on enemies

- **Kulu**
  - ATK buff (single target, low)
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via Damage taken debuff (all units)
- **Frieren**
  - ATK buff (single target, high)
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via DoT (area)
- **Alna**
  - ATK buff (single target, average)
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via Haste debuff (area)
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via Energy drain (all units)
- **Cyran**
  - Enables Multiple debuffs on target via ATK debuff
  - Enables Debuff on target via ATK debuff (all units)

### Units benefitting most from Indris

- Carolina (2.2 / 5)
- Nerion (1.9 / 5)
- Aliceth (1.4 / 5)

### Units that can act as a replacement for Indris

**Damage**

- Athalia (100% `Physical` `True damage`)
- Dionel (100% `True damage` `Physical`)
- Faramor (100% `True damage` `Physical`)

**Crowd Control**

- Kordan (79% `Bind` `Knock back`)
- Lenya (67% `Knock back`)
- Eironn (63% `Bind`)

### Summary for Indris

#### Damage types dealt by Indris

- Physical — Area, Multiple targets, Single target
- True damage — Multiple targets — `high`

#### Debuffs provided by Indris

- Damage taken — Multiple targets — `low`
- Magic DEF — Single target — `low`
- Phys DEF — Single target — `average`

#### Crowd Control provided by Indris

- Bind — Single target — `high`
- Knock back — Area — `low`

## Isabella

### Isabella's behavior

`AFK Stages [C]`, `Dream Realm [S]`, `Dream Realm (Endless) [A+]`, `PVP [C]`

- **Signature skill**: Grimoire Pact (ultimate)
- **Movement**: stationary (no finite attack range)
- **Ally composition**: frontmost ally becomes companion (stat stacks and ult buffs)
- **Damage types**: Magic `low`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, buffs `average`
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
Common buffers are **Twins**, **Hugin**, or **Contess**.

- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, low) `signature fuel`
- **Gunnar**
  - ATK buff (single target, low)
  - ATK SPD buff (single target, high) `signature fuel`
- **Velara**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Healing (area, low)
- **Zanie**
  - ATK buff (single target, low)
  - Healing (single target, average)
- **Mehira**
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Isabella

Isabella provides ATK buff to multiple targets `low` — conditional (frequent), DEF buff to single targets `low`, and Haste buff (Supreme+) to multiple targets `low`.

- Shakir (1.8 / 5)
- Rowan (1.7 / 5)

### Units that can act as a replacement for Isabella

**Buffs on allies**

- Twins (100% `ATK` `Haste` `Magic DEF` `Physical DEF`)
- Hugin (96% `ATK` `Haste`)
- Kordan (60% `ATK` `Magic DEF` `Physical DEF`)

**Damage**

- Aurora (100% `Magic`)
- Cryonaia (100% `Magic`)
- Cyran (100% `Magic`)

**Debuffs on enemies**

- Athalia (100% `ATK debuff`)
- Contess (100% `ATK debuff`)
- Cyran (100% `ATK debuff`)

### Summary for Isabella

#### Damage types dealt by Isabella

- Magic — Area, Single target

#### Debuffs provided by Isabella

- ATK — Single target — `low`

#### Crowd Control provided by Isabella

- Unaffected — Single target — Once

## Kafra

### Kafra's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Gale Thrust (ultimate)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Physical `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, debuffs `average`, damage `average`
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

Look for units providing: `ATK` `Max HP`  
Common buffers are **Twins**, **Rowan**, or **Lyca**.

- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Pandora**
  - Max HP buff (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Hepler**
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`

### Units benefitting most from Kafra

- Indris (2.1 / 5)
- Aliceth (1.7 / 5)
- Nerion (1.6 / 5)

### Units that can act as a replacement for Kafra

**Similar Skills**

- Sinbad (80% `enemy-debuffer` `mark-target`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Lenya (100% `Stun` `Knock back`)
- Perseus (100% `Stun` `Knock back`)
- Scarlita (100% `Stun` `Knock back`)

### Summary for Kafra

#### Kafra Provides

- Marked target (focus fire) — Single target

#### Damage types dealt by Kafra

- Physical — Single target

#### Debuffs provided by Kafra

- Marked target (focus fire) — Single target — `average`
- Phys DEF — Single target — `high`
- ATK (Mythic+) — Single target — `low`
- Haste (Mythic+) — Single target — `high`

#### Crowd Control provided by Kafra

- Unaffected (Mythic+) — Self — Conditional
- Knock back — Single target — `low`
- Stun — Single target — `average`

## Koko

### Koko's behavior

`AFK Stages [A]`, `Dream Realm [B]`, `Dream Realm (Endless) [B]`, `PVP [B]`

- **Signature skill**: Full Energy (ultimate)
- **Movement**: mostly stationary (avg attack range 4.0 tiles)
- **Damage types**: Physical `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `average`
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

Look for units providing: `Haste` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Pandora**
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Isabella**
  - Haste buff (multiple targets, low) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Dunlingr**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
- **Thador**
  - Energy recovery (lieutenant, start of battle) `signature fuel`

### Units benefitting most from Koko

Koko provides Damage taken reduction to all units `low`, Healing to all units `average`, Lifedrain buff to multiple targets `average`, Shield (Mythic+) to all units `low`, and Vitality buff (Supreme+) to single targets `low`.

**14** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Igor (5.0 / 5)
- Talene (4.4 / 5)
- Callan (4.3 / 5)
- Salazer (4.3 / 5)
- Tilaya (4.3 / 5)
- Ulmus (4.3 / 5)
- Harak (3.3 / 5)
- Gunnar (3.2 / 5)
- Valka (3.0 / 5)
- Perseus (2.9 / 5)

### Units that can act as a replacement for Koko

**Healing**

- Contess (100% `Healing`)
- Smokey & Meerky (100% `Healing`)
- Solise (100% `Healing`)

**Similar Skills**

- Saida (66% `ally-shielder` `life-drain`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Debuffs on enemies**

- Bonnie (100% `Damage taken debuff`)
- Cryonaia (100% `Damage taken debuff`)
- Kruger (100% `Damage taken debuff`)

**Crowd Control**

- Perseus (100% `Stun`)
- Zandrok (60% `Stun`)

### Summary for Koko

#### Damage types dealt by Koko

- Physical — Area, Single target

#### Debuffs provided by Koko

- Damage taken — Single target — `low`

#### Crowd Control provided by Koko

- Stun — Area — `average`

## Kordan

### Kordan's behavior

`AFK Stages [C]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S]`, `PVP [A]`

- **Signature skill**: Dominance Ring (ultimate)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Physical `high`, HP loss `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `average`, damage `average`
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

Look for units providing: `ATK` `Max HP` `Healing` `DEF Penetration` `Life Drain`  
Common buffers are **Twins**, **Hugin**, or **Contess**.

- **Aliceth**
  - ATK buff (multiple targets, average)
  - DEF Penetration buff (multiple targets, high)
- **Zanie**
  - ATK buff (single target, low)
  - Max HP via Shield (single target, high)
  - Healing (single target, average)
  - DEF Penetration buff (single target, average)
- **Velara**
  - Healing (area, low)
  - DEF buff (single target, average)
  - DEF buff (single target, average)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Gunnar**
  - ATK SPD buff (single target, high) `signature fuel`

### Units benefitting most from Kordan

Kordan provides ATK buff to multiple targets `high`, Lifedrain buff to multiple targets `high`, DEF buff (EX+10) to single targets `low`, and DEF Penetration buff (Supreme+) to multiple targets `low`.

- Carolina (4.1 / 5)
- Brutus (4.0 / 5)
- Talene (3.9 / 5)
- Nerion (3.5 / 5)
- Lily May (3.3 / 5)

### Units that can act as a replacement for Kordan

**Damage**

- Aliceth (100% `Physical` `HP loss`)
- Faramor (100% `Physical` `HP loss`)
- Ravion (100% `Physical` `HP loss`)

### Summary for Kordan

#### Damage types dealt by Kordan

- Physical — Area, Single target
- HP loss — Single target — `average`

#### Crowd Control provided by Kordan

- Bind — Area — `high`
- Knock back — Single target — `low`
- Knock down — Single target — `low`
- Knock up (Mythic+) — Single target — `low`

## Korin

### Korin's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Demonseal Spear (ultimate)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Physical `average`, True damage `low`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `low`
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
Common buffers are **Twins**, **Hugin**, or **Lyca**.

- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
- **Cecia**
  - ATK SPD buff (single target, high) `signature fuel`
  - Max HP buff (single target, high)
- **Pandora**
  - Max HP buff (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, low) `signature fuel`

### Units benefitting most from Korin

Korin provides Shield to single targets `average`.

- Carolina (2.0 / 5)
- Nerion (2.0 / 5)
- Perseus (1.3 / 5)

### Units that can act as a replacement for Korin

**Buffs on allies**

- Callan (100% `Max HP`)
- Contess (100% `Max HP`)
- Daimon (100% `Max HP`)

**Similar Skills**

- Scarlita (80% `ally-shielder` `hp-scaling`)
- Lucca (60% `ally-shielder`)
- Silven (60% `hp-scaling`)

**Damage**

- Athalia (100% `Physical` `True damage`)
- Baelran (100% `Physical` `True damage`)
- Cyran (100% `True damage`)

**Crowd Control**

- Indris (80% `Bind` `Knock back`)
- Kordan (77% `Bind` `Knock back`)
- Cassadee (68% `Knock back`)

### Summary for Korin

#### Damage types dealt by Korin

- Physical — Area, Single target
- True damage — Single target — `low`

#### Crowd Control provided by Korin

- Bind — Single target — `average`
- Knock back — Area — `low`

## Kruger

### Kruger's behavior

`AFK Stages [C]`, `Dream Realm [S]`, `Dream Realm (Endless) [A]`, `PVP [C]`

- **Signature skill**: Devastating Axe (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Damage types**: Physical `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `average`, debuffs `average`, damage `high`
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

Look for units providing: `Max HP` `Physical DEF`  
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zandrok**
  - Max HP buff (multiple targets, low)
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Zanie**
  - Max HP via Shield (single target, high)
- **Velara**
  - DEF buff (single target, average)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Isabella**
  - DEF buff (single target, low)
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`

### Units benefitting most from Kruger

- Indris (2.6 / 5)
- Bonnie (1.8 / 5)
- Aliceth (1.6 / 5)

### Units that can act as a replacement for Kruger

**Similar Skills**

- Shadewing (60% `enemy-debuffer`)

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

#### Damage types dealt by Kruger

- Physical — Single target

#### Debuffs provided by Kruger

- Damage taken — Single target — `low`
- Phys DEF — Single target — `low`
- Vulnerable — Area — `low`

#### Crowd Control provided by Kruger

- Knock down — Single target — `low`

## Kulu

### Kulu's behavior

`AFK Stages [S]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Demolition Zone (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Physical `high`

#### Skill overview

- **Signature skill**: speed `slow`, first cast speed `fast`, buffs `average`, damage `low`
- **Ultimate**: speed `average`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `high`

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
Common buffers are **Twins**, **Hugin**, or **Galahad**.

- **Aliceth**
  - ATK buff (multiple targets, average)
  - DEF Penetration buff (multiple targets, high)
- **Gunnar**
  - ATK SPD buff (single target, high) `signature fuel`
- **Zanie**
  - ATK buff (single target, low)
  - DEF Penetration buff (single target, average)
- **Mehira**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Velara**
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Kulu

Kulu provides ATK buff (Legendary+) to single targets `low` and DEF Penetration buff (EX+15) to single targets `low`.

- Bonnie (4.1 / 5)
- Indris (3.8 / 5)

### Units that can act as a replacement for Kulu

**Buffs on allies**

- Aliceth (100% `ATK` `DEF Penetration`)
- Kordan (100% `ATK` `DEF Penetration`)
- Zanie (100% `ATK` `DEF Penetration`)

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

- Physical — All units, Area, Single target

#### Debuffs provided by Kulu

- Movement speed — Area — `low`
- Damage taken (Mythic+) — All units — `high`

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
- **Damage types**: Physical `low`

#### Skill overview

- **Signature skill**: speed `slow`, heal `average`, buffs `average`
- **Ultimate**: speed `fast`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`

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
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, average, conditional (frequent))
  - Max HP via Shield (summons only, average)
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Talene**
  - ATK buff (area, high)
  - Healing (area, low)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, average)

### Units benefitting most from Laios

Laios provides ATK buff to multiple targets `low` — conditional (rare) and DEF buff to single targets `low` — conditional (rare).

- Carolina (3.1 / 5)
- Nerion (2.6 / 5)
- Shadewing (2.0 / 5)

### Units that can act as a replacement for Laios

**Similar Skills**

- Damian (66% `ally-healer` `summoner`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Crowd Control**

- Alna (100% `Bind`)
- Kordan (100% `Bind`)
- Evie (84% `Bind`)

### Summary for Laios

#### Laios Provides

- Summoning — Single target
- Stacking buff (EX+10) — Single target

#### Crowd Control provided by Laios

- Bind — Area — `average`

## Lenya

### Lenya's behavior

`AFK Stages [C]`, `Dream Realm [A+]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Wild Duel (ultimate)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Physical `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `average`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `high`

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

Look for units providing: `ATK` `Haste` `Max HP` `CRIT` `CRIT DMG Boost`  
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, low)
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Pandora**
  - Max HP buff (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, low, conditional (frequent))
  - Haste buff (multiple targets, low) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`

### Units benefitting most from Lenya

Lenya provides Shield (Supreme+) to single targets `high`.

- Nerion (2.1 / 5)
- Perseus (1.6 / 5)
- Silven (1.5 / 5)

### Units that can act as a replacement for Lenya

**Buffs on allies**

- Galahad (100% `Max HP`)
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

- Physical — Area, Single target

#### Crowd Control provided by Lenya

- Unaffected — Self — Once
- Knock back — Area — `low`
- Stun — Single target — `average`

## Lily May

### Lily May's behavior

`AFK Stages [A]`, `Dream Realm [B]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Tempest Shot (ultimate)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Magic `average`, Max HP-based damage `low`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, debuffs `average`, damage `high`
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
Common buffers are **Twins**, **Rowan**, or **Ravion**.

- **Aliceth**
  - ATK buff (multiple targets, average)
  - DEF Penetration buff (multiple targets, high)
- **Kordan**
  - ATK buff (multiple targets, high)
  - DEF Penetration buff (multiple targets, low)
- **Pandora**
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, low, conditional (frequent))
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Lily May

Lily May provides DEF Penetration buff (Legendary+) to single targets `low`.

- Bonnie (2.6 / 5)
- Aliceth (1.8 / 5)
- Indris (1.7 / 5)

### Units that can act as a replacement for Lily May

**Buffs on allies**

- Aliceth (100% `DEF Penetration`)
- Kordan (100% `DEF Penetration`)
- Kulu (100% `DEF Penetration`)

**Similar Skills**

- Athalia (72% `hp-scaling` `self-repositioner` `transformation`)

**Damage**

- Shemira (100% `Magic` `Max HP-based damage`)
- Sylphira (100% `Magic` `Max HP-based damage`)
- Silven (96% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Dunlingr (100% `Energy drain`)
- Rowan (100% `Energy drain`)
- Sylphira (80% `Energy drain`)

**Crowd Control**

- Sylphira (100% `Interrupt`)
- Saida (80% `Interrupt`)
- Reinier (66% `Interrupt`)

### Summary for Lily May

#### Lily May Provides

- Invincibility — Single target

#### Damage types dealt by Lily May

- Magic — All units, Single target
- Max HP-based damage — Single target — `low`

#### Debuffs provided by Lily May

- Energy drain — Single target — `high`

#### Crowd Control provided by Lily May

- Unaffected — Self — Start of battle
- Interrupt — Single target — `low`

## Lorsan

### Lorsan's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Whispering Tempest (ultimate)
- **Movement**: stationary (no finite attack range)
- **Damage types**: Magic `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`

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

- **Talene**
  - ATK buff (area, high)
  - Healing (area, low)
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (single target, high)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Tasi**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Lorsan

Lorsan provides Healing to all units `average`.

- Carolina (3.3 / 5)
- Nerion (2.9 / 5)
- Perseus (1.6 / 5)

### Units that can act as a replacement for Lorsan

**Healing**

- Koko (100% `Healing`)
- Smokey & Meerky (100% `Healing`)
- Solise (100% `Healing`)

**Similar Skills**

- Faramor (80% `aoe-damage` `dot-specialist`)

**Damage**

- Aurora (100% `Magic`)
- Berial (100% `Magic`)
- Bonnie (100% `Magic`)

**Crowd Control**

- Perseus (100% `Stun`)
- Soren (100% `Stun`)
- Zorya (100% `Stun`)

### Summary for Lorsan

#### Damage types dealt by Lorsan

- Magic — Area, Single target

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
- **Damage types**: Physical `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `average`, damage `high`
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

Look for units providing: `Max HP` `Healing` `Physical DEF` `Magic DEF`  
Common buffers are **Twins**, **Rowan**, or **Hugin**.

- **Tilaya**
  - Max HP buff (area, average)
  - DEF buff (area, average)
  - DEF buff (area, average)
- **Hepler**
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
  - DEF buff (single target, low)
  - DEF buff (single target, low)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Lumont**
  - DEF buff (multiple targets, high)
  - DEF buff (multiple targets, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, average)
- **Fay**
  - Healing (arc, average, conditional (frequent))
  - DEF buff (multiple targets, low)
  - DEF buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`

### Units benefitting most from Lucca

Lucca provides DEF buff in an area `high`.

- Cecia (3.8 / 5)
- Seth (2.8 / 5)

### Units that can act as a replacement for Lucca

**Buffs on allies**

- Lumont (90% `Magic DEF` `Physical DEF`)
- Tilaya (80% `Magic DEF` `Physical DEF`)
- Sonja (60% `Magic DEF` `Physical DEF`)

**Similar Skills**

- Lucius (72% `ally-shielder`)
- Antandra (60% `ally-shielder`)
- Hugin (60% `ally-shielder`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Antandra (84% `Stun` `Knock down`)
- Zorya (70% `Stun` `Knock down`)

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

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Divine Light Aegis (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Damage types**: Physical `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `average`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `average`

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

Look for units providing: `Healing`  
Common buffers are **Rowan**, **Lyca**, or **Twins**.

- **Pandora**
  - Healing (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Hepler**
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Hewynn**
  - Healing (all units, average)
- **Koko**
  - Healing (all units, average)
- **Lorsan**
  - Healing (all units, average)

### Units benefitting most from Lucius

Lucius provides Shield in an area `average`.

- Himmel (2.5 / 5)
- Nerion (1.8 / 5)
- Perseus (1.8 / 5)

### Units that can act as a replacement for Lucius

**Buffs on allies**

- Hepler (100% `Max HP`)
- Hugin (100% `Max HP`)
- Saida (100% `Max HP`)

**Similar Skills**

- Hepler (80% `ally-healer` `ally-shielder`)
- Lucca (72% `ally-shielder`)
- Solise (66% `ally-healer` `ally-shielder`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Athalia (100% `ATK debuff`)
- Bonnie (100% `ATK debuff`)
- Contess (100% `ATK debuff`)

**Crowd Control**

- Aliceth (100% `Knock back` `Stun`)
- Alsa (100% `Knock back` `Stun`)
- Atalanta (100% `Knock back` `Stun`)

### Summary for Lucius

#### Damage types dealt by Lucius

- Physical — Area, Single target

#### Debuffs provided by Lucius

- ATK (Mythic+) — Single target — `low`

#### Crowd Control provided by Lucius

- Knock back — Single target — `low`
- Stun — Single target — `low`

## Lucy

### Lucy's behavior

- **Signature skill**: Star Dress: Aquarius Form (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Damage types**: Magic `high`

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
Common buffers are **Twins**, **Hugin**, or **Lyca**.

- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, low) `signature fuel`
- **Tasi**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Cecia**
  - ATK SPD buff (single target, high) `signature fuel`

### Units benefitting most from Lucy

Lucy provides Shield (Mythic+) to single targets `high`.

- Himmel (2.1 / 5)
- Nerion (1.9 / 5)
- Perseus (1.4 / 5)

### Units that can act as a replacement for Lucy

**Buffs on allies**

- Galahad (100% `Max HP`)
- Hepler (100% `Max HP`)
- Hugin (100% `Max HP`)

**Damage**

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Cassadee (100% `Magic`)

**Crowd Control**

- Lucca (100% `Stun` `Knock up`)
- Zandrok (100% `Stun` `Knock up`)
- Scarlita (93% `Stun` `Knock up`)

### Summary for Lucy

#### Damage types dealt by Lucy

- Magic — All units, Single target

#### Crowd Control provided by Lucy

- Unaffected — Self — On skill
- Knock up — Single target — `low`
- Stun — Single target — `average`

## Ludovic

### Ludovic's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [A]`, `PVP [A]`

- **Signature skill**: Eternal Serenity (ultimate)
- **Movement**: stationary (no finite attack range)
- **Damage types**: Magic `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `average`
- **Non-ultimate**: speed `fast`, heal `average`, damage `high`

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
Common buffers are **Rowan**, **Twins**, or **Smokey & Meerky**.

- **Pandora**
  - Healing (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Koko**
  - Healing (all units, average)
- **Velara**
  - Healing (area, low)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Thador**
  - Energy recovery (lieutenant, start of battle) `signature fuel`
- **Evie**
  - Healing (single target, high)

### Units benefitting most from Ludovic

Ludovic provides Healing in an area `low`.

- Himmel (2.0 / 5)
- Nerion (1.6 / 5)
- Perseus (1.2 / 5)

### Units that can act as a replacement for Ludovic

**Healing**

- Contess (100% `Healing`)
- Evie (100% `Healing`)
- Koko (100% `Healing`)

**Similar Skills**

- Smokey & Meerky (100% `ally-healer` `aoe-healing`)
- Solise (80% `ally-healer` `aoe-healing`)
- Velara (60% `ally-healer` `aoe-healing`)

**Damage**

- Callan (100% `Magic`)
- Cryonaia (100% `Magic`)
- Cyran (100% `Magic`)

**Crowd Control**

- Aliceth (100% `Stun`)
- Bonnie (100% `Stun`)
- Callan (100% `Stun`)

### Summary for Ludovic

#### Damage types dealt by Ludovic

- Magic — All units, Single target

#### Crowd Control provided by Ludovic

- Unaffected — Self — On skill
- Stun (Supreme+) — Single target — `average`

## Lumont

### Lumont's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Lumont's Charge (ultimate)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Physical `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `average`
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

Look for units providing: `Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Damian**.

- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, average)
- **Pandora**
  - Max HP buff (single target, average)
  - Healing (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, low)
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Tasi**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Lumont

Lumont provides DEF buff to multiple targets `high`.

- Lucca (4.0 / 5)

### Units that can act as a replacement for Lumont

**Buffs on allies**

- Lucca (100% `Magic DEF` `Physical DEF`)
- Tilaya (100% `Magic DEF` `Physical DEF`)
- Sonja (66% `Magic DEF` `Physical DEF`)

**Similar Skills**

- Kruger (60% `enemy-debuffer`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Bonnie (100% `ATK debuff`)
- Cyran (100% `ATK debuff`)
- Lyca (100% `ATK debuff`)

**Crowd Control**

- Antandra (100% `Taunt` `Stun`)
- Hepler (100% `Taunt` `Stun`)
- Phraesto (72% `Stun` `Taunt`)

### Summary for Lumont

#### Damage types dealt by Lumont

- Physical — Area, Single target

#### Debuffs provided by Lumont

- ATK (Mythic+) — Single target — `high`

#### Crowd Control provided by Lumont

- Unaffected — Self — On skill
- Stun — Area — `low`
- Taunt — Single target — `average`
- Knock up (Mythic+) — Single target — `low`

## Lyca

### Lyca's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Comet Archery (ultimate)
- **Movement**: stationary (avg attack range 11.0 tiles)
- **Damage types**: Physical `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `average`
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

- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
- **Pandora**
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, high) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Isabella**
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`

### Units benefitting most from Lyca

Lyca provides ATK SPD buff to all units `average` and Energy recovery to all units `low`.

**33** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight
- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Indris (5.0 / 5)
- Fay (4.4 / 5)
- Gwyneth (4.4 / 5)
- Mirael (4.4 / 5)
- Rhys (4.4 / 5)
- Cecia (4.1 / 5)
- Korin (3.9 / 5)
- Marilee (3.9 / 5)
- Parisa (3.7 / 5)
- Nerion (3.2 / 5)

### Units that can act as a replacement for Lyca

**Damage**

- Alna (100% `Physical`)
- Athalia (100% `Physical`)
- Dionel (100% `Physical`)

**Debuffs on enemies**

- Cyran (100% `ATK debuff`)

**Crowd Control**

- Aliceth (100% `Stun`)
- Bonnie (100% `Stun`)
- Callan (100% `Stun`)

### Summary for Lyca

#### Damage types dealt by Lyca

- Physical — All units, Area, Single target

#### Debuffs provided by Lyca

- ATK — All units — `high`

#### Crowd Control provided by Lyca

- Stun (EX+10) — Single target — `average`

## Marcille

### Marcille's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Silver-White Wings that Streak Across the Skies (ultimate)
- **Movement**: stationary (no finite attack range)
- **Ally composition**: place ally 1 tile in front at battle prep (revive target)
- **Damage types**: Magic `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `average`, buffs `average`, damage `high`
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
Common buffers are **Twins**, **Smokey & Meerky**, or **Mikola**.

- **Koko**
  - Healing (all units, average)
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, low) `signature fuel`
- **Velara**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Healing (area, low)
- **Gunnar**
  - ATK SPD buff (single target, high) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Marcille

Marcille provides Haste buff to single targets `low` and Healing to multiple targets `low`.

- Himmel (2.1 / 5)
- Nerion (1.8 / 5)
- Perseus (1.4 / 5)

### Units that can act as a replacement for Marcille

**Buffs on allies**

- Dunlingr (100% `Haste`)
- Galahad (100% `Haste`)
- Hugin (100% `Haste`)

**Healing**

- Contess (100% `Healing`)
- Evie (100% `Healing`)
- Koko (100% `Healing`)

**Damage**

- Callan (100% `Magic`)
- Cryonaia (100% `Magic`)
- Cyran (100% `Magic`)

**Crowd Control**

- Aliceth (80% `Blind`)
- Twins (66% `Blind`)

### Summary for Marcille

#### Marcille Provides

- Revive ally (Mythic+) — Single target
- Stacking buff (Supreme+) — Single target

#### Damage types dealt by Marcille

- Magic — All units, Area, Single target

#### Crowd Control provided by Marcille

- Unaffected (Supreme+) — Self — On skill
- Blind — Single target — `average`
- Interrupt (Mythic+) — Single target — `low`

## Marilee

### Marilee's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Mid-Air Shot (ultimate)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Physical `low`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `low`
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
Common buffers are **Twins**, **Lyca**, or **Mikola**.

- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
- **Tasi**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, low, conditional (frequent))
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`

### Units benefitting most from Marilee

- Carolina (1.4 / 5)
- Nerion (1.3 / 5)

### Units that can act as a replacement for Marilee

**Similar Skills**

- Pippa (80% `hp-scaling` `self-repositioner`)
- Kordan (66% `hp-scaling` `self-repositioner`)
- Tasi (66% `mass-cc` `self-repositioner`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Aliceth (100% `Stun`)
- Alsa (100% `Stun`)
- Antandra (100% `Stun`)

### Summary for Marilee

#### Marilee Provides

- Stacking buff (Mythic+) — Multiple targets

#### Damage types dealt by Marilee

- Physical — Multiple targets, Single target

#### Crowd Control provided by Marilee

- Stun — Single target — `low`

## Mehira

### Mehira's behavior

`AFK Stages [S+]`, `Dream Realm [A]`, `Dream Realm (Endless) [A+]`, `PVP [A+]`

- **Signature skill**: Euphoric Rush (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Damage types**: Magic `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `average`
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

Look for units providing: `Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Solise**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Velara**
  - Haste buff (single target, low) `signature fuel`
  - Healing (area, low)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, high) `signature fuel`
- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`

### Units benefitting most from Mehira

Mehira provides Haste buff to single targets `low`.

- Hugin (1.3 / 5)
- Aurora (1.3 / 5)
- Ravion (1.3 / 5)
- Florabelle (1.3 / 5)
- Galahad (1.3 / 5)

### Units that can act as a replacement for Mehira

**Buffs on allies**

- Hugin (100% `Haste`)
- Twins (100% `Haste`)
- Velara (100% `Haste`)

**Damage**

- Aurora (100% `Magic`)
- Saida (100% `Magic`)
- Solise (100% `Magic`)

### Summary for Mehira

#### Mehira Provides

- HP threshold strike (Mythic+) — Self
- Summoning (Mythic+) — Self

#### Damage types dealt by Mehira

- Magic — Area, Single target

#### Debuffs provided by Mehira

- Damage taken (Supreme+) — Single target — `low`

#### Crowd Control provided by Mehira

- Untargetable (Mythic+) — Self — Start of battle
- Charm — Single target — `average`

## Mikola

### Mikola's behavior

`AFK Stages [C]`, `Dream Realm [A]`, `Dream Realm (Endless) [A]`, `PVP [B]`

- **Signature skill**: Dauntless Hymn (ultimate)
- **Movement**: moving (avg attack range 2.0 tiles)
- **Damage types**: Physical `low`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `average`, buffs `average`
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
Common buffers are **Twins**, **Rowan**, or **Hugin**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Velara**
  - Haste buff (single target, low) `signature fuel`
  - Healing (area, low)
  - DEF buff (single target, average)
  - DEF buff (single target, average)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (single target, high)
- **Isabella**
  - ATK buff (multiple targets, low, conditional (frequent))
  - Haste buff (multiple targets, low) `signature fuel`
  - DEF buff (single target, low)
  - DEF buff (single target, low)
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Kordan**
  - ATK buff (multiple targets, high)
  - DEF buff (single target, low)
  - DEF buff (single target, low)

### Units benefitting most from Mikola

Mikola provides ATK buff to all units `high`, Haste buff to multiple targets `low`, Healing to multiple targets `low`, Healing over time to all units `average`, and Vitality buff (EX+10) to multiple targets `low`.

**32** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Hammie (5.0 / 5)
- Hodgkin (5.0 / 5)
- Perseus (3.9 / 5)
- Lorsan (3.7 / 5)
- Vala (3.6 / 5)
- Laios (3.6 / 5)
- Temesia (3.6 / 5)
- Seth (3.5 / 5)
- Tasi (3.4 / 5)
- Hepler (3.3 / 5)

### Units that can act as a replacement for Mikola

**Buffs on allies**

- Hugin (68% `ATK` `Haste`)
- Twins (68% `ATK` `Haste` `Vitality buff`)

**Healing**

- Solise (69% `Healing over time` `Healing`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

### Summary for Mikola

#### Crowd Control provided by Mikola

- Unaffected (Supreme+) — Self — Conditional

## Mirael

### Mirael's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Winged Flame (ultimate)
- **Movement**: stationary (avg attack range 10.1 tiles)
- **Damage types**: Magic `average`, DoT `low`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
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
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Tasi**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
- **Pandora**
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Cecia**
  - ATK SPD buff (single target, high) `signature fuel`

### Units benefitting most from Mirael

- Shadewing (2.0 / 5)
- Bonnie (1.6 / 5)
- Himmel (1.6 / 5)

### Units that can act as a replacement for Mirael

**Similar Skills**

- Gwyneth (96% `dot-specialist` `fire-attack`)
- Satrana (66% `dot-specialist` `fire-attack`)

**Damage**

- Frieren (100% `Magic` `DoT`)
- Tasi (100% `Magic` `DoT`)
- Alsa (87% `Magic`)

### Summary for Mirael

#### Damage types dealt by Mirael

- Magic — Area, Single target
- DoT — Single target

## Nara

### Nara's behavior

`AFK Stages [A]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Phantom Chains (Skill 1)
- **Movement**: mostly stationary (pulls enemies)
- **Damage types**: Physical `high`, HP loss `average`, True damage `high`

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
Common buffers are **Ravion**, **Smokey & Meerky**, or **Rowan**.

- **Thador**
  - Energy recovery (single target, low) `signature fuel`
- **Thoran**
  - Energy recovery (single target, low) `signature fuel`
- **Ulmus**
  - Energy recovery (single target, low) `signature fuel`
- **Seth**
  - Energy recovery (single target, high) `signature fuel`
- **Arden**
  - Energy recovery (single target, low) `signature fuel`

### Units benefitting most from Nara

Nara provides Healing (Mythic+) in an area `low`.

- Aliceth (1.6 / 5)
- Nerion (1.6 / 5)
- Perseus (1.2 / 5)

### Units that can act as a replacement for Nara

**Healing**

- Contess (100% `Healing`)
- Evie (100% `Healing`)
- Hepler (100% `Healing`)

**Damage**

- Faramor (100% `True damage` `HP loss` `Physical`)
- Zorya (62% `HP loss`)
- Kordan (61% `HP loss` `Physical`)

**Debuffs on enemies**

- Alna (100% `Vitality debuff`)
- Dionel (100% `Vitality debuff`)
- Faramor (100% `Vitality debuff`)

**Crowd Control**

- Scarlita (80% `Knock down` `Knock up`)
- Reinier (77% `Displace` `Knock down` `Knock up`)
- Baelran (66% `Knock down` `Knock up`)

### Summary for Nara

#### Damage types dealt by Nara

- Physical — Single target
- HP loss — Single target — `average`
- True damage — Single target — `high`

#### Debuffs provided by Nara

- Vitality (Supreme+) — Single target — `low`

#### Crowd Control provided by Nara

- Unaffected (Supreme+) — Self — Permanent
- Displace — Single target — `low`
- Knock down — Single target — `average`
- Knock up — Single target — `low`

## Natsu

### Natsu's behavior

- **Signature skill**: Lightning Fire Dragon's Roar/Fire Dragon King's Roar (ultimate)
- **Movement**: stationary (avg attack range 11.0 tiles)
- **Damage types**: Magic `high`, Max HP-based damage `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `average`, first cast speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, debuffs `average`, damage `high`

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

Look for units providing: `ATK` `Haste` `CRIT` `CRIT DMG Boost`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Tasi**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, low, conditional (frequent))
  - Haste buff (multiple targets, low) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, low)
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Natsu

- Shadewing (2.6 / 5)
- Bonnie (2.5 / 5)
- Nerion (1.8 / 5)

### Units that can act as a replacement for Natsu

**Similar Skills**

- Frieren (61% `aoe-damage` `dot-specialist` `high-damage-ult`)
- Gwyneth (60% `dot-specialist` `fire-attack` `mass-cc`)

**Damage**

- Himmel (100% `Max HP-based damage`)
- Shemira (100% `Max HP-based damage` `Magic`)
- Lily May (94% `Magic` `Max HP-based damage`)

**Crowd Control**

- Antandra (100% `Stun` `Knock down`)
- Lucca (100% `Stun` `Knock down`)
- Zorya (100% `Stun` `Knock down`)

### Summary for Natsu

#### Damage types dealt by Natsu

- Magic — Area, Single target
- Max HP-based damage — Area — `high`

#### Debuffs provided by Natsu

- Haste — Single target — `average`
- Max HP (Mythic+) — Single target — `low`
- DoT (Supreme+) — Single target — `average`

#### Crowd Control provided by Natsu

- Knock down — Area — `low`
- Stun — Single target — `average`

## Nazrik

### Nazrik's behavior

`AFK Stages [B]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [B]`

- **Signature skill**: Rend Rupture (ultimate)
- **Movement**: stationary (avg attack range 10.0 tiles)
- **Damage types**: Physical `high`, True damage `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `average`, damage `high`
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
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, high) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Isabella**
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Valka**
  - ATK SPD buff (multiple targets, low) `signature fuel`

### Units benefitting most from Nazrik

- Indris (1.9 / 5)
- Carolina (1.8 / 5)
- Nerion (1.6 / 5)

### Units that can act as a replacement for Nazrik

**Similar Skills**

- Aliceth (60% `hp-scaling` `mark-target`)
- Silven (60% `hp-scaling`)

**Damage**

- Athalia (100% `True damage` `Physical`)
- Baelran (100% `True damage` `Physical`)
- Faramor (100% `True damage` `Physical`)

**Crowd Control**

- Aliceth (100% `Stun`)
- Bonnie (100% `Stun`)
- Callan (100% `Stun`)

### Summary for Nazrik

#### Nazrik Provides

- Stacking buff — Single target

#### Damage types dealt by Nazrik

- Physical — Single target
- True damage — Single target — `average`

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

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Drowning Doom (ultimate)
- **Movement**: mostly stationary (avg attack range 4.0 tiles)
- **Damage types**: Magic `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `low`
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

Look for units providing: `ATK SPD / Haste` `Max HP` `Energy` `DEF Penetration`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

Nerion also requires units **applying crowd control** to enemies

- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
  - Enables CC on enemies via Blind (area, high)
- **Kordan**
  - Enables CC on enemies via Bind (area, high)
- **Aliceth**
  - DEF Penetration buff (multiple targets, high)
  - Enables CC on enemies via Blind (area, average)
- **Koko**
  - Max HP via Shield (all units, low)
  - Enables CC on enemies via Stun (area, average)
- **Daimon**
  - Max HP via Shield (multiple targets, low)
  - Enables CC on enemies via Frighten (area, average)

### Units benefitting most from Nerion

- Bonnie (2.2 / 5)
- Carolina (1.8 / 5)
- Indris (1.3 / 5)

### Units that can act as a replacement for Nerion

**Similar Skills**

- Shadewing (100% `dot-specialist` `enemy-debuffer`)
- Kruger (60% `enemy-debuffer`)

**Damage**

- Aurora (100% `Magic`)
- Bonnie (100% `Magic`)
- Callan (100% `Magic`)

**Debuffs on enemies**

- Athalia (100% `ATK debuff`)
- Bonnie (100% `ATK debuff`)
- Contess (100% `ATK debuff`)

**Crowd Control**

- Aliceth (100% `Stun`)
- Bonnie (100% `Stun`)
- Callan (100% `Stun`)

### Summary for Nerion

#### Nerion Provides

- Enhanced form (Supreme+) — Single target

#### Damage types dealt by Nerion

- Magic — Area, Single target

#### Debuffs provided by Nerion

- ATK (Mythic+) — Single target — `low`

#### Crowd Control provided by Nerion

- Stun — Single target — `average`

## Niru

### Niru's behavior

`AFK Stages [A+]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Soul Shepherd (ultimate)
- **Movement**: stationary (no finite attack range)
- **Ally composition**: nearest ally auto-selected at battle start; prioritizes ally behind
- **Damage types**: Magic `average`, HP loss `low`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, heal `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, damage `average`

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
Common buffers are **Rowan**, **Twins**, or **Solise**.

Niru also requires a unit **to bless** and/or enemies **to be defeated**

- **Velara**
  - Healing (area, low)
  - DEF buff (single target, average)
  - DEF buff (single target, average)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Isabella**
  - DEF buff (single target, low)
  - DEF buff (single target, low)
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Enables Enemy defeat via HP threshold strike
- **Aliceth**
  - Enables Enemy defeat via Instant defeat
- **Cryonaia**
  - Enables Enemy defeat via Instant defeat

### Units benefitting most from Niru

- Bonnie (2.0 / 5)
- Himmel (1.6 / 5)
- Zorya (1.5 / 5)

### Units that can act as a replacement for Niru

**Damage**

- Dunlingr (100% `Magic` `HP loss`)
- Shadewing (96% `Magic` `HP loss`)
- Aliceth (71% `HP loss`)

### Summary for Niru

#### Niru Provides

- Spirit form protection — Single target
- Start-of-battle cast (Mythic+) — Self

#### Damage types dealt by Niru

- Magic — All units, Single target
- HP loss — Single target — `low`

## Odie

### Odie's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Heart Crusher (Mythic+)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Damage types**: Magic `low`, DoT `average`

#### Skill overview

- **Signature skill**: speed `fast`, debuffs `average`
- **Ultimate**: speed `slow`, damage `low`
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
Common buffers are **Twins**, **Hugin**, or **Lyca**.

- **Tasi**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, high) `signature fuel`
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Odie

- Shadewing (2.3 / 5)
- Bonnie (1.9 / 5)
- Indris (1.3 / 5)

### Units that can act as a replacement for Odie

**Damage**

- Bryon (100% `DoT` `Magic`)
- Frieren (100% `DoT` `Magic`)
- Shadewing (100% `DoT` `Magic`)

**Debuffs on enemies**

- Evie (100% `DoT`)
- Frieren (100% `DoT`)
- Gwyneth (100% `DoT`)

### Summary for Odie

#### Damage types dealt by Odie

- Magic — Single target
- DoT — Single target

#### Debuffs provided by Odie

- DoT — Single target — `low`

## Pandora

### Pandora's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [A]`, `PVP [A+]`

- **Signature skill**: Boxed Blessing (Skill 1)
- **Movement**: stationary (no finite attack range)
- **Ally composition**: rearmost ally enters invincible box, then gains Energy and ATK
- **Damage types**: Magic `average`

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `average`
- **Ultimate**: speed `slow`, debuffs `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `average`

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
Common buffers are **Rowan**, **Ravion**, or **Twins**.

- **Thador**
  - Energy recovery (single target, low) `signature fuel`
- **Thoran**
  - Energy recovery (single target, low) `signature fuel`
- **Seth**
  - Energy recovery (single target, high) `signature fuel`
- **Arden**
  - Energy recovery (single target, low) `signature fuel`
- **Ulmus**
  - Energy recovery (single target, low) `signature fuel`

### Units benefitting most from Pandora

Pandora provides Healing to single targets `average`, Invincible to single targets `high`, and Max HP buff (Legendary+) to single targets `average`.

- Ludovic (3.1 / 5)
- Satrana (3.0 / 5)

### Units that can act as a replacement for Pandora

**Buffs on allies**

- Aurora (72% `Invincible`)

**Healing**

- Contess (100% `Healing`)
- Rowan (100% `Healing`)
- Solise (100% `Healing`)

**Damage**

- Aurora (100% `Magic`)
- Bonnie (100% `Magic`)
- Cryonaia (100% `Magic`)

**Debuffs on enemies**

- Alna (66% `Haste debuff` `Vitality debuff`)

### Summary for Pandora

#### Pandora Provides

- Invincibility — Single target

#### Damage types dealt by Pandora

- Magic — Single target

#### Debuffs provided by Pandora

- Damage taken — Single target — `low`
- Energy drain — Single target — `low`
- Haste — Single target — `average`
- Vitality — Single target — `average`

## Pang

### Pang's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Sky Splitter (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Damage types**: Physical `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `average`, damage `high`
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

Look for units providing: `ATK` `Haste` `DEF Penetration`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Aliceth**
  - ATK buff (multiple targets, average)
  - DEF Penetration buff (multiple targets, high)
- **Kordan**
  - ATK buff (multiple targets, high)
  - DEF Penetration buff (multiple targets, low)
- **Tasi**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, low, conditional (frequent))
  - Haste buff (multiple targets, low) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`

### Units benefitting most from Pang

Pang provides ATK buff to single targets `high`, Shield (EX+10) to single targets `low`, and DEF Penetration buff (Supreme+) to single targets `low`.

- Perseus (1.7 / 5)
- Silven (1.6 / 5)
- Nerion (1.5 / 5)

### Units that can act as a replacement for Pang

**Buffs on allies**

- Aliceth (96% `ATK` `DEF Penetration`)
- Contess (80% `ATK` `Max HP`)
- Hugin (80% `ATK` `Max HP`)

**Similar Skills**

- Ulmus (100% `ally-shielder` `transformation`)
- Hepler (66% `ally-shielder` `transformation`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Crowd Control**

- Aliceth (100% `Stun`)
- Bonnie (100% `Stun`)
- Callan (100% `Stun`)

### Summary for Pang

#### Pang Provides

- Transformation — Self

#### Damage types dealt by Pang

- Physical — Area, Single target

#### Crowd Control provided by Pang

- Unaffected — Self — On skill
- Stun — Single target — `low`

## Parisa

### Parisa's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Floral Splendor (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Damage types**: Magic `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `low`

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
Common buffers are **Twins**, **Hugin**, or **Lyca**.

- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
- **Tasi**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Gunnar**
  - ATK buff (single target, low)
  - ATK SPD buff (single target, high) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, low, conditional (frequent))
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`

### Units benefitting most from Parisa

- Bonnie (1.6 / 5)
- Himmel (1.6 / 5)
- Niru (1.5 / 5)

### Units that can act as a replacement for Parisa

**Similar Skills**

- Cassadee (60% `ally-buffer` `aoe-damage`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

### Summary for Parisa

#### Parisa Provides

- Marked target (focus fire) — Area

#### Damage types dealt by Parisa

- Magic — Area, Single target

## Perseus

### Perseus's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S+]`

- **Signature skill**: Divine Rend (ultimate)
- **Movement**: moving (avg attack range 2.9 tiles)
- **Damage types**: Physical `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
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

Look for units providing: `ATK` `ATK SPD / Haste` `Max HP`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

Perseus also requires units **buffing them**

- **Koko**
  - Max HP via Shield (all units, low)
  - Grants 5 distinct stat buffs to Perseus
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
  - Grants 3 distinct stat buffs to Perseus
- **Pandora**
  - Max HP buff (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`
  - Grants 3 distinct stat buffs to Perseus (start of battle)
- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
  - Grants 3 distinct stat buffs to Perseus
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
  - Grants 4 distinct stat buffs to Perseus

### Units benefitting most from Perseus

Perseus provides ATK buff to multiple targets `low`.

- Carolina (3.1 / 5)
- Nerion (2.6 / 5)
- Silven (1.2 / 5)

### Units that can act as a replacement for Perseus

**Buffs on allies**

- Aliceth (100% `ATK`)
- Alna (100% `ATK`)
- Contess (100% `ATK`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

### Summary for Perseus

#### Damage types dealt by Perseus

- Physical — Area, Single target

#### Crowd Control provided by Perseus

- Unaffected — Multiple targets — On skill
- Knock back — Area — `low`
- Stun — Area — `average`

## Phraesto

### Phraesto's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [B]`, `PVP [B]`

- **Signature skill**: Crimson Contract (Skill 1)
- **Movement**: moving (avg attack range 1.8 tiles)
- **Ally composition**: place allies 1 tile behind this hero and the Illusion for contract buffs
- **Self placement**: keep this hero and Illusion in the same row (damage reduction and battle-start shields)
- **Damage types**: Magic `average`

#### Skill overview

- **Signature skill**: speed `slow`, first cast speed `fast`, buffs `average`, damage `low`
- **Ultimate**: speed `slow`, damage `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, damage `high`

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

Look for units providing: `Healing` `Energy` `Physical DEF` `Magic DEF`  
Common buffers are **Solise**, **Rowan**, or **Smokey & Meerky**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, average, conditional (frequent))
- **Hepler**
  - Healing (multiple targets, high)
  - DEF buff (single target, low)
  - DEF buff (single target, low)
- **Sonja**
  - DEF buff (multiple targets, average)
  - DEF buff (multiple targets, average)
- **Koko**
  - Healing (all units, average)

### Units benefitting most from Phraesto

Phraesto provides Damage taken reduction to single targets `low`, Healing to single targets `low`, Max HP buff to single targets `average`, and Shield to single targets `average`.

- Nerion (2.0 / 5)
- Perseus (1.8 / 5)
- Silven (1.7 / 5)

### Units that can act as a replacement for Phraesto

**Buffs on allies**

- Himmel (60% `Max HP`)
- Koko (60% `Max HP` `Damage taken reduction`)
- Twins (60% `Max HP`)

**Healing**

- Contess (100% `Healing`)
- Evie (100% `Healing`)
- Hepler (100% `Healing`)

**Damage**

- Aurora (100% `Magic`)
- Bonnie (100% `Magic`)
- Callan (100% `Magic`)

**Crowd Control**

- Hepler (100% `Stun` `Taunt`)
- Brutus (60% `Taunt`)
- Callan (60% `Stun`)

### Summary for Phraesto

#### Phraesto Provides

- Summoning — Area

#### Damage types dealt by Phraesto

- Magic — Area, Single target

#### Crowd Control provided by Phraesto

- Stun (Mythic+) — Single target — `average`
- Taunt (Mythic+) — Single target — `average`

## Pippa

### Pippa's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Wild Shift (ultimate)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Magic `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `average`, damage `average`
- **Non-ultimate**: speed `fast`, debuffs `average`, damage `average`

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
Common buffers are **Twins**, **Hugin**, or **Galahad**.

- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Isabella**
  - Haste buff (multiple targets, low) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Dunlingr**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Marcille**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Pippa

- Bonnie (2.5 / 5)
- Nerion (1.6 / 5)
- Indris (1.5 / 5)

### Units that can act as a replacement for Pippa

**Similar Skills**

- Kordan (100% `hp-scaling` `self-repositioner`)
- Athalia (80% `hp-scaling` `self-repositioner`)
- Silven (60% `hp-scaling`)

**Damage**

- Aurora (100% `Magic`)
- Bonnie (100% `Magic`)
- Callan (100% `Magic`)

**Debuffs on enemies**

- Dunlingr (100% `Energy drain`)
- Lily May (100% `Energy drain`)
- Rowan (100% `Energy drain`)

**Crowd Control**

- Eironn (84% `Bind` `Displace`)
- Evie (70% `Bind` `Displace`)
- Kordan (60% `Bind` `Knock down`)

### Summary for Pippa

#### Damage types dealt by Pippa

- Magic — Area, Multiple targets, Single target

#### Debuffs provided by Pippa

- Energy drain — Single target — `average`

#### Crowd Control provided by Pippa

- Unaffected — Self — On skill
- Bind — Single target — `average`
- Displace — Single target — `low`
- Knock down — Single target — `low`

## Ravion

### Ravion's behavior

`AFK Stages [A]`, `Dream Realm [S]`, `Dream Realm (Endless) [A]`, `PVP [A+]`

- **Signature skill**: Killer Flush (ultimate)
- **Movement**: high movement (repositioning skills)
- **Ally composition**: Objectives go to the 2 rearmost allies; backline heroes receive ATK and Energy on completion
- **Damage types**: Physical `average`, HP loss `low`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `low`
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
Common buffers are **Twins**, **Hugin**, or **Galahad**.

- **Mehira**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Velara**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, high) `signature fuel`
- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Tasi**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Ravion

Ravion provides ATK buff to multiple targets `average`, Energy recovery to multiple targets `average`, Lifedrain buff (EX+10) to single targets `low` — conditional (rare), and Shield (EX+10) to single targets `low` — conditional (rare).

**22** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Arden (4.3 / 5)
- Lily May (4.0 / 5)
- Valen (4.0 / 5)
- Hodgkin (3.7 / 5)
- Cryonaia (3.3 / 5)
- Aliceth (3.0 / 5)
- Kordan (2.9 / 5)
- Cyran (2.7 / 5)
- Frieren (2.4 / 5)
- Sylphira (2.3 / 5)

### Units that can act as a replacement for Ravion

**Buffs on allies**

- Twins (75% `ATK` `Energy`)
- Kordan (60% `ATK`)

**Similar Skills**

- Hugin (66% `ally-shielder` `energy-provider`)

**Damage**

- Aliceth (100% `Physical` `HP loss`)
- Faramor (100% `Physical` `HP loss`)
- Kordan (100% `Physical` `HP loss`)

**Debuffs on enemies**

- Zanie (100% `ATK debuff` `Phys DEF debuff`)

**Crowd Control**

- Kordan (60% `Knock down`)

### Summary for Ravion

#### Damage types dealt by Ravion

- Physical — Area, Multiple targets, Single target
- HP loss — Single target — `average`

#### Debuffs provided by Ravion

- ATK — Single target — `average`
- Phys DEF — Single target — `average`

#### Crowd Control provided by Ravion

- Unaffected — Self — Start of battle
- Displace — Single target — `low`
- Knock down — Single target — `low`

## Reinier

### Reinier's behavior

`AFK Stages [B]`, `Dream Realm [A]`, `Dream Realm (Endless) [A]`, `PVP [B]`

- **Signature skill**: Dynamic Balance (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Magic `average`

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, heal `average`
- **Ultimate**: speed `slow`, damage `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, debuffs `average`, damage `low`

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
Common buffers are **Solise**, **Contess**, or **Rowan**.

- **Velara**
  - Healing (area, low)
- **Pandora**
  - Healing (single target, average)
- **Zanie**
  - Healing (single target, average)
- **Hewynn**
  - Healing (all units, average)
- **Koko**
  - Healing (all units, average)

### Units benefitting most from Reinier

Reinier provides ATK buff (Legendary+) to single targets `low`.

- Bonnie (2.4 / 5)
- Indris (1.8 / 5)
- Himmel (1.7 / 5)

### Units that can act as a replacement for Reinier

**Buffs on allies**

- Aliceth (100% `ATK`)
- Alna (100% `ATK`)
- Contess (100% `ATK`)

**Damage**

- Aurora (100% `Magic`)
- Bonnie (100% `Magic`)
- Cryonaia (100% `Magic`)

**Debuffs on enemies**

- Bonnie (100% `ATK debuff` `Damage taken debuff`)
- Cyran (66% `ATK debuff`)
- Ravion (66% `ATK debuff`)

**Crowd Control**

- Kulu (60% `Displace` `Knock up`)
- Saida (60% `Displace` `Interrupt`)

### Summary for Reinier

#### Damage types dealt by Reinier

- Magic — Multiple targets, Single target

#### Debuffs provided by Reinier

- ATK (Legendary+) — Single target — `average`
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

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Flame Barrage (ultimate)
- **Movement**: high movement (moves while attacking)
- **Damage types**: Physical `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `average`
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
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Tasi**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
- **Pandora**
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Cecia**
  - ATK SPD buff (single target, high) `signature fuel`

### Units benefitting most from Rhys

Rhys provides Crit buff to single targets `low`, Healing to single targets `low`, and Movement speed buff (Mythic+) to single targets `low`.

- Silven (1.3 / 5)
- Nerion (1.3 / 5)
- Perseus (1.3 / 5)

### Units that can act as a replacement for Rhys

**Buffs on allies**

- Seth (72% `Crit`)

**Healing**

- Contess (100% `Healing`)
- Damian (100% `Healing`)
- Evie (100% `Healing`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Aliceth (100% `Knock back`)
- Alsa (100% `Knock back`)
- Atalanta (100% `Knock back`)

### Summary for Rhys

#### Damage types dealt by Rhys

- Physical — Arc, Single target

#### Crowd Control provided by Rhys

- Immune — Single target — Conditional
- Knock back — Single target — `low`

## Rowan

### Rowan's behavior

`AFK Stages [A]`, `Dream Realm [A]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Fatal Greed (ultimate)
- **Movement**: moving (repositions on cast)
- **Damage types**: Magic `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `average`, buffs `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `average`

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

Look for units providing: `Haste` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Galahad**.

- **Isabella**
  - Haste buff (multiple targets, low) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Dunlingr**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
- **Mehira**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Velara**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, high) `signature fuel`

### Units benefitting most from Rowan

Rowan provides Energy recovery in an area `high`, Healing in an area `low`, DEF buff (Mythic+) to single targets `high`, and Max HP buff (Mythic+) to single targets `high`.

**61** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Antandra (5.0 / 5)
- Granny Dahnie (5.0 / 5)
- Niru (5.0 / 5)
- Seth (3.7 / 5)
- Temesia (3.6 / 5)
- Soren (3.5 / 5)
- Hepler (3.4 / 5)
- Perseus (3.3 / 5)
- Mikola (3.3 / 5)
- Zorya (3.2 / 5)

### Units that can act as a replacement for Rowan

**Healing**

- Contess (100% `Healing`)
- Solise (100% `Healing`)
- Velara (100% `Healing`)

**Similar Skills**

- Twins (80% `ally-healer` `energy-provider`)

**Damage**

- Aurora (100% `Magic`)
- Cryonaia (100% `Magic`)
- Cyran (100% `Magic`)

**Debuffs on enemies**

- Dunlingr (100% `Energy drain`)
- Sylphira (66% `Energy drain`)

### Summary for Rowan

#### Rowan Provides

- Energy steal — Single target

#### Damage types dealt by Rowan

- Magic — Single target

#### Debuffs provided by Rowan

- Energy drain — Single target — `high`

## Saida

### Saida's behavior

`AFK Stages [S+]`, `Dream Realm [A]`, `Dream Realm (Endless) [A]`, `PVP [S+]`

- **Signature skill**: Seed Siphon (ultimate)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Magic `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `fast`, debuffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `high`

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
Common buffers are **Contess**, **Solise**, or **Twins**.

- **Velara**
  - Healing (area, low)
- **Hepler**
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, average)
- **Hewynn**
  - Healing (all units, average)
- **Lorsan**
  - Healing (all units, average)

### Units benefitting most from Saida

Saida provides Shield to multiple targets `high`.

**13** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Daimon (5.0 / 5)
- Gerda (5.0 / 5)
- Kruger (2.9 / 5)
- Athalia (2.8 / 5)
- Alna (2.5 / 5)
- Eironn (2.4 / 5)
- Cryonaia (2.3 / 5)
- Baelran (2.2 / 5)
- Shadewing (2.2 / 5)
- Faramor (1.9 / 5)

### Units that can act as a replacement for Saida

**Damage**

- Solise (100% `Magic`)
- Twins (80% `Magic`)
- Velara (80% `Magic`)

### Summary for Saida

#### Saida Provides

- Revive ally — Single target

#### Damage types dealt by Saida

- Magic — All units, Area, Single target

#### Crowd Control provided by Saida

- Unaffected — Self — Conditional
- Displace — Single target — `low`
- Interrupt — Single target — `low`

## Salazer

### Salazer's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Spirit Shackles (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Damage types**: Physical `average`

#### Skill overview

- **Signature skill**: speed `fast`, damage `average`
- **Ultimate**: speed `slow`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, damage `average`

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

Look for units providing: `Max HP` `Healing`  
Common buffers are **Contess**, **Smokey & Meerky**, or **Mikola**.

- **Hepler**
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, average)
- **Hewynn**
  - Healing (all units, average)
- **Lorsan**
  - Healing (all units, average)
- **Saida**
  - Max HP via Shield (multiple targets, high)

### Units benefitting most from Salazer

Salazer provides Lifedrain buff to single targets `low` and Shield (Supreme+) to single targets `low` — conditional (frequent).

- Carolina (2.2 / 5)
- Nerion (2.0 / 5)
- Perseus (1.2 / 5)

### Units that can act as a replacement for Salazer

**Buffs on allies**

- Daimon (100% `Life Drain` `Max HP`)
- Koko (100% `Life Drain` `Max HP`)
- Cecia (72% `Life Drain`)

**Similar Skills**

- Zorya (80% `hp-scaling` `life-drain`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Alna (100% `Bind`)
- Carolina (100% `Bind`)
- Evie (100% `Bind`)

### Summary for Salazer

#### Damage types dealt by Salazer

- Physical — Arc, Single target

#### Crowd Control provided by Salazer

- Bind — Single target — `high`

## Satrana

### Satrana's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Fiery Dance (ultimate)
- **Movement**: moving (avg attack range 1.5 tiles)
- **Damage types**: Magic `average`, Max HP-based damage `low`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `average`, damage `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `average`

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
Common buffers are **Twins**, **Rowan**, or **Lyca**.

- **Pandora**
  - Max HP buff (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Hepler**
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Phraesto**
  - Max HP via Shield (single target, average)
  - Energy via Energy recovery speed (contract ally, start of battle) `signature fuel`

### Units benefitting most from Satrana

- Shadewing (2.6 / 5)
- Bonnie (2.5 / 5)
- Indris (2.2 / 5)

### Units that can act as a replacement for Satrana

**Damage**

- Daimon (100% `Magic` `Max HP-based damage`)
- Shemira (100% `Magic` `Max HP-based damage`)
- Lily May (93% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Frieren (75% `DoT` `Vitality debuff`)

**Crowd Control**

- Mehira (100% `Charm`)

### Summary for Satrana

#### Satrana Provides

- Ally Vitality debuff on enemies — Area
- Ally grant (Sparks) — Area
- Invincibility — Self

#### Damage types dealt by Satrana

- Magic — Arc, Area, Single target
- Max HP-based damage — Arc — `low`

#### Debuffs provided by Satrana

- DoT — Multiple targets — `low`
- Vitality — Multiple targets — `low`

#### Crowd Control provided by Satrana

- Charm — Single target — `average`

## Scarlita

### Scarlita's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Divine Wrath (Mythic+)
- **Movement**: moving (brief reposition)
- **Damage types**: Physical `high`

#### Skill overview

- **Signature skill**: speed `fast`
- **Ultimate**: speed `slow`, damage `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, damage `average`

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
Common buffers are **Rowan**, **Smokey & Meerky**, or **Ravion**.

- **Thador**
  - Energy recovery (single target, low) `signature fuel`
- **Thoran**
  - Energy recovery (single target, low) `signature fuel`
- **Ulmus**
  - Energy recovery (single target, low) `signature fuel`
- **Seth**
  - Energy recovery (single target, high) `signature fuel`
- **Arden**
  - Energy recovery (single target, low) `signature fuel`

### Units benefitting most from Scarlita

Scarlita provides Shield to single targets `low` and DEF buff (Supreme+) to single targets `average`.

- Carolina (2.3 / 5)
- Nerion (2.1 / 5)
- Silven (1.5 / 5)

### Units that can act as a replacement for Scarlita

**Buffs on allies**

- Twins (80% `Magic DEF` `Max HP` `Physical DEF`)
- Hepler (66% `Magic DEF` `Max HP` `Physical DEF`)
- Rowan (66% `Magic DEF` `Physical DEF`)

**Similar Skills**

- Zandrok (60% `aoe-damage` `hp-scaling`)

**Damage**

- Alna (100% `Physical`)
- Athalia (100% `Physical`)
- Dionel (100% `Physical`)

**Crowd Control**

- Cassadee (64% `Knock back` `Knock up` `Stun`)

### Summary for Scarlita

#### Scarlita Provides

- Invincibility — Self

#### Damage types dealt by Scarlita

- Physical — All units, Arc, Area, Single target

#### Crowd Control provided by Scarlita

- Unaffected — Self — Conditional
- Knock back — All units — `low`
- Knock down — Arc — `low`
- Knock up — Area — `low`
- Stun — Single target — `average`

## Seth

### Seth's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Shadow Strike (ultimate)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Physical `low`, HP loss `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `average`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `low`

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
Common buffers are **Twins**, **Rowan**, or **Mikola**.

- **Lucca**
  - DEF buff (area, high)
  - DEF buff (area, high)
- **Sonja**
  - ATK buff (multiple targets, high)
  - DEF buff (multiple targets, average)
  - DEF buff (multiple targets, average)
- **Lumont**
  - DEF buff (multiple targets, high)
  - DEF buff (multiple targets, high)
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, average, conditional (frequent))
  - DEF buff (multiple targets, low)
  - DEF buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`
- **Koko**
  - Healing (all units, average)
  - Lifedrain buff (multiple targets, average)

### Units benefitting most from Seth

Seth provides Crit buff to single targets `low` and Energy recovery (Mythic+) to single targets `high`.

- Silven (1.6 / 5)
- Nerion (1.6 / 5)
- Perseus (1.4 / 5)

### Units that can act as a replacement for Seth

**Buffs on allies**

- Smokey & Meerky (90% `Energy`)
- Lyca (75% `Energy`)
- Ravion (75% `Energy`)

**Similar Skills**

- Harak (80% `assassin` `life-drain`)

**Damage**

- Aliceth (100% `Physical` `HP loss`)
- Faramor (100% `Physical` `HP loss`)
- Harak (100% `Physical` `HP loss`)

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

- Physical — Single target
- HP loss — Single target — `low`

#### Debuffs provided by Seth

- Phys DEF (Supreme+) — Single target — `low`

#### Crowd Control provided by Seth

- Bind — Single target — `low`

## Shadewing

### Shadewing's behavior

`AFK Stages [A+]`, `Dream Realm [S]`, `Dream Realm (Endless) [B]`, `PVP [S+]`

- **Signature skill**: Withering Curse (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Damage types**: Magic `low`, DoT `average`, HP loss `low`

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

Look for units providing: `ATK` `Max HP` `Energy` `Life Drain`  
Common buffers are **Twins**, **Contess**, or **Hugin**.

Shadewing also requires units **dealing continuous damage** to enemies and/or units **putting debuffs** on enemies

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Gunnar**
  - Enables Continuous damage on enemies via DoT
- **Velara**
  - Enables Debuff on target via Magic DEF debuff (single target)
- **Baelran**
  - Enables Debuff on target via Max HP debuff (single target)
- **Mehira**
  - Enables Debuff on target via Damage taken debuff (single target)

### Units benefitting most from Shadewing

- Bonnie (2.2 / 5)
- Indris (1.6 / 5)
- Aliceth (1.4 / 5)

### Units that can act as a replacement for Shadewing

**Debuffs on enemies**

- Velara (100% `Magic DEF debuff` `Phys DEF debuff`)

### Summary for Shadewing

#### Shadewing Provides

- Debuff application — Single target
- DoT conversion — All units
- Invincibility — Self
- Damage leech from allies (Supreme+) — Self

#### Damage types dealt by Shadewing

- Magic — Single target
- DoT — Single target
- HP loss — Single target — `low`

#### Debuffs provided by Shadewing

- Magic DEF — Single target — `average`
- Phys DEF — Single target — `low`

## Shakir

### Shakir's behavior

`AFK Stages [B]`, `Dream Realm [B]`, `Dream Realm (Endless) [B]`, `PVP [A]`

- **Signature skill**: Ravaging Claws (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Damage types**: Physical `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `average`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `average`

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
Common buffers are **Twins**, **Hugin**, or **Galahad**.

- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Isabella**
  - Haste buff (multiple targets, low) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Dunlingr**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD buff (all units, low) `signature fuel`
- **Mehira**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Velara**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Shakir

Shakir provides Damage taken reduction to multiple targets `average`, Haste buff to multiple targets `high`, and Lifedrain buff to single targets `average`.

**12** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Sinbad (3.2 / 5)
- Atalanta (3.1 / 5)
- Pang (3.0 / 5)
- Dionel (2.9 / 5)
- Korin (2.9 / 5)
- Soren (2.8 / 5)
- Mikola (2.8 / 5)
- Lenya (2.7 / 5)
- Hepler (2.6 / 5)
- Zorya (2.5 / 5)

### Units that can act as a replacement for Shakir

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

- Physical — Arc, Area

#### Debuffs provided by Shakir

- Vitality (Supreme+) — Single target — `low`

#### Crowd Control provided by Shakir

- Unaffected — Self — Form

## Shemira

### Shemira's behavior

`AFK Stages [A]`, `Dream Realm [S+]`, `Dream Realm (Endless) [A]`, `PVP [A+]`

- **Signature skill**: Phantom Procession (ultimate)
- **Movement**: mostly stationary (avg attack range 4.0 tiles)
- **Damage types**: Magic `high`, Max HP-based damage `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `average`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `average`, damage `high`

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

Look for units providing: `Max HP` `Healing` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Contess**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
  - Healing (single target, average)
- **Velara**
  - Healing (area, low)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, high) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, low) `signature fuel`

### Units benefitting most from Shemira

- Bonnie (1.8 / 5)
- Himmel (1.6 / 5)

### Units that can act as a replacement for Shemira

**Damage**

- Silven (92% `Max HP-based damage` `Magic`)
- Gunnar (84% `Max HP-based damage`)

### Summary for Shemira

#### Damage types dealt by Shemira

- Magic — All units, Area, Single target
- Max HP-based damage — Area, Single target — `average`

## Silven

### Silven's behavior

`AFK Stages [S]`, `Dream Realm [S]`, `Dream Realm (Endless) [A+]`, `PVP [A+]`

- **Signature skill**: Gravity Collapse (Skill 1)
- **Movement**: stationary (avg attack range 12.0 tiles)
- **Damage types**: Magic `high`, Max HP-based damage `low`

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
Common buffers are **Twins**, **Contess**, or **Solise**.

Silven also requires units **buffing them**

- **Gunnar**
  - ATK SPD buff (single target, high) `signature fuel`
  - Grants 4 distinct stat buffs to Silven (start of battle)
- **Velara**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - DEF buff (single target, average)
  - Grants 3 distinct stat buffs to Silven (start of battle)
- **Saida**
  - Grants 1 distinct stat buff to Silven
- **Aliceth**
  - DEF Penetration buff (multiple targets, high)
  - Grants 4 distinct stat buffs to Silven
- **Tilaya**
  - DEF buff (area, average)
  - Grants 2 distinct stat buffs to Silven (start of battle)

### Units benefitting most from Silven

Silven provides DEF Penetration buff (Mythic+) to single targets `low`.

- Carolina (1.8 / 5)
- Nerion (1.7 / 5)
- Bonnie (1.6 / 5)

### Units that can act as a replacement for Silven

**Damage**

- Gunnar (86% `Max HP-based damage`)

**Crowd Control**

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
- **Damage types**: Physical `average`

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, damage `average`
- **Ultimate**: speed `average`, debuffs `average`, damage `average`
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

Look for units providing: `Max HP` `CRIT`  
Common buffers are **Hugin**, **Galahad**, or **Contess**.

- **Hepler**
  - Max HP via Shield (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Koko**
  - Max HP via Shield (all units, low)
- **Lenya**
  - Max HP via Shield (single target, high)
- **Zanie**
  - Max HP via Shield (single target, high)

### Units benefitting most from Silvina

- Carolina (3.1 / 5)
- Nerion (2.6 / 5)
- Indris (1.8 / 5)

### Units that can act as a replacement for Silvina

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Debuffs on enemies**

- Lily May (90% `Energy drain`)
- Dunlingr (75% `Energy drain`)
- Rowan (75% `Energy drain`)

**Crowd Control**

- Berial (65% `Frighten`)
- Daimon (65% `Frighten`)

### Summary for Silvina

#### Silvina Provides

- Marked target (focus fire) — Single target

#### Damage types dealt by Silvina

- Physical — Single target

#### Debuffs provided by Silvina

- Energy drain — Single target — `high`
- Vitality (Supreme+) — Single target — `low`

#### Crowd Control provided by Silvina

- Stun — Single target — `high`
- Frighten (EX+10) — Area — `average`

## Sinbad

### Sinbad's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Whizzing Edge (ultimate)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Physical `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `average`, damage `average`
- **Non-ultimate**: speed `fast`, debuffs `average`, damage `average`

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
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Tasi**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, high) `signature fuel`

### Units benefitting most from Sinbad

- Indris (2.8 / 5)
- Bonnie (2.2 / 5)
- Aliceth (1.9 / 5)

### Units that can act as a replacement for Sinbad

**Similar Skills**

- Kruger (60% `enemy-debuffer`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

### Summary for Sinbad

#### Sinbad Provides

- Marked target (focus fire) — Multiple targets

#### Damage types dealt by Sinbad

- Physical — Multiple targets, Single target

#### Debuffs provided by Sinbad

- Damage taken — Single target — `low`
- Magic DEF (Mythic+) — Multiple targets — `average`
- Phys DEF (Mythic+) — Multiple targets — `low`
- Vitality (Mythic+) — Multiple targets — `average`

#### Crowd Control provided by Sinbad

- Unaffected — Multiple targets — Conditional

## Smokey & Meerky

### Smokey & Meerky's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [S]`, `PVP [C]`

- **Signature skill**: Special Aroma (ultimate)
- **Movement**: stationary (no finite attack range)
- **Damage types**: Magic `low`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `average`, buffs `average`
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
Common buffers are **Mikola**, **Contess**, or **Rowan**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (single target, high)
- **Koko**
  - Healing (all units, average)
- **Zanie**
  - ATK buff (single target, low)
  - Healing (single target, average)
- **Velara**
  - Healing (area, low)
- **Pandora**
  - Healing (single target, average)

### Units benefitting most from Smokey & Meerky

Smokey & Meerky provides Energy recovery in an area `average`, Healing in an area `high`, and ATK buff (Legendary+) to multiple targets `low`.

**25** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner

These are the **10** strongest pairings: 

- Contess (5.0 / 5)
- Hodgkin (4.2 / 5)
- Phraesto (4.0 / 5)
- Harak (3.7 / 5)
- Hammie (3.7 / 5)
- Marcille (3.6 / 5)
- Antandra (3.6 / 5)
- Granny Dahnie (3.2 / 5)
- Zorya (3.2 / 5)
- Mikola (2.4 / 5)

### Units that can act as a replacement for Smokey & Meerky

**Buffs on allies**

- Rowan (87% `Energy`)
- Ravion (81% `Energy` `ATK`)
- Twins (65% `ATK` `Energy`)

**Healing**

- Koko (100% `Healing`)
- Solise (100% `Healing`)
- Contess (90% `Healing`)

**Similar Skills**

- Solise (80% `ally-healer` `aoe-healing`)
- Velara (60% `ally-healer` `aoe-healing`)

**Damage**

- Aurora (100% `Magic`)
- Bonnie (100% `Magic`)
- Callan (100% `Magic`)

**Crowd Control**

- Lily May (60% `Interrupt`)
- Sylphira (60% `Interrupt`)

### Summary for Smokey & Meerky

#### Crowd Control provided by Smokey & Meerky

- Interrupt — Single target — `low`
- Stun (Mythic+) — Single target — `low`

## Solise

### Solise's behavior

`AFK Stages [S]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S]`, `PVP [S]`

- **Signature skill**: Life's Embrace (ultimate)
- **Movement**: stationary (no finite attack range)
- **Damage types**: Magic `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `average`, heal `average`, damage `high`
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
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Gunnar**
  - ATK buff (single target, low)
  - ATK SPD buff (single target, high) `signature fuel`
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, low, conditional (frequent))
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
- **Tasi**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Solise

Solise provides ATK buff to summons `high` — conditional (frequent), Healing to all units `average`, Healing over time to single targets `high`, Shield to summons `average`, and DEF buff (Mythic+) to summons `low`.

**24** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Phraesto (4.9 / 5)
- Berial (4.6 / 5)
- Dunlingr (4.4 / 5)
- Mehira (3.0 / 5)
- Laios (3.0 / 5)
- Niru (2.9 / 5)
- Himmel (2.7 / 5)
- Bryon (2.7 / 5)
- Alna (2.7 / 5)
- Silven (2.1 / 5)

### Units that can act as a replacement for Solise

**Similar Skills**

- Twins (60% `ally-healer` `ally-shielder`)

**Damage**

- Twins (96% `Magic`)

### Summary for Solise

#### Solise Provides

- Ally blessing (Mythic+) — Single target

#### Damage types dealt by Solise

- Magic — All units

#### Crowd Control provided by Solise

- Unaffected — Self — Start of battle

## Sonja

### Sonja's behavior

`AFK Stages [C]`, `Dream Realm [B]`, `Dream Realm (Endless) [B]`, `PVP [B]`

- **Signature skill**: Crimson Covenant (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Ally composition**: place allies on left and right at battle start (Crimson Covenant buffs; prioritizes front row)
- **Damage types**: Physical `average`

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `average`
- **Ultimate**: speed `slow`, damage `average`
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
Common buffers are **Twins**, **Hugin**, or **Galahad**.

- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, low)
- **Koko**
  - Max HP via Shield (all units, low)

### Units benefitting most from Sonja

Sonja provides ATK buff to multiple targets `high` and DEF buff to multiple targets `average`.

- Kordan (3.5 / 5)
- Hepler (2.5 / 5)
- Silven (2.4 / 5)

### Units that can act as a replacement for Sonja

**Buffs on allies**

- Evie (86% `ATK`)
- Hugin (86% `ATK`)
- Mikola (72% `ATK`)

**Similar Skills**

- Perseus (60% `ally-buffer`)
- Silven (60% `hp-scaling`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Crowd Control**

- Aliceth (100% `Stun`)
- Bonnie (100% `Stun`)
- Callan (100% `Stun`)

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
- **Damage types**: Physical `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
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
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, average)
- **Pandora**
  - Max HP buff (single target, average)
  - Healing (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, low)
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Soren

Soren provides Haste buff (Legendary+) to single targets `low` and Shield (Supreme+) to single targets `average`.

- Carolina (2.7 / 5)
- Nerion (2.6 / 5)
- Perseus (1.5 / 5)

### Units that can act as a replacement for Soren

**Buffs on allies**

- Galahad (100% `Max HP` `Haste`)
- Hepler (100% `Max HP` `Haste`)
- Hugin (100% `Max HP` `Haste`)

**Similar Skills**

- Lenya (66% `counterattack` `self-repositioner`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Crowd Control**

- Perseus (100% `Stun` `Knock back`)
- Lorsan (72% `Stun`)
- Zorya (72% `Stun`)

### Summary for Soren

#### Damage types dealt by Soren

- Physical — Area, Multiple targets, Single target

#### Crowd Control provided by Soren

- Knock back — Area — `low`
- Stun — Multiple targets — `average`

## Sylphira

### Sylphira's behavior

`AFK Stages [A]`, `Dream Realm [A+]`, `Dream Realm (Endless) [?]`, `PVP [S]`

- **Signature skill**: Grand Finale (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Damage types**: Magic `high`, Max HP-based damage `low`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `average`, debuffs `average`, damage `high`
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

Look for units providing: `ATK` `Haste` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Ravion**.

- **Velara**
  - Haste buff (single target, low) `signature fuel`
  - Healing (area, low)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Zanie**
  - ATK buff (single target, low)
  - Healing (single target, average)
- **Mehira**
  - Haste buff (single target, low) `signature fuel`
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, high) `signature fuel`
- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`

### Units benefitting most from Sylphira

- Carolina (3.1 / 5)
- Nerion (2.6 / 5)
- Bonnie (2.5 / 5)

### Units that can act as a replacement for Sylphira

**Damage**

- Shemira (100% `Magic` `Max HP-based damage`)
- Silven (99% `Magic` `Max HP-based damage`)
- Gunnar (72% `Max HP-based damage`)

**Crowd Control**

- Baelran (76% `Knock down`)

### Summary for Sylphira

#### Sylphira Provides

- Dispel debuffs (Mythic+) — Self
- Stacking buff (Mythic+) — Self

#### Damage types dealt by Sylphira

- Magic — Area, Single target
- Max HP-based damage — Single target — `low`

#### Debuffs provided by Sylphira

- Energy drain — Single target — `average`

#### Crowd Control provided by Sylphira

- Immune — Self — On skill
- Unaffected — Area — Conditional
- Cleanse (Mythic+) — Self — On skill
- Interrupt — Single target — `low`
- Knock down — Area — `average`
- Silence — Single target — `low`

## Talene

### Talene's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [A]`, `PVP [B]`

- **Signature skill**: Divine Conflagration (ultimate)
- **Movement**: moving (avg attack range 3.0 tiles)
- **Ally composition**: frontmost ally carries Pyre of Renewal (AoE damage and healing)
- **Damage types**: Magic `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `low`
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
Common buffers are **Mikola**, **Contess**, or **Twins**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, average)
  - Lifedrain buff (multiple targets, average)
- **Hepler**
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
- **Kordan**
  - ATK buff (multiple targets, high)
  - Lifedrain buff (multiple targets, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (single target, high)
- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)

### Units benefitting most from Talene

Talene provides Healing in an area `low`, Healing over time in an area `low`, and ATK buff (Legendary+) in an area `high`.

- Shadewing (3.6 / 5)
- Himmel (3.4 / 5)
- Silven (2.5 / 5)

### Units that can act as a replacement for Talene

**Buffs on allies**

- Mikola (100% `ATK`)
- Kordan (90% `ATK`)
- Evie (75% `ATK`)

**Healing**

- Solise (100% `Healing` `Healing over time`)
- Mikola (87% `Healing over time` `Healing`)
- Nara (60% `Healing`)

**Damage**

- Aurora (100% `Magic`)
- Bonnie (100% `Magic`)
- Callan (100% `Magic`)

**Crowd Control**

- Cassadee (100% `Knock back`)
- Indris (100% `Knock back`)
- Lenya (100% `Knock back`)

### Summary for Talene

#### Talene Provides

- Transformation — Self
- Stacking buff (Mythic+) — Area

#### Damage types dealt by Talene

- Magic — Area, Single target

#### Crowd Control provided by Talene

- Knock back — Area — `low`

## Tasi

### Tasi's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Eternal Dreamscape (ultimate)
- **Movement**: stationary (avg attack range 10.0 tiles)
- **Damage types**: Magic `average`, DoT `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `low`
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
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Talene**
  - ATK buff (area, high)
  - Healing (area, low)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, average)
- **Pandora**
  - Max HP buff (single target, average)
  - Healing (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (single target, high)

### Units benefitting most from Tasi

Tasi provides Haste buff (Mythic+) to single targets `high`.

- Carolina (2.8 / 5)
- Nerion (2.6 / 5)
- Perseus (1.6 / 5)

### Units that can act as a replacement for Tasi

**Buffs on allies**

- Damian (100% `Haste`)
- Galahad (100% `Haste`)
- Hugin (100% `Haste`)

**Damage**

- Frieren (100% `DoT` `Magic`)
- Bryon (73% `DoT` `Magic`)
- Eironn (64% `Magic`)

### Summary for Tasi

#### Tasi Provides

- Invincibility — Area
- Sleep (area) — Single target
- Transformation — Self

#### Damage types dealt by Tasi

- Magic — Area
- DoT — All units, Single target

#### Crowd Control provided by Tasi

- Bind — Single target — `average`
- Sleep — All units — `low`
- Stun — Area — `low`

## Temesia

### Temesia's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Knight's Heart (ultimate)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Physical `high`, Max HP-based damage `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, damage `low`

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

Look for units providing: `ATK` `ATK SPD / Haste` `Max HP` `Healing` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Rowan**.

- **Hepler**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Talene**
  - ATK buff (area, high)
  - Healing (area, low)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, average)
- **Pandora**
  - Max HP buff (single target, average)
  - Healing (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Temesia

- Carolina (2.0 / 5)
- Nerion (1.8 / 5)
- Himmel (1.6 / 5)

### Units that can act as a replacement for Temesia

**Similar Skills**

- Cassadee (72% `aoe-damage` `enemy-debuffer`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)
- Valka (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Atalanta (100% `Phys DEF debuff`)
- Brutus (100% `Phys DEF debuff`)
- Fay (100% `Phys DEF debuff`)

**Crowd Control**

- Lucca (100% `Knock down` `Interrupt`)
- Sylphira (100% `Knock down` `Interrupt`)
- Zorya (96% `Knock down`)

### Summary for Temesia

#### Temesia Provides

- Stacking buff — Single target

#### Damage types dealt by Temesia

- Physical — All units, Area, Single target
- Max HP-based damage — Single target — `average`

#### Debuffs provided by Temesia

- Phys DEF (Supreme+) — Single target — `low`

#### Crowd Control provided by Temesia

- Unaffected (Mythic+) — Self — Permanent
- Interrupt — Single target — `low`
- Knock down — Area — `low`

## Thador

### Thador's behavior

`AFK Stages [S]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A+]`

- **Signature skill**: Darkmoon Pact (Skill 1)
- **Movement**: moving (avg attack range 0.2 tiles)
- **Ally composition**: place lieutenant 1 tile behind at battle prep (Crit + shared shields)
- **Damage types**: Physical `high`

#### Skill overview

- **Signature skill**: speed `slow`, first cast speed `fast`, buffs `average`
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

Look for units providing: `Max HP` `CRIT` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
  - Healing (single target, average)
- **Velara**
  - Healing (area, low)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
- **Gunnar**
  - ATK SPD buff (single target, high) `signature fuel`

### Units benefitting most from Thador

Thador provides Energy recovery (EX+10) to single targets `low`.

- Pandora (1.5 / 5)

### Units that can act as a replacement for Thador

**Buffs on allies**

- Ravion (100% `Energy`)
- Rowan (100% `Energy`)
- Thoran (100% `Energy`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Debuffs on enemies**

- Velara (90% `Magic DEF debuff` `Phys DEF debuff`)
- Shadewing (75% `Magic DEF debuff` `Phys DEF debuff`)
- Eironn (60% `Magic DEF debuff`)

**Crowd Control**

- Athalia (100% `Knock down`)
- Baelran (100% `Knock down`)
- Frieren (100% `Knock down`)

### Summary for Thador

#### Damage types dealt by Thador

- Physical — Area, Single target

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
- **Ally composition**: place ally 1 tile behind at battle prep (Soul Pact damage share and revive)
- **Damage types**: Physical `average`

#### Skill overview

- **Signature skill**: speed `fast`
- **Ultimate**: speed `slow`, buffs `average`, damage `low`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `average`

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
Common buffers are **Rowan**, **Contess**, or **Twins**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
  - Healing (single target, average)
- **Velara**
  - Healing (area, low)
- **Thador**
  - Energy recovery (single target, low) `signature fuel`
- **Hepler**
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)

### Units benefitting most from Thoran

Thoran provides Lifedrain buff to single targets `high` and Energy recovery (Legendary+) to single targets `low`.

- Brutus (2.5 / 5)
- Pandora (1.5 / 5)

### Units that can act as a replacement for Thoran

**Buffs on allies**

- Dunlingr (90% `Life Drain`)
- Kordan (75% `Life Drain`)

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

- Physical — Single target

#### Crowd Control provided by Thoran

- Unaffected — Self — On skill
- Interrupt — Single target — `low`

## Tilaya

### Tilaya's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Wrath of the Wilds (ultimate)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Physical `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, heal `average`, buffs `average`, damage `low`
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

Look for units providing: `Max HP` `Healing`  
Common buffers are **Contess**, **Smokey & Meerky**, or **Mikola**.

- **Hepler**
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, average)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
  - Healing (single target, average)
- **Pandora**
  - Max HP buff (single target, average)
  - Healing (single target, average)

### Units benefitting most from Tilaya

Tilaya provides DEF buff (EX+10) in an area `average` and Max HP buff (EX+10) in an area `average`.

- Lucca (5.0 / 5)
- Granny Dahnie (2.8 / 5)

### Units that can act as a replacement for Tilaya

**Similar Skills**

- Silven (100% `hp-scaling`)
- Baelran (60% `hp-scaling`)
- Pippa (60% `hp-scaling`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

### Summary for Tilaya

#### Tilaya Provides

- Start-of-battle cast — Arc

#### Damage types dealt by Tilaya

- Physical — Arc, Area, Single target

#### Crowd Control provided by Tilaya

- Unaffected — Arc — Start of battle

## Twins

### Twins's behavior

`AFK Stages [S]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S+]`, `PVP [A+]`

- **Signature skill**: Starlight Waltz (ultimate)
- **Movement**: moving / stationary (two units)
- **Damage types**: Magic `low`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `average`
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
Common buffers are **Solise**, **Damian**, or **Rowan**.

Twins also requires units **positioned on their link**

- **Gunnar**
  - ATK SPD buff (single target, high) `signature fuel`
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Tasi**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Pandora**
  - Healing (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Twins

Twins provides ATK buff to multiple targets `average`, Energy recovery to multiple targets `low`, Haste buff to all units `high`, Healing to multiple targets `low`, Max HP buff to multiple targets `average`, Shield to single targets `low`, Vitality buff (Mythic+) to multiple targets `low`, and DEF buff (Supreme+) to single targets `low`.

**102** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight
- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner

These are the **10** strongest pairings: 

- Hepler (5.0 / 5)
- Lenya (5.0 / 5)
- Mikola (5.0 / 5)
- Nerion (5.0 / 5)
- Perseus (5.0 / 5)
- Seth (5.0 / 5)
- Silven (5.0 / 5)
- Soren (5.0 / 5)
- Tasi (5.0 / 5)
- Zorya (5.0 / 5)

### Units that can act as a replacement for Twins

**Healing**

- Solise (100% `Healing`)
- Contess (100% `Healing`)
- Damian (100% `Healing`)

**Similar Skills**

- Solise (60% `ally-healer` `ally-shielder`)

**Damage**

- Solise (100% `Magic`)

### Summary for Twins

#### Twins Provides

- Ally positioning link — Single target
- Shared HP and Energy — All units

#### Damage types dealt by Twins

- Magic — Area, Single target

#### Crowd Control provided by Twins

- Unaffected — Area — On skill
- Blind — Area — `average`
- Knock back — Area — `low`

## Ulmus

### Ulmus's behavior

`AFK Stages [B]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [A]`

- **Signature skill**: Way of the Forest (Skill 2)
- **Movement**: moving (stationary when rooted)
- **Ally composition**: when rooted, shields frontmost ally instead of self
- **Damage types**: Physical `average`

#### Skill overview

- **Signature skill**: speed `fast`, heal `average`, buffs `average`
- **Ultimate**: speed `slow`, heal `average`, damage `average`
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

Look for units providing: `Max HP` `Healing` `Energy`  
Common buffers are **Smokey & Meerky**, **Rowan**, or **Contess**.

- **Hepler**
  - Max HP via Shield (multiple targets, high)
  - Healing (multiple targets, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, average)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
  - Healing (single target, average)
- **Pandora**
  - Max HP buff (single target, average)
  - Healing (single target, average)

### Units benefitting most from Ulmus

Ulmus provides Energy recovery to single targets `low` and Shield to single targets `low`.

- Carolina (2.1 / 5)
- Nerion (2.0 / 5)
- Zorya (1.5 / 5)

### Units that can act as a replacement for Ulmus

**Buffs on allies**

- Twins (100% `Energy` `Max HP`)
- Lyca (72% `Energy`)
- Ravion (72% `Energy`)

**Similar Skills**

- Hepler (66% `ally-shielder` `transformation`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

**Crowd Control**

- Cassadee (100% `Knock back`)
- Indris (100% `Knock back`)
- Lenya (100% `Knock back`)

### Summary for Ulmus

#### Damage types dealt by Ulmus

- Physical — Area, Single target

#### Crowd Control provided by Ulmus

- Unaffected — Self — Conditional
- Knock back (Supreme+) — Area — `low`

## Vala

### Vala's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Swift Shift (ultimate)
- **Movement**: high movement (repositioning skills)
- **Damage types**: Physical `average`, HP loss `average`, True damage `low`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, heal `average`, buffs `average`, debuffs `average`, damage `low`

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
Common buffers are **Twins**, **Mikola**, or **Damian**.

Vala also requires enemies **to be defeated**

- **Talene**
  - ATK buff (area, high)
  - Healing (area, low)
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (single target, high)
- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Tasi**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Aliceth**
  - ATK buff (multiple targets, average)
  - Enables Enemy defeat via Instant defeat

### Units benefitting most from Vala

Vala provides Haste buff (Mythic+) to single targets `high`.

- Indris (2.3 / 5)
- Nerion (2.2 / 5)
- Perseus (1.6 / 5)

### Units that can act as a replacement for Vala

**Buffs on allies**

- Damian (100% `Haste`)
- Galahad (100% `Haste`)
- Hugin (100% `Haste`)

**Similar Skills**

- Athalia (60% `hp-scaling` `self-repositioner` `transformation`)

**Damage**

- Faramor (100% `HP loss` `Physical` `True damage`)
- Nara (100% `HP loss` `Physical` `True damage`)
- Aliceth (71% `HP loss` `Physical`)

**Debuffs on enemies**

- Aliceth (60% `Marked target (focus fire)`)
- Bryon (60% `Haste debuff`)

**Crowd Control**

- Damian (100% `Stun`)
- Faramor (100% `Stun`)
- Gwyneth (100% `Stun`)

### Summary for Vala

#### Vala Provides

- Marked target (focus fire) — Self

#### Damage types dealt by Vala

- Physical — Single target
- HP loss — Single target — `average`
- True damage — Single target — `low`

#### Debuffs provided by Vala

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
- **Damage types**: Physical `average`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `average`, damage `low`
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

Look for units providing: `ATK`  
Common buffers are **Twins**, **Lyca**, or **Mikola**.

- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Pandora**
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Isabella**
  - ATK buff (multiple targets, low, conditional (frequent))
  - ATK SPD via Haste buff (multiple targets, low) `signature fuel`
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`

### Units benefitting most from Valen

- Carolina (1.8 / 5)
- Nerion (1.6 / 5)
- Indris (1.3 / 5)

### Units that can act as a replacement for Valen

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Alna (100% `Haste debuff`)
- Bonnie (100% `Haste debuff`)
- Bryon (100% `Haste debuff`)

**Crowd Control**

- Aliceth (100% `Stun`)
- Alsa (100% `Stun`)
- Antandra (100% `Stun`)

### Summary for Valen

#### Valen Provides

- Invincibility — Self
- Stacking buff (Mythic+) — Single target

#### Damage types dealt by Valen

- Physical — Area, Single target

#### Debuffs provided by Valen

- Haste (Supreme+) — Single target — `low`

#### Crowd Control provided by Valen

- Stun (Supreme+) — Single target — `average`

## Valka

### Valka's behavior

`AFK Stages [C]`, `Dream Realm [A+]`, `Dream Realm (Endless) [B]`, `PVP [B]`

- **Signature skill**: Phantom Slasher (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Damage types**: Physical `high`, Max HP-based damage `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `fast`, first cast speed `fast`, heal `average`, damage `high`
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

Look for units providing: `ATK SPD / Haste` `Max HP` `Healing` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Smokey & Meerky**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, average)
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
  - Healing (single target, average)
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, low)

### Units benefitting most from Valka

Valka provides ATK SPD buff to multiple targets `low` and Lifedrain buff (EX+10) to single targets `average`.

- Nerion (1.6 / 5)
- Silven (1.6 / 5)
- Perseus (1.5 / 5)

### Units that can act as a replacement for Valka

**Buffs on allies**

- Dunlingr (100% `ATK SPD` `Life Drain`)
- Daimon (60% `Life Drain`)
- Kordan (60% `Life Drain`)

**Damage**

- Himmel (100% `Max HP-based damage` `Physical`)
- Daimon (97% `Max HP-based damage`)
- Shemira (97% `Max HP-based damage`)

**Crowd Control**

- Callan (100% `Stun` `Knock down`)
- Bonnie (86% `Stun`)
- Frieren (80% `Knock down` `Stun`)

### Summary for Valka

#### Damage types dealt by Valka

- Physical — Area, Single target
- Max HP-based damage — Area — `high`

#### Crowd Control provided by Valka

- Unaffected — Self — On skill
- Knock down — Single target — `low`
- Stun — Single target — `low`

## Velara

### Velara's behavior

`AFK Stages [S+]`, `Dream Realm [S+]`, `Dream Realm (Endless) [S]`, `PVP [B]`

- **Signature skill**: Ruthless Rite (ultimate)
- **Movement**: stationary (no finite attack range)
- **Damage types**: Magic `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, heal `average`, debuffs `average`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `high`

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

Look for units providing: `Haste` `Max HP` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Max HP via Shield (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, average)
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, low)
- **Koko**
  - Max HP via Shield (all units, low)

### Units benefitting most from Velara

Velara provides DEF buff to single targets `average`, Haste buff to single targets `low`, and Healing in an area `low`.

- Niru (2.6 / 5)
- Reinier (2.3 / 5)
- Silven (2.1 / 5)
- Contess (1.9 / 5)
- Saida (1.9 / 5)
- Baelran (1.7 / 5)
- Gwyneth (1.4 / 5)
- Hugin (1.3 / 5)
- Aurora (1.3 / 5)
- Galahad (1.3 / 5)

### Units that can act as a replacement for Velara

**Buffs on allies**

- Twins (80% `Haste` `Magic DEF` `Physical DEF`)

**Healing**

- Solise (100% `Healing`)
- Twins (90% `Healing`)
- Contess (100% `Healing`)

**Similar Skills**

- Solise (100% `ally-healer` `ally-shielder` `aoe-healing`)

**Damage**

- Solise (100% `Magic`)
- Twins (100% `Magic`)

**Crowd Control**

- Gwyneth (100% `Bind`)

### Summary for Velara

#### Velara Provides

- Start-of-battle cast — All units

#### Damage types dealt by Velara

- Magic — Area

#### Debuffs provided by Velara

- Haste — Single target — `low`
- Magic DEF — Single target — `average`
- Phys DEF — Single target — `low`

#### Crowd Control provided by Velara

- Bind — Single target — `high`

## Viperian

### Viperian's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [C]`

- **Signature skill**: Crimson Waltz (Mythic+)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)
- **Damage types**: Magic `high`

#### Skill overview

- **Signature skill**: speed `slow`, damage `low`
- **Ultimate**: speed `average`, first cast speed `fast`, heal `average`, damage `high`
- **Non-ultimate**: speed `slow`, heal `average`, debuffs `average`, damage `average`

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

- **Hepler**
  - Haste buff (single target, low) `signature fuel`
  - Healing (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Tasi**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Hewynn**
  - Healing (all units, average)
- **Koko**
  - Healing (all units, average)

### Units benefitting most from Viperian

- Shadewing (2.6 / 5)
- Bonnie (2.3 / 5)
- Indris (1.5 / 5)

### Units that can act as a replacement for Viperian

**Similar Skills**

- Arden (80% `aoe-damage` `dot-specialist`)
- Cecia (72% `dot-specialist` `life-drain`)
- Lorsan (66% `aoe-damage` `dot-specialist`)

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

- Magic — All units, Single target

#### Debuffs provided by Viperian

- Energy drain — Single target — `average`

#### Crowd Control provided by Viperian

- Unaffected — Self — Start of battle

## Walker

### Walker's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [B]`

- **Signature skill**: Six-Shot (ultimate)
- **Movement**: moving (avg attack range 2.0 tiles)
- **Damage types**: Physical `low`, Max HP-based damage `low`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, first cast speed `fast`, buffs `average`, debuffs `average`, damage `low`

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

Look for units providing: `Max HP` `CRIT` `CRIT DMG Boost` `Life Drain`  
Common buffers are **Twins**, **Rowan**, or **Lyca**.

- **Shakir**
  - Lifedrain buff (single target, average)
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Koko**
  - Max HP via Shield (all units, low)
  - Lifedrain buff (multiple targets, average)
- **Pandora**
  - Max HP buff (single target, average)
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Hepler**
  - Max HP via Shield (multiple targets, high)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Zandrok**
  - Max HP buff (multiple targets, low)
  - Lifedrain buff (area, low, conditional (frequent))
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Walker

Walker provides Crit buff to single targets `low`.

- Carolina (2.0 / 5)
- Nerion (1.6 / 5)
- Indris (1.3 / 5)

### Units that can act as a replacement for Walker

**Damage**

- Brutus (100% `Physical` `Max HP-based damage`)
- Gunnar (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Nazrik (100% `Crit Resist debuff`)

**Crowd Control**

- Damian (100% `Stun`)
- Gwyneth (100% `Stun`)
- Hepler (100% `Stun`)

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
- **Damage types**: Physical `low`

#### Skill overview

- **Signature skill**: speed `fast`, first cast speed `fast`, buffs `average`
- **Ultimate**: speed `slow`
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
Common buffers are **Twins**, **Hugin**, or **Contess**.

- **Kordan**
  - Lifedrain buff (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
  - Healing (single target, average)
- **Dunlingr**
  - Haste buff (single target, low) `signature fuel`
  - Lifedrain buff (all units, low)
- **Daimon**
  - Max HP via Shield (multiple targets, low)
  - Lifedrain buff (single target, average)

### Units benefitting most from Zandrok

Zandrok provides Haste buff in an area `low` — conditional (frequent), Lifedrain buff in an area `low` — conditional (frequent), and Max HP buff to multiple targets `low`.

- Brutus (2.1 / 5)
- Cassadee (1.9 / 5)
- Pippa (1.9 / 5)
- Shakir (1.9 / 5)

### Units that can act as a replacement for Zandrok

**Buffs on allies**

- Twins (63% `Haste` `Max HP`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Athalia (100% `Physical`)

### Summary for Zandrok

#### Crowd Control provided by Zandrok

- Knock up — Area — `low`
- Stun — Area — `low`

## Zanie

### Zanie's behavior

`AFK Stages [A+]`, `Dream Realm [S]`, `Dream Realm (Endless) [A+]`, `PVP [A]`

- **Signature skill**: Vein Pulse (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Damage types**: Physical `low`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, buffs `average`
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

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Twins**, **Hugin**, or **Galahad**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Gunnar**
  - ATK SPD buff (single target, high) `signature fuel`
- **Mehira**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Velara**
  - ATK SPD via Haste buff (single target, low) `signature fuel`
- **Florabelle**
  - Summon damage buff (summons only, average)
  - ATK SPD via Haste buff (summons only, average, conditional (frequent))

### Units benefitting most from Zanie

Zanie provides ATK buff to single targets `low`, Healing to single targets `average`, Shield to single targets `high`, DEF Penetration buff (Legendary+) to single targets `average`, and Max HP buff (Mythic+) to single targets `low`.

- Daimon (3.0 / 5)
- Aliceth (2.2 / 5)

### Units that can act as a replacement for Zanie

**Buffs on allies**

- Hugin (68% `Max HP` `ATK`)

**Healing**

- Contess (100% `Healing`)
- Solise (100% `Healing`)
- Twins (100% `Healing`)

**Damage**

- Baelran (100% `Physical`)
- Faramor (100% `Physical`)
- Gunnar (100% `Physical`)

**Crowd Control**

- Gwyneth (60% `Stun`)

### Summary for Zanie

#### Zanie Provides

- Summoning — Self

#### Damage types dealt by Zanie

- Physical — Single target

#### Debuffs provided by Zanie

- ATK (Supreme+) — Single target — `average`
- Phys DEF (Supreme+) — Single target — `average`

#### Crowd Control provided by Zanie

- Knock back — Single target — `low`
- Stun — Single target — `low`

## Zorya

### Zorya's behavior

`AFK Stages [C]`, `Dream Realm [C]`, `Dream Realm (Endless) [C]`, `PVP [S]`

- **Signature skill**: Guardian's Ring (ultimate)
- **Movement**: moving (inactive while dormant)
- **Damage types**: Magic `high`, HP loss `high`

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, first cast speed `fast`, heal `average`, buffs `average`, damage `high`
- **Non-ultimate**: speed `fast`, heal `average`, buffs `average`, damage `high`

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

Look for units providing: `Haste` `Max HP` `Healing` `Energy`  
Common buffers are **Twins**, **Rowan**, or **Hugin**.

Zorya also requires allies **casting ultimates**

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, average)
- **Velara**
  - Haste buff (single target, low) `signature fuel`
  - Healing (area, low)
  - ATK SPD via Haste buff (single target, low) `signature fuel`
  - Enables Ally Ultimate casts via Start-of-battle Ultimate
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, low)
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Evie**
  - Healing (single target, high)
  - Enables Ally Ultimate casts via Start-of-battle Ultimate

### Units benefitting most from Zorya

- Carolina (3.1 / 5)
- Nerion (2.6 / 5)
- Bonnie (1.9 / 5)

### Units that can act as a replacement for Zorya

**Similar Skills**

- Daimon (60% `hp-scaling` `life-drain`)
- Shemira (60% `hp-scaling` `life-drain`)

**Damage**

- Shadewing (100% `Magic` `HP loss`)
- Niru (94% `Magic` `HP loss`)
- Dunlingr (91% `HP loss` `Magic`)

**Crowd Control**

- Perseus (66% `Stun`)

### Summary for Zorya

#### Zorya Provides

- Invincibility — Area

#### Damage types dealt by Zorya

- Magic — Arc, Area, Single target
- HP loss — Area — `high`

#### Crowd Control provided by Zorya

- Steadfast — Self — Start of battle
- Unaffected (EX+10) — Single target — On skill
- Knock down — Arc — `average`
- Stun — Area — `average`

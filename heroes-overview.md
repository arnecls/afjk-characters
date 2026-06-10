# Heroes Overview

Per-hero synergy picks and summaries derived from skill text in
[Heroes.md](Heroes.md). [Heroes.md](Heroes.md) has skills only.
Synergy: stat buff tags under **Units X benefits from**, and
enabler partners matching **Requires** special effects.
Up to five partners by combined score. Omitted: ATK-only, Max HP
buff-only, and Shield-only (unless the hero benefits from Max HP/
shields). Rare conditional buffs score lower.
Regenerate: `python3 scripts/generate-heroes-overview.py`.

## Aliceth

### Aliceth's behavior

- **Signature skill**: Radiant Rain (ultimate)
- **Movement**: stationary (avg attack range 8.0 tiles)
- **Ally composition**: nearest ally in same row receives Brightfeather at battle start

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `high`
- **True damage**: HP loss `high`

##### Ultimate

invincible AoE volleys with HP-loss bonus damage

##### Skill 1

Passive: empower nearest row ally with follow-up bonus effects; Active: stun charge

##### Skill 2

mark farthest enemy, boosting penetration; execute threshold

##### Legendary+

battle ATK grows after first marked target falls

##### Mythic+

block first fatal blow per ally; invincible repositioning

##### Supreme+

empowered ally attacks add extra ultimate casts

### Units Aliceth benefits from

Look for units providing: `ATK` `Healing` `DEF Penetration`  
Common buffers are **Lyca**, **Rowan**, or **Ravion**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (single target, high)
  - Enables Debuff on target via DoT (all units)
- **Kulu**
  - DEF Penetration buff (single target, low)
  - Enables Debuff on target via Damage taken debuff (all units)
- **Lily May**
  - DEF Penetration buff (single target, low)
  - Enables Debuff on target via Energy drain (all units)
- **Alna**
  - ATK buff (single target, medium)
  - Enables Debuff on target via Haste debuff (area)
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
  - Enables Debuff on target via ATK debuff (all units)

### Units benefitting most from Aliceth

- Kulu
- Lily May

### Units that can act as a replacement for Aliceth

**Damage**

- Athalia (100% `Physical` `HP loss`)
- Faramor (100% `Physical` `HP loss`)
- Dunlingr (97% `HP loss`)

**Crowd Control**

- Hepler (86% `Blind` `Stun`)
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

- **Signature skill**: Winter Anthem (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Ally composition**: place ally in same row at battle prep (Winter Warrior buffs)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, debuffs `medium`, damage `high`
- **Non-ultimate**: speed `slow`, heal `medium`, buffs `medium`, debuffs `medium`, damage `high`

##### Ultimate

Passive: frost field lowers all haste; Active: AoE strips buffs

##### Skill 1

Passive: same-row ally max HP boost; Active: attack deals damage and heals

##### Skill 2

multi-hit arc sweep, applying haste reduction

##### Legendary+

battle damage reduction scales over time

##### Mythic+

periodic immunity to damage and control

##### Supreme+

shared stats until one falls; bind on immunity exit

### Units Alna benefits from

Look for units providing: `Max HP` `Healing`  
Common buffers are **Hepler**, **Hewynn**, or **Rowan**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Antandra**
  - Healing (multiple targets, high)
- **Contess**
  - Healing (multiple targets, high)

### Units benefitting most from Alna

- Indris
- Nerion
- Perseus

### Units that can act as a replacement for Alna

**Similar Skills**

- Cryonaia (75% `battlefield-modification` `cc-immunity` `invincibility`)

**Damage**

- Athalia (100% `Physical`)
- Dionel (100% `Physical`)
- Gunnar (100% `Physical`)

**Debuffs on enemies**

- Bryon (75% `Haste debuff`)

**Crowd Control**

- Arden (100% `Bind`)
- Carolina (100% `Bind`)
- Gwyneth (100% `Bind`)

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

- **Signature skill**: Twirling Rocks (ultimate)
- **Movement**: mostly stationary (avg attack range 6.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, debuffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, debuffs `medium`, damage `medium`

##### Ultimate

dash to tile; enter melee buff state with enhanced skill casts

##### Skill 1

targeted stun blast creates terrain obstacles behind target

##### Skill 2

AoE damage on enemies recently affected by control

##### Legendary+

extra haste bonus after entering melee buff state

##### Mythic+

repeated skill casts stack damage and shield value

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
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, low)
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`
- **Mehira**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
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

- **Signature skill**: Shield Assault (ultimate)
- **Movement**: high movement (repositioning skills)
- **Ally composition**: frontmost ally becomes guarded ally (shared shields)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `low`

##### Ultimate

taunt nearby; damage reduction then stun slam and heal

##### Skill 1

shield frontmost ally with shared ongoing protection

##### Skill 2

frontal arc attack, reducing enemy ATK

##### Legendary+

battle max HP increase

##### Mythic+

rush to endangered ally, reducing their damage taken

##### Supreme+

hits boost own DEF; shielded ally heals tank in return

### Units Antandra benefits from

Look for units providing: `Max HP` `Healing` `Energy`  
Common buffers are **Rowan**, **Lyca**, or **Smokey & Meerky**.

- **Pandora**
  - Max HP buff (single target, medium)
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Damian**
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`

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

- **Signature skill**: Force of Nature (ultimate)
- **Movement**: stationary (no finite attack range)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, damage `high`

##### Ultimate

AoE strike leaves persistent DoT zone on controlled enemies

##### Skill 1

bind closest enemies, dealing periodic damage

##### Skill 2

recover energy whenever non-summoned enemies are controlled

##### Legendary+

battle ATK increase

##### Mythic+

post-ultimate bind all DoT-zone targets simultaneously

##### Supreme+

shorten DoT zone trigger interval per additional affected target

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

- **Signature skill**: Wild Sniper (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, damage `medium`

##### Ultimate

dash then line AoE stun in chosen direction

##### Skill 1

melee knock back and bind; chain into second target

##### Skill 2

explosive shot with area splash damage

##### Legendary+

haste grows from hitting multiple different foes

##### Mythic+

double cast at start; steal target ATK and DEF

##### Supreme+

direct hit heals; chained hit reduces target DEF

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
- **Velara**
  - Haste buff (single target, high) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)

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

- **Signature skill**: Unbroken Retribution (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, buffs `medium`, debuffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `high`
- **True damage**: HP loss `high`, True damage `medium`

##### Ultimate

Passive: persists after defeat with reduced ATK; Active: true damage scaling on accumulated HP-loss

##### Skill 1

invincible dash targeting highest cumulative attacker

##### Skill 2

unaffected multi-strike with damage reduction and self-heal

##### Legendary+

crit boost higher against highest damage dealer

##### Mythic+

alternate dashes release cross-path area slashes

##### Supreme+

charge and slashes also reduce enemy shield values

### Units Athalia benefits from

Look for units providing: `Max HP` `CRIT` `Execution` `Healing`  
Common buffers are **Hepler**, **Rowan**, or **Hugin**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Damian**
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Velara**
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Athalia

- Indris
- Nerion
- Aliceth

### Units that can act as a replacement for Athalia

**Similar Skills**

- Baelran (80% `hp-scaling` `transformation`)
- Kordan (66% `hp-scaling` `self-repositioner`)
- Pippa (66% `hp-scaling` `self-repositioner`)

**Damage**

- Faramor (83% `Physical` `HP loss` `True damage`)
- Vala (76% `HP loss` `True damage` `Physical`)
- Shadewing (69% `HP loss` `True damage`)

**Debuffs on enemies**

- Lyca (100% `ATK debuff`)
- Lucius (80% `ATK debuff`)
- Ravion (60% `ATK debuff`)

**Crowd Control**

- Antandra (100% `Knock down`)
- Baelran (100% `Knock down`)
- Ravion (100% `Knock down`)

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

- **Signature skill**: Starlit Slumber (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, debuffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `high`

##### Ultimate

sleep state summons stat-inherit companion with ally aura

##### Skill 1

while in sleep state summon companion that explodes on expiry

##### Skill 2

nearby field transforms lingering controlled enemies into harmless summons

##### Legendary+

ATK scales with variety of allied summons on field

##### Mythic+

allied summons receive type-based combat role buffs

##### Supreme+

high energy deepens sleep, expanding transform field radius

### Units Aurora benefits from

Look for units providing: `ATK` `Haste`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Vala**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Aurora

- Damian
- Florabelle

### Units that can act as a replacement for Aurora

**Buffs on allies**

- Harak (100% `Invincible`)
- Pandora (100% `Invincible`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Berial (100% `Magic`)

**Debuffs on enemies**

- Alna (100% `Haste debuff`)
- Bonnie (100% `Haste debuff`)
- Bryon (100% `Haste debuff`)

**Crowd Control**

- Tasi (100% `Sleep`)

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

- **Signature skill**: Celestial Rise (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, buffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `high`
- **True damage**: True damage `high`

##### Ultimate

start with decaying bonus max HP; restore triggers transformation

##### Skill 1

passive HP regeneration; transformation adds true damage per hit

##### Skill 2

upward slash, then downward knock down slam

##### Legendary+

haste grows with each form transition

##### Mythic+

enhanced form fully restores max HP and becomes unaffected

##### Supreme+

true damage per hit also reduces enemy max HP permanently

### Units Baelran benefits from

Look for units providing: `ATK` `Haste` `Max HP` `Healing`  
Common buffers are **Mikola**, **Hepler**, or **Hugin**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (single target, high)

### Units benefitting most from Baelran

- Nerion
- Carolina

### Units that can act as a replacement for Baelran

**Similar Skills**

- Athalia (80% `hp-scaling` `transformation`)

**Damage**

- Athalia (100% `Physical` `True damage`)
- Dionel (100% `True damage` `Physical`)
- Faramor (100% `True damage` `Physical`)

**Debuffs on enemies**

- Contess (100% `Max HP debuff`)
- Natsu (100% `Max HP debuff`)
- Nazrik (100% `Max HP debuff`)

**Crowd Control**

- Scarlita (66% `Knock up` `Knock down`)
- Lucca (60% `Knock down` `Knock up`)
- Lucy (60% `Knock up`)

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

- **Signature skill**: Scared Swamp (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `low`

##### Ultimate

enter stealth on target, draining energy then leap to frighten

##### Skill 1

enter stealth to hunt isolated targets

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
- **Solise**
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

### Units benefitting most from Berial

- Nerion
- Carolina
- Bonnie

### Units that can act as a replacement for Berial

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

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

- **Signature skill**: Decay's Reach (Skill 1)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill**: speed `fast`, debuffs `medium`, damage `high`
- **Ultimate**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

##### Ultimate

magic AoE damage twice; bonus damage and stun on max debuff stack

##### Skill 1

stacking haste debuff on rearmost enemy reduces haste permanently

##### Skill 2

invincible teleport firing multi-target magic damage

##### Legendary+

battle ATK increase

##### Mythic+

debuff spreads to new targets on max stack or debuffed unit death

##### Supreme+

max-stack debuffed targets suffer increased magic damage

### Units Bonnie benefits from

Look for units providing: `ATK`  
Common buffers are **Lyca**, **Ravion**, or **Rowan**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Enables Debuff on target via DoT (all units)
  - Enables Magic damage from allies via Magic damage + early battle + all enemies (all units)
- **Lily May**
  - Enables Debuff on target via Energy drain (all units)
  - Enables Magic damage from allies via Magic damage + all enemies (all units)
- **Bryon**
  - Enables Debuff on target via Haste debuff (area)
  - Enables Magic damage from allies via Magic damage + early battle (area)
- **Frieren**
  - Enables Debuff on target via DoT (area)
  - Enables Magic damage from allies via Magic damage + all enemies (all units)
- **Kulu**
  - Enables Debuff on target via Damage taken debuff (all units)

### Units benefitting most from Bonnie

- Indris
- Aliceth
- Shadewing

### Units that can act as a replacement for Bonnie

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Debuffs on enemies**

- Kafra (85% `ATK debuff` `Haste debuff`)
- Pandora (85% `ATK debuff` `Haste debuff` `Damage taken debuff`)

**Crowd Control**

- Aliceth (100% `Stun`)
- Alsa (100% `Stun`)
- Antandra (100% `Stun`)

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

- **Signature skill**: Whirlwind Wrath (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, debuffs `medium`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`
- **True damage**: Max HP-based damage `high`

##### Ultimate

spin, dealing sustained area damage while unaffected

##### Skill 1

taunt surrounding enemies, reducing their DEF

##### Skill 2

survive first fatal blow then gain temporary immunity

##### Legendary+

battle life drain elevated during spin

##### Mythic+

counterattack after absorbing adjacent melee hits, with HP-scaling damage

##### Supreme+

extend immunity and unaffected duration from damage survival

### Units Brutus benefits from

Look for units providing: `Life Drain`  
Common buffers are **Lyca**, **Rowan**, or **Ravion**.

- **Cecia**
  - Lifedrain buff (area, high)
  - ATK SPD buff (single target, low) `signature fuel`
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

### Units benefitting most from Brutus

- Shadewing
- Indris
- Aliceth

### Units that can act as a replacement for Brutus

**Buffs on allies**

- Cecia (100% `Life Drain`)
- Daimon (100% `Life Drain`)
- Dunlingr (100% `Life Drain`)

**Similar Skills**

- Granny Dahnie (66% `hp-scaling` `taunt`)
- Zorya (66% `hp-scaling` `life-drain`)

**Damage**

- Gunnar (100% `Max HP-based damage` `DoT` `Physical`)
- Satrana (97% `Max HP-based damage`)
- Korin (88% `Max HP-based damage` `Physical`)

**Debuffs on enemies**

- Lyca (66% `Phys DEF debuff`)

**Crowd Control**

- Hepler (100% `Taunt`)
- Antandra (60% `Taunt`)

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

- **Signature skill**: Falcon Raid (ultimate)
- **Movement**: stationary (summon moves)

#### Skill overview

- **Signature skill (ultimate)**: speed `fast`, debuffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, damage `medium`

##### Ultimate

Passive: summons companion; Active: cast deals coordinated strike damage

##### Skill 1

launch multiple magic projectiles at target

##### Skill 2

Passive: drain enemy energy on each hit; Active: secondary strike

##### Legendary+

haste scales while companion is on battlefield

##### Mythic+

companion counterattacks when owner is controlled or struck hard

##### Supreme+

projectiles spawn near companion; companion chains damage to multiple targets

### Units Bryon benefits from

Look for units providing: `Haste` `Healing`  
Common buffers are **Hewynn**, **Mikola**, or **Smokey & Meerky**.

- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
- **Velara**
  - Haste buff (single target, high) `signature fuel`
  - Healing (area, medium)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))

### Units benefitting most from Bryon

- Shadewing
- Bonnie

### Units that can act as a replacement for Bryon

**Damage**

- Frieren (100% `DoT` `Magic`)
- Tasi (100% `DoT` `Magic`)
- Mirael (68% `Magic` `DoT`)

**Debuffs on enemies**

- Alna (100% `Haste debuff`)
- Natsu (66% `Haste debuff`)
- Eironn (60% `Haste debuff`)

**Crowd Control**

- Gerda (100% `Interrupt` `Stun`)
- Lucca (100% `Interrupt` `Stun`)
- Smokey & Meerky (100% `Interrupt` `Stun`)

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

- **Signature skill**: Restless Guardian (ultimate)
- **Movement**: moving (avg attack range 1.7 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`
- **Non-ultimate**: speed `fast`, damage `high`

##### Ultimate

start shielded, absorbing portion of ally damage then join battle

##### Skill 1

double hit, then arc ground slam with knock down

##### Skill 2

convert absorbed damage to stored burst release

##### Legendary+

battle vitality increase

##### Mythic+

low HP threshold triggers burst damage and stun

##### Supreme+

heal when gaining any shield

### Units Callan benefits from

Look for units providing: `Healing`  
Common buffers are **Hewynn**, **Smokey & Meerky**, or **Mikola**.

- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Koko**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Contess**
  - Healing (multiple targets, high)

### Units benefitting most from Callan

- Nerion
- Carolina
- Perseus

### Units that can act as a replacement for Callan

**Buffs on allies**

- Daimon (100% `Max HP`)
- Galahad (100% `Max HP`)
- Hepler (100% `Max HP`)

**Damage**

- Alsa (100% `Magic`)
- Cassadee (100% `Magic`)
- Contess (100% `Magic`)

**Crowd Control**

- Antandra (100% `Knock down` `Stun`)
- Lucca (100% `Knock down` `Stun`)
- Valka (100% `Knock down` `Stun`)

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

- **Signature skill**: Frozen Grave (ultimate)
- **Movement**: mostly stationary (avg attack range 4.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, debuffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, debuffs `medium`, damage `medium`

##### Ultimate

charge up bind then surrounding DoT field

##### Skill 1

area damage applies DoT stacks to targets

##### Skill 2

orbiting projectiles automatically attack controlled enemies

##### Legendary+

crit scales with repeated use count

##### Mythic+

repeated casts stack projectile damage and reduce DEF

##### Supreme+

stacking projectiles also apply DoT on impact

### Units Carolina benefits from

Look for units providing: `CRIT`  
Common buffers are **Ravion**, **Lyca**, or **Hepler**.

- **Tasi**
  - Enables CC on enemies via Sleep (all units, high)
- **Baelran**
  - Enables CC on enemies via Knock up (area, high)
- **Indris**
  - Enables CC on enemies via Knock back (area, high)
- **Kordan**
  - Enables CC on enemies via Bind (area, high)
- **Lumont**
  - Enables CC on enemies via Stun (area, high)

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

- **Signature skill**: Running Tide (ultimate)
- **Movement**: stationary (avg attack range 10.0 tiles)
- **Ally composition**: nearest ally auto-selected at battle start; prioritizes ally behind

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, damage `medium`

##### Ultimate

wide wave knock back all enemies in path

##### Skill 1

displace enemy upward, stunning on landing

##### Skill 2

bless one ally whose hits trigger bonus magic damage

##### Legendary+

haste grows while first blessed ally remains alive

##### Mythic+

ultimate path blesses all hit allies temporarily

##### Supreme+

ultimate reduces magic DEF; ally blessing becomes permanent

### Units Cassadee benefits from

Look for units providing: `Haste`  
Common buffers are **Twins**, **Hugin**, or **Lyca**.

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
- **Velara**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Cassadee

- Nerion
- Carolina
- Bonnie

### Units that can act as a replacement for Cassadee

**Similar Skills**

- Temesia (60% `aoe-damage` `enemy-debuffer`)

**Damage**

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Contess (100% `Magic`)

**Debuffs on enemies**

- Carolina (100% `Magic DEF debuff`)
- Eironn (100% `Magic DEF debuff`)
- Fay (100% `Magic DEF debuff`)

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

- **Signature skill**: Queen's Summons (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `low`

##### Ultimate

summon companion that binds on arrival

##### Skill 1

grant ATK speed burst and companion power attack

##### Skill 2

passive DEF penetration; periodic enhanced normal attack

##### Legendary+

ATK speed scales with companion presence on battlefield

##### Mythic+

bind permanently drains enemy DEF

##### Supreme+

reduce normal attacks needed to trigger enhanced trigger

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

- Shadewing
- Kordan
- Walker
- Talene
- Zandrok
- Brutus
- Igor

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

call allies together for a combined powerful slam

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

- **Signature skill**: Detention Pass (ultimate)
- **Movement**: stationary (no finite attack range)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, heal `medium`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, debuffs `medium`, damage `medium`

##### Ultimate

Passive: start hidden recovering energy; Active: heal and grant immunity

##### Skill 1

penalize damage threshold violators with max HP reduction

##### Skill 2

penalize ultimate casters by reducing energy recovery

##### Legendary+

violations permanently stack ATK and energy reduction

##### Mythic+

repeated violations lead to permanent silence

##### Supreme+

violations trigger stun or silence based on rule type

### Units Contess benefits from

Look for units providing: `Max HP` `Healing` `Energy`  
Common buffers are **Rowan**, **Hepler**, or **Smokey & Meerky**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Antandra**
  - Healing (multiple targets, high)
- **Gerda**
  - Healing (multiple targets, high)

### Units benefitting most from Contess

- Perseus
- Silven
- Indris

### Units that can act as a replacement for Contess

**Buffs on allies**

- Smokey & Meerky (88% `Healing` `ATK`)
- Mikola (77% `Healing` `ATK`)
- Antandra (66% `Healing`)

**Damage**

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Cassadee (100% `Magic`)

**Debuffs on enemies**

- Sylphira (75% `Max HP debuff` `Energy drain`)

**Crowd Control**

- Gwyneth (93% `Silence` `Stun`)
- Cyran (60% `Silence`)
- Dunlingr (60% `Silence`)

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

- **Signature skill**: Frostveil Domain (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, debuffs `medium`, damage `high`

##### Ultimate

isolate top damage dealers in a separate domain

##### Skill 1

sweeping AoE damage crosses the entire battlefield

##### Skill 2

rapid burst; cooldown halved while shielded

##### Legendary+

ATK grows the longer shield stays active

##### Mythic+

only caster can cast ultimates inside the domain

##### Supreme+

instantly defeat weakened enemies inside domain

### Units Cryonaia benefits from

Look for units providing: `ATK` `Max HP`  
Common buffers are **Hugin**, **Lyca**, or **Rowan**.

- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Pandora**
  - Max HP buff (single target, medium)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, medium)
- **Galahad**
  - Max HP via Shield (single target, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Cryonaia

- Bonnie
- Himmel
- Niru

### Units that can act as a replacement for Cryonaia

**Similar Skills**

- Alna (75% `battlefield-modification` `cc-immunity` `invincibility`)

**Damage**

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Cassadee (100% `Magic`)

**Debuffs on enemies**

- Berial (100% `Damage taken debuff`)
- Bonnie (100% `Damage taken debuff`)
- Indris (100% `Damage taken debuff`)

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

- **Signature skill**: Gravitic Requiem (ultimate)
- **Movement**: mostly stationary (avg attack range 6.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `low`
- **True damage**: True damage `medium`

##### Ultimate

place AoE pull zone damaging nearby enemies

##### Skill 1

launch cluster projectiles at area with most enemies

##### Skill 2

lift nearest enemy and throw at area with most enemies

##### Legendary+

crit grows and stacks after kills inside pull zone

##### Mythic+

cast sequential opening spells at battle start

##### Supreme+

gain large initial energy bonus

### Units Cyran benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `CRIT`  
Common buffers are **Lyca**, **Hugin**, or **Twins**.

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

### Units benefitting most from Cyran

- Bonnie
- Nerion
- Indris

### Units that can act as a replacement for Cyran

**Damage**

- Frieren (100% `True damage` `Magic`)
- Sylphira (97% `True damage` `Magic`)
- Pippa (93% `True damage` `Magic`)

**Debuffs on enemies**

- Athalia (100% `ATK debuff`)
- Lucius (100% `ATK debuff`)
- Lyca (100% `ATK debuff`)

**Crowd Control**

- Evie (100% `Silence` `Bind`)
- Gwyneth (100% `Bind` `Silence`)
- Indris (73% `Bind` `Silence`)

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

- **Signature skill**: Buddy Barrier (Skill 2)
- **Movement**: stationary (no finite attack range)
- **Ally composition**: place ally directly behind at battle prep (shield share, Life Drain, and ATK bond)

#### Skill overview

- **Signature skill**: speed `fast`, buffs `medium`
- **Ultimate**: speed `slow`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `high`
- **True damage**: Max HP-based damage `high`

##### Ultimate

Passive: companion auto-attacks; Active: cast deals true damage scaling on target max HP

##### Skill 1

companion periodic true damage converts to personal shield

##### Skill 2

shield linked ally, boosting their ATK and drain

##### Legendary+

damage reduction grows while shielded

##### Mythic+

companion frightens nearby enemies after sustained damage taken

##### Supreme+

expiring shields convert remainder to ally healing

### Units Daimon benefits from

Look for units providing: `Max HP`  
Common buffers are **Hepler** or **Hugin**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, medium)
- **Koko**
  - Max HP via Shield (all units, low)
- **Lenya**
  - Max HP via Shield (single target, high)
- **Lucy**
  - Max HP via Shield (single target, high)

### Units benefitting most from Daimon

- Gerda

### Units that can act as a replacement for Daimon

**Buffs on allies**

- Koko (88% `Max HP` `Life Drain`)
- Hepler (66% `Max HP`)
- Hugin (66% `Max HP`)

**Similar Skills**

- Shemira (72% `hp-scaling` `life-drain` `summoner`)
- Zorya (60% `hp-scaling` `life-drain`)

**Damage**

- Satrana (100% `Max HP-based damage` `Magic`)
- Shadewing (100% `Max HP-based damage` `Magic`)
- Shemira (100% `Max HP-based damage` `Magic`)

**Crowd Control**

- Berial (100% `Frighten`)
- Silvina (100% `Frighten`)

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

- **Signature skill**: Inventor's Will (Mythic+)
- **Movement**: stationary (off battlefield)

#### Skill overview

- **Signature skill**: speed `fast`, heal `medium`, buffs `medium`, damage `low`
- **Ultimate**: speed `slow`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

##### Ultimate

Passive: proxy summon holds position; Active: charge deals damage and blinds

##### Skill 1

summon heals weakest nearby ally or restores energy

##### Skill 2

launched projectile stuns and damages farthest target

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
- **Vala**
  - Haste buff (single target, high) `signature fuel`

### Units benefitting most from Damian

**13** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Twins
- Viperian
- Bryon
- Aurora
- Cassadee
- Koko
- Natsu
- Hugin
- Pippa
- Rowan

### Units that can act as a replacement for Damian

**Buffs on allies**

- Velara (100% `Healing` `Haste`)
- Hewynn (68% `Healing`)
- Lorsan (68% `Healing`)

**Similar Skills**

- Laios (66% `ally-healer` `summoner`)
- Florabelle (60% `summoner`)

**Damage**

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Cassadee (100% `Magic`)

**Crowd Control**

- Hepler (94% `Blind` `Stun`)
- Aliceth (66% `Blind` `Stun`)
- Arden (60% `Stun`)

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

- **Signature skill**: Dawn Light (ultimate)
- **Movement**: moving (avg attack range 0.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `medium`
- **True damage**: True damage `medium`

##### Ultimate

untargetable aerial AoE damage on area with most enemies

##### Skill 1

normal attack becomes long-range penetrating line

##### Skill 2

Passive: stack buffs from allies; Active: ATK speed surge

##### Legendary+

ATK speed permanently rises with each normal attack

##### Mythic+

true damage burst available at max buff stacks

##### Supreme+

execution grows with active buff; shield at max stacks

### Units Dionel benefits from

Look for units providing: `ATK SPD / Haste` `Max HP` `Execution`  
Common buffers are **Lyca**, **Hugin**, or **Twins**.

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
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`

### Units benefitting most from Dionel

- Nerion
- Silven
- Aliceth

### Units that can act as a replacement for Dionel

**Buffs on allies**

- Aliceth (100% `DEF Penetration`)
- Cecia (66% `DEF Penetration`)
- Kordan (66% `DEF Penetration`)

**Damage**

- Athalia (100% `Physical` `True damage`)
- Baelran (100% `True damage` `Physical`)
- Scarlita (100% `Physical` `True damage`)

**Debuffs on enemies**

- Alna (100% `Vitality debuff`)
- Frieren (100% `Vitality debuff`)
- Hodgkin (100% `Vitality debuff`)

**Crowd Control**

- Baelran (100% `Knock up`)
- Florabelle (100% `Knock up`)
- Lucca (100% `Knock up`)

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

- **Signature skill**: Echo of Silence (ultimate)
- **Movement**: stationary (avg attack range 6.4 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `medium`
- **True damage**: HP loss `medium`

##### Ultimate

choose battlefield rule blocking ultimates or blocking healing

##### Skill 1

frontal area multi-hit with rule-based bonus effect

##### Skill 2

gain shield when active rule type is violated

##### Legendary+

battle damage reduction strengthened during active rule

##### Mythic+

protect one ally from the imposed rule penalty

##### Supreme+

rule start grants allies ATK speed or life drain

### Units Dunlingr benefits from

Look for units providing: `ATK SPD / Haste` `Max HP` `Healing`  
Common buffers are **Hugin**, **Hepler**, or **Twins**.

- **Solise**
  - Healing (all units, high)
  - Max HP via Shield (summons only, medium)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
  - Max HP via Shield (summons only, medium)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)

### Units benefitting most from Dunlingr

- Perseus
- Indris
- Nerion

### Units that can act as a replacement for Dunlingr

**Buffs on allies**

- Valka (84% `ATK SPD` `Life Drain` `Haste`)

**Damage**

- Athalia (100% `HP loss`)
- Talene (100% `HP loss` `Magic`)
- Zorya (96% `HP loss` `Magic`)

**Debuffs on enemies**

- Sinbad (100% `Energy drain` `ATK debuff`)
- Pandora (61% `ATK debuff` `Energy drain`)

**Crowd Control**

- Evie (100% `Silence`)
- Sylphira (96% `Silence`)
- Contess (60% `Silence`)

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

- **Signature skill**: Howling Hurricane (Mythic+)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill**: speed `fast`
- **Ultimate**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `medium`

##### Ultimate

pull nearby enemies inward then explode, immobilizing

##### Skill 1

arc slash lowers enemy haste; stab reduces magic DEF

##### Skill 2

large personal shield, granting high dodge rate

##### Legendary+

ranged DEF scales up when health is low

##### Mythic+

first pull per battle is free at reduced power

##### Supreme+

extra magic DEF reduction on immobilized targets

### Units Eironn benefits from

Look for units providing: `Max HP` `Physical DEF`  
Common buffers are **Hepler**, **Hugin**, or **Rowan**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, medium)
- **Daimon**
  - Max HP via Shield (multiple targets, medium)
- **Koko**
  - Max HP via Shield (all units, low)
- **Lenya**
  - Max HP via Shield (single target, high)

### Units benefitting most from Eironn

- Indris
- Bonnie
- Nerion

### Units that can act as a replacement for Eironn

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Debuffs on enemies**

- Shadewing (60% `Magic DEF debuff`)

**Crowd Control**

- Evie (96% `Displace` `Bind`)
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

- **Signature skill**: Starlight Waltz (ultimate)
- **Movement**: moving / stationary (two units)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `low`

##### Ultimate

linked duo performance inspires allied haste; linked allies become unaffected

##### Skill 1

row alignment link boosts ATK of all linked allies

##### Skill 2

one twin shields an ally; the other blasts nearby foes

##### Legendary+

haste grows each time the performance is repeated

##### Mythic+

same-faction link grants resonance and energy burst

##### Supreme+

linked allies borrow best stats from each other

### Units Twins benefits from

Look for units providing: `Haste` `Healing` `Energy`  
Common buffers are **Rowan**, **Hugin**, or **Lyca**.

- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Velara**
  - Haste buff (single target, high) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`

### Units benefitting most from Twins

**69** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Perseus
- Alsa
- Hepler
- Lenya
- Lumont
- Mehira
- Soren
- Tasi
- Zorya
- Dionel

### Units that can act as a replacement for Twins

**Similar Skills**

- Hugin (66% `ally-shielder` `energy-provider`)
- Lucius (66% `ally-healer` `ally-shielder`)
- Rowan (66% `ally-healer` `energy-provider`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Crowd Control**

- Aliceth (82% `Blind` `Knock back`)
- Scarlita (60% `Knock back`)
- Talene (60% `Knock back`)

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

- **Signature skill**: Intel Chase (ultimate)
- **Movement**: high movement (repositioning skills)
- **Ally composition**: rearmost ally starts with healing quill; tracks highest damage dealer

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, debuffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `high`

##### Ultimate

start concealed gathering debuff stacks on enemy heroes

##### Skill 1

Passive: observation stacks reduce target magic DEF; Active: multi-strike

##### Skill 2

roving support heals and buffs highest damage dealer

##### Legendary+

battle healing stat increase

##### Mythic+

full observation permanently reduces all enemy damage dealt

##### Supreme+

extra support ally buffs second-highest damage dealer

### Units Evie benefits from

Look for units providing: `Healing`  
Common buffers are **Hewynn**, **Smokey & Meerky**, or **Mikola**.

- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Koko**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Contess**
  - Healing (multiple targets, high)

### Units benefitting most from Evie

- Bonnie
- Shadewing
- Aliceth

### Units that can act as a replacement for Evie

**Buffs on allies**

- Mikola (100% `ATK` `Healing`)
- Hugin (80% `ATK`)
- Contess (66% `ATK` `Healing`)

**Damage**

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Cassadee (100% `Magic`)

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

- **Signature skill**: Sanctified Circle (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Ally composition**: bless adjacent ally at battle prep; prioritizes tile behind

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `high`
- **True damage**: HP loss `high`, True damage `high`

##### Ultimate

circular area blocks healing and deals sustained true damage

##### Skill 1

gain shield then strike; true damage when buffed by allies

##### Skill 2

bless adjacent ally, sharing ATK and triggering periodic area damage

##### Legendary+

battle haste increase

##### Mythic+

sustain attacks inside area; allies deal true damage within

##### Supreme+

reduce vitality of enemies revived inside circular area

### Units Faramor benefits from

Look for units providing: `ATK` `Haste` `Max HP`  
Common buffers are **Hugin**, **Twins**, or **Mikola**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Galahad**
  - Haste buff (single target, high) `signature fuel`
  - Max HP via Shield (single target, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, low)
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Faramor

- Nerion
- Carolina
- Indris

### Units that can act as a replacement for Faramor

**Similar Skills**

- Arden (80% `aoe-damage` `dot-specialist`)
- Lorsan (80% `aoe-damage` `dot-specialist`)

**Damage**

- Athalia (88% `Physical` `HP loss` `True damage`)
- Vala (79% `HP loss` `True damage` `Physical`)
- Indris (70% `True damage` `Physical`)

**Debuffs on enemies**

- Alna (100% `Vitality debuff`)
- Dionel (100% `Vitality debuff`)
- Frieren (100% `Vitality debuff`)

**Crowd Control**

- Antandra (100% `Stun`)
- Arden (100% `Stun`)
- Koko (100% `Stun`)

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

- **Signature skill**: Vibrant Dance (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, buffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `medium`

##### Ultimate

frontal arc ally heal and ATK boost

##### Skill 1

sustained heal weakest ally over time

##### Skill 2

AoE burst damages foes and heals allies

##### Legendary+

combat max HP increase

##### Mythic+

battle-start front ally grants skill buffs

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
- **Vala**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Fay

- Perseus
- Silven
- Indris

### Units that can act as a replacement for Fay

**Buffs on allies**

- Rowan (65% `Healing` `Magic DEF` `Physical DEF`)
- Mikola (63% `Healing` `ATK` `Vitality buff`)

**Similar Skills**

- Hewynn (100% `ally-healer` `aoe-healing`)
- Ludovic (100% `ally-healer` `aoe-healing`)
- Smokey & Meerky (100% `ally-healer` `aoe-healing`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Debuffs on enemies**

- Sinbad (100% `Magic DEF debuff` `Phys DEF debuff`)
- Indris (75% `Phys DEF debuff` `Magic DEF debuff`)
- Atalanta (60% `Phys DEF debuff`)

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

- **Signature skill**: Pounding Blow (ultimate)
- **Movement**: stationary (no finite attack range)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `low`

##### Ultimate

Passive: battle-start tank summon; Active: cast is adjacent AoE smash

##### Skill 1

grant growth buff to ally summon, boosting haste and life drain

##### Skill 2

summon ranged ally with rapid fire volleys

##### Legendary+

combat ATK bonus with multiple summons on field

##### Mythic+

summon entrance triggers shield and growth buff

##### Supreme+

large summons gain control immunity and ATK boost

### Units Florabelle benefits from

Look for units providing: `ATK` `Haste`  
Common buffers are **Hugin**, **Mikola**, or **Twins**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, medium)
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Galahad**
  - Haste buff (single target, high) `signature fuel`
- **Mehira**
  - Haste buff (single target, high) `signature fuel`
- **Vala**
  - Haste buff (single target, high) `signature fuel`

### Units benefitting most from Florabelle

- Dunlingr
- Damian
- Zanie

### Units that can act as a replacement for Florabelle

**Similar Skills**

- Chippy (100% `summoner`)
- Zanie (100% `summoner`)
- Damian (60% `summoner`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Baelran (100% `Knock up`)
- Dionel (100% `Knock up`)
- Lucca (100% `Knock up`)

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

- **Signature skill**: Zoltraak (ultimate)
- **Movement**: stationary (avg attack range 7.0 tiles)
- **Ally composition**: frontmost ally shares damage reduction with this hero

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`
- **True damage**: True damage `high`

##### Ultimate

reposition rear; sustained area true damage

##### Skill 1

conceal then amplify state replaces normal attacks

##### Skill 2

area burn applies vitality reduction

##### Legendary+

combat ATK bonus after amplification

##### Mythic+

battle-start damage cap on front ally

##### Supreme+

post-amplify throw top damage dealer to knock down

### Units Frieren benefits from

Look for units providing: `ATK` `Haste`  
Common buffers are **Hugin**, **Twins**, or **Lyca**.

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
- **Velara**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Frieren

- Shadewing
- Bonnie

### Units that can act as a replacement for Frieren

**Damage**

- Sylphira (86% `True damage` `Magic`)
- Cyran (85% `True damage` `Magic`)
- Pippa (81% `True damage` `Magic`)

**Debuffs on enemies**

- Evie (60% `DoT`)

**Crowd Control**

- Antandra (100% `Knock down` `Stun`)
- Callan (100% `Knock down` `Stun`)
- Lucca (100% `Knock down` `Stun`)

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

- **Signature skill**: Time Recast (Mythic+)
- **Movement**: stationary (avg attack range 10.0 tiles)
- **Ally composition**: nearest ally auto-selected at battle start; prioritizes ally behind

#### Skill overview

- **Signature skill**: speed `fast`
- **Ultimate**: speed `normal`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `high`

##### Ultimate

consume energy for AoE then build slow-forming circular zone

##### Skill 1

immobilize top attacker; target loses HP from prior healing

##### Skill 2

shield weakest ally; explodes on expiry, dealing area damage

##### Legendary+

ATK grows after circular zone fully forms

##### Mythic+

zone summons clone of marked ally

##### Supreme+

external buff grants sustained energy and steadfast state

### Units Galahad benefits from

Look for units providing: `ATK` `Haste` `Energy`  
Common buffers are **Hugin**, **Mikola**, or **Ravion**.

- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Mehira**
  - Haste buff (single target, high) `signature fuel`
- **Vala**
  - Haste buff (single target, high) `signature fuel`
- **Velara**
  - Haste buff (single target, high) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Galahad

- Alsa
- Hugin
- Pippa
- Rowan
- Shakir

### Units that can act as a replacement for Galahad

**Buffs on allies**

- Hugin (100% `Haste` `Max HP`)
- Twins (80% `Haste` `Max HP`)
- Hepler (72% `Max HP` `Haste`)

**Damage**

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Cassadee (100% `Magic`)

**Crowd Control**

- Alna (100% `Bind`)
- Arden (100% `Bind`)
- Atalanta (100% `Bind`)

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

- **Signature skill**: Spring Therapy (Skill 1)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill**: speed `fast`, heal `medium`, damage `medium`
- **Ultimate**: speed `slow`, heal `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

##### Ultimate

AoE sleep nearby enemies and heal allies

##### Skill 1

leap stomp creates AoE healing zone

##### Skill 2

taunt one enemy while gaining large shield

##### Legendary+

battle damage taken reduction

##### Mythic+

healing zone bonus; entering ally gains unaffected briefly

##### Supreme+

stomp stuns instead of interrupting; allies entering gain shield

### Units Gerda benefits from

Look for units providing: `Max HP`  
Common buffers are **Hepler** or **Hugin**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, medium)
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
- Antandra (63% `Healing`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Lucca (83% `Stun` `Interrupt`)
- Smokey & Meerky (80% `Interrupt` `Stun`)
- Alsa (60% `Stun`)

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

- **Signature skill**: Threshold of Jade (ultimate)
- **Movement**: moving (avg attack range 2.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `low`

##### Ultimate

ensnare enemies, draining energy and HP; self-heals equal amount

##### Skill 1

trigger projectile when absorbing threshold damage

##### Skill 2

taunt enemy targeting weakest ally with instant self-heal

##### Legendary+

battle vitality scales with ultimate casting

##### Mythic+

low HP triggers DEF surge and sustained HP regeneration

##### Supreme+

triggered projectiles grant instant self HP recovery

### Units Granny Dahnie benefits from

Look for units providing: `Healing` `Energy` `Physical DEF` `Magic DEF`  
Common buffers are **Rowan**, **Lyca**, or **Smokey & Meerky**.

- **Lorsan**
  - Healing (all units, high)
- **Solise**
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
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Bonnie (100% `ATK debuff` `Haste debuff`)
- Kafra (100% `ATK debuff` `Haste debuff`)
- Pandora (100% `ATK debuff` `Haste debuff`)

**Crowd Control**

- Antandra (100% `Stun` `Taunt`)
- Lumont (100% `Stun` `Taunt`)
- Hepler (80% `Taunt` `Stun`)

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

- **Signature skill**: Annihilation Directive (ultimate)
- **Movement**: stationary (no finite attack range)
- **Ally composition**: place ally 1 tile behind at battle start (Doomfield buffs and coordinated attacks)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `medium`
- **True damage**: Max HP-based damage `medium`

##### Ultimate

battle-start empower adjacent ally in field; both steadfast

##### Skill 1

multi-shot burst; empowered ally coordinates strike and stun

##### Skill 2

shield self and allies behind; strengthen field ATK speed

##### Legendary+

ranged DEF and vitality scale with allied positioning

##### Mythic+

ally damage threshold triggers missile with self-heal

##### Supreme+

scorched area enemies cannot heal or gain shields

### Units Gunnar benefits from

Look for units providing: `ATK SPD / Haste` `Max HP` `Healing`  
Common buffers are **Hugin**, **Hepler**, or **Twins**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
- **Velara**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
  - Healing (area, medium)

### Units benefitting most from Gunnar

- Nerion
- Carolina
- Perseus

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

- **Signature skill**: Hailing Arrows (ultimate)
- **Movement**: stationary (avg attack range 8.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, debuffs `medium`, damage `high`
- **True damage**: Max HP-based damage `low`

##### Ultimate

Passive: build-up heavy normal; Active: immobilizing AoE damage

##### Skill 1

third attack in cycle: lightning silence splash stun

##### Skill 2

second attack in cycle: fire burn with vitality reduction

##### Legendary+

ATK speed grows higher when no nearby enemies present

##### Mythic+

combined lightning-fire first attack also burns splash

##### Supreme+

no nearby enemies reduces normal attack interval further

### Units Gwyneth benefits from

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

### Units benefitting most from Gwyneth

- Nerion
- Carolina
- Shadewing

### Units that can act as a replacement for Gwyneth

**Similar Skills**

- Mirael (80% `dot-specialist` `fire-attack`)

**Damage**

- Brutus (100% `Physical` `Max HP-based damage`)
- Gunnar (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Evie (100% `DoT`)
- Frieren (100% `DoT`)
- Brutus (88% `DoT`)

**Crowd Control**

- Indris (71% `Bind` `Silence`)
- Evie (69% `Bind` `Silence`)
- Arden (65% `Bind` `Stun`)

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

channel then single-target magic damage

##### Skill 1

heal weakest ally, boosting their ATK briefly

##### Skill 2

self-heal when HP falls below threshold

### Units Hammie benefits from

Look for units providing: `ATK` `Healing`  
Common buffers are **Rowan**, **Mikola**, or **Lyca**.

- **Lorsan**
  - Healing (all units, high)
- **Solise**
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

- **Signature skill**: Flesh Feast (Skill 2)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill**: speed `fast`, buffs `medium`, debuffs `medium`
- **Ultimate**: speed `slow`, heal `medium`, damage `low`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `low`
- **True damage**: HP loss `low`

##### Ultimate

sustained multi-strike preventing target HP recovery

##### Skill 1

dive surfacing to damage frontmost; assists and defeats reset cooldown

##### Skill 2

enhanced state boosts crit and haste; ends by absorbing weakest unit

##### Legendary+

life drain increases with assists and defeats

##### Mythic+

absorb defeated unit stats and max HP temporarily

##### Supreme+

multiple assists in one ultimate restore energy

### Units Harak benefits from

Look for units providing: `Haste` `Max HP` `CRIT` `Healing` `Energy`  
Common buffers are **Rowan**, **Hepler**, or **Hugin**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
- **Velara**
  - Haste buff (single target, high) `signature fuel`
  - Healing (area, medium)

### Units benefitting most from Harak

- Perseus
- Silven
- Nerion

### Units that can act as a replacement for Harak

**Buffs on allies**

- Aurora (75% `Invincible`)
- Pandora (75% `Invincible`)

**Similar Skills**

- Seth (66% `assassin` `life-drain`)

**Damage**

- Aliceth (100% `Physical` `HP loss`)
- Athalia (100% `Physical` `HP loss`)
- Faramor (100% `Physical` `HP loss`)

**Debuffs on enemies**

- Aliceth (100% `Execution debuff`)

**Crowd Control**

- Antandra (100% `Knock down`)
- Athalia (100% `Knock down`)
- Baelran (100% `Knock down`)

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

- **Signature skill**: Form Shift (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Ally composition**: frontmost adjacent ally gets fatal-blow protection

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `high`

##### Ultimate

enter alternate form with AoE taunt and charge stacks

##### Skill 1

alternate form AoE stun; base form single haste reduction stun

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
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Velara**
  - Haste buff (single target, high) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Pandora**
  - Max HP buff (single target, medium)
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)

### Units benefitting most from Hepler

**34** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Nerion
- Carolina
- Himmel
- Lumont
- Mehira
- Soren
- Tasi
- Dunlingr
- Gunnar
- Valka

### Units that can act as a replacement for Hepler

**Buffs on allies**

- Koko (86% `Healing` `Max HP`)

**Similar Skills**

- Lucius (66% `ally-healer` `ally-shielder`)
- Pang (66% `ally-shielder` `transformation`)
- Ulmus (66% `ally-shielder` `transformation`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

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

- **Signature skill**: Rain Prayer (ultimate)
- **Movement**: stationary (no finite attack range)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, damage `low`
- **Non-ultimate**: speed `fast`, heal `medium`, damage `medium`

##### Ultimate

sustained AoE heal over time for all allies

##### Skill 1

large single-target heal; extra during ultimate

##### Skill 2

heal ally, cleansing dispellable debuffs

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

**24** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Himmel
- Alna
- Athalia
- Baelran
- Berial
- Bryon
- Callan
- Contess
- Evie
- Granny Dahnie

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

- **Signature skill**: Hero Party (Skill 2)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill**: speed `slow`, buffs `medium`, damage `medium`
- **Ultimate**: speed `normal`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `medium`
- **True damage**: Max HP-based damage `low`

##### Ultimate

sustained frontal multi-slash then true damage sweep

##### Skill 1

dash to two top damage dealers knocking both down

##### Skill 2

battle-start multi-class formation inspires shared stats and shield

##### Legendary+

battle haste increase

##### Mythic+

formation members receive class-based stat and max HP buffs

##### Supreme+

formation deals extra HP-loss on boss targets

### Units Himmel benefits from

Look for units providing: `ATK` `Haste` `Max HP` `Healing`  
Common buffers are **Mikola**, **Hepler**, or **Hugin**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
  - Enables Party composition via Support (party slot)
- **Lorsan**
  - Healing (all units, high)
  - Enables Party composition via Support (party slot)
- **Solise**
  - Healing (all units, high)
  - Enables Party composition via Support (party slot)
- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)
  - Enables Party composition via Support (party slot)
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (single target, high)
  - Enables Party composition via Support (party slot)

### Units benefitting most from Himmel

- Faramor

### Units that can act as a replacement for Himmel

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Temesia (98% `Physical` `Max HP-based damage`)
- Brutus (96% `Physical` `Max HP-based damage`)

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

- **Signature skill**: Cannon Fire (ultimate)
- **Movement**: moving (avg attack range 3.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, debuffs `medium`, damage `medium`

##### Ultimate

sequential single-target shots on each enemy with adjacent splash

##### Skill 1

intangible phase grants physical immunity with sustained HP regeneration

##### Skill 2

arc damage stealing enemy energy

##### Legendary+

ATK grows higher during intangible phase

##### Mythic+

summon minions at start; minion defeat triggers AoE explosion

##### Supreme+

shots reduce target DEF stacking; energy and vitality drain

### Units Hodgkin benefits from

Look for units providing: `ATK` `Healing` `Energy`  
Common buffers are **Rowan**, **Smokey & Meerky**, or **Mikola**.

- **Lorsan**
  - Healing (all units, high)
- **Solise**
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

- **Signature skill**: Unstoppable! (ultimate)
- **Movement**: stationary (no finite attack range)
- **Self placement**: stays anchored to battle-prep tile; returns after displacement
- **Ally composition**: put one ally 1 tile behind him (ATK bonus; buff ends if they leave the sigil)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `high`

##### Ultimate

enhance top damage dealer with permanent combat stat boosts

##### Skill 1

large shield granted to weakest ally

##### Skill 2

adjacent ally gets ATK boost and energy whenever shielded

##### Legendary+

battle haste increase

##### Mythic+

ultimate generates enhanced shields for two weakest allies

##### Supreme+

shielded allies reduce their damage taken

### Units Hugin benefits from

Look for units providing: `Haste` `Energy`  
Common buffers are **Twins**, **Lyca**, or **Rowan**.

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
- **Velara**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Hugin

**80** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Perseus
- Silven
- Tasi
- Alsa
- Frieren
- Hepler
- Lenya
- Lorsan
- Lumont
- Mehira

### Units that can act as a replacement for Hugin

**Similar Skills**

- Ravion (66% `ally-shielder` `energy-provider`)
- Twins (66% `ally-shielder` `energy-provider`)
- Lucca (60% `ally-shielder`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

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

- **Signature skill**: Funereal Ring (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, debuffs `medium`, damage `high`

##### Ultimate

place field markers at start and on enemy HP thresholds

##### Skill 1

leap to field markers, dealing area damage; immune while leaping

##### Skill 2

dodge fatal blows by leaping to markers with HP recovery

##### Legendary+

life drain scales with marker first-use trigger

##### Mythic+

leaping high-HP targets reduces target healing

##### Supreme+

extra field marker at start placed on tile with most enemies

### Units Igor benefits from

Look for units providing: `Healing` `Life Drain`  
Common buffers are **Hewynn**, **Smokey & Meerky**, or **Mikola**.

- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Koko**
  - Healing (all units, medium)
  - Lifedrain buff (multiple targets, low)
- **Cecia**
  - Lifedrain buff (area, high)
- **Antandra**
  - Healing (multiple targets, high)

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

- **Signature skill**: Spellbane Shot (ultimate)
- **Movement**: stationary (no finite attack range)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, debuffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`
- **True damage**: Max HP-based damage `low`, True damage `high`

##### Ultimate

multi-stat debuffs expose weakness; guaranteed crit true damage on target

##### Skill 1

three-hit penetrating normal attack; extra true damage on exposed

##### Skill 2

push back all close enemies then immobilize nearest

##### Legendary+

ATK grows while an enemy has exposed weakness

##### Mythic+

ATK speed burst each time exposed weakness bonus effects

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
- **Sinbad**
  - Enables Multiple debuffs on target via 6 debuff types
  - Enables Debuff on target via Vitality debuff (multiple targets)
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

### Units benefitting most from Indris

- Nerion
- Carolina
- Aliceth

### Units that can act as a replacement for Indris

**Damage**

- Pippa (100% `True damage` `Max HP-based damage`)
- Sylphira (88% `True damage` `Max HP-based damage`)
- Korin (86% `Physical` `True damage` `Max HP-based damage`)

**Debuffs on enemies**

- Sinbad (100% `Damage taken debuff` `Phys DEF debuff` `Magic DEF debuff`)
- Fay (60% `Phys DEF debuff` `Magic DEF debuff`)
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

- **Signature skill**: Grimoire Pact (ultimate)
- **Movement**: stationary (no finite attack range)
- **Ally composition**: frontmost ally becomes companion (stat stacks and ult buffs)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `medium`

##### Ultimate

track companion buff types to build stacked debuff counts

##### Skill 1

heal companion and deal damage to adjacent foes

##### Skill 2

grant companion unaffected after accumulated control; reduce attacker ATK

##### Legendary+

battle assistance stat increase

##### Mythic+

cast stat debuffs matching tracked buff types on top attacker

##### Supreme+

large enough buff grants extra debuff stack

### Units Isabella benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `Healing` `Energy`  
Common buffers are **Mikola**, **Smokey & Meerky**, or **Hugin**.

- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
- **Velara**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
  - Healing (area, medium)
- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)

### Units benefitting most from Isabella

- Indris
- Bonnie
- Perseus

### Units that can act as a replacement for Isabella

**Buffs on allies**

- Damian (100% `Haste`)
- Galahad (100% `Haste`)
- Hugin (100% `Haste`)

**Similar Skills**

- Hammie (66% `ally-buffer` `ally-healer`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Debuffs on enemies**

- Athalia (100% `ATK debuff`)
- Bonnie (100% `ATK debuff`)
- Cyran (100% `ATK debuff`)

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

- **Signature skill**: Gale Thrust (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, debuffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

##### Ultimate

prioritize marked enemy; knock back strike on mark

##### Skill 1

charge out-of-range marked enemy, stunning them

##### Skill 2

mark reduces enemy DEF; mark kill triggers area heal

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
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Lucius**
  - Max HP via Shield (area, medium)

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

- **Signature skill**: Full Energy (ultimate)
- **Movement**: mostly stationary (avg attack range 4.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `high`

##### Ultimate

inspire all allies with damage reduction and stat buffs

##### Skill 1

heal weakest ally; companion gains bonus energy on hit

##### Skill 2

throw projectile at enemy; companion stuns adjacent enemies

##### Legendary+

battle haste increase

##### Mythic+

post-reduction damage converted to team shield

##### Supreme+

allies receiving heals gain vitality boost temporarily

### Units Koko benefits from

Look for units providing: `Haste` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Rowan**.

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
- **Velara**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Koko

**17** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Silven
- Talene
- Zandrok
- Alna
- Athalia
- Contess
- Gunnar
- Lucca
- Saida
- Thoran

### Units that can act as a replacement for Koko

**Similar Skills**

- Saida (66% `ally-shielder` `life-drain`)

**Damage**

- Alna (100% `Physical`)
- Athalia (100% `Physical`)
- Dionel (100% `Physical`)

**Debuffs on enemies**

- Kruger (100% `Damage taken debuff`)
- Kulu (100% `Damage taken debuff`)
- Indris (75% `Damage taken debuff`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Arden (100% `Stun`)

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

- **Signature skill**: Dominance Ring (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `high`
- **True damage**: HP loss `medium`

##### Ultimate

immobilize adjacent enemy inside hunting zone AoE

##### Skill 1

powerful slash with proportional self-shield

##### Skill 2

leap slam with knock down on target

##### Legendary+

battle ATK increase

##### Mythic+

enhanced attacks unlock inside circular zone after first kill

##### Supreme+

assists reposition the circular zone; allies inside gain penetration

### Units Kordan benefits from

Look for units providing: `ATK` `Max HP` `Healing` `DEF Penetration` `Life Drain`  
Common buffers are **Rowan**, **Mikola**, or **Lyca**.

- **Cecia**
  - Max HP buff (single target, high)
  - DEF Penetration buff (single target, medium)
  - Lifedrain buff (area, high)
  - ATK SPD buff (single target, low) `signature fuel`
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
  - Lifedrain buff (multiple targets, low)
- **Pandora**
  - Max HP buff (single target, medium)
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)

### Units benefitting most from Kordan

- Nerion
- Carolina
- Perseus

### Units that can act as a replacement for Kordan

**Buffs on allies**

- Cecia (100% `Life Drain` `DEF Penetration`)

**Similar Skills**

- Pippa (100% `hp-scaling` `self-repositioner`)
- Athalia (66% `hp-scaling` `self-repositioner`)
- Marilee (66% `hp-scaling` `self-repositioner`)

**Damage**

- Aliceth (100% `Physical` `HP loss`)
- Athalia (100% `Physical` `HP loss`)
- Faramor (100% `Physical` `HP loss`)

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

- **Signature skill**: Demonseal Spear (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `medium`
- **True damage**: Max HP-based damage `medium`, True damage `medium`

##### Ultimate

arc sweep immobilize and knock back adjacent enemies

##### Skill 1

jump to weakest ally shielding both then dash true damage

##### Skill 2

guaranteed crit on distant targets; crit rate scales crit damage

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
- **Pandora**
  - Max HP buff (single target, medium)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Dunlingr**
  - ATK SPD buff (all units, low) `signature fuel`
  - Haste buff (single target, low) `signature fuel`

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

- **Signature skill**: Devastating Axe (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, debuffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

##### Ultimate

large knock down slash, applying DEF shatter stacks

##### Skill 1

single slash, applying armor shatter stack

##### Skill 2

heavy strike on max-shattered enemy, draining life

##### Legendary+

battle ranged DEF increase

##### Mythic+

isolated positioning grants large shield and control immunity

##### Supreme+

permanent ATK boost stacks on vulnerable enemy kills

### Units Kruger benefits from

Look for units providing: `Max HP` `Physical DEF`  
Common buffers are **Hugin**, **Rowan**, or **Twins**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, medium)
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Galahad**
  - Max HP via Shield (single target, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Daimon**
  - Max HP via Shield (multiple targets, medium)

### Units benefitting most from Kruger

- Indris
- Aliceth
- Bonnie

### Units that can act as a replacement for Kruger

**Similar Skills**

- Lumont (60% `enemy-debuffer`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Antandra (100% `Knock down`)
- Athalia (100% `Knock down`)
- Baelran (100% `Knock down`)

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

- **Signature skill**: Demolition Zone (Skill 1)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill**: speed `slow`, buffs `medium`, damage `low`
- **Ultimate**: speed `normal`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

##### Ultimate

Passive: normal attacks explode hitting all adjacent; Active: bombardment

##### Skill 1

battle-start debris blocks center tile and marks it

##### Skill 2

bouncing projectile swallows frontmost then releases at rearmost

##### Legendary+

battle ATK stacks from dealing damage to enemies

##### Mythic+

enemies gain explosive debuff; defeated become detonation traps

##### Supreme+

ATK speed scales inversely with enemies on own side

### Units Kulu benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `DEF Penetration`  
Common buffers are **Lyca**, **Mikola**, or **Twins**.

- **Aliceth**
  - ATK buff (multiple targets, low)
  - DEF Penetration buff (multiple targets, high)
- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) `signature fuel`
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`

### Units benefitting most from Kulu

- Indris
- Aliceth
- Bonnie

### Units that can act as a replacement for Kulu

**Buffs on allies**

- Aliceth (100% `DEF Penetration`)
- Cecia (100% `DEF Penetration`)
- Dionel (100% `DEF Penetration`)

**Damage**

- Alna (100% `Physical`)
- Athalia (100% `Physical`)
- Dionel (100% `Physical`)

**Crowd Control**

- Cassadee (66% `Knock back` `Knock up`)
- Kordan (66% `Knock back` `Knock up`)
- Reinier (66% `Displace` `Knock up`)

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

- **Signature skill**: Dungeon Gourmet (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill**: speed `slow`, heal `medium`, buffs `medium`, damage `high`
- **Ultimate**: speed `fast`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `high`

##### Ultimate

summon slow-moving armor construct with sustained combat

##### Skill 1

wide frontal confusion and DEF reduction on enemies

##### Skill 2

collect resource tokens from defeated units to trigger team heal

##### Legendary+

battle ATK increase

##### Mythic+

units drop bonus token when defeated above HP threshold

##### Supreme+

max HP grows with each unique resource type collected

### Units Laios benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `Max HP` `Healing`  
Common buffers are **Lyca**, **Hugin**, or **Twins**.

- **Solise**
  - Healing (all units, high)
  - Max HP via Shield (summons only, medium)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
  - Max HP via Shield (summons only, medium)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Velara**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
  - Healing (area, medium)

### Units benefitting most from Laios

- Nerion
- Carolina

### Units that can act as a replacement for Laios

**Similar Skills**

- Damian (66% `ally-healer` `summoner`)
- Hammie (66% `ally-buffer` `ally-healer`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Antandra (100% `Stun`)
- Arden (100% `Stun`)
- Faramor (100% `Stun`)

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

- **Signature skill**: Wild Duel (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `high`

##### Ultimate

isolate top attacker in one-on-one combat

##### Skill 1

counter adjacent melee attack and counterattack with stun

##### Skill 2

crit triggers follow-up power kick with stun

##### Legendary+

battle haste increase

##### Mythic+

full potential in duel for super multi-hit kick

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
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Pandora**
  - Max HP buff (single target, medium)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Zandrok**
  - Haste buff (area, low, conditional (frequent)) `signature fuel`
  - Max HP buff (multiple targets, low)
  - ATK SPD via Haste buff (area, low, conditional (frequent)) `signature fuel`

### Units benefitting most from Lenya

- Nerion
- Perseus
- Silven

### Units that can act as a replacement for Lenya

**Buffs on allies**

- Daimon (100% `Max HP`)
- Hepler (100% `Max HP`)
- Hugin (100% `Max HP`)

**Similar Skills**

- Soren (66% `counterattack` `self-repositioner`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Cassadee (100% `Knock back` `Stun`)
- Perseus (100% `Knock back` `Stun`)
- Atalanta (85% `Knock back` `Stun`)

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

- **Signature skill**: Tempest Shot (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, debuffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `low`
- **True damage**: Max HP-based damage `low`

##### Ultimate

interrupt enemy ultimate with anti-ultimate projectile draining energy

##### Skill 1

invincible dash multi-hit; continues after defensive trigger

##### Skill 2

experience from attacks; growth stacks ATK and enhanced true hits

##### Legendary+

battle penetration bonus scales with dash usage

##### Mythic+

ally buff triggers growth, expanding enhanced hit count

##### Supreme+

first ultimate interrupt drains extra energy from target

### Units Lily May benefits from

Look for units providing: `ATK` `DEF Penetration`  
Common buffers are **Lyca**, **Rowan**, or **Ravion**.

- **Aliceth**
  - ATK buff (multiple targets, low)
  - DEF Penetration buff (multiple targets, high)
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

### Units benefitting most from Lily May

- Bonnie

### Units that can act as a replacement for Lily May

**Buffs on allies**

- Aliceth (100% `DEF Penetration`)
- Cecia (100% `DEF Penetration`)
- Dionel (100% `DEF Penetration`)

**Similar Skills**

- Athalia (60% `hp-scaling` `self-repositioner` `transformation`)

**Damage**

- Pippa (100% `Magic` `Max HP-based damage`)
- Shadewing (100% `Magic` `Max HP-based damage`)
- Shemira (100% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Pippa (64% `Energy drain`)

**Crowd Control**

- Smokey & Meerky (80% `Interrupt`)
- Sylphira (80% `Interrupt`)
- Gerda (60% `Interrupt`)

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

- **Signature skill**: Whispering Tempest (ultimate)
- **Movement**: stationary (no finite attack range)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, damage `medium`

##### Ultimate

AoE zone on frontmost enemy, dealing sustained damage and haste reduction

##### Skill 1

link farthest and nearest enemy chain-transferring damage

##### Skill 2

protect weakest ally with dodge haste and sustained HP regeneration

##### Legendary+

ATK scales after damage-link chain breaks the first time

##### Mythic+

chain break heals allies; resets for multiple casts per battle

##### Supreme+

chain transfer stuns on break; protected ally gains unaffected

### Units Lorsan benefits from

Look for units providing: `ATK` `Haste` `Healing`  
Common buffers are **Hugin**, **Mikola**, or **Twins**.

- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Velara**
  - Haste buff (single target, high) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Solise**
  - Healing (all units, high)
- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (single target, high)

### Units benefitting most from Lorsan

**14** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Alna
- Berial
- Bryon
- Callan
- Evie
- Granny Dahnie
- Igor
- Lucius
- Ludovic
- Phraesto

### Units that can act as a replacement for Lorsan

**Buffs on allies**

- Hewynn (100% `Healing`)
- Solise (100% `Healing`)
- Smokey & Meerky (80% `Healing`)

**Similar Skills**

- Arden (100% `aoe-damage` `dot-specialist`)
- Faramor (80% `aoe-damage` `dot-specialist`)
- Viperian (66% `aoe-damage` `dot-specialist`)

**Damage**

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Cassadee (100% `Magic`)

**Crowd Control**

- Antandra (100% `Stun`)
- Arden (100% `Stun`)
- Faramor (100% `Stun`)

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

- **Signature skill**: Quake Slam (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Ally composition**: place adjacent allies behind at battle prep (DEF buff)
- **Ally composition**: place allies on adjacent tiles behind at battle start (shields and ATK boost)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `low`

##### Ultimate

slam target to origin tile or slam adjacent area, stunning

##### Skill 1

gain shield then shoulder-charge disabling enemy

##### Skill 2

cleanse own debuffs and reduce damage taken briefly

##### Legendary+

battle max HP increase

##### Mythic+

steadfast; gain shield from each adjacent supporting ally

##### Supreme+

adjacent allies reduce damage taken; melee hit triggers free ultimate

### Units Lucca benefits from

Look for units providing: `Max HP` `Healing` `Physical DEF` `Magic DEF`  
Common buffers are **Rowan**, **Hepler**, or **Hugin**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Fay**
  - Healing (arc, medium, conditional (frequent))
  - DEF buff (multiple targets, low)
  - DEF buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`
- **Damian**
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`

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

gain heal for weakest ally whenever gaining a shield

##### Legendary+

battle healing stat increase

##### Mythic+

frontal line attack reduces enemy ATK; gain shield per hit

##### Supreme+

heal one extra ally per cast

### Units Lucius benefits from

Look for units providing: `Healing`  
Common buffers are **Rowan**, **Lyca**, or **Smokey & Meerky**.

- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Damian**
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Velara**
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Lucius

- Daimon
- Eironn
- Gerda

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

strike top damage dealer, stunning and returning to tile

##### Skill 2

ultimate triggers transformation with AoE swirl attacks

##### Legendary+

battle haste increase

##### Mythic+

companion shields weakest ally with large barrier

##### Supreme+

ally at full energy grants companion ATK speed boost

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

- **Signature skill**: Eternal Serenity (ultimate)
- **Movement**: stationary (no finite attack range)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, damage `high`

##### Ultimate

generate healing field at position restoring adjacent allies

##### Skill 1

throw projectiles at top attacker, dealing sustained HP-loss

##### Skill 2

move field to weakest ally, absorbing nearby enemy HP

##### Legendary+

battle healing stat scales with field total healing stored

##### Mythic+

field produces consumables that AoE heal and damage on explode

##### Supreme+

enemies entering field take damage and are stunned

### Units Ludovic benefits from

Look for units providing: `Healing`  
Common buffers are **Rowan**, **Lyca**, or **Smokey & Meerky**.

- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Damian**
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Velara**
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Ludovic

- Himmel
- Perseus
- Silven

### Units that can act as a replacement for Ludovic

**Buffs on allies**

- Antandra (100% `Healing`)
- Contess (100% `Healing`)
- Damian (100% `Healing`)

**Similar Skills**

- Fay (100% `ally-healer` `aoe-healing`)
- Hewynn (100% `ally-healer` `aoe-healing`)
- Smokey & Meerky (100% `ally-healer` `aoe-healing`)

**Damage**

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Cassadee (100% `Magic`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Arden (100% `Stun`)

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

- **Signature skill**: Lumont's Charge (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

##### Ultimate

charge to tile, pushing enemies along; taunt on arrival

##### Skill 1

large shield growing per adjacent enemy

##### Skill 2

stomp, stunning adjacent enemies; cooldown reduced per hit

##### Legendary+

battle haste grows with nearby enemy count

##### Mythic+

sustained damage taken triggers multi-ring slam with ATK reduction

##### Supreme+

regenerate HP each second while shielded

### Units Lumont benefits from

Look for units providing: `Haste` `Max HP` `Healing`  
Common buffers are **Hugin**, **Twins**, or **Rowan**.

- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Velara**
  - Haste buff (single target, high) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Pandora**
  - Max HP buff (single target, medium)
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)

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

- **Signature skill**: Comet Archery (ultimate)
- **Movement**: stationary (avg attack range 11.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `medium`

##### Ultimate

line shot leaves AoE aura zone buffing allies

##### Skill 1

buff all allies ATK speed and grant energy at battle start

##### Skill 2

AoE rain reduces enemy DEF

##### Legendary+

battle ATK speed increase

##### Mythic+

persistent companion attacks with normal attacks; enhanced shot breaks shields

##### Supreme+

ultimate hit permanently reduces target DEF

### Units Lyca benefits from

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Twins**, **Hugin**, or **Rowan**.

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

### Units benefitting most from Lyca

**75** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight
- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Perseus
- Indris
- Silven
- Nerion
- Aliceth
- Cecia
- Cyran
- Dionel
- Fay
- Gwyneth

### Units that can act as a replacement for Lyca

**Damage**

- Alna (100% `Physical`)
- Athalia (100% `Physical`)
- Dionel (100% `Physical`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Arden (100% `Stun`)

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

- **Signature skill**: Silver-White Wings that Streak Across the Skies (ultimate)
- **Movement**: stationary (no finite attack range)
- **Ally composition**: place ally 1 tile in front at battle prep (revive target)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, damage `high`

##### Ultimate

Passive: channeling stacks permanent haste; Active: periodic line AoE damage across battlefield

##### Skill 1

AoE explosion after channeling completes

##### Skill 2

AoE blind and ally heal after channeling

##### Legendary+

battle haste grows with each completed channel

##### Mythic+

channel revives one allied hero once per battle

##### Supreme+

active ally buffs grant extra energy recovery while channeling

### Units Marcille benefits from

Look for units providing: `ATK SPD / Haste` `Energy`  
Common buffers are **Lyca**, **Twins**, or **Hugin**.

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
- **Mehira**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Marcille

- Perseus
- Himmel
- Silven

### Units that can act as a replacement for Marcille

**Buffs on allies**

- Antandra (100% `Healing`)
- Contess (100% `Healing`)
- Gerda (100% `Healing`)

**Damage**

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Cassadee (100% `Magic`)

**Crowd Control**

- Gerda (60% `Interrupt`)
- Lily May (60% `Interrupt`)
- Reinier (60% `Interrupt`)

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

- **Signature skill**: Mid-Air Shot (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `low`
- **True damage**: True damage `low`

##### Ultimate

leap and shoot two closest targets

##### Skill 1

enhanced normal attack every few hits with brief stun

##### Skill 2

ATK and ATK speed increase when no close enemy present

##### Legendary+

battle crit damage boost

##### Mythic+

ATK stacks from each ally ultimate; true damage at max stacks

##### Supreme+

required no-enemy distance for ATK speed bonus shortened

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

- **Signature skill**: Euphoric Rush (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `low`

##### Ultimate

multi-hit blast then charmed AoE burst on targets

##### Skill 1

melee hits cause HP-loss; allies gain haste from it

##### Skill 2

decoy taunts all enemies to rush toward it

##### Legendary+

life drain and ATK scale with received healing

##### Mythic+

summon sacrificial minions to block fatal blows

##### Supreme+

charmed and taunted targets take increased damage

### Units Mehira benefits from

Look for units providing: `Haste` `Max HP` `Healing`  
Common buffers are **Hugin**, **Twins**, or **Rowan**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Solise**
  - Healing (all units, high)
  - Max HP via Shield (summons only, medium)
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Velara**
  - Haste buff (single target, high) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
  - Max HP via Shield (summons only, medium)

### Units benefitting most from Mehira

- Nerion
- Carolina
- Perseus

### Units that can act as a replacement for Mehira

**Buffs on allies**

- Damian (100% `Haste`)
- Galahad (100% `Haste`)
- Hugin (100% `Haste`)

**Damage**

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Cassadee (100% `Magic`)

**Debuffs on enemies**

- Berial (100% `Damage taken debuff`)
- Bonnie (100% `Damage taken debuff`)
- Cryonaia (100% `Damage taken debuff`)

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

- **Signature skill**: Dauntless Hymn (ultimate)
- **Movement**: moving (avg attack range 2.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, buffs `medium`, damage `low`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `low`

##### Ultimate

mobile aura zone follows caster; nearby allies gain haste and ranged DEF; damage threshold triggers heal wave

##### Skill 1

control arena; side with more units gains healing and ATK

##### Skill 2

heal self and two weakest allies with DEF boost

##### Legendary+

ATK scales while own side holds arena control

##### Mythic+

enhanced aura grants combat fury with sustained area damage

##### Supreme+

aura duration frozen when own side controls arena

### Units Mikola benefits from

Look for units providing: `ATK` `Haste`  
Common buffers are **Twins**, **Hugin**, or **Lyca**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
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

### Units benefitting most from Mikola

**34** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Perseus
- Silven
- Himmel
- Hepler
- Lorsan
- Seth
- Sylphira
- Tasi
- Vala
- Laios

### Units that can act as a replacement for Mikola

**Damage**

- Alna (100% `Physical`)
- Athalia (100% `Physical`)
- Dionel (100% `Physical`)

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

post-first-ultimate AoE fire becomes permanent normal; burns added

##### Supreme+

extend burn duration; ATK speed surge on each burn applied

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

- **Signature skill**: Phantom Chains (Skill 1)
- **Movement**: mostly stationary (pulls enemies)

#### Skill overview

- **Signature skill**: speed `fast`
- **Ultimate**: speed `fast`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, damage `low`
- **True damage**: Max HP-based damage `medium`, True damage `high`

##### Ultimate

start full energy; execute low HP targets with true damage

##### Skill 1

pull distant enemy hero; HP-loss damage per tile pulled

##### Skill 2

strike knock up then rapid follow-up attacks

##### Legendary+

ATK grows after each assist or defeat

##### Mythic+

execute kill triggers shockwave healing all allies

##### Supreme+

chain pull applies slow and permanent max HP reduction

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

- Antandra (100% `Healing`)
- Contess (100% `Healing`)
- Damian (100% `Healing`)

**Damage**

- Shadewing (100% `Max HP-based damage` `True damage`)
- Korin (96% `Max HP-based damage` `True damage` `Physical`)
- Indris (84% `True damage` `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Alna (100% `Vitality debuff`)
- Dionel (100% `Vitality debuff`)
- Faramor (100% `Vitality debuff`)

**Crowd Control**

- Baelran (100% `Knock down` `Knock up`)
- Kordan (100% `Knock down` `Knock up`)
- Lucca (100% `Knock down` `Knock up`)

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

- **Signature skill (ultimate)**: speed `normal`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`
- **True damage**: Max HP-based damage `low`

##### Ultimate

mode choice: frontal stun AoE or single high damage strike

##### Skill 1

mode choice: haste debuff attack or HP-based knock down damage

##### Skill 2

rage grants ATK and DEF boost after first ally defeat

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
- **Velara**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

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

- **Signature skill**: Rend Rupture (ultimate)
- **Movement**: stationary (avg attack range 10.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, damage `high`
- **Non-ultimate**: speed `fast`, debuffs `medium`, damage `medium`
- **True damage**: Max HP-based damage `low`, True damage `high`

##### Ultimate

guaranteed critical throw, dealing true damage then detonate stacks

##### Skill 1

crit hits deal extra HP-based true damage reducing target max HP

##### Skill 2

target highest healer with damage stun and anti-heal

##### Legendary+

crit stat grows after accumulating debuff stacks

##### Mythic+

debuffed target crit resist reduced; allies add stacks on crit hits

##### Supreme+

crit damage boosts further per point of crit rate

### Units Nazrik benefits from

Look for units providing: `CRIT`  
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

### Units benefitting most from Nazrik

- Indris
- Nerion
- Carolina

### Units that can act as a replacement for Nazrik

**Damage**

- Indris (100% `True damage` `Physical` `Max HP-based damage`)
- Nara (100% `True damage` `Physical` `Max HP-based damage`)
- Korin (93% `True damage` `Physical` `Max HP-based damage`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Arden (100% `Stun`)

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

- **Signature skill**: Drowning Doom (ultimate)
- **Movement**: mostly stationary (avg attack range 4.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

##### Ultimate

Passive: prolonged control inflicts sustained DoT debuff; Active: empowerment state

##### Skill 1

enhanced attack every few normal attacks with knock back and stun

##### Skill 2

projectile then delayed water eruption knock up

##### Legendary+

battle ATK speed increase

##### Mythic+

battle-start apply sustained DoT to rearmost enemy immediately

##### Supreme+

all enemies DoT-afflicted grants permanent empowered state

### Units Nerion benefits from

Look for units providing: `ATK SPD / Haste` `Max HP` `Energy` `DEF Penetration`  
Common buffers are **Hepler**, **Lyca**, or **Ravion**.

- **Tasi**
  - Enables CC on enemies via Sleep (all units, high)
- **Baelran**
  - Enables CC on enemies via Knock up (area, high)
- **Carolina**
  - Enables CC on enemies via Bind (area, high)
- **Indris**
  - Enables CC on enemies via Knock back (area, high)
- **Kordan**
  - Enables CC on enemies via Bind (area, high)

### Units benefitting most from Nerion

- Bonnie
- Carolina
- Indris

### Units that can act as a replacement for Nerion

**Similar Skills**

- Shadewing (100% `dot-specialist` `enemy-debuffer`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Debuffs on enemies**

- Athalia (100% `ATK debuff`)
- Bonnie (100% `ATK debuff`)
- Contess (100% `ATK debuff`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Arden (100% `Stun`)

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

- **Signature skill**: Soul Shepherd (ultimate)
- **Movement**: stationary (no finite attack range)
- **Ally composition**: nearest ally auto-selected at battle start; prioritizes ally behind

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, damage `medium`
- **True damage**: HP loss `low`

##### Ultimate

block fatal blow on weakest ally; they return at partial HP with reduced damage until HP depletes

##### Skill 1

attack weakest enemy with HP-loss bonus damage

##### Skill 2

drain all enemy HP restoring equal amount to weakest ally

##### Legendary+

battle max HP increase

##### Mythic+

battle-start automatically casts fatal-blow save on nearest ally

##### Supreme+

replace normal attacks with drain; bonus DEF to specific allies

### Units Niru benefits from

Look for units providing: `Healing` `Physical DEF` `Magic DEF`  
Common buffers are **Rowan**, **Lyca**, or **Smokey & Meerky**.

- **Solise**
  - Healing (all units, high)
  - Enables Ally blessing active via Ally blessing
- **Lorsan**
  - Healing (all units, high)
- **Fay**
  - Healing (arc, medium, conditional (frequent))
  - DEF buff (multiple targets, low)
  - DEF buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) `signature fuel`
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Damian**
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`

### Units benefitting most from Niru

- Bonnie
- Zorya
- Himmel

### Units that can act as a replacement for Niru

**Damage**

- Dunlingr (100% `Magic` `HP loss`)
- Shadewing (100% `Magic` `HP loss`)
- Zorya (100% `Magic` `HP loss`)

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

- **Signature skill**: Heart Crusher (Mythic+)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)

#### Skill overview

- **Signature skill**: speed `fast`, debuffs `medium`
- **Ultimate**: speed `slow`, debuffs `medium`, damage `low`
- **Non-ultimate**: speed `fast`, debuffs `medium`, damage `low`

##### Ultimate

apply persistent poison DoT to target that grows on hits

##### Skill 1

triple penetrating normal attack sequence

##### Skill 2

normal attacks on poisoned targets stack DoT base damage

##### Legendary+

battle ATK speed increase

##### Mythic+

instantly defeat poisoned enemies below HP threshold

##### Supreme+

normal attack bonus damage scales with DoT rate

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
- Mirael (100% `DoT` `Magic`)

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

- **Signature skill**: Boxed Blessing (Skill 1)
- **Movement**: stationary (no finite attack range)
- **Ally composition**: rearmost ally enters invincible box, then gains Energy and ATK

#### Skill overview

- **Signature skill**: speed `fast`, buffs `medium`
- **Ultimate**: speed `slow`, debuffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `medium`

##### Ultimate

AoE frighten all units fleeing; enemies ATK reduced after

##### Skill 1

pull rearmost ally into invincible enclosure then release empowered

##### Skill 2

each skill cast restores released ally and spreads debuff

##### Legendary+

battle max HP grows with debuff stack count

##### Mythic+

enclosure persists after defeat continuing to fire debuffs

##### Supreme+

pulled ally permanently immune to AoE frighten effect

### Units Pandora benefits from

Look for units providing: `Energy`  
Common buffers are **Rowan**, **Smokey & Meerky**, or **Ravion**.

- **Thador**
  - Energy recovery (single target, low) `signature fuel`

### Units benefitting most from Pandora

- Indris
- Salazer
- Chippy
- Satrana
- Nara
- Scarlita

### Units that can act as a replacement for Pandora

**Buffs on allies**

- Rowan (66% `Healing` `Max HP` `Energy`)

**Damage**

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Cassadee (100% `Magic`)

**Debuffs on enemies**

- Sinbad (80% `ATK debuff` `Vitality debuff` `Damage taken debuff` `Energy drain`)

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

- **Signature skill**: Sky Splitter (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `medium`

##### Ultimate

meditate then burst AoE entering sustained drain-powered buff state

##### Skill 1

large strike with bonus damage based on target current HP

##### Skill 2

personal shield releases burst damage on expiry

##### Legendary+

battle ATK grows while in enhanced combat buff state

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
- Antandra (100% `Physical`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Arden (100% `Stun`)

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

- **Signature skill**: Floral Splendor (ultimate)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `low`

##### Ultimate

Passive: mark enemies; Active: burst hits all marked targets

##### Skill 1

ATK speed and normal damage boost to self and nearest ally

##### Skill 2

periodic line attack deals damage and restores energy

##### Legendary+

battle ATK increase

##### Mythic+

mark at start; normal attacks hit extra targets after accumulating marks

##### Supreme+

reduce normal attacks needed to trigger periodic trigger

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

- **Signature skill**: Divine Rend (ultimate)
- **Movement**: moving (avg attack range 2.9 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `high`
- **True damage**: True damage `low`

##### Ultimate

advance with repeated multi-hit then terminal shield bash stun

##### Skill 1

broad spin, dealing damage while gaining shield and ATK speed

##### Skill 2

nearby terrain buff boosts ally ATK and DEF; low HP threshold expands own max HP

##### Legendary+

ATK boost grows with temporary ally buffs active

##### Mythic+

ally buffs amplified; extra damage and damage reduction from each

##### Supreme+

expand ally terrain buff area by one tile

### Units Perseus benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `Max HP`  
Common buffers are **Lyca**, **Hugin**, or **Rowan**.

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
- **Cecia**
  - ATK SPD buff (single target, low) `signature fuel`
  - Max HP buff (single target, high)
  - Enables Ally stat buffs via 4 ally stat buffs
- **Evie**
  - ATK buff (multiple targets, high)
  - Enables Ally stat buffs via 2 ally stat buffs (start of battle)

### Units benefitting most from Perseus

- Nerion
- Carolina
- Silven

### Units that can act as a replacement for Perseus

**Buffs on allies**

- Evie (100% `ATK`)
- Hugin (100% `ATK`)
- Mikola (100% `ATK`)

**Similar Skills**

- Hammie (60% `ally-buffer`)
- Sonja (60% `ally-buffer`)

**Damage**

- Athalia (100% `Physical` `True damage`)
- Baelran (100% `Physical` `True damage`)
- Dionel (100% `Physical` `True damage`)

**Crowd Control**

- Lucca (80% `Stun`)
- Cassadee (70% `Knock back` `Stun`)
- Antandra (66% `Stun`)

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

- **Signature skill**: Crimson Contract (Skill 1)
- **Movement**: moving (avg attack range 1.8 tiles)
- **Ally composition**: place allies 1 tile behind this hero and the Illusion for contract buffs
- **Self placement**: keep this hero and Illusion in the same row (damage reduction and battle-start shields)

#### Skill overview

- **Signature skill**: speed `slow`, buffs `medium`, damage `low`
- **Ultimate**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `high`

##### Ultimate

clone on same row shares damage reduction with caster until one falls

##### Skill 1

Passive: clone and self grant rear allies stat contracts; Active: frontal multi-strike

##### Skill 2

single-target hit applies sustained HP drain, haste reduction, and vitality reduction

##### Legendary+

DEF boost shared with clone; energy cross-transfers on damage

##### Mythic+

clone defeat triggers taunt burst stun

##### Supreme+

both in same row gain initial shield at battle start

### Units Phraesto benefits from

Look for units providing: `Healing` `Energy`  
Common buffers are **Smokey & Meerky**, **Rowan**, or **Hewynn**.

- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, medium)
- **Koko**
  - Healing (all units, medium)

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

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Crowd Control**

- Antandra (100% `Stun` `Taunt`)
- Granny Dahnie (100% `Stun` `Taunt`)
- Hepler (100% `Stun` `Taunt`)

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

- **Signature skill**: Chaos Manifest (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, damage `medium`
- **Non-ultimate**: speed `fast`, debuffs `medium`, damage `medium`
- **True damage**: True damage `medium`

##### Ultimate

immobilize two rearmost then teleport them onto target tile

##### Skill 1

scatter magic missiles at enemies; out-of-control hits allies

##### Skill 2

magical growth on area with most enemies, dealing damage and draining energy

##### Legendary+

battle haste scales with controlled consecutive casts

##### Mythic+

first cast guaranteed; mutation adds true damage and immobilize

##### Supreme+

teleport targets take extra max HP damage on delayed landing

### Units Pippa benefits from

Look for units providing: `Haste`  
Common buffers are **Twins**, **Hugin**, or **Lyca**.

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
- **Velara**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Pippa

- Bonnie
- Indris
- Aliceth

### Units that can act as a replacement for Pippa

**Similar Skills**

- Kordan (100% `hp-scaling` `self-repositioner`)
- Athalia (66% `hp-scaling` `self-repositioner`)
- Marilee (66% `hp-scaling` `self-repositioner`)

**Damage**

- Indris (100% `True damage` `Max HP-based damage`)
- Sylphira (100% `True damage` `Magic` `Max HP-based damage`)
- Shadewing (84% `Magic` `Max HP-based damage` `True damage`)

**Debuffs on enemies**

- Lily May (100% `Energy drain`)
- Sinbad (75% `Energy drain`)
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

- **Signature skill**: Killer Flush (ultimate)
- **Movement**: high movement (repositioning skills)
- **Ally composition**: Objectives go to the 2 rearmost allies; backline heroes receive ATK and Energy on completion

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `medium`
- **True damage**: HP loss `low`

##### Ultimate

multi-hit fan, dealing damage scaling on target HP-loss

##### Skill 1

assign objectives to two rearmost allies; completion rewards energy and ATK

##### Skill 2

teleport multiple times to areas with most enemies then retreat to safety

##### Legendary+

ATK bonus activates after first enhanced strike

##### Mythic+

enhanced strike unlocks permanent haste and ATK for self and allies

##### Supreme+

assigned ally tasks grant brief ATK boost and unaffected state

### Units Ravion benefits from

Look for units providing: `ATK` `Haste` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
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

### Units benefitting most from Ravion

**22** units include this provider among their top 5 synergy partners. Why the match is common:

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
- Hewynn

### Units that can act as a replacement for Ravion

**Buffs on allies**

- Smokey & Meerky (75% `Energy` `ATK`)

**Similar Skills**

- Hugin (66% `ally-shielder` `energy-provider`)

**Damage**

- Aliceth (100% `Physical` `HP loss`)
- Athalia (100% `Physical` `HP loss`)
- Faramor (100% `Physical` `HP loss`)

**Debuffs on enemies**

- Lyca (100% `ATK debuff` `Phys DEF debuff`)
- Sinbad (100% `ATK debuff` `Phys DEF debuff`)
- Kafra (90% `ATK debuff` `Phys DEF debuff`)

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

- **Signature skill**: Dynamic Balance (Skill 1)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill**: speed `fast`, heal `medium`, damage `high`
- **Ultimate**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, debuffs `medium`, damage `high`

##### Ultimate

temporarily removes enemy from battlefield alone or with caster

##### Skill 1

battle-start swap symmetrical ally-enemy positions; damage heals ally

##### Skill 2

multi-hit attack on healthiest enemy while off battlefield

##### Legendary+

position swap boosts ally ATK or reduces enemy ATK

##### Mythic+

swap enemy takes permanent damage increase

##### Supreme+

symmetrical ally gains ATK boost while in position

### Units Reinier benefits from

Look for units providing: `Healing`  
Common buffers are **Hewynn**, **Smokey & Meerky**, or **Mikola**.

- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Koko**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Contess**
  - Healing (multiple targets, high)

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

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Cassadee (100% `Magic`)

**Debuffs on enemies**

- Bonnie (100% `ATK debuff` `Damage taken debuff`)
- Pandora (100% `ATK debuff` `Damage taken debuff`)
- Sinbad (100% `ATK debuff` `Damage taken debuff`)

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

- **Signature skill**: Flame Barrage (ultimate)
- **Movement**: high movement (moves while attacking)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

##### Ultimate

continuous walking arc fire burst with loaded-shot cycle

##### Skill 1

Passive: crit boost; Active: control immunity and self-heal

##### Skill 2

load knock back shot for next attack

##### Legendary+

battle crit damage boost scales with splash shots equipped

##### Mythic+

movement loads splash shots for enhanced area attacks

##### Supreme+

control immunity cooldown reduced; blast ultimate freezes time

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

- **Signature skill**: Fatal Greed (ultimate)
- **Movement**: moving (repositions on cast)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `medium`

##### Ultimate

restore energy to surrounding allies

##### Skill 1

place consumable heals triggered when ally HP drops low

##### Skill 2

companion attacks draining energy; replenishes heals when depleted

##### Legendary+

battle haste bonus before first heal restock

##### Mythic+

multiple heal uses unlock enhanced heal with permanent DEF boost

##### Supreme+

place one extra heal at battle start

### Units Rowan benefits from

Look for units providing: `Haste` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Lyca**.

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
- **Velara**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Rowan

**76** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Perseus
- Silven
- Granny Dahnie
- Zorya
- Antandra
- Shemira
- Soren
- Temesia
- Niru
- Aliceth

### Units that can act as a replacement for Rowan

**Similar Skills**

- Twins (66% `ally-healer` `energy-provider`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Debuffs on enemies**

- Dunlingr (100% `Energy drain`)
- Lily May (100% `Energy drain`)
- Pippa (100% `Energy drain`)

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

- **Signature skill**: Seed Siphon (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `fast`, debuffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `high`

##### Ultimate

teleport to enemy, immobilize, drain energy, and plant marker

##### Skill 1

self-heal proportional to all damage dealt; excess becomes shield

##### Skill 2

consume a planted marker to revive after defeat

##### Legendary+

damage reduction grows per active marker count

##### Mythic+

markers weaken attacker damage and accelerate DoT interval

##### Supreme+

battle-start markers on allied heroes grant protective shields

### Units Saida benefits from

Look for units providing: `Max HP` `Healing`  
Common buffers are **Hepler**, **Hewynn**, or **Rowan**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Antandra**
  - Healing (multiple targets, high)
- **Contess**
  - Healing (multiple targets, high)

### Units benefitting most from Saida

- Daimon
- Eironn
- Gerda
- Silvina
- Sonja
- Velara

### Units that can act as a replacement for Saida

**Buffs on allies**

- Hepler (100% `Max HP`)
- Hugin (100% `Max HP`)
- Lucius (88% `Max HP`)

**Similar Skills**

- Koko (66% `ally-shielder` `life-drain`)

**Damage**

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Cassadee (100% `Magic`)

**Debuffs on enemies**

- Dunlingr (100% `Energy drain`)
- Lily May (100% `Energy drain`)
- Pippa (100% `Energy drain`)

**Crowd Control**

- Reinier (100% `Interrupt` `Displace`)
- Gerda (64% `Interrupt`)
- Lily May (64% `Interrupt`)

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

- **Signature skill**: Rain of Blades (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, damage `low`
- **Non-ultimate**: speed `fast`, damage `medium`

##### Ultimate

nine strikes on highest-HP enemy; each hit scales on target current HP

##### Skill 1

arc strike; extra hit when target is low HP

##### Skill 2

imprison low HP enemy permanently, absorbing their ATK

##### Legendary+

battle damage taken reduction

##### Mythic+

charge state triggers free skill casts on form change or bind

##### Supreme+

imprisoned enemy defeat grants shield and self-healing

### Units Salazer benefits from

Look for units providing: `Max HP` `Healing`  
Common buffers are **Rowan**, **Lyca**, or **Hepler**.

- **Pandora**
  - Max HP buff (single target, medium)
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Damian**
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`

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

- **Signature skill**: Fiery Dance (ultimate)
- **Movement**: moving (avg attack range 1.5 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `medium`
- **True damage**: Max HP-based damage `high`

##### Ultimate

spin AoE; final hit charms enemies

##### Skill 1

frontal arc strike with HP-based extra damage and lifesteal

##### Skill 2

buff shared with allies burns targets after enough hits

##### Legendary+

battle damage taken reduction

##### Mythic+

damage reduction grows for each ignited enemy hero

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
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`

### Units benefitting most from Satrana

- Indris
- Shadewing
- Bonnie

### Units that can act as a replacement for Satrana

**Buffs on allies**

- Koko (100% `Damage taken reduction`)
- Shakir (100% `Damage taken reduction`)
- Soren (100% `Damage taken reduction`)

**Similar Skills**

- Mirael (66% `dot-specialist` `fire-attack`)

**Damage**

- Daimon (100% `Max HP-based damage` `Magic`)
- Shadewing (100% `Max HP-based damage` `Magic`)
- Shemira (100% `Max HP-based damage` `Magic`)

**Debuffs on enemies**

- Frieren (70% `Vitality debuff` `DoT`)
- Sinbad (66% `Vitality debuff`)

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

- **Signature skill**: Divine Wrath (Mythic+)
- **Movement**: moving (brief reposition)

#### Skill overview

- **Signature skill**: speed `fast`, damage `low`
- **Ultimate**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `medium`
- **True damage**: True damage `low`

##### Ultimate

battle-start hover invincible, gaining ATK; descend triggers ground smash

##### Skill 1

while airborne send ally shields; descend triggers arc sweep knock down

##### Skill 2

execution scales with blessings sent while airborne

##### Legendary+

true damage and AoE knockout available with enough surviving allies

##### Mythic+

aerial blessings also transfer own DEF to protected ally

##### Supreme+

instant shield for ally when their shield drops critically low

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

**Similar Skills**

- Korin (66% `ally-shielder` `hp-scaling`)

**Damage**

- Athalia (100% `Physical` `True damage`)
- Baelran (100% `Physical` `True damage`)
- Dionel (100% `Physical` `True damage`)

**Crowd Control**

- Baelran (69% `Knock up` `Knock down`)
- Cassadee (65% `Knock back` `Knock up` `Stun`)
- Lucca (63% `Knock up` `Knock down` `Stun`)

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

- **Signature skill**: Shadow Strike (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, buffs `medium`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `low`

##### Ultimate

multi-hit flash then brief bind; final leap strike with self-heal

##### Skill 1

pounce on weakest target with lost HP bonus damage

##### Skill 2

stacks from enemy HP thresholds, boosting haste and drain

##### Legendary+

battle ATK increase

##### Mythic+

cooldown and energy reset on each enemy defeat

##### Supreme+

frenzy stacks further reduce target DEF on pounce

### Units Seth benefits from

Look for units providing: `ATK` `Haste` `CRIT` `Healing` `Energy`  
Common buffers are **Rowan**, **Mikola**, or **Twins**.

- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Velara**
  - Haste buff (single target, high) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)

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

- **Signature skill**: Withering Curse (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill**: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`
- **Ultimate**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`
- **True damage**: HP loss `low`, Max HP-based damage `high`, True damage `low`

##### Ultimate

sustained DoT per second scaling on target lost HP

##### Skill 1

dual strike then sustained wound DoT

##### Skill 2

battle-start dash through foes, applying persistent DEF reduction

##### Legendary+

battle ATK increase

##### Mythic+

trigger hits build energy and permanent damage boost

##### Supreme+

drain ally HP at start for lasting ATK boost and shield

### Units Shadewing benefits from

Look for units providing: `ATK` `Max HP` `Energy` `Life Drain`  
Common buffers are **Lyca**, **Hepler**, or **Rowan**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Enables Debuff on target via DoT (all units)
  - Enables Continuous damage on enemies via Burn
- **Bryon**
  - Enables Debuff on target via Haste debuff (area)
  - Enables Continuous damage on enemies via DoT
- **Frieren**
  - Enables Debuff on target via DoT (area)
  - Enables Continuous damage on enemies via DoT + Burn
- **Cecia**
  - Max HP buff (single target, high)
  - Lifedrain buff (area, high)
  - Enables Continuous damage on enemies via DoT
- **Alna**
  - ATK buff (single target, medium)
  - Max HP buff (single target, low)
  - Enables Debuff on target via Haste debuff (area)

### Units benefitting most from Shadewing

- Bonnie
- Indris
- Aliceth

### Units that can act as a replacement for Shadewing

**Similar Skills**

- Nerion (100% `dot-specialist` `enemy-debuffer`)

**Damage**

- Nara (66% `Max HP-based damage` `True damage`)

**Debuffs on enemies**

- Eironn (90% `Magic DEF debuff`)
- Sinbad (60% `Magic DEF debuff`)

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

- **Signature skill**: Ravaging Claws (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `medium`

##### Ultimate

transformation form AoE normal attacks with sustained energy drain

##### Skill 1

three-hit frontal arc; enhanced third hit

##### Skill 2

passive ranged DEF; transformation unaffected with drain and aura buff

##### Legendary+

battle damage taken reduction grows with aura allies

##### Mythic+

transformation sustained at lower energy threshold

##### Supreme+

third hit reduces target vitality

### Units Shakir benefits from

Look for units providing: `Haste`  
Common buffers are **Twins**, **Hugin**, or **Lyca**.

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
- **Velara**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Shakir

**17** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Atalanta
- Hepler
- Lenya
- Mehira
- Mikola
- Pang
- Ravion
- Soren
- Sylphira
- Dionel

### Units that can act as a replacement for Shakir

**Buffs on allies**

- Koko (68% `Damage taken reduction` `Life Drain`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Alna (100% `Vitality debuff`)
- Dionel (100% `Vitality debuff`)
- Faramor (100% `Vitality debuff`)

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

- **Signature skill**: Phantom Procession (ultimate)
- **Movement**: mostly stationary (avg attack range 4.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `high`
- **True damage**: Max HP-based damage `high`

##### Ultimate

Passive: summons join attacks; Active: sustained summon AoE and self-heal

##### Skill 1

HP sacrifice fires orb line, dealing area damage

##### Skill 2

Passive: summon on ally losing HP; Active: true damage HP sacrifice

##### Legendary+

battle energy recovery from attacks grows with summon count

##### Mythic+

summon expiry converts remaining power to all-enemy damage

##### Supreme+

each hero defeat spawns an extra summon

### Units Shemira benefits from

Look for units providing: `Max HP` `Healing` `Energy`  
Common buffers are **Rowan**, **Lyca**, or **Smokey & Meerky**.

- **Pandora**
  - Max HP buff (single target, medium)
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Damian**
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`

### Units benefitting most from Shemira

- Bonnie
- Himmel

### Units that can act as a replacement for Shemira

**Similar Skills**

- Daimon (72% `hp-scaling` `life-drain` `summoner`)
- Zorya (60% `hp-scaling` `life-drain`)

**Damage**

- Daimon (100% `Max HP-based damage` `Magic`)
- Shadewing (100% `Max HP-based damage` `Magic`)
- Satrana (97% `Max HP-based damage` `Magic`)

### Summary for Shemira

#### Damage types dealt by Shemira

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target
- Max HP-based damage — Area, Single target — `high`

## Silven

### Silven's behavior

- **Signature skill**: Gravity Collapse (Skill 1)
- **Movement**: stationary (avg attack range 12.0 tiles)

#### Skill overview

- **Signature skill**: speed `fast`, damage `high`
- **Ultimate**: speed `fast`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `high`
- **True damage**: True damage `low`

##### Ultimate

summon flying blades that augment normal attacks

##### Skill 1

mark triggers cluster detonation and knock down

##### Skill 2

standing still sharpens blades for true damage bonus

##### Legendary+

battle ATK speed increase

##### Mythic+

ally buff triggers energy gain and penetration boost

##### Supreme+

deal bonus damage to enemies with high HP ratio

### Units Silven benefits from

Look for units providing: `ATK SPD / Haste` `Energy` `DEF Penetration` `Physical DEF`  
Common buffers are **Lyca**, **Rowan**, or **Hugin**.

- **Koko**
  - Enables Ally stat buffs via 5 ally stat buffs
- **Cecia**
  - ATK SPD buff (single target, low) `signature fuel`
  - DEF Penetration buff (single target, medium)
  - Enables Ally stat buffs via 4 ally stat buffs
- **Velara**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
  - Enables Ally stat buffs via 2 ally stat buffs (start of battle)
- **Aliceth**
  - DEF Penetration buff (multiple targets, high)
  - Enables Ally stat buffs via 4 ally stat buffs
- **Shakir**
  - Enables Ally stat buffs via 3 ally stat buffs

### Units benefitting most from Silven

- Nerion
- Carolina
- Bonnie

### Units that can act as a replacement for Silven

**Buffs on allies**

- Aliceth (100% `DEF Penetration`)
- Cecia (100% `DEF Penetration`)
- Dionel (100% `DEF Penetration`)

**Similar Skills**

- Tilaya (100% `hp-scaling`)
- Korin (60% `hp-scaling`)
- Sonja (60% `hp-scaling`)

**Damage**

- Pippa (100% `Magic` `True damage`)
- Shadewing (100% `Magic` `True damage`)
- Sylphira (100% `Magic` `True damage`)

**Crowd Control**

- Antandra (100% `Knock down`)
- Athalia (100% `Knock down`)
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

- **Signature skill**: Shadow Slayer (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, debuffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `medium`

##### Ultimate

battle-start rush mark nearest symmetrical enemy stun

##### Skill 1

sustained rapid normal attacks in opening window; extended on mark kill

##### Skill 2

battle crit increase

##### Legendary+

post-first-strike shield blocking damage

##### Mythic+

rapid attacks frighten nearby enemies on mark target defeat

##### Supreme+

rapid attack hits also reduce target vitality

### Units Silvina benefits from

Look for units providing: `Max HP` `CRIT`  
Common buffers are **Hugin**, **Twins**, or **Hepler**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, medium)
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
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Hodgkin (100% `Energy drain` `Vitality debuff`)
- Sinbad (100% `Energy drain` `Vitality debuff`)
- Dunlingr (75% `Energy drain`)

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

- **Signature skill**: Whizzing Edge (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, damage `medium`
- **Non-ultimate**: speed `fast`, debuffs `medium`, damage `medium`

##### Ultimate

Passive: skills count as normal attacks; Active: sustained rapid strikes

##### Skill 1

battle-start mark two enemy roles; charge both with debuffs

##### Skill 2

double two-hit blade strike

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

### Units that can act as a replacement for Sinbad

**Similar Skills**

- Kafra (66% `enemy-debuffer` `mark-target`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

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

- **Signature skill**: Special Aroma (ultimate)
- **Movement**: stationary (no finite attack range)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, buffs `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

##### Ultimate

sustained channeled aura healing and energy recovery nearby

##### Skill 1

aura boosts ally ATK; scales with affected count

##### Skill 2

instant heal all allies inside aura

##### Legendary+

ATK boost grows with more allies inside aura

##### Mythic+

third aura upgrade empowers and drains enemy max HP

##### Supreme+

extra healing on each aura use

### Units Smokey & Meerky benefits from

Look for units providing: `ATK` `Healing` `Energy`  
Common buffers are **Mikola**, **Rowan**, or **Hewynn**.

- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (single target, high)
- **Koko**
  - Healing (all units, medium)

### Units benefitting most from Smokey & Meerky

**27** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner

These are the **10** strongest pairings: 

- Zorya
- Hodgkin
- Seth
- Vala
- Isabella
- Antandra
- Granny Dahnie
- Shemira
- Twins
- Hammie

### Units that can act as a replacement for Smokey & Meerky

**Buffs on allies**

- Rowan (69% `Energy` `Healing`)

**Similar Skills**

- Fay (100% `ally-healer` `aoe-healing`)
- Hewynn (100% `ally-healer` `aoe-healing`)
- Ludovic (100% `ally-healer` `aoe-healing`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Crowd Control**

- Gerda (96% `Interrupt` `Stun`)
- Lily May (80% `Interrupt`)
- Sylphira (80% `Interrupt`)

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

- **Signature skill**: Life's Embrace (ultimate)
- **Movement**: stationary (no finite attack range)

#### Skill overview

- **Signature skill (ultimate)**: speed `normal`, heal `medium`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `high`

##### Ultimate

healing waves restore allies; companion rings damage foes

##### Skill 1

battle-start send healing projectiles to all non-summoned allies

##### Skill 2

heal two weakest allies; shielded if companion present

##### Legendary+

ATK scales with companion count present

##### Mythic+

growth stage grants permanent DEF and ATK boost to host

##### Supreme+

companion damage scales on stored excess healing

### Units Solise benefits from

Look for units providing: `ATK`  
Common buffers are **Hugin**, **Mikola**, or **Lyca**.

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
- **Galahad**
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Solise

**12** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Dunlingr
- Niru
- Alna
- Bryon
- Callan
- Evie
- Igor
- Phraesto
- Reinier
- Saida

### Units that can act as a replacement for Solise

**Buffs on allies**

- Hewynn (92% `Healing`)
- Lorsan (92% `Healing`)
- Gerda (69% `Healing`)

**Similar Skills**

- Velara (90% `ally-healer` `ally-shielder` `aoe-healing`)
- Hewynn (80% `ally-healer` `aoe-healing`)
- Fay (66% `ally-healer` `aoe-healing`)

**Damage**

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Cassadee (100% `Magic`)

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

- **Signature skill**: Crimson Covenant (Skill 1)
- **Movement**: high movement (repositioning skills)
- **Ally composition**: place allies on left and right at battle start (Crimson Covenant buffs; prioritizes front row)

#### Skill overview

- **Signature skill**: speed `fast`, buffs `medium`
- **Ultimate**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `low`

##### Ultimate

multi-hit then charge through frontal area

##### Skill 1

adjacent ally bond, boosting ATK and DEF

##### Skill 2

spin slash stun adjacent enemies

##### Legendary+

battle haste grows after first ultimate cast

##### Mythic+

enhanced bond continuously accumulates bonuses while partners live

##### Supreme+

ultimate converts portion of damage dealt to self-healing

### Units Sonja benefits from

Look for units providing: `Haste` `Max HP`  
Common buffers are **Hugin**, **Twins**, or **Hepler**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
- **Lucius**
  - Max HP via Shield (area, medium)
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
- Antandra (100% `Physical`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Arden (100% `Stun`)

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

- **Signature skill**: Whirlwind Swing (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

##### Ultimate

rush to tile; knock back on collision deals stun damage

##### Skill 1

melee knock back; collision stuns and repositions

##### Skill 2

big hit damage reduction resets knock back skill

##### Legendary+

combat haste increase

##### Mythic+

low HP haste regeneration cleanse cooldown

##### Supreme+

extended knock back grants energy on collision

### Units Soren benefits from

Look for units providing: `Haste` `Max HP` `Healing` `Energy`  
Common buffers are **Rowan**, **Hugin**, or **Twins**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Velara**
  - Haste buff (single target, high) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
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
- Antandra (100% `Physical`)

**Crowd Control**

- Atalanta (100% `Knock back` `Stun`)
- Cassadee (100% `Knock back` `Stun`)
- Lenya (100% `Knock back` `Stun`)

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

- **Signature skill**: Grand Finale (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, debuffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `high`
- **True damage**: True damage `high`

##### Ultimate

accumulated rhythm charge activates area resonance buff

##### Skill 1

periodic strikes drain enemy energy

##### Skill 2

control then area knock down burst

##### Legendary+

haste grows with accumulated rhythm charge

##### Mythic+

active rhythm auto-plays cleanse and heal

##### Supreme+

enhanced attacks true damage life drain

### Units Sylphira benefits from

Look for units providing: `ATK` `Haste` `Healing`  
Common buffers are **Mikola**, **Twins**, or **Rowan**.

- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Velara**
  - Haste buff (single target, high) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)

### Units benefitting most from Sylphira

- Nerion
- Indris
- Bonnie

### Units that can act as a replacement for Sylphira

**Damage**

- Pippa (90% `True damage` `Magic` `Max HP-based damage`)
- Indris (83% `True damage` `Max HP-based damage`)
- Shadewing (81% `Magic` `Max HP-based damage` `True damage`)

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

- **Signature skill**: Divine Conflagration (ultimate)
- **Movement**: moving (avg attack range 3.0 tiles)
- **Ally composition**: frontmost ally carries Pyre of Renewal (AoE damage and healing)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `high`
- **True damage**: HP loss `medium`

##### Ultimate

fly to center spending HP and energy to fire sustained beam

##### Skill 1

HP-loss triggers ally heal; HP regeneration triggers enemy damage

##### Skill 2

transformation on defeat; regeneration to resurrect

##### Legendary+

ATK scales with cumulative HP consumed

##### Mythic+

apply sustained frontal burn-heal aura to front ally

##### Supreme+

regeneration rate increased when defeated for the first time

### Units Talene benefits from

Look for units providing: `ATK` `Max HP` `Healing` `Life Drain`  
Common buffers are **Mikola**, **Hepler**, or **Hewynn**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
  - Lifedrain buff (multiple targets, low)
- **Cecia**
  - Max HP buff (single target, high)
  - Lifedrain buff (area, high)
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)

### Units benefitting most from Talene

- Nerion
- Perseus
- Silven

### Units that can act as a replacement for Talene

**Buffs on allies**

- Gerda (100% `Healing`)
- Mikola (100% `Healing`)
- Solise (100% `Healing`)

**Damage**

- Athalia (100% `HP loss`)
- Dunlingr (100% `HP loss` `Magic`)
- Zorya (100% `HP loss` `Magic`)

**Crowd Control**

- Atalanta (100% `Knock back`)
- Cassadee (100% `Knock back`)
- Indris (100% `Knock back`)

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

- **Signature skill**: Eternal Dreamscape (ultimate)
- **Movement**: stationary (avg attack range 10.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

##### Ultimate

AoE sleep all enemies with sustained damage

##### Skill 1

HP sacrifice leaps to two enemies dealing area stun damage

##### Skill 2

transform to secondary form on low HP; invincible regeneration burst

##### Legendary+

ATK grows after sleep cast is active

##### Mythic+

post-sleep haste surge and free HP-free leaps

##### Supreme+

extra secondary form use gained per assist or kill

### Units Tasi benefits from

Look for units providing: `ATK` `Haste` `Max HP` `Healing`  
Common buffers are **Hugin**, **Twins**, or **Rowan**.

- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Velara**
  - Haste buff (single target, high) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Pandora**
  - Max HP buff (single target, medium)
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)

### Units benefitting most from Tasi

- Nerion
- Carolina

### Units that can act as a replacement for Tasi

**Similar Skills**

- Marilee (66% `mass-cc` `self-repositioner`)

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

- **Signature skill**: Knight's Heart (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, damage `low`
- **True damage**: True damage `low`

##### Ultimate

passive auto-charge farthest enemy; ATK speed boosts charge damage

##### Skill 1

kick interrupts and weakens when charge direction changes

##### Skill 2

sword attacks adjacent scaling on target ATK

##### Legendary+

battle ATK grows after first ultimate activation

##### Mythic+

permanent unaffected and true damage after repeated charges

##### Supreme+

charges stack target DEF reduction

### Units Temesia benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `Max HP` `Healing` `Energy`  
Common buffers are **Lyca**, **Rowan**, or **Hugin**.

- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Velara**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
  - Healing (area, medium)
- **Pandora**
  - Max HP buff (single target, medium)
  - Healing (single target, high)
  - Energy recovery (single target, low) `signature fuel`
  - Energy recovery (1000 at battle start, single target) `signature fuel`
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)

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

- **Signature skill**: Darkmoon Pact (Skill 1)
- **Movement**: moving (avg attack range 0.2 tiles)
- **Ally composition**: place lieutenant 1 tile behind at battle prep (Crit + shared shields)

#### Skill overview

- **Signature skill**: speed `slow`, buffs `medium`, damage `medium`
- **Ultimate**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

##### Ultimate

ground slam AoE then ritual zone for eruption and healing

##### Skill 1

Passive: designate rear ally bond granting crit; Active: shield both

##### Skill 2

frontal arc knock down

##### Legendary+

battle damage taken reduction

##### Mythic+

bonded ally ultimate triggers sustained DEF reduction and AoE burst

##### Supreme+

passive HP regeneration while bonded ally is alive

### Units Thador benefits from

Look for units providing: `Max HP` `CRIT` `Healing`  
Common buffers are **Hepler**, **Rowan**, or **Hugin**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Damian**
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Velara**
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`

### Units benefitting most from Thador

- Pandora

### Units that can act as a replacement for Thador

**Buffs on allies**

- Lyca (100% `Energy`)
- Pandora (100% `Energy`)
- Ravion (100% `Energy`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Eironn (100% `Magic DEF debuff`)
- Shadewing (100% `Magic DEF debuff`)
- Sinbad (100% `Magic DEF debuff`)

**Crowd Control**

- Antandra (100% `Knock down`)
- Athalia (100% `Knock down`)
- Baelran (100% `Knock down`)

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

- **Signature skill**: Resurrection (Skill 2)
- **Movement**: moving (avg attack range 1.0 tiles)
- **Ally composition**: place ally 1 tile behind at battle prep (Soul Pact damage share and revive)

#### Skill overview

- **Signature skill**: speed `fast`
- **Ultimate**: speed `slow`, buffs `medium`, damage `low`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`

##### Ultimate

charge-up slash that absorbs damage dealt during charge

##### Skill 1

drain target current HP, boosting own max HP and marking them

##### Skill 2

revive once at partial HP after defeat

##### Legendary+

energy recovery from attacks; higher before revive triggers

##### Mythic+

bonded ally absorbs tank damage; ally sacrifice revives tank

##### Supreme+

ultimate drains additional HP from all previously marked enemies

### Units Thoran benefits from

Look for units providing: `Max HP` `Healing` `Energy`  
Common buffers are **Rowan**, **Hepler**, or **Smokey & Meerky**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Antandra**
  - Healing (multiple targets, high)
- **Contess**
  - Healing (multiple targets, high)

### Units benefitting most from Thoran

- Himmel
- Perseus
- Silven

### Units that can act as a replacement for Thoran

**Buffs on allies**

- Brutus (100% `Life Drain`)
- Cecia (100% `Life Drain`)
- Daimon (100% `Life Drain`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Bryon (100% `Interrupt`)
- Gerda (100% `Interrupt`)
- Lily May (100% `Interrupt`)

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

- **Signature skill**: Wrath of the Wilds (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, buffs `medium`, damage `low`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

##### Ultimate

battle-start lose HP then gain auto-regeneration unaffected shield

##### Skill 1

strike deals damage and restores shield value proportionally

##### Skill 2

attacks gain extra damage proportional to current shield value

##### Legendary+

battle vitality increase

##### Mythic+

first shield break refills instantly; nature bond buffs nearby allies

##### Supreme+

shield regeneration per second while casting ultimate

### Units Tilaya benefits from

Look for units providing: `Max HP` `Healing`  
Common buffers are **Hepler**, **Hewynn**, or **Rowan**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Antandra**
  - Healing (multiple targets, high)
- **Contess**
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
- Granny Dahnie (60% `hp-scaling`)
- Pippa (60% `hp-scaling`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

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

- **Signature skill**: Way of the Forest (Skill 2)
- **Movement**: moving (stationary when rooted)
- **Ally composition**: when rooted, shields frontmost ally instead of self

#### Skill overview

- **Signature skill**: speed `fast`, heal `medium`
- **Ultimate**: speed `slow`, heal `medium`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

##### Ultimate

on low HP retreat to rooted backline; normal attacks become ranged AoE

##### Skill 1

HP-scaled personal shield; if rooted grant to frontmost ally

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
Common buffers are **Rowan**, **Hepler**, or **Smokey & Meerky**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Antandra**
  - Healing (multiple targets, high)
- **Contess**
  - Healing (multiple targets, high)

### Units benefitting most from Ulmus

- Nerion
- Carolina
- Himmel

### Units that can act as a replacement for Ulmus

**Buffs on allies**

- Lenya (60% `Max HP`)
- Pang (60% `Max HP`)
- Solise (60% `Healing`)

**Similar Skills**

- Pang (100% `ally-shielder` `transformation`)
- Hepler (66% `ally-shielder` `transformation`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Kordan (100% `Knock back` `Bind` `Knock down`)
- Indris (94% `Knock back` `Bind`)
- Atalanta (78% `Knock back` `Bind`)

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

- **Signature skill**: Swift Shift (ultimate)
- **Movement**: high movement (repositioning skills)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `low`
- **True damage**: HP loss `medium`, True damage `medium`

##### Ultimate

jump to empty tile switches ranged mode; rush enemy switches melee

##### Skill 1

mark farthest or nearest enemy; absorb energy per hit

##### Skill 2

ranged mode haste reduction shot; melee mode multi-hit stun

##### Legendary+

ATK grows with each non-summoned enemy defeated

##### Mythic+

mark defeat triggers stealth and haste surge

##### Supreme+

marked enemy deals reduced damage; mode-based bonus stacks

### Units Vala benefits from

Look for units providing: `ATK` `Haste` `Healing` `Energy`  
Common buffers are **Rowan**, **Mikola**, or **Twins**.

- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Velara**
  - Haste buff (single target, high) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Mehira**
  - Haste buff (single target, high) `signature fuel`
  - ATK SPD via Haste buff (single target, high) `signature fuel`
  - Enables Enemy defeat via HP threshold strike
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)

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

- Kafra (100% `Marked target (focus fire)` `Haste debuff`)
- Aliceth (66% `Marked target (focus fire)`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Arden (100% `Stun`)

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

- **Signature skill**: Thunder Swordwork (ultimate)
- **Movement**: moving (avg attack range 1.4 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`, damage `low`
- **Non-ultimate**: speed `fast`, damage `medium`

##### Ultimate

AoE multi-strike area then enter sustained ATK buff state

##### Skill 1

three-hit consecutive strikes; chain lightning to nearby during buff

##### Skill 2

AoE lightning burst available only while buffed

##### Legendary+

battle ATK increase

##### Mythic+

permanent buff state; buff activations stack ATK bonus

##### Supreme+

lightning AoE stuns; hit enemies lose haste and movement

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

- **Signature skill**: Blooming Terror (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `fast`, heal `medium`, damage `high`
- **Non-ultimate**: speed `fast`, buffs `medium`, damage `high`
- **True damage**: Max HP-based damage `medium`

##### Ultimate

full stacks trigger stun slash at energy cost

##### Skill 1

multiple sword techniques at appropriate range cost energy

##### Skill 2

battle-start shield from nearby allies; ATK speed buff to all

##### Legendary+

battle ATK speed increase

##### Mythic+

counter incoming ultimate damage with free parry counter

##### Supreme+

while shielded gain bonus energy from normal attacks

### Units Valka benefits from

Look for units providing: `ATK SPD / Haste` `Max HP` `Healing` `Energy`  
Common buffers are **Rowan**, **Hugin**, or **Hepler**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
- **Velara**
  - ATK SPD via Haste buff (single target, high) `signature fuel`
  - Healing (area, medium)

### Units benefitting most from Valka

**12** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Cecia
- Fay
- Gwyneth
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
- Lyca (60% `ATK SPD`)

**Damage**

- Brutus (100% `Max HP-based damage` `Physical`)
- Daimon (100% `Max HP-based damage`)
- Gunnar (100% `Max HP-based damage` `Physical`)

**Crowd Control**

- Antandra (100% `Stun` `Knock down`)
- Lucca (100% `Stun` `Knock down`)
- Zorya (100% `Stun` `Knock down`)

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

- **Signature skill**: Ruthless Rite (ultimate)
- **Movement**: stationary (no finite attack range)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, debuffs `medium`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

##### Ultimate

dormant circles accumulate energy; awaken for area heal and haste drain

##### Skill 1

immobilize top attacker, reducing haste and DEF

##### Skill 2

instant-awaken one circular zone; ally debuffs charge circle energy

##### Legendary+

battle haste grows with awakened circle count

##### Mythic+

awakened circles fire bolts shielding weakest ally or damaging foe

##### Supreme+

all circles awakened expands burst range; allies gain unaffected

### Units Velara benefits from

Look for units providing: `Haste` `Max HP` `Energy`  
Common buffers are **Hugin**, **Twins**, or **Rowan**.

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
- **Daimon**
  - Max HP via Shield (multiple targets, medium)

### Units benefitting most from Velara

- Viperian

### Units that can act as a replacement for Velara

**Buffs on allies**

- Damian (100% `Healing` `Haste`)
- Hewynn (76% `Healing`)
- Lorsan (76% `Healing`)

**Similar Skills**

- Solise (90% `ally-healer` `ally-shielder` `aoe-healing`)
- Hewynn (60% `ally-healer` `aoe-healing`)

**Damage**

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Cassadee (100% `Magic`)

**Debuffs on enemies**

- Alna (100% `Haste debuff`)
- Aurora (100% `Haste debuff`)
- Bonnie (100% `Haste debuff`)

**Crowd Control**

- Alna (100% `Bind`)
- Arden (100% `Bind`)
- Carolina (100% `Bind`)

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

- **Signature skill**: Crimson Waltz (Mythic+)
- **Movement**: mostly stationary (avg attack range 5.0 tiles)

#### Skill overview

- **Signature skill**: speed `slow`, damage `low`
- **Ultimate**: speed `normal`, heal `medium`, damage `high`
- **Non-ultimate**: speed `slow`, heal `medium`, debuffs `medium`, damage `medium`

##### Ultimate

spend HP to send possessing summons onto all enemies

##### Skill 1

drain HP from healthiest enemy recovering same amount

##### Skill 2

Passive: possessed enemies take periodic drain; Active: enhances it

##### Legendary+

battle haste increase

##### Mythic+

high HP threshold triggers large AoE damage burst

##### Supreme+

summons return on possessed enemy defeat restoring HP and energy

### Units Viperian benefits from

Look for units providing: `Haste` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Velara**
  - Haste buff (single target, high) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
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

- **Signature skill**: Six-Shot (ultimate)
- **Movement**: moving (avg attack range 2.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, damage `low`
- **Non-ultimate**: speed `fast`, buffs `medium`, debuffs `medium`, damage `low`
- **True damage**: HP loss `medium`, Max HP-based damage `low`

##### Ultimate

fire multiple revolving shots at random enemies, stunning per hit

##### Skill 1

triple penetrating bullets per normal attack

##### Skill 2

mark top attacker for damage boost and damage reduction

##### Legendary+

battle crit damage boost

##### Mythic+

battle-start grenades stun and reduce target DEF

##### Supreme+

shield on first hit of marked target; crit bonus against marked target

### Units Walker benefits from

Look for units providing: `Max HP` `CRIT` `CRIT DMG Boost` `Life Drain`  
Common buffers are **Lyca**, **Rowan**, or **Hugin**.

- **Cecia**
  - Max HP buff (single target, high)
  - Lifedrain buff (area, high)
  - ATK SPD buff (single target, low) `signature fuel`
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
- Korin (68% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Nazrik (100% `Crit Resist debuff`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Arden (100% `Stun`)

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

- **Signature skill**: Rallying Roar (Skill 1)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill**: speed `fast`, buffs `medium`
- **Ultimate**: speed `slow`
- **Non-ultimate**: speed `fast`, buffs `medium`

##### Ultimate

slam destroys obstacles and knock up area enemies

##### Skill 1

charge formation inspires all allies with max HP and stats

##### Skill 2

HP-scaled stomp stuns adjacent enemies

##### Legendary+

battle max HP increase

##### Mythic+

high HP threshold enables HP-scaling normal attack bonus

##### Supreme+

excess healing converts to permanent max HP gain

### Units Zandrok benefits from

Look for units providing: `Haste` `Max HP` `Healing` `Life Drain`  
Common buffers are **Hepler**, **Hugin**, or **Twins**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)
  - Lifedrain buff (multiple targets, low)
- **Cecia**
  - Max HP buff (single target, high)
  - Lifedrain buff (area, high)
- **Lorsan**
  - Healing (all units, high)
- **Solise**
  - Healing (all units, high)
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)

### Units benefitting most from Zandrok

- Perseus
- Nerion
- Silven

### Units that can act as a replacement for Zandrok

**Buffs on allies**

- Shakir (76% `Haste` `Life Drain`)
- Cecia (63% `Life Drain` `Max HP`)
- Twins (63% `Haste` `Max HP`)

**Similar Skills**

- Atalanta (66% `aoe-damage` `battle-start-burst`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Cassadee (100% `Knock up` `Stun`)
- Lucca (100% `Knock up` `Stun`)
- Lucy (100% `Knock up` `Stun`)

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

- **Signature skill**: Vein Pulse (ultimate)
- **Movement**: moving (avg attack range 1.0 tiles)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, buffs `medium`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

##### Ultimate

deploy linked turrets that fire or combine beams

##### Skill 1

build turret; after normal attacks triggers heavy multi-hit attack

##### Skill 2

repair turrets restoring HP and granting shields

##### Legendary+

battle penetration increase

##### Mythic+

periodic turret upgrades boost max HP, ATK, and range

##### Supreme+

turret hits burn enemy ATK and DEF

### Units Zanie benefits from

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Lyca**, **Twins**, or **Hugin**.

- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, medium)
- **Valka**
  - ATK SPD buff (multiple targets, high) `signature fuel`
- **Damian**
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`

### Units benefitting most from Zanie

- Perseus
- Silven
- Nerion

### Units that can act as a replacement for Zanie

**Buffs on allies**

- Hepler (66% `Healing` `Max HP`)
- Koko (66% `Healing` `Max HP`)

**Similar Skills**

- Chippy (100% `summoner`)
- Florabelle (100% `summoner`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Sinbad (90% `Phys DEF debuff` `ATK debuff`)
- Brutus (75% `Phys DEF debuff` `DoT`)
- Kafra (75% `Phys DEF debuff` `ATK debuff`)

**Crowd Control**

- Atalanta (100% `Knock back` `Stun`)
- Cassadee (100% `Knock back` `Stun`)
- Lenya (100% `Knock back` `Stun`)

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

- **Signature skill**: Circle of Vigil (ultimate)
- **Movement**: moving (inactive while dormant)

#### Skill overview

- **Signature skill (ultimate)**: speed `slow`, heal `medium`, buffs `medium`, damage `high`
- **Non-ultimate**: speed `fast`, heal `medium`, buffs `medium`, damage `high`
- **True damage**: HP loss `high`

##### Ultimate

dormant phase recovers HP and energy; awaken with AoE stun

##### Skill 1

Passive: awaken hardens skin reducing damage taken; Active: arc knock down

##### Skill 2

Passive: awaken life drain; nearby defeat heals; Active: burst on lost HP

##### Legendary+

battle damage dealt grows with surrounding enemy count

##### Mythic+

awaken creates aura slowing enemy haste and movement

##### Supreme+

fatal blow triggers dormancy once per battle

### Units Zorya benefits from

Look for units providing: `Haste` `Max HP` `Healing` `Energy`  
Common buffers are **Rowan**, **Hugin**, or **Smokey & Meerky**.

- **Velara**
  - Haste buff (single target, high) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) `signature fuel`
  - Enables Ally Ultimate casts via Start-of-battle Ultimate
- **Shakir**
  - Haste buff (multiple targets, high) `signature fuel`
  - ATK SPD via Haste buff (multiple targets, high) `signature fuel`
- **Damian**
  - Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
  - Healing (area, medium)
  - ATK SPD via Haste buff (multiple targets, medium, conditional (frequent)) `signature fuel`
- **Contess**
  - Healing (multiple targets, high)
  - Enables Ally Ultimate casts via Start-of-battle Ultimate
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (all units, medium)

### Units benefitting most from Zorya

- Nerion
- Carolina
- Bonnie

### Units that can act as a replacement for Zorya

**Similar Skills**

- Salazer (80% `hp-scaling` `life-drain`)
- Brutus (66% `hp-scaling` `life-drain`)
- Daimon (60% `hp-scaling` `life-drain`)

**Damage**

- Talene (95% `HP loss` `Magic`)
- Niru (94% `Magic` `HP loss`)
- Shadewing (94% `Magic` `HP loss`)

**Crowd Control**

- Antandra (100% `Stun` `Knock down`)
- Lucca (100% `Stun` `Knock down`)
- Lumont (66% `Stun`)

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

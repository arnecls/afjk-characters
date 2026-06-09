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

- Signature skill: Radiant Rain (ultimate) — aerial area arrow rain
- Movement: stationary (avg attack range 8.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, buffs `medium`, damage `high`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `high`
- True damage: HP loss `high`

### Units Aliceth benefits from

Look for units providing: `ATK`  
Common buffers are **Lyca**, **Rowan**, or **Hugin**.

- **Kulu**
  - Enables Ranged damage from allies via ranged attacks
  - Enables Debuff on target via Damage taken debuff (all units)
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
  - Enables Debuff on target via ATK debuff (multiple targets)
- **Evie**
  - ATK buff (multiple targets, high)
  - Enables Debuff on target via DoT (all units)
- **Lily May**
  - Enables Debuff on target via Energy drain (all units)
- **Alna**
  - ATK buff (single target, medium)
  - Enables Debuff on target via Haste debuff (area)

### Units benefitting from Aliceth

- Kulu

### Units that can act as a replacement for Aliceth

**Damage**

- Faramor (100% `Physical` `HP loss`)
- Dunlingr (97% `HP loss`)
- Talene (97% `HP loss`)

**Crowd Control**

- Hepler (86% `Blind` `Stun`)
- Twins (60% `Blind` `Knock back`)

### Summary for Aliceth

#### Aliceth Provides

- Ally grant (Brightfeather) — Single target
- Invincibility — Single target
- Marked target (focus fire) — Single target
- Reposition enemies — Single target
- Fatal blow save (Mythic+) — Area

#### Aliceth Requires

- Passive with internal cooldown — Allies
- Ranged damage from allies — Allies
- Debuff on target (Legendary+) — Enemies

#### Damage types dealt by Aliceth

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- HP loss — Single target — `high`

#### Buffs provided by Aliceth

- Ally empower buff — Single target — `low`
- Attack range buff — Single target — `low`
- DEF Penetration buff — Single target — `high`
- ATK buff (Legendary+) — Multiple targets — `medium`
- Fatal blow immunity (Mythic+) — Single target — `high` — conditional (rare)
- Healing (Mythic+) — Single target — `low`

#### Debuffs provided by Aliceth

- Marked target (focus fire) (Legendary+) — Multiple targets — `medium`
- Blind HP loss debuff (EX+15) — Area — `low`

#### Crowd Control provided by Aliceth

- Knock back — Single target — `low`
- Stun — Single target — `low`
- Blind (EX+15) — Area — `medium`

## Alna

### Alna's behavior

- Signature skill: Winter Anthem (ultimate) — battle-start area blizzard
- Movement: moving (avg attack range 1.0 tiles)
- Ally composition: place ally in same row at battle prep (Winter Warrior buffs)

#### Skill overview

- Signature skill (ultimate): speed `slow`, heal `medium`, debuffs `medium`, damage `high`
- Non-ultimate: speed `slow`, heal `medium`, buffs `medium`, debuffs `medium`, damage `high`

### Units Alna benefits from

Look for units providing: `Max HP` `Healing`  
Common buffers are **Koko**, **Lorsan**, or **Hugin**.

- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Evie**
  - Healing (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)

### Units benefitting from Alna

- Shadewing

### Units that can act as a replacement for Alna

**Similar Skills**

- Cryonaia (75% `battlefield-modification` `cc-immunity` `invincibility`)

**Damage**

- Gunnar (90% `Physical` `DoT`)
- Brutus (80% `DoT` `Physical`)
- Cecia (70% `Physical` `DoT`)

**Debuffs on enemies**

- Natsu (75% `Haste debuff`)

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
- Physical — All units, Arc, Self, Single target
- DoT — All units

#### Buffs provided by Alna

- Ally empower buff — Single target — `low`
- Max HP buff — Single target — `low`
- Damage and control immunity (EX+15) — Single target — `high`
- ATK buff (Supreme+) — Single target — `medium`

#### Debuffs provided by Alna

- Haste debuff — Arc — `high`
- Vitality debuff (Supreme+) — Area — `low`

#### Crowd Control provided by Alna

- Immune (Mythic+) — Self — Start of Battle
- Bind (Supreme+) — Area — `medium`

## Alsa

### Alsa's behavior

- Signature skill: Twirling Rocks (ultimate) — area physical rock damage
- Movement: mostly stationary (avg attack range 6.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, buffs `medium`, debuffs `medium`, damage `high`
- Non-ultimate: speed `fast`, debuffs `medium`, damage `high`

### Units Alsa benefits from

Look for units providing: `Haste` `Max HP`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Lucius**
  - Max HP via Shield (area, high)
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Alsa

**Damage**

- Callan (100% `Magic`)
- Cassadee (100% `Magic`)
- Contess (100% `Magic`)

**Debuffs on enemies**

- Kulu (100% `Movement speed debuff`)

**Crowd Control**

- Perseus (100% `Stun` `Knock back`)
- Antandra (98% `Stun`)
- Koko (98% `Stun`)

### Summary for Alsa

#### Alsa Provides

- Enhanced form — Area

#### Alsa Requires

- Form or stance active — Enemies
- Passive with internal cooldown — Enemies

#### Damage types dealt by Alsa

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target

#### Debuffs provided by Alsa

- Movement speed debuff — Area — `medium`

#### Crowd Control provided by Alsa

- Immune — Area — Once
- Knock back — Single target — `low`
- Stun — Single target — `high`

## Antandra

### Antandra's behavior

- Signature skill: Shield Assault (ultimate) — charge + area knockback
- Movement: high movement (repositioning skills)
- Ally composition: frontmost ally becomes guarded ally (shared shields)

#### Skill overview

- Signature skill (ultimate): speed `slow`, heal `medium`, buffs `medium`, damage `high`
- Non-ultimate: speed `fast`, buffs `medium`, damage `low`

### Units Antandra benefits from

Look for units providing: `Max HP` `Healing` `Energy`  
Common buffers are **Rowan**, **Twins**, or **Lyca**.

- **Pandora**
  - Max HP buff (single target, low)
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Velara**
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)

### Units benefitting from Antandra

- Alna
- Callan
- Contess
- Evie
- Gerda
- Igor
- Reinier
- Saida
- Tilaya

### Units that can act as a replacement for Antandra

**Buffs on allies**

- Evie (100% `Healing`)
- Fay (100% `Healing`)
- Hewynn (100% `Healing`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Atalanta (100% `Physical`)

**Crowd Control**

- Hepler (62% `Taunt` `Stun`)

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

- Unaffected — Area — On Skill
- Knock down — Area — `medium`
- Stun — Area — `medium`
- Taunt — Area — `high`

## Arden

### Arden's behavior

- Signature skill: Force of Nature (ultimate) — area nature damage burst
- Movement: stationary (no finite attack range)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `high`
- Non-ultimate: speed `fast`, damage `high`

### Units Arden benefits from

Look for units providing: `ATK` `Energy`  
Common buffers are **Rowan**, **Lyca**, or **Hugin**.

- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Smokey & Meerky**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, low) [signature fuel]

### Units that can act as a replacement for Arden

**Similar Skills**

- Lorsan (100% `aoe-damage` `dot-specialist`)
- Faramor (80% `aoe-damage` `dot-specialist`)
- Viperian (66% `aoe-damage` `dot-specialist`)

**Damage**

- Berial (100% `Magic` `DoT`)
- Bryon (100% `Magic` `DoT`)
- Cryonaia (100% `Magic` `DoT`)

**Crowd Control**

- Gwyneth (72% `Bind` `Stun`)
- Indris (60% `Bind`)
- Lorsan (60% `Stun`)

### Summary for Arden

#### Damage types dealt by Arden

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target
- DoT — Multiple targets

#### Crowd Control provided by Arden

- Bind — Single target — `high`
- Stun — Multiple targets — `high`

## Atalanta

### Atalanta's behavior

- Signature skill: Wild Sniper (ultimate) — dash + line stun shot
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `medium`
- Non-ultimate: speed `fast`, damage `medium`

### Units Atalanta benefits from

Look for units providing: `Haste` `Healing` `Physical DEF`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Velara**
  - Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Fay**
  - Healing (arc, high, conditional (frequent))
  - DEF buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]

### Units that can act as a replacement for Atalanta

**Similar Skills**

- Zandrok (66% `aoe-damage` `battle-start-burst`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Brutus (100% `Phys DEF debuff`)
- Lyca (100% `Phys DEF debuff`)
- Ravion (100% `Phys DEF debuff`)

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

- Signature skill: Unbroken Retribution (ultimate) — post-death attacking lance
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill (ultimate): speed `normal`, buffs `medium`, debuffs `medium`, damage `high`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `high`
- True damage: True damage `high`

### Units Athalia benefits from

Look for units providing: `Max HP` `CRIT` `Execution` `Healing`  
Common buffers are **Koko**, **Twins**, or **Hugin**.

- **Lucius**
  - Max HP via Shield (area, high)
- **Velara**
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Hewynn**
  - Healing (all units, medium)
- **Fay**
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Antandra**
  - Healing (multiple targets, high)

### Units that can act as a replacement for Athalia

**Similar Skills**

- Baelran (80% `hp-scaling` `transformation`)
- Kordan (66% `hp-scaling` `self-repositioner`)
- Pippa (66% `hp-scaling` `self-repositioner`)

**Damage**

- Baelran (100% `True damage` `Physical`)
- Dionel (100% `True damage` `Physical`)
- Scarlita (100% `Physical` `True damage`)

**Debuffs on enemies**

- Lucius (100% `ATK debuff`)
- Lyca (100% `ATK debuff`)
- Sinbad (90% `ATK debuff`)

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
- True damage — All units, Single target — `high`

#### Debuffs provided by Athalia

- ATK debuff — All units — `medium`

#### Crowd Control provided by Athalia

- Unaffected — Area — On Skill
- Knock down — All units — `low`

## Aurora

### Aurora's behavior

- Signature skill: Starlit Slumber (ultimate) — sleep all enemies
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill (ultimate): speed `slow`, buffs `medium`, debuffs `medium`, damage `medium`
- Non-ultimate: speed `fast`, buffs `medium`, damage `high`

### Units Aurora benefits from

Look for units providing: `ATK` `Haste`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units benefitting from Aurora

- Bryon
- Florabelle
- Gala
- Phraesto
- Zanie

### Units that can act as a replacement for Aurora

**Buffs on allies**

- Pandora (100% `Invincible`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Berial (100% `Magic`)

**Debuffs on enemies**

- Alna (100% `Haste debuff`)
- Bryon (100% `Haste debuff`)
- Carolina (100% `Haste debuff`)

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

- Haste buff — Summons only — `high`
- Invincible — Single target — `high`
- Summon damage buff (Mythic+) — Summons only — `low`

#### Debuffs provided by Aurora

- Haste debuff — Multiple targets — `low`

#### Crowd Control provided by Aurora

- Unaffected — Self — Conditional
- Sleep — Single target — `high`

## Baelran

### Baelran's behavior

- Signature skill: Celestial Rise (ultimate) — HP-based shield + transform
- Movement: moving (avg attack range 1.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, heal `medium`, buffs `medium`, damage `high`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `high`
- True damage: True damage `high`

### Units Baelran benefits from

Look for units providing: `ATK` `Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Koko**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Velara**
  - Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))

### Units that can act as a replacement for Baelran

**Similar Skills**

- Athalia (80% `hp-scaling` `transformation`)

**Damage**

- Athalia (100% `True damage` `Physical`)
- Dionel (100% `True damage` `Physical`)
- Indris (100% `True damage` `Physical`)

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

- Form or stance active — Enemies
- Boss encounter (Supreme+) — Enemies

#### Damage types dealt by Baelran

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- True damage — Arc, Area, Single target — `medium`

#### Debuffs provided by Baelran

- Max HP debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Baelran

- Unaffected — Self — Start of Battle
- Knock down — Area — `medium`
- Knock up — Area — `high`

## Berial

### Berial's behavior

- Signature skill: Scared Swamp (ultimate) — shadow dive + area frighten
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill (ultimate): speed `slow`, buffs `medium`, damage `high`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `medium`

### Units Berial benefits from

Look for units providing: `Healing`  
Common buffers are **Lyca**, **Mikola**, or **Rowan**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Velara**
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Hewynn**
  - Healing (all units, medium)

### Units that can act as a replacement for Berial

**Damage**

- Bryon (100% `DoT` `Magic`)
- Cryonaia (100% `DoT` `Magic`)
- Daimon (100% `DoT` `Magic`)

**Debuffs on enemies**

- Sinbad (100% `Energy drain` `Damage taken debuff`)
- Saida (80% `Energy drain`)
- Dunlingr (66% `Energy drain`)

**Crowd Control**

- Silvina (66% `Frighten`)

### Summary for Berial

#### Berial Provides

- Invincibility — Self
- Revive ally — Single target
- Summoning (Mythic+) — Single target

#### Damage types dealt by Berial

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target
- DoT — Area

#### Debuffs provided by Berial

- Damage taken debuff (Legendary+) — Single target — `low`
- Energy drain (Mythic+) — Single target — `low`

#### Crowd Control provided by Berial

- Frighten — Area — `medium`

## Bonnie

### Bonnie's behavior

- Signature skill: Decay's Reach — battle-start aging debuff
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill: speed `fast`, debuffs `medium`, damage `high`
- Ultimate: speed `slow`, damage `low`
- Non-ultimate: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

### Units Bonnie benefits from

Look for units providing: `ATK`  
Common buffers are **Lyca**, **Rowan**, or **Koko**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Enables Debuff on target via DoT (all units)
  - Enables Magic damage from allies via Magic damage + early battle + all enemies (all units)
- **Lily May**
  - Enables Debuff on target via Energy drain (all units)
  - Enables Magic damage from allies via Magic damage + all enemies (all units)
- **Natsu**
  - Enables Debuff on target via Haste debuff (area)
  - Enables Magic damage from allies via Magic damage + wide area (area)
- **Frieren**
  - Enables Debuff on target via DoT (area)
  - Enables Magic damage from allies via Magic damage + all enemies (all units)
- **Kulu**
  - Enables Debuff on target via Damage taken debuff (all units)

### Units that can act as a replacement for Bonnie

**Damage**

- Arden (100% `Magic` `DoT`)
- Berial (100% `Magic` `DoT`)
- Bryon (100% `Magic` `DoT`)

**Debuffs on enemies**

- Pandora (100% `ATK debuff` `Damage taken debuff` `Haste debuff`)
- Granny Dahnie (75% `ATK debuff` `Haste debuff`)
- Kafra (75% `ATK debuff` `Haste debuff`)

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
- Form or stance active — Enemies
- Magic damage from allies — Allies

#### Damage types dealt by Bonnie

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Single target

#### Debuffs provided by Bonnie

- ATK debuff — Single target — `medium`
- Haste debuff — Single target — `low`
- Damage taken debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Bonnie

- Stun — Single target — `low`

## Brutus

### Brutus's behavior

- Signature skill: Whirlwind Wrath (ultimate) — area spin damage
- Movement: moving (avg attack range 1.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, debuffs `medium`, damage `medium`
- Non-ultimate: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`
- True damage: Max HP-based damage `medium`

### Units Brutus benefits from

Look for units providing: `Life Drain`  
Common buffers are **Lyca**, **Rowan**, or **Twins**.

- **Cecia**
  - Lifedrain buff (area, high)
  - ATK SPD buff (single target, low) [signature fuel]
- **Valka**
  - Lifedrain buff (single target, high)
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Dunlingr**
  - Lifedrain buff (all units, low)
  - ATK SPD buff (all units, low) [signature fuel]
- **Shakir**
  - Lifedrain buff (single target, medium)
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]

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
- Satrana (100% `Max HP-based damage` `DoT`)
- Daimon (90% `Max HP-based damage` `DoT`)

**Crowd Control**

- Antandra (100% `Taunt`)
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

- DoT — Area — `medium`
- Phys DEF debuff — Area — `medium`

#### Crowd Control provided by Brutus

- Immune — Self — On Skill
- Unaffected — Self — On Skill
- Taunt — Area — `high`

## Bryon

### Bryon's behavior

- Signature skill: Falcon Raid (ultimate) — falcon area dive damage
- Movement: stationary (summon moves)

#### Skill overview

- Signature skill (ultimate): speed `fast`, debuffs `medium`, damage `high`
- Non-ultimate: speed `fast`, heal `medium`, damage `medium`

### Units Bryon benefits from

Look for units providing: `Haste` `Healing`  
Common buffers are **Mikola**, **Twins**, or **Koko**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Velara**
  - Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)

### Units that can act as a replacement for Bryon

**Damage**

- Arden (100% `Magic` `DoT`)
- Berial (100% `DoT` `Magic`)
- Cryonaia (100% `DoT` `Magic`)

**Debuffs on enemies**

- Alna (100% `Haste debuff`)
- Carolina (100% `Haste debuff`)
- Eironn (100% `Haste debuff`)

**Crowd Control**

- Gerda (100% `Stun` `Interrupt`)
- Lucca (100% `Stun` `Interrupt`)
- Arden (80% `Stun`)

### Summary for Bryon

#### Bryon Provides

- Energy steal — Single target
- Stacking buff — Single target
- Start-of-battle cast — Area
- Summoning — Self
- Counterattack (EX+10) — Single target

#### Damage types dealt by Bryon

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Area

#### Debuffs provided by Bryon

- Haste debuff — Area — `low`

#### Crowd Control provided by Bryon

- Untargetable (Mythic+) — Single target — Conditional
- Interrupt — Single target — `low`
- Stun (Mythic+) — Single target — `medium`

## Callan

### Callan's behavior

- Signature skill: Restless Guardian (ultimate) — absorb ally damage shield
- Movement: moving (avg attack range 1.7 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, buffs `medium`
- Non-ultimate: speed `fast`, damage `medium`

### Units Callan benefits from

Look for units providing: `Healing`  
Common buffers are **Koko**, **Lorsan**, or **Mikola**.

- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Evie**
  - Healing (multiple targets, high)
- **Ludovic**
  - Healing (area, medium)
- **Velara**
  - Healing (area, medium)

### Units benefitting from Callan

- Daimon
- Eironn
- Thoran

### Units that can act as a replacement for Callan

**Buffs on allies**

- Hepler (100% `Max HP`)
- Hugin (100% `Max HP`)
- Lucius (100% `Max HP`)

**Damage**

- Alsa (100% `Magic`)
- Cassadee (100% `Magic`)
- Contess (100% `Magic`)

**Crowd Control**

- Antandra (100% `Knock down` `Stun`)
- Lucca (100% `Knock down` `Stun`)
- Zorya (100% `Knock down` `Stun`)

### Summary for Callan

#### Callan Provides

- Damage absorption (allies) — Multiple targets
- Stored damage release — Self

#### Callan Requires

- Stored resource threshold — Enemies

#### Damage types dealt by Callan

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Multiple targets, Self, Single target

#### Buffs provided by Callan

- Shield — Multiple targets — `medium`

#### Crowd Control provided by Callan

- Unaffected — Self — Once
- Knock down — All units — `low`
- Stun (Mythic+) — Single target — `medium`

## Carolina

### Carolina's behavior

- Signature skill: Frozen Grave (ultimate) — freeze + bury area
- Movement: mostly stationary (avg attack range 4.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, debuffs `medium`, damage `high`
- Non-ultimate: speed `fast`, debuffs `medium`, damage `medium`

### Units Carolina benefits from

Look for units providing: `CRIT`  
Common buffers are **Lorsan**, **Lyca**, or **Twins**.

- **Tasi**
  - Enables CC on enemies via Sleep (all units, high)
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
  - Enables CC on enemies via Knock down (multiple targets, high)
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) [signature fuel]
  - Enables CC on enemies via Stun (area, high)
- **Hepler**
  - ATK SPD via Haste buff (single target, low) [signature fuel]
  - Enables CC on enemies via Blind (area, high)
- **Baelran**
  - Enables CC on enemies via Knock up (area, high)

### Units that can act as a replacement for Carolina

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Debuffs on enemies**

- Eironn (100% `Haste debuff` `Magic DEF debuff`)
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
- DoT — Self

#### Debuffs provided by Carolina

- Haste debuff — Area — `low`
- Magic DEF debuff (Mythic+) — Area — `low`

#### Crowd Control provided by Carolina

- Bind — Area — `high`

## Cassadee

### Cassadee's behavior

- Signature skill: Running Tide (ultimate) — tidal wave knockback
- Movement: stationary (avg attack range 10.0 tiles)
- Ally composition: nearest ally blessed at battle start; prioritizes ally behind

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `high`
- Non-ultimate: speed `fast`, damage `low`

### Units Cassadee benefits from

Look for units providing: `Haste`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

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

**Crowd Control**

- Perseus (76% `Knock back` `Stun`)
- Scarlita (75% `Knock back` `Knock up` `Stun`)
- Atalanta (65% `Knock back` `Stun`)

### Summary for Cassadee

#### Cassadee Provides

- Ally blessing — Single target

#### Cassadee Requires

- Ally blessing active (Supreme+) — Allies

#### Damage types dealt by Cassadee

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Debuffs provided by Cassadee

- Magic DEF debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Cassadee

- Knock back — All units — `low`
- Knock up — Single target — `high`
- Stun — Single target — `high`

## Cecia

### Cecia's behavior

- Signature skill: Queen's Summons (ultimate) — summon AoE damage unit
- Movement: mostly stationary (avg attack range 5.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, buffs `medium`, damage `high`
- Non-ultimate: speed `fast`, buffs `medium`, debuffs `medium`, damage `low`

### Units Cecia benefits from

Look for units providing: `ATK SPD / Haste` `DEF Penetration` `Physical DEF` `Magic DEF`  
Common buffers are **Lyca**, **Twins**, or **Rowan**.

- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]

### Units benefitting from Cecia

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

- Alna (100% `Physical` `DoT`)
- Brutus (100% `Physical` `DoT`)
- Gunnar (100% `Physical` `DoT`)

**Debuffs on enemies**

- Berial (100% `Damage taken debuff`)
- Bonnie (100% `Damage taken debuff`)
- Cryonaia (100% `Damage taken debuff`)

**Crowd Control**

- Alna (100% `Bind`)
- Arden (100% `Bind`)
- Atalanta (100% `Bind`)

### Summary for Cecia

#### Cecia Provides

- Summoning — Self
- Stat absorb (Mythic+) — Single target

#### Cecia Requires

- Enemy not CC-immune (Mythic+) — Enemies

#### Damage types dealt by Cecia

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- DoT — Arc, Single target

#### Buffs provided by Cecia

- ATK SPD buff — Single target — `high`
- DEF Penetration buff — Single target — `medium`
- Lifedrain buff — Area — `high`
- Max HP buff — Single target — `high`

#### Debuffs provided by Cecia

- Damage taken debuff (Mythic+) — Single target — `low`

#### Crowd Control provided by Cecia

- Bind — Single target — `medium`

## Chippy

### Chippy's behavior

- Signature skill: Brothers-in-arms (ultimate) — summon support ally
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `medium`
- Non-ultimate: speed `normal`, damage `high`

### Units Chippy benefits from

- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]

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

- Signature skill: Detention Pass (ultimate) — stealth start + punish
- Movement: stationary (no finite attack range)

#### Skill overview

- Signature skill (ultimate): speed `normal`, heal `medium`, buffs `medium`, damage `high`
- Non-ultimate: speed `fast`, heal `medium`, debuffs `medium`, damage `medium`

### Units Contess benefits from

Look for units providing: `Healing` `Energy`  
Common buffers are **Koko**, **Lorsan**, or **Mikola**.

- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Evie**
  - Healing (multiple targets, high)
- **Smokey & Meerky**
  - Healing (multiple targets, medium)
  - Energy recovery (multiple targets, low) [signature fuel]
- **Ludovic**
  - Healing (area, medium)

### Units that can act as a replacement for Contess

**Buffs on allies**

- Hugin (100% `ATK` `Max HP`)
- Aliceth (60% `ATK`)
- Evie (60% `ATK`)

**Damage**

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Cassadee (100% `Magic`)

**Debuffs on enemies**

- Sylphira (75% `Max HP debuff` `Energy drain`)

**Crowd Control**

- Gwyneth (100% `Silence` `Stun`)
- Gunnar (60% `Stun`)

### Summary for Contess

#### Contess Provides

- Start-of-battle cast — All units

#### Damage types dealt by Contess

- Primary damage type (unit): **Magic**
- Magic — All units, Multiple targets

#### Buffs provided by Contess

- ATK buff — Single target — `high`
- Shield — Single target — `medium`

#### Debuffs provided by Contess

- Energy drain — Single target — `low`
- Max HP debuff — Multiple targets — `low`
- ATK debuff (Legendary+) — Single target — `low`

#### Crowd Control provided by Contess

- Untargetable — Multiple targets — Start of Battle
- Silence (Mythic+) — Single target — `medium`
- Stun (Supreme+) — Single target — `medium`

## Cryonaia

### Cryonaia's behavior

- Signature skill: Frostveil Domain (ultimate) — area frost slow field
- Movement: mostly stationary (avg attack range 5.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, buffs `medium`, damage `high`
- Non-ultimate: speed `fast`, debuffs `medium`, damage `high`

### Units Cryonaia benefits from

Look for units providing: `ATK` `Max HP`  
Common buffers are **Hugin**, **Twins**, or **Lyca**.

- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Pandora**
  - Max HP buff (single target, low)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Saida**
  - Max HP via Shield (multiple targets, high)

### Units that can act as a replacement for Cryonaia

**Similar Skills**

- Alna (75% `battlefield-modification` `cc-immunity` `invincibility`)

**Damage**

- Frieren (100% `DoT` `Magic`)
- Tasi (100% `DoT` `Magic`)
- Berial (96% `DoT` `Magic`)

**Debuffs on enemies**

- Berial (100% `Damage taken debuff`)
- Bonnie (100% `Damage taken debuff`)
- Cecia (100% `Damage taken debuff`)

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
- DoT — All units

#### Debuffs provided by Cryonaia

- Damage taken debuff (Mythic+) — Single target — `low`

#### Crowd Control provided by Cryonaia

- Immune — Self — Conditional

## Cyran

### Cyran's behavior

- Signature skill: Gravitic Requiem (ultimate) — pull all + execute low HP
- Movement: mostly stationary (avg attack range 6.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `high`
- Non-ultimate: speed `fast`, buffs `medium`, debuffs `medium`, damage `medium`
- True damage: True damage `medium`

### Units Cyran benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `CRIT`  
Common buffers are **Lyca**, **Twins**, or **Hugin**.

- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) [signature fuel]

### Units that can act as a replacement for Cyran

**Damage**

- Frieren (100% `Magic` `True damage`)
- Sylphira (96% `Magic` `True damage`)
- Pippa (93% `Magic` `True damage`)

**Debuffs on enemies**

- Athalia (100% `ATK debuff`)
- Lucius (100% `ATK debuff`)
- Lyca (100% `ATK debuff`)

**Crowd Control**

- Dunlingr (100% `Silence`)
- Evie (100% `Silence`)
- Gwyneth (100% `Silence`)

### Summary for Cyran

#### Cyran Provides

- Artifact mimic (Mythic+) — All units
- Enemy artifact block (EX+10) — Single target

#### Damage types dealt by Cyran

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- True damage — All units — `low`

#### Debuffs provided by Cyran

- ATK debuff (Mythic+) — All units — `low`

#### Crowd Control provided by Cyran

- Steadfast — Area — Conditional
- Unaffected — Self — Conditional
- Bind — Area — `high`
- Silence (EX+10) — Single target — `high`

## Daimon

### Daimon's behavior

- Signature skill: Buddy Barrier — shield + ATK buff ally behind
- Movement: stationary (no finite attack range)
- Ally composition: place ally directly behind at battle prep (shield share, Life Drain, and ATK bond)

#### Skill overview

- Signature skill: speed `fast`, buffs `medium`
- Ultimate: speed `slow`, buffs `medium`, damage `low`
- Non-ultimate: speed `fast`, buffs `medium`, damage `high`
- True damage: Max HP-based damage `high`

### Units Daimon benefits from

Look for units providing: `Max HP`  
Common buffers are **Hugin** or **Koko**.

- **Lucius**
  - Max HP via Shield (area, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
- **Gala**
  - Max HP via Shield (single target, high)

### Units that can act as a replacement for Daimon

**Buffs on allies**

- Koko (100% `Life Drain` `Max HP`)
- Callan (60% `Max HP`)
- Cecia (60% `Life Drain`)

**Similar Skills**

- Shemira (72% `hp-scaling` `life-drain` `summoner`)
- Zorya (60% `hp-scaling` `life-drain`)

**Damage**

- Satrana (100% `Max HP-based damage` `DoT` `Magic`)
- Shadewing (100% `Max HP-based damage` `Magic` `DoT`)
- Shemira (100% `Max HP-based damage` `Magic`)

### Summary for Daimon

#### Damage types dealt by Daimon

- Primary damage type (unit): **Magic**
- Magic — Area, Self, Single target
- DoT — Area
- Max HP-based damage — Area — `high`

#### Buffs provided by Daimon

- Lifedrain buff — Single target — `medium`
- Shield — Multiple targets — `low`

## Damian

### Damian's behavior

- Signature skill: Inventor's Will — chariot haste aura for allies
- Movement: stationary (off battlefield)

#### Skill overview

- Signature skill: speed `fast`, heal `medium`, buffs `medium`, damage `low`
- Ultimate: speed `slow`, buffs `medium`, damage `high`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

### Units Damian benefits from

Look for units providing: `ATK` `Haste` `Healing` `Energy`  
Common buffers are **Mikola**, **Hugin**, or **Twins**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Velara**
  - Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Smokey & Meerky**
  - ATK buff (multiple targets, low)
  - Healing (multiple targets, medium)
  - Energy recovery (multiple targets, low) [signature fuel]

### Units benefitting from Damian

**16** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Aurora
- Cassadee
- Frieren
- Mikola
- Natsu
- Viperian
- Lyca
- Faramor
- Hugin
- Pippa

### Units that can act as a replacement for Damian

**Buffs on allies**

- Hugin (100% `Haste`)
- Mikola (100% `Haste`)
- Twins (100% `Haste`)

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

- Haste buff (Mythic+) — Multiple targets — `high` — conditional (frequent)

#### Crowd Control provided by Damian

- Blind — Single target — `high`
- Stun — Single target — `high`

## Dionel

### Dionel's behavior

- Signature skill: Dawn Light (ultimate) — airborne multi-hit AoE
- Movement: moving (avg attack range 0.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `medium`
- Non-ultimate: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`
- True damage: True damage `high`

### Units Dionel benefits from

Look for units providing: `ATK SPD / Haste` `Max HP` `Execution`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]

### Units that can act as a replacement for Dionel

**Buffs on allies**

- Aliceth (100% `DEF Penetration`)
- Cecia (66% `DEF Penetration`)
- Kordan (66% `DEF Penetration`)

**Damage**

- Athalia (100% `True damage` `Physical`)
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
- True damage — All units, Single target — `high`

#### Buffs provided by Dionel

- DEF Penetration buff — Single target — `high`

#### Debuffs provided by Dionel

- Vitality debuff (Mythic+) — Single target — `medium`

#### Crowd Control provided by Dionel

- Untargetable — Area — On Skill
- Knock up — Area — `low`

## Dunlingr

### Dunlingr's behavior

- Signature skill: Echo of Silence (ultimate) — forbid heals or ultimates
- Movement: stationary (avg attack range 6.4 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, heal `medium`, damage `high`
- Non-ultimate: speed `fast`, buffs `medium`, debuffs `medium`, damage `medium`
- True damage: HP loss `medium`

### Units Dunlingr benefits from

Look for units providing: `ATK SPD / Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
  - Max HP via Shield (summons only, low, conditional (frequent))
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Velara**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
- **Lucius**
  - Max HP via Shield (area, high)
- **Fay**
  - ATK SPD buff (multiple targets, low) [signature fuel]
  - Healing (arc, high, conditional (frequent))

### Units that can act as a replacement for Dunlingr

**Buffs on allies**

- Valka (73% `ATK SPD` `Life Drain`)

**Damage**

- Talene (100% `HP loss` `Magic`)
- Zorya (96% `HP loss` `Magic`)
- Aliceth (90% `HP loss`)

**Debuffs on enemies**

- Sinbad (100% `Energy drain` `ATK debuff`)
- Pandora (61% `ATK debuff` `Energy drain`)

**Crowd Control**

- Evie (100% `Silence`)
- Sylphira (96% `Silence`)
- Cyran (60% `Silence`)

### Summary for Dunlingr

#### Dunlingr Provides

- Heal lock (Curelock) — All units
- Summoning — Self
- Ultimate lock (Spellbind) — All units

#### Damage types dealt by Dunlingr

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target
- HP loss — Area — `medium`

#### Buffs provided by Dunlingr

- ATK buff (Mythic+) — Single target — `low`
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

- Signature skill: Howling Hurricane — free area pull at start
- Movement: moving (avg attack range 1.0 tiles)

#### Skill overview

- Signature skill: speed `fast`
- Ultimate: speed `slow`, damage `high`
- Non-ultimate: speed `fast`, buffs `medium`, debuffs `medium`, damage `medium`

### Units Eironn benefits from

Look for units providing: `Max HP` `Physical DEF`  
Common buffers are **Hugin**, **Rowan**, or **Koko**.

- **Lucius**
  - Max HP via Shield (area, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
- **Gala**
  - Max HP via Shield (single target, high)

### Units that can act as a replacement for Eironn

**Buffs on allies**

- Lorsan (80% `Dodge chance buff`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Crowd Control**

- Evie (96% `Displace` `Bind`)
- Ravion (65% `Displace`)

### Summary for Eironn

#### Damage types dealt by Eironn

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Single target

#### Buffs provided by Eironn

- Dodge chance buff — Single target — `high`

#### Debuffs provided by Eironn

- Haste debuff — Arc — `medium`
- Magic DEF debuff — Single target — `high`

#### Crowd Control provided by Eironn

- Bind — Single target — `high`
- Displace — Area — `medium`

## Twins

### Twins's behavior

- Signature skill: Starlight Waltz (ultimate) — high haste buff all allies
- Movement: moving / stationary (two units)

#### Skill overview

- Signature skill (ultimate): speed `slow`, buffs `medium`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

### Units Twins benefits from

Look for units providing: `Haste` `Healing` `Energy`  
Common buffers are **Mikola**, **Hugin**, or **Rowan**.

- **Velara**
  - Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]

### Units benefitting from Twins

**82** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Perseus
- Silven
- Nerion
- Valka
- Alsa
- Hepler
- Lenya
- Lumont
- Mehira
- Tasi

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

- Haste buff — All units — `high`
- Max HP buff — Multiple targets — `high`
- Shield — Single target — `medium`
- Vitality buff (Mythic+) — Multiple targets — `low`

#### Crowd Control provided by Twins

- Unaffected — Area — Conditional
- Blind — Area — `low`
- Knock back — Area — `low`

## Evie

### Evie's behavior

- Signature skill: Intel Chase (ultimate) — stealth + trigger burst
- Movement: high movement (repositioning skills)
- Ally composition: rearmost ally starts with healing quill; tracks highest damage dealer

#### Skill overview

- Signature skill (ultimate): speed `slow`, buffs `medium`, debuffs `medium`, damage `medium`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `high`

### Units Evie benefits from

Look for units providing: `Healing` `Energy`  
Common buffers are **Koko**, **Lorsan**, or **Mikola**.

- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Smokey & Meerky**
  - Healing (multiple targets, medium)
  - Energy recovery (multiple targets, low) [signature fuel]
- **Ludovic**
  - Healing (area, medium)
- **Velara**
  - Healing (area, medium)

### Units benefitting from Evie

**16** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Bonnie
- Shadewing
- Aliceth
- Himmel
- Baelran
- Damian
- Hammie
- Hodgkin
- Isabella
- Lorsan

### Units that can act as a replacement for Evie

**Buffs on allies**

- Fay (80% `Healing` `ATK`)
- Mikola (66% `Healing` `ATK`)
- Hugin (60% `ATK`)

**Damage**

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Cassadee (100% `Magic`)

**Debuffs on enemies**

- Frieren (100% `DoT`)
- Brutus (80% `DoT`)

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
- Healing — Multiple targets — `high`

#### Debuffs provided by Evie

- DoT — All units — `medium`

#### Crowd Control provided by Evie

- Bind — All units — `low`
- Displace — All units — `low`
- Silence — All units — `low`

## Faramor

### Faramor's behavior

- Signature skill: Sanctified Circle (ultimate) — no-heal zone + true DoT
- Movement: moving (avg attack range 1.0 tiles)
- Ally composition: bless adjacent ally at battle prep; prioritizes tile behind

#### Skill overview

- Signature skill (ultimate): speed `normal`, damage `high`
- Non-ultimate: speed `fast`, buffs `medium`, damage `high`
- True damage: HP loss `high`, True damage `medium`

### Units Faramor benefits from

Look for units providing: `ATK` `Haste` `Max HP`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]

### Units that can act as a replacement for Faramor

**Similar Skills**

- Arden (80% `aoe-damage` `dot-specialist`)
- Lorsan (80% `aoe-damage` `dot-specialist`)

**Damage**

- Vala (79% `True damage` `Physical` `HP loss`)
- Shadewing (71% `HP loss` `True damage`)
- Indris (69% `True damage` `Physical`)

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
- True damage — Multiple targets — `medium`

#### Debuffs provided by Faramor

- Vitality debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Faramor

- Stun — Area — `medium`

## Fay

### Fay's behavior

- Signature skill: Vibrant Dance (ultimate) — arc heal + ATK buff
- Movement: mostly stationary (avg attack range 5.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, heal `medium`, buffs `medium`, damage `medium`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `medium`

### Units Fay benefits from

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Lyca**, **Twins**, or **Hugin**.

- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units benefitting from Fay

- Granny Dahnie
- Niru
- Lucca
- Smokey & Meerky

### Units that can act as a replacement for Fay

**Buffs on allies**

- Evie (73% `Healing` `ATK`)
- Mikola (69% `Healing` `ATK` `Vitality buff`)

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
- Healing — Arc — `high` — conditional (frequent)
- Vitality buff (Mythic+) — Single target — `low`

#### Debuffs provided by Fay

- Magic DEF debuff — Multiple targets — `low`
- Phys DEF debuff — Multiple targets — `low`

## Florabelle

### Florabelle's behavior

- Signature skill: Pounding Blow (ultimate) — summon stomper ally
- Movement: stationary (no finite attack range)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `high`
- Non-ultimate: speed `fast`, buffs `medium`, damage `low`

### Units Florabelle benefits from

Look for units providing: `ATK` `Haste`  
Common buffers are **Hugin**, **Twins**, or **Mikola**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]

### Units benefitting from Florabelle

- Gala
- Phraesto
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
- Physical — Area, Self, Single target

#### Buffs provided by Florabelle

- Lifedrain buff — Summons only — `high` — conditional (frequent)
- Haste buff (Mythic+) — Summons only — `medium` — conditional (frequent)
- Shield (Mythic+) — Summons only — `low` — conditional (frequent)
- Summon damage buff (Supreme+) — Summons only — `medium`

#### Crowd Control provided by Florabelle

- Immune (Supreme+) — Self — Form
- Knock up — Area — `low`

## Frieren

### Frieren's behavior

- Signature skill: Zoltraak (ultimate) — high-damage magic beam
- Movement: stationary (avg attack range 7.0 tiles)
- Ally composition: frontmost ally shares damage reduction with this hero

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `high`
- Non-ultimate: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`
- True damage: True damage `high`

### Units Frieren benefits from

Look for units providing: `ATK` `Haste`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units benefitting from Frieren

- Bonnie

### Units that can act as a replacement for Frieren

**Damage**

- Sylphira (86% `True damage` `Magic`)
- Athalia (83% `True damage`)
- Dionel (83% `True damage`)

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
- DoT — All units, Area, Single target
- True damage — All units, Single target — `high`

#### Debuffs provided by Frieren

- DoT — Area — `high`
- Vitality debuff — Single target — `high`

#### Crowd Control provided by Frieren

- Stun — Single target — `low`
- Knock down (Supreme+) — Single target — `medium`

## Gala

### Gala's behavior

- Signature skill: Time Recast — summon shadow copy of ally
- Movement: stationary (avg attack range 10.0 tiles)

#### Skill overview

- Signature skill: speed `fast`
- Ultimate: speed `normal`, buffs `medium`, damage `high`
- Non-ultimate: speed `fast`, buffs `medium`, damage `high`

### Units Gala benefits from

Look for units providing: `ATK` `Haste` `Energy`  
Common buffers are **Hugin**, **Twins**, or **Mikola**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]

### Units benefitting from Gala

- Faramor
- Sonja
- Velara

### Units that can act as a replacement for Gala

**Buffs on allies**

- Hugin (100% `Haste` `Max HP`)
- Twins (83% `Haste` `Max HP`)
- Hepler (80% `Max HP` `Haste`)

**Damage**

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Cassadee (100% `Magic`)

**Crowd Control**

- Alna (100% `Bind`)
- Arden (100% `Bind`)
- Atalanta (100% `Bind`)

### Summary for Gala

#### Gala Provides

- Artifact amplification (Mythic+) — Single target
- Artifact echo (Mythic+) — Single target
- Summoning (Mythic+) — Single target

#### Gala Requires

- Boss encounter — Enemies
- Artifact buffs active (Supreme+) — Self

#### Damage types dealt by Gala

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Buffs provided by Gala

- Haste buff — Single target — `high`
- Shield — Single target — `high`

#### Crowd Control provided by Gala

- Steadfast (Supreme+) — Self — On Skill
- Bind — Single target — `medium`

## Gerda

### Gerda's behavior

- Signature skill: Spring Therapy — battle-start heal zone
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill: speed `fast`, heal `medium`, damage `medium`
- Ultimate: speed `slow`, heal `medium`, damage `medium`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

### Units Gerda benefits from

Look for units providing: `Max HP` `Healing`  
Common buffers are **Koko**, **Lorsan**, or **Hugin**.

- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Evie**
  - Healing (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)

### Units that can act as a replacement for Gerda

**Buffs on allies**

- Antandra (100% `Healing`)
- Evie (100% `Healing`)
- Fay (100% `Healing`)

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
- Physical — Area, Multiple targets, Self, Single target

#### Buffs provided by Gerda

- Healing — Single target — `medium`

#### Crowd Control provided by Gerda

- Unaffected — Self — Conditional
- Interrupt — Area — `medium`
- Stun — Single target — `high`

## Granny Dahnie

### Granny Dahnie's behavior

- Signature skill: Threshold of Jade (ultimate) — root zone + HP drain
- Movement: moving (avg attack range 2.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, heal `medium`, damage `medium`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `low`

### Units Granny Dahnie benefits from

Look for units providing: `Healing` `Energy` `Physical DEF` `Magic DEF`  
Common buffers are **Rowan**, **Lyca**, or **Mikola**.

- **Fay**
  - Healing (arc, high, conditional (frequent))
  - DEF buff (multiple targets, low)
  - DEF buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Velara**
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Hewynn**
  - Healing (all units, medium)

### Units that can act as a replacement for Granny Dahnie

**Similar Skills**

- Brutus (66% `hp-scaling` `taunt`)
- Tilaya (60% `hp-scaling`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Pandora (100% `ATK debuff` `Haste debuff`)
- Kafra (72% `ATK debuff` `Haste debuff`)
- Lyca (72% `ATK debuff`)

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
- ATK debuff (Supreme+) — Single target — `high`

#### Crowd Control provided by Granny Dahnie

- Unaffected — Self — Conditional
- Stun — Area — `low`
- Taunt — Single target — `high`

## Gunnar

### Gunnar's behavior

- Signature skill: Annihilation Directive (ultimate) — long-range area bombing
- Movement: stationary (no finite attack range)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `high`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `medium`
- True damage: Max HP-based damage `medium`

### Units Gunnar benefits from

Look for units providing: `ATK SPD / Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Velara**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
- **Lucius**
  - Max HP via Shield (area, high)
- **Fay**
  - ATK SPD buff (multiple targets, low) [signature fuel]
  - Healing (arc, high, conditional (frequent))
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
- **Hewynn**
  - Healing (all units, medium)

### Units that can act as a replacement for Gunnar

**Buffs on allies**

- Fay (66% `ATK SPD` `Vitality buff`)

**Damage**

- Satrana (91% `Max HP-based damage` `DoT`)
- Brutus (90% `Max HP-based damage` `DoT` `Physical`)
- Daimon (87% `Max HP-based damage` `DoT`)

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
- Max HP-based damage — All units — `high`

#### Buffs provided by Gunnar

- ATK SPD buff — Single target — `low`
- Shield — Single target — `high`
- Ranged DEF buff (Legendary+) — Single target — `low`
- Vitality buff (Legendary+) — Single target — `low`

#### Crowd Control provided by Gunnar

- Stun — All units — `low`

## Gwyneth

### Gwyneth's behavior

- Signature skill: Hailing Arrows (ultimate) — area arrow rain
- Movement: stationary (avg attack range 8.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `high`
- Non-ultimate: speed `fast`, debuffs `medium`, damage `high`
- True damage: Max HP-based damage `medium`

### Units Gwyneth benefits from

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Lyca**, **Twins**, or **Hugin**.

- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Gwyneth

**Similar Skills**

- Mirael (80% `dot-specialist` `fire-attack`)

**Damage**

- Brutus (100% `Physical` `DoT` `Max HP-based damage`)
- Gunnar (100% `Physical` `DoT` `Max HP-based damage`)
- Korin (100% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Brutus (100% `DoT`)
- Evie (100% `DoT`)
- Frieren (100% `DoT`)

**Crowd Control**

- Indris (71% `Bind` `Silence`)
- Evie (69% `Bind` `Silence`)
- Arden (65% `Bind` `Stun`)

### Summary for Gwyneth

#### Damage types dealt by Gwyneth

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- DoT — Single target
- Max HP-based damage — Single target — `low`

#### Debuffs provided by Gwyneth

- DoT — Single target — `high`

#### Crowd Control provided by Gwyneth

- Bind — Area — `medium`
- Silence — Area — `low`
- Stun — Area — `low`

## Hammie

### Hammie's behavior

- Signature skill: Pretty Fireball (ultimate) — AoE magic fireball
- Movement: mostly stationary (avg attack range 5.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `medium`
- Non-ultimate: speed `normal`, heal `medium`, buffs `medium`, damage `low`

### Units Hammie benefits from

Look for units providing: `ATK` `Healing`  
Common buffers are **Lyca**, **Mikola**, or **Hugin**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Velara**
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]

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

- Signature skill: Flesh Feast — instantly defeat weakest unit
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill: speed `fast`, buffs `medium`, debuffs `medium`
- Ultimate: speed `slow`, heal `medium`, damage `low`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `low`
- True damage: HP loss `low`

### Units Harak benefits from

Look for units providing: `Haste` `Max HP` `CRIT` `Healing` `Energy`  
Common buffers are **Twins**, **Koko**, or **Hugin**.

- **Velara**
  - Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Evie**
  - Healing (multiple targets, high)

### Units that can act as a replacement for Harak

**Buffs on allies**

- Brutus (100% `Life Drain`)
- Cecia (100% `Life Drain`)
- Daimon (100% `Life Drain`)

**Similar Skills**

- Seth (66% `assassin` `life-drain`)

**Damage**

- Aliceth (100% `Physical` `HP loss`)
- Faramor (100% `Physical` `HP loss`)
- Kordan (100% `Physical` `HP loss`)

**Crowd Control**

- Kordan (100% `Knock back` `Knock down`)
- Scarlita (100% `Knock back` `Knock down`)
- Ulmus (91% `Knock back` `Knock down`)

### Summary for Harak

#### Harak Provides

- Instant defeat — Single target
- Invincibility — Self

#### Harak Requires

- Boss encounter — Allies

#### Damage types dealt by Harak

- Primary damage type (unit): **Physical**
- Physical — Single target
- HP loss — Single target — `low`

#### Buffs provided by Harak

- Crit buff — Single target — `high`
- Lifedrain buff (Legendary+) — Single target — `low`

#### Debuffs provided by Harak

- Execution debuff — Single target — `low`

#### Crowd Control provided by Harak

- Unaffected — Self — On Skill
- Knock back — Single target — `high`
- Knock down — Single target — `low`

## Hepler

### Hepler's behavior

- Signature skill: Form Shift (ultimate) — toggle attack/support form
- Movement: moving (avg attack range 1.0 tiles)
- Ally composition: frontmost adjacent ally gets fatal-blow protection

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `high`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `high`

### Units Hepler benefits from

Look for units providing: `ATK` `Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Velara**
  - Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]

### Units benefitting from Hepler

- Nerion
- Daimon

### Units that can act as a replacement for Hepler

**Buffs on allies**

- Hugin (100% `Max HP` `Haste`)
- Gala (96% `Max HP` `Haste`)
- Callan (80% `Max HP`)

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
- Natsu (100% `Haste debuff`)
- Eironn (75% `Haste debuff`)

**Crowd Control**

- Antandra (66% `Taunt` `Stun`)

### Summary for Hepler

#### Hepler Provides

- Invincibility (Mythic+) — Area

#### Hepler Requires

- Form or stance active (Legendary+) — Enemies

#### Damage types dealt by Hepler

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target

#### Buffs provided by Hepler

- Haste buff — Single target — `low`
- Shield — Multiple targets — `medium`

#### Debuffs provided by Hepler

- Haste debuff — Area — `medium`

#### Crowd Control provided by Hepler

- Blind — Area — `high`
- Stun — Area — `low`
- Taunt — Area — `high`

## Hewynn

### Hewynn's behavior

- Signature skill: Rain Prayer (ultimate) — AoE team healing
- Movement: stationary (no finite attack range)

#### Skill overview

- Signature skill (ultimate): speed `slow`, heal `medium`, damage `medium`
- Non-ultimate: speed `fast`, heal `medium`, damage `medium`

### Units Hewynn benefits from

Look for units providing: `ATK`  
Common buffers are **Lyca**, **Hugin**, or **Rowan**.

- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]

### Units benefitting from Hewynn

**11** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Alna
- Callan
- Contess
- Evie
- Gerda
- Igor
- Phraesto
- Reinier
- Saida
- Tilaya

### Units that can act as a replacement for Hewynn

**Buffs on allies**

- Koko (100% `Healing`)
- Lorsan (100% `Healing`)
- Velara (96% `Healing`)

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

- Unaffected (Mythic+) — Self — On Skill

## Himmel

### Himmel's behavior

- Signature skill: Hero Party — buff needing Mage+Tank+Support
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill: speed `slow`, buffs `medium`, damage `high`
- Ultimate: speed `normal`, damage `high`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `high`
- True damage: Max HP-based damage `low`

### Units Himmel benefits from

Look for units providing: `ATK` `Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Koko**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
  - Enables Party composition via Support (party slot)
- **Velara**
  - Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
  - Enables Party composition via Support (party slot)
- **Lucius**
  - Max HP via Shield (area, high)
  - Enables Party composition via Tank (party slot)
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))
  - Enables Party composition via Support (party slot)
- **Hewynn**
  - Healing (all units, medium)
  - Enables Party composition via Support (party slot)

### Units benefitting from Himmel

- Talene

### Units that can act as a replacement for Himmel

**Buffs on allies**

- Twins (77% `Max HP`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Brutus (96% `Physical` `Max HP-based damage`)
- Korin (96% `Physical` `Max HP-based damage`)

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

#### Crowd Control provided by Himmel

- Unaffected — Multiple targets — On Skill

## Hodgkin

### Hodgkin's behavior

- Signature skill: Cannon Fire (ultimate) — AoE cannon salvo
- Movement: moving (avg attack range 3.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `high`
- Non-ultimate: speed `fast`, heal `medium`, debuffs `medium`, damage `medium`

### Units Hodgkin benefits from

Look for units providing: `ATK` `Healing` `Energy`  
Common buffers are **Rowan**, **Lyca**, or **Mikola**.

- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]

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

- Signature skill: Unstoppable! (ultimate) — charge + shield assault
- Movement: stationary (no finite attack range)
- Self placement: stays anchored to battle-prep tile; returns after displacement
- Ally composition: put one ally on the tile 1 tile behind (ATK bonus; buff ends if they leave the sigil)

#### Skill overview

- Signature skill (ultimate): speed `slow`, buffs `medium`
- Non-ultimate: speed `fast`, buffs `medium`, damage `high`

### Units Hugin benefits from

Look for units providing: `Haste` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Lyca**.

- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units benefitting from Hugin

**78** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Perseus
- Silven
- Tasi
- Valka
- Alsa
- Frieren
- Hepler
- Lenya
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

- Signature skill: Funereal Ring (ultimate) — tombstone zone damage
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `medium`
- Non-ultimate: speed `fast`, heal `medium`, debuffs `medium`, damage `medium`

### Units Igor benefits from

Look for units providing: `Healing` `Life Drain`  
Common buffers are **Koko**, **Lorsan**, or **Mikola**.

- **Cecia**
  - Lifedrain buff (area, high)
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Evie**
  - Healing (multiple targets, high)
- **Ludovic**
  - Healing (area, medium)

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
- Physical — All units, Area, Single target

#### Debuffs provided by Igor

- Healing debuff (EX+5) — Single target — `low`

#### Crowd Control provided by Igor

- Untargetable — Area — On Skill

## Indris

### Indris's behavior

- Signature skill: Spellbane Shot (ultimate) — silence + multi-debuff shot
- Movement: stationary (no finite attack range)

#### Skill overview

- Signature skill (ultimate): speed `slow`, debuffs `medium`, damage `medium`
- Non-ultimate: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`
- True damage: Max HP-based damage `medium`, True damage `high`

### Units Indris benefits from

Look for units providing: `ATK` `ATK SPD / Haste`  
Common buffers are **Lyca**, **Twins**, or **Hugin**.

- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
  - Enables Multiple debuffs on target via 5 debuff types
  - Enables Debuff on target via ATK debuff (all units)
- **Sinbad**
  - Enables Multiple debuffs on target via 6 debuff types
  - Enables Debuff on target via ATK debuff (multiple targets)
- **Kulu**
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via Damage taken debuff (all units)
- **Natsu**
  - Enables Multiple debuffs on target via 3 debuff types
  - Enables Debuff on target via Haste debuff (area)
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via ATK debuff (multiple targets)

### Units that can act as a replacement for Indris

**Damage**

- Pippa (91% `True damage` `Max HP-based damage`)
- Sylphira (89% `True damage` `Max HP-based damage`)
- Korin (87% `Physical` `Max HP-based damage` `True damage`)

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
- Max HP-based damage — Single target — `medium`
- True damage — Multiple targets — `high`

#### Debuffs provided by Indris

- Damage taken debuff — Multiple targets — `low`
- Magic DEF debuff — Single target — `low`
- Phys DEF debuff (EX+10) — Single target — `medium`

#### Crowd Control provided by Indris

- Bind — Single target — `high`
- Knock back — Area — `high`
- Silence — Single target — `low`

## Isabella

### Isabella's behavior

- Signature skill: Grimoire Pact (ultimate) — permanent stat buff to companion
- Movement: stationary (no finite attack range)
- Ally composition: frontmost ally becomes companion (stat stacks and ult buffs)

#### Skill overview

- Signature skill (ultimate): speed `slow`, buffs `medium`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `medium`

### Units Isabella benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `Healing` `Energy`  
Common buffers are **Mikola**, **Hugin**, or **Twins**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
  - Healing (arc, high, conditional (frequent))
- **Velara**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
- **Smokey & Meerky**
  - ATK buff (multiple targets, low)
  - Healing (multiple targets, medium)
  - Energy recovery (multiple targets, low) [signature fuel]
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]

### Units that can act as a replacement for Isabella

**Buffs on allies**

- Damian (100% `Haste`)
- Gala (100% `Haste`)
- Hugin (100% `Haste`)

**Similar Skills**

- Hammie (66% `ally-buffer` `ally-healer`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Debuffs on enemies**

- Athalia (100% `ATK debuff`)
- Cyran (100% `ATK debuff`)
- Granny Dahnie (100% `ATK debuff`)

### Summary for Isabella

#### Isabella Requires

- Once per battle — Allies

#### Damage types dealt by Isabella

- Primary damage type (unit): **Magic**
- Magic — Area, Single target

#### Buffs provided by Isabella

- Haste buff — Multiple targets — `low` — conditional (frequent)

#### Debuffs provided by Isabella

- ATK debuff — Single target — `high`

#### Crowd Control provided by Isabella

- Unaffected — Single target — Once

## Kafra

### Kafra's behavior

- Signature skill: Gale Thrust (ultimate) — mark + high single-target hit
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill (ultimate): speed `slow`, debuffs `medium`, damage `medium`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `high`

### Units Kafra benefits from

Look for units providing: `ATK` `Max HP` `Healing`  
Common buffers are **Twins**, **Lyca**, or **Rowan**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Pandora**
  - Max HP buff (single target, low)
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Velara**
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Kafra

**Similar Skills**

- Sinbad (66% `enemy-debuffer` `mark-target`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Granny Dahnie (60% `ATK debuff` `Haste debuff`)
- Lyca (60% `ATK debuff` `Phys DEF debuff`)
- Ravion (60% `ATK debuff` `Phys DEF debuff`)

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
- Phys DEF debuff — Single target — `low`
- ATK debuff (Mythic+) — Single target — `medium`
- Haste debuff (Mythic+) — Single target — `low`

#### Crowd Control provided by Kafra

- Unaffected (Mythic+) — Self — On Skill
- Knock back — Single target — `low`
- Stun — Single target — `high`

## Koko

### Koko's behavior

- Signature skill: Full Energy (ultimate) — DMG reduction + true damage return
- Movement: mostly stationary (avg attack range 4.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, buffs `medium`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `high`

### Units Koko benefits from

Look for units providing: `Haste` `Healing` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Velara**
  - Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]

### Units benefitting from Koko

**41** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Perseus
- Silven
- Valka
- Kordan
- Talene
- Himmel
- Igor
- Alna
- Antandra
- Athalia

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
- Lucy (100% `Damage taken debuff`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Arden (100% `Stun`)

### Summary for Koko

#### Damage types dealt by Koko

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target

#### Buffs provided by Koko

- Damage taken reduction — All units — `high`
- Healing — All units — `high`
- Lifedrain buff — Multiple targets — `medium`
- Shield (Mythic+) — All units — `low`
- Vitality buff (Supreme+) — Single target — `low`

#### Debuffs provided by Koko

- Damage taken debuff — Area — `low`

#### Crowd Control provided by Koko

- Stun — Area — `medium`

## Kordan

### Kordan's behavior

- Signature skill: Dominance Ring (ultimate) — immobilize + zone damage
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill (ultimate): speed `slow`, buffs `medium`, damage `medium`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `high`
- True damage: HP loss `low`

### Units Kordan benefits from

Look for units providing: `ATK` `Max HP` `Healing` `DEF Penetration` `Life Drain`  
Common buffers are **Koko**, **Twins**, or **Lyca**.

- **Cecia**
  - Max HP buff (single target, high)
  - DEF Penetration buff (single target, medium)
  - Lifedrain buff (area, high)
  - ATK SPD buff (single target, low) [signature fuel]
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Pandora**
  - Max HP buff (single target, low)
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]

### Units that can act as a replacement for Kordan

**Buffs on allies**

- Cecia (100% `Life Drain` `DEF Penetration`)
- Koko (80% `Life Drain`)

**Similar Skills**

- Pippa (100% `hp-scaling` `self-repositioner`)
- Athalia (66% `hp-scaling` `self-repositioner`)
- Marilee (66% `hp-scaling` `self-repositioner`)

**Damage**

- Aliceth (100% `Physical` `HP loss`)
- Faramor (100% `Physical` `HP loss`)
- Ravion (100% `Physical` `HP loss`)

### Summary for Kordan

#### Damage types dealt by Kordan

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- HP loss — Single target — `low`

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

- Signature skill: Demonseal Spear (ultimate) — pierce-through spear strike
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `low`
- Non-ultimate: speed `fast`, buffs `medium`, damage `medium`
- True damage: Max HP-based damage `medium`, True damage `medium`

### Units Korin benefits from

Look for units providing: `ATK SPD / Haste` `Max HP`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]

### Units that can act as a replacement for Korin

**Buffs on allies**

- Callan (100% `Max HP`)
- Contess (100% `Max HP`)
- Daimon (100% `Max HP`)

**Similar Skills**

- Scarlita (66% `ally-shielder` `hp-scaling`)
- Lucca (60% `ally-shielder`)
- Silven (60% `hp-scaling`)

**Damage**

- Temesia (99% `Physical` `Max HP-based damage`)
- Nara (92% `Max HP-based damage` `True damage` `Physical`)
- Indris (89% `Physical` `Max HP-based damage` `True damage`)

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

- Signature skill: Devastating Axe (ultimate) — stack Phys DEF debuff
- Movement: moving (avg attack range 1.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `normal`, debuffs `medium`, damage `medium`
- Non-ultimate: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

### Units Kruger benefits from

Look for units providing: `Max HP` `Physical DEF`  
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Lucius**
  - Max HP via Shield (area, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Gala**
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
  - ATK SPD via Haste buff (single target, low) [signature fuel]
- **Callan**
  - Max HP via Shield (multiple targets, medium)

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

- Signature skill: Demolition Zone — battle-start movement-blocking wall
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill: speed `slow`, buffs `medium`, damage `low`
- Ultimate: speed `normal`, damage `high`
- Non-ultimate: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

### Units Kulu benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `DEF Penetration`  
Common buffers are **Twins**, **Lyca**, or **Mikola**.

- **Aliceth**
  - ATK buff (multiple targets, medium)
  - DEF Penetration buff (single target, high)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) [signature fuel]

### Units benefitting from Kulu

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

- Reinier (80% `Displace` `Knock up`)
- Cassadee (66% `Knock back` `Knock up`)
- Kordan (66% `Knock back` `Knock up`)

### Summary for Kulu

#### Kulu Provides

- Invincibility — Self
- Enhanced form (Mythic+) — Single target

#### Damage types dealt by Kulu

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target

#### Buffs provided by Kulu

- ATK buff (Legendary+) — Single target — `low`
- DEF Penetration buff (Mythic+) — Single target — `low`

#### Debuffs provided by Kulu

- Movement speed debuff — Area — `medium`
- Damage taken debuff (Mythic+) — All units — `low`

#### Crowd Control provided by Kulu

- Unaffected — Area — On Ultimate
- Displace — Single target — `low`
- Knock back — Single target — `low`
- Knock up — Single target — `low`

## Laios

### Laios's behavior

- Signature skill: Dungeon Gourmet — cook ingredients for random ally buffs
- Movement: moving (avg attack range 1.0 tiles)

#### Skill overview

- Signature skill: speed `slow`, heal `medium`, buffs `medium`, damage `high`
- Ultimate: speed `fast`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `high`

### Units Laios benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Lyca**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Velara**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
  - Healing (arc, high, conditional (frequent))
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
  - Max HP via Shield (summons only, low, conditional (frequent))

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

- Enemy monsters present (Mythic+) — Enemies
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

- Signature skill: Wild Duel (ultimate) — dash + duel multi-hit
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `medium`
- Non-ultimate: speed `fast`, buffs `medium`, damage `high`

### Units Lenya benefits from

Look for units providing: `Haste` `Max HP` `CRIT` `CRIT DMG Boost` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Lucius**
  - Max HP via Shield (area, high)

### Units that can act as a replacement for Lenya

**Buffs on allies**

- Callan (100% `Max HP`)
- Gala (100% `Max HP`)
- Hepler (100% `Max HP`)

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

- Crit buff — Single target — `medium`
- Shield (Supreme+) — Single target — `high`

#### Crowd Control provided by Lenya

- Unaffected — Self — Once
- Knock back — Area — `low`
- Stun — Single target — `medium`

## Lily May

### Lily May's behavior

- Signature skill: Tempest Shot (ultimate) — interrupt enemy ultimate
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill (ultimate): speed `slow`, debuffs `medium`, damage `high`
- Non-ultimate: speed `fast`, buffs `medium`, damage `low`
- True damage: Max HP-based damage `low`

### Units Lily May benefits from

Look for units providing: `ATK` `DEF Penetration`  
Common buffers are **Lyca**, **Rowan**, or **Twins**.

- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Aliceth**
  - ATK buff (multiple targets, medium)
  - DEF Penetration buff (single target, high)
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]

### Units benefitting from Lily May

- Bonnie
- Aliceth

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

- Reinier (100% `Interrupt`)
- Smokey & Meerky (100% `Interrupt`)
- Sylphira (80% `Interrupt`)

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

- Energy drain — Single target — `high`

#### Crowd Control provided by Lily May

- Unaffected — Self — Start of Battle
- Interrupt — Single target — `low`

## Lorsan

### Lorsan's behavior

- Signature skill: Whispering Tempest (ultimate) — storm zone + haste debuff
- Movement: stationary (no finite attack range)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `high`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `high`

### Units Lorsan benefits from

Look for units providing: `ATK` `Healing`  
Common buffers are **Lyca**, **Mikola**, or **Hugin**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Velara**
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units benefitting from Lorsan

**27** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Nerion
- Valka
- Carolina
- Alna
- Athalia
- Berial
- Bryon
- Callan
- Contess
- Dunlingr

### Units that can act as a replacement for Lorsan

**Buffs on allies**

- Koko (83% `Healing`)
- Hewynn (66% `Healing`)

**Similar Skills**

- Arden (100% `aoe-damage` `dot-specialist`)
- Faramor (80% `aoe-damage` `dot-specialist`)
- Viperian (66% `aoe-damage` `dot-specialist`)

**Damage**

- Bryon (100% `DoT` `Magic`)
- Cryonaia (100% `Magic` `DoT`)
- Frieren (100% `Magic` `DoT`)

**Crowd Control**

- Tasi (96% `Stun`)
- Antandra (80% `Stun`)
- Lucca (80% `Stun`)

### Summary for Lorsan

#### Damage types dealt by Lorsan

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — Area

#### Buffs provided by Lorsan

- Dodge chance buff — Single target — `medium`
- Healing (Mythic+) — All units — `high`

#### Crowd Control provided by Lorsan

- Unaffected (Supreme+) — Self — On Skill
- Stun (Mythic+) — Multiple targets — `high`

## Lucca

### Lucca's behavior

- Signature skill: Quake Slam (ultimate) — area knockdown slam
- Movement: moving (avg attack range 1.0 tiles)
- Ally composition: place adjacent allies behind at battle prep (DEF buff)
- Ally composition: place allies on adjacent tiles behind at battle start (shields and ATK boost)

#### Skill overview

- Signature skill (ultimate): speed `normal`, damage `medium`
- Non-ultimate: speed `fast`, buffs `medium`, damage `low`

### Units Lucca benefits from

Look for units providing: `Max HP` `Healing` `Physical DEF` `Magic DEF`  
Common buffers are **Koko**, **Twins**, or **Rowan**.

- **Fay**
  - Healing (arc, high, conditional (frequent))
  - DEF buff (multiple targets, low)
  - DEF buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Lucius**
  - Max HP via Shield (area, high)
- **Velara**
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)

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
- Physical — Area, Self, Single target

#### Crowd Control provided by Lucca

- Immune — Self — On Skill
- Interrupt — Single target — `medium`
- Knock down — Area — `low`
- Knock up — Area — `low`
- Stun — Area — `medium`

## Lucius

### Lucius's behavior

- Signature skill: Divine Light Aegis (ultimate) — area shield + light damage
- Movement: moving (avg attack range 1.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, buffs `medium`, damage `high`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `medium`

### Units Lucius benefits from

Look for units providing: `Healing`  
Common buffers are **Lyca**, **Mikola**, or **Rowan**.

- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Velara**
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Hewynn**
  - Healing (all units, medium)
- **Fay**
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]

### Units benefitting from Lucius

**14** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Shadewing
- Alna
- Daimon
- Eironn
- Gerda
- Kruger
- Saida
- Silvina
- Sonja
- Thoran

### Units that can act as a replacement for Lucius

**Buffs on allies**

- Hugin (90% `Max HP`)
- Saida (75% `Max HP`)

**Similar Skills**

- Hepler (66% `ally-healer` `ally-shielder`)
- Solise (66% `ally-healer` `ally-shielder`)
- Twins (66% `ally-healer` `ally-shielder`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Lyca (100% `ATK debuff`)
- Sinbad (90% `ATK debuff`)
- Athalia (83% `ATK debuff`)

**Crowd Control**

- Atalanta (100% `Knock back` `Stun`)
- Cassadee (100% `Knock back` `Stun`)
- Lenya (100% `Knock back` `Stun`)

### Summary for Lucius

#### Lucius Provides

- Reposition enemies — Single target

#### Damage types dealt by Lucius

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Lucius

- Shield — Area — `high`

#### Debuffs provided by Lucius

- ATK debuff (Mythic+) — Single target — `high`

#### Crowd Control provided by Lucius

- Knock back — Single target — `high`
- Stun — Single target — `low`

## Lucy

### Lucy's behavior

- Signature skill: Star Dress: Aquarius Form — permanent AoE water form
- Movement: moving (avg attack range 1.0 tiles)

#### Skill overview

- Signature skill: speed `fast`, debuffs `medium`, damage `high`
- Ultimate: speed `fast`, damage `high`
- Non-ultimate: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

### Units Lucy benefits from

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Dunlingr**
  - ATK SPD buff (all units, low) [signature fuel]
  - Haste buff (single target, low) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Lucy

**Buffs on allies**

- Callan (100% `Max HP`)
- Gala (100% `Max HP`)
- Hepler (100% `Max HP`)

**Damage**

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Cassadee (100% `Magic`)

**Debuffs on enemies**

- Kulu (100% `Damage taken debuff`)
- Koko (80% `Damage taken debuff`)
- Kruger (80% `Damage taken debuff`)

### Summary for Lucy

#### Damage types dealt by Lucy

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Lucy

- Shield (Mythic+) — Single target — `high`

#### Debuffs provided by Lucy

- Damage taken debuff — All units — `low`

#### Crowd Control provided by Lucy

- Unaffected — Self — On Skill
- Knock up — All units — `medium`
- Stun — Single target — `high`

## Ludovic

### Ludovic's behavior

- Signature skill: Eternal Serenity (ultimate) — area sustained healing
- Movement: stationary (no finite attack range)

#### Skill overview

- Signature skill (ultimate): speed `slow`, heal `medium`, damage `medium`
- Non-ultimate: speed `fast`, heal `medium`, damage `medium`

### Units Ludovic benefits from

Look for units providing: `Healing`  
Common buffers are **Lyca**, **Mikola**, or **Rowan**.

- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Velara**
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Hewynn**
  - Healing (all units, medium)
- **Fay**
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]

### Units that can act as a replacement for Ludovic

**Buffs on allies**

- Antandra (64% `Healing`)
- Evie (64% `Healing`)
- Fay (64% `Healing`)

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

#### Ludovic Provides

- Revive ally — Area

#### Damage types dealt by Ludovic

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Buffs provided by Ludovic

- Healing — Area — `medium`
- Healing over time — Single target — `high`

#### Crowd Control provided by Ludovic

- Unaffected — Self — On Skill
- Stun (Supreme+) — Single target — `medium`

## Lumont

### Lumont's behavior

- Signature skill: Lumont's Charge (ultimate) — charge + stomp knockdown
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `high`
- Non-ultimate: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

### Units Lumont benefits from

Look for units providing: `Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Velara**
  - Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Pandora**
  - Max HP buff (single target, low)
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]

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
- Zandrok (80% `Stun`)
- Lucca (75% `Stun` `Knock up`)

### Summary for Lumont

#### Damage types dealt by Lumont

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Lumont

- DEF buff — Multiple targets — `low`

#### Debuffs provided by Lumont

- ATK debuff (Mythic+) — Single target — `medium`

#### Crowd Control provided by Lumont

- Unaffected — Self — On Skill
- Stun — Area — `high`
- Taunt — Single target — `medium`
- Knock up (Mythic+) — Single target — `low`

## Lyca

### Lyca's behavior

- Signature skill: Comet Archery (ultimate) — area ranged volley
- Movement: stationary (avg attack range 11.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `medium`
- Non-ultimate: speed `fast`, buffs `medium`, debuffs `medium`, damage `medium`

### Units Lyca benefits from

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units benefitting from Lyca

**75** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight
- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Perseus
- Indris
- Silven
- Aliceth
- Valka
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

#### Crowd Control provided by Lyca

- Stun (EX+10) — Single target — `medium`

## Marcille

### Marcille's behavior

- Signature skill: Silver-White Wings that Streak Across the Skies (ultimate) — large AoE magic damage
- Movement: stationary (no finite attack range)
- Ally composition: place ally 1 tile in front at battle prep (revive target)

#### Skill overview

- Signature skill (ultimate): speed `normal`, buffs `medium`, damage `high`
- Non-ultimate: speed `fast`, heal `medium`, damage `high`

### Units Marcille benefits from

Look for units providing: `ATK SPD / Haste` `Healing` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Lyca**.

- **Velara**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Fay**
  - ATK SPD buff (multiple targets, low) [signature fuel]
  - Healing (arc, high, conditional (frequent))
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Hewynn**
  - Healing (all units, medium)

### Units that can act as a replacement for Marcille

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

- Haste buff — Single target — `low`

#### Crowd Control provided by Marcille

- Unaffected (Supreme+) — Self — On Skill
- Blind — Single target — `medium`
- Interrupt (Mythic+) — Single target — `high`

## Marilee

### Marilee's behavior

- Signature skill: Mid-Air Shot (ultimate) — high-damage precision shot
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `low`
- Non-ultimate: speed `fast`, buffs `medium`, damage `low`
- True damage: True damage `low`

### Units Marilee benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `CRIT` `CRIT DMG Boost`  
Common buffers are **Lyca**, **Twins**, or **Mikola**.

- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) [signature fuel]

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

- Signature skill: Euphoric Rush (ultimate) — AoE damage + charm
- Movement: moving (avg attack range 1.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `medium`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `low`

### Units Mehira benefits from

Look for units providing: `Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Velara**
  - Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
  - Max HP via Shield (summons only, low, conditional (frequent))

### Units that can act as a replacement for Mehira

**Buffs on allies**

- Damian (100% `Haste`)
- Gala (100% `Haste`)
- Hugin (100% `Haste`)

**Damage**

- Alsa (100% `Magic`)
- Callan (100% `Magic`)
- Cassadee (100% `Magic`)

**Debuffs on enemies**

- Berial (100% `Damage taken debuff`)
- Bonnie (100% `Damage taken debuff`)
- Cecia (100% `Damage taken debuff`)

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

- Untargetable (Mythic+) — Self — Start of Battle
- Charm — Single target — `medium`

## Mikola

### Mikola's behavior

- Signature skill: Dauntless Hymn (ultimate) — haste + DEF aura zone
- Movement: moving (avg attack range 2.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, heal `medium`, buffs `medium`, damage `low`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `low`

### Units Mikola benefits from

Look for units providing: `ATK` `Haste` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Lyca**.

- **Velara**
  - Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]

### Units benefitting from Mikola

**74** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Perseus
- Silven
- Hepler
- Seth
- Sylphira
- Tasi
- Vala
- Atalanta
- Koko
- Lumont

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

- ATK buff — Multiple targets — `medium`
- Haste buff — Multiple targets — `high`
- Healing — Multiple targets — `high`
- Vitality buff (Mythic+) — Multiple targets — `low`

#### Crowd Control provided by Mikola

- Unaffected (Supreme+) — Self — Conditional

## Mirael

### Mirael's behavior

- Signature skill: Winged Flame (ultimate) — area fire barrage
- Movement: stationary (avg attack range 10.1 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `high`
- Non-ultimate: speed `fast`, debuffs `medium`, damage `high`

### Units Mirael benefits from

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Lyca**, **Twins**, or **Hugin**.

- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Mirael

**Similar Skills**

- Gwyneth (80% `dot-specialist` `fire-attack`)
- Satrana (66% `dot-specialist` `fire-attack`)

**Damage**

- Arden (100% `Magic` `DoT`)
- Berial (100% `Magic` `DoT`)
- Bonnie (100% `Magic` `DoT`)

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

- Signature skill: Phantom Chains — pull enemy to self
- Movement: mostly stationary (pulls enemies)

#### Skill overview

- Signature skill: speed `fast`
- Ultimate: speed `fast`, damage `medium`
- Non-ultimate: speed `fast`, heal `medium`, damage `low`
- True damage: Max HP-based damage `medium`, True damage `medium`

### Units Nara benefits from

Look for units providing: `ATK` `Energy`  
Common buffers are **Rowan** or **Lyca**.

- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
- **Smokey & Meerky**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, low) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
- **Thador**
  - Energy recovery (single target, low) [signature fuel]

### Units that can act as a replacement for Nara

**Buffs on allies**

- Antandra (100% `Healing`)
- Evie (100% `Healing`)
- Fay (100% `Healing`)

**Damage**

- Korin (100% `Max HP-based damage` `True damage` `Physical`)
- Shadewing (100% `Max HP-based damage` `True damage`)
- Indris (86% `Max HP-based damage` `True damage` `Physical`)

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
- True damage — Single target — `medium`

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

- Signature skill: Lightning Fire Dragon's Roar/Fire Dragon King's Roar (ultimate) — high-damage elemental beam
- Movement: stationary (avg attack range 11.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `normal`, damage `high`
- Non-ultimate: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`
- True damage: Max HP-based damage `medium`

### Units Natsu benefits from

Look for units providing: `ATK` `Haste` `CRIT` `CRIT DMG Boost`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units benefitting from Natsu

- Indris
- Bonnie

### Units that can act as a replacement for Natsu

**Damage**

- Daimon (100% `Max HP-based damage` `Magic` `DoT`)
- Satrana (100% `Max HP-based damage` `Magic` `DoT`)
- Shadewing (100% `Max HP-based damage` `Magic` `DoT`)

**Debuffs on enemies**

- Alna (72% `Haste debuff`)

**Crowd Control**

- Antandra (100% `Stun` `Knock down`)
- Lucca (100% `Stun` `Knock down`)
- Zorya (100% `Stun` `Knock down`)

### Summary for Natsu

#### Damage types dealt by Natsu

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Single target
- Max HP-based damage — Area — `medium`

#### Debuffs provided by Natsu

- Haste debuff — Area — `high`
- Max HP debuff (Mythic+) — Single target — `medium`
- DoT (Supreme+) — Single target — `low`

#### Crowd Control provided by Natsu

- Knock down — Area — `low`
- Stun — Single target — `medium`

## Nazrik

### Nazrik's behavior

- Signature skill: Rend Rupture (ultimate) — HP-drain bleed DoT
- Movement: stationary (avg attack range 10.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `normal`, damage `high`
- Non-ultimate: speed `fast`, debuffs `medium`, damage `medium`
- True damage: True damage `high`

### Units Nazrik benefits from

Look for units providing: `CRIT`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Nazrik

**Damage**

- Athalia (100% `True damage` `Physical`)
- Baelran (100% `True damage` `Physical`)
- Dionel (100% `True damage` `Physical`)

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

- Signature skill: Drowning Doom (ultimate) — pull + submerge enemies
- Movement: mostly stationary (avg attack range 4.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `medium`
- Non-ultimate: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

### Units Nerion benefits from

Look for units providing: `ATK SPD / Haste` `Max HP` `Energy` `DEF Penetration`  
Common buffers are **Twins**, **Lorsan**, or **Lyca**.

- **Tasi**
  - Enables CC on enemies via Sleep (all units, high)
- **Hepler**
  - ATK SPD via Haste buff (single target, low) [signature fuel]
  - Max HP via Shield (multiple targets, medium)
  - Enables CC on enemies via Blind (area, high)
- **Zandrok**
  - ATK SPD via Haste buff (area, low, conditional (frequent)) [signature fuel]
  - Enables CC on enemies via Stun (area, high)
- **Kordan**
  - DEF Penetration buff (multiple targets, low)
  - Enables CC on enemies via Bind (area, high)
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
  - Enables CC on enemies via Knock down (multiple targets, high)

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

- Signature skill: Soul Shepherd (ultimate) — save ally from fatal blow
- Movement: stationary (no finite attack range)

#### Skill overview

- Signature skill (ultimate): speed `slow`, heal `medium`
- Non-ultimate: speed `fast`, heal `medium`, damage `medium`
- True damage: HP loss `low`

### Units Niru benefits from

Look for units providing: `Healing` `Physical DEF` `Magic DEF`  
Common buffers are **Rowan**, **Lyca**, or **Mikola**.

- **Fay**
  - Healing (arc, high, conditional (frequent))
  - DEF buff (multiple targets, low)
  - DEF buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Velara**
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Hewynn**
  - Healing (all units, medium)
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]

### Units that can act as a replacement for Niru

**Damage**

- Dunlingr (100% `Magic` `HP loss`)
- Shadewing (100% `Magic` `HP loss`)
- Talene (100% `Magic` `HP loss`)

### Summary for Niru

#### Niru Provides

- Spirit form protection — Single target
- Start-of-battle cast (Mythic+) — All units

#### Niru Requires

- Ally blessing active — Allies
- Enemy defeat — Allies

#### Damage types dealt by Niru

- Primary damage type (unit): **Magic**
- Magic — All units, Self, Single target
- HP loss — Single target — `low`

## Odie

### Odie's behavior

- Signature skill: Heart Crusher — instantly defeat below poison threshold
- Movement: mostly stationary (avg attack range 5.0 tiles)

#### Skill overview

- Signature skill: speed `fast`, debuffs `medium`
- Ultimate: speed `slow`, debuffs `medium`, damage `low`
- Non-ultimate: speed `fast`, debuffs `medium`, damage `low`

### Units Odie benefits from

Look for units providing: `ATK SPD / Haste` `Energy`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Odie

**Damage**

- Arden (100% `DoT` `Magic`)
- Berial (100% `DoT` `Magic`)
- Bonnie (100% `DoT` `Magic`)

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

- Signature skill: Boxed Blessing — pull ally into box at start
- Movement: stationary (no finite attack range)
- Ally composition: rearmost ally enters invincible box, then gains Energy and ATK

#### Skill overview

- Signature skill: speed `fast`, buffs `medium`
- Ultimate: speed `slow`, debuffs `medium`, damage `high`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `medium`

### Units Pandora benefits from

Look for units providing: `Energy`  
Common buffers are **Rowan** or **Lyca**.

- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
- **Smokey & Meerky**
  - Energy recovery (multiple targets, low) [signature fuel]
- **Thador**
  - Energy recovery (single target, low) [signature fuel]

### Units benefitting from Pandora

- Indris
- Chippy
- Satrana
- Nara
- Scarlita

### Units that can act as a replacement for Pandora

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
- Max HP buff (Legendary+) — Single target — `low`

#### Debuffs provided by Pandora

- ATK debuff — Single target — `low`
- Damage taken debuff — Single target — `low`
- Energy drain — Single target — `low`
- Haste debuff — Single target — `medium`
- Vitality debuff — Single target — `high`

## Pang

### Pang's behavior

- Signature skill: Sky Splitter (ultimate) — area knockdown burst
- Movement: moving (avg attack range 1.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, buffs `medium`, damage `high`
- Non-ultimate: speed `fast`, buffs `medium`, damage `medium`

### Units Pang benefits from

Look for units providing: `ATK` `Haste` `Energy` `DEF Penetration`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

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

- Unaffected — Self — On Skill
- Stun — Area — `low`

## Parisa

### Parisa's behavior

- Signature skill: Floral Splendor (ultimate) — mark + AoE burst damage
- Movement: mostly stationary (avg attack range 5.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `high`
- Non-ultimate: speed `fast`, buffs `medium`, damage `low`

### Units Parisa benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `Energy`  
Common buffers are **Lyca**, **Twins**, or **Hugin**.

- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) [signature fuel]

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

- Signature skill: Divine Rend (ultimate) — march + continuous knockback
- Movement: moving (avg attack range 2.9 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `high`
- Non-ultimate: speed `fast`, buffs `medium`, damage `high`
- True damage: True damage `low`

### Units Perseus benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `Max HP`  
Common buffers are **Twins**, **Lyca**, or **Koko**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Enables Ally stat buffs via 2 ally stat buffs (start of battle)
- **Cecia**
  - ATK SPD buff (single target, low) [signature fuel]
  - Max HP buff (single target, high)
  - Enables Ally stat buffs via 4 ally stat buffs
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
  - Enables Ally stat buffs via 5 ally stat buffs
- **Velara**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Enables Ally stat buffs via 2 ally stat buffs (start of battle)
- **Pandora**
  - Max HP buff (single target, low)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
  - Enables Ally stat buffs via 4 ally stat buffs (start of battle)

### Units that can act as a replacement for Perseus

**Buffs on allies**

- Aliceth (100% `ATK`)
- Evie (100% `ATK`)
- Hugin (100% `ATK`)

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

- Unaffected — Multiple targets — Conditional
- Knock back — Area — `low`
- Stun — Area — `medium`

## Phraesto

### Phraesto's behavior

- Signature skill: Crimson Contract — buff two allies at battle start
- Movement: moving (avg attack range 1.8 tiles)
- Ally composition: place allies 1 tile behind this hero and the Illusion for contract buffs
- Self placement: keep this hero and Illusion in the same row (damage reduction and battle-start shields)

#### Skill overview

- Signature skill: speed `slow`, buffs `medium`, damage `low`
- Ultimate: speed `slow`, damage `high`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `high`

### Units Phraesto benefits from

Look for units providing: `Healing` `Energy`  
Common buffers are **Koko**, **Lorsan**, or **Mikola**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Evie**
  - Healing (multiple targets, high)

### Units that can act as a replacement for Phraesto

**Buffs on allies**

- Koko (75% `Max HP` `Damage taken reduction`)
- Twins (75% `Max HP`)
- Zanie (75% `Max HP`)

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
- Shield — Single target — `high`

#### Crowd Control provided by Phraesto

- Stun (Mythic+) — Single target — `low`
- Taunt (Mythic+) — Single target — `low`

## Pippa

### Pippa's behavior

- Signature skill: Chaos Manifest (ultimate) — reposition + random chaos
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill (ultimate): speed `normal`, damage `medium`
- Non-ultimate: speed `fast`, debuffs `medium`, damage `medium`
- True damage: True damage `low`

### Units Pippa benefits from

Look for units providing: `Haste`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Pippa

**Similar Skills**

- Kordan (100% `hp-scaling` `self-repositioner`)
- Athalia (66% `hp-scaling` `self-repositioner`)
- Marilee (66% `hp-scaling` `self-repositioner`)

**Damage**

- Sylphira (100% `Magic` `True damage` `Max HP-based damage`)
- Indris (99% `True damage` `Max HP-based damage`)
- Shadewing (91% `Magic` `Max HP-based damage` `True damage`)

**Debuffs on enemies**

- Lily May (100% `Energy drain`)
- Sinbad (75% `Energy drain`)
- Dunlingr (62% `Energy drain`)

**Crowd Control**

- Eironn (84% `Bind` `Displace`)
- Ulmus (84% `Bind` `Knock down`)
- Ravion (72% `Displace` `Knock down`)

### Summary for Pippa

#### Damage types dealt by Pippa

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target
- Max HP-based damage — Single target — `low`
- True damage — Area — `low`

#### Debuffs provided by Pippa

- Energy drain — Area — `medium`

#### Crowd Control provided by Pippa

- Unaffected — Self — On Skill
- Bind — Single target — `medium`
- Displace — Single target — `low`
- Knock down — Single target — `low`

## Ravion

### Ravion's behavior

- Signature skill: Killer Flush (ultimate) — multi-hit lost-HP scaling
- Movement: high movement (repositioning skills)
- Ally composition: Objectives go to the 2 rearmost allies; backline heroes receive ATK and Energy on completion

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `low`
- Non-ultimate: speed `fast`, buffs `medium`, debuffs `medium`, damage `medium`
- True damage: HP loss `low`

### Units Ravion benefits from

Look for units providing: `ATK` `Haste` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units benefitting from Ravion

**13** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Carolina
- Aliceth
- Arden
- Hodgkin
- Cryonaia
- Hewynn
- Lily May
- Valen
- Nara
- Chippy

### Units that can act as a replacement for Ravion

**Similar Skills**

- Hugin (66% `ally-shielder` `energy-provider`)

**Damage**

- Aliceth (100% `Physical` `HP loss`)
- Faramor (100% `Physical` `HP loss`)
- Kordan (100% `Physical` `HP loss`)

**Debuffs on enemies**

- Lyca (100% `ATK debuff` `Phys DEF debuff`)
- Sinbad (100% `ATK debuff` `Phys DEF debuff`)

### Summary for Ravion

#### Ravion Provides

- Position swap (Mythic+) — Multiple targets

#### Ravion Requires

- Boss encounter — Allies

#### Damage types dealt by Ravion

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- HP loss — Single target — `low`

#### Buffs provided by Ravion

- ATK buff — Multiple targets — `medium`
- Energy recovery — Multiple targets — `medium`
- Lifedrain buff (Mythic+) — Single target — `low` — conditional (rare)
- Shield (Mythic+) — Multiple targets — `low` — conditional (rare)

#### Debuffs provided by Ravion

- ATK debuff — Multiple targets — `medium`
- Phys DEF debuff — Multiple targets — `medium`

#### Crowd Control provided by Ravion

- Unaffected — Self — Conditional
- Displace — Multiple targets — `high`
- Knock down — Multiple targets — `high`

## Reinier

### Reinier's behavior

- Signature skill: Dynamic Balance — swap ally+enemy positions at start
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill: speed `fast`, heal `medium`, damage `high`
- Ultimate: speed `slow`, damage `high`
- Non-ultimate: speed `fast`, heal `medium`, debuffs `medium`, damage `high`

### Units Reinier benefits from

Look for units providing: `Healing`  
Common buffers are **Koko**, **Lorsan**, or **Mikola**.

- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Evie**
  - Healing (multiple targets, high)
- **Ludovic**
  - Healing (area, medium)
- **Velara**
  - Healing (area, medium)

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
- Interrupt — All units — `high`
- Knock up — All units — `low`
- Knock down (Mythic+) — Single target — `low`

## Rhys

### Rhys's behavior

- Signature skill: Flame Barrage (ultimate) — ranged fire barrage
- Movement: high movement (moves while attacking)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `medium`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

### Units Rhys benefits from

Look for units providing: `ATK SPD / Haste` `CRIT` `CRIT DMG Boost` `Healing`  
Common buffers are **Lyca**, **Twins**, or **Mikola**.

- **Velara**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Fay**
  - ATK SPD buff (multiple targets, low) [signature fuel]
  - Healing (arc, high, conditional (frequent))

### Units that can act as a replacement for Rhys

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Atalanta (100% `Knock back`)
- Cassadee (100% `Knock back`)
- Harak (100% `Knock back`)

### Summary for Rhys

#### Damage types dealt by Rhys

- Primary damage type (unit): **Physical**
- Physical — Arc, Single target

#### Buffs provided by Rhys

- Healing — Single target — `medium`
- Movement speed buff (Mythic+) — Single target — `high`

#### Crowd Control provided by Rhys

- Knock back — Single target — `high`

## Rowan

### Rowan's behavior

- Signature skill: Fatal Greed (ultimate) — AoE energy recovery burst
- Movement: moving (repositions on cast)

#### Skill overview

- Signature skill (ultimate): speed `normal`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `low`

### Units Rowan benefits from

Look for units providing: `Haste` `Healing` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Velara**
  - Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Hewynn**
  - Healing (all units, medium)
- **Fay**
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]

### Units benefitting from Rowan

**57** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Granny Dahnie
- Zorya
- Antandra
- Lenya
- Shemira
- Temesia
- Cecia
- Niru
- Arden
- Hodgkin

### Units that can act as a replacement for Rowan

**Similar Skills**

- Twins (66% `ally-healer` `energy-provider`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Debuffs on enemies**

- Berial (100% `Energy drain`)
- Dunlingr (100% `Energy drain`)
- Hodgkin (100% `Energy drain`)

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
- DEF buff (Mythic+) — Single target — `high`
- Max HP buff (Mythic+) — Single target — `high`

#### Debuffs provided by Rowan

- Energy drain — Single target — `medium`

## Saida

### Saida's behavior

- Signature skill: Seed Siphon (ultimate) — pin + energy drain + seed
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill (ultimate): speed `fast`, debuffs `medium`, damage `high`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `high`

### Units Saida benefits from

Look for units providing: `Max HP` `Healing`  
Common buffers are **Koko**, **Lorsan**, or **Hugin**.

- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Evie**
  - Healing (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
  - Healing (single target, high)

### Units benefitting from Saida

- Daimon
- Eironn
- Silvina
- Thoran

### Units that can act as a replacement for Saida

**Buffs on allies**

- Hugin (100% `Max HP`)
- Lucius (100% `Max HP`)
- Callan (66% `Max HP`)

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
- Magic — All units, Area, Multiple targets, Self, Single target

#### Buffs provided by Saida

- Healing — Single target — `medium`
- Shield — Multiple targets — `high`

#### Debuffs provided by Saida

- Energy drain — Single target — `high`

#### Crowd Control provided by Saida

- Unaffected — Self — Conditional
- Displace — Single target — `low`
- Interrupt — Area — `low`

## Salazer

### Salazer's behavior

- Signature skill: Rain of Blades (ultimate) — area blade storm
- Movement: moving (avg attack range 1.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, buffs `medium`, damage `low`
- Non-ultimate: speed `fast`, damage `low`

### Units Salazer benefits from

Look for units providing: `Max HP` `Healing`  
Common buffers are **Twins**, **Lyca**, or **Rowan**.

- **Pandora**
  - Max HP buff (single target, low)
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Velara**
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)
- **Fay**
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]

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
- Physical — Self, Single target

#### Buffs provided by Salazer

- Lifedrain buff — Single target — `low`
- Shield (Supreme+) — Single target — `low` — conditional (frequent)

#### Crowd Control provided by Salazer

- Bind — Self — `low`

## Satrana

### Satrana's behavior

- Signature skill: Fiery Dance (ultimate) — area fire burn damage
- Movement: moving (avg attack range 1.5 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, buffs `medium`, damage `medium`
- Non-ultimate: speed `fast`, buffs `medium`, debuffs `medium`, damage `low`
- True damage: Max HP-based damage `high`

### Units Satrana benefits from

- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]

### Units that can act as a replacement for Satrana

**Buffs on allies**

- Koko (100% `Damage taken reduction`)
- Shakir (100% `Damage taken reduction`)
- Soren (100% `Damage taken reduction`)

**Similar Skills**

- Mirael (66% `dot-specialist` `fire-attack`)

**Damage**

- Brutus (100% `Max HP-based damage` `DoT`)
- Daimon (94% `Max HP-based damage` `DoT` `Magic`)
- Shadewing (93% `Max HP-based damage` `Magic` `DoT`)

**Debuffs on enemies**

- Sinbad (100% `Vitality debuff`)
- Frieren (90% `Vitality debuff`)
- Pandora (90% `Vitality debuff`)

**Crowd Control**

- Mehira (100% `Charm`)

### Summary for Satrana

#### Satrana Provides

- Ally DoT on enemies — All units
- Ally Vitality debuff on enemies — All units
- Ally grant (Sparks) — All units
- Invincibility — Self

#### Damage types dealt by Satrana

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Single target
- DoT — All units
- Max HP-based damage — All units, Arc — `high`

#### Buffs provided by Satrana

- Damage taken reduction (Legendary+) — Single target — `medium`

#### Debuffs provided by Satrana

- Vitality debuff — All units — `low`

#### Crowd Control provided by Satrana

- Charm — Single target — `high`

## Scarlita

### Scarlita's behavior

- Signature skill: Divine Wrath — instantly defeat low-HP enemies
- Movement: moving (brief reposition)

#### Skill overview

- Signature skill: speed `fast`, damage `medium`
- Ultimate: speed `slow`, damage `high`
- Non-ultimate: speed `fast`, buffs `medium`, damage `medium`
- True damage: True damage `medium`

### Units Scarlita benefits from

Look for units providing: `Execution` `Energy`  
Common buffers are **Rowan** or **Lyca**.

- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
- **Smokey & Meerky**
  - Energy recovery (multiple targets, low) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
- **Thador**
  - Energy recovery (single target, low) [signature fuel]

### Units that can act as a replacement for Scarlita

**Buffs on allies**

- Callan (100% `Max HP`)
- Contess (100% `Max HP`)
- Daimon (100% `Max HP`)

**Similar Skills**

- Korin (66% `ally-shielder` `hp-scaling`)

**Damage**

- Athalia (100% `Physical` `True damage`)
- Baelran (100% `True damage` `Physical`)
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
- Physical — All units, Arc, Area, Multiple targets, Single target
- True damage — Multiple targets — `medium`

#### Buffs provided by Scarlita

- Shield — Single target — `medium`

#### Crowd Control provided by Scarlita

- Unaffected — Self — Conditional
- Knock back — All units — `low`
- Knock down — Arc — `low`
- Knock up — Area — `medium`
- Stun — Single target — `medium`

## Seth

### Seth's behavior

- Signature skill: Shadow Strike (ultimate) — multi-hit shadow burst
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill (ultimate): speed `slow`, heal `medium`, buffs `medium`, damage `low`
- Non-ultimate: speed `fast`, buffs `medium`, damage `low`

### Units Seth benefits from

Look for units providing: `ATK` `Haste` `CRIT` `Healing` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Velara**
  - Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
  - Lifedrain buff (single target, medium)
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]

### Units that can act as a replacement for Seth

**Buffs on allies**

- Brutus (60% `Life Drain`)
- Koko (60% `Life Drain`)
- Kordan (60% `Life Drain`)

**Similar Skills**

- Harak (66% `assassin` `life-drain`)

**Damage**

- Aliceth (100% `Physical`)
- Faramor (100% `Physical`)
- Harak (100% `Physical`)

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

- Signature skill: Withering Curse — convert DoT to burst damage
- Movement: moving (avg attack range 1.0 tiles)

#### Skill overview

- Signature skill: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`
- Ultimate: speed `slow`, damage `low`
- Non-ultimate: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`
- True damage: HP loss `low`, Max HP-based damage `high`, True damage `low`

### Units Shadewing benefits from

Look for units providing: `ATK` `Max HP` `Energy` `Life Drain`  
Common buffers are **Lyca**, **Rowan**, or **Koko**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Enables Debuff on target via DoT (all units)
  - Enables Continuous damage on enemies via Burn
- **Alna**
  - ATK buff (single target, medium)
  - Max HP buff (single target, low)
  - Enables Debuff on target via Haste debuff (area)
  - Enables Continuous damage on enemies via DoT
- **Lucius**
  - Max HP via Shield (area, high)
  - Enables Debuff on target via ATK debuff (area)
- **Cecia**
  - Max HP buff (single target, high)
  - Lifedrain buff (area, high)
  - Enables Debuff on target via Damage taken debuff (single target)
  - Enables Continuous damage on enemies via DoT
- **Frieren**
  - Enables Debuff on target via DoT (area)
  - Enables Continuous damage on enemies via DoT + Burn

### Units that can act as a replacement for Shadewing

**Similar Skills**

- Nerion (100% `dot-specialist` `enemy-debuffer`)

**Damage**

- Nara (66% `Max HP-based damage` `True damage`)

**Debuffs on enemies**

- Eironn (100% `Magic DEF debuff`)
- Sinbad (100% `Magic DEF debuff`)
- Carolina (96% `Magic DEF debuff`)

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

- Magic DEF debuff — All units — `low`

## Shakir

### Shakir's behavior

- Signature skill: Ravaging Claws (ultimate) — single-target charge damage
- Movement: moving (avg attack range 1.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `normal`, buffs `medium`, damage `medium`
- Non-ultimate: speed `fast`, buffs `medium`, damage `low`

### Units Shakir benefits from

Look for units providing: `Haste`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Velara**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units benefitting from Shakir

- Aurora
- Natsu
- Hugin
- Pippa

### Units that can act as a replacement for Shakir

**Buffs on allies**

- Koko (72% `Damage taken reduction` `Life Drain`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Alna (100% `Vitality debuff`)
- Dionel (100% `Vitality debuff`)
- Frieren (100% `Vitality debuff`)

**Crowd Control**

- Baelran (100% `Knock up`)
- Dionel (100% `Knock up`)
- Florabelle (100% `Knock up`)

### Summary for Shakir

#### Shakir Provides

- Transformation — Self

#### Shakir Requires

- Form or stance active — Enemies

#### Damage types dealt by Shakir

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Multiple targets, Single target

#### Buffs provided by Shakir

- Damage taken reduction — Multiple targets — `medium`
- Haste buff — Multiple targets — `medium`
- Lifedrain buff — Single target — `medium`

#### Debuffs provided by Shakir

- Vitality debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Shakir

- Unaffected — Self — Form
- Knock up — Area — `low`

## Shemira

### Shemira's behavior

- Signature skill: Phantom Procession (ultimate) — sustained area ghost damage
- Movement: mostly stationary (avg attack range 4.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, heal `medium`, damage `low`
- Non-ultimate: speed `fast`, buffs `medium`, damage `high`
- True damage: Max HP-based damage `high`

### Units Shemira benefits from

Look for units providing: `Max HP` `Healing` `Energy`  
Common buffers are **Rowan**, **Twins**, or **Lyca**.

- **Pandora**
  - Max HP buff (single target, low)
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Velara**
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)

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

- Signature skill: Gravity Collapse — stack marks + detonate stun
- Movement: stationary (avg attack range 12.0 tiles)

#### Skill overview

- Signature skill: speed `fast`, damage `low`
- Ultimate: speed `fast`, damage `low`
- Non-ultimate: speed `fast`, buffs `medium`, damage `low`
- True damage: True damage `low`

### Units Silven benefits from

Look for units providing: `ATK SPD / Haste` `Energy` `DEF Penetration` `Physical DEF`  
Common buffers are **Twins**, **Koko**, or **Lyca**.

- **Evie**
  - Enables Ally stat buffs via 2 ally stat buffs (start of battle)
- **Cecia**
  - ATK SPD buff (single target, low) [signature fuel]
  - DEF Penetration buff (single target, medium)
  - Enables Ally stat buffs via 4 ally stat buffs
- **Fay**
  - ATK SPD buff (multiple targets, low) [signature fuel]
  - DEF buff (multiple targets, low)
  - Enables Ally stat buffs via 5 ally stat buffs
- **Velara**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Enables Ally stat buffs via 2 ally stat buffs (start of battle)
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
  - Enables Ally stat buffs via 3 ally stat buffs

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

- Signature skill: Shadow Slayer (ultimate) — stealth + execute burst
- Movement: moving (avg attack range 1.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `normal`, debuffs `medium`, damage `medium`
- Non-ultimate: speed `fast`, buffs `medium`, damage `medium`

### Units Silvina benefits from

Look for units providing: `Max HP` `CRIT`  
Common buffers are **Twins**, **Hugin**, or **Lyca**.

- **Lucius**
  - Max HP via Shield (area, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Gala**
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
  - ATK SPD via Haste buff (single target, low) [signature fuel]
- **Callan**
  - Max HP via Shield (multiple targets, medium)

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

- Signature skill: Whizzing Edge (ultimate) — multi-hit physical slashes
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill (ultimate): speed `normal`, damage `low`
- Non-ultimate: speed `fast`, debuffs `medium`, damage `low`

### Units Sinbad benefits from

Look for units providing: `ATK SPD / Haste` `Energy`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units benefitting from Sinbad

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

- Damage taken debuff — Single target — `low`
- ATK debuff (Mythic+) — Single target — `high`
- Energy drain (Mythic+) — Multiple targets — `medium`
- Magic DEF debuff (Mythic+) — Multiple targets — `medium`
- Phys DEF debuff (Mythic+) — Multiple targets — `medium`
- Vitality debuff (Mythic+) — Multiple targets — `high`

#### Crowd Control provided by Sinbad

- Unaffected — Multiple targets — Conditional

## Smokey & Meerky

### Smokey & Meerky's behavior

- Signature skill: Special Aroma (ultimate) — heal aura + upgradeable zone
- Movement: stationary (no finite attack range)

#### Skill overview

- Signature skill (ultimate): speed `slow`, heal `medium`, buffs `medium`, damage `medium`
- Non-ultimate: speed `fast`, heal `medium`, damage `low`

### Units Smokey & Meerky benefits from

Look for units providing: `ATK` `Healing` `Energy`  
Common buffers are **Koko**, **Lorsan**, or **Mikola**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)

### Units benefitting from Smokey & Meerky

- Nara
- Pandora
- Scarlita

### Units that can act as a replacement for Smokey & Meerky

**Buffs on allies**

- Mikola (90% `Healing` `ATK`)
- Evie (75% `Healing` `ATK`)
- Fay (75% `Healing` `ATK`)

**Similar Skills**

- Fay (100% `ally-healer` `aoe-healing`)
- Hewynn (100% `ally-healer` `aoe-healing`)
- Ludovic (100% `ally-healer` `aoe-healing`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Crowd Control**

- Reinier (88% `Interrupt`)

### Summary for Smokey & Meerky

#### Damage types dealt by Smokey & Meerky

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target

#### Buffs provided by Smokey & Meerky

- Energy recovery — Multiple targets — `low`
- Healing — Multiple targets — `medium`
- ATK buff (Legendary+) — Multiple targets — `low`

#### Crowd Control provided by Smokey & Meerky

- Interrupt — Area — `medium`
- Stun (Mythic+) — Single target — `low`

## Solise

### Solise's behavior

- Signature skill: Life's Embrace (ultimate) — AoE healing waves
- Movement: stationary (no finite attack range)

#### Skill overview

- Signature skill (ultimate): speed `normal`, heal `medium`, damage `medium`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

### Units Solise benefits from

Look for units providing: `ATK` `Healing`  
Common buffers are **Mikola**, **Hugin**, or **Koko**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Velara**
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Smokey & Meerky**
  - ATK buff (multiple targets, low)
  - Healing (multiple targets, medium)
  - Energy recovery (multiple targets, low) [signature fuel]
- **Hewynn**
  - Healing (all units, medium)

### Units that can act as a replacement for Solise

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

- Shield — Summons only — `medium`

#### Crowd Control provided by Solise

- Unaffected — Self — On Skill

## Sonja

### Sonja's behavior

- Signature skill: Crimson Covenant — ATK + DEF buff two flanking allies
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill: speed `fast`, buffs `medium`
- Ultimate: speed `slow`, damage `medium`
- Non-ultimate: speed `fast`, buffs `medium`, damage `medium`

### Units Sonja benefits from

Look for units providing: `Haste` `Max HP`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Lucius**
  - Max HP via Shield (area, high)
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Hepler**
  - Haste buff (single target, low) [signature fuel]
  - Max HP via Shield (multiple targets, medium)

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

- Stun — Single target — `low`

## Soren

### Soren's behavior

- Signature skill: Whirlwind Swing (ultimate) — knockback + collision stun
- Movement: moving (avg attack range 1.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `high`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

### Units Soren benefits from

Look for units providing: `Haste` `Healing` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Velara**
  - Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]

### Units that can act as a replacement for Soren

**Buffs on allies**

- Koko (100% `Damage taken reduction` `Max HP`)
- Shakir (90% `Damage taken reduction`)
- Satrana (60% `Damage taken reduction`)

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
- Physical — Area, Multiple targets, Self, Single target

#### Buffs provided by Soren

- Damage taken reduction — Single target — `high`
- Haste buff (Legendary+) — Single target — `low`
- Shield (Supreme+) — Single target — `low`

#### Crowd Control provided by Soren

- Knock back — Single target — `high`
- Stun — Single target — `medium`

## Sylphira

### Sylphira's behavior

- Signature skill: Grand Finale (ultimate) — beat stacking + song DoT
- Movement: moving (avg attack range 1.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, buffs `medium`, debuffs `medium`, damage `high`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `high`
- True damage: True damage `high`

### Units Sylphira benefits from

Look for units providing: `ATK` `Haste` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Velara**
  - Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]

### Units that can act as a replacement for Sylphira

**Damage**

- Indris (85% `True damage` `Max HP-based damage`)
- Pippa (83% `Magic` `True damage` `Max HP-based damage`)
- Shadewing (81% `Magic` `Max HP-based damage` `True damage`)

**Crowd Control**

- Temesia (60% `Knock down` `Interrupt`)

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

- Immune — Self — On Skill
- Unaffected — Area — Conditional
- Cleanse (Mythic+) — Self — On Skill
- Interrupt — Area — `low`
- Knock down — Area — `medium`
- Silence — Area — `low`

## Talene

### Talene's behavior

- Signature skill: Divine Conflagration (ultimate) — sustained channelled flame beam
- Movement: moving (avg attack range 3.0 tiles)
- Ally composition: frontmost ally carries Pyre of Renewal (AoE damage and healing)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `high`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `medium`
- True damage: HP loss `high`

### Units Talene benefits from

Look for units providing: `ATK` `Max HP` `Healing` `Life Drain`  
Common buffers are **Koko**, **Lorsan**, or **Mikola**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Cecia**
  - Max HP buff (single target, high)
  - Lifedrain buff (area, high)
- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))

### Units that can act as a replacement for Talene

**Damage**

- Dunlingr (100% `HP loss` `Magic`)
- Zorya (93% `HP loss` `Magic`)
- Aliceth (86% `HP loss`)

**Crowd Control**

- Atalanta (100% `Knock back`)
- Cassadee (100% `Knock back`)
- Harak (100% `Knock back`)

### Summary for Talene

#### Talene Provides

- Transformation — Self
- Stacking buff (Mythic+) — Area

#### Damage types dealt by Talene

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- HP loss — All units, Single target — `high`

#### Crowd Control provided by Talene

- Knock back — Area — `low`

## Tasi

### Tasi's behavior

- Signature skill: Eternal Dreamscape (ultimate) — sleep all enemies
- Movement: stationary (avg attack range 10.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `medium`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `high`

### Units Tasi benefits from

Look for units providing: `ATK` `Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Velara**
  - Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]

### Units benefitting from Tasi

- Nerion
- Carolina

### Units that can act as a replacement for Tasi

**Similar Skills**

- Marilee (66% `mass-cc` `self-repositioner`)

**Damage**

- Cryonaia (100% `DoT` `Magic`)
- Frieren (100% `DoT` `Magic`)
- Lorsan (100% `Magic` `DoT`)

### Summary for Tasi

#### Tasi Provides

- Invincibility — Area
- Sleep (area) — Single target
- Transformation — Self

#### Damage types dealt by Tasi

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — All units, Area, Single target

#### Buffs provided by Tasi

- Haste buff (Mythic+) — Single target — `high`

#### Crowd Control provided by Tasi

- Sleep — Single target — `high`
- Stun — Area — `high`

## Temesia

### Temesia's behavior

- Signature skill: Knight's Heart (ultimate) — constant charge + knockdown through enemies
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill (ultimate): speed `slow`, buffs `medium`, damage `high`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `low`

### Units Temesia benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `Max HP` `Healing` `Energy`  
Common buffers are **Twins**, **Lyca**, or **Mikola**.

- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Velara**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
  - Healing (arc, high, conditional (frequent))
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]

### Units that can act as a replacement for Temesia

**Similar Skills**

- Cassadee (60% `aoe-damage` `enemy-debuffer`)

**Damage**

- Korin (100% `Physical` `Max HP-based damage`)
- Indris (95% `Physical` `Max HP-based damage`)
- Nara (83% `Max HP-based damage` `Physical`)

**Debuffs on enemies**

- Atalanta (100% `Phys DEF debuff`)
- Brutus (100% `Phys DEF debuff`)
- Fay (100% `Phys DEF debuff`)

**Crowd Control**

- Sylphira (100% `Knock down` `Interrupt`)
- Lucca (90% `Knock down` `Interrupt`)
- Antandra (62% `Knock down`)

### Summary for Temesia

#### Temesia Provides

- Stacking buff — Single target
- Invincibility (Mythic+) — Self

#### Damage types dealt by Temesia

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target
- Max HP-based damage — Single target — `medium`
- True damage — Self

#### Buffs provided by Temesia

- Healing over time (Mythic+) — Single target — `low`

#### Debuffs provided by Temesia

- Phys DEF debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Temesia

- Unaffected (Mythic+) — Self — Permanent
- Interrupt — Single target — `high`
- Knock down — All units — `low`

## Thador

### Thador's behavior

- Signature skill: Darkmoon Pact — crit + shield for ally behind
- Movement: moving (avg attack range 0.2 tiles)
- Ally composition: place lieutenant 1 tile behind at battle prep (Crit + shared shields)

#### Skill overview

- Signature skill: speed `slow`, buffs `medium`, damage `medium`
- Ultimate: speed `slow`, damage `high`
- Non-ultimate: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

### Units Thador benefits from

Look for units providing: `Max HP` `CRIT` `Healing`  
Common buffers are **Twins**, **Koko**, or **Hugin**.

- **Velara**
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)
- **Fay**
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Antandra**
  - Healing (multiple targets, high)

### Units benefitting from Thador

- Pandora

### Units that can act as a replacement for Thador

**Buffs on allies**

- Lyca (100% `Energy`)
- Pandora (100% `Energy`)
- Ravion (100% `Energy`)

**Damage**

- Alna (100% `Physical` `DoT`)
- Brutus (100% `Physical` `DoT`)
- Cecia (100% `Physical` `DoT`)

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
- DoT — Single target

#### Buffs provided by Thador

- Energy recovery (EX+10) — Single target — `low`

#### Debuffs provided by Thador

- Magic DEF debuff (Mythic+) — Single target — `high`

#### Crowd Control provided by Thador

- Knock down — Single target — `high`

## Thoran

### Thoran's behavior

- Signature skill: Resurrection — self-revive on defeat
- Movement: moving (avg attack range 1.0 tiles)

#### Skill overview

- Signature skill: speed `fast`, heal `medium`
- Ultimate: speed `slow`, buffs `medium`, damage `low`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`

### Units Thoran benefits from

Look for units providing: `Max HP` `Energy`  
Common buffers are **Rowan**, **Hugin**, or **Koko**.

- **Lucius**
  - Max HP via Shield (area, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
- **Gala**
  - Max HP via Shield (single target, high)

### Units that can act as a replacement for Thoran

**Buffs on allies**

- Koko (100% `Healing` `Life Drain`)
- Ludovic (80% `Healing`)
- Nara (80% `Healing`)

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

- Healing — Single target — `medium`
- Lifedrain buff — Single target — `low` — conditional (frequent)

#### Crowd Control provided by Thoran

- Unaffected — Self — On Skill
- Interrupt — Single target — `low`

## Tilaya

### Tilaya's behavior

- Signature skill: Wrath of the Wilds (ultimate) — 8-hit greatsword arc slashes
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill (ultimate): speed `slow`, heal `medium`, buffs `medium`, damage `low`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `low`

### Units Tilaya benefits from

Look for units providing: `Max HP` `Healing`  
Common buffers are **Koko**, **Lorsan**, or **Hugin**.

- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Evie**
  - Healing (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)

### Units that can act as a replacement for Tilaya

**Buffs on allies**

- Himmel (100% `Max HP`)
- Twins (100% `Max HP`)

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

- Unaffected — Arc — Start of Battle

## Ulmus

### Ulmus's behavior

- Signature skill: Way of the Forest — HP regen + energy when rooted
- Movement: moving (stationary when rooted)
- Ally composition: when rooted, shields frontmost ally instead of self

#### Skill overview

- Signature skill: speed `fast`, heal `medium`
- Ultimate: speed `slow`, heal `medium`, damage `medium`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

### Units Ulmus benefits from

Look for units providing: `Max HP` `Healing` `Energy`  
Common buffers are **Koko**, **Lorsan**, or **Rowan**.

- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Evie**
  - Healing (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)

### Units that can act as a replacement for Ulmus

**Buffs on allies**

- Callan (100% `Max HP`)
- Contess (100% `Max HP`)
- Daimon (100% `Max HP`)

**Similar Skills**

- Pang (100% `ally-shielder` `transformation`)
- Hepler (66% `ally-shielder` `transformation`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Kordan (100% `Knock back` `Bind` `Knock down`)
- Indris (84% `Knock back` `Bind`)
- Atalanta (70% `Knock back` `Bind`)

### Summary for Ulmus

#### Ulmus Requires

- Vulnerable enemy (Mythic+) — Enemies

#### Damage types dealt by Ulmus

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Ulmus

- Shield — Single target — `low`

#### Crowd Control provided by Ulmus

- Unaffected — Self — On Skill
- Bind (Mythic+) — Single target — `medium`
- Knock down (Mythic+) — Single target — `medium`
- Knock back (Supreme+) — Area — `low`

## Vala

### Vala's behavior

- Signature skill: Swift Shift (ultimate) — mode shift + stun/true damage
- Movement: high movement (repositioning skills)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `medium`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, debuffs `medium`, damage `low`
- True damage: HP loss `low`, True damage `medium`

### Units Vala benefits from

Look for units providing: `ATK` `Haste` `Healing` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Velara**
  - Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Enables Enemy defeat via HP threshold strike

### Units that can act as a replacement for Vala

**Buffs on allies**

- Damian (100% `Haste`)
- Gala (100% `Haste`)
- Hugin (100% `Haste`)

**Damage**

- Faramor (100% `True damage` `Physical` `HP loss`)
- Shadewing (81% `HP loss` `True damage`)
- Korin (71% `True damage` `Physical`)

**Debuffs on enemies**

- Kafra (75% `Marked target (focus fire)` `Haste debuff`)

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
- HP loss — Single target — `low`
- True damage — Single target — `medium`

#### Buffs provided by Vala

- Haste buff (Mythic+) — Single target — `high`

#### Debuffs provided by Vala

- Haste debuff — Single target — `medium`
- Marked target (focus fire) — Single target — `medium`

#### Crowd Control provided by Vala

- Untargetable (Mythic+) — Multiple targets — Conditional
- Stun — Single target — `medium`

## Valen

### Valen's behavior

- Signature skill: Thunder Swordwork (ultimate) — multi-hit area + ATK buff
- Movement: moving (avg attack range 1.4 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, buffs `medium`, damage `low`
- Non-ultimate: speed `fast`, damage `medium`

### Units Valen benefits from

Look for units providing: `ATK`  
Common buffers are **Lyca**, **Rowan**, or **Twins**.

- **Ravion**
  - ATK buff (multiple targets, medium)
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]

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

- Signature skill: Blooming Terror (ultimate) — stack fear + consume enemy
- Movement: moving (avg attack range 1.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `fast`, heal `medium`, damage `high`
- Non-ultimate: speed `fast`, buffs `medium`, damage `medium`
- True damage: Max HP-based damage `low`

### Units Valka benefits from

Look for units providing: `ATK SPD / Haste` `Max HP` `Healing` `Energy`  
Common buffers are **Twins**, **Koko**, or **Lyca**.

- **Velara**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
  - Enables Adjacent allies via Multiple ally buffs
- **Fay**
  - ATK SPD buff (multiple targets, low) [signature fuel]
  - Healing (arc, high, conditional (frequent))
  - Enables Adjacent allies via Multiple ally buffs
- **Cecia**
  - ATK SPD buff (single target, low) [signature fuel]
  - Max HP buff (single target, high)
  - Enables Adjacent allies via Multiple ally buffs
- **Lucius**
  - Max HP via Shield (area, high)
  - Enables Adjacent allies via Shield (area)
- **Evie**
  - Healing (multiple targets, high)
  - Enables Adjacent allies via Multiple ally buffs

### Units benefitting from Valka

- Brutus

### Units that can act as a replacement for Valka

**Buffs on allies**

- Dunlingr (70% `ATK SPD` `Life Drain`)
- Lyca (66% `ATK SPD`)

**Damage**

- Brutus (100% `Physical` `Max HP-based damage`)
- Gunnar (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Crowd Control**

- Antandra (100% `Stun` `Knock down`)
- Lucca (100% `Stun` `Knock down`)
- Zorya (100% `Stun` `Knock down`)

### Summary for Valka

#### Valka Requires

- Adjacent allies — Allies

#### Damage types dealt by Valka

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- Max HP-based damage — Area — `low`

#### Buffs provided by Valka

- ATK SPD buff — Multiple targets — `high`
- Lifedrain buff (EX+10) — Single target — `high`
- Haste buff (Supreme+) — Single target — `low`

#### Crowd Control provided by Valka

- Unaffected — Self — On Skill
- Knock down — Area — `low`
- Stun — Area — `low`

## Velara

### Velara's behavior

- Signature skill: Ruthless Rite (ultimate) — transfer enemy stats to allies
- Movement: stationary (no finite attack range)

#### Skill overview

- Signature skill (ultimate): speed `slow`, heal `medium`, debuffs `medium`, damage `low`
- Non-ultimate: speed `fast`, buffs `medium`, debuffs `medium`, damage `high`

### Units Velara benefits from

Look for units providing: `Haste` `Max HP` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Lucius**
  - Max HP via Shield (area, high)
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Hepler**
  - Haste buff (single target, low) [signature fuel]
  - Max HP via Shield (multiple targets, medium)

### Units benefitting from Velara

- Mikola
- Sylphira
- Twins
- Viperian
- Rhys
- Rowan

### Units that can act as a replacement for Velara

**Buffs on allies**

- Mikola (100% `Healing` `Haste`)
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
- Bryon (100% `Haste debuff`)

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

- Haste debuff — Single target — `medium`

#### Crowd Control provided by Velara

- Bind — Single target — `high`

## Viperian

### Viperian's behavior

- Signature skill: Crimson Waltz — AoE burst damage to all enemies
- Movement: mostly stationary (avg attack range 5.0 tiles)

#### Skill overview

- Signature skill: speed `slow`, damage `medium`
- Ultimate: speed `normal`, heal `medium`, damage `high`
- Non-ultimate: speed `slow`, heal `medium`, debuffs `medium`, damage `medium`

### Units Viperian benefits from

Look for units providing: `Haste` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Velara**
  - Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

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

- Berial (100% `Energy drain`)
- Dunlingr (100% `Energy drain`)
- Hodgkin (100% `Energy drain`)

### Summary for Viperian

#### Damage types dealt by Viperian

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Debuffs provided by Viperian

- Energy drain — Single target — `medium`

#### Crowd Control provided by Viperian

- Unaffected — Self — Once

## Walker

### Walker's behavior

- Signature skill: Six-Shot (ultimate) — multi-target burst shots
- Movement: moving (avg attack range 2.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, damage `low`
- Non-ultimate: speed `fast`, buffs `medium`, debuffs `medium`, damage `low`
- True damage: HP loss `low`, Max HP-based damage `low`

### Units Walker benefits from

Look for units providing: `Max HP` `CRIT` `CRIT DMG Boost` `Life Drain`  
Common buffers are **Twins**, **Lyca**, or **Rowan**.

- **Cecia**
  - Max HP buff (single target, high)
  - Lifedrain buff (area, high)
  - ATK SPD buff (single target, low) [signature fuel]
- **Lucius**
  - Max HP via Shield (area, high)
- **Valka**
  - Lifedrain buff (single target, high)
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Pandora**
  - Max HP buff (single target, low)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Ravion**
  - Energy recovery (multiple targets, medium) [signature fuel]
  - Energy recovery (150 early objective, multiple targets) [signature fuel]

### Units that can act as a replacement for Walker

**Damage**

- Shadewing (77% `HP loss` `Max HP-based damage`)
- Gwyneth (73% `Physical` `Max HP-based damage`)
- Korin (73% `Physical` `Max HP-based damage`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Arden (100% `Stun`)

### Summary for Walker

#### Damage types dealt by Walker

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Self, Single target
- HP loss — Self, Single target — `low`
- Max HP-based damage — Single target — `low`

#### Debuffs provided by Walker

- Crit Resist debuff (Mythic+) — Single target — `low`

#### Crowd Control provided by Walker

- Stun — Single target — `medium`

## Zandrok

### Zandrok's behavior

- Signature skill: Rallying Roar — destroy obstacles + inspire allies
- Movement: moving (avg attack range 1.0 tiles)

#### Skill overview

- Signature skill: speed `fast`, buffs `medium`
- Ultimate: speed `slow`
- Non-ultimate: speed `fast`, buffs `medium`

### Units Zandrok benefits from

Look for units providing: `Haste` `Max HP` `Life Drain`  
Common buffers are **Twins**, **Hugin**, or **Koko**.

- **Cecia**
  - Max HP buff (single target, high)
  - Lifedrain buff (area, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Shakir**
  - Haste buff (multiple targets, medium) [signature fuel]
  - Lifedrain buff (single target, medium)

### Units benefitting from Zandrok

- Nerion
- Carolina

### Units that can act as a replacement for Zandrok

**Buffs on allies**

- Shakir (100% `Haste` `Life Drain`)
- Dunlingr (68% `Life Drain` `Haste`)
- Gala (60% `Haste`)

**Similar Skills**

- Atalanta (66% `aoe-damage` `battle-start-burst`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Antandra (100% `Stun`)
- Lorsan (100% `Stun`)
- Lucca (100% `Stun`)

### Summary for Zandrok

#### Damage types dealt by Zandrok

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target

#### Buffs provided by Zandrok

- Haste buff — Area — `low` — conditional (frequent)
- Lifedrain buff — Area — `low` — conditional (frequent)

#### Crowd Control provided by Zandrok

- Stun — Area — `high`

## Zanie

### Zanie's behavior

- Signature skill: Vein Pulse (ultimate) — deploy turrets at battle start
- Movement: moving (avg attack range 1.0 tiles)

#### Skill overview

- Signature skill (ultimate): speed `slow`, buffs `medium`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `medium`

### Units Zanie benefits from

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Damian**
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Shakir**
  - ATK SPD via Haste buff (multiple targets, medium) [signature fuel]

### Units that can act as a replacement for Zanie

**Buffs on allies**

- Koko (60% `Healing` `Max HP`)

**Similar Skills**

- Chippy (100% `summoner`)
- Florabelle (100% `summoner`)

**Damage**

- Alna (100% `DoT` `Physical`)
- Brutus (100% `DoT` `Physical`)
- Gunnar (100% `DoT` `Physical`)

**Debuffs on enemies**

- Sinbad (90% `Phys DEF debuff` `ATK debuff`)
- Brutus (75% `Phys DEF debuff` `DoT`)
- Lyca (75% `Phys DEF debuff` `ATK debuff`)

**Crowd Control**

- Atalanta (100% `Knock back` `Stun`)
- Cassadee (100% `Knock back` `Stun`)
- Lenya (100% `Knock back` `Stun`)

### Summary for Zanie

#### Zanie Provides

- Summoning — Self

#### Damage types dealt by Zanie

- Primary damage type (unit): **Physical**
- Physical — Self, Single target
- DoT — Area

#### Buffs provided by Zanie

- Healing — Single target — `high`
- Shield — Single target — `high`
- DEF Penetration buff (Legendary+) — Single target — `medium`
- Max HP buff (Mythic+) — Single target — `medium`

#### Debuffs provided by Zanie

- ATK debuff (Supreme+) — Single target — `low`
- DoT (Supreme+) — Single target — `low`
- Phys DEF debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Zanie

- Knock back — Single target — `high`
- Stun — Single target — `low`

## Zorya

### Zorya's behavior

- Signature skill: Circle of Vigil (ultimate) — dormant cycle + AoE jump
- Movement: moving (inactive while dormant)

#### Skill overview

- Signature skill (ultimate): speed `slow`, heal `medium`, buffs `medium`, damage `high`
- Non-ultimate: speed `fast`, heal `medium`, buffs `medium`, damage `high`
- True damage: HP loss `high`

### Units Zorya benefits from

Look for units providing: `Haste` `Max HP` `Healing` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Velara**
  - Haste buff (single target, high) [signature fuel]
  - Healing (area, medium)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Enables Ally Ultimate casts via Start-of-battle Ultimate
- **Damian**
  - Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, high, conditional (frequent)) [signature fuel]
- **Smokey & Meerky**
  - Healing (multiple targets, medium)
  - Energy recovery (multiple targets, low) [signature fuel]
  - Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
- **Evie**
  - Healing (multiple targets, high)
  - Enables Ally Ultimate casts via Start-of-battle Ultimate
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Zorya

**Similar Skills**

- Salazer (80% `hp-scaling` `life-drain`)
- Brutus (66% `hp-scaling` `life-drain`)
- Daimon (60% `hp-scaling` `life-drain`)

**Damage**

- Talene (100% `HP loss` `Magic`)
- Niru (94% `Magic` `HP loss`)
- Shadewing (94% `Magic` `HP loss`)

**Crowd Control**

- Antandra (100% `Stun` `Knock down`)
- Lucca (100% `Stun` `Knock down`)
- Lorsan (66% `Stun`)

### Summary for Zorya

#### Zorya Provides

- Invincibility — Area

#### Zorya Requires

- Ally Ultimate casts (Mythic+) — Allies

#### Damage types dealt by Zorya

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Single target
- HP loss — Area — `high`

#### Buffs provided by Zorya

- Haste buff (Mythic+) — Single target — `low`

#### Crowd Control provided by Zorya

- Steadfast — Self — Start of Battle
- Unaffected (EX+10) — Single target — On Skill
- Knock down — Arc — `medium`
- Stun — Area — `medium`

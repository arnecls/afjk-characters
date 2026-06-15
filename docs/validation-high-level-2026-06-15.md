# High-level validation — 2026-06-15

Scope: compare detected **damage types**, **CC types**, **buff labels**, and **debuff
labels** per skill in `data/heroes_data_processed.json` against each skill's
`description`. No values, timings, or targeting checked.

Roster: **117 heroes**, **696 skills**. Skills with at least one discrepancy:
**~116** (~17%). Down from ~120 (~18%) on 2026-06-11; several former gaps are
closed (see Resolved).

Baseline: [validation-high-level-2026-06-11.md](validation-high-level-2026-06-11.md).

## Resolved since 2026-06-11

Detection and data fixes verified in this pass:

- **Artifact taxonomy** — labels normalized to **Artifact buff**, **Artifact
  block**, **Artifact mimic** (schema + synergy_profile).
- **Galahad** — shadow Merlin EX+10 → `Artifact buff`; Temporal Field now has
  Haste + Movement speed debuffs.
- **Cyran** — `Artifact mimic` + `Artifact block` on synergy_profile.
- **Kazim** — Gale Barrage max-HP tier uses upgrade scalar (+40%), not base +140%.
- **Harak Vicious Bite** — DoT false positive removed (June doc expected DoT;
  description is healing-lock HP drain, not sustained enemy DoT).
- **Gerda Splashing Fun** — Sleep + Bind present.
- **Bryon Tacit Strike** — Stun present.
- **Indris Spellbane Shot** — Silence + Max HP-based damage present.
- **Odie** corrosive skills — DoT + Poison debuff present.
- **Saida Deepening Roots** — Bind + DoT present.
- **Aurora Plushification** — Bind present.
- **Mehira Alluring Mirage** — Charm present (no longer empty effects).
- **Arden** vine skills — DoT present.
- **Alna Winter Anthem** — DoT present.
- **Dionel Celestial Spear** — True damage + Vitality debuff present.
- **Gunnar Annihilation Directive** — Vitality debuff + DoT present.
- **Cyran Mystic Recollection** — enemy-side debuff targeting corrected; Silence,
  Bind, Magic, True damage present.
- **Evie Pointed Proof** — spurious debuff-DoT removed from Intel Chase pipeline
  (Intel Chase still has separate issues below).

## Common failure patterns

1. **Spurious damage riders** — execute thresholds, upgrade stat lines, or ally
   riders parsed as damage (Aliceth Sealed Fate stat_mod, Athalia Unbroken
   Retribution max_hp on true-damage line).
2. **True vs Physical/Magic** — true-damage phrases also tagged as normal damage
   (Himmel Heroic Slash, Shemira, Silven, Valka, Faramor).
3. **Missing debuffs from tier upgrades** — Enhance Force / Ex lines often
   partial (Contess, Dunlingr, Granny Dahnie, Nara, Niru, Pang, Zanie).
4. **DoT gaps** — sustained per-second enemy damage not tagged (Bonnie Decay's
   Reach max-stack Aging).
5. **DoT / HoT false positives** — self HP drain or healing-lock cast cost parsed
   as DoT or Healing over time (Harak Vicious Bite, Berial Shadow Reflection).
6. **Buff vs debuff / wrong label** — focus-fire mark as ATK buff (Aliceth Hero
   Focus); damage taken vs damage dealt (Berial Hero Focus).
7. **Upgrade-only CC or utility** — Energy drain, haste buff, damage reduction
   missing when only stated on Ex/Mythic tiers (Bryon Shadow Flash, Hewynn
   Tranquility, Hugin Enhance Force).
8. **Conditional / mode-split text** — second-form or unlock branches skipped
   (Natsu Fiery Ties, Marilee Battlefield Learning).
9. **Summon / artifact-only skills** — combat skill `effects` empty while
   description is artifact or summon driven (Galahad Time Recast → synergy only).

## Findings

Format: `Character, Skill, found, expected`

### Batch A–Damian

Aliceth, Hero Focus, ATK buff (stat_mod), Marked target (focus fire)
Aliceth, Sealed Fate, DEF Penetration buff + Execution debuff, Execution debuff only
Alsa, Don of Terra, Energy drain, none
Antandra, Spear Barrage, none, ATK debuff
Athalia, Unbroken Retribution, max_hp, none
Atalanta, Sleight of Hand, none, ATK debuff
Berial, Hero Focus, Damage taken debuff, damage dealt debuff
Berial, Shadow Reflection, dot, none
Bonnie, Decay's Reach, none, dot
Bryon, Shadow Flash, interrupt, Energy drain
Carolina, Freezing Nova, none, Haste debuff
Carolina, Enhance Force, none, Haste debuff
Cassadee, Tidal Strength, none, Tidal Strength buff
Cecia, Trial of Thorns, none, Vitality debuff
Chippy, Eureka!, physical, magic
Contess, Detention Pass, none, stun
Contess, Detention Pass, none, hp_loss
Contess, Mandatory Civility, none, ATK debuff
Contess, Quiet Period, none, Energy recovery debuff
Contess, Hero Focus, none, Energy recovery debuff
Contess, Expulsion Notice, hp_loss, hp_loss + Energy recovery debuff
Cryonaia, Frostveil Domain, shield + immunity, magic
Cryonaia, Icicle Tempest, magic + dot, dot only
Cyran, Mystic Recollection, ATK buff (stat_mod), ATK SPD debuff
Daimon, Dolly Defender, magic + true, physical
Daimon, Guardian Howl, max_hp, dot
Damian, Inventor's Will, stat_mod + healing over time, Haste buff

### Batch Dionel–Hewynn

Dunlingr, Grand Resonance, ATK debuff, Haste debuff
Dunlingr, Harmonic Soundwall, magic + shield, none
Dunlingr, Enhance Force, none, Magic
Evie, Intel Chase, dot, none
Evie, Intel Chase, none, Magic
Evie, Pointed Proof, none, Magic DEF debuff
Faramor, Sanctified Circle, physical + true, True damage only
Florabelle, Overgrowth, Lifedrain buff, Haste buff + Lifedrain buff
Granny Dahnie, Threshold of Jade, none, Physical
Granny Dahnie, Threshold of Jade, none, Energy drain
Granny Dahnie, Enhance Force, Haste buff, ATK debuff + Haste buff
Gunnar, Annihilation Directive, none, ATK buff + Attack range buff
Gunnar, Enhance Force, Healing debuff, cannot heal/gain shields debuff
Gwyneth, Flare Arrow, DoT, DoT + Vitality debuff
Harak, Vicious Bite, healing over time, none
Hepler, Remedial Class, Haste buff, none
Hewynn, Tranquility, immunity, Damage taken reduction

### Batch Himmel–Lyca

Himmel, Heroic Slash, max_hp + physical + true, True damage only
Himmel, Heroic Dash, physical + knock_down, Knock down only
Himmel, Hero Party, shield + physical, ATK buff + Direct healing
Himmel, Blue-Moon Blessings, stat_mod + heal, Penetration buff
Himmel, Enhance Force, Damage taken debuff, HP loss
Hodgkin, Rending Cleave, physical, Energy drain
Hodgkin, Ardent Believers, physical, Max HP-based damage
Hugin, Titan's Aegis, none, Shield
Hugin, Enhance Force Hugin, none, Damage taken reduction
Kafra, Forest's Wrath, Marked target (focus fire), Healing over time
Koko, Full Energy, Lifedrain buff + Damage taken reduction, True damage + ATK buff
Koko, Fulfilling Feast, Direct healing, ATK buff
Korin, Vine Arms, ATK SPD buff, Max HP-based damage
Kruger, Smashing Assault, physical, Phys DEF debuff
Kruger, Ruthless Vanguard, shield, Lifedrain buff
Kruger, Enhance Force, none, ATK buff
Laios, Living Armor - Kensuke, none, Physical
Laios, Intimidate, DEF buff (ally), Phys DEF debuff + Magic DEF debuff (enemy)
Lorsan, Whispering Tempest, magic + dot, DoT + Haste debuff
Lorsan, Zephyr's Embrace, healing over time, Haste buff
Ludovic, Lifeweaver's Blooms, magic, Max HP-based damage + HP loss
Ludovic, Ethereal Blooms, magic, Max HP-based damage
Lumont, Lumont's Charge, taunt + physical, Knock back
Lyca, Nova Fall, Phys DEF debuff + ATK debuff, Phys DEF debuff only

### Batch Marcille–Zorya

Marcille, Silver-White Wings that Streak Across the Skies, stat_mod, Haste buff + Energy recovery
Marcille, Ancient Magic, magic, Magic + DoT
Marilee, Hyperfocus, ATK SPD buff, ATK buff + ATK SPD buff
Marilee, Hero Focus, Crit buff, Crit DMG boost
Marilee, Battlefield Learning, true, ATK buff + True damage
Mehira, Blissful Whip, hp_loss, Haste buff + HP loss
Mehira, Hero Focus, stat_mod, Lifedrain buff
Mikola, Dauntless Hymn, DEF buff + heal, Haste buff + Ranged DEF buff
Mikola, Passionate Opening, Vitality buff, Vitality buff + Physical
Nara, Eerie Execution, none, Max HP-based damage
Nara, Enhance Force, Vitality debuff, Vitality debuff + Max HP debuff
Natsu, Fiery Ties, Crit buff + Crit DMG boost, + DEF buff
Nazrik, Rend Rupture, true + physical, + Marked target (focus fire)
Nazrik, Savage Wound, physical + Max HP debuff, + Max HP-based damage
Nerion, Drowning Doom, magic, Magic + ATK buff + ATK SPD buff
Nerion, Tidal Rebuke, stun + magic, + Knock back
Nerion, Riptide Wrath, magic, Magic + Knock up
Nerion, Abyssal Embrace, magic + shield, + Haste debuff
Niru, Spirit Devour, magic, Magic + Max HP-based damage
Niru, Enhance Force, DEF buff, DEF buff + Healing debuff
Pandora, Panic Projection, dot + ATK debuff, Frighten + HP loss + ATK debuff
Pandora, Boxed Blessing, Invincible + Energy recovery, + ATK buff + Displace
Pandora, Tainted Tribute, magic + debuffs, debuffs only (no Magic)
Pandora, Eternal Legacy, Energy recovery + ATK debuff, + Unaffected
Pang, Sky Splitter, Stun + buffs, + Energy recovery debuff
Pang, Zen Ward, physical + shield, Physical + Shield + Unaffected
Pang, Spirit Sync, shield, Shield + ATK buff
Parisa, Floral Splendor, magic, Magic + Marked target (focus fire)
Perseus, Spear-Shield Combo, physical, Physical + Shield + ATK SPD buff
Perseus, Fertile Ground, stat_mod, + DEF buff
Phraesto, Futile Echo, magic, Magic + Damage taken reduction
Phraesto, Crimson Contract, magic + shield, + Energy recovery
Phraesto, Vicious Sting, magic + debuffs, Magic + Haste debuff + Vitality debuff + Max HP-based damage
Pippa, Mage's Bloom, bind, Bind + True damage
Pippa, Enhance Force, bind + displace, + Max HP-based damage
Reinier, Mutual Reflection, magic + displace, Magic + Displace
Reinier, Golden Ratio, magic + knock_up, + HP loss
Satrana, Ignite Passions, DoT, Max HP-based damage
Shadewing, Withering Curse, DEF debuffs, Max HP-based damage
Shemira, Ghastly Tribute, physical + max_hp, True damage + Max HP-based damage
Shemira, Spectral Barrier, max_hp, True damage
Silven, Tempered Field, max_hp, True damage + Max HP-based damage
Sinbad, Tracker's Instincts, Damage taken debuff, ATK debuff + Damage taken debuff
Solise, Resonant Bloom, DEF buff, ATK buff + DEF buff + Max HP buff
Sylphira, Harmonic Refrain, none, True damage
Talene, Divine Conflagration, none, Magic + HP loss
Ulmus, Prowling Roots, none, Bind
Valka, Phantom Slasher, max_hp + physical, True damage
Valka, Phantom Slasher, none, Haste debuff
Walker, Bounty Pursuit, physical, Physical + HP loss
Zandrok, Shock Stomp, stun, Max HP-based damage
Zanie, Enhance Force, none, DoT

### Artifact / synergy-only (not per-skill effects)

Galahad, Time Recast, none, summon recast (synergy_profile only)
Galahad, synergy_profile, Artifact buff, shadow Merlin casts same skill (verified)
Cyran, synergy_profile, Artifact mimic + Artifact block, verified

## Spot-checked confirmations

- **Kazim Gale Barrage** — max-HP value **40%** after upgrade-tier parsing (was
  140% from base-line bleed-through).
- **Harak Vicious Bite** — no enemy DoT; **Healing over time** spurious (0%
  self tick from healing-lock cast wording).
- **Galahad Temporal Field** — Movement speed + Haste debuffs match description.
- **Bonnie Decay's Reach** — max-stack Aging (`100% damage every 1s`) still not
  emitted as DoT.
- **Athalia Unbroken Retribution** — knock_down correct; **max_hp** still
  spurious on true-damage execute rider.
- **Himmel Heroic Slash** — both **max_hp** and **true** on same strike; June
  convention preferred true-only.
- **Berial Shadow Reflection** — DoT on Silhouette self HP drain (debatable:
  self-cost vs enemy DoT).
- **Laios Intimidate** — bind present; ally DEF buff spurious; enemy Phys/Magic
  DEF debuffs still missing.

## Fixes applied (detection pass)

Code and data changes made after the initial findings above. Primary files:
`scripts/rewrite-summaries.py`, `scripts/heroes_io.py`, `scripts/hero_schema.py`,
`scripts/test_detect_damage_types.py`, `scripts/test_skill_descriptions.py`.
Regenerated via `just analyze`. Findings tables were not re-run; rows below may
now be closed.

### Damage types

- **True vs Physical/Magic** — `(ATK-based) … true damage` no longer also tags
  normal damage when true damage is the scored hit (Faramor Sanctified Circle,
  Himmel-style riders).
- **True vs max-HP dedup** — `+X% true damage` and `Increases the true damage
  dealt to…` no longer double-count max-HP damage (Athalia Unbroken Retribution).
- **DoT** — `takes X% damage every` emits DoT when a value is extractable
  (Bonnie Decay's Reach); channeled per-second skill damage stays Magic, not DoT
  (Evie Intel Chase); self/summon HP drain excluded (Harak, Berial Shadow
  Reflection).
- **HoT false positive** — healing-lock cast HP drain no longer tagged as
  Healing over time (Harak Vicious Bite).
- **Scalar upgrade chunks** — tier lines that only bump numbers (summoning damage,
  storm per-hit damage, dark flame damage, entangled DoT tiers) no longer add
  new damage effects (Faramor, Lorsan, Cecia upgrades).
- **Shield absorb** — `(ATK-based)` in shield/absorb phrasing no longer parsed
  as enemy damage (Dunlingr Harmonic Soundwall, Hugin cogshield).
- **Kazim Gale Barrage** — max-HP magnitude uses upgrade tier (+40%), not base
  bleed-through (+140%).

### Debuffs and crowd control

- **Marked target** — `mark of … on`, `prioritize attacking` (Aliceth Sealed
  Fate).
- **DEF Penetration** — not emitted as a hero buff when penetration applies to
  attacks against a marked enemy.
- **Damage dealt / taken** — enemy `damage dealt` reduction patterns; Berial Hero
  Focus damage-dealt debuff.
- **DEF debuffs** — Magic DEF from upgrade text (Evie Pointed Proof); Phys DEF
  from Shatter Armor (Kruger Smashing Assault).
- **Energy drain** — absorbing targets' Energy (Bryon Shadow Flash); spurious
  Interrupt removed.
- **Haste debuff** — `N + M Haste reduction` noun form (Lorsan Whispering
  Tempest).
- **ATK SPD debuff** — flat `ATK SPD by N for` kept as ATK SPD (Cyran Starshard
  Spell); `atk spd by an extra N` still maps to Haste debuff (Dunlingr Grand
  Resonance).
- **Vitality debuff** — `Absorbs N of the target's Vitality` on EX+ tiers
  (Cecia Trial of Thorns).
- **ATK debuff** — Antandra Spear Barrage; Laios Intimidate Phys/Magic DEF.

### Buffs and mitigation

- **Damage taken reduction** — `allies take X% less damage` (Hewynn
  Tranquility); `protected ally also takes X% less damage` (Hugin Enhance Force
  Hugin).
- **Haste buff** — `gain an extra 60 + 6 Haste` and comma-list `, 30 + 3 Haste`
  (Florabelle Overgrowth, Lorsan Zephyr's Embrace).
- **Lifedrain buff** — self grants such as Kruger Ruthless Vanguard no longer
  skipped entirely.
- **Summon buffs** — numeric Haste on summons serializes as `buff`, not
  `stat_mod` (`hero_schema.py`).

### Artifacts and special effects

- **Artifact taxonomy** — Artifact buff / Artifact block / Artifact mimic labels
  (Galahad shadow Merlin, Cyran synergy_profile).

### Skill text parsing (`heroes_io.py`)

- **Preamble before Passive** — text before `Passive.` kept in active chunks
  (Aliceth Sealed Fate mark line).
- **Raw backfill** — missing normalized sentences merged at chunk-build time
  (does not mutate stored JSON).
- **Phase markers** — bare `Active.` / `Passive.` sentences skipped in chunks
  only.

### Verified spot-checks after fixes

| Skill | Outcome |
| --- | --- |
| Harak Vicious Bite | No DoT/HoT; Healing debuff |
| Bonnie Decay's Reach | DoT present |
| Aliceth Sealed Fate | Marked target + Execution debuff |
| Athalia Unbroken Retribution | True + HP loss; no spurious max_hp |
| Berial Shadow Reflection | Energy drain only |
| Bryon Shadow Flash | Energy drain only |
| Evie Intel Chase | Magic, no DoT |
| Evie Pointed Proof | Magic DEF debuff |
| Berial Hero Focus | Damage dealt + taken debuffs |
| Hewynn Tranquility | Damage taken reduction |
| Florabelle Overgrowth | Haste buff + Lifedrain buff |
| Lorsan Whispering Tempest | DoT + Haste debuff |
| Cecia Trial of Thorns | + Vitality debuff (EX+5) |
| Kruger Smashing Assault | Phys DEF debuff + Physical |
| Cyran Mystic Recollection | ATK SPD debuff (not Haste) |
| Hugin Enhance Force Hugin | Damage taken reduction |
| Faramor Sanctified Circle | True + HP loss + DoT; no spurious Physical |
| Dunlingr Harmonic Soundwall | Shield only; no spurious Physical |

**138** unit tests in `test_detect_damage_types` and `test_skill_descriptions`
pass after this pass.

## Next step

Detailed validation (targeting, area, timings, magnitudes) per AGENTS.md — not
included here.

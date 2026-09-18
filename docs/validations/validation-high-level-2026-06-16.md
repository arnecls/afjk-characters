# High-level validation — 2026-06-16

Scope: compare detected **damage types**, **CC types**, **buff labels**, and **debuff
labels** per skill in `data/heroes_data_processed.json` against each skill's
`description`. No values, timings, or targeting checked.

Roster: **117 heroes**, **696 skills**. This pass is a **delta** from
[validation-high-level-2026-06-15.md](validation-high-level-2026-06-15.md) after
June detection fixes (Seth, Granny Dahnie, Kafra, Temesia, chip defs,
`CACHE_VERSION` 13). Sample re-audit of Batch A suggests open label gaps remain
at roughly **~15%** of skills; full four-batch re-audit not repeated here.

Baseline: [validation-high-level-2026-06-15.md](validation-high-level-2026-06-15.md).

## Pre-scan results (start of pass)

| Pre-scan | Count |
|----------|-------|
| Self-debuff (`target: self`) | 0 |
| True + Max HP double-label | 0 |
| Spurious immunity (targeting priority) | 0 |
| Artifact Silence CC | 0 |
| Debuff missing from `skill_card_tags` | 0 |
| Heal `value: 0` (all heal rows) | 0 |
| Hero Focus self-stat mis-tagged ally | 10 |
| Skill-card tag Self vs effect `ally` | 6 |

## Resolved since 2026-06-15

Detection and data fixes verified in this pass:

- **Seth Hunter Instinct** — `DEF buff Self`, `Crit buff Self` (combined Phys/Magic
  DEF gain; impersonal crit upgrade).
- **Seth Enhance Force** — `Phys DEF debuff` on enemy (not DEF buff).
- **Granny Dahnie Glimmerbloom Blessings** — `DEF buff Self`; no self DEF debuff;
  HoT scalar no longer inflates DEF magnitude.
- **Kafra Sylvan Banishment** — `Haste debuff`; no spurious `ATK debuff` or
  `Haste buff`.
- **Temesia Iron Heel** — `Damage dealt debuff` (detection + debuff chip display).
- **Temesia Invincible Fury** — `True damage` on conversion line (`turning … into
  true damage`).
- **Bonnie Decay's Reach** — DoT present (June gap closed).
- **Berial Hero Focus** — `Damage dealt debuff` + `Damage taken debuff` (June
  spot-check confirmed).
- **Evie Intel Chase** — Magic only; no spurious DoT (June gap closed).
- **Florabelle Overgrowth** — Haste buff + Lifedrain buff (June gap closed).
- **Marilee Battlefield Learning** — True damage present (June gap closed).
- **Self-debuff false positives** — pre-scan **0** (Granny-style fixes holding).
- **True + Max HP hierarchy** — pre-scan **0** double-label candidates.

## Common failure patterns (this pass)

1. **Hero Focus dual clause** — `{name} increases her ATK/Haste by N` parsed as
   ally buff while skill-card tags show `— Self`; ally conditional clause missing
   or merged wrong (Aliceth, Atalanta, Twins, Smokey & Meerky, Cassadee).
2. **Empty Hero Focus** — passive damage-dealt or stat lines with no `effects`
   (Zorya, Fay, Isabella, Niru, Shemira).
3. **Skill-card tags vs effects mismatch** — Self suffix on tags when
   `effects[].target` is `ally` (Aliceth, Atalanta, Isabella Enhance Force).
4. **Missing true-damage rider** — composite ATK hit with `plus extra true damage`
   not tagged True (Himmel Heroic Slash).
5. **Missing dual damage type** — magic + physical in text, Physical only
   (Chippy Eureka!).
6. **Enhance Force upgrade-only** — many Supreme+ lines still have empty
   `effects` (42 skills); triage per skill, do not bulk-parse.
7. **June carry-over** — upgrade-only debuffs, mode branches, spurious damage
   riders (see June doc batches B–D).

## Findings

Format: `Character, Skill, found, expected`

### Pattern — Hero Focus (label + targeting)

Aliceth, Hero Focus, ATK buff ally, ATK buff Self + ally ATK buff
Atalanta, Hero Focus, Haste buff ally, Haste buff Self
Cassadee, Hero Focus, Tidal Strength buff + Haste ally, Haste buff Self + ally clause
Smokey & Meerky, Hero Focus, ATK buff ally, ATK buff Self (+ ally clause if text)
Twins, Hero Focus, Haste buff ally, Haste buff Self + permanent ally Haste
Thoran, Hero Focus, Energy recovery ally, Energy recovery Self (if caster-only)
Fay, Hero Focus, none, stat or damage-dealt buff Self
Isabella, Hero Focus, none, stat buff Self
Niru, Hero Focus, none, stat buff Self
Shemira, Hero Focus, none, stat buff Self
Zorya, Hero Focus, none, damage dealt buff Self (+ conditional)

### Pattern — skill-card tag drift

Aliceth, Hero Focus, tag ATK buff Self / effect ally, align tag to effect target
Atalanta, Hero Focus, tag Haste buff Self / effect ally, align tag to effect target
Isabella, Enhance Force, mixed Self tags on ally rows, align tags to targets

### Batch A sample (delta vs June 15)

Aliceth, Hero Focus, ATK buff ally, Self + ally (see above)
Chippy, Eureka!, Physical, Magic + Physical
Himmel, Heroic Slash, Physical + Max HP-based, True damage rider on sweep
Bonnie, Decay's Reach, DoT, (resolved)
Berial, Shadow Reflection, Energy drain, (resolved)
Evie, Intel Chase, Magic, (resolved; no DoT)

### Batch A — still open from June (unchanged sample)

Alsa, Don of Terra, Energy drain, none
Antandra, Spear Barrage, none, ATK debuff
Atalanta, Sleight of Hand, none, ATK debuff
Carolina, Enhance Force, none, Haste debuff
Cecia, Trial of Thorns, none, Vitality debuff
Contess, Mandatory Civility, none, ATK debuff
Daimon, Dolly Defender, magic + true, physical
Damian, Inventor's Will, stat_mod + healing over time, Haste buff

## Spot-checked confirmations

| Skill | Outcome |
| --- | --- |
| Seth Hunter Instinct | DEF buff Self, Crit buff Self, Haste/Lifedrain Self |
| Granny Dahnie Glimmerbloom Blessings | DEF buff Self, HoT Self, Unaffected Self |
| Kafra Sylvan Banishment | Haste debuff, Shield Self, no ATK debuff |
| Temesia Iron Heel | Damage dealt debuff, Physical, Interrupt |
| Temesia Invincible Fury | True damage, Unaffected Self |
| Bonnie Decay's Reach | DoT + Magic + debuffs |
| Berial Hero Focus | Damage dealt + Damage taken debuffs |
| Harak Vicious Bite | No DoT/HoT; Healing debuff |

## Fixes applied during this validation run

See git history for detection changes after this report (Hero Focus split, Zorya
damage-dealt buff, Contess heal targeting, Himmel true-damage rider).

## Next step

[validation-detailed-2026-06-16.md](validation-detailed-2026-06-16.md) — targeting,
durations, magnitudes. Prioritize Hero Focus targeting and tag sync before broad
Enhance Force triage.

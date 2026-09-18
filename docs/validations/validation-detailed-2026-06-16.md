# Detailed validation — 2026-06-16

Scope: compare detected **targeting**, **area types**, **timings**, and **magnitudes**
per skill effect in `data/heroes_data_processed.json` against each skill's
`description` (raw + active/passive + max-tier upgrades). Damage-type labels,
buff/debuff labels, and CC-type labels are **not** checked here — see
[validation-high-level-2026-06-16.md](validation-high-level-2026-06-16.md).

Roster: **117 heroes**, **696 skills**. This is a **delta pass** from
[validation-detailed-2026-06-15.md](validation-detailed-2026-06-15.md); not every
skill re-audited. Focus: themes still open after June fixes and pre-scans.

Baseline high-level pass: [validation-high-level-2026-06-16.md](validation-high-level-2026-06-16.md).

## Pre-scan results

| Pre-scan | Start count | Notes |
|----------|-------------|-------|
| Ally-target self-effect candidates | 8 | Triage below; not all are bugs |
| Self-debuff | 0 | |
| Heal `value: 0` | 0 | June theme largely closed |
| DoT tick 1 with 0.25/0.5s text | 0 | |
| Knock down `duration: 0` | 13 | Still open |

### Ally-target triage (8 candidates)

| Hero / Skill | Effect | Verdict |
|--------------|--------|---------|
| Atalanta / Hero Focus | Haste buff ally | **Bug** — base Haste is Self |
| Twins / Hero Focus | Haste buff ally | **Bug** — base Haste is Self |
| Contess / Detention Pass | Shield ally | **OK** — grants Exemption shield to ally |
| Hugin / Unstoppable! | Haste buff ally | Read text — may be ally aura |
| Ravion / Designated Duty | Energy recovery ally | Read text — may be ally grant |
| Smokey & Meerky / Special Aroma | Energy + heal ally | Read text — aroma affects allies |
| Smokey & Meerky / Energizing Formula | Energy recovery ally | Read text — ally grant |

## Common failure patterns (carried + delta)

1. **Hero Focus `target: ally` for self stat** — Aliceth, Atalanta, Twins (see
   high-level pass). Corrupts replacement **Buffs on allies** when combined with
   mis-tagged Invincible patterns.
2. **Heal target wrong** — Contess Detention Pass: `restores … to a target ally`
   stored as `target: self`.
3. **Knock down `duration: 0`** — 13 skills (Antandra Shield Assault, Callan
   Flail Slam, Cyran Cursed Grasp, Harak Vicious Bite, Himmel Heroic Dash,
   Kordan Sundering Strike, Lucca Quake Slam, Pippa Wild Shift, Ravion Designated
   Duty, Reinier Tuned Art, Scarlita Valkyrie Spirit, Temesia Knight's Heart).
4. **Area / `target_count`** — June findings still apply (Atalanta Wild Sniper
   line, Contess Mandatory Civility count 3 vs 2, Faramor `area_count` 1).
5. **Upgrade-tier magnitudes** — selective items from June doc (Kazim resolved;
   Lorsan Haste -33 flat, Faramor 0.5s tick still open).
6. **Skill-card tag Self vs effect ally** — six mismatches; fix with Hero Focus
   targeting pass.

## Findings

Format: `Character (Skill): found -> expected`

### Targeting — Hero Focus

Aliceth (Hero Focus): target ally / Multiple targets -> Self base ATK + ally conditional
Atalanta (Hero Focus): target ally -> Self Haste + conditional self Haste
Twins (Hero Focus): target ally -> Self Haste + ally bond Haste
Smokey & Meerky (Hero Focus): target ally -> Self ATK (+ ally if text)

### Targeting — heals

Contess (Detention Pass): Direct healing Self -> Direct healing ally (target ally)

### Durations — knock down

Antandra (Shield Assault): knock_down duration 0 -> brief lock when text implies
Callan (Flail Slam): knock_down duration 0 -> brief lock when text implies
Himmel (Heroic Dash): knock_down duration 0 -> brief lock when text implies
Temesia (Knight's Heart): knock_down duration 0 -> brief lock when text implies

### Magnitudes — sample from June still open

Lorsan (Whispering Tempest): Haste debuff magnitude generic -> -33 flat
Faramor (Sanctified Circle): area_count 2 -> 1; DoT tick 1s -> 0.5s at max tier
Atalanta (Wild Sniper): Single target -> line/area along path
Contess (Mandatory Civility): target_count 3 -> 2 weakest allies / 2 enemies

### Relation to high-level

| Skill | High-level | Detailed still open |
| --- | --- | --- |
| Aliceth Hero Focus | ATK buff label OK | target Self vs ally |
| Contess Detention Pass | HP loss + shield OK | heal target ally; HP-loss tick |
| Himmel Heroic Slash | missing True rider | area 3×3; knock down duration |
| Zorya Hero Focus | empty effects | damage-dealt % Self |
| Lorsan Whispering Tempest | DoT + Haste debuff OK | -33 flat; 5s / 0.5s tick |

## Spot-checked confirmations

- **Kazim Gale Barrage** — max-HP magnitude 40% at max tier (June fix holding).
- **Faramor Sanctified Circle** — True + DoT labels OK; detailed gaps on
  `area_count` and tick remain.
- **Chippy** (all skills) — no new detailed issues in sample check.
- **Seth / Kafra / Temesia** — recent single-hero fixes verified in processed JSON.

## Fixes applied during this validation run

Detection patches for Hero Focus, Zorya damage-dealt buff, Contess heal targeting,
and Himmel true-damage rider (see `rewrite-summaries.py` and tests).

## Next step

After Hero Focus + tag sync land: re-run ally-target pre-scan; grep
`heroes_data_synergies.json` `"buff"` replacements for Aliceth/Atalanta/Twins.
Continue four-batch detailed audit for area/`target_count`/durations per June
method.

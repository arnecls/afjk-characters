# Audit change table — 2026-09-22

This document is a synthesis of the accepted reducer relay only. “Not
stated” means the relay recorded that the hero changed but did not include
the prior or corrected skill-level detail.

## Batch coverage and clean counts

| Relayed batch ID | Relay range | Changed heroes | Clean heroes |
| --- | --- | ---: | ---: |
| `batch-a` | aliceth–evie | 11 | 15 |
| `batch-b` | faramor–lucca | 26 | 0 |
| `batch-c` | lucius–odie (C1) | 11 | 2 |
| `batch-c2` | orion–scarlita (C2) | 11 | 2 |
| `batch-d` | seth–karma | 18 | 8 |
| **Total** | A–D | **77** | **27** |

## Changed hero/skill rows

| Batch | Hero ID | Skill or upgrade | Found → expected | Failure pattern |
| --- | --- | --- | --- | --- |
| `batch-a` | `baelran` | Ultimate | Unsupported 400% / wrong HP-based area value → 10% HP AoE, with no 400% value | Unsupported magnitude |
| `batch-a` | `bonnie` | Not stated | Prior state not stated → accepted refreshed skill effects, detail not relayed | Relay detail unavailable |
| `batch-a` | `brutus` | Not stated | Prior state not stated → accepted refreshed skill effects, detail not relayed | Relay detail unavailable |
| `batch-a` | `bryon` | Enhance Force | Haste present → Haste removed | Spurious effect |
| `batch-a` | `bryon` | Exclusive: Tacit Strike | Healing absent or incorrect → Direct healing 200% plus HoT 40% for 5s | Missing/incorrect healing |
| `batch-a` | `bryon` | Ultimate | Wrong storm DoT value → text-backed value (magnitude not relayed) | Wrong magnitude |
| `batch-a` | `callan` | Not stated | Prior state not stated → accepted refreshed skill effects, detail not relayed | Relay detail unavailable |
| `batch-a` | `cecia` | Skill not stated | Incorrect DoT/summon values → DoT 140% plus summon 60% | Wrong magnitudes |
| `batch-a` | `cryonaia` | Skill not stated | Extracted 77% value → removed; source has zero matching occurrences | Unsupported magnitude |
| `batch-a` | `cyran` | Not stated | Prior state not stated → accepted refreshed skill effects, detail not relayed | Relay detail unavailable |
| `batch-a` | `daimon` | Not stated | Prior state not stated → accepted refreshed skill effects, detail not relayed | Relay detail unavailable |
| `batch-a` | `dunlingr` | Not stated | Prior state not stated → accepted refreshed skill effects, detail not relayed | Relay detail unavailable |
| `batch-a` | `eironn` | Skill not stated | Slash/stab damage combined or incorrect → slash 125% and stab 250% | Split-hit conflation |
| `batch-b` | `faramor` | Skill 2 | Incorrect/missing ATK value → ATK 15% | Wrong/missing magnitude |
| `batch-b` | `faramor` | Exclusive | Incorrect/missing self ATK value → ATK Self 10% | Wrong/missing magnitude |
| `batch-b` | `fay` | Skill 2 | Incorrect/missing rows → 160 damage and DEF rows | Missing/incorrect effects |
| `batch-b` | `fay` | Exclusive | Incorrect/missing Vitality value → Vitality 25 | Wrong/missing magnitude |
| `batch-b` | `florabelle` | Summon giant | Incorrect/missing duration → 10s | Duration |
| `batch-b` | `frieren` | Ultimate | Wrong damage typing/value → True damage 1800 | Damage type/magnitude |
| `batch-b` | `frieren` | Skill 1 | Incorrect rows, including spurious DoT → 250 damage, Damage dealt Self 60%, ATK Self 30%, and no DoT | Missing/spurious effects |
| `batch-b` | `frieren` | Skill 2 | Incorrect/missing rows → 300 damage plus Vitality 50 | Missing/incorrect effects |
| `batch-b` | `frieren` | Exclusive | Incorrect/missing Damage taken value → Damage taken 85% | Wrong/missing magnitude |
| `batch-b` | `gerda` | Ultimate | Incorrect damage value → 180 | Wrong magnitude |
| `batch-b` | `gerda` | Skill 1 | Incorrect damage/HoT rows → 260 damage plus Area HoT at rank 2 | Missing/incorrect effects |
| `batch-b` | `gerda` | Skill 2 | Incorrect/missing rows → 150 damage plus 400 shield for 8s | Missing/incorrect effects |
| `batch-b` | `granny-dahnie` | Ultimate | Incorrect/missing energy and duration → Energy 40 plus 3s | Missing/incorrect effects |
| `batch-b` | `granny-dahnie` | Skill 1 | Incorrect/missing rows → Haste for 6s plus 120 damage | Missing/incorrect effects |
| `batch-b` | `granny-dahnie` | Skill not stated | Incorrect/missing Vitality value → Vitality 19 | Wrong/missing magnitude |
| `batch-b` | `gunnar` | Ultimate | Incorrect/missing damage rows → 640 damage, meteor 550, and DoT 80 for 15s | Multi-part effect loss |
| `batch-b` | `gunnar` | Skill 1 | Incorrect damage value → 80 | Wrong magnitude |
| `batch-b` | `gunnar` | Skill labels | Incorrect targets → Self labels | Targeting |
| `batch-b` | `gunnar` | Exclusive | Invincible ally row absent or incorrect → Invincible ally | Missing/incorrect effect |
| `batch-b` | `gwyneth` | Skill 1 | Incorrect damage value → 280 | Wrong magnitude |
| `batch-b` | `gwyneth` | Skill 2 | Incorrect/missing periodic and speed rows → DoT 20 every 0.25s for 4s plus permanent ATK SPD | Periodic/duration extraction |
| `batch-b` | `gwyneth` | Exclusive | Incorrect/missing DEF Penetration value → DEF Penetration 60 | Wrong/missing magnitude |
| `batch-b` | `hammie` | Skill 1 | Incorrect/missing ATK duration → 5s | Duration |
| `batch-b` | `hepler` | Skill 1 | Incorrect/missing Haste row → Haste 90 for 3.3s | Missing/incorrect effect |
| `batch-b` | `hepler` | Skill 2 | Duplicate HoT rows → deduplicated HoT | Duplicate effect |
| `batch-b` | `hepler` | Exclusive | Incomplete exclusive effects → Invincible ally for 3s, Cheat death, ATK Self 30%, Max HP ally 40% | Multi-effect loss |
| `batch-b` | `hepler` | Supreme+ | DEF rows absent or incorrect → corrected DEF rows (values not relayed) | Missing/incorrect effects |
| `batch-b` | `hewynn` | Skill 1 | Incorrect value → 300 | Wrong magnitude |
| `batch-b` | `hewynn` | Exclusive | Incorrect/missing Damage taken value → Damage taken 36% | Wrong/missing magnitude |
| `batch-b` | `hugin` | Ultimate | Incorrect/missing Haste duration → 10s | Duration |
| `batch-b` | `hugin` | Skills not stated | Incorrect/missing defensive rows → shields for 8s, Haste 20, Damage taken 30% | Missing/incorrect effects |
| `batch-b` | `igor` | Ultimate | Incorrect damage value → 270 | Wrong magnitude |
| `batch-b` | `igor` | Skill 1 | Incorrect damage value → 170 | Wrong magnitude |
| `batch-b` | `igor` | Skill 2 | Incomplete rows → heal 4.5%, Cheat death, and Lifedrain 12 | Multi-effect loss |
| `batch-b` | `indris` | Ultimate | Mixed/incorrect damage typing or control → True-only damage plus 8s silence | Damage type/control |
| `batch-b` | `indris` | Exclusive | Incorrect/missing durations → 6s | Duration |
| `batch-b` | `isabella` | Skill 2 | Incorrect/missing ATK debuff → 75% for 5s | Debuff magnitude/duration |
| `batch-b` | `isabella` | Exclusive | Incorrect/missing duration → 8s | Duration |
| `batch-b` | `kafra` | Exclusive | Incorrect/missing Haste duration → 5s | Duration |
| `batch-b` | `kafra` | Supreme+ | Incorrect value → 520 | Wrong magnitude |
| `batch-b` | `kazim` | Ultimate | Incomplete rows → Arc plus 200 for 3s | Multi-part effect loss |
| `batch-b` | `kazim` | Skill 1 | Incorrect/missing values → 500 plus 400 | Multi-part effect loss |
| `batch-b` | `kazim` | Skill 2 | Incorrect value → 400 | Wrong magnitude |
| `batch-b` | `kazim` | Exclusive | Wrong/duplicate rows → Damage dealt Self 35%, with doubled Max HP row removed | Wrong target/duplicate |
| `batch-b` | `koko` | Skill 2 | Incomplete rows → Damage taken 10% for 5s plus spear damage 240 | Multi-effect loss |
| `batch-b` | `koko` | Exclusive | Incorrect/missing shield duration → 7s | Duration |
| `batch-b` | `korin` | Ultimate | Incorrect/missing area value → area 2 | Area |
| `batch-b` | `korin` | Skill 1 | Wrong damage typing/value → True damage 220 | Damage type/magnitude |
| `batch-b` | `korin` | Exclusive | Doubled Max HP rows → duplicates removed | Duplicate effect |
| `batch-b` | `korin` | Supreme+ | Incorrect/missing Damage taken value → Damage taken 25% | Wrong/missing magnitude |
| `batch-b` | `kruger` | Skill 1 | Incorrect/missing DEF value → DEF 10% | Wrong/missing magnitude |
| `batch-b` | `kruger` | Skill 2 | Incomplete defensive rows → Damage taken Area 40% and Ranged DEF 26 | Multi-effect loss |
| `batch-b` | `kruger` | Exclusive | Incomplete shield/control rows → shield 48% for 15s plus immunity | Multi-effect loss |
| `batch-b` | `kruger` | Supreme+ | Incorrect/missing ATK value → ATK 40% | Wrong/missing magnitude |
| `batch-b` | `laios` | Skill 1 | Incomplete rows → DEF 50% plus stun | Multi-effect loss |
| `batch-b` | `laios` | Skill 2 | Incorrect/missing heals → self heal 500 plus ally heal 560 | Target/value split |
| `batch-b` | `laios` | Ultimate | Incomplete summon rows → summon ATK SPD 120 for 10s plus immunity | Multi-effect loss |
| `batch-b` | `lamentis` | Ultimate | Incomplete debuff rows → Max HP debuff 20% plus ATK SPD for 10s | Multi-effect loss |
| `batch-b` | `lamentis` | Skill 1 | Incorrect/missing Max HP value → Max HP 20% | Wrong/missing magnitude |
| `batch-b` | `lenya` | Ultimate | Incorrect target/value → Single 480 | Targeting/magnitude |
| `batch-b` | `lenya` | Skill 1 | Conflated target/value rows → Single 260 plus Area 390 | Target/value split |
| `batch-b` | `lenya` | Skill 2 | Incomplete rows → Crit 15, stun 1s, and damage 240 | Multi-effect loss |
| `batch-b` | `lily-may` | Ultimate | Incorrect value → 240 | Wrong magnitude |
| `batch-b` | `lily-may` | Skill 1 | Incomplete rows → 480 plus temporary Invincible | Multi-effect loss |
| `batch-b` | `lily-may` | Skill 2 | Incorrect/missing rows → ATK 14 with 4 stacks plus True damage 6 | Stacks/damage type |
| `batch-b` | `lorsan` | Ultimate | Incorrect/missing Haste duration → 5s | Duration |
| `batch-b` | `lorsan` | Skill 2 | Incorrect/missing rows → 6s durations plus HoT 120 | Missing/incorrect effects |
| `batch-b` | `lorsan` | Supreme+ | Incorrect immunity scope → unaffected immunity | Immunity semantics |
| `batch-b` | `lucca` | Ultimate | Incorrect value → 240 | Wrong magnitude |
| `batch-b` | `lucca` | Skill 1 | Incomplete rows → shield 400 plus damage 150 | Multi-effect loss |
| `batch-b` | `lucca` | Exclusive | Incorrect ATK target → ATK Multiple | Targeting |
| `batch-c` | `lucius` | Ultimate | Incorrect shield value → 520 | Wrong magnitude |
| `batch-c` | `lucius` | Skill 1 | Incorrect/missing rows → damage 70 plus shield 320 | Multi-effect loss |
| `batch-c` | `lucius` | Exclusive | Incorrect/missing shield row → shield 3% for 4s | Missing/incorrect effect |
| `batch-c` | `lumont` | Ultimate | Incorrect/missing taunt duration → 4s | Duration |
| `batch-c` | `lumont` | Skill 1 | Incomplete rows → shield 450 plus ally DEF 2 for 7s | Multi-effect loss |
| `batch-c` | `lumont` | Skill 2 | Stun present → stun removed | Spurious control |
| `batch-c` | `lumont` | Exclusive | Incorrect/missing area and value → 3-tile Area 210 | Area/magnitude |
| `batch-c` | `lyca` | Skill 1 | Incorrect/missing rows → 8s duration plus Energy 120 | Missing/incorrect effects |
| `batch-c` | `lyca` | Skill 2 | Incorrect/missing DEF debuff → 12% for 6.5s | Debuff magnitude/duration |
| `batch-c` | `lyca` | Focus | Wrong unlock tier → Legendary+ | Tier |
| `batch-c` | `marcille` | Skill 2 | Incomplete targeting/effects → Area blind plus ally heal 300 | Multi-effect loss |
| `batch-c` | `marcille` | Exclusive | Incomplete rows → once-per-battle plus DoT relabel | Condition/label |
| `batch-c` | `marcille` | Supreme+ | Energy row absent or incorrect → corrected energy row (value not relayed) | Missing/incorrect effect |
| `batch-c` | `marilee` | Skill 1 | Conditions absent or incorrect → corrected conditions (detail not relayed) | Condition |
| `batch-c` | `marilee` | Focus | Wrong unlock tier → Legendary+ | Tier |
| `batch-c` | `marilee` | Skill not stated | ATK stack conditions absent or incorrect → corrected stack conditions (detail not relayed) | Stack condition |
| `batch-c` | `mikola` | Ultimate | Incorrect/missing sphere duration → 12s | Duration |
| `batch-c` | `mikola` | Skill 2 | Incorrect/missing rows → heal count 3 plus DEF for 5s | Count/duration |
| `batch-c` | `mikola` | Skill 1 | Incorrect/missing HoT value → 12% per second | Periodic healing |
| `batch-c` | `mirael` | Ultimate | Incorrect/missing Area count → 3 | Area/count |
| `batch-c` | `mirael` | Skill not stated | Incorrect/missing DoT duration/conditions → 14s plus corrected conditions | Duration/condition |
| `batch-c` | `nara` | Ultimate | Incorrect energy target/value → Energy Self 750 | Targeting/magnitude |
| `batch-c` | `nara` | Skill 1 | Incorrect/missing HP-loss value → 5% | Wrong/missing magnitude |
| `batch-c` | `nara` | Skill 2 | Incorrect damage typing/value → Physical 80 | Damage type/magnitude |
| `batch-c` | `nara` | Focus | Incorrect/missing ATK value → ATK 20% | Wrong/missing magnitude |
| `batch-c` | `nara` | Supreme+ | Incorrect target → Self | Targeting |
| `batch-c` | `natsu` | Skill 2 | Incomplete crit rows → Crit 5 plus Crit DMG Boost 5 | Multi-effect loss |
| `batch-c` | `nerion` | Ultimate | Incorrect/missing ATK buff → 30% for 12s | Buff magnitude/duration |
| `batch-c` | `nerion` | Skill 2 | Incorrect/missing spear row → 220 Area | Area/magnitude |
| `batch-c` | `odie` | Exclusive +10 | Incorrect energy target → Energy Self | Targeting |
| `batch-c2` | `pang` | Not stated | Prior state not stated → accepted refreshed skill effects, detail not relayed | Relay detail unavailable |
| `batch-c2` | `parisa` | Skills not stated | Incorrect durations → 10.0s | Duration |
| `batch-c2` | `peggy` | Not stated | Prior state not stated → accepted refreshed skill effects, detail not relayed | Relay detail unavailable |
| `batch-c2` | `perseus` | Not stated | Prior state not stated → accepted refreshed skill effects, detail not relayed | Relay detail unavailable |
| `batch-c2` | `phraesto` | Not stated | Prior state not stated → accepted refreshed skill effects, detail not relayed | Relay detail unavailable |
| `batch-c2` | `rowan` | Not stated | Prior state not stated → accepted refreshed skill effects, detail not relayed | Relay detail unavailable |
| `batch-c2` | `rolan` | Not stated | Prior state not stated → accepted refreshed skill effects, detail not relayed | Relay detail unavailable |
| `batch-c2` | `saida` | Exclusive +10 | DoT absent or incorrect → corrected DoT (value not relayed) | Missing/incorrect effect |
| `batch-c2` | `saida` | Ultimate | Stale Energy 240 plus valid periodic energy → stale 240 removed; Energy 120 per 2.5s tick retained | Stale effect |
| `batch-c2` | `saida` | Skills not stated | Immunity rows present → immunity rows removed | Spurious immunity |
| `batch-c2` | `salazer` | Spirit Shackles | Missing/mis-synthesized stat steal → `stat_steal`, Self, 12%, permanent | Converter synthesis |
| `batch-c2` | `satrana` | Exclusive | Incorrect/missing target/value rows → Self 16/20/22 plus ally 20/22 | Target/value split |
| `batch-c2` | `satrana` | Exclusive +5 | Incorrect/missing energy value → Energy 200 | Wrong/missing magnitude |
| `batch-c2` | `scarlita` | Not stated | Prior state not stated → accepted refreshed skill effects, detail not relayed | Relay detail unavailable |
| `batch-d` | `shemira` | Skill not stated | Mixed/incorrect delivery → True-only delivery | Damage type |
| `batch-d` | `silven` | Skill 2 | Mixed/incorrect damage typing → True-only | Damage type |
| `batch-d` | `silven` | Exclusive | ATK row absent or incorrect → corrected ATK row (value not relayed) | Missing/incorrect effect |
| `batch-d` | `sinbad` | Skill not stated | Mark provider attached to wrong location → mark provide moved to corrected location | Effect ownership |
| `batch-d` | `solise` | Exclusive | Rows absent or incorrect → corrected exclusive rows (detail not relayed) | Missing/incorrect effects |
| `batch-d` | `solise` | Skill not stated | Duplicate Magic DEF row → duplicate removed | Duplicate effect |
| `batch-d` | `solise` | Ultimate | Incorrect/missing value → 30 | Wrong/missing magnitude |
| `batch-d` | `solise` | Skill 1 | Incorrect/missing ATK value → ATK 15 | Wrong/missing magnitude |
| `batch-d` | `sonja` | Supreme | Lifedrain row absent or incorrect → corrected Lifedrain row (value not relayed) | Missing/incorrect effect |
| `batch-d` | `sonja` | Ultimate | Incorrect value → 672 | Wrong magnitude |
| `batch-d` | `soren` | Supreme | Rows present → Supreme rows removed | Spurious effects |
| `batch-d` | `soren` | Skill not stated | Incorrect value → 90 | Wrong magnitude |
| `batch-d` | `taichi-agumon` | Skill not stated | Incomplete rows → Max HP plus 330 | Multi-effect loss |
| `batch-d` | `talene` | Ultimate | Rows absent or incorrect → corrected Ultimate rows, detail not relayed | Missing/incorrect effects |
| `batch-d` | `talene` | Skill 1 | Rows absent or incorrect → corrected Skill 1 rows, detail not relayed | Missing/incorrect effects |
| `batch-d` | `talene` | Skill 2 | Rows absent or incorrect → corrected Skill 2 rows, detail not relayed | Missing/incorrect effects |
| `batch-d` | `temesia` | Ultimate | Damage dealt buff present → buff removed | Spurious effect |
| `batch-d` | `thador` | Ultimate | Rows absent or incorrect → corrected Ultimate rows, detail not relayed | Missing/incorrect effects |
| `batch-d` | `thador` | Skill not stated | Incorrect/missing shield duration → 8s | Duration |
| `batch-d` | `ulmus` | Skill not stated | Incorrect/missing rows → Max HP-based effect plus 260 | Formula/magnitude |
| `batch-d` | `vala` | Supreme | Buff target absent or incorrect → buff Self | Targeting |
| `batch-d` | `vala` | Skill not stated | Incorrect/missing lost-HP value → 12% | Wrong/missing magnitude |
| `batch-d` | `valka` | Ultimate | Wrong damage typing → True damage | Damage type |
| `batch-d` | `valka` | Skill 1 | Shield present → shield removed | Spurious effect |
| `batch-d` | `velara` | Skills not stated | Incorrect durations plus stale Haste → corrected durations and stale Haste removed | Duration/stale effect |
| `batch-d` | `velara` | Skill 1 | Wrong tier/value selection → maximum tier | Tier selection |
| `batch-d` | `walker` | Skill not stated | Lost-HP/mark rows absent or incorrect → corrected lost-HP and mark rows | Missing/incorrect effects |
| `batch-d` | `yamato-gabumon` | Ultimate | Wrong damage typing plus incorrect/missing energy → True damage plus corrected energy | Damage type/energy |
| `batch-d` | `zandrok` | Skill not stated | Incorrect Max HP target → Self Max HP | Targeting |
| `batch-d` | `zorya` | Skill not stated | ATK stack rows absent or incorrect → corrected ATK stacks | Stack extraction |

## Clean heroes

- `batch-a` (15): `aliceth`, `antandra`, `arden`, `atalanta`,
  `athalia`, `berial`, `carolina`, `cassadee`, `chippy`, `contess`,
  `damian`, `dionel`, `twins`, `eryndor`, `evie`.
- `batch-b` (0): none.
- `batch-c` (2): `nazrik`, `niru`.
- `batch-c2` (2): `orion`, `pandora`.
- `batch-d` (8): `seth`, `silvina`, `tasi`, `tilaya`, `valen`,
  `voracia`, `zanie`, `karma`.

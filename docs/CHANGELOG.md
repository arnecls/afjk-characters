# Changelog

## 2026-09-24

### Corrected hero data

- repaired skill data and values for almost every character. Skill texts sourced
  from the afk journey wiki were sometimes incomplete or incorrect. These have
  been repaired, which resulted in several changes.
- repaired the "stats steal" mechanic detection.

### Damage types

- renamed and merged damage types in the list view and CSV exports. This makes
  it a lot easier to filter for different damage types.
- fixed the detection of HP-loss, max-HP damage, lost-HP damage and true damage.
  There was a lot of confusion about these damage types, which is now resolved.

### Assets

- updated the Karma portrait image.

### Character data changes

| Character | What changed |
|---|---|
| aliceth | - Refreshed skill effects to match text; reclassified damage types |
| alna | - Fixed confirmed skill-effect gaps against skill text |
| alsa | - Gated Swift Evasion shield on 7s re-trigger |
| antandra | - Refreshed skill effects to match text |
| arden | - Refreshed skill effects to match text |
| athalia | - Refreshed skill effects to match text |
| aurora | - Deduped Ultimate 320% Magic damage to single text-backed row |
| baelran | - Fixed Ultimate to 10% HP AoE; removed unsupported 400% |
| bonnie | - Refreshed skill effects to match text |
| brutus | - Refreshed skill effects to match text |
| bryon | - Removed spurious Haste; added Tacit Strike 200% heal + 40% HoT; fixed Ult storm DoT |
| callan | - Refreshed skill effects to match text |
| carolina | - Refreshed skill effects to match text |
| cassadee | - Refreshed skill effects to match text |
| cecia | - Fixed DoT to 140% + summon to 60% |
| contess | - Reclassified damage types; refreshed counters/behavior |
| cryonaia | - Removed unsupported 77% value |
| cyran | - Refreshed skill effects to match text |
| daimon | - Refreshed skill effects; reclassified damage types |
| damian | - Refreshed skill effects to match text |
| dionel | - Refreshed skill effects to match text |
| dunlingr | - Refreshed skill effects to match text |
| eironn | - Split slash 125% / stab 250% |
| eryndor | - Refreshed skill effects to match text |
| evie | - Refreshed skill effects; reclassified damage types |
| faramor | - Fixed Skill2 ATK 15% and Exclusive self ATK 10% |
| fay | - Added Skill2 160 damage + DEF; fixed Exclusive Vitality 25 |
| florabelle | - Fixed summon duration to 10s |
| frieren | - Fixed Ult to True 1800; rebuilt Skill1/2 rows; removed spurious DoT |
| galahad | - Fixed Ult/max damage, Skill1 AoE strikes, shield-expiry damage |
| gerda | - Fixed damage 180 / 260 / 150 + HoT and 400 shield rows |
| granny-dahnie | - Fixed Energy 40 + durations; added Haste/damage; Vitality 19; reclassified damage |
| gunnar | - Rebuilt Ult 640 / meteor 550 / DoT; fixed Skill1 80 and Invincible ally row |
| gwyneth | - Fixed 280 damage, periodic DoT, ATK SPD, DEF Pen 60 |
| hammie | - Fixed ATK duration to 5s |
| harak | - Moved devour to Skill2; dropped unsupported Skill1 invincibility; reclassified damage |
| hepler | - Added Haste 90, deduped HoT, rebuilt Exclusive invincible/cheat-death/buff rows |
| hewynn | - Fixed damage 300 and Damage taken 36% |
| himmel | - Added Skill1 unaffected + Skill2/Ex heals; moved party require |
| hodgkin | - Dropped unsupported heal-inhibitor tag |
| hugin | - Fixed Haste 10s, shields 8s, defensive rows |
| igor | - Fixed Ult 270 / Skill1 170; rebuilt heal + cheat-death + lifedrain |
| indris | - Fixed Ult to True-only + 8s silence; fixed durations; reclassified damage |
| isabella | - Fixed ATK debuff 75% 5s and Exclusive 8s |
| kafra | - Fixed Haste 5s and Supreme+ 520 |
| karma | - Portrait + audit sidecar refresh (clean in audit) |
| kazim | - Rebuilt Ult arc + Skill1/2 values; fixed Exclusive; reclassified damage |
| koko | - Added Damage taken + spear rows; fixed shield 7s |
| kordan | - Fixed confirmed skill effects against text |
| korin | - Fixed area 2, True 220, Damage taken 25%; deduped Max HP; reclassified damage |
| kruger | - Rebuilt DEF / Damage taken / shield / ATK rows |
| kulu | - Added Ex doom-bomb max-HP rider |
| laios | - Rebuilt DEF/stun, heals 500/560, summon rows |
| lamentis | - Added Max HP debuff + ATK SPD; fixed Max HP 20% |
| lenya | - Fixed Single 480 / Single 260 + Area 390 / crit + stun rows |
| lily-may | - Fixed Ult 240; rebuilt invincible / ATK-stack / True damage rows |
| lorsan | - Fixed Haste 5s, HoT 120, immunity scope |
| lucca | - Fixed Ult 240; rebuilt shield 400 + damage 150 |
| lucius | - Fixed shields 520 / 320 / 3% and damage 70 |
| lucy | - Corrected fully-ascended shield 450 -> 550; damage reclass |
| ludovic | - Corrected Ex berry heal 130 -> 150; reclassified damage |
| lumont | - Fixed taunt 4s, shield/DEF rows; removed spurious stun |
| lyca | - Added Energy/duration rows; fixed DEF debuff; fixed Focus tier |
| marcille | - Added Area blind + heal 300; fixed once-per-battle + energy rows |
| marilee | - Fixed conditions and ATK-stack conditions; fixed Focus tier |
| mehira | - Fixed Ex Skill, Skill1, Ultimate sidecar gaps |
| mikola | - Fixed sphere 12s, heal count, HoT 12%/s |
| mirael | - Fixed Area 3 and DoT 14s + conditions |
| nara | - Fixed Energy Self 750, HP-loss 5%, Physical 80, ATK 20% |
| natsu | - Added Crit 5 + Crit DMG 5 |
| nazrik | - Refreshed skill effects to match text (audit-clean) |
| nerion | - Fixed ATK buff 30% 12s and spear 220 Area |
| niru | - Refreshed skill effects to match text (audit-clean) |
| odie | - Fixed Exclusive energy target to Self |
| orion | - Refreshed skill effects (audit-clean) |
| pandora | - Triage fix + damage reclassification |
| pang | - Refreshed skill effects to match text |
| parisa | - Fixed durations to 10s |
| peggy | - Refreshed skill effects to match text |
| perseus | - Refreshed skill effects to match text |
| phraesto | - Refreshed skill effects; reclassified damage |
| pippa | - Triage fix + damage reclassification |
| ravion | - Fixed Supreme+ sidecar gaps |
| reinier | - Corrected Ex max damage to 300% per text |
| rhys | - Triage-corrected stale expectations |
| rolan | - Refreshed skill effects; damage reclass |
| rowan | - Refreshed skill effects to match text |
| saida | - Fixed DoT, removed stale Energy 240, removed spurious immunity |
| salazer | - Added missing stat-steal Self 12% permanent; fixed label/target |
| satrana | - Fixed Exclusive Self/ally splits + Energy 200 |
| scarlita | - Refreshed skill effects to match text |
| seth | - Refreshed skill effects (audit-clean) |
| shadewing | - Added missing Legendary+ Hero Focus ATK buff |
| shakir | - Triage-corrected stale expectations |
| shemira | - Fixed to True-only delivery; reclassified damage |
| silven | - Fixed to True-only; corrected Exclusive ATK |
| silvina | - Refreshed skill effects (audit-clean) |
| sinbad | - Moved mark provider to correct location |
| smokey-meerky | - Triage fix + damage reclassification |
| solise | - Removed duplicate Magic DEF; fixed values 30 / ATK 15 |
| sonja | - Fixed Ult 672 and Lifedrain row |
| soren | - Removed spurious Supreme rows; fixed value 90 |
| sylphira | - Corrected skill effects against skill text |
| taichi-agumon | - Added Max HP + 330 rows; damage reclass |
| talene | - Rebuilt Ultimate / Skill1 / Skill2 rows |
| tasi | - Refreshed skill effects (audit-clean) |
| temesia | - Removed spurious Damage-dealt buff |
| thador | - Rebuilt Ultimate rows; fixed shield 8s |
| thoran | - Captured pact recovery; triage fix |
| tilaya | - Refreshed skill effects (audit-clean) |
| twins | - Refreshed skill effects to match text |
| ulmus | - Fixed Max-HP formula + 260 value |
| vala | - Fixed buff Self + lost-HP 12% |
| valen | - Refreshed skill effects (audit-clean) |
| valka | - Removed spurious shield; fixed to True damage; reclassified damage |
| velara | - Fixed durations; removed stale Haste; fixed tier selection |
| viperian | - Fixed confirmed discrepancies; reclassified damage |
| voracia | - Refreshed skill effects (audit-clean) |
| walker | - Fixed lost-HP and mark rows |
| yamato-gabumon | - Fixed to True damage + energy; reclassified damage |
| zandrok | - Fixed Max HP target to Self |
| zanie | - Refreshed skill effects (audit-clean) |
| zorya | - Fixed ATK-stack extraction |
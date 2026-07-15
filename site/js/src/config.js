window.AFKJ = window.AFKJ || {};

window.AFKJ.config = {
  WELCOME_WARNING_KEY: "afjk-welcome-dismissed",
  VIEW_MODE_KEY: "afjk-view-mode",
  MIX_SLOT_DOUBLE_TAP_MS: 400,

  TAG_DEFINITIONS: {
    Physical: { emoji: "⚔️", cls: "chip-damage" },
    Magic: { emoji: "🪄", cls: "chip-damage" },
    "HP loss": { emoji: "💔", cls: "chip-damage" },
    Melee: { emoji: "🗡️", cls: "chip-damage" },
    Ranged: { emoji: "🏹", cls: "chip-damage" },
    "True damage": { emoji: "♾️", cls: "chip-damage" },
    Normal: { emoji: "👊", cls: "chip-damage" },
    "Magic damage": { emoji: "🪄", cls: "chip-damage" },
    "Physical damage": { emoji: "⚔️", cls: "chip-damage" },
    "Magic damage from allies": { emoji: "🪄", cls: "chip-role" },
    "Debuff on target": { emoji: "🥀", cls: "chip-debuff" },
    "Multiple debuffs on target": { emoji: "🥀", cls: "chip-debuff" },
    "CC on enemies": { emoji: "🫯", cls: "chip-cc" },
    "Temporary ally stat buffs": { emoji: "💪", cls: "chip-role" },
    "Party composition": { emoji: "👥", cls: "chip-role" },
    "Continuous damage on enemies": { emoji: "🔥", cls: "chip-debuff" },
    "Enemy defeat": { emoji: "💀", cls: "chip-role" },
    "Ally Ultimate casts": { emoji: "⚡", cls: "chip-role" },
    "Ally blessing active": { emoji: "🙏", cls: "chip-role" },
    ATK: { emoji: "💪", cls: "chip-stat" },
    "ATK SPD": { emoji: "⚡", cls: "chip-stat" },
    "ATK SPD / Haste": { emoji: "⚡", cls: "chip-stat" },
    Haste: { emoji: "💨", cls: "chip-stat" },
    Healing: { emoji: "💚", cls: "chip-heal" },
    "Healing stat": { emoji: "💚", cls: "chip-stat" },
    "Direct healing": { emoji: "💚", cls: "chip-heal" },
    HoT: { emoji: "💚", cls: "chip-heal" },
    "Healing over time": { emoji: "💚", cls: "chip-heal" },
    Shield: { emoji: "🛡️", cls: "chip-stat" },
    "Max HP": { emoji: "❤️", cls: "chip-stat" },
    Energy: { emoji: "🔋", cls: "chip-stat" },
    "DEF Penetration": { emoji: "🎯", cls: "chip-stat" },
    Penetration: { emoji: "🎯", cls: "chip-stat" },
    Crit: { emoji: "💥", cls: "chip-stat" },
    "Crit DMG Boost": { emoji: "💥", cls: "chip-stat" },
    Execution: { emoji: "🗡️", cls: "chip-stat" },
    "Life Drain": { emoji: "🩸", cls: "chip-stat" },
    Lifedrain: { emoji: "🩸", cls: "chip-stat" },
    "Physical DEF": { emoji: "🛡️", cls: "chip-stat" },
    "Phys DEF": { emoji: "🛡️", cls: "chip-stat" },
    "Magic DEF": { emoji: "🔮", cls: "chip-stat" },
    "Ranged DEF": { emoji: "🛡️", cls: "chip-stat" },
    DEF: { emoji: "🛡️", cls: "chip-stat" },
    "Basic stats": { emoji: "📈", cls: "chip-stat" },
    Vitality: { emoji: "🌿", cls: "chip-stat" },
    "Damage taken": { emoji: "🛡️", cls: "chip-stat" },
    "Damage dealt": { emoji: "⚔️", cls: "chip-stat" },
    "Ranged damage": { emoji: "🏹", cls: "chip-stat" },
    "Dodge chance": { emoji: "🛡️", cls: "chip-stat" },
    "Movement speed": { emoji: "💨", cls: "chip-stat" },
    "Attack range": { emoji: "📏", cls: "chip-stat" },
    "Ally empower": { emoji: "💪", cls: "chip-stat" },
    Exemption: { emoji: "✨", cls: "chip-stat" },
    "Debuff duration": { emoji: "⏱️", cls: "chip-stat" },
    "Crit Resist": { emoji: "💥", cls: "chip-stat" },
    Vulnerable: { emoji: "🎯", cls: "chip-stat" },
    "Crit DMG boost": { emoji: "💥", cls: "chip-stat" },
    "Fatal blow immunity": { emoji: "♻️", cls: "chip-stat" },
    Blind: { emoji: "👁️", cls: "chip-cc" },
    Disarm: { emoji: "👊", cls: "chip-cc" },
    Stun: { emoji: "💫", cls: "chip-cc" },
    "Knock back": { emoji: "↩️", cls: "chip-cc" },
    "Knock down": { emoji: "⬇️", cls: "chip-cc" },
    Bind: { emoji: "⛓️", cls: "chip-cc" },
    Silence: { emoji: "🤐", cls: "chip-cc" },
    Charm: { emoji: "💕", cls: "chip-cc" },
    Sleep: { emoji: "😴", cls: "chip-cc" },
    Taunt: { emoji: "📣", cls: "chip-cc" },
    Frighten: { emoji: "😱", cls: "chip-cc" },
    "DoT": { emoji: "🔥", cls: "chip-debuff" },
    "ally-buffer": { emoji: "📈", cls: "chip-role" },
    "ally-healer": { emoji: "💚", cls: "chip-role" },
    "ally-shielder": { emoji: "🛡️", cls: "chip-role" },
    "aoe-damage": { emoji: "💥", cls: "chip-role" },
    "aoe-healing": { emoji: "💚", cls: "chip-role" },
    "assassin": { emoji: "🎯", cls: "chip-role" },
    "battle-start-burst": { emoji: "🚀", cls: "chip-role" },
    "battle-start-ult": { emoji: "⚡", cls: "chip-role" },
    "battlefield-modification": { emoji: "🗺️", cls: "chip-role" },
    "cc-immunity": { emoji: "🔰", cls: "chip-anti-cc" },
    "cheat-death": { emoji: "♻️", cls: "chip-role" },
    "counterattack": { emoji: "↩️", cls: "chip-role" },
    interrupt: { emoji: "⛔", cls: "chip-role" },
    "dot-specialist": { emoji: "🔥", cls: "chip-role" },
    "enemy-debuffer": { emoji: "🥀", cls: "chip-role" },
    "enemy-grouping": { emoji: "🧲", cls: "chip-role" },
    "energy-provider": { emoji: "🔋", cls: "chip-role" },
    "execute": { emoji: "☠️", cls: "chip-role" },
    "high-damage-ult": { emoji: "💣", cls: "chip-role" },
    "high-initial-energy": { emoji: "🔋", cls: "chip-role" },
    "hp-scaling": { emoji: "❤️", cls: "chip-role" },
    invincibility: { emoji: "👑", cls: "chip-role" },
    "life-drain": { emoji: "🩸", cls: "chip-role" },
    "mark-target": { emoji: "🎯", cls: "chip-role" },
    "mass-cc": { emoji: "🫯", cls: "chip-role" },
    "non-ult-utility": { emoji: "🛠️", cls: "chip-role" },
    revive: { emoji: "🌱", cls: "chip-role" },
    "self-repositioner": { emoji: "💨", cls: "chip-role" },
    "static-tile-buffer": { emoji: "📍", cls: "chip-role" },
    stealth: { emoji: "🥷", cls: "chip-role" },
    summoner: { emoji: "🐾", cls: "chip-role" },
    taunt: { emoji: "📣", cls: "chip-role" },
    "temporary-stat-buffer": { emoji: "⏱️", cls: "chip-role" },
    "ultimate-cancel": { emoji: "🚫", cls: "chip-cc" },
    untargetable: { emoji: "👻", cls: "chip-role" },
    Invincible: { emoji: "👑", cls: "chip-role" },
    "DMG+CC immunity": { emoji: "🔰", cls: "chip-anti-cc" },
    "Knock up": { emoji: "⬆️", cls: "chip-cc" },
    Interrupt: { emoji: "🚫", cls: "chip-cc" },
    Displace: { emoji: "↔️", cls: "chip-cc" },
    Unaffected: { emoji: "🛡️", cls: "chip-anti-cc" },
    Steadfast: { emoji: "🛡️", cls: "chip-anti-cc" },
    Immune: { emoji: "⛔", cls: "chip-anti-cc" },
    Untargetable: { emoji: "👻", cls: "chip-anti-cc" },
    Cleanse: { emoji: "💧", cls: "chip-anti-cc" },
    "Max HP damage": { emoji: "💔", cls: "chip-damage" },
    "Max HP-based damage": { emoji: "💔", cls: "chip-damage" },
  },

  BEHAVIOR_TAG_TOOLTIPS: {
    "ally-buffer":
      "Grants meaningful offensive or defensive stat buffs to allies.",
    "ally-healer":
      "Restores ally HP directly or via healing over time as a core role.",
    "ally-shielder":
      "Grants shields to allies as a significant part of the kit.",
    "aoe-damage":
      "Deals substantial multi-target or area damage on a regular basis.",
    "aoe-healing":
      "Heals multiple allies or wide ally groups, not only single-target.",
    "assassin":
      "Built to pick off isolated or backline targets with burst damage.",
    "battle-start-burst":
      "Deals damage to one or more units in the first ~2–3s of battle.",
    "battle-start-ult":
      "Casts ultimate or reaches full energy unusually early in the fight.",
    "battlefield-modification":
      "Adds physical obstacles or transforms the map layout.",
    "cc-immunity":
      "Grants self or allies immunity to crowd control as a defining mechanic.",
    "cheat-death":
      "Survives a would-be defeat or critical HP threshold via self-recovery.",
    "counterattack":
      "Punishes enemies for attacking with reactive damage or effects.",
    "interrupt":
      "Applies hard shutdown effects such as Silence or Interrupt.",
    "dot-specialist":
      "Relies on damage over time or recurring tick damage as a primary pattern.",
    "enemy-debuffer":
      "Applies meaningful stat or combat debuffs to enemies as a core output.",
    "enemy-grouping":
      "Pulls, pushes, or clusters enemies to set up follow-up damage or CC.",
    "energy-provider":
      "Grants Energy to allies or routinely accelerates ally ultimates.",
    execute:
      "Finishes low-HP enemies or scales damage strongly on wounded targets.",
    "high-damage-ult":
      "Ultimate is the main damage spike and a large share of total output.",
    "high-initial-energy":
      "Ultimate starts with high Initial Energy when fully built (~fast fill).",
    "hp-scaling":
      "Damage, survivability, or effects scale strongly with HP values.",
    invincibility:
      "Grants damage and/or control immunity windows to self or allies.",
    "life-drain":
      "Sustains through lifesteal or HP recovery tied to dealing damage.",
    "mark-target":
      "Marks or designates units so allies or self can focus amplified damage.",
    "mass-cc":
      "Applies crowd control to multiple enemies or wide areas reliably.",
    "non-ult-utility":
      "Strong combat value from non-ultimate skills without relying on the ultimate.",
    revive: "Brings defeated allies back to the fight; not self-survival.",
    "self-repositioner":
      "Regularly moves self across the grid via jumps, dashes, or teleports.",
    "static-tile-buffer":
      "Buffs an ally only while they remain on a specific placement tile.",
    stealth:
      "Enters hidden or untargetable states to avoid focus or enable picks.",
    summoner:
      "Fields persistent summons or companions that contribute in combat.",
    taunt:
      "Forces enemies to attack the hero or redirects enemy focus onto them.",
    "temporary-stat-buffer":
      "Grants at least one temporary ally stat buff that can end before battle does.",
    "ultimate-cancel":
      "Cancels or interrupts enemy ultimates when they begin casting.",
    untargetable:
      "Routinely becomes untargetable by enemy skills during normal gameplay.",
  },

  TARGETING_DEFINITIONS: {
    "single target": { emoji: "🎯", cls: "chip-target" },
    "multiple targets": { emoji: "👥", cls: "chip-target" },
    "all units": { emoji: "🌐", cls: "chip-target" },
    area: { emoji: "⭕", cls: "chip-target" },
    path: { emoji: "〰️", cls: "chip-target" },
    arc: { emoji: "📐", cls: "chip-target" },
    self: { emoji: "🪞", cls: "chip-target" },
    allies: { emoji: "🤝", cls: "chip-target" },
    enemies: { emoji: "☠️", cls: "chip-target" },
    global: { emoji: "🌍", cls: "chip-target" },
    "on skill": { emoji: "⏱️", cls: "chip-target" },
    "all summons": { emoji: "🐾", cls: "chip-target" },
    "owned summons": { emoji: "🐾", cls: "chip-target" },
    "summons only": { emoji: "🐾", cls: "chip-target" },
  },

  ROLE_CATEGORY_META: {
    damage_dealer: {
      label: "Damage dealer",
      emoji: "⚔️",
      className: "badge-role-damage-dealer",
    },
    specialist: {
      label: "Specialist",
      emoji: "🎭",
      className: "badge-role-specialist",
    },
    support: {
      label: "Support",
      emoji: "🤝",
      className: "badge-role-support",
    },
    tank: {
      label: "Tank",
      emoji: "🛡️",
      className: "badge-role-tank",
    },
  },

  // Prydwen role icons
  ROLE_CATEGORY_ICONS: {
    damage_dealer: {
      viewBox: "0 0 448 512",
      path:
        "M192 0c17.7 0 32 14.3 32 32l0 112-64 0 0-112c0-17.7 14.3-32 32-32zM64 64c0-17.7 14.3-32 32-32s32 14.3 32 32l0 80-64 0 0-80zm192 0c0-17.7 14.3-32 32-32s32 14.3 32 32l0 96c0 17.7-14.3 32-32 32s-32-14.3-32-32l0-96zm96 64c0-17.7 14.3-32 32-32s32 14.3 32 32l0 64c0 17.7-14.3 32-32 32s-32-14.3-32-32l0-64zm-96 88l0-.6c9.4 5.4 20.3 8.6 32 8.6c13.2 0 25.4-4 35.6-10.8c8.7 24.9 32.5 42.8 60.4 42.8c11.7 0 22.6-3.1 32-8.6l0 8.6c0 52.3-25.1 98.8-64 128l0 96c0 17.7-14.3 32-32 32l-160 0c-17.7 0-32-14.3-32-32l0-78.4c-17.3-7.9-33.2-18.8-46.9-32.5L69.5 357.5C45.5 333.5 32 300.9 32 267l0-27c0-35.3 28.7-64 64-64l88 0c22.1 0 40 17.9 40 40s-17.9 40-40 40l-56 0c-8.8 0-16 7.2-16 16s7.2 16 16 16l56 0c39.8 0 72-32.2 72-72z",
    },
    specialist: {
      viewBox: "0 0 512 512",
      path:
        "M288 32c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 11.5c0 49.9-60.3 74.9-95.6 39.6L120.2 75C107.7 62.5 87.5 62.5 75 75s-12.5 32.8 0 45.3l8.2 8.2C118.4 163.7 93.4 224 43.5 224L32 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l11.5 0c49.9 0 74.9 60.3 39.6 95.6L75 391.8c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l8.2-8.2c35.3-35.3 95.6-10.3 95.6 39.6l0 11.5c0 17.7 14.3 32 32 32s32-14.3 32-32l0-11.5c0-49.9 60.3-74.9 95.6-39.6l8.2 8.2c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3l-8.2-8.2c-35.3-35.3-10.3-95.6 39.6-95.6l11.5 0c17.7 0 32-14.3 32-32s-14.3-32-32-32l-11.5 0c-49.9 0-74.9-60.3-39.6-95.6l8.2-8.2c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0l-8.2 8.2C348.3 118.4 288 93.4 288 43.5L288 32zM176 224a48 48 0 1 1 96 0 48 48 0 1 1 -96 0zm128 56a24 24 0 1 1 0 48 24 24 0 1 1 0-48z",
    },
    support: {
      viewBox: "0 0 512 512",
      path:
        "M184 48l144 0c4.4 0 8 3.6 8 8l0 40L176 96l0-40c0-4.4 3.6-8 8-8zm-56 8l0 40L64 96C28.7 96 0 124.7 0 160L0 416c0 35.3 28.7 64 64 64l384 0c35.3 0 64-28.7 64-64l0-256c0-35.3-28.7-64-64-64l-64 0 0-40c0-30.9-25.1-56-56-56L184 0c-30.9 0-56 25.1-56 56zm96 152c0-8.8 7.2-16 16-16l32 0c8.8 0 16 7.2 16 16l0 48 48 0c8.8 0 16 7.2 16 16l0 32c0 8.8-7.2 16-16 16l-48 0 0 48c0 8.8-7.2 16-16 16l-32 0c-8.8 0-16-7.2-16-16l0-48-48 0c-8.8 0-16-7.2-16-16l0-32c0-8.8 7.2-16 16-16l48 0 0-48z",
    },
    tank: {
      viewBox: "0 0 512 512",
      path:
        "M256 0c4.6 0 9.2 1 13.4 2.9L457.7 82.8c22 9.3 38.4 31 38.3 57.2c-.5 99.2-41.3 280.7-213.6 363.2c-16.7 8-36.1 8-52.8 0C57.3 420.7 16.5 239.2 16 140c-.1-26.2 16.3-47.9 38.3-57.2L242.7 2.9C246.8 1 251.4 0 256 0z",
    },
  },

  ROLE_FILTER_ORDER: ["damage_dealer", "specialist", "support", "tank"],

  REPLACEMENT_CATEGORY_ICONS: {
    "Best overall replacement": "🏆",
    "Buffs on allies": "🔼",
    "Energy provider": "🔋",
    Healing: "💚",
    "Similar Skills": "♊️",
    Damage: "⚔️",
    "Debuffs on enemies": "🥀",
    "Crowd Control": "⛓️",
  },

  MIX_FOCUS_CONFIG_KEYS: {
    cc: "cc",
    ccImmunity: "cc_immunity",
    sustain: "sustain",
    speed: "speed",
    noUltimate: "no_ultimate",
  },

  MIX_FOCUS_TAG_DEFAULTS: {
    cc_immunity: {
      "cc-immunity": 7.0,
      "DMG+CC immunity": 6.0,
      Immune: 5.0,
      Unaffected: 5.0,
    },
  },
};

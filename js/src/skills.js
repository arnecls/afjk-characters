window.AFKJ = window.AFKJ || {};

(function () {
  const utils = window.AFKJ.utils;
  const chips = window.AFKJ.chips;
  const escapeHtml = utils.escapeHtml.bind(utils);

  const SKILL_META_EMOJI = {
    Cooldown: "⏱️",
    "Initial Cooldown": "⏳",
    "Skill Range": "📏",
    "Initial Energy": "🔋",
  };

  const SKILL_META_ORDER = [
    "Cooldown",
    "Initial Cooldown",
    "Skill Range",
    "Initial Energy",
  ];

  const SKILL_CARD_DAMAGE_KEYS = [
    "HP loss",
    "Max HP damage",
    "Max HP-based damage",
    "True damage",
    "Physical",
    "Magic",
    "DoT",
  ];

  const SKILL_CARD_CC_KEYS = Object.keys(window.AFKJ.config.TAG_DEFINITIONS)
    .filter(function (key) {
      return chips.isCcChipClass(window.AFKJ.config.TAG_DEFINITIONS[key].cls);
    })
    .sort(function (a, b) {
      return b.length - a.length;
    });

  const SKILL_CARD_HEX_ICONS = {
    ultimate: "🌟",
    skill1: "💫",
    skill2: "💫",
    skill3: "🗡️",
    skill4: "⚔️",
    skill5: "✨",
  };

  const SKILL_SCALING_DURATION_MOD_RE =
    /(\d+(?:\.\d+)?)\s*(\((?:SP-based|HP[- ]based|ATK[- ]based)\))\s*s\b/gi;

  const SKILL_SCALING_MODIFIERS = [
    {
      re: /\(SP-based\)/gi,
      emoji: "💡",
      tooltip: "This number is based on skill power.",
    },
    {
      re: /\(HP[- ]based\)/gi,
      emoji: "❤️",
      tooltip: "This number is based on HP.",
    },
    {
      re: /\(ATK[- ]based\)/gi,
      emoji: "💪",
      tooltip: "This number is based on ATK.",
    },
  ];

  function normalizeScalingDurationModifiers(text) {
    return text.replace(SKILL_SCALING_DURATION_MOD_RE, "$1s $2");
  }

  function skillScalingModifierChip(entry) {
    return chips.chipSpan(entry.emoji, "", "chip-scaling-mod", entry.tooltip);
  }

  function enrichSkillInline(text, opts) {
    opts = opts || {};
    if (!text) {
      return "";
    }
    const TAG_DEFINITIONS = window.AFKJ.config.TAG_DEFINITIONS;
    let out = escapeHtml(normalizeScalingDurationModifiers(text));
    SKILL_SCALING_MODIFIERS.forEach(function (entry) {
      out = chips.replaceOutsideChips(out, entry.re, function () {
        return skillScalingModifierChip(entry);
      });
    });
    out = chips.replaceOutsideChips(
      out,
      /\bphys(?:ical)?\s*&\s*magic\s+def\b/gi,
      function () {
        const physDef = TAG_DEFINITIONS["Phys DEF"];
        const magicDef = TAG_DEFINITIONS["Magic DEF"];
        return (
          chips.chipSpan(physDef.emoji, "Phys DEF", physDef.cls) +
          " &amp; " +
          chips.chipSpan(magicDef.emoji, "Magic DEF", magicDef.cls)
        );
      }
    );
    chips.STAT_KEYS.forEach(function (key) {
      const def = TAG_DEFINITIONS[key];
      const re = new RegExp(
        "\\b" + key.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + "\\b",
        "gi"
      );
      out = chips.replaceOutsideChips(out, re, function (match) {
        return chips.chipSpan(def.emoji, match, def.cls);
      });
    });
    chips.HEAL_CHIP_KEYS.forEach(function (key) {
      const def = TAG_DEFINITIONS[key];
      const re = new RegExp(
        "\\b" + key.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + "\\b",
        "gi"
      );
      out = chips.replaceOutsideChips(out, re, function (match) {
        return chips.chipSpan(def.emoji, match, def.cls);
      });
    });
    chips.TARGETING_PHRASES.forEach(function (entry) {
      const def = window.AFKJ.config.TARGETING_DEFINITIONS[entry.key];
      out = chips.replaceOutsideChips(out, entry.re, function (match) {
        return chips.chipSpan(def.emoji, match, def.cls);
      });
    });
    chips.ccFamilyChipKeys().forEach(function (key) {
      const def = TAG_DEFINITIONS[key];
      const re = new RegExp(
        "\\b" + key.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + "\\b",
        "gi"
      );
      out = chips.replaceOutsideChips(out, re, function (match) {
        return chips.chipSpan(def.emoji, match, def.cls);
      });
    });
    const SKILL_DURATION_PATTERNS = [
      /\d+(?:\.\d+)?\s*\+\s*\d+(?:\.\d+)?\s*s\b/gi,
      /\d+(?:\.\d+)?\s*-\s*\d+(?:\.\d+)?\s*s\b/gi,
      /\d+(?:\.\d+)?\s*s\b/gi,
    ];
    SKILL_DURATION_PATTERNS.forEach(function (re) {
      out = chips.replaceOutsideChips(out, re, function (match) {
        return (
          '<span class="skill-inline-time">⏱️ ' +
          escapeHtml(match) +
          "</span>"
        );
      });
    });
    if (opts.boldNumbers) {
      out = chips.boldSkillNumericTokens(out);
    }
    return out;
  }

  function skillDetailPhases(card) {
    const passive = (card.passive || "").trim();
    const active = (card.active || "").trim();
    const phases = [];
    if (passive) {
      phases.push({ label: "passive", body: passive });
    }
    if (active) {
      phases.push({ label: "active", body: active });
    }
    if (phases.length === 0 && card.description) {
      phases.push({ label: "description", body: card.description });
    }
    return phases;
  }

  function formatSkillDetail(card) {
    const title = card.name || card.label || "Skill";
    let headerHtml =
      '<div class="skill-popover-header">' +
      '<button type="button" class="skill-popover-close" aria-label="Close">' +
      "×</button>" +
      '<h4 id="skill-popover-title" class="skill-popover-title">' +
      escapeHtml(title) +
      "</h4>";
    if (card.unlock) {
      headerHtml +=
        '<p class="skill-popover-unlock">🔓 <em>' +
        escapeHtml(card.unlock) +
        "</em></p>";
    }

    const meta = card.meta || {};
    const metaItems = [];
    SKILL_META_ORDER.forEach(function (label) {
      if (meta[label]) {
        metaItems.push(
          '<span class="skill-popover-meta-item">' +
          SKILL_META_EMOJI[label] +
          " " +
          escapeHtml(label) +
          ": " +
          escapeHtml(meta[label]) +
          "</span>"
        );
      }
    });
    if (metaItems.length) {
      headerHtml +=
        '<div class="skill-popover-meta">' + metaItems.join("") + "</div>";
    }

    headerHtml += "</div>";

    let scrollHtml = '<div class="skill-popover-scroll">';

    const phases = skillDetailPhases(card);
    if (phases.length) {
      scrollHtml += '<div class="skill-popover-body">';
      phases.forEach(function (phase) {
        if (phase.label === "passive") {
          scrollHtml +=
            '<p class="skill-popover-phase">' +
            '<span class="skill-popover-phase-label">📖 <strong>Passive</strong></span> ' +
            enrichSkillInline(phase.body, { boldNumbers: true }) +
            "</p>";
        } else if (phase.label === "active") {
          scrollHtml +=
            '<p class="skill-popover-phase">' +
            '<span class="skill-popover-phase-label">⚡ <strong>Active</strong></span> ' +
            enrichSkillInline(phase.body, { boldNumbers: true }) +
            "</p>";
        } else {
          scrollHtml +=
            '<p class="skill-popover-phase">' +
            enrichSkillInline(phase.body, { boldNumbers: true }) +
            "</p>";
        }
      });
      scrollHtml += "</div>";
    }

    const levels = card.levels || [];
    if (levels.length) {
      scrollHtml += '<ul class="skill-popover-levels">';
      levels.forEach(function (level) {
        const levelLabel = level.unlock
          ? "Level " + level.level + " — " + level.unlock
          : "Level " + level.level;
        scrollHtml +=
          "<li><span class=\"skill-popover-level-label\">🔼 " +
          escapeHtml(levelLabel) +
          ":</span> " +
          enrichSkillInline(level.text || "", { boldNumbers: true }) +
          "</li>";
      });
      scrollHtml += "</ul>";
    }

    scrollHtml += "</div>";
    return headerHtml + scrollHtml;
  }

  function skillCardData(category) {
    const state = window.AFKJ.state;
    if (!state.detailHero || !state.detailHero.sections || !state.detailHero.sections.skillCards) {
      return null;
    }
    const cards = state.detailHero.sections.skillCards;
    for (let i = 0; i < cards.length; i++) {
      if (cards[i].category === category) {
        return cards[i];
      }
    }
    return null;
  }

  function skillCardHexPoints(scale) {
    const cx = 50;
    const cy = 57.5;
    const outer = [
      [50, 3],
      [97, 29.75],
      [97, 85.25],
      [50, 112],
      [3, 85.25],
      [3, 29.75],
    ];
    return outer
      .map(function (point) {
        const x = cx + (point[0] - cx) * scale;
        const y = cy + (point[1] - cy) * scale;
        return x + "," + y;
      })
      .join(" ");
  }

  function skillCardHexIcon(category) {
    return SKILL_CARD_HEX_ICONS[category] || "";
  }

  function renderSkillCardHex(category) {
    const patternId = "skill-hex-stripe-" + category;
    const outerPoints = skillCardHexPoints(1);
    const innerPoints = skillCardHexPoints(0.84);
    const icon = skillCardHexIcon(category);
    const iconHtml = icon
      ? '<span class="skill-card-hex-icon" aria-hidden="true">' +
      escapeHtml(icon) +
      "</span>"
      : "";
    return (
      '<div class="skill-card-hex" aria-hidden="true">' +
      '<svg class="skill-card-hex-svg" viewBox="-6 -6 112 127" preserveAspectRatio="xMidYMid meet">' +
      "<defs>" +
      '<pattern id="' +
      patternId +
      '" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">' +
      '<rect width="5" height="5" fill="var(--skill-card-hex-fill)"></rect>' +
      '<rect width="2.5" height="5" fill="var(--skill-card-hex-stripe)"></rect>' +
      "</pattern></defs>" +
      '<polygon class="skill-card-hex-fill" points="' +
      outerPoints +
      '" fill="url(#' +
      patternId +
      ')"></polygon>' +
      '<polygon class="skill-card-hex-border-outer" points="' +
      outerPoints +
      '"></polygon>' +
      '<polygon class="skill-card-hex-border-inner" points="' +
      innerPoints +
      '"></polygon>' +
      "</svg>" +
      iconHtml +
      "</div>"
    );
  }

  function renderSkillCards(cards, hero) {
    if (!cards || !cards.length) {
      return "";
    }

    const factionKey = hero ? utils.factionDataKey(hero.faction) : "";
    const factionAttr = factionKey
      ? ' data-faction="' + escapeHtml(factionKey) + '"'
      : "";

    let html = '<div class="skill-card-grid">';
    cards.forEach(function (card) {
      const tags = card.tags || card.effects || [];
      html +=
        '<div class="skill-card" data-skill-category="' +
        escapeHtml(card.category) +
        '"' +
        factionAttr +
        ' role="button" tabindex="0" aria-expanded="false" ' +
        'aria-haspopup="dialog">';
      html += '<div class="skill-card-headline">';
      html +=
        '<h4 class="skill-card-title">' + escapeHtml(card.label) + "</h4>";
      html += renderSkillCardHex(card.category);
      html += "</div>";
      html += '<div class="skill-card-content">';
      if (card.summary) {
        html +=
          '<p class="skill-card-summary">' +
          escapeHtml(card.summary) +
          "</p>";
      }
      if (tags.length) {
        html +=
          '<div class="skill-card-tags">' +
          chips.renderSkillCardTags(tags) +
          "</div>";
      }
      html += "</div></div>";
    });
    html += "</div>";
    return html;
  }

  function skillCardChipKey(raw) {
    const text = skillCardTagLabel(raw);
    if (!text) {
      return "";
    }
    let tag = text.trim();
    if (!tag) {
      return "";
    }
    const tierMatch = tag.match(
      /\s*\((legendary\+|mythic\+|supreme\+|ex\+\d+)\)\s*$/i
    );
    let tierKey = "";
    if (tierMatch) {
      tierKey = ":" + tierMatch[1].toLowerCase();
      tag = tag.slice(0, tierMatch.index).trim();
    }
    const singleMatch = tag.match(/\s*(?:—|–)\s*single target\s*$/i);
    let singleKey = "";
    if (singleMatch) {
      singleKey = ":single target";
      tag = tag.slice(0, singleMatch.index).trim();
    }
    const areaMatch = tag.match(
      /\s*(?:—|–)\s*(area|arc|all units|multiple targets|path)\s*$/i
    );
    let areaKey = "";
    if (areaMatch) {
      areaKey = ":" + areaMatch[1].trim().toLowerCase();
      tag = tag.slice(0, areaMatch.index).trim();
    }
    let selfKey = "";
    if (/\s*(?:—|–)\s*self\s*$/i.test(tag)) {
      selfKey = ":self";
      tag = tag.replace(/\s*(?:—|–)\s*self\s*$/i, "").trim();
    }
    tag = tag.replace(/\s*(?:—|–)\s*(?:owned|summons?)\s*$/i, "").trim();
    tag = tag.toLowerCase();
    const targetingKey = selfKey || areaKey || singleKey;

    if (chips.isStatModifierLabel(tag)) {
      return tag + targetingKey + tierKey;
    }

    let i;
    for (i = 0; i < chips.STAT_KEYS.length; i++) {
      const stat = chips.STAT_KEYS[i].toLowerCase();
      if (tag === stat || tag.indexOf(stat + " ") === 0) {
        return stat + targetingKey + tierKey;
      }
    }
    for (i = 0; i < SKILL_CARD_DAMAGE_KEYS.length; i++) {
      const dt = SKILL_CARD_DAMAGE_KEYS[i].toLowerCase();
      if (tag === dt || tag.indexOf(dt + " ") === 0) {
        return dt + tierKey;
      }
    }
    for (i = 0; i < SKILL_CARD_CC_KEYS.length; i++) {
      const cc = SKILL_CARD_CC_KEYS[i].toLowerCase();
      if (tag === cc || tag.indexOf(cc + " ") === 0) {
        return cc;
      }
    }
    if (tag === "hot" || tag === "healing over time" || tag.indexOf("healing over time") === 0) {
      return "hot" + targetingKey + tierKey;
    }
    if (tag === "direct healing" || tag.indexOf("direct healing") === 0) {
      return "direct healing" + targetingKey + tierKey;
    }
    if (tag.indexOf("healing") !== -1 && tag.indexOf("over time") === -1) {
      return "direct healing" + targetingKey + tierKey;
    }
    if (tag.indexOf("healing") !== -1 && tag.indexOf("over time") !== -1) {
      return "hot" + targetingKey + tierKey;
    }
    const base = tag.replace(/\s*\([^)]*\)/g, "").trim();
    return base + targetingKey + tierKey;
  }

  function skillCardTagLabel(tag) {
    if (typeof tag === "string") {
      return tag;
    }
    return tag && tag.label ? tag.label : "";
  }

  function renderSkillCardTags(tags) {
    if (!tags || !tags.length) {
      return "";
    }

    const seen = new Set();
    let html = "";
    tags.forEach(function (tag) {
      const label = skillCardTagLabel(tag);
      const key = skillCardChipKey(label);
      if (!key || seen.has(key)) {
        return;
      }
      seen.add(key);
      const polarity = typeof tag === "object" && tag.polarity ? tag.polarity : "";
      const chip = chips.chipifySkillCardTag(label, polarity);
      if (chip) {
        html += chip;
      }
    });
    return html;
  }

  // Export module API to window.AFKJ.skills
  window.AFKJ.skills = {
    enrichSkillInline: enrichSkillInline,
    skillDetailPhases: skillDetailPhases,
    formatSkillDetail: formatSkillDetail,
    skillCardData: skillCardData,
    renderSkillCards: renderSkillCards,
    skillCardChipKey: skillCardChipKey,
    skillCardTagLabel: skillCardTagLabel,
    renderSkillCardTags: renderSkillCardTags,
  };

  // Add renderSkillCardTags and chipifySkillCardTag into window.AFKJ.chips for compatibility
  window.AFKJ.chips.renderSkillCardTags = renderSkillCardTags;
})();

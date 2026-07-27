window.AFKJ = window.AFKJ || {};

(function () {
  const utils = window.AFKJ.utils;
  const config = window.AFKJ.config;

  const escapeHtml = utils.escapeHtml.bind(utils);

  const QUALITY_CLASS = {
    high: "chip-q-high",
    average: "chip-q-medium",
    low: "chip-q-low",
  };

  const SKILL_OVERVIEW_SPEED_LABELS = {
    speed: true,
    "first cast speed": true,
  };

  const SPEED_CLASS = {
    slow: "chip-s-slow",
    average: "chip-s-normal",
    fast: "chip-s-fast",
  };

  const SPEED_EMOJI = {
    slow: "🐢",
    average: "🚶",
    fast: "🚀",
  };

  const QUALITY_EMOJI = {
    high: "⬆️",
    average: "➡️",
    low: "⬇️",
  };

  const CC_DURATION_LABEL = {
    low: "short",
    average: "average",
    high: "long",
  };

  const QUALITY_TOOLTIPS = {
    high: "Top third across the roster for this effect.",
    average: "Middle band across the roster with the same effect label.",
    low: "Below average across the roster for this effect type.",
  };

  const CLASS_RANK_TOOLTIPS = {
    high: "Top third within this hero's class.",
    average: "Middle third within this hero's class.",
    low: "Bottom third within this hero's class.",
  };

  const SPEED_TOOLTIPS = {
    slow: "Slow to cast: longer cooldown, initial delay, or ultimate energy fill time.",
    average: "Typical cast timing for this skill group across the roster.",
    fast: "Quick to cast: short delay, low cooldown, or battle-start override.",
  };

  // Base Unit.WalkSpeed tiers (orthogonal to cast-speed pills above).
  const WALK_SPEED_STYLE = {
    zero: "chip-s-slow",
    slow: "chip-s-slow",
    normal: "chip-s-normal",
    fast: "chip-s-fast",
    veryfast: "chip-s-fast",
  };

  const WALK_SPEED_EMOJI = {
    zero: "🛑",
    slow: "🐢",
    normal: "🚶",
    fast: "💨",
    veryfast: "⚡",
  };

  const WALK_SPEED_TOOLTIPS = {
    zero: "Base walk speed: zero (does not walk).",
    slow: "Base walk speed: slow.",
    normal: "Base walk speed: normal.",
    fast: "Base walk speed: fast.",
    veryfast: "Base walk speed: very fast.",
  };

  const SIGNATURE_FUEL_TOOLTIP = "Signature skill casts slowly; Haste and Energy recovery buffs are especially valuable.";

  const TARGETING_RANK = {
    "all units": 70,
    global: 65,
    area: 60,
    path: 55,
    arc: 50,
    "multiple targets": 40,
    allies: 35,
    enemies: 35,
    "single target": 30,
    self: 20,
  };

  const MOVEMENT_DEFINITIONS = {
    stationary: { emoji: "📍", cls: "chip-movement" },
    moving: { emoji: "🏃", cls: "chip-movement" },
    "mostly stationary": { emoji: "🚶", cls: "chip-movement" },
    "high movement": { emoji: "💨", cls: "chip-movement" },
    "moving / stationary": { emoji: "↔️", cls: "chip-movement" },
  };

  const MOVEMENT_KEYS = Object.keys(MOVEMENT_DEFINITIONS).sort(function (a, b) {
    return b.length - a.length;
  });

  const TARGETING_PHRASES = [
    { re: /\bMultiple targets\b/gi, key: "multiple targets" },
    { re: /\bSingle target\b/gi, key: "single target" },
    { re: /\bAll units\b/gi, key: "all units" },
    { re: /\bEnemies\b/gi, key: "enemies" },
    { re: /\bGlobal\b/gi, key: "global" },
    { re: /\bOn Skill\b/gi, key: "on skill" },
    { re: /\bAll summons\b/gi, key: "all summons" },
    { re: /\bOwned summons\b/gi, key: "owned summons" },
    { re: /\bSummons only\b/gi, key: "owned summons" },
    { re: /\bArea\b/g, key: "area" },
    { re: /\bArc\b/g, key: "arc" },
    { re: /\bpath\b/gi, key: "path" },
    { re: /\bSelf\b/g, key: "self" },
  ];

  const STAT_KEYS = Object.keys(config.TAG_DEFINITIONS)
    .filter(function (key) {
      const cls = config.TAG_DEFINITIONS[key].cls;
      return cls && cls.indexOf("chip-stat") !== -1;
    })
    .sort(function (a, b) {
      return b.length - a.length;
    });

  const HEAL_CHIP_KEYS = ["Direct healing", "Healing over time", "HoT", "Healing"]
    .sort(function (a, b) {
      return b.length - a.length;
    });

  function healingChipDisplay(text) {
    if (text === "Healing over time") {
      return "HoT";
    }
    return text;
  }

  function tryMergeTrailingLabel(before, indicator) {
    const match = before.match(/(^|[\s,])([\w][\w\s]*?)\s+$/);
    if (!match) {
      return null;
    }
    const prefix = before.slice(0, match.index) + match[1];
    const label = match[2].trim();
    const merged = window.AFKJ.chips.mergeLabelWithIndicator(label, indicator.trim());
    if (!merged) {
      return null;
    }
    return escapeHtml(prefix) + merged;
  }

  function renderCharacterPill(name) {
    const utils = window.AFKJ.utils;
    const state = window.AFKJ.state;
    const hero = state.heroByName[name];
    if (!hero) {
      return escapeHtml(name);
    }
    const factionKey = utils.factionDataKey(hero.faction);
    const factionClass = utils.factionClass(hero.faction);
    const portraitSrc = utils.assetUrl(utils.characterPortraitPath(hero));
    const href = utils.escapeHtml(utils.heroUrl(hero.slug));
    const slugAttr = utils.escapeHtml(hero.slug);
    const nameHtml = utils.escapeHtml(name);
    return (
      '<a href="' +
      href +
      '" class="character-pill hero-link ' +
      factionClass +
      '" data-faction="' +
      utils.escapeHtml(factionKey) +
      '" data-slug="' +
      slugAttr +
      '">' +
      '<span class="character-pill-hex" aria-hidden="true">' +
      '<span class="character-pill-hex-wrap">' +
      '<span class="character-pill-hex-inner">' +
      '<img class="character-pill-hex-icon" src="' +
      utils.escapeHtml(portraitSrc) +
      '" alt="" loading="lazy" onerror="this.style.opacity=0.3">' +
      "</span></span></span>" +
      '<span class="character-pill-name">' +
      nameHtml +
      "</span></a>"
    );
  }

  function renderInline(text) {
    const parts = [];
    let last = 0;
    const re = /`([^`]+)`|\[\[([^\]]+)\]\]/g;
    let match;
    while ((match = re.exec(text))) {
      const backtickLabel = match[1];
      const heroName = match[2];
      if (backtickLabel !== undefined) {
        const merged = tryMergeTrailingLabel(
          text.slice(last, match.index),
          backtickLabel
        );
        if (merged) {
          parts.push(merged);
        } else {
          parts.push(escapeHtml(text.slice(last, match.index)));
          parts.push(window.AFKJ.chips.formatTag(backtickLabel));
        }
      } else {
        parts.push(escapeHtml(text.slice(last, match.index)));
        if (heroName.indexOf("filter:") === 0) {
          parts.push(renderFilterComboChips(heroName.slice(7)));
        } else {
          parts.push(renderCharacterPill(heroName));
        }
      }
      last = match.index + match[0].length;
    }
    parts.push(escapeHtml(text.slice(last)));
    let out = parts.join("");
    out = out.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
    return out;
  }

  function conditionalTooltip(text) {
    const lower = text.toLowerCase();
    if (lower.indexOf("conditional (frequent)") !== -1) {
      return "Often applies in a fight; magnitude is not reduced.";
    }
    if (lower.indexOf("conditional (rare)") !== -1) {
      return "Situational or once per battle; magnitude is lowered by two steps.";
    }
    return "";
  }

  function chipTipAttrs(tooltip) {
    if (!tooltip) {
      return "";
    }
    return (
      ' data-tip="' +
      escapeHtml(tooltip) +
      '" tabindex="0" role="button" aria-describedby="chip-tooltip"'
    );
  }

  function chipTipHtmlAttrs(tooltipHtml) {
    if (!tooltipHtml) {
      return "";
    }
    return (
      ' data-tip-html="' +
      escapeHtml(tooltipHtml) +
      '" tabindex="0" role="button" aria-describedby="chip-tooltip"'
    );
  }

  function normalizeToken(text) {
    return text.replace(/\u200b/g, "").trim();
  }

  function normalizeSummaryText(text) {
    return text.replace(/\s+/g, " ").trim();
  }

  function splitSummarySegments(text) {
    return normalizeSummaryText(text)
      .split(/\s*(?:—|–)\s*/)
      .map(function (s) {
        return s.trim();
      })
      .filter(Boolean);
  }

  function isInsideHtmlTag(html, index) {
    const before = html.slice(0, index);
    const lastOpen = before.lastIndexOf("<");
    const lastClose = before.lastIndexOf(">");
    return lastOpen > lastClose;
  }

  function isInsideChipSpan(html, index) {
    const before = html.slice(0, index);
    const openTag = "<span class=\"chip";
    let openPos = -1;
    let searchFrom = 0;
    for (; ;) {
      const idx = before.indexOf(openTag, searchFrom);
      if (idx === -1) {
        break;
      }
      openPos = idx;
      searchFrom = idx + 1;
    }
    if (openPos === -1) {
      return false;
    }
    const closePos = before.indexOf("</span>", openPos);
    return closePos === -1 || closePos >= index;
  }

  function isInsideSpanClass(html, index, className) {
    const before = html.slice(0, index);
    const openTag = '<span class="' + className + '"';
    let openPos = -1;
    let searchFrom = 0;
    for (; ;) {
      const idx = before.indexOf(openTag, searchFrom);
      if (idx === -1) {
        break;
      }
      openPos = idx;
      searchFrom = idx + 1;
    }
    if (openPos === -1) {
      return false;
    }
    const closePos = before.indexOf("</span>", openPos);
    return closePos === -1 || closePos >= index;
  }

  function isInsideSkillInlineStat(html, index) {
    return isInsideSpanClass(html, index, "skill-inline-stat");
  }

  function isInsideSkillInlineTime(html, index) {
    return isInsideSpanClass(html, index, "skill-inline-time");
  }

  function isInsideSkillInlineNum(html, index) {
    return isInsideStrong(html, index) || isInsideSpanClass(html, index, "skill-inline-num");
  }

  function isInsideStrong(html, index) {
    const before = html.slice(0, index);
    const openPos = before.lastIndexOf("<strong");
    if (openPos === -1) {
      return false;
    }
    const closePos = before.indexOf("</strong>", openPos);
    return closePos === -1 || closePos >= index;
  }

  function boldSkillNumericTokens(html) {
    return replaceOutsideChips(
      html,
      /(?:[×x*]\s*)?[+\-−]?\d+(?:\.\d+)?(?:%|s\b)?(?:\s*[×x*÷/]\s*(?:[×x*]\s*)?[+\-−]?\d+(?:\.\d+)?(?:%|s\b)?)*/g,
      function (match) {
        return '<strong class="skill-inline-num">' + match + "</strong>";
      }
    );
  }

  function replaceOutsideChips(text, re, replacer) {
    return text.replace(re, function () {
      const args = Array.prototype.slice.call(arguments);
      const offset = args[args.length - 2];
      const match = args[0];
      if (
        isInsideHtmlTag(text, offset) ||
        isInsideChipSpan(text, offset) ||
        isInsideSkillInlineStat(text, offset) ||
        isInsideSkillInlineTime(text, offset) ||
        isInsideSkillInlineNum(text, offset)
      ) {
        return match;
      }
      return replacer.apply(null, args);
    });
  }

  function enhancePlainTargetingInHtml(html) {
    let out = html;
    TARGETING_PHRASES.forEach(function (entry) {
      out = out.replace(entry.re, function (match, offset) {
        if (
          isInsideHtmlTag(out, offset) ||
          isInsideChipSpan(out, offset)
        ) {
          return match;
        }
        const def = config.TARGETING_DEFINITIONS[entry.key];
        if (!def) {
          return match;
        }
        return window.AFKJ.chips.chipSpan(def.emoji, match, def.cls);
      });
    });
    return out;
  }

  function targetingTokenMeta(token) {
    const text = normalizeToken(token);
    if (!text) {
      return null;
    }
    const lower = text.toLowerCase();
    const def = config.TARGETING_DEFINITIONS[lower];
    if (!def) {
      return null;
    }
    return {
      emoji: def.emoji,
      text: text,
      cls: def.cls,
      rank: TARGETING_RANK[lower] || 0,
    };
  }

  function renderStackedTargetingTipHtml(metas) {
    return (
      '<div class="chip-stacked-tip">' +
      metas
        .map(function (meta) {
          return (
            '<span class="chip ' +
            meta.cls +
            '">' +
            meta.emoji +
            " " +
            escapeHtml(chipDisplayLabel(meta.text)) +
            "</span>"
          );
        })
        .join("") +
      "</div>"
    );
  }

  function renderStackedTargetingPill(tokens, tipHtmlOverride) {
    const metas = tokens
      .map(function (token) {
        return targetingTokenMeta(token);
      })
      .filter(Boolean)
      .sort(function (a, b) {
        return b.rank - a.rank;
      });
    if (!metas.length) {
      return "";
    }
    if (metas.length === 1) {
      const only = metas[0];
      return chipSpan(only.emoji, only.text, only.cls);
    }

    const segmentsHtml = metas
      .map(function (meta, index) {
        const isFirst = index === 0;
        const content = isFirst
          ? meta.emoji + " " + escapeHtml(chipDisplayLabel(meta.text))
          : meta.emoji;
        return (
          '<span class="chip-stacked-seg ' +
          meta.cls +
          (isFirst ? " chip-stacked-first" : " chip-stacked-icon") +
          '">' +
          content +
          "</span>"
        );
      })
      .join("");

    const tipHtml = tipHtmlOverride || renderStackedTargetingTipHtml(metas);
    return (
      '<span class="chip chip-stacked chip-has-tip" data-tip-html="' +
      escapeHtml(tipHtml) +
      '" tabindex="0" role="button" aria-describedby="chip-tooltip">' +
      segmentsHtml +
      "</span>"
    );
  }

  function chipifyTargetingSegment(segment) {
    const normalized = unwrapBackticks(segment.trim());
    if (!normalized) {
      return "";
    }
    const parts = normalized
      .split(/\s*,\s*/)
      .map(function (part) {
        return normalizeToken(part);
      })
      .filter(Boolean);
    if (
      parts.length > 1 &&
      parts.every(function (part) {
        return targetingTokenMeta(part);
      })
    ) {
      return renderStackedTargetingPill(parts);
    }
    return parts
      .map(function (part) {
        return tokenToHtml(part);
      })
      .join(" ");
  }

  function chipDisplayLabel(text) {
    const trimmed = (text || "").trim();
    if (!trimmed) {
      return trimmed;
    }
    if (trimmed === "Healing over time") {
      return "HoT";
    }
    const lower = trimmed.toLowerCase();
    if (lower.indexOf("conditional (frequent)") !== -1) {
      return "conditional (frequent)";
    }
    if (lower.indexOf("conditional (rare)") !== -1) {
      return "conditional (rare)";
    }
    if (trimmed === "Max HP-based damage") {
      return "Max HP damage";
    }
    const statModifierDisplay = {
      "Damage taken": "DMG taken",
      "Magic damage": "Magic DMG",
      "Damage dealt": "DMG dealt",
    };
    if (Object.prototype.hasOwnProperty.call(statModifierDisplay, trimmed)) {
      return statModifierDisplay[trimmed];
    }
    return trimmed;
  }

  function skillCardTargetingDisplayLabel(text) {
    const trimmed = (text || "").trim();
    const lower = trimmed.toLowerCase();
    const short = {
      "all units": "all",
      "multiple targets": "multiple",
      "single target": "single",
    };
    if (Object.prototype.hasOwnProperty.call(short, lower)) {
      return short[lower];
    }
    return chipDisplayLabel(trimmed);
  }

  function targetingDisplayLabel(text, skillCardDisplay) {
    if (skillCardDisplay) {
      return skillCardTargetingDisplayLabel(text);
    }
    return chipDisplayLabel(text);
  }

  function chipSpan(emoji, text, cls, tooltip) {
    const tipAttr = chipTipAttrs(tooltip);
    const tipCls = tooltip ? " chip-has-tip" : "";
    return (
      '<span class="chip ' +
      cls +
      tipCls +
      '"' +
      tipAttr +
      ">" +
      (emoji ? emoji + " " : "") +
      escapeHtml(chipDisplayLabel(text)) +
      "</span>"
    );
  }

  function behaviorTagTooltip(tag) {
    return config.BEHAVIOR_TAG_TOOLTIPS[tag] || "";
  }

  function behaviorTagDefinition(tag) {
    return config.TAG_DEFINITIONS[tag] || null;
  }

  function behaviorTagChip(tag, withTooltip) {
    const def = behaviorTagDefinition(tag);
    const emoji = def ? def.emoji : "🏷️";
    const tooltip = withTooltip ? behaviorTagTooltip(tag) : "";
    return chipSpan(emoji, tag.trim(), "chip-behavior-tag", tooltip);
  }

  function filterColumnEmoji(columnLabel) {
    const key = exactTagDefinitionKey(columnLabel);
    if (key && config.TAG_DEFINITIONS[key]) {
      return config.TAG_DEFINITIONS[key].emoji;
    }
    const dmgEmojis = {
      "Magic DMG": config.TAG_DEFINITIONS.Magic.emoji,
      "Physical DMG": config.TAG_DEFINITIONS.Physical.emoji,
      "True DMG": config.TAG_DEFINITIONS["True damage"].emoji,
    };
    return dmgEmojis[columnLabel] || "";
  }

  function behaviorTagIdForComboChip(combo, chipIndex) {
    const spec = combo.filters && combo.filters["Behavior tags"];
    if (!spec || !spec.values || !spec.values.length) {
      return null;
    }
    const chip = combo.chips[chipIndex];
    if (!chip || chip.style !== "behavior-tag") {
      return null;
    }
    let behaviorIdx = 0;
    for (let i = 0; i < chipIndex; i++) {
      if (combo.chips[i].style === "behavior-tag") {
        behaviorIdx += 1;
      }
    }
    const values = spec.values;
    return values[Math.min(behaviorIdx, values.length - 1)];
  }

  function renderFilterComboChip(chip, combo, chipIndex) {
    const cls =
      chip.style === "behavior-tag" ? "chip-behavior-tag" : "chip-filter-column";
    let emoji = "";
    let tooltip = "";
    if (chip.style === "behavior-tag") {
      const tagId = behaviorTagIdForComboChip(combo, chipIndex);
      const def = tagId ? behaviorTagDefinition(tagId) : null;
      emoji = def ? def.emoji : "🏷️";
      tooltip = tagId ? behaviorTagTooltip(tagId) : "";
    } else {
      emoji = filterColumnEmoji(chip.label);
    }
    return chipSpan(emoji, chip.label, cls, tooltip);
  }

  function renderFilterComboChips(comboId) {
    const combos = window.AFKJ.state.counterFilterCombos || {};
    const combo = combos[comboId];
    if (!combo || !combo.chips || !combo.chips.length) {
      return escapeHtml("[[filter:" + comboId + "]]");
    }
    const listFilters = window.AFKJ.listFilters;
    const href = listFilters ? listFilters.comboDeepLinkById(comboId) : "#";
    const hrefAttr = escapeHtml(href);
    return combo.chips
      .map(function (chip, chipIndex) {
        const inner = renderFilterComboChip(chip, combo, chipIndex);
        return (
          '<a href="' +
          hrefAttr +
          '" class="chip-filter-link">' +
          inner +
          "</a>"
        );
      })
      .join(" ");
  }

  function isSpeedMetricLabel(label) {
    return SKILL_OVERVIEW_SPEED_LABELS[label.toLowerCase()] || false;
  }

  function qualityIndicatorMeta(value, isCc) {
    const lower = value.toLowerCase();
    if (!QUALITY_CLASS[lower]) {
      return null;
    }
    return {
      cls: "chip-quality " + QUALITY_CLASS[lower],
      label: isCc ? CC_DURATION_LABEL[lower] : lower,
      tooltip: QUALITY_TOOLTIPS[lower],
      emoji: "",
    };
  }

  function targetingIndicatorMeta(targeting) {
    const lower = (targeting || "").trim().toLowerCase();
    if (lower === "all summons") {
      return {
        cls: "chip-target",
        label: "summons",
        tooltip: "",
        emoji: "🐾",
      };
    }
    if (
      lower === "owned summons" ||
      lower === "own summons" ||
      lower === "summon" ||
      lower === "summons only"
    ) {
      return {
        cls: "chip-target",
        label: "owned",
        tooltip: "",
        emoji: "🐾",
      };
    }
    const def = config.TARGETING_DEFINITIONS[lower];
    if (def) {
      const label =
        lower === "self"
          ? "Self"
          : lower === "all units"
            ? "All units"
            : lower === "multiple targets"
              ? "Multiple targets"
              : lower === "single target"
                ? "Single target"
                : lower === "path"
                  ? "path"
                  : targeting.trim();
      return {
        cls: def.cls,
        label: label,
        tooltip: "",
        emoji: def.emoji,
      };
    }
    return null;
  }

  function resolveIndicatorMeta(label, indicator, isCc) {
    if (isSpeedMetricLabel(label)) {
      return (
        speedIndicatorMeta(indicator) ||
        qualityIndicatorMeta(indicator, isCc)
      );
    }
    return (
      qualityIndicatorMeta(indicator, isCc) ||
      speedIndicatorMeta(indicator)
    );
  }

  function speedIndicatorMeta(value) {
    const lower = value.toLowerCase();
    if (!SPEED_CLASS[lower]) {
      return null;
    }
    return {
      cls: "chip-speed " + SPEED_CLASS[lower],
      label: lower,
      tooltip: SPEED_TOOLTIPS[lower],
      emoji: SPEED_EMOJI[lower],
    };
  }

  function walkSpeedIndicatorMeta(value) {
    const lower = String(value || "")
      .trim()
      .toLowerCase();
    if (!WALK_SPEED_STYLE[lower]) {
      return null;
    }
    return {
      cls: "chip-speed " + WALK_SPEED_STYLE[lower],
      label: lower,
      tooltip: WALK_SPEED_TOOLTIPS[lower],
      emoji: WALK_SPEED_EMOJI[lower],
    };
  }

  function movementChipMeta(label) {
    const trimmed = String(label || "").trim();
    if (!trimmed) {
      return null;
    }
    const lower = trimmed.toLowerCase();
    for (let i = 0; i < MOVEMENT_KEYS.length; i++) {
      const key = MOVEMENT_KEYS[i];
      if (lower === key.toLowerCase()) {
        const def = MOVEMENT_DEFINITIONS[key];
        return {
          emoji: def.emoji,
          text: trimmed,
          cls: def.cls,
        };
      }
    }
    return null;
  }

  function mergeMovementWithWalkSpeed(movementLabel, walkSpeed) {
    const walkMeta = walkSpeedIndicatorMeta(walkSpeed);
    if (!walkMeta) {
      return null;
    }
    const moveMeta = movementChipMeta(movementLabel);
    if (moveMeta) {
      return formatMergedIndicator(
        {
          hasIcon: true,
          emoji: moveMeta.emoji,
          text: moveMeta.text,
          cls: moveMeta.cls,
          tierSuffix: "",
        },
        walkMeta,
        false
      );
    }
    return formatMergedIndicator(
      { textOnly: movementLabel, tierSuffix: "" },
      walkMeta,
      true
    );
  }

  function isCcChipClass(cls) {
    return cls === "chip-cc";
  }

  function isCcFamilyChipClass(cls) {
    return cls === "chip-cc" || cls === "chip-anti-cc";
  }

  function ccFamilyChipKeys() {
    return Object.keys(config.TAG_DEFINITIONS)
      .filter(function (key) {
        return isCcFamilyChipClass(config.TAG_DEFINITIONS[key].cls);
      })
      .sort(function (a, b) {
        return b.length - a.length;
      });
  }

  function exactTagDefinitionKey(label) {
    const trimmed = label.trim();
    if (!trimmed) {
      return null;
    }
    if (config.TAG_DEFINITIONS[trimmed]) {
      return trimmed;
    }
    const labelLower = trimmed.toLowerCase();
    if (
      labelLower === "max hp-based damage" ||
      labelLower === "max hp damage"
    ) {
      return "Max HP damage";
    }
    for (const key of Object.keys(config.TAG_DEFINITIONS)) {
      if (key.toLowerCase() === labelLower) {
        return key;
      }
    }
    return null;
  }

  function isStatModifierLabel(label) {
    const t = (label || "").trim();
    return (
      t === "Damage taken" ||
      t === "Magic damage" ||
      t === "Damage dealt" ||
      t === "Energy"
    );
  }

  function effectLabelPolarity(label) {
    const trimmed = (label || "").trim().toLowerCase();
    if (trimmed.endsWith(" debuff")) {
      return "debuff";
    }
    if (trimmed.endsWith(" buff")) {
      return "buff";
    }
    return null;
  }

  const BUFF_DISPLAY_EFFECT_CHIPS = {
    "Damage taken": { emoji: "🛡️", cls: "chip-stat" },
    "Magic damage": { emoji: "🪄", cls: "chip-stat" },
    "Damage dealt": { emoji: "⚔️", cls: "chip-stat" },
    "Ranged damage": { emoji: "🏹", cls: "chip-stat" },
    "Basic stats": { emoji: "📈", cls: "chip-stat" },
  };

  function effectChipClassForPolarity(polarity, fallbackCls) {
    if (polarity === "debuff") {
      return "chip-debuff";
    }
    if (polarity === "buff") {
      if (fallbackCls && fallbackCls.indexOf("chip-debuff") !== -1) {
        return "chip-stat";
      }
      if (
        !fallbackCls ||
        fallbackCls === "chip-generic" ||
        fallbackCls.indexOf("chip-stat") !== -1
      ) {
        return "chip-stat";
      }
      return fallbackCls;
    }
    return fallbackCls || "chip-generic";
  }

  function resolveLeadingChip(label, polarity) {
    const trimmed = label.trim();
    if (!trimmed) {
      return { textOnly: "", remainder: "", isCc: false };
    }

    if (polarity === "buff" && BUFF_DISPLAY_EFFECT_CHIPS[trimmed]) {
      const buff = BUFF_DISPLAY_EFFECT_CHIPS[trimmed];
      return {
        emoji: buff.emoji,
        text: trimmed,
        cls: effectChipClassForPolarity("buff", buff.cls),
        isCc: false,
        remainder: "",
      };
    }

    if (polarity === "debuff") {
      const debuffKey = exactTagDefinitionKey(trimmed);
      if (debuffKey && config.TAG_DEFINITIONS[debuffKey]) {
        const def = config.TAG_DEFINITIONS[debuffKey];
        return {
          emoji: def.emoji,
          text: debuffKey,
          cls: effectChipClassForPolarity("debuff", def.cls),
          isCc: isCcChipClass(def.cls),
          remainder: "",
        };
      }
    }

    const exactKey = exactTagDefinitionKey(trimmed);
    if (exactKey) {
      const def = config.TAG_DEFINITIONS[exactKey];
      const resolvedPolarity = polarity || effectLabelPolarity(exactKey);
      return {
        emoji: def.emoji,
        text: exactKey,
        cls: effectChipClassForPolarity(resolvedPolarity, def.cls),
        isCc: isCcChipClass(def.cls),
        remainder: "",
      };
    }

    const ccKeys = ccFamilyChipKeys();
    const labelLower = trimmed.toLowerCase();
    for (let i = 0; i < ccKeys.length; i++) {
      const cc = ccKeys[i];
      const ccLower = cc.toLowerCase();
      if (
        labelLower === ccLower ||
        labelLower.startsWith(ccLower + " ") ||
        labelLower.startsWith(ccLower + " HP")
      ) {
        const def = config.TAG_DEFINITIONS[cc];
        return {
          emoji: def.emoji,
          text: cc,
          cls: def.cls,
          isCc: isCcChipClass(def.cls),
          remainder: trimmed.slice(cc.length),
        };
      }
    }

    for (let i = 0; i < STAT_KEYS.length; i++) {
      const stat = STAT_KEYS[i];
      const statLower = stat.toLowerCase();
      if (labelLower === statLower || labelLower.startsWith(statLower + " ")) {
        const def = config.TAG_DEFINITIONS[stat];
        return {
          emoji: def.emoji,
          text: stat,
          cls: effectChipClassForPolarity(polarity, def.cls),
          isCc: isCcChipClass(def.cls),
          remainder: trimmed.slice(stat.length),
        };
      }
    }

    for (let i = 0; i < HEAL_CHIP_KEYS.length; i++) {
      const heal = HEAL_CHIP_KEYS[i];
      const healLower = heal.toLowerCase();
      if (labelLower === healLower || labelLower.startsWith(healLower + " ")) {
        const def = config.TAG_DEFINITIONS[heal];
        return {
          emoji: def.emoji,
          text: healingChipDisplay(heal),
          cls: def.cls,
          isCc: false,
          remainder: trimmed.slice(heal.length),
        };
      }
    }

    return { textOnly: trimmed, remainder: "", isCc: false };
  }

  function effectChipRemainder(remainder) {
    const trimmed = (remainder || "").trim().toLowerCase();
    if (trimmed === "buff" || trimmed === "debuff") {
      return "";
    }
    if (!remainder) {
      return "";
    }
    const raw = remainder.trim();
    if (raw.startsWith("via") || raw.startsWith("on")) {
      return " " + raw;
    }
    if (raw.startsWith("to allies") || raw.startsWith("to summons")) {
      return " " + raw;
    }
    return remainder || "";
  }

  function shortAscensionTierName(tierName) {
    const trimmed = tierName.trim();
    if (trimmed.startsWith("(") && trimmed.endsWith(")")) {
      const core = trimmed.slice(1, -1).trim();
      const lower = core.toLowerCase();
      if (lower.startsWith("ex+")) {
        return core;
      }
      if (lower === "legendary+") {
        return "L+";
      }
      if (lower === "mythic+") {
        return "M+";
      }
      if (lower === "supreme+") {
        return "S+";
      }
      return core;
    }
    return trimmed;
  }

  function formatAscensionTierDisplay(tierSuffix) {
    if (!tierSuffix) {
      return "";
    }
    const short = shortAscensionTierName(tierSuffix);
    return (
      '<sup class="chip-tier-badge" title="Unlocks at ' +
      escapeHtml(tierSuffix) +
      '">' +
      escapeHtml(short) +
      "</sup>"
    );
  }

  function formatMergedTierSuffix(tierSuffix) {
    if (!tierSuffix) {
      return "";
    }
    return formatAscensionTierDisplay(tierSuffix);
  }

  function targetingSegmentCompact(iconOnlyTargeting, index, segmentCount) {
    if (iconOnlyTargeting) {
      return segmentCount > 1;
    }
    return index > 0;
  }

  function formatMergedIndicator(
    left,
    indicatorMeta,
    textOnlyLeft,
    iconOnlyRight,
    skillCardDisplay
  ) {
    let leftHtml;
    if (left.hasIcon) {
      leftHtml =
        '<span class="chip-merged-left ' +
        left.cls +
        '">' +
        left.emoji +
        " " +
        escapeHtml(chipDisplayLabel(left.text)) +
        formatMergedTierSuffix(left.tierSuffix) +
        "</span>";
    } else {
      const leftTipAttrs = left.tooltipHtml
        ? ' chip-has-tip"' + chipTipHtmlAttrs(left.tooltipHtml)
        : left.tooltip
          ? ' chip-has-tip"' + chipTipAttrs(left.tooltip)
          : '"';
      leftHtml =
        '<span class="chip-merged-left chip-merged-label' +
        leftTipAttrs +
        ">" +
        escapeHtml(chipDisplayLabel(left.textOnly)) +
        formatMergedTierSuffix(left.tierSuffix) +
        "</span>";
    }

    const showLabel = !iconOnlyRight;
    const emojiPart = indicatorMeta.emoji
      ? indicatorMeta.emoji + (showLabel && indicatorMeta.label ? " " : "")
      : "";
    const rightTitle =
      iconOnlyRight && indicatorMeta.label
        ? ' title="' + escapeHtml(indicatorMeta.label) + '"'
        : "";
    const rightAttrs =
      ' class="chip-merged-right ' +
      indicatorMeta.cls +
      (indicatorMeta.tooltip ? " chip-has-tip" : "") +
      '"' +
      rightTitle +
      (indicatorMeta.tooltip ? chipTipAttrs(indicatorMeta.tooltip) : "");
    const rightHtml =
      "<span" +
      rightAttrs +
      ">" +
      emojiPart +
      (showLabel
        ? escapeHtml(
          targetingDisplayLabel(indicatorMeta.label, skillCardDisplay)
        )
        : "") +
      "</span>";

    return (
      '<span class="chip chip-merged">' +
      leftHtml +
      '<span class="chip-merged-sep" aria-hidden="true">|</span>' +
      rightHtml +
      "</span>"
    );
  }

  function mergeLabelWithIndicator(label, indicator, tierSuffix, polarity) {
    const leading = resolveLeadingChip(label, polarity);
    const meta = resolveIndicatorMeta(label, indicator, leading.isCc);
    if (!meta) {
      return null;
    }
    if (leading.emoji) {
      return (
        formatMergedIndicator(
          {
            hasIcon: true,
            emoji: leading.emoji,
            text: leading.text,
            cls: leading.cls,
            tierSuffix: tierSuffix || "",
          },
          meta,
          false
        ) + escapeHtml(effectChipRemainder(leading.remainder))
      );
    }
    return formatMergedIndicator(
      { textOnly: label, tierSuffix: tierSuffix || "" },
      meta,
      true
    );
  }

  function mergeEffectWithQuality(effectLabel, qualityValue, tierSuffix, polarity) {
    const qualityMeta = qualityIndicatorMeta(
      qualityValue,
      resolveLeadingChip(effectLabel, polarity).isCc
    );
    if (!qualityMeta) {
      return null;
    }
    const leading = resolveLeadingChip(effectLabel, polarity);
    if (leading.emoji) {
      return (
        formatMergedIndicator(
          {
            hasIcon: true,
            emoji: leading.emoji,
            text: leading.text,
            cls: leading.cls,
            tierSuffix: tierSuffix || "",
          },
          qualityMeta,
          false
        ) + escapeHtml(effectChipRemainder(leading.remainder))
      );
    }
    return formatMergedIndicator(
      { textOnly: effectLabel, tierSuffix: tierSuffix || "" },
      qualityMeta,
      true
    );
  }

  function classRankIndicatorMeta(value) {
    const lower = (value || "").trim().toLowerCase();
    if (!QUALITY_CLASS[lower]) {
      return null;
    }
    return {
      cls: "chip-quality " + QUALITY_CLASS[lower],
      label: lower,
      tooltip: CLASS_RANK_TOOLTIPS[lower],
      emoji: "",
    };
  }

  function statCategoryCoversHeading(label) {
    return (label || "").replace(/ Stats$/, " stats") + " cover:";
  }

  function formatStatCategoryCoversTooltip(label, covers) {
    if (!covers || !covers.length) {
      return "";
    }
    const items = covers
      .map(function (stat) {
        return "<li>" + escapeHtml(stat) + "</li>";
      })
      .join("");
    return (
      '<div class="stat-category-covers-tip">' +
      '<p class="stat-category-covers-tip__heading">' +
      escapeHtml(statCategoryCoversHeading(label)) +
      "</p>" +
      '<ul class="stat-category-covers-tip__list">' +
      items +
      "</ul>" +
      "</div>"
    );
  }

  function renderClassRankCategoryPill(entry) {
    const qualityMeta = classRankIndicatorMeta(entry.rank);
    if (!qualityMeta) {
      return "";
    }
    return formatMergedIndicator(
      {
        textOnly: entry.label,
        tierSuffix: "",
        tooltipHtml: formatStatCategoryCoversTooltip(
          entry.label,
          entry.covers
        ),
      },
      qualityMeta,
      true
    );
  }

  function renderClassRankMergedPill(label, rank, polarity, withIcon) {
    const qualityMeta = classRankIndicatorMeta(rank);
    if (!qualityMeta) {
      return "";
    }
    if (withIcon === false) {
      return formatMergedIndicator(
        { textOnly: label, tierSuffix: "" },
        qualityMeta,
        true
      );
    }
    const leading = resolveLeadingChip(label, polarity);
    if (leading.emoji) {
      return (
        formatMergedIndicator(
          {
            hasIcon: true,
            emoji: leading.emoji,
            text: leading.text,
            cls: leading.cls,
            tierSuffix: "",
          },
          qualityMeta,
          false
        ) + escapeHtml(effectChipRemainder(leading.remainder))
      );
    }
    return formatMergedIndicator(
      { textOnly: label, tierSuffix: "" },
      qualityMeta,
      true
    );
  }

  function mergeEffectWithTargeting(effectLabel, targeting, tierSuffix, polarity) {
    const targetingMeta = targetingIndicatorMeta(targeting);
    if (!targetingMeta) {
      return null;
    }
    const leading = resolveLeadingChip(effectLabel, polarity);
    if (leading.emoji) {
      return (
        formatMergedIndicator(
          {
            hasIcon: true,
            emoji: leading.emoji,
            text: leading.text,
            cls: leading.cls,
            tierSuffix: tierSuffix || "",
          },
          targetingMeta,
          false,
          false,
          true
        ) + escapeHtml(effectChipRemainder(leading.remainder))
      );
    }
    return formatMergedIndicator(
      { textOnly: effectLabel, tierSuffix: tierSuffix || "" },
      targetingMeta,
      true,
      false,
      true
    );
  }

  function tryChipify(token) {
    const text = normalizeToken(token);
    if (!text) {
      return null;
    }
    const lower = text.toLowerCase();

    if (QUALITY_CLASS[lower]) {
      return formatTag(text);
    }
    if (lower === "signature fuel") {
      return formatTag(text);
    }

    const targeting = config.TARGETING_DEFINITIONS[lower];
    if (targeting) {
      return chipSpan(targeting.emoji, text, targeting.cls);
    }

    if (config.TAG_DEFINITIONS[text]) {
      const def = config.TAG_DEFINITIONS[text];
      return chipSpan(def.emoji, healingChipDisplay(text), def.cls);
    }
    for (const key of Object.keys(config.TAG_DEFINITIONS)) {
      if (key.toLowerCase() === lower) {
        const def = config.TAG_DEFINITIONS[key];
        return chipSpan(def.emoji, healingChipDisplay(key), def.cls);
      }
    }

    return null;
  }

  function tokenToHtml(token) {
    const chip = tryChipify(token);
    return chip !== null ? chip : escapeHtml(token.trim());
  }

  function extractChipHtml(html) {
    if (!html || html.indexOf('<span class="chip') !== 0) {
      return null;
    }
    const end = html.indexOf("</span>");
    if (end === -1) {
      return null;
    }
    return html.slice(0, end + 7);
  }

  function chipifyEffectName(name, polarity) {
    const parsed = parseEffectLabelParts(name);
    const label = parsed.base;
    const tier = parsed.tier;

    if (label.indexOf(" via ") === -1) {
      return renderStandaloneEffectChip(label, tier, polarity);
    }

    const viaIdx = label.indexOf(" via ");
    const left = label.slice(0, viaIdx).trim();
    const right = label.slice(viaIdx + 5).trim();
    const leftChip = chipifyLeadingStat(left);
    const rightChip = chipifyLeadingStat(right);
    if (leftChip !== null || rightChip !== null) {
      let leftHtml = leftChip !== null ? leftChip : escapeHtml(left);
      let rightHtml = rightChip !== null ? rightChip : escapeHtml(right);
      if (tier) {
        const leftOnly = extractChipHtml(leftHtml);
        const rightOnly = extractChipHtml(rightHtml);
        if (leftOnly) {
          leftHtml = injectTierIntoChipHtml(leftOnly, tier) + leftHtml.slice(leftOnly.length);
        } else if (rightOnly) {
          rightHtml = injectTierIntoChipHtml(rightOnly, tier) + rightHtml.slice(rightOnly.length);
        } else {
          leftHtml += formatMergedTierSuffix(tier);
        }
      }
      return leftHtml + " via " + rightHtml;
    }

    return renderStandaloneEffectChip(label, tier, polarity);
  }

  function chipifyLeadingCcType(label) {
    const ccKeys = ccFamilyChipKeys();
    const labelLower = label.toLowerCase();
    for (let i = 0; i < ccKeys.length; i++) {
      const cc = ccKeys[i];
      const ccLower = cc.toLowerCase();
      if (labelLower === ccLower) {
        return tryChipify(cc);
      }
      if (
        labelLower.startsWith(ccLower + " ") ||
        labelLower.startsWith(ccLower + " HP")
      ) {
        return tryChipify(cc) + escapeHtml(label.slice(cc.length));
      }
    }
    return null;
  }

  function chipifyLeadingStat(label) {
    const exactKey = exactTagDefinitionKey(label);
    if (exactKey) {
      return tryChipify(exactKey);
    }
    const labelLower = label.toLowerCase();
    for (let i = 0; i < STAT_KEYS.length; i++) {
      const stat = STAT_KEYS[i];
      const statLower = stat.toLowerCase();
      if (labelLower === statLower) {
        return tryChipify(stat);
      }
      if (labelLower.startsWith(statLower + " ")) {
        return tryChipify(stat) + escapeHtml(label.slice(stat.length));
      }
    }
    return null;
  }

  function unwrapBackticks(text) {
    const trimmed = text.trim();
    const match = trimmed.match(/^`([^`]+)`$/);
    return match ? match[1].trim() : trimmed;
  }

  function promoteStrongToDamageChips(html) {
    return html.replace(/<strong>([^<]+)<\/strong>/g, function (_match, name) {
      const chip = tryChipify(name.trim());
      return chip !== null ? chip : "<strong>" + name + "</strong>";
    });
  }

  const ASCENSION_TIER_SUFFIX_RE = /\s*(\((?:Legendary\+|Mythic\+|Supreme\+|EX\+\d+)\))\s*$/i;

  function parseEffectLabelParts(label) {
    let text = (label || "").trim();
    let tier = "";
    const tierMatch = text.match(ASCENSION_TIER_SUFFIX_RE);
    if (tierMatch) {
      tier = tierMatch[1];
      text = text.slice(0, tierMatch.index).trim();
    }
    return { base: text, tier: tier };
  }

  function injectTierIntoChipHtml(chipHtml, tier) {
    if (!tier || !chipHtml) {
      return chipHtml;
    }
    const closeIdx = chipHtml.lastIndexOf("</span>");
    if (closeIdx === -1) {
      return chipHtml + formatMergedTierSuffix(tier);
    }
    return (
      chipHtml.slice(0, closeIdx) +
      formatMergedTierSuffix(tier) +
      chipHtml.slice(closeIdx)
    );
  }

  function applyEffectPolarityToChipHtml(html, polarity) {
    if (!html || !polarity) {
      return html;
    }
    const cls = effectChipClassForPolarity(polarity, "chip-stat");
    return html.replace(/\bchip-(?:stat|debuff|generic|heal)\b/, cls);
  }

  function renderStandaloneEffectChip(base, tier, polarity) {
    const leading = resolveLeadingChip(base, polarity);
    if (leading.emoji) {
      return (
        '<span class="chip ' +
        leading.cls +
        '">' +
        leading.emoji +
        " " +
        escapeHtml(chipDisplayLabel(leading.text)) +
        formatMergedTierSuffix(tier) +
        escapeHtml(effectChipRemainder(leading.remainder) || "") +
        "</span>"
      );
    }
    const direct = tryChipify(base);
    if (direct) {
      return injectTierIntoChipHtml(
        applyEffectPolarityToChipHtml(direct, polarity),
        tier
      );
    }
    const ccChip = extractChipHtml(chipifyLeadingCcType(base));
    if (ccChip) {
      return injectTierIntoChipHtml(ccChip, tier);
    }
    const statChip = extractChipHtml(chipifyLeadingStat(base));
    if (statChip) {
      return injectTierIntoChipHtml(
        applyEffectPolarityToChipHtml(statChip, polarity),
        tier
      );
    }
    return (
      '<span class="chip ' +
      effectChipClassForPolarity(polarity, "chip-generic") +
      '">' +
      escapeHtml(chipDisplayLabel(base)) +
      formatMergedTierSuffix(tier) +
      "</span>"
    );
  }

  function renderSummaryEffectChip(base, tier, quality, polarity) {
    const merged = mergeEffectWithQuality(base, quality, tier, polarity) ||
      mergeLabelWithIndicator(base, quality, tier, polarity);
    if (merged) {
      return merged;
    }
    const exact = exactTagDefinitionKey(base);
    const isCc = exact ? isCcChipClass(config.TAG_DEFINITIONS[exact].cls) : false;
    const qMeta = qualityIndicatorMeta(quality || "", isCc);
    if (qMeta) {
      return formatMergedIndicator(
        { textOnly: base, tierSuffix: tier || "" },
        qMeta,
        true
      );
    }
    return renderStandaloneEffectChip(base, tier, polarity) + (quality ? " " + formatTag(quality) : "");
  }

  function summaryCardPolarity(title) {
    if (/^Debuffs provided by /i.test(title)) {
      return "debuff";
    }
    if (/^Buffs provided by /i.test(title)) {
      return "buff";
    }
    return null;
  }

  function renderEmDashLine(text, polarity) {
    const segments = splitSummarySegments(text);

    const trailingParts = [];
    let trailingQuality = null;

    function popTrailingQuality() {
      if (!segments.length) {
        return;
      }
      const raw = segments[segments.length - 1];
      const unwrapped = unwrapBackticks(raw);
      const lower = unwrapped.toLowerCase();
      if (QUALITY_CLASS[lower]) {
        trailingQuality = unwrapped;
        segments.pop();
      }
    }

    function popTrailingConditional() {
      if (!segments.length) {
        return;
      }
      const last = segments[segments.length - 1];
      if (/conditional/i.test(last)) {
        trailingParts.unshift(
          '<span class="chip chip-generic chip-has-tip"' +
          chipTipAttrs(conditionalTooltip(last)) +
          ">🎲 " +
          escapeHtml(last) +
          "</span>"
        );
        segments.pop();
      }
    }

    popTrailingConditional();
    popTrailingQuality();
    popTrailingConditional();

    const first = segments.shift();
    const parsed = parseEffectLabelParts(first);
    let firstHtml;
    if (/^Primary damage type/i.test(first)) {
      firstHtml = promoteStrongToDamageChips(renderInline(first));
    } else if (trailingQuality) {
      firstHtml = renderSummaryEffectChip(
        parsed.base,
        parsed.tier,
        trailingQuality,
        polarity
      );
    } else {
      firstHtml = renderSummaryEffectChip(parsed.base, parsed.tier, "", polarity);
    }

    const targetingTokens = [];
    segments.forEach(function (seg) {
      unwrapBackticks(seg.trim())
        .split(/\s*,\s*/)
        .forEach(function (part) {
          const normalized = normalizeToken(part);
          if (normalized && targetingTokenMeta(normalized)) {
            targetingTokens.push(normalized);
          }
        });
    });
    let targetingHtml = renderStackedTargetingPill(targetingTokens);
    if (targetingTokens.length > 1) {
      const sharedTipHtml = renderEffectTargetingStackedTipHtml(
        first,
        polarity,
        targetingTokens
      );
      firstHtml = withAnyChipTooltip(firstHtml, sharedTipHtml);
      targetingHtml = renderStackedTargetingPill(
        targetingTokens,
        sharedTipHtml
      );
    }

    return enhancePlainTargetingInHtml(
      [firstHtml, targetingHtml, trailingParts.join(" ")]
        .filter(Boolean)
        .join(" ")
    );
  }

  function renderRichLine(raw, polarity) {
    const text = normalizeSummaryText(raw);

    if (/\s*(?:—|–)\s*/.test(text)) {
      return renderEmDashLine(text, polarity);
    }

    const parenMatch = text.match(/^(.+?)\s*\(([^)]+)\)\s*(.*)$/);
    if (parenMatch && !/^Primary damage type/i.test(text)) {
      const prefixHtml = chipifyEffectName(parenMatch[1].trim(), polarity);
      const innerParts = parenMatch[2]
        .split(/\s*,\s*/)
        .map(function (s) {
          return normalizeToken(s);
        })
        .filter(Boolean);
      const innerHtml = innerParts.map(tokenToHtml).join(" ");
      const suffixRaw = parenMatch[3].trim();
      const suffixHtml = suffixRaw ? renderInline(suffixRaw) : "";
      return enhancePlainTargetingInHtml(
        prefixHtml +
        " (" +
        innerHtml +
        ")" +
        (suffixHtml ? " " + suffixHtml : "")
      );
    }

    return enhancePlainTargetingInHtml(
      promoteStrongToDamageChips(renderInline(text))
    );
  }

  function formatTag(raw) {
    const tag = normalizeToken(raw);
    if (!tag) {
      return "";
    }
    const lower = tag.toLowerCase();

    if (QUALITY_CLASS[lower]) {
      const cls = QUALITY_CLASS[lower];
      return chipSpan("⭐", tag, cls, QUALITY_TOOLTIPS[lower]);
    }

    if (lower === "signature fuel") {
      return chipSpan("🔋", tag, "chip-stat", SIGNATURE_FUEL_TOOLTIP);
    }

    const mMeta = speedIndicatorMeta(tag);
    if (mMeta) {
      return chipSpan(mMeta.emoji, tag, mMeta.cls, mMeta.tooltip);
    }

    const targeting = config.TARGETING_DEFINITIONS[lower];
    if (targeting) {
      return chipSpan(targeting.emoji, tag, targeting.cls);
    }

    const def = config.TAG_DEFINITIONS[tag] || null;
    if (def) {
      return chipSpan(def.emoji, healingChipDisplay(tag), def.cls);
    }
    for (const key of Object.keys(config.TAG_DEFINITIONS)) {
      if (key.toLowerCase() === lower) {
        const entry = config.TAG_DEFINITIONS[key];
        return chipSpan(entry.emoji, healingChipDisplay(key), entry.cls);
      }
    }

    return '<span class="chip chip-generic">' + escapeHtml(chipDisplayLabel(tag)) + "</span>";
  }

  function renderMergedEffectPill(baseLabel, quality, tier, conditional, polarity) {
    const resolvedPolarity = polarity || effectLabelPolarity(baseLabel) || "buff";
    const leading = resolveLeadingChip(baseLabel, resolvedPolarity);
    const qMeta = qualityIndicatorMeta(quality, leading.isCc);
    let merged = mergeEffectWithQuality(baseLabel, quality, tier, resolvedPolarity) ||
      mergeLabelWithIndicator(baseLabel, quality, tier, resolvedPolarity);
    if (!merged && qMeta) {
      merged = formatMergedIndicator(
        { textOnly: baseLabel, tierSuffix: tier || "" },
        qMeta,
        true
      );
    }
    if (!merged) {
      merged =
        chipifyEffectName(baseLabel, resolvedPolarity) +
        formatMergedTierSuffix(tier) +
        (quality ? " " + formatTag(quality) : "");
    }
    if (conditional) {
      merged +=
        ' <span class="chip chip-generic chip-has-tip"' +
        chipTipAttrs(conditionalTooltip(conditional)) +
        ">🎲 " +
        escapeHtml("conditional (" + conditional + ")") +
        "</span>";
    }
    return merged;
  }

  function renderBuffProvidedEntry(buff) {
    const parsed = parseEffectLabelParts(buff.label || "");
    const quality = buff.quality || "";
    const polarity = effectLabelPolarity(parsed.base) || "buff";
    let html = renderMergedEffectPill(
      parsed.base,
      quality,
      parsed.tier,
      buff.conditional,
      polarity
    );
    const targetingHtml = renderBuffTargetingChip(
      buff.targetingType || buff.targeting
    );
    if (targetingHtml) {
      html += " " + targetingHtml;
    }
    return '<span class="synergy-buff-entry">' + html + "</span>";
  }

  function renderBuffTargetingChip(targetingType) {
    if (!targetingType) {
      return "";
    }
    return chipifyTargetingSegment(targetingType);
  }

  const QUALITY_RANK = { low: 0, average: 1, high: 2 };

  function isQualityToken(value) {
    return !!QUALITY_CLASS[(value || "").toLowerCase()];
  }

  function combineQualities(qualities) {
    const uniq = [];
    qualities.forEach(function (q) {
      const lower = (q || "").toLowerCase();
      if (isQualityToken(lower) && uniq.indexOf(lower) === -1) {
        uniq.push(lower);
      }
    });
    if (!uniq.length) {
      return "";
    }
    uniq.sort(function (a, b) {
      return QUALITY_RANK[a] - QUALITY_RANK[b];
    });
    if (uniq.length === 1) {
      return uniq[0];
    }
    return uniq[0] + "-" + uniq[uniq.length - 1];
  }

  function combineTargetings(targetings) {
    const parts = [];
    const seen = new Set();
    targetings.forEach(function (t) {
      if (!t) {
        return;
      }
      t.split(/\s*,\s*/).forEach(function (piece) {
        const norm = piece.trim();
        const key = norm.toLowerCase();
        if (!norm || seen.has(key)) {
          return;
        }
        seen.add(key);
        const meta = targetingIndicatorMeta(norm);
        parts.push({
          key: key,
          label: meta ? meta.label : norm,
          rank: TARGETING_RANK[key] || 0,
        });
      });
    });
    parts.sort(function (a, b) {
      return b.rank - a.rank;
    });
    return parts
      .map(function (p) {
        return p.label;
      })
      .join(" + ");
  }

  function combineTierLabels(tiers) {
    const uniq = [];
    tiers.forEach(function (t) {
      if (t && uniq.indexOf(t) === -1) {
        uniq.push(t);
      }
    });
    return uniq
      .map(function (t) {
        return shortAscensionTierName(t);
      })
      .join(", ");
  }

  function combineUniqueText(values) {
    const uniq = [];
    values.forEach(function (v) {
      if (v && uniq.indexOf(v) === -1) {
        uniq.push(v);
      }
    });
    return uniq.join(" + ");
  }

  function buildVariantModifier(variants) {
    const parts = [];
    const quality = combineQualities(
      variants.map(function (v) {
        return v.quality;
      })
    );
    if (quality) {
      parts.push(quality);
    }
    const targeting = combineTargetings(
      variants.map(function (v) {
        return v.targeting;
      })
    );
    if (targeting) {
      parts.push(targeting);
    }
    const tiers = combineTierLabels(
      variants.map(function (v) {
        return v.tier;
      })
    );
    if (tiers) {
      parts.push(tiers);
    }
    const timing = combineUniqueText(
      variants.map(function (v) {
        return v.timing;
      })
    );
    if (timing) {
      parts.push(timing);
    }
    return parts.join("; ");
  }

  function effectVariantGroupKey(variant, cardPolarity) {
    const polarity = cardPolarity || variant.polarity || "";
    return variant.base.toLowerCase() + ":" + polarity;
  }

  function parseSkillCardVariant(raw, explicitPolarity) {
    let work = (raw || "").trim();
    if (!work) {
      return null;
    }
    let tier = "";
    const tierMatch = work.match(ASCENSION_TIER_SUFFIX_RE);
    if (tierMatch) {
      tier = tierMatch[1];
      work = work.slice(0, tierMatch.index).trim();
    }
    const split = parseSkillCardTag(work);
    if (!split.tag) {
      return null;
    }
    const polarity =
      explicitPolarity || effectLabelPolarity(split.tag) || "buff";
    return {
      base: split.tag,
      tier: tier,
      targeting: split.targeting || "",
      quality: "",
      conditional: "",
      timing: "",
      polarity: polarity,
      raw: raw,
    };
  }

  function parseSummaryVariant(raw, cardPolarity) {
    const segments = splitSummarySegments(raw);
    if (!segments.length) {
      return null;
    }
    const parsed = parseEffectLabelParts(segments[0]);
    if (!parsed.base) {
      return null;
    }
    let targeting = "";
    let quality = "";
    let conditional = "";
    let timing = "";
    for (let i = 1; i < segments.length; i++) {
      const seg = unwrapBackticks(segments[i]);
      const lower = seg.toLowerCase();
      if (isQualityToken(lower)) {
        quality = lower;
      } else if (/conditional\s*\(/i.test(seg)) {
        conditional = seg;
      } else if (targetingIndicatorMeta(seg)) {
        if (targeting) {
          targeting += ", " + seg;
        } else {
          targeting = seg;
        }
      } else if (!timing) {
        timing = seg;
      } else {
        timing += " + " + seg;
      }
    }
    if (
      !targeting &&
      segments[1] &&
      !isQualityToken(unwrapBackticks(segments[1]).toLowerCase()) &&
      !/conditional\s*\(/i.test(segments[1])
    ) {
      targeting = unwrapBackticks(segments[1]);
      if (
        segments[2] &&
        isQualityToken(unwrapBackticks(segments[2]).toLowerCase())
      ) {
        quality = unwrapBackticks(segments[2]).toLowerCase();
      }
      if (segments[3] && /conditional\s*\(/i.test(segments[3])) {
        conditional = segments[3];
      } else if (segments[3]) {
        timing = segments[3];
      }
    }
    const polarity =
      cardPolarity || effectLabelPolarity(parsed.base) || "buff";
    return {
      base: parsed.base,
      tier: parsed.tier || "",
      targeting: targeting,
      quality: quality,
      conditional: conditional,
      timing: timing,
      polarity: polarity,
      raw: raw,
    };
  }

  function collectTargetingSegments(variants) {
    const parts = [];
    const seen = new Set();
    variants.forEach(function (v) {
      if (!v.targeting) {
        return;
      }
      v.targeting.split(/\s*,\s*/).forEach(function (piece) {
        const norm = piece.trim();
        const key = norm.toLowerCase();
        if (!norm || seen.has(key)) {
          return;
        }
        seen.add(key);
        const tokenMeta = targetingTokenMeta(norm);
        if (tokenMeta) {
          parts.push(tokenMeta);
          return;
        }
        const indMeta = targetingIndicatorMeta(norm);
        if (indMeta) {
          parts.push({
            emoji: indMeta.emoji,
            text: indMeta.label,
            cls: indMeta.cls,
            rank: TARGETING_RANK[key] || 0,
          });
        }
      });
    });
    parts.sort(function (a, b) {
      return b.rank - a.rank;
    });
    return parts;
  }

  function mergedVariantSep() {
    return '<span class="chip-merged-sep" aria-hidden="true">|</span>';
  }

  function qualityRangeMeta(qualityValue, isCc) {
    if (!qualityValue) {
      return null;
    }
    if (qualityValue.indexOf("-") !== -1) {
      const range = qualityValue.split("-");
      if (
        range.length === 2 &&
        isQualityToken(range[0]) &&
        isQualityToken(range[1])
      ) {
        return {
          cls: "chip-generic",
          label: qualityValue,
          tooltip: "",
          emoji: "",
        };
      }
    }
    return qualityIndicatorMeta(qualityValue, isCc);
  }

  function renderMergedQualitySegment(qualityValue, isCc) {
    if (!qualityValue) {
      return "";
    }
    const qMeta = qualityRangeMeta(qualityValue, isCc);
    if (!qMeta) {
      return (
        '<span class="chip-merged-right chip-generic">' +
        escapeHtml(qualityValue) +
        "</span>"
      );
    }
    return (
      '<span class="chip-merged-right ' +
      qMeta.cls +
      '">' +
      escapeHtml(qMeta.label) +
      "</span>"
    );
  }

  function renderEffectQualityMergedPill(base, polarity, qualityRange) {
    const leading = resolveLeadingChip(base, polarity);
    const qMeta = qualityRangeMeta(qualityRange, leading.isCc);
    if (!qMeta) {
      return "";
    }
    if (leading.emoji) {
      return formatMergedIndicator(
        {
          hasIcon: true,
          emoji: leading.emoji,
          text: leading.text,
          cls: leading.cls,
          tierSuffix: "",
        },
        qMeta,
        false
      );
    }
    return formatMergedIndicator(
      { textOnly: base, tierSuffix: "" },
      qMeta,
      true
    );
  }

  function renderTargetingMergedPill(
    targetingSegments,
    iconOnlyTargeting,
    skillCardDisplay
  ) {
    if (!targetingSegments.length) {
      return "";
    }
    if (targetingSegments.length === 1) {
      const meta = targetingSegments[0];
      return chipSpan(
        meta.emoji,
        targetingDisplayLabel(meta.text || meta.label, skillCardDisplay),
        meta.cls
      );
    }
    if (iconOnlyTargeting) {
      const segmentCount = targetingSegments.length;
      const parts = targetingSegments.map(function (meta, index) {
        return renderMergedTargetingSegment(
          meta,
          targetingSegmentCompact(iconOnlyTargeting, index, segmentCount),
          skillCardDisplay
        );
      });
      return '<span class="chip chip-merged">' + parts.join("") + "</span>";
    }
    const parts = [];
    targetingSegments.forEach(function (meta, index) {
      if (index === 0) {
        parts.push(
          '<span class="chip-merged-left ' +
          meta.cls +
          '">' +
          meta.emoji +
          " " +
          escapeHtml(chipDisplayLabel(meta.text || meta.label)) +
          "</span>"
        );
        return;
      }
      parts.push(renderMergedTargetingSegment(meta, true, false));
    });
    return '<span class="chip chip-merged">' + parts.join("") + "</span>";
  }

  function renderMergedEffectBodyParts(
    first,
    leading,
    qualityRange,
    targetingSegments,
    iconOnlyTargeting,
    skillCardDisplay
  ) {
    const bodyParts = [];
    if (leading.emoji) {
      bodyParts.push(
        '<span class="chip-merged-left ' +
        leading.cls +
        '">' +
        leading.emoji +
        " " +
        escapeHtml(chipDisplayLabel(leading.text)) +
        "</span>"
      );
    } else {
      bodyParts.push(
        '<span class="chip-merged-left chip-merged-label">' +
        escapeHtml(chipDisplayLabel(first.base)) +
        "</span>"
      );
    }

    const qualitySeg = renderMergedQualitySegment(qualityRange, leading.isCc);
    if (qualitySeg) {
      bodyParts.push(qualitySeg);
    }

    const segmentCount = targetingSegments.length;
    targetingSegments.forEach(function (meta, index) {
      bodyParts.push(
        renderMergedTargetingSegment(
          meta,
          targetingSegmentCompact(iconOnlyTargeting, index, segmentCount),
          skillCardDisplay
        )
      );
    });
    return bodyParts;
  }

  function groupedVariantTipAttrs(tipHtml) {
    return (
      ' chip-has-tip" data-tip-html="' +
      escapeHtml(tipHtml) +
      '" tabindex="0" role="button" aria-describedby="chip-tooltip"'
    );
  }

  function withChipTooltip(chipHtml, tipHtml) {
    if (!chipHtml || !tipHtml) {
      return chipHtml;
    }
    return chipHtml.replace(
      '<span class="chip chip-merged"',
      '<span class="chip chip-merged' + groupedVariantTipAttrs(tipHtml)
    );
  }

  function withAnyChipTooltip(chipHtml, tipHtml) {
    if (!chipHtml || !tipHtml) {
      return chipHtml;
    }
    return chipHtml.replace(
      /(<span class="chip[^"]*)"/,
      "$1" + groupedVariantTipAttrs(tipHtml)
    );
  }

  function renderEffectTargetingStackedTipHtml(effectLabel, polarity, targetingTokens) {
    return (
      '<div class="chip-stacked-tip">' +
      targetingTokens
        .map(function (token) {
          return (
            '<div class="chip-merged-tip-line">' +
            renderRichLine(effectLabel + " — " + token, polarity) +
            "</div>"
          );
        })
        .join("") +
      "</div>"
    );
  }

  function renderStandaloneEffectTooltipChip(variant) {
    const parsed = parseEffectLabelParts(variant.base);
    const tier = variant.tier || parsed.tier;
    const base = parsed.base;
    const polarity = variant.polarity;
    const leading = resolveLeadingChip(base, polarity);
    if (leading.emoji) {
      return (
        '<span class="chip ' +
        leading.cls +
        '">' +
        leading.emoji +
        " " +
        escapeHtml(chipDisplayLabel(leading.text)) +
        formatMergedTierSuffix(tier) +
        "</span>"
      );
    }
    const chip = extractChipHtml(
      renderStandaloneEffectChip(base, tier, polarity)
    );
    return chip || renderStandaloneEffectChip(base, tier, polarity);
  }

  function renderVariantTooltipParts(variant) {
    const parts = [renderStandaloneEffectTooltipChip(variant)];
    if (variant.quality) {
      const qChip = formatTag(variant.quality);
      if (qChip) {
        parts.push(qChip);
      }
    }
    const targeting = renderTargetingTooltipLine(variant);
    if (targeting) {
      parts.push(targeting);
    }
    if (variant.timing) {
      parts.push(
        '<span class="chip chip-generic">' +
        escapeHtml(variant.timing) +
        "</span>"
      );
    }
    if (variant.conditional) {
      parts.push(
        '<span class="chip chip-generic chip-has-tip"' +
        chipTipAttrs(conditionalTooltip(variant.conditional)) +
        ">🎲 " +
        escapeHtml(variant.conditional) +
        "</span>"
      );
    }
    return parts;
  }

  function renderTargetingTooltipLine(variant) {
    if (!variant.targeting) {
      return "";
    }
    const tMeta = targetingIndicatorMeta(variant.targeting);
    if (tMeta) {
      return (
        '<span class="chip ' +
        tMeta.cls +
        '">' +
        (tMeta.emoji ? tMeta.emoji + " " : "") +
        escapeHtml(chipDisplayLabel(tMeta.label)) +
        "</span>"
      );
    }
    return chipifyTargetingSegment(variant.targeting);
  }

  function renderMergedTargetingSegment(meta, compact, skillCardDisplay) {
    const emoji = meta.emoji ? meta.emoji : "";
    const label = compact
      ? ""
      : escapeHtml(
        targetingDisplayLabel(meta.text || meta.label, skillCardDisplay)
      );
    const spacer = compact || !label ? "" : " ";
    const titleAttr =
      compact && (meta.text || meta.label)
        ? ' title="' +
        escapeHtml(meta.text || meta.label) +
        '"'
        : "";
    return (
      '<span class="chip-merged-right ' +
      meta.cls +
      '"' +
      titleAttr +
      ">" +
      emoji +
      spacer +
      label +
      "</span>"
    );
  }

  function variantTierOnTrailingSegment(variant) {
    if (!variant.tier) {
      return false;
    }
    const segments = splitSummarySegments(variant.raw);
    if (!segments.length) {
      return false;
    }
    const parsed = parseEffectLabelParts(segments[0]);
    return !parsed.tier;
  }

  function renderVariantTooltipContent(variant) {
    if (!variant.raw) {
      return "";
    }
    if (variant.quality || /`/.test(variant.raw)) {
      return renderRichLine(variant.raw, variant.polarity);
    }
    return renderVariantTooltipParts(variant).join(" ");
  }

  function renderMergedVariantTooltipHtml(variants) {
    return (
      '<div class="chip-stacked-tip">' +
      variants
        .map(function (variant) {
          return (
            '<div class="chip-merged-tip-line">' +
            renderVariantTooltipContent(variant) +
            "</div>"
          );
        })
        .join("") +
      "</div>"
    );
  }

  function renderGroupedVariantPill(variants, opts) {
    opts = opts || {};
    const iconOnlyTargeting = !!opts.iconOnlyTargeting;
    const skillCardDisplay = !!opts.skillCardDisplay;
    if (!variants || variants.length <= 1) {
      return "";
    }

    const first = variants[0];
    const polarity = first.polarity;
    const leading = resolveLeadingChip(first.base, polarity);
    const qualityRange = combineQualities(
      variants.map(function (v) {
        return v.quality;
      })
    );
    const targetingSegments = collectTargetingSegments(variants);

    if (qualityRange && targetingSegments.length) {
      const fullTip = renderMergedVariantTooltipHtml(variants);
      const effectPill = withChipTooltip(
        renderEffectQualityMergedPill(first.base, polarity, qualityRange),
        fullTip
      );
      const targetingPill = withChipTooltip(
        renderTargetingMergedPill(
          targetingSegments,
          iconOnlyTargeting,
          skillCardDisplay
        ),
        fullTip
      );
      return (
        '<span class="grouped-variant-pills">' +
        effectPill +
        " " +
        targetingPill +
        "</span>"
      );
    }

    const bodyHtml = renderMergedEffectBodyParts(
      first,
      leading,
      qualityRange,
      targetingSegments,
      iconOnlyTargeting,
      skillCardDisplay
    ).join("");

    return withChipTooltip(
      '<span class="chip chip-merged">' + bodyHtml + "</span>",
      renderMergedVariantTooltipHtml(variants)
    );
  }

  function groupParsedVariants(items, parseFn, cardPolarity) {
    const groupByKey = {};

    items.forEach(function (item, index) {
      const variant = parseFn(item, cardPolarity);
      if (!variant) {
        return;
      }
      const key = effectVariantGroupKey(variant, cardPolarity);
      if (!groupByKey[key]) {
        groupByKey[key] = {
          key: key,
          variants: [],
          indices: [],
          firstIndex: index,
        };
      }
      const group = groupByKey[key];
      if (group.firstIndex > index) {
        group.firstIndex = index;
      }
      if (
        !group.variants.some(function (v) {
          return v.raw === variant.raw;
        })
      ) {
        group.variants.push(variant);
      }
      group.indices.push(index);
    });

    const consumed = new Set();
    const result = [];
    items.forEach(function (item, index) {
      if (consumed.has(index)) {
        return;
      }
      const variant = parseFn(item, cardPolarity);
      if (!variant) {
        result.push({ type: "raw", item: item });
        return;
      }
      const key = effectVariantGroupKey(variant, cardPolarity);
      const group = groupByKey[key];
      if (group.variants.length > 1) {
        result.push({ type: "group", variants: group.variants });
        group.indices.forEach(function (i) {
          consumed.add(i);
        });
        return;
      }
      result.push({ type: "raw", item: item });
      consumed.add(index);
    });
    return result;
  }

  function groupSummaryItems(items, cardPolarity) {
    return groupParsedVariants(items, parseSummaryVariant, cardPolarity);
  }

  function parseSkillCardTag(raw) {
    let tag = raw.trim();
    let targeting = "";
    const allSummonMatch = tag.match(/^(.+?)\s*(?:—|–)\s*Summons\s*$/i);
    if (allSummonMatch) {
      tag = allSummonMatch[1].trim();
      targeting = "All summons";
      return { tag: tag, targeting: targeting };
    }
    const ownSummonMatch = tag.match(/^(.+?)\s*(?:—|–)\s*Owned\s*$/i);
    if (ownSummonMatch) {
      tag = ownSummonMatch[1].trim();
      targeting = "Owned summons";
      return { tag: tag, targeting: targeting };
    }
    const legacySummonMatch = tag.match(/^(.+?)\s*(?:—|–)\s*Summon\s*$/i);
    if (legacySummonMatch) {
      tag = legacySummonMatch[1].trim();
      targeting = "Owned summons";
      return { tag: tag, targeting: targeting };
    }
    const enemyTargetingMatch = tag.match(
      /^(.+?)\s*(?:—|–)\s*(All units|Area|Arc|Path|Multiple targets|Single target)\s*$/i
    );
    if (enemyTargetingMatch) {
      tag = enemyTargetingMatch[1].trim();
      targeting = enemyTargetingMatch[2].trim();
      return { tag: tag, targeting: targeting };
    }
    const selfMatch = tag.match(/^(.+?)\s*(?:—|–)\s*Self\s*$/i);
    if (selfMatch) {
      tag = selfMatch[1].trim();
      targeting = "Self";
    }
    return { tag: tag, targeting: targeting };
  }

  function chipifySkillCardTag(raw, explicitPolarity) {
    let work = raw.trim();
    if (!work) {
      return "";
    }
    let tier = "";
    const tierMatch = work.match(ASCENSION_TIER_SUFFIX_RE);
    if (tierMatch) {
      tier = tierMatch[1];
      work = work.slice(0, tierMatch.index).trim();
    }
    const split = parseSkillCardTag(work);
    let tag = split.tag;
    if (!tag) {
      return "";
    }
    const parsed = parseEffectLabelParts(tag);
    const polarity = explicitPolarity || effectLabelPolarity(parsed.base) || "buff";

    tag = parsed.base;
    const tierSuffix = tier || parsed.tier;

    if (split.targeting && targetingIndicatorMeta(split.targeting)) {
      const merged = mergeEffectWithTargeting(
        tag,
        split.targeting,
        tierSuffix,
        polarity
      );
      if (merged) {
        return merged;
      }
    }

    if (polarity === "debuff") {
      const debuffChip = tryChipify(tag);
      if (debuffChip) {
        return injectTierIntoChipHtml(
          applyEffectPolarityToChipHtml(debuffChip, polarity),
          tierSuffix
        );
      }
    }

    const direct = tryChipify(tag);
    if (direct) {
      return injectTierIntoChipHtml(
        applyEffectPolarityToChipHtml(direct, polarity),
        tierSuffix
      );
    }

    const ccChip = extractChipHtml(chipifyLeadingCcType(tag));
    if (ccChip) {
      return injectTierIntoChipHtml(ccChip, tierSuffix);
    }

    const statChip = extractChipHtml(chipifyLeadingStat(tag));
    if (statChip) {
      return injectTierIntoChipHtml(
        applyEffectPolarityToChipHtml(statChip, polarity),
        tierSuffix
      );
    }

    const effectChip = extractChipHtml(
      renderStandaloneEffectChip(tag, tierSuffix, polarity)
    );
    if (effectChip) {
      return effectChip;
    }

    const label = tag.replace(/\s*\([^)]*\)/g, "").trim();
    if (!label) {
      return "";
    }
    return injectTierIntoChipHtml(
      chipSpan(
        "🏷️",
        label,
        effectChipClassForPolarity(polarity, "chip-generic")
      ),
      tierSuffix
    );
  }

  // Export module API to window.AFKJ.chips
  window.AFKJ.chips = {
    QUALITY_CLASS: QUALITY_CLASS,
    SPEED_CLASS: SPEED_CLASS,
    SPEED_EMOJI: SPEED_EMOJI,
    QUALITY_EMOJI: QUALITY_EMOJI,
    QUALITY_TOOLTIPS: QUALITY_TOOLTIPS,
    CLASS_RANK_TOOLTIPS: CLASS_RANK_TOOLTIPS,
    SPEED_TOOLTIPS: SPEED_TOOLTIPS,
    WALK_SPEED_STYLE: WALK_SPEED_STYLE,
    WALK_SPEED_EMOJI: WALK_SPEED_EMOJI,
    WALK_SPEED_TOOLTIPS: WALK_SPEED_TOOLTIPS,
    SIGNATURE_FUEL_TOOLTIP: SIGNATURE_FUEL_TOOLTIP,
    MOVEMENT_DEFINITIONS: MOVEMENT_DEFINITIONS,
    MOVEMENT_KEYS: MOVEMENT_KEYS,
    TARGETING_PHRASES: TARGETING_PHRASES,
    STAT_KEYS: STAT_KEYS,
    HEAL_CHIP_KEYS: HEAL_CHIP_KEYS,
    healingChipDisplay: healingChipDisplay,
    tryMergeTrailingLabel: tryMergeTrailingLabel,
    renderCharacterPill: renderCharacterPill,
    renderInline: renderInline,
    conditionalTooltip: conditionalTooltip,
    chipTipAttrs: chipTipAttrs,
    chipTipHtmlAttrs: chipTipHtmlAttrs,
    normalizeToken: normalizeToken,
    normalizeSummaryText: normalizeSummaryText,
    splitSummarySegments: splitSummarySegments,
    isInsideHtmlTag: isInsideHtmlTag,
    isInsideChipSpan: isInsideChipSpan,
    isInsideSpanClass: isInsideSpanClass,
    isInsideSkillInlineStat: isInsideSkillInlineStat,
    isInsideSkillInlineTime: isInsideSkillInlineTime,
    isInsideSkillInlineNum: isInsideSkillInlineNum,
    isInsideStrong: isInsideStrong,
    boldSkillNumericTokens: boldSkillNumericTokens,
    replaceOutsideChips: replaceOutsideChips,
    enhancePlainTargetingInHtml: enhancePlainTargetingInHtml,
    targetingTokenMeta: targetingTokenMeta,
    renderStackedTargetingTipHtml: renderStackedTargetingTipHtml,
    renderStackedTargetingPill: renderStackedTargetingPill,
    chipifyTargetingSegment: chipifyTargetingSegment,
    chipDisplayLabel: chipDisplayLabel,
    chipSpan: chipSpan,
    behaviorTagTooltip: behaviorTagTooltip,
    behaviorTagDefinition: behaviorTagDefinition,
    behaviorTagChip: behaviorTagChip,
    renderFilterComboChip: renderFilterComboChip,
    renderFilterComboChips: renderFilterComboChips,
    isSpeedMetricLabel: isSpeedMetricLabel,
    qualityIndicatorMeta: qualityIndicatorMeta,
    targetingIndicatorMeta: targetingIndicatorMeta,
    resolveIndicatorMeta: resolveIndicatorMeta,
    speedIndicatorMeta: speedIndicatorMeta,
    walkSpeedIndicatorMeta: walkSpeedIndicatorMeta,
    movementChipMeta: movementChipMeta,
    mergeMovementWithWalkSpeed: mergeMovementWithWalkSpeed,
    isCcChipClass: isCcChipClass,
    isCcFamilyChipClass: isCcFamilyChipClass,
    ccFamilyChipKeys: ccFamilyChipKeys,
    exactTagDefinitionKey: exactTagDefinitionKey,
    isStatModifierLabel: isStatModifierLabel,
    effectLabelPolarity: effectLabelPolarity,
    effectChipClassForPolarity: effectChipClassForPolarity,
    resolveLeadingChip: resolveLeadingChip,
    effectChipRemainder: effectChipRemainder,
    shortAscensionTierName: shortAscensionTierName,
    formatAscensionTierDisplay: formatAscensionTierDisplay,
    formatMergedTierSuffix: formatMergedTierSuffix,
    formatMergedIndicator: formatMergedIndicator,
    mergeLabelWithIndicator: mergeLabelWithIndicator,
    mergeEffectWithQuality: mergeEffectWithQuality,
    classRankIndicatorMeta: classRankIndicatorMeta,
    renderClassRankMergedPill: renderClassRankMergedPill,
    renderClassRankCategoryPill: renderClassRankCategoryPill,
    formatStatCategoryCoversTooltip: formatStatCategoryCoversTooltip,
    mergeEffectWithTargeting: mergeEffectWithTargeting,
    tryChipify: tryChipify,
    tokenToHtml: tokenToHtml,
    chipifyEffectName: chipifyEffectName,
    chipifyLeadingCcType: chipifyLeadingCcType,
    chipifyLeadingStat: chipifyLeadingStat,
    unwrapBackticks: unwrapBackticks,
    promoteStrongToDamageChips: promoteStrongToDamageChips,
    parseEffectLabelParts: parseEffectLabelParts,
    injectTierIntoChipHtml: injectTierIntoChipHtml,
    applyEffectPolarityToChipHtml: applyEffectPolarityToChipHtml,
    renderStandaloneEffectChip: renderStandaloneEffectChip,
    renderSummaryEffectChip: renderSummaryEffectChip,
    summaryCardPolarity: summaryCardPolarity,
    renderEmDashLine: renderEmDashLine,
    renderRichLine: renderRichLine,
    formatTag: formatTag,
    renderMergedEffectPill: renderMergedEffectPill,
    renderBuffProvidedEntry: renderBuffProvidedEntry,
    renderBuffTargetingChip: renderBuffTargetingChip,
    extractChipHtml: extractChipHtml,
    parseSkillCardTag: parseSkillCardTag,
    chipifySkillCardTag: chipifySkillCardTag,
    parseSkillCardVariant: parseSkillCardVariant,
    parseSummaryVariant: parseSummaryVariant,
    groupSummaryItems: groupSummaryItems,
    groupParsedVariants: groupParsedVariants,
    renderGroupedVariantPill: renderGroupedVariantPill,
    buildVariantModifier: buildVariantModifier,
  };
})();

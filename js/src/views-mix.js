window.AFKJ = window.AFKJ || {};

(function () {
  const utils = window.AFKJ.utils;
  const config = window.AFKJ.config;
  const chips = window.AFKJ.chips;
  const tiers = window.AFKJ.tiers;
  const gridView = window.AFKJ.views.grid;
  const escapeHtml = utils.escapeHtml.bind(utils);

  const MIX_SLOT_COUNT = 5;

  const MIX_CROWN_BODY =
    "M3.5 17.5 L2 10.5 Q1.5 7.5 3.5 10 Q6.5 13.5 9 11" +
    " Q12 4 15 11 Q17.5 13.5 20.5 10 Q22.5 7.5 22 10.5 L20.5 17.5Z";
  const MIX_CROWN_BAND = 'x="3.5" y="19" width="17" height="3" rx="1.2"';

  const MIX_CROWN_SVG =
    '<svg class="hero-card-crown" viewBox="0 0 24 24" aria-hidden="true">' +
    '<path fill="#d4a017" d="' + MIX_CROWN_BODY + '"/>' +
    '<rect fill="#d4a017" ' + MIX_CROWN_BAND + '/>' +
    '</svg>';

  const MIX_CONTEXT_ICONS = {
    mark:
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
      'stroke-width="1.8"><path d="' + MIX_CROWN_BODY + '"/>' +
      '<rect ' + MIX_CROWN_BAND + '/></svg>',
    unmark:
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
      'stroke-width="1.8"><path d="' + MIX_CROWN_BODY + '"/>' +
      '<rect ' + MIX_CROWN_BAND + '/>' +
      '<path d="M4 4l16 16"/></svg>',
    highlight:
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
      'stroke-width="2"><path d="M12 3l2.4 7.4H22l-6 4.6 2.3 7 L12 17.4 ' +
      '5.7 22l2.3-7-6-4.6h7.6z"/></svg>',
    replace:
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
      'stroke-width="2"><path d="M16 3h5v5M4 21 20.5 4.5M21 16v5h-5' +
      'M4 21 3 16"/></svg>',
    remove:
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
      'stroke-width="2"><path d="M3 6h18M8 6V4h8v2M6 6l1 14h10l1-14"/></svg>',
    view:
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
      'stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>' +
      '<circle cx="12" cy="12" r="3"/></svg>',
    add:
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
      'stroke-width="2"><path d="M12 5v14M5 12h14"/></svg>',
  };

  const MIX_TOUCH_DEVICE = window.matchMedia("(hover: none) and (pointer: coarse)");

  let mixHighlightMap = {};
  let mixHighlightSource = null;
  let mixGridOrder = [];
  let mixDragDidMove = false;
  let mixDragGhostEl = null;
  let mixGridPointer = null;
  let mixContextMenuEl = null;
  let mixContextSlotIndex = -1;
  let mixContextGridSlug = null;
  let mixSlotLastTap = null;
  const mixMarked = new Set();

  function mixDataUrl(path) {
    const state = window.AFKJ.state;
    const bust =
      state.heroesMeta && state.heroesMeta.generated
        ? "?v=" + encodeURIComponent(state.heroesMeta.generated)
        : "";
    return utils.assetUrl(path) + bust;
  }

  function normalizeMixConfig(raw) {
    const out = Object.assign({}, raw || {});
    const focusTags = Object.assign({}, out.focusTags || {});
    Object.keys(config.MIX_FOCUS_TAG_DEFAULTS).forEach(function (key) {
      focusTags[key] = Object.assign(
        {},
        config.MIX_FOCUS_TAG_DEFAULTS[key],
        focusTags[key] || {}
      );
    });
    out.focusTags = focusTags;
    return out;
  }

  function loadMixData() {
    const state = window.AFKJ.state;
    if (Object.keys(state.mixSynergyIndex).length) {
      return Promise.resolve();
    }
    const idxUrl = mixDataUrl("data/mix-synergy-index.json");
    const configUrl = mixDataUrl("data/mix-config.json");
    const promUrl = mixDataUrl("data/mix-role-prominence.json");

    return Promise.all([
      fetch(idxUrl).then(function (r) { return r.json(); }),
      fetch(configUrl).then(function (r) { return r.json(); }),
      fetch(promUrl).then(function (r) { return r.json(); }),
    ]).then(function (results) {
      state.mixSynergyIndex = results[0] || {};
      state.mixConfig = normalizeMixConfig(results[1]);
      state.mixRoleProminence = results[2] || {};
    });
  }

  function mixSlottedSlugSet() {
    const set = {};
    window.AFKJ.state.mixSlots.forEach(function (slug) {
      if (slug) {
        set[slug] = true;
      }
    });
    return set;
  }

  function compactMixSlots() {
    const state = window.AFKJ.state;
    const filled = state.mixSlots.filter(Boolean);
    state.mixSlots = filled.concat(
      Array(Math.max(0, MIX_SLOT_COUNT - filled.length)).fill(null)
    );
  }

  function mixFirstFreeSlotIndex() {
    const slots = window.AFKJ.state.mixSlots;
    for (let i = 0; i < MIX_SLOT_COUNT; i++) {
      if (!slots[i]) {
        return i;
      }
    }
    return -1;
  }

  function removeSlugFromMixSlots(slug) {
    const state = window.AFKJ.state;
    for (let i = 0; i < MIX_SLOT_COUNT; i++) {
      if (state.mixSlots[i] === slug) {
        state.mixSlots[i] = null;
      }
    }
    compactMixSlots();
    mixMarked.delete(slug);
    if (mixHighlightSource === slug) {
      mixHighlightSource = null;
      mixHighlightMap = {};
    }
  }

  function clearMixAlternativeHighlights() {
    mixHighlightSource = null;
    mixHighlightMap = {};
  }

  function mixSlotIndexForSlug(slug) {
    const slots = window.AFKJ.state.mixSlots;
    for (let i = 0; i < MIX_SLOT_COUNT; i++) {
      if (slots[i] === slug) {
        return i;
      }
    }
    return -1;
  }

  function tryReplaceHighlightedAlternative(slug) {
    if (!mixHighlightSource || !mixHighlightMap[slug]) {
      return false;
    }
    if (mixSlottedSlugSet()[slug]) {
      return false;
    }
    const slotIndex = mixSlotIndexForSlug(mixHighlightSource);
    if (slotIndex < 0) {
      clearMixAlternativeHighlights();
      return false;
    }
    mixMarked.delete(mixHighlightSource);
    window.AFKJ.state.mixSlots[slotIndex] = slug;
    compactMixSlots();
    clearMixAlternativeHighlights();
    renderMix();
    return true;
  }

  function addHeroToMixZone(slug) {
    if (!slug || mixSlottedSlugSet()[slug]) {
      return false;
    }
    compactMixSlots();
    const slot = mixFirstFreeSlotIndex();
    if (slot < 0) {
      return false;
    }
    window.AFKJ.state.mixSlots[slot] = slug;
    clearMixAlternativeHighlights();
    renderMix();
    return true;
  }

  function placeHeroInMixZone(slug, source) {
    if (!slug) {
      return false;
    }
    const state = window.AFKJ.state;
    const fromSlot = source && source.indexOf("slot-") === 0;
    if (fromSlot) {
      const fromIndex = parseInt(source.split("-")[1], 10);
      if (!isNaN(fromIndex) && state.mixSlots[fromIndex] === slug) {
        state.mixSlots[fromIndex] = null;
      }
    } else {
      removeSlugFromMixSlots(slug);
    }
    compactMixSlots();
    if (mixSlottedSlugSet()[slug]) {
      renderMix();
      return true;
    }
    const slot = mixFirstFreeSlotIndex();
    if (slot < 0) {
      renderMix();
      return false;
    }
    state.mixSlots[slot] = slug;
    compactMixSlots();
    if (!fromSlot) {
      clearMixAlternativeHighlights();
    }
    renderMix();
    return true;
  }

  function synergyScoreForPair(providerSlug, receiverSlug) {
    const state = window.AFKJ.state;
    const byReceiver =
      state.mixSynergyIndex && state.mixSynergyIndex.byReceiver;
    if (!byReceiver || !byReceiver[receiverSlug]) {
      return 0;
    }
    return byReceiver[receiverSlug][providerSlug] || 0;
  }

  function getQualifyingMixFactions() {
    const state = window.AFKJ.state;
    const count = {};
    state.mixSlots.forEach(function (slug) {
      if (!slug) {
        return;
      }
      const hero = state.heroBySlug[slug];
      if (hero && hero.faction) {
        const key = utils.factionBonusGroupKey(hero.faction);
        count[key] = (count[key] || 0) + 1;
      }
    });
    const qualifying = {};
    Object.keys(count).forEach(function (key) {
      if (count[key] >= 2) {
        qualifying[key] = true;
      }
    });
    return qualifying;
  }

  function mixHeroSkillTags(hero) {
    const state = window.AFKJ.state;
    if (!hero || !hero.sections || !hero.sections.skillCards) {
      return [];
    }
    const list = [];
    hero.sections.skillCards.forEach(function (card) {
      const tags = card.tags || card.effects || [];
      tags.forEach(function (t) {
        const label = window.AFKJ.skills.skillCardTagLabel(t);
        const key = window.AFKJ.skills.skillCardChipKey(label);
        if (key) {
          list.push({ key: key, label: label });
        }
      });
    });
    return list;
  }

  function mixHeroBehaviorTags(hero) {
    const behavior = hero && hero.sections && hero.sections.behavior;
    if (!behavior) {
      return [];
    }
    const match = behavior.match(/\*\*Behavior tags\*\*:\s*([^\n]+)/);
    if (!match) {
      return [];
    }
    const found = [];
    const re = /`([^`]+)`/g;
    let m;
    while ((m = re.exec(match[1])) !== null) {
      found.push(m[1]);
    }
    return found;
  }

  function mixTagBaseLabel(tag) {
    const parts = String(tag).split(/\s+[—–-]\s+/);
    return parts[0].trim();
  }

  function mixFocusTagWeight(map, key) {
    if (!map || !key) {
      return null;
    }
    if (map[key] != null) {
      return map[key];
    }
    const lower = key.toLowerCase();
    const keys = Object.keys(map);
    for (let i = 0; i < keys.length; i++) {
      if (keys[i].toLowerCase() === lower) {
        return map[keys[i]];
      }
    }
    return null;
  }

  function mixCcTargetingWeight(tag) {
    const state = window.AFKJ.state;
    const weights = (state.mixConfig && state.mixConfig.ccTargetingWeight) || {};
    const lower = String(tag).toLowerCase();
    if (lower.indexOf("all units") !== -1) {
      return weights["All units"] || 2.0;
    }
    if (lower.indexOf("area") !== -1) {
      return weights.Area || 1.6;
    }
    if (lower.indexOf("arc") !== -1) {
      return weights.Arc || 1.3;
    }
    if (lower.indexOf("multiple targets") !== -1) {
      return weights["Multiple targets"] || 1.3;
    }
    return weights["Single target"] || 1.0;
  }

  function mixTagTargetingWeight(tag) {
    const lower = tag.trim().toLowerCase();
    const isSummons = lower.indexOf("to summons") !== -1 || lower.indexOf("to owned summons") !== -1;
    const isAllies = lower.indexOf("to allies") !== -1;
    if (isSummons || isAllies) {
      return 1.4;
    }
    const re = /\b(?:all\s+enemies|center\s+of\s+the\s+battlefield|all\s+units|area)\b/i;
    if (re.test(tag)) {
      return 1.25;
    }
    return 1.0;
  }

  function mixHeroSkillOverviewSpeeds(hero) {
    if (!hero || !hero.sections || !hero.sections.behavior) {
      return {};
    }
    const md = hero.sections.behavior;
    const overviewLines = md.split("\n").filter(function (line) {
      return line.startsWith("- **Signature skill") || line.startsWith("- **Ultimate") || line.startsWith("- **Non-ultimate");
    });
    const out = {};
    overviewLines.forEach(function (line) {
      const match = line.match(/^\s*-\s*\*\*([^*]+)\*\*:\s*([^\n]+)$/);
      if (!match) return;
      const slot = match[1].replace(/\s*\(ult\)$/, "").trim().toLowerCase();
      const right = match[2];
      const speedMatch = right.match(/`([^`]+)`\s*first\s+cast\s+speed/i) || right.match(/`([^`]+)`\s*speed/i);
      if (speedMatch) {
        out[slot] = speedMatch[1].trim().toLowerCase();
      }
    });
    return out;
  }

  function computeMixSpeedBonus(hero) {
    const state = window.AFKJ.state;
    const weight = (state.mixConfig.mixMode && state.mixConfig.mixMode.role_prominence_tier_weight) ?? 7;
    const scoreMult = weight * 1.5;
    const speeds = mixHeroSkillOverviewSpeeds(hero);
    const signature = speeds.signature || speeds.ultimate || "average";
    const multipliers = { slow: 1.6, average: 1.2, fast: 1.0 };
    const mult = multipliers[signature] || 1.2;

    let energyBuffValue = 0;
    let hasteBuffValue = 0;

    state.mixSlots.forEach(function (slotSlug) {
      if (!slotSlug) {
        return;
      }
      const slotHero = state.heroBySlug[slotSlug];
      if (!slotHero) {
        return;
      }
      const byReceiver =
        state.mixSynergyIndex && state.mixSynergyIndex.byReceiver;
      const row = byReceiver && byReceiver[hero.slug];
      if (!row) {
        return;
      }
      const pairScore = row[slotSlug] || 0;
      if (pairScore === 0) {
        return;
      }

      const recSpeeds = mixHeroSkillOverviewSpeeds(slotHero);
      const recSig = recSpeeds.signature || recSpeeds.ultimate || "average";
      const recMult = multipliers[recSig] || 1.2;

      const providerTags = mixHeroSkillTags(slotHero);
      providerTags.forEach(function (tag) {
        const base = mixTagBaseLabel(tag.label).toLowerCase();
        const polarity = chips.effectLabelPolarity(tag.label) || "buff";
        if (polarity !== "buff") return;
        const tw = mixTagTargetingWeight(tag.label);

        if (base === "energy" || base === "energy recovery" || base === "energy recovery buff") {
          energyBuffValue = Math.max(energyBuffValue, 3.0 * tw * recMult);
        }
        if (base === "haste" || base === "haste buff" || base === "atk spd" || base === "atk spd buff") {
          hasteBuffValue = Math.max(hasteBuffValue, 3.0 * tw * recMult);
        }
      });
    });

    return (energyBuffValue + hasteBuffValue) * mult * scoreMult * 0.05;
  }

  function mixHasActiveFocus() {
    const state = window.AFKJ.state;
    return Object.values(state.mixFocus).some(Boolean);
  }

  function computeMixFocusBonus(hero) {
    const state = window.AFKJ.state;
    if (!state.mixConfig || !state.mixConfig.focusTags) {
      return 0;
    }
    const focusTags = state.mixConfig.focusTags;
    const heroSkillTags = mixHeroSkillTags(hero);
    const heroBehaviorTags = mixHeroBehaviorTags(hero);
    const focusKeys = config.MIX_FOCUS_CONFIG_KEYS;
    let bonus = 0;

    function addFromMap(map, isCc) {
      if (!map) {
        return 0;
      }
      let focusMax = 0;
      heroSkillTags.forEach(function (tag) {
        const base = mixTagBaseLabel(tag.label);
        const weight = mixFocusTagWeight(map, base);
        if (weight != null) {
          const mult = isCc ? mixCcTargetingWeight(tag.label) : 1;
          focusMax = Math.max(focusMax, weight * mult);
        }
      });
      heroBehaviorTags.forEach(function (bt) {
        const weight = mixFocusTagWeight(map, bt);
        if (weight != null) {
          focusMax = Math.max(focusMax, weight);
        }
      });
      return focusMax;
    }

    if (state.mixFocus.ccImmunity) {
      bonus += addFromMap(focusTags[focusKeys.ccImmunity], false);
    }
    if (state.mixFocus.cc) {
      bonus += addFromMap(focusTags[focusKeys.cc], true);
    }
    if (state.mixFocus.sustain) {
      bonus += addFromMap(focusTags[focusKeys.sustain], false);
    }
    if (state.mixFocus.speed) {
      bonus += computeMixSpeedBonus(hero);
    }
    if (state.mixFocus.noUltimate) {
      bonus += addFromMap(focusTags[focusKeys.noUltimate], false);
    }
    return bonus;
  }

  function computeMixScore(slug) {
    const state = window.AFKJ.state;
    const team = state.mixSlots.filter(Boolean);
    const hero = state.heroBySlug[slug];
    if (!team.length) {
      if (!mixHasActiveFocus() || !hero) {
        return 0;
      }
      return computeMixFocusBonus(hero);
    }
    let total = 0;
    const markMult =
      state.mixConfig && state.mixConfig.markSynergyMultiplier != null
        ? state.mixConfig.markSynergyMultiplier
        : 2.0;
    team.forEach(function (receiverSlug) {
      const score = synergyScoreForPair(slug, receiverSlug);
      const mult = mixMarked.has(receiverSlug) ? markMult : 1.0;
      total += score * mult;
    });
    if (hero) {
      total += computeMixFocusBonus(hero);
      const qualifying = getQualifyingMixFactions();
      if (
        hero.faction &&
        qualifying[utils.factionBonusGroupKey(hero.faction)]
      ) {
        const factionBonus =
          state.mixConfig && state.mixConfig.factionBonus != null
            ? state.mixConfig.factionBonus
            : 3.0;
        total += factionBonus;
      }
    }
    return total;
  }

  function mixRawRoleProminence(slug, roleKey) {
    const state = window.AFKJ.state;
    const bySlug =
      state.mixRoleProminence && state.mixRoleProminence.bySlug
        ? state.mixRoleProminence.bySlug
        : null;
    if (!bySlug || !roleKey) {
      return 0;
    }
    const row = bySlug[slug];
    if (!row || row[roleKey] == null) {
      return 0;
    }
    return row[roleKey];
  }

  function normalizePrydwenTiersForRoleProminence(tiers) {
    const out = {};
    config.ROLE_FILTER_ORDER.forEach(function (role) {
      const modeKey = role === "damage_dealer" ? "afk_stages" : role === "specialist" ? "pvp" : "dream_realm";
      const raw = tiers[modeKey] || "?";
      out[role] = raw;
    });
    return out;
  }

  function averagePrydwenTierRankFromTiers(tiers) {
    let sum = 0;
    let count = 0;
    tiers.forEach(function (mode) {
      const rank = window.AFKJ.tiers.prydwenTierRank(mode);
      if (rank >= 0) {
        sum += rank;
        count++;
      }
    });
    return count > 0 ? sum / count : -1;
  }

  function resolvePrydwenTierRank(hero) {
    const state = window.AFKJ.state;
    const mode = state.mixMode;
    const key = mode === "pvp" ? "pvp" : mode === "afk" ? "afk_stages" : mode === "boss" ? "dream_realm" : "average";
    const modeTiers = window.AFKJ.tiers.getHeroPrydwenTiers(hero);
    if (key === "average") {
      const list = Object.values(modeTiers);
      return averagePrydwenTierRankFromTiers(list);
    }
    return window.AFKJ.tiers.prydwenTierRank(modeTiers[key]);
  }

  function roleProminenceTierPoints(hero) {
    const rank = resolvePrydwenTierRank(hero);
    if (rank < 0) {
      return 0;
    }
    return (rank + 1) * 100;
  }

  function mixCombinedRoleProminenceRaw(hero, roleKey) {
    const rawProm = mixRawRoleProminence(hero.slug, roleKey);
    const points = roleProminenceTierPoints(hero);
    return rawProm + points;
  }

  function normalizeScores(pool, scoreFn) {
    const bonuses = {};
    if (!pool || !pool.length) {
      return bonuses;
    }
    let min = Infinity;
    let max = -Infinity;
    pool.forEach(function (h) {
      const raw = scoreFn(h);
      if (raw < min) {
        min = raw;
      }
      if (raw > max) {
        max = raw;
      }
    });
    if (!isFinite(min) || !isFinite(max) || min === max) {
      pool.forEach(function (h) {
        bonuses[h.slug] = 0;
      });
      return bonuses;
    }
    const range = max - min;
    pool.forEach(function (h) {
      const raw = scoreFn(h);
      bonuses[h.slug] = ((raw - min) / range) * 10;
    });
    return bonuses;
  }

  function computeNormalizedRoleBonuses(pool, roleKey) {
    if (!roleKey) {
      return {};
    }
    return normalizeScores(pool, function (h) {
      return mixCombinedRoleProminenceRaw(h, roleKey);
    });
  }

  function computeNormalizedTierBonuses(pool) {
    return normalizeScores(pool, function (h) {
      return roleProminenceTierPoints(h);
    });
  }

  function mixPoolHeroes() {
    const state = window.AFKJ.state;
    const slotsSet = mixSlottedSlugSet();
    const list = window.AFKJ.router.filteredHeroes();
    return list.filter(function (h) {
      return !slotsSet[h.slug];
    });
  }

  function mixSortedPoolHeroes() {
    const state = window.AFKJ.state;
    const pool = mixPoolHeroes();
    const candidates = [];

    const modeTiers = computeNormalizedTierBonuses(pool);
    const roleTiers = state.activeRole ? computeNormalizedRoleBonuses(pool, state.activeRole) : {};

    pool.forEach(function (h) {
      const score = computeMixScore(h.slug);
      let promBonus = 0;
      if (state.activeRole) {
        promBonus = roleTiers[h.slug] || 0;
      } else {
        promBonus = modeTiers[h.slug] || 0;
      }
      const finalScore = score + promBonus;
      candidates.push({ hero: h, score: finalScore });
    });

    candidates.sort(function (a, b) {
      if (Math.abs(a.score - b.score) < 0.0001) {
        return a.hero.name.localeCompare(b.hero.name);
      }
      return b.score - a.score;
    });

    return candidates.map(function (c) {
      return c.hero;
    });
  }

  function replacementCategoryIcon(label) {
    return config.REPLACEMENT_CATEGORY_ICONS[label] || "";
  }

  function renderMixHighlightIcons(categories) {
    if (!categories || !categories.length) {
      return "";
    }
    let html = '<div class="mix-highlight-icons">';
    categories.forEach(function (label) {
      const icon = replacementCategoryIcon(label);
      html +=
        '<span class="mix-highlight-icon" title="' +
        escapeHtml(label) +
        '">' +
        escapeHtml(icon) +
        "</span>";
    });
    html += "</div>";
    return html;
  }

  function renderMixHeroCard(h, opts) {
    opts = opts || {};
    const factionKey = utils.factionDataKey(h.faction);
    let extraClass = "";
    const isHighlightSource =
      opts.highlightSource || mixHighlightSource === h.slug;
    if (opts.marked || isHighlightSource) {
      extraClass += " hero-card--mix-marked";
    }
    let highlightCats = [];
    if (!opts.inSlot && mixHighlightMap[h.slug]) {
      highlightCats = mixHighlightMap[h.slug];
      extraClass += " hero-card--mix-highlight";
    }
    const draggable = opts.draggable !== false;
    const chromeHtml =
      (opts.marked || isHighlightSource ? MIX_CROWN_SVG : "") +
      (highlightCats.length && !opts.inSlot
        ? renderMixHighlightIcons(highlightCats)
        : "");
    const cardHtml =
      '<article class="hero-card afkj-box afkj-box-sm' +
      extraClass +
      '" data-slug="' +
      escapeHtml(h.slug) +
      '" data-faction="' +
      escapeHtml(factionKey) +
      '"' +
      (draggable ? ' draggable="true"' : "") +
      (opts.mixSource
        ? ' data-mix-source="' + escapeHtml(opts.mixSource) + '"'
        : "") +
      ' tabindex="0" aria-label="' +
      escapeHtml(h.name) +
      '">' +
      gridView.renderHeroPortrait(h) +
      gridView.renderHeroCardWave(h.slug) +
      '<div class="hero-card-info">' +
      '<div class="hero-card-name"><h2>' +
      escapeHtml(h.name) +
      "</h2></div>" +
      '<div class="hero-card-meta">' +
      gridView.renderGridCardRole(h) +
      "</div></div>" +
      gridView.renderGridCardFactionStack(h) +
      "</article>";
    if (!chromeHtml) {
      return '<div class="mix-hero-card-shell">' + cardHtml + "</div>";
    }
    return (
      '<div class="mix-hero-card-shell">' +
      cardHtml +
      '<div class="mix-hero-card-chrome" aria-hidden="true">' +
      chromeHtml +
      "</div></div>"
    );
  }

  function renderMixSlots() {
    const state = window.AFKJ.state;
    const dom = state.dom;
    if (!dom.mixDropZone) {
      return;
    }
    compactMixSlots();
    let html = "";
    for (let i = 0; i < MIX_SLOT_COUNT; i++) {
      const slug = state.mixSlots[i];
      html += '<div class="mix-slot" data-slot="' + i + '">';
      if (slug && state.heroBySlug[slug]) {
        html += renderMixHeroCard(state.heroBySlug[slug], {
          inSlot: true,
          marked: mixMarked.has(slug),
          highlightSource: mixHighlightSource === slug,
          mixSource: "slot-" + i,
        });
      } else {
        html += '<div class="mix-slot--empty" aria-label="Empty slot"></div>';
      }
      html += "</div>";
    }
    dom.mixDropZone.innerHTML = html;
  }

  function animateMixGridReorder(prevRects) {
    const state = window.AFKJ.state;
    if (!state.dom.mixHeroGrid) {
      return;
    }
    const cards = state.dom.mixHeroGrid.querySelectorAll(".hero-card");
    cards.forEach(function (el) {
      const slug = el.dataset.slug;
      const prev = prevRects.get(slug);
      const next = el.getBoundingClientRect();
      if (!prev) {
        el.style.opacity = "0";
        return;
      }
      const dx = prev.left - next.left;
      const dy = prev.top - next.top;
      if (Math.abs(dx) > 0.5 || Math.abs(dy) > 0.5) {
        el.style.transform = "translate(" + dx + "px, " + dy + "px)";
        el.style.opacity = "0";
      }
    });
    requestAnimationFrame(function () {
      cards.forEach(function (el) {
        el.classList.add("mix-sort-anim");
        el.style.transform = "";
        el.style.opacity = "1";
      });
      setTimeout(function () {
        cards.forEach(function (el) {
          el.classList.remove("mix-sort-anim");
          el.style.transform = "";
          el.style.opacity = "";
        });
      }, 1000);
    });
  }

  function renderMixGrid() {
    const state = window.AFKJ.state;
    const dom = state.dom;
    if (!dom.mixHeroGrid) {
      return;
    }
    const list = mixSortedPoolHeroes();
    const newOrder = list.map(function (h) {
      return h.slug;
    });
    const orderChanged = mixGridOrder.join(",") !== newOrder.join(",");
    const prevRects = new Map();
    if (orderChanged) {
      dom.mixHeroGrid.querySelectorAll(".hero-card").forEach(function (el) {
        prevRects.set(el.dataset.slug, el.getBoundingClientRect());
      });
    }
    mixGridOrder = newOrder;
    dom.mixHeroGrid.innerHTML = list
      .map(function (h) {
        return renderMixHeroCard(h, { mixSource: "grid" });
      })
      .join("");
    if (dom.mixEmptyState) {
      dom.mixEmptyState.classList.toggle("hidden", list.length > 0);
    }
    if (orderChanged && prevRects.size) {
      animateMixGridReorder(prevRects);
    }
    gridView.scheduleFitHeroCardNames();
  }

  function renderMix() {
    renderMixSlots();
    renderMixGrid();
    syncMixFocusButtons();
    syncMixModeButtons();
  }

  function syncMixFocusButtons() {
    const state = window.AFKJ.state;
    const toolbar = document.querySelector(".mix-focus-selector");
    if (!toolbar) {
      return;
    }
    toolbar.querySelectorAll(".mix-focus-btn").forEach(function (btn) {
      const fKey = btn.dataset.focus;
      const active = !!state.mixFocus[fKey];
      btn.classList.toggle("active", active);
      btn.setAttribute("aria-pressed", active ? "true" : "false");
    });
  }

  function syncMixModeButtons() {
    const state = window.AFKJ.state;
    const toolbar = document.querySelector(".mix-mode-selector");
    if (!toolbar) {
      return;
    }
    toolbar.querySelectorAll(".mix-mode-btn").forEach(function (btn) {
      const mKey = btn.dataset.mode;
      const active = state.mixMode === mKey;
      btn.classList.toggle("active", active);
      btn.setAttribute("aria-pressed", active ? "true" : "false");
    });
  }

  function buildMixHighlightMap(sourceSlug) {
    const state = window.AFKJ.state;
    const hero = state.heroBySlug[sourceSlug];
    const map = {};
    if (!hero || !hero.sections || !hero.sections.replacements) {
      return map;
    }
    hero.sections.replacements.forEach(function (cat) {
      (cat.entries || []).forEach(function (entry) {
        if (!entry.slug) {
          return;
        }
        if (!map[entry.slug]) {
          map[entry.slug] = [];
        }
        if (map[entry.slug].indexOf(cat.category) === -1) {
          map[entry.slug].push(cat.category);
        }
      });
    });
    return map;
  }

  function getMixOverallReplacement(sourceSlug) {
    const state = window.AFKJ.state;
    const hero = state.heroBySlug[sourceSlug];
    if (!hero || !hero.sections || !hero.sections.replacements) {
      return null;
    }
    const overall = hero.sections.replacements.find(function (cat) {
      return cat.category === "Best overall replacement";
    });
    if (!overall || !overall.entries || !overall.entries.length) {
      return null;
    }
    return overall.entries[0];
  }

  function ensureMixContextMenu() {
    if (mixContextMenuEl) {
      return mixContextMenuEl;
    }
    mixContextMenuEl = document.createElement("div");
    mixContextMenuEl.className = "mix-context-menu";
    mixContextMenuEl.hidden = true;
    mixContextMenuEl.setAttribute("role", "menu");
    document.body.appendChild(mixContextMenuEl);
    mixContextMenuEl.addEventListener("click", function (e) {
      const menuBtn = e.target.closest(".mix-context-menu-item");
      if (!menuBtn || menuBtn.disabled) {
        return;
      }
      e.preventDefault();
      e.stopPropagation();
      if (mixContextGridSlug) {
        handleMixGridContextAction(menuBtn.dataset.action);
      } else {
        handleMixContextAction(menuBtn.dataset.action);
      }
    });
    document.addEventListener("click", function (e) {
      if (
        mixContextMenuEl &&
        !mixContextMenuEl.hidden &&
        !mixContextMenuEl.contains(e.target)
      ) {
        closeMixContextMenu();
      }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        closeMixContextMenu();
      }
    });
    return mixContextMenuEl;
  }

  function closeMixContextMenu() {
    if (mixContextMenuEl) {
      mixContextMenuEl.hidden = true;
    }
    mixContextSlotIndex = -1;
    mixContextGridSlug = null;
  }

  function positionMixContextMenu(menu, clientX, clientY) {
    menu.hidden = false;
    menu.style.left = clientX + "px";
    menu.style.top = clientY + "px";
    const rect = menu.getBoundingClientRect();
    if (rect.right > window.innerWidth - 8) {
      menu.style.left = Math.max(8, clientX - rect.width) + "px";
    }
    if (rect.bottom > window.innerHeight - 8) {
      menu.style.top = Math.max(8, clientY - rect.height) + "px";
    }
  }

  function mixContextMenuItem(label, iconKey, action, disabled) {
    const isDisabled = !!disabled;
    return (
      '<button type="button" class="mix-context-menu-item' +
      (isDisabled ? " mix-context-menu-item--disabled" : "") +
      '" data-action="' +
      escapeHtml(action) +
      '"' +
      (isDisabled ? " disabled" : "") +
      ">" +
      '<span class="mix-context-menu-icon">' +
      (MIX_CONTEXT_ICONS[iconKey] || "") +
      "</span>" +
      escapeHtml(label) +
      "</button>"
    );
  }

  function openMixContextMenu(slotIndex, clientX, clientY) {
    const state = window.AFKJ.state;
    const slug = state.mixSlots[slotIndex];
    if (!slug) {
      return;
    }
    const menu = ensureMixContextMenu();
    mixContextSlotIndex = slotIndex;
    mixContextGridSlug = null;
    let html = "";
    if (mixMarked.has(slug)) {
      html += mixContextMenuItem("Unmark", "unmark", "unmark");
    } else {
      html += mixContextMenuItem("Mark", "mark", "mark");
    }
    html += mixContextMenuItem(
      mixHighlightSource === slug
        ? "Unmark alternatives"
        : "Highlight alternatives",
      "highlight",
      "highlight"
    );
    if (getMixOverallReplacement(slug)) {
      html += mixContextMenuItem("Replace", "replace", "replace");
    }
    html += mixContextMenuItem("View character", "view", "view");
    html += mixContextMenuItem("Remove", "remove", "remove");
    menu.innerHTML = html;
    positionMixContextMenu(menu, clientX, clientY);
  }

  function openMixGridContextMenu(slug, clientX, clientY) {
    if (!slug || mixSlottedSlugSet()[slug]) {
      return;
    }
    const menu = ensureMixContextMenu();
    mixContextSlotIndex = -1;
    mixContextGridSlug = slug;
    const isReplacement =
      mixHighlightSource && mixHighlightMap[slug];
    const zoneFull = mixFirstFreeSlotIndex() < 0;
    const addDisabled = !isReplacement && zoneFull;
    let html = mixContextMenuItem("View character", "view", "grid-view");
    html += mixContextMenuItem(
      isReplacement ? "Replace" : "Add",
      isReplacement ? "replace" : "add",
      isReplacement ? "grid-replace" : "grid-add",
      addDisabled
    );
    menu.innerHTML = html;
    positionMixContextMenu(menu, clientX, clientY);
  }

  function removeHeroFromMixSlot(slotIndex) {
    const state = window.AFKJ.state;
    const slug = state.mixSlots[slotIndex];
    if (!slug) {
      return;
    }
    state.mixSlots[slotIndex] = null;
    mixMarked.delete(slug);
    if (mixHighlightSource === slug) {
      clearMixAlternativeHighlights();
    }
    compactMixSlots();
    renderMix();
  }

  function handleMixGridContextAction(action) {
    const slug = mixContextGridSlug;
    closeMixContextMenu();
    if (!slug) {
      return;
    }
    if (action === "grid-view") {
      window.AFKJ.router.navigateTo(utils.heroUrl(slug));
      return;
    }
    if (action === "grid-replace") {
      tryReplaceHighlightedAlternative(slug);
      return;
    }
    if (action === "grid-add") {
      addHeroToMixZone(slug);
    }
  }

  function handleMixContextAction(action) {
    const state = window.AFKJ.state;
    const slotIndex = mixContextSlotIndex;
    const slug = slotIndex >= 0 ? state.mixSlots[slotIndex] : null;
    closeMixContextMenu();
    if (!slug) {
      return;
    }
    if (action === "view") {
      window.AFKJ.router.navigateTo(utils.heroUrl(slug));
      return;
    }
    if (action === "mark") {
      mixMarked.add(slug);
      renderMix();
      return;
    }
    if (action === "unmark") {
      mixMarked.delete(slug);
      renderMix();
      return;
    }
    if (action === "highlight") {
      if (mixHighlightSource === slug) {
        mixHighlightSource = null;
        mixHighlightMap = {};
      } else {
        mixHighlightSource = slug;
        mixHighlightMap = buildMixHighlightMap(slug);
      }
      renderMix();
      return;
    }
    if (action === "replace") {
      const rep = getMixOverallReplacement(slug);
      if (!rep || !rep.slug) {
        return;
      }
      state.mixSlots[slotIndex] = rep.slug;
      mixMarked.delete(slug);
      if (mixHighlightSource === slug) {
        mixHighlightSource = null;
        mixHighlightMap = {};
      }
      compactMixSlots();
      renderMix();
      return;
    }
    if (action === "remove") {
      removeHeroFromMixSlot(slotIndex);
    }
  }

  function clearMixDragGhost() {
    if (mixDragGhostEl && mixDragGhostEl.parentNode) {
      mixDragGhostEl.parentNode.removeChild(mixDragGhostEl);
    }
    mixDragGhostEl = null;
  }

  function setMixDragImage(e, card) {
    clearMixDragGhost();
    const rect = card.getBoundingClientRect();
    const clone = card.cloneNode(true);
    clone.classList.add("mix-drag-ghost");
    clone.setAttribute("aria-hidden", "true");
    clone.style.position = "fixed";
    clone.style.top = "-10000px";
    clone.style.left = "0";
    clone.style.width = rect.width + "px";
    clone.style.height = rect.height + "px";
    clone.style.margin = "0";
    clone.style.pointerEvents = "none";
    clone.style.transform = "none";
    clone.style.opacity = "1";
    const nameH2 = card.querySelector(".hero-card-name h2");
    const cloneH2 = clone.querySelector(".hero-card-name h2");
    if (nameH2 && cloneH2 && nameH2.style.fontSize) {
      cloneH2.style.fontSize = nameH2.style.fontSize;
    }
    document.body.appendChild(clone);
    mixDragGhostEl = clone;
    e.dataTransfer.setDragImage(
      clone,
      e.clientX - rect.left,
      e.clientY - rect.top
    );
  }

  function mixDragSourceFromEvent(e) {
    const card = e.target.closest(".hero-card[data-mix-source]");
    return card ? card.dataset.mixSource : "";
  }

  function initMixInteractions() {
    const state = window.AFKJ.state;
    const dom = state.dom;
    if (!dom.mixView) {
      return;
    }

    const mixFocusSelector = dom.mixView.querySelector(".mix-focus-selector");
    if (mixFocusSelector) {
      mixFocusSelector.addEventListener("click", function (e) {
        const btn = e.target.closest(".mix-focus-btn");
        if (!btn) {
          return;
        }
        const key = btn.dataset.focus;
        if (key && Object.prototype.hasOwnProperty.call(state.mixFocus, key)) {
          state.mixFocus[key] = !state.mixFocus[key];
        }
        syncMixFocusButtons();
        loadMixData().then(renderMix);
      });
    }

    const modeSelector = dom.mixView.querySelector(".mix-mode-selector");
    if (modeSelector) {
      modeSelector.addEventListener("click", function (e) {
        const btn = e.target.closest(".mix-mode-btn");
        if (!btn) {
          return;
        }
        const mode = btn.dataset.mode;
        state.mixMode = state.mixMode === mode ? null : mode;
        renderMix();
      });
    }

    if (dom.mixRemoveAllBtn) {
      dom.mixRemoveAllBtn.addEventListener("click", function () {
        state.mixSlots = [null, null, null, null, null];
        mixMarked.clear();
        mixHighlightSource = null;
        mixHighlightMap = {};
        renderMix();
      });
    }

    dom.mixView.addEventListener("dragstart", function (e) {
      if (state.viewMode !== "mix") {
        return;
      }
      const card = e.target.closest(".hero-card[data-slug]");
      const slug = card ? card.dataset.slug : "";
      if (!slug) {
        return;
      }
      mixDragDidMove = false;
      e.dataTransfer.setData("text/plain", slug);
      e.dataTransfer.setData(
        "application/x-afkj-mix-source",
        mixDragSourceFromEvent(e) || "grid"
      );
      e.dataTransfer.effectAllowed = "move";
      setMixDragImage(e, card);
    });

    dom.mixView.addEventListener("drag", function () {
      mixDragDidMove = true;
    });

    dom.mixView.addEventListener("dragend", function () {
      clearMixDragGhost();
      setTimeout(function () {
        mixDragDidMove = false;
      }, 0);
    });

    dom.mixView.addEventListener("dragover", function (e) {
      if (state.viewMode !== "mix") {
        return;
      }
      const grid = e.target.closest(".mix-hero-grid");
      const zone = e.target.closest(".mix-drop-zone");
      if (zone || grid) {
        e.preventDefault();
        e.dataTransfer.dropEffect = "move";
      }
      dom.mixView.querySelectorAll(".mix-drag-over").forEach(function (el) {
        el.classList.remove("mix-drag-over");
      });
      if (zone) {
        zone.classList.add("mix-drag-over");
      } else if (grid) {
        grid.classList.add("mix-drag-over");
      }
    });

    dom.mixView.addEventListener("dragleave", function (e) {
      const related = e.relatedTarget;
      if (related && dom.mixView.contains(related)) {
        return;
      }
      dom.mixView.querySelectorAll(".mix-drag-over").forEach(function (el) {
        el.classList.remove("mix-drag-over");
      });
    });

    dom.mixView.addEventListener("drop", function (e) {
      if (state.viewMode !== "mix") {
        return;
      }
      e.preventDefault();
      dom.mixView.querySelectorAll(".mix-drag-over").forEach(function (el) {
        el.classList.remove("mix-drag-over");
      });
      const slug = e.dataTransfer.getData("text/plain");
      const source = e.dataTransfer.getData("application/x-afkj-mix-source");
      if (!slug) {
        return;
      }
      const slotEl = e.target.closest(".mix-slot");
      const gridEl = e.target.closest(".mix-hero-grid");
      const zoneEl = e.target.closest(".mix-drop-zone");

      if (gridEl && source.indexOf("slot-") === 0) {
        removeSlugFromMixSlots(slug);
        renderMix();
        return;
      }

      if (slotEl || zoneEl) {
        placeHeroInMixZone(slug, source);
      }
    });

    dom.mixView.addEventListener("pointerdown", function (e) {
      if (state.viewMode !== "mix" || e.button !== 0) {
        return;
      }
      const card = e.target.closest("#mix-hero-grid .hero-card");
      if (!card) {
        mixGridPointer = null;
        return;
      }
      mixGridPointer = {
        slug: card.dataset.slug,
        x: e.clientX,
        y: e.clientY,
      };
    });

    dom.mixView.addEventListener("pointerup", function (e) {
      if (state.viewMode !== "mix" || !mixGridPointer) {
        return;
      }
      const card = e.target.closest("#mix-hero-grid .hero-card");
      const pointer = mixGridPointer;
      mixGridPointer = null;
      if (!card || card.dataset.slug !== pointer.slug) {
        return;
      }
      const dx = e.clientX - pointer.x;
      const dy = e.clientY - pointer.y;
      if (dx * dx + dy * dy > 36) {
        return;
      }
      e.preventDefault();
      if (!tryReplaceHighlightedAlternative(pointer.slug)) {
        addHeroToMixZone(pointer.slug);
      }
    });

    dom.mixView.addEventListener("click", function (e) {
      if (state.viewMode !== "mix") {
        return;
      }
      const slotCard = e.target.closest(".mix-slot .hero-card");
      if (slotCard) {
        e.preventDefault();
        e.stopPropagation();
        if (MIX_TOUCH_DEVICE.matches) {
          return;
        }
        const slot = slotCard.closest(".mix-slot");
        const index = slot ? parseInt(slot.dataset.slot, 10) : -1;
        if (index >= 0) {
          removeHeroFromMixSlot(index);
        }
        return;
      }
    });

    dom.mixView.addEventListener("touchend", function (e) {
      if (state.viewMode !== "mix") {
        return;
      }
      const slotCard = e.target.closest(".mix-slot .hero-card");
      if (!slotCard) {
        return;
      }
      const slot = slotCard.closest(".mix-slot");
      const index = slot ? parseInt(slot.dataset.slot, 10) : -1;
      if (index < 0) {
        return;
      }
      const touch = e.changedTouches[0];
      if (!touch) {
        return;
      }
      const tapKey = index + "|" + slotCard.dataset.slug;
      const now = Date.now();
      if (
        mixSlotLastTap &&
        mixSlotLastTap.key === tapKey &&
        now - mixSlotLastTap.time < config.MIX_SLOT_DOUBLE_TAP_MS
      ) {
        e.preventDefault();
        mixSlotLastTap = null;
        openMixContextMenu(index, touch.clientX, touch.clientY);
        return;
      }
      mixSlotLastTap = { key: tapKey, time: now };
    });

    dom.mixView.addEventListener("contextmenu", function (e) {
      if (state.viewMode !== "mix") {
        return;
      }
      const slotCard = e.target.closest(".mix-slot .hero-card");
      if (slotCard) {
        e.preventDefault();
        e.stopPropagation();
        const slot = slotCard.closest(".mix-slot");
        const index = slot ? parseInt(slot.dataset.slot, 10) : -1;
        if (index >= 0) {
          openMixContextMenu(index, e.clientX, e.clientY);
        }
        return;
      }
      const gridCard = e.target.closest("#mix-hero-grid .hero-card");
      if (gridCard && gridCard.dataset.slug) {
        e.preventDefault();
        e.stopPropagation();
        openMixGridContextMenu(gridCard.dataset.slug, e.clientX, e.clientY);
      }
    });

    ensureMixContextMenu();
  }

  // Export module API to window.AFKJ.views.mix
  window.AFKJ.views.mix = {
    loadMixData: loadMixData,
    mixSlottedSlugSet: mixSlottedSlugSet,
    compactMixSlots: compactMixSlots,
    mixFirstFreeSlotIndex: mixFirstFreeSlotIndex,
    removeSlugFromMixSlots: removeSlugFromMixSlots,
    clearMixAlternativeHighlights: clearMixAlternativeHighlights,
    mixSlotIndexForSlug: mixSlotIndexForSlug,
    tryReplaceHighlightedAlternative: tryReplaceHighlightedAlternative,
    addHeroToMixZone: addHeroToMixZone,
    placeHeroInMixZone: placeHeroInMixZone,
    synergyScoreForPair: synergyScoreForPair,
    getQualifyingMixFactions: getQualifyingMixFactions,
    mixHeroSkillTags: mixHeroSkillTags,
    mixHeroBehaviorTags: mixHeroBehaviorTags,
    computeMixSpeedBonus: computeMixSpeedBonus,
    computeMixFocusBonus: computeMixFocusBonus,
    computeMixScore: computeMixScore,
    mixRawRoleProminence: mixRawRoleProminence,
    resolvePrydwenTierRank: resolvePrydwenTierRank,
    roleProminenceTierPoints: roleProminenceTierPoints,
    mixCombinedRoleProminenceRaw: mixCombinedRoleProminenceRaw,
    normalizeScores: normalizeScores,
    computeNormalizedRoleBonuses: computeNormalizedRoleBonuses,
    computeNormalizedTierBonuses: computeNormalizedTierBonuses,
    mixPoolHeroes: mixPoolHeroes,
    mixSortedPoolHeroes: mixSortedPoolHeroes,
    renderMixHeroCard: renderMixHeroCard,
    renderMixSlots: renderMixSlots,
    animateMixGridReorder: animateMixGridReorder,
    renderMixGrid: renderMixGrid,
    renderMix: renderMix,
    syncMixFocusButtons: syncMixFocusButtons,
    syncMixModeButtons: syncMixModeButtons,
    buildMixHighlightMap: buildMixHighlightMap,
    getMixOverallReplacement: getMixOverallReplacement,
    closeMixContextMenu: closeMixContextMenu,
    openMixContextMenu: openMixContextMenu,
    openMixGridContextMenu: openMixGridContextMenu,
    removeHeroFromMixSlot: removeHeroFromMixSlot,
    initMixInteractions: initMixInteractions,
  };
})();

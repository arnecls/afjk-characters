window.AFKJ = window.AFKJ || {};

(function () {
  const utils = window.AFKJ.utils;
  const escapeHtml = utils.escapeHtml.bind(utils);

  const PRYDWEN_TIER_MODES = [
    { key: "afk_stages", label: "AFK Stages" },
    { key: "dream_realm", label: "Dream Realm" },
    { key: "dream_realm_endless", label: "Dream Realm (Endless)" },
    { key: "pvp", label: "PVP" },
  ];

  const TIER_CSV_COLUMNS = [
    { header: "AFK Stages tier", key: "afk_stages" },
    { header: "Dream Realm tier", key: "dream_realm" },
    { header: "Dream Realm Endless tier", key: "dream_realm_endless" },
    { header: "PVP tier", key: "pvp" },
  ];

  const TIER_CSV_HEADERS = {};
  TIER_CSV_COLUMNS.forEach(function (tierCol) {
    TIER_CSV_HEADERS[tierCol.header] = true;
  });

  const TIER_RANK_ORDER = ["C", "B", "A", "A+", "S", "S+"];
  const REFERENCE_TIER_WEIGHT = 7;
  const REFERENCE_TIER_POINTS_PER_STEP = 100;
  const TIER_FILTER_ORDER = ["?", "C", "B", "A", "A+", "S", "S+"];

  function isUnrankedPrydwenTier(tier) {
    const value = tier != null ? String(tier).trim() : "";
    return !value || value === "?";
  }

  function prydwenTierClass(tier) {
    if (isUnrankedPrydwenTier(tier)) {
      return "tier-unknown";
    }
    const normalized = String(tier).trim().replace(/\+/g, "-plus");
    return "tier-" + normalized.toLowerCase();
  }

  function prydwenTierDisplay(tier) {
    return isUnrankedPrydwenTier(tier) ? "?" : String(tier).trim();
  }

  function prydwenTierRank(tier) {
    if (!tier || tier === "?") {
      return -1;
    }
    const idx = TIER_RANK_ORDER.indexOf(tier);
    return idx >= 0 ? idx : -1;
  }

  function comparePrydwenTiers(repTier, mainTier) {
    const repRank = prydwenTierRank(repTier);
    const mainRank = prydwenTierRank(mainTier);
    if (mainRank < 0 && repRank < 0) {
      return "same";
    }
    if (mainRank < 0) {
      return "better";
    }
    if (repRank < 0) {
      return "worse";
    }
    if (repRank > mainRank) {
      return "better";
    }
    if (repRank < mainRank) {
      return mainRank - repRank === 1 ? "worse-1" : "worse";
    }
    return "same";
  }

  function relativeTierTooltip(
    relation,
    mainHeroName,
    modeLabel,
    mainTier,
    repTier
  ) {
    const base = mainHeroName + "'s " + modeLabel + " tier";
    if (!mainTier) {
      return "No Prydwen tier listed for " + base + ".";
    }
    if (!repTier) {
      return "No Prydwen tier listed for this replacement hero.";
    }
    if (relation === "better") {
      return "Better than " + base + " (" + mainTier + "). This replacement is " + repTier + ".";
    }
    if (relation === "worse-1") {
      return "One tier below " + base + " (" + mainTier + "). This replacement is " + repTier + ".";
    }
    if (relation === "worse") {
      return "Worse than " + base + " (" + mainTier + "). This replacement is " + repTier + ".";
    }
    return "Same as " + base + " (" + mainTier + ").";
  }

  function formatTierColumnHeader(col) {
    if (col.endsWith(" tier")) {
      return escapeHtml(col.slice(0, -5)) + "<br>" + escapeHtml("tier");
    }
    return escapeHtml(col);
  }

  function getHeroPrydwenTiers(hero) {
    const tiers = (hero && hero.prydwenTiers) || {};
    const out = {};
    PRYDWEN_TIER_MODES.forEach(function (mode) {
      const raw = tiers[mode.key];
      out[mode.key] = isUnrankedPrydwenTier(raw) ? "?" : String(raw).trim();
    });
    return out;
  }

  function renderTierTableCell(tier) {
    const value = (tier || "").trim();
    const display = prydwenTierDisplay(value);
    return (
      '<span class="tier-chip tier-chip-table ' +
      prydwenTierClass(value) +
      '"><span class="tier-grade">' +
      escapeHtml(display) +
      "</span></span>"
    );
  }

  function augmentCsvWithTiers() {
    const state = window.AFKJ.state;
    if (!state.csvHeaders.length || !Object.keys(state.heroByName).length) {
      return;
    }
    const classIdx = state.csvHeaders.indexOf("Class");
    if (classIdx === -1) {
      return;
    }

    let roleIdx = state.csvHeaders.indexOf("Role");
    if (roleIdx === -1) {
      roleIdx = classIdx + 1;
      state.csvHeaders.splice(roleIdx, 0, "Role");
      state.csvRows = state.csvRows.map(function (row) {
        const newRow = row.slice();
        newRow.splice(roleIdx, 0, "");
        return newRow;
      });
    }

    const missing = TIER_CSV_COLUMNS.filter(function (tierCol) {
      return state.csvHeaders.indexOf(tierCol.header) === -1;
    });
    if (missing.length) {
      const insertAt = roleIdx + 1;
      missing.forEach(function (tierCol, offset) {
        state.csvHeaders.splice(insertAt + offset, 0, tierCol.header);
      });
      state.csvRows = state.csvRows.map(function (row) {
        const newRow = row.slice();
        missing.forEach(function (_, offset) {
          newRow.splice(insertAt + offset, 0, "");
        });
        return newRow;
      });
    }

    const colByKey = {};
    TIER_CSV_COLUMNS.forEach(function (tierCol) {
      const idx = state.csvHeaders.indexOf(tierCol.header);
      if (idx !== -1) {
        colByKey[tierCol.key] = idx;
      }
    });

    const roleColIdx = state.csvHeaders.indexOf("Role");
    state.csvRows.forEach(function (row) {
      const hero = state.heroByName[row[0] || ""];
      if (!hero) {
        return;
      }
      if (roleColIdx !== -1 && !String(row[roleColIdx] || "").trim()) {
        const roleMeta = window.AFKJ.config.ROLE_CATEGORY_META[hero.roleCategory];
        if (roleMeta) {
          row[roleColIdx] = roleMeta.label;
        }
      }
      const tiers = getHeroPrydwenTiers(hero);
      Object.keys(colByKey).forEach(function (key) {
        const idx = colByKey[key];
        if (!String(row[idx] || "").trim()) {
          row[idx] = tiers[key] || "?";
        }
      });
    });
  }

  function renderPrydwenTierBoxes(tiers, variant, compareTo, mainHeroName) {
    if (!tiers) {
      return "";
    }
    const compact = variant === "compact";
    const relative = compact && compareTo;
    const rowClass = compact ? "tier-box-row tier-box-row-compact" : "tier-box-row";
    const chipClass = compact ? "tier-chip tier-chip-compact" : "tier-chip";
    let html = '<div class="' + rowClass + '">';
    PRYDWEN_TIER_MODES.forEach(function (mode) {
      const rawTier = tiers[mode.key];
      const displayTier = prydwenTierDisplay(rawTier);
      let colorClass = prydwenTierClass(rawTier);
      let tipAttrs = "";
      if (relative) {
        const mainTier = compareTo[mode.key];
        const relation = comparePrydwenTiers(rawTier, mainTier);
        colorClass = "tier-rel-" + relation;
        tipAttrs = window.AFKJ.chips.chipTipAttrs(
          relativeTierTooltip(
            relation,
            mainHeroName || "this hero",
            mode.label,
            mainTier,
            displayTier
          )
        );
      }
      html +=
        '<span class="' +
        chipClass +
        " " +
        colorClass +
        (tipAttrs ? " chip-has-tip" : "") +
        '"' +
        tipAttrs +
        ">" +
        '<span class="tier-grade">' +
        escapeHtml(displayTier) +
        "</span>" +
        '<span class="tier-mode">' +
        escapeHtml(mode.label) +
        "</span></span>";
    });
    html += "</div>";
    return html;
  }

  function stripPrydwenTierLine(md) {
    if (!md) {
      return md;
    }
    const parts = md.split("\n\n");
    if (parts.length < 3) {
      return md;
    }
    if (!parts[0].endsWith("'s behavior")) {
      return md;
    }
    if (parts[1].startsWith("- ") || parts[1].startsWith("#")) {
      return md;
    }
    return [parts[0], parts.slice(2).join("\n\n")].join("\n\n");
  }

  function roleCategoryMeta(roleCategory) {
    return window.AFKJ.config.ROLE_CATEGORY_META[roleCategory] || null;
  }

  // Export module API to window.AFKJ.tiers
  window.AFKJ.tiers = {
    PRYDWEN_TIER_MODES: PRYDWEN_TIER_MODES,
    TIER_CSV_COLUMNS: TIER_CSV_COLUMNS,
    TIER_CSV_HEADERS: TIER_CSV_HEADERS,
    TIER_RANK_ORDER: TIER_RANK_ORDER,
    REFERENCE_TIER_WEIGHT: REFERENCE_TIER_WEIGHT,
    REFERENCE_TIER_POINTS_PER_STEP: REFERENCE_TIER_POINTS_PER_STEP,
    TIER_FILTER_ORDER: TIER_FILTER_ORDER,
    isUnrankedPrydwenTier: isUnrankedPrydwenTier,
    prydwenTierClass: prydwenTierClass,
    prydwenTierDisplay: prydwenTierDisplay,
    prydwenTierRank: prydwenTierRank,
    comparePrydwenTiers: comparePrydwenTiers,
    relativeTierTooltip: relativeTierTooltip,
    formatTierColumnHeader: formatTierColumnHeader,
    getHeroPrydwenTiers: getHeroPrydwenTiers,
    renderTierTableCell: renderTierTableCell,
    augmentCsvWithTiers: augmentCsvWithTiers,
    renderPrydwenTierBoxes: renderPrydwenTierBoxes,
    stripPrydwenTierLine: stripPrydwenTierLine,
    roleCategoryMeta: roleCategoryMeta,
  };
})();

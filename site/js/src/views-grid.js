window.AFKJ = window.AFKJ || {};

(function () {
  const utils = window.AFKJ.utils;
  const config = window.AFKJ.config;
  const escapeHtml = utils.escapeHtml.bind(utils);

  function renderHeroPortrait(hero, extraClass) {
    const factionKey = utils.factionDataKey(hero.faction);
    const combatIcon = utils.combatIconPath(hero);
    const combatSrc = utils.assetUrl(combatIcon || hero.portrait);
    const portraitFallback = utils.assetUrl(hero.portrait);
    return (
      '<div class="hero-card-portrait hero-card-portrait--' +
      escapeHtml(factionKey) +
      (extraClass ? " " + extraClass : "") +
      '">' +
      '<div class="hero-card-portrait-frame">' +
      '<img class="hero-card-combat-icon" src="' +
      escapeHtml(combatSrc) +
      '" alt="" loading="lazy" onerror="this.onerror=null;this.src=' +
      JSON.stringify(portraitFallback) +
      '">' +
      "</div></div>"
    );
  }

  function renderGridCardFactionIcon(hero) {
    if (!hero.faction) {
      return "";
    }
    const icon = utils.iconPath("factions", hero.faction);
    if (!icon) {
      return "";
    }
    return (
      '<img class="hero-card-faction-icon" src="' +
      utils.assetUrl(icon) +
      '" alt="' +
      escapeHtml(hero.faction) +
      '" loading="lazy">'
    );
  }

  function renderGridCardClassIcon(hero) {
    if (!hero.class) {
      return "";
    }
    const icon = utils.iconPath("class", hero.class);
    if (!icon) {
      return "";
    }
    return (
      '<span class="hero-card-class-badge">' +
      '<img src="' +
      utils.assetUrl(icon) +
      '" alt="' +
      escapeHtml(hero.class) +
      '" loading="lazy">' +
      "</span>"
    );
  }

  function renderGridCardFactionStack(hero) {
    const factionIcon = renderGridCardFactionIcon(hero);
    const classIcon = renderGridCardClassIcon(hero);
    if (!factionIcon && !classIcon) {
      return "";
    }
    return (
      '<div class="hero-card-faction-stack">' +
      factionIcon +
      classIcon +
      "</div>"
    );
  }

  function renderGridCardRole(hero) {
    const meta = window.AFKJ.tiers.roleCategoryMeta(hero.roleCategory) || config.ROLE_CATEGORY_META[hero.roleCategory];
    if (!meta) {
      return "";
    }
    return (
      '<span class="hero-card-role ' +
      meta.className +
      '">' +
      escapeHtml(meta.label) +
      "</span>"
    );
  }

  function buildReferenceWavePath(options) {
    const leftX = options.leftX;
    const rightX = options.rightX;
    const curveRightX = options.curveRightX != null ? options.curveRightX : rightX;
    const peakX = options.peakX;
    const troughX = options.troughX;
    const peakY = options.peakY;
    const troughY = options.troughY;
    const leftY = options.leftY;
    const endY = options.endY;
    const xShift = options.xShift || 0;
    const xScale = options.xScale || 1;
    const xAnchor = options.xAnchor != null ? options.xAnchor : 50;
    const step = 1.5;

    function mapX(x) {
      const shifted = x + xShift;
      if (xScale === 1) {
        return shifted;
      }
      return xAnchor + (shifted - xAnchor) * xScale;
    }

    function edgeY(x) {
      if (x <= peakX) {
        const t = (x - leftX) / (peakX - leftX);
        return leftY + (peakY - leftY) * (1 - Math.cos(Math.PI * t)) / 2;
      }
      if (x <= troughX) {
        const t = (x - peakX) / (troughX - peakX);
        return peakY + (troughY - peakY) * (1 - Math.cos(Math.PI * t)) / 2;
      }
      if (x >= curveRightX) {
        return endY;
      }
      const t = (x - troughX) / (curveRightX - troughX);
      return troughY - (troughY - endY) * (1 - Math.cos(Math.PI * t)) / 2;
    }

    function fmt(n) {
      return (Math.round(n * 100) / 100).toString();
    }

    let d = "M" + fmt(mapX(leftX)) + " " + fmt(edgeY(leftX));
    for (let x = leftX + step; x < rightX; x += step) {
      d += " L" + fmt(mapX(x)) + " " + fmt(edgeY(x));
    }
    d += " L" + fmt(mapX(rightX)) + " " + fmt(edgeY(rightX));
    d += " L" + fmt(mapX(rightX)) + " 100 L" + fmt(mapX(leftX)) + " 100 Z";
    return d;
  }

  function heroCardWavePaths() {
    const panelPeakX = 27;
    const panelTroughX = panelPeakX + (78 - panelPeakX) * 1.3;
    return {
      panelPath: buildReferenceWavePath({
        leftX: -15,
        rightX: 115,
        peakX: panelPeakX,
        troughX: panelTroughX,
        peakY: 10,
        troughY: 28,
        leftY: 23,
        endY: 25,
      }),
      accentPath: buildReferenceWavePath({
        leftX: -22,
        rightX: 125,
        curveRightX: 130,
        peakX: 40,
        troughX: 95,
        peakY: 1,
        troughY: 19,
        leftY: 9,
        endY: 11,
        xShift: -20,
      }),
    };
  }

  function renderHeroCardWave(patternId) {
    const paths = heroCardWavePaths();
    const hatchId = "hero-panel-hatch-" + patternId;
    return (
      '<div class="hero-card-wave" aria-hidden="true">' +
      '<svg class="hero-card-wave-svg" viewBox="0 0 100 100" preserveAspectRatio="none">' +
      "<defs>" +
      '<pattern id="' +
      hatchId +
      '" width="3" height="3" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)">' +
      '<rect width="3" height="0.4" y="2.4" fill="var(--fc-hatch)"></rect>' +
      "</pattern></defs>" +
      '<path class="hero-card-wave-accent" d="' +
      paths.accentPath +
      '"></path>' +
      '<path class="hero-card-wave-panel" d="' +
      paths.panelPath +
      '"></path>' +
      '<path class="hero-card-wave-panel-hatch" d="' +
      paths.panelPath +
      '" fill="url(#' +
      hatchId +
      ')"></path></svg></div>'
    );
  }

  function renderCompactCardWave(patternId) {
    const paths = heroCardWavePaths();
    const hatchId = "hero-compact-hatch-" + patternId;
    return (
      '<div class="hero-compact-wave" aria-hidden="true">' +
      '<svg class="hero-compact-wave-svg" viewBox="0 0 100 100" preserveAspectRatio="none">' +
      "<defs>" +
      '<pattern id="' +
      hatchId +
      '" width="3" height="3" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)">' +
      '<rect width="3" height="0.4" y="2.4" fill="var(--compact-wave-hatch)"></rect>' +
      "</pattern></defs>" +
      '<g transform="translate(40 100) scale(2 1) rotate(-90)">' +
      '<path class="hero-compact-wave-accent" d="' +
      paths.accentPath +
      '"></path>' +
      '<path class="hero-compact-wave-panel" d="' +
      paths.panelPath +
      '"></path>' +
      '<path class="hero-compact-wave-panel-hatch" d="' +
      paths.panelPath +
      '" fill="url(#' +
      hatchId +
      ')"></path></g></svg></div>'
    );
  }

  const HERO_CARD_NAME_BASE_CQI = 13.5;
  const HERO_CARD_NAME_NARROW_CHARS = {
    i: 0.3,
    l: 0.3,
    I: 0.3,
    j: 0.5,
    t: 0.5,
  };

  function heroCardNameWordVisibleLength(word) {
    let visible = 0;
    for (let i = 0; i < word.length; i++) {
      visible += HERO_CARD_NAME_NARROW_CHARS[word[i]] ?? 1;
    }
    return visible;
  }

  function heroCardNameVisibleLength(text) {
    const words = text.trim().split(/\s+/).filter(Boolean);
    if (!words.length) {
      return 0;
    }
    const visibleLengths = words.map(heroCardNameWordVisibleLength);
    visibleLengths.forEach(function (_, index) {
      if (words[index].length === 1 && index > 0) {
        visibleLengths[index] += visibleLengths[index - 1] + 1;
      }
    });
    return Math.max.apply(null, visibleLengths);
  }

  function fitHeroCardName(h2) {
    const text = h2.textContent || "";
    if (text.length < 7) {
      h2.style.fontSize = "";
      return;
    }
    const visibleLength = heroCardNameVisibleLength(text);
    if (visibleLength < 7) {
      h2.style.fontSize = "";
      return;
    }
    const reduction = (visibleLength - 7) * 1.7;
    h2.style.fontSize =
      "calc(" + HERO_CARD_NAME_BASE_CQI + "cqi - " + reduction + "cqi)";
  }

  function fitHeroCardNames() {
    const state = window.AFKJ.state;
    if (state.viewMode === "mix") {
      const roots = [];
      if (state.dom.mixHeroGrid) {
        roots.push(state.dom.mixHeroGrid);
      }
      if (state.dom.mixDropZone) {
        roots.push(state.dom.mixDropZone);
      }
      roots.forEach(function (root) {
        root.querySelectorAll(".hero-card-name h2").forEach(fitHeroCardName);
      });
      return;
    }
    if (state.viewMode === "grid" && state.dom.heroGrid) {
      state.dom.heroGrid.querySelectorAll(".hero-card-name h2").forEach(fitHeroCardName);
    }
  }

  function scheduleFitHeroCardNames() {
    const run = fitHeroCardNames;
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(run).catch(run);
    } else {
      run();
    }
  }

  function buildHeroCardHtml(h, opts) {
    opts = opts || {};
    const factionKey = utils.factionDataKey(h.faction);

    let extraClass = opts.extraClass || "";
    if (opts.marked) {
      extraClass += " hero-card--mix-marked";
    }

    const dragAttr = opts.draggable ? ' draggable="true"' : "";
    const sourceAttr = opts.mixSource ? ' data-mix-source="' + escapeHtml(opts.mixSource) + '"' : "";
    const roleAttr = opts.role ? ' role="' + escapeHtml(opts.role) + '"' : "";

    const cardHtml =
      '<article class="hero-card afkj-box afkj-box-sm' +
      extraClass +
      '" data-slug="' +
      escapeHtml(h.slug) +
      '" data-faction="' +
      escapeHtml(factionKey) +
      '"' +
      dragAttr +
      sourceAttr +
      roleAttr +
      ' tabindex="0" aria-label="' +
      escapeHtml(h.name) +
      '">' +
      renderHeroPortrait(h) +
      renderHeroCardWave(h.slug) +
      '<div class="hero-card-info">' +
      '<div class="hero-card-name"><h2>' +
      escapeHtml(h.name) +
      "</h2></div>" +
      '<div class="hero-card-meta">' +
      renderGridCardRole(h) +
      "</div></div>" +
      renderGridCardFactionStack(h) +
      "</article>";

    if (opts.chromeHtml) {
      return (
        '<div class="hero-card-wrapper' +
        (opts.marked ? " hero-card-wrapper--mix-marked" : "") +
        '">' +
        cardHtml +
        opts.chromeHtml +
        "</div>"
      );
    }
    return cardHtml;
  }

  function renderGrid() {
    const state = window.AFKJ.state;
    const list = window.AFKJ.router.filteredHeroes();
    state.dom.heroGrid.innerHTML = list
      .map(function (h) {
        return buildHeroCardHtml(h, { role: "link" });
      })
      .join("");

    state.dom.emptyState.classList.toggle("hidden", list.length > 0);
    scheduleFitHeroCardNames();
  }

  // Export module API to window.AFKJ.views.grid
  window.AFKJ.views.grid = {
    renderHeroPortrait: renderHeroPortrait,
    renderGridCardFactionIcon: renderGridCardFactionIcon,
    renderGridCardClassIcon: renderGridCardClassIcon,
    renderGridCardFactionStack: renderGridCardFactionStack,
    renderGridCardRole: renderGridCardRole,
    renderHeroCardWave: renderHeroCardWave,
    renderCompactCardWave: renderCompactCardWave,
    fitHeroCardName: fitHeroCardName,
    fitHeroCardNames: fitHeroCardNames,
    scheduleFitHeroCardNames: scheduleFitHeroCardNames,
    buildHeroCardHtml: buildHeroCardHtml,
    renderGrid: renderGrid,
  };
})();

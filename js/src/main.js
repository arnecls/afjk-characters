window.AFKJ = window.AFKJ || {};

(function () {
  const utils = window.AFKJ.utils;
  const config = window.AFKJ.config;
  const state = window.AFKJ.state;
  const chips = window.AFKJ.chips;
  const list = window.AFKJ.views.list;
  const mix = window.AFKJ.views.mix;
  const grid = window.AFKJ.views.grid;
  const router = window.AFKJ.router;
  const escapeHtml = utils.escapeHtml.bind(utils);

  function readStoredViewMode() {
    try {
      const stored = localStorage.getItem(config.VIEW_MODE_KEY);
      if (stored === "grid" || stored === "list" || stored === "mix") {
        return stored;
      }
    } catch (e) {
      /* ignore quota / private-mode errors */
    }
    return "grid";
  }

  function storeViewMode(mode) {
    try {
      localStorage.setItem(config.VIEW_MODE_KEY, mode);
    } catch (e) {
      /* ignore quota / private-mode errors */
    }
  }

  function syncViewToggleButtons() {
    const dom = state.dom;
    if (!dom.viewToggle) {
      return;
    }
    dom.viewToggle.querySelectorAll(".view-btn").forEach(function (b) {
      const active = b.dataset.view === state.viewMode;
      b.classList.toggle("active", active);
      b.setAttribute("aria-pressed", active ? "true" : "false");
    });
  }

  function buildFilters() {
    const dom = state.dom;
    const factions = [];
    const classes = [];
    const seenF = {};
    const seenC = {};
    const seenRoles = {};
    state.heroes.forEach(function (h) {
      if (h.faction && !seenF[h.faction]) {
        seenF[h.faction] = true;
        factions.push(h.faction);
      }
      if (h.class && !seenC[h.class]) {
        seenC[h.class] = true;
        classes.push(h.class);
      }
      if (h.roleCategory && !seenRoles[h.roleCategory]) {
        seenRoles[h.roleCategory] = true;
      }
    });
    factions.sort();
    classes.sort();

    let html =
      '<div class="filter-row filter-row-faction">' +
      '<span class="filter-label">Faction</span>';
    factions.forEach(function (f) {
      html +=
        '<button type="button" class="filter-btn" data-filter="faction" data-value="' +
        escapeHtml(f) +
        '">' +
        escapeHtml(f) +
        "</button>";
    });
    html += "</div>";
    html += '<div class="filter-row filter-row-secondary">';
    html += '<div class="filter-secondary-groups">';
    html += '<div class="filter-group filter-group-class">';
    html += '<span class="filter-label">Class</span>';
    classes.forEach(function (c) {
      html +=
        '<button type="button" class="filter-btn" data-filter="class" data-value="' +
        escapeHtml(c) +
        '">' +
        escapeHtml(c) +
        "</button>";
    });
    html += "</div>";
    html += '<div class="filter-group filter-group-role">';
    html += '<span class="filter-label filter-label-role">Role</span>';
    config.ROLE_FILTER_ORDER.forEach(function (roleKey) {
      if (!seenRoles[roleKey]) {
        return;
      }
      const meta = config.ROLE_CATEGORY_META[roleKey];
      html +=
        '<button type="button" class="filter-btn" data-filter="role" data-value="' +
        escapeHtml(roleKey) +
        '">' +
        escapeHtml(meta.label) +
        "</button>";
    });
    html += "</div></div></div>";
    dom.filtersEl.innerHTML = html;
    updateFilterActiveStates();
    window.AFKJ.ui.updateListStickyOffset();
  }

  function updateFilterActiveStates() {
    const dom = state.dom;
    dom.filtersEl.querySelectorAll(".filter-btn").forEach(function (b) {
      const f = b.dataset.filter;
      if (f === "faction") {
        b.classList.toggle("active", b.dataset.value === state.activeFaction);
      } else if (f === "class") {
        b.classList.toggle("active", b.dataset.value === state.activeClass);
      } else if (f === "role") {
        b.classList.toggle("active", b.dataset.value === state.activeRole);
      }
    });
    window.AFKJ.ui.updateFiltersToggleLabel();
  }

  function initCsv(text) {
    const dom = state.dom;
    const parsed = list.parseCsv(text);
    if (!parsed.length) {
      state.csvHeaders = [];
      state.csvRows = [];
      return;
    }
    state.csvHeaders = parsed[0];
    state.csvRows = parsed.slice(1);
    state.csvColumnWidths = [];
    state.columnWidthsLocked = false;
    window.AFKJ.tiers.augmentCsvWithTiers();
    list.buildColumnFilterOptions();
    if (!dom.detailView.classList.contains("hidden")) {
      return;
    }
    router.renderCurrentView();
  }

  function initHeroes(data) {
    state.heroes = data.heroes || [];
    state.heroesMeta = data.meta || {};
    state.heroBySlug = {};
    state.heroByName = {};
    state.heroes.forEach(function (h) {
      state.heroBySlug[h.slug] = h;
      state.heroByName[h.name] = h;
    });
    window.AFKJ.tiers.augmentCsvWithTiers();
    list.buildColumnFilterOptions();
    buildFilters();
    router.route();
  }

  function localServerHint() {
    return (
      "<code>python3 -m http.server</code> from the " +
      "<code>site/</code> directory (after " +
      "<code>just render-site</code>)."
    );
  }

  function loadHeroData() {
    const dom = state.dom;
    if (location.protocol === "file:") {
      dom.heroGrid.innerHTML =
        '<p class="empty-state">Open this site via a local web server: ' +
        localServerHint() +
        "</p>";
      return;
    }
    fetch(utils.assetUrl("data/heroes.json"))
      .then(function (r) {
        if (!r.ok) throw new Error("Failed to load hero data");
        return r.json();
      })
      .then(initHeroes)
      .catch(function (err) {
        dom.heroGrid.innerHTML =
          '<p class="empty-state">Could not load hero data: ' +
          escapeHtml(String(err)) +
          ". Run <code>just render-site</code>.</p>";
      });
  }

  function initListColumns(columns) {
    const byId = {};
    (columns || []).forEach(function (col) {
      byId[col.id] = col;
    });
    state.listColumnsById = byId;
  }

  function loadCsvData() {
    if (location.protocol === "file:") {
      return;
    }
    const columnsPromise = fetch(utils.assetUrl("data/list-columns.json"))
      .then(function (r) {
        if (!r.ok) {
          return [];
        }
        return r.json();
      })
      .catch(function () {
        return [];
      });
    const csvPromise = fetch(utils.assetUrl("data/heroes-overview.csv"))
      .then(function (r) {
        if (!r.ok) {
          throw new Error("Failed to load table data");
        }
        return r.text();
      });
    Promise.all([columnsPromise, csvPromise])
      .then(function (results) {
        initListColumns(results[0]);
        initCsv(results[1]);
      })
      .catch(function () {
        /* list view shows missing-data message */
      });
  }

  // Application bootstrap
  document.addEventListener("DOMContentLoaded", function () {
    // Resolve base path
    state.BASE = utils.resolveBase();

    // Cache DOM Elements
    state.dom = {
      gridView: document.getElementById("grid-view"),
      listView: document.getElementById("list-view"),
      mixView: document.getElementById("mix-view"),
      detailView: document.getElementById("detail-view"),
      heroGrid: document.getElementById("hero-grid"),
      mixHeroGrid: document.getElementById("mix-hero-grid"),
      mixDropZone: document.getElementById("mix-drop-zone"),
      mixEmptyState: document.getElementById("mix-empty-state"),
      mixRemoveAllBtn: document.getElementById("mix-remove-all"),
      heroDetail: document.getElementById("hero-detail"),
      emptyState: document.getElementById("empty-state"),
      listEmptyState: document.getElementById("list-empty-state"),
      heroesTableHead: document.getElementById("heroes-table-head"),
      heroesTableBody: document.getElementById("heroes-table-body"),
      heroesTable: document.getElementById("heroes-table"),
      searchInput: document.getElementById("search"),
      filtersPanel: document.getElementById("filters-panel"),
      filtersEl: document.getElementById("filters"),
      filtersToggle: document.getElementById("filters-toggle"),
      filtersToggleLabel: document.getElementById("filters-toggle-label"),
      headerBack: document.getElementById("header-back"),
      viewToggle: document.querySelector(".view-toggle"),
      siteHeader: document.querySelector(".site-header"),
    };

    const dom = state.dom;

    // Load initial stored state
    state.viewMode = readStoredViewMode();
    state.activeFaction = "";
    state.activeClass = "";
    state.activeRole = "";

    syncViewToggleButtons();

    // Run UI Initializations
    window.AFKJ.ui.initWelcomeWarning();
    window.AFKJ.ui.initFiltersCollapse();
    window.AFKJ.ui.initChipTooltips();
    window.AFKJ.ui.initSkillCardPopover();

    // List sticky offsets
    window.addEventListener("resize", window.AFKJ.ui.updateListStickyOffset);
    if (dom.siteHeader && typeof ResizeObserver !== "undefined") {
      new ResizeObserver(window.AFKJ.ui.updateListStickyOffset).observe(dom.siteHeader);
    }

    // Mix Mode interaction initialization
    mix.initMixInteractions();

    // Attach filters click listener
    dom.filtersEl.addEventListener("click", function (e) {
      const btn = e.target.closest(".filter-btn");
      if (!btn) {
        return;
      }
      if (btn.dataset.filter === "faction") {
        const v = btn.dataset.value;
        state.activeFaction = state.activeFaction === v ? "" : v;
      } else if (btn.dataset.filter === "class") {
        const v = btn.dataset.value;
        const next = state.activeClass === v ? "" : v;
        state.activeClass = next;
        if (next) {
          state.activeRole = "";
        }
      } else if (btn.dataset.filter === "role") {
        const v = btn.dataset.value;
        const next = state.activeRole === v ? "" : v;
        state.activeRole = next;
        if (next) {
          state.activeClass = "";
        }
      }
      updateFilterActiveStates();
      router.renderCurrentView();
    });

    // Attach search event
    dom.searchInput.addEventListener("input", router.renderCurrentView);

    // View toggles (grid / list / mix)
    if (dom.viewToggle) {
      dom.viewToggle.addEventListener("click", function (e) {
        const btn = e.target.closest(".view-btn");
        if (!btn) {
          return;
        }
        state.viewMode = btn.dataset.view;
        storeViewMode(state.viewMode);
        syncViewToggleButtons();
        if (!dom.detailView.classList.contains("hidden")) {
          return;
        }
        router.showIndexView();
      });
    }

    // Heroes table head and filtering listeners
    if (dom.heroesTableHead) {
      dom.heroesTableHead.addEventListener("mousedown", function (e) {
        if (e.target.closest(".col-filter-combine-toggle")) {
          e.stopPropagation();
        }
      });

      dom.heroesTableHead.addEventListener("click", function (e) {
        const clearBtn = e.target.closest(".col-filter-clear");
        if (clearBtn) {
          e.preventDefault();
          e.stopPropagation();
          const col = parseInt(clearBtn.dataset.col, 10);
          state.openColumnFilter = col;
          delete state.csvColumnFilters[col];
          list.renderList();
          return;
        }

        const combineToggle = e.target.closest(".col-filter-combine-toggle");
        if (combineToggle) {
          e.preventDefault();
          e.stopPropagation();
          const col = parseInt(combineToggle.dataset.col, 10);
          list.toggleColumnFilterCombine(col);
          return;
        }

        if (e.target.closest(".col-filter-panel")) {
          return;
        }

        const filterTrigger = e.target.closest(".col-filter-trigger");
        if (filterTrigger) {
          const details = filterTrigger.closest("details.col-filter");
          if (details) {
            state.openColumnFilter = parseInt(details.dataset.col, 10);
          }
          return;
        }

        const sortBtn = e.target.closest(".th-sort-btn");
        if (!sortBtn) {
          return;
        }
        const col = parseInt(sortBtn.dataset.col, 10);
        if (col === state.sortColumn) {
          state.sortDir = -state.sortDir;
        } else {
          state.sortColumn = col;
          state.sortDir = 1;
        }
        list.renderList();
      });

      dom.heroesTableHead.addEventListener("change", function (e) {
        const input = e.target;
        if (input.type !== "checkbox") {
          return;
        }
        const details = input.closest("details.col-filter");
        if (!details) {
          return;
        }
        const col = parseInt(details.dataset.col, 10);
        const value = input.value;
        if (!state.csvColumnFilters[col]) {
          state.csvColumnFilters[col] = [];
        }
        const set = new Set(state.csvColumnFilters[col]);
        if (input.checked) {
          set.add(value);
        } else {
          set.delete(value);
        }
        state.csvColumnFilters[col] = Array.from(set);
        if (state.csvColumnFilters[col].length === 0) {
          delete state.csvColumnFilters[col];
        }
        state.openColumnFilter = col;
        list.renderList();
      });

      dom.heroesTableHead.addEventListener("toggle", function (e) {
        const details = e.target;
        if (!details.matches || !details.matches("details.col-filter")) {
          return;
        }
        if (details.open) {
          state.openColumnFilter = parseInt(details.dataset.col, 10);
          // Render filter panel options dynamically
          const panelContainer = details.querySelector(".col-filter-panel-placeholder");
          if (panelContainer) {
            const col = state.openColumnFilter;
            const title = state.csvHeaders[col];
            const groups = state.csvColumnFilterOptions[col] || [];
            panelContainer.innerHTML = list.renderColumnFilterPanel(col, title, groups);
          }
          requestAnimationFrame(list.positionOpenColumnFilter);
          list.bindColumnFilterPointerTracking();
        } else {
          list.clearColumnFilterPanelPosition(details);
          list.unbindColumnFilterPointerTracking();
          if (state.openColumnFilter === parseInt(details.dataset.col, 10)) {
            state.openColumnFilter = -1;
          }
        }
      }, true);

      const tableScrollEl = list.getTableScrollEl();
      if (tableScrollEl) {
        tableScrollEl.addEventListener("scroll", list.closeColumnFilterOnScroll, {
          passive: true,
        });
      }
      window.addEventListener("scroll", list.closeColumnFilterOnScroll, {
        passive: true,
      });
      window.addEventListener("resize", list.positionOpenColumnFilter);
    }

    // Global document navigation clicks
    document.addEventListener("click", function (e) {
      const home = e.target.closest("[data-nav-home]");
      if (home) {
        e.preventDefault();
        router.navigateHome();
        return;
      }

      const card = e.target.closest(".hero-card, .hero-row-card, .hero-compact-card");
      if (card && card.dataset.slug) {
        if (
          card.closest("#mix-hero-grid") ||
          card.closest(".mix-slot")
        ) {
          return;
        }
        e.preventDefault();
        router.navigateTo(utils.heroUrl(card.dataset.slug));
        return;
      }

      const link = e.target.closest("a[data-slug], a.hero-link");
      if (link && link.dataset.slug) {
        e.preventDefault();
        router.navigateTo(utils.heroUrl(link.dataset.slug));
        return;
      }

      const sigLink = e.target.closest("a.signature-skill-link");
      if (sigLink && sigLink.dataset.skillCategory) {
        e.preventDefault();
        window.AFKJ.views.detail.highlightSkillCard(sigLink.dataset.skillCategory);
      }
    });

    document.addEventListener("keydown", function (e) {
      const mixGridCard = e.target.closest("#mix-hero-grid .hero-card");
      if (
        mixGridCard &&
        state.viewMode === "mix" &&
        (e.key === "Enter" || e.key === " ")
      ) {
        e.preventDefault();
        const slug = mixGridCard.dataset.slug;
        if (!mix.tryReplaceHighlightedAlternative(slug)) {
          mix.addHeroToMixZone(slug);
        }
        return;
      }
      const card = e.target.closest(".hero-card, .hero-row-card, .hero-compact-card");
      if (card && (e.key === "Enter" || e.key === " ")) {
        if (
          card.closest("#mix-hero-grid") ||
          card.closest(".mix-slot")
        ) {
          return;
        }
        e.preventDefault();
        router.navigateTo(utils.heroUrl(card.dataset.slug));
      }
    });

    window.addEventListener("popstate", router.route);
    window.addEventListener("hashchange", router.route);

    // Redirect legacy hero paths if needed
    utils.redirectLegacyHeroPath();

    // Load actual data
    loadHeroData();
    loadCsvData();
  });
})();

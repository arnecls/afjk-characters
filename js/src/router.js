window.AFKJ = window.AFKJ || {};

(function () {
  const utils = window.AFKJ.utils;
  const config = window.AFKJ.config;

  function renderCurrentView() {
    const state = window.AFKJ.state;
    if (state.viewMode === "list") {
      window.AFKJ.views.list.renderList();
    } else if (state.viewMode === "mix") {
      window.AFKJ.views.mix.loadMixData().then(function () {
        window.AFKJ.views.mix.renderMix();
      });
    } else {
      window.AFKJ.views.grid.renderGrid();
    }
  }

  function showIndexView() {
    const state = window.AFKJ.state;
    const dom = state.dom;
    state.closeSkillCardPopover();
    state.detailHero = null;
    dom.heroDetail.removeAttribute("data-faction");
    dom.detailView.classList.add("hidden");
    dom.gridView.classList.toggle("hidden", state.viewMode !== "grid");
    dom.listView.classList.toggle("hidden", state.viewMode !== "list");
    if (dom.mixView) {
      dom.mixView.classList.toggle("hidden", state.viewMode !== "mix");
    }
    window.AFKJ.ui.updateHeaderNav(false);
    renderCurrentView();
  }

  function showGrid() {
    document.title = "AFK Journey Heroes";
    showIndexView();
  }

  function navigateHome(replace) {
    const state = window.AFKJ.state;
    state.csvColumnFilters = {};
    state.csvColumnFilterCombine = {};
    state.pendingListFilterMap = null;
    const home = utils.homeUrl();
    if (replace) {
      history.replaceState(null, "", home);
    } else {
      history.pushState(null, "", home);
    }
    showGrid();
  }

  function navigateTo(url, replace) {
    if (replace) {
      history.replaceState(null, "", url);
    } else {
      history.pushState(null, "", url);
    }
    route();
  }

  function route() {
    const state = window.AFKJ.state;
    const listFilters = window.AFKJ.listFilters;

    if (listFilters.isListFilterHash()) {
      const filterMap = listFilters.parseListFilterHash();
      if (filterMap) {
        state.pendingListFilterMap = filterMap;
      }
      if (state.csvHeaders.length && state.pendingListFilterMap) {
        listFilters.tryApplyPendingListFilters();
        showGrid();
        return;
      }
      if (filterMap) {
        state.viewMode = "list";
        showGrid();
        return;
      }
    }

    const slug = utils.slugFromLocation();
    if (slug) {
      const hero = state.heroBySlug[slug];
      if (hero) {
        window.AFKJ.views.detail.showDetail(hero);
        return;
      }
    }
    showGrid();
  }

  function heroMatchesSearch(h, q) {
    if (!q) {
      return true;
    }
    const tokens = q.split(/\s+/).filter(Boolean);
    return tokens.every(function (token) {
      const meta = window.AFKJ.tiers.roleCategoryMeta(h.roleCategory) || config.ROLE_CATEGORY_META[h.roleCategory];
      const roleLabel = meta ? meta.label : "";
      return (
        h.name.toLowerCase().indexOf(token) !== -1 ||
        (h.faction || "").toLowerCase().indexOf(token) !== -1 ||
        (h.class || "").toLowerCase().indexOf(token) !== -1 ||
        roleLabel.toLowerCase().indexOf(token) !== -1
      );
    });
  }

  function filteredHeroes() {
    const state = window.AFKJ.state;
    const q = (state.dom.searchInput.value || "").trim().toLowerCase();
    return state.heroes.filter(function (h) {
      if (state.activeFaction && h.faction !== state.activeFaction) {
        return false;
      }
      if (state.activeClass && h.class !== state.activeClass) {
        return false;
      }
      if (state.activeRole && h.roleCategory !== state.activeRole) {
        return false;
      }
      if (!heroMatchesSearch(h, q)) {
        return false;
      }
      return true;
    });
  }

  function filteredHeroNames() {
    const names = {};
    filteredHeroes().forEach(function (h) {
      names[h.name] = true;
    });
    return names;
  }

  // Export module API to window.AFKJ.router
  window.AFKJ.router = {
    renderCurrentView: renderCurrentView,
    showIndexView: showIndexView,
    showGrid: showGrid,
    navigateHome: navigateHome,
    navigateTo: navigateTo,
    route: route,
    heroMatchesSearch: heroMatchesSearch,
    filteredHeroes: filteredHeroes,
    filteredHeroNames: filteredHeroNames,
  };
})();

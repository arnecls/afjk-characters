window.AFKJ = window.AFKJ || {};

window.AFKJ.state = {
  // Configured base path
  BASE: "",

  // Loaded data stores
  heroes: [],
  heroesMeta: {},
  heroBySlug: {},
  heroByName: {},
  activeFaction: "",
  activeClass: "",
  activeRole: "",
  viewMode: "grid",

  // CSV List/Table data
  csvHeaders: [],
  csvRows: [],
  listColumnsById: {},
  sortColumn: 0,
  sortDir: 1,
  csvColumnFilters: {},
  csvColumnFilterCombine: {},
  csvColumnFilterOptions: [],
  openColumnFilter: -1,
  csvColumnWidths: [],
  columnWidthsLocked: false,

  // Detail view state
  detailHero: null,

  // Popover state
  closeSkillCardPopover: function () {},

  // Mix mode state
  mixSlots: [null, null, null, null, null],
  mixMarked: [false, false, false, false, false],
  mixFocus: {
    cc: false,
    ccImmunity: false,
    sustain: false,
    speed: false,
    noUltimate: false,
  },
  mixMode: "", // empty, 'pvp', 'afk', or 'boss'
  mixSynergyIndex: {},
  mixConfig: {},
  mixRoleProminence: {},
  mixContextSlotIndex: -1,
  mixContextGridSlug: null,
  mixSlotLastTap: null,

  // DOM Elements cache (resolved in main.js bootstrap)
  dom: {
    gridView: null,
    listView: null,
    mixView: null,
    detailView: null,
    heroGrid: null,
    mixHeroGrid: null,
    mixDropZone: null,
    mixEmptyState: null,
    mixRemoveAllBtn: null,
    heroDetail: null,
    emptyState: null,
    listEmptyState: null,
    heroesTableHead: null,
    heroesTableBody: null,
    heroesTable: null,
    searchInput: null,
    filtersPanel: null,
    filtersEl: null,
    filtersToggle: null,
    filtersToggleLabel: null,
    headerBack: null,
    viewToggle: null,
    themeToggle: null,
    siteHeader: null,
  }
};

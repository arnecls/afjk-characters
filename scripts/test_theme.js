#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");
const vm = require("vm");

const ROOT = path.resolve(__dirname, "..");
const SRC = path.join(ROOT, "site", "js", "src");

function loadModule(relativePath) {
  const code = fs.readFileSync(path.join(SRC, relativePath), "utf8");
  vm.runInContext(code, context, { filename: relativePath });
}

const storage = {};
const context = {
  window: {},
  document: {
    documentElement: {
      dataset: {},
    },
    querySelector() {
      return null;
    },
    createElement() {
      return { setAttribute() {}, appendChild() {} };
    },
  },
  sessionStorage: {
    getItem(key) {
      return Object.prototype.hasOwnProperty.call(storage, key)
        ? storage[key]
        : null;
    },
    setItem(key, value) {
      storage[key] = String(value);
    },
    removeItem(key) {
      delete storage[key];
    },
  },
  matchMedia(query) {
    return mediaState[query] || { matches: false, addEventListener() {} };
  },
  location: { pathname: "/", protocol: "file:" },
  console,
};
context.window = context;
vm.createContext(context);

const mediaState = {
  "(prefers-color-scheme: dark)": {
    matches: false,
    listeners: [],
    addEventListener(_type, fn) {
      this.listeners.push(fn);
    },
  },
};

loadModule("namespace.js");
loadModule("config.js");
loadModule("theme.js");

const theme = context.window.AFKJ.theme;
const THEME_KEY = context.window.AFKJ.config.THEME_OVERRIDE_KEY;

let failed = 0;

function assertEqual(actual, expected, message) {
  if (actual !== expected) {
    failed += 1;
    console.error(
      message + ": expected " + JSON.stringify(expected) +
      ", got " + JSON.stringify(actual)
    );
  }
}

function reset() {
  Object.keys(storage).forEach(function (key) {
    delete storage[key];
  });
  context.document.documentElement.dataset = {};
  mediaState["(prefers-color-scheme: dark)"].matches = false;
}

reset();
assertEqual(theme.readStoredThemeOverride(), null, "no stored override");
assertEqual(theme.getEffectiveTheme(), "light", "system light default");

mediaState["(prefers-color-scheme: dark)"].matches = true;
assertEqual(theme.getEffectiveTheme(), "dark", "system dark default");

theme.applyThemeOverride("light");
assertEqual(theme.readStoredThemeOverride(), "light", "stores light override");
assertEqual(
  context.document.documentElement.dataset.theme,
  "light",
  "applies light override"
);
assertEqual(theme.getEffectiveTheme(), "light", "override beats system dark");

theme.applyThemeOverride("dark");
assertEqual(theme.getEffectiveTheme(), "dark", "stores dark override");

const toggle = {
  checked: false,
  title: "",
  attrs: {},
  setAttribute(name, value) {
    this.attrs[name] = value;
  },
  getAttribute(name) {
    return this.attrs[name];
  },
};

theme.syncToggleControl(toggle);
assertEqual(toggle.checked, true, "sync toggle checked in dark mode");
assertEqual(toggle.attrs["aria-checked"], "true", "aria-checked true in dark");
assertEqual(
  toggle.title,
  "Switch to light mode",
  "toggle title when dark"
);

theme.applyThemeOverride("light");
theme.syncToggleControl(toggle);
assertEqual(toggle.checked, false, "sync toggle unchecked in light mode");
assertEqual(
  toggle.attrs["aria-checked"],
  "false",
  "aria-checked false in light"
);

reset();
mediaState["(prefers-color-scheme: dark)"].matches = true;
theme.syncToggleControl(toggle);
assertEqual(toggle.checked, true, "system dark syncs toggle");

reset();
mediaState["(prefers-color-scheme: dark)"].matches = false;
context.sessionStorage.setItem(THEME_KEY, "dark");
assertEqual(theme.getEffectiveTheme(), "dark", "session override persists");

if (failed) {
  process.exit(1);
}

console.log("test_theme.js: all checks passed");

#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");
const vm = require("vm");

const ROOT = path.resolve(__dirname, "..");
const SRC = path.join(ROOT, "site", "js", "src");

const context = {
  window: {},
  document: {
    querySelector() {
      return null;
    },
    createElement() {
      return { setAttribute() { }, appendChild() { } };
    },
  },
  location: { pathname: "/", protocol: "file:" },
  console,
};
context.window = context;
vm.createContext(context);

function loadModule(relativePath) {
  const code = fs.readFileSync(path.join(SRC, relativePath), "utf8");
  vm.runInContext(code, context, { filename: relativePath });
}

[
  "namespace.js",
  "utils.js",
  "config.js",
  "chips.js",
  "skills.js",
  "tiers.js",
  "views-grid.js",
  "views-detail.js",
].forEach(loadModule);

const renderExplanation =
  context.window.AFKJ.views.detail.renderSynergyPartnerExplanation;
if (typeof renderExplanation !== "function") {
  console.error("renderSynergyPartnerExplanation not found");
  process.exit(1);
}

function assertIncludes(label, html, needle) {
  if (!html.includes(needle)) {
    throw new Error(`${label}: expected ${JSON.stringify(needle)} in ${html}`);
  }
}

function assertNotIncludes(label, html, needle) {
  if (html.includes(needle)) {
    throw new Error(
      `${label}: did not expect ${JSON.stringify(needle)} in ${html}`
    );
  }
}

let failed = 0;

function runCase(label, fn) {
  try {
    fn();
  } catch (err) {
    failed += 1;
    console.error(`${label}: ${err.message}`);
  }
}

runCase("enemy DEF debuff keeps prefix and debuff styling", function () {
  const html = renderExplanation([
    "Enemy defense via Magic DEF debuff (all units, high)",
  ]);
  assertIncludes("def debuff", html, "Enemy defense via ");
  assertIncludes("def debuff", html, "chip-merged-left chip-debuff");
  assertIncludes("def debuff", html, "Magic DEF");
  assertNotIncludes("def debuff", html, "chip-merged-left chip-stat");
  assertNotIncludes("def debuff", html, "Enables");
});

runCase("damage taken debuff renders as debuff", function () {
  const html = renderExplanation([
    "Enemy defense via Damage taken debuff (single target, low)",
  ]);
  assertIncludes("dmg taken", html, "Enemy defense via ");
  assertIncludes("dmg taken", html, "chip-merged-left chip-debuff");
});

runCase("ally DEF Penetration buff keeps buff styling", function () {
  const html = renderExplanation([
    "Enemy defense via DEF Penetration (multiple targets, high)",
  ]);
  assertIncludes("def pen", html, "Enemy defense via ");
  assertIncludes("def pen", html, "chip-merged-left chip-stat");
  assertNotIncludes("def pen", html, "chip-merged-left chip-debuff");
});

runCase("enabler lines still read as Enables", function () {
  const html = renderExplanation([
    "Enables CC on enemies via Bind (single target, high)",
  ]);
  assertIncludes("enables", html, "Enables ");
  assertIncludes("enables", html, "CC on enemies");
});

runCase("stat-buff reasons still collapse to the effect pill", function () {
  const html = renderExplanation(["ATK via ATK (single target, high)"]);
  assertIncludes("stat buff", html, "chip-merged-left chip-stat");
  assertIncludes("stat buff", html, "ATK");
  assertNotIncludes("stat buff", html, " via ");
});

if (failed) {
  process.exit(1);
}

console.log("synergy reason chip tests passed");

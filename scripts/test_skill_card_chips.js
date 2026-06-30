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

const context = {
  window: {},
  document: {
    querySelector() {
      return null;
    },
    createElement() {
      return { setAttribute() {}, appendChild() {} };
    },
  },
  location: { pathname: "/", protocol: "file:" },
  console,
};
context.window = context;
vm.createContext(context);

loadModule("namespace.js");
loadModule("utils.js");
loadModule("config.js");
loadModule("chips.js");

const chipify = context.window.AFKJ.chips.chipifySkillCardTag;
if (typeof chipify !== "function") {
  console.error("chipifySkillCardTag not found");
  process.exit(1);
}

function assertTargetingRendered(label, polarity, needle) {
  const html = chipify(label, polarity);
  if (!html) {
    throw new Error(`empty chip html for ${label}`);
  }
  if (!html.includes(needle)) {
    throw new Error(
      `expected ${JSON.stringify(needle)} in chip html for ${label}: ${html}`
    );
  }
}

const cases = [
  ["Phys DEF — Area", "debuff", "Area"],
  ["ATK — Self (EX+10)", "buff", "Self"],
  ["Lifedrain — Multiple targets", "buff", "Multiple targets"],
  ["Blind — Area (EX+15)", "", "Area"],
  ["Direct healing — Self (Supreme+)", "buff", "Self"],
];

let failed = 0;
for (const [label, polarity, needle] of cases) {
  try {
    assertTargetingRendered(label, polarity, needle);
  } catch (err) {
    failed += 1;
    console.error(err.message);
  }
}

if (failed) {
  process.exit(1);
}
console.log(`OK: ${cases.length} skill-card chip targeting checks`);

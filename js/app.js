(function(){'use strict';window.AFKJ=window.AFKJ||{};window.AFKJ.state={};window.AFKJ.config={};window.AFKJ.utils={};window.AFKJ.chips={};window.AFKJ.tiers={};window.AFKJ.markdown={};window.AFKJ.skills={};window.AFKJ.ui={};window.AFKJ.views={grid:{},list:{},mix:{},detail:{}};window.AFKJ.router={};window.AFKJ.listFilters={};window.AFKJ.main={};window.AFKJ=window.AFKJ||{};window.AFKJ.config={WELCOME_WARNING_KEY:"afjk-welcome-dismissed",VIEW_MODE_KEY:"afjk-view-mode",THEME_OVERRIDE_KEY:"afjk-theme-override",MIX_SLOT_DOUBLE_TAP_MS:400,TAG_DEFINITIONS:{Physical:{emoji:"⚔️",cls:"chip-damage"},Magic:{emoji:"🪄",cls:"chip-damage"},"HP loss":{emoji:"💔",cls:"chip-damage"},Melee:{emoji:"🗡️",cls:"chip-damage"},Ranged:{emoji:"🏹",cls:"chip-damage"},"True damage":{emoji:"♾️",cls:"chip-damage"},Normal:{emoji:"👊",cls:"chip-damage"},"Magic damage":{emoji:"🪄",cls:"chip-damage"},"Physical damage":{emoji:"⚔️",cls:"chip-damage"},"Magic damage from allies":{emoji:"🪄",cls:"chip-role"},"Debuff on target":{emoji:"🥀",cls:"chip-debuff"},"Multiple debuffs on target":{emoji:"🥀",cls:"chip-debuff"},"CC on enemies":{emoji:"🫯",cls:"chip-cc"},"Enemy grouping":{emoji:"🧲",cls:"chip-role"},"Temporary ally stat buffs":{emoji:"💪",cls:"chip-role"},"Party composition":{emoji:"👥",cls:"chip-role"},"Continuous damage on enemies":{emoji:"🔥",cls:"chip-debuff"},"Enemy defeat":{emoji:"💀",cls:"chip-role"},"Ally Ultimate casts":{emoji:"⚡",cls:"chip-role"},"Ally blessing active":{emoji:"🙏",cls:"chip-role"},ATK:{emoji:"💪",cls:"chip-stat"},"ATK SPD":{emoji:"⚡",cls:"chip-stat"},"ATK SPD / Haste":{emoji:"⚡",cls:"chip-stat"},Haste:{emoji:"💨",cls:"chip-stat"},Healing:{emoji:"💚",cls:"chip-heal"},"Healing stat":{emoji:"💚",cls:"chip-stat"},"Direct healing":{emoji:"💚",cls:"chip-heal"},HoT:{emoji:"💚",cls:"chip-heal"},"Healing over time":{emoji:"💚",cls:"chip-heal"},Shield:{emoji:"🛡️",cls:"chip-stat"},HP:{emoji:"❤️",cls:"chip-stat"},"Max HP":{emoji:"❤️",cls:"chip-stat"},Energy:{emoji:"🔋",cls:"chip-stat"},"DEF Penetration":{emoji:"🎯",cls:"chip-stat"},Penetration:{emoji:"🎯",cls:"chip-stat"},Crit:{emoji:"💥",cls:"chip-stat"},"Crit DMG Boost":{emoji:"💥",cls:"chip-stat"},Execution:{emoji:"🗡️",cls:"chip-stat"},"Life Drain":{emoji:"🩸",cls:"chip-stat"},Lifedrain:{emoji:"🩸",cls:"chip-stat"},"Physical DEF":{emoji:"🛡️",cls:"chip-stat"},"Phys DEF":{emoji:"🛡️",cls:"chip-stat"},"Magic DEF":{emoji:"🔮",cls:"chip-stat"},"Ranged DEF":{emoji:"🛡️",cls:"chip-stat"},DEF:{emoji:"🛡️",cls:"chip-stat"},"Basic stats":{emoji:"📈",cls:"chip-stat"},Vitality:{emoji:"🌿",cls:"chip-stat"},"Damage taken":{emoji:"🛡️",cls:"chip-stat"},"Damage dealt":{emoji:"⚔️",cls:"chip-stat"},"Ranged damage":{emoji:"🏹",cls:"chip-stat"},"Dodge chance":{emoji:"🛡️",cls:"chip-stat"},"Movement speed":{emoji:"💨",cls:"chip-stat"},"Attack range":{emoji:"📏",cls:"chip-stat"},"Ally empower":{emoji:"💪",cls:"chip-stat"},Exemption:{emoji:"✨",cls:"chip-stat"},"Debuff duration":{emoji:"⏱️",cls:"chip-stat"},"Crit Resist":{emoji:"💥",cls:"chip-stat"},Vulnerable:{emoji:"🎯",cls:"chip-stat"},"Crit DMG boost":{emoji:"💥",cls:"chip-stat"},"Fatal blow immunity":{emoji:"♻️",cls:"chip-stat"},Blind:{emoji:"👁️",cls:"chip-cc"},Disarm:{emoji:"👊",cls:"chip-cc"},Stun:{emoji:"💫",cls:"chip-cc"},"Knock back":{emoji:"↩️",cls:"chip-cc"},"Knock down":{emoji:"⬇️",cls:"chip-cc"},Bind:{emoji:"⛓️",cls:"chip-cc"},Silence:{emoji:"🤐",cls:"chip-cc"},Charm:{emoji:"💕",cls:"chip-cc"},Sleep:{emoji:"😴",cls:"chip-cc"},Taunt:{emoji:"📣",cls:"chip-cc"},Frighten:{emoji:"😱",cls:"chip-cc"},"DoT":{emoji:"🔥",cls:"chip-debuff"},"ally-buffer":{emoji:"📈",cls:"chip-role"},"ally-healer":{emoji:"💚",cls:"chip-role"},"ally-shielder":{emoji:"🛡️",cls:"chip-role"},"aoe-damage":{emoji:"💥",cls:"chip-role"},"aoe-healing":{emoji:"💚",cls:"chip-role"},"assassin":{emoji:"🎯",cls:"chip-role"},"backline-assassin":{emoji:"🔪",cls:"chip-role"},"backline-inhibit":{emoji:"🪤",cls:"chip-role"},"battle-start-burst":{emoji:"🚀",cls:"chip-role"},"battle-start-ult":{emoji:"⚡",cls:"chip-role"},"battlefield-modification":{emoji:"🗺️",cls:"chip-role"},"cc-immunity":{emoji:"🔰",cls:"chip-anti-cc"},"cheat-death":{emoji:"♻️",cls:"chip-role"},"counterattack":{emoji:"↩️",cls:"chip-role"},interrupt:{emoji:"⛔",cls:"chip-role"},"dot-specialist":{emoji:"🔥",cls:"chip-role"},"enemy-debuffer":{emoji:"🥀",cls:"chip-role"},"enemy-grouping":{emoji:"🧲",cls:"chip-role"},"energy-provider":{emoji:"🔋",cls:"chip-role"},"execute":{emoji:"☠️",cls:"chip-role"},"high-damage-ult":{emoji:"💣",cls:"chip-role"},"high-initial-energy":{emoji:"🔋",cls:"chip-role"},"hp-scaling":{emoji:"❤️",cls:"chip-role"},invincibility:{emoji:"👑",cls:"chip-role"},"life-drain":{emoji:"🩸",cls:"chip-role"},"mark-target":{emoji:"🎯",cls:"chip-role"},"mass-cc":{emoji:"🫯",cls:"chip-role"},"non-ult-utility":{emoji:"🛠️",cls:"chip-role"},revive:{emoji:"🌱",cls:"chip-role"},"self-repositioner":{emoji:"💨",cls:"chip-role"},"static-tile-buffer":{emoji:"📍",cls:"chip-role"},stealth:{emoji:"🥷",cls:"chip-role"},summoner:{emoji:"🐾",cls:"chip-role"},taunt:{emoji:"📣",cls:"chip-role"},"temporary-stat-buffer":{emoji:"⏱️",cls:"chip-role"},"ultimate-cancel":{emoji:"🚫",cls:"chip-cc"},untargetable:{emoji:"👻",cls:"chip-role"},Invincible:{emoji:"👑",cls:"chip-role"},"DMG+CC immunity":{emoji:"🔰",cls:"chip-anti-cc"},"Knock up":{emoji:"⬆️",cls:"chip-cc"},Interrupt:{emoji:"🚫",cls:"chip-cc"},Displace:{emoji:"↔️",cls:"chip-cc"},Unaffected:{emoji:"🛡️",cls:"chip-anti-cc"},Steadfast:{emoji:"🛡️",cls:"chip-anti-cc"},Immune:{emoji:"⛔",cls:"chip-anti-cc"},Untargetable:{emoji:"👻",cls:"chip-anti-cc"},Cleanse:{emoji:"💧",cls:"chip-anti-cc"},"Max HP damage":{emoji:"💔",cls:"chip-damage"},"Max HP-based damage":{emoji:"💔",cls:"chip-damage"},},BEHAVIOR_TAG_TOOLTIPS:{"ally-buffer":"Grants meaningful offensive or defensive stat buffs to allies.","ally-healer":"Restores ally HP directly or via healing over time as a core role.","ally-shielder":"Grants shields to allies as a significant part of the kit.","aoe-damage":"Deals substantial multi-target or area damage on a regular basis.","aoe-healing":"Heals multiple allies or wide ally groups, not only single-target.","assassin":"Selectively attacks a chosen enemy by non-positional criteria (weakest, marked, isolated, etc.) on any row.","backline-assassin":"Targets rear/far/highest-damage enemies with substantial damage that can kill within ~10s (dash, teleport, or long range).","backline-inhibit":"Targets rear/far/highest-damage enemies with CC, slow, DEF cuts, damage-taken amp, or DoT that softens that unit.","battle-start-burst":"Deals damage to one or more units in the first ~2–3s of battle.","battle-start-ult":"Casts ultimate or reaches full energy unusually early in the fight.","battlefield-modification":"Adds physical obstacles or transforms the map layout.","cc-immunity":"Grants self or allies immunity to crowd control as a defining mechanic.","cheat-death":"Survives a would-be defeat or critical HP threshold via self-recovery.","counterattack":"Punishes enemies for attacking with reactive damage or effects.","interrupt":"Applies hard shutdown effects such as Silence or Interrupt.","dot-specialist":"Relies on damage over time or recurring tick damage as a primary pattern.","enemy-debuffer":"Applies meaningful stat or combat debuffs to enemies as a core output.","enemy-grouping":"Pulls, pushes, or clusters enemies to set up follow-up damage or CC.","energy-provider":"Grants Energy to allies or routinely accelerates ally ultimates.",execute:"Finishes low-HP enemies or scales damage strongly on wounded targets.","high-damage-ult":"Ultimate is the main damage spike and a large share of total output.","high-initial-energy":"Ultimate starts with high Initial Energy when fully built (~fast fill).","hp-scaling":"Damage, survivability, or effects scale strongly with HP values.",invincibility:"Grants damage and/or control immunity windows to self or allies.","life-drain":"Sustains through lifesteal or HP recovery tied to dealing damage.","mark-target":"Marks or designates units so allies or self can focus amplified damage.","mass-cc":"Applies crowd control to multiple enemies or wide areas reliably.","non-ult-utility":"Strong combat value from non-ultimate skills without relying on the ultimate.",revive:"Brings defeated allies back to the fight; not self-survival.","self-repositioner":"Regularly moves self across the grid via jumps, dashes, or teleports.","static-tile-buffer":"Buffs an ally only while they remain on a specific placement tile.",stealth:"Enters hidden or untargetable states to avoid focus or enable picks.",summoner:"Fields persistent summons or companions that contribute in combat.",taunt:"Forces enemies to attack the hero or redirects enemy focus onto them.","temporary-stat-buffer":"Grants at least one temporary ally stat buff that can end before battle does.","ultimate-cancel":"Cancels or interrupts enemy ultimates when they begin casting.",untargetable:"Routinely becomes untargetable by enemy skills during normal gameplay.",},TARGETING_DEFINITIONS:{"single target":{emoji:"🎯",cls:"chip-target"},"multiple targets":{emoji:"👥",cls:"chip-target"},"all units":{emoji:"🌐",cls:"chip-target"},area:{emoji:"⭕",cls:"chip-target"},path:{emoji:"〰️",cls:"chip-target"},arc:{emoji:"📐",cls:"chip-target"},self:{emoji:"🪞",cls:"chip-target"},allies:{emoji:"🤝",cls:"chip-target"},enemies:{emoji:"☠️",cls:"chip-target"},global:{emoji:"🌍",cls:"chip-target"},"on skill":{emoji:"⏱️",cls:"chip-target"},"all summons":{emoji:"🐾",cls:"chip-target"},"owned summons":{emoji:"🐾",cls:"chip-target"},"summons only":{emoji:"🐾",cls:"chip-target"},},ROLE_CATEGORY_META:{damage_dealer:{label:"Damage dealer",emoji:"⚔️",className:"badge-role-damage-dealer",},specialist:{label:"Specialist",emoji:"🎭",className:"badge-role-specialist",},support:{label:"Support",emoji:"🤝",className:"badge-role-support",},tank:{label:"Tank",emoji:"🛡️",className:"badge-role-tank",},},ROLE_CATEGORY_ICONS:{damage_dealer:{viewBox:"0 0 448 512",path:"M192 0c17.7 0 32 14.3 32 32l0 112-64 0 0-112c0-17.7 14.3-32 32-32zM64 64c0-17.7 14.3-32 32-32s32 14.3 32 32l0 80-64 0 0-80zm192 0c0-17.7 14.3-32 32-32s32 14.3 32 32l0 96c0 17.7-14.3 32-32 32s-32-14.3-32-32l0-96zm96 64c0-17.7 14.3-32 32-32s32 14.3 32 32l0 64c0 17.7-14.3 32-32 32s-32-14.3-32-32l0-64zm-96 88l0-.6c9.4 5.4 20.3 8.6 32 8.6c13.2 0 25.4-4 35.6-10.8c8.7 24.9 32.5 42.8 60.4 42.8c11.7 0 22.6-3.1 32-8.6l0 8.6c0 52.3-25.1 98.8-64 128l0 96c0 17.7-14.3 32-32 32l-160 0c-17.7 0-32-14.3-32-32l0-78.4c-17.3-7.9-33.2-18.8-46.9-32.5L69.5 357.5C45.5 333.5 32 300.9 32 267l0-27c0-35.3 28.7-64 64-64l88 0c22.1 0 40 17.9 40 40s-17.9 40-40 40l-56 0c-8.8 0-16 7.2-16 16s7.2 16 16 16l56 0c39.8 0 72-32.2 72-72z",},specialist:{viewBox:"0 0 512 512",path:"M288 32c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 11.5c0 49.9-60.3 74.9-95.6 39.6L120.2 75C107.7 62.5 87.5 62.5 75 75s-12.5 32.8 0 45.3l8.2 8.2C118.4 163.7 93.4 224 43.5 224L32 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l11.5 0c49.9 0 74.9 60.3 39.6 95.6L75 391.8c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l8.2-8.2c35.3-35.3 95.6-10.3 95.6 39.6l0 11.5c0 17.7 14.3 32 32 32s32-14.3 32-32l0-11.5c0-49.9 60.3-74.9 95.6-39.6l8.2 8.2c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3l-8.2-8.2c-35.3-35.3-10.3-95.6 39.6-95.6l11.5 0c17.7 0 32-14.3 32-32s-14.3-32-32-32l-11.5 0c-49.9 0-74.9-60.3-39.6-95.6l8.2-8.2c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0l-8.2 8.2C348.3 118.4 288 93.4 288 43.5L288 32zM176 224a48 48 0 1 1 96 0 48 48 0 1 1 -96 0zm128 56a24 24 0 1 1 0 48 24 24 0 1 1 0-48z",},support:{viewBox:"0 0 512 512",path:"M184 48l144 0c4.4 0 8 3.6 8 8l0 40L176 96l0-40c0-4.4 3.6-8 8-8zm-56 8l0 40L64 96C28.7 96 0 124.7 0 160L0 416c0 35.3 28.7 64 64 64l384 0c35.3 0 64-28.7 64-64l0-256c0-35.3-28.7-64-64-64l-64 0 0-40c0-30.9-25.1-56-56-56L184 0c-30.9 0-56 25.1-56 56zm96 152c0-8.8 7.2-16 16-16l32 0c8.8 0 16 7.2 16 16l0 48 48 0c8.8 0 16 7.2 16 16l0 32c0 8.8-7.2 16-16 16l-48 0 0 48c0 8.8-7.2 16-16 16l-32 0c-8.8 0-16-7.2-16-16l0-48-48 0c-8.8 0-16-7.2-16-16l0-32c0-8.8 7.2-16 16-16l48 0 0-48z",},tank:{viewBox:"0 0 512 512",path:"M256 0c4.6 0 9.2 1 13.4 2.9L457.7 82.8c22 9.3 38.4 31 38.3 57.2c-.5 99.2-41.3 280.7-213.6 363.2c-16.7 8-36.1 8-52.8 0C57.3 420.7 16.5 239.2 16 140c-.1-26.2 16.3-47.9 38.3-57.2L242.7 2.9C246.8 1 251.4 0 256 0z",},},ROLE_FILTER_ORDER:["damage_dealer","specialist","support","tank"],REPLACEMENT_CATEGORY_ICONS:{"Best overall replacement":"🏆","Buffs on allies":"🔼","Energy provider":"🔋",Healing:"💚","Similar Skills":"♊️",Damage:"⚔️","Debuffs on enemies":"🥀","Crowd Control":"⛓️",},MIX_FOCUS_CONFIG_KEYS:{cc:"cc",ccImmunity:"cc_immunity",sustain:"sustain",speed:"speed",noUltimate:"no_ultimate",},MIX_FOCUS_TAG_DEFAULTS:{cc_immunity:{"cc-immunity":7.0,"DMG+CC immunity":6.0,Immune:5.0,Unaffected:5.0,},},};window.AFKJ=window.AFKJ||{};window.AFKJ.theme={readStoredThemeOverride:function(){const key=window.AFKJ.config.THEME_OVERRIDE_KEY;try{const stored=sessionStorage.getItem(key);if(stored==="light"||stored==="dark"){return stored;}}catch(e){}
return null;},storeThemeOverride:function(theme){const key=window.AFKJ.config.THEME_OVERRIDE_KEY;try{sessionStorage.setItem(key,theme);}catch(e){}},systemPrefersDark:function(){return window.matchMedia("(prefers-color-scheme: dark)").matches;},getEffectiveTheme:function(){const override=this.readStoredThemeOverride();if(override){return override;}
return this.systemPrefersDark()?"dark":"light";},applyThemeOverride:function(theme){const root=document.documentElement;if(theme==="light"||theme==="dark"){root.dataset.theme=theme;this.storeThemeOverride(theme);return;}
delete root.dataset.theme;},syncToggleControl:function(input){if(!input){return;}
const dark=this.getEffectiveTheme()==="dark";input.checked=dark;input.setAttribute("aria-checked",dark?"true":"false");input.title=dark?"Switch to light mode":"Switch to dark mode";input.setAttribute("aria-label",dark?"Dark mode on":"Dark mode off");},};window.AFKJ=window.AFKJ||{};window.AFKJ.utils={inferBase:function(){const path=location.pathname;const heroIdx=path.indexOf("/hero/");if(heroIdx!==-1){return path.slice(0,heroIdx+1);}
if(!path.endsWith("/")){const last=path.lastIndexOf("/");if(last>=0){return path.slice(0,last+1);}}
return path.endsWith("/")?path:path+"/";},resolveBase:function(){if(location.protocol==="file:"){return this.inferBase();}
const meta=document.querySelector('meta[name="github-pages-base"]');const configured=meta&&meta.content;if(configured&&location.pathname.startsWith(configured)){return configured;}
return this.inferBase();},isLocalFile:function(){return location.protocol==="file:";},assetUrl:function(relative){if(this.isLocalFile()){return relative;}
return window.AFKJ.state.BASE+relative;},heroHash:function(slug){return"#hero/"+encodeURIComponent(slug);},heroUrl:function(slug){if(this.isLocalFile()){return this.heroHash(slug);}
return window.AFKJ.state.BASE+this.heroHash(slug);},homeUrl:function(){if(this.isLocalFile()){return location.pathname;}
return window.AFKJ.state.BASE;},slugFromLocation:function(){const hashMatch=location.hash.match(/^#hero\/([^/?#]+)/);if(hashMatch){return decodeURIComponent(hashMatch[1]);}
const path=location.pathname;const prefix=window.AFKJ.state.BASE.replace(/\/$/,"");if(path.startsWith(prefix+"/hero/")){return decodeURIComponent(path.slice((prefix+"/hero/").length).replace(/\/$/,""));}
if(path.indexOf("/hero/")!==-1){return decodeURIComponent(path.split("/hero/")[1].replace(/\/$/,""));}
return null;},redirectLegacyHeroPath:function(){if(location.hash.match(/^#hero\//)){return;}
const path=location.pathname;const idx=path.indexOf("/hero/");if(idx===-1){return;}
const slug=path.slice(idx+6).replace(/\/$/,"");if(!slug){return;}
const base=path.slice(0,idx+1);history.replaceState(null,"",base+this.heroHash(decodeURIComponent(slug)));},iconPath:function(kind,value){if(!value)return null;const fname=value.toLowerCase().replace(/\s+/g,"");return"assets/icons/"+kind+"/"+fname+".png";},characterPortraitPath:function(hero){if(!hero||!hero.name){return null;}
return this.characterPortraitPathForName(hero.name);},characterPortraitPathForName:function(name){if(!name){return null;}
return"assets/portraits/"+name+".png";},factionDataKey:function(faction){if(!faction){return"";}
return faction.toLowerCase().replace(/\s+/g,"");},CELESTIAL_HYPOGEAN_BONUS_KEY:"celestialhypogean",factionBonusGroupKey:function(faction){const key=this.factionDataKey(faction);if(key==="celestial"||key==="hypogean"){return this.CELESTIAL_HYPOGEAN_BONUS_KEY;}
return key;},factionClass:function(faction){if(!faction)return"";return"badge-faction-"+faction.toLowerCase().replace(/\s+/g,"");},escapeHtml:function(text){if(typeof text!=="string")return"";return text.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");},linkifyHero:function(name,slug){const state=window.AFKJ.state;if(slug&&state.heroBySlug[slug]){return('<a href="'+
this.escapeHtml(this.heroUrl(slug))+'" class="hero-link" data-slug="'+
this.escapeHtml(slug)+'">'+
this.escapeHtml(name)+"</a>");}
return this.escapeHtml(name);},rectContainsPoint:function(rect,x,y,pad){return(x>=rect.left-pad&&x<=rect.right+pad&&y>=rect.top-pad&&y<=rect.bottom+pad);}};window.AFKJ=window.AFKJ||{};window.AFKJ.state={BASE:"",heroes:[],heroesMeta:{},heroBySlug:{},heroByName:{},counterFilterCombos:{},pendingListFilterMap:null,activeFaction:"",activeClass:"",activeRole:"",viewMode:"grid",csvHeaders:[],csvRows:[],listColumnsById:{},sortColumn:0,sortDir:1,csvColumnFilters:{},csvColumnFilterCombine:{},csvColumnFilterOptions:[],openColumnFilter:-1,csvColumnWidths:[],columnWidthsLocked:false,detailHero:null,closeSkillCardPopover:function(){},mixSlots:[null,null,null,null,null],mixMarked:[false,false,false,false,false],mixFocus:{cc:false,ccImmunity:false,sustain:false,speed:false,noUltimate:false,},mixMode:"",mixSynergyIndex:{},mixConfig:{},mixRoleProminence:{},mixContextSlotIndex:-1,mixContextGridSlug:null,mixSlotLastTap:null,dom:{gridView:null,listView:null,mixView:null,detailView:null,heroGrid:null,mixHeroGrid:null,mixDropZone:null,mixEmptyState:null,mixRemoveAllBtn:null,heroDetail:null,emptyState:null,listEmptyState:null,heroesTableHead:null,heroesTableBody:null,heroesTable:null,searchInput:null,filtersPanel:null,filtersEl:null,filtersToggle:null,filtersToggleLabel:null,headerBack:null,viewToggle:null,themeToggle:null,siteHeader:null,}};window.AFKJ=window.AFKJ||{};(function(){const utils=window.AFKJ.utils;const config=window.AFKJ.config;const escapeHtml=utils.escapeHtml.bind(utils);const QUALITY_CLASS={high:"chip-q-high",average:"chip-q-medium",low:"chip-q-low",};const SKILL_OVERVIEW_SPEED_LABELS={speed:true,"first cast speed":true,};const SPEED_CLASS={slow:"chip-s-slow",average:"chip-s-normal",fast:"chip-s-fast",};const SPEED_EMOJI={slow:"🐢",average:"🚶",fast:"🚀",};const QUALITY_EMOJI={high:"⬆️",average:"➡️",low:"⬇️",};const CC_DURATION_LABEL={low:"short",average:"average",high:"long",};const QUALITY_TOOLTIPS={high:"Top third across the roster for this effect.",average:"Middle band across the roster with the same effect label.",low:"Below average across the roster for this effect type.",};const CLASS_RANK_TOOLTIPS={high:"Top third within this hero's class.",average:"Middle third within this hero's class.",low:"Bottom third within this hero's class.",};const SPEED_TOOLTIPS={slow:"Slow to cast: longer cooldown, initial delay, or ultimate energy fill time.",average:"Typical cast timing for this skill group across the roster.",fast:"Quick to cast: short delay, low cooldown, or battle-start override.",};const SIGNATURE_FUEL_TOOLTIP="Signature skill casts slowly; Haste and Energy recovery buffs are especially valuable.";const TARGETING_RANK={"all units":70,global:65,area:60,path:55,arc:50,"multiple targets":40,allies:35,enemies:35,"single target":30,self:20,};const MOVEMENT_DEFINITIONS={stationary:{emoji:"📍",cls:"chip-movement"},moving:{emoji:"🏃",cls:"chip-movement"},"mostly stationary":{emoji:"🚶",cls:"chip-movement"},"high movement":{emoji:"💨",cls:"chip-movement"},"moving / stationary":{emoji:"↔️",cls:"chip-movement"},};const MOVEMENT_KEYS=Object.keys(MOVEMENT_DEFINITIONS).sort(function(a,b){return b.length-a.length;});const TARGETING_PHRASES=[{re:/\bMultiple targets\b/gi,key:"multiple targets"},{re:/\bSingle target\b/gi,key:"single target"},{re:/\bAll units\b/gi,key:"all units"},{re:/\bEnemies\b/gi,key:"enemies"},{re:/\bGlobal\b/gi,key:"global"},{re:/\bOn Skill\b/gi,key:"on skill"},{re:/\bAll summons\b/gi,key:"all summons"},{re:/\bOwned summons\b/gi,key:"owned summons"},{re:/\bSummons only\b/gi,key:"owned summons"},{re:/\bArea\b/g,key:"area"},{re:/\bArc\b/g,key:"arc"},{re:/\bpath\b/gi,key:"path"},{re:/\bSelf\b/g,key:"self"},];const STAT_KEYS=Object.keys(config.TAG_DEFINITIONS).filter(function(key){const cls=config.TAG_DEFINITIONS[key].cls;return cls&&cls.indexOf("chip-stat")!==-1;}).sort(function(a,b){return b.length-a.length;});const HEAL_CHIP_KEYS=["Direct healing","Healing over time","HoT","Healing"].sort(function(a,b){return b.length-a.length;});function healingChipDisplay(text){if(text==="Healing over time"){return"HoT";}
return text;}
function tryMergeTrailingLabel(before,indicator){const match=before.match(/(^|[\s,])([\w][\w\s]*?)\s+$/);if(!match){return null;}
const prefix=before.slice(0,match.index)+match[1];const label=match[2].trim();const merged=window.AFKJ.chips.mergeLabelWithIndicator(label,indicator.trim());if(!merged){return null;}
return escapeHtml(prefix)+merged;}
function renderCharacterPill(name){const utils=window.AFKJ.utils;const state=window.AFKJ.state;const hero=state.heroByName[name];if(!hero){return escapeHtml(name);}
const factionKey=utils.factionDataKey(hero.faction);const factionClass=utils.factionClass(hero.faction);const portraitSrc=utils.assetUrl(utils.characterPortraitPath(hero));const href=utils.escapeHtml(utils.heroUrl(hero.slug));const slugAttr=utils.escapeHtml(hero.slug);const nameHtml=utils.escapeHtml(name);return('<a href="'+
href+'" class="character-pill hero-link '+
factionClass+'" data-faction="'+
utils.escapeHtml(factionKey)+'" data-slug="'+
slugAttr+'">'+'<span class="character-pill-hex" aria-hidden="true">'+'<span class="character-pill-hex-wrap">'+'<span class="character-pill-hex-inner">'+'<img class="character-pill-hex-icon" src="'+
utils.escapeHtml(portraitSrc)+'" alt="" loading="lazy" onerror="this.style.opacity=0.3">'+"</span></span></span>"+'<span class="character-pill-name">'+
nameHtml+"</span></a>");}
function renderInline(text){const parts=[];let last=0;const re=/`([^`]+)`|\[\[([^\]]+)\]\]/g;let match;while((match=re.exec(text))){const backtickLabel=match[1];const heroName=match[2];if(backtickLabel!==undefined){const merged=tryMergeTrailingLabel(text.slice(last,match.index),backtickLabel);if(merged){parts.push(merged);}else{parts.push(escapeHtml(text.slice(last,match.index)));parts.push(window.AFKJ.chips.formatTag(backtickLabel));}}else{parts.push(escapeHtml(text.slice(last,match.index)));if(heroName.indexOf("filter:")===0){parts.push(renderFilterComboChips(heroName.slice(7)));}else{parts.push(renderCharacterPill(heroName));}}
last=match.index+match[0].length;}
parts.push(escapeHtml(text.slice(last)));let out=parts.join("");out=out.replace(/\*\*([^*]+)\*\*/g,"<strong>$1</strong>");return out;}
function conditionalTooltip(text){const lower=text.toLowerCase();if(lower.indexOf("conditional (frequent)")!==-1){return"Often applies in a fight; magnitude is not reduced.";}
if(lower.indexOf("conditional (rare)")!==-1){return"Situational or once per battle; magnitude is lowered by two steps.";}
return"";}
function chipTipAttrs(tooltip){if(!tooltip){return"";}
return(' data-tip="'+
escapeHtml(tooltip)+'" tabindex="0" role="button" aria-describedby="chip-tooltip"');}
function chipTipHtmlAttrs(tooltipHtml){if(!tooltipHtml){return"";}
return(' data-tip-html="'+
escapeHtml(tooltipHtml)+'" tabindex="0" role="button" aria-describedby="chip-tooltip"');}
function normalizeToken(text){return text.replace(/\u200b/g,"").trim();}
function normalizeSummaryText(text){return text.replace(/\s+/g," ").trim();}
function splitSummarySegments(text){return normalizeSummaryText(text).split(/\s*(?:—|–)\s*/).map(function(s){return s.trim();}).filter(Boolean);}
function isInsideHtmlTag(html,index){const before=html.slice(0,index);const lastOpen=before.lastIndexOf("<");const lastClose=before.lastIndexOf(">");return lastOpen>lastClose;}
function isInsideChipSpan(html,index){const before=html.slice(0,index);const openTag="<span class=\"chip";let openPos=-1;let searchFrom=0;for(;;){const idx=before.indexOf(openTag,searchFrom);if(idx===-1){break;}
openPos=idx;searchFrom=idx+1;}
if(openPos===-1){return false;}
const closePos=before.indexOf("</span>",openPos);return closePos===-1||closePos>=index;}
function isInsideSpanClass(html,index,className){const before=html.slice(0,index);const openTag='<span class="'+className+'"';let openPos=-1;let searchFrom=0;for(;;){const idx=before.indexOf(openTag,searchFrom);if(idx===-1){break;}
openPos=idx;searchFrom=idx+1;}
if(openPos===-1){return false;}
const closePos=before.indexOf("</span>",openPos);return closePos===-1||closePos>=index;}
function isInsideSkillInlineStat(html,index){return isInsideSpanClass(html,index,"skill-inline-stat");}
function isInsideSkillInlineTime(html,index){return isInsideSpanClass(html,index,"skill-inline-time");}
function isInsideSkillInlineNum(html,index){return isInsideStrong(html,index)||isInsideSpanClass(html,index,"skill-inline-num");}
function isInsideStrong(html,index){const before=html.slice(0,index);const openPos=before.lastIndexOf("<strong");if(openPos===-1){return false;}
const closePos=before.indexOf("</strong>",openPos);return closePos===-1||closePos>=index;}
function boldSkillNumericTokens(html){return replaceOutsideChips(html,/(?:[×x*]\s*)?[+\-−]?\d+(?:\.\d+)?(?:%|s\b)?(?:\s*[×x*÷/]\s*(?:[×x*]\s*)?[+\-−]?\d+(?:\.\d+)?(?:%|s\b)?)*/g,function(match){return'<strong class="skill-inline-num">'+match+"</strong>";});}
function replaceOutsideChips(text,re,replacer){return text.replace(re,function(){const args=Array.prototype.slice.call(arguments);const offset=args[args.length-2];const match=args[0];if(isInsideHtmlTag(text,offset)||isInsideChipSpan(text,offset)||isInsideSkillInlineStat(text,offset)||isInsideSkillInlineTime(text,offset)||isInsideSkillInlineNum(text,offset)){return match;}
return replacer.apply(null,args);});}
function enhancePlainTargetingInHtml(html){let out=html;TARGETING_PHRASES.forEach(function(entry){out=out.replace(entry.re,function(match,offset){if(isInsideHtmlTag(out,offset)||isInsideChipSpan(out,offset)){return match;}
const def=config.TARGETING_DEFINITIONS[entry.key];if(!def){return match;}
return window.AFKJ.chips.chipSpan(def.emoji,match,def.cls);});});return out;}
function targetingTokenMeta(token){const text=normalizeToken(token);if(!text){return null;}
const lower=text.toLowerCase();const def=config.TARGETING_DEFINITIONS[lower];if(!def){return null;}
return{emoji:def.emoji,text:text,cls:def.cls,rank:TARGETING_RANK[lower]||0,};}
function renderStackedTargetingTipHtml(metas){return('<div class="chip-stacked-tip">'+
metas.map(function(meta){return('<span class="chip '+
meta.cls+'">'+
meta.emoji+" "+
escapeHtml(chipDisplayLabel(meta.text))+"</span>");}).join("")+"</div>");}
function renderStackedTargetingPill(tokens,tipHtmlOverride){const metas=tokens.map(function(token){return targetingTokenMeta(token);}).filter(Boolean).sort(function(a,b){return b.rank-a.rank;});if(!metas.length){return"";}
if(metas.length===1){const only=metas[0];return chipSpan(only.emoji,only.text,only.cls);}
const segmentsHtml=metas.map(function(meta,index){const isFirst=index===0;const content=isFirst?meta.emoji+" "+escapeHtml(chipDisplayLabel(meta.text)):meta.emoji;return('<span class="chip-stacked-seg '+
meta.cls+
(isFirst?" chip-stacked-first":" chip-stacked-icon")+'">'+
content+"</span>");}).join("");const tipHtml=tipHtmlOverride||renderStackedTargetingTipHtml(metas);return('<span class="chip chip-stacked chip-has-tip" data-tip-html="'+
escapeHtml(tipHtml)+'" tabindex="0" role="button" aria-describedby="chip-tooltip">'+
segmentsHtml+"</span>");}
function chipifyTargetingSegment(segment){const normalized=unwrapBackticks(segment.trim());if(!normalized){return"";}
const parts=normalized.split(/\s*,\s*/).map(function(part){return normalizeToken(part);}).filter(Boolean);if(parts.length>1&&parts.every(function(part){return targetingTokenMeta(part);})){return renderStackedTargetingPill(parts);}
return parts.map(function(part){return tokenToHtml(part);}).join(" ");}
function chipDisplayLabel(text){const trimmed=(text||"").trim();if(!trimmed){return trimmed;}
if(trimmed==="Healing over time"){return"HoT";}
const lower=trimmed.toLowerCase();if(lower.indexOf("conditional (frequent)")!==-1){return"conditional (frequent)";}
if(lower.indexOf("conditional (rare)")!==-1){return"conditional (rare)";}
if(trimmed==="Max HP-based damage"){return"Max HP damage";}
const statModifierDisplay={"Damage taken":"DMG taken","Magic damage":"Magic DMG","Damage dealt":"DMG dealt",};if(Object.prototype.hasOwnProperty.call(statModifierDisplay,trimmed)){return statModifierDisplay[trimmed];}
return trimmed;}
function skillCardTargetingDisplayLabel(text){const trimmed=(text||"").trim();const lower=trimmed.toLowerCase();const short={"all units":"all","multiple targets":"multiple","single target":"single",};if(Object.prototype.hasOwnProperty.call(short,lower)){return short[lower];}
return chipDisplayLabel(trimmed);}
function targetingDisplayLabel(text,skillCardDisplay){if(skillCardDisplay){return skillCardTargetingDisplayLabel(text);}
return chipDisplayLabel(text);}
function chipSpan(emoji,text,cls,tooltip){const tipAttr=chipTipAttrs(tooltip);const tipCls=tooltip?" chip-has-tip":"";return('<span class="chip '+
cls+
tipCls+'"'+
tipAttr+">"+
(emoji?emoji+" ":"")+
escapeHtml(chipDisplayLabel(text))+"</span>");}
function behaviorTagTooltip(tag){return config.BEHAVIOR_TAG_TOOLTIPS[tag]||"";}
function behaviorTagDefinition(tag){return config.TAG_DEFINITIONS[tag]||null;}
function behaviorTagChip(tag,withTooltip){const def=behaviorTagDefinition(tag);const emoji=def?def.emoji:"🏷️";const tooltip=withTooltip?behaviorTagTooltip(tag):"";return chipSpan(emoji,tag.trim(),"chip-behavior-tag",tooltip);}
function filterColumnEmoji(columnLabel){const key=exactTagDefinitionKey(columnLabel);if(key&&config.TAG_DEFINITIONS[key]){return config.TAG_DEFINITIONS[key].emoji;}
const dmgEmojis={"Magic DMG":config.TAG_DEFINITIONS.Magic.emoji,"Physical DMG":config.TAG_DEFINITIONS.Physical.emoji,"True DMG":config.TAG_DEFINITIONS["True damage"].emoji,};return dmgEmojis[columnLabel]||"";}
function behaviorTagIdForComboChip(combo,chipIndex){const spec=combo.filters&&combo.filters["Behavior tags"];if(!spec||!spec.values||!spec.values.length){return null;}
const chip=combo.chips[chipIndex];if(!chip||chip.style!=="behavior-tag"){return null;}
let behaviorIdx=0;for(let i=0;i<chipIndex;i++){if(combo.chips[i].style==="behavior-tag"){behaviorIdx+=1;}}
const values=spec.values;return values[Math.min(behaviorIdx,values.length-1)];}
function renderFilterComboChip(chip,combo,chipIndex){const cls=chip.style==="behavior-tag"?"chip-behavior-tag":"chip-filter-column";let emoji="";let tooltip="";if(chip.style==="behavior-tag"){const tagId=behaviorTagIdForComboChip(combo,chipIndex);const def=tagId?behaviorTagDefinition(tagId):null;emoji=def?def.emoji:"🏷️";tooltip=tagId?behaviorTagTooltip(tagId):"";}else{emoji=filterColumnEmoji(chip.label);}
return chipSpan(emoji,chip.label,cls,tooltip);}
function renderFilterComboChips(comboId){const combos=window.AFKJ.state.counterFilterCombos||{};const combo=combos[comboId];if(!combo||!combo.chips||!combo.chips.length){return escapeHtml("[[filter:"+comboId+"]]");}
const listFilters=window.AFKJ.listFilters;const href=listFilters?listFilters.comboDeepLinkById(comboId):"#";const hrefAttr=escapeHtml(href);return combo.chips.map(function(chip,chipIndex){const inner=renderFilterComboChip(chip,combo,chipIndex);return('<a href="'+
hrefAttr+'" class="chip-filter-link">'+
inner+"</a>");}).join(" ");}
function isSpeedMetricLabel(label){return SKILL_OVERVIEW_SPEED_LABELS[label.toLowerCase()]||false;}
function qualityIndicatorMeta(value,isCc){const lower=value.toLowerCase();if(!QUALITY_CLASS[lower]){return null;}
return{cls:"chip-quality "+QUALITY_CLASS[lower],label:isCc?CC_DURATION_LABEL[lower]:lower,tooltip:QUALITY_TOOLTIPS[lower],emoji:"",};}
function targetingIndicatorMeta(targeting){const lower=(targeting||"").trim().toLowerCase();if(lower==="all summons"){return{cls:"chip-target",label:"summons",tooltip:"",emoji:"🐾",};}
if(lower==="owned summons"||lower==="own summons"||lower==="summon"||lower==="summons only"){return{cls:"chip-target",label:"owned",tooltip:"",emoji:"🐾",};}
const def=config.TARGETING_DEFINITIONS[lower];if(def){const label=lower==="self"?"Self":lower==="all units"?"All units":lower==="multiple targets"?"Multiple targets":lower==="single target"?"Single target":lower==="path"?"path":targeting.trim();return{cls:def.cls,label:label,tooltip:"",emoji:def.emoji,};}
return null;}
function resolveIndicatorMeta(label,indicator,isCc){if(isSpeedMetricLabel(label)){return(speedIndicatorMeta(indicator)||qualityIndicatorMeta(indicator,isCc));}
return(qualityIndicatorMeta(indicator,isCc)||speedIndicatorMeta(indicator));}
function speedIndicatorMeta(value){const lower=value.toLowerCase();if(!SPEED_CLASS[lower]){return null;}
return{cls:"chip-speed "+SPEED_CLASS[lower],label:lower,tooltip:SPEED_TOOLTIPS[lower],emoji:SPEED_EMOJI[lower],};}
function isCcChipClass(cls){return cls==="chip-cc";}
function isCcFamilyChipClass(cls){return cls==="chip-cc"||cls==="chip-anti-cc";}
function ccFamilyChipKeys(){return Object.keys(config.TAG_DEFINITIONS).filter(function(key){return isCcFamilyChipClass(config.TAG_DEFINITIONS[key].cls);}).sort(function(a,b){return b.length-a.length;});}
function exactTagDefinitionKey(label){const trimmed=label.trim();if(!trimmed){return null;}
if(config.TAG_DEFINITIONS[trimmed]){return trimmed;}
const labelLower=trimmed.toLowerCase();if(labelLower==="max hp-based damage"||labelLower==="max hp damage"){return"Max HP damage";}
for(const key of Object.keys(config.TAG_DEFINITIONS)){if(key.toLowerCase()===labelLower){return key;}}
return null;}
function isStatModifierLabel(label){const t=(label||"").trim();return(t==="Damage taken"||t==="Magic damage"||t==="Damage dealt"||t==="Energy");}
function effectLabelPolarity(label){return null;}
const BUFF_DISPLAY_EFFECT_CHIPS={"Damage taken":{emoji:"🛡️",cls:"chip-stat"},"Magic damage":{emoji:"🪄",cls:"chip-stat"},"Damage dealt":{emoji:"⚔️",cls:"chip-stat"},"Ranged damage":{emoji:"🏹",cls:"chip-stat"},"Basic stats":{emoji:"📈",cls:"chip-stat"},};function effectChipClassForPolarity(polarity,fallbackCls){if(polarity==="debuff"){return"chip-debuff";}
if(polarity==="buff"){if(fallbackCls&&fallbackCls.indexOf("chip-debuff")!==-1){return"chip-stat";}
if(!fallbackCls||fallbackCls==="chip-generic"||fallbackCls.indexOf("chip-stat")!==-1){return"chip-stat";}
return fallbackCls;}
return fallbackCls||"chip-generic";}
function resolveLeadingChip(label,polarity){const trimmed=label.trim();if(!trimmed){return{textOnly:"",remainder:"",isCc:false};}
if(polarity==="buff"&&BUFF_DISPLAY_EFFECT_CHIPS[trimmed]){const buff=BUFF_DISPLAY_EFFECT_CHIPS[trimmed];return{emoji:buff.emoji,text:trimmed,cls:effectChipClassForPolarity("buff",buff.cls),isCc:false,remainder:"",};}
if(polarity==="debuff"){const debuffKey=exactTagDefinitionKey(trimmed);if(debuffKey&&config.TAG_DEFINITIONS[debuffKey]){const def=config.TAG_DEFINITIONS[debuffKey];return{emoji:def.emoji,text:debuffKey,cls:effectChipClassForPolarity("debuff",def.cls),isCc:isCcChipClass(def.cls),remainder:"",};}}
const exactKey=exactTagDefinitionKey(trimmed);if(exactKey){const def=config.TAG_DEFINITIONS[exactKey];const resolvedPolarity=polarity||effectLabelPolarity(exactKey);return{emoji:def.emoji,text:exactKey,cls:effectChipClassForPolarity(resolvedPolarity,def.cls),isCc:isCcChipClass(def.cls),remainder:"",};}
const ccKeys=ccFamilyChipKeys();const labelLower=trimmed.toLowerCase();for(let i=0;i<ccKeys.length;i++){const cc=ccKeys[i];const ccLower=cc.toLowerCase();if(labelLower===ccLower||labelLower.startsWith(ccLower+" ")||labelLower.startsWith(ccLower+" HP")){const def=config.TAG_DEFINITIONS[cc];return{emoji:def.emoji,text:cc,cls:def.cls,isCc:isCcChipClass(def.cls),remainder:trimmed.slice(cc.length),};}}
for(let i=0;i<STAT_KEYS.length;i++){const stat=STAT_KEYS[i];const statLower=stat.toLowerCase();if(labelLower===statLower||labelLower.startsWith(statLower+" ")){const def=config.TAG_DEFINITIONS[stat];return{emoji:def.emoji,text:stat,cls:effectChipClassForPolarity(polarity,def.cls),isCc:isCcChipClass(def.cls),remainder:trimmed.slice(stat.length),};}}
for(let i=0;i<HEAL_CHIP_KEYS.length;i++){const heal=HEAL_CHIP_KEYS[i];const healLower=heal.toLowerCase();if(labelLower===healLower||labelLower.startsWith(healLower+" ")){const def=config.TAG_DEFINITIONS[heal];return{emoji:def.emoji,text:healingChipDisplay(heal),cls:def.cls,isCc:false,remainder:trimmed.slice(heal.length),};}}
return{textOnly:trimmed,remainder:"",isCc:false};}
function effectChipRemainder(remainder){const trimmed=(remainder||"").trim().toLowerCase();if(trimmed==="buff"||trimmed==="debuff"){return"";}
if(!remainder){return"";}
const raw=remainder.trim();if(raw.startsWith("via")||raw.startsWith("on")){return" "+raw;}
if(raw.startsWith("to allies")||raw.startsWith("to summons")){return" "+raw;}
return remainder||"";}
function shortAscensionTierName(tierName){const trimmed=tierName.trim();if(trimmed.startsWith("(")&&trimmed.endsWith(")")){const core=trimmed.slice(1,-1).trim();const lower=core.toLowerCase();if(lower.startsWith("ex+")){return core;}
if(lower==="legendary+"){return"L+";}
if(lower==="mythic+"){return"M+";}
if(lower==="supreme+"){return"S+";}
return core;}
return trimmed;}
function formatAscensionTierDisplay(tierSuffix){if(!tierSuffix){return"";}
const short=shortAscensionTierName(tierSuffix);return('<sup class="chip-tier-badge" title="Unlocks at '+
escapeHtml(tierSuffix)+'">'+
escapeHtml(short)+"</sup>");}
function formatMergedTierSuffix(tierSuffix){if(!tierSuffix){return"";}
return formatAscensionTierDisplay(tierSuffix);}
function targetingSegmentCompact(iconOnlyTargeting,index,segmentCount){if(iconOnlyTargeting){return segmentCount>1;}
return index>0;}
function formatMergedIndicator(left,indicatorMeta,textOnlyLeft,iconOnlyRight,skillCardDisplay){let leftHtml;if(left.hasIcon){leftHtml='<span class="chip-merged-left '+
left.cls+'">'+
left.emoji+" "+
escapeHtml(chipDisplayLabel(left.text))+
formatMergedTierSuffix(left.tierSuffix)+"</span>";}else{const leftTipAttrs=left.tooltipHtml?' chip-has-tip"'+chipTipHtmlAttrs(left.tooltipHtml):left.tooltip?' chip-has-tip"'+chipTipAttrs(left.tooltip):'"';leftHtml='<span class="chip-merged-left chip-merged-label'+
leftTipAttrs+">"+
escapeHtml(chipDisplayLabel(left.textOnly))+
formatMergedTierSuffix(left.tierSuffix)+"</span>";}
const showLabel=!iconOnlyRight;const emojiPart=indicatorMeta.emoji?indicatorMeta.emoji+(showLabel&&indicatorMeta.label?" ":""):"";const rightTitle=iconOnlyRight&&indicatorMeta.label?' title="'+escapeHtml(indicatorMeta.label)+'"':"";const rightAttrs=' class="chip-merged-right '+
indicatorMeta.cls+
(indicatorMeta.tooltip?" chip-has-tip":"")+'"'+
rightTitle+
(indicatorMeta.tooltip?chipTipAttrs(indicatorMeta.tooltip):"");const rightHtml="<span"+
rightAttrs+">"+
emojiPart+
(showLabel?escapeHtml(targetingDisplayLabel(indicatorMeta.label,skillCardDisplay)):"")+"</span>";return('<span class="chip chip-merged">'+
leftHtml+'<span class="chip-merged-sep" aria-hidden="true">|</span>'+
rightHtml+"</span>");}
function mergeLabelWithIndicator(label,indicator,tierSuffix,polarity){const leading=resolveLeadingChip(label,polarity);const meta=resolveIndicatorMeta(label,indicator,leading.isCc);if(!meta){return null;}
if(leading.emoji){return(formatMergedIndicator({hasIcon:true,emoji:leading.emoji,text:leading.text,cls:leading.cls,tierSuffix:tierSuffix||"",},meta,false)+escapeHtml(effectChipRemainder(leading.remainder)));}
return formatMergedIndicator({textOnly:label,tierSuffix:tierSuffix||""},meta,true);}
function mergeEffectWithQuality(effectLabel,qualityValue,tierSuffix,polarity){const qualityMeta=qualityIndicatorMeta(qualityValue,resolveLeadingChip(effectLabel,polarity).isCc);if(!qualityMeta){return null;}
const leading=resolveLeadingChip(effectLabel,polarity);if(leading.emoji){return(formatMergedIndicator({hasIcon:true,emoji:leading.emoji,text:leading.text,cls:leading.cls,tierSuffix:tierSuffix||"",},qualityMeta,false)+escapeHtml(effectChipRemainder(leading.remainder)));}
return formatMergedIndicator({textOnly:effectLabel,tierSuffix:tierSuffix||""},qualityMeta,true);}
function classRankIndicatorMeta(value){const lower=(value||"").trim().toLowerCase();if(!QUALITY_CLASS[lower]){return null;}
return{cls:"chip-quality "+QUALITY_CLASS[lower],label:lower,tooltip:CLASS_RANK_TOOLTIPS[lower],emoji:"",};}
function statCategoryCoversHeading(label){return(label||"").replace(/ Stats$/," stats")+" cover:";}
function formatStatCategoryCoversTooltip(label,covers){if(!covers||!covers.length){return"";}
const items=covers.map(function(stat){return"<li>"+escapeHtml(stat)+"</li>";}).join("");return('<div class="stat-category-covers-tip">'+'<p class="stat-category-covers-tip__heading">'+
escapeHtml(statCategoryCoversHeading(label))+"</p>"+'<ul class="stat-category-covers-tip__list">'+
items+"</ul>"+"</div>");}
function renderClassRankCategoryPill(entry){const qualityMeta=classRankIndicatorMeta(entry.rank);if(!qualityMeta){return"";}
return formatMergedIndicator({textOnly:entry.label,tierSuffix:"",tooltipHtml:formatStatCategoryCoversTooltip(entry.label,entry.covers),},qualityMeta,true);}
function renderClassRankMergedPill(label,rank,polarity,withIcon){const qualityMeta=classRankIndicatorMeta(rank);if(!qualityMeta){return"";}
if(withIcon===false){return formatMergedIndicator({textOnly:label,tierSuffix:""},qualityMeta,true);}
const leading=resolveLeadingChip(label,polarity);if(leading.emoji){return(formatMergedIndicator({hasIcon:true,emoji:leading.emoji,text:leading.text,cls:leading.cls,tierSuffix:"",},qualityMeta,false)+escapeHtml(effectChipRemainder(leading.remainder)));}
return formatMergedIndicator({textOnly:label,tierSuffix:""},qualityMeta,true);}
function mergeEffectWithTargeting(effectLabel,targeting,tierSuffix,polarity){const targetingMeta=targetingIndicatorMeta(targeting);if(!targetingMeta){return null;}
const leading=resolveLeadingChip(effectLabel,polarity);if(leading.emoji){return(formatMergedIndicator({hasIcon:true,emoji:leading.emoji,text:leading.text,cls:leading.cls,tierSuffix:tierSuffix||"",},targetingMeta,false,false,true)+escapeHtml(effectChipRemainder(leading.remainder)));}
return formatMergedIndicator({textOnly:effectLabel,tierSuffix:tierSuffix||""},targetingMeta,true,false,true);}
function tryChipify(token){const text=normalizeToken(token);if(!text){return null;}
const lower=text.toLowerCase();if(QUALITY_CLASS[lower]){return formatTag(text);}
if(lower==="signature fuel"){return formatTag(text);}
const targeting=config.TARGETING_DEFINITIONS[lower];if(targeting){return chipSpan(targeting.emoji,text,targeting.cls);}
if(config.TAG_DEFINITIONS[text]){const def=config.TAG_DEFINITIONS[text];return chipSpan(def.emoji,healingChipDisplay(text),def.cls);}
for(const key of Object.keys(config.TAG_DEFINITIONS)){if(key.toLowerCase()===lower){const def=config.TAG_DEFINITIONS[key];return chipSpan(def.emoji,healingChipDisplay(key),def.cls);}}
return null;}
function tokenToHtml(token){const chip=tryChipify(token);return chip!==null?chip:escapeHtml(token.trim());}
function extractChipHtml(html){if(!html||html.indexOf('<span class="chip')!==0){return null;}
const end=html.indexOf("</span>");if(end===-1){return null;}
return html.slice(0,end+7);}
function chipifyEffectName(name,polarity){const parsed=parseEffectLabelParts(name);const label=parsed.base;const tier=parsed.tier;if(label.indexOf(" via ")===-1){return renderStandaloneEffectChip(label,tier,polarity);}
const viaIdx=label.indexOf(" via ");const left=label.slice(0,viaIdx).trim();const right=label.slice(viaIdx+5).trim();const leftChip=chipifyLeadingStat(left);const rightChip=chipifyLeadingStat(right);if(leftChip!==null||rightChip!==null){let leftHtml=leftChip!==null?leftChip:escapeHtml(left);let rightHtml=rightChip!==null?rightChip:escapeHtml(right);if(tier){const leftOnly=extractChipHtml(leftHtml);const rightOnly=extractChipHtml(rightHtml);if(leftOnly){leftHtml=injectTierIntoChipHtml(leftOnly,tier)+leftHtml.slice(leftOnly.length);}else if(rightOnly){rightHtml=injectTierIntoChipHtml(rightOnly,tier)+rightHtml.slice(rightOnly.length);}else{leftHtml+=formatMergedTierSuffix(tier);}}
return leftHtml+" via "+rightHtml;}
return renderStandaloneEffectChip(label,tier,polarity);}
function chipifyLeadingCcType(label){const ccKeys=ccFamilyChipKeys();const labelLower=label.toLowerCase();for(let i=0;i<ccKeys.length;i++){const cc=ccKeys[i];const ccLower=cc.toLowerCase();if(labelLower===ccLower){return tryChipify(cc);}
if(labelLower.startsWith(ccLower+" ")||labelLower.startsWith(ccLower+" HP")){return tryChipify(cc)+escapeHtml(label.slice(cc.length));}}
return null;}
function chipifyLeadingStat(label){const exactKey=exactTagDefinitionKey(label);if(exactKey){return tryChipify(exactKey);}
const labelLower=label.toLowerCase();for(let i=0;i<STAT_KEYS.length;i++){const stat=STAT_KEYS[i];const statLower=stat.toLowerCase();if(labelLower===statLower){return tryChipify(stat);}
if(labelLower.startsWith(statLower+" ")){return tryChipify(stat)+escapeHtml(label.slice(stat.length));}}
return null;}
function unwrapBackticks(text){const trimmed=text.trim();const match=trimmed.match(/^`([^`]+)`$/);return match?match[1].trim():trimmed;}
function promoteStrongToDamageChips(html){return html.replace(/<strong>([^<]+)<\/strong>/g,function(_match,name){const chip=tryChipify(name.trim());return chip!==null?chip:"<strong>"+name+"</strong>";});}
const ASCENSION_TIER_SUFFIX_RE=/\s*(\((?:Legendary\+|Mythic\+|Supreme\+|EX\+\d+)\))\s*$/i;function parseEffectLabelParts(label){let text=(label||"").trim();let tier="";const tierMatch=text.match(ASCENSION_TIER_SUFFIX_RE);if(tierMatch){tier=tierMatch[1];text=text.slice(0,tierMatch.index).trim();}
return{base:text,tier:tier};}
function injectTierIntoChipHtml(chipHtml,tier){if(!tier||!chipHtml){return chipHtml;}
const closeIdx=chipHtml.lastIndexOf("</span>");if(closeIdx===-1){return chipHtml+formatMergedTierSuffix(tier);}
return(chipHtml.slice(0,closeIdx)+
formatMergedTierSuffix(tier)+
chipHtml.slice(closeIdx));}
function applyEffectPolarityToChipHtml(html,polarity){if(!html||!polarity){return html;}
const cls=effectChipClassForPolarity(polarity,"chip-stat");return html.replace(/\bchip-(?:stat|debuff|generic|heal)\b/,cls);}
function renderStandaloneEffectChip(base,tier,polarity){const leading=resolveLeadingChip(base,polarity);if(leading.emoji){return('<span class="chip '+
leading.cls+'">'+
leading.emoji+" "+
escapeHtml(chipDisplayLabel(leading.text))+
formatMergedTierSuffix(tier)+
escapeHtml(effectChipRemainder(leading.remainder)||"")+"</span>");}
const direct=tryChipify(base);if(direct){return injectTierIntoChipHtml(applyEffectPolarityToChipHtml(direct,polarity),tier);}
const ccChip=extractChipHtml(chipifyLeadingCcType(base));if(ccChip){return injectTierIntoChipHtml(ccChip,tier);}
const statChip=extractChipHtml(chipifyLeadingStat(base));if(statChip){return injectTierIntoChipHtml(applyEffectPolarityToChipHtml(statChip,polarity),tier);}
return('<span class="chip '+
effectChipClassForPolarity(polarity,"chip-generic")+'">'+
escapeHtml(chipDisplayLabel(base))+
formatMergedTierSuffix(tier)+"</span>");}
function renderSummaryEffectChip(base,tier,quality,polarity){const merged=mergeEffectWithQuality(base,quality,tier,polarity)||mergeLabelWithIndicator(base,quality,tier,polarity);if(merged){return merged;}
const exact=exactTagDefinitionKey(base);const isCc=exact?isCcChipClass(config.TAG_DEFINITIONS[exact].cls):false;const qMeta=qualityIndicatorMeta(quality||"",isCc);if(qMeta){return formatMergedIndicator({textOnly:base,tierSuffix:tier||""},qMeta,true);}
return renderStandaloneEffectChip(base,tier,polarity)+(quality?" "+formatTag(quality):"");}
function summaryCardPolarity(title){if(/^Debuffs provided by /i.test(title)){return"debuff";}
if(/^Buffs provided by /i.test(title)){return"buff";}
return null;}
function renderEmDashLine(text,polarity){const segments=splitSummarySegments(text);const trailingParts=[];let trailingQuality=null;function popTrailingQuality(){if(!segments.length){return;}
const raw=segments[segments.length-1];const unwrapped=unwrapBackticks(raw);const lower=unwrapped.toLowerCase();if(QUALITY_CLASS[lower]){trailingQuality=unwrapped;segments.pop();}}
function popTrailingConditional(){if(!segments.length){return;}
const last=segments[segments.length-1];if(/conditional/i.test(last)){trailingParts.unshift('<span class="chip chip-generic chip-has-tip"'+
chipTipAttrs(conditionalTooltip(last))+">🎲 "+
escapeHtml(last)+"</span>");segments.pop();}}
popTrailingConditional();popTrailingQuality();popTrailingConditional();const first=segments.shift();const parsed=parseEffectLabelParts(first);let firstHtml;if(/^Primary damage type/i.test(first)){firstHtml=promoteStrongToDamageChips(renderInline(first));}else if(trailingQuality){firstHtml=renderSummaryEffectChip(parsed.base,parsed.tier,trailingQuality,polarity);}else{firstHtml=renderSummaryEffectChip(parsed.base,parsed.tier,"",polarity);}
const targetingTokens=[];segments.forEach(function(seg){unwrapBackticks(seg.trim()).split(/\s*,\s*/).forEach(function(part){const normalized=normalizeToken(part);if(normalized&&targetingTokenMeta(normalized)){targetingTokens.push(normalized);}});});let targetingHtml=renderStackedTargetingPill(targetingTokens);if(targetingTokens.length>1){const sharedTipHtml=renderEffectTargetingStackedTipHtml(first,polarity,targetingTokens);firstHtml=withAnyChipTooltip(firstHtml,sharedTipHtml);targetingHtml=renderStackedTargetingPill(targetingTokens,sharedTipHtml);}
return enhancePlainTargetingInHtml([firstHtml,targetingHtml,trailingParts.join(" ")].filter(Boolean).join(" "));}
function renderRichLine(raw,polarity){const text=normalizeSummaryText(raw);if(/\s*(?:—|–)\s*/.test(text)){return renderEmDashLine(text,polarity);}
const parenMatch=text.match(/^(.+?)\s*\(([^)]+)\)\s*(.*)$/);if(parenMatch&&!/^Primary damage type/i.test(text)){const prefixHtml=chipifyEffectName(parenMatch[1].trim(),polarity);const innerParts=parenMatch[2].split(/\s*,\s*/).map(function(s){return normalizeToken(s);}).filter(Boolean);const innerHtml=innerParts.map(tokenToHtml).join(" ");const suffixRaw=parenMatch[3].trim();const suffixHtml=suffixRaw?renderInline(suffixRaw):"";return enhancePlainTargetingInHtml(prefixHtml+" ("+
innerHtml+")"+
(suffixHtml?" "+suffixHtml:""));}
return enhancePlainTargetingInHtml(promoteStrongToDamageChips(renderInline(text)));}
function formatTag(raw){const tag=normalizeToken(raw);if(!tag){return"";}
const lower=tag.toLowerCase();if(QUALITY_CLASS[lower]){const cls=QUALITY_CLASS[lower];return chipSpan("⭐",tag,cls,QUALITY_TOOLTIPS[lower]);}
if(lower==="signature fuel"){return chipSpan("🔋",tag,"chip-stat",SIGNATURE_FUEL_TOOLTIP);}
const mMeta=speedIndicatorMeta(tag);if(mMeta){return chipSpan(mMeta.emoji,tag,mMeta.cls,mMeta.tooltip);}
const targeting=config.TARGETING_DEFINITIONS[lower];if(targeting){return chipSpan(targeting.emoji,tag,targeting.cls);}
const def=config.TAG_DEFINITIONS[tag]||null;if(def){return chipSpan(def.emoji,healingChipDisplay(tag),def.cls);}
for(const key of Object.keys(config.TAG_DEFINITIONS)){if(key.toLowerCase()===lower){const entry=config.TAG_DEFINITIONS[key];return chipSpan(entry.emoji,healingChipDisplay(key),entry.cls);}}
return'<span class="chip chip-generic">'+escapeHtml(chipDisplayLabel(tag))+"</span>";}
function renderMergedEffectPill(baseLabel,quality,tier,conditional,polarity){const resolvedPolarity=polarity||effectLabelPolarity(baseLabel)||"buff";const leading=resolveLeadingChip(baseLabel,resolvedPolarity);const qMeta=qualityIndicatorMeta(quality,leading.isCc);let merged=mergeEffectWithQuality(baseLabel,quality,tier,resolvedPolarity)||mergeLabelWithIndicator(baseLabel,quality,tier,resolvedPolarity);if(!merged&&qMeta){merged=formatMergedIndicator({textOnly:baseLabel,tierSuffix:tier||""},qMeta,true);}
if(!merged){merged=chipifyEffectName(baseLabel,resolvedPolarity)+
formatMergedTierSuffix(tier)+
(quality?" "+formatTag(quality):"");}
if(conditional){merged+=' <span class="chip chip-generic chip-has-tip"'+
chipTipAttrs(conditionalTooltip(conditional))+">🎲 "+
escapeHtml("conditional ("+conditional+")")+"</span>";}
return merged;}
function renderBuffProvidedEntry(buff){const parsed=parseEffectLabelParts(buff.label||"");const quality=buff.quality||"";const polarity=effectLabelPolarity(parsed.base)||"buff";let html=renderMergedEffectPill(parsed.base,quality,parsed.tier,buff.conditional,polarity);const targetingHtml=renderBuffTargetingChip(buff.targetingType||buff.targeting);if(targetingHtml){html+=" "+targetingHtml;}
return'<span class="synergy-buff-entry">'+html+"</span>";}
function renderBuffTargetingChip(targetingType){if(!targetingType){return"";}
return chipifyTargetingSegment(targetingType);}
const QUALITY_RANK={low:0,average:1,high:2};function isQualityToken(value){return!!QUALITY_CLASS[(value||"").toLowerCase()];}
function combineQualities(qualities){const uniq=[];qualities.forEach(function(q){const lower=(q||"").toLowerCase();if(isQualityToken(lower)&&uniq.indexOf(lower)===-1){uniq.push(lower);}});if(!uniq.length){return"";}
uniq.sort(function(a,b){return QUALITY_RANK[a]-QUALITY_RANK[b];});if(uniq.length===1){return uniq[0];}
return uniq[0]+"-"+uniq[uniq.length-1];}
function combineTargetings(targetings){const parts=[];const seen=new Set();targetings.forEach(function(t){if(!t){return;}
t.split(/\s*,\s*/).forEach(function(piece){const norm=piece.trim();const key=norm.toLowerCase();if(!norm||seen.has(key)){return;}
seen.add(key);const meta=targetingIndicatorMeta(norm);parts.push({key:key,label:meta?meta.label:norm,rank:TARGETING_RANK[key]||0,});});});parts.sort(function(a,b){return b.rank-a.rank;});return parts.map(function(p){return p.label;}).join(" + ");}
function combineTierLabels(tiers){const uniq=[];tiers.forEach(function(t){if(t&&uniq.indexOf(t)===-1){uniq.push(t);}});return uniq.map(function(t){return shortAscensionTierName(t);}).join(", ");}
function combineUniqueText(values){const uniq=[];values.forEach(function(v){if(v&&uniq.indexOf(v)===-1){uniq.push(v);}});return uniq.join(" + ");}
function buildVariantModifier(variants){const parts=[];const quality=combineQualities(variants.map(function(v){return v.quality;}));if(quality){parts.push(quality);}
const targeting=combineTargetings(variants.map(function(v){return v.targeting;}));if(targeting){parts.push(targeting);}
const tiers=combineTierLabels(variants.map(function(v){return v.tier;}));if(tiers){parts.push(tiers);}
const timing=combineUniqueText(variants.map(function(v){return v.timing;}));if(timing){parts.push(timing);}
return parts.join("; ");}
function effectVariantGroupKey(variant,cardPolarity){const polarity=cardPolarity||variant.polarity||"";return variant.base.toLowerCase()+":"+polarity;}
function parseSkillCardVariant(raw,explicitPolarity){let work=(raw||"").trim();if(!work){return null;}
let tier="";const tierMatch=work.match(ASCENSION_TIER_SUFFIX_RE);if(tierMatch){tier=tierMatch[1];work=work.slice(0,tierMatch.index).trim();}
const split=parseSkillCardTag(work);if(!split.tag){return null;}
const polarity=explicitPolarity||effectLabelPolarity(split.tag)||"buff";return{base:split.tag,tier:tier,targeting:split.targeting||"",quality:"",conditional:"",timing:"",polarity:polarity,raw:raw,};}
function parseSummaryVariant(raw,cardPolarity){const segments=splitSummarySegments(raw);if(!segments.length){return null;}
const parsed=parseEffectLabelParts(segments[0]);if(!parsed.base){return null;}
let targeting="";let quality="";let conditional="";let timing="";for(let i=1;i<segments.length;i++){const seg=unwrapBackticks(segments[i]);const lower=seg.toLowerCase();if(isQualityToken(lower)){quality=lower;}else if(/conditional\s*\(/i.test(seg)){conditional=seg;}else if(targetingIndicatorMeta(seg)){if(targeting){targeting+=", "+seg;}else{targeting=seg;}}else if(!timing){timing=seg;}else{timing+=" + "+seg;}}
if(!targeting&&segments[1]&&!isQualityToken(unwrapBackticks(segments[1]).toLowerCase())&&!/conditional\s*\(/i.test(segments[1])){targeting=unwrapBackticks(segments[1]);if(segments[2]&&isQualityToken(unwrapBackticks(segments[2]).toLowerCase())){quality=unwrapBackticks(segments[2]).toLowerCase();}
if(segments[3]&&/conditional\s*\(/i.test(segments[3])){conditional=segments[3];}else if(segments[3]){timing=segments[3];}}
const polarity=cardPolarity||effectLabelPolarity(parsed.base)||"buff";return{base:parsed.base,tier:parsed.tier||"",targeting:targeting,quality:quality,conditional:conditional,timing:timing,polarity:polarity,raw:raw,};}
function collectTargetingSegments(variants){const parts=[];const seen=new Set();variants.forEach(function(v){if(!v.targeting){return;}
v.targeting.split(/\s*,\s*/).forEach(function(piece){const norm=piece.trim();const key=norm.toLowerCase();if(!norm||seen.has(key)){return;}
seen.add(key);const tokenMeta=targetingTokenMeta(norm);if(tokenMeta){parts.push(tokenMeta);return;}
const indMeta=targetingIndicatorMeta(norm);if(indMeta){parts.push({emoji:indMeta.emoji,text:indMeta.label,cls:indMeta.cls,rank:TARGETING_RANK[key]||0,});}});});parts.sort(function(a,b){return b.rank-a.rank;});return parts;}
function mergedVariantSep(){return'<span class="chip-merged-sep" aria-hidden="true">|</span>';}
function qualityRangeMeta(qualityValue,isCc){if(!qualityValue){return null;}
if(qualityValue.indexOf("-")!==-1){const range=qualityValue.split("-");if(range.length===2&&isQualityToken(range[0])&&isQualityToken(range[1])){return{cls:"chip-generic",label:qualityValue,tooltip:"",emoji:"",};}}
return qualityIndicatorMeta(qualityValue,isCc);}
function renderMergedQualitySegment(qualityValue,isCc){if(!qualityValue){return"";}
const qMeta=qualityRangeMeta(qualityValue,isCc);if(!qMeta){return('<span class="chip-merged-right chip-generic">'+
escapeHtml(qualityValue)+"</span>");}
return('<span class="chip-merged-right '+
qMeta.cls+'">'+
escapeHtml(qMeta.label)+"</span>");}
function renderEffectQualityMergedPill(base,polarity,qualityRange){const leading=resolveLeadingChip(base,polarity);const qMeta=qualityRangeMeta(qualityRange,leading.isCc);if(!qMeta){return"";}
if(leading.emoji){return formatMergedIndicator({hasIcon:true,emoji:leading.emoji,text:leading.text,cls:leading.cls,tierSuffix:"",},qMeta,false);}
return formatMergedIndicator({textOnly:base,tierSuffix:""},qMeta,true);}
function renderTargetingMergedPill(targetingSegments,iconOnlyTargeting,skillCardDisplay){if(!targetingSegments.length){return"";}
if(targetingSegments.length===1){const meta=targetingSegments[0];return chipSpan(meta.emoji,targetingDisplayLabel(meta.text||meta.label,skillCardDisplay),meta.cls);}
if(iconOnlyTargeting){const segmentCount=targetingSegments.length;const parts=targetingSegments.map(function(meta,index){return renderMergedTargetingSegment(meta,targetingSegmentCompact(iconOnlyTargeting,index,segmentCount),skillCardDisplay);});return'<span class="chip chip-merged">'+parts.join("")+"</span>";}
const parts=[];targetingSegments.forEach(function(meta,index){if(index===0){parts.push('<span class="chip-merged-left '+
meta.cls+'">'+
meta.emoji+" "+
escapeHtml(chipDisplayLabel(meta.text||meta.label))+"</span>");return;}
parts.push(renderMergedTargetingSegment(meta,true,false));});return'<span class="chip chip-merged">'+parts.join("")+"</span>";}
function renderMergedEffectBodyParts(first,leading,qualityRange,targetingSegments,iconOnlyTargeting,skillCardDisplay){const bodyParts=[];if(leading.emoji){bodyParts.push('<span class="chip-merged-left '+
leading.cls+'">'+
leading.emoji+" "+
escapeHtml(chipDisplayLabel(leading.text))+"</span>");}else{bodyParts.push('<span class="chip-merged-left chip-merged-label">'+
escapeHtml(chipDisplayLabel(first.base))+"</span>");}
const qualitySeg=renderMergedQualitySegment(qualityRange,leading.isCc);if(qualitySeg){bodyParts.push(qualitySeg);}
const segmentCount=targetingSegments.length;targetingSegments.forEach(function(meta,index){bodyParts.push(renderMergedTargetingSegment(meta,targetingSegmentCompact(iconOnlyTargeting,index,segmentCount),skillCardDisplay));});return bodyParts;}
function groupedVariantTipAttrs(tipHtml){return(' chip-has-tip" data-tip-html="'+
escapeHtml(tipHtml)+'" tabindex="0" role="button" aria-describedby="chip-tooltip"');}
function withChipTooltip(chipHtml,tipHtml){if(!chipHtml||!tipHtml){return chipHtml;}
return chipHtml.replace('<span class="chip chip-merged"','<span class="chip chip-merged'+groupedVariantTipAttrs(tipHtml));}
function withAnyChipTooltip(chipHtml,tipHtml){if(!chipHtml||!tipHtml){return chipHtml;}
return chipHtml.replace(/(<span class="chip[^"]*)"/,"$1"+groupedVariantTipAttrs(tipHtml));}
function renderEffectTargetingStackedTipHtml(effectLabel,polarity,targetingTokens){return('<div class="chip-stacked-tip">'+
targetingTokens.map(function(token){return('<div class="chip-merged-tip-line">'+
renderRichLine(effectLabel+" — "+token,polarity)+"</div>");}).join("")+"</div>");}
function renderStandaloneEffectTooltipChip(variant){const parsed=parseEffectLabelParts(variant.base);const tier=variant.tier||parsed.tier;const base=parsed.base;const polarity=variant.polarity;const leading=resolveLeadingChip(base,polarity);if(leading.emoji){return('<span class="chip '+
leading.cls+'">'+
leading.emoji+" "+
escapeHtml(chipDisplayLabel(leading.text))+
formatMergedTierSuffix(tier)+"</span>");}
const chip=extractChipHtml(renderStandaloneEffectChip(base,tier,polarity));return chip||renderStandaloneEffectChip(base,tier,polarity);}
function renderVariantTooltipParts(variant){const parts=[renderStandaloneEffectTooltipChip(variant)];if(variant.quality){const qChip=formatTag(variant.quality);if(qChip){parts.push(qChip);}}
const targeting=renderTargetingTooltipLine(variant);if(targeting){parts.push(targeting);}
if(variant.timing){parts.push('<span class="chip chip-generic">'+
escapeHtml(variant.timing)+"</span>");}
if(variant.conditional){parts.push('<span class="chip chip-generic chip-has-tip"'+
chipTipAttrs(conditionalTooltip(variant.conditional))+">🎲 "+
escapeHtml(variant.conditional)+"</span>");}
return parts;}
function renderTargetingTooltipLine(variant){if(!variant.targeting){return"";}
const tMeta=targetingIndicatorMeta(variant.targeting);if(tMeta){return('<span class="chip '+
tMeta.cls+'">'+
(tMeta.emoji?tMeta.emoji+" ":"")+
escapeHtml(chipDisplayLabel(tMeta.label))+"</span>");}
return chipifyTargetingSegment(variant.targeting);}
function renderMergedTargetingSegment(meta,compact,skillCardDisplay){const emoji=meta.emoji?meta.emoji:"";const label=compact?"":escapeHtml(targetingDisplayLabel(meta.text||meta.label,skillCardDisplay));const spacer=compact||!label?"":" ";const titleAttr=compact&&(meta.text||meta.label)?' title="'+
escapeHtml(meta.text||meta.label)+'"':"";return('<span class="chip-merged-right '+
meta.cls+'"'+
titleAttr+">"+
emoji+
spacer+
label+"</span>");}
function variantTierOnTrailingSegment(variant){if(!variant.tier){return false;}
const segments=splitSummarySegments(variant.raw);if(!segments.length){return false;}
const parsed=parseEffectLabelParts(segments[0]);return!parsed.tier;}
function renderVariantTooltipContent(variant){if(!variant.raw){return"";}
if(variant.quality||/`/.test(variant.raw)){return renderRichLine(variant.raw,variant.polarity);}
return renderVariantTooltipParts(variant).join(" ");}
function renderMergedVariantTooltipHtml(variants){return('<div class="chip-stacked-tip">'+
variants.map(function(variant){return('<div class="chip-merged-tip-line">'+
renderVariantTooltipContent(variant)+"</div>");}).join("")+"</div>");}
function renderGroupedVariantPill(variants,opts){opts=opts||{};const iconOnlyTargeting=!!opts.iconOnlyTargeting;const skillCardDisplay=!!opts.skillCardDisplay;if(!variants||variants.length<=1){return"";}
const first=variants[0];const polarity=first.polarity;const leading=resolveLeadingChip(first.base,polarity);const qualityRange=combineQualities(variants.map(function(v){return v.quality;}));const targetingSegments=collectTargetingSegments(variants);if(qualityRange&&targetingSegments.length){const fullTip=renderMergedVariantTooltipHtml(variants);const effectPill=withChipTooltip(renderEffectQualityMergedPill(first.base,polarity,qualityRange),fullTip);const targetingPill=withChipTooltip(renderTargetingMergedPill(targetingSegments,iconOnlyTargeting,skillCardDisplay),fullTip);return('<span class="grouped-variant-pills">'+
effectPill+" "+
targetingPill+"</span>");}
const bodyHtml=renderMergedEffectBodyParts(first,leading,qualityRange,targetingSegments,iconOnlyTargeting,skillCardDisplay).join("");return withChipTooltip('<span class="chip chip-merged">'+bodyHtml+"</span>",renderMergedVariantTooltipHtml(variants));}
function groupParsedVariants(items,parseFn,cardPolarity){const groupByKey={};items.forEach(function(item,index){const variant=parseFn(item,cardPolarity);if(!variant){return;}
const key=effectVariantGroupKey(variant,cardPolarity);if(!groupByKey[key]){groupByKey[key]={key:key,variants:[],indices:[],firstIndex:index,};}
const group=groupByKey[key];if(group.firstIndex>index){group.firstIndex=index;}
if(!group.variants.some(function(v){return v.raw===variant.raw;})){group.variants.push(variant);}
group.indices.push(index);});const consumed=new Set();const result=[];items.forEach(function(item,index){if(consumed.has(index)){return;}
const variant=parseFn(item,cardPolarity);if(!variant){result.push({type:"raw",item:item});return;}
const key=effectVariantGroupKey(variant,cardPolarity);const group=groupByKey[key];if(group.variants.length>1){result.push({type:"group",variants:group.variants});group.indices.forEach(function(i){consumed.add(i);});return;}
result.push({type:"raw",item:item});consumed.add(index);});return result;}
function groupSummaryItems(items,cardPolarity){return groupParsedVariants(items,parseSummaryVariant,cardPolarity);}
function parseSkillCardTag(raw){let tag=raw.trim();let targeting="";const allSummonMatch=tag.match(/^(.+?)\s*(?:—|–)\s*Summons\s*$/i);if(allSummonMatch){tag=allSummonMatch[1].trim();targeting="All summons";return{tag:tag,targeting:targeting};}
const ownSummonMatch=tag.match(/^(.+?)\s*(?:—|–)\s*Owned\s*$/i);if(ownSummonMatch){tag=ownSummonMatch[1].trim();targeting="Owned summons";return{tag:tag,targeting:targeting};}
const legacySummonMatch=tag.match(/^(.+?)\s*(?:—|–)\s*Summon\s*$/i);if(legacySummonMatch){tag=legacySummonMatch[1].trim();targeting="Owned summons";return{tag:tag,targeting:targeting};}
const enemyTargetingMatch=tag.match(/^(.+?)\s*(?:—|–)\s*(All units|Area|Arc|Path|Multiple targets|Single target)\s*$/i);if(enemyTargetingMatch){tag=enemyTargetingMatch[1].trim();targeting=enemyTargetingMatch[2].trim();return{tag:tag,targeting:targeting};}
const selfMatch=tag.match(/^(.+?)\s*(?:—|–)\s*Self\s*$/i);if(selfMatch){tag=selfMatch[1].trim();targeting="Self";}
return{tag:tag,targeting:targeting};}
function chipifySkillCardTag(raw,explicitPolarity){let work=raw.trim();if(!work){return"";}
let tier="";const tierMatch=work.match(ASCENSION_TIER_SUFFIX_RE);if(tierMatch){tier=tierMatch[1];work=work.slice(0,tierMatch.index).trim();}
const split=parseSkillCardTag(work);let tag=split.tag;if(!tag){return"";}
const parsed=parseEffectLabelParts(tag);const polarity=explicitPolarity||effectLabelPolarity(parsed.base)||"buff";tag=parsed.base;const tierSuffix=tier||parsed.tier;if(split.targeting&&targetingIndicatorMeta(split.targeting)){const merged=mergeEffectWithTargeting(tag,split.targeting,tierSuffix,polarity);if(merged){return merged;}}
if(polarity==="debuff"){const debuffChip=tryChipify(tag);if(debuffChip){return injectTierIntoChipHtml(applyEffectPolarityToChipHtml(debuffChip,polarity),tierSuffix);}}
const direct=tryChipify(tag);if(direct){return injectTierIntoChipHtml(applyEffectPolarityToChipHtml(direct,polarity),tierSuffix);}
const ccChip=extractChipHtml(chipifyLeadingCcType(tag));if(ccChip){return injectTierIntoChipHtml(ccChip,tierSuffix);}
const statChip=extractChipHtml(chipifyLeadingStat(tag));if(statChip){return injectTierIntoChipHtml(applyEffectPolarityToChipHtml(statChip,polarity),tierSuffix);}
const effectChip=extractChipHtml(renderStandaloneEffectChip(tag,tierSuffix,polarity));if(effectChip){return effectChip;}
const label=tag.replace(/\s*\([^)]*\)/g,"").trim();if(!label){return"";}
return injectTierIntoChipHtml(chipSpan("🏷️",label,effectChipClassForPolarity(polarity,"chip-generic")),tierSuffix);}
window.AFKJ.chips={QUALITY_CLASS:QUALITY_CLASS,SPEED_CLASS:SPEED_CLASS,SPEED_EMOJI:SPEED_EMOJI,QUALITY_EMOJI:QUALITY_EMOJI,QUALITY_TOOLTIPS:QUALITY_TOOLTIPS,CLASS_RANK_TOOLTIPS:CLASS_RANK_TOOLTIPS,SPEED_TOOLTIPS:SPEED_TOOLTIPS,SIGNATURE_FUEL_TOOLTIP:SIGNATURE_FUEL_TOOLTIP,MOVEMENT_DEFINITIONS:MOVEMENT_DEFINITIONS,MOVEMENT_KEYS:MOVEMENT_KEYS,TARGETING_PHRASES:TARGETING_PHRASES,STAT_KEYS:STAT_KEYS,HEAL_CHIP_KEYS:HEAL_CHIP_KEYS,healingChipDisplay:healingChipDisplay,tryMergeTrailingLabel:tryMergeTrailingLabel,renderCharacterPill:renderCharacterPill,renderInline:renderInline,conditionalTooltip:conditionalTooltip,chipTipAttrs:chipTipAttrs,chipTipHtmlAttrs:chipTipHtmlAttrs,normalizeToken:normalizeToken,normalizeSummaryText:normalizeSummaryText,splitSummarySegments:splitSummarySegments,isInsideHtmlTag:isInsideHtmlTag,isInsideChipSpan:isInsideChipSpan,isInsideSpanClass:isInsideSpanClass,isInsideSkillInlineStat:isInsideSkillInlineStat,isInsideSkillInlineTime:isInsideSkillInlineTime,isInsideSkillInlineNum:isInsideSkillInlineNum,isInsideStrong:isInsideStrong,boldSkillNumericTokens:boldSkillNumericTokens,replaceOutsideChips:replaceOutsideChips,enhancePlainTargetingInHtml:enhancePlainTargetingInHtml,targetingTokenMeta:targetingTokenMeta,renderStackedTargetingTipHtml:renderStackedTargetingTipHtml,renderStackedTargetingPill:renderStackedTargetingPill,chipifyTargetingSegment:chipifyTargetingSegment,chipDisplayLabel:chipDisplayLabel,chipSpan:chipSpan,behaviorTagTooltip:behaviorTagTooltip,behaviorTagDefinition:behaviorTagDefinition,behaviorTagChip:behaviorTagChip,renderFilterComboChip:renderFilterComboChip,renderFilterComboChips:renderFilterComboChips,isSpeedMetricLabel:isSpeedMetricLabel,qualityIndicatorMeta:qualityIndicatorMeta,targetingIndicatorMeta:targetingIndicatorMeta,resolveIndicatorMeta:resolveIndicatorMeta,speedIndicatorMeta:speedIndicatorMeta,isCcChipClass:isCcChipClass,isCcFamilyChipClass:isCcFamilyChipClass,ccFamilyChipKeys:ccFamilyChipKeys,exactTagDefinitionKey:exactTagDefinitionKey,isStatModifierLabel:isStatModifierLabel,effectLabelPolarity:effectLabelPolarity,effectChipClassForPolarity:effectChipClassForPolarity,resolveLeadingChip:resolveLeadingChip,effectChipRemainder:effectChipRemainder,shortAscensionTierName:shortAscensionTierName,formatAscensionTierDisplay:formatAscensionTierDisplay,formatMergedTierSuffix:formatMergedTierSuffix,formatMergedIndicator:formatMergedIndicator,mergeLabelWithIndicator:mergeLabelWithIndicator,mergeEffectWithQuality:mergeEffectWithQuality,classRankIndicatorMeta:classRankIndicatorMeta,renderClassRankMergedPill:renderClassRankMergedPill,renderClassRankCategoryPill:renderClassRankCategoryPill,formatStatCategoryCoversTooltip:formatStatCategoryCoversTooltip,mergeEffectWithTargeting:mergeEffectWithTargeting,tryChipify:tryChipify,tokenToHtml:tokenToHtml,chipifyEffectName:chipifyEffectName,chipifyLeadingCcType:chipifyLeadingCcType,chipifyLeadingStat:chipifyLeadingStat,unwrapBackticks:unwrapBackticks,promoteStrongToDamageChips:promoteStrongToDamageChips,parseEffectLabelParts:parseEffectLabelParts,injectTierIntoChipHtml:injectTierIntoChipHtml,applyEffectPolarityToChipHtml:applyEffectPolarityToChipHtml,renderStandaloneEffectChip:renderStandaloneEffectChip,renderSummaryEffectChip:renderSummaryEffectChip,summaryCardPolarity:summaryCardPolarity,renderEmDashLine:renderEmDashLine,renderRichLine:renderRichLine,formatTag:formatTag,renderMergedEffectPill:renderMergedEffectPill,renderBuffProvidedEntry:renderBuffProvidedEntry,renderBuffTargetingChip:renderBuffTargetingChip,extractChipHtml:extractChipHtml,parseSkillCardTag:parseSkillCardTag,chipifySkillCardTag:chipifySkillCardTag,parseSkillCardVariant:parseSkillCardVariant,parseSummaryVariant:parseSummaryVariant,groupSummaryItems:groupSummaryItems,groupParsedVariants:groupParsedVariants,renderGroupedVariantPill:renderGroupedVariantPill,buildVariantModifier:buildVariantModifier,};})();window.AFKJ=window.AFKJ||{};(function(){const utils=window.AFKJ.utils;const escapeHtml=utils.escapeHtml.bind(utils);const PRYDWEN_TIER_MODES=[{key:"afk_stages",label:"AFK Stages"},{key:"dream_realm",label:"Dream Realm"},{key:"dream_realm_endless",label:"Dream Realm (Endless)"},{key:"pvp",label:"PVP"},];const TIER_CSV_COLUMNS=[{header:"AFK Stages tier",key:"afk_stages"},{header:"Dream Realm tier",key:"dream_realm"},{header:"Dream Realm Endless tier",key:"dream_realm_endless"},{header:"PVP tier",key:"pvp"},];const TIER_CSV_HEADERS={};TIER_CSV_COLUMNS.forEach(function(tierCol){TIER_CSV_HEADERS[tierCol.header]=true;});const TIER_RANK_ORDER=["C","B","A","A+","S","S+"];const REFERENCE_TIER_WEIGHT=7;const REFERENCE_TIER_POINTS_PER_STEP=100;const TIER_FILTER_ORDER=["?","C","B","A","A+","S","S+"];function isUnrankedPrydwenTier(tier){const value=tier!=null?String(tier).trim():"";return!value||value==="?";}
function prydwenTierClass(tier){if(isUnrankedPrydwenTier(tier)){return"tier-unknown";}
const normalized=String(tier).trim().replace(/\+/g,"-plus");return"tier-"+normalized.toLowerCase();}
function prydwenTierDisplay(tier){return isUnrankedPrydwenTier(tier)?"?":String(tier).trim();}
function prydwenTierRank(tier){if(!tier||tier==="?"){return-1;}
const idx=TIER_RANK_ORDER.indexOf(tier);return idx>=0?idx:-1;}
function comparePrydwenTiers(repTier,mainTier){const repRank=prydwenTierRank(repTier);const mainRank=prydwenTierRank(mainTier);if(mainRank<0&&repRank<0){return"same";}
if(mainRank<0){return"better";}
if(repRank<0){return"worse";}
if(repRank>mainRank){return"better";}
if(repRank<mainRank){return mainRank-repRank===1?"worse-1":"worse";}
return"same";}
function relativeTierTooltip(relation,mainHeroName,modeLabel,mainTier,repTier){const base=mainHeroName+"'s "+modeLabel+" tier";if(!mainTier){return"No Prydwen tier listed for "+base+".";}
if(!repTier){return"No Prydwen tier listed for this replacement hero.";}
if(relation==="better"){return"Better than "+base+" ("+mainTier+"). This replacement is "+repTier+".";}
if(relation==="worse-1"){return"One tier below "+base+" ("+mainTier+"). This replacement is "+repTier+".";}
if(relation==="worse"){return"Worse than "+base+" ("+mainTier+"). This replacement is "+repTier+".";}
return"Same as "+base+" ("+mainTier+").";}
function formatTierColumnHeader(col){if(col.endsWith(" tier")){return escapeHtml(col.slice(0,-5))+"<br>"+escapeHtml("tier");}
return escapeHtml(col);}
function getHeroPrydwenTiers(hero){const tiers=(hero&&hero.prydwenTiers)||{};const out={};PRYDWEN_TIER_MODES.forEach(function(mode){const raw=tiers[mode.key];out[mode.key]=isUnrankedPrydwenTier(raw)?"?":String(raw).trim();});return out;}
function renderTierTableCell(tier){const value=(tier||"").trim();const display=prydwenTierDisplay(value);return('<span class="tier-chip tier-chip-table '+
prydwenTierClass(value)+'"><span class="tier-grade">'+
escapeHtml(display)+"</span></span>");}
function augmentCsvWithTiers(){const state=window.AFKJ.state;if(!state.csvHeaders.length||!Object.keys(state.heroByName).length){return;}
const classIdx=state.csvHeaders.indexOf("Class");if(classIdx===-1){return;}
let roleIdx=state.csvHeaders.indexOf("Role");if(roleIdx===-1){roleIdx=classIdx+1;state.csvHeaders.splice(roleIdx,0,"Role");state.csvRows=state.csvRows.map(function(row){const newRow=row.slice();newRow.splice(roleIdx,0,"");return newRow;});}
const missing=TIER_CSV_COLUMNS.filter(function(tierCol){return state.csvHeaders.indexOf(tierCol.header)===-1;});if(missing.length){const insertAt=roleIdx+1;missing.forEach(function(tierCol,offset){state.csvHeaders.splice(insertAt+offset,0,tierCol.header);});state.csvRows=state.csvRows.map(function(row){const newRow=row.slice();missing.forEach(function(_,offset){newRow.splice(insertAt+offset,0,"");});return newRow;});}
const colByKey={};TIER_CSV_COLUMNS.forEach(function(tierCol){const idx=state.csvHeaders.indexOf(tierCol.header);if(idx!==-1){colByKey[tierCol.key]=idx;}});const roleColIdx=state.csvHeaders.indexOf("Role");state.csvRows.forEach(function(row){const hero=state.heroByName[row[0]||""];if(!hero){return;}
if(roleColIdx!==-1&&!String(row[roleColIdx]||"").trim()){const roleMeta=window.AFKJ.config.ROLE_CATEGORY_META[hero.roleCategory];if(roleMeta){row[roleColIdx]=roleMeta.label;}}
const tiers=getHeroPrydwenTiers(hero);Object.keys(colByKey).forEach(function(key){const idx=colByKey[key];if(!String(row[idx]||"").trim()){row[idx]=tiers[key]||"?";}});});}
function renderPrydwenTierBoxes(tiers,variant,compareTo,mainHeroName){if(!tiers){return"";}
const compact=variant==="compact";const relative=compact&&compareTo;const rowClass=compact?"tier-box-row tier-box-row-compact":"tier-box-row";const chipClass=compact?"tier-chip tier-chip-compact":"tier-chip";let html='<div class="'+rowClass+'">';PRYDWEN_TIER_MODES.forEach(function(mode){const rawTier=tiers[mode.key];const displayTier=prydwenTierDisplay(rawTier);let colorClass=prydwenTierClass(rawTier);let tipAttrs="";if(relative){const mainTier=compareTo[mode.key];const relation=comparePrydwenTiers(rawTier,mainTier);colorClass="tier-rel-"+relation;tipAttrs=window.AFKJ.chips.chipTipAttrs(relativeTierTooltip(relation,mainHeroName||"this hero",mode.label,mainTier,displayTier));}
html+='<span class="'+
chipClass+" "+
colorClass+
(tipAttrs?" chip-has-tip":"")+'"'+
tipAttrs+">"+'<span class="tier-grade">'+
escapeHtml(displayTier)+"</span>"+'<span class="tier-mode">'+
escapeHtml(mode.label)+"</span></span>";});html+="</div>";return html;}
function stripPrydwenTierLine(md){if(!md){return md;}
const parts=md.split("\n\n");if(parts.length<3){return md;}
if(!parts[0].endsWith("'s behavior")){return md;}
if(parts[1].startsWith("- ")||parts[1].startsWith("#")){return md;}
return[parts[0],parts.slice(2).join("\n\n")].join("\n\n");}
function roleCategoryMeta(roleCategory){return window.AFKJ.config.ROLE_CATEGORY_META[roleCategory]||null;}
window.AFKJ.tiers={PRYDWEN_TIER_MODES:PRYDWEN_TIER_MODES,TIER_CSV_COLUMNS:TIER_CSV_COLUMNS,TIER_CSV_HEADERS:TIER_CSV_HEADERS,TIER_RANK_ORDER:TIER_RANK_ORDER,REFERENCE_TIER_WEIGHT:REFERENCE_TIER_WEIGHT,REFERENCE_TIER_POINTS_PER_STEP:REFERENCE_TIER_POINTS_PER_STEP,TIER_FILTER_ORDER:TIER_FILTER_ORDER,isUnrankedPrydwenTier:isUnrankedPrydwenTier,prydwenTierClass:prydwenTierClass,prydwenTierDisplay:prydwenTierDisplay,prydwenTierRank:prydwenTierRank,comparePrydwenTiers:comparePrydwenTiers,relativeTierTooltip:relativeTierTooltip,formatTierColumnHeader:formatTierColumnHeader,getHeroPrydwenTiers:getHeroPrydwenTiers,renderTierTableCell:renderTierTableCell,augmentCsvWithTiers:augmentCsvWithTiers,renderPrydwenTierBoxes:renderPrydwenTierBoxes,stripPrydwenTierLine:stripPrydwenTierLine,roleCategoryMeta:roleCategoryMeta,};})();window.AFKJ=window.AFKJ||{};(function(){function renderMarkdown(md,options){if(!md)return"";const chips=window.AFKJ.chips;const detail=window.AFKJ.views.detail;const skillOverview=options&&options.skillOverview;const behaviorSection=options&&options.behaviorSection;const overviewList=skillOverview||behaviorSection;const renderItem=skillOverview?detail.renderSkillOverviewItem:function(text){return detail.renderBehaviorItem(text,options);};const lines=md.split("\n");const parts=[];let inList=false;function closeList(){if(inList){parts.push("</ul>");inList=false;}}
for(const raw of lines){const line=raw.trimEnd();if(!line.trim()){closeList();continue;}
if(line.startsWith("##### ")){closeList();parts.push("<h5>"+chips.renderInline(line.slice(6))+"</h5>");}else if(line.startsWith("#### ")){closeList();parts.push("<h4>"+chips.renderInline(line.slice(5))+"</h4>");}else if(line.startsWith("### ")){closeList();parts.push("<h3>"+chips.renderInline(line.slice(4))+"</h3>");}else if(line.startsWith("- ")){if(!inList){parts.push(overviewList?'<ul class="skill-overview-list">':"<ul>");inList=true;}
parts.push("<li>"+renderItem(line.slice(2))+"</li>");}else{closeList();parts.push("<p>"+chips.renderInline(line)+"</p>");}}
closeList();return parts.join("\n");}
window.AFKJ.markdown={renderMarkdown:renderMarkdown};})();window.AFKJ=window.AFKJ||{};(function(){const utils=window.AFKJ.utils;const chips=window.AFKJ.chips;const escapeHtml=utils.escapeHtml.bind(utils);const SKILL_META_EMOJI={Cooldown:"⏱️","Initial Cooldown":"⏳","Skill Range":"📏","Initial Energy":"🔋",};const SKILL_META_ORDER=["Cooldown","Initial Cooldown","Skill Range","Initial Energy",];const SKILL_CARD_DAMAGE_KEYS=["HP loss","Max HP damage","Max HP-based damage","True damage","Physical","Magic","DoT",];const SKILL_CARD_CC_KEYS=Object.keys(window.AFKJ.config.TAG_DEFINITIONS).filter(function(key){return chips.isCcChipClass(window.AFKJ.config.TAG_DEFINITIONS[key].cls);}).sort(function(a,b){return b.length-a.length;});const SKILL_CARD_HEX_ICONS={ultimate:"🌟",skill1:"💫",skill2:"💫",skill3:"🗡️",skill4:"⚔️",skill5:"✨",};const SKILL_SCALING_DURATION_MOD_RE=/(\d+(?:\.\d+)?)\s*(\((?:SP-based|HP[- ]based|ATK[- ]based)\))\s*s\b/gi;const SKILL_SCALING_MODIFIERS=[{re:/\(SP-based\)/gi,emoji:"💡",tooltip:"This number is based on skill power.",},{re:/\(HP[- ]based\)/gi,emoji:"❤️",tooltip:"This number is based on HP.",},{re:/\(ATK[- ]based\)/gi,emoji:"💪",tooltip:"This number is based on ATK.",},];function normalizeScalingDurationModifiers(text){return text.replace(SKILL_SCALING_DURATION_MOD_RE,"$1s $2");}
function skillScalingModifierChip(entry){return chips.chipSpan(entry.emoji,"","chip-scaling-mod",entry.tooltip);}
function enrichSkillInline(text,opts){opts=opts||{};if(!text){return"";}
const TAG_DEFINITIONS=window.AFKJ.config.TAG_DEFINITIONS;let out=escapeHtml(normalizeScalingDurationModifiers(text));SKILL_SCALING_MODIFIERS.forEach(function(entry){out=chips.replaceOutsideChips(out,entry.re,function(){return skillScalingModifierChip(entry);});});out=chips.replaceOutsideChips(out,/\bphys(?:ical)?\s*&\s*magic\s+def\b/gi,function(){const physDef=TAG_DEFINITIONS["Phys DEF"];const magicDef=TAG_DEFINITIONS["Magic DEF"];return(chips.chipSpan(physDef.emoji,"Phys DEF",physDef.cls)+" &amp; "+
chips.chipSpan(magicDef.emoji,"Magic DEF",magicDef.cls));});chips.STAT_KEYS.forEach(function(key){const def=TAG_DEFINITIONS[key];const re=new RegExp("\\b"+key.replace(/[.*+?^${}()|[\]\\]/g,"\\$&")+"\\b","gi");out=chips.replaceOutsideChips(out,re,function(match){return chips.chipSpan(def.emoji,match,def.cls);});});chips.HEAL_CHIP_KEYS.forEach(function(key){const def=TAG_DEFINITIONS[key];const re=new RegExp("\\b"+key.replace(/[.*+?^${}()|[\]\\]/g,"\\$&")+"\\b","gi");out=chips.replaceOutsideChips(out,re,function(match){return chips.chipSpan(def.emoji,match,def.cls);});});chips.TARGETING_PHRASES.forEach(function(entry){const def=window.AFKJ.config.TARGETING_DEFINITIONS[entry.key];out=chips.replaceOutsideChips(out,entry.re,function(match){return chips.chipSpan(def.emoji,match,def.cls);});});chips.ccFamilyChipKeys().forEach(function(key){const def=TAG_DEFINITIONS[key];const re=new RegExp("\\b"+key.replace(/[.*+?^${}()|[\]\\]/g,"\\$&")+"\\b","gi");out=chips.replaceOutsideChips(out,re,function(match){return chips.chipSpan(def.emoji,match,def.cls);});});const SKILL_DURATION_PATTERNS=[/\d+(?:\.\d+)?\s*\+\s*\d+(?:\.\d+)?\s*s\b/gi,/\d+(?:\.\d+)?\s*-\s*\d+(?:\.\d+)?\s*s\b/gi,/\d+(?:\.\d+)?\s*s\b/gi,];SKILL_DURATION_PATTERNS.forEach(function(re){out=chips.replaceOutsideChips(out,re,function(match){return('<span class="skill-inline-time">⏱️ '+
escapeHtml(match)+"</span>");});});if(opts.boldNumbers){out=chips.boldSkillNumericTokens(out);}
return out;}
function skillDetailPhases(card){const passive=(card.passive||"").trim();const active=(card.active||"").trim();const phases=[];if(passive){phases.push({label:"passive",body:passive});}
if(active){phases.push({label:"active",body:active});}
if(phases.length===0&&card.description){phases.push({label:"description",body:card.description});}
return phases;}
function formatSkillDetail(card){const title=card.name||card.label||"Skill";let headerHtml='<div class="skill-popover-header">'+'<button type="button" class="skill-popover-close" aria-label="Close">'+"×</button>"+'<h4 id="skill-popover-title" class="skill-popover-title">'+
escapeHtml(title)+"</h4>";if(card.unlock){headerHtml+='<p class="skill-popover-unlock">🔓 <em>'+
escapeHtml(card.unlock)+"</em></p>";}
const meta=card.meta||{};const metaItems=[];SKILL_META_ORDER.forEach(function(label){if(meta[label]){metaItems.push('<span class="skill-popover-meta-item">'+
SKILL_META_EMOJI[label]+" "+
escapeHtml(label)+": "+
escapeHtml(meta[label])+"</span>");}});if(metaItems.length){headerHtml+='<div class="skill-popover-meta">'+metaItems.join("")+"</div>";}
headerHtml+="</div>";let scrollHtml='<div class="skill-popover-scroll">';const phases=skillDetailPhases(card);if(phases.length){scrollHtml+='<div class="skill-popover-body">';phases.forEach(function(phase){if(phase.label==="passive"){scrollHtml+='<p class="skill-popover-phase">'+'<span class="skill-popover-phase-label">📖 <strong>Passive</strong></span> '+
enrichSkillInline(phase.body,{boldNumbers:true})+"</p>";}else if(phase.label==="active"){scrollHtml+='<p class="skill-popover-phase">'+'<span class="skill-popover-phase-label">⚡ <strong>Active</strong></span> '+
enrichSkillInline(phase.body,{boldNumbers:true})+"</p>";}else{scrollHtml+='<p class="skill-popover-phase">'+
enrichSkillInline(phase.body,{boldNumbers:true})+"</p>";}});scrollHtml+="</div>";}
const levels=card.levels||[];if(levels.length){scrollHtml+='<ul class="skill-popover-levels">';levels.forEach(function(level){const levelLabel=level.unlock?"Level "+level.level+" — "+level.unlock:"Level "+level.level;scrollHtml+="<li><span class=\"skill-popover-level-label\">🔼 "+
escapeHtml(levelLabel)+":</span> "+
enrichSkillInline(level.text||"",{boldNumbers:true})+"</li>";});scrollHtml+="</ul>";}
scrollHtml+="</div>";return headerHtml+scrollHtml;}
function skillCardData(category){const state=window.AFKJ.state;if(!state.detailHero||!state.detailHero.sections||!state.detailHero.sections.skillCards){return null;}
const cards=state.detailHero.sections.skillCards;for(let i=0;i<cards.length;i++){if(cards[i].category===category){return cards[i];}}
return null;}
function skillCardHexPoints(scale){const cx=50;const cy=57.5;const outer=[[50,3],[97,29.75],[97,85.25],[50,112],[3,85.25],[3,29.75],];return outer.map(function(point){const x=cx+(point[0]-cx)*scale;const y=cy+(point[1]-cy)*scale;return x+","+y;}).join(" ");}
function skillCardHexIcon(category){return SKILL_CARD_HEX_ICONS[category]||"";}
function renderSkillCardHex(category){const patternId="skill-hex-stripe-"+category;const outerPoints=skillCardHexPoints(1);const innerPoints=skillCardHexPoints(0.84);const icon=skillCardHexIcon(category);const iconHtml=icon?'<span class="skill-card-hex-icon" aria-hidden="true">'+
escapeHtml(icon)+"</span>":"";return('<div class="skill-card-hex" aria-hidden="true">'+'<svg class="skill-card-hex-svg" viewBox="-6 -6 112 127" preserveAspectRatio="xMidYMid meet">'+"<defs>"+'<pattern id="'+
patternId+'" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'+'<rect width="5" height="5" fill="var(--skill-card-hex-fill)"></rect>'+'<rect width="2.5" height="5" fill="var(--skill-card-hex-stripe)"></rect>'+"</pattern></defs>"+'<polygon class="skill-card-hex-fill" points="'+
outerPoints+'" fill="url(#'+
patternId+')"></polygon>'+'<polygon class="skill-card-hex-border-outer" points="'+
outerPoints+'"></polygon>'+'<polygon class="skill-card-hex-border-inner" points="'+
innerPoints+'"></polygon>'+"</svg>"+
iconHtml+"</div>");}
function renderSkillCards(cards,hero){if(!cards||!cards.length){return"";}
const factionKey=hero?utils.factionDataKey(hero.faction):"";const factionAttr=factionKey?' data-faction="'+escapeHtml(factionKey)+'"':"";let html='<div class="skill-card-grid">';cards.forEach(function(card){const tags=card.tags||card.effects||[];html+='<div class="skill-card" data-skill-category="'+
escapeHtml(card.category)+'"'+
factionAttr+' role="button" tabindex="0" aria-expanded="false" '+'aria-haspopup="dialog">';html+='<div class="skill-card-headline">';html+='<h4 class="skill-card-title">'+escapeHtml(card.label)+"</h4>";html+=renderSkillCardHex(card.category);html+="</div>";html+='<div class="skill-card-content">';if(card.summary){html+='<p class="skill-card-summary">'+
escapeHtml(card.summary)+"</p>";}
if(tags.length){html+='<div class="skill-card-tags">'+
chips.renderSkillCardTags(tags)+"</div>";}
html+="</div></div>";});html+="</div>";return html;}
function skillCardChipKey(raw){const text=skillCardTagLabel(raw);if(!text){return"";}
let tag=text.trim();if(!tag){return"";}
const tierMatch=tag.match(/\s*\((legendary\+|mythic\+|supreme\+|ex\+\d+)\)\s*$/i);let tierKey="";if(tierMatch){tierKey=":"+tierMatch[1].toLowerCase();tag=tag.slice(0,tierMatch.index).trim();}
const singleMatch=tag.match(/\s*(?:—|–)\s*single target\s*$/i);let singleKey="";if(singleMatch){singleKey=":single target";tag=tag.slice(0,singleMatch.index).trim();}
const areaMatch=tag.match(/\s*(?:—|–)\s*(area|arc|all units|multiple targets|path)\s*$/i);let areaKey="";if(areaMatch){areaKey=":"+areaMatch[1].trim().toLowerCase();tag=tag.slice(0,areaMatch.index).trim();}
let selfKey="";if(/\s*(?:—|–)\s*self\s*$/i.test(tag)){selfKey=":self";tag=tag.replace(/\s*(?:—|–)\s*self\s*$/i,"").trim();}
tag=tag.replace(/\s*(?:—|–)\s*(?:owned|summons?)\s*$/i,"").trim();tag=tag.toLowerCase();const targetingKey=selfKey||areaKey||singleKey;if(chips.isStatModifierLabel(tag)){return tag+targetingKey+tierKey;}
let i;for(i=0;i<chips.STAT_KEYS.length;i++){const stat=chips.STAT_KEYS[i].toLowerCase();if(tag===stat||tag.indexOf(stat+" ")===0){return stat+targetingKey+tierKey;}}
for(i=0;i<SKILL_CARD_DAMAGE_KEYS.length;i++){const dt=SKILL_CARD_DAMAGE_KEYS[i].toLowerCase();if(tag===dt||tag.indexOf(dt+" ")===0){return dt+tierKey;}}
for(i=0;i<SKILL_CARD_CC_KEYS.length;i++){const cc=SKILL_CARD_CC_KEYS[i].toLowerCase();if(tag===cc||tag.indexOf(cc+" ")===0){return cc;}}
if(tag==="hot"||tag==="healing over time"||tag.indexOf("healing over time")===0){return"hot"+targetingKey+tierKey;}
if(tag==="direct healing"||tag.indexOf("direct healing")===0){return"direct healing"+targetingKey+tierKey;}
if(tag.indexOf("healing")!==-1&&tag.indexOf("over time")===-1){return"direct healing"+targetingKey+tierKey;}
if(tag.indexOf("healing")!==-1&&tag.indexOf("over time")!==-1){return"hot"+targetingKey+tierKey;}
const base=tag.replace(/\s*\([^)]*\)/g,"").trim();return base+targetingKey+tierKey;}
function skillCardTagLabel(tag){if(typeof tag==="string"){return tag;}
return tag&&tag.label?tag.label:"";}
function renderSkillCardTags(tags){if(!tags||!tags.length){return"";}
const entries=[];tags.forEach(function(tag){const label=skillCardTagLabel(tag);if(!label){return;}
const polarity=typeof tag==="object"&&tag.polarity?tag.polarity:"";entries.push({label:label,polarity:polarity});});const grouped=chips.groupParsedVariants(entries.map(function(entry){return entry;}),function(entry){return chips.parseSkillCardVariant(entry.label,entry.polarity);},"");let html="";grouped.forEach(function(item){if(item.type==="group"){const pill=chips.renderGroupedVariantPill(item.variants,{iconOnlyTargeting:true,skillCardDisplay:true,});if(pill){html+=pill;}
return;}
const entry=item.item;const chip=chips.chipifySkillCardTag(entry.label,entry.polarity);if(chip){html+=chip;}});return html;}
window.AFKJ.skills={enrichSkillInline:enrichSkillInline,skillDetailPhases:skillDetailPhases,formatSkillDetail:formatSkillDetail,skillCardData:skillCardData,renderSkillCards:renderSkillCards,skillCardChipKey:skillCardChipKey,skillCardTagLabel:skillCardTagLabel,renderSkillCardTags:renderSkillCardTags,};window.AFKJ.chips.renderSkillCardTags=renderSkillCardTags;})();window.AFKJ=window.AFKJ||{};(function(){const config=window.AFKJ.config;const utils=window.AFKJ.utils;const escapeHtml=utils.escapeHtml.bind(utils);const FILTERS_COLLAPSE_MQ=window.matchMedia("(max-width: 600px)");function updateListStickyOffset(){const dom=window.AFKJ.state.dom;if(!dom.siteHeader){return;}
const offset=dom.siteHeader.offsetHeight;document.documentElement.style.setProperty("--list-sticky-top",offset+"px");if(dom.listView){dom.listView.style.setProperty("--list-sticky-offset",offset+"px");}}
function updateHeaderNav(inDetail){const state=window.AFKJ.state;const dom=state.dom;if(dom.filtersPanel){dom.filtersPanel.classList.toggle("hidden",inDetail||state.viewMode==="list");}
if(dom.headerBack){dom.headerBack.classList.toggle("hidden",!inDetail);}
updateListStickyOffset();}
function updateFiltersToggleLabel(){const state=window.AFKJ.state;const dom=state.dom;if(!dom.filtersToggle){return;}
const collapsed=dom.filtersPanel?dom.filtersPanel.classList.contains("filters-collapsed"):false;const parts=[];if(state.activeFaction){parts.push(state.activeFaction);}
if(state.activeClass){parts.push(state.activeClass);}
if(state.activeRole){const roleMeta=window.AFKJ.config.ROLE_CATEGORY_META[state.activeRole];parts.push(roleMeta?roleMeta.label:state.activeRole);}
const action=collapsed?"Show filters":"Hide filters";const activeSuffix=parts.length?" ("+parts.join(", ")+")":"";const label=action+activeSuffix;dom.filtersToggle.title=action;dom.filtersToggle.setAttribute("aria-label",label);if(dom.filtersToggleLabel){dom.filtersToggleLabel.textContent=label;}}
function setFiltersCollapsed(collapsed){const dom=window.AFKJ.state.dom;if(!dom.filtersPanel||!dom.filtersToggle){return;}
dom.filtersPanel.classList.toggle("filters-collapsed",collapsed);dom.filtersToggle.setAttribute("aria-expanded",collapsed?"false":"true");updateFiltersToggleLabel();updateListStickyOffset();}
function initFiltersCollapse(){const dom=window.AFKJ.state.dom;if(!dom.filtersPanel||!dom.filtersToggle){return;}
setFiltersCollapsed(FILTERS_COLLAPSE_MQ.matches);dom.filtersToggle.addEventListener("click",function(){setFiltersCollapsed(!dom.filtersPanel.classList.contains("filters-collapsed"));});FILTERS_COLLAPSE_MQ.addEventListener("change",function(){setFiltersCollapsed(FILTERS_COLLAPSE_MQ.matches);});}
function initWelcomeWarning(){const state=window.AFKJ.state;const dom=state.dom;const root=document.getElementById("welcome-warning");if(!root){return;}
if(localStorage.getItem(config.WELCOME_WARNING_KEY)==="1"){root.hidden=true;document.documentElement.classList.remove("welcome-warning-pending");return;}
const dismissBtn=document.getElementById("welcome-warning-dismiss");const blocked=[dom.siteHeader,document.getElementById("app"),document.querySelector(".site-footer"),].filter(Boolean);function setBlocked(block){root.classList.toggle("is-open",block);document.body.classList.toggle("welcome-warning-open",block);document.documentElement.classList.toggle("welcome-warning-pending",block);blocked.forEach(function(el){if(block){el.setAttribute("inert","");el.setAttribute("aria-hidden","true");}else{el.removeAttribute("inert");el.removeAttribute("aria-hidden");}});}
function blockSitePointer(e){if(root.hidden){return;}
if(root.contains(e.target)){return;}
e.preventDefault();e.stopPropagation();if(typeof e.stopImmediatePropagation==="function"){e.stopImmediatePropagation();}}
function dismissWelcomeWarning(){root.hidden=true;setBlocked(false);try{localStorage.setItem(config.WELCOME_WARNING_KEY,"1");}catch(e){}}
dismissBtn.addEventListener("click",dismissWelcomeWarning);["click","mousedown","touchstart"].forEach(function(type){document.addEventListener(type,blockSitePointer,true);});root.addEventListener("keydown",function(e){if(e.key==="Escape"){e.preventDefault();}
if(e.key==="Tab"){e.preventDefault();dismissBtn.focus();}});setBlocked(true);dismissBtn.focus();}
function initChipTooltips(){const TIP_CHIP_SELECTOR="[data-tip].chip-has-tip, [data-tip-html].chip-has-tip, .tier-chip[data-tip]";const chipTooltip=document.createElement("div");chipTooltip.id="chip-tooltip";chipTooltip.className="chip-tooltip";chipTooltip.hidden=true;chipTooltip.setAttribute("role","tooltip");document.body.appendChild(chipTooltip);let tipAnchor=null;let tipHideTimer=null;const hoverCapable=window.matchMedia("(hover: hover) and (pointer: fine)").matches;function tipChipFromEvent(e){return e.target.closest(TIP_CHIP_SELECTOR);}
function positionChipTooltip(anchor){const rect=anchor.getBoundingClientRect();chipTooltip.style.left=rect.left+rect.width/2+"px";chipTooltip.style.top=rect.top-8+"px";}
function showChipTooltip(anchor){const html=anchor.getAttribute("data-tip-html");const text=anchor.getAttribute("data-tip");if(!html&&!text){return;}
clearTimeout(tipHideTimer);if(tipAnchor&&tipAnchor!==anchor){tipAnchor.classList.remove("chip-tip-active");}
tipAnchor=anchor;anchor.classList.add("chip-tip-active");if(html){chipTooltip.innerHTML=html;chipTooltip.classList.add("chip-tooltip--html");}else{chipTooltip.textContent=text;chipTooltip.classList.remove("chip-tooltip--html");}
chipTooltip.hidden=false;positionChipTooltip(anchor);}
function hideChipTooltip(delay){clearTimeout(tipHideTimer);tipHideTimer=setTimeout(function(){if(tipAnchor){tipAnchor.classList.remove("chip-tip-active");}
chipTooltip.hidden=true;tipAnchor=null;},delay||0);}
if(hoverCapable){document.addEventListener("pointerover",function(e){if(e.pointerType!=="mouse"){return;}
const chip=tipChipFromEvent(e);if(chip){showChipTooltip(chip);}},true);document.addEventListener("pointerout",function(e){if(e.pointerType!=="mouse"){return;}
const chip=tipChipFromEvent(e);if(chip&&tipAnchor===chip&&!chip.contains(e.relatedTarget)){hideChipTooltip(100);}},true);}
document.addEventListener("keydown",function(e){const chip=tipChipFromEvent(e);if(!chip){return;}
if(e.key==="Escape"&&tipAnchor===chip){hideChipTooltip(0);chip.blur();return;}
if((e.key===" "||e.key==="Enter")&&!hoverCapable){e.preventDefault();if(tipAnchor===chip){hideChipTooltip(0);}else{showChipTooltip(chip);}}});document.addEventListener("click",function(e){const chip=tipChipFromEvent(e);if(!chip){if(tipAnchor){hideChipTooltip(0);}
return;}
const touchLike=e.pointerType==="touch"||!hoverCapable;if(!touchLike){return;}
e.stopPropagation();if(tipAnchor===chip){hideChipTooltip(0);}else{showChipTooltip(chip);}},true);document.addEventListener("focusin",function(e){const chip=tipChipFromEvent(e);if(chip){showChipTooltip(chip);}});document.addEventListener("focusout",function(e){const chip=tipChipFromEvent(e);if(chip&&tipAnchor===chip){hideChipTooltip(0);}});window.addEventListener("scroll",function(){if(tipAnchor&&!chipTooltip.hidden){positionChipTooltip(tipAnchor);}},true);window.addEventListener("resize",function(){if(tipAnchor&&!chipTooltip.hidden){positionChipTooltip(tipAnchor);}});}
function initSkillCardPopover(){const state=window.AFKJ.state;const popoverModule=window.AFKJ.skills;const backdrop=document.createElement("div");backdrop.className="skill-card-popover-backdrop";backdrop.hidden=true;const popover=document.createElement("div");popover.id="skill-card-popover";popover.className="skill-card-popover";popover.hidden=true;popover.setAttribute("role","dialog");popover.setAttribute("aria-modal","true");popover.setAttribute("aria-labelledby","skill-popover-title");document.body.appendChild(backdrop);document.body.appendChild(popover);let anchorCard=null;function setCardExpanded(card,expanded){if(!card){return;}
card.setAttribute("aria-expanded",expanded?"true":"false");card.classList.toggle("skill-card-active",expanded);}
function viewportMetrics(){const viewport=window.visualViewport;if(!viewport){return{top:0,left:0,width:window.innerWidth,height:window.innerHeight,};}
return{top:viewport.offsetTop,left:viewport.offsetLeft,width:viewport.width,height:viewport.height,};}
function clearPopoverLayout(){popover.style.top="";popover.style.left="";popover.style.width="";popover.style.height="";popover.style.maxHeight="";popover.style.visibility="";}
function positionSkillPopover(card){const cardRect=card.getBoundingClientRect();const offset=20;const viewMargin=8;const view=viewportMetrics();const isNarrow=view.width<=600;const heightCap=Math.min(view.height*(isNarrow?0.82:0.6),420);popover.style.maxHeight=heightCap+"px";popover.style.visibility="hidden";popover.hidden=false;const popW=popover.offsetWidth;const popH=popover.offsetHeight;const viewCenter=view.left+view.width/2;const cardCenter=cardRect.left+cardRect.width/2;const alignRight=cardCenter>=viewCenter;let left;let top=cardRect.bottom-offset-popH;if(alignRight){left=cardRect.right-offset-popW;}else{left=cardRect.left+offset;}
const maxLeft=view.left+view.width-popW-viewMargin;left=Math.max(view.left+viewMargin,Math.min(left,maxLeft));top=Math.max(view.top+viewMargin,Math.min(top,view.top+view.height-popH-viewMargin));popover.style.top=top+"px";popover.style.left=left+"px";popover.style.visibility="";}
function hideSkillPopover(){if(anchorCard){setCardExpanded(anchorCard,false);}
popover.hidden=true;backdrop.hidden=true;anchorCard=null;clearPopoverLayout();}
function showSkillPopover(card,cardData){if(!card||!cardData){return;}
if(anchorCard===card){hideSkillPopover();return;}
if(anchorCard){setCardExpanded(anchorCard,false);}
anchorCard=card;popover.innerHTML=popoverModule.formatSkillDetail(cardData);backdrop.hidden=false;popover.hidden=false;setCardExpanded(card,true);positionSkillPopover(card);}
state.closeSkillCardPopover=hideSkillPopover;popover.addEventListener("click",function(e){if(e.target.closest(".skill-popover-close")){e.stopPropagation();hideSkillPopover();}});function skillCardFromEvent(e){const chip=e.target.closest(".skill-card-tags .chip");if(chip){return null;}
return e.target.closest(".skill-card[data-skill-category]");}
function openFromCard(card){const data=popoverModule.skillCardData(card.dataset.skillCategory);if(!data){return;}
showSkillPopover(card,data);}
document.addEventListener("click",function(e){const card=skillCardFromEvent(e);if(card){e.preventDefault();e.stopPropagation();openFromCard(card);return;}
if(anchorCard&&!popover.contains(e.target)&&!anchorCard.contains(e.target)){hideSkillPopover();}});backdrop.addEventListener("click",function(){hideSkillPopover();});document.addEventListener("keydown",function(e){const card=e.target.closest(".skill-card[data-skill-category]");if(card&&(e.key==="Enter"||e.key===" ")&&!e.target.closest(".skill-card-tags .chip")){e.preventDefault();openFromCard(card);return;}
if(e.key==="Escape"&&anchorCard){hideSkillPopover();anchorCard.focus();}});window.addEventListener("scroll",function(){if(anchorCard&&!popover.hidden){positionSkillPopover(anchorCard);}},true);window.addEventListener("resize",function(){if(anchorCard&&!popover.hidden){positionSkillPopover(anchorCard);}});if(window.visualViewport){window.visualViewport.addEventListener("resize",function(){if(anchorCard&&!popover.hidden){positionSkillPopover(anchorCard);}});window.visualViewport.addEventListener("scroll",function(){if(anchorCard&&!popover.hidden){positionSkillPopover(anchorCard);}});}}
function initThemeToggle(){const theme=window.AFKJ.theme;const dom=window.AFKJ.state.dom;const input=dom.themeToggle;if(!input){return;}
theme.syncToggleControl(input);input.addEventListener("change",function(){const next=input.checked?"dark":"light";theme.applyThemeOverride(next);theme.syncToggleControl(input);});const colorMq=window.matchMedia("(prefers-color-scheme: dark)");colorMq.addEventListener("change",function(){if(!theme.readStoredThemeOverride()){theme.syncToggleControl(input);}});}
window.AFKJ.ui={updateListStickyOffset:updateListStickyOffset,updateHeaderNav:updateHeaderNav,updateFiltersToggleLabel:updateFiltersToggleLabel,setFiltersCollapsed:setFiltersCollapsed,initFiltersCollapse:initFiltersCollapse,initWelcomeWarning:initWelcomeWarning,initChipTooltips:initChipTooltips,initSkillCardPopover:initSkillCardPopover,initThemeToggle:initThemeToggle,};})();window.AFKJ=window.AFKJ||{};(function(){const utils=window.AFKJ.utils;const config=window.AFKJ.config;const escapeHtml=utils.escapeHtml.bind(utils);function renderHeroPortrait(hero,extraClass){const factionKey=utils.factionDataKey(hero.faction);const portraitSrc=utils.assetUrl(utils.characterPortraitPath(hero));return('<div class="hero-card-portrait hero-card-portrait--'+
escapeHtml(factionKey)+
(extraClass?" "+extraClass:"")+'">'+'<div class="hero-card-portrait-frame">'+'<img class="hero-card-character-portrait" src="'+
escapeHtml(portraitSrc)+'" alt="" loading="lazy" onerror="this.style.opacity=0.3">'+"</div></div>");}
function renderListHeroPortrait(hero){const factionKey=utils.factionDataKey(hero.faction);return('<span class="list-hero-hex" data-faction="'+
escapeHtml(factionKey)+'" aria-hidden="true">'+'<span class="list-hero-hex-wrap">'+
renderHeroPortrait(hero,"list-portrait")+"</span></span>");}
function renderGridCardFactionIcon(hero){if(!hero.faction){return"";}
const icon=utils.iconPath("factions",hero.faction);if(!icon){return"";}
return('<img class="hero-card-faction-icon" src="'+
utils.assetUrl(icon)+'" alt="'+
escapeHtml(hero.faction)+'" loading="lazy">');}
function renderGridCardClassIcon(hero){if(!hero.class){return"";}
const icon=utils.iconPath("class",hero.class);if(!icon){return"";}
return('<span class="hero-card-class-badge">'+'<img src="'+
utils.assetUrl(icon)+'" alt="'+
escapeHtml(hero.class)+'" loading="lazy">'+"</span>");}
function renderGridCardFactionStack(hero){const factionIcon=renderGridCardFactionIcon(hero);const classIcon=renderGridCardClassIcon(hero);if(!factionIcon&&!classIcon){return"";}
return('<div class="hero-card-faction-stack">'+
factionIcon+
classIcon+"</div>");}
function renderGridCardRole(hero){const meta=window.AFKJ.tiers.roleCategoryMeta(hero.roleCategory)||config.ROLE_CATEGORY_META[hero.roleCategory];if(!meta){return"";}
return('<span class="hero-card-role '+
meta.className+'">'+
escapeHtml(meta.label)+"</span>");}
function buildReferenceWavePath(options){const leftX=options.leftX;const rightX=options.rightX;const curveRightX=options.curveRightX!=null?options.curveRightX:rightX;const peakX=options.peakX;const troughX=options.troughX;const peakY=options.peakY;const troughY=options.troughY;const leftY=options.leftY;const endY=options.endY;const xShift=options.xShift||0;const xScale=options.xScale||1;const xAnchor=options.xAnchor!=null?options.xAnchor:50;const step=1.5;function mapX(x){const shifted=x+xShift;if(xScale===1){return shifted;}
return xAnchor+(shifted-xAnchor)*xScale;}
function edgeY(x){if(x<=peakX){const t=(x-leftX)/(peakX-leftX);return leftY+(peakY-leftY)*(1-Math.cos(Math.PI*t))/2;}
if(x<=troughX){const t=(x-peakX)/(troughX-peakX);return peakY+(troughY-peakY)*(1-Math.cos(Math.PI*t))/2;}
if(x>=curveRightX){return endY;}
const t=(x-troughX)/(curveRightX-troughX);return troughY-(troughY-endY)*(1-Math.cos(Math.PI*t))/2;}
function fmt(n){return(Math.round(n*100)/100).toString();}
let d="M"+fmt(mapX(leftX))+" "+fmt(edgeY(leftX));for(let x=leftX+step;x<rightX;x+=step){d+=" L"+fmt(mapX(x))+" "+fmt(edgeY(x));}
d+=" L"+fmt(mapX(rightX))+" "+fmt(edgeY(rightX));d+=" L"+fmt(mapX(rightX))+" 100 L"+fmt(mapX(leftX))+" 100 Z";return d;}
function heroCardWavePaths(){const panelPeakX=27;const panelTroughX=panelPeakX+(78-panelPeakX)*1.3;return{panelPath:buildReferenceWavePath({leftX:-15,rightX:115,peakX:panelPeakX,troughX:panelTroughX,peakY:10,troughY:28,leftY:23,endY:25,}),accentPath:buildReferenceWavePath({leftX:-22,rightX:125,curveRightX:130,peakX:40,troughX:95,peakY:1,troughY:19,leftY:9,endY:11,xShift:-20,}),};}
function renderHeroCardWave(patternId){const paths=heroCardWavePaths();const hatchId="hero-panel-hatch-"+patternId;return('<div class="hero-card-wave" aria-hidden="true">'+'<svg class="hero-card-wave-svg" viewBox="0 0 100 100" preserveAspectRatio="none">'+"<defs>"+'<pattern id="'+
hatchId+'" width="3" height="3" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)">'+'<rect width="3" height="0.4" y="2.4" fill="var(--fc-hatch)"></rect>'+"</pattern></defs>"+'<path class="hero-card-wave-accent" d="'+
paths.accentPath+'"></path>'+'<path class="hero-card-wave-panel" d="'+
paths.panelPath+'"></path>'+'<path class="hero-card-wave-panel-hatch" d="'+
paths.panelPath+'" fill="url(#'+
hatchId+')"></path></svg></div>');}
function renderCompactCardWave(patternId){const paths=heroCardWavePaths();const hatchId="hero-compact-hatch-"+patternId;return('<div class="hero-compact-wave" aria-hidden="true">'+'<svg class="hero-compact-wave-svg" viewBox="0 0 100 100" preserveAspectRatio="none">'+"<defs>"+'<pattern id="'+
hatchId+'" width="3" height="3" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)">'+'<rect width="3" height="0.4" y="2.4" fill="var(--compact-wave-hatch)"></rect>'+"</pattern></defs>"+'<g transform="translate(40 100) scale(2 1) rotate(-90)">'+'<path class="hero-compact-wave-accent" d="'+
paths.accentPath+'"></path>'+'<path class="hero-compact-wave-panel" d="'+
paths.panelPath+'"></path>'+'<path class="hero-compact-wave-panel-hatch" d="'+
paths.panelPath+'" fill="url(#'+
hatchId+')"></path></g></svg></div>');}
const HERO_CARD_NAME_BASE_CQI=13.5;const HERO_CARD_NAME_NARROW_CHARS={i:0.3,l:0.3,I:0.3,j:0.5,t:0.5,};function heroCardNameWordVisibleLength(word){let visible=0;for(let i=0;i<word.length;i++){visible+=HERO_CARD_NAME_NARROW_CHARS[word[i]]??1;}
return visible;}
function heroCardNameVisibleLength(text){const words=text.trim().split(/\s+/).filter(Boolean);if(!words.length){return 0;}
const visibleLengths=words.map(heroCardNameWordVisibleLength);visibleLengths.forEach(function(_,index){if(words[index].length===1&&index>0){visibleLengths[index]+=visibleLengths[index-1]+1;}});return Math.max.apply(null,visibleLengths);}
function fitHeroCardName(h2){const text=h2.textContent||"";if(text.length<7){return;}
const visibleLength=heroCardNameVisibleLength(text);if(visibleLength<7){return;}
const reduction=(visibleLength-7)*2.2;h2.style.fontSize="calc("+HERO_CARD_NAME_BASE_CQI+"cqi - "+reduction+"cqi)";}
function fitHeroCardNames(){const state=window.AFKJ.state;if(state.viewMode==="mix"){const roots=[];if(state.dom.mixHeroGrid){roots.push(state.dom.mixHeroGrid);}
if(state.dom.mixDropZone){roots.push(state.dom.mixDropZone);}
roots.forEach(function(root){root.querySelectorAll(".hero-card-name h2").forEach(fitHeroCardName);});return;}
if(state.viewMode==="grid"&&state.dom.heroGrid){state.dom.heroGrid.querySelectorAll(".hero-card-name h2").forEach(fitHeroCardName);}}
function scheduleFitHeroCardNames(){const run=fitHeroCardNames;if(document.fonts&&document.fonts.ready){document.fonts.ready.then(run).catch(run);}else{run();}}
function buildHeroCardHtml(h,opts){opts=opts||{};const factionKey=utils.factionDataKey(h.faction);let extraClass=opts.extraClass||"";if(opts.marked){extraClass+=" hero-card--mix-marked";}
const dragAttr=opts.draggable?' draggable="true"':"";const sourceAttr=opts.mixSource?' data-mix-source="'+escapeHtml(opts.mixSource)+'"':"";const roleAttr=opts.role?' role="'+escapeHtml(opts.role)+'"':"";const cardHtml='<article class="hero-card afkj-box afkj-box-sm'+
extraClass+'" data-slug="'+
escapeHtml(h.slug)+'" data-faction="'+
escapeHtml(factionKey)+'"'+
dragAttr+
sourceAttr+
roleAttr+' tabindex="0" aria-label="'+
escapeHtml(h.name)+'">'+
renderHeroPortrait(h)+
renderHeroCardWave(h.slug)+'<div class="hero-card-info">'+'<div class="hero-card-name"><h2>'+
escapeHtml(h.name)+"</h2></div>"+'<div class="hero-card-meta">'+
renderGridCardRole(h)+"</div></div>"+
renderGridCardFactionStack(h)+"</article>";if(opts.chromeHtml){return('<div class="hero-card-wrapper'+
(opts.marked?" hero-card-wrapper--mix-marked":"")+'">'+
cardHtml+
opts.chromeHtml+"</div>");}
return cardHtml;}
function renderGrid(){const state=window.AFKJ.state;const list=window.AFKJ.router.filteredHeroes();state.dom.heroGrid.innerHTML=list.map(function(h){return buildHeroCardHtml(h,{role:"link"});}).join("");state.dom.emptyState.classList.toggle("hidden",list.length>0);scheduleFitHeroCardNames();}
window.AFKJ.views.grid={renderHeroPortrait:renderHeroPortrait,renderListHeroPortrait:renderListHeroPortrait,renderGridCardFactionIcon:renderGridCardFactionIcon,renderGridCardClassIcon:renderGridCardClassIcon,renderGridCardFactionStack:renderGridCardFactionStack,renderGridCardRole:renderGridCardRole,renderHeroCardWave:renderHeroCardWave,renderCompactCardWave:renderCompactCardWave,buildHeroCardHtml:buildHeroCardHtml,scheduleFitHeroCardNames:scheduleFitHeroCardNames,renderGrid:renderGrid,};})();window.AFKJ=window.AFKJ||{};(function(){const utils=window.AFKJ.utils;const config=window.AFKJ.config;const chips=window.AFKJ.chips;const gridView=window.AFKJ.views.grid;const escapeHtml=utils.escapeHtml.bind(utils);const EFFECT_CC_COLUMNS=["Stun","Knock down","Knock up","Knock back","Frighten","Silence","Charm","Sleep","Displace","Bind","Interrupt","Taunt","Blind",];const EFFECT_ANTI_CC_COLUMNS=["Unaffected","Steadfast","Immune","Untargetable","Cleanse",];const TIMING_RANK={permanent:50,"start of battle":40,form:35,"on ultimate":30,"on skill":25,once:20,"conditional (frequent)":15,conditional:10,"conditional (rare)":5,};const STRENGTH_RANK={high:3,average:2,low:1,};const DMG_COLUMN_BASE={Magic:"Magic",Physical:"Physical",Ranged:"Ranged",True:"True damage","HP Loss":"HP loss","Max HP":"Max HP damage",};let columnFilterPointerHandler=null;function parseCsv(text){const rows=[];let row=[];let field="";let inQuotes=false;for(let i=0;i<text.length;i++){const c=text[i];if(inQuotes){if(c==='"'){if(text[i+1]==='"'){field+='"';i++;}else{inQuotes=false;}}else{field+=c;}}else if(c==='"'){inQuotes=true;}else if(c===","){row.push(field);field="";}else if(c==="\n"||(c==="\r"&&text[i+1]==="\n")){row.push(field);if(row.some(function(cell){return cell.length>0;})){rows.push(row);}
row=[];field="";if(c==="\r"){i++;}}else if(c!=="\r"){field+=c;}}
if(field.length||row.length){row.push(field);rows.push(row);}
return rows;}
function listColumnMeta(columnId){const state=window.AFKJ.state;return state.listColumnsById[columnId]||null;}
function listColumnDisplayLabel(columnId){const meta=listColumnMeta(columnId);return meta?meta.label:columnId;}
function parseEffectColumnLabel(column){const meta=listColumnMeta(column);if(meta){return{base:meta.label,polarity:meta.polarity,tier:"",};}
if(column.endsWith(" DMG")){const short=column.slice(0,-4);return{base:DMG_COLUMN_BASE[short]||short,polarity:"damage",tier:"",};}
const parsed=chips.parseEffectLabelParts(column);return{base:parsed.base,polarity:null,tier:parsed.tier,};}
function isTimingSegment(segment){const lower=segment.trim().toLowerCase();if(Object.prototype.hasOwnProperty.call(TIMING_RANK,lower)){return true;}
if(lower.indexOf("start of battle")!==-1){return true;}
if(lower.indexOf("on ultimate")!==-1){return true;}
if(lower.indexOf("on skill")!==-1){return true;}
if(lower.indexOf("permanent")!==-1){return true;}
return false;}
function parseEffectCellPart(text){const segments=chips.splitSummarySegments(text);let quality="";let conditional="";let timing="";function popTrailingQuality(){if(!segments.length){return;}
const last=chips.unwrapBackticks(segments[segments.length-1]);const lower=last.toLowerCase();if(chips.QUALITY_CLASS[lower]){quality=last;segments.pop();}}
function popTrailingConditional(){if(!segments.length){return;}
const last=segments[segments.length-1];if(/conditional/i.test(last)){conditional=last;segments.pop();}}
function popTrailingTiming(){if(!segments.length){return;}
const last=segments[segments.length-1];if(isTimingSegment(last)){timing=last;segments.pop();}}
popTrailingConditional();popTrailingQuality();popTrailingConditional();popTrailingTiming();const targeting=segments.join(" — ");return{targeting:targeting,quality:quality,conditional:conditional,timing:timing,};}
function renderEffectConditionalChip(conditionalText){if(!conditionalText){return"";}
const condMatch=conditionalText.match(/conditional\s*\(([^)]+)\)/i);if(condMatch){return"";}
return(' <span class="chip chip-generic chip-has-tip"'+
chips.chipTipAttrs(chips.conditionalTooltip(conditionalText))+">🎲 "+
escapeHtml(conditionalText)+"</span>");}
function renderEffectCellPart(column,text){if(!text||!text.trim()){return"";}
const colMeta=parseEffectColumnLabel(column);const parsed=parseEffectCellPart(text.trim());let conditionalParam="";if(parsed.conditional){const condMatch=parsed.conditional.match(/conditional\s*\(([^)]+)\)/i);if(condMatch){conditionalParam=condMatch[1].trim();}}
let html=chips.renderMergedEffectPill(colMeta.base,parsed.quality,colMeta.tier||"",conditionalParam,colMeta.polarity);if(parsed.targeting){html+=" "+chips.renderBuffTargetingChip(parsed.targeting);}
if(parsed.timing){const timingChip=chips.tryChipify(parsed.timing);html+=" "+
(timingChip!==null?timingChip:chips.formatTag(parsed.timing));}
html+=renderEffectConditionalChip(parsed.conditional);return html;}
function getListCellRawValue(row,colIdx,col){const state=window.AFKJ.state;const tiers=window.AFKJ.tiers;let cellValue=row[colIdx]||"";const hero=state.heroByName[row[0]||""];if(col==="Role"&&!String(cellValue||"").trim()&&hero){const roleMeta=tiers.roleCategoryMeta(hero.roleCategory);if(roleMeta){cellValue=roleMeta.label;}}
if(hero&&tiers.TIER_CSV_HEADERS[col]&&!String(cellValue||"").trim()){const tierCol=tiers.TIER_CSV_COLUMNS.find(function(t){return t.header===col;});if(tierCol){cellValue=tiers.getHeroPrydwenTiers(hero)[tierCol.key]||"?";}}
return String(cellValue||"").trim();}
const FILTER_GROUP_META=[{id:"targeting",label:"Targeting"},{id:"quality",label:"Magnitude"},{id:"timing",label:"Timing"},{id:"conditional",label:"Conditional"},{id:"other",label:"Other"},];function classifyFilterAtom(value){const trimmed=(value||"").trim();if(!trimmed){return"other";}
const lower=trimmed.toLowerCase();if(chips.QUALITY_CLASS[lower]){return"quality";}
if(chips.SPEED_CLASS[lower]){return"quality";}
if(/conditional/i.test(trimmed)){return"conditional";}
if(config.TARGETING_DEFINITIONS[lower]){return"targeting";}
if(isTimingSegment(trimmed)){return"timing";}
return"other";}
function splitSelectedByFilterGroup(selected){const groups={};selected.forEach(function(value){const kind=classifyFilterAtom(value);if(!groups[kind]){groups[kind]=new Set();}
groups[kind].add(value);});return groups;}
function atomSetMatchesGroupedSelection(atomSet,selectedByGroup){const normalized={};atomSet.forEach(function(atom){normalized[atom.toLowerCase()]=atom;});return FILTER_GROUP_META.every(function(meta){const groupSelected=selectedByGroup[meta.id];if(!groupSelected||!groupSelected.size){return true;}
let groupMatched=false;groupSelected.forEach(function(value){if(normalized[value.toLowerCase()]){groupMatched=true;}});return groupMatched;});}
function sortFilterOptionValues(values,column){const isTier=window.AFKJ.tiers.TIER_CSV_HEADERS[column];const isRole=column==="Role";if(isTier){return values.slice().sort(function(a,b){return tierFilterSortRank(a)-tierFilterSortRank(b);});}
if(isRole){return values.slice().sort(function(a,b){const metaA=window.AFKJ.tiers.roleCategoryMeta(a)||config.ROLE_CATEGORY_META[a];const metaB=window.AFKJ.tiers.roleCategoryMeta(b)||config.ROLE_CATEGORY_META[b];const rankA=metaA?config.ROLE_FILTER_ORDER.indexOf(a):99;const rankB=metaB?config.ROLE_FILTER_ORDER.indexOf(b):99;return rankA-rankB;});}
return values.slice().sort();}
function tierFilterSortRank(value){const idx=window.AFKJ.tiers.TIER_FILTER_ORDER.indexOf(value);return idx>=0?idx:99;}
function buildEffectColumnFilterGroups(col,idx){const state=window.AFKJ.state;const byGroup={};state.csvRows.forEach(function(row){const raw=getListCellRawValue(row,idx,col);if(!raw){return;}
extractCellFilterAtoms(col,raw).forEach(function(v){const kind=classifyFilterAtom(v);if(!byGroup[kind]){byGroup[kind]=new Set();}
byGroup[kind].add(v);});});return FILTER_GROUP_META.map(function(meta){const values=byGroup[meta.id];return{id:meta.id,label:meta.label,values:values?sortFilterOptionValues(Array.from(values)):[],};}).filter(function(group){return group.values.length;});}
function filterOptionGroupsHasChoices(groups){return groups.some(function(group){return group.values&&group.values.length;});}
function columnFilterCombineMode(colIdx){return window.AFKJ.state.csvColumnFilterCombine[colIdx]||"or";}
function toggleColumnFilterCombine(colIdx){const state=window.AFKJ.state;if(columnFilterCombineMode(colIdx)==="and"){delete state.csvColumnFilterCombine[colIdx];}else{state.csvColumnFilterCombine[colIdx]="and";}
renderList();}
function atomsFromEffectEntry(entry){const atoms=new Set();const trimmed=entry.trim();if(!trimmed){return atoms;}
const parsed=parseEffectCellPart(trimmed);if(parsed.targeting){parsed.targeting.split(/\s*,\s*/).forEach(function(token){const t=token.trim();if(t){atoms.add(t);}});}
if(parsed.quality){atoms.add(parsed.quality);}
if(parsed.conditional){atoms.add(parsed.conditional);}
if(parsed.timing){atoms.add(parsed.timing);}
return atoms;}
function renderBehaviorTagsCell(value){const parts=String(value||"").split(/\s*;\s*/).filter(function(part){return part.trim();});if(!parts.length){return"";}
return('<span class="behavior-tags-cell">'+
parts.map(function(tag){return chips.behaviorTagChip(tag);}).join(" ")+"</span>");}
function extractCellFilterAtoms(column,cellValue){const values=new Set();const raw=String(cellValue||"").trim();if(!raw){return values;}
if(column==="Behavior tags"){raw.split(/\s*;\s*/).forEach(function(tag){const trimmed=tag.trim();if(trimmed){values.add(trimmed);}});return values;}
if(isEffectSortColumn(column)){raw.split(/\s*;\s*/).forEach(function(entry){atomsFromEffectEntry(entry).forEach(function(atom){values.add(atom);});});return values;}
values.add(raw);return values;}
function effectEntryAtomSets(cellValue){const raw=String(cellValue||"").trim();if(!raw){return[];}
return raw.split(/\s*;\s*/).map(function(entry){return atomsFromEffectEntry(entry);});}
function buildColumnFilterOptions(){const state=window.AFKJ.state;const filterOptions=[];state.csvHeaders.forEach(function(col,idx){if(idx===0){filterOptions.push([]);return;}
if(isEffectSortColumn(col)){filterOptions.push(buildEffectColumnFilterGroups(col,idx));return;}
const vals=new Set();state.csvRows.forEach(function(row){const raw=getListCellRawValue(row,idx,col);if(!raw)return;const atoms=extractCellFilterAtoms(col,raw);atoms.forEach(vals.add,vals);});const uniqueVals=Array.from(vals);filterOptions.push([{id:"value",label:"",values:sortFilterOptionValues(uniqueVals,col),},]);});state.csvColumnFilterOptions=filterOptions;}
function cellMatchesColumnFilter(column,cellValue,selected,combineMode){if(selected.length===0){return true;}
const rawVal=(cellValue||"").trim();if(!rawVal){return false;}
if(isEffectSortColumn(column)){const selectedByGroup=splitSelectedByFilterGroup(selected);const entrySets=effectEntryAtomSets(rawVal);return entrySets.some(function(atomSet){return atomSetMatchesGroupedSelection(atomSet,selectedByGroup);});}
const atoms=extractCellFilterAtoms(column,rawVal);const mode=combineMode==="and"?"and":"or";if(mode==="and"){return selected.every(function(value){return atoms.has(value);});}
return selected.some(function(value){return atoms.has(value);});}
function rowMatchesColumnFilters(row){const state=window.AFKJ.state;for(let i=1;i<state.csvHeaders.length;i++){const col=state.csvHeaders[i];const selected=state.csvColumnFilters[i]||[];if(selected.length>0){const combine=columnFilterCombineMode(i);const cellValue=row[i];if(!cellMatchesColumnFilter(col,cellValue,selected,combine)){return false;}}}
return true;}
function filterOptionIconHtml(column,value){const trimmed=(value||"").trim();if(!trimmed){return"";}
const lower=trimmed.toLowerCase();if(column==="Faction"){const icon=utils.iconPath("factions",value);if(icon){return('<img class="col-filter-opt-icon" src="'+
utils.assetUrl(icon)+'" alt="">');}}
if(column==="Class"){const icon=utils.iconPath("class",value);if(icon){return('<img class="col-filter-opt-icon" src="'+
utils.assetUrl(icon)+'" alt="">');}}
if(column==="Role"){const roleKey=Object.keys(config.ROLE_CATEGORY_META).find(function(key){return config.ROLE_CATEGORY_META[key].label.toLowerCase()===lower;});if(roleKey){return('<span class="col-filter-opt-emoji" aria-hidden="true">'+
config.ROLE_CATEGORY_META[roleKey].emoji+"</span>");}}
for(let i=0;i<chips.MOVEMENT_KEYS.length;i++){const key=chips.MOVEMENT_KEYS[i];if(lower===key.toLowerCase()){return('<span class="col-filter-opt-emoji" aria-hidden="true">'+
chips.MOVEMENT_DEFINITIONS[key].emoji+"</span>");}}
if(chips.SPEED_CLASS[lower]){const emoji=chips.SPEED_EMOJI[lower]||"⏱️";return('<span class="col-filter-opt-emoji" aria-hidden="true">'+
emoji+"</span>");}
if(chips.QUALITY_CLASS[lower]){const emoji=chips.QUALITY_EMOJI[lower]||"";return('<span class="col-filter-opt-emoji" aria-hidden="true">'+
emoji+"</span>");}
const targeting=config.TARGETING_DEFINITIONS[lower];if(targeting){return('<span class="col-filter-opt-emoji" aria-hidden="true">'+
targeting.emoji+"</span>");}
if(isTimingSegment(trimmed)){return'<span class="col-filter-opt-emoji" aria-hidden="true">⏱️</span>';}
const tagKey=chips.exactTagDefinitionKey(trimmed);if(tagKey){const def=config.TAG_DEFINITIONS[tagKey];return('<span class="col-filter-opt-emoji" aria-hidden="true">'+
def.emoji+"</span>");}
return"";}
function renderColumnFilterPanel(colIdx,column,optionGroups){if(!filterOptionGroupsHasChoices(optionGroups)){return"";}
const state=window.AFKJ.state;const selected=state.csvColumnFilters[colIdx]||[];const selectedSet=new Set(selected);const visibleGroups=optionGroups.filter(function(group){return group.values&&group.values.length;});const showGroupLabels=visibleGroups.length>1;let html='<div class="col-filter-panel" role="group" aria-label="Filter column">';visibleGroups.forEach(function(group,groupIdx){if(showGroupLabels&&group.label){if(groupIdx>0){html+='<div class="col-filter-group-sep" role="separator"></div>';}
html+='<div class="col-filter-group-label">'+
escapeHtml(group.label)+"</div>";}else if(groupIdx>0){html+='<div class="col-filter-group-sep" role="separator"></div>';}
group.values.forEach(function(value){const checked=selectedSet.has(value)?" checked":"";const iconHtml=filterOptionIconHtml(column,value);html+='<label class="col-filter-option">'+'<input type="checkbox" class="col-filter-cb" data-col="'+
colIdx+'" data-group="'+
escapeHtml(group.id)+'" value="'+
escapeHtml(value)+'"'+
checked+">"+'<span class="col-filter-option-body">'+
(iconHtml?'<span class="col-filter-option-icon">'+iconHtml+"</span>":"")+'<span class="col-filter-option-text">'+
escapeHtml(value)+"</span>"+"</span></label>";});});if(selected.length){html+='<button type="button" class="col-filter-clear" data-col="'+
colIdx+'">Clear</button>';}
html+="</div>";return html;}
function renderColumnFilterCombineToggle(colIdx,column){if(column!=="Behavior tags"){return"";}
const mode=columnFilterCombineMode(colIdx);const combineTitle=mode==="and"?"Match all selected tags (and). Click to match any (or).":"Match any selected tag (or). Click to match all (and).";return('<button type="button" class="col-filter-combine-toggle" data-col="'+
colIdx+'" aria-label="Combine filter selections" title="'+
escapeHtml(combineTitle)+'">'+'<span class="col-filter-combine-seg'+
(mode==="or"?" active":"")+'">or</span>'+'<span class="col-filter-combine-seg'+
(mode==="and"?" active":"")+'">and</span>'+"</button>");}
function renderBadgeChip(label,kind){if(!label){return"";}
if(kind==="faction"){const icon=utils.iconPath("factions",label);return('<span class="badge '+
utils.factionClass(label)+'">'+
(icon?'<img src="'+
utils.assetUrl(icon)+'" alt="" loading="lazy">':"")+
escapeHtml(label)+"</span>");}
if(kind==="class"){const icon=utils.iconPath("class",label);return('<span class="badge">'+
(icon?'<img src="'+
utils.assetUrl(icon)+'" alt="" loading="lazy">':"")+
escapeHtml(label)+"</span>");}
return'<span class="badge">'+escapeHtml(label)+"</span>";}
function formatMovementChip(text){const trimmed=text.trim();if(!trimmed){return null;}
const lower=trimmed.toLowerCase();for(let i=0;i<chips.MOVEMENT_KEYS.length;i++){const key=chips.MOVEMENT_KEYS[i];if(lower===key.toLowerCase()){const def=chips.MOVEMENT_DEFINITIONS[key];return chips.chipSpan(def.emoji,trimmed,def.cls);}}
return null;}
function renderTableCell(column,value){const rawVal=(value||"").trim();if(!rawVal){return"";}
if(column==="Hero"){const state=window.AFKJ.state;const hero=state.heroByName[rawVal];return utils.linkifyHero(rawVal,hero?hero.slug:null);}
if(column==="Faction"){return renderBadgeChip(rawVal,"faction");}
if(column==="Class"){return renderBadgeChip(rawVal,"class");}
if(column==="Role"){const roleKey=Object.keys(config.ROLE_CATEGORY_META).find(function(key){return config.ROLE_CATEGORY_META[key].label.toLowerCase()===rawVal.toLowerCase();});if(roleKey){return window.AFKJ.views.detail.renderRoleCategoryBadge(roleKey);}
return escapeHtml(rawVal);}
if(column==="Signature skill speed"||column==="Non-ultimate speed"){return chips.formatTag(rawVal);}
if(column==="DoT"||column==="HoT"||column==="Summons"||column==="Energy provider"){if(rawVal.toLowerCase()==="yes"){return'<span class="chip chip-generic">✓ yes</span>';}
return escapeHtml(rawVal);}
if(column==="Movement"){const chip=formatMovementChip(rawVal);if(chip!==null){return chip;}
return('<span class="chip chip-movement">🚶 '+
escapeHtml(rawVal)+"</span>");}
if(window.AFKJ.tiers.TIER_CSV_HEADERS[column]){return window.AFKJ.tiers.renderTierTableCell(rawVal);}
if(column==="Behavior tags"){return renderBehaviorTagsCell(rawVal);}
if(isEffectSortColumn(column)){const parts=rawVal.split(/\s*;\s*/).filter(function(part){return part.trim();});if(!parts.length){return"";}
return('<span class="effect-cell-stack">'+
parts.map(function(part){return('<span class="effect-cell-entry">'+
renderEffectCellPart(column,part)+"</span>");}).join("")+"</span>");}
return rawVal.split(/\s*;\s*/).map(function(part){return renderTableEntry(part.trim());}).join(" ");}
function renderTableEntry(text){if(/\s*(?:—|–)\s*/.test(text)){return chips.renderRichLine(text);}
return text.split(/\s*,\s*/).map(function(part){const chip=chips.tryChipify(part.trim());return chip!==null?chip:escapeHtml(part.trim());}).join(" ");}
function isDmgColumn(column){return!!column&&column.endsWith(" DMG");}
function isEffectSortColumn(column){if(!column){return false;}
if(isDmgColumn(column)){return true;}
if(column==="Healing"||column==="Shields"){return true;}
if(listColumnMeta(column)){return true;}
if(EFFECT_CC_COLUMNS.indexOf(column)!==-1){return true;}
if(EFFECT_ANTI_CC_COLUMNS.indexOf(column)!==-1){return true;}
return false;}
function listColumnClass(col){const tiers=window.AFKJ.tiers;if(col==="Name"){return"col-name";}
if(col==="Faction"){return"col-faction";}
if(col==="Class"){return"col-class";}
if(col==="Role"){return"col-role";}
if(tiers.TIER_CSV_HEADERS[col]){return"col-tier";}
if(col==="Movement"){return"col-movement";}
if(col==="Behavior tags"){return"col-behavior-tags";}
if(isEffectSortColumn(col)){return"col-effect-stack";}
return"col-general";}
function targetingRank(text){const trimmed=text.trim();if(!trimmed){return 0;}
const lower=trimmed.toLowerCase();if(Object.prototype.hasOwnProperty.call(TARGETING_RANK,lower)){return TARGETING_RANK[lower];}
if(trimmed.indexOf(",")!==-1){return trimmed.split(/\s*,\s*/).reduce(function(max,part){return Math.max(max,targetingRank(part));},0);}
return 0;}
function timingRank(text){const lower=text.trim().toLowerCase();if(Object.prototype.hasOwnProperty.call(TIMING_RANK,lower)){return TIMING_RANK[lower];}
if(lower.indexOf("conditional (frequent)")!==-1){return TIMING_RANK["conditional (frequent)"];}
if(lower.indexOf("conditional (rare)")!==-1){return TIMING_RANK["conditional (rare)"];}
if(lower.indexOf("start of battle")!==-1){return TIMING_RANK["start of battle"];}
if(lower.indexOf("on ultimate")!==-1){return TIMING_RANK["on ultimate"];}
if(lower.indexOf("on skill")!==-1){return TIMING_RANK["on skill"];}
if(lower.indexOf("permanent")!==-1){return TIMING_RANK.permanent;}
return 0;}
function parseEffectEntry(entry){const cellMeta=parseEffectCellPart(entry);if(!cellMeta){return{label:entry,targetRank:0,timeRank:0,strengthRank:0};}
return{label:cellMeta.label,targetRank:targetingRank(cellMeta.timing),timeRank:timingRank(cellMeta.timing),strengthRank:STRENGTH_RANK[cellMeta.quality.toLowerCase()]||0,};}
function effectSortKey(cellValue){const trimmed=(cellValue||"").trim();if(!trimmed){return null;}
const parts=trimmed.split(/\s*;\s*/).map(function(s){return s.trim();}).filter(Boolean);const parsed=parts.map(parseEffectEntry);parsed.sort(compareEffectSortKeys);return parsed[0]||null;}
function compareEffectSortKeys(ka,kb){if(ka.strengthRank!==kb.strengthRank){return kb.strengthRank-ka.strengthRank;}
if(ka.targetRank!==kb.targetRank){return kb.targetRank-ka.targetRank;}
if(ka.timeRank!==kb.timeRank){return kb.timeRank-ka.timeRank;}
return ka.label.localeCompare(kb.label);}
function compareEffectCells(av,bv){const ka=effectSortKey(av);const kb=effectSortKey(bv);if(ka===null&&kb===null){return 0;}
if(ka===null){return 1;}
if(kb===null){return-1;}
return compareEffectSortKeys(ka,kb);}
function compareCsvRows(a,b){const state=window.AFKJ.state;const idx=state.sortColumn;const col=state.csvHeaders[idx];const av=a[idx];const bv=b[idx];if(isEffectSortColumn(col)){return compareEffectCells(av,bv)*state.sortDir;}
if(window.AFKJ.tiers.TIER_CSV_HEADERS[col]){const rankA=window.AFKJ.tiers.prydwenTierRank(av);const rankB=window.AFKJ.tiers.prydwenTierRank(bv);if(rankA!==rankB){return(rankB-rankA)*state.sortDir;}}
const sA=String(av||"").trim();const sB=String(bv||"").trim();const numA=Number(sA);const numB=Number(sB);if(!isNaN(numA)&&!isNaN(numB)){return(numA-numB)*state.sortDir;}
return sA.localeCompare(sB)*state.sortDir;}
function getTableScrollEl(){const state=window.AFKJ.state;return state.dom.listView?state.dom.listView.querySelector(".table-scroll"):null;}
function clearColumnFilterPanelPosition(details){if(!details){return;}
const panel=details.querySelector(".col-filter-panel");if(!panel){return;}
panel.classList.remove("is-floating");panel.style.top="";panel.style.left="";panel.style.minWidth="";panel.style.maxWidth="";}
function positionOpenColumnFilter(){const state=window.AFKJ.state;if(state.openColumnFilter<0||!state.dom.heroesTableHead){return;}
state.dom.heroesTableHead.querySelectorAll("details.col-filter[open]").forEach(function(details){if(parseInt(details.dataset.col,10)!==state.openColumnFilter){clearColumnFilterPanelPosition(details);}});const details=getOpenColumnFilterDetails();if(!details||!details.open){return;}
const panel=details.querySelector(".col-filter-panel");const trigger=details.querySelector(".col-filter-trigger");if(!panel||!trigger){return;}
const rect=trigger.getBoundingClientRect();panel.classList.add("is-floating");panel.style.top=Math.round(rect.bottom+2)+"px";panel.style.left=Math.round(rect.left)+"px";panel.style.minWidth=Math.round(rect.width)+"px";panel.style.maxWidth="16rem";}
function getOpenColumnFilterDetails(){const state=window.AFKJ.state;if(state.openColumnFilter<0||!state.dom.heroesTableHead){return null;}
return state.dom.heroesTableHead.querySelector('details.col-filter[data-col="'+state.openColumnFilter+'"]');}
function isPointerInColumnFilterZone(clientX,clientY){const details=getOpenColumnFilterDetails();if(!details){return false;}
const trigger=details.querySelector(".col-filter-trigger");const panel=details.querySelector(".col-filter-panel");const pad=6;if(trigger&&utils.rectContainsPoint(trigger.getBoundingClientRect(),clientX,clientY,pad)){return true;}
if(panel&&utils.rectContainsPoint(panel.getBoundingClientRect(),clientX,clientY,pad)){return true;}
return false;}
function unbindColumnFilterPointerTracking(){if(columnFilterPointerHandler){document.removeEventListener("pointerdown",columnFilterPointerHandler,true);columnFilterPointerHandler=null;}}
function bindColumnFilterPointerTracking(){unbindColumnFilterPointerTracking();columnFilterPointerHandler=function(e){if(!isPointerInColumnFilterZone(e.clientX,e.clientY)){closeColumnFilter();}};document.addEventListener("pointerdown",columnFilterPointerHandler,true);}
function closeColumnFilter(){const details=getOpenColumnFilterDetails();if(details){details.open=false;clearColumnFilterPanelPosition(details);}
window.AFKJ.state.openColumnFilter=-1;unbindColumnFilterPointerTracking();}
function closeColumnFilterOnScroll(){if(window.AFKJ.state.openColumnFilter>=0){closeColumnFilter();}}
function measureEffectStackCellWidth(cell){const entries=cell.querySelectorAll(".effect-cell-entry");if(!entries.length){return 0;}
let maxWidth=0;entries.forEach(function(ent){let width=0;Array.from(ent.childNodes).forEach(function(node){if(node.nodeType===Node.ELEMENT_NODE){width+=node.getBoundingClientRect().width;}else if(node.nodeType===Node.TEXT_NODE){const range=document.createRange();range.selectNodeContents(node);width+=range.getBoundingClientRect().width;}});maxWidth=Math.max(maxWidth,width);});return maxWidth+32;}
function measureColumnWidths(){const state=window.AFKJ.state;if(!state.dom.heroesTableHead||!state.dom.heroesTableBody||!state.csvHeaders.length){return;}
if(!state.dom.heroesTableBody.rows.length){return;}
const widths=new Array(state.csvHeaders.length).fill(0);const labelRow=state.dom.heroesTableHead.querySelector(".heroes-table-label-row");if(labelRow){let colIdx=0;Array.from(labelRow.cells).forEach(function(cell){widths[colIdx]=Math.max(widths[colIdx],cell.getBoundingClientRect().width);colIdx+=cell.colSpan||1;});}
const filterRow=state.dom.heroesTableHead.querySelector(".heroes-table-filter-row");if(filterRow){let colIdx=1;Array.from(filterRow.cells).forEach(function(cell){widths[colIdx]=Math.max(widths[colIdx],cell.getBoundingClientRect().width);colIdx+=1;});}
Array.from(state.dom.heroesTableBody.rows).forEach(function(row){Array.from(row.cells).forEach(function(cell,idx){const col=state.csvHeaders[idx];const width=isEffectSortColumn(col)&&cell.querySelector(".effect-cell-entry")?measureEffectStackCellWidth(cell):cell.getBoundingClientRect().width;widths[idx]=Math.max(widths[idx],width);});});state.csvColumnWidths=widths.map(function(width){return Math.ceil(width);});}
function updateTableColgroup(){const state=window.AFKJ.state;if(!state.dom.heroesTable){return;}
let colgroup=state.dom.heroesTable.querySelector("colgroup");if(!state.csvColumnWidths.length){if(colgroup){colgroup.remove();}
state.dom.heroesTable.style.tableLayout="";return;}
if(!colgroup){colgroup=document.createElement("colgroup");state.dom.heroesTable.insertBefore(colgroup,state.dom.heroesTableHead);}
colgroup.innerHTML=state.csvColumnWidths.map(function(width){return('<col style="width:'+
width+"px;min-width:"+
width+'px">');}).join("");state.dom.heroesTable.style.tableLayout="fixed";}
function buildListBodyHtml(rows){const state=window.AFKJ.state;const tiers=window.AFKJ.tiers;let bodyHtml="";rows.forEach(function(row){const name=row[0]||"";const hero=state.heroByName[name];bodyHtml+="<tr>";row.forEach(function(cell,idx){const col=state.csvHeaders[idx];let inner;if(col==="Name"){if(hero){inner='<a href="'+
escapeHtml(utils.heroUrl(hero.slug))+'" class="hero-link col-name-link" data-slug="'+
escapeHtml(hero.slug)+'">'+'<span class="col-name-text">'+
escapeHtml(name)+"</span>"+
gridView.renderListHeroPortrait(hero)+"</a>";}else{inner=escapeHtml(name);}}else{inner=renderTableCell(col,getListCellRawValue(row,idx,col));}
let tdCls="";const colCls=listColumnClass(col);if(colCls){tdCls=' class="'+colCls+'"';}
bodyHtml+="<td"+tdCls+">"+inner+"</td>";});bodyHtml+="</tr>";});return bodyHtml;}
function renderList(){const state=window.AFKJ.state;const dom=state.dom;const tiers=window.AFKJ.tiers;if(!state.csvHeaders.length){if(dom.heroesTableHead){dom.heroesTableHead.innerHTML="";}
if(dom.heroesTableBody){dom.heroesTableBody.innerHTML='<tr><td class="empty-state">Table data missing. Run '+"<code>just render-site</code>.</td></tr>";}
if(dom.listEmptyState){dom.listEmptyState.classList.add("hidden");}
return;}
if(!dom.heroesTableHead||!dom.heroesTableBody){return;}
const allowed=window.AFKJ.router.filteredHeroNames();let rows=state.csvRows.filter(function(row){return allowed[row[0]]&&rowMatchesColumnFilters(row);});rows=rows.slice().sort(compareCsvRows);let labelRowHtml='<tr class="heroes-table-label-row">';let filterRowHtml='<tr class="heroes-table-filter-row">';state.csvHeaders.forEach(function(col,idx){let cls="sortable "+listColumnClass(col);const optionGroups=state.csvColumnFilterOptions[idx]||[];const selected=state.csvColumnFilters[idx]||[];const activeCount=selected.length;const hasFilter=activeCount>0;const filterCls="col-filter"+
(hasFilter?" is-active":"")+
(filterOptionGroupsHasChoices(optionGroups)?"":" is-empty");const label=tiers.TIER_CSV_HEADERS[col]?tiers.formatTierColumnHeader(col):escapeHtml(listColumnDisplayLabel(col));let sortCls="th-sort-btn";if(idx===state.sortColumn){sortCls+=state.sortDir===1?" sort-asc":" sort-desc";}
const showFilter=col!=="Name"&&filterOptionGroupsHasChoices(optionGroups);const nameRowSpan=col==="Name"?' rowspan="2"':"";labelRowHtml+="<th"+
nameRowSpan+' class="'+
cls+'" data-col="'+
idx+'">'+'<button type="button" class="'+
sortCls+'" data-col="'+
idx+'">'+
label+"</button></th>";if(col==="Name"){return;}
let filterCellCls="col-filter-cell "+listColumnClass(col);filterRowHtml+='<th class="'+
filterCellCls+'" data-col="'+
idx+'">';if(showFilter){const countHtml=hasFilter?'<span class="col-filter-count">('+activeCount+")</span>":"";const combineToggleHtml=renderColumnFilterCombineToggle(idx,col);filterRowHtml+='<div class="col-filter-row">';filterRowHtml+=combineToggleHtml;filterRowHtml+='<details class="'+
filterCls+'" data-col="'+
idx+'"'+
(state.openColumnFilter===idx?" open":"")+">"+'<summary class="col-filter-trigger" title="Filter column">'+'<span class="col-filter-field-label">'+'<span class="col-filter-status-dot" aria-hidden="true"></span>'+'<span class="col-filter-label-text">filter</span>'+
countHtml+"</span>"+'<span class="col-filter-sep" aria-hidden="true"></span>'+'<span class="col-filter-caret" aria-hidden="true"></span>'+"</summary>"+
renderColumnFilterPanel(idx,col,optionGroups)+"</details>";filterRowHtml+="</div>";}
filterRowHtml+="</th>";});labelRowHtml+="</tr>";filterRowHtml+="</tr>";dom.heroesTableHead.innerHTML=labelRowHtml+filterRowHtml;requestAnimationFrame(positionOpenColumnFilter);const allRows=state.csvRows.filter(function(row){return allowed[row[0]];});const tableScroll=getTableScrollEl();if(!state.columnWidthsLocked&&allRows.length){if(tableScroll){tableScroll.style.visibility="hidden";}
dom.heroesTableBody.innerHTML=buildListBodyHtml(allRows);dom.listEmptyState.classList.toggle("hidden",rows.length>0);requestAnimationFrame(function(){measureColumnWidths();state.columnWidthsLocked=state.csvColumnWidths.length>0;updateTableColgroup();dom.heroesTableBody.innerHTML=buildListBodyHtml(rows);dom.listEmptyState.classList.toggle("hidden",rows.length>0);if(tableScroll){tableScroll.style.visibility="";}});return;}
dom.heroesTableBody.innerHTML=buildListBodyHtml(rows);updateTableColgroup();dom.listEmptyState.classList.toggle("hidden",rows.length>0);}
window.AFKJ.views.list={EFFECT_CC_COLUMNS:EFFECT_CC_COLUMNS,EFFECT_ANTI_CC_COLUMNS:EFFECT_ANTI_CC_COLUMNS,TIMING_RANK:TIMING_RANK,parseCsv:parseCsv,parseEffectColumnLabel:parseEffectColumnLabel,parseEffectCellPart:parseEffectCellPart,renderEffectCellPart:renderEffectCellPart,cellMatchesColumnFilter:cellMatchesColumnFilter,rowMatchesColumnFilters:rowMatchesColumnFilters,buildColumnFilterOptions:buildColumnFilterOptions,renderColumnFilterPanel:renderColumnFilterPanel,renderTableCell:renderTableCell,compareCsvRows:compareCsvRows,getTableScrollEl:getTableScrollEl,clearColumnFilterPanelPosition:clearColumnFilterPanelPosition,positionOpenColumnFilter:positionOpenColumnFilter,getOpenColumnFilterDetails:getOpenColumnFilterDetails,isPointerInColumnFilterZone:isPointerInColumnFilterZone,unbindColumnFilterPointerTracking:unbindColumnFilterPointerTracking,bindColumnFilterPointerTracking:bindColumnFilterPointerTracking,closeColumnFilter:closeColumnFilter,closeColumnFilterOnScroll:closeColumnFilterOnScroll,measureColumnWidths:measureColumnWidths,updateTableColgroup:updateTableColgroup,buildListBodyHtml:buildListBodyHtml,renderList:renderList,toggleColumnFilterCombine:toggleColumnFilterCombine,};})();window.AFKJ=window.AFKJ||{};(function(){const utils=window.AFKJ.utils;function columnIndex(columnName){const headers=window.AFKJ.state.csvHeaders||[];return headers.indexOf(columnName);}
function allOptionsForColumn(colIdx){const groups=window.AFKJ.state.csvColumnFilterOptions[colIdx]||[];const values=[];groups.forEach(function(group){(group.values||[]).forEach(function(value){if(value){values.push(value);}});});return values;}
function encodeFilterParam(column,values){if(values.length===1&&values[0]==="all"){return encodeURIComponent(column)+"=all";}
return(encodeURIComponent(column)+"="+
values.map(encodeURIComponent).join(","));}
function comboDeepLink(combo){const parts=[];Object.keys(combo.filters||{}).forEach(function(column){const spec=combo.filters[column];parts.push(encodeFilterParam(column,spec.values||[]));});return"#list?f="+parts.join(";");}
function comboDeepLinkById(comboId){const combos=window.AFKJ.state.counterFilterCombos||{};const combo=combos[comboId];if(!combo){return"#";}
return comboDeepLink(combo);}
function parseListFilterHash(){const hash=location.hash||"";const match=hash.match(/^#list\?(?:.*&)?f=([^&#]+)/);if(!match){const direct=hash.match(/^#list\?f=([^#]+)/);if(!direct){return null;}
return parseFilterQuery(direct[1]);}
return parseFilterQuery(match[1]);}
function parseFilterQuery(raw){const decoded=decodeURIComponent(raw);const result={};decoded.split(";").forEach(function(pair){if(!pair){return;}
const eq=pair.indexOf("=");if(eq===-1){return;}
const column=decodeURIComponent(pair.slice(0,eq));const valPart=pair.slice(eq+1);const values=valPart.split(",").map(decodeURIComponent);result[column]=values;});return Object.keys(result).length?result:null;}
function resolveFilterValues(column,colIdx,values){if(values.length===1&&values[0]==="all"){return allOptionsForColumn(colIdx);}
return values.slice();}
function applyListFilterMap(filterMap){const state=window.AFKJ.state;state.csvColumnFilters={};state.csvColumnFilterCombine={};Object.keys(filterMap).forEach(function(column){const colIdx=columnIndex(column);if(colIdx===-1){return;}
const resolved=resolveFilterValues(column,colIdx,filterMap[column]);if(!resolved.length){return;}
state.csvColumnFilters[colIdx]=resolved;if(column==="Behavior tags"&&filterMap[column].length>1){state.csvColumnFilterCombine[colIdx]="and";}});state.viewMode="list";try{localStorage.setItem(window.AFKJ.config.VIEW_MODE_KEY,"list");}catch(e){}
if(window.AFKJ.main&&window.AFKJ.main.syncViewToggleButtons){window.AFKJ.main.syncViewToggleButtons();}}
function applyComboFilters(combo){const filterMap={};Object.keys(combo.filters||{}).forEach(function(column){const spec=combo.filters[column];filterMap[column]=(spec.values||[]).slice();if(column==="Behavior tags"&&spec.combine==="and"){}});applyListFilterMap(filterMap);Object.keys(combo.filters||{}).forEach(function(column){const spec=combo.filters[column];if(column==="Behavior tags"&&spec.combine==="and"){const colIdx=columnIndex(column);if(colIdx!==-1){window.AFKJ.state.csvColumnFilterCombine[colIdx]="and";}}});}
function tryApplyPendingListFilters(){const state=window.AFKJ.state;if(!state.pendingListFilterMap||!state.csvHeaders.length){return false;}
applyListFilterMap(state.pendingListFilterMap);state.pendingListFilterMap=null;return true;}
function isListFilterHash(){return/^#list(?:\?|$)/.test(location.hash||"");}
window.AFKJ.listFilters={columnIndex:columnIndex,allOptionsForColumn:allOptionsForColumn,comboDeepLink:comboDeepLink,comboDeepLinkById:comboDeepLinkById,parseListFilterHash:parseListFilterHash,parseFilterQuery:parseFilterQuery,applyListFilterMap:applyListFilterMap,applyComboFilters:applyComboFilters,tryApplyPendingListFilters:tryApplyPendingListFilters,isListFilterHash:isListFilterHash,};})();window.AFKJ=window.AFKJ||{};(function(){const utils=window.AFKJ.utils;const config=window.AFKJ.config;const chips=window.AFKJ.chips;const tiers=window.AFKJ.tiers;const gridView=window.AFKJ.views.grid;const escapeHtml=utils.escapeHtml.bind(utils);const MIX_SLOT_COUNT=5;const MIX_CORE_ROLES=["tank","damage_dealer","support","specialist"];const MIX_CROWN_BODY="M3.5 17.5 L2 10.5 Q1.5 7.5 3.5 10 Q6.5 13.5 9 11"+" Q12 4 15 11 Q17.5 13.5 20.5 10 Q22.5 7.5 22 10.5 L20.5 17.5Z";const MIX_CROWN_BAND='x="3.5" y="19" width="17" height="3" rx="1.2"';const MIX_CROWN_SVG='<svg class="hero-card-crown" viewBox="0 0 24 24" aria-hidden="true">'+'<path fill="#d4a017" d="'+MIX_CROWN_BODY+'"/>'+'<rect fill="#d4a017" '+MIX_CROWN_BAND+'/>'+'</svg>';const MIX_CONTEXT_ICONS={mark:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '+'stroke-width="1.8"><path d="'+MIX_CROWN_BODY+'"/>'+'<rect '+MIX_CROWN_BAND+'/></svg>',unmark:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '+'stroke-width="1.8"><path d="'+MIX_CROWN_BODY+'"/>'+'<rect '+MIX_CROWN_BAND+'/>'+'<path d="M4 4l16 16"/></svg>',highlight:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '+'stroke-width="2"><path d="M12 3l2.4 7.4H22l-6 4.6 2.3 7 L12 17.4 '+'5.7 22l2.3-7-6-4.6h7.6z"/></svg>',replace:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '+'stroke-width="2"><path d="M16 3h5v5M4 21 20.5 4.5M21 16v5h-5'+'M4 21 3 16"/></svg>',remove:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '+'stroke-width="2"><path d="M3 6h18M8 6V4h8v2M6 6l1 14h10l1-14"/></svg>',view:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '+'stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>'+'<circle cx="12" cy="12" r="3"/></svg>',add:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '+'stroke-width="2"><path d="M12 5v14M5 12h14"/></svg>',};const MIX_TOUCH_DEVICE=window.matchMedia("(hover: none) and (pointer: coarse)");let mixHighlightMap={};let mixHighlightSource=null;let mixGridOrder=[];let mixGridFadeTimer=null;let mixDragDidMove=false;let mixDragGhostEl=null;let mixGridPointer=null;let mixContextMenuEl=null;let mixContextSlotIndex=-1;let mixContextGridSlug=null;let mixSlotLastTap=null;const mixMarked=new Set();function mixDataUrl(path){const state=window.AFKJ.state;const bust=state.heroesMeta&&state.heroesMeta.generated?"?v="+encodeURIComponent(state.heroesMeta.generated):"";return utils.assetUrl(path)+bust;}
function normalizeMixConfig(raw){const out=Object.assign({},raw||{});const focusTags=Object.assign({},out.focusTags||{});Object.keys(config.MIX_FOCUS_TAG_DEFAULTS).forEach(function(key){focusTags[key]=Object.assign({},config.MIX_FOCUS_TAG_DEFAULTS[key],focusTags[key]||{});});out.focusTags=focusTags;return out;}
function loadMixData(){const state=window.AFKJ.state;if(Object.keys(state.mixSynergyIndex).length){return Promise.resolve();}
const idxUrl=mixDataUrl("data/mix-synergy-index.json");const configUrl=mixDataUrl("data/mix-config.json");const promUrl=mixDataUrl("data/mix-role-prominence.json");return Promise.all([fetch(idxUrl).then(function(r){return r.json();}),fetch(configUrl).then(function(r){return r.json();}),fetch(promUrl).then(function(r){return r.json();}),]).then(function(results){state.mixSynergyIndex=results[0]||{};state.mixConfig=normalizeMixConfig(results[1]);state.mixRoleProminence=results[2]||{};});}
function mixSlottedSlugSet(){const set={};window.AFKJ.state.mixSlots.forEach(function(slug){if(slug){set[slug]=true;}});return set;}
function compactMixSlots(){const state=window.AFKJ.state;const filled=state.mixSlots.filter(Boolean);state.mixSlots=filled.concat(Array(Math.max(0,MIX_SLOT_COUNT-filled.length)).fill(null));}
function mixFirstFreeSlotIndex(){const slots=window.AFKJ.state.mixSlots;for(let i=0;i<MIX_SLOT_COUNT;i++){if(!slots[i]){return i;}}
return-1;}
function removeSlugFromMixSlots(slug){const state=window.AFKJ.state;for(let i=0;i<MIX_SLOT_COUNT;i++){if(state.mixSlots[i]===slug){state.mixSlots[i]=null;}}
compactMixSlots();mixMarked.delete(slug);if(mixHighlightSource===slug){mixHighlightSource=null;mixHighlightMap={};}}
function clearMixAlternativeHighlights(){mixHighlightSource=null;mixHighlightMap={};}
function mixSlotIndexForSlug(slug){const slots=window.AFKJ.state.mixSlots;for(let i=0;i<MIX_SLOT_COUNT;i++){if(slots[i]===slug){return i;}}
return-1;}
function tryReplaceHighlightedAlternative(slug){if(!mixHighlightSource||!mixHighlightMap[slug]){return false;}
if(mixSlottedSlugSet()[slug]){return false;}
const slotIndex=mixSlotIndexForSlug(mixHighlightSource);if(slotIndex<0){clearMixAlternativeHighlights();return false;}
mixMarked.delete(mixHighlightSource);window.AFKJ.state.mixSlots[slotIndex]=slug;compactMixSlots();clearMixAlternativeHighlights();renderMix();return true;}
function addHeroToMixZone(slug){if(!slug||mixSlottedSlugSet()[slug]){return false;}
compactMixSlots();const slot=mixFirstFreeSlotIndex();if(slot<0){return false;}
window.AFKJ.state.mixSlots[slot]=slug;clearMixAlternativeHighlights();renderMix();return true;}
function placeHeroInMixZone(slug,source){if(!slug){return false;}
const state=window.AFKJ.state;const fromSlot=source&&source.indexOf("slot-")===0;if(fromSlot){const fromIndex=parseInt(source.split("-")[1],10);if(!isNaN(fromIndex)&&state.mixSlots[fromIndex]===slug){state.mixSlots[fromIndex]=null;}}else{removeSlugFromMixSlots(slug);}
compactMixSlots();if(mixSlottedSlugSet()[slug]){renderMix();return true;}
const slot=mixFirstFreeSlotIndex();if(slot<0){renderMix();return false;}
state.mixSlots[slot]=slug;compactMixSlots();if(!fromSlot){clearMixAlternativeHighlights();}
renderMix();return true;}
function getMixCompositionConfig(){const state=window.AFKJ.state;const cfg=state.mixConfig&&state.mixConfig.compositionScoring?state.mixConfig.compositionScoring:{};return{baseBonus:cfg.baseBonus!=null?cfg.baseBonus:10.0,urgencyPerFilledSlot:cfg.urgencyPerFilledSlot!=null?cfg.urgencyPerFilledSlot:0.25,maxHyperCarryPremium:cfg.maxHyperCarryPremium!=null?cfg.maxHyperCarryPremium:0.5,};}
function getMixSlottedCoreRoles(){const state=window.AFKJ.state;const roles={};MIX_CORE_ROLES.forEach(function(role){roles[role]=false;});state.mixSlots.forEach(function(slug){if(!slug){return;}
const hero=state.heroBySlug[slug];if(!hero||!hero.roleCategory){return;}
if(Object.prototype.hasOwnProperty.call(roles,hero.roleCategory)){roles[hero.roleCategory]=true;}});return roles;}
function getMixMissingCoreRoles(){const slotted=getMixSlottedCoreRoles();return MIX_CORE_ROLES.filter(function(role){return!slotted[role];});}
function mixCompositionUrgencyMultiplier(filledSlots){const cfg=getMixCompositionConfig();return 1+cfg.urgencyPerFilledSlot*filledSlots;}
function computeDamageDealerCarryScores(pool){const damageDealers=pool.filter(function(h){return h.roleCategory==="damage_dealer";});if(!damageDealers.length){return{};}
const scored=damageDealers.map(function(h){const tierRank=resolvePrydwenTierRank(h);const prominence=mixRawRoleProminence(h.slug,"damage_dealer");return{slug:h.slug,tierRank:tierRank<0?-1:tierRank,prominence:prominence,};});let minTier=Infinity;let maxTier=-Infinity;let minProm=Infinity;let maxProm=-Infinity;scored.forEach(function(s){if(s.tierRank<minTier){minTier=s.tierRank;}
if(s.tierRank>maxTier){maxTier=s.tierRank;}
if(s.prominence<minProm){minProm=s.prominence;}
if(s.prominence>maxProm){maxProm=s.prominence;}});const out={};scored.forEach(function(s){const tierNorm=maxTier===minTier?1:(s.tierRank-minTier)/(maxTier-minTier);const promNorm=maxProm===minProm?1:(s.prominence-minProm)/(maxProm-minProm);out[s.slug]=tierNorm*1000+promNorm;});const composites=Object.keys(out).map(function(slug){return out[slug];});const cMin=Math.min.apply(null,composites);const cMax=Math.max.apply(null,composites);Object.keys(out).forEach(function(slug){if(cMax===cMin){out[slug]=1;}else{out[slug]=(out[slug]-cMin)/(cMax-cMin);}});return out;}
function computeMixCompositionBonus(slug,missingRoles,filledSlots,carryScores){const state=window.AFKJ.state;if(!missingRoles.length){return 0;}
const hero=state.heroBySlug[slug];if(!hero||!hero.roleCategory){return 0;}
if(missingRoles.indexOf(hero.roleCategory)===-1){return 0;}
const cfg=getMixCompositionConfig();let bonus=cfg.baseBonus*mixCompositionUrgencyMultiplier(filledSlots);if(hero.roleCategory==="damage_dealer"&&carryScores){const carryNorm=carryScores[slug]||0;bonus*=1+cfg.maxHyperCarryPremium*carryNorm;}
return bonus;}
function synergyScoreForPair(providerSlug,receiverSlug){const state=window.AFKJ.state;const byReceiver=state.mixSynergyIndex&&state.mixSynergyIndex.byReceiver;if(!byReceiver||!byReceiver[receiverSlug]){return 0;}
return byReceiver[receiverSlug][providerSlug]||0;}
function getQualifyingMixFactions(){const state=window.AFKJ.state;const count={};state.mixSlots.forEach(function(slug){if(!slug){return;}
const hero=state.heroBySlug[slug];if(hero&&hero.faction){const key=utils.factionBonusGroupKey(hero.faction);count[key]=(count[key]||0)+1;}});const qualifying={};Object.keys(count).forEach(function(key){if(count[key]>=2){qualifying[key]=true;}});return qualifying;}
function mixHeroSkillTags(hero){const state=window.AFKJ.state;if(!hero||!hero.sections||!hero.sections.skillCards){return[];}
const list=[];hero.sections.skillCards.forEach(function(card){const tags=card.tags||card.effects||[];tags.forEach(function(t){const label=window.AFKJ.skills.skillCardTagLabel(t);const key=window.AFKJ.skills.skillCardChipKey(label);if(key){list.push({key:key,label:label});}});});return list;}
function mixHeroBehaviorTags(hero){const behavior=hero&&hero.sections&&hero.sections.behavior;if(!behavior){return[];}
const match=behavior.match(/\*\*Behavior tags\*\*:\s*([^\n]+)/);if(!match){return[];}
const found=[];const re=/`([^`]+)`/g;let m;while((m=re.exec(match[1]))!==null){found.push(m[1]);}
return found;}
function mixTagBaseLabel(tag){const parts=String(tag).split(/\s+[—–-]\s+/);return parts[0].trim();}
function mixFocusTagWeight(map,key){if(!map||!key){return null;}
if(map[key]!=null){return map[key];}
const lower=key.toLowerCase();const keys=Object.keys(map);for(let i=0;i<keys.length;i++){if(keys[i].toLowerCase()===lower){return map[keys[i]];}}
return null;}
function mixCcTargetingWeight(tag){const state=window.AFKJ.state;const weights=(state.mixConfig&&state.mixConfig.ccTargetingWeight)||{};const lower=String(tag).toLowerCase();if(lower.indexOf("all units")!==-1){return weights["All units"]||2.0;}
if(lower.indexOf("area")!==-1){return weights.Area||1.6;}
if(lower.indexOf("arc")!==-1){return weights.Arc||1.3;}
if(lower.indexOf("multiple targets")!==-1){return weights["Multiple targets"]||1.3;}
return weights["Single target"]||1.0;}
function mixTagTargetingWeight(tag){const lower=tag.trim().toLowerCase();const isSummons=lower.indexOf("to summons")!==-1||lower.indexOf("to owned summons")!==-1;const isAllies=lower.indexOf("to allies")!==-1;if(isSummons||isAllies){return 1.4;}
const re=/\b(?:all\s+enemies|center\s+of\s+the\s+battlefield|all\s+units|area)\b/i;if(re.test(tag)){return 1.25;}
return 1.0;}
function mixHeroSkillOverviewSpeeds(hero){if(!hero||!hero.sections||!hero.sections.behavior){return{};}
const md=hero.sections.behavior;const overviewLines=md.split("\n").filter(function(line){return line.startsWith("- **Signature skill")||line.startsWith("- **Ultimate")||line.startsWith("- **Non-ultimate");});const out={};overviewLines.forEach(function(line){const match=line.match(/^\s*-\s*\*\*([^*]+)\*\*:\s*([^\n]+)$/);if(!match)return;const slot=match[1].replace(/\s*\(ult\)$/,"").trim().toLowerCase();const right=match[2];const speedMatch=right.match(/`([^`]+)`\s*first\s+cast\s+speed/i)||right.match(/`([^`]+)`\s*speed/i);if(speedMatch){out[slot]=speedMatch[1].trim().toLowerCase();}});return out;}
function computeMixSpeedBonus(hero){const state=window.AFKJ.state;const weight=(state.mixConfig.mixMode&&state.mixConfig.mixMode.role_prominence_tier_weight)??7;const scoreMult=weight*1.5;const speeds=mixHeroSkillOverviewSpeeds(hero);const signature=speeds.signature||speeds.ultimate||"average";const multipliers={slow:1.6,average:1.2,fast:1.0};const mult=multipliers[signature]||1.2;let energyBuffValue=0;let hasteBuffValue=0;state.mixSlots.forEach(function(slotSlug){if(!slotSlug){return;}
const slotHero=state.heroBySlug[slotSlug];if(!slotHero){return;}
const byReceiver=state.mixSynergyIndex&&state.mixSynergyIndex.byReceiver;const row=byReceiver&&byReceiver[hero.slug];if(!row){return;}
const pairScore=row[slotSlug]||0;if(pairScore===0){return;}
const recSpeeds=mixHeroSkillOverviewSpeeds(slotHero);const recSig=recSpeeds.signature||recSpeeds.ultimate||"average";const recMult=multipliers[recSig]||1.2;const providerTags=mixHeroSkillTags(slotHero);providerTags.forEach(function(tag){const base=mixTagBaseLabel(tag.label).toLowerCase();const polarity=chips.effectLabelPolarity(tag.label)||"buff";if(polarity!=="buff")return;const tw=mixTagTargetingWeight(tag.label);if(base==="energy"||base==="energy recovery"||base==="energy recovery buff"){energyBuffValue=Math.max(energyBuffValue,3.0*tw*recMult);}
if(base==="haste"||base==="haste buff"||base==="atk spd"||base==="atk spd buff"){hasteBuffValue=Math.max(hasteBuffValue,3.0*tw*recMult);}});});return(energyBuffValue+hasteBuffValue)*mult*scoreMult*0.05;}
function mixHasActiveFocus(){const state=window.AFKJ.state;return Object.values(state.mixFocus).some(Boolean);}
function computeMixFocusBonus(hero){const state=window.AFKJ.state;if(!state.mixConfig||!state.mixConfig.focusTags){return 0;}
const focusTags=state.mixConfig.focusTags;const heroSkillTags=mixHeroSkillTags(hero);const heroBehaviorTags=mixHeroBehaviorTags(hero);const focusKeys=config.MIX_FOCUS_CONFIG_KEYS;let bonus=0;function addFromMap(map,isCc){if(!map){return 0;}
let focusMax=0;heroSkillTags.forEach(function(tag){const base=mixTagBaseLabel(tag.label);const weight=mixFocusTagWeight(map,base);if(weight!=null){const mult=isCc?mixCcTargetingWeight(tag.label):1;focusMax=Math.max(focusMax,weight*mult);}});heroBehaviorTags.forEach(function(bt){const weight=mixFocusTagWeight(map,bt);if(weight!=null){focusMax=Math.max(focusMax,weight);}});return focusMax;}
if(state.mixFocus.ccImmunity){bonus+=addFromMap(focusTags[focusKeys.ccImmunity],false);}
if(state.mixFocus.cc){bonus+=addFromMap(focusTags[focusKeys.cc],true);}
if(state.mixFocus.sustain){bonus+=addFromMap(focusTags[focusKeys.sustain],false);}
if(state.mixFocus.speed){bonus+=computeMixSpeedBonus(hero);}
if(state.mixFocus.noUltimate){bonus+=addFromMap(focusTags[focusKeys.noUltimate],false);}
return bonus;}
function computeMixScore(slug){const state=window.AFKJ.state;const team=state.mixSlots.filter(Boolean);const hero=state.heroBySlug[slug];if(!team.length){if(!mixHasActiveFocus()||!hero){return 0;}
return computeMixFocusBonus(hero);}
let total=0;const markMult=state.mixConfig&&state.mixConfig.markSynergyMultiplier!=null?state.mixConfig.markSynergyMultiplier:2.0;team.forEach(function(receiverSlug){const score=synergyScoreForPair(slug,receiverSlug);const mult=mixMarked.has(receiverSlug)?markMult:1.0;total+=score*mult;});if(hero){total+=computeMixFocusBonus(hero);const qualifying=getQualifyingMixFactions();if(hero.faction&&qualifying[utils.factionBonusGroupKey(hero.faction)]){const factionBonus=state.mixConfig&&state.mixConfig.factionBonus!=null?state.mixConfig.factionBonus:3.0;total+=factionBonus;}}
return total;}
function mixRawRoleProminence(slug,roleKey){const state=window.AFKJ.state;const bySlug=state.mixRoleProminence&&state.mixRoleProminence.bySlug?state.mixRoleProminence.bySlug:null;if(!bySlug||!roleKey){return 0;}
const row=bySlug[slug];if(!row||row[roleKey]==null){return 0;}
return row[roleKey];}
function normalizePrydwenTiersForRoleProminence(tiers){const out={};config.ROLE_FILTER_ORDER.forEach(function(role){const modeKey=role==="damage_dealer"?"afk_stages":role==="specialist"?"pvp":"dream_realm";const raw=tiers[modeKey]||"?";out[role]=raw;});return out;}
function averagePrydwenTierRankFromTiers(tiers){let sum=0;let count=0;tiers.forEach(function(mode){const rank=window.AFKJ.tiers.prydwenTierRank(mode);if(rank>=0){sum+=rank;count++;}});return count>0?sum/count:-1;}
function resolvePrydwenTierRank(hero){const state=window.AFKJ.state;const mode=state.mixMode;const key=mode==="pvp"?"pvp":mode==="afk"?"afk_stages":mode==="boss"?"dream_realm":"average";const modeTiers=window.AFKJ.tiers.getHeroPrydwenTiers(hero);if(key==="average"){const list=Object.values(modeTiers);return averagePrydwenTierRankFromTiers(list);}
return window.AFKJ.tiers.prydwenTierRank(modeTiers[key]);}
function roleProminenceTierPoints(hero){const rank=resolvePrydwenTierRank(hero);if(rank<0){return 0;}
return(rank+1)*100;}
function mixCombinedRoleProminenceRaw(hero,roleKey){const rawProm=mixRawRoleProminence(hero.slug,roleKey);const points=roleProminenceTierPoints(hero);return rawProm+points;}
function normalizeScores(pool,scoreFn){const bonuses={};if(!pool||!pool.length){return bonuses;}
let min=Infinity;let max=-Infinity;pool.forEach(function(h){const raw=scoreFn(h);if(raw<min){min=raw;}
if(raw>max){max=raw;}});if(!isFinite(min)||!isFinite(max)||min===max){pool.forEach(function(h){bonuses[h.slug]=0;});return bonuses;}
const range=max-min;pool.forEach(function(h){const raw=scoreFn(h);bonuses[h.slug]=((raw-min)/range)*10;});return bonuses;}
function computeNormalizedRoleBonuses(pool,roleKey){if(!roleKey){return{};}
return normalizeScores(pool,function(h){return mixCombinedRoleProminenceRaw(h,roleKey);});}
function computeNormalizedTierBonuses(pool){return normalizeScores(pool,function(h){return roleProminenceTierPoints(h);});}
function mixPoolHeroes(){const state=window.AFKJ.state;const slotsSet=mixSlottedSlugSet();const list=window.AFKJ.router.filteredHeroes();return list.filter(function(h){return!slotsSet[h.slug];});}
function mixSortedPoolHeroes(){const state=window.AFKJ.state;const pool=mixPoolHeroes();const candidates=[];const filledSlots=state.mixSlots.filter(Boolean).length;const missingRoles=getMixMissingCoreRoles();const carryScores=missingRoles.indexOf("damage_dealer")>=0?computeDamageDealerCarryScores(pool):null;const modeTiers=computeNormalizedTierBonuses(pool);const roleTiers=state.activeRole?computeNormalizedRoleBonuses(pool,state.activeRole):{};pool.forEach(function(h){const score=computeMixScore(h.slug);let promBonus=0;if(state.activeRole){promBonus=roleTiers[h.slug]||0;}else{promBonus=modeTiers[h.slug]||0;}
const compBonus=computeMixCompositionBonus(h.slug,missingRoles,filledSlots,carryScores);const finalScore=score+promBonus+compBonus;candidates.push({hero:h,score:finalScore});});candidates.sort(function(a,b){if(Math.abs(a.score-b.score)<0.0001){return a.hero.name.localeCompare(b.hero.name);}
return b.score-a.score;});return candidates.map(function(c){return c.hero;});}
function replacementCategoryIcon(label){return config.REPLACEMENT_CATEGORY_ICONS[label]||"";}
function renderMixHighlightIcons(categories){if(!categories||!categories.length){return"";}
let html='<div class="mix-highlight-icons">';categories.forEach(function(label){const icon=replacementCategoryIcon(label);html+='<span class="mix-highlight-icon" title="'+
escapeHtml(label)+'">'+
escapeHtml(icon)+"</span>";});html+="</div>";return html;}
function renderMixHeroCard(h,opts){opts=opts||{};const factionKey=utils.factionDataKey(h.faction);let extraClass="";const isHighlightSource=opts.highlightSource||mixHighlightSource===h.slug;if(opts.marked||isHighlightSource){extraClass+=" hero-card--mix-marked";}
let highlightCats=[];if(!opts.inSlot&&mixHighlightMap[h.slug]){highlightCats=mixHighlightMap[h.slug];extraClass+=" hero-card--mix-highlight";}
const draggable=opts.draggable!==false;const chromeHtml=(opts.marked||isHighlightSource?MIX_CROWN_SVG:"")+
(highlightCats.length&&!opts.inSlot?renderMixHighlightIcons(highlightCats):"");const cardHtml='<article class="hero-card afkj-box afkj-box-sm'+
extraClass+'" data-slug="'+
escapeHtml(h.slug)+'" data-faction="'+
escapeHtml(factionKey)+'"'+
(draggable?' draggable="true"':"")+
(opts.mixSource?' data-mix-source="'+escapeHtml(opts.mixSource)+'"':"")+' tabindex="0" aria-label="'+
escapeHtml(h.name)+'">'+
gridView.renderHeroPortrait(h)+
gridView.renderHeroCardWave(h.slug)+'<div class="hero-card-info">'+'<div class="hero-card-name"><h2>'+
escapeHtml(h.name)+"</h2></div>"+'<div class="hero-card-meta">'+
gridView.renderGridCardRole(h)+"</div></div>"+
gridView.renderGridCardFactionStack(h)+"</article>";if(!chromeHtml){return'<div class="mix-hero-card-shell">'+cardHtml+"</div>";}
return('<div class="mix-hero-card-shell">'+
cardHtml+'<div class="mix-hero-card-chrome" aria-hidden="true">'+
chromeHtml+"</div></div>");}
function renderMixSlots(){const state=window.AFKJ.state;const dom=state.dom;if(!dom.mixDropZone){return;}
compactMixSlots();let html="";for(let i=0;i<MIX_SLOT_COUNT;i++){const slug=state.mixSlots[i];html+='<div class="mix-slot" data-slot="'+i+'">';if(slug&&state.heroBySlug[slug]){html+=renderMixHeroCard(state.heroBySlug[slug],{inSlot:true,marked:mixMarked.has(slug),highlightSource:mixHighlightSource===slug,mixSource:"slot-"+i,});}else{html+='<div class="mix-slot--empty" aria-label="Empty slot"></div>';}
html+="</div>";}
dom.mixDropZone.innerHTML=html;}
const MIX_GRID_FADE_MS=200;function animateMixGridFadeIn(){const grid=window.AFKJ.state.dom.mixHeroGrid;if(!grid){return;}
requestAnimationFrame(function(){const shells=grid.querySelectorAll(".mix-hero-card-shell");shells.forEach(function(shell){shell.style.opacity="0";});requestAnimationFrame(function(){shells.forEach(function(shell){shell.classList.add("mix-sort-anim");shell.style.opacity="1";});setTimeout(function(){shells.forEach(function(shell){shell.classList.remove("mix-sort-anim");shell.style.opacity="";});},MIX_GRID_FADE_MS);});});}
function fadeOutMixGridThen(run){const grid=window.AFKJ.state.dom.mixHeroGrid;if(!grid){run();return;}
const shells=grid.querySelectorAll(".mix-hero-card-shell");if(!shells.length){run();return;}
shells.forEach(function(shell){shell.classList.add("mix-sort-anim");});requestAnimationFrame(function(){shells.forEach(function(shell){shell.style.opacity="0";});clearTimeout(mixGridFadeTimer);mixGridFadeTimer=setTimeout(function(){mixGridFadeTimer=null;run();},MIX_GRID_FADE_MS);});}
function renderMixGrid(){const state=window.AFKJ.state;const dom=state.dom;if(!dom.mixHeroGrid){return;}
const list=mixSortedPoolHeroes();const newOrder=list.map(function(h){return h.slug;});const orderChanged=mixGridOrder.join(",")!==newOrder.join(",");const hadShells=dom.mixHeroGrid.querySelectorAll(".mix-hero-card-shell").length>0;function applyMixGrid(fadeIn){mixGridOrder=newOrder;dom.mixHeroGrid.innerHTML=list.map(function(h){return renderMixHeroCard(h,{mixSource:"grid"});}).join("");if(dom.mixEmptyState){dom.mixEmptyState.classList.toggle("hidden",list.length>0);}
if(fadeIn){animateMixGridFadeIn();}
gridView.scheduleFitHeroCardNames();}
if(orderChanged&&hadShells){clearTimeout(mixGridFadeTimer);fadeOutMixGridThen(function(){applyMixGrid(true);});return;}
applyMixGrid(false);}
function renderMix(){renderMixSlots();renderMixGrid();syncMixFocusButtons();syncMixModeButtons();}
function syncMixFocusButtons(){const state=window.AFKJ.state;const toolbar=document.querySelector(".mix-focus-selector");if(!toolbar){return;}
toolbar.querySelectorAll(".mix-focus-btn").forEach(function(btn){const fKey=btn.dataset.focus;const active=!!state.mixFocus[fKey];btn.classList.toggle("active",active);btn.setAttribute("aria-pressed",active?"true":"false");});}
function syncMixModeButtons(){const state=window.AFKJ.state;const toolbar=document.querySelector(".mix-mode-selector");if(!toolbar){return;}
toolbar.querySelectorAll(".mix-mode-btn").forEach(function(btn){const mKey=btn.dataset.mode;const active=state.mixMode===mKey;btn.classList.toggle("active",active);btn.setAttribute("aria-pressed",active?"true":"false");});}
function buildMixHighlightMap(sourceSlug){const state=window.AFKJ.state;const hero=state.heroBySlug[sourceSlug];const map={};if(!hero||!hero.sections||!hero.sections.replacements){return map;}
hero.sections.replacements.forEach(function(cat){(cat.entries||[]).forEach(function(entry){if(!entry.slug){return;}
if(!map[entry.slug]){map[entry.slug]=[];}
if(map[entry.slug].indexOf(cat.category)===-1){map[entry.slug].push(cat.category);}});});return map;}
function getMixOverallReplacement(sourceSlug){const state=window.AFKJ.state;const hero=state.heroBySlug[sourceSlug];if(!hero||!hero.sections||!hero.sections.replacements){return null;}
const overall=hero.sections.replacements.find(function(cat){return cat.category==="Best overall replacement";});if(!overall||!overall.entries||!overall.entries.length){return null;}
return overall.entries[0];}
function ensureMixContextMenu(){if(mixContextMenuEl){return mixContextMenuEl;}
mixContextMenuEl=document.createElement("div");mixContextMenuEl.className="mix-context-menu";mixContextMenuEl.hidden=true;mixContextMenuEl.setAttribute("role","menu");document.body.appendChild(mixContextMenuEl);mixContextMenuEl.addEventListener("click",function(e){const menuBtn=e.target.closest(".mix-context-menu-item");if(!menuBtn||menuBtn.disabled){return;}
e.preventDefault();e.stopPropagation();if(mixContextGridSlug){handleMixGridContextAction(menuBtn.dataset.action);}else{handleMixContextAction(menuBtn.dataset.action);}});document.addEventListener("click",function(e){if(mixContextMenuEl&&!mixContextMenuEl.hidden&&!mixContextMenuEl.contains(e.target)){closeMixContextMenu();}});document.addEventListener("keydown",function(e){if(e.key==="Escape"){closeMixContextMenu();}});return mixContextMenuEl;}
function closeMixContextMenu(){if(mixContextMenuEl){mixContextMenuEl.hidden=true;}
mixContextSlotIndex=-1;mixContextGridSlug=null;}
function positionMixContextMenu(menu,clientX,clientY){menu.hidden=false;menu.style.left=clientX+"px";menu.style.top=clientY+"px";const rect=menu.getBoundingClientRect();if(rect.right>window.innerWidth-8){menu.style.left=Math.max(8,clientX-rect.width)+"px";}
if(rect.bottom>window.innerHeight-8){menu.style.top=Math.max(8,clientY-rect.height)+"px";}}
function mixContextMenuItem(label,iconKey,action,disabled){const isDisabled=!!disabled;return('<button type="button" class="mix-context-menu-item'+
(isDisabled?" mix-context-menu-item--disabled":"")+'" data-action="'+
escapeHtml(action)+'"'+
(isDisabled?" disabled":"")+">"+'<span class="mix-context-menu-icon">'+
(MIX_CONTEXT_ICONS[iconKey]||"")+"</span>"+
escapeHtml(label)+"</button>");}
function openMixContextMenu(slotIndex,clientX,clientY){const state=window.AFKJ.state;const slug=state.mixSlots[slotIndex];if(!slug){return;}
const menu=ensureMixContextMenu();mixContextSlotIndex=slotIndex;mixContextGridSlug=null;let html="";if(mixMarked.has(slug)){html+=mixContextMenuItem("Unmark","unmark","unmark");}else{html+=mixContextMenuItem("Mark","mark","mark");}
html+=mixContextMenuItem(mixHighlightSource===slug?"Unmark alternatives":"Highlight alternatives","highlight","highlight");if(getMixOverallReplacement(slug)){html+=mixContextMenuItem("Replace","replace","replace");}
html+=mixContextMenuItem("View character","view","view");html+=mixContextMenuItem("Remove","remove","remove");menu.innerHTML=html;positionMixContextMenu(menu,clientX,clientY);}
function openMixGridContextMenu(slug,clientX,clientY){if(!slug||mixSlottedSlugSet()[slug]){return;}
const menu=ensureMixContextMenu();mixContextSlotIndex=-1;mixContextGridSlug=slug;const isReplacement=mixHighlightSource&&mixHighlightMap[slug];const zoneFull=mixFirstFreeSlotIndex()<0;const addDisabled=!isReplacement&&zoneFull;let html=mixContextMenuItem("View character","view","grid-view");html+=mixContextMenuItem(isReplacement?"Replace":"Add",isReplacement?"replace":"add",isReplacement?"grid-replace":"grid-add",addDisabled);menu.innerHTML=html;positionMixContextMenu(menu,clientX,clientY);}
function removeHeroFromMixSlot(slotIndex){const state=window.AFKJ.state;const slug=state.mixSlots[slotIndex];if(!slug){return;}
state.mixSlots[slotIndex]=null;mixMarked.delete(slug);if(mixHighlightSource===slug){clearMixAlternativeHighlights();}
compactMixSlots();renderMix();}
function handleMixGridContextAction(action){const slug=mixContextGridSlug;closeMixContextMenu();if(!slug){return;}
if(action==="grid-view"){window.AFKJ.router.navigateTo(utils.heroUrl(slug));return;}
if(action==="grid-replace"){tryReplaceHighlightedAlternative(slug);return;}
if(action==="grid-add"){addHeroToMixZone(slug);}}
function handleMixContextAction(action){const state=window.AFKJ.state;const slotIndex=mixContextSlotIndex;const slug=slotIndex>=0?state.mixSlots[slotIndex]:null;closeMixContextMenu();if(!slug){return;}
if(action==="view"){window.AFKJ.router.navigateTo(utils.heroUrl(slug));return;}
if(action==="mark"){mixMarked.add(slug);renderMix();return;}
if(action==="unmark"){mixMarked.delete(slug);renderMix();return;}
if(action==="highlight"){if(mixHighlightSource===slug){mixHighlightSource=null;mixHighlightMap={};}else{mixHighlightSource=slug;mixHighlightMap=buildMixHighlightMap(slug);}
renderMix();return;}
if(action==="replace"){const rep=getMixOverallReplacement(slug);if(!rep||!rep.slug){return;}
state.mixSlots[slotIndex]=rep.slug;mixMarked.delete(slug);if(mixHighlightSource===slug){mixHighlightSource=null;mixHighlightMap={};}
compactMixSlots();renderMix();return;}
if(action==="remove"){removeHeroFromMixSlot(slotIndex);}}
function clearMixDragGhost(){if(mixDragGhostEl&&mixDragGhostEl.parentNode){mixDragGhostEl.parentNode.removeChild(mixDragGhostEl);}
mixDragGhostEl=null;}
function setMixDragImage(e,card){clearMixDragGhost();const rect=card.getBoundingClientRect();const clone=card.cloneNode(true);clone.classList.add("mix-drag-ghost");clone.setAttribute("aria-hidden","true");clone.style.position="fixed";clone.style.top="-10000px";clone.style.left="0";clone.style.width=rect.width+"px";clone.style.height=rect.height+"px";clone.style.margin="0";clone.style.pointerEvents="none";clone.style.transform="none";clone.style.opacity="1";const nameH2=card.querySelector(".hero-card-name h2");const cloneH2=clone.querySelector(".hero-card-name h2");if(nameH2&&cloneH2&&nameH2.style.fontSize){cloneH2.style.fontSize=nameH2.style.fontSize;}
document.body.appendChild(clone);mixDragGhostEl=clone;e.dataTransfer.setDragImage(clone,e.clientX-rect.left,e.clientY-rect.top);}
function mixDragSourceFromEvent(e){const card=e.target.closest(".hero-card[data-mix-source]");return card?card.dataset.mixSource:"";}
function initMixInteractions(){const state=window.AFKJ.state;const dom=state.dom;if(!dom.mixView){return;}
const mixFocusSelector=dom.mixView.querySelector(".mix-focus-selector");if(mixFocusSelector){mixFocusSelector.addEventListener("click",function(e){const btn=e.target.closest(".mix-focus-btn");if(!btn){return;}
const key=btn.dataset.focus;if(key&&Object.prototype.hasOwnProperty.call(state.mixFocus,key)){state.mixFocus[key]=!state.mixFocus[key];}
syncMixFocusButtons();loadMixData().then(renderMix);});}
const modeSelector=dom.mixView.querySelector(".mix-mode-selector");if(modeSelector){modeSelector.addEventListener("click",function(e){const btn=e.target.closest(".mix-mode-btn");if(!btn){return;}
const mode=btn.dataset.mode;state.mixMode=state.mixMode===mode?null:mode;renderMix();});}
if(dom.mixRemoveAllBtn){dom.mixRemoveAllBtn.addEventListener("click",function(){state.mixSlots=[null,null,null,null,null];mixMarked.clear();mixHighlightSource=null;mixHighlightMap={};renderMix();});}
dom.mixView.addEventListener("dragstart",function(e){if(state.viewMode!=="mix"){return;}
const card=e.target.closest(".hero-card[data-slug]");const slug=card?card.dataset.slug:"";if(!slug){return;}
mixDragDidMove=false;e.dataTransfer.setData("text/plain",slug);e.dataTransfer.setData("application/x-afkj-mix-source",mixDragSourceFromEvent(e)||"grid");e.dataTransfer.effectAllowed="move";setMixDragImage(e,card);});dom.mixView.addEventListener("drag",function(){mixDragDidMove=true;});dom.mixView.addEventListener("dragend",function(){clearMixDragGhost();setTimeout(function(){mixDragDidMove=false;},0);});dom.mixView.addEventListener("dragover",function(e){if(state.viewMode!=="mix"){return;}
const grid=e.target.closest(".mix-hero-grid");const zone=e.target.closest(".mix-drop-zone");if(zone||grid){e.preventDefault();e.dataTransfer.dropEffect="move";}
dom.mixView.querySelectorAll(".mix-drag-over").forEach(function(el){el.classList.remove("mix-drag-over");});if(zone){zone.classList.add("mix-drag-over");}else if(grid){grid.classList.add("mix-drag-over");}});dom.mixView.addEventListener("dragleave",function(e){const related=e.relatedTarget;if(related&&dom.mixView.contains(related)){return;}
dom.mixView.querySelectorAll(".mix-drag-over").forEach(function(el){el.classList.remove("mix-drag-over");});});dom.mixView.addEventListener("drop",function(e){if(state.viewMode!=="mix"){return;}
e.preventDefault();dom.mixView.querySelectorAll(".mix-drag-over").forEach(function(el){el.classList.remove("mix-drag-over");});const slug=e.dataTransfer.getData("text/plain");const source=e.dataTransfer.getData("application/x-afkj-mix-source");if(!slug){return;}
const slotEl=e.target.closest(".mix-slot");const gridEl=e.target.closest(".mix-hero-grid");const zoneEl=e.target.closest(".mix-drop-zone");if(gridEl&&source.indexOf("slot-")===0){removeSlugFromMixSlots(slug);renderMix();return;}
if(slotEl||zoneEl){placeHeroInMixZone(slug,source);}});dom.mixView.addEventListener("pointerdown",function(e){if(state.viewMode!=="mix"||e.button!==0){return;}
const card=e.target.closest("#mix-hero-grid .hero-card");if(!card){mixGridPointer=null;return;}
mixGridPointer={slug:card.dataset.slug,x:e.clientX,y:e.clientY,};});dom.mixView.addEventListener("pointerup",function(e){if(state.viewMode!=="mix"||!mixGridPointer){return;}
const card=e.target.closest("#mix-hero-grid .hero-card");const pointer=mixGridPointer;mixGridPointer=null;if(!card||card.dataset.slug!==pointer.slug){return;}
const dx=e.clientX-pointer.x;const dy=e.clientY-pointer.y;if(dx*dx+dy*dy>36){return;}
e.preventDefault();if(!tryReplaceHighlightedAlternative(pointer.slug)){addHeroToMixZone(pointer.slug);}});dom.mixView.addEventListener("click",function(e){if(state.viewMode!=="mix"){return;}
const slotCard=e.target.closest(".mix-slot .hero-card");if(slotCard){e.preventDefault();e.stopPropagation();if(MIX_TOUCH_DEVICE.matches){return;}
const slot=slotCard.closest(".mix-slot");const index=slot?parseInt(slot.dataset.slot,10):-1;if(index>=0){removeHeroFromMixSlot(index);}
return;}});dom.mixView.addEventListener("touchend",function(e){if(state.viewMode!=="mix"){return;}
const slotCard=e.target.closest(".mix-slot .hero-card");if(!slotCard){return;}
const slot=slotCard.closest(".mix-slot");const index=slot?parseInt(slot.dataset.slot,10):-1;if(index<0){return;}
const touch=e.changedTouches[0];if(!touch){return;}
const tapKey=index+"|"+slotCard.dataset.slug;const now=Date.now();if(mixSlotLastTap&&mixSlotLastTap.key===tapKey&&now-mixSlotLastTap.time<config.MIX_SLOT_DOUBLE_TAP_MS){e.preventDefault();mixSlotLastTap=null;openMixContextMenu(index,touch.clientX,touch.clientY);return;}
mixSlotLastTap={key:tapKey,time:now};});dom.mixView.addEventListener("contextmenu",function(e){if(state.viewMode!=="mix"){return;}
const slotCard=e.target.closest(".mix-slot .hero-card");if(slotCard){e.preventDefault();e.stopPropagation();const slot=slotCard.closest(".mix-slot");const index=slot?parseInt(slot.dataset.slot,10):-1;if(index>=0){openMixContextMenu(index,e.clientX,e.clientY);}
return;}
const gridCard=e.target.closest("#mix-hero-grid .hero-card");if(gridCard&&gridCard.dataset.slug){e.preventDefault();e.stopPropagation();openMixGridContextMenu(gridCard.dataset.slug,e.clientX,e.clientY);}});ensureMixContextMenu();}
window.AFKJ.views.mix={loadMixData:loadMixData,mixSlottedSlugSet:mixSlottedSlugSet,compactMixSlots:compactMixSlots,mixFirstFreeSlotIndex:mixFirstFreeSlotIndex,removeSlugFromMixSlots:removeSlugFromMixSlots,clearMixAlternativeHighlights:clearMixAlternativeHighlights,mixSlotIndexForSlug:mixSlotIndexForSlug,tryReplaceHighlightedAlternative:tryReplaceHighlightedAlternative,addHeroToMixZone:addHeroToMixZone,placeHeroInMixZone:placeHeroInMixZone,synergyScoreForPair:synergyScoreForPair,getQualifyingMixFactions:getQualifyingMixFactions,mixHeroSkillTags:mixHeroSkillTags,mixHeroBehaviorTags:mixHeroBehaviorTags,computeMixSpeedBonus:computeMixSpeedBonus,computeMixFocusBonus:computeMixFocusBonus,computeMixScore:computeMixScore,getMixCompositionConfig:getMixCompositionConfig,getMixSlottedCoreRoles:getMixSlottedCoreRoles,getMixMissingCoreRoles:getMixMissingCoreRoles,mixCompositionUrgencyMultiplier:mixCompositionUrgencyMultiplier,computeDamageDealerCarryScores:computeDamageDealerCarryScores,computeMixCompositionBonus:computeMixCompositionBonus,mixRawRoleProminence:mixRawRoleProminence,resolvePrydwenTierRank:resolvePrydwenTierRank,roleProminenceTierPoints:roleProminenceTierPoints,mixCombinedRoleProminenceRaw:mixCombinedRoleProminenceRaw,normalizeScores:normalizeScores,computeNormalizedRoleBonuses:computeNormalizedRoleBonuses,computeNormalizedTierBonuses:computeNormalizedTierBonuses,mixPoolHeroes:mixPoolHeroes,mixSortedPoolHeroes:mixSortedPoolHeroes,renderMixHeroCard:renderMixHeroCard,renderMixSlots:renderMixSlots,renderMixGrid:renderMixGrid,renderMix:renderMix,syncMixFocusButtons:syncMixFocusButtons,syncMixModeButtons:syncMixModeButtons,buildMixHighlightMap:buildMixHighlightMap,getMixOverallReplacement:getMixOverallReplacement,closeMixContextMenu:closeMixContextMenu,openMixContextMenu:openMixContextMenu,openMixGridContextMenu:openMixGridContextMenu,removeHeroFromMixSlot:removeHeroFromMixSlot,initMixInteractions:initMixInteractions,};})();window.AFKJ=window.AFKJ||{};(function(){const utils=window.AFKJ.utils;const config=window.AFKJ.config;const chips=window.AFKJ.chips;const tiers=window.AFKJ.tiers;const skills=window.AFKJ.skills;const markdown=window.AFKJ.markdown;const gridView=window.AFKJ.views.grid;const escapeHtml=utils.escapeHtml.bind(utils);const BENEFIT_MAX_STARS=5;const BENEFIT_MIN_STARS=1;const BENEFIT_STAR="⭐";function clampBenefitRating(scoreRating){const rating=Number(scoreRating);if(!isFinite(rating)){return 0;}
return Math.max(BENEFIT_MIN_STARS,Math.min(BENEFIT_MAX_STARS,rating));}
function boxedRatingIconCount(rating){const clamped=clampBenefitRating(rating);if(!clamped){return 0;}
return Math.max(BENEFIT_MIN_STARS,Math.min(BENEFIT_MAX_STARS,Math.round(clamped)));}
function renderCompactRatingIcons(filledCount,glyph){const emptyCount=BENEFIT_MAX_STARS-filledCount;let html="";for(let i=0;i<BENEFIT_MAX_STARS;i++){if(i<emptyCount){html+='<span class="compact-rating-icon compact-rating-icon--empty" aria-hidden="true"></span>';}else{html+='<span class="compact-rating-icon" aria-hidden="true">'+
glyph+"</span>";}}
return html;}
function renderBoxedCompactScore(filledCount,glyph,tooltip,modifierClass){if(!filledCount||!glyph){return"";}
const classes="hero-compact-score hero-compact-score--boxed";return('<div class="'+
classes+
(modifierClass?" "+modifierClass:"")+'" title="'+
escapeHtml(tooltip)+'" aria-label="'+
escapeHtml(tooltip)+'">'+
renderCompactRatingIcons(filledCount,glyph)+"</div>");}
function formatBeneficiaryRatingDisplay(scoreRating){const count=boxedRatingIconCount(scoreRating);if(!count){return"";}
return BENEFIT_STAR.repeat(count);}
function beneficiaryScoreTooltip(scoreRating){const clamped=clampBenefitRating(scoreRating);if(!clamped){return"Benefit rating out of 5";}
return"Benefit rating: "+clamped.toFixed(1)+" out of 5";}
function renderBeneficiaryScore(scoreRating){const count=boxedRatingIconCount(scoreRating);return renderBoxedCompactScore(count,BENEFIT_STAR,beneficiaryScoreTooltip(scoreRating));}
function replacementScoreRating(score){const value=Number(score);if(!isFinite(value)||value<=0){return BENEFIT_MIN_STARS;}
return Math.max(BENEFIT_MIN_STARS,Math.min(BENEFIT_MAX_STARS,BENEFIT_MIN_STARS+(BENEFIT_MAX_STARS-BENEFIT_MIN_STARS)*value));}
function replacementRatingIconCount(score){return boxedRatingIconCount(replacementScoreRating(score));}
function replacementScoreTooltip(score){const value=Number(score);if(!isFinite(value)){return"Replacement fit";}
return"Replacement fit: "+Math.round(value*100)+"%";}
function renderReplacementScore(score,categoryLabel){const icon=replacementCategoryIcon(categoryLabel);const count=replacementRatingIconCount(score);const glyph=icon||"•";return renderBoxedCompactScore(count,glyph,replacementScoreTooltip(score),"hero-compact-score--replacement");}
function renderHeroCompactCard(slug,name,bodyHtml,footerHtml,headerHtml){const hero=window.AFKJ.state.heroBySlug[slug];const factionKey=hero?utils.factionDataKey(hero.faction):"";const portraitHero=hero||{name:name,faction:""};const portraitHtml=gridView.renderHeroPortrait(portraitHero,"compact-portrait");return('<article class="hero-compact-card afkj-box afkj-box-sm" data-slug="'+
escapeHtml(slug)+'" data-faction="'+
escapeHtml(factionKey)+'" tabindex="0" role="link" aria-label="'+
escapeHtml(name)+'">'+'<div class="hero-compact-portrait-wrap">'+
portraitHtml+"</div>"+'<div class="hero-compact-body">'+'<div class="hero-compact-header">'+'<div class="hero-compact-name">'+
utils.linkifyHero(name,slug)+"</div>"+
(headerHtml||"")+"</div>"+
(bodyHtml||"")+
(footerHtml||"")+"</div></article>");}
function renderHeroRowCard(slug,name,bodyHtml){const hero=window.AFKJ.state.heroBySlug[slug];const portraitSrc=utils.assetUrl(utils.characterPortraitPath(hero||{name:name}));return('<article class="hero-row-card" data-slug="'+
escapeHtml(slug)+'" tabindex="0" role="link" aria-label="'+
escapeHtml(name)+'">'+'<img src="'+
escapeHtml(portraitSrc)+'" alt="" loading="lazy" onerror="this.style.opacity=0.3">'+'<div class="hero-row-body">'+'<div class="hero-row-name">'+
utils.linkifyHero(name,slug)+"</div>"+
(bodyHtml||"")+"</div></article>");}
function renderHeroRowList(items,layoutClass){if(!items.length){return"";}
return('<div class="hero-row-list'+
(layoutClass?" "+layoutClass:"")+'">'+
items.join("")+"</div>");}
function parseSkillOverviewMetricEntry(entry){const match=entry.trim().match(/^(.+?)\s+`(high|average|low|slow|fast)`$/i);if(!match){return null;}
return{label:match[1].trim(),value:match[2].trim(),};}
function formatSkillOverviewRow(labelHtml,pillsHtml){if(pillsHtml){return('<span class="skill-overview-label">'+
labelHtml+"</span>"+'<span class="skill-overview-pills">'+
pillsHtml+"</span>");}
return'<span class="skill-overview-full">'+labelHtml+"</span>";}
function renderDamageTypeEntry(typeName,quality){const merged=chips.mergeEffectWithQuality(typeName,quality);if(merged){return merged;}
const typeChip=chips.tryChipify(typeName);const qualityChip=chips.formatTag(quality);return((typeChip!==null?typeChip:escapeHtml(typeName))+" "+
qualityChip);}
function renderDamageTypesOverviewLine(text){const match=text.match(/^\*\*Damage types\*\*:\s*(.+)$/i);if(!match){return null;}
const entries=match[1].split(/\s*,\s*/).map(function(s){return s.trim();}).filter(Boolean);const rendered=entries.map(function(entry){const parsed=parseSkillOverviewMetricEntry(entry);if(!parsed){return chips.renderInline(entry);}
return renderDamageTypeEntry(parsed.label,parsed.value);});return formatSkillOverviewRow("<strong>Damage types</strong>",rendered.join(""));}
function formatMovementChip(text){const trimmed=text.trim();if(!trimmed){return null;}
const lower=trimmed.toLowerCase();for(let i=0;i<chips.MOVEMENT_KEYS.length;i++){const key=chips.MOVEMENT_KEYS[i];if(lower===key.toLowerCase()){const def=chips.MOVEMENT_DEFINITIONS[key];return chips.chipSpan(def.emoji,trimmed,def.cls);}}
return null;}
function renderSignatureSkillLine(text,hero){const match=text.match(/^\*\*Signature skill\*\*:\s*(.+)$/i);if(!match){return null;}
const body=match[1].trim();let pillsHtml;if(hero&&hero.signatureSkill){pillsHtml='<a href="#" class="signature-skill-link" data-skill-category="'+
escapeHtml(hero.signatureSkill.category)+'">'+
escapeHtml(body)+"</a>";}else{pillsHtml=escapeHtml(body);}
return formatSkillOverviewRow("<strong>Signature skill</strong>",pillsHtml);}
function renderMovementLine(text){const match=text.match(/^\*\*Movement\*\*:\s*(.+)$/i);if(!match){return null;}
const rest=match[1].trim();const paren=rest.match(/^(.+?)\s*(\([^)]+\))\s*$/);const base=paren?paren[1].trim():rest;const suffix=paren?" "+escapeHtml(paren[2]):"";const chip=formatMovementChip(base);return formatSkillOverviewRow("<strong>Movement</strong>",(chip!==null?chip:escapeHtml(base))+suffix);}
function renderBehaviorTagsLine(text){const match=text.match(/^\*\*Behavior tags\*\*:\s*(.+)$/i);if(!match){return null;}
const tags=match[1].match(/`([^`]+)`/g);if(!tags||!tags.length){return null;}
const tagChips=tags.map(function(raw){return chips.behaviorTagChip(raw.slice(1,-1),true);}).join(" ");return formatSkillOverviewRow("<strong>Behavior tags</strong>",'<span class="behavior-tags-cell">'+tagChips+"</span>");}
function renderSkillOverviewMetric(text){const trimmed=text.trim();const parsed=parseSkillOverviewMetricEntry(trimmed);if(!parsed){return chips.renderInline(trimmed);}
const labelParts=chips.parseEffectLabelParts(parsed.label);if(chips.isSpeedMetricLabel(labelParts.base)){return(chips.mergeLabelWithIndicator(labelParts.base,parsed.value,labelParts.tier)||chips.renderSummaryEffectChip(labelParts.base,labelParts.tier,parsed.value));}
return(chips.mergeEffectWithQuality(labelParts.base,parsed.value,labelParts.tier)||chips.mergeLabelWithIndicator(labelParts.base,parsed.value,labelParts.tier)||chips.renderSummaryEffectChip(labelParts.base,labelParts.tier,parsed.value));}
function renderSkillOverviewItem(text){if(renderDamageTypesOverviewLine(text)!==null){return"";}
const colonMatch=text.match(/^(.+?:\s*)(.+)$/);if(colonMatch){const segments=colonMatch[2].trim().split(/\s*,\s*/).filter(Boolean);const allMetrics=segments.length>0&&segments.every(function(segment){return parseSkillOverviewMetricEntry(segment.trim())!==null;});if(allMetrics){const parsedSegments=segments.map(function(segment){return parseSkillOverviewMetricEntry(segment.trim());});const speedEntry=parsedSegments.find(function(entry){return entry&&entry.label.trim().toLowerCase()==="speed";});const filteredSegments=segments.filter(function(segment){const entry=parseSkillOverviewMetricEntry(segment.trim());if(entry&&entry.label.trim().toLowerCase()==="first cast speed"&&speedEntry&&entry.value.toLowerCase()===speedEntry.value.toLowerCase()){return false;}
return true;});const pills=filteredSegments.map(function(segment){return renderSkillOverviewMetric(segment);});return formatSkillOverviewRow(chips.renderInline(colonMatch[1].trim().replace(/:\s*$/,"")),pills.join(""));}}
return chips.renderInline(text);}
function renderBehaviorItem(text,options){const hero=options&&options.behaviorHero;const signature=renderSignatureSkillLine(text,hero);if(signature!==null){return signature;}
const movement=renderMovementLine(text);if(movement!==null){return movement;}
const behaviorTags=renderBehaviorTagsLine(text);if(behaviorTags!==null){return behaviorTags;}
const damageTypes=renderDamageTypesOverviewLine(text);if(damageTypes!==null){return damageTypes;}
const colonMatch=text.match(/^\*\*(.+?)\*\*:\s*(.+)$/);if(colonMatch){const label=colonMatch[1].trim();return formatSkillOverviewRow("<strong>"+escapeHtml(label)+"</strong>",chips.renderInline(colonMatch[2].trim()));}
return chips.renderInline(text);}
const SYNERGY_TARGETING_TOKENS={"single target":true,"multiple targets":true,"all units":true,area:true,arc:true,global:true,self:true,allies:true,enemies:true,"on skill":true,"all summons":true,"owned summons":true,"summons only":true,};const SYNERGY_QUALITY_TOKENS={low:true,average:true,high:true,};function splitSynergyReasonDetail(text){const match=text.match(/^(.+?)\s*\((.+)\)\s*$/);if(!match){return{label:text.trim(),quality:"",conditional:"",modifiers:[],};}
let label=match[1].trim();let inner=match[2].trim();let conditional="";const condMatch=inner.match(/(?:,\s*)?conditional\s*\(([^)]+)\)\s*$/i);if(condMatch){conditional=condMatch[1].trim();inner=inner.slice(0,condMatch.index).replace(/,\s*$/,"").trim();}
let quality="";const modifiers=[];inner.split(/\s*,\s*/).forEach(function(part){const trimmed=part.trim();if(!trimmed){return;}
const lower=trimmed.toLowerCase();if(SYNERGY_QUALITY_TOKENS[lower]){quality=lower;return;}
if(SYNERGY_TARGETING_TOKENS[lower]){return;}
modifiers.push(trimmed);});return{label:label,quality:quality,conditional:conditional,modifiers:modifiers,};}
function stripSynergyReasonTargeting(text){const detail=splitSynergyReasonDetail(text);const kept=detail.modifiers.slice();if(detail.quality){kept.push(detail.quality);}
if(detail.conditional){kept.push("conditional ("+detail.conditional+")");}
if(!kept.length){return detail.label;}
return detail.label+" ("+kept.join(", ")+")";}
function parseSynergyReason(reason){let text=chips.normalizeSummaryText(reason);let signatureFuel=false;if(/`signature fuel`\s*$/i.test(text)){signatureFuel=true;text=text.replace(/`signature fuel`\s*$/i,"").trim();}
if(/^Enables /i.test(text)||/^Grants /i.test(text)){return{type:"enable",text:stripSynergyReasonTargeting(text),};}
const viaIdx=text.toLowerCase().indexOf(" via ");if(viaIdx!==-1){text=text.slice(viaIdx+5).trim();}
const detail=splitSynergyReasonDetail(text);const parsed=chips.parseEffectLabelParts(detail.label);return{type:"effect",base:parsed.base,tier:parsed.tier,quality:detail.quality,conditional:detail.conditional,signatureFuel:signatureFuel,};}
function synergyReasonKey(parsed){return[parsed.base,parsed.tier,parsed.quality,parsed.conditional,parsed.signatureFuel?"1":"0",].join("|");}
function chipifySynergyEnableLabel(text){const direct=chips.tryChipify(text);if(direct){return direct;}
return escapeHtml(text);}
function chipifySynergyEnableDetail(text){const detail=splitSynergyReasonDetail(text);const parsed=chips.parseEffectLabelParts(detail.label);const parts=parsed.base.split(/\s+\+\s+/);function renderPart(part,applyQuality){const partParsed=chips.parseEffectLabelParts(part.trim());const polarity=chips.effectLabelPolarity(partParsed.base)||"buff";return chips.renderMergedEffectPill(partParsed.base,applyQuality?detail.quality:"",applyQuality?parsed.tier||partParsed.tier:partParsed.tier,applyQuality?detail.conditional:"",polarity);}
if(parts.length===1){return renderPart(parts[0],true);}
return parts.map(function(part,idx){const applyQuality=idx===parts.length-1&&!!detail.quality;return renderPart(part,applyQuality);}).join(" + ");}
function renderSynergyEnableLine(text){if(/^Grants /i.test(text)){return escapeHtml(text);}
const viaIdx=text.toLowerCase().indexOf(" via ");if(viaIdx===-1){return chipifySynergyEnableLabel(text);}
const prefix=text.slice(0,viaIdx).trim();const effect=text.slice(viaIdx+5).trim();const enableMatch=prefix.match(/^Enables\s+(.+)$/i);const enableLabel=enableMatch?enableMatch[1].trim():prefix;return("Enables "+
chipifySynergyEnableLabel(enableLabel)+" via "+
chipifySynergyEnableDetail(effect));}
function renderSynergyPartnerExplanation(reasons,options){if(!reasons||!reasons.length){return"";}
options=options||{};const prioritizeSignatureFuel=!!options.prioritizeSignatureFuel;const effects=[];const enables=[];const seen=Object.create(null);reasons.forEach(function(reason){const parsed=parseSynergyReason(reason);if(parsed.type==="enable"){enables.push(parsed.text);return;}
const key=synergyReasonKey(parsed);if(seen[key]){return;}
seen[key]=true;effects.push(parsed);});let html="";if(effects.length){const hasSignatureFuel=prioritizeSignatureFuel&&effects.some(function(effect){return effect.signatureFuel;});const pillsClass="synergy-partner-pills"+
(hasSignatureFuel?" synergy-partner-pills-has-signature-fuel":"");function renderEffectPill(effect,inlineSignatureFuel){let pill=chips.renderMergedEffectPill(effect.base,effect.quality,effect.tier,"");if(inlineSignatureFuel&&effect.signatureFuel){pill+=" "+chips.formatTag("signature fuel");}
return'<span class="synergy-partner-pill">'+pill+"</span>";}
if(hasSignatureFuel){const fuelEffects=effects.filter(function(effect){return effect.signatureFuel;});const otherEffects=effects.filter(function(effect){return!effect.signatureFuel;});html+='<div class="'+pillsClass+'">';html+='<div class="synergy-partner-fuel-row">';html+='<span class="synergy-partner-signature-fuel">'+
chips.formatTag("signature fuel")+"</span>";fuelEffects.forEach(function(effect){html+=renderEffectPill(effect,false);});html+="</div>";if(otherEffects.length){html+='<div class="synergy-partner-other-pills">';otherEffects.forEach(function(effect){html+=renderEffectPill(effect,false);});html+="</div>";}
html+="</div>";}else{html+='<div class="'+pillsClass+'">';effects.forEach(function(effect){html+=renderEffectPill(effect,true);});html+="</div>";}}
if(enables.length){html+='<div class="synergy-partner-specials">';enables.forEach(function(line){html+='<div class="synergy-partner-special">'+
renderSynergyEnableLine(line)+"</div>";});html+="</div>";}
return html;}
function synergyPartnerScoreRating(ref){const rating=ref.scoreRating!=null?ref.scoreRating:ref.score_rating;const value=Number(rating);return Number.isFinite(value)?value:0;}
function sortSynergyHeroes(heroes){return heroes.slice().sort(function(a,b){const aRating=a.scoreRating!=null?a.scoreRating:a.score_rating;const bRating=b.scoreRating!=null?b.scoreRating:b.score_rating;if(bRating!==aRating){return bRating-aRating;}
return String(a.name||"").localeCompare(String(b.name||""));});}
function renderSynergyHeroCard(ref,bodyHtml){const scoreHtml=renderBeneficiaryScore(ref.scoreRating!=null?ref.scoreRating:ref.score_rating);return renderHeroCompactCard(ref.slug,ref.name,bodyHtml||"","",scoreHtml);}
function renderSynergyHeroGrid(heroes,bodyForHero){if(!heroes||!heroes.length){return"";}
return renderHeroRowList(sortSynergyHeroes(heroes).map(function(hero){return renderSynergyHeroCard(hero,bodyForHero(hero));}),"hero-compact-grid-2");}
function renderInlineHeroPortrait(slug,name){const hero=window.AFKJ.state.heroBySlug[slug];const factionKey=hero?utils.factionDataKey(hero.faction):"";const portraitSrc=utils.assetUrl(utils.characterPortraitPath(hero||{name:name}));return('<span class="inline-hero-hex" data-faction="'+
escapeHtml(factionKey)+'" aria-hidden="true">'+'<span class="inline-hero-hex-wrap">'+'<span class="inline-hero-hex-inner">'+'<img class="inline-hero-hex-icon" src="'+
escapeHtml(portraitSrc)+'" alt="" loading="lazy" onerror="this.style.opacity=0.3">'+"</span></span></span>");}
function synergyIntroWithoutCommonBuffers(intro){if(!intro){return"";}
return intro.split("\n").filter(function(line){return!/^Common buffers are /i.test(line.trim());}).join("\n").trim();}
function renderCommonBuffers(buffers){if(!buffers||!buffers.length){return"";}
const chips=window.AFKJ.chips;const items=buffers.map(function(ref){return chips.renderCharacterPill(ref.name);});return('<div class="synergy-common-buffers">Common buffers are '+
joinIntroFragments(items)+".</div>");}
function renderSynergyOverflowTooltipGrid(partners){const names=partners.slice().sort(function(a,b){const ratingDiff=synergyPartnerScoreRating(b)-synergyPartnerScoreRating(a);if(ratingDiff!==0){return ratingDiff;}
return a.name.localeCompare(b.name);}).map(function(ref){return ref.name;});return('<div class="synergy-overflow-tip-grid">'+
names.map(function(name){return"<span>"+escapeHtml(name)+"</span>";}).join("")+"</div>");}
function renderSynergyPartnerOverflow(morePartners){if(!morePartners||!morePartners.length){return"";}
const overflowCount=morePartners.length;const unitLabel=overflowCount===1?"unit":"units";const moreUnitsPhrase=overflowCount+" more "+unitLabel;if(overflowCount<=5){return('<p class="synergy-partner-overflow">There were '+'<span class="synergy-overflow-trigger chip-has-tip" data-tip-html="'+
escapeHtml(renderSynergyOverflowTooltipGrid(morePartners))+'" tabindex="0" role="button" aria-describedby="chip-tooltip">'+
moreUnitsPhrase+"</span> detected.</p>");}
const highRated=morePartners.filter(function(ref){return synergyPartnerScoreRating(ref)>2;});const highCount=highRated.length;let html='<p class="synergy-partner-overflow">There were '+
overflowCount+" more "+
unitLabel+" detected of which ";if(highCount>0){html+='<span class="synergy-overflow-trigger chip-has-tip" data-tip-html="'+
escapeHtml(renderSynergyOverflowTooltipGrid(highRated))+'" tabindex="0" role="button" aria-describedby="chip-tooltip">'+
highCount+" score higher</span>";}else{html+=highCount+" score higher";}
html+=" than 2.</p>";return html;}
function renderSynergies(sections,heroName){const syn=sections.benefits_from;if(!syn)return"";let html='<div class="detail-section synergy-section">';html+="<h2>Units improving "+escapeHtml(heroName)+"</h2>";if(syn.intro||(syn.common_buffers&&syn.common_buffers.length)){const introText=synergyIntroWithoutCommonBuffers(syn.intro);const buffersHtml=renderCommonBuffers(syn.common_buffers);if(introText||buffersHtml){html+='<div class="synergy-intro-block">';if(introText){html+='<div class="synergy-intro">'+
chips.renderInline(introText.replace(/\n/g," "))+"</div>";}
html+=buffersHtml;html+="</div>";}}
if(syn.requires&&syn.requires.text){html+='<div class="synergy-requires"><p>'+
chips.renderInline(syn.requires.text)+"</p></div>";}
if(syn.partners&&syn.partners.length){html+=renderSynergyHeroGrid(syn.partners,function(partner){return renderSynergyPartnerExplanation(partner.reasons,{prioritizeSignatureFuel:true,});});html+=renderSynergyPartnerOverflow(syn.more_partners);}else{html+="<p><em>No synergy partners matched stat buffs or enablers.</em></p>";}
html+="</div>";if(syn.benefited_by){html+=renderBenefitedBySection(syn.benefited_by,heroName);}
return html;}
function joinIntroFragments(fragments){if(!fragments.length){return"";}
if(fragments.length===1){return fragments[0];}
if(fragments.length===2){return fragments[0]+" and "+fragments[1];}
return(fragments.slice(0,-1).join(", ")+", and "+
fragments[fragments.length-1]);}
function renderBuffsProvidedIntro(data){if(!data||!data.buffs||!data.buffs.length){return"";}
const entries=data.buffs.map(chips.renderBuffProvidedEntry);return(escapeHtml(data.hero+" provides ")+'<span class="synergy-buff-pills">'+
joinIntroFragments(entries)+"</span>.");}
function renderBenefitedBySection(bb,heroName){const hasHeroes=bb.heroes&&bb.heroes.length;const hasOverflow=bb.intro||(bb.overflow_reasons&&bb.overflow_reasons.length)||bb.strongest_note;const buffsProvided=bb.buffs_provided||null;if(!buffsProvided&&!bb.buffs_intro&&!hasHeroes&&!hasOverflow){return"";}
let html='<div class="detail-section synergy-section synergy-benefited-by-section">';html+="<h2>Units benefitting most from "+escapeHtml(heroName)+"</h2>";if(buffsProvided){html+='<div class="synergy-intro">'+
renderBuffsProvidedIntro(buffsProvided)+"</div>";}else if(bb.buffs_intro){html+='<div class="synergy-intro">'+
chips.renderInline(bb.buffs_intro)+"</div>";}
if(bb.intro){html+='<div class="synergy-intro">'+
chips.renderInline(bb.intro.replace(/\n/g," "))+"</div>";}
if(bb.overflow_reasons&&bb.overflow_reasons.length){html+="<ul>";bb.overflow_reasons.forEach(function(r){html+="<li>"+chips.renderInline(r)+"</li>";});html+="</ul>";}
if(bb.strongest_note){html+='<div class="synergy-intro">'+
chips.renderInline(bb.strongest_note)+"</div>";}
if(hasHeroes){html+=renderSynergyHeroGrid(bb.heroes,function(hero){return renderSynergyPartnerExplanation(hero.reasons);});}
html+="</div>";return html;}
function replacementCategoryIcon(label){return config.REPLACEMENT_CATEGORY_ICONS[label]||"";}
function replacementCategoryClass(label){const classes={"Best overall replacement":"replacement-category--overall","Buffs on allies":"replacement-category--buff","Energy provider":"replacement-category--energy",Healing:"replacement-category--healing","Similar Skills":"replacement-category--similar",Damage:"replacement-category--damage","Debuffs on enemies":"replacement-category--debuff","Crowd Control":"replacement-category--cc",};return classes[label]||"replacement-category--generic";}
function renderReplacementCategoryHeading(label){const icon=replacementCategoryIcon(label);if(!icon){return"<h4>"+escapeHtml(label)+"</h4>";}
return("<h4>"+'<span class="replacement-category-icon" aria-hidden="true">'+
icon+"</span> "+
escapeHtml(label)+"</h4>");}
function renderReplacements(sections,mainHero){const reps=sections.replacements;if(!reps||!reps.length)return"";let html='<div class="detail-section">';html+="<h2>Replacement options</h2>";reps.forEach(function(cat){html+='<div class="replacement-category '+
replacementCategoryClass(cat.category)+'">';html+=renderReplacementCategoryHeading(cat.category);html+=renderHeroRowList(cat.entries.map(function(e){let body="";if(e.detail){body='<div class="hero-compact-detail">'+
chips.renderInline(e.detail)+"</div>";}
let footer="";const repHero=window.AFKJ.state.heroBySlug[e.slug];if(repHero){footer=tiers.renderPrydwenTierBoxes(tiers.getHeroPrydwenTiers(repHero),"compact",mainHero?tiers.getHeroPrydwenTiers(mainHero):null,mainHero&&mainHero.name);}
let header="";if(e.score!=null){header=renderReplacementScore(e.score,cat.category);}
return renderHeroCompactCard(e.slug,e.name,body,footer,header);}),"hero-compact-grid-3");html+="</div>";});html+="</div>";return html;}
function renderRoleCategoryIcon(roleCategory){const icon=config.ROLE_CATEGORY_ICONS[roleCategory];if(!icon){return"";}
const parts=icon.viewBox.split(/\s+/).map(Number);const iconCx=parts[0]+parts[2]/2;const iconCy=parts[1]+parts[3]/2;const iconScale=13.5/Math.max(parts[2],parts[3]);return('<span class="role-category-icon" aria-hidden="true">'+'<svg class="role-category-icon-svg" viewBox="0 0 24 24" focusable="false">'+'<circle class="role-category-icon-bg" cx="12" cy="12" r="10.5"/>'+'<g transform="translate(12 12) scale('+
iconScale+") translate("+
-iconCx+" "+
-iconCy+')">'+'<path class="role-category-icon-shape" d="'+
icon.path+'"/>'+"</g></svg></span>");}
function renderRoleCategoryBadge(heroOrCategory,options){const key=typeof heroOrCategory==="string"?heroOrCategory:heroOrCategory.roleCategory;const meta=window.AFKJ.tiers.roleCategoryMeta(key)||config.ROLE_CATEGORY_META[key];if(!meta){return"";}
const useSheetIcon=options&&options.sheetIcon===true;const iconHtml=useSheetIcon?renderRoleCategoryIcon(key):'<span class="badge-emoji" aria-hidden="true">'+
meta.emoji+"</span>";const badgeClass=meta.className+(useSheetIcon?" badge-role-with-icon":"");return('<span class="badge '+
badgeClass+'">'+
iconHtml+
escapeHtml(meta.label)+"</span>");}
function renderBadges(hero,options){const includeRoleCategory=options&&options.includeRoleCategory===true;const badges=[];if(hero.faction){const icon=utils.iconPath("factions",hero.faction);badges.push('<span class="badge '+
utils.factionClass(hero.faction)+'">'+
(icon?'<img src="'+utils.assetUrl(icon)+'" alt="" loading="lazy">':"")+
escapeHtml(hero.faction)+"</span>");}
if(hero.class){const icon=utils.iconPath("class",hero.class);badges.push('<span class="badge">'+
(icon?'<img src="'+utils.assetUrl(icon)+'" alt="" loading="lazy">':"")+
escapeHtml(hero.class)+"</span>");}
if(includeRoleCategory){const roleBadge=renderRoleCategoryBadge(hero,{sheetIcon:true});if(roleBadge){badges.push(roleBadge);}}
if(hero.damage_type){const dmgDef=config.TAG_DEFINITIONS[hero.damage_type];badges.push('<span class="badge">'+
(dmgDef?'<span class="badge-emoji" aria-hidden="true">'+
dmgDef.emoji+"</span>":"")+
escapeHtml(hero.damage_type)+"</span>");}
return badges.join("");}
const REPLACEMENT_ALGORITHM_URL="https://github.com/arnecls/afjk-characters/blob/main/docs/replacement-algorithm.md";function renderAlgorithmDisclaimer(){return('<div class="replacement-warning" role="note">'+'<p class="replacement-warning-text"><span class="replacement-warning-icon" aria-hidden="true">⚠️ </span>'+"The sections below are not curated lists but have been <a href=\""+
REPLACEMENT_ALGORITHM_URL+'" target="_blank" rel="noopener noreferrer">detected by an algorithm</a>.</p>'+"</div>");}
function renderSummaryCards(md){const cards=[];let current=null;md.split("\n").forEach(function(line){if(line.startsWith("### Summary")){return;}
if(line.startsWith("#### ")){if(current){cards.push(current);}
const cardTitle=line.slice(5).trim();if(/ Requires$/i.test(cardTitle)){current=null;return;}
current={title:cardTitle,items:[]};return;}
if(line.startsWith("- ")&&current){current.items.push(line.slice(2));}});if(current){cards.push(current);}
if(!cards.length){return"";}
let html='<div class="detail-section summary-section">';html+="<h2>Summary</h2>";html+='<div class="summary-grid">';cards.forEach(function(card){html+='<div class="summary-card">';html+="<h4>"+chips.renderInline(card.title)+"</h4>";if(card.items.length){html+="<ul>";const polarity=chips.summaryCardPolarity(card.title);chips.groupSummaryItems(card.items,polarity).forEach(function(item){if(item.type==="group"){html+="<li>"+chips.renderGroupedVariantPill(item.variants)+"</li>";return;}
html+="<li>"+chips.renderRichLine(item.item,polarity)+"</li>";});html+="</ul>";}
html+="</div>";});html+="</div>";html+="</div>";return html;}
function splitBehavior(md){const marker="#### Skill overview";const idx=md.indexOf(marker);if(idx===-1){return{behavior:md,skillOverview:null};}
return{behavior:md.slice(0,idx).trim(),skillOverview:md.slice(idx).trim(),};}
function splitBehaviorHeading(md){if(!md){return{title:"",body:""};}
const lines=md.split("\n");const firstLine=lines[0].trim();if(firstLine.startsWith("### ")){return{title:firstLine.slice(4).trim(),body:lines.slice(1).join("\n").trim(),};}
return{title:"",body:md.trim()};}
function renderSkillOverviewMetrics(md){if(!md){return"";}
const metrics=stripSkillSummarySubsections(stripSkillOverviewDamageTypesLine(md));const lines=metrics.split("\n").filter(function(line){return!line.startsWith("#### ");});return markdown.renderMarkdown(lines.join("\n"),{skillOverview:true});}
function stripSkillSummarySubsections(md){if(!md)return"";return md.replace(/^\s*####\s+[^\n]*\n?/gm,"");}
function stripSkillOverviewDamageTypesLine(md){return md.replace(/\n- \*\*Damage types\*\*:[^\n]*/gi,"");}
function renderStatsOverviewRow(entries,rowKind){if(!entries||!entries.length){return"";}
return entries.map(function(entry){if(rowKind==="category"){return chips.renderClassRankCategoryPill(entry);}
return chips.renderClassRankMergedPill(entry.label,entry.rank,"buff",true);}).join("");}
function renderStatsOverview(statsOverview){if(!statsOverview){return"";}
const categories=renderStatsOverviewRow(statsOverview.categories,"category");const stats=renderStatsOverviewRow(statsOverview.stats,"stat");if(!categories&&!stats){return"";}
let html='<div class="detail-section summary-section skill-overview-section stats-overview-section">';html+="<h2>Stats overview</h2>";html+='<div class="skill-overview-metrics stats-overview-pills">';if(categories){html+='<div class="stats-overview-row">'+categories+"</div>";}
if(stats){html+='<div class="stats-overview-row">'+stats+"</div>";}
html+="</div></div>";return html;}
function highlightSkillCard(category){const state=window.AFKJ.state;if(!category||!state.dom.heroDetail){return;}
const card=state.dom.heroDetail.querySelector('.skill-card[data-skill-category="'+category+'"]');if(!card||card.classList.contains("skill-card-highlight")){return;}
function onHighlightEnd(event){if(event.animationName!=="skill-card-glow"){return;}
card.classList.remove("skill-card-highlight");card.removeEventListener("animationend",onHighlightEnd);}
card.addEventListener("animationend",onHighlightEnd);card.classList.add("skill-card-highlight");}
function showDetail(hero){const state=window.AFKJ.state;state.closeSkillCardPopover();state.detailHero=hero;state.dom.gridView.classList.add("hidden");state.dom.listView.classList.add("hidden");if(state.dom.mixView){state.dom.mixView.classList.add("hidden");}
state.dom.detailView.classList.remove("hidden");let html='<div class="detail-panel afkj-box afkj-box-lg">';html+='<div class="detail-header">';html+='<div class="detail-portrait-wrap afkj-box afkj-box-sm">'+
gridView.renderHeroPortrait(hero,"detail-portrait")+"</div>";html+='<div class="detail-title">';html+="<h1>"+escapeHtml(hero.name)+"</h1>";if(hero.season!=null&&hero.seasonNumber!=null){html+='<p class="detail-subtitle"><b>Season:</b> '+
escapeHtml(hero.season)+" (S"+
hero.seasonNumber+")</p>";}else if(hero.season){html+='<p class="detail-subtitle"><b>Season:</b> '+
escapeHtml(hero.season)+"</p>";}
html+='<div class="badges badges-left">'+
renderBadges(hero,{includeRoleCategory:true})+"</div>";if(hero.description){html+='<p class="detail-desc">'+escapeHtml(hero.description)+"</p>";}
html+="</div></div>";if(hero.sections.behavior){const parts=splitBehavior(hero.sections.behavior);if(parts.behavior){html+='<div class="detail-section summary-section skill-overview-section">';html+=tiers.renderPrydwenTierBoxes(tiers.getHeroPrydwenTiers(hero));const behaviorMd=tiers.stripPrydwenTierLine(parts.behavior);const behaviorParts=splitBehaviorHeading(behaviorMd);if(behaviorParts.title){html+="<h2>"+escapeHtml(behaviorParts.title)+"</h2>";}
if(behaviorParts.body){html+='<div class="skill-overview-metrics">';html+=markdown.renderMarkdown(behaviorParts.body,{behaviorHero:hero,behaviorSection:true,});html+="</div>";}
html+="</div>";}
if(hero.sections.statsOverview){html+=renderStatsOverview(hero.sections.statsOverview);}
if(parts.skillOverview||(hero.sections.skillCards&&hero.sections.skillCards.length)){html+='<div class="detail-section summary-section skill-overview-section">';html+="<h2>Skill overview</h2>";if(parts.skillOverview){const metricsHtml=renderSkillOverviewMetrics(parts.skillOverview);html+='<div class="skill-overview-metrics">'+metricsHtml+"</div>";}
if(hero.sections.skillCards&&hero.sections.skillCards.length){html+=skills.renderSkillCards(hero.sections.skillCards,hero);}
html+="</div>";}}
if(hero.sections.summary){html+=renderSummaryCards(hero.sections.summary);}
html+="</div>";html+=renderAlgorithmDisclaimer();const synergyHtml=renderSynergies(hero.sections,hero.name);if(synergyHtml){html+='<div class="detail-panel afkj-box afkj-box-lg">';html+=synergyHtml;html+="</div>";}
const replacementHtml=renderReplacements(hero.sections,hero);if(replacementHtml){html+='<div class="detail-panel afkj-box afkj-box-lg">';html+=replacementHtml;html+="</div>";}
state.dom.heroDetail.innerHTML=html;state.dom.heroDetail.setAttribute("data-faction",utils.factionDataKey(hero.faction)||"");document.title=hero.name+" — AFK Journey Heroes";window.AFKJ.ui.updateHeaderNav(true);window.scrollTo(0,0);}
window.AFKJ.views.detail={formatBeneficiaryRatingDisplay:formatBeneficiaryRatingDisplay,renderBeneficiaryScore:renderBeneficiaryScore,renderHeroCompactCard:renderHeroCompactCard,renderHeroRowCard:renderHeroRowCard,renderHeroRowList:renderHeroRowList,renderDamageTypesOverviewLine:renderDamageTypesOverviewLine,formatMovementChip:formatMovementChip,renderSignatureSkillLine:renderSignatureSkillLine,renderMovementLine:renderMovementLine,renderBehaviorTagsLine:renderBehaviorTagsLine,renderSkillOverviewMetric:renderSkillOverviewMetric,renderSkillOverviewItem:renderSkillOverviewItem,renderBehaviorItem:renderBehaviorItem,splitSynergyReasonDetail:splitSynergyReasonDetail,stripSynergyReasonTargeting:stripSynergyReasonTargeting,parseSynergyReason:parseSynergyReason,synergyReasonKey:synergyReasonKey,chipifySynergyEnableLabel:chipifySynergyEnableLabel,chipifySynergyEnableDetail:chipifySynergyEnableDetail,renderSynergyEnableLine:renderSynergyEnableLine,renderSynergyPartnerExplanation:renderSynergyPartnerExplanation,sortSynergyHeroes:sortSynergyHeroes,renderSynergyHeroCard:renderSynergyHeroCard,renderSynergyHeroGrid:renderSynergyHeroGrid,renderInlineHeroPortrait:renderInlineHeroPortrait,synergyIntroWithoutCommonBuffers:synergyIntroWithoutCommonBuffers,renderCommonBuffers:renderCommonBuffers,renderSynergyOverflowTooltipGrid:renderSynergyOverflowTooltipGrid,renderSynergyPartnerOverflow:renderSynergyPartnerOverflow,renderSynergies:renderSynergies,joinIntroFragments:joinIntroFragments,renderBuffsProvidedIntro:renderBuffsProvidedIntro,renderBenefitedBySection:renderBenefitedBySection,renderReplacements:renderReplacements,renderRoleCategoryIcon:renderRoleCategoryIcon,renderRoleCategoryBadge:renderRoleCategoryBadge,renderBadges:renderBadges,renderAlgorithmDisclaimer:renderAlgorithmDisclaimer,renderSummaryCards:renderSummaryCards,splitBehavior:splitBehavior,splitBehaviorHeading:splitBehaviorHeading,renderSkillOverviewMetrics:renderSkillOverviewMetrics,renderStatsOverview:renderStatsOverview,highlightSkillCard:highlightSkillCard,showDetail:showDetail,};})();window.AFKJ=window.AFKJ||{};(function(){const utils=window.AFKJ.utils;const config=window.AFKJ.config;function renderCurrentView(){const state=window.AFKJ.state;if(state.viewMode==="list"){window.AFKJ.views.list.renderList();}else if(state.viewMode==="mix"){window.AFKJ.views.mix.loadMixData().then(function(){window.AFKJ.views.mix.renderMix();});}else{window.AFKJ.views.grid.renderGrid();}}
function showIndexView(){const state=window.AFKJ.state;const dom=state.dom;state.closeSkillCardPopover();state.detailHero=null;dom.heroDetail.removeAttribute("data-faction");dom.detailView.classList.add("hidden");dom.gridView.classList.toggle("hidden",state.viewMode!=="grid");dom.listView.classList.toggle("hidden",state.viewMode!=="list");if(dom.mixView){dom.mixView.classList.toggle("hidden",state.viewMode!=="mix");}
window.AFKJ.ui.updateHeaderNav(false);renderCurrentView();}
function showGrid(){document.title="AFK Journey Heroes";showIndexView();}
function navigateHome(replace){const state=window.AFKJ.state;state.csvColumnFilters={};state.csvColumnFilterCombine={};state.pendingListFilterMap=null;const home=utils.homeUrl();if(replace){history.replaceState(null,"",home);}else{history.pushState(null,"",home);}
showGrid();}
function navigateTo(url,replace){if(replace){history.replaceState(null,"",url);}else{history.pushState(null,"",url);}
route();}
function route(){const state=window.AFKJ.state;const listFilters=window.AFKJ.listFilters;if(listFilters.isListFilterHash()){const filterMap=listFilters.parseListFilterHash();if(filterMap){state.pendingListFilterMap=filterMap;}
if(state.csvHeaders.length&&state.pendingListFilterMap){listFilters.tryApplyPendingListFilters();showGrid();return;}
if(filterMap){state.viewMode="list";showGrid();return;}}
const slug=utils.slugFromLocation();if(slug){const hero=state.heroBySlug[slug];if(hero){window.AFKJ.views.detail.showDetail(hero);return;}}
showGrid();}
function heroMatchesSearch(h,q){if(!q){return true;}
const tokens=q.split(/\s+/).filter(Boolean);return tokens.every(function(token){const meta=window.AFKJ.tiers.roleCategoryMeta(h.roleCategory)||config.ROLE_CATEGORY_META[h.roleCategory];const roleLabel=meta?meta.label:"";return(h.name.toLowerCase().indexOf(token)!==-1||(h.faction||"").toLowerCase().indexOf(token)!==-1||(h.class||"").toLowerCase().indexOf(token)!==-1||roleLabel.toLowerCase().indexOf(token)!==-1);});}
function filteredHeroes(){const state=window.AFKJ.state;const q=(state.dom.searchInput.value||"").trim().toLowerCase();return state.heroes.filter(function(h){if(state.activeFaction&&h.faction!==state.activeFaction){return false;}
if(state.activeClass&&h.class!==state.activeClass){return false;}
if(state.activeRole&&h.roleCategory!==state.activeRole){return false;}
if(!heroMatchesSearch(h,q)){return false;}
return true;});}
function filteredHeroNames(){const names={};filteredHeroes().forEach(function(h){names[h.name]=true;});return names;}
window.AFKJ.router={renderCurrentView:renderCurrentView,showIndexView:showIndexView,showGrid:showGrid,navigateHome:navigateHome,navigateTo:navigateTo,route:route,heroMatchesSearch:heroMatchesSearch,filteredHeroes:filteredHeroes,filteredHeroNames:filteredHeroNames,};})();window.AFKJ=window.AFKJ||{};(function(){const utils=window.AFKJ.utils;const config=window.AFKJ.config;const state=window.AFKJ.state;const chips=window.AFKJ.chips;const list=window.AFKJ.views.list;const mix=window.AFKJ.views.mix;const grid=window.AFKJ.views.grid;const router=window.AFKJ.router;const escapeHtml=utils.escapeHtml.bind(utils);function readStoredViewMode(){try{const stored=localStorage.getItem(config.VIEW_MODE_KEY);if(stored==="grid"||stored==="list"||stored==="mix"){return stored;}}catch(e){}
return"grid";}
function storeViewMode(mode){try{localStorage.setItem(config.VIEW_MODE_KEY,mode);}catch(e){}}
function syncViewToggleButtons(){const dom=state.dom;if(!dom.viewToggle){return;}
dom.viewToggle.querySelectorAll(".view-btn").forEach(function(b){const active=b.dataset.view===state.viewMode;b.classList.toggle("active",active);b.setAttribute("aria-pressed",active?"true":"false");});}
window.AFKJ.main.syncViewToggleButtons=syncViewToggleButtons;function filterContextClass(filterType,value){if(filterType==="faction"){return"filter-btn-faction-"+utils.factionDataKey(value);}
if(filterType==="class"){return"filter-btn-class-"+value.toLowerCase().replace(/\s+/g,"");}
if(filterType==="role"){return"filter-btn-role-"+value.replace(/_/g,"-");}
return"";}
function renderFilterFactionIcon(faction){const icon=utils.iconPath("factions",faction);if(!icon){return"";}
return('<span class="filter-btn-icon filter-btn-icon-img" aria-hidden="true">'+'<img src="'+
utils.assetUrl(icon)+'" alt="">'+"</span>");}
function renderFilterClassIcon(className){const icon=utils.iconPath("class",className);if(!icon){return"";}
return('<span class="filter-btn-icon filter-btn-icon-img" aria-hidden="true">'+'<img src="'+
utils.assetUrl(icon)+'" alt="">'+"</span>");}
function renderFilterBtn(filterType,value,label){let iconHtml="";if(filterType==="faction"){iconHtml=renderFilterFactionIcon(value);}else if(filterType==="class"){iconHtml=renderFilterClassIcon(value);}else if(filterType==="role"){iconHtml=window.AFKJ.views.detail.renderRoleCategoryIcon(value);if(iconHtml){iconHtml=iconHtml.replace('class="role-category-icon"','class="filter-btn-icon filter-btn-icon-role role-category-icon"');}}
const ctxClass=filterContextClass(filterType,value);return('<button type="button" class="filter-btn '+
ctxClass+'" data-filter="'+
escapeHtml(filterType)+'" data-value="'+
escapeHtml(value)+'">'+
iconHtml+'<span class="filter-btn-label">'+
escapeHtml(label)+"</span></button>");}
function buildFilters(){const dom=state.dom;const factions=[];const classes=[];const seenF={};const seenC={};const seenRoles={};state.heroes.forEach(function(h){if(h.faction&&!seenF[h.faction]){seenF[h.faction]=true;factions.push(h.faction);}
if(h.class&&!seenC[h.class]){seenC[h.class]=true;classes.push(h.class);}
if(h.roleCategory&&!seenRoles[h.roleCategory]){seenRoles[h.roleCategory]=true;}});factions.sort();classes.sort();let html='<div class="filter-row filter-row-faction">'+'<span class="filter-label">Faction</span>';factions.forEach(function(f){html+=renderFilterBtn("faction",f,f);});html+="</div>";html+='<div class="filter-row filter-row-secondary">';html+='<div class="filter-secondary-groups">';html+='<div class="filter-group filter-group-class">';html+='<span class="filter-label">Class</span>';classes.forEach(function(c){html+=renderFilterBtn("class",c,c);});html+="</div>";html+='<div class="filter-group filter-group-role">';html+='<span class="filter-label filter-label-role">Role</span>';config.ROLE_FILTER_ORDER.forEach(function(roleKey){if(!seenRoles[roleKey]){return;}
const meta=config.ROLE_CATEGORY_META[roleKey];html+=renderFilterBtn("role",roleKey,meta.label);});html+="</div></div></div>";dom.filtersEl.innerHTML=html;updateFilterActiveStates();window.AFKJ.ui.updateListStickyOffset();}
function updateFilterActiveStates(){const dom=state.dom;dom.filtersEl.querySelectorAll(".filter-btn").forEach(function(b){const f=b.dataset.filter;if(f==="faction"){b.classList.toggle("active",b.dataset.value===state.activeFaction);}else if(f==="class"){b.classList.toggle("active",b.dataset.value===state.activeClass);}else if(f==="role"){b.classList.toggle("active",b.dataset.value===state.activeRole);}});window.AFKJ.ui.updateFiltersToggleLabel();}
function initCsv(text){const dom=state.dom;const parsed=list.parseCsv(text);if(!parsed.length){state.csvHeaders=[];state.csvRows=[];return;}
state.csvHeaders=parsed[0];state.csvRows=parsed.slice(1);state.csvColumnWidths=[];state.columnWidthsLocked=false;window.AFKJ.tiers.augmentCsvWithTiers();list.buildColumnFilterOptions();if(window.AFKJ.listFilters.tryApplyPendingListFilters()){syncViewToggleButtons();}
if(!dom.detailView.classList.contains("hidden")){return;}
router.renderCurrentView();}
function initHeroes(data){state.heroes=data.heroes||[];state.heroesMeta=data.meta||{};state.heroBySlug={};state.heroByName={};state.heroes.forEach(function(h){state.heroBySlug[h.slug]=h;state.heroByName[h.name]=h;});window.AFKJ.tiers.augmentCsvWithTiers();list.buildColumnFilterOptions();buildFilters();router.route();}
function localServerHint(){return("<code>python3 -m http.server</code> from the "+"<code>site/</code> directory (after "+"<code>just render-site</code>).");}
function loadHeroData(){const dom=state.dom;if(location.protocol==="file:"){dom.heroGrid.innerHTML='<p class="empty-state">Open this site via a local web server: '+
localServerHint()+"</p>";return;}
fetch(utils.assetUrl("data/heroes.json")).then(function(r){if(!r.ok)throw new Error("Failed to load hero data");return r.json();}).then(initHeroes).catch(function(err){dom.heroGrid.innerHTML='<p class="empty-state">Could not load hero data: '+
escapeHtml(String(err))+". Run <code>just render-site</code>.</p>";});}
function initListColumns(columns){const byId={};(columns||[]).forEach(function(col){byId[col.id]=col;});state.listColumnsById=byId;}
function loadCounterFilterCombos(){if(location.protocol==="file:"){return;}
fetch(utils.assetUrl("data/counter_filter_combos.json")).then(function(r){if(!r.ok){return{};}
return r.json();}).then(function(data){state.counterFilterCombos=data||{};}).catch(function(){state.counterFilterCombos={};});}
function loadCsvData(){if(location.protocol==="file:"){return;}
const columnsPromise=fetch(utils.assetUrl("data/list-columns.json")).then(function(r){if(!r.ok){return[];}
return r.json();}).catch(function(){return[];});const csvPromise=fetch(utils.assetUrl("data/heroes-overview.csv")).then(function(r){if(!r.ok){throw new Error("Failed to load table data");}
return r.text();});Promise.all([columnsPromise,csvPromise]).then(function(results){initListColumns(results[0]);initCsv(results[1]);}).catch(function(){});}
document.addEventListener("DOMContentLoaded",function(){state.BASE=utils.resolveBase();state.dom={gridView:document.getElementById("grid-view"),listView:document.getElementById("list-view"),mixView:document.getElementById("mix-view"),detailView:document.getElementById("detail-view"),heroGrid:document.getElementById("hero-grid"),mixHeroGrid:document.getElementById("mix-hero-grid"),mixDropZone:document.getElementById("mix-drop-zone"),mixEmptyState:document.getElementById("mix-empty-state"),mixRemoveAllBtn:document.getElementById("mix-remove-all"),heroDetail:document.getElementById("hero-detail"),emptyState:document.getElementById("empty-state"),listEmptyState:document.getElementById("list-empty-state"),heroesTableHead:document.getElementById("heroes-table-head"),heroesTableBody:document.getElementById("heroes-table-body"),heroesTable:document.getElementById("heroes-table"),searchInput:document.getElementById("search"),filtersPanel:document.getElementById("filters-panel"),filtersEl:document.getElementById("filters"),filtersToggle:document.getElementById("filters-toggle"),filtersToggleLabel:document.getElementById("filters-toggle-label"),headerBack:document.getElementById("header-back"),viewToggle:document.querySelector(".view-toggle"),themeToggle:document.getElementById("theme-toggle"),siteHeader:document.querySelector(".site-header"),};const dom=state.dom;state.viewMode=readStoredViewMode();state.activeFaction="";state.activeClass="";state.activeRole="";syncViewToggleButtons();window.AFKJ.ui.initWelcomeWarning();window.AFKJ.ui.initFiltersCollapse();window.AFKJ.ui.initThemeToggle();window.AFKJ.ui.initChipTooltips();window.AFKJ.ui.initSkillCardPopover();window.addEventListener("resize",window.AFKJ.ui.updateListStickyOffset);if(dom.siteHeader&&typeof ResizeObserver!=="undefined"){new ResizeObserver(window.AFKJ.ui.updateListStickyOffset).observe(dom.siteHeader);}
mix.initMixInteractions();dom.filtersEl.addEventListener("click",function(e){const btn=e.target.closest(".filter-btn");if(!btn){return;}
if(btn.dataset.filter==="faction"){const v=btn.dataset.value;state.activeFaction=state.activeFaction===v?"":v;}else if(btn.dataset.filter==="class"){const v=btn.dataset.value;const next=state.activeClass===v?"":v;state.activeClass=next;if(next){state.activeRole="";}}else if(btn.dataset.filter==="role"){const v=btn.dataset.value;const next=state.activeRole===v?"":v;state.activeRole=next;if(next){state.activeClass="";}}
updateFilterActiveStates();router.renderCurrentView();});dom.searchInput.addEventListener("input",router.renderCurrentView);if(dom.viewToggle){dom.viewToggle.addEventListener("click",function(e){const btn=e.target.closest(".view-btn");if(!btn){return;}
state.viewMode=btn.dataset.view;storeViewMode(state.viewMode);syncViewToggleButtons();if(!dom.detailView.classList.contains("hidden")){return;}
router.showIndexView();});}
if(dom.heroesTableHead){dom.heroesTableHead.addEventListener("mousedown",function(e){if(e.target.closest(".col-filter-combine-toggle")){e.stopPropagation();}});dom.heroesTableHead.addEventListener("click",function(e){const clearBtn=e.target.closest(".col-filter-clear");if(clearBtn){e.preventDefault();e.stopPropagation();const col=parseInt(clearBtn.dataset.col,10);state.openColumnFilter=col;delete state.csvColumnFilters[col];list.renderList();return;}
const combineToggle=e.target.closest(".col-filter-combine-toggle");if(combineToggle){e.preventDefault();e.stopPropagation();const col=parseInt(combineToggle.dataset.col,10);list.toggleColumnFilterCombine(col);return;}
if(e.target.closest(".col-filter-panel")){return;}
const filterTrigger=e.target.closest(".col-filter-trigger");if(filterTrigger){const details=filterTrigger.closest("details.col-filter");if(details){state.openColumnFilter=parseInt(details.dataset.col,10);}
return;}
const sortBtn=e.target.closest(".th-sort-btn");if(!sortBtn){return;}
const col=parseInt(sortBtn.dataset.col,10);if(col===state.sortColumn){state.sortDir=-state.sortDir;}else{state.sortColumn=col;state.sortDir=1;}
list.renderList();});dom.heroesTableHead.addEventListener("change",function(e){const input=e.target;if(input.type!=="checkbox"){return;}
const details=input.closest("details.col-filter");if(!details){return;}
const col=parseInt(details.dataset.col,10);const value=input.value;if(!state.csvColumnFilters[col]){state.csvColumnFilters[col]=[];}
const set=new Set(state.csvColumnFilters[col]);if(input.checked){set.add(value);}else{set.delete(value);}
state.csvColumnFilters[col]=Array.from(set);if(state.csvColumnFilters[col].length===0){delete state.csvColumnFilters[col];}
state.openColumnFilter=col;list.renderList();});dom.heroesTableHead.addEventListener("toggle",function(e){const details=e.target;if(!details.matches||!details.matches("details.col-filter")){return;}
if(details.open){state.openColumnFilter=parseInt(details.dataset.col,10);const panelContainer=details.querySelector(".col-filter-panel-placeholder");if(panelContainer){const col=state.openColumnFilter;const title=state.csvHeaders[col];const groups=state.csvColumnFilterOptions[col]||[];panelContainer.innerHTML=list.renderColumnFilterPanel(col,title,groups);}
requestAnimationFrame(list.positionOpenColumnFilter);list.bindColumnFilterPointerTracking();}else{list.clearColumnFilterPanelPosition(details);list.unbindColumnFilterPointerTracking();if(state.openColumnFilter===parseInt(details.dataset.col,10)){state.openColumnFilter=-1;}}},true);const tableScrollEl=list.getTableScrollEl();if(tableScrollEl){tableScrollEl.addEventListener("scroll",list.closeColumnFilterOnScroll,{passive:true,});}
window.addEventListener("scroll",list.closeColumnFilterOnScroll,{passive:true,});window.addEventListener("resize",list.positionOpenColumnFilter);}
document.addEventListener("click",function(e){const home=e.target.closest("[data-nav-home]");if(home){e.preventDefault();router.navigateHome();return;}
const card=e.target.closest(".hero-card, .hero-row-card, .hero-compact-card");if(card&&card.dataset.slug){if(card.closest("#mix-hero-grid")||card.closest(".mix-slot")){return;}
e.preventDefault();router.navigateTo(utils.heroUrl(card.dataset.slug));return;}
const link=e.target.closest("a[data-slug], a.hero-link");if(link&&link.dataset.slug){e.preventDefault();router.navigateTo(utils.heroUrl(link.dataset.slug));return;}
const sigLink=e.target.closest("a.signature-skill-link");if(sigLink&&sigLink.dataset.skillCategory){e.preventDefault();window.AFKJ.views.detail.highlightSkillCard(sigLink.dataset.skillCategory);}});document.addEventListener("keydown",function(e){const mixGridCard=e.target.closest("#mix-hero-grid .hero-card");if(mixGridCard&&state.viewMode==="mix"&&(e.key==="Enter"||e.key===" ")){e.preventDefault();const slug=mixGridCard.dataset.slug;if(!mix.tryReplaceHighlightedAlternative(slug)){mix.addHeroToMixZone(slug);}
return;}
const card=e.target.closest(".hero-card, .hero-row-card, .hero-compact-card");if(card&&(e.key==="Enter"||e.key===" ")){if(card.closest("#mix-hero-grid")||card.closest(".mix-slot")){return;}
e.preventDefault();router.navigateTo(utils.heroUrl(card.dataset.slug));}});window.addEventListener("popstate",router.route);window.addEventListener("hashchange",router.route);utils.redirectLegacyHeroPath();loadHeroData();loadCounterFilterCombos();loadCsvData();});})();})();
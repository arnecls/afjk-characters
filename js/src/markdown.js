window.AFKJ = window.AFKJ || {};

(function () {
  function renderMarkdown(md, options) {
    if (!md) return "";
    const chips = window.AFKJ.chips;
    const detail = window.AFKJ.views.detail;

    const skillOverview = options && options.skillOverview;
    const behaviorSection = options && options.behaviorSection;
    const overviewList = skillOverview || behaviorSection;
    const renderItem = skillOverview
      ? detail.renderSkillOverviewItem
      : function (text) {
        return detail.renderBehaviorItem(text, options);
      };
    const lines = md.split("\n");
    const parts = [];
    let inList = false;

    function closeList() {
      if (inList) {
        parts.push("</ul>");
        inList = false;
      }
    }

    for (const raw of lines) {
      const line = raw.trimEnd();
      if (!line.trim()) {
        closeList();
        continue;
      }

      if (line.startsWith("##### ")) {
        closeList();
        parts.push("<h5>" + chips.renderInline(line.slice(6)) + "</h5>");
      } else if (line.startsWith("#### ")) {
        closeList();
        parts.push("<h4>" + chips.renderInline(line.slice(5)) + "</h4>");
      } else if (line.startsWith("### ")) {
        closeList();
        parts.push("<h3>" + chips.renderInline(line.slice(4)) + "</h3>");
      } else if (line.startsWith("- ")) {
        if (!inList) {
          parts.push(
            overviewList ? '<ul class="skill-overview-list">' : "<ul>"
          );
          inList = true;
        }
        parts.push("<li>" + renderItem(line.slice(2)) + "</li>");
      } else {
        closeList();
        parts.push("<p>" + chips.renderInline(line) + "</p>");
      }
    }
    closeList();
    return parts.join("\n");
  }

  window.AFKJ.markdown = {
    renderMarkdown: renderMarkdown
  };
})();

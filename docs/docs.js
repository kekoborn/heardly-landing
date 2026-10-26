/* Heardly Docs — навигация, язык и оглавление.
   Карта разделов живёт здесь одним списком: страницы её только подключают,
   поэтому добавление страницы правит один файл, а не двадцать шесть. */
(function () {
  "use strict";

  var NAV = [
    { ru: "Начало", en: "Get started", items: [
      { f: "overview.html",   ru: "Что такое Heardly",        en: "What Heardly is" },
      { f: "install.html",    ru: "Установка и первый запуск", en: "Install and first launch" },
      { f: "permissions.html",ru: "Разрешения macOS",          en: "macOS permissions" },
      { f: "quickstart.html", ru: "Первая диктовка",           en: "Your first dictation" }
    ]},
    { ru: "Диктовка", en: "Dictation", items: [
      { f: "dictation.html",     ru: "Как диктовать",            en: "How to dictate" },
      { f: "dictation-bar.html", ru: "Панель диктовки",          en: "The dictation bar" },
      { f: "replacements.html",  ru: "Словарь замен",            en: "Replacement list" },
      { f: "muffle.html",        ru: "Звук других приложений",   en: "Silencing other apps" }
    ]},
    { ru: "Звонки и встречи", en: "Calls and meetings", items: [
      { f: "live.html",        ru: "Запись звонка без бота",  en: "Recording a call, no bot" },
      { f: "live-window.html", ru: "Окно живой расшифровки",  en: "The live window" }
    ]},
    { ru: "Файлы", en: "Files", items: [
      { f: "files.html", ru: "Расшифровка аудио и видео", en: "Transcribing audio and video" }
    ]},
    { ru: "Записи", en: "Recordings", items: [
      { f: "history.html", ru: "История",            en: "History" },
      { f: "export.html",  ru: "Экспорт",            en: "Export" },
      { f: "folder.html",  ru: "Папка расшифровок",  en: "Transcripts folder" }
    ]},
    { ru: "Терминал", en: "Terminal", items: [
      { f: "cli.html", ru: "Команда heardly", en: "The heardly command" }
    ]},
    { ru: "Настройки", en: "Settings", items: [
      { f: "settings.html", ru: "Справочник настроек", en: "Settings reference" },
      { f: "model.html",    ru: "Модель и языки",      en: "Model and languages" },
      { f: "stats.html",    ru: "Статистика",          en: "Statistics" }
    ]},
    { ru: "Аккаунт", en: "Account", items: [
      { f: "pricing.html", ru: "Бесплатно, пробный период и Pro", en: "Free, trial and Pro" },
      { f: "license.html", ru: "Лицензия и устройства",           en: "Licence and devices" }
    ]},
    { ru: "Приватность", en: "Privacy", items: [
      { f: "privacy.html", ru: "Что уходит в интернет", en: "What leaves your Mac" }
    ]},
    { ru: "Решение проблем", en: "Troubleshooting", items: [
      { f: "fix-dictation.html", ru: "Текст не вставляется",   en: "Text is not inserted" },
      { f: "fix-audio.html",     ru: "Нет звука приложений",   en: "No app audio" },
      { f: "fix-mic.html",       ru: "Микрофон и Bluetooth",   en: "Microphone and Bluetooth" },
      { f: "updates.html",       ru: "Обновления",             en: "Updates" },
      { f: "support.html",       ru: "Сообщить о проблеме",    en: "Report a problem" }
    ]}
  ];

  function el(tag, cls) { var n = document.createElement(tag); if (cls) n.className = cls; return n; }

  function bilingual(ru, en) {
    var f = document.createDocumentFragment();
    var a = el("span"); a.setAttribute("lang", "ru"); a.textContent = ru;
    var b = el("span"); b.setAttribute("lang", "en"); b.textContent = en;
    f.appendChild(a); f.appendChild(b);
    return f;
  }

  var here = location.pathname.split("/").pop() || "index.html";

  /* ── Боковая навигация ─────────────────────────── */
  var side = document.querySelector(".d-side");
  if (side) {
    NAV.forEach(function (group) {
      var box = el("div", "d-group");
      var h = el("h4");
      h.appendChild(bilingual(group.ru, group.en));
      box.appendChild(h);
      group.items.forEach(function (item) {
        var a = el("a");
        a.href = item.f;
        a.appendChild(bilingual(item.ru, item.en));
        if (item.f === here) a.setAttribute("aria-current", "page");
        box.appendChild(a);
      });
      side.appendChild(box);
    });
  }

  /* ── Соседние страницы ─────────────────────────── */
  var flat = NAV.reduce(function (acc, g) { return acc.concat(g.items); }, []);
  var idx = flat.findIndex(function (i) { return i.f === here; });
  var updown = document.querySelector(".d-updown");
  if (updown && idx >= 0) {
    [[idx - 1, "prev", "Назад", "Previous"], [idx + 1, "next", "Дальше", "Next"]].forEach(function (p) {
      var item = flat[p[0]];
      if (!item) return;
      var a = el("a", p[1]);
      a.href = item.f;
      var dir = el("span", "dir"); dir.appendChild(bilingual(p[2], p[3]));
      var ttl = el("span", "ttl"); ttl.appendChild(bilingual(item.ru, item.en));
      a.appendChild(dir); a.appendChild(ttl);
      updown.appendChild(a);
    });
  }

  /* ── Оглавление страницы ───────────────────────── */
  var toc = document.querySelector(".d-toc");
  var heads = [].slice.call(document.querySelectorAll(".d-main h2[id], .d-main h3[id]"));
  if (toc && heads.length) {
    var title = el("h5"); title.appendChild(bilingual("На этой странице", "On this page"));
    toc.appendChild(title);
    heads.forEach(function (h) {
      var a = el("a", h.tagName === "H3" ? "lvl3" : "");
      a.href = "#" + h.id;
      // Заголовок уже двуязычный — переносим его парные span'ы как есть.
      a.innerHTML = h.innerHTML;
      toc.appendChild(a);
    });
    var links = [].slice.call(toc.querySelectorAll("a"));
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        links.forEach(function (l) { l.classList.toggle("on", l.getAttribute("href") === "#" + e.target.id); });
      });
    }, { rootMargin: "-80px 0px -70% 0px" });
    heads.forEach(function (h) { spy.observe(h); });
  } else if (toc) {
    toc.remove();
  }

  /* ── Окно «скачивание началось» ─────────────────
     Разметку держим здесь, а не в шаблоне страницы: кнопка «Скачать» стоит в шапке
     всех 27 страниц, и одинаковый блок разъехался бы по ним копиями. Переход по
     ссылке не отменяем — файл отдаётся как вложение, страница остаётся на месте. */
  var dlLinks = document.querySelectorAll('a[href$="Heardly.dmg"]');
  if (dlLinks.length && window.HTMLDialogElement) {
    var dlg = document.createElement("dialog");
    dlg.className = "dldlg";
    dlg.innerHTML =
      '<button class="x" type="button" aria-label="Закрыть / Close">×</button>' +
      '<h3><span lang="ru">Скачивание началось</span><span lang="en">The download has started</span></h3>' +
      '<p><span lang="ru">Heardly.dmg сохраняется в&nbsp;папку «Загрузки». Если скачивание не&nbsp;началось, нажмите на&nbsp;ссылку ниже.</span>' +
      '<span lang="en">Heardly.dmg is being saved to your Downloads folder. If the download did not start, use the link below.</span></p>' +
      '<a class="again" href="https://github.com/kekoborn/heardly-releases/releases/latest/download/Heardly.dmg">' +
      '<span lang="ru">Скачать Heardly.dmg</span><span lang="en">Download Heardly.dmg</span></a>';
    document.body.appendChild(dlg);
    dlg.querySelector(".x").addEventListener("click", function () { dlg.close(); });
    Array.prototype.forEach.call(dlLinks, function (a) {
      a.addEventListener("click", function () { dlg.showModal(); });
    });
  }

  /* ── Навигация на узком экране ─────────────────── */
  var burger = document.querySelector(".d-burger");
  if (burger) {
    burger.addEventListener("click", function () { document.body.classList.toggle("nav-open"); });
    document.addEventListener("click", function (e) {
      if (!document.body.classList.contains("nav-open")) return;
      if (e.target.closest(".d-side") || e.target.closest(".d-burger")) return;
      document.body.classList.remove("nav-open");
    });
  }
})();

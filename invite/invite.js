/* «Пригласить друга»: email и согласие → POST /ref/create → личная ссылка и код. RU/EN как на главной. */
(function () {
  "use strict";
  var API = "https://heardly-api.cafmanar.workers.dev";
  var CONSENT_VERSION = "consent-2026-10-25"; // редакция /consent/; поднимать вместе с главной
  // Цели Метрики: ref_invite_open, ref_code_created, ref_link_copied. Счётчик грузится только после согласия на cookie.
  var YM_ID = 113735110;
  function goal(name) { try { if (window.ym) ym(YM_ID, "reachGoal", name); } catch (e) {} }

  // Язык — тот же механизм, что на главной: ?lang=, иначе выбор из localStorage, иначе язык браузера.
  var T = {
    ru: {
      title: "Бесплатный Heardly на месяц за приглашение",
      email: "Проверьте email: на него начислим бонусные дни.",
      agree: "Поставьте галочку согласия на обработку данных.",
      closed: "Программа приглашений закончилась.",
      rate: "Слишком много попыток с этого адреса. Попробуйте через час.",
      fail: "Не получилось создать ссылку. Попробуйте ещё раз или напишите на support@kekoborn.ru.",
      offline: "Нет связи с сервером. Попробуйте ещё раз.",
      copied: "Скопировано",
      share: "Heardly — расшифровка звонков и диктовка на Mac. По этой ссылке первый месяц дешевле:"
    },
    en: {
      title: "Free month of Heardly for every friend you invite",
      email: "Check your email address: your bonus days go there.",
      agree: "Please tick the consent box.",
      closed: "The referral program has ended.",
      rate: "Too many attempts from this address. Try again in an hour.",
      fail: "Couldn't create your link. Try again or write to support@kekoborn.ru.",
      offline: "Can't reach the server. Try again.",
      copied: "Copied",
      share: "Heardly turns calls and dictation into text on your Mac. Your first month is cheaper with this link:"
    }
  };
  var lang = "ru";
  try { var s = localStorage.getItem("heardly-lang"); if (s === "ru" || s === "en") lang = s; else if (!/^(ru|uk|be|kk)/i.test(navigator.language || "ru")) lang = "en"; } catch (e) {}
  var q = new URLSearchParams(location.search).get("lang"); if (q === "ru" || q === "en") lang = q;
  function setLang(l) {
    lang = l;
    document.documentElement.dataset.lang = l; document.documentElement.lang = l;
    document.title = T[l].title;
    document.querySelectorAll("[data-set-lang]").forEach(function (b) { b.setAttribute("aria-pressed", b.dataset.setLang === l); });
    document.querySelectorAll("[data-ph-" + l + "]").forEach(function (n) { n.placeholder = n.getAttribute("data-ph-" + l); });
    try { localStorage.setItem("heardly-lang", l); } catch (e) {}
  }
  document.querySelectorAll("[data-set-lang]").forEach(function (b) { b.addEventListener("click", function () { setLang(b.dataset.setLang); }); });
  setLang(lang);

  // device_id приходит из приложения во фрагменте (#d=…): фрагмент не уходит ни на сервер сайта, ни в аналитику.
  var device = (location.hash.match(/[#&]d=([\w-]{1,64})/) || [])[1] || "";
  if (device) history.replaceState(null, "", location.pathname + location.search);
  goal("ref_invite_open");

  var form = document.getElementById("invite"), email = document.getElementById("email"),
      agree = document.getElementById("agree"), btn = document.getElementById("go"), msg = document.getElementById("msg");
  var RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
  function say(key) { msg.textContent = key ? T[lang][key] : ""; }

  email.addEventListener("input", function () { email.classList.remove("bad"); say(""); });
  form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    var v = email.value.trim();
    if (!RE.test(v)) { email.classList.add("bad"); say("email"); email.focus(); return; }
    if (!agree.checked) { say("agree"); agree.focus(); return; }
    btn.disabled = true; say("");
    fetch(API + "/ref/create", {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: v, device_hint: device, consent: { version: CONSENT_VERSION, at: new Date().toISOString() } })
    }).then(function (r) { return r.json().then(function (j) { return { s: r.status, j: j }; }); })
      .then(function (res) {
        var j = res.j || {};
        btn.disabled = false;
        if (j.ok) { show(j.code, j.link); goal("ref_code_created"); return; }
        if (j.closed) say("closed");
        else if (res.s === 429) say("rate");
        else if (j.error === "invalid_email") { email.classList.add("bad"); say("email"); }
        else say("fail");
      })
      .catch(function () { btn.disabled = false; say("offline"); });
  });

  function show(code, link) {
    var url = link + "&utm_source=referral&utm_medium=invite";
    document.getElementById("link").value = url;
    document.querySelectorAll("#result .code").forEach(function (n) { n.textContent = code; });
    document.getElementById("tg").href = "https://t.me/share/url?url=" + encodeURIComponent(url) +
      "&text=" + encodeURIComponent(T[lang].share);
    form.hidden = true;
    document.getElementById("result").hidden = false;
  }

  var copyBtn = document.getElementById("copy");
  copyBtn.addEventListener("click", function () {
    var input = document.getElementById("link");
    var labels = copyBtn.querySelectorAll("span"), old = [].map.call(labels, function (n) { return n.textContent; });
    function done() {
      labels.forEach(function (n) { n.textContent = T[n.lang].copied; });
      goal("ref_link_copied");
      setTimeout(function () { labels.forEach(function (n, i) { n.textContent = old[i]; }); }, 2000);
    }
    if (navigator.clipboard) navigator.clipboard.writeText(input.value).then(done, function () { input.select(); });
    else { input.select(); try { document.execCommand("copy"); done(); } catch (e) {} }
  });
})();

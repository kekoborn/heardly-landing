/* Баннер cookie и Яндекс Метрика. Метрика грузится только после «Принять» (152-ФЗ, позиция РКН).
   Выбор хранится в localStorage на 12 месяцев; кнопки [data-cookie-settings] открывают баннер снова. */
(function () {
  "use strict";
  var KEY = "heardly-cookie-consent", TTL = 365 * 864e5, YM_ID = 113735110;

  function read() {
    try {
      var c = JSON.parse(localStorage.getItem(KEY) || "null");
      if (c && (c.v === "accepted" || c.v === "rejected") && Date.now() - c.at < TTL) return c.v;
    } catch (e) {}
    return null;
  }
  function save(v) { try { localStorage.setItem(KEY, JSON.stringify({ v: v, at: Date.now() })); } catch (e) {} }

  function loadMetrika() {
    if (window.ym) return;
    (function (m, e, t, r, i, k, a) {
      m[i] = m[i] || function () { (m[i].a = m[i].a || []).push(arguments); };
      m[i].l = 1 * new Date();
      for (var j = 0; j < document.scripts.length; j++) { if (document.scripts[j].src === r) { return; } }
      k = e.createElement(t), a = e.getElementsByTagName(t)[0], k.async = 1, k.src = r, a.parentNode.insertBefore(k, a);
    })(window, document, "script", "https://mc.yandex.ru/metrika/tag.js?id=" + YM_ID, "ym");
    ym(YM_ID, "init", { ssr: true, webvisor: true, clickmap: true, ecommerce: "dataLayer", referrer: document.referrer, url: location.href, accurateTrackBounce: true, trackLinks: true });
  }

  // После отказа стираем уже записанные cookie Метрики на нашем домене.
  function dropMetrikaCookies() {
    document.cookie.split("; ").forEach(function (c) {
      var n = c.split("=")[0];
      if (/^(_ym|mdd$)/.test(n)) ["", "; domain=" + location.hostname, "; domain=." + location.hostname.split(".").slice(-2).join(".")].forEach(function (d) {
        document.cookie = n + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/" + d;
      });
    });
  }

  var TXT = {
    ru: { text: "Мы используем Яндекс Метрику, чтобы понимать, как читают сайт. Она ставит cookie и записывает действия на странице. Включим её, только если вы разрешите.", more: "Подробнее", yes: "Принять", no: "Отклонить" },
    en: { text: "We use Yandex Metrica to see how the site is read. It sets cookies and records actions on the page. It only runs if you allow it.", more: "Details", yes: "Accept", no: "Decline" }
  };
  var CSS = ".hc-banner{position:fixed;z-index:2147483000;left:16px;right:16px;bottom:16px;max-width:560px;margin:0 auto;padding:18px 20px;border-radius:18px;background:#FBF9F4;color:#232633;box-shadow:0 0 0 1px rgba(35,38,51,.1) inset,0 20px 60px -20px rgba(35,38,51,.45);font:400 14.5px/1.5 Onest,-apple-system,BlinkMacSystemFont,sans-serif}" +
    ".hc-banner p{margin:0 0 14px;color:#4A4E5C}.hc-banner a{color:inherit;text-decoration:underline;text-underline-offset:2px}" +
    ".hc-row{display:flex;gap:10px;flex-wrap:wrap}.hc-row button{flex:1 1 140px;height:44px;border:0;border-radius:999px;font:500 15px Onest,-apple-system,sans-serif;cursor:pointer;background:#EFEBE2;color:#232633}" +
    ".hc-row button:hover{background:#E6E1D5}.hc-row button:focus-visible{outline:2px solid #5E6AD2;outline-offset:2px}";

  var el = null;
  function lang() { return /^en/i.test(document.documentElement.lang) ? "en" : "ru"; }
  function close() { if (el) { el.remove(); el = null; } }
  function show() {
    close();
    if (!document.getElementById("hc-css")) { var st = document.createElement("style"); st.id = "hc-css"; st.textContent = CSS; document.head.appendChild(st); }
    var t = TXT[lang()];
    el = document.createElement("div");
    el.className = "hc-banner"; el.setAttribute("role", "dialog"); el.setAttribute("aria-live", "polite"); el.setAttribute("aria-label", "Cookie");
    el.innerHTML = '<p>' + t.text + ' <a href="/cookies/">' + t.more + '</a></p><div class="hc-row"><button type="button" data-v="rejected">' + t.no + '</button><button type="button" data-v="accepted">' + t.yes + '</button></div>';
    el.addEventListener("click", function (e) {
      var v = e.target.getAttribute && e.target.getAttribute("data-v"); if (!v) return;
      var was = read(); save(v); close();
      if (v === "accepted") loadMetrika();
      else { dropMetrikaCookies(); if (was === "accepted" || window.ym) location.reload(); }
    });
    document.body.appendChild(el);
  }

  function init() {
    var c = read();
    if (c === "accepted") loadMetrika(); else if (!c) show();
    document.addEventListener("click", function (e) {
      if (e.target.closest && e.target.closest("[data-cookie-settings]")) { e.preventDefault(); show(); }
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();

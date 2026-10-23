/* Первый экран подарка: живая волна, расшифровка по словам и форма «Скачать на Mac». */
(function () {
  "use strict";
  var API = "https://heardly-api.cafmanar.workers.dev";
  var CONSENT_VERSION = "consent-2026-10-22"; // редакция /consent/; поднимать вместе с главной
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  var css = getComputedStyle(document.documentElement);
  var COL = { m: css.getPropertyValue("--mic").trim() || "#5E6AD2", a: css.getPropertyValue("--app").trim() || "#D9845A" };
  var S = { speaking: false, who: "m" };

  // ── Волна: пилюли без градиента, как DotsWaveform в приложении ──
  var waves = [].slice.call(document.querySelectorAll("canvas.wave")).map(function (c) {
    var o = { c: c, ctx: c.getContext("2d"), bar: +c.dataset.bar || 0, live: c.dataset.mode === "live", w: 0, h: 0, lvl: 0 };
    o.size = function () {
      var d = window.devicePixelRatio || 1;
      o.w = c.clientWidth; o.h = c.clientHeight;
      c.width = o.w * d; c.height = o.h * d; o.ctx.setTransform(d, 0, 0, d, 0, 0);
    };
    o.size();
    return o;
  });
  function drawWave(o, t) {
    var ctx = o.ctx, w = o.w, h = o.h;
    ctx.clearRect(0, 0, w, h);
    var active = o.live ? S.speaking : true;
    o.lvl += ((active ? 1 : 0) - o.lvl) * (active ? 0.18 : 0.08);
    var n, bw, gap;
    if (o.bar) { bw = o.bar; gap = Math.max(3, bw * 0.55); n = Math.max(4, Math.floor((w + gap) / (bw + gap))); }
    else { bw = 5; gap = 4; n = Math.min(14, Math.floor((w + gap) / (bw + gap))); }
    var total = n * bw + (n - 1) * gap, x0 = o.bar ? (w - total) / 2 : 0;
    ctx.fillStyle = o.live ? COL[S.who] : COL.m;
    for (var i = 0; i < n; i++) {
      var e = (0.5 + 0.5 * Math.sin(t * 2.3 + i * 0.75)) * (0.55 + 0.45 * Math.sin(t * 0.9 + i * 1.3));
      var idle = 0.5 + 0.5 * Math.sin(t * 1.4 + i * 0.5);
      var hh = bw + (h - bw) * (0.14 + 0.86 * e) * o.lvl;
      var r = bw / 2;
      ctx.globalAlpha = o.lvl > 0.05 ? 1 : 0.55 + 0.35 * idle;
      var x = x0 + i * (bw + gap), y = (h - hh) / 2;
      ctx.beginPath();
      if (ctx.roundRect) ctx.roundRect(x, y, bw, hh, r); else ctx.rect(x, y, bw, hh);
      ctx.fill();
    }
    ctx.globalAlpha = 1;
  }
  var t0 = performance.now();
  function frame(now) {
    var t = (now - t0) / 1000;
    for (var i = 0; i < waves.length; i++) drawWave(waves[i], t);
    if (!reduce) requestAnimationFrame(frame);
  }
  window.addEventListener("resize", function () { waves.forEach(function (o) { o.size(); }); if (reduce) frame(performance.now() + 3000); });
  if (reduce) { S.speaking = true; waves.forEach(function (o) { o.lvl = 1; }); frame(t0 + 3000); } else requestAnimationFrame(frame);

  // ── Расшифровка: слова проявляются, как в живом режиме ──
  var rows = [].slice.call(document.querySelectorAll("#lines .ln"));
  var timers = [];
  function later(fn, ms) { timers.push(setTimeout(fn, ms)); }
  function runLines() {
    rows.forEach(function (r) { r.classList.remove("on"); r.querySelector(".tx").textContent = ""; });
    S.speaking = false;
    var at = 500;
    rows.forEach(function (r, i) {
      var words = r.dataset.t.split(" "), who = r.dataset.w, tx = r.querySelector(".tx");
      later(function () { r.classList.add("on"); S.who = who; S.speaking = true; }, at);
      words.forEach(function (_, k) {
        later(function () {
          tx.textContent = words.slice(0, k + 1).join(" ");
          if (i === rows.length - 1 && k === words.length - 1) S.speaking = false;
        }, at + 120 + k * 150);
      });
      at += 120 + words.length * 150 + 500;
      later(function () { S.speaking = false; }, at - 380);
    });
    later(function () { rows.forEach(function (r) { r.classList.remove("on"); }); }, at + 3200);
    later(runLines, at + 3800);
  }
  if (rows.length) {
    if (reduce) rows.forEach(function (r) { r.classList.add("on"); r.querySelector(".tx").textContent = r.dataset.t; });
    else runLines();
  }
  document.addEventListener("visibilitychange", function () {
    if (rows.length && !reduce && !document.hidden) { timers.forEach(clearTimeout); timers = []; runLines(); }
  });

  // ── Форма ──
  var form = document.getElementById("claim");
  if (!form) return;
  var email = document.getElementById("email"), agree = document.getElementById("agree"),
      btn = document.getElementById("go"), msg = document.getElementById("msg");
  var RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
  function say(html) { msg.innerHTML = html; }
  function fallback(text) {
    say(text + ' <a href="start/?plain=1">Скачать без подарка</a>');
  }
  email.addEventListener("input", function () { email.classList.remove("bad"); if (msg.textContent) say(""); });
  form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    var v = email.value.trim();
    if (!RE.test(v)) { email.classList.add("bad"); say("Проверьте email: на этот адрес мы включим подарок."); email.focus(); return; }
    if (!agree.checked) { say("Поставьте галочку согласия на обработку данных."); agree.focus(); return; }
    btn.disabled = true; say("");
    var label = btn.querySelector("span"), old = label.textContent;
    label.textContent = "Готовим подарок…";
    var ctl = window.AbortController ? new AbortController() : null;
    var to = setTimeout(function () { if (ctl) ctl.abort(); }, 12000);
    fetch(API + "/promo/claim", {
      method: "POST", headers: { "Content-Type": "application/json" }, signal: ctl ? ctl.signal : undefined,
      body: JSON.stringify({ email: v, consent: { version: CONSENT_VERSION, at: new Date().toISOString() } })
    }).then(function (r) { return r.json().then(function (j) { return { s: r.status, j: j }; }); })
      .then(function (res) {
        clearTimeout(to);
        var j = res.j || {};
        if (j.ok) {
          try {
            sessionStorage.setItem("heardly_gift_email", j.email || v.toLowerCase());
            sessionStorage.setItem("heardly_gift_expires", j.expires_at || "");
            sessionStorage.setItem("heardly_gift_dl", "1");
            sessionStorage.setItem("heardly_gift_existing", j.existing ? "1" : "");
            sessionStorage.setItem("heardly_gift_mailed", j.mailed ? "1" : "");
          } catch (e) {}
          location.href = "start/";
          return;
        }
        btn.disabled = false; label.textContent = old;
        if (j.closed) fallback("Акция закончилась.");
        else if (j.error === "already_claimed") fallback("На этот почтовый ящик подарок уже выдан. В приложении введите адрес, с которого получили его впервые.");
        else if (res.s === 429) say("Слишком много попыток с этого адреса. Попробуйте через час.");
        else if (j.error === "invalid_email") { email.classList.add("bad"); say("Проверьте email: на этот адрес мы включим подарок."); }
        else fallback("Не получилось включить подарок.");
      })
      .catch(function () {
        clearTimeout(to);
        btn.disabled = false; label.textContent = old;
        fallback("Нет связи с сервером. Проверьте сеть и нажмите ещё раз.");
      });
  });
})();

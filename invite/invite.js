/* «Пригласить друга»: email и согласие → POST /ref/create → личная ссылка и код. */
(function () {
  "use strict";
  var API = "https://heardly-api.cafmanar.workers.dev";
  var CONSENT_VERSION = "consent-2026-10-25"; // редакция /consent/; поднимать вместе с главной
  // Цели Метрики: ref_invite_open, ref_code_created, ref_link_copied. Счётчик грузится только после согласия на cookie.
  var YM_ID = 113735110;
  function goal(name) { try { if (window.ym) ym(YM_ID, "reachGoal", name); } catch (e) {} }

  // device_id приходит из приложения во фрагменте (#d=…): фрагмент не уходит ни на сервер сайта, ни в аналитику.
  var device = (location.hash.match(/[#&]d=([\w-]{1,64})/) || [])[1] || "";
  if (device) history.replaceState(null, "", location.pathname);
  goal("ref_invite_open");

  var form = document.getElementById("invite"), email = document.getElementById("email"),
      agree = document.getElementById("agree"), btn = document.getElementById("go"), msg = document.getElementById("msg");
  var RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
  function say(text) { msg.textContent = text; }

  email.addEventListener("input", function () { email.classList.remove("bad"); say(""); });
  form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    var v = email.value.trim();
    if (!RE.test(v)) { email.classList.add("bad"); say("Проверьте email: на него начислим бонусные дни."); email.focus(); return; }
    if (!agree.checked) { say("Поставьте галочку согласия на обработку данных."); agree.focus(); return; }
    btn.disabled = true; say("");
    fetch(API + "/ref/create", {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: v, device_hint: device, consent: { version: CONSENT_VERSION, at: new Date().toISOString() } })
    }).then(function (r) { return r.json().then(function (j) { return { s: r.status, j: j }; }); })
      .then(function (res) {
        var j = res.j || {};
        btn.disabled = false;
        if (j.ok) { show(j.code, j.link); goal("ref_code_created"); return; }
        if (j.closed) say("Программа приглашений закончилась.");
        else if (res.s === 429) say("Слишком много попыток с этого адреса. Попробуйте через час.");
        else if (j.error === "invalid_email") { email.classList.add("bad"); say("Проверьте email: на него начислим бонусные дни."); }
        else say("Не получилось создать ссылку. Попробуйте ещё раз или напишите на support@kekoborn.ru.");
      })
      .catch(function () { btn.disabled = false; say("Нет связи с сервером. Попробуйте ещё раз."); });
  });

  function show(code, link) {
    var url = link + "&utm_source=referral&utm_medium=invite";
    document.getElementById("link").value = url;
    document.getElementById("code").textContent = code;
    document.getElementById("tg").href = "https://t.me/share/url?url=" + encodeURIComponent(url) +
      "&text=" + encodeURIComponent("Heardly — расшифровка звонков и диктовка на Mac. По этой ссылке первый месяц дешевле:");
    form.hidden = true;
    document.getElementById("result").hidden = false;
  }

  document.getElementById("copy").addEventListener("click", function () {
    var input = document.getElementById("link"), label = this.querySelector("span");
    function done() { label.textContent = "Скопировано"; goal("ref_link_copied"); setTimeout(function () { label.textContent = "Скопировать"; }, 2000); }
    if (navigator.clipboard) navigator.clipboard.writeText(input.value).then(done, function () { input.select(); });
    else { input.select(); try { document.execCommand("copy"); done(); } catch (e) {} }
  });
})();

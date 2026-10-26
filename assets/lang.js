/* Язык сайта. Переключателя нет: язык идёт за регионом, как и цена.
   Российский часовой пояс → русский, остальные → английский (воркер /pricing
   ещё уточняет регион по IP — лендинг досылает это сам).
   Ссылка с ?lang=ru|en закрепляет язык в этом браузере, пока не придёт другая.
   Подключается синхронно в <head>, чтобы страница не мигала вторым языком. */
(function () {
  var RU_TZ = /^(Europe\/(Moscow|Kaliningrad|Simferopol|Kirov|Volgograd|Astrakhan|Saratov|Ulyanovsk|Samara)|Asia\/(Yekaterinburg|Omsk|Novosibirsk|Barnaul|Tomsk|Novokuznetsk|Krasnoyarsk|Irkutsk|Chita|Yakutsk|Khandyga|Vladivostok|Ust-Nera|Magadan|Sakhalin|Srednekolymsk|Kamchatka|Anadyr)|W-SU)$/;
  var KEY = "heardly-lang-pin";
  var q = null, pin = null, tz = "";
  try { q = new URLSearchParams(location.search).get("lang"); } catch (e) {}
  try {
    localStorage.removeItem("heardly-lang"); // выбор старого переключателя больше не действует
    if (q === "ru" || q === "en") localStorage.setItem(KEY, q);
    pin = localStorage.getItem(KEY);
  } catch (e) { pin = q; }
  if (pin !== "ru" && pin !== "en") pin = null;
  try { tz = Intl.DateTimeFormat().resolvedOptions().timeZone || ""; } catch (e) {}
  var lang = pin || (RU_TZ.test(tz) ? "ru" : "en");
  document.documentElement.dataset.lang = lang;
  document.documentElement.lang = lang;
  window.HeardlyLang = { lang: lang, pinned: !!pin, tz: tz, ruTz: RU_TZ };
})();

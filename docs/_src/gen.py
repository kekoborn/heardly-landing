#!/usr/bin/env python3
"""Собирает статические страницы docs/ из кусков контента.

В репозиторий попадают только готовые .html — шага сборки у сайта нет,
этот скрипт нужен лишь чтобы 26 страниц имели одинаковую обвязку.
"""
import importlib
import os
import re
import pathlib
import sys

# Куда класть готовые страницы. По умолчанию — папка docs/, в которой лежит сам
# генератор, так что запуск из любого места кладёт страницы туда же;
# переопределяется переменной HEARDLY_DOCS_OUT.
OUT = pathlib.Path(
    os.environ.get("HEARDLY_DOCS_OUT", pathlib.Path(__file__).resolve().parent.parent)
).resolve()

SHELL = """<!doctype html>
<html lang="ru" data-lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title_ru} — Heardly</title>
<meta name="description" content="{desc_ru}">
<meta name="theme-color" content="#F6F4EF">
<link rel="stylesheet" href="../assets/fonts/fonts.css">
<link rel="stylesheet" href="docs.css">
</head>
<body>

<header class="d-header">
  <div class="d-nav">
    <button class="d-burger" type="button" aria-label="Разделы / Sections"><i></i></button>
    <a class="d-brand" href="../"><img src="img/logo.png" alt="" width="26" height="26">Heardly<span class="tag"><span lang="ru">Документация</span><span lang="en">Docs</span></span></a>
    <div class="d-nav-r">
      <div class="lang" role="group" aria-label="Язык / Language"><button type="button" data-set-lang="ru">RU</button><button type="button" data-set-lang="en">EN</button></div>
      <a class="btn btn-w" href="https://github.com/kekoborn/heardly-releases/releases/latest/download/Heardly.dmg"><span lang="ru">Скачать</span><span lang="en">Download</span></a>
    </div>
  </div>
</header>

<div class="d-shell">
  <nav class="d-side" aria-label="Разделы документации"></nav>

  <main class="d-main">
    <div class="d-eyebrow"><span lang="ru">{group_ru}</span><span lang="en">{group_en}</span></div>
    <h1><span lang="ru">{title_ru}</span><span lang="en">{title_en}</span></h1>
    <p class="d-lede"><span lang="ru">{lede_ru}</span><span lang="en">{lede_en}</span></p>

{body}

    <nav class="d-updown" aria-label="Соседние страницы"></nav>
  </main>

  <aside class="d-toc"></aside>
</div>

<footer class="d-foot">
  <div class="in">
    <span>© 2026 Heardly</span>
    <a href="../"><span lang="ru">Про Heardly</span><span lang="en">About Heardly</span></a>
    <a href="index.html"><span lang="ru">Все разделы</span><span lang="en">All sections</span></a>
    <a href="support.html"><span lang="ru">Поддержка</span><span lang="en">Support</span></a>
  </div>
</footer>

<script src="docs.js"></script>
<script src="../assets/consent.js" defer></script>
</body>
</html>
"""


# Английские alt'ы к снимкам: русский текст в alt на английской странице читался бы
# скринридером как мусор, поэтому у каждого кадра своя подпись.
ALT_EN = {
    "menubar-popup": "The Heardly menu bar panel: record button, microphone and app audio switches, word statistics and a file drop zone",
    "settings-general": "The General section of Heardly settings: shortcut, dictation activation, microphone and recognition language",
    "settings-dictation": "The Dictation section: bar style, replacement list and silencing other apps",
    "settings-recordings": "The Recordings section: the transcripts folder path and the button that opens History",
    "settings-statistics": "The Statistics section: speaking speed, time saved, total words, a breakdown by recording type and an activity calendar",
    "settings-subscription": "The Subscription section of Heardly settings",
    "settings-system": "The System section: launch at login, terminal command, interface language and updates with the version number",
    "history-dictations": "The Dictations section of History: word and speed counters on top, today's entries below",
    "history-calls": "The Calls and meetings section: the list of recordings on the left, the transcript with timecodes and source labels on the right",
    "history-files": "The Files section of History: the drop zone, the Choose file button and a finished transcript with timecodes",
    "live-window": "The live transcription window: Mic and Apps sources, Pause and Stop buttons, lines carrying a time and a source label",
    "dictation-bar-large": "The large dictation bar: voice waveform, timer and the Stop and Cancel hints",
    "dictation-bar-mini": "The mini dictation bar — a small capsule showing the voice waveform",
    "replacements": "The Replacement list window: rules in the form heard arrow intended, with a rule counter at the bottom",
    "onboarding-welcome": "The first onboarding screen: the Heardly icon, a welcome line and the Start setup button",
    "onboarding-permissions": "The permissions step of onboarding: microphone, app audio and text insertion, each with its own Allow button",
    "export-panel": "The History window with the Export panel open: eight formats, switches for timecodes and source labels, and the Save as TXT button",
    "language-sheet": "The Recognition language sheet: an auto-detect switch, a search field and seventeen languages as cards",
}

FIGURE = re.compile(r"<figure>(.*?)</figure>", re.S)


def bilingual_figures(body: str, slug: str) -> str:
    """Каждый <figure> становится парой: русский кадр и английский.

    Прятать лишнее не нужно — правило html[data-lang] скрывает фигуру целиком,
    а внутри неё и неподходящий span подписи.
    """
    def pair(m):
        inner = m.group(1)
        src = re.search(r'src="img/([^"]+)\.png"', inner)
        if not src:
            raise SystemExit(f"{slug}: в <figure> нет снимка из img/")
        name = src.group(1)
        en_file = OUT / "img" / f"{name}-en.png"
        if not en_file.exists():
            raise SystemExit(f"{slug}: нет английского кадра {en_file.name}")
        if name not in ALT_EN:
            raise SystemExit(f"{slug}: нет английского alt для {name}")
        en_inner = inner.replace(f'src="img/{name}.png"', f'src="img/{name}-en.png"')
        en_inner = re.sub(r'alt="[^"]*"', lambda _: f'alt="{ALT_EN[name]}"', en_inner, count=1)
        return f"<figure lang=\"ru\">{inner}</figure>\n    <figure lang=\"en\">{en_inner}</figure>"

    return FIGURE.sub(pair, body)


def build(pages):
    OUT.mkdir(parents=True, exist_ok=True)
    for slug, p in pages.items():
        p = dict(p, body=bilingual_figures(p["body"], slug))
        html = SHELL.format(
            title_ru=p["title_ru"], title_en=p["title_en"],
            desc_ru=p["lede_ru"].replace('"', "&quot;"),
            lede_ru=p["lede_ru"], lede_en=p["lede_en"],
            group_ru=p["group_ru"], group_en=p["group_en"],
            body=p["body"].rstrip() + "\n",
        )
        (OUT / f"{slug}.html").write_text(html, encoding="utf-8")
        print("wrote", slug + ".html")


if __name__ == "__main__":
    sys.path.insert(0, str(pathlib.Path(__file__).parent))
    merged = {}
    for mod in sys.argv[1:]:
        merged.update(importlib.import_module(mod).PAGES)
    build(merged)

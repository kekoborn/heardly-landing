# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static HTML/CSS/JS, single file `index.html` (inferred: the landing was built that way and the user did not ask for a framework). The docs section under `docs/` is assembled by `docs/_src/gen.py`. The macOS app itself is Swift and lives in another repository; this record covers the marketing site.

## Users

Age 20–35 (owner, 2026-10-21). Bureaucratic, legal or old-office vocabulary and imagery ("стенограмма", "протокол", court stenography, rubber stamps) reads as 60+ and is off-brand; speak their everyday language.

Russian- and English-speaking people on Apple Silicon Macs who talk for a living: managers, founders, sales, consultants, researchers who sit in calls; developers and writers who would rather dictate than type (prompts for AI, mail, Slack); journalists, students and interviewers who turn recordings into text; people with sensitive material (lawyers, doctors, psychologists, NDA projects) who are not allowed or do not want to send audio to a cloud.

They arrive from search (comparing Heardly with MacWhisper, Wispr Flow, Teamlogs), from Telegram and social posts (have not heard of the category), and from word of mouth or the app itself (want to download or pay now).

## Product Purpose

Heardly is a menu-bar Mac app that turns speech into text on the computer itself: live call transcription (microphone + app audio, no bot joins the call), dictation into any text field via a hotkey, and audio/video file transcription. The site must let a visitor download the app and pay for Pro.

## Positioning

- Audio never leaves the Mac: the model (~600 MB, downloaded once) runs on the Neural Engine, works offline. In the Russian market every competitor (Teamlogs, Speech2Text, SaluteJazz, Telemost) processes audio on its servers.
- Three modes in one app is a benefit, not a unique claim: MacWhisper and Superwhisper also have dictation, bot-free calls and files.
- Russian speech and ruble pricing.
- Speed and accuracy measurements are not a positioning point and are not shown on the site (owner decision 2026-10-21).

## Operating Context

Visitors read on a Mac (the only platform the app supports), often in a browser next to a call or a document. Download is a notarized DMG from GitHub releases (`releases/latest/download/Heardly.dmg`). Payment: email + plan → `POST https://heardly-api.cafmanar.workers.dev/create-order` → Robokassa page; after paying, the user enters the email in Heardly → Settings → Subscription.

## Capabilities and Constraints

- macOS 14+, Apple Silicon only. No Windows, iOS, web app, team workspace, calendar bot, CRM sync.
- Free: 14 days of full Pro after install, no card; then 2,000 words a week of live + dictation, reset Monday.
- Pro: unlimited live + dictation, files with speaker separation, export (TXT, SRT, VTT, DOCX, PDF, Markdown, CSV, HTML), local AI summary (~2.5 GB model), `heardly` CLI / MCP connection to Claude and Codex, one subscription on all the user's Macs.
- Prices: RU 499 ₽/month, 3,990 ₽/year; EN $9.99/month, $79.99/year (charged 899 / 7,190 ₽). One-time payment, no auto-renewal.
- What goes online: one-time model download, subscription check, updates, anonymous crash reports; never audio or text.
- Undecided: recognition language list for Parakeet Ultra; refund policy; seller details, offer and privacy policy; support address; domain.

## Brand Commitments

- Name "Heardly", app icon `docs/logo.png`. The app's own palette («Лён и барвинок», `docs/design-system.md`) binds the app, not the site: the owner allowed a new visual world for the landing (2026-10-21).
- The app's waveform (`WaveformView`, mirrored smoothed 48-point shape) is a recognisable product element.
- Owner's tastes from the app work: soft and human, no glass, no shadows; numbers set without serifs.
- Quality bar named by the owner: Wispr Flow, Granola, Apple product pages, betterstack.com, lovable.dev, gradientshub.com, decimals.co, linearity.io, raycast.com/keyboard, router.com. Do not copy.
- Landing form (owner, 2026-10-21): no page-wide metaphor. A high-end product landing that shows the real product and every feature working, with a full demo screen of dictation, live mode and file transcription, lots of air, moderate smooth motion. Metaphor directions (stenographer, court record) were rejected.

## Evidence on Hand

Internal benchmarks exist (`.finetune-data/bench-2026-10-18/`) but are not used on the site; competitor facts verified on official sites 2026-10-21 (`landing-brain/sessions/heardly/competitors.md`); Apple notarization since v1.6.10. Absent and must not be invented: testimonials, user counts, customer logos, press.

## Product Principles

- Show the mechanism working rather than describing it.
- Every number carries its conditions (device, dataset, date).
- Honest about limits: who it is not for, what does go online.
- One clear next step: download, or pay.

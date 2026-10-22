#!/usr/bin/env python3
"""Заменяет настоящий email в блоке License на демо-адрес.

Поле покупки правится прямо в приложении, а строка под «Subscription on this Mac»
читается из лицензии и руками не меняется — поэтому её перерисовываем в картинке.
Публиковать личный адрес в документации нельзя.

Отступ и базовую линию берём у заголовка плашки, который стоит строкой выше:
так подставленный адрес встаёт ровно туда же, где стоял настоящий.
"""
import sys
from PIL import Image, ImageDraw, ImageFont

FONT = "/System/Library/Fonts/SFNS.ttf"
PLACEHOLDER = "you@example.com"
TITLE_BAND = (952, 988)    # «Subscription on this Mac» / «Подписка на этом Mac»
EMAIL_BAND = (992, 1030)   # строка адреса под ним
# Край плашки около x=483; начинаем правее, чтобы не принять рамку за текст.
SCAN_LEFT, SCAN_RIGHT = 505, 1200


def span(px, bg, band, left, right):
    """Границы текста в полосе: (x0, y0, x1, y1) или None."""
    xs, ys = [], []
    for y in range(*band):
        for x in range(left, right):
            if sum(abs(a - b) for a, b in zip(px[x, y], bg)) > 40:
                xs.append(x)
                ys.append(y)
    return (min(xs), min(ys), max(xs), max(ys)) if xs else None


def redact(path: str) -> None:
    im = Image.open(path).convert("RGB")
    px = im.load()
    bg = px[SCAN_RIGHT, sum(EMAIL_BAND) // 2]

    title = span(px, bg, TITLE_BAND, SCAN_LEFT, SCAN_RIGHT)
    email = span(px, bg, EMAIL_BAND, SCAN_LEFT, SCAN_RIGHT)
    if not title or not email:
        sys.exit(f"{path}: не нашёл строки блока License — проверь координаты")

    colour = min((px[x, y] for y in range(email[1], email[3] + 1)
                  for x in range(email[0], email[2] + 1)
                  if sum(abs(a - b) for a, b in zip(px[x, y], bg)) > 40), key=sum)

    draw = ImageDraw.Draw(im)
    draw.rectangle([email[0] - 6, EMAIL_BAND[0] - 6, email[2] + 10, EMAIL_BAND[1] + 6], fill=bg)

    target = email[3] - email[1]
    best = 10
    for size in range(10, 60):
        f = ImageFont.truetype(FONT, size)
        box = draw.textbbox((0, 0), PLACEHOLDER, font=f)
        if box[3] - box[1] <= target:
            best = size
    font = ImageFont.truetype(FONT, best)
    # Левый край — как у заголовка; верх — как у заменяемой строки.
    box = draw.textbbox((0, 0), PLACEHOLDER, font=font)
    draw.text((title[0] - box[0], email[1] - box[1]), PLACEHOLDER, font=font, fill=colour)
    im.save(path)
    print(f"{path}: адрес заменён (кегль {best}, цвет {colour}, x={title[0]}, y={email[1]})")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        redact(p)

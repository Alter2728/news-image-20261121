#!/usr/bin/env python3
"""Draw entry.png for news-image-20261121.

A 1024x1024 newspaper-style infographic summing up Saturday
21 November 2026 in six stories. Run at build time only; the
grader copies the finished PNG via main.py.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 243, 234)
INK = (26, 26, 26)
RED = (178, 34, 34)
GREY = (90, 90, 90)
PANEL_BG = (255, 255, 255)
RULE = (26, 26, 26)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill, max_w, leading):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def tag(draw, x, y, label, color):
    f = font(SANS_B, 17)
    w = draw.textlength(label, font=f) + 16
    draw.rectangle([x, y, x + w, y + 26], fill=color)
    draw.text((x + 8, y + 4), label, font=f, fill=(255, 255, 255))
    return y + 34


def icon_flags(d, x, y, s):
    # three podium flags: US / China / Russia (geometric, no emblems)
    cols = [(60, 60, 160), (200, 30, 30), (240, 240, 240)]
    for i, c in enumerate(cols):
        fx = x + i * (s // 3)
        d.rectangle([fx, y, fx + s // 3 - 6, y + s // 2], fill=c, outline=INK, width=2)
        d.line([fx, y, fx, y + s], fill=INK, width=3)
    d.line([x - 4, y + s, x + s + 4, y + s], fill=INK, width=3)


def icon_scales(d, x, y, s):
    cx = x + s // 2
    d.line([cx, y, cx, y + s - 8], fill=INK, width=4)
    d.line([x, y + 10, x + s, y + 10], fill=INK, width=4)
    for px in (x + 6, x + s - 6):
        d.line([px, y + 10, px - 14, y + s // 2], fill=INK, width=2)
        d.line([px, y + 10, px + 14, y + s // 2], fill=INK, width=2)
        d.arc([px - 16, y + s // 2 - 6, px + 16, y + s // 2 + 12], 0, 180, fill=INK, width=3)
    d.line([cx - 18, y + s - 4, cx + 18, y + s - 4], fill=INK, width=4)


def icon_chart(d, x, y, s):
    d.line([x, y, x, y + s], fill=INK, width=3)
    d.line([x, y + s, x + s, y + s], fill=INK, width=3)
    pts = [(x + 6, y + 14), (x + s // 3, y + 30), (x + 2 * s // 3, y + 22), (x + s - 8, y + s - 16)]
    d.line(pts, fill=RED, width=5)
    d.polygon([(x + s - 8, y + s - 16), (x + s - 22, y + s - 18), (x + s - 10, y + s - 30)], fill=RED)


def icon_burst(d, x, y, s):
    import math
    cx, cy = x + s // 2, y + s // 2
    for k in range(8):
        a = k * math.pi / 4
        r1, r2 = s // 6, s // 2
        d.line([cx + r1 * math.cos(a), cy + r1 * math.sin(a),
                cx + r2 * math.cos(a), cy + r2 * math.sin(a)], fill=RED, width=5)
    d.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], fill=(230, 140, 30), outline=INK, width=2)


def icon_badge(d, x, y, s):
    cx, cy, r = x + s // 2, y + s // 2, s // 2 - 4
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(230, 190, 60), outline=INK, width=3)
    d.ellipse([cx - r // 2, cy - r // 2, cx + r // 2, cy + r // 2], outline=INK, width=3)
    d.line([cx, cy - r + 6, cx, cy - 8], fill=INK, width=3)
    d.line([cx, cy + 8, cx, cy + r - 6], fill=INK, width=3)


def icon_leaf(d, x, y, s):
    d.ellipse([x + 6, y + 4, x + s - 6, y + s - 14], fill=(70, 150, 70), outline=INK, width=3)
    d.line([x + 12, y + s - 10, x + s - 14, y + 12], fill=INK, width=3)
    d.line([x + s // 2, y + s - 12, x + s // 2, y + s + 2], fill=INK, width=3)


def panel(d, x, y, w, h, tag_label, tag_color, headline, body, icon_fn):
    d.rectangle([x, y, x + w, y + h], fill=PANEL_BG, outline=RULE, width=2)
    yy = tag(d, x + 16, y + 14, tag_label, tag_color)
    icon_fn(d, x + w - 86, y + 14, 64)
    yy = text_block(d, x + 16, yy + 4, headline, font(SERIF_B, 30), INK, w - 110, 34)
    text_block(d, x + 16, yy + 6, body, font(SANS, 20), GREY, w - 32, 26)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # masthead
    title = "THE WORLD IN A DAY"
    tf = font(SERIF_B, 62)
    tw = d.textlength(title, font=tf)
    d.text(((W - tw) / 2, 26), title, font=tf, fill=INK)
    d.line([40, 108, W - 40, 108], fill=RULE, width=4)
    d.line([40, 116, W - 40, 116], fill=RULE, width=1)
    date = "SATURDAY 21 NOVEMBER 2026"
    df = font(SANS_B, 40)
    dw = d.textlength(date, font=df)
    d.text(((W - dw) / 2, 126), date, font=df, fill=RED)
    sub = "The day's world news in one picture"
    sf = font(SERIF, 24)
    sw = d.textlength(sub, font=sf)
    d.text(((W - sw) / 2, 176), sub, font=sf, fill=GREY)

    # lead story
    panel(d, 40, 216, W - 80, 168, "DIPLOMACY · SHENZHEN", (60, 60, 160),
          "Trump, Xi and Putin meet in Shenzhen",
          "The US, Chinese and Russian presidents held a 90-minute trilateral "
          "summit and signed a four-point peace declaration — silent on Ukraine.",
          icon_flags)

    # 2x2 grid
    gx, gy, gw, gh, gap = 40, 398, (W - 80 - 16) // 2, 206, 14
    panel(d, gx, gy, gw, gh, "JUSTICE · THE HAGUE", (110, 60, 140),
          "World Court: Myanmar guilty of genocide",
          "The ICJ found Myanmar responsible for genocide against the "
          "Rohingya — a first against a state.",
          icon_scales)
    panel(d, gx + gw + gap, gy, gw, gh, "MARKETS · GLOBAL", (160, 90, 20),
          "AI sell-off pushes markets into correction",
          "S&P 500 fell 3.7%, Nikkei 5.1%, Hang Seng 3.8% as the AI "
          "sell-off spread worldwide.",
          icon_chart)
    panel(d, gx, gy + gh + gap, gw, gh, "WAR · UKRAINE", RED,
          "Russian missile hits Zelensky's hometown",
          "A ballistic missile struck Kryvyi Rih, killing 2 and "
          "wounding 60; Kyiv was also hit.",
          icon_burst)
    panel(d, gx + gw + gap, gy + gh + gap, gw, gh, "AMERICAS · MEXICO", (40, 120, 90),
          "Mexico captures FBI most-wanted cartel boss",
          "Forces seized 'El Chapo Isidro' in Sinaloa; a burst of violence "
          "followed the arrest.",
          icon_badge)

    # bottom strip
    panel(d, 40, gy + 2 * gh + 2 * gap, W - 80, 116, "CLIMATE · ANTALYA", (70, 150, 70),
          "COP31 talks run past deadline over fossil fuels",
          "Negotiators in Turkey missed Friday's deadline; the draft text "
          "omits a fossil-fuel phase-out.",
          icon_leaf)

    # footer
    foot = "All six stories happened or were first reported on Saturday 21 November 2026."
    ff = font(SANS_B, 20)
    fw = d.textlength(foot, font=ff)
    d.text(((W - fw) / 2, H - 44), foot, font=ff, fill=INK)

    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()

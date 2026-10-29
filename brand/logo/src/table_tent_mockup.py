"""Render a Liinky table-tent mockup (logo + QR placeholder + call to action) to ../presentation/.

The QR pattern is decorative random noise with finder squares, not a scannable code.
"""
import os
import random
import re

import cairosvg

HERE = os.path.dirname(__file__)
FINAL = os.path.join(HERE, "..", "final")
OUT = os.path.join(HERE, "..", "presentation")
BERRY, INK, CREAM = "#E5245E", "#1C1433", "#FFF5EC"


def inner(name):
    """Contents and viewBox size of one of the final SVGs."""
    s = open(os.path.join(FINAL, name)).read()
    w, h = map(float, re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', s).groups())
    body = re.sub(r"^.*?</title>", "", s, flags=re.S).replace("</svg>", "").strip()
    return body, w, h


def place(name, x, y, width):
    body, w, h = inner(name)
    s = width / w
    return f'<g transform="translate({x} {y}) scale({s:.4f})">{body}</g>', h * s


def qr(x, y, size, n=29, seed=7):
    rnd = random.Random(seed)
    m = size / n
    cells = []
    finder = [(0, 0), (n - 7, 0), (0, n - 7)]

    def in_finder(i, j):
        return any(fx - 1 <= i <= fx + 7 and fy - 1 <= j <= fy + 7 for fx, fy in finder)

    def in_logo(i, j):
        c = n / 2
        return abs(i + 0.5 - c) < 5 and abs(j + 0.5 - c) < 5

    for i in range(n):
        for j in range(n):
            if not in_finder(i, j) and not in_logo(i, j) and rnd.random() < 0.5:
                cells.append(f'<rect x="{x + i * m:.2f}" y="{y + j * m:.2f}" width="{m:.2f}" height="{m:.2f}"/>')
    for fx, fy in finder:
        X, Y = x + fx * m, y + fy * m
        cells.append(f'<path fill-rule="evenodd" d="M{X} {Y} h{7 * m} v{7 * m} h{-7 * m} Z '
                     f'M{X + m} {Y + m} v{5 * m} h{5 * m} v{-5 * m} Z"/>')
        cells.append(f'<rect x="{X + 2 * m}" y="{Y + 2 * m}" width="{3 * m}" height="{3 * m}"/>')
    c = size / 2
    logo_tile = 9 * m
    tile = (f'<rect x="{x + c - logo_tile / 2:.2f}" y="{y + c - logo_tile / 2:.2f}" width="{logo_tile:.2f}" '
            f'height="{logo_tile:.2f}" rx="{logo_tile * 0.22:.2f}" fill="{BERRY}"/>')
    sym, _ = place("symbol/liinky-symbol-white.svg", x + c - logo_tile * 0.36, y + c - logo_tile * 0.36,
                   logo_tile * 0.72)
    return f'<g fill="{INK}">{"".join(cells)}</g>{tile}{sym}'


def main():
    W, H = 1280, 800
    parts = [f'<rect width="{W}" height="{H}" fill="#EDE6DE"/>',
             # table top and shadow
             f'<rect y="560" width="{W}" height="240" fill="#C9A98A"/>',
             f'<ellipse cx="640" cy="640" rx="260" ry="26" fill="#000" opacity="0.18"/>',
             # tent card (front face)
             f'<path d="M420 640 L470 120 H810 L860 640 Z" fill="{CREAM}"/>',
             f'<path d="M470 120 H810 L812 132 H468 Z" fill="#E8DCCF"/>']
    lockup, lh = place("liinky-horizontal.svg", 520, 170, 240)
    parts.append(lockup)
    parts.append(qr(540, 270, 200))
    parts.append(f'<text x="640" y="530" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" '
                 f'font-size="30" font-weight="700" fill="{INK}">Scan for the menu</text>')
    parts.append(f'<text x="640" y="568" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" '
                 f'font-size="20" fill="{INK}" opacity="0.7">Table 12 · order from your phone</text>')
    parts.append(f'<rect x="596" y="590" width="88" height="10" rx="5" fill="{BERRY}"/>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
           f'{"".join(parts)}</svg>')
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, "mockup-table-tent.svg")
    open(path, "w").write(svg)
    cairosvg.svg2png(url=path, write_to=os.path.join(OUT, "mockup-table-tent.png"))


if __name__ == "__main__":
    main()

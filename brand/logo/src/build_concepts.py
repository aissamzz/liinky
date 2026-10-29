"""Generate the round-1 Liinky logo concepts (black, greyscale) as SVG files.

Symbols use a 256 x 256 canvas; lockups keep height 256. Symbols are filled outlines. The exploratory
wordmark is drawn with round-capped strokes and must be expanded to outlines before final delivery.
"""
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "concepts")
INK = "#111111"


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-labelledby="title"><title id="title">{title}</title>{body}</svg>\n')


# --- symbols ---------------------------------------------------------------------------------------------

def symbol_shared_dot():
    # Two i-stems (44 wide, fully rounded) share one capsule tittle spanning both: "linked" letters / a table.
    return (f'<g id="symbol" fill="{INK}">'
            f'<rect x="60" y="32" width="136" height="48" rx="24"/>'
            f'<rect x="60" y="104" width="48" height="120" rx="24"/>'
            f'<rect x="148" y="104" width="48" height="120" rx="24"/>'
            f'</g>')


def symbol_smile():
    # Two i-stems join at the base into one U: two guests, one table, one smile.
    return (f'<g id="symbol" fill="{INK}">'
            f'<circle cx="88" cy="56" r="24"/><circle cx="168" cy="56" r="24"/>'
            f'<path d="M66 118 A22 22 0 0 1 110 118 V160 A18 18 0 0 0 146 160 V118 '
            f'A22 22 0 0 1 190 118 V160 A62 62 0 0 1 66 160 Z"/>'
            f'</g>')


def symbol_scan_corner():
    # The L of Liinky as a scan-frame corner, holding one QR module in the opposite corner.
    return (f'<g id="symbol" fill="{INK}">'
            f'<path d="M40 64 A24 24 0 0 1 88 64 V156 A12 12 0 0 0 100 168 H192 A24 24 0 0 1 192 216 '
            f'H96 A56 56 0 0 1 40 160 Z"/>'
            f'<rect x="160" y="40" width="56" height="56" rx="14"/>'
            f'</g>')


# --- wordmark (exploration: stroked) -----------------------------------------------------------------------

SW = 26          # stroke width
BASE, XH, ASC, DESC = 176, 100, 56, 216


def wordmark(x0, shared_dot=False):
    p = []
    x = x0
    p.append(f'M{x} {ASC} V{BASE}')                                   # l
    xi1 = x + 52
    xi2 = xi1 + 52
    p.append(f'M{xi1} {XH + 8} V{BASE}')                             # i
    p.append(f'M{xi2} {XH + 8} V{BASE}')                             # i
    xn = xi2 + 56
    p.append(f'M{xn} {XH} V{BASE} M{xn} 136 A34 34 0 0 1 {xn + 68} 136 V{BASE}')   # n
    xk = xn + 68 + 56
    p.append(f'M{xk} {ASC} V{BASE} M{xk + 52} {XH} L{xk + 4} 148 M{xk + 16} 136 L{xk + 56} {BASE}')  # k
    xy = xk + 56 + 48
    p.append(f'M{xy} {XH} V140 A34 34 0 0 0 {xy + 68} 140 M{xy + 68} {XH} V182 '
             f'A34 34 0 0 1 {xy + 34} {DESC} H{xy + 14}')                                   # y
    body = (f'<path fill="none" stroke="{INK}" stroke-width="{SW}" stroke-linecap="round" '
            f'stroke-linejoin="round" d="{" ".join(p)}"/>')
    if shared_dot:
        body += f'<rect x="{xi1 - 13}" y="56" width="{xi2 - xi1 + 26}" height="26" rx="13" fill="{INK}"/>'
    else:
        body += f'<circle cx="{xi1}" cy="69" r="14" fill="{INK}"/><circle cx="{xi2}" cy="69" r="14" fill="{INK}"/>'
    return f'<g id="wordmark">{body}</g>', xy + 68 + SW


def lockup(symbol_body, shared_dot=False):
    # Symbol scaled to 75 % and optically centred on the x-height band, wordmark to the right.
    s = 0.75
    sym = f'<g transform="translate(0 {round((256 - 256 * s) / 2 + 4)}) scale({s})">{symbol_body}</g>'
    wm, right = wordmark(232, shared_dot)
    return svg(right + 24, 256, sym + wm, "Liinky logo")


def main():
    os.makedirs(OUT, exist_ok=True)
    concepts = {
        "a-shared-dot": (symbol_shared_dot(), True),
        "b-smile": (symbol_smile(), False),
        "c-scan-corner": (symbol_scan_corner(), False),
    }
    for name, (body, shared) in concepts.items():
        with open(os.path.join(OUT, f"{name}-symbol.svg"), "w") as fh:
            fh.write(svg(256, 256, body, "Liinky symbol"))
        with open(os.path.join(OUT, f"{name}-lockup.svg"), "w") as fh:
            fh.write(lockup(body, shared))
    wm, right = wordmark(16, True)
    with open(os.path.join(OUT, "wordmark-shared-dot.svg"), "w") as fh:
        fh.write(svg(right + 16, 256, wm, "Liinky wordmark"))


if __name__ == "__main__":
    main()

"""Build the final Liinky logo masters (direction B, "Smile ii").

Outputs to ../final/: symbol, small-size symbol, outlined wordmark, horizontal and stacked lockups (colour and
reversed). The wordmark is drawn as round-capped strokes and expanded to filled outlines with shapely
(pip install shapely), so no font or stroke settings are needed downstream.
"""
import math
import os

from shapely.geometry import LineString, Point
from shapely.ops import unary_union
from shapely import affinity

OUT = os.path.join(os.path.dirname(__file__), "..", "final")

BERRY = "#E5245E"
INK = "#1C1433"
WHITE = "#FFFFFF"


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:g} {h:g}" width="{w:g}" height="{h:g}" '
            f'role="img" aria-labelledby="title"><title id="title">{title}</title>{body}</svg>\n')


# --- symbol ----------------------------------------------------------------------------------------------

def smile_path(cx1, cx2, stem, top, base):
    """Two fully rounded i-stems (width `stem`, top-cap centre y=`top`) joined by a U whose straight sides end
    at y=`base`."""
    r = stem / 2
    inner = (cx2 - cx1) / 2 - r
    outer = (cx2 - cx1) / 2 + r
    l, li, ri, rr = cx1 - r, cx1 + r, cx2 - r, cx2 + r
    return (f"M{l:g} {top:g} A{r:g} {r:g} 0 0 1 {li:g} {top:g} V{base:g} "
            f"A{inner:g} {inner:g} 0 0 0 {ri:g} {base:g} V{top:g} A{r:g} {r:g} 0 0 1 {rr:g} {top:g} V{base:g} "
            f"A{outer:g} {outer:g} 0 0 1 {l:g} {base:g} Z")


def symbol(color=BERRY, small=False):
    if small:  # favicon cut: heavier stems, bigger dots, wider gaps so the counters stay open at 16 px
        dots = [(80, 48, 28), (176, 48, 28)]
        d = smile_path(80, 176, 56, 124, 150)
    else:
        dots = [(88, 56, 24), (168, 56, 24)]
        d = smile_path(88, 168, 44, 118, 160)
    circles = "".join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in dots)
    return f'<g id="symbol" fill="{color}">{circles}<path d="{d}"/></g>'


SYMBOL_BBOX = (64, 32, 192, 222)   # x0, y0, x1, y1 of the regular symbol on its 256 canvas


# --- wordmark --------------------------------------------------------------------------------------------

SW = 26
BASE, XH, ASC, DESC = 176, 100, 56, 216


def arc(cx, cy, r, a0, a1, n=48):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)),
             cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]


def wordmark_geometry():
    """Return (letters, dots): stroked letter skeletons as one outlined shape, and the two i-dots."""
    lines = []
    x = 0
    lines.append([(x, ASC), (x, BASE)])                                   # l
    xi1, xi2 = x + 52, x + 104
    lines.append([(xi1, XH + 8), (xi1, BASE)])                            # i
    lines.append([(xi2, XH + 8), (xi2, BASE)])                            # i
    xn = xi2 + 56                                                          # n
    lines.append([(xn, XH), (xn, BASE)])
    lines.append([(xn, BASE)] + [(xn, 136)] + arc(xn + 34, 136, 34, 180, 360) + [(xn + 68, BASE)])
    xk = xn + 68 + 56                                                      # k
    lines.append([(xk, ASC), (xk, BASE)])
    lines.append([(xk + 52, XH), (xk + 4, 148)])
    lines.append([(xk + 16, 136), (xk + 56, BASE)])
    xy = xk + 104                                                          # y
    lines.append([(xy, XH), (xy, 140)] + arc(xy + 34, 140, 34, 180, 0))
    lines.append([(xy + 68, XH), (xy + 68, 182)] + arc(xy + 34, 182, 34, 0, 90) + [(xy + 14, DESC)])
    letters = unary_union([LineString(p).buffer(SW / 2, quad_segs=16) for p in lines])
    dots = unary_union([Point(xi1, 69).buffer(14, quad_segs=16), Point(xi2, 69).buffer(14, quad_segs=16)])
    return letters, dots


def to_path(geom):
    geom = geom.simplify(0.15, preserve_topology=True)   # drop near-collinear points; max deviation 0.15 units
    polys = getattr(geom, "geoms", [geom])
    out = []
    for poly in polys:
        for ring in [poly.exterior, *poly.interiors]:
            pts = list(ring.coords)[:-1]
            out.append("M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + " Z")
    return " ".join(out)


def wordmark(dx, dy, ink=INK, dot=BERRY, scale=1.0):
    letters, dots = wordmark_geometry()
    letters = affinity.translate(affinity.scale(letters, scale, scale, origin=(0, 0)), dx, dy)
    dots = affinity.translate(affinity.scale(dots, scale, scale, origin=(0, 0)), dx, dy)
    return (f'<g id="wordmark"><path fill="{ink}" fill-rule="evenodd" d="{to_path(letters)}"/>'
            f'<path fill="{dot}" d="{to_path(dots)}"/></g>')


def wordmark_bounds():
    letters, dots = wordmark_geometry()
    return unary_union([letters, dots]).bounds


# --- lockups ---------------------------------------------------------------------------------------------

PAD = 32


def placed_symbol(s, x, y, color):
    """Symbol scaled by s with its bbox top-left at (x, y)."""
    tx, ty = x - SYMBOL_BBOX[0] * s, y - SYMBOL_BBOX[1] * s
    return f'<g transform="translate({tx:.2f} {ty:.2f}) scale({s:g})">{symbol(color)}</g>'


def horizontal(ink=INK, mark=BERRY, dot=BERRY):
    wx0, wy0, wx1, wy1 = wordmark_bounds()
    cap = BASE + SW / 2 - (ASC - SW / 2)              # ascender-to-baseline height of the wordmark
    s = (cap + 6) / (SYMBOL_BBOX[3] - SYMBOL_BBOX[1])  # symbol a touch taller than the ascenders (U overshoot)
    sym_w = (SYMBOL_BBOX[2] - SYMBOL_BBOX[0]) * s
    gap = 48
    top = PAD + (ASC - SW / 2 - wy0)
    body = placed_symbol(s, PAD, top - 3, mark)
    dx = PAD + sym_w + gap - wx0
    dy = PAD - wy0
    body += wordmark(dx, dy, ink, dot)
    w = dx + wx1 + PAD
    h = PAD + (wy1 - wy0) + PAD
    return w, h, body


def stacked(ink=INK, mark=BERRY, dot=BERRY):
    wx0, wy0, wx1, wy1 = wordmark_bounds()
    ww = wx1 - wx0
    s = 1.0
    sym_w = (SYMBOL_BBOX[2] - SYMBOL_BBOX[0]) * s
    sym_h = (SYMBOL_BBOX[3] - SYMBOL_BBOX[1]) * s
    w = ww + 2 * PAD
    body = placed_symbol(s, (w - sym_w) / 2, PAD, mark)
    wy = PAD + sym_h + 56
    body += wordmark(PAD - wx0, wy - wy0, ink, dot)
    h = wy + (wy1 - wy0) + PAD
    return w, h, body


def write(name, w, h, body, title="Liinky logo"):
    with open(os.path.join(OUT, name), "w") as fh:
        fh.write(svg(round(w), round(h), body, title))


def main():
    os.makedirs(OUT, exist_ok=True)
    write("liinky-symbol.svg", 256, 256, symbol(), "Liinky symbol")
    write("liinky-symbol-small.svg", 256, 256, symbol(small=True), "Liinky symbol (small sizes)")
    wx0, wy0, wx1, wy1 = wordmark_bounds()
    write("liinky-wordmark.svg", wx1 - wx0 + 2 * PAD, wy1 - wy0 + 2 * PAD,
          wordmark(PAD - wx0, PAD - wy0), "Liinky wordmark")
    write("liinky-horizontal.svg", *horizontal())
    write("liinky-horizontal-reversed.svg", *horizontal(ink=WHITE))
    write("liinky-stacked.svg", *stacked())
    write("liinky-stacked-reversed.svg", *stacked(ink=WHITE))


if __name__ == "__main__":
    main()

# Liinky logo

Designed with the project skill `.claude/skills/logo-design` ([kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill), MIT).

- `BRIEF.md` — design brief, word map and concept longlist
- `concepts/`, `concepts-round1.png`, `preview.html` — round 1 (three greyscale concepts and test sheet)
- `final/` — **the chosen logo (Smile ii)**: masters, lockups, one-colour variants, PNGs, web icon set
- `GUIDELINES.md` — how to use the logo: versions, clear space, minimum sizes, colours, don'ts
- `presentation/` — presentation board (`liinky-presentation.html`, `slides/*.png`) and a table-tent QR mockup
- `src/` — scripts that regenerate everything (`python3 src/build_final.py`, needs `pip install shapely`;
  mockup needs `cairosvg`)

## Handover notes
- **Wordmark outlines**: drawn as round-capped strokes and expanded to filled outlines in code. Curves are stored as
  fine polyline segments (max deviation 0.15 units on a 256-unit-tall artboard), so the files are heavier than a
  hand-drawn Bézier version (~400 points). They render smoothly at every size; if a printer or sign-maker asks for
  "clean curves", have a designer redraw them with Béziers in Illustrator/Figma, using these files as the template.
- **Symbol**: exact geometry (circles + one arc path), 15 points — production-ready as is.
- **Colour codes**: CMYK and Pantone values are conversions; check against a printed swatch before a big print run.
- **Trademark**: not checked. Run a trademark search (e.g. EUIPO/USPTO/your national office) and a reverse image search
  before launch.
- **Tests run**: SVG audit (symbol 100/100; lockups flagged only for point count, see above), 16/32/48 px favicon
  check, one-colour, reversed and blur checks on the round-1 test sheet, mockups reviewed visually.

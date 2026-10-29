# Liinky — Logo Guidelines

## 1. The logo
- **Idea**: the two i's of Liinky join at the base into a smile: two guests, one happy table. The two dots come back
  as berry i-dots in the wordmark.
- **Versions** (all in `final/`):

| Version | Colour | On dark | Use it for |
|---|---|---|---|
| Horizontal (primary) | `liinky-horizontal.svg` | `liinky-horizontal-reversed.svg` | website header, app top bar, emails, documents |
| Stacked | `liinky-stacked.svg` | `liinky-stacked-reversed.svg` | square spaces, table tents, posters, splash screens |
| Symbol | `liinky-symbol.svg` | `symbol/liinky-symbol-white.svg` | app icon, avatar, QR-code centre badge, stickers |
| Symbol, small sizes | `liinky-symbol-small.svg` | — | anything under 32 px (favicon) |
| Wordmark | `liinky-wordmark.svg` | `wordmark/liinky-wordmark-white.svg` | when the symbol is already nearby |

One-colour versions (black, white, Berry, Ink) for each are in `horizontal/`, `stacked/`, `symbol/` and `wordmark/`,
as SVG plus PNG. Use SVG wherever possible.

## 2. Clear space
Keep a clear zone of **one symbol dot** (the diameter of one of the symbol's round dots) around the logo on all
sides. The zone scales with the logo.

## 3. Minimum size
| Version | Screen | Print |
|---|---|---|
| Horizontal | 96 px wide | 25 mm wide |
| Stacked | 64 px wide | 18 mm wide |
| Symbol | 32 px (16–31 px: use `liinky-symbol-small.svg` / the favicon files) | 6 mm |

## 4. Colour
| Name | HEX | RGB | CMYK (approx.) | Pantone (nearest, confirm with a swatch) |
|---|---|---|---|---|
| Berry (primary) | `#E5245E` | 229 36 94 | 0 84 59 10 | 1925 C |
| Ink (text, dark backgrounds) | `#1C1433` | 28 20 51 | 45 61 0 80 | 5255 C |
| Cream (warm background) | `#FFF5EC` | 255 245 236 | 0 4 7 0 | — |

Contrast: Berry on white 4.4 : 1 · Berry on Ink 4.0 : 1 · Ink on white 17.5 : 1.

**Approved logo/background pairs**: colour logo on white or Cream · reversed logo (Berry symbol, white wordmark) on
Ink · white logo on Berry · black or Ink logo on white for one-colour print. On photos, use the white version on a
calm, dark area, or place the symbol on a Berry rounded square (the app-icon tile).

**Next to a QR code**: put the white symbol on a Berry rounded square in the centre of the code (keep it under
~9 × 9 modules and use error-correction level H), and the horizontal or stacked logo above the code, never touching it.

## 5. Typography
- The wordmark is custom-drawn artwork; never retype "liinky" in a font.
- Suggested UI/marketing typeface: **Nunito** (SIL Open Font License, Google Fonts) — rounded, friendly, matches the
  wordmark. Headlines 700–800, body 400–600. Fallback: `system-ui, sans-serif`.

## 6. Don'ts
Don't stretch or squash · don't recolour outside the palette (e.g. no Berry wordmark with an Ink symbol) · don't
rotate · don't add shadows, outlines, gradients or effects · don't rearrange or resize the parts of a lockup · don't
use the regular symbol below 32 px (use the small version) · don't place on busy backgrounds without the Berry tile ·
don't recreate the wordmark by typing it.

## 7. Web icons
`final/web/` has `favicon.ico`, `favicon.svg`, PNG favicons, `apple-touch-icon.png`, `icon-192/512.png`,
`maskable-512.png` and `site.webmanifest`. Copy them to the site's public root and paste `head-snippet.html` into
`<head>`.

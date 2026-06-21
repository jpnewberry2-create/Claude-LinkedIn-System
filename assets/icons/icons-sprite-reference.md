# Icon Sprite Reference — v4

The complete icon system for the Jamie Newberry LinkedIn brand. One consolidated file,
`icons-sprite.svg`, holds every glyph and background tile. This document is the index.

## At a glance

- **78 line glyphs** (`glyph-` prefix) + **9 background tiles** (`bg-` prefix) = 87 symbols.
- Glyphs: single-weight line style, **stroke 2 on a 24×24 viewBox**, round caps and joins.
- Tiles: squircle (rounded square with a soft gloss), **256×256 viewBox**, nine palette colours.
- The 51 original glyphs plus 27 added in the v4 icon build (LinkedIn-action, content and
  editorial sets).

## How the icons are used

A carousel icon is a **glyph composited onto a coloured tile**: the glyph sits centred at
~54% of the tile size. On dark tiles (pink, ink-blue, dark-blue, lilac, chart-blue, charcoal)
the glyph is **white**; on light tiles (teal, orange) the glyph is **charcoal** for contrast.

Because Canva cannot recolour uploaded raster images, glyphs are exported **pre-coloured** —
flat transparent PNGs in white `#FFFFFF`, charcoal `#1E293B`, and ink `#0476D0` — and the
common glyph+tile pairings are exported as finished **composite tile PNGs** that drop into
Canva complete. Naming: `glyph-{name}-{colour}.png`, `tile-{colour}.png`, `tile-{glyph}-{colour}.png`.

Standard carousel tile sizes: **148.5px** on single-icon / process slides (S04), **120px** on
the 2×3 grid (S07), **144px** for the SWIPE cue, **164px** for the large CTA tiles.

---

## Background tiles (9)

| Tile id | Hex | Glyph colour on it | Typical use |
|---|---|---|---|
| `bg-ink-blue` | `#0476D0` | white | Follow CTA, primary actions |
| `bg-chart-blue` | `#12B1FF` | white | Process step 1, save/share, info |
| `bg-pink` | `#FF107A` | white | SWIPE, comment, emphasis, CTAs |
| `bg-lilac` | `#9671F1` | white | Process/grid accents |
| `bg-chart-lilac` | (lilac chart) | white | Chart-matched tiles |
| `bg-dark-blue` | `#024A86` | white | Deep accent |
| `bg-charcoal` | `#1E293B` | white | Neutral/reserve |
| `bg-teal` | `#2CEEF0` | **charcoal** | Light tile — glyph goes dark |
| `bg-orange` | `#F9AB51` | **charcoal** | Light tile — glyph goes dark |

---

## Glyphs by category (78)

### Arrows & navigation (7)
`arrowup` · `arrowdown` · `arrowleft` · `arrowright` · `swipe1` · `swipe2` · `swipe3`
The swipe chevrons are the cue tiles on the cover and early slides; `swipe1` is the default.

### LinkedIn actions (11)
`like` · `comment` · `write-comment` · `repost` · `send` · `save` · `share` · `follow` · `link` · `download` · `vote`
Mirror LinkedIn's own UI affordances. Used on the CTA slides: `follow` (S10), `write-comment` (S11), `save`/`send` (S12). `write-comment` is the bubble-with-pencil; plain `comment` is the empty bubble.

### Faces & reactions (8)
`facehappy` · `facelaugh` · `facewink` · `faceneutral` · `facesad` · `faceangry` · `facesurprised` · `faceunamused`
Use sparingly. `faceneutral` reads as "meh / unimpressed" — fits obligation or flat-response lines, not enthusiasm.

### Ideas & insight (8)
`idea` (lightbulb) · `insight` (magnifying glass) · `ai` (4-point sparkle) · `new` (burst/tag) · `prediction` (crystal ball) · `question` (? in circle) · `ask-question` (raised hand) · `help` (life buoy)

### Work & business (13)
`career` (briefcase) · `suited-man` (tie figure) · `board-meeting` (table + dots) · `strategy` (target) · `product` · `code` · `data` (bar chart) · `revenue` (£) · `milestone` · `template` (layout frame) · `demo` (screen + play) · `calendar` · `newsletter`

### Growth & momentum (11)
`growth` · `growthexp` · `momentum` · `momentumslow` · `rocket` · `win` (trophy) · `reach` (globe) · `engagement` · `network` · `audience` · `community`

### States & concepts (20)
`risk` (warning triangle) · `bad` · `slow` (snail) · `delay` (clock + arrow) · `tired` · `shush` (finger to lips) · `no-substance` (empty/hollow) · `puppet` (figure on strings) · `trust` (shield + check) · `make` · `conversation` · `speech` · `loud-speaker` · `learn` · `learning` (open book) · `graduate` (cap) · `chess` · `present` (gift) · `profile` (person) · `video`

---

## The 27 glyphs added in v4

`ask-question` · `board-meeting` · `calendar` · `chess` · `delay` · `demo` · `download` ·
`follow` · `graduate` · `learn` · `link` · `loud-speaker` · `new` · `no-substance` ·
`prediction` · `present` · `puppet` · `repost` · `save` · `send` · `shush` ·
`speech` · `suited-man` · `template` · `tired` · `vote` · `write-comment`

---

## Files & where they live

- **`icons-sprite.svg`** — the single source of truth. All 87 symbols. Edit here; everything
  else derives from it.
- **Pre-coloured PNG exports** (Canva upload set) — `glyph-{name}-{white|charcoal|ink}.png`,
  512×512 transparent.
- **Composite tile PNGs** — `tile-{glyph}-{colour}.png`, glyph baked onto the coloured squircle.
- **`real_glyphs.py`** — the renderer helper: extracts the sprite to standalone SVGs and
  composites glyph-on-tile for the reference carousel renderer. Not part of the live Canva
  pipeline (Canva is the source of truth for slides); kept as a backup/reference tool.

## Editing rules

- New glyphs must match the set: line style only, stroke 2 on 24×24, round caps/joins, single
  stroke colour, transparent background, no fills, no text, consistent optical weight.
- Light tiles (teal, orange) always take a charcoal glyph; all other tiles take white.
- After adding a glyph to `icons-sprite.svg`, re-export its three pre-coloured PNGs and any
  composite tiles, and add a row to this reference.

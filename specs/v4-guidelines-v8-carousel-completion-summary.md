# v4.0 Guidelines — Completion Summary

**Date:** 21 June 2026
**Status:** Complete. The News & Insights carousel and the v4.0 brand guidelines are finished and signed off.
**Companion doc:** `canva-build-log.md` holds the full decision history.

---

## 1. What this chat delivered

This chat finished the News & Insights carousel, brought the v4.0 guidelines fully into line with
it, rebuilt the supporting files, and cleaned the project for hand-off. Specifically:

- **Carousel finalised** in Canva (design `DAHNNfv1MMw`): all 12 slides signed off, including
  several rounds of copy refinement (S03 tense fix, S09 numbered-list layout, S10 and S11 copy),
  the circled-arrow SWIPE cue, and the enlarged CTA pills.
- **v4.0 guidelines updated** to match: all 12 template-card thumbnails refreshed from the final
  slides; the S06 matrix two-line label rule and colour-quality system documented; design
  reference pointed at `DAHNNfv1MMw`; the Next list and status page brought current. Rebuilt to
  20 pages, fonts embedded, full-bleed cover, and QA'd (automated sweep + every page inspected
  visually).
- **Icon system** consolidated to 78 glyphs + 9 tiles, with a self-contained HTML reference.
- **Quote-mark font** (oversized double marks) built, tested, and parked — standard marks kept.
- **Transparent wordmarks** supplied for all six variants (01/02/03 × light/dark), closing the
  long-standing no-alpha issue.
- **carousel.py and real_glyphs.py** synced to the 78-glyph sprite, x108 margin, and final S10/S11
  copy (reference/backup only — Canva remains the source of truth).
- **Project cleaned**: redundant v7-era and v3.5 files removed.

---

## 2. The canonical design — critical

- **CURRENT / SOURCE OF TRUTH: `DAHNNfv1MMw`** — shortlink `https://canva.link/1v2ypgenxdmbh5n`.
  All final changes live here.
- **OLD / SUPERSEDED: `DAHMZ37HNnU`** ("JN Carousel Master v7") — do not use.
- Brand Kit: **"*NEW* LinkedIn Brand - June 26"**, ID `kAHLoHtCCJc`.

---

## 3. Final carousel copy (all 12 slides, signed off)

- **S01** NEWS & INSIGHTS — Why most enterprise AI projects *never ship.* / It's not the technology. It never was.
- **S02** NEWS & INSIGHTS — 95% / of enterprise GenAI pilots *deliver no return.*
- **S03** NEWS & INSIGHTS — "The hard part was never the code. It was knowing *what was worth building.*"
- **S04** THE PATTERN — How it usually goes. (board-meeting → faceneutral → snail → £)
- **S05** THE ODDS — Even before AI. (bar 31/52/17, Standish CHAOS)
- **S06** THE TRADE OFF — AI spend vs AI return. (2×2 matrix)
- **S07** THE BLOCKERS — Why they stall. (6-icon grid)
- **S08** THE DROP OFF — Most never leave the demo. (funnel 100/60/20/5, MIT NANDA 2025)
- **S09** WHAT WORKS — The 5% do this. (numbered list 1–4)
- **S10** FOLLOW — I share how to bring ideas to life. ("Follow Me" pill)
- **S11** YOUR TURN — What's the most common reason you've seen AI pilots fail? ("Comment Below" pill)
- **S12** KEEP THIS — Save this for your next AI pitch. ("Save & Send" pill)

---

## 4. NEXT STEPS (in order)

1. **File the deliverables to the local hard drive** (see the checklist in section 5), so Claude
   Code can push them to GitHub.
2. **Publish the carousel as a Canva Brand Template.** This is the milestone: it makes the deck
   autofill-ready and bakes colour / line-height / spacing into the text boxes. Until it's
   published, post by duplicating the design and editing.
3. **Post the first carousel** and start the testing phase. The system is ready — the first few
   posts will teach more than further polishing.
4. **Build the other three pillar variants** (Thought Pieces V4 warm-pink, Best Practice V2 pink,
   reserve V1 warm) by duplicating the News & Insights design and swapping the background, once
   the first pillar has proven out.

---

## 5. CHECKLIST — file these to the local hard drive for GitHub

Download from this chat's outputs and place in the repo, replacing older versions. These are the
files that changed or are canonical:

**Guidelines (replace existing):**
- [ ] `brand-guidelines-v4.0.html` — the latest build (1182KB), all 12 final thumbnails, matrix
      requirements documented. Replaces the older `brand-guidelines-v4_0.html` in the project.
- [ ] `brand-guidelines-v4.0.pdf` — 20-page rendered PDF. (Distinct from the carousel PDF.)

**Reference / code (replace existing):**
- [ ] `canva-build-log.md` — full decision history, updated through this session.
- [ ] `carousel.py` — renderer, synced to final S10/S11 copy + 78-glyph map + x108 margin.
- [ ] `real_glyphs.py` — glyph helper, 78 glyphs, 9 tiles.
- [ ] `icons-sprite-reference.html` and `icons-sprite-reference.md` — the 78-glyph reference.

**Assets (replace the flat-RGB / mis-sized versions already in the project):**
- [ ] `wordmark01onlight.png`, `wordmark01ondark.png`
- [ ] `wordmark02onlight.png`, `wordmark02ondark.png`
- [ ] `wordmark03onlight.png`, `wordmark03ondark.png`
      (all six now transparent RGBA)
- [ ] `compositeV1warm1080x1350.png`, `compositeV4warmpink1080x1350.png`,
      `frostedpaneltransparent1080x1350.png` (corrected to true 1080×1350)

**Fonts (if not already in the repo):**
- [ ] The 8 Brand Kit fonts (`JN-*.ttf`) plus `FrauncesJN-*` / `InterJN-*` families.
      Note: `JN-Quote-BigMarks.ttf` is PARKED — do not upload to the Brand Kit; delete it there
      if it was uploaded.

**Already in the project, no change needed:**
- `JN_Carousel_Master_v8.pdf` (the high-res carousel posting artefact), `content-playbook.md`,
  `research-table.md`, `profile-review.md`, `profileradial.png`, `photofullbody.png`,
  the four raw fractal backgrounds, `project-os-spec.html`, the 12 slide PNGs (s01–s10c).

**Repo hygiene note:** the project still holds older copies of the guidelines HTML and a
flat-RGB wordmark set; the GitHub push should overwrite these with the versions above. The
icon `icons-sprite.svg` source can't be uploaded through the chat (SVG upload blocked) — the
HTML reference stands in for it.

---

## 6. The locked system (do not reopen)

**Positioning:** "Bringing ideas to life." Profile is credibility, content is personality.
**Voice:** UK English, banned-words list, no em-dashes. Warm, direct, builder-biased.

**Visual identity (v4.0):**
- Fonts: Fraunces (SemiBold 600, display) + Inter (400–900, body/UI). Eight pre-tracked Brand Kit
  fonts (letter-spacing baked in).
- Palette: Canvas #F8FAFC, Ink #0476D0, Dark Blue #024A86, Charcoal #1E293B, Slate #334155,
  Accent Pink #FF107A (CTA/emphasis <5%).
- Colour rule: Slate = display/editorial text; Charcoal = body in lists/grids beside icons
  (S04/S07/S09); Ink = kickers, italic accents, subtitles, axis labels, CTA directives. Accent
  italics are Ink only (Lilac is a chart/numeral colour, not an accent).
- Margin: x108 left, x972 right, content width 864px. Bottom-zone left margin x140.
- Two footer sizes: ~126px on statement slides (covers + CTAs), ~95px on data slides.
- Kicker strategy: cover = pillar name (NEWS & INSIGHTS) at 28–30pt; inner slides = slide-type
  label at 24pt. No hyphens (THE TRADE OFF, THE DROP OFF).
- Type scale: Hero/Stat 200, Title 110, CTA 92, Hook/Quote 68, Section/Support 52, Subtitle 40,
  Body 34, Kicker 24.
- Squircle panel 1032×1290 on 1080×1350; fractal-glass background baked in.

**S06 matrix (locked, documented in guidelines):**
- Colour encodes quadrant quality, not the pink-warning rule: bottom-left (low/low) red (worst);
  other weak quadrants pink; top-right (high/high) blue (best); two medium quadrants purple.
- Label boxes are deliberately different widths so all four labels wrap to exactly two lines for
  equal visual weight.

**Icons:** 78 glyphs (51 original + 27 new) + 9 tiles in `icons-sprite.svg`. White glyph on dark
tiles, charcoal on teal/orange. Pre-coloured PNG export workflow (Canva can't recolour raster).

---

## 7. Working principles (how Jamie works)

- Lead with the answer. Confident, direct, dense. UK English. Banned-words list. No em-dashes.
- Batch decision questions; give a recommendation, not just options. Flag wrong assumptions.
- Visually inspect rendered output before claiming it's right — render to image and look.
- Canva is the source of truth for the slides; carousel.py is reference/backup only.
- Connector can read/edit existing Canva elements and resolve shortlinks, but cannot create new
  text elements, read Brand Kit fonts/colours, or read element colours. Signed S3 thumbnail URLs
  aren't fetchable via bash/web — use exports/screenshots to QA visuals.
- `/mnt/project/` is stable across sessions; `/home/claude/` resets (copy outputs to
  `/mnt/user-data/outputs/` to persist).

---

## 8. Deferred / later (not blocking)

- Other three pillar variants (after News & Insights proves out).
- Profile rewrite (headline, About, Featured); banner/featured asset rebuild.
- Performance feedback loop into content strategy.
- Notion Life OS restructure (separate workstream).
- The `li-brand-` skill .md files (seven scoped, build order undecided).
- Oversized quote-mark font (parked).

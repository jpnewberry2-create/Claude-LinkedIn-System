# JN Carousel Master v7 — Build Log

Running decision log. Updated as Jamie builds slides and gives commentary. Claude adds assessment and flags downstream work in real time.

**Scope column:** "All" = applies to every slide. "S##" = specific slide only.
**Agreement column:** ✓ Agree / ~ Partial / ✗ Disagree + reason.
**Status:** 🔒 Locked | 🔄 In progress | ⏳ Pending Jamie confirm | 🚧 Work queued

---

## Decision & Change Log

| # | Scope | Jamie's decision / observation | Actual change made | Claude agrees? | Downstream updates needed | Status |
|---|---|---|---|---|---|---|
| 1 | All | Left margin x108, not x93. Content width 864, right edge x972. | Adopted x108 as the system margin after S01 build. | ✓ x108 gives cleaner optical margin inside the squircle panel corner. Better than x93. | Build spec margin updated to x108. Chrome prompt to use x108. | 🔒 |
| 2 | All | 4-column Canva guides, 18pt gutters. Key lines: 1/3 ≈ x396, 2/3 ≈ x684, 3/4 ≈ x756. | Guides set in Canva design. | ✓ Consistent with V7 distribution logic. | Add column positions to build spec reference table. | 🔒 |
| 3 | All | Even distribution: content blocks distributed evenly between hook heading bottom and footer wordmark top. No fixed gaps. | Applied by Jamie on S04, S05. Consistent with V7 renderer formula. | ✓ This is exactly what the V7 renderer does mathematically. Good that it's confirmed by eye too. | Build spec to replace fixed Y coords with the distribution rule as the primary instruction. | 🔒 |
| 4 | All | Text boxes stack directly — top edge of one block meets bottom edge of the one above. | Applied from S02 onwards. | ✓ Keeps the layout tight and deliberate. | Note in build spec and Chrome prompt. | 🔒 |
| 5 | All | Full stops on everything. Exception: single-word labels (SWIPE) and kickers. | Editorial rule, applied going forward. | ✓ Correct. The V7 copy already does this; good to make it explicit. | Update any V7 copy in the build spec that's missing full stops. Amend guidelines copy rules. | 🔒 |
| 6 | All | Footer wordmark centred. 84px height. | Committed to S01 via connector. | ✓ Matches V7 spec. | Already in build spec. No further change needed. | 🔒 |
| 7 | All | SWIPE tile: width ≈ span from 2/3 line to right margin (≈ 288px), tile ≈ 144px centred in right third. If in doubt, left edge to 1/3 line. | Applied from S01. | ✓ Gives the SWIPE tile a consistent optical weight across all slides. | Build spec SWIPE rule updated to column-based positioning. | 🔒 |
| 8 | All | Line height and letter spacing need setting per element — cannot be baked into font files or Brand Kit. | No change possible at font/kit level. Will be pre-set in published Brand Templates. | ✓ Confirmed limitation. Line height is a paragraph property, not a font metric. Only fix is publishing templates. | Noted in connector behaviour log. Add to Chrome prompt: set line height per element. | 🔒 |
| 9 | All | Brand Kit cannot assign default colour to a font style. Colour set manually per element. | No change possible at kit level. Pre-set in published Brand Templates. | ✓ Confirmed Canva limitation. | Noted in connector behaviour log. Add to Chrome prompt: set colour per element. | 🔒 |
| 10 | All | Hook headings need a bolder weight — current SemiBold 600 not punchy enough. | JN-Hook-Black (Fraunces 900, display axis) to be generated for comparison. | ✓ Fraunces Black at 68pt on the frosted panel will read significantly stronger. Worth trialling. | Generate JN-Hook-Black TTF. Add to Brand Kit. Update build spec if adopted. Update guidelines type table. | 🚧 |
| 11 | All | New icons needed: tired, suited man, shush, demo, delay/time, calendar, no substance, puppet. | Queue for icon build session. Check 60-glyph sprite first for existing matches. | ✓ All valid content-pillar concepts. Good timing to build before templates are published. | Build new SVG glyphs. Add to sprite. Update icons-sprite-reference.md. Update guidelines icon section. | 🚧 |
| 12 | S01 | Kicker changed to "NEWS & INSIGHTS" (pillar label) rather than slide-specific topic label. | Applied in Canva. This slide is the News & Insights template. | ✓ Correct — the kicker identifies the content pillar on a template, not a per-post topic. Future posts swap this text via autofill. | Build spec: kicker on all templates = pillar name, not topic. Note in Chrome prompt. | 🔒 |
| 13 | S01 | Subtitle size: Jamie's version was ~40pt. Corrected to 52pt SemiBold Italic Ink. | Corrected and committed via connector. | ✓ V7 uses 52pt here because the subtitle sits under a 110pt title — 40pt reads too weak at that contrast ratio. | Build spec subtitle note: cover subtitle is 52pt exception (not 40pt Subtitle row). | 🔒 |
| 14 | S02 | Hero stat width: x108 → x684 (2/3 column). Starts at top content margin. | Applied by Jamie in Canva. | ✓ Gives the stat visual dominance over left two-thirds without bleeding to full width. | Add 2/3-column stat width rule to build spec S02 entry. | 🔒 |
| 15 | S02 | Support lines: Hook typography (68pt SemiBold), width x108 → x756 (3/4 column). | Applied by Jamie. Overrides V7's 52pt support line. | ~ Partial. 68pt is bolder than V7 and may compete with the 200pt stat. Worth reviewing in context of the full 12-slide set. Flag if it reads heavy. | Build spec S02: note 68pt as Jamie's decision pending full-set review. Guidelines type table unaffected (Hook row already 68pt). | ⏳ |
| 16 | S02 | SWIPE tile centred in x756→x972 band, same vertical band as support text. | Applied by Jamie. | ✓ Consistent with the SWIPE column rule established on S01. | No change needed beyond what's in the SWIPE rule (decision #7). | 🔒 |
| 17 | S03 | Oversized quote marks: " " to appear exaggerated relative to 68pt body text, same font size. | Requires modified font file (JN-Quote-Display) with quote mark glyphs scaled up. Interim: standard JN-Quote. | ✓ Strong typographic treatment. Fraunces's quote marks have good character at large scale. | Generate JN-Quote-Display TTF with scaled quote glyphs. Add to Brand Kit. Update build spec S03. Update guidelines S03 card. | 🚧 |
| 18 | S04 | Icons same size as SWIPE tile. Icon + text grouped. Groups distributed evenly between heading and wordmark. | Applied by Jamie. | ✓ Grouping icon+text before distributing is the right approach — keeps the pairs locked together. | Build spec S04: icons = SWIPE tile size (≈144px). Confirm exact size and lock. Chrome prompt: group icon+text before distributing. | ⏳ |
| 19 | S04 | Icon left edge at x108 (left margin). Jamie likes this indent amount. | Applied by Jamie. | ✓ Aligns icons to the content margin, not the column indent. Clean and consistent with other slides. | Lock x108 as icon left edge in build spec S04. | 🔒 |
| 20 | S05 | X-axis labels and data callouts both Inter Bold. No weight mixing between the two. | Applied by Jamie. Overrides V7 which used Inter 700 for labels and Fraunces for values. | ✓ Cleaner and more consistent. Keeps the chart zone in one typeface. | Build spec S05: both axis labels and value callouts = Inter JN Bold. Update carousel-v7.py if renderer is ever re-run. | 🔒 |
| 21 | S05 | Chart centred, width spans to first indent (matching icon indent from S04). | Applied by Jamie. | ✓ Consistent horizontal rhythm with S04. Good instinct. | Build spec S05: chart width = x108 → x972 with inner padding, or confirm exact px after Jamie finalises. | ⏳ |
| 22 | S05 | Source text: top edge meets bottom edge of chart directly. | Applied by Jamie. | ✓ Tight stacking consistent with decision #4. | Build spec S05: source y = chart bottom (no gap). | 🔒 |
| 23 | S05 | Takeaway text: Subtitle typography (Fraunces JN Light Italic, 40pt, Ink). | Applied by Jamie. Matches the Subtitle row in the type scale. | ✓ Good. The takeaway is a quieter editorial comment, not a heading — Subtitle weight is right. | Build spec S05: takeaway = JN-Subtitle, 40pt, Ink. | 🔒 |
| 24 | S05 | All sections distributed evenly between hook heading and footer. | Applied by Jamie. Consistent with global rule #3. | ✓ | No additional change beyond global rule #3. | 🔒 |
| 25 | S06–S12 | Slides in progress — decisions not yet logged. | — | — | Update this log as Jamie gives commentary. | 🔄 |
| 26 | S06 | All text in the 2×2 matrix uses line spacing 1.2. | Applied by Jamie in Canva. | ✓ 1.2 is the right multiplier for label text inside tight quadrant boxes. | Add line-height 1.2 to build spec S06 for all matrix text elements. Note in Chrome prompt. | 🔒 |
| 27 | S06 | Axis arrows (SPEND →, RETURN →) in Ink Blue #0476D0. | Applied by Jamie. | ✓ Ink Blue on the axes is correct — they are navigational labels, same register as kickers. | Build spec S06: axis labels Ink Blue confirmed. Update carousel-v7.py axis colour note. | 🔒 |
| 28 | S06 | Quadrant box positions corrected to properly represent the 2×2 (low/high spend vs low/high impact). Labels clarified to show all four combinations. | Applied by Jamie — corrects V7 renderer's quadrant labelling and positioning. | ✓ The V7 renderer had "return" not "impact" on the Y-axis. Worth confirming the four quadrant labels so the build spec has the correct copy. | Update build spec S06 quadrant copy to match Jamie's final labels. Flag to re-check V7 reference copy. | ⏳ |
| 29 | S06 | Box labels: 34pt Fraunces. | Applied by Jamie. | ~ Partial. 34pt is the Body size but in Inter in the spec — using Fraunces at 34pt gives display character but departs from the type scale logic. Worth checking it doesn't feel heavy in the small boxes. | Update build spec S06: quadrant labels = Fraunces JN 34pt. Note as S06-specific exception to the Body=Inter rule. | ⏳ |
| 30 | S07 | Body text size reduced to 24pt (from spec's 30pt). | Applied by Jamie in Canva. | ✓ Makes sense — S07 has 6 items in a 2×3 grid with icon tiles. 30pt would be cramped; 24pt gives the labels room. | Update build spec S07: body text = 24pt (S07-specific exception to Body 34pt rule). Update Chrome prompt. | 🔒 |
| 31 | S07 | Line spacing 1.2 for body text in the grid. | Applied by Jamie. | ✓ Consistent with S06 matrix decision (#26). 1.2 becoming the standard for dense/grid layouts. | Add to build spec as grid layout rule: line-height 1.2 for any 2-column grid or matrix slide (S06, S07). | 🔒 |
| 32 | S07 | Icon tiles reduced to 120×120px (from SWIPE tile size). | Applied by Jamie. Overrides decision #18 which assumed icon size = SWIPE tile (≈144px). | ✓ 120px is better for a 2×3 grid — 144px would crowd 6 tiles. Also closes open item D. | Build spec S07: icon tiles = 120×120px. Close open item D. Update Chrome prompt. | 🔒 |
| 33 | S07 | Text aligned to top of icon tile, not vertically centred. | Applied by Jamie. | ✓ Top-alignment is right for multi-line labels beside a tile. Keeps baselines predictable across all 6 items. | Build spec S07: text top-aligned to icon tile top edge. Note as exception to vertical-centre rule used on S04. | 🔒 |
| 34 | S07 | 2×3 grid distributed evenly between hook heading and footer wordmark. | Applied by Jamie. Consistent with global rule #3. | ✓ | No additional change beyond global rule #3. | 🔒 |
| 35 | S07 | 2×3 grid spans full content width: x108 → x972 (864px total). Tiles and text fill full width within margins. | Applied by Jamie. | ✓ Right call — full width gives each column 432px, plenty for a 120px tile + 24pt text. | Build spec S07: grid width = full content width x108→x972. Each column = 432px. | 🔒 |
| 36 | S08 | Canva's funnel diagram requires labelling the *boundaries* between sections (4 labels for 3 segments) rather than labelling inside each segment as V7 did. | Applied by Jamie — fundamental structural difference from V7 renderer approach. | ✓ Correct for Canva's native funnel element. The boundary-label model is also arguably clearer — each label marks a drop-off point. | Build spec S08: rewrite funnel instructions to boundary labels. Note V7 renderer approach incompatible with Canva's funnel element. | 🔒 |
| 37 | S08 | Funnel formatting not satisfactory — Jamie may deprioritise funnel diagrams as a slide type. | No change yet — flagged for review. | ~ Partial. Funnel is a strong data type for showing drop-off. Worth attempting a manual trapezoid build rather than Canva's inflexible native element. If it doesn't read well, deprioritising is reasonable. | Flag for post-build review: attempt trapezoid funnel manually if time allows. If deprioritised, remove S08 from template set. | ⏳ |
| 38 | S08 | Chart labels use Inter Bold — consistent with S05 bar chart decision (#20). | Confirmed by Jamie. | ✓ Locks Inter Bold as the standard for all data labels across chart slides. | Build spec: Inter Bold = standard for all chart/data labels (S05, S08, future chart slides). | 🔒 |

---

## Open items (work queued for Claude)

| # | Item | Triggered by | Priority |
|---|---|---|---|
| A | Generate JN-Hook-Black (Fraunces 900, display axis) | Decision #10 | High — needed before templates published |
| B | Generate JN-Quote-Display (oversized quote mark glyphs) | Decision #17 | Medium — S03 functional without it |
| C | Confirm S02 support line size (68pt vs 52pt) after full-set review | Decision #15 | Low — Jamie's call |
| D | ~~Confirm S04 icon size exact px~~ — CLOSED: S04 icons = SWIPE tile size (≈144px), S07 icons = 120×120px | Decision #18, #32 | ✓ Done |
| E | Confirm S05 chart exact width px | Decision #21 | Medium — needed for build spec |
| F | Build 8 new icon glyphs | Decision #11 | Medium — before Brand Template publish |
| G | Update canva-build-spec-v7.md with all locked decisions from this log | Decisions #1–24 | High — do after S12 complete |
| H | Update brand-guidelines: full stops rule, stale Brand Kit copy, type table if Hook-Black adopted | Decisions #5, #10 | After template build complete |
| I | Re-render carousel-v7.py if any spec changes adopted (Hook-Black, chart font) | Decisions #10, #20 | After template build complete |

---

## Connector design audit (read 17 Jun 2026 — S01–S09 populated)

Full element inventory read via Canva connector. Key observations.

**What's confirmed correct across all slides:**
- All 12 pages 1080×1350, fixed (non-responsive). ✓
- Background image `MAHMaEd2KL4` (V3 cool composite) placed at 0,0 full-bleed on all 12 pages. ✓
- Footer wordmark `MAHMZ8lpJ1Y` on S01–S07: top y1205, left x270, w538, h95. ✓
- Kicker "NEWS & INSIGHTS" at x108, y108 on all built slides. ✓
- All hook headings start at y147, x108, width 864. ✓
- S04 icon tiles: 148.5×148.5px. Note: slightly larger than the 144px SWIPE tile.
- S07 icon tiles: 120×120px. ✓ Matches decision #32.
- S06 matrix: 4 shape elements 324×324px in 2×2. Axis labels and arrow elements present. ✓

**Issues spotted:**
- **S01 subtitle box**: left x111.87 (not x108). 3px drift. Flag for connector correction.
- **S04 icon tiles**: 148.5px not 144px. Confirm with Jamie.
- **S09 (page 9)**: only one fill element (image placeholder), no text elements yet. Check usage.
- **S10–S12**: S10/S11 background only, no content. S12 has leftover placeholder text — delete before templating.
- **S03 quote text**: quote marks and body in the same box — makes the oversized-mark font modification harder. Flag when S03 finalised.

---

## Colour rules — Slate vs Charcoal (locked from V7 renderer analysis)

**The core distinction:**
- **SLATE `#334155`** — all display/editorial text. Anything at hook size (68pt) or above, plus supporting text on display-only slides. The default for most of the deck.
- **CHARCOAL `#1E293B`** — body text only, in structured lists and grids, beside icon tiles, at 34pt or below.
- **INK `#0476D0`** — kickers (every slide), italic accent words, subtitles, chart takeaway lines, axis labels, CTA directive lines, SWIPE label. Anything navigational or emphatic.

**Which slides use which body colour:**

| Slide | Type | Hook heading | Body/list text | Italic accents |
|---|---|---|---|---|
| S01 | Display | SLATE | SLATE | INK |
| S02 | Display | SLATE | SLATE | INK |
| S03 | Display | SLATE | SLATE | INK |
| S04 | List | SLATE | **CHARCOAL** | INK |
| S05 | Display | SLATE | SLATE | INK |
| S06 | Display | SLATE | SLATE | INK |
| S07 | List | SLATE | **CHARCOAL** | INK |
| S08 | Display | SLATE | SLATE | INK |
| S09 | List | SLATE | **CHARCOAL** (body) + Ink/Pink/Lilac/DarkBlue (numerals) | INK |
| S10/b/c | Display | SLATE | SLATE | INK |

**Simple rule for building:** If text sits beside an icon tile or in a structured list at body size → Charcoal. Everything else → Slate. When in doubt → Slate.

| 39 | All | Kicker carries the content pillar/series name ("NEWS & INSIGHTS") not a per-slide topic. Same on every slide of one carousel. | Applied by Jamie from S01. | ✓ The kicker is brand-level navigation, not editorial metadata. Readers orient by pillar. | Hook headings now carry 100% of slide-level orientation — ensure all are specific statements. Note in guidelines. | 🔒 |
| 40 | All | Colour rule: SLATE display/editorial, CHARCOAL body in lists/grids beside icons, INK kickers/accents. Verified against V7 renderer. | Locked as the system rule. | ✓ | Update guidelines typography section with the Slate/Charcoal/Ink logic. Add to Chrome prompt. | 🔒 |
| 41 | S04, S07, S09 | Body text beside icon tiles = CHARCOAL not SLATE. Connector can't read colours — Jamie to verify in Canva. | Needs Jamie's visual check. | ✓ | If wrong: correct in Canva, then lock in Brand Template text boxes. | ⏳ |
| 42 | S09 | Numbers indented to match S04 icon left edge (x153.5). Numbers ≈110pt (CTA size). Text vertically centred against the number. Numbers+text grouped per item, distributed evenly. | Applied by Jamie. | ✓ Strong — large numerals at CTA size give the list visual weight; matching indent ties S09 to S04. | Build spec S09: numerals = CTA headline size (~110pt), indent x153.5. Confirm line spacing. | 🔒 |
| 43 | S10 | "Follow Jamie Newberry" pill + suffix saved as a Canva COMPONENT, not text/typography elements. | Applied by Jamie. | ~ Partial. Reusable and locks formatting — but a component can't be autofilled or edited via connector. Fine for the CTA (text never changes). | Note in build spec: S10 CTA pill is a locked component, intentionally non-variable. Confirm before templating. | ⏳ |
| 44 | S10/b/c | Footer wordmark made BIGGER on CTA slides than content slides. S10 footer w644 h114 (vs w538 h95). | Applied by Jamie. | ~ Partial. A larger wordmark on the closing slide makes sense as a sign-off, but breaks footer consistency. Decide: deliberate exception or normalise. | Decide CTA footer size as exception or normalise. Update build spec footer rule. | ⏳ |

---

## End-of-session full audit (17 Jun 2026 — S01–S10 populated, S11–S12 outstanding)

**Build status by slide:** S01 Cover ✓ (corrected + committed); S02 Big Stat ✓; S03 Pull Quote ✓ (marks + body combined); S04 Process Flow ✓ (icons 148.5px); S05 Bar Chart ✓; S06 2×2 Matrix ✓; S07 Icon Grid ✓ (icons 120px); S08 Funnel ✓ (flagged unsatisfactory); S09 Numbered List ✓; S10 CTA Follow ✓ (pill component, bigger footer); **S11 — EMPTY except background (CTA Comment slot, outstanding); S12 — leftover placeholder text + stray title (CTA Save slot, needs clearing).**

**New concerns spotted:**
1. **S09 item 4 copy error**: "agreed **for** the budget is spent" should be "agreed **before** the budget is spent."
2. **S03 quote copy**: missing full stop — "never the code it was knowing what" should be "never the code. It was knowing what".
3. **S05 hook heading**: "Even Before AI." title case on "Before"; others sentence case. Inconsistent.
4. **S05 takeaway**: leading space before "And that's software…" — trim.
5. **S12 stray content**: placeholder kicker/source text still present. Must clear.
6. **S04 icons 148.5px vs S07 icons 120px**: confirm both intended.
7. **S04 process flow**: no visible connector lines (V7 had vertical connectors). Confirm.
8. **Footer inconsistency**: content w538/h95, S10 CTA w644/h114. (Decision #44.)
9. **S06 matrix**: quadrant top labels and spend/return positions need a sense-check.
10. **S03 / S09 numeral colours**: connector can't read colour. S09 numerals should cycle Ink→Pink→Lilac→DarkBlue. Verify.

---

## Session 3 update (19 Jun 2026 — all 12 slides built)

**Jamie's answers to the 10 priority questions:**
| Q | Answer | Status |
|---|---|---|
| 1,2,8 | Copy errors fixed (S09 "before", S03 full stop, S05 sentence case). Verified. | 🔒 |
| 3 | Pink pill = locked component. | 🔒 |
| 4 | CTA footer bigger — made even larger (w714/h126 vs content w538/h95). | 🔒 |
| 5 | Icons always 148.5px. Exception: 2×3 grid slides use 120px. | 🔒 |
| 6 | Connecting lines added (S04). Keep. Line matches colour of icon above it. | 🔒 |
| 7 | Matrix logic — Jamie thinks it's right. See colour-semantics concern below. | ⏳ |
| 9 | Keep quote marks combined for now. Will update font to oversized marks at every size. | 🚧 |
| 10 | S11 (Comment) + S12 (Save) CTAs built. All pink CTA pills = components. | 🔒 |

**New decisions:**
| 45 | S04 | Connecting lines between process icons, colour-matched to the icon above. | Applied. | ✓ Ties each segment to its origin. | Build spec S04: add colour-matched connector lines. | 🔒 |
| 46 | S11 | CTA Comment. Hook-style question. "Comment Below" pill (component). Two icons. Kicker still "NEWS & INSIGHTS". | Applied. | ~ CTA kicker is the open strategic question below. | Resolve CTA kicker strategy. | ⏳ |
| 47 | S12 | CTA Save. "Save this for your next AI pitch." "Save & Send" pill (component). Two icons. | Applied. | ✓ Good. | — | 🔒 |
| 48 | All | Glyph SVG colour change in Canva is painful — Jamie had to edit brightness to force white. | Workflow friction noted. | The cairosvg/recolour problem. Better fix: pre-render every glyph in its required colour as separate PNG assets. | Icon build: export each needed glyph in white + charcoal + ink variants as flat PNGs. | 🚧 |

**Icon build queue (expanded):** LinkedIn-action set (write comment, repost, send, save, follow, link, download, vote, template); content set (new, prediction, ask question, need help); plus earlier list (tired, suited man, shush, demo, delay/time, calendar, no substance, puppet). All exported in white/charcoal/ink flat PNG variants.

**Matrix colour-semantics concern (Q7):** Currently top row (high return) = pink, bottom row = blue. Pink is the brand's emphasis/warning colour (reserved for the bad data point, <5% usage); here it marks the GOOD quadrants. Also pink-on-pink and blue-on-blue are the lowest-contrast elements. Options: (A) flip — the trap quadrant gets pink as warning; (B) drop the two-colour split, one neutral tint, labels carry meaning (cleanest); (C) keep as-is, accept pink is decorative (contradicts guidelines). Recommend B or A.

---

## Kicker strategy — LOCKED: Option B

Cover gets a larger pillar kicker (28-30pt). Every inner slide gets a smaller (24pt) slide-type kicker naming its function. CTAs get action kickers. Inner kickers are per-post writable template fields; the pillar kicker on the cover is the constant.

| Slide | Kicker | Notes |
|---|---|---|
| S01 Cover | **NEWS & INSIGHTS** | Pillar name. Larger (28-30pt). The constant brand label. |
| S02 Big Stat | **THE NUMBER** | |
| S03 Pull Quote | **THE INSIGHT** | |
| S04 Process Flow | **THE PATTERN** | (or "HOW IT GOES") |
| S05 Bar Chart | **THE ODDS** | |
| S06 Matrix | **THE TRADE-OFF** | (spend vs return framing) |
| S07 Icon Grid | **THE BLOCKERS** | |
| S08 Funnel | **THE DROP-OFF** | |
| S09 Numbered List | **WHAT WORKS** | |
| S10 CTA Follow | **FOLLOW** | |
| S11 CTA Comment | **YOUR TURN** | |
| S12 CTA Save | **KEEP THIS** | |

These are defaults for THIS carousel. On future carousels the inner kickers are rewritten to suit the content; the cover pillar kicker stays fixed per pillar.

| 49 | All | Kicker strategy = Option B. Cover pillar kicker larger (28-30pt), inner slide-type kickers 24pt, per-post writable. | Locked. | ✓ Keeps hook headings short by moving the "what is this slide" job to the kicker. | Build spec: cover kicker 28-30pt pillar constant; inner kickers 24pt writable. Update Chrome prompt + guidelines. | 🔒 |
| 50 | All | Claude Design icon brief created: 21 new glyphs + pre-coloured PNG exports (white/charcoal/ink) + composite tiles. JPEG rejected (no transparency). | Brief written. | ✓ Pre-colouring is the correct fix. Contact-sheet review built in before full export. | Hand brief to Claude Design. On return: load PNGs to Brand Kit, update icon guidance. | 🚧 |

---

## Session 4 (20 Jun 2026)

**Jamie's answers, priorities round 2:**
| Q | Answer | Status |
|---|---|---|
| 1 | Matrix colours = pink & ink blue at 80% transparency (20% opacity tints). Kept the split. | 🔒 |
| 2 | S11 copy now "What's the most costly pilot you've seen fail?" | 🔒 |
| 3 | All kickers updated to the agreed slide-type labels. | 🔒 |
| 4 | Fixed. | 🔒 |
| 5 | Footer large on covers (S01,02,03) AND CTAs (S10,11,12). Content slides keep smaller footer. | 🔒 |
| 6 | Icons being updated via Claude Design. | 🚧 |
| 7 | Oversized quote-mark font built (JN Quote BigMarks). | ✓ delivered |
| 8 | Happy with darker numbering colours (S09). | 🔒 |
| 9 | Matrix labels don't collide. | 🔒 |
| 10 | 12 slides only, clean. | 🔒 |

| 51 | S06 | Matrix quadrant tints = pink and ink-blue at 20% opacity. Top row pink, bottom row blue. | Applied. | ~ Still flags the pink-semantics point, but at 20% opacity the tint is decorative and soft; contrast concern reduced. Accepted. | Note in guidelines: matrix is the one place pink is used as a neutral zone tint at 20% opacity. Documents the exception. | 🔒 |
| 52 | footer | Footer large on covers + CTAs (S01,02,03,10,11,12); compact on content slides (04-09). | Applied. | ✓ Coherent: "statement" slides get the large sign-off; working/data slides get the compact footer. | Build spec: two footer sizes — large (statement) vs compact (content). Document which is which. | 🔒 |
| 53 | S03 | Oversized quote-mark font: JN Quote BigMarks (Fraunces 600 Italic, curly quote glyphs scaled 1.85x, opening marks hang left as hanging punctuation). Scales correctly at every size. | Delivered. | ✓ Hanging punctuation is the correct treatment — opening mark overhangs the margin, body stays aligned. | Jamie uploads JN-Quote-BigMarks.ttf to Brand Kit. Use for S03. Update guidelines S03. | 🚧 |

---

## Session 5 (21 Jun 2026) — Final export review before lock-down

**Icons:** 27 new glyphs delivered via Claude Design. Style match excellent — new glyphs indistinguishable from existing set. White-on-tile composites correct. Bonus glyphs beyond the brief: present, chess, speech, board-meeting, graduate, learn, loud-speaker. READY to load to Brand Kit.

**Final slide export review (from Jamie's 12 PNGs) — issues to fix before lock:**
1. **S04 icon mismatch**: some glyph choices slightly off the meaning (neutral face for "a board mandate", send/arrow for "rolled into next year's budget"). Now the new glyphs exist (calendar, suited-man, board-meeting) these can be improved. Optional but worth it.
2. **S08 funnel copy**: four tiers (Submitted 100, Evaluated 60, Pilot 20, Production 5) — confirm the figures are defensible (MIT NANDA gives the 5%). Funnel is Canva's native element; colours don't follow brand order.
3. **"THE TRADE OFF" / "THE DROP OFF"**: hyphenation question (later resolved — see below).
4. **S09 numeral colours**: cycle Ink→Pink→Lilac→DarkBlue matches spec. ✓
5. **S05 chart**: pink on "Challenged" (middle value), lilac on "Fail". Per brand rule pink = the point you want read first; might be better on Fail. Minor — Jamie's call.
6. **S10 footer**: verify the larger CTA footer actually applied on S10 (S11/S12 look larger).

**Non-issues (confirmed good):** kickers correct and consistent; hooks sentence case; full stops present; quote marks combined fine for now; matrix tint at 20% reads soft and clean; margins, footer, SWIPE tiles, distribution all consistent. The pack looks professional and on-brand.

**Jamie's instruction:** lock the template, update with all discussed changes, create FINAL v4 guidelines for the initial posting/testing phase.

---

## LOCK-DOWN (21 Jun 2026) — v4.0 issued for posting/testing phase

**Status: the News & Insights carousel is locked as the working template.** All 12 slides built, reviewed, and consistent. v4.0 guidelines issued (supersedes v3.5). This is the version that goes into use for the initial posting and testing phase.

**v4.0 guidelines changes from v3.5:**
- Kicker strategy documented: cover = pillar name (28-30pt), inner slides = slide-type label (24pt), per-post writable.
- Colour rule documented: Slate (display/editorial) / Charcoal (list body beside icons) / Ink (kickers, accents, subtitles, axis, CTA directives).
- Margin updated to x108 (width 864) throughout, replacing x93.
- Two footer sizes: large (~126px) on statement slides, compact (~95px) on data slides.
- Icon system: 51 original + 27 new glyphs; pre-coloured PNG export workflow noted.
- Type scale: eight pre-tracked fonts in the Brand Kit (letter-spacing baked in).
- Locked + Next lists rewritten for the posting phase.

**To do in Canva to complete the lock (UI actions):**
1. Publish "JN Carousel Master v7" as a Canva Brand Template (the milestone — converts the master into an autofill-ready, reusable template; locks colour, line-height, spacing into the text boxes).
2. Load the 27 new icons (pre-coloured PNGs + composite tiles) into the Brand Kit.
3. Minor fixes (can be done in template): swap the two off-meaning S04 glyphs now better ones exist; confirm S08 funnel figures sourced; verify S10 footer is the large size.

**Then: post the first carousel and begin testing the system.**

**Deferred to later phases:** oversized quote-mark font (parked); stacked wordmark PNGs; profile banner/featured rebuild; the other three pillar background variants; performance feedback loop.

---

## Icon update verified (21 Jun 2026)

Visual review of S04, S07, S10b, S10c confirms new icons applied and reading well. S10c Save (bookmark + paper-plane), S11 Comment (bubble+pencil + down arrow), S07 Blockers (neutral-face, people, question, suited-man, AI sparkle, person-reading) all read clearly. S04 Process (board-meeting → neutral-face → snail → £): three good; the neutral face on "a flashy pilot everyone loves" undersells the line. Optional swap. Flagged, Jamie's call.

**Hyphens**: Jamie's decision — kicker labels stay WITHOUT hyphens (THE TRADE OFF, THE DROP OFF). Removed the hyphenation instruction from the v4 Next list.

**v4.0 guidelines re-issued** with: icons marked loaded+applied, hyphen instruction removed, S04 demo-glyph note added. 20 pages, fonts verified.

| 54 | S03 | Oversized quote-mark font (JN-Quote-BigMarks) — CLOSED. The apostrophe fix worked technically but the visual effect in Canva didn't land. Standard JN-Quote retained for S03. Quote marks normal size. | Closed. | ✓ Right call — the slide reads clearly without the treatment. | Remove JN-Quote-BigMarks from the Brand Kit to avoid confusion. | 🔒 |

---

## v4.0 guidelines QA + slide refresh (21 Jun 2026)

Comprehensive QA pass on the v4.0 guidelines. Stale info corrected (x93→x108 in 3 places; "Ink or Lilac"→"Ink" in 2 places; footer row updated to two sizes; S04/S05/S09 card specs corrected to the live values). All 12 template-card thumbnails regenerated from the latest Canva exports. Verified clean: version consistent (v4.0, supersedes v3.5); all v4 measurements present; no stale terms. 20 pages, fonts embedded.

---

## v4.0 detailed QA + image fixes (21 Jun 2026, session close)

Two reported issues fixed — same root cause: unsubstituted `DATA_URI` placeholders. (1) Cover background added (raw V3 cool fractal + frosted panel; white meta now legible; reads v4.0 · Supersedes v3.5). (2) Page 12 "real cover demo" fixed (swap regex now targets the placeholder; shows the real S01 Canva export). Every one of the 20 pages rendered to image and inspected — all correct. Final automated sweep all clear: zero DATA_URI, zero broken images, zero stale terms. 20 pages, A4, fonts embedded.

---

## v4.0 final polish (21 Jun 2026)

Four changes, all verified: (1) cover now full-bleed (fractal fills edge to edge, frosted panel centred, meta inset at corners); (2) page 11 pink "Pending files" box removed; (3) page 20 Next bullets normalised from pink to standard Ink; (4) "Icons loaded and applied" Next bullet removed. Page 8 figures confirmed correct. 20 pages, fonts embedded, no regressions. **v4.0 is final for the posting/testing phase.**

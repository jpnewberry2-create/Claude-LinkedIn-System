# CLAUDE.md — Operating instructions for Claude Code and Cowork

This file is read automatically by Claude Code when you open a session in this repo directory. It defines the two recurring tasks: the initial bulk upload (Claude Code) and ongoing maintenance updates (Cowork).

---

## What this repo is

The durable source of truth for the Jamie Newberry LinkedIn personal brand system. Any Claude session — chat, Code, Design, or Cowork — should fetch the current guideline and specs from here at session start rather than relying on chat history.

Three-part system:
- **Notion** — project management (tasks, decisions, session log)
- **GitHub (this repo)** — working files that change: guideline, assets, specs, skills
- **Canva** — downstream only; Brand Kit `kAHLoHtCCJc`, Carousel Master `DAHMZ37HNnU`

Full context: read `README.md` first, then fetch the current guideline from `guidelines/brand-guidelines-v4.0.html`.

---

## Commit conventions

All commits follow: `<type>: <imperative summary>`

Types: `guideline` / `assets` / `docs` / `structure` / `fix` / `design-system`

Examples:
- `assets: add V4 warm-pink fractal background`
- `guideline: update to v4.1`
- `docs: update canva-build-log decisions 55-58`

After every commit: read back the file at HEAD and verify size matches the source. Do not trust the commit response alone.

---

## Folder map — where each file type lives

```
guidelines/
    brand-guidelines-v{version}.html    The canonical guideline (HTML, may contain base64)
    brand-guidelines-v{version}.pdf     Locked PDF render of the canonical guideline
    project-os-v2.html                  System blueprint
    CHANGELOG.md                        Human-readable revision history
    README.md                           Folder overview

assets/
    squircle-36-shape.svg               The definitive locked squircle vector
    brand-assets.html                   Brand assets overview
    backgrounds/                        Baked slide backgrounds (PNG, 1080x1350)
        fractalbgV1warm1080x1350.png
        fractalbgV2pink1080x1350.png
        fractalbgV3cool1080x1350.png
        fractalbgV4warmpink1080x1350.png
        compositeV1warm1080x1350.png
        compositeV2pink1080x1350.png
        compositeV3cool1080x1350.png
        compositeV4warmpink1080x1350.png
        frostedpaneltransparent1080x1350.png
    fonts/                              JN-named TTF files
        FrauncesJN-Display.ttf
        FrauncesJN-DisplayItalic.ttf
        FrauncesJN-Italic.ttf
        FrauncesJN-LightItalic.ttf
        InterJN-Bold.ttf
        InterJN-ExtraBold.ttf
        InterJN-Regular.ttf
        (JN-Quote-BigMarks not uploaded — "Not Working" variant retired, decision #54)
    icons/
        icons-sprite.svg                Master SVG sprite of all glyphs
        icon-sprite-reference.html      Visual reference for all glyphs
        icons-sprite-reference.md       Glyph reference (markdown)
        icon-glyphs/                    Source SVG glyphs (78)
        icon-backgrounds/               Background tile SVGs (9)
        icons-chart-blue/               Glyphs coloured chart-blue (78)
        icons-chart-lilac/              Glyphs coloured chart-lilac (78)
        icons-orange/                   Glyphs coloured orange (78)
        icons-pink/                     Glyphs coloured pink (78)
        icons-teal/                     Glyphs coloured teal (78)
        pre-coloured-glyphs/            Pre-coloured PNG exports
            png-charcoal/               Pre-coloured PNGs on charcoal (78)
            png-ink-blue/               Pre-coloured PNGs on ink blue (78)
            png-lilac/                  Pre-coloured PNGs on lilac (78)
            png-pink/                   Pre-coloured PNGs on pink (78)
            png-white/                  Pre-coloured PNGs on white (78)
    images/
        wordmark01ondark.png
        wordmark01onlight.png
        wordmark02ondark.png
        wordmark02onlight.png
        wordmark03ondark.png
        wordmark03onlight.png
        photo-fullbody.png
        profile-radial.png
        profile-light.png
        profile-dark.png
        LinkedIn-Logo-White.png

design-system/                          Tokens, type scale, primitives (Phase 2)
specs/                                  Markdown specs, research files, real_glyphs.py
skills/                                 Skill files for Claude Code and Cowork
    v1-github-structuring-documenting-updating/SKILL.md
    v1-notion-sandbox-project-management/SKILL.md
templates/                              References to Canva brand templates
```

---

## Task A — Bulk binary upload (Claude Code, one-off)

Run this once to populate the binary assets the chat connector cannot commit.

**Pre-flight:**
1. Read this file.
2. Read `skills/v1-github-structuring-documenting-updating/SKILL.md`.
3. Confirm the local source folder path with Jamie before touching anything.
4. `git status` — confirm you are on `main` and the working tree is clean.

**Execution:**
1. Copy each file from its local source path to the correct repo folder per the map above.
2. `git add` the files.
3. Commit with the format: `assets: bulk upload brand assets v4.0`
4. `git push origin main`
5. Read back every committed file path from GitHub via the API and confirm file sizes match the source. Report any mismatches before closing.

**Post-upload:**
- Update `guidelines/CHANGELOG.md` with a note that binary assets were uploaded.
- Do not update the Notion File Register yet — that is Phase 3, handled from the chat connector once raw URLs are confirmed.

**Files NOT to commit:**
- `JN-Quote-BigMarks.ttf` — parked (decision #54 in canva-build-log). Skip unless Jamie explicitly says otherwise.
- Any file with `_OLD`, `_DRAFT`, or `WIP` in the name.

---

## Task B — Ongoing maintenance updates (Cowork, little-and-often)

For future updates after the bulk upload is complete.

**Trigger:** Jamie has updated one or more files in the brand system and wants the repo synced.

**Pattern:**
1. Read this file and the relevant skill file.
2. Identify which files have changed (ask Jamie if not obvious).
3. For text files (markdown, HTML without large base64 payload): commit via the GitHub API connector.
4. For binary files (PNG, TTF, SVG, HTML with base64): use the GitHub web UI or git push via terminal.
5. Commit each logical change separately with a descriptive message.
6. After committing: if the file is in the `guidelines/` folder, update `CHANGELOG.md` with the version and what changed.
7. If the update adds or changes a file that is referenced in the Notion File Register: flag it for a Notion update in the same session.

**Cross-tool update sequence (when a guideline version bumps):**
1. Commit updated HTML to `guidelines/`
2. Update `CHANGELOG.md`
3. Read back the raw URL: `https://raw.githubusercontent.com/jpnewberry2-create/Claude-LinkedIn-System/main/guidelines/<filename>`
4. Update the Notion File Register row for that file with the new raw URL
5. If font or icon files changed: flag for manual Canva Brand Kit update (UI only — cannot automate)

---

## Key IDs and references

- **Repo:** `jpnewberry2-create/Claude-LinkedIn-System` (public)
- **Branch:** `main`
- **Raw URL base:** `https://raw.githubusercontent.com/jpnewberry2-create/Claude-LinkedIn-System/main/`
- **Canva Brand Kit:** `kAHLoHtCCJc`
- **Canva Carousel Master v7:** `DAHMZ37HNnU`
- **Notion LinkedIn Command Centre:** `321c96325fbb8056b4cece5156527a20`
- **Notion Build Progress Tracker:** `5caa304db0ab4c6ba09eb56fa875274e`

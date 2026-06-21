# Claude LinkedIn System

The working-files home for the **LinkedIn Personal Brand** project. This repository is the durable, fetchable source of truth for the brand guideline and assets, so any chat can pull the current version at session start instead of relying on chat history.

It is one node in a three-part system:

| System | Role | Holds |
| --- | --- | --- |
| **Notion** | Project manager (the record) | Tasks, decisions, session log, ideas, the project page. Lives inside the Career area of Jamie's Life OS. |
| **GitHub** (this repo) | Maintainer (live files) | Working files that change: the guideline, brand assets, the design system, skill files. |
| **Canva** | Final editor (downstream) | Palette, type and logo (brand kit `kAHLoHtCCJc`); carousel templates. Consumes a slice of the guideline; never canonical. |

## Repository structure

```
README.md                  This file: what the repo is, where the current guideline lives.
/guidelines/               The canonical brand guideline (current version) + CHANGELOG.md.
/assets/
    /backgrounds/          Baked slide backgrounds, mapped to content pillars.
    /icons/                The consolidated icon sprite and source glyphs.
    /images/               Photography and raster assets.
/design-system/            Tokens, type scale, squircle/panel primitives. Derived by Claude Design.
/templates/                References to the Canva brand templates.
/skills/                   v1 sandbox-stage skill files governing safe execution.
```

## How to find the current guideline

The current guideline file lives in `/guidelines/` with its version in the filename. Its raw URL is the source of truth. Fetch that at the start of any session that needs the brand spec.

## Conventions

- File and folder names: lowercase, hyphens, max three levels deep. Words spelled out use "and", not "&".
- The guideline filename carries its version (e.g. `brand-guidelines-v4.0.html`).
- Every commit uses a structured message: `<type>: <imperative summary>`, where type is one of `guideline`, `assets`, `docs`, `structure`, `fix`, `design-system`.
- The reasoning-level changelog lives in two places: `CHANGELOG.md` here (what changed, when) and a Notion Decisions Log row (what changed and why).

## The agent / record distinction

Only humans and Claude act. This repo is a record: it holds state, it does not initiate it. Commits are made by Jamie, by Claude Code, or by Claude via the GitHub connector. The repo is acted upon; it does not act.

Built and maintained with Claude.

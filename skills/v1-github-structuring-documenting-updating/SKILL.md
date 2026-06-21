---
name: v1-github-structuring-documenting-updating
description: Commit and document the brand guideline and assets to the Claude-LinkedIn-System repo with consistent structure, naming, commit messages, and matching Notion records. Use whenever committing, restructuring, or updating brand files in this repo. v1 test instrument; defers to life_os_governance.md.
---

# v1 GitHub Structuring, Documenting and Updating Skill

A test-stage skill governing how brand files are committed and documented in the `Claude-LinkedIn-System` repo. v1: expected to change as the workflow proves out. Defers to `life_os_governance.md` where they conflict.

## When this fires

Any time files are committed, restructured, renamed, or updated in this repo: the bulk asset upload, a single guideline bump, a new spec file, an icon set update, a folder reorganisation.

## Scope and safety

- This skill acts only on the `jpnewberry2-create/Claude-LinkedIn-System` repo. It does not touch other repos.
- It commits and documents. It does not delete history or force-push.
- It is a v1 test instrument. If an instruction conflicts with `life_os_governance.md`, governance wins.

## Repository structure (the fixed homes)

```
/guidelines/        Canonical guideline (version in filename) + CHANGELOG.md.
/assets/backgrounds Baked slide backgrounds, mapped to pillars.
/assets/icons       Consolidated icon sprite + source glyphs.
/assets/images      Photography and raster assets.
/assets/fonts       FrauncesJN and InterJN TTFs.
/design-system/     Derived tokens, type scale, squircle/panel primitives.
/templates/         References to Canva brand templates.
/skills/            v1 skill files.
/specs/             Build specs, research table, content playbook, profile review, build log.
```

Every file has one home. No file lands in two folders. If unsure, place by what the file *is* (a background, an icon, a spec), not by what it is *for*.

## Naming conventions

- Lowercase, hyphens, max three levels deep.
- "and" not "&".
- Guideline filename carries its version: `brand-guidelines-v4_0.html`.
- New version = new filename. Do not overwrite the old version's filename; bump it and update the README + CHANGELOG pointer.

## Commit conventions

- Message format: `<type>: <imperative summary>`.
- Type is one of: `guideline`, `assets`, `docs`, `structure`, `fix`, `design-system`.
- Group related files into one logical commit. Do not commit one file at a time when several changed together.

## The procedure

1. **Probe the write path.** Before any bulk operation, commit one tiny harmless file (or read the tree) to confirm the write path is live. The connector has shown 4-minute timeouts that commit nothing.
2. **Place each file in its fixed home** per the structure above.
3. **Commit** with a `<type>: <summary>` message.
4. **Read back.** Read the repo tree or the specific files to confirm they landed at the expected path and size. A commit is not done until a read confirms it. Never report success from the write response alone.
5. **Document the change** in two places:
   - `guidelines/CHANGELOG.md` (or the relevant folder): what changed, when.
   - A Notion Decisions Log row, if the change locks a decision: what changed and why.
6. **Update the Notion File Register** with the raw URL of each committed file (and version if bumped).

## Binary boundary

The GitHub connector `push_files` takes plain text only. Files that must go via Claude Code or the GitHub web UI:

- PNGs, TTFs, SVGs.
- HTML over ~10% base64 (the guideline HTML is ~94% base64).

When a binary file is part of the change, do the text files via the connector, then hand the binary list to Claude Code or flag it for a Cowork session. Do not attempt to base64-encode a binary into `push_files`; it corrupts.

## Update an existing file

Fetch the current SHA via `get_file_contents` first, then update. The connector rejects an update without the current SHA.

## Definition of done

A change is done when:
- The file is in its fixed home with a conventional name.
- The commit message follows the format.
- A read-back confirms it landed.
- The Notion File Register and (if a decision locked) the Decisions Log reflect it.

Anything short of this is in progress, not done.

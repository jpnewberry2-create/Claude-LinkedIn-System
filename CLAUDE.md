# CLAUDE.md

Operating instructions for any Claude surface working in this repository: Claude Code (terminal), Cowork (desktop), or a chat with the GitHub connector. Read this first, every session.

This file is the entry point. It tells you what the repo is, where files go, how to commit, how to verify, and how to keep the wider system in sync after a change. For the full skill rules, read `skills/v1-github-structuring-documenting-updating/SKILL.md` before any commit.

---

## What this repo is

The durable, fetchable source of truth for the LinkedIn personal brand guideline and assets. Any chat pulls the current version here at session start instead of relying on chat history.

One node in a three-part system:

| System | Role | Holds |
| --- | --- | --- |
| Notion | Project manager (the record) | Tasks, decisions, session log, ideas, the project page. |
| GitHub (this repo) | Maintainer (live files) | Working files that change: guideline, assets, design system, skills. |
| Google Drive | Archive (locked files) | Finished, signed-off deliverables that no longer change. |
| Canva | Final editor (downstream) | Brand kit `kAHLoHtCCJc`, carousel templates. Consumes a slice; never canonical. |

The one rule worth remembering: GitHub versions files that are still changing; Drive archives files that are finished.

Only humans and Claude act. This repo is a record. It holds state, it does not initiate it.

---

## Repository structure

```
README.md                  What the repo is, where the current guideline lives.
CLAUDE.md                  This file: operating instructions.
/guidelines/               The canonical brand guideline (current version) + CHANGELOG.md.
/assets/
    /backgrounds/          Baked slide backgrounds, mapped to content pillars.
    /icons/                The consolidated icon sprite and source glyphs.
    /images/               Photography and raster assets.
    /fonts/                The FrauncesJN and InterJN TTF files. Created on first font upload.
/design-system/            Tokens, type scale, squircle/panel primitives. Derived by Claude Design.
/templates/                References to the Canva brand templates.
/skills/                   v1 sandbox-stage skill files governing safe execution.
/specs/                    Build specs, research table, content playbook, profile review, build log.
```

---

## The upload task (Claude Code, one-off bulk)

When the instruction is "run the upload task," commit the local brand files into the repo per this mapping. Confirm the local root path with Jamie at session start if it is not already given.

Expected local structure:

```
LOCKED LI Brand Elements / LI Brand Assets /
    JN Fonts /          (8 TTFs)            → /assets/fonts/
    Iconography /       (icon folders + sprite HTML) → /assets/icons/

And separately, in the same parent:
    brand-guidelines-v4_0.html              → /guidelines/
    fractalbg*.png   (×4)                    → /assets/backgrounds/
    composite*.png   (×4)                    → /assets/backgrounds/
    frostedpanel*.png                        → /assets/backgrounds/
    wordmark*.png    (×6)                     → /assets/images/
    photofullbody.png                        → /assets/images/
    profileradial.png                        → /assets/images/
```

Folder mapping table:

| Local | Repo destination |
| --- | --- |
| `JN Fonts/*.ttf` | `assets/fonts/` |
| `Iconography/*` | `assets/icons/` |
| `brand-guidelines-v4_0.html` | `guidelines/` |
| `fractalbg*.png`, `composite*.png`, `frostedpanel*.png` | `assets/backgrounds/` |
| `wordmark*.png`, `photofullbody.png`, `profileradial.png` | `assets/images/` |

After the bulk commit, do the read-back step (below), then update the Notion File Register with the raw URLs of each committed file.

---

## Commit conventions

- File and folder names: lowercase, hyphens, max three levels deep. Words spelled out use "and", not "&".
- The guideline filename carries its version (e.g. `brand-guidelines-v4_0.html`).
- Every commit message: `<type>: <imperative summary>`, where type is one of `guideline`, `assets`, `docs`, `structure`, `fix`, `design-system`.
- Group related files into one logical commit, not one commit per file.

---

## Read-back verification (mandatory)

After any commit, verify by reading the repo tree or the specific files back, not by trusting the write response. A commit is not "done" until a read confirms it landed at the expected path and size. This catches the silent write-path failures the GitHub connector has shown.

---

## Keep the system in sync (after any change)

A file change is not finished when it is committed. It is finished when the record reflects it:

1. Commit the file here, with a `<type>: <summary>` message.
2. Read it back to confirm.
3. Update the Notion File Register row with the new raw URL (and version, if bumped).
4. Write a Notion Decisions Log row if the change locks a decision (what changed and why).
5. If the change affects the Canva brand kit (new icon, new colour, new background), flag it for the next Cowork session: the connector cannot write kit colours, fonts, or logos.

---

## The Cowork update pattern (ongoing, little-and-often)

Cowork is the tool for ongoing maintenance after the one-off bulk upload. It sees the latest files from the local machine or a Claude project folder and operates GitHub, Notion, and Canva in one session.

A typical Cowork update:

1. Pick up the changed file (new background variant, icon set, guideline bump to v4.1, new spec).
2. Commit it to the right repo folder, message per convention, read back to confirm.
3. Update the Notion File Register and, if a decision is locked, the Decisions Log.
4. If a Canva-side action is needed (load new icons to the brand kit, publish a template), do it in the same session.

---

## Tool boundaries (known limits)

- GitHub connector `push_files` takes plain text only. PNGs, TTFs, SVGs, and HTML over ~10% base64 must go via Claude Code or the GitHub web UI. The guideline HTML is ~94% base64: Claude Code or web UI only.
- Probe first: attempt one tiny commit before bulk operations to confirm the write path is live. The connector has shown 4-minute timeouts that commit nothing.
- Updating an existing file via the connector needs the current SHA, fetched first.
- Canva brand kit colours, fonts, and logos cannot be written by any connector. They are manual UI or Cowork tasks.

---

Built and maintained with Claude.

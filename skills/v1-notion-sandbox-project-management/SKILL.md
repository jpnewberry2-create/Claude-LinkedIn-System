---
name: v1-notion-sandbox-project-management
description: Manage the LinkedIn project plan autonomously inside an isolated Notion sandbox (Tasks, Decisions Log, Session Log, Ideas/Inputs) only. Use when reading or writing project state to Notion: updating task status, logging a locked decision, writing a session log, or shaping an idea into a brief. Never touches the canonical Life OS spine. v1 test instrument; defers to life_os_governance.md.
---

# v1 Notion Sandbox Project Management Skill

A test-stage skill governing autonomous plan management in an isolated Notion sandbox. v1: expected to change. Defers to `life_os_governance.md` where they conflict.

## When this fires

Any time project state is read from or written to Notion: a task moves status, a decision locks, a session ends, an idea is shaped into a generation brief, the File Register is updated.

## Hard boundary

This skill acts ONLY on the four Project OS databases under the blueprint page. It NEVER writes to the canonical Life OS spine (Goals, Projects, Areas, the main Tasks database). The sandbox is isolated by design so a v1 test instrument cannot corrupt the live system.

If an instruction would write outside the sandbox, stop and ask. Do not assume permission.

## The sandbox (fixed IDs)

Blueprint parent page: `386c96325fbb801daf35e02728988fb8`

| Database | Data source ID |
| --- | --- |
| Tasks | `743480eb-e783-416c-ba57-bfc96cac8477` |
| Decisions Log | `4c923726-f51c-4e9b-b5c1-a6a41f68f641` |
| Session Log | `4d444be0-0df3-44d2-aa03-7896568501c0` |
| Ideas / Inputs | `544d4e3f-89fc-4419-8624-3147e71e4c9c` |

Related (read for context, do not restructure):
- LinkedIn Command Centre: `321c96325fbb8056b4cece5156527a20`
- Build Progress Tracker: `5caa304db0ab4c6ba09eb56fa875274e`

## Database roles

- **Tasks** — open work with a status model. The only place tasks live. Status, Priority (Now/Next/Later), Phase, Notes.
- **Decisions Log** — one row per locked decision, with rationale. The "why" record. Written when something is locked, not while it is still open.
- **Session Log** — one row per working session. The narrative thread for cold re-entry: what was done, what was deferred. Written at session end, no exceptions.
- **Ideas / Inputs** — the backlog. Each row structured enough to become a generation brief. Status (Raw/Shaped/In progress/Shipped), Type (the pillar), Brief, Performance (filled after a post ships, closing the feedback loop).

## The named triggers

Information moves at defined moments:

- **On approval** → the asset is committed to GitHub; the Task moves to Done.
- **On lock** → a Decisions Log row is written (what and why).
- **At session end** → a Session Log row is written. Always. This is the rule that makes cold re-entry work.
- **On ship** → the Idea's Performance field is filled with real data, closing the loop.

## Procedure for a write

1. **Read first.** Fetch the target database or page before writing, to avoid duplicates and to confirm the current state.
2. **Write to the correct database** per its role. A task goes to Tasks, a decision to Decisions Log. Do not log a decision as a task or vice versa.
3. **Use `notion-create-pages` with the `data_source_id`** for new rows.
4. **Confirm by querying back** with `notion-query-database-view` where the write matters.

## Known Notion limits

- Valid colours: default, gray, brown, orange, yellow, green, blue, purple, pink, red. "teal" is rejected.
- Status property custom options cannot be added via DDL. Add manually in the UI.
- Views cannot be deleted via API. Rename with a warning prefix for manual deletion.
- Fetch by full notion.so URL or internal page ID.

## Definition of done

A session is done when the Session Log has a row for it. A decision is done when the Decisions Log has a row with rationale. A shipped post is done when its Idea row carries performance data. Anything short of this leaves the record behind the reality.

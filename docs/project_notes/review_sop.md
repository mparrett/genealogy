# Review SOP (Local Only)

Purpose: quickly review open questions and pending tasks without using the public site.

## Entry Point

Start here in the documentation browser:
- `docs/project_notes/open_questions.md` (primary tracker)
- `TODO.md` (project backlog)

## How to use `mdserve`

From the repo root:

```bash
mdserve .
```

Then open the URL shown in the terminal (for example `http://0.0.0.0:8037/`).
The index page lists all supported files and renders Markdown.
Press `Ctrl+C` to stop the server.

## Internal vs Site Content

Use directory/location to distinguish intent:

**Internal research / task docs (not part of site):**
- `docs/project_notes/` (project memory + trackers)
- `research/*-prompt.md`, `research/*-summary.md`, `research/*-results.md`
- `TODO.md`, `DEV.md`, `OVERVIEW.md`
- `assets/bear/` (Bear sync notes)

**Site content (published):**
- `research/reports/*.md` (source biographies/reports)
- `research/reports/html/` (generated HTML; do not edit)
- `index.html` (manual homepage)
- `pdf/` (published PDFs)

If a doc is not under `research/reports/` (or `index.html` / `pdf/`), treat it as internal by default.

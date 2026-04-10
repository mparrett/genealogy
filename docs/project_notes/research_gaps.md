# Research Gaps & Consistency Log

Last scan: 2026-02-05

Purpose: Track discrepancies, inconsistencies, open questions, and uncertainties across research sources, generated outputs, and assets. This log is the meta-layer for repo hygiene. Genealogy questions still live in `docs/project_notes/open_questions.md`.

## Scan Checklist
1. Generated output parity: confirm each `research/reports/*.md` has a matching HTML file and each `lines/data/*.yml` has a matching line page.
2. Asset references: confirm image and PDF references resolve to existing files; list unreferenced assets.
3. Documentation consistency: reconcile `OVERVIEW.md`, `docs/project_notes/key_facts.md`, and `AGENTS.md`.
4. Research uncertainties: identify explicit "unclear/TBD" statements in bios and ensure they are tracked in `open_questions.md` if actionable.
5. Record updates: add new gaps here, and move resolved items to the Resolved Log with date and fix summary.

## Open Gaps
- ID: ASSET-001 | Status: OPEN | Gap: Moses Mansfield Mowery lineage PDF is linked from pages but stored in a non-public location.
Notes: Links in `lines/data/mowery.yml` and `research/reports/moses_mansfield_mowery_bio.md` point to `pdf/Moses_Mansfield_Mowery_1822-1904_Lineage_Confirmation.pdf`, but the file currently lives in `pdf/internal/`.
Next action: Decide whether this PDF should be public. If yes, move/copy to `pdf/` and keep links. If no, remove the links or point to an internal-only path.
Source refs: `lines/data/mowery.yml`, `research/reports/moses_mansfield_mowery_bio.md`, `pdf/internal/Moses_Mansfield_Mowery_1822-1904_Lineage_Confirmation.pdf`.

- ID: ASSET-002 | Status: OPEN | Gap: 16 non-original image files appear unreferenced by reports or line data.
Notes: Unreferenced images outside `images/originals/` were detected in the 2026-02-05 scan. Some are likely pre-conversion PNGs or future-use location panels.
Next action: Decide which should be used, converted to JPG, moved under `images/originals/`, or archived.
Source refs: `images/george-kuthe-migration.png`, `images/huldah-oregon-pioneer.png`, `images/james-gleeson-mondovi.png`, `images/laurence-higgins-newark.png`, `images/locations/feather-river-canyon-1915.jpg`, `images/locations/newark-nj-1895.jpg`, `images/locations/sligo-town-1880.jpg`, `images/mary-knight-sligo-nyc.png`, `images/railroad-wwi-era.png`, `images/tennessee-pioneer.png`, `images/texas-farming-1820-1830.png`, `images/thumbs/huldah-oregon-pioneer.jpg`, `images/thumbs/urban-irish-eastcoast.jpg`, `images/thumbs/wisconsin-irish-farming.jpg`, `images/urban-irish-eastcoast.png`, `images/wisconsin-irish-farming.png`.

- ID: DOC-001 | Status: OPEN | Gap: File naming guidance conflicts with current report filenames.
Notes: Instructions specify kebab-case for research files, but `research/reports/` uses snake_case naming. This creates ambiguity for future additions and tooling.
Next action: Decide whether to update guidance to match current practice or plan a rename migration.
Source refs: `AGENTS.md`, `research/reports/`.

- ID: DOC-002 | Status: OPEN | Gap: `OVERVIEW.md` content is out of date relative to the current site and report inventory.
Notes: Overview lists 11 biographies across three lines and describes a homepage layout with `<details>` sections, but the repo now contains 29 report HTML files and `index.html` uses line cards with thumbnails.
Next action: Update `OVERVIEW.md` to reflect current counts and homepage layout, or mark it as historical.
Source refs: `OVERVIEW.md`, `research/reports/html/`, `index.html`.

- ID: UNC-001 | Status: OPEN | Gap: Explicit uncertainty statements exist in bios but are not centrally tracked.
Notes: The following bios include "unclear"/open-ended items that are not mapped to `open_questions.md`: `james_e_higgins_bio.md`, `howard_higgins_bio.md`, `doris_kuthe_bio.md`, `laurence_higgins_bio.md`, `pleasant_a_mowrey_bio.md`.
Next action: Decide whether to add these as discrete items in `docs/project_notes/open_questions.md` or keep them inline only.
Source refs: `research/reports/james_e_higgins_bio.md`, `research/reports/howard_higgins_bio.md`, `research/reports/doris_kuthe_bio.md`, `research/reports/laurence_higgins_bio.md`, `research/reports/pleasant_a_mowrey_bio.md`.

## Resolved Log
- 2026-02-05: Updated `docs/project_notes/key_facts.md` to align local server session naming and ancestry assets path with the actual repo structure.

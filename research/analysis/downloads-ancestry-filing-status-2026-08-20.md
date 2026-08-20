# Downloads Ancestry Filing — Status Check

**Date:** 2026-08-20
**Purpose:** Follow-up on the filing plan from `research/analysis/downloads-ancestry-inventory-james-higgins-2026-06-11.md` — checking what's been executed since that survey.

---

## The plan (§8 of the 2026-06-11 survey)

1. Promote confirmed James Everett Higgins sources (interment card, birth cert #6077, portrait, Theresa+James photo) into `assets/external/ancestry/james-higgins/`
2. Quarantine namesakes (Butte MT "James Higgins," AZ infant death cert, J.E. Higgins Lumber Co., SAR bulletin) into `assets/external/_namesakes-not-ours/`
3. Re-home the SAR bulletin to the Mowery/Birch colonial line
4. Visually verify 4 unverified "Genealogy Image" PDFs before trusting them
5. Import the master GEDCOM (`Ancestry2/public-parrett-birch-higgins.ged`) as a cross-reference backbone

## Execution status (checked 2026-08-20)

| Step | Status | Evidence |
|------|--------|----------|
| 1. Promote confirmed James sources | ❌ Not done | No `assets/external/ancestry/james-higgins/` subfolder exists. Interment card, birth cert #6077, portrait, and Theresa+James photo are still only in `~/Downloads-no-iCloud/`. |
| 2. Quarantine namesakes | ❌ Not done | No `assets/external/_namesakes-not-ours/` folder exists anywhere in the repo. |
| 3. Re-home SAR bulletin | ❌ Not done | Bulletin not found under any Mowery/Birch path in `assets/external/`. |
| 4. Verify 4 "Genealogy Image" PDFs | ❓ Unknown | No record of this check in `docs/project_notes/` or `research/findings/james-higgins/facts.md`. |
| 5. Import master GEDCOM | ❌ Not done | `find . -iname "*.ged"` returns nothing — no GEDCOM file in the repo. |

**Partial exception:** `James Everett Higgins-ancestry-2026-01-26.pdf` (the Ancestry profile export, item 6 of the survey's confirmed-sources table) did get filed into `assets/external/ancestry/`, along with `Laurence Higgins-ancestry-2026-01-26.pdf` and a `James Higgins - Print.md`. These appear to predate the June survey (Jan 2026 exports) rather than being a result of acting on it.

## Bottom line

The June 2026 survey produced a filing plan but the plan was never executed — nothing from the Downloads folders was moved, quarantined, or GEDCOM-imported as a direct result of it. The only James-Higgins-related files in `assets/external/ancestry/` are older Ancestry.com "Print" exports unrelated to §8's action items.

## Next steps (if resuming this work)

- Decide whether to execute §8 now, given ~10 weeks have passed and the burial-record open question (resolved by the interment card) is still not reflected in the repo's tracked facts.
- Re-survey `~/Downloads-no-iCloud/` first in case folder contents have changed since 2026-06-11.

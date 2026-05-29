# Gleeson Pages Audit — 2026-04-11

Cross-checked all Gleeson-related files for consistency. Six issues found, ranked by severity.

## Issues

### 1. CRITICAL: James J. Gleeson years wrong in line page

**File:** `lines/data/gleeson.yml` line 39
**Problem:** Lists `years: 1850–1936` — should be `1863–1946`
**Every other source agrees:** bio, summary, parish records, obituary

### 2. HIGH: Anne Barbara marriage date conflicts across files

Three different claims:
- `anne_barbara_gleeson_bio.md` — **May 1928** to Raymond Mowrey (correct, per Williams News primary source)
- `research/summaries/gleeson.md` line 115 — says "1 June 1921, Maricopa, AZ" as the Raymond Mowrey marriage date. This is actually the uncertain Paul B. Hannah record, wrongly attributed.
- `research/reports/james_j_gleeson_bio.md` line 21 — says Anne "married Raymond R. Mowrey in 1930"

**Fix:** James bio should say 1928. Summary should not attribute the 1921 record to Raymond Mowrey. The Anne Barbara bio handles this correctly already (1928 confirmed, 1921 uncertain/Hannah).

### 3. HIGH: Mother's death — Australia attribution without caveat

**File:** `research/summaries/gleeson.md` lines 25-28
**Problem:** States Margaret Moloney died "25 October 1886 in Drouin, Victoria, Australia" as a fact for our line
**Reality:** `patrick_gleeson_bio.md` correctly notes this likely belongs to the **Australian** Patrick's wife Margaret Mahony, not our Margaret Moloney
**Fix:** Add disambiguation caveat or remove from our line's summary

### 4. MEDIUM: Patrick Gleeson birth year inconsistency

| Source | Birth year |
|--------|-----------|
| Bio heading | c. 1835 |
| Bio text | 1830–1845 |
| Timeline YAML | 1835 |
| Line YAML | c. 1835 |
| Summary (from Ancestry) | 1843 |

The summary's 1843 and "bef. 1925" death may come from Ancestry data that conflates the Australian Patrick. Consider standardizing on "c. 1835" with the range noted in the bio text.

### 5. MEDIUM: Children list discrepancy for James J. Gleeson

Summary (`gleeson.md`) lists 8 children; bio lists 7. Differences:
- Summary has "Jennie Gleason (1896–)" and "Jane Agnes Gleeson (1897–1977)" — possibly the same person?
- Summary includes "Harold Francis Gleason (1903–1988) — born Chicago" not in bio
- Bio includes "Maria Johanna (1894–1894)" who died in infancy

These need reconciliation against census records.

### 6. LOW: Open question GLE-006 may be partially resolved

GLE-006 asks about Anne Barbara's marriage date (1921 vs ~1930). The Anne Barbara bio and findings file have already resolved this: **May 1928** per Williams News primary source. The 1921 record is a separate uncertain marriage to Paul B. Hannah. Consider updating GLE-006 status to reflect this.

## Files checked

- `research/reports/patrick_gleeson_bio.md`
- `research/reports/james_j_gleeson_bio.md`
- `research/reports/anne_barbara_gleeson_bio.md`
- `research/reports/timeline-data/patrick_gleeson_bio.yml`
- `research/summaries/gleeson.md`
- `research/results/gleeson-croom-family.md`
- `research/findings/anne-gleeson/facts.md`
- `lines/data/gleeson.yml`
- `docs/project_notes/open_questions.md`

## CLAUDE.md status

Checked against actual repo structure — **accurate**. Build commands, project structure, research organization, naming conventions, and bio layout docs all match. Only minor omission: `research/origins/` directory not mentioned (small, not critical).

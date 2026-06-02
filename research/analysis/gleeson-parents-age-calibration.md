# Calibrating Patrick Gleeson + Margaret Moloney birth years

**Date:** 2026-05-30 (initial), revised **2026-06-01** after withdrawal of the Ella firstborn anchor
**Purpose:** Replace generic Ancestry birth-year estimates with a defensible calibration using post-Famine Irish demographic norms.

---

## Why we need this

The "1843" birth years floating around our Ancestry data for both Patrick and Margaret are contamination from the Australian Patrick Gleeson line (his wife Margaret Mahony was born 22 Dec 1842, and tree-merging propagated paired 1843 dates). With that struck, we have no documentary birth year for either Patrick or Margaret. This document anchors a calibrated estimate on what we actually know.

## Revision history

- **2026-05-30 (initial):** Anchored on "Ella Isabel Gleason (eldest known child) married 24 Dec 1874 in Eau Claire WI; she was likely 16–20 at marriage; born ~1854–1858; therefore parents married ~1853–1857." This gave Patrick c. 1828, Margaret c. 1832, marriage ~1855.
- **2026-06-01 (current):** Ella anchor **withdrawn**. The 1874 Eau Claire marriage record's bride's father is C. R. Gleason, not Patrick — a different family. **James (baptized 23 Dec 1863, Croom) is now our earliest documented child.** Calibration redone below.

## What we know (anchors)

| Fact | Source |
|------|--------|
| Earliest documented child James baptized 23 Dec 1863, Croom | NLI Catholic Parish Registers, vtls000634977 page 87 |
| Last documented child Jane baptized 28 Sep 1878, Croom | NLI Catholic Parish Registers, vtls000634977 page 121 |
| Documented family span James (1863) → Jane (1878) = **15 years of confirmed childbearing** | Derived |
| **Patrick documented as a Farmer in Croom by 11 Sept 1859** | NAI Petty Sessions Order Books, CSPS1/8381 |
| Croom marriage register searched continuously May 1853 – Feb 1858 — no Patrick + Margaret found | NLI parish register sweep 2026-06-01 |

**Important new constraint (added 2026-06-02):** Patrick was already an established farmer in Croom by Sept 1859. This means he was a man of standing (rented land) in his late 20s, ready to marry. The 1859 anchor supports a marriage anywhere from **1860–1863** (between farming-established and James's baptism). It does NOT rule out an even earlier marriage, but combined with the negative results from the 1853–1858 Croom marriage sweep, **1860–1863 is now our highest-confidence window**.

## Demographic baseline: post-Famine Ireland

Post-Famine Ireland (1850s–80s) had the latest marriage age in Europe, driven by land-inheritance practices and economic conditions. Generic 1860s averages (often quoted by LLMs) **do not apply** to Irish data.

| Population | Female 1st marriage | Male 1st marriage |
|---|---|---|
| Generic Anglo-American 1860s | 22–23 | 25–26 |
| **Post-Famine Ireland** | **25–28** | **28–32** |

Sources: Kennedy, *The Irish: Emigration, Marriage, and Fertility* (1973); Ó Gráda, *Ireland: A New Economic History* (1994).

## Calibration

Anchoring on James (Dec 1863) as the earliest documented child, with Irish post-Famine norms:

If James is firstborn → parents married ~1862 (assuming typical 9–12 month interval between marriage and first child).

| Person | Low end (younger marriage) | Average | High end (older marriage) |
|---|---|---|---|
| **Margaret** at 1st child age | b. ~1838 (age 25) | b. ~1835 (age 28) | b. ~1833 (age 30) |
| **Patrick** at 1st child age | b. ~1835 (age 28) | b. ~1832 (age 31) | b. ~1830 (age 34) |

### Sanity check: last child Jane 1878

- If Margaret was b. 1838, she'd be **40** at Jane's birth — typical upper edge
- If Margaret was b. 1836, she'd be **42** — still plausible
- If Margaret was b. 1834, she'd be **44** — at the upper edge of typical childbearing

The Jane-1878 anchor is compatible with the full Margaret range 1834–1838.

### Important caveat: James may not be firstborn

We don't have evidence James was actually firstborn. There could be:
- Older siblings baptized in Croom pre-1863 (we haven't searched those pages yet)
- Older siblings baptized in a neighboring parish (if Margaret was from elsewhere and they married+started family there)
- Older siblings born and died before 1863 with no surviving record

If James is NOT firstborn, the marriage is earlier and the parents' birth years shift earlier accordingly.

The 1946 obit mentions a third surviving sister ("Mrs. John Hayes, Staten Island NY") whose identity is unknown — she could be a younger emigrant sister (= one of the 7 documented Croom children) OR an older sister we haven't documented. If the latter, calibration shifts earlier.

## Resulting estimates

- **Margaret: c. 1836 (range 1834–1838)**
- **Patrick: c. 1832 (range 1830–1834)**
- **Marriage: c. 1862**

These are materially **later** than the previous (now-withdrawn) calibration anchored on Ella (which gave Margaret c. 1832, Patrick c. 1828, marriage ~1855). The shift is ~4–7 years later for the marriage and parents' births.

## Caveats

- Birth years for individuals can deviate significantly from population norms — these are priors, not posteriors. Any documentary evidence (baptism, marriage, death, census) trumps the calibration.
- The "James is firstborn" assumption is the largest source of uncertainty. If there's an older sibling we haven't found, both estimates shift earlier.
- The Croom marriage register has been swept May 1853 – Feb 1858 (no match). Either (a) marriage was in Croom outside that window — most likely 1860–1862, or (b) marriage was in a neighboring parish (Fedamore, Adare, Bruff, Athlacca, Knockainey).

## Recommendation

Update bio, fact sheet, and timeline YAML to use:

- **Patrick:** "c. 1832 (range 1830–1834)"
- **Margaret:** "c. 1836 (range 1834–1838)"
- **Marriage:** "c. 1862"

Strike all "1843" references and the prior "1828/1832" calibration based on Ella as firstborn.

## Search priority for next phase

The new calibration points the marriage search at:

1. **Croom marriage register page 151** (Aug 1861 – Mar 1862) — was previously obscured by thumb shadow in an older review; needs re-fetch and re-read at the new hi-res capability
2. **Croom marriage register pages 148–150** (1859–1861) — unchecked
3. **Croom marriage register pages 152** (overlap with 151) — unchecked
4. Neighboring parishes if Croom yields nothing in that window

## Related files

- `research/findings/patrick-gleeson/facts.md`
- `research/reports/patrick_gleeson_bio.md`
- `research/reports/timeline-data/patrick_gleeson_bio.yml`
- `research/summaries/gleeson.md`
- `research/analysis/nli-parish-register-pipeline.md` — how to fetch the needed pages

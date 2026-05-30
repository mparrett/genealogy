# Calibrating Patrick Gleeson + Margaret Moloney birth years

**Date:** 2026-05-30
**Purpose:** Replace generic Ancestry birth-year estimates with a defensible calibration using post-Famine Irish demographic norms.

---

## Why we need this

The "1843" birth years floating around our Ancestry data for both Patrick and Margaret are contamination from the Australian Patrick Gleeson line (his wife Margaret Mahony was born 22 Dec 1842, and tree-merging propagated paired 1843 dates). With that struck, we have no documentary birth year for either Patrick or Margaret. This document anchors a calibrated estimate on what we actually know.

## What we know (anchors)

| Fact | Source |
|------|--------|
| Eldest known child Ella Isabel married 24 Dec 1874 in Eau Claire, WI | Wisconsin Marriage Records, Box 674142 |
| Ella was likely 16–20 at marriage → born **~1854–1858** | Inference from marriage age |
| James Gleeson (2nd child) baptized 23 Dec 1863, Croom | NLI Catholic Parish Registers |
| Last known child Jane baptized 25–28 Sep 1878, Croom | NLI Catholic Parish Registers |
| Family span Ella (~1856) → Jane (1878) = **~22 years of childbearing** | Derived |

## Demographic baseline: post-Famine Ireland

Post-Famine Ireland (1850s–80s) had the latest marriage age in Europe, driven by land-inheritance practices and economic conditions. Generic 1860s averages (often quoted by LLMs) **do not apply** to Irish data.

| Population | Female 1st marriage | Male 1st marriage |
|---|---|---|
| Generic Anglo-American 1860s | 22–23 | 25–26 |
| **Post-Famine Ireland** | **25–28** | **28–32** |

Sources: Kennedy, *The Irish: Emigration, Marriage, and Fertility* (1973); Ó Gráda, *Ireland: A New Economic History* (1994).

## Why Gemini's calibration was off

Gemini suggested mother age 22–25 / father 26–28 for the 1863 child if firstborn. Two problems:

1. **Wrong demographic baseline** — used Anglo-American 1860s averages, not Irish post-Famine norms (which run ~3–6 years older).
2. **Wrong anchor child** — James (1863) was the 2nd child, not the firstborn. Ella (~1856) is the eldest known child, and the marriage formation event is anchored on her, not James.

## Calibration

Anchoring on Ella as firstborn (~1856) with Irish post-Famine norms:

| Person | Low end (younger marriage) | Average | High end (older marriage) |
|---|---|---|---|
| **Margaret** at 1st child age | b. ~1831 (age 25) | b. ~1828 (age 28) | b. ~1826 (age 30) |
| **Patrick** at 1st child age | b. ~1828 (age 28) | b. ~1825 (age 31) | b. ~1822 (age 34) |

### Sanity check: last child Jane 1878

- If Margaret was b. 1828, she'd be **50** at Jane's birth — improbable
- If Margaret was b. 1830, she'd be **48** — still very old
- If Margaret was b. 1832, she'd be **46** — at the upper edge of typical childbearing
- If Margaret was b. 1834, she'd be **44** — plausible

The Jane-1878 anchor pulls Margaret's birth year **later** than the Ella-firstborn anchor alone would suggest. Reconciling:

- **Margaret: c. 1830–1834** (centered c. 1832)
- **Patrick: c. 1825–1830** (centered c. 1828)

This brackets Patrick about **7 years older than our previous "c. 1835"** estimate and gives Margaret a defensible range that's compatible with both her firstborn (Ella ~1856) and her lastborn (Jane 1878).

## Caveats

- Birth years for individuals can deviate significantly from population norms — these are priors, not posteriors. Any documentary evidence (baptism, marriage, death, census) trumps the calibration.
- The "Ella was firstborn" assumption is the largest source of uncertainty. If there's an older sibling we haven't found, both estimates shift earlier.
- Patrick's "sailor" occupation might correlate with later marriage (maritime workers often delayed family formation) — would push Patrick's estimate even earlier, but the evidence is thin.

## Recommendation

Update bio, fact sheet, and timeline YAML to use:

- **Patrick:** "c. 1828 (range 1825–1830)"
- **Margaret:** "c. 1832 (range 1830–1834)"
- **Marriage:** "~1855" (not "~1860" as currently in bio — Ella's existence pushes it earlier)

Strike all "1843" references.

## Related files

- `research/findings/patrick-gleeson/facts.md`
- `research/reports/patrick_gleeson_bio.md`
- `research/reports/timeline-data/patrick_gleeson_bio.yml`
- `research/summaries/gleeson.md`

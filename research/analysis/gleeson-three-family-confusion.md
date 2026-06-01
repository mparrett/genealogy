# Three Patrick Gleeson families that get confused with ours

**Date:** 2026-05-31
**Purpose:** Disentangle three distinct Patrick Gleeson families that have been merging in Ancestry trees and earlier research notes. Identify which data points have been wrongly attributed to our Croom Patrick.

---

## The three families

| | **Ours (Croom)** | **Limerick City** | **Australian** |
|---|---|---|---|
| **Patrick's residence** | Scagh, Croom parish, Co. Limerick | The Windmill, St Michael's, Limerick City | Victoria, Australia |
| **Wife** | Margaret **Moloney** | Mary **Mahony** | Margaret **Mahony** |
| **Wife's origin** | Limerick area (presumed) | (unknown) | Bantry, Cork |
| **Marriage** | ~1855, Ireland (presumed Croom) | (unknown) | 1862, Victoria (reg. #639) |
| **Patrick's occupation** | **Unknown** (see correction below) | Sailor (per civil record) | (varies) |
| **Sample children** | James (Dec 1863), Honora (1866), Bridget (1868), Ellen (1869), Mary (1872), Margaret (1875), Jane (1878) | John (17 May 1864) | Michael, Patrick Thomas (1868), Mary Ellen (1875), John (1877) |

## Smoking-gun timing

The Limerick City John was born **17 May 1864**, just **5 months after** our James was baptized 23 Dec 1863. That's biologically impossible if they're siblings — so John 1864 is definitively NOT ours.

Adding to that: the Limerick City civil record names the mother as **Mary** (not Margaret), and her maiden name as **Mahony** (not Moloney). Two hard conflicts on identity.

## Data points wrongly attributed to our Patrick

Earlier notes (`research/prompts/patrick-gleeson-marriage.md`, the previous bio) imported these from the **Limerick City** family without flagging the conflict:

| Attribution | Real source | Action |
|---|---|---|
| Occupation: **Sailor** | Limerick City Pat Gleeson civil record | **Remove** — our Patrick's occupation is unknown |
| Residence: **The Windmill, St Michael's, Limerick City** | Limerick City Pat Gleeson civil record | **Remove** — our Patrick lived in Scagh, Croom |
| Birth: **~1840** | (mixed; partly Limerick City inference, partly Australian Patrick) | Replaced by calibration (c. 1828) |
| Margaret birth: **~1843** | Australian Margaret Mahony (b. 22 Dec 1842) | Replaced by calibration (c. 1832) |
| Son **John 17 May 1864** | Limerick City Pat + Mary Mahony | **Remove** from our children list |

## How the merge happened

The previous research prompt strung together datapoints that *looked* compatible — Patrick Gleeson, Limerick, mid-1860s — without checking surface details:

1. James Dec 1863 baptism from Croom (correct for us)
2. John May 1864 civil record from Limerick City (Mary Mahony, not us)
3. Sailor occupation pulled from #2
4. Address (The Windmill) pulled from #2

Once "sailor at The Windmill" was in our prompt, it propagated forward as if true for our Patrick. This is a research-hygiene cautionary tale: always cross-check the **mother's name** before accepting a sibling.

## What stays

The **Moloney** surname lock is unaffected — if anything, separating out the Mahony families *strengthens* it. The Mahony confusion belongs entirely to the Limerick City and Australian lines.

## Fingerprint summary (for future record evaluation)

**Reject as Limerick City Pat Gleeson family if:**
- Residence: The Windmill, St Michael's, Limerick City
- Wife: Mary Mahony
- Occupation: Sailor
- Child John b. 17 May 1864

**Reject as Australian Patrick Gleeson family if:**
- Wife: Margaret Mahony (b. Bantry, Cork, 22 Dec 1842)
- Marriage: 1862, Victoria, Australia
- Children include Michael, Patrick Thomas (1868), Mary Ellen (1875), John (1877)

**Accept as our Croom Patrick Gleeson family if:**
- Wife: Margaret **Moloney**
- Residence: Scagh, Croom parish, Co. Limerick
- Children include James Dec 1863, Bridget 1868, Ellen 1869, Mary 1872

## Related files

- `research/findings/patrick-gleeson/facts.md`
- `research/reports/patrick_gleeson_bio.md`
- `research/reports/timeline-data/patrick_gleeson_bio.yml`
- `research/summaries/gleeson.md`
- `research/analysis/gleeson-parents-age-calibration.md` (related — also strips Ancestry contamination)

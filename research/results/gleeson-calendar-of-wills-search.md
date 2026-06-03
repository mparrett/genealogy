# Calendar of Wills Search — Patrick & Margaret Gleeson

**Date searched:** 2026-06-02
**Source:** National Archives of Ireland, Calendars of Wills and Administrations 1858–1922
**URL:** https://www.willcalendars.nationalarchives.ie/search/cwa/

## Searches run

Programmatic queries via the form's GET endpoint (`results.jsp`). Form parameters: `deceasedSurname`, `deceasedForename`, `placeDeath`, `dateYear`, `probateOrAdministration`.

### Patrick Gleeson — Co. Limerick (1858–1922)

Only **three hits**, all checked against the PDF scans. **None are our Patrick.**

| ID | Death date | Place | Occupation | Beneficiary | Effects | Verdict |
|---|---|---|---|---|---|---|
| 1639547374 | 7 Jul 1897 | Cloon and Commons, Co. Limerick (died at Limerick Union Workhouse) | Farmer | Anne Gleeson, Widow | £34 5s | ❌ Wrong widow (Anne not Margaret); not Croom |
| 1639578957 | 28 Sep 1899 | Kyle, Cappamore, Co. Limerick | Farmer | Thomas Gleeson, Farmer (admin) | £267 | ❌ Cappamore is ~25 mi east of Croom |
| 1639575474 | 14 Jan 1900 | Six-mile-bridge, Co. Limerick | Licensed Victualler | Elizabeth Gleeson, Widow | £55 | ❌ Wrong occupation (publican, not farmer); wrong widow |

### Patrick Gleeson — adjacent counties for the 1911–1918 window

Patrick Gleeson death years near our 1918 deed window included Tipperary 1918 hits. Both checked and ruled out by beneficiary name:

| ID | Death date | County | Beneficiary | Verdict |
|---|---|---|---|---|
| 1700505748 | 11 Mar 1918 | Tipperary | Honora Gleeson | ❌ Wrong beneficiary |
| 1700505749 | 23 Dec 1918 | Tipperary | Cathe Gleeson | ❌ Wrong beneficiary |

### Margaret Gleeson — Co. Limerick (1858–1922)

Only **two hits**, both ruled out via PDF verification.

| ID | Death date | Place | Status | Beneficiary | Verdict |
|---|---|---|---|---|---|
| 1700515770 | 24 Feb 1919 | Nicker, Pallasgreen, Co. Limerick | **M.W. (Married Woman)** | Daniel Gleeson, Farmer, Husband | ❌ Married, not Widow — wrong family |
| 1700515768 | **14 Mar 1910** | Baggotstown West, Hospital, Co. Limerick | W (Widow) | Mary Gleeson, Spinster | ❌ Wrong death year (our Margaret alive Jan 1918) |

## Conclusions

1. **Patrick Gleeson is NOT in the Calendar of Wills 1858–1922.** Most likely died **intestate without probate granted** — consistent with a small estate or with property held jointly with Margaret (transferring to her automatically without need for administration).

2. **Margaret Gleeson is NOT in the Calendar of Wills 1858–1922.** Most likely died **after 1922** (when the 26-county calendar ends). Given she was c. 82 in 1918, dying age 87–94 in 1923–1930 is plausible.

3. **Patrick's death window relaxes** from "1911–1918" to **"after 1864 (last Petty Sessions appearance) and before Jan 1918 (1918 deed names Margaret as widow)"** — a 54-year window. The 1911 mortgage referenced in the 1918 deed was very possibly Margaret signing as already-widow, not Patrick co-signing.

4. **The 1918 Registry of Deeds memorial remains our strongest single document for the family** and the Kilfinny lead (via Jeremiah Molony of Ballymackeamore) remains the highest-leverage marriage-hunt direction.

## Disambiguation fingerprints — three wrong-family Limerick Patrick Gleesons

Any Ancestry hint or tree merging these into our Croom Patrick should be rejected:

- **Patrick Gleeson of Cloon and Commons, Co. Limerick** — Farmer, died 7 Jul 1897 at Limerick Union Workhouse, widow Anne Gleeson, effects £34
- **Patrick Gleeson of Kyle, Cappamore, Co. Limerick** — Farmer, died 28 Sep 1899, administrator Thomas Gleeson, effects £267
- **Patrick Gleeson of Six-mile-bridge** — Licensed Victualler, died 14 Jan 1900, widow Elizabeth Gleeson, effects £55

## Two wrong-family Limerick Margaret Gleesons

- **Margaret Gleeson of Nicker, Pallasgreen, Co. Limerick** — Married Woman, died 24 Feb 1919, husband Daniel Gleeson (farmer)
- **Margaret Gleeson of Baggotstown West, Hospital, Co. Limerick** — Widow, died 14 Mar 1910, executor Mary Gleeson (Spinster), probate delayed to 15 Nov 1919

## Artifacts saved

PDFs of the three relevant Calendar pages are at:
- `assets/external/willcalendars/calendar_1900_p184-185_patrick-gleesons.pdf` (1899/1900 Patricks)
- `assets/external/willcalendars/calendar_1902_p166-167_patrick-gleeson-cloon-commons.pdf` (1897 Patrick)
- `assets/external/willcalendars/calendar_1919_p140_margaret-gleesons.pdf` (1919 Margarets)

## Programmatic access pattern (for future searches)

The site uses simple GET-based search; no auth required. URL templates:

```
# Search (returns HTML with results in <td> elements)
https://www.willcalendars.nationalarchives.ie/search/cwa/results.jsp?deceasedSurname=X&deceasedForename=Y&placeDeath=Z&search=Search&pageSize=100

# Individual record details
https://www.willcalendars.nationalarchives.ie/search/cwa/details.jsp?id=<numeric_id>

# Full PDF calendar page scan (id from details page)
https://www.willcalendars.nationalarchives.ie/reels/cwa/<reel_dir>/<file>.pdf
```

The HTML form fields:
- `deceasedSurname`, `deceasedForename` — name
- `beneficiarySurname`, `beneficiaryForename` — beneficiary search
- `dateDay`, `dateMonth`, `dateYear` — death date
- `placeDeath` — free-text county
- `probateOrAdministration` — Probate/Administration/Both
- `search=Search` — required submit value

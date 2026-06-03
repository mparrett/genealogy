# Civil Birth Registrations — Croom SRD Gleeson 1879–1886

**Search date:** 2026-06-03
**Source:** irishgenealogy.ie civil records
**Search URL pattern:**
```
https://www.irishgenealogy.ie/search/?church-or-civil=civil&event-birth=1&lastname=Gleeson&yearStart=1879&yearEnd=1886&location=Croom
```

## Methodology

After completing the Croom Catholic parish register baptism sweep through page 125 (Jun 1881 — register ends), the post-register window (and the gap between Jane 1878 and Bridget 1881) required a different source. irishgenealogy.ie civil birth registrations are free, mandatory in Ireland post-1864, and indexed at the Superintendent Registrar's District (SRD) level — Croom is its own SRD covering the parish plus adjacent townlands.

**Search inputs:**
- Type: Civil records
- Event: Birth
- Lastname: Gleeson
- Location: Croom (autocomplete-resolved)
- Year range: 1879–1886
- (Mother's surname filter NOT useful — indexed field returns "N/R" Not Recorded for nearly all entries in this period; checked separately against Moloney/Molony/Maloney → 0 nationwide Gleeson hits for our window)

**Results:** 15 Gleeson civil births returned, all under the Croom SRD.

## Disambiguation outcome

The 15 results sort into at least three distinct Croom-area Gleeson family clusters. **Only one is OUR Patrick + Margaret Moloney family.**

### ⭐ OUR FAMILY — confirmed

| # | Child | Birth date | Register details | Notes |
|---|-------|-----------|------|-------|
| 8 | **Bridget Gleeson** (the second) | **11 Oct 1881, Croom** | Group reg ID **10767889**, page 189 entry 78, image `1966810/2027318.pdf` | Father Patrick Gleeson **Shopkeeper**, mother Margaret Gleeson formerly Moloney, residence Croom. **Informant: "Patt Gleeson, Father"** — Patrick signed personally (literate). Registered 3 Nov 1881 by E. Wallace Asst Registrar. PDF saved at `assets/external/civil-births-croom-1879-1886/bridget_1881.pdf` |

This is the **8th documented child** of Patrick + Margaret Moloney. Significance:
1. Confirms the 1901 Census Bridget age 18 at Main Street = this child (~1 yr understatement, normal)
2. Hard proof Patrick alive 3 Nov 1881 (replaces the 17 Feb 1881 godfather inference as our hard lower bound)
3. Patrick had transitioned from **Farmer to Shopkeeper** by 1881, residence had moved from Scagh to **Croom village** — both before his death, not as widow relocations
4. **Repeat name "Bridget"** — sister #3 (Bridget Feb 1868) was almost certainly still alive (= Mrs. Bridget O'Connor per 1946 obit); the repeat suggests honoring a grandmother (paternal grandmother per Irish naming = supports "Patrick's mother = Bridget" hypothesis)

### Cluster B — James Gleeson + Margaret Hickey, Fedamore

Likely an extended-family Gleeson branch, possibly cousins. Patriarch's occupation improved Labourer → Land Steward over the window — a notable social mobility marker.

| Child | Date | Father | Occupation | PDF |
|---|---|---|---|---|
| Michael | 10 Jan 1880 | James Gleeson + Margaret Hickey | Labourer | `michael_1880.pdf` |
| Mary | 10 Feb 1881 | James Gleeson + Margaret Hickey | Labourer | `mary_1881.pdf` |
| Margaret | 22 Dec 1885 | James Gleeson + Margaret Hickey | Land Steward | `margaret_1885.pdf` |

Possible link to **Catharina Gleeson of Fedamore** (1872 illegitimate baptism mother with Jeremiah Meara, mentioned in `research/analysis/`) and the **John Gleeson + Honora Walsh** 1855 Croom marriage. James Gleeson + Margaret Hickey may be a son of that branch.

### Cluster C — Stephen Gleeson + Mary Toomey, Boherygeela

Almost certainly the **Stephen Gleeson + Mariam Twomey/Toomey** marriage (Croom 1862, "sponte dispensatione" suggesting consanguinity dispensation — i.e. cousin marriage) we had already hypothesized as a Patrick-cousin / kinsman family.

| Child | Date | Father | Occupation | PDF |
|---|---|---|---|---|
| Anne | 5 Aug 1879 | Stephen Gleeson + Mary Toomey | Farmer | `anne_1879.pdf` |
| Patrick | 2 May 1884 | Stephen Gleeson + Mary Toomey | Farmer | `patrick_1884.pdf` (registered late, 27 Oct 1885) |

**Note:** Patrick (1884) and Margaret (1885 = Cluster B) sit on consecutive PDF IDs (1966806 / 1966808) in the births_1885 folder despite belonging to different families. The PDF-ID adjacency was coincidence — both are on register page 171/173 of the Croom SR 1885 register.

### Cluster D — Still to identify

The remaining records pulled but not yet inspected for parents:
- Helena 1880 (`helena_1880.pdf`)
- Ellen 1881 (`ellen_1881.pdf`)
- Catherine 1881 (`catherine_1881.pdf`)
- Michael 1882 (`michael_1882.pdf`)
- Honoria 1882 (`honoria_1882.pdf`)
- Thomas 1883 (`thomas_1883.pdf`)
- Daniel 1883 (`daniel_1883.pdf`)
- Garrett 1884 (`garrett_1884.pdf`)
- Maurice 1884 (`maurice_1884.pdf`)

These represent at least one more family cluster (probably more). Low-priority follow-up unless a new lead surfaces.

## Question resolved: Mary at Main Street in 1901 Census

The 1901 Census Main Street Croom household had **Mary Gleeson age 24** (Dressmaker, single, with Margaret Head Widow + Bridget 18). We previously hypothesized this Mary was a previously-undocumented additional daughter (b. ~1877).

**The civil birth search 1879–1886 found no Mary Gleeson child of Patrick + Margaret Moloney.** Only candidate was the Fedamore Mary (different family, ruled out).

**Best-fit interpretation now:**
- The Main Street Mary 1901 (age 24, Dressmaker) is most likely our **documented Mary 1872** — would have been 28 at 31 Mar 1901 → reported as 24, a 4-year understatement (large but not unheard of in Irish 1901 Census, especially for unmarried women)
- The Workhouse Mary 1901 (age 27, Matron of Workhouse, Skagh) is most likely an **unrelated Gleeson Workhouse staff member**, not our family
- (Previously we'd assumed the opposite — Workhouse Mary = our Mary 1872 working as Matron, Main Street Mary = unfound younger daughter. The civil-births absence flips this.)

A trace residual possibility: Mary was born to Patrick + Margaret outside the search window (pre-1879 or post-1886). Both are low probability given the existing 1872 Mary baptism is documented and the 1878–1881 gap is bridged by Bridget.

## Search system notes

- The civilrecords.irishgenealogy.ie legacy subdomain redirects to homepage as of 2026-06-03 — no longer curlable. Search is now JavaScript-driven at `https://www.irishgenealogy.ie/search/` with form params passed via URL.
- URL-param GET-form pattern works: `?church-or-civil=civil&event-birth=1&lastname=X&yearStart=Y1&yearEnd=Y2&location=L`
- Mother's surname filter (`mothers-surname=`) is highly restrictive — the GRO index frequently has "N/R" Not Recorded for that field in 1879–1886 records, so filtering by mother's surname **misses true positives** including our family's Bridget 1881 (the mother surname WAS recorded on Bridget's image but Bridget's index entry shows N/R). Use mother's surname only as a confirmatory check, not as a primary filter.
- Per-page count of 50 surfaces all results on one page. Pagination via URL `?page=N` doesn't work but the on-page "50 per page" link does.

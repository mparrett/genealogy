# NLI Parish Register Image Pipeline

**Date:** 2026-05-31
**Purpose:** Document how to fetch parish register page images directly from the National Library of Ireland (NLI) via curl. This bypasses paywalled providers (Ancestry, FindMyPast) and Cloudflare-protected ones (AskAboutIreland) and gives us a scriptable path to **every Irish Catholic parish register page**, free.

---

## TL;DR

You can fetch any NLI parish register page as a JPEG with a single curl:

```bash
curl -s "https://iserver.nli.ie/fcgi-bin/iipsrv.fcgi?FIF=000640000/000634977/vtls000634977_087.jp2&CVT=JPG" -o page.jpg
```

The above URL fetches Croom baptisms page 87 (Nov 1863–Mar 1864), which contains James J. Gleeson's baptism entry.

---

## Discovery path

This started as a question of whether Griffith's Valuation could be curled to speed up search. Direct answer for Griffith's: **no** — AskAboutIreland.ie (the canonical free source) is behind a Cloudflare browser-fingerprint challenge that bare curl can't pass.

Investigation pivoted to **NLI Catholic Parish Registers** (`registers.nli.ie`) — which turned out to be openly scrapeable. The image server (`iserver.nli.ie`) is an IIPImage instance that serves tiles and full JPEGs without auth.

---

## URL structure

### 1. Find the parish ID

Each Catholic parish has a numeric ID in NLI's catalog. Use search:

```bash
curl -s "https://registers.nli.ie/parishes?q=Croom" | grep -oE 'href="/parishes/[0-9]+'
```

For Croom: **parish ID `0881`**. Detail page is at `https://registers.nli.ie/parishes/0881`.

### 2. Find the register VTLS ID

A parish detail page lists each microfilm with a "vtls" identifier. For Croom:

| Microfilm | VTLS ID | Contents |
|---|---|---|
| 02427/04 | vtls000634974 | Marriages |
| 02427/05 | vtls000634975 | Marriages |
| 02427/06 | vtls000634976 | Baptisms + Marriages |
| **02427/07** | **vtls000634977** | **Baptisms + Marriages** (this is the one with our family) |

### 3. Fetch the page metadata

The register viewer page (`https://registers.nli.ie/registers/vtls000634977`) embeds a JavaScript `gon.pages_metadata` object that maps page numbers to date ranges. Extract it with:

```bash
curl -s "https://registers.nli.ie/registers/vtls000634977" | grep -oE 'gon\.pages_metadata=\{[^}]+\}'
```

For Croom baptism microfilm 02427/07, the baptisms run pages 4–125 (1844–1881) and marriages pages 126–161.

### 4. Fetch the page list (with file names)

```bash
curl -s "https://registers.nli.ie/diva/php/divaserve.php?d=000634977"
```

Returns JSON with a `pgs` array. Each page has a `"f"` field giving the JP2 filename, e.g. `vtls000634977_087.jp2`.

### 5. Construct the image URL

The URL format is:

```
https://iserver.nli.ie/fcgi-bin/iipsrv.fcgi?FIF={parent_dir}/{vtls_padded}/{filename}&CVT=JPG
```

Where:
- `vtls_padded` = the VTLS ID with "vtls" stripped, zero-padded to 9 chars. For `vtls000634977` that's `000634977`.
- `parent_dir` = a 10000-bucket containing the VTLS ID. Computed as `floor(vtls_num / 10000) * 10000 + 10000`, zero-padded to 9 chars. For 634977: `634977 - 4977 + 10000 = 640000` → `000640000`.
- `filename` = from the `pgs[index].f` field (e.g. `vtls000634977_087.jp2`).

### 6. Optional: scale and quality params

The IIP server supports:
- `WID=N` — width in pixels (max ≈4900)
- `HEI=N` — height in pixels
- `CVT=JPG` — output JPEG (default high quality)

A full-resolution Croom page is ~1500×1183 ≈ 255KB by default; you can request larger if needed.

---

## Page-to-date mapping for Croom baptisms (microfilm 02427/07)

Full mapping extracted from `gon.pages_metadata`. Pages 1–3 are intro/blank; 4–125 are baptisms; 126–161 are marriages.

### Our baptisms

| Child | Date | Page | Date range on page |
|---|---|---|---|
| James | 23 Dec 1863 | **87** | Nov 1863 to Mar 1864 |
| Honora | **24 March 1866** (baptized; born ~22–24 Mar, civil-reg 25 Mar. Superseded: "10 Mar" Gemini draft + "24 Feb" image month-misread) | **93** | Jan 1866 to May 1866 |
| Bridget | Feb 1868 | **98** | Jan 1868 to May 1868 |
| Ellen | 9 Jul 1869 | **102** | May 1869 to Dec 1869 |
| Mary | 18 Dec 1872 | **109** | Aug 1872 to Jan 1873 |
| Margaret | 29 Sep 1875 | **115** | July 1875 to Jan 1876 |
| Jane | Sep 1878 | **120** or **121** | Feb 1878 to Aug 1878 / Aug 1878 to Mar 1879 |

### Ella pre-1863 search window (calibrated ~1854–1858)

| Year | Pages |
|---|---|
| 1854 | 49–52 |
| 1855 | 52–55 |
| 1856 | 56–60 |
| 1857 | 61–65 |
| 1858 | 66–69 |

### Patrick + Margaret marriage search (~1855)

Marriages are on the same microfilm but later pages:

| Year window | Pages |
|---|---|
| Jul 1854–Feb 1855 | 138 |
| Feb 1855–Jan 1856 | 139 |
| Feb 1856–Jun 1856 | 140 |
| May 1862–Oct 1864 | 153 (where the Bridget Gleeson 1864 marriage lives) |

---

## Reproducible URL construction (in shell)

```bash
# For a given VTLS ID and page number, print the image URL:
vtls_id="000634977"  # Croom baptisms 02427/07
page=87              # James's baptism

vtls_num=$(echo "$vtls_id" | sed 's/^0*//')
parent_num=$(( vtls_num - vtls_num % 10000 + 10000 ))
parent_dir=$(printf "%09d" "$parent_num")
page_padded=$(printf "%03d" "$page")
filename="vtls${vtls_id}_${page_padded}.jp2"

echo "https://iserver.nli.ie/fcgi-bin/iipsrv.fcgi?FIF=${parent_dir}/${vtls_id}/${filename}&CVT=JPG"
```

---

## Implications

- **Every Croom Gleeson baptism, marriage, and death image** is fetchable for free, on demand, without auth.
- **Same trick works for every other Irish Catholic parish** — just look up the parish ID and the VTLS IDs for its microfilms.
- **Combined with LLM-based Latin transcription**, this enables systematic sweeps: "every Gleeson in Croom register 1844–1881" becomes a script + LLM run, not a multi-day Ancestry click-through.
- **Other parishes we may want to sweep next:** Fedamore (Catharina Gleeson lead), Croom's neighbors for the marriage record search (Kilfinane, Bruff, Athlacca, Knockainey, Adare), and Limerick City St Michael's (the wrong-family Pat Gleeson — to confirm the disambiguation).

## Cited code & data

- Image URL construction logic: `/assets/registers-*.js` on registers.nli.ie (`BookReader.prototype.getPageURI` and `getParentDir`).
- Page metadata: `gon.pages_metadata` injected into register viewer pages.
- Page list JSON: `/diva/php/divaserve.php?d={vtls_num}`.

## Related files

- `assets/external/nli-croom/` — downloaded Croom register page images
- `research/results/gleeson-croom-family.md` — Croom Gleeson family data we've extracted
- `research/results/gleeson-croom-marriages-review.md` — earlier (un-imaged) marriage review

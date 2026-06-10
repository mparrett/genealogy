# Browser-Claude Handoff: Margaret Moloney/Gleeson — NLI register sweep + 1911 census verify

**Date:** 2026-06-09
**For:** a Claude with live browser / image-fetch access
**Source of leads:** ChatGPT web pass (2026-06-09) confirmed the NLI microfilm coverage but could not read the register images. Your job is to read them.

## Mission (in priority order)

1. **Find the marriage of Patrick Gleeson × Margaret Moloney, c. 1860–1861** (the single highest-value missing record — it names both fathers and gives both ages, locking Margaret's natal family).
2. **Verify the 1911 census household of John Kelly at Ballymackeamore** to resolve whether Kate Moloney is Margaret's *sister* or *niece* (a generational question that affects how much weight the natal-family ID carries).
3. (opportunistic) **Margaret Gleeson's death**, Croom SRD, 1918–1930.

## The couple (matching key)

- **Groom:** Patrick Gleeson, Farmer, of **Scagh townland, Croom, Co. Limerick**; born **Hospital parish, Co. Limerick** (~1833–1837) to James Gleeson + Honora O'Brien.
- **Bride:** Margaret **Moloney** (Molony/Moloney; Latin *Margarita Molony/Moloney*), b. ~1836, probably of **Croagh/Kilfinny parish**, daughter of **James Molony + Catherine Kenny** (this is the hypothesis the marriage record would confirm).
- **Date logic:** firstborn **Catherine baptized 31 Jan 1862 at Croom** → marriage ~mid-1860 to mid-1861. Second child James baptized 23 Dec 1863. Search window **1856–1862**, bullseye **1860–1861**.
- **Latin form to scan for:** *Patritius/Patricius Gleeson* + *Margarita Molony/Moloney*. Witnesses ("Coram"/"Testes") are often siblings — a **Molony** or **Gleeson** witness is corroborating.

---

## TASK 1 — Croagh/Kilfinny marriage register (TOP PRIORITY)

NLI parish **0880** (Croagh; "Kilfinny" redirects here). Marriage register = microfilm **02420/06 = vtls000634972** (Marriages 1844–1881, 28 images).

**Page → date map for the search window** (extracted from `gon.pages_metadata`):

| Page | Date range | Priority |
|---|---|---|
| 9  | June 1854 – Jan 1856 | tail |
| 10 | Jan 1856 – Feb 1857 | search |
| 11 | Feb 1857 – Feb 1858 | search |
| 12 | Feb 1858 – Jan 1859 | search |
| 13 | Jan 1859 – Mar 1859 | search |
| **14** | **May 1859 – Nov 1860** | **BULLSEYE** |
| **15** | **Nov 1860 – Jan 1862** | **BULLSEYE** |
| 16 | Feb 1862 – Feb 1863 | tail |

**Start with pages 14 and 15**, then widen to 10–16 if no hit.

- Viewer (visual browsing): `https://registers.nli.ie/registers/vtls000634972#page/15/mode/1up` (change `/15/` to any page)
- High-res JPEG (for zooming faded entries): `https://iserver.nli.ie/fcgi-bin/iipsrv.fcgi?FIF=000640000/000634972/vtls000634972_015.jp2&CVT=JPG` (change `_015` to `_0NN`) — **verified HTTP 200, ~242 KB JPEG.**

---

## TASK 2 — Hospital marriage register (FALLBACK — groom's natal parish)

NLI parish **0268** (Hospital; variant Hospital & Herbertstown, Cashel & Emly). Marriages are in microfilm **02507/04 = vtls000632731**. NOTE: pages 5–70 are **baptisms**; the **marriage section restarts at page 71**.

| Page | Date range | Priority |
|---|---|---|
| 78 | Nov 1853 – Apr 1856 | tail |
| 79 | June 1856 – July 1858 | search |
| 80 | Aug 1858 – July 1860 | search |
| **81** | **July 1860 – Jan 1862** | **BULLSEYE** |
| 82 | Jan 1862 – Sep 1864 | tail |

- Viewer: `https://registers.nli.ie/registers/vtls000632731#page/81/mode/1up`
- High-res JPEG: `https://iserver.nli.ie/fcgi-bin/iipsrv.fcgi?FIF=000640000/000632731/vtls000632731_081.jp2&CVT=JPG` — **verified HTTP 200, ~282 KB JPEG.**

---

## TASK 3 — Re-grab the shadowed Croom marriage page

Croom parish **0881**, microfilm **02427/07 = vtls000634977**. **Page 151's left column (≈ Aug 1861 – early Feb 1862)** was obscured by a shadow in our earlier scan — exactly overlapping the most likely marriage date. Try a fresh/zoomed grab; also glance at pages 150 and 152.

- Viewer: `https://registers.nli.ie/registers/vtls000634977#page/151/mode/1up`
- High-res JPEG: `https://iserver.nli.ie/fcgi-bin/iipsrv.fcgi?FIF=000640000/000634977/vtls000634977_151.jp2&CVT=JPG` — **verified HTTP 200, ~166 KB JPEG.** (Request a larger render with `&WID=4000` if the shadow obscures text.)

---

## TASK 4 — 1911 census: John Kelly, Ballymackeamore (RESOLVE THE KATE QUESTION)

Site: **census.nationalarchives.ie** (free). Find: **John Kelly**, House 8 (or nearby), **Ballymackeamore townland, Kilfinny civil parish, Co. Limerick**, census night 2 Apr 1911. ChatGPT's index snippet showed: John Kelly 45 (head), Kate Kelly 32 (wife), Nora Kelly 15 (daughter) — but that may be partial.

**Pull the full household form and record verbatim:**
- Kate's **exact stated age**, and her entry in the **"Years Married"** and **"Children born alive / still living"** columns (the 1911 form has these).
- **Every household member** with age + relationship (we expect Ellen, b. 3 Mar 1905, age ~6 — confirm she's present).
- Townland/DED exactly as written.

**Why it matters:** our recent (2026-06-08) work promoted Margaret's natal-family ID partly by treating **Kate Moloney as Margaret's sister** (→ Kate's daughter Ellen = Helen J. Ryan = Catherine Hayes's *first cousin*). But Kate bearing a child in 1905 implies she was born ~1865–1879 — a full generation after Margaret (b.1836), so **Kate is more likely Margaret's niece, and Helen a first-cousin-once-removed** (still consistent with the loose "cousin" on Catherine's 1944 estate). The census's years-married/children columns will tell us Kate's true age and family structure. Also look for nearby **Moloney / Molony** households in the same DED (Jeremiah; Griffith's puts Michael Moloney + John Kelly in this exact townland).

---

## TASK 5 — (opportunistic) Margaret's death

irishgenealogy.ie civil **death** index/images, **Margaret Gleeson** (married name — NOT Moloney), **1918–1930**, **Croom SRD** first (then Rathkeale, Limerick, Newcastle West). Accept only with Croom / Main Street / family-informant context. Also check **Find-A-Grave / HistoricGraves** for a Croom or Manister burial with Patrick. (Already rejected: HistoricGraves Margaret Gleeson d. 7 Nov 1942 **Doon** — wrong place/family.)

---

## NLI image-fetch mechanics (to reach any other page)

Image URL = `https://iserver.nli.ie/fcgi-bin/iipsrv.fcgi?FIF={parent_dir}/{vtls}/{vtls}_{page3}.jp2&CVT=JPG`
- `{vtls}` e.g. `vtls000634972`; `{page3}` = zero-padded page, e.g. `015`.
- `{parent_dir}` = `floor(vtls_num/10000)*10000 + 10000`, padded to 9 digits. For all three registers here (634972, 632731, 634977) it is **000640000**.
- Page→date map: `curl -s "https://registers.nli.ie/registers/{vtls}" | grep -oE 'pages_metadata=[^;]+'`
- Add `&WID=4000` (max ~4900) for high-res when handwriting is faint.
- Full pipeline doc: `research/analysis/nli-parish-register-pipeline.md`.

## Cautions

- **These are handwritten Latin registers.** Transcribe entries verbatim; give your confidence per field. **Do NOT invent priest/place/surnames on faded or shadowed scans** — that's a known failure mode here (see memory `gemini-hallucinates-shadowed-scans`). If illegible, say so and grab a higher-res render.
- **Cross-check the date printed/written on the page against the page→date map** before trusting a page number (rare off-by-one between viewer index and file index).
- **A hit must meet the acceptance criteria:** Co. Limerick, the right couple, 1856–62. Record verbatim: date, parish, both spouses, both fathers (if given), ages, and witnesses.

## Output

For each task: **what you found verbatim + source URL**, or a one-line "swept Croagh marriages pp.10–16, no Gleeson×Molony — no match." Flag any entry that names **Margaret's father** — that's the lock.

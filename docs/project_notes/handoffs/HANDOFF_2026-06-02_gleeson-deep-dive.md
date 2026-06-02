# Session Handoff

**Created:** 2026-06-02
**Session ID:** 26fff187-700b-4f4e-a2cb-8217192cd257
**Working Directory:** /Users/matt/projects-new/genealogy

## What to read first

This was a multi-day deep dive on the **Patrick Gleeson + Margaret Moloney line (Croom, Co. Limerick)** centered on three high-leverage developments:

1. **The NLI Catholic Parish Register image pipeline** is now cracked open and scriptable — see `research/analysis/nli-parish-register-pipeline.md` and `scripts/nli_fetch_hires.sh`. Any Irish Catholic parish register page can be fetched as a hi-res JPEG without auth.
2. **Ella Isabel Gleason was WITHDRAWN as Patrick's daughter** — the 1874 Eau Claire marriage was traced to a different Gleason family (C. R. Gleason, not Patrick). Cascading recalibration of marriage dates, parents' birth years, and the chain-migration story. See memory `gleeson-ella-isabel-false-lead` — **reject if it resurfaces**.
3. **Patrick documented as a FARMER at Scagh by 1859** — first non-parish primary record. Two Petty Sessions appearances (1859 + 1864) at NAI CSPS series. See memory `gleeson-patrick-petty-sessions`.

The current open thread is **Patrick + Margaret's marriage record** — Croom register exhaustively swept for the calibrated window with one critical gap: page 151's left column remains unreadable due to a shadow.

## Summary

Started by folding in research drops about James Gleeson's 1946 obituary, James + Maria's 1892 marriage record, and the Ella Isabel "Mrs. John Hayes" hypothesis. Built increasingly sophisticated repository state, then **discovered the NLI register pipeline** mid-session — which let us scriptably fetch hi-res page images, then run them through Gemini for Latin transcription, then back into the bio/fact sheet. Page-by-page sweep of Croom marriages from May 1853 through Feb 1858 came up empty, then we recalibrated.

Then the **Ella collapse**: ChatGPT independently checked the 1874 Eau Claire marriage image and found the bride's father was C. R. Gleason (not Patrick), with the groom John Nelson Hayes having a documented later life in Dunn County WI with Antoinette Ring. We withdrew Ella entirely, redid the calibration math with James as earliest documented child, and shifted the marriage window to ~1860–1863.

Then **Petty Sessions discoveries**: two NAI court entries documenting Patrick as a Farmer at Scagh (1859 + 1864). Locked in occupation, refined Croom residence anchor.

Then **second-wave marriage page sweep** (148–152) covering the new calibrated window. Page 152 is clean — but page 151's left column remains obscured, and pages 151 and 152 turned out to be parallel sub-parish registers (different priests). So the Croom marriage hasn't actually been ruled out — it could be on page 151's still-unreadable section.

## Current State

- Branch: `main`, **57 commits ahead of origin** (not pushed)
- Working tree clean
- 18 new commits this session covering Gleeson work
- Session commits (oldest → newest, Gleeson only):

```
22a0f12  Lock Margaret Moloney spelling + add Ella Hayes (=Mrs. John Hayes NY)
52ed8db  Track Margaret Moloney candidate records + add Ellen/James citations
ec9c6c8  Calibrate Patrick + Margaret birth years using Irish post-Famine norms
d0e7ac2  Disentangle Limerick City Pat Gleeson from our Croom Patrick
02a9d94  Record James + Maria 1892 marriage record in Patrick Gleeson fact sheet
3226930  Fold James Gleeson 1946 obituary findings into Patrick research
7be4678  Downgrade Michael Gleeson (Patrick's father) to unverified hypothesis
458a802  Refine Ellen 1869 baptism from manuscript re-read
1093dec  Add Margaret 1875 baptism data + retire Francis Dunlan + sponsor leads
a426a63  Mary 1872 baptism corrections + new Croom Gleeson/Moloney leads
4b266e2  Crack open NLI parish register pipeline + targeted Croom fetches  ⭐
09a8b02  Upgrade Croom register pages to ~1.5x resolution via IIP tile assembly
bb537d8  Resolve James 1863 sponsor as William Storan + add Phase 1 marriage pages
5c994d7  Correct James Gleeson obit source: St. Cloud Times (not Leader-Telegram)
3b6eb40  Withdraw Ella Isabel Gleason as Patrick's daughter — false attribution  ⭐
021123e  Add first non-parish primary record for Patrick: 1864 Petty Sessions
bf02cd2  Add 1859 Petty Sessions: Patrick documented as Farmer at Scagh  ⭐
7d9b3ea  Fold page 152 marriage register findings + correct search scope
```

New / updated / withdrawn memories:
- New: `gleeson-moloney-not-maloney` — surname locked
- New: `gleeson-ella-hayes-finding` — initially active, **later WITHDRAWN**
- New: `gleeson-ella-staten-island` — initially active, **later WITHDRAWN**
- New: `gleeson-ella-isabel-false-lead` — the post-withdrawal guard rail
- New: `gleeson-storan-sponsor` — William Storan = James's 1863 male sponsor (Croom-rooted family)
- New: `research-hygiene-check-prompts` — pattern flag for old prompt-file contamination
- New: `gleeson-patrick-petty-sessions` — 1859 + 1864 NAI court entries
- New: `gleeson-patrick-1864-petty-sessions` — renamed/superseded by above

## Key Findings (high-confidence, locked in)

### Patrick is a Farmer

- **Occupation: Farmer** (per 1859 Petty Sessions, NAI CSPS1/8381)
- Previously held "sailor" attribution was wrong-family contamination (Limerick City Pat Gleeson at The Windmill)

### Patrick was at Scagh by 1859

- 11 Sept 1859 documented in NAI court records — **4 years before James's 1863 baptism**
- Confirms long-term Croom residence anchor independent of parish records

### The 7 documented children — all corroborated with hi-res manuscripts

| # | Name | Date | Sponsors | Notes |
|---|------|------|----------|-------|
| 1 | James | 23 Dec 1863 | **William Storan + Margaret Kiely** | Storan is a distinctively Croom-rooted surname |
| 2 | Honora | 24 Feb 1866 | Thomas Shea + Ellena Moloney | Date corrected from index "10 Mar" |
| 3 | Bridget | 24 Feb 1868 | Jacob Moloney + Ellena Gleeson | "Cleary" reading on father needs verification |
| 4 | Ellen | 9 Jul 1869 | Jeremiah O'Leary + Bridget Shanahan | Date corrected from index "15 Jul" |
| 5 | Mary | 18 Dec 1872 | John + Ellen O'Shaughnessy | Date corrected from index "15 Dec" |
| 6 | Margaret | 29 Sep 1875 | William Blake + Ellen Condon | |
| 7 | Jane | 28 Sep 1878 | Michael Moloney + Maria Quaid | |

Officiant for all: **Rev. John (Joannes) Quinlan** at Croom (C.C., later P.P.).

### Withdrawn: Ella Isabel Gleason

- Previous "8th child" (the 1874 Eau Claire bride) is **NOT** our family
- 1874 marriage record's bride's father = **C. R. Gleason**, not Patrick
- Groom John Nelson Hayes was b. Venice NY, son of Henry + Elmira Hayes, later partnered with Antoinette Ring in Dunn County WI
- Memory `gleeson-ella-isabel-false-lead` is the guard rail

### Recalibrated parent ages

- **Patrick: c. 1832 (range 1830–1834)**
- **Margaret: c. 1836 (range 1834–1838)**
- **Marriage: c. 1862** (anchored on James 1863 as earliest documented)
- See `research/analysis/gleeson-parents-age-calibration.md` for full revision history

### Irish naming pattern analysis predicts Patrick's parents

- **Patrick's father = James Gleeson** (1st-son rule applied to James 1863)
- **Patrick's mother = Bridget [maiden unknown]** (2nd-daughter rule applied to Bridget 1868)
- **Margaret Moloney's mother = Honora** (1st-daughter rule applied to Honora 1866)
- See `research/analysis/gleeson-irish-naming-pattern.md`
- **Reinforces** the existing hypothesis that the 1864 Bridget Gleeson + Thomas Shea marriage = Patrick's sister (a sister named for the mother is exactly what the 2nd-daughter rule produces)

### Extended-family network (hypotheses with documentary support)

- **Bridget Gleeson + Thomas Shea** married Croom 27 Aug 1864 = **likely Patrick's sister**
- **Michael Moloney + Bridget Martin** married Croom 10 Aug 1861 = **likely Margaret's brother**
- **Ellena Moloney** appears as witness/sponsor at multiple family events = **likely Margaret's sister**; later married Patrick Lynch (per page 120 transcription)
- **Patrick Moloney + Mary McNamara** (Croom 1864) = possible Margaret brother
- **John Moloney + Johanna Moylan** (Croom 1872) = possible Margaret brother
- **Jacob Moloney** = frequent sponsor, possible brother
- Multiple Gleeson candidates as Patrick's siblings: **John Gleeson + Honora Walsh** (married Croom 1855), **Timothy Gleeson** (1864 sponsor), **Jacob Gleeson** (1864 witness), **Catharina Gleeson** (Fedamore, 1872), **Anna Gleeson** (1878), possibly **Stephen Gleeson** (married Croom 1862)

### Four disambiguation fingerprints (NOT our family)

| Fingerprint | Wife/marker | Where |
|---|---|---|
| Australian Patrick | Margaret **Mahony** b. Bantry Cork; married 1862 Victoria | Australia |
| Limerick City Pat | Mary **Mahony**; "The Windmill, St Michael's" | Limerick City |
| Ohio Patrick | Margaret Moloney too old | Ohio |
| Eau Claire 1874 | C. R. Gleason father; John Nelson Hayes b. NY | Eau Claire WI |

## Uncommitted State / Untouched

**Uncommitted:** none. Working tree clean.

**Untouched (deliberate):**
- Did NOT pursue the 1901 Killaloe Patrick candidate beyond writing `patrick-gleeson-killaloe-1901-candidate.md` — needs decisive 1901 Croom census check
- Did NOT touch Mowery, Higgins, Kuthe, Parrett, Fitzgerald bio details — Gleeson-only session
- Did NOT push 57 commits to origin (consistent with user's pattern)
- Did NOT investigate the FamilySearch-indexed 4 July 1883 Patrick Gleeson record (content blocked — needs NAI lookup)
- Did NOT sweep additional NAI Petty Sessions for Patrick (only have 1859 + 1864; likely more exist)
- Did NOT pull Honora's death record or any post-1878 record for the children other than the obit-named ones

## Gotchas

- **Page 151 left column is the prime suspect** for Patrick + Margaret's marriage. It covers Aug 1861 – early Feb 1862 in a sub-parish register that uses Scanlan/Roche as officiants. Hi-res fetch (JTL=4) was already done; the shadow appears to be in the original manuscript or the microfilm itself, not a resolution artifact. **Next attempts should be JTL=5 (max 4656 wide), or alternate sources (FamilySearch / Ancestry scans of the same microfilm) which may have different lighting.**
- **Pages 151 and 152 are parallel registers from different sub-parishes** (different priest signatures despite overlapping dates). So page 152 being clean does NOT eliminate the marriage from page 151's obscured section. The "Croom register" actually contains parallel sub-parish records.
- **Quinlan title puzzle:** Quinlan signs as **P.P.** on page 152 (Nov 1861) but as **C.C.** on page 87 (Dec 1863 for James's baptism). Resolution hypothesis: he was **P.P. of Patrickswell** simultaneously with being **C.C. of Croom** (adjacent parishes). Worth verifying with diocese records.
- **"Sean" vs "Scaugh" vs "Scagh"** all refer to the same townland — confirmed by same justice + court + charge pattern across 1859 and 1864.
- **Honora's 1866 baptism father reading**: Gemini transcribed as "Patritii Leeson (?)" — almost certainly "Gleeson" but worth verifying against the manuscript image (we have it at `assets/external/nli-croom/page_093_honora_1866_baptism.jpg`).
- **Bridget's 1868 baptism father reading**: Gemini transcribed as "Patricii **Cleary** et Margaritae Moloney" — needs visual verification. If it's actually "Gleeson," that's our Bridget with sponsors Jacob Moloney + Ellena Gleeson. If it's truly "Cleary," our Bridget's entry is missing from page 98.
- **"Mrs. John Hayes" of Staten Island** in James's 1946 obit is a REAL person (real surviving sister) but her identity is unknown after the Ella withdrawal. Could be Honora, Ellen, Margaret, or Jane (any of the 4 unmarried-at-our-knowledge daughters) OR an older undocumented sister. The "John Nelson" middle name has zero independent attestation — only appears in the (withdrawn) 1874 record.
- **The "Rev. ? Gleeson" Croom curate 1856–1857** is a possible kinsman of Patrick — initial reading varies (T/S/L/D/J). A Gleeson priest at Croom during the likely-marriage window. Worth searching diocese records for his full name.
- **FamilySearch's 4 July 1883 Patrick Gleeson** — indexed but content blocked from public view. Worth pulling at the NAI directly.

## Next Steps

In rough order of leverage:

1. **Crack page 151's left column.** Try JTL=5 fetch (~4656 wide, 285 tiles, slower). If still obscured, try FamilySearch's scan of the same microfilm (different lighting, may not have the shadow). If still blocked, sweep neighboring parishes (Patrickswell first — Quinlan was P.P. there). The marriage is the single biggest unanswered question.
2. **Verify the 1901 Croom census** — Test 1 from `research/analysis/patrick-gleeson-killaloe-1901-candidate.md`. If Patrick is alive and in Croom in 1901, the Killaloe candidate is eliminated. If not, we have a death/migration window to characterize.
3. **Identify Mrs. John Hayes of Staten Island** — search 1940 census Richmond Co. NY for any Irish-born Hayes/Hays female sister-aged to James (b. ~1863). Drop the "Ella Isabel" filter. Then chain back to 1930/1920 censuses for parents' birthplaces.
4. **Pull the 4 July 1883 record** at NAI — FamilySearch indexed it but content is missing.
5. **Petty Sessions sweep** — Patrick had 1859 + 1864 appearances. CSPS series is well-indexed; likely more Patrick or extended-family entries available.
6. **Verify the "Cleary"/"Gleeson" reading** on Bridget's 1868 baptism — could be our missing Bridget entry or could be a different family. Image at `assets/external/nli-croom/page_098_bridget_1868_baptism.jpg`.
7. **Sweep pages 148–150 transcriptions** (we fetched them but didn't run them all through Gemini in detail; verify no Patrick + Margaret marriage there for Oct 1859 – Jul 1861).
8. **Search the Croom register for Patrick's own baptism** (~1830–1834) — filter for "Patrick, son of James Gleeson + Bridget [any]". Also Margaret's baptism (~1834–1838) — filter for "Margaret, daughter of [any] Moloney + Honora".
9. **Diocese records for Croom 1856–57** — identify the "Rev. ? Gleeson" curate who was active at Croom during Patrick's likely marriage window.
10. **Push 57 commits to origin** when convenient.

## Open Tickets

None.

## Tools available

- `scripts/nli_fetch.sh` — single-page low-res NLI fetch
- `scripts/nli_fetch_hires.sh` — hi-res via IIP tile assembly (zoom configurable)
- Page metadata extraction from NLI viewer's gon.pages_metadata JS variable
- Full pipeline documented at `research/analysis/nli-parish-register-pipeline.md`

## Critical reference files

- `research/findings/patrick-gleeson/facts.md` — main research summary
- `research/reports/patrick_gleeson_bio.md` — narrative bio
- `research/summaries/gleeson.md` — full Gleeson line summary
- `research/analysis/gleeson-parents-age-calibration.md` — birth year math
- `research/analysis/gleeson-irish-naming-pattern.md` — naming pattern predictions
- `research/analysis/gleeson-three-family-confusion.md` — Australian + Limerick City + Ohio disambiguation
- `research/analysis/patrick-gleeson-killaloe-1901-candidate.md` — Test 1 / Test 2 candidate evaluation
- `research/analysis/nli-parish-register-pipeline.md` — pipeline documentation
- `assets/external/nli-croom/` — 18 hi-res Croom register page images + Gemini transcriptions
- `assets/external/james-gleeson-obit-minnesota-1946.jpg` — primary obituary source

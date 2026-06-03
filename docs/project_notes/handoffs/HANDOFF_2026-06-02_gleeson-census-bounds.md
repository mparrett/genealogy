# Session Handoff

**Created:** 2026-06-02T22:30:00-07:00
**Session ID:** 876455d1-6268-4dba-94f4-2a731eef4f63
**Working Directory:** /Users/matt/projects-new/genealogy

## What to read first

This was a Gleeson research deep-dive that produced **major calibration revisions** to the Patrick + Margaret family model. Three load-bearing changes the next session needs to know: (1) **Margaret's birth year is now c. 1845, not c. 1836** (9-yr revision from 1901+1911 Census ages); (2) **Patrick is dead by 31 March 1901**, collapsing the death window from "1869–1918" to "1883–1901"; (3) **The Gleeson family geography is tri-county** (Limerick + Tipperary + Cork) per WI-side oral history from Robert Gleeson — Cork records should no longer be blanket-rejected.

`research/findings/patrick-gleeson/facts.md` was updated extensively. Read its "Documented life events" table and "What we don't know" sections first.

## Summary

The session began as a continuation of the marriage hunt from the previous handoff, but pivoted dramatically when the user surfaced two transformative external documents: the **1918 Registry of Deeds memorial** (Jeremiah Molony of Ballymackeamore releasing a mortgage to widow Margaret Gleeson) and the **1901 + 1911 Censuses** (Margaret at Main Street Croom as widow shop-keeper with two daughters). Combined with a programmatic Calendar of Wills search, civil-death record reviews, and Robert Gleeson's WI-side family lore, the session collapsed Patrick's death window from 49 years to ≤18 years, revised Margaret's birth year by 9 years, surfaced 2 likely additional daughters, and reframed the family geography across three counties. The marriage hunt itself made no direct progress, but multiple high-leverage next moves were unlocked.

## Current State

- Branch: `main`, **72 commits ahead of origin** (still unpushed, matches user's pattern)
- Working tree: clean
- Session commits (this session only, 14 total since previous handoff archived as `8f35699`):

```
31ae972  Track gleeson-marriage-web prompt + results
c87649b  Add 1901 + 1911 Census of Ireland records for Margaret Gleeson household  ⭐
6b04ced  Add Robert Gleeson tri-county family lore (Limerick + Tipperary + Cork)   ⭐
3830228  Add Ballinhassig Cork Patrick Gleeson 1914 as wrong-family fingerprint
512f764  Add Moigh Caherconlish Patrick Gleeson 1911 as wrong-family fingerprint
74a31ef  Record 1869 Petty Sessions dog-license entry for Patrick at Scagh        ⭐
76be237  Record NAI Calendar of Wills negative search for Patrick + Margaret
3197cf8  Add 1918 Registry of Deeds memorial: Molony to Gleeson                    ⭐
8d381b2  Sweep Croom baptism pages 70-108 testing missing-children hypotheses
f6b352c  Add Lurriga marriage transcriptions 095, 096
41324a1  Add Lurriga parish register pages 95-96 for O'Rorke's Patrickswell
b607610  Add Knockany & Patrickswell parish register sweep for 1861-1862
0f3ac55  Quarantine discarded Croom page 151 transcription attempts
7dd9081  Add Croom marriage register transcriptions for 1859-1862 sweep
```

Memory additions:
- `gemini_hallucinates_shadowed_scans.md` (feedback) — pattern guard for future register-page work
- `gleeson_tri_county_family_lore.md` (project) — Robert's WI-side oral history confirming Limerick/Tipperary/Cork family geography

## Uncommitted State / Untouched

**Uncommitted:** none. Working tree clean.

**Untouched (deliberate):**
- Did NOT push 72 commits to origin (consistent with user's pattern)
- Did NOT investigate Mowery / Higgins / Kuthe / Parrett lines — Gleeson-only session
- Did NOT sweep Croom baptism pages 122–135 (~Mar 1879 – ~1886) — these contain the likely baptisms of the two undocumented daughters Mary and Bridget, which would prove Patrick was alive 1882-83. Top open Croom-side task.
- Did NOT search civil deaths under variant spellings (Gleason / Glissan) for Patrick 1883–1901 — high-leverage variant-spelling sweep still untried
- Did NOT pull the 13 June 1911 antecedent mortgage from Registry of Deeds — would tighten the Patrick death window further if Patrick co-signed
- Did NOT fetch the Kilfinny parish marriage register from NLI — top remaining marriage-hunt lead

## In Progress

None — all session work either committed or deliberately deferred. Three open task-list tasks are pending (look-ups for next session, low priority).

## Gotchas

- **Margaret's c. 1836 birth year calibration is WITHDRAWN.** Both 1901 (age 55) and 1911 (age 66) Censuses point to c. 1845. Older `gleeson-parents-age-calibration.md` analysis is now stale — do not cite it.
- **Patrick + Margaret had at least 9 children, not 7.** The 1901 Census Main Street Croom household has Mary (24) and Bridget (18) as daughters — too young to be the documented Mary 1872 and Bridget 1868. These are likely **NEW children born ~1877–1886** that we haven't found in baptism records. The Croom baptism sweep stopped at page 121 (Aug 1878 – Mar 1879). Pages 122–135 are unfetched.
- **The Workhouse at Skagh complicates the residence story.** In 1901, "Mary Gleeson" age 27 at "Skagh, Croom, House 4.1" is NOT at Patrick's farm — that address is the **Croom Union Workhouse**, where Mary is the Matron (staff). Skagh townland contained both Patrick's farm (where he lived 1859–1869) and the Workhouse. Patrick Carroll (the unrelated Master of Workhouse with wife Margaret Carroll) is a name-coincidence trap to avoid.
- **The 1911 Census signature is gold.** Margaret signed Form A herself — proof of literacy, mental competence, and her actual identity. The enumerator John Bourke missed filling columns 10–12 (years married / children born / children living) — would have given us a definitive child count.
- **Pages 151 and 152 of the Croom marriage register are the SAME physical page** (re-scan, with operator shadow on 151). The previous handoff's "parallel sub-parish registers" theory was wrong. Five Gemini transcription passes on the bad 151 scan produced internally-coherent but hallucinated priest names (J. Walsh, J. Bourke, James Scanlan, J. J. White, J. O'Meara) — see the `gemini-hallucinates-shadowed-scans` memory and `discarded-151-attempts/` subdir.
- **Cork records should NOT be blanket-rejected.** Robert Gleeson (WI-side cousin, 2nd cousin once removed to Matt) confirmed family memory of relatives in Tipperary + Cork. The Ballinhassig 1914 Patrick Gleeson is *not our Patrick* (widower in 1914 disqualifies — Margaret alive 1918), but he or his second-cousin informant John Gleeson of Hill Terrace Bandon may be Patrick's cousins. Same applies to the Tipperary Patrick Gleeson death-calendar hits.
- **Civil registration variant-spelling traps.** Our Patrick is absent from indexed civil deaths in Co. Limerick 1864–1918 (four candidates, all wrong-family). Variant spellings (Gleason / Glissan / Glesson) or alternate given name (Pat / Patk) plausibly explain the gap.
- **The Calendar of Wills 1858–1922 has no Patrick or Margaret.** Patrick likely died intestate; Margaret likely died post-1922 when the 26-county calendar ends. Don't re-search the Calendar.

## Next Steps

In rough order of leverage:

1. **Sweep Croom baptism pages 122–135** (~Mar 1879 – ~1886). NLI pipeline already validated, fetch script in handoff `2026-06-02_gleeson-deep-dive`. If the two undocumented daughters (Mary ~1880, Bridget ~1883) appear there, Patrick is proven alive 1882–83 and the death window tightens to 1883–1901.
2. **Sweep Kilfinny parish marriage register** for ~1860–1862 via NLI pipeline. This is the top remaining marriage-hunt lead — Jeremiah Molony of Ballymackeamore lived in Kilfinny parish per the Co. Limerick townland index, and the cross-parish marriage practice we documented in 1860s Croom registers means the marriage is most likely in Margaret's natal parish.
3. **Civil death sweep for "Pat" or "Patk" Gleeson, Co. Limerick, 1883–1901** + variant surname "Gleason" same window. If Patrick was registered under a variant, this surfaces him.
4. **Pull the 13 June 1911 antecedent mortgage** from the Irish Registry of Deeds. Confirms or denies whether Patrick was a co-signatory (he probably wasn't, given the 1901 widow status — but worth verifying). The 1911 deed is the bridge document between the 1901 Census and the 1918 release.
5. **Civil birth records for the 7+ documented children** at irishgenealogy.ie (free, post-1864). Each record names mother as "Margaret Gleeson formerly Molony" + townland + Patrick's occupation. Multiple records corroborate identity and may reveal Patrick's birthplace field if civil reg captured it.
6. **Sweep Tipperary border-parish marriage registers** for ~1860 Patrick Gleeson + Margaret Moloney. Robert's tri-county lore opens this — Cappamore, Doon, Hospital, Galbally, Pallasgreen.
7. **Identify Mrs. John Hayes of Staten Island** — 1940 Staten Island census for an Irish-born female Hayes sister-aged to James (b. 1863). The earlier "Ella Isabel" identification is withdrawn; we still don't know which of Honora/Ellen/the new Mary/the new Bridget she is, OR if she's the older sister whose baptism would be in Tipperary or Cork.
8. **Optional: re-contact Robert Gleeson** for fragmentary Cork detail. Even one specific Cork town name or surname mentioned in family visits would shortcut months of register sweeping. Matt has the iMessage thread; light contact pattern, only ask if needed.
9. **Push 72 commits to origin** when convenient.

## Open Tickets

None in `docs/project_incoming/`. Three pending tasks in this session's task list (Calendar of Wills search, Patrickswell parish lookup, etc.) are all completed-or-superseded; they can be ignored.

## Tools available (validated this session)

- `census.nationalarchives.ie` — GET-form endpoint for 1901/1911 census search. Form params: `surname`, `firstname`, `census_year`, `county19011911`, `ded`, `townland`, `parish`, `search=Search`. Household pages at `/pages/<year>/<county>/<DED>/<townland>/<id>/`. Form A PDF images via `/reels/nai<reel_id>/` (returns PDF directly, Content-Type application/pdf).
- `willcalendars.nationalarchives.ie` — GET-form endpoint for Calendar of Wills 1858–1922 (already documented in `research/results/gleeson-calendar-of-wills-search.md`).
- NLI parish register pipeline — `scripts/nli_fetch_hires.sh` + manual curl. Documented in `research/analysis/nli-parish-register-pipeline.md`.

## Critical reference files

- `research/findings/patrick-gleeson/facts.md` — main source of truth, extensively updated this session
- `research/results/gleeson-calendar-of-wills-search.md` — full Calendar of Wills methodology + negative results
- `assets/external/census/` — 4 PDF scans of 1901 + 1911 Census Form A returns
- `assets/external/willcalendars/` — 3 PDF scans of Calendar of Wills pages with wrong-family Patrick Gleesons
- `assets/external/transcripts-memories-gleeson-molony-1918*.md` — 3 independent transcriptions of the 1918 Registry of Deeds memorial #29
- `assets/external/petty-sessions-1869-04-26-croom.md` — 1869 Petty Sessions dog-license entry
- `assets/external/nli-croom/discarded-151-attempts/` — 5 known-hallucinated Gemini transcriptions, preserved as historical record

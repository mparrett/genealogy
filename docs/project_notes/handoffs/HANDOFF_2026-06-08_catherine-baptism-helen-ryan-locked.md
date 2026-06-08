# Session Handoff

**Created:** 2026-06-08T15:34:50-07:00
**Session ID:** 3d8657d1-6dda-4a11-9701-b4780d03b287
**Working Directory:** /Users/matt/projects-new/genealogy

## What to read first

Massive Gleeson/Moloney lock-in session — two full Patrick/Margaret-line breakthroughs (Catherine 1862 baptism + Helen Ryan = Ellen Kelly identification) plus six other substantial finds. The natal-family chain on Margaret's side jumped from T2 to T1.5 via the Ballymackeamore cousin link. **Patrick × Margaret marriage record is now definitively NOT in any of the four most-predicted parishes** — accept the T1.5 chain and stop spending cycles there unless pursuing Bruff, rootsireland.ie, or Limerick Diocesan Archive.

## Summary

Spent the session running a rapid civil-records + parish-register sweep on the Gleeson/Moloney/Hayes lines with user driving searches on irishgenealogy.ie, FamilySearch, Ancestry, and NLI registers. Locked Patrick Sr's 1897 death, Bridget #8 × Michael O'Connor 1924 marriage, Catherine #0 baptism 31 Jan 1862, and Helen J. Ryan = Ellen Kelly (Ballymackeamore 1905, mother Kate Moloney = strongly inferred sister of our Margaret). Also added Honora 1866 + Mary 1872 civil regs, Bohergeela East 1911 household (Jeremiah as new head + Katherine Gleson 65 as new person), and Margaret Moloney Ballinscola eliminated as kin candidate via 1906 suicide cert.

## Current State

**Branch:** main (default). Up to date with prior session work plus today's 4 new commits.

```
faaaa76  LOCK Catherine #0 baptized 31 Jan 1862 Croom (Scagh) + Patrick × Margaret marriage record 4-parish negative
d2b11cd  LOCK Helen J. Ryan = Ellen Kelly (Ballymackeamore 1905) → Catherine's maternal first cousin; promotes Margaret natal family to T1.5
a38aa28  Bohergeela East 1911 census: Jeremiah heads Stephen Sr's surviving siblings + new Katherine Gleson 65
4a8cb83  LOCK Patrick Gleeson Sr d. 7 Dec 1897 Croom via Bridget × O'Connor 1924 marriage
55c0bb4  docs: handoff 2026-06-05_nora-bina-locked (prior-session handoff archived)
```

facts.md, memory entries, and MEMORY.md index all synchronized to reflect today's locks. New memories created this session:
- `gleeson_patrick_1897_death_candidate` (renamed to CONFIRMED status)
- `gleeson_bridget_oconnor_1924_marriage`
- `gleeson_baggotstown_west_brothers`
- `gleeson_margaret_moloney_ballinscola_eliminated`
- `gleeson_katherine_65_connolly_1911`
- `gleeson_mary_widow_stephen_death_window`
- `gleeson_helen_ryan_ellen_kelly_identified`

## Uncommitted State / Untouched

**Uncommitted:**
- `docs/project_notes/handoffs/HANDOFF_2026-06-05_nora-bina-locked.md` — modified by user earlier with Mucklin annotation + GRO paper-order note. NOT today's work; don't bundle.

**Untracked (pre-existing, NOT today's scope — leave alone):**
- `assets/external/ancestry/hospital.png`
- `assets/external/misc/gleeson-1829-vs-1833-web-response.md`
- `research/prompts/gleeson-1829-vs-1833-web.md`

**Untracked (today's items — review/file as needed):**
- `incoming/chatgpt-gleeson-moloney-2.md` — reviewed today, rejected (John Gleeson = Patrick's father claim broke against locked T1). Could file as a rejected lead or delete.
- `incoming/chatgpt-gleeson-moloney-bolo.md` — UNREVIEWED. Small file (1.3K), worth a 30-second triage before discard or filing.
- `research/prompts/gleeson-patrick-margaret-marriage-2026-06-08.md` — likely the marriage-search prompt the user gave to chrome-extension Claude. Worth filing for posterity.

**Untouched (deliberate):**
- Higgins / Kuthe / Parrett / Mowery lines — focused entirely on Gleeson today.
- The Boherygeela "Tina" → Timothy transcription-error verification (per `gleeson_mary_widow_stephen_death_window` open follow-up) — punted to a future session.

## In Progress

Nothing actively mid-task. User wound down with all session findings committed and memory synchronized. The marriage-search closure is itself a completion ("we will not search this again unless new evidence emerges").

## Gotchas

- **Patrick's birth year is genuinely undetermined**: facts.md and memories now reflect 1829 / 1833 / 1837 as three live candidates (death-cert age 60 → ~1837 is the most recent reading, but Hospital baptisms for James + Honora are documented in 1829 + 1833 only). Don't pick one without new evidence; the trinary is the current honest state.
- **Bridget #3 (b. 1868) fate is unknown** post-2026-06-07 — previously was the leading "Mrs. O'Connor" candidate, but Bridget #8 (b. 1881) now confirmed = the O'Connor bride. #3 may have died young or emigrated; search Croom child/young-adult deaths 1868–1900.
- **Helen J. Ryan = Ellen Kelly + Kate Moloney sister chain is T1 on the baptism, strong T2 on the sibling inference.** Kate's parents are NOT directly verified — promotion to full T1 requires either Kate's baptism record at Croagh ~1845–1860 or her marriage record to John Kelly. Don't overstate as "locked T1" on the sister-Margaret claim.
- **Catherine 1862 baptism: year header on NLI page 81 is visually ambiguous** between 1862 and 1863. FS index says 1862 — trust that. User's visual check leaned 1862 but acknowledged 1863 was possible. If the year matters for a downstream argument, double-check by scrolling to a neighboring page in the NLI viewer.
- **Catherine's 1898 arrival in US (per 1900 + 1920 censuses) is anomalous** — 19 yrs after the 1879 Croom marriage. Either she + John lived in Croom 1879–1898 (reshapes their biographies) or both census enumerators recorded a consistent error. Unresolved.
- **Research-session-2026-06-07.md (v1 + v2)** in `assets/external/familysearch/` have correction notes annotated — the original §6 misidentified the Main St Croom widow household as "different family." That's NOT correct — it IS our family. Read the correction annotations, not the original §6 text.
- **The 1851 Griffith's "John Gleeson at Main Street Croom = Patrick's father" claim from chatgpt-gleeson-moloney-2.md is REJECTED** — our family didn't live at Main Street in 1851 (Patrick was at Scagh through ≥1872). The rejected claim is preserved in incoming/ for the audit trail but should not be relied on.
- **Don't chase the 1860 Crew Lists "Pat Gleeson 26 Limerick"** — per memory `research_hygiene_check_prompts`, this is the wrong-family Limerick City Pat the sailor.
- **Don't chase Catherine M Hayes records** — middle initial M = not our Catherine.

## Next Steps

Ordered by ROI:

1. **Pull Catherine 1862 baptism manuscript image directly** (NLI vtls000634977 page 81) — the FS index gave us the bare fact, but the manuscript page may have additional context (other sponsors on the same date, the year header definitively). Already confirmed: Scagh + sponsors John Moloney + Bridget Gleeson + officiant J.L. Roche CC.
2. **Pull cert image of Patrick 1897 death cert** if not yet saved as PDF — it's already filed at `assets/external/familysearch/patrick-gleason-death-cert-1897.pdf`. Verify townland column for the strongest possible Patrick = our Patrick lock-down.
3. **Search Croom SRD death index 1907–1911 for Mary Gleeson** (Stephen Sr's widow, b. ~1843, expected age 64–68 at death). Per `gleeson_mary_widow_stephen_death_window` memory.
4. **Search for Patrick Gleeson child deaths Croom SRD 1868–1880** — would resolve Bridget #3 fate (if she died as a child/young adult).
5. **Search for Margaret Moloney's death post-1918** — she was alive Jan 1918 signing the deed release; death unfound. May be in a different SRD (lived with a married daughter post-1918?).
6. **Search for Catherine + John Hayes US Catholic sacramental records** — marriage convalidation? Their childlessness across 1880-1944 makes baptisms unlikely but worth a long-shot pull. St Mary's Grasmere parish records.
7. **Search Mary Gleeson (3rd obit sister) marriage post-1915** — obit confirms she stayed in Croom till 1946, but no Croom-SRD marriage found post-1911. May have married elsewhere or stayed single.
8. **Helen J. Ryan's parentage refinement via Croagh CPR ~1845–1860 for Kate Moloney baptism** — would lock the Kate-as-Margaret's-sister claim to T1.
9. **Try Bruff parish 1858–1862 marriages** for Patrick × Margaret — only remaining family-connected unsearched parish. NLI free image browse.
10. **Try rootsireland.ie €5 paid search** for Patrick Gleeson × Margaret Moloney Limerick 1858–1865 — could surface a record on a damaged/missing NLI page.

## Open Tickets

None tracked in `docs/project_incoming/` — this project uses memory + facts.md rather than ticket-based tracking. All session findings are in memory (`~/.claude/projects/-Users-matt-projects-new-genealogy/memory/`) and facts.md (`research/findings/patrick-gleeson/facts.md`).

## Wide-context references for next session

The Gleeson/Moloney research is now substantially advanced:
- Patrick Sr line: parents James + Honora O'Brien Hospital (T1), siblings Margaret 1842 + Catherine 1850 + John (Baggotstown West) [T1], 9 documented children all with births/baptisms identified, death 7 Dec 1897 (T1)
- Margaret Moloney line: parents James Molony + Catherine Kenny Croagh (T1.5), siblings Margaret + James + Kate + Jeremiah at Ballymackeamore/Croom cluster
- Catherine #0 (firstborn, b. Jan 1862 Croom) → Mrs. John Hayes Staten Island → no children → cared for in widowhood by first cousin Helen Ryan (= Ellen Kelly, daughter of Kate Moloney) → Helen executed her 1944 estate
- Bridget #8 (b. 1881 Croom) → Mrs. Bridget O'Connor (Croom 1924) → in James J.'s 1946 obit
- Boherygeela family: Stephen Sr (d. 1907) + Timothy Sr (d. 1905) + their children largely documented; Jeremiah heads household by 1911

The unresolved primary questions are now: Patrick's exact birth year (1829/1833/1837), the Patrick × Margaret marriage record's location (probably nowhere — accept), Margaret's death post-1918, and the unaccounted-for siblings' fates (Bridget #3 + Honora 1866 + Ellen 1869 + Margaret 1875 + Jane 1878).

# Session Handoff

**Created:** 2026-06-03T19:51-07:00
**Session ID:** aa92900e-b003-4fd6-a1fc-64238561bb4b
**Working Directory:** /Users/matt/projects-new/genealogy

## What to read first

This session locked **both natal families** of Patrick Gleeson + Margaret Moloney via parish-register transcripts, plus identified Catherine Hayes (Staten Island) as their firstborn daughter — three single-line breakthroughs that ~3 weeks ago were three open hypotheses. The new lock-ins extend the documented tree back **one full generation** above Patrick + Margaret. `research/findings/patrick-gleeson/facts.md` was rewritten extensively; read the "What we know" + "Documented life events" sections first. The current state-of-the-art tree summary is at `docs/project_incoming/tree-2026-06-03.md`.

## Summary

The session began as a continuation of the Croom 1879–1881 baptism sweep (handoff 2026-06-02_gleeson-census-bounds item #1) but escalated rapidly when a series of Ancestry index hits + Matt's "random walk" through the Croom marriage register surfaced (a) the 29 Nov 1879 Croom marriage of Catherine Gleeson + John Hayes — locking Mrs. John Hayes of Staten Island as Patrick + Margaret's firstborn daughter; (b) the 20 Mar 1829 Hospital, Co. Limerick baptism of Patrick himself — locking his parents as James Gleeson + Honora O'Brien; and (c) the 31 Dec 1836 Croagh (= NLI catalog variant for Kilfinny) baptism of Margaret — locking her parents as James Molony + Catherine Kenny. Every Irish naming-pattern prediction we'd published was independently confirmed by the transcripts. Multiple disambiguation hypotheses (1894 Teutonic Catherine, 1912 Cameronia John Hayes + Agnes, 1915 Rensselaer marriage, 1865 headstone date, 1876 death cert date, "tentative #9 daughter Catherine") were either retired or repositioned by the new evidence.

## Current State

- Branch: `main`, **86 commits ahead of origin** (still unpushed; matches Matt's pattern)
- Working tree: about to be clean after this handoff is committed
- Session commits (this session only, 13 new total since the 2026-06-02 handoff `6df9237`):

```
3e2b54e  LOCK Margaret's natal family: James Molony + Catherine Kenny, Croagh/Kilfinny 1836  ⭐⭐⭐
cabcf02  Add 2 wrong-family Patrick Gleeson transcripts (disambiguation context)
a7cc304  Add Ireland Police Gazette Patrick Gleeson hits 1876-1891
718e67c  LOCK Patrick's natal family: James Gleeson + Honora O'Brien, Hospital 1829  ⭐⭐⭐
6a4473a  Add Croom marriage transcripts 1860-1869 + 4 new sibling candidates
2b137e5  Add Croom marriage register transcripts 1871-1879 + Thomas Moloney lead
c9dae8a  Lock Catherine Hayes (Staten Island) as Patrick + Margaret's firstborn  ⭐⭐
e6445ea  Identify Mrs. John Hayes as Catherine Gleason (Staten Island, d. 1944)  ⭐
cb88d11  Sweep Croom baptism pages 88-92 + 116-119 for Catherine Hayes hunt
1a27029  Add chronological Gleeson timeline (Patrick c.1832 - James 1946)
74ecaed  Confirm Bridget Gleeson 1881 as 8th child via civil birth registration  ⭐
884bb38  Sweep Croom baptism pages 122-125 (Mar 1879 - Jun 1881)
```

Memory additions/updates:
- `gleeson_bridget_1881_civil_birth.md` (project) — 8th child via civil reg
- `irishgenealogy_mother_surname_trap.md` (feedback) — civil-birth index returns "N/R" pre-1900; don't primary-filter
- `gleeson_two_chain_proof_architecture.md` (project) — Chain A (Irish) + Chain B (US) meeting at 1892 marriage doc
- `gleeson_mrs_hayes_catherine_identified.md` (project) — Catherine = Mrs. John Hayes Staten Island, LOCKED
- `gleeson_ella_staten_island.md` (project, updated) — superseded by Catherine identification
- `gleeson_patrick_natal_family_locked.md` (project) — Patrick b. 20 Mar 1829 Hospital; parents James Gleeson + Honora O'Brien
- `gleeson_margaret_natal_family_locked.md` (project) — Margaret b. 31 Dec 1836 Croagh/Kilfinny; parents James Molony + Catherine Kenny

## Uncommitted State / Untouched

**Uncommitted:** the handoff file itself (this document) — will be committed alone per skill protocol.

**Untouched (deliberate):**
- Did NOT push 86 commits to origin (consistent with Matt's pattern across recent sessions)
- Did NOT investigate Mowery / Higgins / Kuthe / Parrett lines this session — Gleeson-only
- Did NOT pull the 1900–1940 Hayes household US Census records yet (top remaining NY-side test for Nora Gleason 1881–1939 = Bridget #2 hypothesis)
- Did NOT search Hospital parish 1820s–1840s for Patrick's siblings (other children of James Gleeson + Honora O'Brien) — known next step
- Did NOT search Croagh/Kilfinny pre-1836 or 1837–1845 for Margaret's siblings (other children of James Molony + Catherine Kenny) — known next step
- Did NOT pull James Gleeson + Honora O'Brien's own marriage record (~1820s Hospital parish) — known next step
- Did NOT pull James Molony + Catherine Kenny's own marriage record (~1820s–1830s Croagh/Kilfinny) — known next step
- Did NOT investigate the 1833 Ballinvriana Patrick (same parents James Gleeson + Honora O'Brien, different parish) — recorded both interpretations (1829 lock holds; 1833 is either younger brother or memorial-named replacement)
- Did NOT pull the 17 unread Croagh baptism pages (1837–1845 in vtls000634970 + vtls000634971) — fetched pages 5–13 only (1836 + Feb 1838); pages 14–61 of vtls000634970 untouched
- Did NOT refresh `research/summaries/gleeson-timeline.md` with the new natal-family extensions

## In Progress

None — all session work either committed or deliberately deferred. Final task list:
- All session tasks closed.

## Gotchas

- **Surname spelling: Molony vs Moloney vs Maloney is parish-record variation, NOT a different-family signal.** The existing `gleeson-moloney-not-maloney` memory says "not Maloney" — that guidance is about US-side Ancestry trees only, NOT Irish parish records. The Croagh 1836 entry's cursive can be read as Molony OR Maloney; both are renderings of *Ó Maoldhomhnaigh*. Identification holds either way because the four other converging predictions (Catherine mother, Kilfinny parish, James father, 9-10 yr age-shaving) lock the candidate regardless of -o- vs -a-. Updated note in `facts.md` "Wife" section + `gleeson-margaret-natal-family-locked.md` memory.
- **Croagh = Kilfinny in NLI's catalog** — Matt nearly skipped this lead because clicking "Kilfinny" got redirected to parish 0880 "Croagh." NLI lists Kilfinny as a *variant name*; same parish.
- **Both Patrick and Margaret's families consistently under-reported their ages by 9-11 years on records.** Catherine Hayes too (b. 1865 per headstone, reported 68 at death = 11-yr shave). This is a family pattern, not a single-record error. Apply when reading any Census age for this family.
- **The 1833 Ballinvriana Patrick is ambiguous.** Same parents (James Gleeson + Honora O'Brien) baptized a SECOND Patrick on St. Patrick's Day 1833 in Emly parish (~8-10 miles from Hospital where the 1829 Patrick was baptized). Two interpretations recorded in `facts.md`: (a) 1829 Patrick died young, 1833 Patrick is OUR Patrick named in memorial (most parsimonious; would make Patrick's birth date 17 Mar 1833 not 20 Mar 1829); (b) both survived and OUR Patrick is the 1829 one with a younger brother also named Patrick (unusual but documented). Current `facts.md` keeps the 1829 lock as the primary candidate with the 1833 alternative noted. **Don't silently overwrite without considering both.**
- **Nora Gleason 1881–1939 in the Hayes burial plot is most likely Bridget #2 (b. 11 Oct 1881 Croom) emigrated to NY as "Nora."** Strong hypothesis, not yet confirmed. 1900–1940 Hayes household US Census records are the cleanest test — single biggest pending data pull.
- **The 1894 Teutonic Catherine Gleeson age 20 → Philadelphia is NOT our Catherine.** She was already Mrs. Hayes since 1879. Don't re-chase as a candidate. The Nenagh-cluster arrival is a coincidental name collision.
- **The 1912 Cameronia John Hayes + Agnes Hayes + 4 children is a DIFFERENT John Hayes family** from our Catherine's husband. Our John 1862–1929 was married to Catherine only. Don't re-merge.
- **The 1915 Rensselaer/Troy "Catherine Hayes + John Hayes" marriage is NOT ours.** They were already married 29 Nov 1879 Croom.
- **The Ireland Police Gazette 4 Feb 1879 Limerick Patrick Gleeson assault wanted notices + the 1871 Nenagh Jail Pat Gleeson 1885 Nenagh death = a SEPARATE Tipperary Pat Gleeson ("Bad Pat of Nenagh")**, not ours. Our Patrick was actively shopkeeping in Croom in 1881 with a clean wedding-witness and birth-registration paper trail in those years.
- **The 1900 Philadelphia Margaret Maloney + the 1905 Buffalo Co. WI Margaret Maloney are both different families** — see facts.md Margaret candidate-records section + tonight's brief disambiguations. Old finds; should NOT re-appear as new candidates.

## Next Steps

In rough order of leverage:

1. **1900, 1910, 1920, 1930, 1940 US Census records for John + Catherine Hayes** at 64 Edison St Staten Island (and earlier addresses like Egbert St shown in 1920). The 1930 census specifically is the cleanest test for whether **Nora Gleason 1881–1939 = Bridget #2 (Croom 1881)** by checking the Hayes household composition. Also disambiguates Catherine's actual birth year (1865 headstone vs 1872 1920 census vs 1876 death cert) by tracking the self-reported age across years.
2. **Hospital parish baptisms 1820s–1840s** — look for siblings of Patrick (other children of James Gleeson + Honora O'Brien). Their existence/non-existence would also disambiguate whether the 1833 Ballinvriana Patrick is our Patrick (in memorial after 1829 died) or a younger brother (both alive). NLI Hospital parish ID + microfilms not yet looked up — needs the lookup flow on https://registers.nli.ie/parishes (search "Hospital").
3. **Hospital parish marriages ~1820s** — find James Gleeson + Honora O'Brien's own marriage record. Would also potentially name THEIR parents (one more generation up).
4. **Croagh/Kilfinny baptisms 1820s–1840s** — look for siblings of Margaret (other children of James Molony + Catherine Kenny). The NLI vtls000634970 covers 1836–1843 (pages 5–61 fetched 5–13 only tonight; pages 14–61 untouched). Pre-1836 records are NOT in NLI's collection; siblings older than Margaret won't surface there.
5. **Croagh/Kilfinny marriages ~1820s–1830s** — find James Molony + Catherine Kenny's own marriage record. Would extend Margaret's maternal lineage one more generation.
6. **Patrick + Margaret's own marriage record** (~1855–1857) — now triple-anchored as a search target: Hospital parish (Patrick's natal), Croagh/Kilfinny (Margaret's natal), or Croom (their later home). Worth a focused sweep of all three.
7. **The 1911 antecedent mortgage from the Irish Registry of Deeds** — referenced by the 1918 deed Memorial #29; not yet pulled. Would close out Margaret's property-chain story.
8. **Police Gazette 4 Feb 1879 Limerick page image** — single-image pull to confirm "Bad Pat of Nenagh" disambiguation (currently inferred but unconfirmed).
9. **Refresh `research/summaries/gleeson-timeline.md`** with the new natal-family extensions + Catherine as firstborn. Currently a "Patrick → James J." timeline; could extend to a "Patrick's parents → Anne Barbara" rail.
10. **Push 86 commits to origin** when convenient.

## Tools available (used / validated this session)

- `scripts/nli_fetch_hires.sh` — NLI parish register hi-res fetch via IIP tile assembly. Used for Croom (vtls000634977) and Croagh (vtls000634970) this session.
- NLI parish-register pipeline documented at `research/analysis/nli-parish-register-pipeline.md`.
- `https://registers.nli.ie/parishes?q=<name>` — parish search (note: Kilfinny redirects to Croagh).
- `https://registers.nli.ie/registers/<vtls_id>#page/<N>/mode/1up` — direct viewer URL (cleaner rendering than fetched JPGs in some cases).
- `irishgenealogy.ie` civil-records search — used for civil birth + death disambiguation. The mother's-surname filter returns N/R for most pre-1900 entries; see [[irishgenealogy-mother-surname-trap]] memory.
- Find A Grave — used by Matt to source the St Mary's Cemetery Grasmere headstone information (Catherine Hayes 1865–1944, John Hayes 1862–1929, Nora Gleason 1881–1939, Helen J. Ryan 1905–1989, Thomas J. Ryan 1899–1982).

## Critical reference files

- `research/findings/patrick-gleeson/facts.md` — main source of truth, rewritten extensively
- `docs/project_incoming/tree-2026-06-03.md` — current state-of-the-art tree summary (Generations 1A + 1B + 2 + 3 + 4)
- `research/summaries/gleeson-timeline.md` — chronological rail (note: not yet refreshed with this session's lock-ins; deferred)
- `assets/external/1829-hospital.md` — Patrick's natal-family lock transcript
- `assets/external/misc/croagh-1836.md` — Margaret's natal-family lock transcript (with multiple page-area transcriptions for context)
- `assets/external/catherine-marriage-maybe.md` — 29 Nov 1879 Croom marriage of Catherine + John Hayes transcript
- `assets/external/catherine-marriage-maybe-page-before-{1,2,3,3or4,4,6,7,8-maybe150}.md` — 8 surrounding Croom marriage-register page transcripts (covering 1860–1879), providing rich context on the Patrick-area kin network
- `assets/external/misc/ancestry-catherine-hayes-ny-death.md` + `...-2.md` — NY death cert + 1940 Manhattan census confounder
- `assets/external/nli-croagh/page_{5..13}_baptism.jpg` — 9 fetched Croagh baptism page images
- `research/results/gleeson-civil-births-croom-1879-1886.md` — civil birth search disposition
- `research/results/gleeson-catherine-hayes-search.md` — full Catherine identification chain

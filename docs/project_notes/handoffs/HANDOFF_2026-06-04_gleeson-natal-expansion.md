# Session Handoff

**Created:** 2026-06-04T21:30 PDT
**Session ID:** d228488d-8b97-456b-899b-bf85ee2cb000
**Working Directory:** /Users/matt/projects-new/genealogy

## What to read first

The "⭐ LOCKED" annotation pattern has been retired in favor of a `[T1]/[T2]/[T3]` evidence-tier scheme — see the legend at top of `research/findings/patrick-gleeson/facts.md` and `research/summaries/gleeson.md`. The 1829 vs 1833 Patrick baptism question is now explicitly open (it had been claimed "LOCKED 1829" in an earlier session). All Gleeson-line memory files were updated accordingly; if you make new claims, tag them.

## Summary

Major expansion of Patrick Gleeson's natal-family knowledge. Two new documented siblings (Margaret 1842 Herbertstown, Catherine 1850 Hospital), all four grandparent names derived [T2] from naming pattern + sponsor corroboration, Callaghan kin network identified, two collateral leads filed (Naas 1888, Anacarty 1858). Methodology shift: adopted T1/T2/T3 tier-tagging across memory + summary + facts doc after ChatGPT review flagged "LOCKED" language as conflating direct documentation with inferential identity.

## Current State

Branch: `main` (96 commits ahead of origin/main — not pushed; that's fine and intentional).

Session commits (9, most recent first):

```
f388198  Sync patrick-gleeson facts.md with current memory + summary state
b257fc7  1829 Hospital transcript: correct page number 55 -> 71, clean up surrounding entries
7e97acd  Caveat the 1850 sponsor read: C___an confirmed; Callaghan network-inferred
91c37ff  Add Margaret 1842 Gleeson sibling + Callaghan kin network; derive grandparent names
b89eb68  Add North Tipperary 1863-1864 marriage register transcript (reference only)
67b2bb9  LOCK Catherine 1850 as Patrick's sibling: Hospital parish baptism, James + Honora O'Brien
cd9d4ea  Add Naas 1888 marriage transcript + Michael Gleeson T3 collateral lead
f355760  gleeson summary: incorporate 1833 Ballinvriana transcript + Pat O'Brien sponsor
2d068ea  gleeson summary: add tier-tag scheme, Patrick natal family, Catherine as firstborn
```

(Note: commit 67b2bb9 uses "LOCK" in its message — written before the user clarified the Callaghan caveat. The content commits are fine; the message reflects pre-caveat thinking.)

### Documented siblings of our Patrick (new this session)

| Year | Child | Townland | Sponsors |
|------|-------|----------|----------|
| 1829 | Patrick | Hospital (no townland) | Stephen Gleeson + Bridget Higgins |
| 1833 | Patrick (2nd) | Ballinvriana | Pat O'Brien + Ellen Walsh |
| **1842** | **Margaret** | **Herbertstown** | Michael Callaghan + Margaret O'Brien |
| **1850** | **Catherine** | Hospital | John Gleeson + Catherine [Callaghan, network-inferred] |

Catherine confirmed via Ancestry index. Margaret transcribed by user from a register page (no separate transcript saved — entry recorded inline in memory + facts.md).

### Derived [T2] grandparents (4th-great-grandparents of Matt)

- Paternal: **Patrick Gleeson + Catherine [?]** (~1770s-80s, Hospital area)
- Maternal: **Patrick O'Brien + Margaret [?]** (~1770s-80s, Hospital/Emly area)

All four corroborated by sponsorship records (Stephen Gleeson 1829, John Gleeson 1850, Pat O'Brien 1833, Margaret O'Brien 1842).

## Uncommitted State / Untouched

**Uncommitted:** Untracked file `assets/external/ancestry/hospital.png` (the source image for the 1829 Hospital register transcript). The user offered it mid-session as a reference image; I didn't ingest it because the transcripts already aligned on our Patrick's entry. Safe to either commit (with the 1829-hospital.md transcript update) or leave untracked — your call. **Not user's in-progress work** — they offered it as research material.

**Untouched (deliberate):**
- `research/reports/patrick_gleeson_bio.md` and its built HTML — the public-facing Patrick biography is meaningfully stale (still says father unknown, lists 7 children, says Mrs. Hayes unidentified). User decided to leave the polished bio as-is for now; the working/research material lives in `research/findings/patrick-gleeson/facts.md` (which I updated). If you're asked to publish anything, raise this before editing the public bio.
- `docs/project_notes/handoffs/HANDOFF_2026-06-03_natal-families-locked.md` — prior session's handoff, untouched. Filename literally says "natal-families-locked" — historical accuracy stands.
- `docs/project_incoming/tree-2026-06-03.md` — external tree import, not assessed for staleness; probably one-time data.

## In Progress

Nothing actively in progress. Session ended at a clean stopping point after the user requested "five highest-value disambiguations or searches" for tonight (see Next Steps).

## Gotchas

- **"LOCKED" terminology is retired** — see What-to-read-first. If you encounter `⭐ LOCKED 2026-XX-XX` annotations in any older docs/handoffs/incoming notes, they predate the methodology shift; don't propagate the pattern.
- **1829 vs 1833 Patrick is genuinely open** — earlier session claimed 1829 locked; we now have slight lean to 1833 (sponsor side-switch + ~1832 calibrated estimate + St Patrick's Day memorial pattern). Don't re-lock without independent evidence.
- **Catherine Callaghan (1850 sponsor) surname is letterform-uncertain** — user confirmed only C-start and -an-end; "Callaghan" is the *network-inferred* read because Michael Callaghan sponsored Margaret 1842. If the network match is coincidence, Corrigan/Cornican remain possible.
- **Margaret Moloney birth year had been "REVISED to c. 1845"** in a prior session based on Census ages, but is now reverted to 31 Dec 1836 (Croagh baptism) — Census ages reflect the documented 9-10 yr age-shaving pattern matching Catherine Hayes's identical pattern. Don't re-revise back to ~1845.
- **The 1829 Hospital register right page is page 71, not 55.** Cleaned up this session; the "page 55" reading was a 5/7 cursive confusion.
- **Naas 1888 + Anacarty 1858 are T3 leads, NOT confirmed kin.** The Naas one would resolve 1829-vs-1833 if upgraded (Michael's father Patk Gleeson + Honora O'Brien Tipperary = surviving 1829 Patrick). The Anacarty one is in-diocese name match only.
- **`research/findings/patrick-gleeson/facts.md` had stale numbering** in Open Questions section before this session's update — items 7-10 were orphaned after 1-6. Now cleanly renumbered 1-16. If you find similar orphaned numbering elsewhere, sweep it.

## Next Steps

User requested top-5 disambiguations for tonight. Ranked by leverage:

1. **Patrick + Margaret's marriage record** [highest value] — Croom register pre-1853; also Hospital parish 1850s; also Croagh/Kilfinny 1850s. Marriage window now ~1856 or earlier (since Catherine firstborn ~1857-62). Would name Margaret's father directly → upgrades her natal family T2 → T1.

2. **Hospital parish baptism sweep 1833-1850** for more siblings of Patrick — likely 4-6 more children of James + Honora O'Brien in the gaps. Each one adds T1 data and tightens grandparent-name predictions. **My top recommendation if user only does one search.**

3. **Nora Gleason at 64 Edison St Staten Island, US Census 1900-1940** — quick check of Catherine Hayes's household for a Nora Gleason boarder. Would resolve the Bridget #2 → Nora Gleason T3 hypothesis.

4. **Catherine Gleeson 1850 marriage record** — Hospital/Croom 1868-1880, bride b. ~1850, father James. Resolves her fate.

5. **Naas 1888 verification** — search Tipperary baptisms 1858-1866 for Michael Gleeson son of Patrick + Honora O'Brien. If found: domino → 1829-Patrick survived in Tipperary → ours is 1833 → settles biggest open question + adds confirmed first cousin.

## Open Tickets

None new this session. Prior session's open work was the natal-family lock-in (now extended/superseded by this session's expansion).

## Cross-references

- Updated this session: `gleeson_patrick_natal_family.md`, `gleeson_margaret_natal_family.md`, `gleeson_naas_1888_michael_lead.md` (new), `gleeson_anacarty_1858_weak_lead.md` (new), `MEMORY.md` (4 entries updated/added).
- Files updated in repo: `research/summaries/gleeson.md`, `research/findings/patrick-gleeson/facts.md`, `assets/external/1829-hospital.md`, `assets/external/misc/patk-honora.md` (1833 transcript), `assets/external/misc/hospital-1850-baptisms.md` (new), `assets/external/misc/naas-1888-marriage.md` (new), `assets/external/misc/north-tipperary-1863-1864-marriages.md` (new, reference only).

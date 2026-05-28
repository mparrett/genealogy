# Higgins / Knight Census Verification Script

**Goal:** Tighten the Knight tree and settle the Laurence-occupation question by pulling two specific federal census enumerations and extracting every useful field. These two records together should resolve ~60–70% of the open questions on the Knight side and on Laurence's NYC/Newark working life.

**Created:** 2026-05-28

---

## Target 1 — 1880 US Federal Census, Newark NJ: the Knight household

### Why this record

The Knight tree currently hinges on Mary's 1930 death certificate (which names parents James Knight + Bridget Larney) plus an asserted-but-uncaptured 1880 Newark enumeration. Every downstream Knight claim — siblings, ages, Sligo origin, "Larney" vs "Courtney" surname — depends on the 1880 household being the right family. We don't have the image, the address, or the household roster.

### What we expect to find (predicted match profile)

A Knight household in Newark, Essex County, NJ, June 1880, with:

| Person | Sex | Age | Birthplace | Father's bp | Mother's bp |
|---|---|---|---|---|---|
| James Knight (head) | M | ~37 | Ireland | Ireland | Ireland |
| Bridget Knight (wife) | F | ~34 | Ireland | Ireland | Ireland |
| **Mary Knight** | F | **14** (or 17 if 1863 birth) | Ireland (working assumption — family-friend research treats this as settled) | Ireland | Ireland |
| James J. Knight | M | ~13 | NJ or Ireland | Ireland | Ireland |
| David H. Knight | M | ~10 | NJ | Ireland | Ireland |
| Mary Rebertha Knight | F | ~1 | NJ | Ireland | Ireland |
| Elizabeth Knight | F | ~1 | NJ | Ireland | Ireland |

Notes:
- 1880 captures birthplace for self **and** both parents — first census year with that detail. Country only, not county.
- "Mary Rebertha" and "Elizabeth" both born 1879 in our notes is suspicious. Either twins (and the census should mark both as age 1), or one is a duplicate. If the household has only one ~age-1 daughter, that resolves it.

### Where to search

**FamilySearch (free, indexed):**
- Start: https://www.familysearch.org/search/collection/1417683 (1880 US Census collection)
- Search constraints to try, in order:
  1. **First pass — tight:** First name "Mary" + surname "Knight" + birth ±2 yrs of 1866 + residence "Essex, New Jersey, United States" + father "James" + mother "Bridget"
  2. **Second pass — loosen wife's name:** drop "Bridget", keep "James" as father — Bridget may have been indexed as "Bridgit", "Brigid", or "B."
  3. **Third pass — head-first:** search head "James Knight" + residence Newark + age range 35–45 + wife's first name "Mary" or blank
  4. **Fourth pass — surname variant:** swap "Knight" → "Night" (the K is sometimes dropped in indexing); also try "McKnight"
  5. **Fifth pass — wildcards on Mary's birth year:** in case our 1866 is wrong and Mary Anne's 1863 is right, search +5 years on the birth-year tolerance

**Ancestry (indexed; need account):**
- 1880 census search form: https://www.ancestry.com/search/collections/6742/
- Same constraint progression. Ancestry's wildcards (`Bridg*`, `Knigh*`) are particularly useful here.

**If both indexes miss:** browse the ED-level pages for Newark wards 1–15 directly. 1880 Newark had ~150,000 people across ~15 wards; with no address it's a lot. FamilySearch lets you page through enumeration districts in browse mode. Start with the wards with the densest Irish populations — wards 5, 6, 8, 10, 11, 12, 13 (heavily Irish in this era). The 1900 enumeration (target #2 below) will give us a Newark Ward 5 address that we can map back; if the 1900 address is the same family-of-origin neighborhood, that narrows 1880 wards too.

### What to extract from a winning match

| Field | Why it matters |
|---|---|
| **Page #, line #, dwelling #, family #** | Citation anchor for everything downstream |
| **Address / street** | Lets us cross-reference 1900, look for Quigleys nearby, identify parish |
| **Head's occupation** | Independent data point on Knight household status |
| **Head's birthplace** + **his parents' birthplaces** | Country-level Irish origin (no county data in 1880, but corroborates Ireland) |
| **Wife's first name spelling** | "Bridget" vs "Bridgit" vs "Bridgid" — small but useful for chasing her records |
| **Each child's birthplace** | Reveals when the family arrived in the US — if all under-10s are NJ-born, emigration was pre-1870 |
| **Each child's age** | Confirms or refutes the duplicate-1879-daughter problem |
| **Marital status fields** | "Married within the year" is a column; check for hints of remarriage |
| **Health columns** | 1880 had columns for "sick or temporarily disabled," "blind," "deaf and dumb," "idiotic," "insane," "maimed, crippled, bedridden" — if any are marked, that's substantive |
| **Whether anyone in household attended school within the year** | Tells us if Mary was in school at 14 |
| **Whether anyone listed could not read / could not write** | Literacy on both parents |

### What this resolves

- ✅ Whether the asserted Newark 1880 placement is real
- ✅ The Mary Rebertha / Elizabeth same-year-birth duplicate question
- ✅ Mary's birth year (1866 vs 1863) — she'll have an age on the line
- ✅ Sibling roster, ages, and birth states (resolves the order of immigration / family-formation timeline)
- ✅ Head-of-household occupation (more Knight context)
- ⚠️ Does *not* resolve Sligo vs Courtney — 1880 doesn't capture Irish county
- 🟦 *Not chasing here:* Mary's Ireland origin — treated as settled per family-friend research

---

## Target 2 — 1900 US Federal Census, Newark Ward 5 NJ: the Laurence Higgins household

### Why this record

1900 is **the single highest-yield US census year for this family** because it captures fields the 1880 and 1910 censuses don't:

- **Month and year of birth** for every individual — settles Mary's 1863 vs 1866 question and confirms Laurence's January 1854 baptismal date
- **Year of immigration** for every foreign-born individual — gives us when both Laurence and Mary actually arrived
- **Number of years married** — settles whether the 1883 Dublin ceremony was real (~17 years married) or only 1887 Manhattan counted (~13 years)
- **Mother of how many children / how many now living** — settles the "Margaret Higgins c. 1882" ghost (if Mary reports 5 children with 3 living, Margaret existed; if 4 with 3, she didn't)
- **Occupation field** — settles "Laurence = porter"
- **Naturalization status** for Laurence — pa/na/al column

It also runs second in chronology, but I'd actually do it **first** in practice because it can guide the 1880 search by giving us a Newark Ward 5 address (the Knight family may still be in the same area).

### What we expect to find (predicted match profile)

A Higgins household enumerated in Newark Ward 5, Essex County, NJ, June 1900:

| Person | Relation | Sex | Month/Year of Birth | Age | Birthplace |
|---|---|---|---|---|---|
| **Laurence Higgins** (head) | head | M | Jan 1854 | 46 | Ireland |
| **Mary Higgins** (wife) | wife | F | Aug 1866 (or 1863) | 33 or 36 | Ireland |
| Mary A. Higgins | dau | F | Sep–Dec 1888 | 11 | NJ (we have her as Jersey City born) |
| **James E. Higgins** | son | M | Feb 1892 (canonical per NYC birth cert) | 8 | NY |
| Theresa Higgins | dau | F | Jul 1894 | 5 | NY |
| (Anne Higgins?) | step-dau | F | 1878 | ~21 | Ireland | — if she's still in the household at age ~22
| (Margaret Higgins?) | dau | F | ~1882 | ~17 | — | — if the "c. 1882 Margaret" is real

Notes:
- Maggie (Mary Verner's daughter, b. 1874) was probably already married out by 1900 — checking for her here is a useful confirmation she's elsewhere.
- James E.'s birth date is treated as settled (NYC birth cert no. 6077, 2 Feb 1892). Census-taker entries are notoriously inconsistent for this household across years — capture what's there but don't relitigate; the canonical date stands.
- Mary's "mother of X children, Y living" should read: if no Margaret, **4 born / 3 living** (Mary A. + Lawrence-d.-infant + James + Theresa, with Lawrence dead). If Margaret existed, **5 born / 4 living**.
- "Years married" should be **~13** if 1887 was their only marriage, **~17** if 1883 Dublin counts. The census-taker recorded what the wife stated.

### Where to search

**FamilySearch (free, indexed):**
- Start: https://www.familysearch.org/search/collection/1325221 (1900 US Census)
- Search constraints:
  1. **First pass:** First name "Laurence" + surname "Higgins" + residence "Essex, New Jersey" + birth year ±2 of 1854 + birthplace Ireland
  2. **Spelling pass:** Re-run as "Lawrence" + "Higgens" + "Higgans"
  3. **Wife-first pass:** "Mary Higgins" wife, birth ±3 of 1866, Essex NJ, husband "Laurence" or blank
  4. **Child-first pass:** "James Higgins" son, b. NY 1892 ±1, residence Essex NJ — this is robust because James's NY birthplace + NJ residence is a distinctive combo

**Ancestry:**
- 1900 census: https://www.ancestry.com/search/collections/7602/
- Same passes

The 1900 enumeration is well-indexed and Laurence + Mary should turn up on the first pass. If they don't, our "Newark Ward 5, 1900–1920" claim itself is suspect and needs a wider geographic search.

### What to extract from a winning match

| Field | Why it matters | Open question resolved |
|---|---|---|
| **Page #, line #, dwelling #, family #** | Citation anchor | — |
| **Address / street** | Ward 5 precise location — neighbor surnames near it become candidate Knight households for the 1880 cross-check, and candidate Quigleys for the Downing Street lead | Mrs. Quigley research (peripherally) |
| **Laurence's occupation** | "Porter," "Longshoreman," "Janitor," "Laborer"? | **Settles the porter question** |
| **Laurence's birth month/year** | Jan 1854 expected; corroborates baptismal date | Validates the Dublin parish record |
| **Laurence's immigration year** | When did he leave Dublin? | New fact entirely; partially fills the 1881–1887 gap (after Mary Verner's death) |
| **Laurence's naturalization status** | Pa (papers filed) / Na (naturalized) / Al (alien) | Lets us hunt for declaration of intent + final naturalization papers, which would give port + ship + arrival date |
| **Mary's month/year of birth** | Aug 1866 vs Aug 1863 vs other | **Settles the 1863 vs 1866 conflict** |
| **Mary's immigration year** | She supposedly came as a teenager then went back for the 1883 wedding — if true, her immigration year here might be the *second* arrival (post-1883) | Big light on her movement |
| **Years married** | ~13 vs ~17 | **Settles the 1883 Dublin first-ceremony question** |
| **Mary's mother of X / X living** | 4/3 or 5/4 | **Settles the Margaret c. 1882 ghost** |
| **James E.'s reported birth month/year** | Feb 1892 (canonical); record what's there but the date is settled | — |
| **Each child's school attendance / literacy** | Were the older kids in school in 1900? | Tells us if Mary A. (age ~12) was still in school or already working — bears on the family's economic stress trajectory |
| **Anyone else in the household** | Anne Higgins (1878, fate unknown)? boarders? in-laws? a Knight relative? | Anne Higgins's fate; possible Knight–Higgins household-level interaction |

### What this resolves

- ✅ **Porter** sourcing — direct from the enumeration column, not from a downstream summary
- ✅ Mary's 1863 vs 1866 birth year
- ✅ Margaret c. 1882 ghost vs real child (via "mother of X children")
- ✅ 1883 Dublin vs 1887 Manhattan-only marriage question (via "years married")
- ✅ Both spouses' immigration years (entirely new data points)
- ✅ Laurence's naturalization status (opens the door to his declaration papers)
- ✅ Anne Higgins (1878) — if she's in the household, her fate is partially answered; if she's not, the search narrows
- ⚠️ Does *not* resolve Mary's parish/townland of origin — 1900 only captures country
- ⚠️ Does *not* tell us about Laurence's 1906 absconding (that's a 1906 event, post-this-census)

---

## Execution order

1. **Do Target 2 (1900 Newark Ward 5) first.** Higher-yield; easier to find because Laurence's name + birth year + Ireland origin is a tight constraint, and the address it gives us narrows Target 1's geographic search.
2. **Then Target 1 (1880 Newark Knight household).** Use the 1900 Higgins address as a hint for which Newark ward to start in (Knights and Higgins families may be in adjacent wards or even the same one — Mary marrying Laurence locally suggests overlap).

## Capture format

When a winning match is found, save the enumeration image to `assets/external/census/` with a name like `1900-newark-ward5-higgins.jpg`, and create a sidecar transcription at `research/results/higgins-1900-census-transcription.md` (and likewise for the Knight 1880). Cite by NARA microfilm publication + roll + ED + sheet + line so the record can be re-pulled cleanly. Then update the Mary Knight, Laurence Higgins, and James E. Higgins bios with the new sourced detail.

## Quick-reference Q&A

| Open question | Census | Field that answers it |
|---|---|---|
| Is "Porter" the real Newark occupation? | 1900 | Occupation column |
| Mary's birth year: 1866 or 1863? | 1900 | Month/year of birth |
| Did the 1883 Dublin ceremony happen? | 1900 | Years married |
| Did "Margaret c. 1882" exist? | 1900 | Mother of X children / X living |
| When did Laurence emigrate? | 1900 | Immigration year |
| When did Mary emigrate? | 1900 | Immigration year |
| Is Laurence a US citizen by 1900? | 1900 | Naturalization status |
| Is the Newark 1880 Knight household real? | 1880 | The whole household roster |
| Are Mary Rebertha and Elizabeth twins or a duplicate? | 1880 | Two ~age-1 daughters or one |
| Knight head's occupation? | 1880 | Occupation column |

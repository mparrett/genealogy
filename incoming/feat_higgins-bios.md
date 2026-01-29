# Feature: Write Higgins Line Biographies

## Summary

Create biography pages for the three Higgins line ancestors who are currently missing from the published reports.

## Background

We have 10 published bios covering the Mowery, Kuthe, and Gleeson/Fitzgerald lines, but none for the Higgins/Knight line. Extensive research already exists in `research/higgins-ancestry-summary.md` with enough detail to write compelling narratives.

## People to Write

### 1. Laurence Higgins (1854–bef. 1930)
**Relationship:** 2nd great-grandfather

**Key facts:**
- Born 8 Jan 1854, Rathmines, Dublin, Ireland
- Parents: James Higgins + Jane Eustace
- First wife: Mary Verner (died 1881 in Dublin)
- Second wife: Mary Knight (married 1883 Dublin, again 1887 NYC)
- Occupation: Porter, later Janitor in Newark, NJ
- Immigration: Liverpool → New York (date uncertain)
- Death: Before 17 Feb 1930 (wife admitted to almshouse as "widowed")

**Story angles:**
- Dublin working-class origins
- Loss of first wife, remarriage
- Building a life in Newark as a porter
- Large family (children from two marriages)

**Image ready:** `images/laurence-higgins-newark.png`

---

### 2. Mary Knight (1866–1930)
**Relationship:** 2nd great-grandmother

**Key facts:**
- Born Aug 1866, Co. Sligo, Ireland
- Parents: James Knight + Bridget Larney
- In Newark by 1880 (age 14, single)
- Married Laurence Higgins twice (1883 Dublin, 1887 NYC)
- Children: Margaret, Mary A, Lawrence (infant), James Everett, Theresa
- Mother Bridget died 1894 in Newark
- Death: 27 March 1930, NYC almshouse (shortly after husband's death)
- Burial: Holy Name Cemetery, NYC

**Story angles:**
- Rural Sligo origins → urban Newark
- The mystery of two weddings (Dublin 1883, NYC 1887)
- Raising children in Newark's immigrant community
- Tragic end in almshouse after husband's death

**Image ready:** `images/mary-knight-sligo-nyc.png`

---

### 3. James Everett Higgins (1892–1938)
**Relationship:** Great-grandfather

**Key facts:**
- Born 2 Feb 1892, Manhattan, New York
- Parents: Laurence Higgins + Mary Knight
- Age 13: In St Agatha's Home For Children (orphanage) with sister Theresa
- Career: Civil Engineer, Western Pacific Railroad
- WWI: Enlisted July 1918, discharged June 1919
- First marriage: c. 1914 Spokane (wife unknown)
- Second marriage: Doris Pauline Kuthe, 1926 Phoenix (divorced 1928)
- Son: Howard Robert Higgins (1927), later raised by Birch family
- Death: 6 July 1938, San Francisco — suicide in jail lodger's cell during financial troubles

**Story angles:**
- Childhood hardship (orphanage)
- Self-made engineer on the Western railroads
- WWI service
- Marriage to Doris Kuthe (connects Higgins and Kuthe lines!)
- Tragic end during Depression

**Image ready:** `images/railroad-wwi-era.png`

---

## Implementation Notes

1. Use existing bio template style (see `research/templates/report-template.md`)
2. Create markdown in `research/reports/`, generate HTML with `just build-reports`
3. Consider adding inline watercolor illustrations using the bio-illustration pipeline
4. Update `index.html` to link the new bios (images already have CSS classes: `.lhiggins`, `.mknight`, `.jehiggins`)

## Illustration Ideas

For the bio-illustration pipeline (Stage 2+3):

**Laurence:**
- Image 1: Dublin departure / emigration
- Image 2: Newark porter life (already have background image, could adapt)

**Mary:**
- Image 1: Sligo cottage / rural Ireland
- Image 2: Newark tenement life / immigrant community

**James Everett:**
- Image 1: Railroad engineering in the West
- Image 2: WWI service / military camp

## Priority

Medium — the data is ready, just needs narrative writing. James Everett's story is the most compelling and complex.

## References

- `research/higgins-ancestry-summary.md` — primary source data
- `research/higgins-research-prompt.md` — research context
- `assets/bear/higgins-research.md` — Bear notes

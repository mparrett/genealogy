# Croagh marriage register — image sweep for a Margaret Molony marriage

**Date:** 2026-08-20
**Register:** NLI microfilm 02420/06 = `vtls000634972`, Croagh (Kilfinny), marriages **9 Jan 1844 – 27 Feb 1881**, 28 images
**Purpose:** the falsifying test in `margaret-moloney-two-candidates.md` §5 — did **Margaret Moloney, bapt. 21 Oct 1840** (daughter of Michael Molony × Honora Minihan of Ballymackeamore, candidate **B**) marry someone other than Patrick Gleeson?

---

## ✅ Method validated by a control

The sweep found **our own marriage** exactly where it should be, at the foot of frame 14:

> **Nov. 18 [1860] — Patritius Gleeson de Croom & Maria Moloney de Kilfenny in Matrimonio Conjuncti sunt, habita dispensatione tam in Banniis quam in 3tio & 4to gradu Consanguinitatis**

This confirms the rendering pipeline reads this hand reliably, and independently re-verifies the 1860 transcription already in `facts.md` — including the **"Maria"** spelling for Margaret, which matters below.

⚠️ **The `gon.pages_metadata` frame numbers do NOT map 1:1 onto the IIP image filenames for this register.** Metadata called image 14 "May 1859 to Nov 1860"; the actual image 14 runs 1851→Nov 1860. A date map was built empirically instead:

| Image | Year reached |
|---|---|
| f14 | 1851 → **Nov 1860** |
| f15 | Nov 1860 – Jan 1862 |
| f16 | 1862 – Feb 1863 |
| f17 | 1863 – Feb 1870 *(page mixes years)* |
| f18 | 1864 – Feb 1866 |
| f19 | 1866 – Mar 1867 |
| f20 | 1867 · f22 1870 · f24 1872 · f26 1876 |

---

## Coverage achieved

**Frames 14 (lower half) through 19, read in full at ~1× with grayscale/contrast** — every entry on both pages, three vertical bands per frame.

**That covers roughly September 1860 to March 1867.**

⚠️ **Frames 20–25 (c. 1867–1876) are NOT yet swept.** The 1840 Margaret would be 27–36 across that span — less likely than her early twenties, but far from impossible. **This sweep is incomplete and must not be cited as a negative result for the whole register.**

---

## Result: exactly ONE Molony bride in the covered span

> **Sept. 13 [1865] — Michael Riordan et Maria Molony in Mat[rimoni]o conjuncti fuerunt a Rev.do J. B. Meehan, coram Jacobo McDonnell et Brigida Fahy**

Read at high magnification to confirm. **No townland and no father is given** — the register supplies neither.

### Is this candidate B?

**Genuinely uncertain, and the ambiguity is structural.**

- The forename reads **Maria** — Latin for *Mary*, not *Margaret* (which would be *Margarita*, a visibly longer word). On its face this is a Mary Molony.
- **But the same register wrote our own Margaret as "Maria Moloney" in 1860.** `facts.md` already flags that as "a lone scribal slip", corrected by three baptisms, two censuses, the 1918 deed and the 1922 death record — all of which read *Margaret*. If the priest did it once he could do it twice.
- A woman born October 1840 would be **24** in September 1865 — a wholly ordinary marrying age.

**Recorded as: a possible but unconfirmed match for candidate B. It does not settle the test.**

Everything else in the covered span was checked and is not Molony: Hartigan, Hayes, O'Connor, Sheehy, English, Walsh, Nunan, Leen, Doody, Gorman, Berkley, Hannan, Frawley, Dempsey, Dillon, Fitzgerald, Quinlan, Guiry, Connors, Conway, Mackessy, Dundon, Morrissey, Masterson, Lenahan, Heffernan, Murphy, Kelly, Enright, Dee, Kinnealy, Storen, Moran, Riordan, Cullhane, Smyth, Curran/O'Shea, Hogan, Quin, Bourke, McMahon, Collins.

*(Incidental: **7 February 1866, Eugenius McGrath et Mariana Curran alias O'Shea, de **BALLYMACAMORE*** — the same townland as Jeremiah Molony. Not a Molony, but confirms the register does record that townland when it chooses to.)*

---

## ⚠️ The important finding: this instrument is blunter than expected

**The Croagh marriage register names no fathers and often no townland.** Even a clean hit on "Margarita Molony" could not be attributed to Michael-of-Ballymackeamore rather than James-of-Croagh. The register can *locate* candidate marriages; it cannot *identify* them.

**Civil registration is the sharper tool, and most of the target window falls inside it.** Civil marriage certificates from **1864** name **both fathers** with their occupations. Candidate B turned 24 in 1864 — so the bulk of her plausible marrying years (24 to 40) are covered by records that would answer the question outright.

### Revised plan for the falsifying test

1. ⭐ **Civil marriage index, Rathkeale SRD (which contains Croagh and Kilfinny), 1864–1885** — every Margaret Molony/Moloney/Maloney. Open each certificate; the one naming **father Michael Molony** is candidate B, and finding her married to anyone settles the question. **This is now the leading route.**
2. **The 1865 Riordan marriage** — check the civil index for a Michael Riordan × Mary/Margaret Molony marriage registered Sept 1865 in Rathkeale. Civil registration began 1 January 1864, so this marriage *should* have a civil counterpart naming her father.
3. **Finish frames 20–25** only if the civil route fails.
4. **1901/1911 censuses for Ballymackeamore** — if she married locally and stayed, she is findable under a married surname near Jeremiah.

---

## 🔧 Method notes

- **IIP path for this register:** `FIF=000640000/000634972/vtls000634972_NNN.jp2&CVT=JPG`.
- **Do not trust `gon.pages_metadata` frame numbers for this register** — build the date map empirically. A cheap way: composite the top-left corner of six frames into one labelled montage canvas and read the years in a single screenshot.
- **Rendering budget:** at 1450 px canvas width for a 1500 px two-page spread (~0.97×) the hand is readable for surname-spotting, and the capture viewport shows ~34% of page height. **Three bands per frame** (y = 0.02, 0.34, 0.66) gives complete coverage. Two bands leaves the bottom ~14% unseen — a real gap that cost a re-run here.

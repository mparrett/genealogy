# Project Overview

A genealogy research website hosted on GitHub Pages at https://mparrett.github.io/genealogy. Markdown biographies are converted to styled HTML with a vintage/sepia aesthetic.

## Structure

```
index.html                      # Homepage, organized by family branch
research/reports/*.md           # Source markdown biographies (11)
research/reports/html/          # Generated HTML output
convert_md.py                   # Mistune-based MD→HTML converter with embedded CSS
justfile                        # Build automation
pdf/                            # PDF research reports
images/                         # Vintage-style illustrations
research/templates/             # Template for new reports
```

## Content

Published biographies across three family lines:

### Mowery Line (Tennessee → Texas → Arizona)

| Person | Dates | Relationship |
|--------|-------|--------------|
| Lewis R. Mowery | c. 1801–c. 1850 | 4th great-grandfather |
| Elizabeth "Betsy" Lisbee Mowery | c. 1806–1859 | 4th great-grandmother |
| Moses Mansfield Mowery | 1822–1904 | 3rd great-grandfather |
| Pleasant A. Mowrey | b. c. 1820s/1830s | 3rd great-granduncle (collateral) |

### Kuthe Line (Missouri → Oregon → Arizona)

| Person | Dates | Relationship |
|--------|-------|--------------|
| Frederick Kuthe | c. 1822–1900 | 3rd great-grandfather |
| George Washington Kuthe | 1869–1925 | 2nd great-grandfather |
| Huldah Imogene (Bridgefarmer) Kuthe | 1873–1907 | 2nd great-grandmother |

### Gleeson/Fitzgerald Line (Ireland → Wisconsin → Arizona)

| Person | Dates | Relationship |
|--------|-------|--------------|
| James Fitzgerald | 1828–1899 | 3rd great-grandfather |
| Maria Ann Fitzgerald | 1865–1916 | 2nd great-grandmother |
| James J. Gleeson | 1863/1864–1946 | 2nd great-grandfather |

## Build

```bash
just build-reports   # Convert all markdown reports to HTML
just build-report X  # Convert a specific report
just serve           # Local preview on port 8000
just clean           # Remove generated HTML
```

The converter runs via `uvx --from mistune python convert_md.py --all`, producing self-contained HTML documents with full inline CSS (no external dependencies).

## Conventions

- **Relationship badges** on each biography (direct ancestor vs. collateral)
- **Markdown footnotes** for source citations (census records, Find a Grave, etc.)
- **Research Notes** sections flag incomplete work and next steps
- **Vintage design** palette: browns (#7a3a0f), greens (#2c5530), golds (#d4a574), sepia gradients
- **Homepage** uses expandable `<details>` sections per family line, with avatar cards linking to HTML reports and PDFs

## Deployment

Push to `main` branch deploys automatically via GitHub Pages.

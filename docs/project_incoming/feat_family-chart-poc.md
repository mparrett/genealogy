# Feature: Family Chart Library POC

**Date**: 2026-01-26
**Status**: POC Complete - Recommended

## Summary

Evaluate [donatso/family-chart](https://github.com/donatso/family-chart) for interactive family tree visualization on the genealogy site.

## Goals

1. Assess suitability for displaying family tree data
2. Test with sample data from one family line (e.g., Gleeson or Mowery)
3. Determine integration approach with existing GitHub Pages site

## Tasks

- [x] Review library documentation and examples
- [x] Set up minimal POC with sample family data
- [x] Test responsiveness and mobile support
- [x] Evaluate data format requirements (JSON structure)
- [ ] Consider how to maintain data (manual JSON vs. generated from other sources)
- [x] Document findings and recommendation

## POC Results

### Working POC Location
- `poc/family-tree/index.html` - Interactive tree visualization
- `poc/family-tree/mowrey-data.json` - Sample data (21 people, 7 generations)

### To Test Locally
```bash
just serve  # or python3 -m http.server 8000
# Then visit http://localhost:8000/poc/family-tree/
```

### Technical Findings

**Dependencies:**
- D3.js v7 (required, not bundled)
- family-chart v0.9.0 (103KB minified)
- Both available via CDN - no build step needed

**Data Format:**
```json
{
  "id": "unique_id",
  "data": {
    "first name": "Name",
    "last name": "Surname",
    "birthday": "1900",
    "death": "1980",
    "gender": "M"
  },
  "rels": {
    "spouses": ["spouse_id"],
    "parents": ["parent1_id", "parent2_id"],
    "children": ["child_id"]
  }
}
```

**Key API Methods:**
- `f3.createChart(selector, data)` - Initialize
- `.setCardHtml()` / `.setCardSvg()` - Card rendering mode
- `.setCardDisplay([['field1'], ['field2']])` - Configure displayed fields
- `.setCardXSpacing(px)` / `.setCardYSpacing(px)` - Layout
- `.updateTree({initial: true})` - Render

**Styling:**
- Uses CSS variables for colors (`--male-color`, `--female-color`, etc.)
- Cards styled via `.f3 div.card-*` classes
- Links styled via `.f3 .link`
- Integrates well with vintage/sepia theme

### Responsiveness

| Viewport | Result |
|----------|--------|
| Desktop (1400x900) | Excellent - full tree visible |
| Tablet (768x1024) | Good - tree readable, pan/zoom works |
| Mobile (390x844) | Acceptable - requires zoom, touch gestures work |

### Pros
- No build step required (CDN-friendly)
- Interactive pan/zoom/click navigation
- Supports both HTML and SVG card rendering
- Customizable styling with CSS variables
- MIT licensed
- Active development (v0.9.0, updated regularly)

### Cons
- Documentation is sparse (had to reverse-engineer from examples)
- D3 dependency not bundled (must load separately)
- Some API methods changed between versions
- Initial zoom level not configurable (starts zoomed out for large trees)

## Recommendation

**Proceed with integration.** The library works well for visualizing the Mowrey/Birch family tree and would complement the existing biography pages.

### Suggested Next Steps

1. **Add to main site**: Create `/tree/` page linking from index.html
2. **Expand data**: Add missing family lines (Parrett, Kemp, etc.)
3. **Link to bios**: Add click handler to open biography pages
4. **Improve mobile**: Consider reducing card size for small screens

### Data Maintenance Options

1. **Manual JSON**: Edit `mowrey-data.json` directly (current approach)
2. **GEDCOM conversion**: Write script to convert existing GEDCOM files
3. **CSV/spreadsheet**: Create simple CSV format, convert to JSON

Manual JSON is fine for initial deployment; conversion scripts can come later if the tree grows significantly.

## Links

- Library: https://github.com/donatso/family-chart
- Demo: https://donatso.github.io/family-chart-doc/
- POC: `poc/family-tree/`

# Decisions

<!-- Format:
## ADR-001: Decision Title (YYYY-MM-DD)

**Context**: Why the decision was needed
**Decision**: What was chosen
**Alternatives**: What else was considered
**Consequences**: Trade-offs accepted
-->

## ADR-001: Bio Layout System (2026-01-29)

**Context**: Bios combine multiple visual elements—location panels, inline watercolor illustrations, and narrative text. Early attempts with full-width images and floated asides created awkward gaps and competing elements.

**Decision**: A flexible system with configurable placement:

1. **Location asides** (vertical or horizontal layout):
   - `vertical`: 33% width, floated right, image on top—compact, good for shorter descriptions
   - `horizontal`: 50% width, floated right, image left + text right (1:1.6 ratio)—better for longer descriptions
   - `after_paragraph: N` controls injection point per bio

2. **Inline images**:
   - `float-left` / `float-right`: 50% width for major illustrations
   - `float-left-sm` / `float-right-sm`: 33% width for secondary images
   - Position varies per bio based on narrative flow

**Why it works**:
- Alternating float directions (left/right) creates visual rhythm
- Smaller images (33%) don't overwhelm text on narrower viewports
- Location asides at strategic points reinforce geographic context without interrupting narrative
- Consistent vintage styling (border-left accent, warm gradients) unifies varied layouts

**Consequences**: Each bio requires manual tuning of image positions and aside placement. This is acceptable—bios are authored infrequently and benefit from individual attention to layout.

## ADR-002: Narrative vs Structured Bio Format (2026-01-29)

**Context**: Early bios (Lewis Mowery, Elizabeth Lusby Mowery) used a structured format with H3 section headers (`### Family Origins`, `### Marriage and Settlement`, etc.), bullet lists, and explicit research notes. Later bios (James Fitzgerald, James E. Higgins) evolved toward a flowing narrative style without section headers.

**Decision**: Adopt narrative format as the default for new bios. Preserve structured bios in git history but consider converting them over time.

**Rationale**:
1. **Layout compatibility**: CSS rule `h3 { clear: both; }` breaks float wrapping around images/asides. Narrative bios without H3 headers allow images to float naturally with text wrapping.
2. **Reading experience**: Narrative prose is more engaging for genealogy storytelling. Section headers create a choppy, reference-manual feel.
3. **Print book potential**: Narrative format translates better to a future print book compilation.

**Alternatives considered**:
- Modify CSS to not clear floats on H3 → Would affect all H3s, including intentional section breaks
- Use a different heading level → Inconsistent with site hierarchy
- Keep both formats → Creates maintenance burden and inconsistent experience

**Consequences**:
- Existing structured bios (Lewis Mowery, Elizabeth Lusby Mowery) will need rewriting if we want consistent layout
- Research notes and source citations move to a `**Notes:**` section at the end (still preserved, just integrated differently)
- Structured format remains available for future use cases (e.g., research-focused reports vs narrative bios)

**Migration**: No immediate action required. Structured bios remain functional; they just don't benefit from float-based layout features. Convert opportunistically when revisiting older bios.

## ADR-003: Bio Header "Relationship" Line (2026-01-30)

**Context**: Bios currently include a "Relationship: Great-grandfather (Mowrey line)" line below the name. This provides context but may be redundant once readers navigate from line-specific index pages.

**Status**: Under consideration. Keep for now, may remove or replace with something else in the future.

**Options**:
- Remove entirely (relationship clear from navigation context)
- Replace with birth/death dates in a styled format
- Replace with a brief tagline or role description
- Keep as-is

## ADR-004: Draft Mode for Bios (2026-01-30)

**Context**: Some bios are incomplete or need review before public visibility.

**Decision**: Add `draft: true` to timeline-data YAML files. The `--production` flag skips drafts during build.

**Usage**:
- `just build-reports` — builds all including drafts
- `just build-production` — skips drafts
- Draft links are hidden from family_links sections in production

## ADR-005: Image Optimization Pipeline (2026-02-01)

**Context**: AI-generated images (DALL-E) are 1024x1024 PNGs, often 2MB+. Watercolor-style images compress poorly as PNG.

**Decision**: Convert bio images to JPEG (quality 85) after generation. Thumbnails resize to 400x400.

**Process**:
```bash
# Convert to JPEG
uv run --with pillow python -c "from PIL import Image; img = Image.open('file.png'); img.convert('RGB').save('file.jpg', 'JPEG', quality=85)"
# Update markdown refs from .png to .jpg
```

**Results**: ~2MB PNG → ~300KB JPEG (85% reduction)

## ADR-006: Markdown Table Support (2026-02-01)

**Context**: Migration timeline tables rendered as raw markdown (pipe characters) instead of HTML tables.

**Decision**: Add `'table'` plugin to mistune in convert_md.py.

**Fix**: `plugins=['footnotes', 'table']`

## ADR-007: Canonical Bio Heading and Title Extraction (2026-02-07)

**Context**: Bio markdown files had inconsistent first headings (`## Biography of ...`, `### **Name**`, leading blank lines), which led to inconsistent semantic structure and brittle HTML `<title>` values.

**Decision**:
- For all bios (files with a matching `research/reports/timeline-data/<stem>.yml`), the first non-empty line is a single H1: `# Person Name (dates)`.
- H1 text should not be wrapped in markdown emphasis (`**...**`) and should avoid boilerplate prefixes like `Biography of`.
- `convert_md.py` extracts titles from the first heading at any level as a fallback-safe mechanism.

**Consequences**:
- Bio source files are easier to audit and keep consistent.
- Generated HTML titles and heading hierarchy are stable across the site.
- Future drift is reduced by explicit convention in `CLAUDE.md`.

## ADR-008: Canonical Bio Filename Stem (2026-02-07)

**Context**: One bio used an outlier stem (`Moses_Mansfield_Mowery_1822-1904_Biography`) that diverged from the standard bio naming pattern and made references harder to maintain.

**Decision**:
- Bio files use lowercase snake-case stems with `_bio` suffix.
- Report markdown, timeline YAML, and generated HTML use the same stem.
- Example canonical stem: `moses_mansfield_mowery_bio`.

**Consequences**:
- Link references in line data and family links are more predictable.
- Renames become mechanical and less error-prone.

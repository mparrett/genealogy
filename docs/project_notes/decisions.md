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

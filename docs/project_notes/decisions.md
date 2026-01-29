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

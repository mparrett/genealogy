# Feature: Bio Page Timeline Sidebar (POC)

## Summary

Explore adding a floating/sticky sidebar timeline to biography pages that visualizes the subject's life within a broader historical context (roughly 1700–present).

## Concept

As readers scroll through a bio, a vertical timeline in the margin would:
- Show the full date range (1700–present or similar)
- Highlight the subject's lifespan as a colored segment
- Mark key life events (birth, marriage, immigration, death)
- Possibly show historical context markers (Famine, Civil War, WWI, etc.)

## Why This Could Be Useful

1. **Temporal orientation** — Readers can instantly see "when" someone lived relative to other ancestors
2. **Life event visualization** — Quick scan of major milestones
3. **Cross-reference potential** — Could eventually link timelines across bios (e.g., "Maria was born the same year James emigrated")
4. **Historical context** — Understand the person's life against major events

## Open Questions

- **Scope:** Full timeline (1700–present) or just the subject's era with padding?
- **Interactivity:** Click to jump to that section of bio? Hover for details?
- **Data source:** Extract dates from bio text? Separate structured data file?
- **Mobile:** Hide on small screens? Collapse to horizontal?
- **Positioning:** Right sidebar? Left margin? Fixed or scrolls with content?

## Visual Ideas

```
                                    │
     1700 ─────────────────────────┤
                                    │
                                    │
     1800 ─────────────────────────┤
            ┌──────────────────────┤ 1828 Born (Limerick)
            │ ████████████████████ │
            │ █ JAMES FITZGERALD █ │ 1854 Married Margaret
            │ ████████████████████ │ 1865 Daughter Maria born
            └──────────────────────┤ 1899 Died (Wisconsin)
     1900 ─────────────────────────┤
                                    │
                                    │
     2000 ─────────────────────────┤
                                    │
```

Alternative: Compact version showing just lifespan + key events

```
┌─────────────────────────┐
│  1828 ● Born            │
│       │                 │
│  1854 ● Married         │
│       │                 │
│  1865 ○ Maria born      │
│       │                 │
│  1899 ● Died            │
└─────────────────────────┘
```

## Implementation Considerations

### Data Structure

Could add frontmatter or a companion JSON file per bio:

```yaml
---
name: James Fitzgerald
birth: 1828
death: 1899
events:
  - year: 1850
    label: Emigrated
    type: migration
  - year: 1854
    label: Married Margaret
    type: marriage
  - year: 1865
    label: Maria born
    type: child
---
```

### CSS Approach

- `position: sticky` for the sidebar
- CSS-only version possible for static timelines
- JS needed for scroll-linked highlighting

### Progressive Enhancement

- Static timeline works without JS
- JS adds scroll-linked highlighting and interactivity
- Falls back gracefully on mobile (hide or reposition)

## Prior Art / Inspiration

- Wikipedia article timelines
- NY Times multimedia story sidebars
- Ancestry.com profile timelines
- Museum exhibit chronologies

## Scope for POC

Start simple:
1. Pick one bio (James Fitzgerald?)
2. Manually create the timeline data
3. Build a sticky sidebar with CSS
4. Add basic markers for birth/death + 2-3 events
5. No JS interactivity initially

## Success Criteria

- Timeline visually complements the bio without distracting
- Key dates are easy to scan
- Works on desktop (mobile can be deferred)
- Doesn't require changes to markdown content (data lives elsewhere)

## Future Possibilities

- Cross-bio timeline view (see all ancestors on one timeline)
- Historical event overlay (Famine, wars, etc.)
- Generation indicators
- Click-to-navigate within bio
- Animated scroll highlighting

## Priority

Low — this is exploratory/enhancement. Core bios and research are higher priority.

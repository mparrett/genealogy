# Development Notes

## ChatGPT 4o Image Designer Prompts

### Base Template for Genealogy Graphics

Use this template for all genealogy-related graphics to ensure consistency:

```
Create a vintage-style illustration representing [SPECIFIC TOPIC/PERIOD]. The design should be suitable for use as either a background element or icon in genealogy research reports. Include elements like:

- [SPECIFIC ELEMENTS FOR THIS TOPIC/PERIOD]
- [GEOGRAPHIC/HISTORICAL DETAILS]
- [RELEVANT ACTIVITIES/OBJECTS]
- Warm, earthy color palette (browns, golds, muted greens)
- Soft, aged appearance with slight sepia tones

Style: Historical illustration with a clean, not overly detailed approach that works well as a background element. The design should feel authentic to the [TIME PERIOD] but remain legible and not too busy when used behind text.

CONSISTENCY REQUIREMENTS (use for all genealogy graphics):
- Maintain the same vintage illustration style with sepia/aged tones
- Use consistent warm, earthy color palette across all images
- Keep the same level of detail and artistic approach
- All graphics should complement each other as part of a cohesive genealogy research collection
- Ensure typography and decorative elements (if any) match this historical aesthetic

Format: Square aspect ratio, suitable for web use. The design should work both as a subtle background and as a standalone decorative element.
```

### Example: Texas Farming 1820s-1830s

```
Create a vintage-style illustration representing Texas farming in the 1820s-1830s period. The design should be suitable for use as either a background element or icon in genealogy research reports. Include elements like:

- Rolling hills or open prairie landscape typical of 1820s Texas
- A simple wooden farmhouse or cabin with a stone chimney
- Split-rail fencing
- A horse-drawn plow or oxen working the fields
- Perhaps a covered wagon in the distance to represent westward migration
- Warm, earthy color palette (browns, golds, muted greens)
- Soft, aged appearance with slight sepia tones

Style: Historical illustration with a clean, not overly detailed approach that works well as a background element. The design should feel authentic to the 1820s-1830s Texas frontier period but remain legible and not too busy when used behind text.

CONSISTENCY REQUIREMENTS (use for all genealogy graphics):
- Maintain the same vintage illustration style with sepia/aged tones
- Use consistent warm, earthy color palette across all images
- Keep the same level of detail and artistic approach
- All graphics should complement each other as part of a cohesive genealogy research collection
- Ensure typography and decorative elements (if any) match this historical aesthetic

Format: Square aspect ratio, suitable for web use. The design should work both as a subtle background and as a standalone decorative element.
```

## Project Structure

- `/pdf/` - PDF research reports
- `/research/reports/` - Markdown source files for reports
- `/research/reports/html/` - Generated HTML from markdown
- `/research/templates/` - Templates for new reports

## Build Commands

- `just build-reports` - Convert all markdown reports to HTML
- `just build-report <filename>` - Convert specific report
- `just clean` - Remove generated HTML files
- `just serve` - Start local preview server
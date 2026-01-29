# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A genealogy research website hosted on GitHub Pages at https://mparrett.github.io/genealogy. Reports are written in Markdown and converted to HTML for web viewing.

## Build Commands

```bash
# Convert all markdown reports to HTML
just build-reports

# Convert a specific report (without .md extension)
just build-report <filename>

# Preview site locally
just serve

# Clean generated HTML
just clean
```

The build uses `uvx --from mistune python convert_md.py` to run the converter with the mistune dependency.

## Project Structure

- `research/reports/*.md` - Source markdown reports (biographies, research findings)
- `research/reports/html/` - Generated HTML (do not edit directly)
- `research/templates/report-template.md` - Template for new reports
- `pdf/` - PDF research reports
- `convert_md.py` - Markdown to HTML converter with custom CSS styling
- `index.html` - Main site homepage (manually maintained)
- `PROMPTS.md` - ChatGPT image generation prompts for vintage-style illustrations

## Workflow

1. Create new reports in `research/reports/` using the template
2. Run `just build-reports` to generate HTML
3. Manually update `index.html` to link new reports
4. Commit and push to deploy via GitHub Pages

## Content Guidelines

Reports use Markdown footnotes for citations. The HTML converter applies custom vintage-style CSS with sepia tones appropriate for genealogy content.

## Bio Layout Components

Bios support several layout components configured via YAML files in `research/reports/timeline-data/<bio_name>.yml`.

### Inline Images (in Markdown)

Use CSS classes directly on `<img>` tags:

| Class | Width | Position |
|-------|-------|----------|
| `float-right` | 50% | Right |
| `float-left` | 50% | Left |
| `float-right-sm` | 33% | Right |
| `float-left-sm` | 33% | Left |

```html
<img src="../../../images/bio/example.png" alt="Description" class="float-right-sm">
```

### YAML-Configured Components

Create `research/reports/timeline-data/<bio_name>.yml` to enable these features:

#### Timeline Sidebar

Fixed sidebar showing life events (visible on wide screens):

```yaml
name: Person Name
birth:
  year: 1892
  label: Born
  location: Place
death:
  year: 1938
  label: Died
  location: Place
events:
  - year: 1918
    label: Event description
    type: event  # or 'marriage'
```

#### Location Aside

Floating panel with location image and description:

```yaml
location_aside:
  place: Feather River Canyon
  region: California
  year: c. 1915
  image: locations/feather-river-canyon-1915.png  # relative to images/
  layout: vertical  # or 'horizontal'
  after_paragraph: 3  # insert after Nth paragraph
  description: >
    Optional descriptive text about the location's
    significance to the person.
```

- **vertical** (default): 33% width, image above text
- **horizontal**: 50% width, image left of text

#### Family Links

Cards linking to related bios (appears before Notes section):

```yaml
family_links:
  - name: Person Name
    relation: Father
    link: person_bio.html
```

### Image Types

| Type | Location | Style | Use |
|------|----------|-------|-----|
| Bio illustrations | `images/bio/` | Watercolor | Inline narrative scenes |
| Location panels | `images/locations/` | Engraving + watercolor wash | Location asides, context |

See `PROMPTS.md` for image generation prompts.

## Project Memory

Memory files live in `docs/project_notes/`.

**Before proposing changes**: Check `decisions.md` for existing ADRs
**When encountering errors**: Search `bugs.md` for known solutions
**When looking up config**: Check `key_facts.md` for ports, URLs, environments

When resolving bugs or making decisions, update the relevant file.

## Bear Notes Sync

Research prompts and notes are maintained in Bear and mirrored to `assets/bear/` for version control.

### Directory Structure

```
assets/bear/
├── higgins-research.md      # Higgins/Knight line research prompt
├── higgins-deep-research.md # Higgins deep research questions
├── gleeson-research.md      # Gleeson/Fitzgerald research prompt
└── gleeson-deep-research.md # Gleeson deep research questions
```

### Bear CLI Commands

```bash
# Search for notes
bear search "<term>"

# Export note to file (includes bear_uuid in frontmatter)
bear export-note --uuid "<uuid>" --output "<path>"

# Update Bear from local file (requires bear_uuid in frontmatter)
bear update-note --file "<path>"

# Get note content to stdout
bear get-note --uuid "<uuid>"
```

### Sync Workflow

**When updating a research note:**
1. Make edits to `assets/bear/<note>.md`
2. Run `bear update-note --file assets/bear/<note>.md` to push to Bear
3. Commit the local file

**When Bear has newer content:**
1. Export: `bear export-note --uuid "<uuid>" --output assets/bear/<note>.md`
2. Review diff with `git diff`
3. Commit if changes are intentional

**When creating a new research note:**
1. Create in Bear first (to get UUID)
2. Export to `assets/bear/` with descriptive filename
3. Commit the new file

### Key Note UUIDs

| Note | UUID |
|------|------|
| Higgins Research | `0593C530-E296-4934-99D6-6E23B8D1172B` |
| Higgins Deep Research | `3066BF31-1FAA-4342-A060-D34F1460A44A` |
| Gleeson Research | `0DEA9B4E-6E21-48EC-AB24-2699EA2CE87F` |
| Gleeson Deep Research | `4F423776-2BC2-4F01-98FF-563DFF24301B` |

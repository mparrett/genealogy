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

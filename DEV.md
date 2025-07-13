# Development Notes

## Image Generation
- [Image Generation Prompts](PROMPTS.md)

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
# Genealogy Resources

A collection of genealogy research, reports, and family history documentation.

## 🌐 Live Site
Visit the live site at: https://mparrett.github.io/genealogy

## 📋 Project Structure

```
genealogy/
├── index.html              # Main site homepage
├── research/
│   ├── reports/            # Research reports and documentation
│   └── templates/          # Templates for new reports
├── _config.yml            # Jekyll configuration for GitHub Pages
└── justfile               # Build automation tasks
```

## 🔧 Development

This project uses [Just](https://github.com/casey/just) for task automation:

```bash
# Convert markdown reports to HTML
just build-reports

# List available tasks
just --list
```

## 📚 Adding New Reports

1. Create a new markdown file in `research/reports/`
2. Use the template in `research/templates/report-template.md`
3. Run `just build-reports` to convert to HTML
4. Commit and push to update the live site

## 🏗️ Family Tree Resources

Family tree profiles and genetic genealogy data are maintained across multiple platforms including Ancestry, WikiTree, FamilySearch, and 23andMe. Links to these profiles are available upon request.

## 📖 About

This repository serves as a centralized location for documenting family history research, sharing findings, and maintaining genealogical records. Reports are written in Markdown and automatically converted to HTML for web viewing.

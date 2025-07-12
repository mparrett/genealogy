# Genealogy project tasks

# List all available tasks
default:
    @just --list

# Convert all markdown reports to HTML
build-reports:
    uvx --from mistune python convert_md.py --all

# Convert a specific markdown file to HTML
build-report file:
    uvx --from mistune python convert_md.py --file {{file}}

# Clean generated HTML files
clean:
    rm -rf research/reports/html/
    echo "✅ Cleaned HTML reports"

# Preview the site locally (requires Python)
serve:
    python3 -m http.server 8000

# Update the main site index with new reports
update-index:
    #!/usr/bin/env bash
    set -euo pipefail
    
    echo "📝 Updating site index with new reports..."
    echo "⚠️  This task needs to be implemented - manually update index.html for now"
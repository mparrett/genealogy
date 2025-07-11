# Genealogy project tasks

# List all available tasks
default:
    @just --list

# Convert all markdown reports to HTML
build-reports:
    #!/usr/bin/env bash
    set -euo pipefail
    
    # Create HTML reports directory if it doesn't exist
    mkdir -p research/reports/html
    
    # Convert each markdown file to HTML
    for md_file in research/reports/*.md; do
        if [[ -f "$md_file" ]]; then
            base_name=$(basename "$md_file" .md)
            html_file="research/reports/html/${base_name}.html"
            
            echo "Converting $md_file → $html_file"
            uvx --from mistune python -c "import mistune; import sys; print(mistune.html(open('$md_file').read()))" > "$html_file"
        fi
    done
    
    echo "✅ All markdown reports converted to HTML"

# Convert a specific markdown file to HTML
build-report file:
    #!/usr/bin/env bash
    set -euo pipefail
    
    if [[ ! -f "research/reports/{{file}}.md" ]]; then
        echo "❌ File research/reports/{{file}}.md not found"
        exit 1
    fi
    
    mkdir -p research/reports/html
    uvx --from mistune python -c "import mistune; print(mistune.html(open('research/reports/{{file}}.md').read()))" > "research/reports/html/{{file}}.html"
    echo "✅ Converted {{file}}.md to HTML"

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
# Genealogy project tasks

# List all available tasks
default:
    @just --list

# Convert all markdown reports to HTML
build-reports:
    uvx --from mistune --with pyyaml python convert_md.py --all

# Convert a specific markdown file to HTML
build-report file:
    uvx --from mistune --with pyyaml python convert_md.py --file {{file}}

# Generate all line pages from YAML data
build-lines:
    uvx --with pyyaml python convert_lines.py

# Generate a specific line page
build-line name:
    uvx --with pyyaml python convert_lines.py {{name}}

# Build everything (reports + lines)
build-all: build-reports build-lines

# Build for production (skips drafts)
build-production:
    uvx --from mistune --with pyyaml python convert_md.py --all --production
    uvx --with pyyaml python convert_lines.py --production

# Check for missing bios and PDFs referenced by YAML data
check-links:
    uvx --with pyyaml python check_links.py

# Clean generated HTML files
clean:
    rm -rf research/reports/html/
    echo "✅ Cleaned HTML reports"

# Preview the site locally
serve:
    npx serve . --listen tcp://0.0.0.0:3000

# Extract one or more pages of the Catholic Protectory 1909 PDF at 300 DPI JPEG q=95.
# Output: assets/external/catholic-protectory-1909/page-NNN-hires.jpg next to the 150 DPI source.
# Usage: just protectory-hires 252        # single page
#        just protectory-hires 100-105    # inclusive range
protectory-hires page:
    #!/usr/bin/env bash
    set -euo pipefail
    PDF="${PROTECTORY_PDF:-$HOME/Downloads-no-iCloud/Annual_report_of_the_New_York_Catholic_Protectory_to_the_Legislature_of_the_State,_and_to_the_Common_Council_of_the_City_(IA_annualreportofn4619newy_0).pdf}"
    OUT="assets/external/catholic-protectory-1909"
    if [[ ! -f "$PDF" ]]; then
        echo "PDF not found: $PDF" >&2
        echo "Override with: PROTECTORY_PDF=/path/to/file.pdf just protectory-hires {{page}}" >&2
        exit 1
    fi
    PAGE="{{page}}"
    if [[ "$PAGE" == *-* ]]; then FIRST="${PAGE%-*}"; LAST="${PAGE#*-}"; else FIRST="$PAGE"; LAST="$PAGE"; fi
    for p in $(seq "$FIRST" "$LAST"); do
        pad=$(printf "%03d" "$p")
        src="$OUT/page-$pad.jpg"
        if [[ ! -f "$src" ]]; then echo "skipping page $p (no source $src)"; continue; fi
        echo "→ page $p"
        pdftoppm -jpeg -jpegopt quality=95 -r 300 -f "$p" -l "$p" "$PDF" "$OUT/__tmp_hires"
        # Match the 150 DPI source orientation: landscape sources need 90° CW.
        if [[ "$(magick identify -format '%[fx:w>h?1:0]' "$src")" == "1" ]]; then
            magick mogrify -rotate 90 "$OUT/__tmp_hires-$pad.jpg"
        fi
        mv "$OUT/__tmp_hires-$pad.jpg" "$OUT/page-$pad-hires.jpg"
        echo "   wrote $OUT/page-$pad-hires.jpg"
    done

# Update the main site index with new reports
update-index:
    #!/usr/bin/env bash
    set -euo pipefail

    echo "📝 Updating site index with new reports..."
    echo "⚠️  This task needs to be implemented - manually update index.html for now"

# Generate _drafts.html page listing all draft bios
build-drafts:
    #!/usr/bin/env bash
    set -euo pipefail

    echo "📝 Generating _drafts.html..."

    # Build JSON array of drafts
    drafts="["
    first=true
    for f in research/reports/timeline-data/*.yml; do
        if grep -q "draft: true" "$f"; then
            name=$(basename "$f" .yml)
            title=$(grep "^name:" "$f" | sed 's/name: //')
            if [ "$first" = true ]; then
                first=false
            else
                drafts+=","
            fi
            drafts+="{\"name\":\"$title\",\"file\":\"$name\"}"
        fi
    done
    drafts+="]"

    cat > _drafts.html << HTMLEOF
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Draft Bios - Dev Only</title>
        <style>
            body { font-family: Georgia, serif; max-width: 800px; margin: 2rem auto; padding: 1rem; background: #faf8f5; color: #4a3728; }
            h1 { color: #8b4513; border-bottom: 2px solid #d4a574; padding-bottom: 0.5rem; }
            .warning { background: #fff3cd; border: 1px solid #ffc107; padding: 1rem; border-radius: 4px; margin-bottom: 1.5rem; }
            ul { list-style: none; padding: 0; }
            li { margin: 0.75rem 0; padding: 0.75rem; background: white; border-left: 3px solid #d4a574; }
            a { color: #8b4513; text-decoration: none; font-weight: 500; }
            a:hover { text-decoration: underline; }
            .filename { font-size: 0.85rem; color: #888; font-family: monospace; }
            .back { margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #d4a574; }
        </style>
    </head>
    <body>
        <h1>Draft Bios</h1>
        <div class="warning">⚠️ <strong>Dev only</strong> - These bios are not linked from the main site and are skipped in production builds.</div>
        <ul id="drafts"></ul>
        <div class="back"><a href="index.html">← Back to Family Index</a></div>
        <script>
            const drafts = $drafts;
            const ul = document.getElementById('drafts');
            drafts.forEach(d => {
                const li = document.createElement('li');
                li.innerHTML = \`<a href="research/reports/html/\${d.file}.html">\${d.name}</a><br><span class="filename">\${d.file}.html</span>\`;
                ul.appendChild(li);
            });
        </script>
    </body>
    </html>
    HTMLEOF

    echo "✅ Generated _drafts.html with $(echo "$drafts" | grep -o '{' | wc -l | tr -d ' ') drafts"

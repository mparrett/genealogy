#!/usr/bin/env python3
"""
Markdown to HTML converter for genealogy reports.
"""

import argparse
import mistune
from mistune.renderers.html import HTMLRenderer
import os
import sys
from pathlib import Path


def convert_file(md_file_path, html_file_path):
    """Convert a single markdown file to HTML."""
    try:
        with open(md_file_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Create markdown processor with HTML renderer and footnotes plugin
        renderer = HTMLRenderer(escape=False)
        markdown = mistune.create_markdown(renderer=renderer, plugins=['footnotes'])
        body_content = markdown(markdown_content)
        
        # Extract title from first heading or filename
        title_line = markdown_content.split('\n')[0] if markdown_content.startswith('#') else md_file_path.stem
        title = title_line.lstrip('#').strip() if title_line.startswith('#') else title_line
        
        # Create complete HTML document with inline CSS
        html_document = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        /* Modern CSS Reset */
        *, *::before, *::after {{
            box-sizing: border-box;
        }}
        
        * {{
            margin: 0;
        }}
        
        body {{
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
        }}
        
        img, picture, video, canvas, svg {{
            display: block;
            max-width: 100%;
        }}
        
        input, button, textarea, select {{
            font: inherit;
        }}
        
        /* Typography */
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            font-size: 16px;
            line-height: 1.6;
            color: #2c3e50;
            background-color: #fdfdfd;
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
        }}
        
        h1, h2, h3, h4, h5, h6 {{
            font-weight: 600;
            line-height: 1.4;
            margin-bottom: 1rem;
            color: #1a252f;
        }}
        
        h1 {{ font-size: 2.25rem; margin-bottom: 1.5rem; }}
        h2 {{ font-size: 1.875rem; margin-top: 2rem; }}
        h3 {{ font-size: 1.5rem; margin-top: 1.5rem; }}
        
        p {{
            margin-bottom: 1.25rem;
        }}
        
        strong {{
            font-weight: 600;
            color: #1a252f;
        }}
        
        em {{
            font-style: italic;
            color: #34495e;
        }}
        
        /* Lists */
        ul, ol {{
            margin-bottom: 1.25rem;
            padding-left: 1.5rem;
        }}
        
        li {{
            margin-bottom: 0.5rem;
            line-height: 1.4;
        }}
        
        /* Links */
        a {{
            color: #3498db;
            text-decoration: none;
            border-bottom: 1px solid transparent;
            transition: border-color 0.2s ease;
        }}
        
        a:hover {{
            border-bottom-color: #3498db;
        }}
        
        /* Horizontal Rule */
        hr {{
            border: none;
            height: 1px;
            background: linear-gradient(to right, transparent, #bdc3c7, transparent);
            margin: 2rem 0;
        }}
        
        /* Footnotes */
        .footnote-ref {{
            font-size: 0.85em;
            font-weight: 500;
        }}
        
        .footnote-ref a {{
            color: #e74c3c;
            text-decoration: none;
            border: none;
        }}
        
        .footnote-ref a:hover {{
            color: #c0392b;
        }}
        
        .footnotes {{
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid #ecf0f1;
        }}
        
        .footnotes h3 {{
            font-size: 1.25rem;
            color: #7f8c8d;
            margin-bottom: 1rem;
        }}
        
        .footnotes ol {{
            padding-left: 1.25rem;
        }}
        
        .footnotes li {{
            font-size: 0.9rem;
            line-height: 1.4;
            margin-bottom: 0.75rem;
            color: #5a6c7d;
        }}
        
        .footnotes .footnote {{
            color: #95a5a6;
            text-decoration: none;
            margin-left: 0.5rem;
        }}
        
        .footnotes .footnote:hover {{
            color: #7f8c8d;
        }}
        
        /* Print styles */
        @media print {{
            body {{
                font-size: 12pt;
                line-height: 1.5;
                color: #000;
                background: #fff;
                margin: 0;
                padding: 1in;
            }}
            
            a {{
                color: #000;
                text-decoration: underline;
            }}
        }}
    </style>
</head>
<body>
{body_content}
</body>
</html>"""
        
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(html_document)
        
        print(f"✅ Converted {md_file_path} → {html_file_path}")
        return True
    
    except Exception as e:
        print(f"❌ Error converting {md_file_path}: {e}")
        return False


def convert_all_reports():
    """Convert all markdown files in research/reports/ to HTML."""
    reports_dir = Path("research/reports")
    html_dir = Path("research/reports/html")
    
    # Create HTML directory if it doesn't exist
    html_dir.mkdir(exist_ok=True)
    
    md_files = list(reports_dir.glob("*.md"))
    if not md_files:
        print("No markdown files found in research/reports/")
        return True
    
    success_count = 0
    for md_file in md_files:
        html_file = html_dir / f"{md_file.stem}.html"
        if convert_file(md_file, html_file):
            success_count += 1
    
    print(f"✅ Converted {success_count}/{len(md_files)} markdown files to HTML")
    return success_count == len(md_files)


def main():
    parser = argparse.ArgumentParser(description="Convert markdown genealogy reports to HTML")
    parser.add_argument("--file", "-f", help="Convert specific file (without .md extension)")
    parser.add_argument("--all", "-a", action="store_true", help="Convert all markdown files")
    
    args = parser.parse_args()
    
    if args.file:
        md_file = Path(f"research/reports/{args.file}.md")
        html_file = Path(f"research/reports/html/{args.file}.html")
        
        if not md_file.exists():
            print(f"❌ File {md_file} not found")
            sys.exit(1)
        
        # Create HTML directory if it doesn't exist
        html_file.parent.mkdir(exist_ok=True)
        
        success = convert_file(md_file, html_file)
        sys.exit(0 if success else 1)
    
    elif args.all:
        success = convert_all_reports()
        sys.exit(0 if success else 1)
    
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
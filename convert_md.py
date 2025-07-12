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
        /* CSS Custom Properties */
        :root {{
            --primary: #7a3a0f;      /* Rich brown - evokes old documents */
            --secondary: #2c5530;    /* Deep forest green */
            --accent: #d4a574;       /* Warm gold */
            --text-primary: #2d3748;
            --text-secondary: #4a5568;
            --text-muted: #718096;
            --background: #fefefe;
            --paper: #fcfcfc;        /* Slight warmth */
            --border-light: #e8e5e0;
            --footnote-red: #c53030; /* Warmer red */
        }}
        
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
            color: var(--text-primary);
            background: linear-gradient(135deg, var(--background) 0%, #f8f9fa 100%);
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
            box-shadow: 0 0 40px rgba(122, 58, 15, 0.08);
            border-radius: 8px;
            min-height: 100vh;
        }}
        
        h1, h2, h3, h4, h5, h6 {{
            font-family: Georgia, 'Times New Roman', serif;
            font-weight: 500;
            line-height: 1.5;
            margin-bottom: 1rem;
            color: var(--primary);
        }}
        
        h1 {{ font-size: 2.25rem; margin-bottom: 1.5rem; }}
        h2 {{ font-size: 1.875rem; margin-top: 2rem; }}
        h3 {{ font-size: 1.5rem; margin-top: 1.5rem; }}
        
        /* Add breathing room at the top */
        h1:first-child, h2:first-child, h3:first-child {{
            margin-top: 1rem;
        }}
        
        p {{
            margin-bottom: 1.25rem;
        }}
        
        strong {{
            font-weight: 600;
            color: var(--primary);
        }}
        
        em {{
            font-style: italic;
            color: var(--text-secondary);
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
            color: var(--secondary);
            text-decoration: none;
            background-image: linear-gradient(120deg, transparent 0%, var(--accent) 100%);
            background-repeat: no-repeat;
            background-size: 100% 0px;
            background-position: 0 88%;
            transition: background-size 0.25s ease-in;
        }}
        
        a:hover {{
            background-size: 100% 3px;
        }}
        
        /* Horizontal Rule */
        hr {{
            border: none;
            height: 1px;
            background: linear-gradient(to right, transparent, var(--border-light), transparent);
            margin: 2rem 0;
        }}
        
        /* Genealogy-specific classes */
        .date, .location {{
            font-variant: small-caps;
            letter-spacing: 0.5px;
            color: var(--text-secondary);
        }}
        
        /* Footnotes */
        .footnote-ref {{
            font-size: 0.85em;
            font-weight: 500;
        }}
        
        .footnote-ref a {{
            color: var(--footnote-red);
            text-decoration: none;
            background: none;
        }}
        
        .footnote-ref a:hover {{
            color: #9c1f1f;
        }}
        
        .footnotes {{
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid var(--border-light);
            background-color: var(--paper);
            border-radius: 6px;
            padding: 2rem;
            margin-left: -2rem;
            margin-right: -2rem;
        }}
        
        .footnotes h3 {{
            font-size: 1.25rem;
            color: var(--text-muted);
            margin-bottom: 1rem;
        }}
        
        .footnotes ol {{
            padding-left: 1.25rem;
        }}
        
        .footnotes li {{
            font-size: 0.9rem;
            line-height: 1.4;
            margin-bottom: 0.75rem;
            color: var(--text-secondary);
        }}
        
        .footnotes .footnote {{
            color: var(--text-muted);
            text-decoration: none;
            margin-left: 0.5rem;
        }}
        
        .footnotes .footnote:hover {{
            color: var(--text-secondary);
        }}
        
        /* Responsive Design */
        @media (max-width: 600px) {{
            body {{ 
                padding: 1rem; 
                box-shadow: none;
                border-radius: 0;
            }}
            h1 {{ font-size: 1.875rem; }}
            h2 {{ font-size: 1.5rem; }}
            h3 {{ font-size: 1.25rem; }}
            
            .footnotes {{
                margin-left: -1rem;
                margin-right: -1rem;
            }}
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
                box-shadow: none;
                border-radius: 0;
            }}
            
            a {{
                color: #000;
                text-decoration: underline;
                background: none;
            }}
            
            .footnotes {{
                background: #fff;
                border: 1px solid #ccc;
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
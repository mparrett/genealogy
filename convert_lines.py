#!/usr/bin/env python3
"""Generate line pages from YAML data files."""

import argparse
import sys
from pathlib import Path

import yaml

LINES_DIR = Path(__file__).parent / "lines"
DATA_DIR = LINES_DIR / "data"
REPORTS_DIR = Path(__file__).parent / "research" / "reports"
TIMELINE_DIR = REPORTS_DIR / "timeline-data"
_DRAFT_CACHE: dict[str, bool] = {}


def is_draft_bio(bio_filename: str) -> bool:
    """Return True if the bio is marked draft in its timeline data."""
    if not bio_filename or not bio_filename.endswith(".html"):
        return False
    if bio_filename in _DRAFT_CACHE:
        return _DRAFT_CACHE[bio_filename]

    stem = Path(bio_filename).stem
    md_path = REPORTS_DIR / f"{stem}.md"
    timeline_path = TIMELINE_DIR / f"{stem}.yml"
    if not md_path.exists() or not timeline_path.exists():
        _DRAFT_CACHE[bio_filename] = False
        return False

    with open(timeline_path, "r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    is_draft = bool(data.get("draft", False))
    _DRAFT_CACHE[bio_filename] = is_draft
    return is_draft


def generate_ancestor_card(
    ancestor: dict, is_direct: bool, accent_color: str, production: bool
) -> str:
    """Generate HTML for a single ancestor card."""
    badge_class = "direct" if is_direct else "collateral"

    # Build image CSS class
    img_class = ancestor.get("image_class", "")

    # Build links
    links = []
    bio = ancestor.get("bio")
    bio_is_draft = bool(production and bio and is_draft_bio(bio))
    if bio and not bio_is_draft:
        links.append(f'<a href="../research/reports/html/{bio}">Biography</a>')
    if pdf := ancestor.get("pdf"):
        links.append(f'<a href="../pdf/{pdf}" target="_blank" rel="noopener noreferrer">Report (PDF)</a>')
    links_html = "\n                        ".join(links) if links else ""

    # Image wrapper (linked if bio exists)
    image_html = f'<div class="ancestor-image {img_class}"></div>'
    if bio and not bio_is_draft:
        image_html = f'<a href="../research/reports/html/{bio}">\n                    {image_html}\n                </a>'

    # Links section
    links_section = f'''
                    <div class="ancestor-links">
                        {links_html}
                    </div>''' if links_html else ""

    return f'''            <div class="ancestor-card">
                {image_html}
                <div class="ancestor-content">
                    <div class="ancestor-name">{ancestor["name"]} ({ancestor["years"]})</div>
                    <div class="ancestor-tagline">{ancestor["tagline"]}</div>
                    <span class="ancestor-badge {badge_class}">{ancestor["relation"]}</span>{links_section}
                </div>
            </div>'''


def generate_image_css(ancestors: list, accent_color: str) -> str:
    """Generate CSS for ancestor images."""
    css_lines = []
    for ancestor in ancestors:
        img_class = ancestor.get("image_class", "")
        thumb = ancestor.get("image_thumb", "")
        initials = ancestor.get("initials", "")
        if img_class and thumb:
            css_lines.append(f"""        .ancestor-image.{img_class} {{
            background-image: url('../images/thumbs/{thumb}');
        }}
        .ancestor-image.{img_class}::after {{ content: '{initials}'; }}""")
    return "\n".join(css_lines)


def hex_to_rgba(hex_color: str, alpha: float) -> str:
    """Convert hex color to rgba."""
    hex_color = hex_color.lstrip("#")
    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    return f"rgba({r}, {g}, {b}, {alpha})"


def generate_line_page(data: dict, production: bool) -> str:
    """Generate full HTML page from line data."""
    name = data["name"]
    accent = data["accent_color"]
    migration = data["migration"]
    intro = data["intro"].strip()

    # Collect all ancestors for image CSS
    all_ancestors = data["ancestors"].get("direct", []) + data["ancestors"].get("collateral", [])
    image_css = generate_image_css(all_ancestors, accent)

    # Generate ancestor cards
    direct_cards = "\n\n".join(
        generate_ancestor_card(a, True, accent, production)
        for a in data["ancestors"].get("direct", [])
    )

    collateral_section = ""
    if collateral := data["ancestors"].get("collateral", []):
        collateral_cards = "\n\n".join(
            generate_ancestor_card(a, False, accent, production)
            for a in collateral
        )
        collateral_section = f'''
        <div class="section-header">
            <h2>Collateral Relatives</h2>
        </div>

        <div class="ancestors">
{collateral_cards}
        </div>'''

    # Compute rgba values for borders
    border_muted = hex_to_rgba(accent, 0.25)
    shadow_color = hex_to_rgba(accent.replace("#", "7a3a0f" if accent == "#8b4513" else accent), 0.08)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} · Parrett Family History</title>
    <style>
        :root {{
            --primary: #7a3a0f;
            --secondary: #2c5530;
            --accent: #d4a574;
            --accent-line: {accent};
            --text-primary: #2d3748;
            --text-secondary: #4a5568;
            --text-muted: #718096;
            --background: #faf9f7;
            --paper: #fcfbf9;
            --border-light: #e8e5e0;
        }}

        *, *::before, *::after {{
            box-sizing: border-box;
        }}

        * {{
            margin: 0;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            font-size: 16px;
            line-height: 1.6;
            color: var(--text-primary);
            background-color: var(--background);
            min-height: 100vh;
        }}

        h1, h2, h3 {{
            font-family: Georgia, 'Times New Roman', serif;
            font-weight: 500;
            color: var(--primary);
        }}

        a {{
            color: var(--secondary);
            text-decoration: none;
        }}

        a:hover {{
            text-decoration: underline;
        }}

        .page-wrapper {{
            max-width: 850px;
            margin: 0 auto;
            background: linear-gradient(135deg, #fefefe 0%, #f8f9fa 100%);
            box-shadow: 0 0 40px rgba(122, 58, 15, 0.08);
            border-radius: 8px;
            min-height: 100vh;
        }}

        .container {{
            max-width: 800px;
            margin: 0 auto;
            padding: 0 2rem 2rem;
        }}

        .breadcrumb {{
            padding: 0.75rem 1.5rem;
            max-width: 800px;
            margin: 0 auto;
            font-size: 0.85rem;
            color: var(--text-muted);
        }}

        .breadcrumb a {{
            color: var(--text-muted);
        }}

        .breadcrumb a:hover {{
            color: var(--secondary);
        }}

        .line-header {{
            padding: 2rem 2rem 1.5rem;
            margin-bottom: 1.5rem;
            position: relative;
        }}

        .line-header::after {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 95%;
            height: 2px;
            background: linear-gradient(90deg, transparent, var(--accent-line), transparent);
        }}

        .line-header-inner {{
            max-width: 800px;
            margin: 0 auto;
        }}

        .line-header h1 {{
            font-size: 2rem;
            margin-bottom: 0.35rem;
            color: var(--accent-line);
        }}

        .line-header .migration {{
            font-size: 1rem;
            color: var(--text-secondary);
            margin-bottom: 0.75rem;
        }}

        .line-header .intro {{
            color: var(--text-secondary);
            max-width: 650px;
            line-height: 1.65;
            font-size: 0.95rem;
        }}

        .section-header {{
            margin: 2.5rem 0 1rem;
        }}

        .section-header h2 {{
            font-size: 0.95rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--text-muted);
            font-weight: 500;
        }}

        .ancestors {{
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
        }}

        .ancestor-card {{
            display: flex;
            gap: 1rem;
            padding: 1rem;
            background: var(--paper);
            border-radius: 5px;
            border-left: 3px solid {border_muted};
            box-shadow: 0 1px 3px rgba(122, 58, 15, 0.05);
            transition: box-shadow 0.2s ease, border-color 0.2s ease;
        }}

        .ancestor-card:hover {{
            box-shadow: 0 2px 8px rgba(122, 58, 15, 0.1);
            border-left-color: var(--accent-line);
        }}

        .ancestor-image {{
            flex-shrink: 0;
            width: 80px;
            height: 80px;
            background-size: cover;
            background-position: center;
            border-radius: 4px;
            position: relative;
        }}

        .ancestor-image::after {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-family: Georgia, 'Times New Roman', serif;
            font-size: 1.25rem;
            font-weight: 500;
            color: rgba(255, 255, 255, 0.9);
            text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
        }}

        .ancestor-content {{
            flex: 1;
            min-width: 0;
        }}

        .ancestor-badge {{
            display: inline-block;
            font-size: 0.7rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.03em;
            padding: 2px 8px;
            border-radius: 3px;
            margin-top: 0.5rem;
        }}

        .ancestor-badge.direct {{
            background: rgba(212, 165, 116, 0.25);
            color: var(--text-secondary);
        }}

        .ancestor-badge.collateral {{
            background: rgba(0, 0, 0, 0.05);
            color: var(--text-muted);
        }}

        .ancestor-name {{
            font-family: Georgia, 'Times New Roman', serif;
            font-size: 1.15rem;
            font-weight: 500;
            color: var(--primary);
            margin-bottom: 0.25rem;
        }}

        .ancestor-tagline {{
            color: var(--text-secondary);
            font-size: 0.95rem;
            margin-bottom: 0.5rem;
        }}

        .ancestor-links {{
            font-size: 0.9rem;
        }}

        .ancestor-links a {{
            margin-right: 1rem;
        }}

{image_css}

        .footer {{
            text-align: center;
            padding: 2rem 1rem;
            color: var(--text-muted);
            font-size: 0.85rem;
            border-top: 1px solid var(--border-light);
            margin-top: 3rem;
        }}

        @media (max-width: 600px) {{
            .ancestor-card {{
                flex-direction: column;
                align-items: flex-start;
            }}

            .ancestor-image {{
                width: 80px;
                height: 80px;
            }}

            .line-header h1 {{
                font-size: 1.75rem;
            }}
        }}
    </style>
</head>
<body>
<div class="page-wrapper">
    <nav class="breadcrumb">
        <a href="../index.html">← All Family Lines</a>
    </nav>

    <header class="line-header">
        <div class="line-header-inner">
            <h1>{name}</h1>
            <div class="migration">{migration}</div>
            <p class="intro">
                {intro}
            </p>
        </div>
    </header>

    <main class="container">
        <div class="section-header">
            <h2>Direct Ancestors</h2>
        </div>

        <div class="ancestors">
{direct_cards}
        </div>
{collateral_section}
    </main>

    <footer class="footer">
        <a href="../index.html">← Back to All Family Lines</a>
    </footer>
</div>
</body>
</html>
'''


def convert_line(yaml_path: Path, production: bool) -> None:
    """Convert a single YAML file to HTML."""
    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    html = generate_line_page(data, production)
    output_path = LINES_DIR / f"{yaml_path.stem}.html"

    with open(output_path, "w") as f:
        f.write(html)

    print(f"Generated {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate line pages from YAML data.")
    parser.add_argument("name", nargs="?", help="Convert a specific line (without .yml)")
    parser.add_argument(
        "--production",
        "-p",
        action="store_true",
        help="Production mode: hide links to draft bios",
    )
    args = parser.parse_args()

    if args.name:
        yaml_path = DATA_DIR / f"{args.name}.yml"
        if not yaml_path.exists():
            print(f"Error: {yaml_path} not found")
            sys.exit(1)
        convert_line(yaml_path, args.production)
    else:
        for yaml_path in sorted(DATA_DIR.glob("*.yml")):
            convert_line(yaml_path, args.production)


if __name__ == "__main__":
    main()

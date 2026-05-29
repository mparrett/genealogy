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

BADGE_ICON_HTML = (
    '<span class="badge-icon" aria-hidden="true">'
    '<svg viewBox="0 0 16 16">'
    '<circle cx="8" cy="5.2" r="2.4"/>'
    '<path d="M2.5 14 a5.5 5.5 0 0 1 11 0 Z"/>'
    '</svg></span>'
)


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
        links.append(f'<a href="../research/reports/html/{bio}">View bio</a>')
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
                    <div class="ancestor-name">{ancestor["name"]} <span class="ancestor-years">({ancestor["years"]})</span></div>
                    <div class="ancestor-tagline">{ancestor["tagline"]}</div>
                    <span class="ancestor-badge {badge_class}">{BADGE_ICON_HTML}<span class="badge-text">{ancestor["relation"]}</span></span>{links_section}
                </div>
            </div>'''


def generate_ancestor_couple(
    couple: dict, accent_color: str, production: bool, has_next: bool = False
) -> str:
    """Generate HTML for a paired-couple block (two ancestor cards side by side)."""
    members = couple.get("members", [])
    if len(members) != 2:
        return "\n\n".join(
            generate_ancestor_card(m, True, accent_color, production) for m in members
        )

    label = couple.get("label", "")
    label_html = (
        f'\n                <div class="ancestor-couple-header"><span>{label}</span></div>'
        if label
        else ""
    )
    card_a = generate_ancestor_card(members[0], True, accent_color, production)
    card_b = generate_ancestor_card(members[1], True, accent_color, production)

    married = couple.get("married") or {}
    marriage_html = ""
    if married:
        parts = []
        if year := married.get("year"):
            parts.append(str(year))
        if place := married.get("place"):
            parts.append(place)
        marriage_text = "Married " + ", ".join(parts) if parts else "Married"
        connector_class = " connect-down" if has_next else ""
        marriage_html = f'\n                <div class="ancestor-couple-marriage{connector_class}">{marriage_text}</div>'

    return f'''            <div class="ancestor-couple">{label_html}
                <div class="ancestor-couple-pair">
{card_a}
                    <div class="ancestor-couple-divider" aria-hidden="true">~</div>
{card_b}
                </div>{marriage_html}
            </div>'''


def generate_direct_entry(
    entry: dict, accent_color: str, production: bool, has_next: bool = False
) -> str:
    """Render a direct-ancestors entry: either a couple block or a single card."""
    if "couple" in entry:
        return generate_ancestor_couple(entry["couple"], accent_color, production, has_next)
    return generate_ancestor_card(entry, True, accent_color, production)


def flatten_direct_entries(entries: list) -> list:
    """Expand any couple wrappers so all members appear in the flat ancestor list."""
    flat = []
    for entry in entries:
        if "couple" in entry:
            flat.extend(entry["couple"].get("members", []))
        else:
            flat.append(entry)
    return flat


def generate_image_css(ancestors: list, accent_color: str) -> str:
    """Generate CSS for ancestor images. Falls back to sepia tint + initials when no thumbnail."""
    css_lines = []
    for ancestor in ancestors:
        img_class = ancestor.get("image_class", "")
        thumb = ancestor.get("image_thumb", "")
        initials = ancestor.get("initials", "")
        if not img_class:
            continue
        if thumb:
            bg_rule = f"background-image: url('../images/thumbs/{thumb}');"
        else:
            bg_rule = "background-color: rgba(212, 165, 116, 0.45);"
        css_lines.append(f"""        .ancestor-image.{img_class} {{
            {bg_rule}
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

    # Collect all ancestors for image CSS (expand couple wrappers)
    direct_flat = flatten_direct_entries(data["ancestors"].get("direct", []))
    all_ancestors = direct_flat + data["ancestors"].get("collateral", [])
    image_css = generate_image_css(all_ancestors, accent)

    # Generate ancestor cards (couple-aware; pass has_next so couples can draw a connector)
    direct_entries = data["ancestors"].get("direct", [])
    direct_cards = "\n\n".join(
        generate_direct_entry(e, accent, production, has_next=(i < len(direct_entries) - 1))
        for i, e in enumerate(direct_entries)
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

        .ancestor-couple {{
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
            position: relative;
        }}

        .ancestor-couple-header {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--text-muted);
            font-weight: 500;
            padding: 0 0.25rem;
            margin: 0.25rem 0;
        }}

        .ancestor-couple-header::before,
        .ancestor-couple-header::after {{
            content: '';
            flex: 1;
            height: 1px;
            background: var(--accent-line);
            opacity: 0.3;
        }}

        .ancestor-couple-pair {{
            display: grid;
            grid-template-columns: 1fr auto 1fr;
            gap: 0.5rem;
            align-items: stretch;
        }}

        /* Drop the accent stripe inside couples — header/divider/marriage already group them */
        .ancestor-couple-pair .ancestor-card,
        .ancestor-couple-pair .ancestor-card:hover {{
            border-left: none;
            padding-left: 1rem;
        }}

        .ancestor-couple-divider {{
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--accent-line);
            opacity: 0.45;
            font-family: Georgia, 'Times New Roman', serif;
            font-size: 1.4rem;
            line-height: 1;
            user-select: none;
        }}

        .ancestor-couple .ancestor-years {{
            display: block;
            font-size: 0.95rem;
            font-weight: 400;
            color: var(--text-secondary);
            margin-top: 0.1rem;
        }}

        .ancestor-couple-marriage {{
            text-align: center;
            font-style: italic;
            font-size: 0.85rem;
            color: var(--text-secondary);
            padding: 0.4rem 0 0.2rem;
            position: relative;
        }}

        .ancestor-couple-marriage.connect-down::after {{
            content: '';
            position: absolute;
            left: 50%;
            top: 100%;
            width: 1px;
            height: 1.25rem;
            background: var(--accent-line);
            opacity: 0.4;
            transform: translateX(-50%);
            pointer-events: none;
        }}

        /* Child of a couple: subtle indent to suggest descent */
        .ancestor-couple + .ancestor-card {{
            margin-left: 2rem;
            margin-right: 2rem;
        }}

        @media (max-width: 700px) {{
            /* Tighten container padding to give cards more horizontal room */
            .container {{
                padding: 0 1rem 1.5rem;
            }}

            .line-header {{
                padding: 1.5rem 1rem 1rem;
            }}

            .breadcrumb {{
                padding: 0.75rem 1rem;
            }}

            /* Keep couple cards side-by-side on mobile — go compact instead of stacking */
            .ancestor-couple-pair {{
                grid-template-columns: 1fr auto 1fr;
                gap: 0.4rem;
            }}

            .ancestor-couple-divider {{
                font-size: 1.1rem;
            }}

            .ancestor-couple-pair .ancestor-card {{
                flex-direction: column;
                align-items: stretch;
                padding: 0.5rem;
                gap: 0.5rem;
            }}

            .ancestor-couple-pair .ancestor-image {{
                width: 100%;
                height: 70px;
                border-radius: 4px;
            }}

            .ancestor-couple-pair .ancestor-image::after {{
                font-size: 1rem;
            }}

            .ancestor-couple .ancestor-name {{
                font-size: 1rem;
                line-height: 1.2;
            }}

            .ancestor-couple .ancestor-years {{
                font-size: 0.85rem;
                margin-top: 0.05rem;
            }}

            .ancestor-couple .ancestor-tagline {{
                font-size: 0.8rem;
                line-height: 1.35;
                margin-bottom: 0.4rem;
            }}

            .ancestor-couple .ancestor-badge {{
                font-size: 0.62rem;
                padding: 1px 6px;
            }}

            .ancestor-couple .ancestor-links {{
                font-size: 0.85rem;
            }}

            .ancestor-couple + .ancestor-card {{
                margin-left: 0;
                margin-right: 0;
            }}
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
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            font-size: 0.7rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-top: 0.5rem;
            color: var(--text-muted);
        }}

        .ancestor-badge .badge-icon {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            flex-shrink: 0;
            overflow: hidden;
        }}

        .ancestor-badge .badge-icon svg {{
            width: 11px;
            height: 11px;
        }}

        .ancestor-badge.direct .badge-icon {{
            background: rgba(212, 165, 116, 0.3);
        }}

        .ancestor-badge.direct .badge-icon svg {{
            fill: #7a5230;
        }}

        .ancestor-badge.collateral .badge-icon {{
            background: rgba(0, 0, 0, 0.06);
        }}

        .ancestor-badge.collateral .badge-icon svg {{
            fill: var(--text-muted);
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
            display: flex;
            justify-content: flex-end;
            gap: 1rem;
            font-size: 0.9rem;
            margin-top: 0.35rem;
        }}

        .ancestor-links a {{
            color: var(--secondary);
        }}

        .ancestor-links a::after {{
            content: ' →';
            display: inline-block;
            transition: transform 0.2s ease;
        }}

        .ancestor-links a:hover {{
            text-decoration: none;
        }}

        .ancestor-links a:hover::after {{
            transform: translateX(3px);
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

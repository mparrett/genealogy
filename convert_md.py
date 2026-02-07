#!/usr/bin/env python3
"""
Markdown to HTML converter for genealogy reports.
"""

import argparse
import html
import mistune
from mistune.renderers.html import HTMLRenderer
import os
import re
import sys
from pathlib import Path

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


def load_timeline_data(md_file_path: Path) -> dict | None:
    """Load timeline data from a companion YAML file if it exists."""
    if not HAS_YAML:
        return None
    timeline_file = md_file_path.parent / "timeline-data" / f"{md_file_path.stem}.yml"
    if not timeline_file.exists():
        return None
    with open(timeline_file, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def _strip_markdown_title(text: str) -> str:
    """Normalize a Markdown heading into plain text for HTML title usage."""
    text = re.sub(r'`([^`]*)`', r'\1', text)
    text = re.sub(r'!\[([^\]]*)\]\([^)]+\)', r'\1', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    text = re.sub(r'[*_~]+', '', text)
    text = re.sub(r'<[^>]+>', '', text)
    return ' '.join(text.split()).strip()


def extract_title(markdown_content: str, body_content: str, fallback: str) -> str:
    """Extract a stable page title from markdown headings, with safe fallback."""
    for line in markdown_content.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        match = re.match(r'#{1,6}\s+(.+?)\s*#*\s*$', stripped)
        if match:
            cleaned = _strip_markdown_title(match.group(1))
            if cleaned:
                return cleaned

    match = re.search(r'<h[1-6][^>]*>(.*?)</h[1-6]>', body_content, re.IGNORECASE | re.DOTALL)
    if match:
        heading_text = re.sub(r'<[^>]+>', '', match.group(1))
        cleaned = ' '.join(html.unescape(heading_text).split())
        if cleaned:
            return cleaned

    return fallback


def generate_timeline_html(data: dict) -> str:
    """Generate the timeline sidebar HTML from YAML data."""
    events = []

    # Add birth
    if 'birth' in data:
        events.append((data['birth']['year'], data['birth']['label'], 'birth'))

    # Add life events
    for event in data.get('events', []):
        events.append((event['year'], event['label'], event.get('type', 'event')))

    # Add death
    if 'death' in data:
        events.append((data['death']['year'], data['death']['label'], 'death'))

    def year_sort_key(value) -> tuple:
        if isinstance(value, int):
            return (0, value)
        if isinstance(value, float):
            return (0, int(value))
        if isinstance(value, str):
            match = re.search(r"\d{3,4}", value)
            if match:
                return (1, int(match.group()))
            return (2, value)
        if value is None:
            return (3, 0)
        return (4, str(value))

    if not events:
        return ""

    # Sort by year (supports values like "c. 1870")
    events.sort(key=lambda x: year_sort_key(x[0]))

    # Generate HTML
    lines = ['<aside class="bio-timeline">']
    for i, (year, label, event_type) in enumerate(events):
        marker_class = "timeline-marker"
        if event_type in ('birth', 'death'):
            marker_class += " timeline-marker--major"
        lines.append(f'  <div class="timeline-event">')
        lines.append(f'    <span class="timeline-year">{year}</span>')
        lines.append(f'    <span class="{marker_class}"></span>')
        lines.append(f'    <span class="timeline-label">{label}</span>')
        lines.append(f'  </div>')
        # Add connecting line between events (except after last)
        if i < len(events) - 1:
            lines.append('  <div class="timeline-line"></div>')
    lines.append('</aside>')

    return '\n'.join(lines)


def generate_location_aside_html(data: dict) -> str:
    """Generate location aside HTML from YAML data."""
    loc = data.get('location_aside')
    if not loc:
        return ""

    place = loc.get('place', '')
    region = loc.get('region', '')
    year = loc.get('year', '')
    image = loc.get('image', '')
    description = loc.get('description', '').strip()
    layout = loc.get('layout', 'vertical')  # vertical (float) or horizontal (banner)

    # Image path is relative to images/ folder, need ../../../images/ from html/
    img_src = f"../../../images/{image}" if image else ""

    if layout == 'horizontal':
        lines = ['<aside class="location-aside-horizontal">']
        if img_src:
            lines.append(f'  <img src="{img_src}" alt="{place}, {region}">')
        lines.append('  <div class="location-aside-content">')
        lines.append(f'    <div class="location-aside-title">{place}</div>')
        lines.append(f'    <div class="location-aside-date">{region}, {year}</div>')
        if description:
            lines.append(f'    <div class="location-aside-text">{description}</div>')
        lines.append('  </div>')
        lines.append('</aside>')
    else:
        lines = ['<aside class="location-aside">']
        if img_src:
            lines.append(f'  <img src="{img_src}" alt="{place}, {region}">')
        lines.append(f'  <div class="location-aside-title">{place}</div>')
        lines.append(f'  <div class="location-aside-date">{region}, {year}</div>')
        if description:
            lines.append(f'  <div class="location-aside-text">{description}</div>')
        lines.append('</aside>')

    return '\n'.join(lines)


def is_draft_link(href: str) -> bool:
    """Return True if the linked bio is marked draft in its timeline data."""
    if not HAS_YAML:
        return False
    if not href or not href.endswith(".html"):
        return False
    stem = Path(href).stem
    md_path = Path("research/reports") / f"{stem}.md"
    if not md_path.exists():
        return False
    data = load_timeline_data(md_path)
    return bool(data and data.get("draft", False))


def generate_family_links_html(data: dict, production: bool = False) -> str:
    """Generate family links section HTML from YAML data."""
    links = data.get('family_links', [])
    if not links:
        return ""
    if production:
        links = [link for link in links if not is_draft_link(link.get('link', ''))]
        if not links:
            return ""

    lines = ['<div class="family-links">']
    lines.append('  <h4 class="family-links-title">Family</h4>')
    lines.append('  <div class="family-links-grid">')
    for link in links:
        name = link['name']
        relation = link.get('relation', '')
        href = link.get('link', '#')
        # Get initials for the watermark
        initials = ''.join(word[0] for word in name.split()[:2]).upper()
        lines.append(f'    <a href="{href}" class="family-link-card">')
        lines.append(f'      <span class="family-link-name">{name}</span>')
        lines.append(f'      <span class="family-link-relation">{relation}</span>')
        lines.append(f'    </a>')
    lines.append('  </div>')
    lines.append('</div>')

    return '\n'.join(lines)


def convert_file(md_file_path, html_file_path, production: bool = False):
    """Convert a single markdown file to HTML."""
    try:
        with open(md_file_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()

        # Create markdown processor with HTML renderer and footnotes plugin
        renderer = HTMLRenderer(escape=False)
        markdown = mistune.create_markdown(renderer=renderer, plugins=['footnotes', 'table'])
        body_content = markdown(markdown_content)

        # Extract title from first heading (any level), fallback to filename stem
        title = extract_title(markdown_content, body_content, md_file_path.stem)

        # Load timeline data if available
        timeline_data = load_timeline_data(md_file_path)
        timeline_html = generate_timeline_html(timeline_data) if timeline_data else ""
        has_timeline = bool(timeline_html)

        # Generate location aside if available - inject after Nth paragraph (default: 3)
        location_aside_html = generate_location_aside_html(timeline_data) if timeline_data else ""
        if location_aside_html:
            after_para = timeline_data.get('location_aside', {}).get('after_paragraph', 3)
            p_count = 0
            insert_pos = 0
            search_str = '</p>'
            pos = 0
            while p_count < after_para:
                found = body_content.find(search_str, pos)
                if found == -1:
                    break
                p_count += 1
                insert_pos = found + len(search_str)
                pos = found + 1
            if p_count >= after_para:
                body_content = body_content[:insert_pos] + '\n' + location_aside_html + '\n' + body_content[insert_pos:]

        # Generate family links if available
        family_links_html = generate_family_links_html(timeline_data, production) if timeline_data else ""
        if family_links_html:
            if '<hr />' in body_content:
                body_content = body_content.replace('<hr />', family_links_html + '\n<hr />', 1)
            else:
                body_content = body_content + '\n' + family_links_html

        
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

        /* Full-width images clear floats */
        img:not(.float-right):not(.float-left) {{
            clear: both;
        }}

        /* Floating images for inline illustrations */
        img.float-right {{
            float: right;
            width: 50%;
            margin: 0 0 1rem 1.5rem;
            border-radius: 4px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}

        img.float-left {{
            float: left;
            width: 50%;
            margin: 0 1.5rem 1rem 0;
            border-radius: 4px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}

        img.float-right-sm {{
            float: right;
            width: 33%;
            margin: 0 0 1rem 1.5rem;
            border-radius: 4px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}

        img.float-left-sm {{
            float: left;
            width: 33%;
            margin: 0 1.5rem 1rem 0;
            border-radius: 4px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}

        /* Feature accordion (expandable sections) */
        details.feature-accordion {{
            margin: 2rem 0;
            padding: 0;
            border: 1px solid rgba(139, 69, 19, 0.2);
            border-radius: 8px;
            background: linear-gradient(135deg, rgba(255,255,255,0.6) 0%, rgba(248,244,240,0.8) 100%);
            overflow: hidden;
        }}

        details.feature-accordion summary {{
            padding: 1rem 1.5rem;
            font-family: Georgia, 'Times New Roman', serif;
            font-size: 1.05rem;
            font-weight: 500;
            color: var(--primary);
            cursor: pointer;
            list-style: none;
            display: flex;
            align-items: center;
            gap: 0.625rem;
            border-radius: 8px;
            transition: background 0.2s ease;
        }}

        details.feature-accordion[open] summary {{
            border-bottom: 1px solid rgba(139, 69, 19, 0.15);
            border-radius: 8px 8px 0 0;
            margin-bottom: 0.5rem;
        }}

        details.feature-accordion summary::-webkit-details-marker {{
            display: none;
        }}

        details.feature-accordion summary::before {{
            content: '▸';
            font-size: 0.875rem;
            color: rgba(139, 69, 19, 0.6);
            transition: transform 0.2s ease, color 0.2s ease;
        }}

        details.feature-accordion[open] summary::before {{
            transform: rotate(90deg);
            color: var(--primary);
        }}

        details.feature-accordion summary:hover {{
            background: rgba(139, 69, 19, 0.08);
        }}

        details.feature-accordion > *:not(summary) {{
            padding: 0 1.5rem;
        }}

        details.feature-accordion > p:first-of-type {{
            padding-top: 0.5rem;
        }}

        details.feature-accordion > p:last-child {{
            padding-bottom: 1.5rem;
            margin-bottom: 0;
        }}

        /* Ensure content clears floated images */
        details.feature-accordion[open]::after {{
            content: '';
            display: block;
            clear: both;
            padding-bottom: 0.5rem;
        }}

        details.feature-accordion em:last-child {{
            display: block;
            margin-top: 1rem;
            padding-bottom: 0.25rem;
            font-size: 0.9rem;
            font-style: italic;
            color: rgba(122, 58, 15, 0.7);
            clear: both;
        }}

        /* Small images within accordions */
        details.feature-accordion img {{
            width: 25%;
            float: right;
            margin: 0.25rem 0 1rem 1.25rem;
        }}

        /* Clear floats after major sections (h2), but allow h3 to flow around location asides */
        h2, hr {{
            clear: both;
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
            padding: 1.875rem;
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
        
        /* Horizontal Rule - simple gradient for markdown hr */
        hr {{
            border: none;
            height: 2px;
            background: linear-gradient(to right, transparent, var(--accent), transparent);
            margin: 2.5rem auto;
            max-width: 95%;
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

            .bio-timeline {{
                display: none;
            }}
        }}

        /* Timeline Sidebar */
        .bio-layout {{
            position: relative;
        }}

        .bio-timeline {{
            position: fixed;
            top: 2rem;
            left: calc(50% + 420px);
            width: 175px;
            padding: 1.25rem 1.5rem;
            background: linear-gradient(
                180deg,
                rgba(252, 252, 250, 0.97) 0%,
                rgba(252, 250, 245, 0.95) 50%,
                rgba(250, 248, 242, 0.97) 100%
            );
            border: 1px solid var(--border-light);
            border-radius: 6px;
            font-size: 0.85rem;
            box-shadow: 0 2px 12px rgba(122, 58, 15, 0.06);
        }}

        .timeline-event {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .timeline-year {{
            font-family: Georgia, serif;
            font-weight: 500;
            color: var(--primary);
            min-width: 2.5rem;
        }}

        .timeline-marker {{
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--accent);
            border: 2px solid var(--primary);
            flex-shrink: 0;
        }}

        .timeline-marker--major {{
            width: 10px;
            height: 10px;
            background: var(--primary);
        }}

        .timeline-label {{
            color: var(--text-secondary);
            font-size: 0.8rem;
            line-height: 1.3;
        }}

        .timeline-line {{
            width: 2px;
            height: 1rem;
            background: linear-gradient(180deg, var(--border-light) 0%, var(--accent) 50%, var(--border-light) 100%);
            margin-left: calc(2.5rem + 0.5rem + 3px);
            opacity: 0.6;
        }}

        @media (max-width: 1100px) {{
            .bio-timeline {{
                display: none;
            }}
        }}

        /* Family Links */
        .family-links {{
            margin: 2rem 0;
        }}

        .family-links-title {{
            font-family: Georgia, serif;
            font-size: 1rem;
            color: var(--text-muted);
            font-weight: 400;
            margin-bottom: 1rem;
            letter-spacing: 0.5px;
        }}

        .family-links-grid {{
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
        }}

        .family-link-card {{
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            align-items: center;
            text-align: center;
            width: 140px;
            padding: 0.875rem 1rem;
            background: linear-gradient(
                180deg,
                rgba(252, 252, 250, 0.97) 0%,
                rgba(250, 248, 242, 0.95) 100%
            );
            border: 1px solid var(--border-light);
            border-left: 3px solid rgba(212, 165, 116, 0.35);
            border-radius: 6px;
            text-decoration: none;
            transition: border-color 0.2s, box-shadow 0.2s;
            overflow: hidden;
        }}

        .family-link-card:hover {{
            border-left-color: var(--accent);
            box-shadow: 0 2px 8px rgba(122, 58, 15, 0.1);
            background-size: 100% 0;
        }}

        .family-link-name {{
            font-family: Georgia, serif;
            font-size: 0.9rem;
            color: var(--primary);
            line-height: 1.25;
            font-weight: 500;
            position: relative;
        }}

        .family-link-relation {{
            font-size: 0.75rem;
            color: var(--text-muted);
            margin-top: 0.25rem;
            position: relative;
        }}

        /* Location Aside */
        .location-aside {{
            float: right;
            width: 33%;
            margin: 0 0 1rem 1.5rem;
            padding: 0.75rem;
            background: linear-gradient(
                180deg,
                rgba(252, 250, 245, 0.6) 0%,
                rgba(250, 247, 240, 0.4) 100%
            );
            border: none;
            border-left: 2px solid rgba(212, 165, 116, 0.6);
            border-radius: 4px;
            font-size: 0.85rem;
        }}

        .location-aside img {{
            width: 100%;
            border-radius: 2px;
            margin-bottom: 0.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.06);
        }}

        .location-aside-title {{
            font-family: Georgia, serif;
            font-size: 0.9rem;
            font-weight: 500;
            color: var(--primary);
            margin-bottom: 0.125rem;
            line-height: 1.3;
        }}

        .location-aside-date {{
            font-size: 0.75rem;
            color: var(--text-muted);
            margin-bottom: 0.5rem;
        }}

        .location-aside-text {{
            font-size: 0.8rem;
            color: var(--text-secondary);
            line-height: 1.5;
        }}

        @media (max-width: 600px) {{
            .location-aside {{
                float: none;
                width: 100%;
                margin: 1rem 0;
            }}
        }}

        @media print {{
            .location-aside {{
                float: right;
                width: 40%;
                border-left: 1px solid #ccc;
            }}
        }}

        /* Location Aside - Horizontal variant (image left, text right) */
        .location-aside-horizontal {{
            float: right;
            width: 50%;
            margin: 0 0 1rem 1.5rem;
            padding: 0.75rem;
            background: linear-gradient(
                180deg,
                rgba(252, 250, 245, 0.6) 0%,
                rgba(250, 247, 240, 0.4) 100%
            );
            border: none;
            border-left: 2px solid rgba(212, 165, 116, 0.6);
            border-radius: 4px;
            font-size: 0.85rem;
            display: flex;
            gap: 0.75rem;
        }}

        .location-aside-horizontal img {{
            flex: 1;
            min-width: 0;
            border-radius: 2px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.06);
            align-self: flex-start;
        }}

        .location-aside-horizontal .location-aside-content {{
            flex: 1.6;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }}

        .location-aside-horizontal .location-aside-title {{
            font-family: Georgia, serif;
            font-size: 0.95rem;
            font-weight: 500;
            color: var(--primary);
            margin-bottom: 0.125rem;
            line-height: 1.3;
        }}

        .location-aside-horizontal .location-aside-date {{
            font-size: 0.75rem;
            color: var(--text-muted);
            margin-bottom: 0.5rem;
        }}

        .location-aside-horizontal .location-aside-text {{
            font-size: 0.8rem;
            color: var(--text-secondary);
            line-height: 1.5;
        }}

        @media (max-width: 600px) {{
            .location-aside-horizontal {{
                float: none;
                width: 100%;
                margin: 1rem 0;
                flex-direction: column;
            }}

            .location-aside-horizontal img {{
                width: 100%;
            }}
        }}

        @media print {{
            .location-aside-horizontal {{
                float: right;
                width: 45%;
                border-left: 1px solid #ccc;
            }}
        }}

        /* Back Navigation - matches line page breadcrumb */
        .bio-nav {{
            padding: 0.5rem 0;
            margin-bottom: 1rem;
            font-size: 0.85rem;
        }}

        .bio-nav a {{
            color: var(--text-muted);
            text-decoration: none;
            background: none;
        }}

        .bio-nav a:hover {{
            color: var(--secondary);
            text-decoration: underline;
        }}


        @media print {{
            .bio-nav {{
                display: none;
            }}
        }}
    </style>
</head>
<body>
<nav class="bio-nav"><a href="../../../index.html">← Family Index</a></nav>
{f'<div class="bio-layout"><div class="bio-content">{body_content}</div>{timeline_html}</div>' if has_timeline else body_content}
</body>
</html>"""
        
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(html_document)
        
        print(f"✅ Converted {md_file_path} → {html_file_path}")
        return True
    
    except Exception as e:
        print(f"❌ Error converting {md_file_path}: {e}")
        return False


def is_draft(md_file_path: Path) -> bool:
    """Check if a bio is marked as draft in its YAML data."""
    data = load_timeline_data(md_file_path)
    if data and data.get('draft', False):
        return True
    return False


def convert_all_reports(production: bool = False):
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
    skipped_count = 0
    for md_file in md_files:
        # Skip drafts in production mode
        if production and is_draft(md_file):
            print(f"⏭️  Skipped draft: {md_file.name}")
            skipped_count += 1
            continue

        html_file = html_dir / f"{md_file.stem}.html"
        if convert_file(md_file, html_file, production):
            success_count += 1

    total = len(md_files) - skipped_count
    print(f"✅ Converted {success_count}/{total} markdown files to HTML")
    if skipped_count:
        print(f"⏭️  Skipped {skipped_count} drafts (production mode)")
    return success_count == total


def main():
    parser = argparse.ArgumentParser(description="Convert markdown genealogy reports to HTML")
    parser.add_argument("--file", "-f", help="Convert specific file (without .md extension)")
    parser.add_argument("--all", "-a", action="store_true", help="Convert all markdown files")
    parser.add_argument("--production", "-p", action="store_true", help="Production mode: skip drafts")

    args = parser.parse_args()

    if args.file:
        md_file = Path(f"research/reports/{args.file}.md")
        html_file = Path(f"research/reports/html/{args.file}.html")

        if not md_file.exists():
            print(f"❌ File {md_file} not found")
            sys.exit(1)

        # Check if draft in production mode
        if args.production and is_draft(md_file):
            print(f"⏭️  Skipped draft: {md_file.name}")
            sys.exit(0)

        # Create HTML directory if it doesn't exist
        html_file.parent.mkdir(exist_ok=True)

        success = convert_file(md_file, html_file, args.production)
        sys.exit(0 if success else 1)

    elif args.all:
        success = convert_all_reports(production=args.production)
        sys.exit(0 if success else 1)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Check for missing bios and PDFs referenced in YAML data."""

from pathlib import Path
import sys

import yaml


ROOT = Path(__file__).parent
REPORTS_DIR = ROOT / "research" / "reports"
HTML_DIR = REPORTS_DIR / "html"
PDF_DIR = ROOT / "pdf"
LINE_DATA_DIR = ROOT / "lines" / "data"
TIMELINE_DATA_DIR = REPORTS_DIR / "timeline-data"


def bio_exists(html_name: str) -> bool:
    if not html_name.endswith(".html"):
        return True
    md_name = Path(html_name).stem + ".md"
    return (HTML_DIR / html_name).exists() or (REPORTS_DIR / md_name).exists()


def load_yaml(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def main() -> int:
    missing_bios = []
    missing_pdfs = []

    for yaml_path in sorted(LINE_DATA_DIR.glob("*.yml")):
        data = load_yaml(yaml_path)
        ancestors = data.get("ancestors", {})
        for group in ("direct", "collateral"):
            for ancestor in ancestors.get(group, []):
                bio = ancestor.get("bio")
                if bio and not bio_exists(bio):
                    missing_bios.append((yaml_path, bio))
                pdf = ancestor.get("pdf")
                if pdf and not (PDF_DIR / pdf).exists():
                    missing_pdfs.append((yaml_path, pdf))

    for yaml_path in sorted(TIMELINE_DATA_DIR.glob("*.yml")):
        data = load_yaml(yaml_path)
        for link in data.get("family_links", []):
            href = link.get("link")
            if href and not bio_exists(href):
                missing_bios.append((yaml_path, href))

    if not missing_bios and not missing_pdfs:
        print("✅ No missing bios or PDFs referenced in YAML data.")
        return 0

    if missing_bios:
        print("Missing bios:")
        for path, bio in missing_bios:
            print(f"  - {bio} (from {path})")
    if missing_pdfs:
        print("Missing PDFs:")
        for path, pdf in missing_pdfs:
            print(f"  - {pdf} (from {path})")
    return 1


if __name__ == "__main__":
    sys.exit(main())

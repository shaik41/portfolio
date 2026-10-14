#!/usr/bin/env python3
"""Wrap each page.html (the Claude artifact copy) into a full index.html for static hosting.

Run from the repo root after editing any page.html:  python3 scripts/build_pages.py
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "site"

PAGES = {
    "page.html": {
        "title": "Bulawa",
        "description": "Animated invitation websites for nikahs, mehndis, birthdays, baby showers and housewarmings.",
        "theme": "#FBF8FF",
    },
    "wedding/noor/page.html": {
        "title": "Ayesha & Imran · Wedding Invitation",
        "description": "Together with their families, Ayesha & Imran invite you to their Nikah on Sunday, 20 December 2026. Tap to open.",
        "theme": "#F4EDE0",
    },
    "wedding/shahi/page.html": {
        "title": "Zoya & Rayyan · Wedding Invitation",
        "description": "The honour of your presence is requested at the Nikah of Zoya & Rayyan on Friday, 12 February 2027. Tap to enter.",
        "theme": "#45091A",
    },
}

HEAD = """<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{description}">
<meta name="theme-color" content="{theme}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta name="twitter:card" content="summary">
"""


def main() -> None:
    for rel, meta in PAGES.items():
        src = ROOT / rel
        out = src.with_name("index.html")
        head = HEAD.format(**{k: escape(v, quote=True) for k, v in meta.items()})
        out.write_text(head + src.read_text(encoding="utf-8") + "\n</html>\n", encoding="utf-8")
        print(f"built {out.relative_to(ROOT.parent)}")


if __name__ == "__main__":
    main()

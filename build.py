"""Builds index.html from src/index.src.html.

Edit src/index.src.html, then run:  python build.py

The only thing this does is paste the IBM Plex fonts (assets/plex.css, base64 data URIs)
into the page in place of the FONTS_PLACEHOLDER marker, so the page needs no font host.
map.html is built separately by myJourney.ipynb.
"""
from pathlib import Path

HERE = Path(__file__).parent
MARK = "/* FONTS_PLACEHOLDER */"

src = (HERE / "src" / "index.src.html").read_text(encoding="utf-8")
fonts = (HERE / "assets" / "plex.css").read_text(encoding="utf-8")

assert MARK in src, f"marker {MARK!r} missing, nothing would be spliced"
out = src.replace(MARK, fonts)
assert len(out) - len(src) > 150_000, "font block too small, wrong file spliced?"

(HERE / "index.html").write_text(out, encoding="utf-8", newline="\n")
print(f"index.html: {len(src):,} -> {len(out):,} bytes")

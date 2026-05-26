"""Generate PDFs from the DataOps Engineer HTML resumes via xhtml2pdf.

xhtml2pdf does not support CSS custom properties (var(--name)), so we
inline them here before rendering.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from xhtml2pdf import pisa

HERE = Path(__file__).resolve().parent

CSS_VARS = {
    "--text": "#1a1a1a",
    "--muted": "#555",
    "--border": "#d0d7de",
    "--accent": "#0d47a1",
    "--bg-soft": "#f6f8fa",
}

GLYPH_FALLBACKS = {
    "\u2014": "-",   # em-dash
    "\u2013": "-",   # en-dash
    "\u2212": "-",   # minus
    "\u00b7": "|",   # middle dot used as separator
    "\u2022": "*",   # bullet
    "\u2018": "'",
    "\u2019": "'",
    "\u201c": '"',
    "\u201d": '"',
}


def inline_css_vars(html: str) -> str:
    out = html
    out = re.sub(
        r":root\s*\{[^}]*\}",
        "",
        out,
        count=1,
        flags=re.DOTALL,
    )
    for name, value in CSS_VARS.items():
        pattern = re.compile(r"var\(\s*" + re.escape(name) + r"\s*\)")
        out = pattern.sub(value, out)
    return out


def normalize_glyphs(html: str) -> str:
    out = html
    for src, dst in GLYPH_FALLBACKS.items():
        out = out.replace(src, dst)
    return out


def render(src_html: Path, dst_pdf: Path) -> bool:
    html = src_html.read_text(encoding="utf-8")
    html = inline_css_vars(html)
    html = normalize_glyphs(html)
    with dst_pdf.open("wb") as fh:
        result = pisa.CreatePDF(html, dest=fh, encoding="utf-8")
    return not result.err


def main() -> int:
    pairs = [
        (HERE / "DataOps_Engineer_Porokhnya_EN.html", HERE / "DataOps_Engineer_Porokhnya_EN.pdf"),
        (HERE / "DataOps_Engineer_Porokhnya_RU.html", HERE / "DataOps_Engineer_Porokhnya_RU.pdf"),
    ]
    rc = 0
    for src, dst in pairs:
        if not src.exists():
            print(f"[skip] {src} not found")
            continue
        ok = render(src, dst)
        print(f"[{'ok' if ok else 'err'}] {dst.name}")
        if not ok:
            rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main())

# -*- coding: utf-8 -*-
"""Build HTML and PDF for the Representative China DM resume from the source MD.

HTML is rendered via the `markdown` package (tables, fenced_code, attr_list)
wrapped into a print-friendly CSS template. PDF is rendered directly from the
MD via fpdf2 (Arial Unicode) so that tables, Cyrillic characters and CJK
fragments render reliably without a headless browser.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

import markdown as md_lib
from fpdf import FPDF

HERE = Path(__file__).resolve().parent
SRC_MD = HERE / "Representative_China_DM_Kurnosenko_RU.md"
DST_HTML = HERE / "Representative_China_DM_Kurnosenko_RU.html"
DST_PDF = HERE / "Representative_China_DM_Kurnosenko_RU.pdf"

FONT_DIR = Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts"
FONTS = {
    "": FONT_DIR / "arial.ttf",
    "B": FONT_DIR / "arialbd.ttf",
    "I": FONT_DIR / "ariali.ttf",
    "BI": FONT_DIR / "arialbi.ttf",
}

L_MARGIN = 18
R_MARGIN = 18
T_MARGIN = 16
PAGE_W = 210
TXT_W = PAGE_W - L_MARGIN - R_MARGIN  # 174 mm


HTML_CSS = """
:root {
  --text: #1a1a1a;
  --muted: #555;
  --border: #d0d7de;
  --accent: #0d47a1;
  --bg-soft: #f6f8fa;
}
* { box-sizing: border-box; }
body {
  margin: 0 auto;
  max-width: 210mm;
  padding: 14mm 16mm 18mm;
  font-family: "Segoe UI", system-ui, -apple-system, Roboto, Arial, sans-serif;
  font-size: 10.5pt;
  line-height: 1.45;
  color: var(--text);
  background: #fff;
}
h1 {
  margin: 0 0 0.35rem;
  font-size: 1.7rem;
  font-weight: 700;
  letter-spacing: -0.02em;
}
h2 {
  margin: 1.2rem 0 0.45rem;
  padding-bottom: 0.2rem;
  font-size: 0.88rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--accent);
  border-bottom: 1px solid var(--border);
}
h3 {
  margin: 0.9rem 0 0.2rem;
  font-size: 1rem;
}
p { margin: 0.35rem 0; }
.meta-line {
  margin-top: 0;
  color: var(--muted);
  font-size: 0.93rem;
}
ul { margin: 0.25rem 0 0.55rem; padding-left: 1.15rem; }
li { margin: 0.18rem 0; }
hr {
  border: 0;
  border-top: 1px solid var(--border);
  margin: 0.8rem 0;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin: 0.4rem 0 0.7rem;
  font-size: 9.7pt;
}
th, td {
  border: 1px solid var(--border);
  padding: 0.35rem 0.5rem;
  vertical-align: top;
  text-align: left;
}
thead th { background: var(--bg-soft); }
tbody th { width: 28%; font-weight: 600; background: #fcfcfc; }
code {
  font-family: Consolas, "Courier New", monospace;
  font-size: 0.94em;
}
a { color: inherit; }
@page { size: A4; margin: 12mm 14mm 14mm; }
@media print {
  body {
    padding: 0;
    max-width: none;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  h2, h3 { break-after: avoid; }
  ul, table { break-inside: avoid; }
}
""".strip()


def render_html(md_text: str) -> str:
    body_html = md_lib.markdown(
        md_text,
        extensions=["tables", "fenced_code", "sane_lists"],
        output_format="html5",
    )
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{SRC_MD.stem}</title>
<style>
{HTML_CSS}
</style>
</head>
<body>
{body_html}
</body>
</html>
"""


def strip_inline(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text


def parse_table(lines: list[str]) -> list[list[str]]:
    rows: list[list[str]] = []
    for ln in lines:
        ln = ln.strip()
        if re.match(r"^\|[-| :]+\|$", ln):
            continue
        if ln.startswith("|"):
            cells = [strip_inline(c.strip()) for c in ln.strip("|").split("|")]
            rows.append(cells)
    return rows


def build_pdf(md_text: str) -> FPDF:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_margins(L_MARGIN, T_MARGIN, R_MARGIN)
    pdf.set_auto_page_break(True, margin=14)
    pdf.add_font("Ar", "", str(FONTS[""]), uni=True)
    pdf.add_font("Ar", "B", str(FONTS["B"]), uni=True)
    pdf.add_font("Ar", "I", str(FONTS["I"]), uni=True)
    pdf.add_font("Ar", "BI", str(FONTS["BI"]), uni=True)
    pdf.add_page()
    pdf.set_text_color(25, 25, 25)

    def f(style: str = "", size: float = 10.5) -> None:
        pdf.set_font("Ar", style, size)

    def mc(
        txt: str,
        h: float = 5.2,
        border: int = 0,
        align: str = "L",
        style: str = "",
        size: float = 10.5,
        color: tuple[int, int, int] | None = None,
    ) -> None:
        f(style, size)
        if color:
            pdf.set_text_color(*color)
        pdf.set_x(L_MARGIN)
        pdf.multi_cell(TXT_W, h, txt, border=border, align=align)
        pdf.set_x(L_MARGIN)
        if color:
            pdf.set_text_color(25, 25, 25)

    def gap(mm: float = 2) -> None:
        pdf.ln(mm)

    def hline(color: tuple[int, int, int] = (190, 190, 190)) -> None:
        pdf.set_draw_color(*color)
        y = pdf.get_y() + 0.5
        pdf.line(L_MARGIN, y, PAGE_W - R_MARGIN, y)
        pdf.set_draw_color(0, 0, 0)
        gap(2.5)

    def draw_table(rows: list[list[str]]) -> None:
        col_w = [56, TXT_W - 56]
        row_h = 5.0
        hdr_fill = (242, 242, 242)
        for ri, row in enumerate(rows):
            is_hdr = ri == 0
            sty = "B" if is_hdr else ""
            max_lines = 1
            for ci, cell in enumerate(row):
                f(sty, 9.5)
                wrapped = pdf.multi_cell(
                    col_w[min(ci, 1)] - 4, row_h, cell, split_only=True
                )
                max_lines = max(max_lines, len(wrapped))
            rh = row_h * max_lines + 3
            if pdf.get_y() + rh > pdf.h - 14:
                pdf.add_page()
            y0 = pdf.get_y()
            x0 = L_MARGIN
            for ci, cell in enumerate(row):
                cw = col_w[min(ci, 1)]
                if is_hdr:
                    pdf.set_fill_color(*hdr_fill)
                    pdf.rect(x0, y0, cw, rh, style="FD")
                else:
                    pdf.rect(x0, y0, cw, rh)
                f(sty, 9.5)
                pdf.set_xy(x0 + 2, y0 + 1.5)
                pdf.multi_cell(cw - 4, row_h, cell, border=0)
                x0 += cw
            pdf.set_xy(L_MARGIN, y0 + rh)
        gap(3)

    lines = md_text.splitlines()
    i = 0
    while i < len(lines):
        raw = lines[i]
        stripped = raw.strip()

        if not stripped:
            gap(1.2)
            i += 1
            continue

        if re.match(r"^-{3,}$|^\*{3,}$", stripped):
            hline()
            i += 1
            continue

        if stripped.startswith("|"):
            tbl: list[str] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                tbl.append(lines[i])
                i += 1
            draw_table(parse_table(tbl))
            continue

        m = re.match(r"^# (.+)$", stripped)
        if m:
            mc(strip_inline(m.group(1)), h=9, style="B", size=18)
            hline((170, 170, 170))
            i += 1
            continue

        m = re.match(r"^## (.+)$", stripped)
        if m:
            gap(3)
            mc(
                strip_inline(m.group(1)),
                h=7,
                style="B",
                size=13,
                color=(30, 30, 100),
            )
            gap(1.5)
            i += 1
            continue

        m = re.match(r"^### (.+)$", stripped)
        if m:
            gap(3)
            mc(strip_inline(m.group(1)), h=6, style="B", size=11)
            i += 1
            continue

        m = re.match(r"^\*([^*].+?)\*\s*(.*)$", stripped)
        if m:
            text = strip_inline(
                m.group(1) + (" " + m.group(2) if m.group(2) else "")
            )
            mc(text, h=5, style="I", size=9.5, color=(90, 90, 90))
            gap(1)
            i += 1
            continue

        m = re.match(r"^[-*] (.+)$", stripped)
        if m:
            text = strip_inline(m.group(1))
            indent = 5
            bw = 4
            f("", 10)
            pdf.set_x(L_MARGIN + indent)
            pdf.cell(bw, 5.2, chr(0x2022))
            pdf.set_x(L_MARGIN + indent + bw)
            pdf.multi_cell(TXT_W - indent - bw, 5.2, text, border=0)
            pdf.set_x(L_MARGIN)
            gap(0.4)
            i += 1
            continue

        text = strip_inline(stripped)
        mc(text, h=5.5, size=10.5)
        gap(1)
        i += 1

    return pdf


def main() -> int:
    if not SRC_MD.exists():
        print(f"[err] source MD not found: {SRC_MD}", file=sys.stderr)
        return 1
    missing = [k for k, v in FONTS.items() if not v.is_file()]
    if missing:
        print(f"[err] font files missing: {missing}", file=sys.stderr)
        return 1

    md_text = SRC_MD.read_text(encoding="utf-8")

    html_text = render_html(md_text)
    DST_HTML.write_text(html_text, encoding="utf-8")
    print(f"[ok] {DST_HTML.name}")

    pdf = build_pdf(md_text)
    tmp = DST_PDF.with_suffix(".pdf.tmp")
    pdf.output(str(tmp))
    if DST_PDF.exists():
        os.replace(tmp, DST_PDF)
    else:
        os.rename(tmp, DST_PDF)
    print(f"[ok] {DST_PDF.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

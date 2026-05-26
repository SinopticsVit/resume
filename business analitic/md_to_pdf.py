# -*- coding: utf-8 -*-
"""Convert Markdown resumes to PDF via fpdf2. Pure multi_cell layout."""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
DEFAULT_MD_PATH = os.path.join(ROOT, "Senior_Business_Analyst_RU.md")
DEFAULT_PDF_PATH = os.path.join(ROOT, "Senior_Business_Analyst_RU_v2.pdf")

FONT_DIR = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts")
FONTS = {
    "": os.path.join(FONT_DIR, "arial.ttf"),
    "B": os.path.join(FONT_DIR, "arialbd.ttf"),
    "I": os.path.join(FONT_DIR, "ariali.ttf"),
    "BI": os.path.join(FONT_DIR, "arialbi.ttf"),
}

L_MARGIN = 18
R_MARGIN = 18
T_MARGIN = 16
PAGE_W   = 210
TXT_W    = PAGE_W - L_MARGIN - R_MARGIN   # 174 mm


def strip_inline(text):
    """Remove markdown inline markers, return plain text."""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*",   r"\1", text)
    text = re.sub(r"`(.+?)`",        r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text


def parse_table(lines):
    rows = []
    for ln in lines:
        ln = ln.strip()
        if re.match(r"^\|[-| :]+\|$", ln):
            continue
        if ln.startswith("|"):
            cells = [strip_inline(c.strip()) for c in ln.strip("|").split("|")]
            rows.append(cells)
    return rows


def build_pdf(md_text):
    from fpdf import FPDF

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_margins(L_MARGIN, T_MARGIN, R_MARGIN)
    pdf.set_auto_page_break(True, margin=14)
    pdf.add_font("Ar",  "",  FONTS[""],  uni=True)
    pdf.add_font("Ar",  "B", FONTS["B"], uni=True)
    pdf.add_font("Ar",  "I", FONTS["I"], uni=True)
    pdf.add_font("Ar", "BI", FONTS["BI"], uni=True)
    pdf.add_page()
    pdf.set_text_color(25, 25, 25)

    def f(style="", size=10.5):
        pdf.set_font("Ar", style, size)

    def mc(txt, h=5.2, border=0, align="L", style="", size=10.5, color=None):
        f(style, size)
        if color:
            pdf.set_text_color(*color)
        pdf.set_x(L_MARGIN)
        pdf.multi_cell(TXT_W, h, txt, border=border, align=align)
        pdf.set_x(L_MARGIN)
        if color:
            pdf.set_text_color(25, 25, 25)

    def gap(mm=2):
        pdf.ln(mm)

    def hline(color=(190, 190, 190)):
        pdf.set_draw_color(*color)
        y = pdf.get_y() + 0.5
        pdf.line(L_MARGIN, y, PAGE_W - R_MARGIN, y)
        pdf.set_draw_color(0, 0, 0)
        gap(2.5)

    # ── table ────────────────────────────────────────────────────────────────
    def draw_table(rows):
        col_w = [56, TXT_W - 56]
        row_h = 5.0
        hdr_fill = (242, 242, 242)

        for ri, row in enumerate(rows):
            is_hdr = ri == 0
            sty = "B" if is_hdr else ""

            # measure height
            max_lines = 1
            for ci, cell in enumerate(row):
                f(sty, 9.5)
                wrapped = pdf.multi_cell(col_w[min(ci, 1)] - 4, row_h,
                                         cell, split_only=True)
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

    # ── parse lines ───────────────────────────────────────────────────────────
    lines = md_text.splitlines()
    i = 0
    while i < len(lines):
        raw     = lines[i]
        stripped = raw.strip()

        # blank
        if not stripped:
            gap(1.2)
            i += 1
            continue

        # HR
        if re.match(r"^-{3,}$|^\*{3,}$", stripped):
            hline()
            i += 1
            continue

        # table
        if stripped.startswith("|"):
            tbl = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                tbl.append(lines[i])
                i += 1
            draw_table(parse_table(tbl))
            continue

        # H1
        m = re.match(r"^# (.+)$", stripped)
        if m:
            mc(strip_inline(m.group(1)), h=9, style="B", size=18)
            hline((170, 170, 170))
            i += 1
            continue

        # H2
        m = re.match(r"^## (.+)$", stripped)
        if m:
            gap(3)
            mc(strip_inline(m.group(1)), h=7, style="B", size=13,
               color=(30, 30, 100))
            gap(1.5)
            i += 1
            continue

        # H3
        m = re.match(r"^### (.+)$", stripped)
        if m:
            gap(3)
            mc(strip_inline(m.group(1)), h=6, style="B", size=11)
            i += 1
            continue

        # italic line  *...*
        m = re.match(r"^\*([^*].+?)\*\s*(.*)$", stripped)
        if m:
            text = strip_inline(m.group(1) + (" " + m.group(2) if m.group(2) else ""))
            mc(text, h=5, style="I", size=9.5, color=(90, 90, 90))
            gap(1)
            i += 1
            continue

        # bullet  - …  or  * …
        m = re.match(r"^[-*] (.+)$", stripped)
        if m:
            text   = strip_inline(m.group(1))
            indent = 5
            bw     = 4
            f("", 10)
            pdf.set_x(L_MARGIN + indent)
            pdf.cell(bw, 5.2, chr(0x2022))
            pdf.set_x(L_MARGIN + indent + bw)
            pdf.multi_cell(TXT_W - indent - bw, 5.2, text, border=0)
            pdf.set_x(L_MARGIN)
            gap(0.4)
            i += 1
            continue

        # regular paragraph (bold markers stripped)
        text = strip_inline(stripped)
        mc(text, h=5.5, size=10.5)
        gap(1)
        i += 1

    return pdf


def main():
    missing = [k for k, v in FONTS.items() if not os.path.isfile(v)]
    if missing:
        print("Font files not found:", missing, file=sys.stderr)
        sys.exit(1)

    md_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_MD_PATH
    pdf_path = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_PDF_PATH

    with open(md_path, "r", encoding="utf-8") as fh:
        md_text = fh.read()

    pdf = build_pdf(md_text)

    # write to temp then replace to avoid locked-file errors
    tmp = pdf_path + ".tmp"
    pdf.output(tmp)
    if os.path.exists(pdf_path):
        os.replace(tmp, pdf_path)
    else:
        os.rename(tmp, pdf_path)
    print("OK ->", pdf_path)


if __name__ == "__main__":
    main()

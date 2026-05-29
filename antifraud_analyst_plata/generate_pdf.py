"""Generate PDF resume from markdown using reportlab."""
import re
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

MD_FILE = Path(__file__).parent / "Antifraud_Analyst_Plata_Kurnosenko_EN.md"
PDF_FILE = Path(__file__).parent / "Antifraud_Analyst_Kurnosenko_EN.pdf"

# ── colour palette ────────────────────────────────────────────────────────────
NAVY   = colors.HexColor("#1a2e4a")
STEEL  = colors.HexColor("#2e6da4")
LIGHT  = colors.HexColor("#f0f4f8")
GRAY   = colors.HexColor("#555555")
BLACK  = colors.black

def build_styles():
    base = getSampleStyleSheet()
    def s(name, **kw):
        return ParagraphStyle(name, parent=base["Normal"], **kw)

    return {
        "name":     s("name",     fontSize=20, leading=24, textColor=NAVY,
                      fontName="Helvetica-Bold", spaceAfter=2),
        "tagline":  s("tagline",  fontSize=10, leading=13, textColor=STEEL,
                      fontName="Helvetica", spaceAfter=4),
        "contacts": s("contacts", fontSize=8.5, leading=12, textColor=GRAY,
                      fontName="Helvetica", spaceAfter=2),
        "h2":       s("h2",       fontSize=11, leading=14, textColor=NAVY,
                      fontName="Helvetica-Bold", spaceBefore=10, spaceAfter=3),
        "h3":       s("h3",       fontSize=9.5, leading=13, textColor=STEEL,
                      fontName="Helvetica-Bold", spaceBefore=7, spaceAfter=2),
        "body":     s("body",     fontSize=8.5, leading=12, textColor=BLACK,
                      fontName="Helvetica", spaceAfter=2),
        "bullet":   s("bullet",   fontSize=8.5, leading=12, textColor=BLACK,
                      fontName="Helvetica", leftIndent=12, firstLineIndent=-8,
                      spaceAfter=2),
        "th":       s("th",       fontSize=8, leading=11, textColor=colors.white,
                      fontName="Helvetica-Bold"),
        "td":       s("td",       fontSize=8, leading=11, textColor=BLACK,
                      fontName="Helvetica"),
    }


def escape(text: str) -> str:
    """Minimal XML escaping for reportlab Paragraph."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def bold_inline(text: str) -> str:
    """Convert **bold** markdown to <b>bold</b> for reportlab."""
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', escape(text))


def parse_table(lines: list[str], styles: dict) -> Table:
    """Parse markdown table lines into a reportlab Table."""
    rows = []
    for line in lines:
        if re.match(r'^\|[-| :]+\|$', line.strip()):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        rows.append(cells)

    if not rows:
        return None

    header = rows[0]
    data_rows = rows[1:]

    col_widths = [5 * cm, 11.5 * cm]  # 2-column table

    table_data = []
    table_data.append([
        Paragraph(bold_inline(h), styles["th"]) for h in header
    ])
    for row in data_rows:
        table_data.append([
            Paragraph(bold_inline(c), styles["td"]) for c in row
        ])

    t = Table(table_data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND",  (0, 0), (-1, 0),  NAVY),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
        ("GRID",        (0, 0), (-1, -1), 0.4, colors.HexColor("#cccccc")),
        ("VALIGN",      (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING",  (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


def md_to_story(md_text: str, styles: dict) -> list:
    story = []
    lines = md_text.splitlines()
    i = 0

    while i < len(lines):
        line = lines[i]

        # blank line
        if not line.strip():
            story.append(Spacer(1, 3))
            i += 1
            continue

        # horizontal rule
        if re.match(r'^---+$', line.strip()):
            story.append(HRFlowable(width="100%", thickness=0.6,
                                    color=STEEL, spaceAfter=4, spaceBefore=2))
            i += 1
            continue

        # H1 — candidate name
        if line.startswith("# ") and not line.startswith("## "):
            story.append(Paragraph(escape(line[2:]), styles["name"]))
            i += 1
            continue

        # H2
        if line.startswith("## "):
            story.append(Paragraph(escape(line[3:]).upper(), styles["h2"]))
            i += 1
            continue

        # H3
        if line.startswith("### "):
            story.append(Paragraph(bold_inline(line[4:]), styles["h3"]))
            i += 1
            continue

        # Table — collect all consecutive table lines
        if line.startswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].startswith("|"):
                table_lines.append(lines[i])
                i += 1
            t = parse_table(table_lines, styles)
            if t:
                story.append(Spacer(1, 4))
                story.append(t)
                story.append(Spacer(1, 4))
            continue

        # Bullet point
        if line.startswith("- "):
            story.append(Paragraph("• " + bold_inline(line[2:]), styles["bullet"]))
            i += 1
            continue

        # Bold-only line (section label inside experience block)
        if re.match(r'^\*\*[^*]+\*\*$', line.strip()):
            story.append(Paragraph(bold_inline(line.strip()), styles["h3"]))
            i += 1
            continue

        # Italic line (dates, notes)
        if re.match(r'^\*[^*]+\*$', line.strip()):
            story.append(Paragraph(
                f'<i>{escape(line.strip().strip("*"))}</i>', styles["body"]))
            i += 1
            continue

        # Regular paragraph
        story.append(Paragraph(bold_inline(line.strip()), styles["body"]))
        i += 1

    return story


def build_pdf():
    styles = build_styles()
    md_text = MD_FILE.read_text(encoding="utf-8")

    # Split off the header block (name + tagline + contacts) to render specially
    # Everything before first --- is the header
    parts = md_text.split("\n---\n", 1)
    header_md = parts[0]
    rest_md = parts[1] if len(parts) > 1 else ""

    doc = SimpleDocTemplate(
        str(PDF_FILE),
        pagesize=A4,
        leftMargin=1.8 * cm,
        rightMargin=1.8 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
    )

    story = []

    # ── render header ──────────────────────────────────────────────────────────
    for line in header_md.splitlines():
        if not line.strip():
            continue
        if line.startswith("# "):
            story.append(Paragraph(escape(line[2:]), styles["name"]))
        elif line.startswith("**") and "|" in line:
            # tagline line: **Role** | detail | detail
            story.append(Paragraph(bold_inline(line.strip()), styles["tagline"]))
        else:
            # contact fields
            story.append(Paragraph(bold_inline(line.strip()), styles["contacts"]))

    story.append(HRFlowable(width="100%", thickness=1.2,
                            color=NAVY, spaceAfter=6, spaceBefore=4))

    # ── render body ────────────────────────────────────────────────────────────
    story += md_to_story(rest_md, styles)

    doc.build(story)
    print(f"PDF written: {PDF_FILE}")


if __name__ == "__main__":
    build_pdf()

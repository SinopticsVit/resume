"""Generate PDF mock enrollment / visa extension letter from Fudan University."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    HRFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "Fudan_Enrollment_Letter_Kurnosenko_Darya_EN.pdf"

NAVY = colors.HexColor("#1a3a6b")
STEEL = colors.HexColor("#e8eef8")
GOLD = colors.HexColor("#b8963e")
TEXT = colors.HexColor("#1a1a2e")
MUTED = colors.HexColor("#5a5a7a")
LINE = colors.HexColor("#c0cce0")


def S(name: str, **kw) -> ParagraphStyle:
    return ParagraphStyle(name, **kw)


STYLES = {
    "uni_name": S("uni_name", fontName="Helvetica-Bold", fontSize=16, leading=20,
                   alignment=TA_CENTER, textColor=NAVY, spaceAfter=2),
    "uni_sub": S("uni_sub", fontName="Helvetica", fontSize=9, leading=13,
                 alignment=TA_CENTER, textColor=MUTED, spaceAfter=1),
    "doc_title": S("doc_title", fontName="Helvetica-Bold", fontSize=13, leading=18,
                   alignment=TA_CENTER, textColor=NAVY, spaceBefore=10, spaceAfter=8),
    "meta": S("meta", fontName="Helvetica", fontSize=9, leading=13, textColor=TEXT),
    "heading": S("heading", fontName="Helvetica-Bold", fontSize=10, leading=14,
                 textColor=NAVY, spaceBefore=10, spaceAfter=4),
    "body": S("body", fontName="Helvetica", fontSize=10, leading=15,
              alignment=TA_JUSTIFY, textColor=TEXT, spaceAfter=6),
    "label": S("label", fontName="Helvetica-Bold", fontSize=9, leading=13, textColor=MUTED),
    "value": S("value", fontName="Helvetica", fontSize=9, leading=13, textColor=TEXT),
    "sign": S("sign", fontName="Helvetica", fontSize=10, leading=14, textColor=TEXT),
    "foot": S("foot", fontName="Helvetica-Oblique", fontSize=8, leading=11,
              alignment=TA_CENTER, textColor=MUTED),
}


def hr(thick: float = 0.5, color=LINE, before: float = 2, after: float = 2):
    return HRFlowable(width="100%", thickness=thick, color=color,
                      spaceBefore=before, spaceAfter=after)


def info_table(rows: list[tuple[str, str]], col_widths) -> Table:
    data = [[Paragraph(lbl, STYLES["label"]), Paragraph(val, STYLES["value"])]
            for lbl, val in rows]
    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), STEEL),
        ("BOX", (0, 0), (-1, -1), 0.6, NAVY),
        ("INNERGRID", (0, 0), (-1, -1), 0.3, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


def build() -> None:
    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=2.5 * cm,
        rightMargin=2.5 * cm,
        topMargin=2.0 * cm,
        bottomMargin=2.5 * cm,
    )
    W = A4[0] - 5 * cm
    story = []

    story.append(hr(4, GOLD, before=0, after=4))
    story.append(hr(1, NAVY, before=0, after=8))

    story.append(Paragraph("FUDAN UNIVERSITY", STYLES["uni_name"]))
    for line in [
        "International Cultural Exchange School (ICES)",
        "220 Handan Road, Yangpu District, Shanghai 200433, P.R. China",
        "Tel: +86 21 6564 2292  |  Email: ices@fudan.edu.cn",
    ]:
        story.append(Paragraph(line, STYLES["uni_sub"]))

    story.append(hr(1, NAVY, before=8, after=6))
    story.append(Paragraph("CERTIFICATE OF ENROLLMENT AND VISA EXTENSION REQUEST",
                           STYLES["doc_title"]))

    story.append(Paragraph(
        "<b>Document No.:</b> FDU-ICES-2026-CL-0847 &nbsp;&nbsp;&nbsp; "
        "<b>Date of Issue:</b> June 22, 2026",
        STYLES["meta"],
    ))
    story.append(Spacer(1, 10))

    story.append(Paragraph("<b>To:</b><br/>"
                           "Shanghai Exit-Entry Administration<br/>"
                           "General Administration of Immigration, P.R. China<br/>"
                           "<i>(or the relevant visa-issuing authority)</i>",
                           STYLES["meta"]))
    story.append(Spacer(1, 8))

    story.append(Paragraph(
        "<b>Subject:</b> Certificate of Enrollment — Request for Visa Extension<br/>"
        "<b>Re:</b> Ms. <b>Darya Vitalievna Kurnosenko</b> (Russian Federation)",
        STYLES["meta"],
    ))
    story.append(Spacer(1, 10))

    story.append(Paragraph("Dear Sir or Madam,", STYLES["body"]))
    story.append(Paragraph(
        "This letter is issued by <b>Fudan University</b>, Shanghai, to confirm the "
        "enrollment status of the above-named student and to respectfully request an "
        "extension of her stay (visa/residence permit validity) in the People's Republic "
        "of China.",
        STYLES["body"],
    ))

    story.append(Paragraph("1. Student Information", STYLES["heading"]))
    story.append(info_table([
        ("Full Name", "KURNOSENKO, Darya Vitalievna"),
        ("Nationality", "Russian Federation"),
        ("Date of Birth", "May 23, 2008"),
        ("Passport No.", "[to be filled in]"),
    ], [4.5 * cm, W - 4.5 * cm]))
    story.append(Spacer(1, 8))

    story.append(Paragraph("2. Program of Study", STYLES["heading"]))
    story.append(Paragraph(
        "The student is currently enrolled in the <b>Intensive Chinese Language Program</b> "
        "at the <b>International Cultural Exchange School (ICES), Fudan University</b>, "
        "Shanghai.",
        STYLES["body"],
    ))
    story.append(info_table([
        ("Institution", "Fudan University"),
        ("Program", "Intensive Chinese Language Course"),
        ("Campus", "Fudan University, Yangpu Campus, Shanghai"),
        ("Student Status", "Active — currently attending classes"),
        ("Last Day of Instruction", "<b>July 3, 2026</b> (Friday)"),
    ], [5.5 * cm, W - 5.5 * cm]))
    story.append(Paragraph(
        "Upon completion of the final class on <b>July 3, 2026</b>, the student will have "
        "fulfilled all academic requirements of the current language course. No further "
        "classes are scheduled after that date.",
        STYLES["body"],
    ))

    story.append(Paragraph("3. Request for Visa Extension", STYLES["heading"]))
    story.append(Paragraph(
        "We kindly request that the relevant authority <b>extend the validity of the "
        "student's visa / residence permit until July 5, 2026 (inclusive)</b>.",
        STYLES["body"],
    ))
    story.append(Paragraph(
        "This extension is necessary to allow the student sufficient time to complete "
        "course-related formalities and personal departure preparations after the last "
        "day of study; check out of accommodation and travel to the airport; and "
        "<b>depart the People's Republic of China and return to the Russian Federation "
        "on July 5, 2026</b>.",
        STYLES["body"],
    ))
    story.append(Paragraph(
        "The student's planned date of departure from China is <b>July 5, 2026</b>. "
        "She does not intend to remain in China beyond that date.",
        STYLES["body"],
    ))

    story.append(Paragraph("4. Confirmation", STYLES["heading"]))
    story.append(Paragraph(
        "Fudan University confirms that <b>Ms. Darya Vitalievna Kurnosenko</b> is a bona "
        "fide student in good standing at our institution and is attending the Chinese "
        "language program described above.",
        STYLES["body"],
    ))
    story.append(Paragraph(
        "Should you require any further information, please do not hesitate to contact "
        "the International Cultural Exchange School at the address or telephone number "
        "indicated above.",
        STYLES["body"],
    ))
    story.append(Paragraph(
        "Respectfully submitted for your consideration.",
        STYLES["body"],
    ))

    story.append(Spacer(1, 16))
    story.append(Paragraph(
        "<b>For and on behalf of Fudan University</b><br/>"
        "International Cultural Exchange School (ICES)",
        STYLES["sign"],
    ))
    story.append(Spacer(1, 24))
    story.append(Paragraph("_______________________________", STYLES["sign"]))
    story.append(Paragraph(
        "<b>Dr. [Name]</b><br/>"
        "Director, International Cultural Exchange School<br/>"
        "Fudan University",
        STYLES["sign"],
    ))
    story.append(Spacer(1, 20))
    story.append(Paragraph("_______________________________", STYLES["sign"]))
    story.append(Paragraph("<b>Official Seal</b><br/>Fudan University", STYLES["sign"]))

    story.append(Spacer(1, 14))
    story.append(hr(1, NAVY, before=0, after=4))
    story.append(hr(4, GOLD, before=0, after=6))
    story.append(Paragraph(
        "DRAFT MOCK-UP — Not an official document issued by Fudan University. "
        "For reference and template purposes only.",
        STYLES["foot"],
    ))

    doc.build(story)
    print(f"[ok] {OUT}")


if __name__ == "__main__":
    build()

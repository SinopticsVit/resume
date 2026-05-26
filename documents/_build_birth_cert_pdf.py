"""Generate official-format Chinese translation PDF of the Russian birth certificate."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "birth_certificate_Kurnosenko_Darya_ZH.pdf"

# ── Fonts ────────────────────────────────────────────────────────────────────
pdfmetrics.registerFont(TTFont("MSYH",     "C:/Windows/Fonts/msyh.ttc",   subfontIndex=0))
pdfmetrics.registerFont(TTFont("MSYHBold", "C:/Windows/Fonts/msyhbd.ttc", subfontIndex=0))

# ── Palette ──────────────────────────────────────────────────────────────────
NAVY   = colors.HexColor("#1a3a6b")
STEEL  = colors.HexColor("#e8eef8")
GOLD   = colors.HexColor("#b8963e")
TEXT   = colors.HexColor("#1a1a2e")
MUTED  = colors.HexColor("#5a5a7a")
LINE   = colors.HexColor("#c0cce0")


def S(name: str, **kw) -> ParagraphStyle:
    return ParagraphStyle(name, **kw)


STYLES = {
    "main_title": S("main_title", fontName="MSYHBold", fontSize=18, leading=26,
                    alignment=TA_CENTER, textColor=NAVY, spaceAfter=2),

    "subtitle": S("subtitle", fontName="MSYH", fontSize=10, leading=15,
                  alignment=TA_CENTER, textColor=MUTED, spaceAfter=2),

    "sec_head": S("sec_head", fontName="MSYHBold", fontSize=10, leading=15,
                  alignment=TA_CENTER, textColor=NAVY, spaceBefore=8, spaceAfter=4),

    "label": S("label", fontName="MSYHBold", fontSize=9, leading=14, textColor=MUTED),

    "value": S("value", fontName="MSYH", fontSize=10, leading=16, textColor=TEXT),

    "cert": S("cert", fontName="MSYH", fontSize=9.5, leading=16,
              alignment=TA_JUSTIFY, textColor=TEXT, spaceBefore=4, spaceAfter=4),

    "foot": S("foot", fontName="MSYH", fontSize=7.5, leading=11,
              alignment=TA_CENTER, textColor=MUTED),
}


def hr(thick: float = 0.5, color=LINE, before: float = 2, after: float = 2):
    return HRFlowable(width="100%", thickness=thick, color=color,
                      spaceBefore=before, spaceAfter=after)


def field(label: str, value: str) -> Table:
    t = Table(
        [[Paragraph(label, STYLES["label"]), Paragraph(value, STYLES["value"])]],
        colWidths=[4.2 * cm, 12.8 * cm],
    )
    t.setStyle(TableStyle([
        ("VALIGN",         (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING",     (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING",  (0, 0), (-1, -1), 3),
    ]))
    return t


def section_box(title: str, W: float) -> Table:
    t = Table([[Paragraph(title, STYLES["sec_head"])]], colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), STEEL),
        ("BOX",           (0, 0), (-1, -1), 0.5, NAVY),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
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

    # ── Top gold rule ─────────────────────────────────────────────────────────
    story.append(hr(4, GOLD, before=0, after=4))
    story.append(hr(1, NAVY, before=0, after=10))

    # ── Title ─────────────────────────────────────────────────────────────────
    story.append(Paragraph("出生证明书翻译件", STYLES["main_title"]))
    story.append(Paragraph("（俄罗斯联邦公民出生证明官方翻译）", STYLES["subtitle"]))
    story.append(Spacer(1, 6))

    # ── Meta info row ─────────────────────────────────────────────────────────
    meta = Table(
        [
            [
                Paragraph("原始语言", STYLES["label"]),
                Paragraph("俄语", STYLES["value"]),
                Paragraph("翻译语言", STYLES["label"]),
                Paragraph("中文（普通话）", STYLES["value"]),
            ],
            [
                Paragraph("文件类型", STYLES["label"]),
                Paragraph("出生证明书（补发件）", STYLES["value"]),
                Paragraph("文件编号", STYLES["label"]),
                Paragraph("VIII-МЮ № 751516", STYLES["value"]),
            ],
        ],
        colWidths=[3.0 * cm, 6.0 * cm, 3.0 * cm, 5.2 * cm],
    )
    meta.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), STEEL),
        ("BOX",           (0, 0), (-1, -1), 0.8, NAVY),
        ("INNERGRID",     (0, 0), (-1, -1), 0.3, LINE),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
    ]))
    story.append(meta)
    story.append(Spacer(1, 14))

    # ── Section 1: 基本信息 ───────────────────────────────────────────────────
    story.append(section_box("一、出生人基本信息", W))
    story.append(Spacer(1, 4))
    for lbl, val in [
        ("姓名：",     "库尔诺先科  达利娅·维塔利耶芙娜"),
        ("出生日期：", "2008年5月23日（二零零八年五月二十三日）"),
        ("出生地点：", "俄罗斯联邦，莫斯科市"),
    ]:
        story.append(field(lbl, val))
        story.append(hr())

    story.append(Spacer(1, 10))

    # ── Section 2: 登记信息 ───────────────────────────────────────────────────
    story.append(section_box("二、登记信息", W))
    story.append(Spacer(1, 4))
    for lbl, val in [
        ("登记日期：", "2008年6月3日"),
        ("登记编号：", "2112"),
        ("登记机关：", "莫斯科市民事登记管理局\n佩罗夫斯基区民事登记处"),
    ]:
        story.append(field(lbl, val))
        story.append(hr())

    story.append(Spacer(1, 10))

    # ── Section 3: 父母信息 ───────────────────────────────────────────────────
    story.append(section_box("三、父母信息", W))
    story.append(Spacer(1, 4))
    for lbl, val in [
        ("父亲：", "库尔诺先科  维塔利·尼古拉耶维奇\n俄罗斯联邦公民"),
        ("母亲：", "库尔诺先科  斯维特拉娜·弗拉基米罗芙娜\n俄罗斯联邦公民"),
    ]:
        story.append(field(lbl, val))
        story.append(hr())

    story.append(Spacer(1, 10))

    # ── Section 4: 签发信息 ───────────────────────────────────────────────────
    story.append(section_box("四、文件签发信息", W))
    story.append(Spacer(1, 4))
    for lbl, val in [
        ("签发日期：", "2017年2月21日"),
        ("签发官员：", "科马罗娃·纳塔利娅·弗拉基米罗芙娜，民事登记处主任"),
        ("文件编号：", "VIII-МЮ № 751516"),
        ("印制单位：", "俄罗斯国家印刷局（Гознак），莫斯科，2016年"),
    ]:
        story.append(field(lbl, val))
        story.append(hr())

    story.append(Spacer(1, 14))

    # ── Certification block ───────────────────────────────────────────────────
    story.append(hr(1.5, NAVY, before=0, after=8))

    cert_box = Table(
        [[Paragraph(
            "本译文系根据俄罗斯联邦出生证明书原件（补发件，编号 VIII-МЮ № 751516）忠实、"
            "准确翻译而成，与原文内容相符，译文对原始文件所有信息进行了完整呈现。",
            STYLES["cert"],
        )]],
        colWidths=[W],
    )
    cert_box.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), STEEL),
        ("BOX",           (0, 0), (-1, -1), 0.5, NAVY),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(cert_box)
    story.append(Spacer(1, 10))

    # ── Bottom rules & footer ─────────────────────────────────────────────────
    story.append(hr(1, NAVY, before=0, after=4))
    story.append(hr(4, GOLD, before=0, after=6))

    story.append(Paragraph(
        "本翻译件仅供参考。如需具有法律效力的官方认证译文，"
        "请联系具备相应资质的公证翻译机构。",
        STYLES["foot"],
    ))

    doc.build(story)
    print(f"[ok] {OUT}")


if __name__ == "__main__":
    build()

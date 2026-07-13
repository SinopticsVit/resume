#!/usr/bin/env python3
"""Generate DOCX for Analytics Engineer DWH resume (EN / RU)."""

from pathlib import Path

from generate_plata_risk_docx import convert_resume_md_to_docx

HERE = Path(__file__).parent

PAIRS = (
    ("Analytics_Engineer_Kurnosenko_EN.md", "Analytics_Engineer_Kurnosenko_EN.docx"),
    ("Analytics_Engineer_DWH_Kurnosenko_EN.md", "Analytics_Engineer_DWH_Kurnosenko_EN.docx"),
    ("Analytics_Engineer_DWH_Kurnosenko_RU.md", "Analytics_Engineer_DWH_Kurnosenko_RU.docx"),
)


if __name__ == "__main__":
    for md_name, docx_name in PAIRS:
        md_path = HERE / md_name
        docx_path = HERE / docx_name
        if not md_path.exists():
            print(f"Skip (no source): {md_path}")
            continue
        convert_resume_md_to_docx(md_path, docx_path)
        print(f"DOCX written: {docx_path}")

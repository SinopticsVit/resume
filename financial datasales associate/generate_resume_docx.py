#!/usr/bin/env python3
"""Generate DOCX for Financial Data Sales Associate resume."""

import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent / "analytics_engineer"))

from generate_plata_risk_docx import convert_resume_md_to_docx

MD = HERE / "Financial_Data_Sales_Associate_Kurnosenko_EN.md"
DOCX = HERE / "Financial_Data_Sales_Associate_Kurnosenko_EN.docx"

if __name__ == "__main__":
    convert_resume_md_to_docx(MD, DOCX)
    print("DOCX written:", DOCX)

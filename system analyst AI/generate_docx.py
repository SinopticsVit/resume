#!/usr/bin/env python3
"""Generate DOCX for System Analyst AI (RU) resume."""

import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent / "analytics_engineer"))

from generate_plata_risk_docx import convert_resume_md_to_docx

MD = HERE / "System_Analyst_AI_Kurnosenko_RU.md"
DOCX = HERE / "System_Analyst_AI_Kurnosenko_RU.docx"


if __name__ == "__main__":
    convert_resume_md_to_docx(MD, DOCX)
    print("DOCX written:", DOCX)

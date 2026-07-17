#!/usr/bin/env python3
"""Generate DOCX resumes for Senior Tester-DevOps @ Gonka."""

import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent / "analytics_engineer"))

from generate_plata_risk_docx import convert_resume_md_to_docx  # noqa: E402

FILES = [
    (
        HERE / "Senior_Tester_DevOps_Gonka_Kurnosenko_EN.md",
        HERE / "Senior_Tester_DevOps_Gonka_Kurnosenko_EN.docx",
    ),
    (
        HERE / "Senior_Tester_DevOps_Gonka_Kurnosenko_RU.md",
        HERE / "Senior_Tester_DevOps_Gonka_Kurnosenko_RU.docx",
    ),
]


if __name__ == "__main__":
    for md, docx in FILES:
        convert_resume_md_to_docx(md, docx)
        print("DOCX written:", docx)

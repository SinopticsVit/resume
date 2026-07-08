#!/usr/bin/env python3
"""Generate DOCX for ML Engineer LLM/RAG/Parsing resume (Gazprombank)."""

import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parents[1] / "analytics_engineer"))

from generate_plata_risk_docx import convert_resume_md_to_docx

MD = HERE / "ML_Engineer_LLM_RAG_Parsing_Gazprombank_Kurnosenko_RU.md"
DOCX = HERE / "ML_Engineer_LLM_RAG_Parsing_Gazprombank_Kurnosenko_RU.docx"

if __name__ == "__main__":
    convert_resume_md_to_docx(MD, DOCX)
    print(f"DOCX written: {DOCX}")

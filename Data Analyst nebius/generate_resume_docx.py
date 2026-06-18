#!/usr/bin/env python3
"""Generate professional DOCX resume for Data Analyst at Nebius."""

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os


def set_cell_shading(cell, color_hex):
    shading = OxmlElement("w:shd")
    shading.set(qn("w:fill"), color_hex)
    cell._tc.get_or_add_tcPr().append(shading)


def add_horizontal_line(doc):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    cell.text = ""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement("w:tcBorders")
    for border_name in ["top", "left", "right"]:
        border = OxmlElement(f"w:{border_name}")
        border.set(qn("w:val"), "nil")
        tcBorders.append(border)
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:color"), "2E5090")
    tcBorders.append(bottom)
    tcPr.append(tcBorders)
    tr = table.rows[0]._tr
    trPr = tr.get_or_add_trPr()
    trHeight = OxmlElement("w:trHeight")
    trHeight.set(qn("w:val"), "50")
    trHeight.set(qn("w:hRule"), "exact")
    trPr.append(trHeight)


def create_resume():
    doc = Document()
    for section in doc.sections:
        section.top_margin = Cm(1.5)
        section.bottom_margin = Cm(1.5)
        section.left_margin = Cm(1.8)
        section.right_margin = Cm(1.8)

    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(10)
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")

    # Header
    p = doc.add_paragraph()
    run = p.add_run("Kurnosenko Vitaly Nikolaevich")
    run.bold = True
    run.font.size = Pt(18)
    run.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p = doc.add_paragraph()
    run = p.add_run(
        "Data Analyst | SQL · Python · dbt · Airflow · BigQuery | "
        "Dashboards · Data Quality · ETL/ELT"
    )
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(0x2E, 0x50, 0x90)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(4)

    contact = (
        "Location: Asia (open to relocation)  |  Citizenship: Russia  |  "
        "Phone: +86 15601694273  |  Email: kurnosenko@mail.ru  |  "
        "Telegram: @vitaly_kur  |  WeChat: porohnya"
    )
    p = doc.add_paragraph()
    run = p.add_run(contact)
    run.font.size = Pt(9)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p = doc.add_paragraph()
    run = p.add_run(
        "Languages: Russian — native; English — B2 working proficiency; "
        "Chinese (Mandarin) — HSK 4"
    )
    run.font.size = Pt(9)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(6)
    add_horizontal_line(doc)

    # Summary
    h = doc.add_heading("Professional Summary", level=1)
    h.runs[0].font.size = Pt(12)
    summary = (
        "Data analyst with 3+ years of hands-on experience on a high-volume e-commerce "
        "anti-fraud platform (Yofi, USA — Shopify merchants including enterprise retail). "
        "Translate business and stakeholder questions into reliable datasets, dashboards, "
        "and actionable insights using SQL, Python, dbt, Airflow, and BigQuery.\n\n"
        "Strong grounding in mathematical statistics and probability (PhD in Physics and "
        "Mathematics) — applied to descriptive analysis, anomaly detection, funnel and "
        "cohort logic, and careful interpretation of metrics. Comfortable end-to-end: "
        "validating sources, shaping raw data into trusted marts, building visualizations "
        "stakeholders rely on, and writing clear root-cause summaries when data or "
        "pipelines break.\n\n"
        "Experienced in international remote teams; ready to support day-to-day "
        "decision-making, improve data quality checks, and contribute to AI-assisted "
        "analytics workflows at Nebius."
    )
    p = doc.add_paragraph(summary)
    for run in p.runs:
        run.font.size = Pt(10)
    add_horizontal_line(doc)

    # Role fit table
    h = doc.add_heading("Role Fit — Data Analyst at Nebius", level=1)
    h.runs[0].font.size = Pt(12)
    fit_rows = [
        (
            "Data Analyst or similar role",
            "3+ years as Data Analyst / Analytics Engineer on production data platform; "
            "earlier product and finance analytics background",
        ),
        (
            "Strong Python and SQL",
            "Advanced SQL (CTEs, window functions) on BigQuery, PostgreSQL, MS SQL; "
            "Python (pandas, PySpark) for analysis and pipeline support",
        ),
        (
            "Statistics and analytical thinking",
            "PhD in mathematical sciences; descriptive statistics, hypothesis-aware "
            "interpretation; fraud and conversion pattern analysis",
        ),
        (
            "Dashboards and communication",
            "ROI and operational dashboards; stakeholder reporting; documented metrics "
            "and business rules",
        ),
        (
            "Data quality and detail",
            "dbt tests, pipeline validation, null/consistency fixes, aligned metric "
            "definitions across teams",
        ),
        (
            "Business → structured analysis",
            "Requirements with product and analysts; recurring ad-hoc work into reusable "
            "marts and reports",
        ),
        (
            "BI tools",
            "Power BI; ready for Looker / Superset / Tableau per team standards",
        ),
        (
            "Modern data stack",
            "dbt on BigQuery; ~25 Airflow DAGs; PostgreSQL, MongoDB, Spanner as sources",
        ),
        (
            "Cohort / funnel / experiments",
            "Sessionization, funnel and merchant KPI logic; AI workflow quality evaluation",
        ),
        (
            "Cloud / technical product",
            "AWS and GCP data platforms; high-volume events; ML-adjacent feature analytics",
        ),
    ]
    table = doc.add_table(rows=len(fit_rows), cols=2)
    table.style = "Table Grid"
    for i, (req, evidence) in enumerate(fit_rows):
        c0 = table.rows[i].cells[0]
        c0.text = req
        for para in c0.paragraphs:
            for run in para.runs:
                run.bold = True
                run.font.size = Pt(9)
        set_cell_shading(c0, "E8EEF4")
        c1 = table.rows[i].cells[1]
        c1.text = evidence
        for para in c1.paragraphs:
            for run in para.runs:
                run.font.size = Pt(9)
    for row in table.rows:
        row.cells[0].width = Cm(5.5)
        row.cells[1].width = Cm(12)
    doc.add_paragraph()
    add_horizontal_line(doc)

    # Core skills
    h = doc.add_heading("Core Skills", level=1)
    h.runs[0].font.size = Pt(12)
    skills = [
        (
            "Data Analysis & SQL",
            "Advanced SQL — CTEs, window functions, aggregations; BigQuery, PostgreSQL, "
            "MS SQL, Spanner; query tuning; exploratory analysis",
        ),
        (
            "Python & Automation",
            "pandas, pandas-gbq, PySpark; exploration, backfills, reporting automation; "
            "Excel when most efficient",
        ),
        (
            "Data Platform & Pipelines",
            "dbt, Airflow, Airbyte, Spark on Kubernetes; lakehouse on GCS / BigLake",
        ),
        (
            "Data Quality & Documentation",
            "Automated tests, source validation, freshness monitoring; internal "
            "documentation; code reviews",
        ),
        (
            "Visualization & Reporting",
            "Power BI; operational and ROI dashboards; plain-language recommendations",
        ),
        (
            "Domain & Methods",
            "E-commerce anti-fraud — orders, billing, customer clusters, merchant KPIs; "
            "funnel, cohort, anomaly thinking; finance metrics discipline",
        ),
        (
            "Collaboration",
            "Product, engineering, analysts; KPI definition alignment; international remote teams",
        ),
    ]
    table = doc.add_table(rows=len(skills), cols=2)
    table.style = "Table Grid"
    for i, (area, detail) in enumerate(skills):
        c0 = table.rows[i].cells[0]
        c0.text = area
        for para in c0.paragraphs:
            for run in para.runs:
                run.bold = True
                run.font.size = Pt(9)
        set_cell_shading(c0, "E8EEF4")
        c1 = table.rows[i].cells[1]
        c1.text = detail
        for para in c1.paragraphs:
            for run in para.runs:
                run.font.size = Pt(9)
    doc.add_paragraph()
    add_horizontal_line(doc)

    # Experience
    h = doc.add_heading("Work Experience", level=1)
    h.runs[0].font.size = Pt(12)
    experiences = [
        {
            "role": "Data Analyst / Analytics Engineer",
            "company": "Yofi Inc. (USA, remote)",
            "period": "February 2022 — October 2025",
            "intro": (
                "Anti-fraud and customer-intelligence platform for Shopify merchants "
                "(enterprise customers including Lululemon)."
            ),
            "bullets": [
                "Built and maintained analytical datasets and marts in BigQuery using dbt — "
                "order and customer dimensions, fraud indicators, merchant reporting layers; "
                "enforced SQL quality standards and documented business logic.",
                "Owned ETL/ELT support: orchestrated ~25 production Airflow DAGs (Spark jobs, "
                "Airbyte syncs, incremental and full-refresh); monitored failures and pipeline health.",
                "Wrote optimized SQL for complex analysis — joins across MongoDB, PostgreSQL, "
                "Spanner and the warehouse; window functions and CTEs for sessionization, "
                "funnels, and risk-confirmation logic.",
                "Ensured data quality via automated tests, batch validation, and fixes for "
                "nulls and schema drift; aligned relational schemas across application and analytics.",
                "Developed PySpark workloads for lakehouse ingestion on GCS; tuned partitioning "
                "for high-volume event processing.",
                "Supported ROI and operational dashboards; Python/pandas for ad-hoc exploration "
                "and report automation.",
                "Documented models and metrics; trained analysts on dbt, Airbyte, and Spark practices.",
                "Collaborated on feature analytics and realtime severity workflows for risk reporting.",
                "Integrated Shopify, partner webhooks, and marketing sources into the analytical lake via Airbyte.",
            ],
            "stack": (
                "Stack: SQL, Python, PySpark, dbt, Airflow, Airbyte, BigQuery, GCS, "
                "PostgreSQL, MongoDB, Redis, Neo4j, Spanner, Power BI, AWS, GCP."
            ),
        },
        {
            "role": "Business Analyst / AI Platform",
            "company": "Sinoptics AI (remote)",
            "period": "March 2025 — Present",
            "intro": "",
            "bullets": [
                "Structured requirements for document-processing and analytics workflows; "
                "validation rules improved reporting transparency.",
                "Built data flows in Python and SQL for product analytics and AI-assisted features.",
                "Participated in evaluation of AI workflows — quality checks and iteration from feedback.",
                "Coordinated pilots; prepared clear status reporting for non-technical stakeholders.",
            ],
            "stack": "",
        },
        {
            "role": "Head of IT and Finance",
            "company": "Engineering Solutions LLC",
            "period": "March 2013 — December 2017",
            "intro": "",
            "bullets": [
                "Led financial and IT operations: investment analysis, budgeting, management "
                "reporting, and automation supporting KPI tracking.",
            ],
            "stack": "",
        },
        {
            "role": "Head of IT Department",
            "company": "New Engineering Solution",
            "period": "April 2003 — February 2013",
            "intro": "",
            "bullets": [
                "Owned ERP and reporting systems; structured internal reporting for management decisions.",
            ],
            "stack": "",
        },
    ]

    for exp in experiences:
        p = doc.add_paragraph()
        r1 = p.add_run(f"{exp['role']} — ")
        r1.bold = True
        r1.font.size = Pt(10)
        r2 = p.add_run(exp["company"])
        r2.bold = True
        r2.font.size = Pt(10)
        r2.font.color.rgb = RGBColor(0x2E, 0x50, 0x90)

        p = doc.add_paragraph()
        r = p.add_run(exp["period"])
        r.italic = True
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

        if exp["intro"]:
            p = doc.add_paragraph(exp["intro"])
            for run in p.runs:
                run.italic = True
                run.font.size = Pt(9.5)

        for bullet in exp["bullets"]:
            p = doc.add_paragraph(bullet, style="List Bullet")
            for run in p.runs:
                run.font.size = Pt(9.5)

        if exp["stack"]:
            p = doc.add_paragraph(exp["stack"])
            for run in p.runs:
                run.font.size = Pt(9)
                run.italic = True

    add_horizontal_line(doc)

    # Education
    h = doc.add_heading("Education", level=1)
    h.runs[0].font.size = Pt(12)
    for item in [
        "PhD in Physics and Mathematics, Southern Federal University, 2000–2003",
        "Physics Diploma (Specialist), Southern Federal University, 1994–1999",
        "MBA, RANEPA, 2005–2007",
        "College of Radio-Electronic Instrumentation, 1991–1995",
    ]:
        p = doc.add_paragraph(f"• {item}")
        for run in p.runs:
            run.font.size = Pt(10)

    add_horizontal_line(doc)

    # Certifications
    h = doc.add_heading("Certifications", level=1)
    h.runs[0].font.size = Pt(12)
    for item in [
        "CAP — Certified Accountant Practitioner",
        "CPA Russia: financial accounting and IFRS reporting, management accounting, taxation",
        "Chief Accountant Courses",
    ]:
        p = doc.add_paragraph(f"• {item}")
        for run in p.runs:
            run.font.size = Pt(10)

    add_horizontal_line(doc)

    # Why Nebius
    h = doc.add_heading("Why Data Analyst at Nebius", level=1)
    h.runs[0].font.size = Pt(12)
    why = (
        "Nebius sits at the intersection of cloud infrastructure, AI, and data-driven "
        "decision-making — where analytical rigor and the ability to explain trade-offs "
        "matter as much as tooling. My background combines production experience on a modern "
        "data stack (dbt, Airflow, BigQuery, Python, SQL) with a PhD-level foundation in "
        "statistics and years of KPI-driven reporting in regulated environments.\n\n"
        "I am comfortable owning the full loop: clarify the business question, validate "
        "definitions, shape trustworthy datasets, build dashboards people use, and dig deeper "
        "when numbers look wrong. Ready to support ETL quality, anomaly-oriented analysis, "
        "and AI-assisted analytics as Nebius scales."
    )
    p = doc.add_paragraph(why)
    for run in p.runs:
        run.font.size = Pt(10)

    p = doc.add_paragraph()
    r = p.add_run("Resume prepared specifically for the Data Analyst position at Nebius.")
    r.italic = True
    r.font.size = Pt(8)
    r.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    return doc


def main():
    output_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(output_dir, "Data_Analyst_Nebius_Kurnosenko_EN.docx")
    create_resume().save(path)
    print(f"Saved: {path}")


if __name__ == "__main__":
    main()

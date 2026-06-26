# Kurnosenko Vitaly 

**Antifraud Analyst (Senior)** | Fraud Rules · SQL Pipelines · ML Scoring · Payment Risk

**Location:** Shanghai, China (remote-friendly, GMT+8)  
**Citizenship:** Russia  
**Phone:** +86 15601694273  
**Email:** vitaly@sinoptics.ai  
**WeChat:** porohnya  
**telegram:** vitaly_kur  
**Languages:** Russian — native; English — A1 working proficiency; Chinese (Mandarin) — HSK 4

---

## Professional Summary

Senior antifraud analyst and engineer with **5+ years** of end-to-end ownership on a production **e-commerce anti-fraud platform** (Yofi, USA — enterprise Shopify merchants including Lululemon). Design, build, and maintain fraud detection rules, **SQL and dbt transformations**, feature tables, and analytics pipelines; tune thresholds and monitor **false positive / false negative** trade-offs in production.

Product-minded and independent: translate emerging fraud patterns into data-driven controls, run back-tests on historical event data, and communicate findings to engineering, product, and business stakeholders. Hands-on with **real-time order scoring**, multi-signal validation (BIN, IP, email, phone, address, device signals), and event-based ingestion at high volume.

**PhD in Physics and Mathematics** — probability theory and statistical modeling applied to rule efficiency analysis and scoring logic. Additional **15+ years** in corporate finance and banking operations — payment flows, treasury, card and transfer processes, and financial controls — providing rare domain context for payment-adjacent fraud typologies.

---

## Core Skills

**Antifraud & Rules**  
Fraud rule design, YAML/config-driven parameters, threshold tuning, allowlist/blocklist management, multi-signal order validation (BIN, IP, email, phone, user agent, address), bot/return/resell/claim/FTID abuse typologies, real-time severity classification

**ML & Scoring**  
SageMaker-backed scoring, context-aware model routing, shadow predictions for offline validation, feature engineering for fraud signals, customer and order abuse scoring (bot, return, resell, claim, fake profile)

**Data & SQL**  
Python, advanced SQL (CTEs, window functions, complex joins), dbt on BigQuery, Airflow orchestration (~25 production DAGs), Spark on Kubernetes, Google Cloud Spanner, MongoDB, PostgreSQL; data quality tests and centralized schema definitions

**Payment & Banking**  
BIN validation, payment execution, treasury operations, banking documentation, account management, card/transfer flows, cross-border transactions, financial compliance (IFRS/CAS)

**Tooling & Infrastructure**  
AWS Lambda, SQS/SNS/EventBridge, Git/GitHub Actions, CI-based rule updates, Airbyte ingestion, lakehouse patterns on GCS (Hudi/Delta); Advanced Excel and MS SQL for financial analytics

---

## Work Experience

### Antifraud Analyst / Data Engineer — **Yofi Inc.** (USA, remote)  
*February 2022 — October 2025*

Anti-fraud and customer-intelligence platform for **Shopify** merchants (enterprise customers including **Lululemon**). Mission: detect and prevent bot purchases, return fraud, discount abuse, reseller abuse, and fake profiles in real time.

**Fraud rules and threshold management**
- Owned the **central fraud rules repository** — single source of truth for detection parameters across merchants; per-client YAML configurations, threshold tuning, allowlist/blocklist management.
- Built automated sync between runtime Python logic and batch SQL (dbt macros); PR-based rule updates via CI with parity checks between online and offline rule logic.
- Tuned production thresholds — conservative merchant lists, return-rate parameters, allowlisted domains — balancing detection coverage against false positive rate.

**ML scoring and routing**
- Built and maintained **real-time ML scoring** (SageMaker + Lambda): bot probability, discount abuse, refund risk; blocklist/allowlist and trust/risk signal logic driving downstream actions.
- Extended **ML routing layer** — context-aware model selection for return abusers, resellers, claim abusers, LLM-based abuse, and FTID fraud; shadow predictions stored for offline validation and back-testing.
- Contributed to **real-time severity classification** feeding alert and escalation workflows.

**Order validation and event data**
- Maintained **multi-signal order validation**: IP geolocation, user agent, credit card BIN, email, phone, shipping/billing address — integrated into the fraud decision pipeline.
- Supported **event-based ingestion** — orders, webhooks, partner streams — into analytical and operational stores for rules and models.

**Feature analytics and back-testing**
- Shipped **return analytics and back-testing datasets**: return rates, refund line-item analysis, fuzzy customer pattern matching, new fraud typology detection; persisted to operational stores for batch model consumption.
- Built **SQL rule logic and marts in BigQuery/dbt** for historical back-testing, rule efficiency analysis, and monitoring of scoring metrics.
- Performed deep-dive analysis on confirmed abuse cases; translated patterns into rule and feature updates.

**Data platform**
- Operated **~25 Airflow DAGs** and **Spark** workloads on Kubernetes for fraud data pipelines (GCS, BigLake, Hudi/Delta formats).
- Extended **Airbyte** connectors for Shopify historical loads and partner data sources (Klaviyo, Moonsense).

**Stack:** Python, SQL, dbt, Airflow, Spark, SageMaker, BigQuery, Spanner, MongoDB, PostgreSQL, AWS, GCP.

### Business Analyst / AI Platform — **Sinoptics AI** (remote)  
*March 2025 — Present*

- Gathered and structured requirements for document-processing workflows; defined **validation rules** and acceptance criteria — including false-positive review and risk assessment outputs.
- Built **data flows in Python and SQL**, turning semi-structured inputs into reusable datasets for product analytics and AI-assisted validation features.
- Coordinated pilots and cross-functional delivery; prepared clear status and risk reporting for non-technical stakeholders.

### CFO — **Shanghai Aircraft Design Limited Company** (Shanghai, China)  
*November 2017 — 2022*

- Designed multi-layer **payment authorization controls**, spending limits, and compliance frameworks from scratch for a new international entity.
- Full-cycle **banking relationship management**: account administration, payment execution, dispute resolution with financial institutions.

### Executive Director — **Engineering Solutions** / **New Technologies** (China / Russia)  
*2008 — 2017*

- Cross-border trade operations: **counterparty due diligence**, payment flow control, pricing and contract compliance across Russian and Chinese regulatory environments.
- Management accounting and financial control over procurement, sales, and international payment cycles.

---

## Education

- **PhD in Physics and Mathematics**, Southern Federal University, 2000–2003  
  *Probability theory, statistical modeling, mathematical analysis*
- **Physics Diploma (Specialist)**, Southern Federal University, 1994–1999
- **MBA**, RANEPA, 2005–2007
- **College of Radio-Electronic Instrumentation**, 1991–1995

---

## Certifications

- **CAP** — Certified Accountant Practitioner
- **CPA Russia Professional Development Courses:** financial accounting and IFRS reporting, management accounting

---

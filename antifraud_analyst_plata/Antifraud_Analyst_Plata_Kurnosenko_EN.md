# Kurnosenko Vitaly Nikolaevich

**Antifraud Analyst** | Fraud Rule Development | ML-based Detection | Payment Risk | Data Analysis (SQL / Python)

**Location:** Shanghai, China  
**Citizenship:** Russia  
**Phone:** +86 15601694273  
**Email:** vitaly@sinoptics.ai  
**WeChat:** porohnya  
**Skype:** kurnosenko_vitaly  
**Languages:** Russian — native; English — B2 working proficiency; Chinese (Mandarin) — HSK 4

---

## Professional Summary

Engineer and analyst with **direct hands-on experience in antifraud systems** — fraud rule design, ML-based bot and abuse detection, order validation pipelines, threshold tuning, and back-testing. Worked **3+ years** on the Yofi/Botnot anti-fraud platform (USA) serving enterprise Shopify merchants including Lululemon, building and maintaining the full fraud detection stack in **Python**, **SQL**, and **dbt**.

Additional layer: **15+ years** in corporate finance and banking operations, giving deep understanding of payment flows, transaction structures, and financial risk — rare context for an analyst working on payment fraud typologies.

**PhD in Physics and Mathematics** — strong grounding in probability theory and statistical modeling directly applicable to rule back-testing, false positive analysis, and fraud scoring.

---

## Role Fit — Antifraud Analyst Middle

| JD Requirement | My Evidence |
|---|---|
| Test and improve antifraud rules | Maintained `yofi-rules-monorepo` — per-shop YAML rule configs, threshold tuning (`min_return_rate`, `min_fraud_tags`), allowlist/blocklist management, pre-commit parity checks between Python and dbt |
| Optimize rules across channels (card, transfers, tokenization) | Order validation pipeline: BIN validation, IP checks, email, phone, user agent, shipping/billing address signals — multi-signal order risk assessment |
| Fraud detection automation | ML routing pipeline — `ShopifyClaimAbusersModel`, `ShopifyReturnFraudstersModel`, `ShopifyResellersModel`, `FTID_FRAUD_SCORE`, `BOT_ABUSE_SCORE`; SageMaker-backed real-time scoring via Lambda |
| Back-testing and efficiency assessment | Feature analytics Lambda — return rate calculations, refund line items analysis, pattern detection in historical order data persisted to BigQuery/Spanner |
| Analyze confirmed fraud cases, identify new patterns | `is_bad_actor`, `is_blacklisted`, trust/risk signal system; return analytics processor for new fraud typologies |
| Monitor metrics, build queries, dashboards | dbt models on BigQuery, Airflow DAGs, SQL-based analytics pipelines; fraud scoring metrics in Spanner |
| SQL + Python | Python throughout the stack; SQL in rules monorepo (`get_shop_parameters.sql`), dbt models, central SQL definitions |
| 2+ years relevant experience | 3+ years on Yofi/Botnot antifraud platform (Feb 2022 — Oct 2025) + 15 years financial risk and controls |
| Understanding of payment processes and fraud typologies | Treasury, banking operations, payment execution, BIN/card validation — direct domain knowledge |
| Mathematical statistics & probability theory | PhD in Physics & Mathematics |

---

## Core Skills

**Antifraud & Detection Systems**  
Fraud rule design, YAML-based rule configuration and threshold tuning, allowlist/blocklist management, multi-signal order validation (BIN, IP, email, phone, user agent, address), bot/abuse/return fraud/resell fraud typologies, real-time severity scoring

**ML-backed Fraud Scoring**  
SageMaker model routing, shadow prediction pipelines, `PredictionLevel` frameworks, feature engineering for fraud signals, customer and order abuse scoring (bot, return, resell, FTID, claim, fake profile)

**Data & Analytics**  
Python (3.9–3.12), SQL, dbt (BigQuery), Airflow, Spark, Google Cloud Spanner, MongoDB, BigQuery; Advanced Excel, MS SQL for financial analytics

**Payment & Banking Domain**  
BIN validation, payment execution, treasury operations, banking documentation, account management, card/transfer flows, cross-border transactions, financial compliance (IFRS/CAS)

**Infrastructure & Tooling**  
AWS Lambda (SST/CDK/SAM), SQS/SNS/EventBridge, MongoDB, Google Cloud Spanner, Git/GitHub Actions, pre-commit hooks, pytest

---

## Work Experience

---

### Data Engineer / Antifraud Platform — **Yofi Inc. (Botnot platform)** (USA, remote)  
*February 2022 — October 2025*

**Product:** Anti-fraud / customer intelligence platform for **Shopify** merchants (enterprise customers including **Lululemon**). Core mission: detect and prevent bot purchases, return fraud, discount abuse, reseller abuse, and fake profiles in real time.

**Fraud Rules & Threshold Management**
- Owned and maintained **`yofi-rules-monorepo`** — the single source of truth for all fraud model parameters across clients. Defined per-shop YAML rule configurations (`shopify_return_abusers_rule`, `shopify_return_fraudsters_model`, allowlisted domains, `min_return_rate` thresholds), CLI tooling to sync parameters between Python runtime and dbt SQL macros, and GitHub Actions for automated PR-based rule updates.
- Tuned fraud thresholds in production: added conservative shop lists, adjusted return parameters (`min_return_note_rate`, `min_fraud_tags`), managed allowlisted email domains — directly balancing detection coverage against false positive rate.

**ML Bot Detection & Abuse Scoring**
- Contributed to **`botnot-lambda-ml-bot-detection`** — SageMaker-backed Lambda scoring each order for `is_bot_score`, `discount_abuse`, refund probability. Implemented `is_blacklisted`, `is_whitelisted`, `is_bad_actor` decision logic; managed trust/risk signal system (`trust_and_risk_messages`) driving downstream actions.
- Extended **`yofi-lambda-ml-gateway`** — ML routing Lambda selecting models per order/customer context: `ShopifyClaimAbusersModel`, `ShopifyResellersModel`, `ShopifyReturnAbusersModel`, `ShopifyReturnFraudstersModel`, LLM-based abuse scoring, FTID fraud scoring. Persisted shadow predictions to **MongoDB** for offline validation and back-testing.
- Contributed to **`yofi-realtime-severity-engine`** — real-time fraud severity classification feeding downstream alert workflows.

**Order Validation Pipeline**
- Maintained **`botnot-lambda-order-validations`** — multi-signal order risk assessment: IP geolocation validation, user agent analysis, credit card **BIN validation**, email validation, shipping/billing address checks, phone number verification. Integrated validation results into downstream fraud decision pipeline.

**Feature Analytics & Back-testing**
- Shipped new return analytics in **`yofi-lambda-feature-analytics`**: return rate calculations, refund line items analysis, fuzzy customer pattern detection, `ReturnAnalyticsProcessor` for new fraud typologies. Persisted analytics to **Google Cloud Spanner** for batch model consumption.
- Built dbt models in **BigQuery** via `yofi-dbt-models` and `yofi-rules-monorepo` dbt package — SQL-based rule logic and parameter macros used for back-testing rule efficiency across historical order data.

**Data Platform**
- Operated **Airflow** DAGs and **Spark** workloads on Kubernetes for fraud data pipelines (GCS, BigLake, Hudi/Delta table formats).
- Extended **Airbyte** connectors for Shopify historical ingestion and partner data sources (Klaviyo, Moonsense).

---

### DataOps / AI Platform Engineer — **Sinoptics AI** (remote)  
*October 2025 - May 2026*

- Built **AI-assisted document validation** workflows (n8n, Dify): OCR extraction, LLM structuring, compliance report generation including **risk assessment** and validation outputs.
- Operated layered microservice architecture (orchestrator → agents → aggregator) with **RBAC**, audit logs, and regulatory compliance awareness (GDPR/CN).
- Deployed FastAPI + Celery + Redis to K3S on AWS China, automated Yandex Cloud infrastructure (Cloud Functions, managed PostgreSQL, Keycloak).

---

### CFO — **Shanghai Aircraft Design Limited Company** (Shanghai, China)  
*November 2017 — 2022*

- Designed multi-layer payment authorization controls, spending limits, and compliance frameworks from scratch for a new international entity.
- Full-cycle banking relationship management: account administration, payment execution, dispute resolution with financial institutions.

### Executive Director — **Engineering Solutions** / **New Technologies** (China / Russia)  
*2008 — 2017*

- Cross-border trade operations: counterparty due diligence, payment flow control, pricing and contract compliance across Russian and Chinese regulatory environments.

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
- **CPA Russia:** financial accounting, IFRS reporting, management accounting

---


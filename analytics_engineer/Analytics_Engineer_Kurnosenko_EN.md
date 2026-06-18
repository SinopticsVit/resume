# Vitaly Kurnosenko

**Analytics Engineer | SQL · DBT · Airflow · Spark | Data Marts · ETL · Data Quality**

**Place of Residence:** Asia (open to relocation to Limassol, Cyprus)  
**Phone / Skype:** +86 15601694273  
**Email:** rikkimortycrypt@gmail.com  
**WeChat:** porohnya  
**Telegram:** @vitaly_kur  
**Languages:** English — B2 / Upper-Intermediate, fluent spoken and written; Chinese — HSK 4; Russian — native

---

## Professional Summary

Analytics engineer with **3+ years** building production **data marts**, **ETL/ELT pipelines**, and **analytical SQL** on a high-volume e-commerce / anti-fraud platform (**Yofi / Botnot**, USA — **Shopify** merchants including **Lululemon**). Translate business and analyst needs into **dbt models**, **Airflow** DAGs, and **Spark** jobs; document schemas and business logic; enforce **data quality** with automated tests and operational monitoring.

Strong in **advanced SQL** (CTEs, window functions, complex joins, query tuning on **BigQuery** and **PostgreSQL**), **Python** for data processing (**pandas**, **PySpark**), and **dbt** transformation DAGs on **BigQuery**. Hands-on with **lakehouse** patterns (**Hudi**, **Delta Lake**, **BigLake**, **GCS**) and **~25 production Airflow DAGs** orchestrating ingestion and mart refresh. Comfortable collaborating with product and analyst stakeholders in international teams.

PhD in mathematical sciences; background in finance and KPI-driven reporting helps connect metrics definitions to reliable datasets.

---

## Core Skills (mapped to the role)

| Area | Tools and experience |
|------|----------------------|
| **SQL (advanced)** | Complex analytical queries — **CTEs**, **window functions**, subqueries, aggregations at scale; **BigQuery**, **PostgreSQL**, **MSSQL**, **Spanner**; query profiling and performance tuning; centralized **SQL data definitions** shared across services |
| **DBT** | **dbt-bigquery** projects, transformation DAGs, **incremental** and mart-layer models, **model documentation**, **sqlfluff** / **sqlfmt** linting; merchant-specific model sets (e.g. enterprise retail analytics) |
| **Python (data)** | **pandas** / **pandas-gbq** for ad-hoc analysis and local ETL scripts; **PySpark** batch jobs; **boto3**, **google-cloud-bigquery**; task automation and pipeline helpers |
| **Orchestration** | **Airflow** on **Google Composer / GKE** (~25 production DAGs): **KubernetesPodOperator** for Spark/Python, **Airbyte** sync DAGs, Slack alerting on failures, retries and resilient trigger rules |
| **Spark & lakehouse** | **PySpark** on **Dataproc Serverless** and **Spark on Kubernetes**; **Hudi**, **Delta Lake**, **BigLake** on **GCS**; partitioning and shuffle tuning for large event volumes |
| **OLAP / warehouses** | **BigQuery** as primary analytical store; **MongoDB**, **Redis**, **Neo4j**, **Spanner** as operational sources; lake-to-warehouse pipelines (`mongodb_to_biglake`, `spanner_to_bigquery`, analytics / sessions / stats marts) |
| **Data quality & docs** | **dbt tests**, schema contracts, null / consistency fixes in production models; **GitBook** internal data/API documentation; code reviews and shared SQL conventions |
| **Ingestion & integrations** | **Airbyte** (custom **Klaviyo** sources, forked platform), **Shopify** historical ingestion, partner webhooks; **GraphQL** and REST source integration |
| **Analytical thinking** | Anti-fraud and e-commerce domain — orders, billing, customer clusters, fraud confirmation codes, merchant KPIs; ROI dashboards and operational reporting |
| **Plus / adjacent** | Open table formats (**Hudi/Delta** — concepts transferable to **Iceberg**); OLAP-style workloads on **BigQuery** (not **ClickHouse** in production yet, strong SQL foundation) |

---

## Professional Experience

### Analytics Engineer / Data Engineer — Yofi Inc. (USA)
*February 2022 — October 2025 (remote)*

Yofi is an anti-fraud and customer-intelligence platform for **Shopify** merchants (enterprise customers including **Lululemon**). Owned the analytics-engineering slice of the data platform on internal **Botnot** codebases.

- Translated analyst and product requirements into **dbt** models and **BigQuery** marts: fraud indicators, order/customer dimensions, merchant-specific reporting layers; maintained **sqlfluff**-based SQL quality gates and model refactors for schema consistency.
- Built and maintained **ETL/ELT** pipelines with **Airflow** (~25 production DAGs): **Spark** jobs on **Kubernetes**, **Airbyte** synchronization, incremental and full-refresh patterns, **Slack** alerts on DAG failures.
- Developed **PySpark** jobs for lakehouse ingestion and transformation — **GCS + BigLake + Hudi/Delta** (`raffles_to_hudi`, `mongodb_to_biglake`, `firestore_to_bq`, `spanner_to_bigquery`, analytics / sessions / stats pipelines); tuned partitioning and IO for high-volume event processing.
- Wrote and optimized **SQL** for analytical tasks — complex joins across operational stores (**MongoDB**, **PostgreSQL/RDS**, **Spanner**) and the warehouse; used window functions and CTEs for sessionization, funnel, and fraud-confirmation logic.
- Ensured **data quality** through **dbt tests**, null-handling fixes, and validation in Spark/Airflow steps; contributed to **central SQL data definitions** so application and analytics schemas stay aligned.
- Documented data models, pipeline behavior, and business rules in **GitBook** and repo READMEs; participated in **code reviews** and trained analysts and engineers on **dbt**, **Airbyte**, and **Spark** practices.
- Monitored and troubleshooted pipeline issues: idempotent DAG design, retry policies, runbook-driven incident response alongside DataOps alerting.
- Supported **ROI** and operational dashboards; used **pandas** / **pandas-gbq** in ad-hoc data-engineering scripts for exploration, normalization, and one-off mart backfills.

**Stack:** SQL, Python, PySpark, DBT, Airflow, Airbyte, BigQuery, GCS, BigLake, Hudi, Delta Lake, PostgreSQL, MongoDB, Redis, Neo4j, Spanner, GraphQL, AWS (Lambda, S3, SQS/SNS), GCP (GKE, Cloud Build, Pulumi).

### Business Analyst / AI Platform Engineer — Sinoptics AI
*March 2025 — present (remote)*

- Gathered and structured requirements between business and engineering for document-processing and analytics workflows; defined validation rules and readiness criteria that improved reporting transparency.
- Built data flows on **Python** and **SQL**, turning semi-structured inputs into reusable datasets for product analytics and AI features.
- Coordinated pilots and cross-functional delivery; prepared stakeholder-facing status and risk reporting.

### Head of IT and Finance — Engineering Solutions LLC
*March 2013 — December 2017*

- Led financial and IT operations: investment analysis, budgeting, management reporting, and process automation supporting KPI tracking and operational control.

### Head of IT Department — New Engineering Solution
*April 2003 — February 2013*

- Owned ERP and reporting systems; built structured internal reporting and data-management practices for management decision-making.

---

## Relevant Yofi / Botnot Projects

| Project | Analytics-engineering contribution |
|---------|-----------------------------------|
| **yofi-dbt-models** | dbt-bigquery marts, SQL refactors, fraud-code datasets, sqlfluff/sqlfmt standards |
| **Yofi-airflow-dags** | Production DAGs — Airbyte sync, dynamic operators, Composer/GKE orchestration |
| **Yofi-Spark-jobs** | PySpark transformations, timestamp/JSON fixes, Airbyte API integration in batch jobs |
| **yofi-data-eng-scripts** | pandas-gbq ad-hoc ETL, BigQuery/Mongo exploration, local pipeline experiments |
| **botnot-central-SQL-data-definitions** | Single source of truth for relational schemas shared with analytics layers |
| **Airbyte / Shopify ingestion** | Klaviyo custom sources, historical Shopify loads, partner event webhooks into the lake |

---

## Education

- **RPANEPA** — MBA, Information Technology *(September 2005 — May 2007)*
- **Southern Federal University** (formerly Rostov State University) — PhD, Mathematical Sciences *(September 1994 — May 2003)*

---

## Certifications and additional training

- **Certified Accountant Practitioner (CAP)**
- Advanced training: **Financial accounting and reporting (IFRS)**, **Management accounting**

---

## Additional Information

- Open to relocation to **Limassol, Cyprus**; experienced in international remote teams (USA, China, Thailand).
- Strong bridge between **business metrics**, **analyst requirements**, and **production data pipelines** — comfortable owning the full path from requirement to tested mart.
- High-load, partner-facing product context: real-time order/webhook ingestion, billing quotas, and ML-adjacent feature pipelines feeding downstream analytics.

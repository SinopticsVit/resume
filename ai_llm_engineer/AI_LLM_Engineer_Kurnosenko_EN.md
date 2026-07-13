# Vitaly Kurnosenko

**Senior AI / LLM Engineer | Python · Agentic Workflows · RAG · Production APIs**

**Location:** Shanghai, China (open to remote)  
**Phone:** +86 15601694273  
**Email:** rikkimortycrypt@gmail.com  
**Telegram:** @vitaly_kur  
**Languages:** English — B2 (professional reading and communication); Russian — native; Chinese — HSK 4

---

## Professional Summary

Senior AI / LLM Engineer with **20+ years in software engineering** and **4+ years building production data and ML systems**. Design and operate **scalable, low-latency AI services** in Python: LLM orchestration, **multi-agent workflows**, RAG, real-time APIs, and cloud-native deployment on **AWS and GCP**.

Recent focus: architecting **agentic automation platforms** that unify multi-channel inputs (Telegram, WeChat, email, web, API/webhooks), run reasoning pipelines, and return reliable structured outputs for business workflows. Strong ownership mindset — comfortable across architecture, backend services, MLOps, and production operations in fast-moving environments.

---

## Core Skills

| Area | Technologies and practices |
|------|---------------------------|
| **AI / LLM** | LLM orchestration, prompt engineering, structured output (JSON Schema), streaming inference patterns, multi-agent systems, tool calling, LLM-as-judge |
| **Agent frameworks** | Dify, n8n, LangChain-compatible orchestration patterns, MCP integrations, orchestrator → domain agents → aggregator architectures |
| **RAG** | Vector indexes, semantic + metadata chunking, hybrid retrieval, reranking, KB freshness, faithfulness / groundedness checks |
| **Python backends** | FastAPI, Celery, async workers, REST APIs, type hints, production debugging, microservices |
| **ML in production** | Feature pipelines, real-time scoring, SageMaker, A/B and shadow deployment, model routing, quality monitoring |
| **Data & messaging** | PostgreSQL, MongoDB, Redis, BigQuery, SQS/SNS, event-driven architectures, SQL + NoSQL data design |
| **Cloud & MLOps** | AWS (Lambda, SageMaker, EC2, ECR, SQS/SNS, Secrets Manager), GCP (GKE, BigQuery, GCS), Docker, Kubernetes (K3S, GKE), GitHub Actions, CodeBuild |
| **Observability** | Structured logging, pipeline alerting, Prometheus/Grafana (Helm), fault tolerance, retries, audit logs |

---

## Professional Experience

### Senior AI / LLM Engineer — Sinoptics AI
*October 2025 — Present · remote*

AI platform for **intelligent document processing and agentic business automation**. End-to-end ownership from multi-channel ingestion to production-grade AI services and structured outputs.

**LLM orchestration and agentic workflows:**

- Architected a **multi-agent processing pipeline**: ingestion (Telegram, WeChat, email, web, API) → OCR / Vision LLM → LLM structuring → orchestrator → domain agents (Finance, Accounting, Legal, Logistics) → aggregated validation / compliance / risk report.
- Built a **production Dify workflow** (24 nodes, 34 edges): PDF/image intake → OCR / PDF parsing → LLM field extraction → external verification → **5 parallel domain agents** → final report; webhook-triggered, fault-tolerant execution.
- Orchestrated **n8n workflows** and **multi-agent architectures** with RBAC, audit logs, retry logic, and error handling for long-running AI tasks.
- Designed **reasoning and task-automation pipelines** for real-world business workflows: supplier due diligence, invoice validation, compliance checks, and proactive exception surfacing.

**RAG and knowledge systems:**

- Built a **RAG system** on Dify for corporate knowledge bases: metadata-aware chunking, vector indexes, retrieval context for agents, versioning and freshness controls.
- Implemented **structured LLM output** via JSON Schema and constrained prompting; post-processing, validation, and human-in-the-loop review.

**Production APIs and infrastructure:**

- Deployed **on-premise LLM platform** (Dify v1.10): Docker Compose, PostgreSQL, nginx, TLS.
- Migrated **FastAPI + Celery + Redis** services to **K3S on AWS EC2**; hybrid CI/CD (**GitHub Actions → CodeCommit → CodeBuild → ECR → kubectl**), secrets in AWS Secrets Manager.
- Integrated external APIs and web sources for enrichment and verification in agent tool chains.

**Stack:** Python, FastAPI, Dify, n8n, OpenAI-compatible LLM APIs, OCR / Vision AI, RAG, PostgreSQL, Redis, Docker, K3S/Kubernetes, AWS, Yandex Cloud.

---

### ML Engineer / Data Engineer — Yofi Inc. (USA)
*February 2022 — October 2025 · remote*

Anti-fraud and customer-intelligence platform for **Shopify** enterprise merchants (**Lululemon** and others). Built and operated **real-time ML services** and data infrastructure at scale.

- Developed **production ML pipelines**: bot detection, abuse scoring, behavioral feature engineering, **real-time scoring** via AWS SageMaker and Lambda.
- Built **ML gateway and safe model rollout**: SNS/SQS-triggered Python services, model routing, **shadow predictions** in MongoDB, **A/B testing** without production risk.
- Delivered **FastAPI prediction services** for behavioral telemetry and real-time risk assessment.
- Operated data plane over **1B+ events** (GCS, BigQuery, Hudi/Delta); Spark jobs on Kubernetes for training data preparation.
- Implemented **monitoring, data quality gates, and automated pipeline testing** to reduce production incidents and model drift impact.
- Integrated multi-source data (Shopify, Klaviyo, Moonsense) via Airbyte connectors and webhook pipelines.

**Stack:** Python, SQL, PySpark, FastAPI, AWS SageMaker, Lambda, SQS/SNS, MongoDB, Neo4j, Redis, BigQuery, Airflow, dbt, Docker, Kubernetes (GKE).

---

### Head of IT and Finance — Engineering Solutions LLC
*March 2013 — December 2017 · Moscow*

- Led IT infrastructure and financial systems; ERP implementation, reporting automation, cross-functional delivery under business constraints.

### Head of IT Department — New Engineering Solution
*April 2003 — February 2013 · Moscow*

- Owned corporate ERP, IT infrastructure, and reporting systems; early data discipline and process automation.

---

## Selected Projects

- **Multi-channel agent orchestration** — unified Telegram / WeChat / email / API inputs into a single intelligent workflow with parallel domain agents and structured final reports.
- **Supplier due diligence workflow** — OCR + LLM extraction + external verification + multi-agent analysis for compliance and risk assessment.
- **OCR forms pipeline** — template-based extraction from scanned trade and logistics documents with validation and post-processing.
- **Real-time ML routing** — production gateway for model selection, shadow deployment, and A/B rollout in a high-volume e-commerce environment.

---

## Education

- **Southern Federal University** — PhD, Mathematical Sciences *(1994 — 2003)*
- **RPANEPA (RANEPA)** — MBA, Information Technology *(2005 — 2007)*

---

## Certifications

- **Certified Accountant Practitioner (CAP)** — IFRS financial reporting, management accounting

---

## Additional

- Comfortable in **remote, async, cross-functional teams**; strong product and ownership mindset in startup-paced environments.
- PhD-level foundation in **mathematical modeling and statistical reasoning** — useful for evaluation design and production AI reliability.
- Ready to discuss: **agentic orchestration**, **RAG architecture**, **real-time Python APIs**, **ML production rollout**, **structured LLM output**, and **observability for AI systems**.

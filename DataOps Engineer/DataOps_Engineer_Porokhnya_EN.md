# Vitaly Kurnosenko

**DataOps / Big Data Engineer | Kubernetes & Spark | Data Lake | CI/CD | On-prem AI**

**Place of Residence:** Asia (open to relocation to Limassol, Cyprus)  
**Phone / Skype:** +86 15601694273  
**Email:** rikkimortycrypt@gmail.com  
**WeChat:** porohnya  
**Telegram:** @vitaly_kur  
**Languages:** English — B2 / Upper-Intermediate, fluent spoken and written; Chinese — HSK 4; Russian — native

---

## Professional Summary

DataOps / Big Data engineer with hands-on experience operating Kubernetes clusters (GKE and **K3S/Rancher** on bare-metal EC2), running **Spark on Kubernetes**, building Data Lakes on object storage (S3, GCS, Yandex Object Storage), and deploying **on-premise AI infrastructure**. Cover the full lifecycle — capacity planning, networking, security, CI/CD, monitoring, and disaster recovery.

5+ years on production data platforms in international fintech / e-commerce products (Yofi, USA — anti-fraud for Shopify / Lululemon; Sinoptics AI — on-prem AI for invoice / document processing). Strong in Python and SQL, comfortable maintaining Java/Scala Spark jobs and reading/patching Go services. Linux is my primary production environment.

Core strengths: physical implementation of Big Data environments, Spark/Hadoop performance tuning, security-by-design (Workload Identity, Secrets Manager, RBAC), incident management, and SLO-grade operational discipline.

---

## Core Skills (mapped to the role)

| Area | Tools and experience |
|------|----------------------|
| Containers / Orchestration | Docker, containerd, Kubernetes, GKE, **K3S (Rancher)** on bare-metal AWS EC2, Helm, KubernetesPodOperator, Workload Identity, namespaces, RBAC, image pull secrets |
| Big Data & Spark | **PySpark on Dataproc Serverless / Spark on K8s**, custom Debian-based Spark Docker images, Hudi, Delta Lake, BigLake, Hadoop FS, partitioning, performance tuning |
| Data Lake / Object Storage | **S3** (AWS, incl. China region), GCS, Yandex Object Storage, BigLake, lakehouse patterns (Hudi/Delta), Trino-class engines (BigQuery, Athena) |
| Languages | **Python** (PySpark, FastAPI, Airflow, boto3, k8s client), **SQL** (PostgreSQL, BigQuery, Spanner, MSSQL, Trino-style), JavaScript/TypeScript; read and patch **Java/Scala** Spark jobs and **Go** services |
| Linux & networking | Ubuntu/Debian, systemd, bash, nginx, certbot/Let's Encrypt, UFW, IPtables, DNS, TLS, jemalloc tuning |
| CI/CD & Automation | **GitHub Actions**, **AWS CodeCommit + CodeBuild**, Google Cloud Build, **Pulumi (IaC)**, bash deployment scripts in the spirit of Ansible/Chef for PostgreSQL and stack installers, Docker BuildKit |
| Data orchestration | Airflow (KubernetesPodOperator pattern), Airbyte, DBT, Hatchet, n8n |
| Security & DR | AWS Secrets Manager, GCP Secret Manager, IAM / Workload Identity, RBAC, encryption at-rest / in-transit, automated PostgreSQL backups with retention, Slack alerting on DAG failures |
| Monitoring & Alerting | Cloud Logging / Monitoring, Slack webhooks, structured logs, runbook-driven incident response |
| AI infrastructure | **On-prem Dify** (LLM platform) on Ubuntu VM with Docker Compose, Hatchet workflow engine on K8s, OCR / LLM pipelines, retrieval / agent context |

---

## Professional Experience

### DataOps / AI Platform Engineer — Sinoptics AI
*March 2025 — October 2025 (remote)*

- Deployed and operate an **on-premise AI stack** for document (invoice) processing: Dify v1.10 on Ubuntu VM in Yandex Cloud + PostgreSQL, isolated Docker Compose stack, nginx as edge with automatic Let's Encrypt issuance and rotation via certbot.
- Migrated a FastAPI + Celery / Redis microservice onto a **K3S cluster (Rancher)** on bare-metal AWS EC2 (China region, `cn-northwest-1`); built a hybrid CI/CD: GitHub Actions → AWS CodeCommit → CodeBuild → ECR → `kubectl rollout`, with kubeconfig stored in AWS Secrets Manager.
- Stood up a **Hatchet workflow engine on K8s** (namespace, ingress, external secrets) to orchestrate long-running OCR / LLM tasks; configured pod monitoring and alerting.
- Implemented automated PostgreSQL deployment and backup on Ubuntu (bash scripts in the style of an Ansible role: package install, `pg_hba.conf` / `postgresql.conf` tuning, UFW, 7-day retention backups, cron).
- Designed a layered document-processing architecture (n8n → specialized AI agents → aggregator → report) with a security model (RBAC, encryption at-rest/in-transit, audit logs, GDPR / Chinese data law compliance).

### Data Engineer — Yofi Inc. (USA)
*February 2022 — October 2025*

Yofi is an anti-fraud / customer-clustering platform for Shopify merchants (Lululemon and others), where I owned the DataOps part of the Big Data stack.

- Operated **GKE clusters** (`yofi-hub`) across dev/prod GCP projects: configured Workload Identity, image pull secrets for Google Artifact Registry, namespace separation (`hub-dev` / `hub-prod`), roles/rolebindings via `kubectl apply`, context switching, and kubeconfig management.
- Ran **Spark on Kubernetes** via the `KubernetesPodOperator` pattern in Airflow + Dataproc Serverless: built custom **Debian 11/12 Docker images** for Spark with Hudi, Delta Lake, MongoDB connector, BigQuery jar, jemalloc memory tuning, conda/mamba and a scientific Python stack.
- Built a Data Lake layer on **GCS + BigLake + Hudi/Delta** (`raffles_to_hudi`, `mongodb_to_biglake`, `firestore_to_bq`, `spanner_to_bigquery`, `analytics` / `sessions` / `stats` pipelines); tuned partitioning, IO throughput, and shuffle parameters for jobs spanning 1B+ events.
- Maintained **Airflow** (~25 production DAGs): a `create_kpo_task` wrapper around `KubernetesPodOperator`, Slack alerting on failures, env vars, retry policies, `TriggerRule.ALL_DONE` for resilient pipelines; CI for pod images via **Google Cloud Build** to Artifact Registry with `:latest` and `:${SHORT_SHA}` tags.
- Owned **infrastructure-as-code** via **Pulumi** (Python) for the base GCP estate: BigQuery, GCS, Cloud Functions, IAM, dev/prod stacks.
- Integrated the AWS side of the platform: dozens of Lambdas (Node.js / Python) behind API Gateway, SQS/SNS, EventBridge, RDS, Cognito, Neptune, Aurora; CDK batch refresh counters; CloudFormation/CDK for base VPC / Cognito / Secrets / EC2 resources.
- Implemented **disaster recovery & security**: Secrets Manager, encryption, GCS versioning, idempotent DAGs with persisted state in Redis, Slack alerting and runbooks; participated in incident response for ingestion-pipeline failures.
- Provided **DataOps consulting** to product teams: API documentation in GitBook, KPO task templates, training on DBT, Airbyte, and Spark best practices.

**Stack:** Python, SQL, JavaScript, PySpark, Spark, Hudi, Delta Lake, Airflow, Airbyte, DBT, Kubernetes (GKE), Docker, Pulumi, GCP (BigQuery, GCS, BigLake, Spanner, Pub/Sub, Cloud Build, Artifact Registry, IAM / Workload Identity), AWS (S3, Lambda, API Gateway, SQS/SNS, RDS, Secrets Manager, EC2, ECR, CodeBuild, CodeCommit), MongoDB, PostgreSQL, Neo4j, Redis, Slack alerting.

### Head of IT and Finance — Engineering Solutions LLC
*March 2013 — December 2017*

- Led IT and finance functions; oversaw rollout and operation of ERP, reporting systems, and office IT infrastructure.
- Supported cross-functional decision-making through systems thinking, governance, and process automation.

### Head of IT Department — New Engineering Solution
*April 2003 — February 2013*

- Owned ERP, corporate IT infrastructure, and reporting systems; introduced practices around structured data management and automation.

---

## Relevant Projects (open-source / personal)

- **k3s-fastapi-app** — production template for FastAPI + Celery + Postgres + Redis on K3S / AWS EC2 with hybrid CI/CD (GitHub Actions → CodeCommit → CodeBuild → ECR → K3S).
- **dify-vm-ubuntu** — one-shot installer for on-prem Dify (Multi-Database Era) on Ubuntu 22.04+ with Postgres / MySQL / OceanBase support, nginx, and certbot.
- **postgresql-yandex-vm** — bash automation (Ansible-role style) for the full PostgreSQL deployment lifecycle on Ubuntu: packages, `pg_hba` / `postgresql.conf`, UFW, retention-aware backups, monitoring.
- **yofi-airflow-kubernetes-operator** — KubernetesPodOperator pattern for Spark/Python jobs on GKE with Workload Identity, Cloud Build pipeline, and dev/prod separation.

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

- Open to relocation to Limassol, Cyprus; experienced living and working across multiple countries (Russia, China, Thailand) and cross-cultural teams.
- Strong focus on security best practices, disaster recovery, and incident management in business-critical environments (anti-fraud, finance).
- Continuously follow Big Data / AI ecosystem developments and use generative AI tools to accelerate operational tasks and runbook authoring.

# Vitaly Kurnosenko

**Senior Tester-DevOps | E2E Automation | CI/CD & Release Quality | Cloud / Kubernetes | AI Platforms**

Remote (UTC+8) | Telegram: @vitaly_kur | Email: rikkimortycrypt@gmail.com  
Citizenship: Russia  
Languages: English — B2+ (working); Russian — native; Chinese — HSK 4

---

## Target Role

- **Senior Tester-DevOps** — full-time remote quality + delivery for **Gonka** testnet/mainnet: catch regressions before release, harden deploy pipelines, stabilize AI-compute / L1 workflows
- Focus: **E2E & integration automation**, **test environments**, **CI quality gates**, **observability**, and release confidence for a decentralized AI-compute network

---

## Profile

Engineer at the intersection of **QA automation** and **DevOps**: I build end-to-end test systems that run against real cloud stacks, wire them into **CI/CD**, and treat release stability as an engineering product — not a checklist.

At **Yofi** (USA fintech / anti-fraud, Shopify-scale), I owned a **serverless Robot Framework E2E harness** (`botnot-lambda-serverless-robot-test` / SST stack `yofi-robot-e2e-test`): API, shop lifecycle, and performance suites that inject **SNS/SQS** events, call production-like APIs, and assert state in **Spanner/Mongo**. I also maintained **integration-test environments** (SAM/pytest) against **ES / RDS / Neptune**. At **Sinoptics**, I added **Playwright** E2E and hybrid **GitHub Actions → CodeBuild → ECR → K3S** delivery for AI workloads.

Comfortable with **distributed systems**, **AI inference/training pipelines**, and production incident discipline. Ready to apply the same release-hardening approach to **Gonka** (Cosmos SDK / Go L1, API + ML nodes, Proof of Compute).

---

## Fit — Senior Tester-DevOps @ Gonka

| Need | Evidence |
|------|----------|
| Reduce bugs on new releases | Built regression E2E that validates API + async pipelines + DB state before/after deploy; smoke + teardown patterns for clean re-runs |
| E2E / integration automation | **Robot Framework** suites (API flow, shop install/billing, performance SLAs); **pytest** integration env; **Playwright** UI E2E |
| Tester + DevOps hybrid | Own both test code and runtime: **SST/CDK Lambda** test runner, SAM local stacks, **K8s** deploys, GitHub Actions / CodeBuild / Cloud Build |
| Environments & isolation | Dedicated **integration-test-environment** (dev-like AWS: ES, RDS, Neptune); stage-aware SST profiles (`dev`/`prod`) |
| Distributed / async systems | Event-driven checks: SNS/SQS → persist → API assert; webhooks, retries, idempotency-minded cleanup |
| AI / compute-adjacent | Yofi ML routing & bot-detection pipelines; Sinoptics on-prem **LLM/OCR** stack (Dify, Hatchet on K8s) — familiar with inference/training ops failure modes |
| Observability & ops | Prometheus/Grafana (Helm), Slack ops alerts, structured logs, incident participation on data/API platforms |
| Blockchain L1 (Cosmos/Go) | Strong distributed-systems & Go-reading background; ready to ramp on Cosmovisor, testnet nets, node/API/ML harnesses quickly |

---

## Key Skills

| Area | Tools & practice |
|------|------------------|
| E2E & API automation | **Robot Framework**, custom Python libraries, fixture events/expected JSON, **pytest**, **Playwright** |
| Test design | Smoke / regression / performance SLA; negative paths; teardown & data isolation |
| CI/CD & quality gates | **GitHub Actions**, AWS CodeBuild/CodeCommit, Google Cloud Build, pipeline-as-code |
| Infra as code | **SST + AWS CDK**, SAM/CloudFormation, **Pulumi**, Helm |
| Runtime / platforms | AWS Lambda, API Gateway, SNS/SQS, **Kubernetes** (GKE, K3S/Rancher), Docker |
| Data validation | Spanner, MongoDB, PostgreSQL/RDS, Elasticsearch, Neptune — assert post-pipeline state |
| Observability | Prometheus, Grafana, Cloud Logging/Monitoring, Slack alerting |
| Domains | Fintech anti-fraud, AI document/LLM platforms, high-volume event pipelines |

---

## Highlighted E2E Work (Yofi / botnot)

### Serverless Robot Framework E2E — `botnot-lambda-serverless-robot-test`

- SST app **`yofi-robot-e2e-test`**: run **Robot Framework** suites inside **AWS Lambda** (Python 3.9) with CDK layers and stage profiles
- **API flow** (`api-flow-testcases.robot`): inject orders via **PERSIST_TOPIC**, assert Spanner persistence, validate dashboard/customer/order APIs against expected JSON
- **Shop flow** (`shop-flow-testcases.robot`): install/finish, billing subscription upgrade, Shopify webhook/API checks, teardown of products/orders
- **Performance flow** (`performance-flow-testcases.robot`): customer/order list latency gates (e.g. response within 10s)
- Maintained suites through datastore migration (Mongo → Spanner assertions); recent work fixing flaky tests for stable regression runs

### Integration test environment — `botnot-integration-test-environment`

- SAM/pytest harness for local + cloud integration against **Elasticsearch, RDS, Neptune**
- CLI/conftest-driven runs; GitHub Actions demo wiring for automated checks

### UI E2E (Sinoptics + Yofi portals)

- **Playwright** critical journeys (auth, document upload, multi-domain Next.js)
- Portal E2E patterns in Svelte merchant frontend (`test:e2e`)

---

## Work Experience

### QA / Platform Engineer — Sinoptics (AI / compliance)

*March 2025 — Present · Remote*

- Own web + platform quality: **Playwright** E2E, component/API checks, release validation before static/cloud deploy
- Migrated **FastAPI + Celery + Redis** to **K3S**; hybrid CI/CD (**GitHub Actions → CodeBuild → ECR → kubectl**); secrets in AWS Secrets Manager
- Operate on-prem **AI** stack (Dify, PostgreSQL, Hatchet on K8s) — treat LLM/OCR pipelines as production systems with backups, TLS, and alertable failures

### Data / Backend Engineer & Test Automation — Yofi (fintech / AI, USA)

*February 2022 — March 2025 · Remote*

- Built and maintained **serverless Robot Framework E2E** for Shopify anti-fraud platform (API, shop lifecycle, performance)
- Stood up / extended **integration-test environments** and **pytest** coverage across Lambda and data services
- Delivered **CI/CD** and IaC (SST/CDK, SAM, Pulumi); GKE hub, Spark/Airflow data plane; GitBook for API consumers
- Validated async order/ML pipelines end-to-end: webhooks → queues → persistence → API — the same shape as off-chain compute + on-chain accounting

### Earlier — IT / Systems leadership (finance)

*2003 — 2017*

- Head of IT / finance systems: ERP, reporting, operational reliability under business constraints

---

## Education

- MBA, RANEPA (CIO track), 2007
- PhD (Candidate of Physical and Mathematical Sciences), Southern Federal University, 2003
- Specialist, Radiophysics, Southern Federal University, 1999

---

## Additional

- Time zone **UTC+8**; async-friendly remote collaboration
- Strengths: release ownership, reproducible test envs, clear failure reports, bridging QA and platform engineering
- Motivated by Gonka’s goal: useful AI compute as consensus work — and by making testnet/mainnet releases boringly stable

---

*Resume prepared for Senior Tester-DevOps @ Gonka (gonka.ai / github.com/gonka-ai/gonka)*

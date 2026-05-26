# yandex-db

**Path:** `D:/_sinoptics_git/yandex-db`  
**Category:** sinoptics-repo  
**Primary language:** YAML  
**Status:** present on disk

## 1. Purpose (2-3 lines)

Internal **Sinoptics** repository `yandex-db` under category **sinoptics-repo**. Supports Yofi/Botnot platform capabilities (e-commerce intelligence, anti-fraud adjacent services, data plane, or infrastructure) as evidenced by repository layout and manifests.

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** YAML
- **Top-level layout:** see listing below.

_No common manifest files found at repository root._


## 3. Architecture

```mermaid
flowchart LR
  subgraph edge [Clients]
    UI[Web_or_Bot]
  end
  subgraph orch [Orchestration]
    WF[n8n_or_K8s_or_FastAPI]
  end
  subgraph ai [AI_Data]
    OCR[OCR_LLM]
    PG[(PostgreSQL_Redis)]
  end
  UI --> WF
  WF --> OCR
  WF --> PG
```

- **Inbound:** HTTP (API Gateway / ALB), scheduled triggers, queues (SQS/SNS), EventBridge rules, or batch — infer from `stacks/`, `template.yaml`, `sst.config.ts`, or `src/` handlers.
- **Outbound:** databases and external HTTP APIs per layers and `package.json` / Python imports in handlers.
- **IaC pattern:** SST/CDK, SAM/CloudFormation, Pulumi, Helm, Terraform, or raw scripts — see manifests section.

## 4. Key files (auto-discovered)

- **Top-level entries:**

```
.github
.vscode
DB_CHANGES_LAST_2_STEPS.md
DEPLOYMENT_SPEC_EN.md
```

## 5. My contribution / role (evidence from git history — if available)

```text
a3b7d27 2026-04-22 Update 2026-04-22 09:47
281e54b 2026-04-22 Update 2026-04-22 09:32
093eec4 2026-04-21 Update 2026-04-21 17:46
fd62922 2026-04-20 Update 2026-04-20 10:36
563da69 2026-03-05 Update 2026-03-05 10:38
d620cfe 2026-02-27 Update 2026-02-27 10:42
a2932a5 2026-02-27 Update 2026-02-27 10:21
e6bf564 2026-02-24 Update 2026-02-24 17:43
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets

_No snippet candidates matched (handler.py / stack.ts / template.yaml etc.). Expand manually after opening the repo._

## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`yandex-db`** capabilities aligned with **sinoptics repo** delivery.
- Applied **YAML** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Sinoptics** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yandex-db`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

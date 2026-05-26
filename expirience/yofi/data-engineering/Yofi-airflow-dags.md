# Yofi-airflow-dags

**Path:** `D:/botnot/Yofi-airflow-dags`  
**Category:** data-engineering  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# Yofi-airflow-dags
airflow script for google composer

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

### `README.md`

```
# Yofi-airflow-dags
airflow script for google composer
```

### `readme.md`

```
# Yofi-airflow-dags
airflow script for google composer
```

### `Readme.md`

```
# Yofi-airflow-dags
airflow script for google composer
```


## 3. Architecture

_High-level: see README and `stacks/` / `src/` layout for service-specific flow._

- **Inbound:** HTTP (API Gateway / ALB), scheduled triggers, queues (SQS/SNS), EventBridge rules, or batch — infer from `stacks/`, `template.yaml`, `sst.config.ts`, or `src/` handlers.
- **Outbound:** databases and external HTTP APIs per layers and `package.json` / Python imports in handlers.
- **IaC pattern:** SST/CDK, SAM/CloudFormation, Pulumi, Helm, Terraform, or raw scripts — see manifests section.

## 4. Key files (auto-discovered)

- **Top-level entries:**

```
.github
.gitignore
.idea
README.md
src
```

## 5. My contribution / role (evidence from git history — if available)

```text
f0b5422 2023-06-30 remove dag metastore
484de91 2023-06-30 ss
b64d1c3 2023-06-08 add bew single dag
ef9cc2c 2023-06-08 add dynamic_operator
9972432 2023-06-06 delete _future_
020c5b6 2023-06-06 add ip
b226877 2023-06-06 add airbyte synch dag
3a8a765 2023-06-04 Merge pull request #184 from BotNotOrg/hotfix/klaviyo-dag
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets

_No snippet candidates matched (handler.py / stack.ts / template.yaml etc.). Expand manually after opening the repo._

## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`Yofi-airflow-dags`** capabilities aligned with **data engineering** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `Yofi-airflow-dags`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

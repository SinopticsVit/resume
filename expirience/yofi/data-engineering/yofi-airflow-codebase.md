# yofi-airflow-codebase

**Path:** `D:/botnot/yofi-airflow-codebase`  
**Category:** data-engineering  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# yofi-airflow-codebase

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

### `README.md`

```
# yofi-airflow-codebase
```

### `readme.md`

```
# yofi-airflow-codebase
```

### `Readme.md`

```
# yofi-airflow-codebase
```


## 3. Architecture

_High-level: see README and `stacks/` / `src/` layout for service-specific flow._

- **Inbound:** HTTP (API Gateway / ALB), scheduled triggers, queues (SQS/SNS), EventBridge rules, or batch — infer from `stacks/`, `template.yaml`, `sst.config.ts`, or `src/` handlers.
- **Outbound:** databases and external HTTP APIs per layers and `package.json` / Python imports in handlers.
- **IaC pattern:** SST/CDK, SAM/CloudFormation, Pulumi, Helm, Terraform, or raw scripts — see manifests section.

## 4. Key files (auto-discovered)

- **Top-level entries:**

```
.gitignore
.idea
README.md
config
dags
```

## 5. My contribution / role (evidence from git history — if available)

```text
747ba03 2025-07-29 update to xy_stacked_bar_chart
68a01e6 2025-07-28 Merge pull request #693 from BotNotOrg/feat/add_17track_register
f4ec770 2025-07-28 Merge branch 'dev' of github.com:BotNotOrg/yofi-airflow-codebase into feat/add_17track_register
c4335b7 2025-07-28 fix: update query condition to filter by is_ftid instead of justifications
c162413 2025-07-28 Merge pull request #691 from BotNotOrg/fix/limit-shopify-partitions
c56482d 2025-07-28 feat: add filter for created_at date in Shopify query
59e8d97 2025-07-25 Merge pull request #689 from BotNotOrg/feat/add_17track_register
d0cd90f 2025-07-25 refactor: remove unused ecommerce_unified_return from SPANNER_TABLES
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets

_No snippet candidates matched (handler.py / stack.ts / template.yaml etc.). Expand manually after opening the repo._

## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`yofi-airflow-codebase`** capabilities aligned with **data engineering** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yofi-airflow-codebase`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

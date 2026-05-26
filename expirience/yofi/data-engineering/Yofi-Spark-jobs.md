# Yofi-Spark-jobs

**Path:** `D:/botnot/Yofi-Spark-jobs`  
**Category:** data-engineering  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# Yofi-Spark-jobs
script for google pyspark jobs

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

### `README.md`

```
# Yofi-Spark-jobs
script for google pyspark jobs
```

### `readme.md`

```
# Yofi-Spark-jobs
script for google pyspark jobs
```

### `Readme.md`

```
# Yofi-Spark-jobs
script for google pyspark jobs
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
archive
src
```

## 5. My contribution / role (evidence from git history — if available)

```text
c90cc9d1 2025-07-17 Use json.dumps to correctly format string literals for SQL
6363c054 2025-07-04 Merge pull request #665 from BotNotOrg/refactor/remove-redundant-timestamp-casting
ed07c59d 2025-07-04 fix: remove redundant timestamp parsing
d5541c2a 2025-06-23 Merge pull request #664 from BotNotOrg/fix/airbyte-api-method
13bd4c70 2025-06-23 fix: also filter when data is empty
5eda8cb3 2025-06-23 Merge pull request #662 from BotNotOrg/fix/airbyte-api-method
1b3d5f03 2025-06-23 fix: include case where shop is not found
821327d4 2025-06-23 Merge pull request #661 from BotNotOrg/fix/airbyte-api-method
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets

_No snippet candidates matched (handler.py / stack.ts / template.yaml etc.). Expand manually after opening the repo._

## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`Yofi-Spark-jobs`** capabilities aligned with **data engineering** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `Yofi-Spark-jobs`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

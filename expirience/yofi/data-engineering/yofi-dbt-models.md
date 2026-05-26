# yofi-dbt-models

**Path:** `D:/botnot/yofi-dbt-models`  
**Category:** data-engineering  
**Primary language:** SQL  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# yofi-dbt-models

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** SQL
- **Top-level layout:** see listing below.

### `README.md`

```
# yofi-dbt-models
```

### `readme.md`

```
# yofi-dbt-models
```

### `Readme.md`

```
# yofi-dbt-models
```

### `pyproject.toml`

```
[project]
name = "yofi-dbt-models"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = ["dbt-bigquery>=1.9.2", "dbt-core>=1.9.6"]

[tool.sqlfmt]
exclude = ["target/**/*", "dbt_packages/**/*"]

[tool.sqlfluff.core]
dialect = "bigquery"
template = "jinja"
large_file_skip_byte_limit = 1000000
max_line_length = 88
exclude_rules = ["L034", "ST07"]

[tool.sqlfluff.templater]
unwrap_wrapped_queries = true

[tool.sqlfluff.templater.jinja]
apply_dbt_builtins = true

[dependency-groups]
dev = ["shandy-sqlfmt[jinjafmt]>=0.26.0", "sqlfluff>=3.4.0"]
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
dbt_lululemon
dbt_project
docs
pyproject.toml
schema.json
uv.lock
venv
```

## 5. My contribution / role (evidence from git history — if available)

```text
67424f63 2025-09-03 fix null in created at
33abc423 2025-09-03 fix bar chart
392916aa 2025-09-02 Merge pull request #867 from BotNotOrg/feat/brooklinen
a5cb1290 2025-09-02 refactor: use any_value for order_number and customer fields in happy_returns SQL models
1c2f5c30 2025-09-02 Merge pull request #865 from BotNotOrg/feat/brooklinen
8c378c90 2025-09-02 refactor: update merchant_name to merchant_id in SQL models for consistency
2a57729d 2025-09-02 Merge pull request #863 from BotNotOrg/feat/add-hr-confirmed-fraud
2a8d7634 2025-09-02 feat: add new known fraud confirmation codes to the dataset
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets

_No snippet candidates matched (handler.py / stack.ts / template.yaml etc.). Expand manually after opening the repo._

## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`yofi-dbt-models`** capabilities aligned with **data engineering** delivery.
- Applied **SQL** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yofi-dbt-models`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

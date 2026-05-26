# yofi-rules-monorepo

**Path:** `D:/botnot/yofi-rules-monorepo`  
**Category:** libs-docs  
**Primary language:** SQL  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# yofi_features

This repository is both a Python package and a dbt package for yofi-rules, working as a
single source of truth for flags and parameters.

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** SQL
- **Top-level layout:** see listing below.

### `README.md`

```
# yofi_features

This repository is both a Python package and a dbt package for yofi-rules, working as a
single source of truth for flags and parameters.

## Getting Started

We use [uv](https://github.com/astral-sh/uv) to manage the package and dependencies.
You can install it with `curl -LsSf https://astral.sh/uv/install.sh | sh`.
We also use [pre-commit](https://pre-commit.com/) to enforce standards and ensure parity
for the parameters between python and dbt.

Run the snippet below to set up your local environment with uv and pre-commit.

```bash
uv sync --all-extras
uv run pre-commit install --install-hooks
```

## Overview

The idea for this Monorepo is to consolidate all fraud models in a single location, and
unify parameter definition across real-time and batch models, although model
implementation is not unified (yet?).

The model pipeline is defined for each shop (or for other shopify shops as "general")
in `src/yofi_rules/parameters/shops`. Each file has the following format:

```yaml
shop_name:
  shop_url: shop_name.shopify.com # override when shop_name is different
  shopify_abuse_pipeline: # shopify only for now
    allowlisted_email_domains: # never flag these customers
      - mydomain.com
    rules:
      shopify_return_abusers_rule: # enables return abusers model
        min_return_rate: 0.5 # override default parameter value
      shopify_return_fraudsters_model: # enable return fraudster model. can be empty
```

In the example above, models not listed (like resellers and claim abusers) are not
enabled. Also, enabling a model implies enabling all flags within it, but parameters
can often be tuned to render the flag "disabled". Enabling each flag separately inside
each model is a planned feature, as well as a refactor standardizing parameter names,
and renaming `rules` > `models`.

After updating your parameters, make sure to run the cli to update the model parameters,
using `uv run yofi-rules`. This will update the `get_shop_parameters.sql` file with
the `shops/*.yaml` files updated so dbt can properly read them. When commiting changes,
a pre-commit hook should always check if the macro file is properly updated.

When updating any rule models, if the schema changes, make sure to update the macro in
`shopify_abuse_pipeline.sql`, as well as modifying it to include new rule models.

## dbt Package

### Installation

Reference this repository in your dbt `packages.yml` as below. In the yofi-dbt-models
[packages.yml](https://github.com/BotNotOrg/yofi-dbt-models/blob/main/dbt_project/packages.yml),
it's already added as a dependency and the revision is semi-automatically updated
using [Github Actions](.github/workflows/update_yofi_dbt_models.yml), which creates
a new PR pointing to the latest commit everytime the `dev` branch is updated. This PR
has to be manually merged.

```yaml
packages:
  - git: "git@github.com:BotNotOrg/yofi-rules-monorepo.git"
    subdirectory: "yofi_rules_dbt"
    revision: <optional git ref>
```

If using in local development, comment the lines above and uncomment the line below
(make sure its pointing to the right

…(truncated)…
```

### `readme.md`

```
# yofi_features

This repository is both a Python package and a dbt package for yofi-rules, working as a
single source of truth for flags and parameters.

## Getting Started

We use [uv](https://github.com/astral-sh/uv) to manage the package and dependencies.
You can install it with `curl -LsSf https://astral.sh/uv/install.sh | sh`.
We also use [pre-commit](https://pre-commit.com/) to enforce standards and ensure parity
for the parameters between python and dbt.

Run the snippet below to set up your local environment with uv and pre-commit.

```bash
uv sync --all-extras
uv run pre-commit install --install-hooks
```

## Overview

The idea for this Monorepo is to consolidate all fraud models in a single location, and
unify parameter definition across real-time and batch models, although model
implementation is not unified (yet?).

The model pipeline is defined for each shop (or for other shopify shops as "general")
in `src/yofi_rules/parameters/shops`. Each file has the following format:

```yaml
shop_name:
  shop_url: shop_name.shopify.com # override when shop_name is different
  shopify_abuse_pipeline: # shopify only for now
    allowlisted_email_domains: # never flag these customers
      - mydomain.com
    rules:
      shopify_return_abusers_rule: # enables return abusers model
        min_return_rate: 0.5 # override default parameter value
      shopify_return_fraudsters_model: # enable return fraudster model. can be empty
```

In the example above, models not listed (like resellers and claim abusers) are not
enabled. Also, enabling a model implies enabling all flags within it, but parameters
can often be tuned to render the flag "disabled". Enabling each flag separately inside
each model is a planned feature, as well as a refactor standardizing parameter names,
and renaming `rules` > `models`.

After updating your parameters, make sure to run the cli to update the model parameters,
using `uv run yofi-rules`. This will update the `get_shop_parameters.sql` file with
the `shops/*.yaml` files updated so dbt can properly read them. When commiting changes,
a pre-commit hook should always check if the macro file is properly updated.

When updating any rule models, if the schema changes, make sure to update the macro in
`shopify_abuse_pipeline.sql`, as well as modifying it to include new rule models.

## dbt Package

### Installation

Reference this repository in your dbt `packages.yml` as below. In the yofi-dbt-models
[packages.yml](https://github.com/BotNotOrg/yofi-dbt-models/blob/main/dbt_project/packages.yml),
it's already added as a dependency and the revision is semi-automatically updated
using [Github Actions](.github/workflows/update_yofi_dbt_models.yml), which creates
a new PR pointing to the latest commit everytime the `dev` branch is updated. This PR
has to be manually merged.

```yaml
packages:
  - git: "git@github.com:BotNotOrg/yofi-rules-monorepo.git"
    subdirectory: "yofi_rules_dbt"
    revision: <optional git ref>
```

If using in local development, comment the lines above and uncomment the line below
(make sure its pointing to the right

…(truncated)…
```

### `Readme.md`

```
# yofi_features

This repository is both a Python package and a dbt package for yofi-rules, working as a
single source of truth for flags and parameters.

## Getting Started

We use [uv](https://github.com/astral-sh/uv) to manage the package and dependencies.
You can install it with `curl -LsSf https://astral.sh/uv/install.sh | sh`.
We also use [pre-commit](https://pre-commit.com/) to enforce standards and ensure parity
for the parameters between python and dbt.

Run the snippet below to set up your local environment with uv and pre-commit.

```bash
uv sync --all-extras
uv run pre-commit install --install-hooks
```

## Overview

The idea for this Monorepo is to consolidate all fraud models in a single location, and
unify parameter definition across real-time and batch models, although model
implementation is not unified (yet?).

The model pipeline is defined for each shop (or for other shopify shops as "general")
in `src/yofi_rules/parameters/shops`. Each file has the following format:

```yaml
shop_name:
  shop_url: shop_name.shopify.com # override when shop_name is different
  shopify_abuse_pipeline: # shopify only for now
    allowlisted_email_domains: # never flag these customers
      - mydomain.com
    rules:
      shopify_return_abusers_rule: # enables return abusers model
        min_return_rate: 0.5 # override default parameter value
      shopify_return_fraudsters_model: # enable return fraudster model. can be empty
```

In the example above, models not listed (like resellers and claim abusers) are not
enabled. Also, enabling a model implies enabling all flags within it, but parameters
can often be tuned to render the flag "disabled". Enabling each flag separately inside
each model is a planned feature, as well as a refactor standardizing parameter names,
and renaming `rules` > `models`.

After updating your parameters, make sure to run the cli to update the model parameters,
using `uv run yofi-rules`. This will update the `get_shop_parameters.sql` file with
the `shops/*.yaml` files updated so dbt can properly read them. When commiting changes,
a pre-commit hook should always check if the macro file is properly updated.

When updating any rule models, if the schema changes, make sure to update the macro in
`shopify_abuse_pipeline.sql`, as well as modifying it to include new rule models.

## dbt Package

### Installation

Reference this repository in your dbt `packages.yml` as below. In the yofi-dbt-models
[packages.yml](https://github.com/BotNotOrg/yofi-dbt-models/blob/main/dbt_project/packages.yml),
it's already added as a dependency and the revision is semi-automatically updated
using [Github Actions](.github/workflows/update_yofi_dbt_models.yml), which creates
a new PR pointing to the latest commit everytime the `dev` branch is updated. This PR
has to be manually merged.

```yaml
packages:
  - git: "git@github.com:BotNotOrg/yofi-rules-monorepo.git"
    subdirectory: "yofi_rules_dbt"
    revision: <optional git ref>
```

If using in local development, comment the lines above and uncomment the line below
(make sure its pointing to the right

…(truncated)…
```

### `pyproject.toml`

```
[project]
name = "yofi_rules"
dynamic = ["version", "description"]
readme = "README.md"
authors = [{ name = "Noel", email = "noel@yofi.ai" }]
classifiers = ["Private :: Do Not Upload"]
requires-python = ">=3.10"
dependencies = ["pydantic>=2.11.5", "ruamel-yaml>=0.18.14"]

[dependency-groups]
dev = [
    "pre-commit>=4.2.0",
    "pyright>=1.1.401",
    "pytest>=8.4.0",
    "ruff>=0.11.13",
    "polars>=1.30.0",
    # Add dbt for easier monorepo development
    "dbt-core>=1.9.8",
    "dbt-bigquery>=1.9.2",
    "shandy-sqlfmt[jinjafmt]>=0.26.0",
    "black>=25.1.0",
    "jupyter>=1.1.1",
    "google-cloud-bigquery>=3.34.0",
    "marimo>=0.13.15",
    "watchdog>=6.0.0",
    "google-cloud-bigquery-storage>=2.32.0",
]

[project.scripts]
yofi-rules = "yofi_rules.cli:main"

[tool.ruff.lint]
select = [
    "A",
    "B",
    "E",
    "F",
    "I",
    "W",
    "ERA",
    "FURB",
    "LOG",
    "PD",
    "PTH",
    "RUF",
    "UP",
]
ignore = ["D1"] # do not complain about undocumented stuff for now

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = ["-v", "--tb=short", "--strict-markers", "--disable-warnings"]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "integration: marks tests as integration tests",
    "unit: marks tests as unit tests"
]

[build-system]
requires = ["flit_core >=3.4,<4"]
build-backend = "flit_core.buildapi"
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
.pre-commit-config.yaml
README.md
dev
pyproject.toml
src
uv.lock
yofi_rules_dbt
```

## 5. My contribution / role (evidence from git history — if available)

```text
e902be6 2025-09-24 Merge pull request #109 from BotNotOrg/dev
8516022 2025-09-24 Merge pull request #108 from BotNotOrg/fix/min_fraud_tags
8124a94 2025-09-24 fix: disable fraud tags/notes matching in real time since it can't look at multiple orders
f325a38 2025-09-22 Merge pull request #105 from BotNotOrg/dev
5597db1 2025-09-22 Merge pull request #106 from BotNotOrg/feat/change_params
64c191d 2025-09-22 fix: update return parameters in rhodeskin.yaml and associated SQL macro
0adba9a 2025-09-22 Merge pull request #104 from BotNotOrg/feat/change_params
d7728cf 2025-09-22 feat: add tradewindservices.com to allowlisted domains and update min_return_note_rate in rhodeskin.yaml
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets

_No snippet candidates matched (handler.py / stack.ts / template.yaml etc.). Expand manually after opening the repo._

## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`yofi-rules-monorepo`** capabilities aligned with **libs docs** delivery.
- Applied **SQL** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yofi-rules-monorepo`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

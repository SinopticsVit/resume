# yofi-common-libs-py

**Path:** `D:/botnot/yofi-common-libs-py`  
**Category:** libs-docs  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# Intro

Common python libs for all projects

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

### `README.md`

```
# Intro

Common python libs for all projects

## Install using version tag (For production deployment)

Just put this line in your `requirements.txt` file
```
git+https://pipdepencymanagement:ghp_REDACTED@github.com/BotNotOrg/yofi-common-libs-py.git@v0.1.0

...
......other packages like: arrow==2.3.5
```

## Install using main branch

pip install git+https://pipdepencymanagement:ghp_REDACTED@github.com/BotNotOrg/yofi-common-libs-py.git


## (Only for local dev and testing) Install using dev branch
> use `--force-reinstall` so that it will overwrite your local without checking version

pip install --force-reinstall git+https://pipdepencymanagement:ghp_REDACTED@github.com/BotNotOrg/yofi-common-libs-py.git@dev

## How to update this lib and deploy new version
> This repo use github action for automatic version deploy, and manually pushing tags is prevented. 

1. Checkout a feature branch from `main` branch (which is the only branch for releasing version tags)
2. Develop your feature in feature branch, add some unittest for the new changes, and make sure all the unittests passed
3. Submit a pull request for team review
4. When PR merged, github action will automatically deploy a new version tag here (https://github.com/BotNotOrg/yofi-common-libs-py/tags)
5. Use the new deployed version tag for your client usage.

## How to develop with local mode
> -e means to install your local paackge with edit mode, so your local changes will always take effect
> use `--config-settings editable_mode=compat` is for pycharm to recognize in this mode

pip install -e <path_to_my_module> --config-settings editable_mode=compat


## VS Code setup
1. Install Python extenstion
2. Install packages
```
pip install -e . --config-settings editable_mode=compat
pip install pytest setuptools python-dotenv
```
```

### `readme.md`

```
# Intro

Common python libs for all projects

## Install using version tag (For production deployment)

Just put this line in your `requirements.txt` file
```
git+https://pipdepencymanagement:ghp_REDACTED@github.com/BotNotOrg/yofi-common-libs-py.git@v0.1.0

...
......other packages like: arrow==2.3.5
```

## Install using main branch

pip install git+https://pipdepencymanagement:ghp_REDACTED@github.com/BotNotOrg/yofi-common-libs-py.git


## (Only for local dev and testing) Install using dev branch
> use `--force-reinstall` so that it will overwrite your local without checking version

pip install --force-reinstall git+https://pipdepencymanagement:ghp_REDACTED@github.com/BotNotOrg/yofi-common-libs-py.git@dev

## How to update this lib and deploy new version
> This repo use github action for automatic version deploy, and manually pushing tags is prevented. 

1. Checkout a feature branch from `main` branch (which is the only branch for releasing version tags)
2. Develop your feature in feature branch, add some unittest for the new changes, and make sure all the unittests passed
3. Submit a pull request for team review
4. When PR merged, github action will automatically deploy a new version tag here (https://github.com/BotNotOrg/yofi-common-libs-py/tags)
5. Use the new deployed version tag for your client usage.

## How to develop with local mode
> -e means to install your local paackge with edit mode, so your local changes will always take effect
> use `--config-settings editable_mode=compat` is for pycharm to recognize in this mode

pip install -e <path_to_my_module> --config-settings editable_mode=compat


## VS Code setup
1. Install Python extenstion
2. Install packages
```
pip install -e . --config-settings editable_mode=compat
pip install pytest setuptools python-dotenv
```
```

### `Readme.md`

```
# Intro

Common python libs for all projects

## Install using version tag (For production deployment)

Just put this line in your `requirements.txt` file
```
git+https://pipdepencymanagement:ghp_REDACTED@github.com/BotNotOrg/yofi-common-libs-py.git@v0.1.0

...
......other packages like: arrow==2.3.5
```

## Install using main branch

pip install git+https://pipdepencymanagement:ghp_REDACTED@github.com/BotNotOrg/yofi-common-libs-py.git


## (Only for local dev and testing) Install using dev branch
> use `--force-reinstall` so that it will overwrite your local without checking version

pip install --force-reinstall git+https://pipdepencymanagement:ghp_REDACTED@github.com/BotNotOrg/yofi-common-libs-py.git@dev

## How to update this lib and deploy new version
> This repo use github action for automatic version deploy, and manually pushing tags is prevented. 

1. Checkout a feature branch from `main` branch (which is the only branch for releasing version tags)
2. Develop your feature in feature branch, add some unittest for the new changes, and make sure all the unittests passed
3. Submit a pull request for team review
4. When PR merged, github action will automatically deploy a new version tag here (https://github.com/BotNotOrg/yofi-common-libs-py/tags)
5. Use the new deployed version tag for your client usage.

## How to develop with local mode
> -e means to install your local paackge with edit mode, so your local changes will always take effect
> use `--config-settings editable_mode=compat` is for pycharm to recognize in this mode

pip install -e <path_to_my_module> --config-settings editable_mode=compat


## VS Code setup
1. Install Python extenstion
2. Install packages
```
pip install -e . --config-settings editable_mode=compat
pip install pytest setuptools python-dotenv
```
```

### `pyproject.toml`

```
[build-system]
requires = ["setuptools", "wheel", "setuptools-git-versioning"]
build-backend = "setuptools.build_meta"
```

### `requirements.txt`

```
wheel
pymongo[srv]
pymongo[aws]
boto3
arrow
google-cloud-logging

google-cloud-spanner==3.54.0
sqlalchemy==2.0.40
sqlalchemy-spanner
# alembic  -- for local migration only
# python-dotenv -- for local testing

aws-secretsmanager-caching
slack_sdk
cachetools
google-cloud-secret-manager
google-genai
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
.vscode
README.md
pyproject.toml
requirements.txt
setup.py
setup_test.py
tools
yofi_common_libs
```

## 5. My contribution / role (evidence from git history — if available)

```text
91ddec9 2025-05-20 Merge remote-tracking branch 'origin/main'
34dc43c 2025-05-20 Merge pull request #66 from BotNotOrg/feature/YOFI-484-check-permission
3533057 2025-05-20 Merge branch 'main' of github.com:BotNotOrg/yofi-common-libs-py into feature/YOFI-484-check-permission
46d213c 2025-05-20 refactor: update get_authorized_resources method to return only authorized apps and add get_module_permissions method; update tests accordingly
2ef357e 2025-05-20 feat: add subscription tier and quota management fields to Organization model and SQL schema
780713b 2025-05-20 Merge pull request #70 from BotNotOrg/feature/add_cloudwatch
6d33225 2025-05-20 Merge pull request #69 from BotNotOrg/hotfix/orm-commit
1446d64 2025-05-20 feat: add cloudwatch metrics
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets

_No snippet candidates matched (handler.py / stack.ts / template.yaml etc.). Expand manually after opening the repo._

## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`yofi-common-libs-py`** capabilities aligned with **libs docs** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yofi-common-libs-py`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

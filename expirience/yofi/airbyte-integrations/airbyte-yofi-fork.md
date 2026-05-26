# airbyte-yofi-fork

**Path:** `D:/botnot/airbyte-yofi-fork`  
**Category:** airbyte-integrations  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

<p align="center">
  <a href="https://airbyte.com"><img src="https://assets.website-files.com/605e01bc25f7e19a82e74788/624d9c4a375a55100be6b257_Airbyte_logo_color_dark.svg" alt="Airbyte"></a>
</p>
<p align="center">
    <em>Data integration platform for ELT pipelines from APIs, databases & files to databases, warehouses & lakes</em>
</p>
<p align="center">
<a href="https://github.com/airbytehq/airbyte/stargazers/" target="_blank">
    <img src="https://img.shields.io/github/stars/airbytehq/airbyte?style=social&label=Star&maxAge=2592000" alt="Test">
</a>
<a href="https://github.com/airbytehq/airbyte/releases" target="_blank">
    <img src="https://img.shields.io/github/v/release/airbytehq/airbyte?color=white" alt="Release">
</a>
<a href="https://airbytehq.sl

…(truncated)…

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

### `README.md`

```
<p align="center">
  <a href="https://airbyte.com"><img src="https://assets.website-files.com/605e01bc25f7e19a82e74788/624d9c4a375a55100be6b257_Airbyte_logo_color_dark.svg" alt="Airbyte"></a>
</p>
<p align="center">
    <em>Data integration platform for ELT pipelines from APIs, databases & files to databases, warehouses & lakes</em>
</p>
<p align="center">
<a href="https://github.com/airbytehq/airbyte/stargazers/" target="_blank">
    <img src="https://img.shields.io/github/stars/airbytehq/airbyte?style=social&label=Star&maxAge=2592000" alt="Test">
</a>
<a href="https://github.com/airbytehq/airbyte/releases" target="_blank">
    <img src="https://img.shields.io/github/v/release/airbytehq/airbyte?color=white" alt="Release">
</a>
<a href="https://airbytehq.slack.com/" target="_blank">
    <img src="https://img.shields.io/badge/slack-join-white.svg?logo=slack" alt="Slack">
</a>
<a href="https://www.youtube.com/c/AirbyteHQ/?sub_confirmation=1" target="_blank">
    <img alt="YouTube Channel Views" src="https://img.shields.io/youtube/channel/views/UCQ_JWEFzs1_INqdhIO3kmrw?style=social">
</a>
<a href="https://github.com/airbytehq/airbyte/actions/workflows/gradle.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/airbytehq/airbyte/gradle.yml?branch=master" alt="Build">
</a>
<a href="https://github.com/airbytehq/airbyte/tree/master/docs/project-overview/licenses" target="_blank">
    <img src="https://img.shields.io/static/v1?label=license&message=MIT&color=white" alt="License">
</a>
<a href="https://github.com/airbytehq/airbyte/tree/master/docs/project-overview/licenses" target="_blank">
    <img src="https://img.shields.io/static/v1?label=license&message=ELv2&color=white" alt="License">
</a>
</p>

We believe that only an **open-source solution to data movement** can cover the long tail of data sources while empowering data engineers to customize existing connectors. Our ultimate vision is to help you move data from any source to any destination. Airbyte already provides the largest [catalog](https://docs.airbyte.com/integrations/) of 300+ connectors for APIs, databases, data warehouses, and data lakes.

![Airbyte OSS Connections UI](https://github.com/airbytehq/airbyte/assets/10663571/870d0479-2765-4ecb-abd5-a5bb877dae37)
_Screenshot taken from [Airbyte Cloud](https://cloud.airbyte.com/signup)_.

### Getting Started
* [Deploy Airbyte Open Source](https://docs.airbyte.com/quickstart/deploy-airbyte) or set up [Airbyte Cloud](https://docs.airbyte.com/cloud/getting-started-with-airbyte-cloud) to start centralizing your data.
* Create connectors in minutes with our [no-code Connector Builder](https://docs.airbyte.com/connector-development/connector-builder-ui/overview) or [low-code CDK](https://docs.airbyte.com/connector-development/config-based/low-code-cdk-overview).
* Explore popular use cases in our [tutorials](https://airbyte.com/tutorials).
* Orchestrate Airbyte syncs with [Airflow](https://docs.airbyte.com/operator-guides/using-the-airflow-airbyte-operator), [Prefect](https://docs.airbyte.com/operator-guides/using-prefect-task), [Dagster](https://docs

…(truncated)…
```

### `readme.md`

```
<p align="center">
  <a href="https://airbyte.com"><img src="https://assets.website-files.com/605e01bc25f7e19a82e74788/624d9c4a375a55100be6b257_Airbyte_logo_color_dark.svg" alt="Airbyte"></a>
</p>
<p align="center">
    <em>Data integration platform for ELT pipelines from APIs, databases & files to databases, warehouses & lakes</em>
</p>
<p align="center">
<a href="https://github.com/airbytehq/airbyte/stargazers/" target="_blank">
    <img src="https://img.shields.io/github/stars/airbytehq/airbyte?style=social&label=Star&maxAge=2592000" alt="Test">
</a>
<a href="https://github.com/airbytehq/airbyte/releases" target="_blank">
    <img src="https://img.shields.io/github/v/release/airbytehq/airbyte?color=white" alt="Release">
</a>
<a href="https://airbytehq.slack.com/" target="_blank">
    <img src="https://img.shields.io/badge/slack-join-white.svg?logo=slack" alt="Slack">
</a>
<a href="https://www.youtube.com/c/AirbyteHQ/?sub_confirmation=1" target="_blank">
    <img alt="YouTube Channel Views" src="https://img.shields.io/youtube/channel/views/UCQ_JWEFzs1_INqdhIO3kmrw?style=social">
</a>
<a href="https://github.com/airbytehq/airbyte/actions/workflows/gradle.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/airbytehq/airbyte/gradle.yml?branch=master" alt="Build">
</a>
<a href="https://github.com/airbytehq/airbyte/tree/master/docs/project-overview/licenses" target="_blank">
    <img src="https://img.shields.io/static/v1?label=license&message=MIT&color=white" alt="License">
</a>
<a href="https://github.com/airbytehq/airbyte/tree/master/docs/project-overview/licenses" target="_blank">
    <img src="https://img.shields.io/static/v1?label=license&message=ELv2&color=white" alt="License">
</a>
</p>

We believe that only an **open-source solution to data movement** can cover the long tail of data sources while empowering data engineers to customize existing connectors. Our ultimate vision is to help you move data from any source to any destination. Airbyte already provides the largest [catalog](https://docs.airbyte.com/integrations/) of 300+ connectors for APIs, databases, data warehouses, and data lakes.

![Airbyte OSS Connections UI](https://github.com/airbytehq/airbyte/assets/10663571/870d0479-2765-4ecb-abd5-a5bb877dae37)
_Screenshot taken from [Airbyte Cloud](https://cloud.airbyte.com/signup)_.

### Getting Started
* [Deploy Airbyte Open Source](https://docs.airbyte.com/quickstart/deploy-airbyte) or set up [Airbyte Cloud](https://docs.airbyte.com/cloud/getting-started-with-airbyte-cloud) to start centralizing your data.
* Create connectors in minutes with our [no-code Connector Builder](https://docs.airbyte.com/connector-development/connector-builder-ui/overview) or [low-code CDK](https://docs.airbyte.com/connector-development/config-based/low-code-cdk-overview).
* Explore popular use cases in our [tutorials](https://airbyte.com/tutorials).
* Orchestrate Airbyte syncs with [Airflow](https://docs.airbyte.com/operator-guides/using-the-airflow-airbyte-operator), [Prefect](https://docs.airbyte.com/operator-guides/using-prefect-task), [Dagster](https://docs

…(truncated)…
```

### `Readme.md`

```
<p align="center">
  <a href="https://airbyte.com"><img src="https://assets.website-files.com/605e01bc25f7e19a82e74788/624d9c4a375a55100be6b257_Airbyte_logo_color_dark.svg" alt="Airbyte"></a>
</p>
<p align="center">
    <em>Data integration platform for ELT pipelines from APIs, databases & files to databases, warehouses & lakes</em>
</p>
<p align="center">
<a href="https://github.com/airbytehq/airbyte/stargazers/" target="_blank">
    <img src="https://img.shields.io/github/stars/airbytehq/airbyte?style=social&label=Star&maxAge=2592000" alt="Test">
</a>
<a href="https://github.com/airbytehq/airbyte/releases" target="_blank">
    <img src="https://img.shields.io/github/v/release/airbytehq/airbyte?color=white" alt="Release">
</a>
<a href="https://airbytehq.slack.com/" target="_blank">
    <img src="https://img.shields.io/badge/slack-join-white.svg?logo=slack" alt="Slack">
</a>
<a href="https://www.youtube.com/c/AirbyteHQ/?sub_confirmation=1" target="_blank">
    <img alt="YouTube Channel Views" src="https://img.shields.io/youtube/channel/views/UCQ_JWEFzs1_INqdhIO3kmrw?style=social">
</a>
<a href="https://github.com/airbytehq/airbyte/actions/workflows/gradle.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/airbytehq/airbyte/gradle.yml?branch=master" alt="Build">
</a>
<a href="https://github.com/airbytehq/airbyte/tree/master/docs/project-overview/licenses" target="_blank">
    <img src="https://img.shields.io/static/v1?label=license&message=MIT&color=white" alt="License">
</a>
<a href="https://github.com/airbytehq/airbyte/tree/master/docs/project-overview/licenses" target="_blank">
    <img src="https://img.shields.io/static/v1?label=license&message=ELv2&color=white" alt="License">
</a>
</p>

We believe that only an **open-source solution to data movement** can cover the long tail of data sources while empowering data engineers to customize existing connectors. Our ultimate vision is to help you move data from any source to any destination. Airbyte already provides the largest [catalog](https://docs.airbyte.com/integrations/) of 300+ connectors for APIs, databases, data warehouses, and data lakes.

![Airbyte OSS Connections UI](https://github.com/airbytehq/airbyte/assets/10663571/870d0479-2765-4ecb-abd5-a5bb877dae37)
_Screenshot taken from [Airbyte Cloud](https://cloud.airbyte.com/signup)_.

### Getting Started
* [Deploy Airbyte Open Source](https://docs.airbyte.com/quickstart/deploy-airbyte) or set up [Airbyte Cloud](https://docs.airbyte.com/cloud/getting-started-with-airbyte-cloud) to start centralizing your data.
* Create connectors in minutes with our [no-code Connector Builder](https://docs.airbyte.com/connector-development/connector-builder-ui/overview) or [low-code CDK](https://docs.airbyte.com/connector-development/config-based/low-code-cdk-overview).
* Explore popular use cases in our [tutorials](https://airbyte.com/tutorials).
* Orchestrate Airbyte syncs with [Airflow](https://docs.airbyte.com/operator-guides/using-the-airflow-airbyte-operator), [Prefect](https://docs.airbyte.com/operator-guides/using-prefect-task), [Dagster](https://docs

…(truncated)…
```

### `pyproject.toml`

```
[tool.poetry]
name = "airbyte"
version = "0.1.0"
description = "Airbyte open source connector code"
authors = ["Airbyte <contact@airbyte.io>"]

[tool.poetry.dependencies]
python = "~3.10"

[tool.poetry.group.dev.dependencies]
isort = "5.6.4"
black = "~22.3.0"

[tool.black]
line-length = 140
target-version = ["py37"]
extend-exclude = "(build|integration_tests|unit_tests|generated)"

[tool.coverage.report]
fail_under = 0
skip_empty = true
sort = "-cover"
omit = [
    ".venv/*",
    "main.py",
    "setup.py",
    "unit_tests/*",
    "integration_tests/*",
    "**/generated/*",
]

[tool.flake8]
extend-exclude = [
    "*/lib/*/site-packages",
    ".venv",
    "build",
    "models",
    ".eggs",
    "airbyte-cdk/python/airbyte_cdk/models/__init__.py",
    "airbyte-cdk/python/airbyte_cdk/sources/declarative/models/__init__.py",
    ".tox",
    "airbyte_api_client",
    "**/generated/*",
]
max-complexity = 20
max-line-length = 140

extend-ignore = [
  "E203",  # whitespace before ':' (conflicts with Black)
  "E231",  # Bad trailing comma (conflicts with Black)
  "E501",  # line too long (conflicts with Black)
  "W503",  # line break before binary operator (conflicts with Black)
]

[tool.isort]
profile = "black"
color_output = false
# skip_gitignore = true
line_length = 140
multi_line_output = 3
include_trailing_comma = true
force_grid_wrap = 0
use_parentheses = true
skip_glob = ["**/connector_builder/generated/**"]


[tool.mypy]
platform = "linux"
exclude = "(build|integration_tests|unit_tests|generated)"

# Optionals
ignore_missing_imports = true

# Strictness
allow_untyped_globals = false
allow_redefinition = false
implicit_reexport = false
strict_equality = true

# Warnings
warn_unused_ignores = true
warn_no_return = true
warn_return_any = true
warn_redundant_casts = true
warn_unreachable = true

# Error output
show_column_numbers = true
show_error_context = true
show_error_codes = true
show_traceback = true
pretty = true
color_output = true
error_summary = true

[tool.pytest.ini_options]
minversion = "6.2.5"
addopts ="-r a --capture=no -vv --color=yes"
```

### `Makefile`

```
##@ Makefile

##@ Define the default airbyte-ci version
AIRBYTE_CI_VERSION ?= latest

## Detect the operating system
OS := $(shell uname)

tools.airbyte-ci.install: tools.airbyte-ci.clean tools.airbyte-ci-binary.install tools.airbyte-ci.check

tools.airbyte-ci-binary.install: ## Install airbyte-ci binary
	@python airbyte-ci/connectors/pipelines/pipelines/external_scripts/airbyte_ci_install.py ${AIRBYTE_CI_VERSION}

tools.airbyte-ci-dev.install: ## Install the local development version of airbyte-ci
	@python airbyte-ci/connectors/pipelines/pipelines/external_scripts/airbyte_ci_dev_install.py

tools.airbyte-ci.check: ## Check if airbyte-ci is installed correctly
	@./airbyte-ci/connectors/pipelines/pipelines/external_scripts/airbyte_ci_check.sh

tools.airbyte-ci.clean: ## Clean airbyte-ci installations
	@./airbyte-ci/connectors/pipelines/pipelines/external_scripts/airbyte_ci_clean.sh

tools.git-hooks.clean: ## Clean git hooks
	@echo "Unset core.hooksPath"
	@git config --unset core.hooksPath || true
	@echo "Removing pre-commit hooks..."
	@pre-commit uninstall
	@echo "Removing pre-push hooks..."
	@rm -rf .git/hooks
	@echo "Git hooks removed."

tools.pre-commit.install.Linux:
	@echo "Installing pre-commit with pip..."
	@pip install --user pre-commit
	@echo "Pre-commit installation complete."

tools.pre-commit.install.Darwin:
	@echo "Installing pre-commit with brew..."
	@brew install pre-commit
	@echo "Pre-commit installation complete"

tools.pre-commit.setup: tools.airbyte-ci.install tools.pre-commit.install.$(OS) tools.git-hooks.clean ## Setup pre-commit hooks
	@echo "Installing pre-commit hooks..."
	@pre-commit install --hook-type pre-push
	@echo "Pre-push hooks installed."

tools.install: tools.airbyte-ci.install tools.pre-commit.setup

.PHONY: tools.install tools.pre-commit.setup tools.airbyte-ci.install tools.airbyte-ci-dev.install tools.airbyte-ci.check tools.airbyte-ci.clean
```


## 3. Architecture

_High-level: see README and `stacks/` / `src/` layout for service-specific flow._

- **Inbound:** HTTP (API Gateway / ALB), scheduled triggers, queues (SQS/SNS), EventBridge rules, or batch — infer from `stacks/`, `template.yaml`, `sst.config.ts`, or `src/` handlers.
- **Outbound:** databases and external HTTP APIs per layers and `package.json` / Python imports in handlers.
- **IaC pattern:** SST/CDK, SAM/CloudFormation, Pulumi, Helm, Terraform, or raw scripts — see manifests section.

## 4. Key files (auto-discovered)

- **Top-level entries:**

```
.bumpversion.cfg
.devcontainer
.dockerignore
.editorconfig
.github
.gitignore
.pre-commit-config.yaml
.prettierignore
.python-version
.readthedocs.yaml
.root
CODE_OF_CONDUCT.md
CONTRIBUTING.md
CONTRIBUTORS.md
LICENSE
LICENSE_SHORT
Makefile
README.md
THANK-YOU.md
airbyte-base-java-image
airbyte-cdk
airbyte-ci
airbyte-integrations
build.gradle
buildSrc
codecov.yml
connectors.md
deps.toml
docs
docusaurus
gradle
gradle.properties
gradlew
gradlew.bat
octavia-cli
poetry.lock
pyproject.toml
pytest.ini
resources
run-ab-platform.sh
… +4 more
```

## 5. My contribution / role (evidence from git history — if available)

```text
6f824717da 2023-12-27 Bump Airbyte version from 0.50.39 to 0.50.40
bf9218d5c7 2023-12-26 Document State Message Principles (#33787)
4d84cc707b 2023-12-26 Update Airbyte Protocol documentation. (#33786)
bfe9d8b466 2023-12-22 source-microsoft-onedrive: remove from cloud registry (#33758)
5c77501b0a 2023-12-22 рџ“љ Add telemetry docs (#33757)
333320edeb 2023-12-21 Make memory-manager log message less scary (#33723)
7bcac9c8d0 2023-12-21 Revert "Add doc about the large records (#32907)" (#33734)
3470ddddf1 2023-12-21 рџ¤– Bump patch version of Python CDK
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`airbyte-cdk/python/airbyte_cdk/connector_builder/main.py`**

```python
#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys
from typing import Any, List, Mapping, Optional, Tuple

from airbyte_cdk.connector import BaseConnector
from airbyte_cdk.connector_builder.connector_builder_handler import TestReadLimits, create_source, get_limits, read_stream, resolve_manifest
from airbyte_cdk.entrypoint import AirbyteEntrypoint
from airbyte_cdk.models import AirbyteMessage, ConfiguredAirbyteCatalog
from airbyte_cdk.sources.declarative.manifest_declarative_source import ManifestDeclarativeSource
from airbyte_cdk.utils.traced_exception import AirbyteTracedException


def get_config_and_catalog_from_args(args: List[str]) -> Tuple[str, Mapping[str, Any], Optional[ConfiguredAirbyteCatalog]]:
    # TODO: Add functionality for the `debug` logger.
    #  Currently, no one `debug` level log will be displayed during `read` a stream for a connector created through `connector-builder`.
    parsed_args = AirbyteEntrypoint.parse_args(args)
    config_path, catalog_path = parsed_args.config, parsed_args.catalog
    if parsed_args.command != "read":
        raise ValueError("Only read commands are allowed for Connector Builder requests.")

    config = BaseConnector.read_config(config_path)

    if "__command" not in config:
        raise ValueError(
            f"Invalid config: `__command` should be provided at the root of the config but config only has keys {list(config.keys())}"
        )

    command = config["__command"]
    if command == "test_read":
        catalog = ConfiguredAirbyteCatalog.parse_obj(BaseConnector.read_config(catalog_path))
    else:
        catalog = None

    if "__injected_declarative_manifest" not in config:
        raise ValueError(
            f"Invalid config: `__injected_declarative_manifest` should be provided at the root of the config but config only has keys {list(config.keys())}"
        )

    return command, config, catalog


def handle_connector_builder_request(
    source: ManifestDeclarativeSource,
    command: str,
    config: Mapping[str, Any],
    catalog: Optional[ConfiguredAirbyteCatalog],
    limits: TestReadLimits,
) 

…(truncated)…
```

**`airbyte-cdk/python/source_declarative_manifest/main.py`**

```python
#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys
from typing import List

from airbyte_cdk.connector import BaseConnector
from airbyte_cdk.entrypoint import AirbyteEntrypoint, launch
from airbyte_cdk.sources.declarative.manifest_declarative_source import ManifestDeclarativeSource


def create_manifest(args: List[str]):
    parsed_args = AirbyteEntrypoint.parse_args(args)
    if parsed_args.command == "spec":
        raise ValueError("spec command is not supported for injected declarative manifest")

    config = BaseConnector.read_config(parsed_args.config)
    if "__injected_declarative_manifest" not in config:
        raise ValueError(
            f"Invalid config: `__injected_declarative_manifest` should be provided at the root of the config but config only has keys {list(config.keys())}"
        )
    return ManifestDeclarativeSource(config.get("__injected_declarative_manifest"))


if __name__ == "__main__":
    source = create_manifest(sys.argv[1:])
    launch(source, sys.argv[1:])
```

**`airbyte-ci/connectors/ci_credentials/ci_credentials/main.py`**

```python
#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#

import json
import sys
from json.decoder import JSONDecodeError

import click
from common_utils import Logger

from . import SecretsManager

logger = Logger()

ENV_GCP_GSM_CREDENTIALS = "GCP_GSM_CREDENTIALS"


# credentials of GSM and GitHub secrets should be shared via shell environment
@click.group()
@click.argument("connector_name")
@click.option("--gcp-gsm-credentials", envvar="GCP_GSM_CREDENTIALS")
@click.pass_context
def ci_credentials(ctx, connector_name: str, gcp_gsm_credentials):
    ctx.ensure_object(dict)
    ctx.obj["connector_name"] = connector_name
    # parse unique connector name, because it can have the common prefix "connectors/<unique connector name>"
    connector_name = connector_name.split("/")[-1]
    if connector_name == "all":
        # if needed to load all secrets
        connector_name = None

    # parse GCP_GSM_CREDENTIALS
    try:
        gsm_credentials = json.loads(gcp_gsm_credentials) if gcp_gsm_credentials else {}
    except JSONDecodeError as e:
        return logger.error(f"incorrect GCP_GSM_CREDENTIALS value, error: {e}")

    if not gsm_credentials:
        return logger.error("GCP_GSM_CREDENTIALS shouldn't be empty!")

    secret_manager = SecretsManager(
        connector_name=connector_name,
        gsm_credentials=gsm_credentials,
    )
    ctx.obj["secret_manager"] = secret_manager
    ctx.obj["connector_secrets"] = secret_manager.read_from_gsm()


@ci_credentials.command(help="Download GSM secrets locally to the connector's secrets directory.")
@click.pass_context
def write_to_storage(ctx):
    written_files = ctx.obj["secret_manager"].write_to_storage(ctx.obj["connector_secrets"])
    written_files_count = len(written_files)
    click.echo(f"{written_files_count} secret files were written: {','.join([str(path) for path in written_files])}")


@ci_credentials.command(help="Update GSM secrets according to the content of the secrets/updated_configurations directory.")
@click.pass_context
def update_secrets(ctx):
    new_remote_secrets = ctx.obj["secret_manager"].update_secrets(ctx

…(truncated)…
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`airbyte-yofi-fork`** capabilities aligned with **airbyte integrations** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `airbyte-yofi-fork`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

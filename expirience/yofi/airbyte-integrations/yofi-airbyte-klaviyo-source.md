# yofi-airbyte-klaviyo-source

**Path:** `D:/botnot/yofi-airbyte-klaviyo-source`  
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
<a href="https://airbytehq.slack.com/" tar

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

We believe that only an **open-source** solution to data movement can cover the **long tail of data sources** while empowering data engineers to **customize existing connectors**. Our ultimate vision is to help you move data from any source to any destination. Airbyte already provides [300+ connectors](https://docs.airbyte.com/integrations/) for popular APIs, databases, data warehouses, and data lakes.

You can implement Airbyte connectors in any language and take the form of a Docker image that follows the [Airbyte specification](https://docs.airbyte.com/understanding-airbyte/airbyte-protocol/). You can create new connectors very fast with:

- The [low-code Connector Development Kit](https://docs.airbyte.com/connector-development/config-based/low-code-cdk-overview) (CDK) for API connectors ([demo](https://www.youtube.com/watch?v=i7VSL2bDvmw))
- The [Python CDK](https://docs.airbyte.com/connector-development/cdk-python/) ([tutorial](https://docs.airbyte.com/connector-development/tutorials/cdk-speedrun))

Airbyte has a built-in scheduler and uses [Temporal](https://airbyte.com/blog/scale-workflow-orchestration-with-temporal) to orchestrate jobs and ensure reliability at scale. Airbyte leverages [dbt](https://www.youtube.com/watch?v=saXwh6SpeHA) to normalize extracted data and can trigger custom transformations in SQL and dbt. You can also orchestrate Airbyte syncs with [Airflow](https://docs.airbyte

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

We believe that only an **open-source** solution to data movement can cover the **long tail of data sources** while empowering data engineers to **customize existing connectors**. Our ultimate vision is to help you move data from any source to any destination. Airbyte already provides [300+ connectors](https://docs.airbyte.com/integrations/) for popular APIs, databases, data warehouses, and data lakes.

You can implement Airbyte connectors in any language and take the form of a Docker image that follows the [Airbyte specification](https://docs.airbyte.com/understanding-airbyte/airbyte-protocol/). You can create new connectors very fast with:

- The [low-code Connector Development Kit](https://docs.airbyte.com/connector-development/config-based/low-code-cdk-overview) (CDK) for API connectors ([demo](https://www.youtube.com/watch?v=i7VSL2bDvmw))
- The [Python CDK](https://docs.airbyte.com/connector-development/cdk-python/) ([tutorial](https://docs.airbyte.com/connector-development/tutorials/cdk-speedrun))

Airbyte has a built-in scheduler and uses [Temporal](https://airbyte.com/blog/scale-workflow-orchestration-with-temporal) to orchestrate jobs and ensure reliability at scale. Airbyte leverages [dbt](https://www.youtube.com/watch?v=saXwh6SpeHA) to normalize extracted data and can trigger custom transformations in SQL and dbt. You can also orchestrate Airbyte syncs with [Airflow](https://docs.airbyte

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

We believe that only an **open-source** solution to data movement can cover the **long tail of data sources** while empowering data engineers to **customize existing connectors**. Our ultimate vision is to help you move data from any source to any destination. Airbyte already provides [300+ connectors](https://docs.airbyte.com/integrations/) for popular APIs, databases, data warehouses, and data lakes.

You can implement Airbyte connectors in any language and take the form of a Docker image that follows the [Airbyte specification](https://docs.airbyte.com/understanding-airbyte/airbyte-protocol/). You can create new connectors very fast with:

- The [low-code Connector Development Kit](https://docs.airbyte.com/connector-development/config-based/low-code-cdk-overview) (CDK) for API connectors ([demo](https://www.youtube.com/watch?v=i7VSL2bDvmw))
- The [Python CDK](https://docs.airbyte.com/connector-development/cdk-python/) ([tutorial](https://docs.airbyte.com/connector-development/tutorials/cdk-speedrun))

Airbyte has a built-in scheduler and uses [Temporal](https://airbyte.com/blog/scale-workflow-orchestration-with-temporal) to orchestrate jobs and ensure reliability at scale. Airbyte leverages [dbt](https://www.youtube.com/watch?v=saXwh6SpeHA) to normalize extracted data and can trigger custom transformations in SQL and dbt. You can also orchestrate Airbyte syncs with [Airflow](https://docs.airbyte

…(truncated)…
```

### `pyproject.toml`

```
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
addopts ="-r a --capture=no -vv --log-level=DEBUG --color=yes"
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
.dockerignore
.editorconfig
.github
.gitignore
.idea
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
README.md
THANK-YOU.md
airbyte-airflow-more
airbyte-api
airbyte-base-java-image
airbyte-cdk
airbyte-ci
airbyte-commons
airbyte-commons-cli
airbyte-commons-protocol
airbyte-config-oss
airbyte-connector-test-harnesses
airbyte-db
airbyte-integrations
airbyte-json-validation
airbyte-test-utils
build.gradle
buildSrc
codecov.yml
connectors.md
deps.toml
docs
docusaurus
gradle
… +13 more
```

## 5. My contribution / role (evidence from git history — if available)

```text
fce47866 2025-01-30 Merge pull request #8 from BotNotOrg/feat/update-destination-klaviyo-version
b9a21ed4 2025-01-30 fix: remove redundant key value in dict
57210c67 2025-01-30 fix: hardfix airbyte cdk version
e48ecb9b 2025-01-30 fix: conflicts
189fe398 2025-01-30 wip: try to fix spec json
d4df53c2 2025-01-30 Merge pull request #15 from BotNotOrg/feat/update-klaviyo-version
4d634884 2025-01-30 Merge branch 'feat/update-destination-klaviyo-version' into feat/update-klaviyo-version
add5fe44 2025-01-30 Merge branch 'dev' into feat/update-klaviyo-version
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
from airbyte_cdk.connector_builder.connector_builder_handler import (
    TestReadLimits,
    create_source,
    get_limits,
    list_streams,
    read_stream,
    resolve_manifest,
)
from airbyte_cdk.entrypoint import AirbyteEntrypoint
from airbyte_cdk.models import ConfiguredAirbyteCatalog
from airbyte_cdk.sources.declarative.manifest_declarative_source import ManifestDeclarativeSource
from airbyte_cdk.utils.traced_exception import AirbyteTracedException


def get_config_and_catalog_from_args(args: List[str]) -> Tuple[str, Mapping[str, Any], Optional[ConfiguredAirbyteCatalog]]:
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
    source: ManifestDeclarativeSource, command: str, config: Mapping[str, Any], catalog: Optional[ConfiguredAirbyteCatalog], limits: TestReadLimits
):
    if command == "resolve_manifest":
        return resolve_manifest(source)
    elif command == "test_read":
        assert catalog is not None, "`test_read` requires a valid `ConfiguredAirbyteCatalog`, got None."
        return 

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

**`airbyte-integrations/connectors/destination-amazon-sqs/main.py`**

```python
#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from destination_amazon_sqs import DestinationAmazonSqs

if __name__ == "__main__":
    DestinationAmazonSqs().run(sys.argv[1:])
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`yofi-airbyte-klaviyo-source`** capabilities aligned with **airbyte integrations** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yofi-airbyte-klaviyo-source`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

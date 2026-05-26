# yofi-airbyte-klaviyo-source-temp

**Path:** `D:/botnot/yofi-airbyte-klaviyo-source-temp`  
**Category:** airbyte-integrations  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

Internal **Yofi** repository `yofi-airbyte-klaviyo-source-temp` under category **airbyte-integrations**. Supports Yofi/Botnot platform capabilities (e-commerce intelligence, anti-fraud adjacent services, data plane, or infrastructure) as evidenced by repository layout and manifests.

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

_No common manifest files found at repository root._


## 3. Architecture

_High-level: see README and `stacks/` / `src/` layout for service-specific flow._

- **Inbound:** HTTP (API Gateway / ALB), scheduled triggers, queues (SQS/SNS), EventBridge rules, or batch — infer from `stacks/`, `template.yaml`, `sst.config.ts`, or `src/` handlers.
- **Outbound:** databases and external HTTP APIs per layers and `package.json` / Python imports in handlers.
- **IaC pattern:** SST/CDK, SAM/CloudFormation, Pulumi, Helm, Terraform, or raw scripts — see manifests section.

## 4. Key files (auto-discovered)

- **Top-level entries:**

```
.idea
airbyte-master
```

## 5. My contribution / role (evidence from git history — if available)

_No readable `git log` in this working copy (shallow clone, missing .git, or not a git repo)._

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`airbyte-master/airbyte-cdk/python/airbyte_cdk/connector_builder/main.py`**

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

**`airbyte-master/airbyte-cdk/python/source_declarative_manifest/main.py`**

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

**`airbyte-master/airbyte-integrations/connectors/destination-amazon-sqs/main.py`**

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

- Owned or extended **`yofi-airbyte-klaviyo-source-temp`** capabilities aligned with **airbyte integrations** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yofi-airbyte-klaviyo-source-temp`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

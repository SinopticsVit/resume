# yofi-lambda-graph-spanner-service

**Path:** `D:/botnot/yofi-lambda-graph-spanner-service`  
**Category:** persistence  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# Getting Started with Serverless Stack (SST)

This project was bootstrapped with [Create Serverless Stack](https://docs.serverless-stack.com/packages/create-serverless-stack).

Start by installing the dependencies.

```bash
$ npm install
```

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

### `README.md`

```
# Getting Started with Serverless Stack (SST)

This project was bootstrapped with [Create Serverless Stack](https://docs.serverless-stack.com/packages/create-serverless-stack).

Start by installing the dependencies.

```bash
$ npm install
```

## Commands

### `npm run start`

Starts the local Lambda development environment.

### `npm run build`

Build your app and synthesize your stacks.

Generates a `.build/` directory with the compiled files and a `.build/cdk.out/` directory with the synthesized CloudFormation stacks.

### `npm run deploy [stack]`

Deploy all your stacks to AWS. Or optionally deploy, a specific stack.

### `npm run remove [stack]`

Remove all your stacks and all of their resources from AWS. Or optionally removes, a specific stack.

### `npm run test`

Runs your tests using Jest. Takes all the [Jest CLI options](https://jestjs.io/docs/en/cli).

## Documentation

Learn more about the Serverless Stack.
- [Docs](https://docs.serverless-stack.com)
- [@serverless-stack/cli](https://docs.serverless-stack.com/packages/cli)
- [@serverless-stack/resources](https://docs.serverless-stack.com/packages/resources)

## Community

[Follow us on Twitter](https://twitter.com/ServerlessStack) or [post on our forums](https://discourse.serverless-stack.com).


## Setup up pytest

Please install below packages to enable pytest

```
pip install pytest setuptools python-dotenv pytest-env pytest-cov
```
```

### `readme.md`

```
# Getting Started with Serverless Stack (SST)

This project was bootstrapped with [Create Serverless Stack](https://docs.serverless-stack.com/packages/create-serverless-stack).

Start by installing the dependencies.

```bash
$ npm install
```

## Commands

### `npm run start`

Starts the local Lambda development environment.

### `npm run build`

Build your app and synthesize your stacks.

Generates a `.build/` directory with the compiled files and a `.build/cdk.out/` directory with the synthesized CloudFormation stacks.

### `npm run deploy [stack]`

Deploy all your stacks to AWS. Or optionally deploy, a specific stack.

### `npm run remove [stack]`

Remove all your stacks and all of their resources from AWS. Or optionally removes, a specific stack.

### `npm run test`

Runs your tests using Jest. Takes all the [Jest CLI options](https://jestjs.io/docs/en/cli).

## Documentation

Learn more about the Serverless Stack.
- [Docs](https://docs.serverless-stack.com)
- [@serverless-stack/cli](https://docs.serverless-stack.com/packages/cli)
- [@serverless-stack/resources](https://docs.serverless-stack.com/packages/resources)

## Community

[Follow us on Twitter](https://twitter.com/ServerlessStack) or [post on our forums](https://discourse.serverless-stack.com).


## Setup up pytest

Please install below packages to enable pytest

```
pip install pytest setuptools python-dotenv pytest-env pytest-cov
```
```

### `Readme.md`

```
# Getting Started with Serverless Stack (SST)

This project was bootstrapped with [Create Serverless Stack](https://docs.serverless-stack.com/packages/create-serverless-stack).

Start by installing the dependencies.

```bash
$ npm install
```

## Commands

### `npm run start`

Starts the local Lambda development environment.

### `npm run build`

Build your app and synthesize your stacks.

Generates a `.build/` directory with the compiled files and a `.build/cdk.out/` directory with the synthesized CloudFormation stacks.

### `npm run deploy [stack]`

Deploy all your stacks to AWS. Or optionally deploy, a specific stack.

### `npm run remove [stack]`

Remove all your stacks and all of their resources from AWS. Or optionally removes, a specific stack.

### `npm run test`

Runs your tests using Jest. Takes all the [Jest CLI options](https://jestjs.io/docs/en/cli).

## Documentation

Learn more about the Serverless Stack.
- [Docs](https://docs.serverless-stack.com)
- [@serverless-stack/cli](https://docs.serverless-stack.com/packages/cli)
- [@serverless-stack/resources](https://docs.serverless-stack.com/packages/resources)

## Community

[Follow us on Twitter](https://twitter.com/ServerlessStack) or [post on our forums](https://discourse.serverless-stack.com).


## Setup up pytest

Please install below packages to enable pytest

```
pip install pytest setuptools python-dotenv pytest-env pytest-cov
```
```

### `package.json`

```
{
  "engines": {
    "node": ">=18.0.0",
    "npm": "9.5.0"
  },
  "name": "botnot-lambda-graph-spanner",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "test": "sst test",
    "start": "sst start",
    "build": "sst build",
    "deploy": "sst deploy",
    "remove": "sst remove"
  },
  "eslintConfig": {
    "extends": [
      "serverless-stack"
    ]
  },
  "devDependencies": {
    "@aws-cdk/aws-lambda-python-alpha": "2.132.1-alpha.0",
    "@tsconfig/node16": "1.0.3",
    "async": ">=2.6.4",
    "aws-cdk-lib": "2.132.1",
    "constructs": "10.3.0",
    "jszip": ">=3.8.0",
    "sst": "2.43.7",
    "ts-node": "^10.9.1",
    "typescript": "^4.8.4"
  }
}
```

### `sst.config.ts`

```
import type {SSTConfig} from "sst"

// @ts-ignore
import {GraphFormationServiceStack} from "./stacks/MainStack.ts"

export default {
    config(input) {
        return {
            name: "graph-spanner-lambda",
            region: "us-east-1",
            profile: input.stage === "prod" ? "prod" : "dev",
        }
    },
    stacks(app) {
        app.setDefaultFunctionProps({
            // handler: 'src/lambda.handler',
            runtime: 'python3.9',
            tracing: "disabled",
            timeout: 30
        })

        app.stack(GraphFormationServiceStack, {id: "sst-stack"})
    },
} satisfies SSTConfig
```

### `Makefile`

```
all:	stack-deploy
all-prod: stack-deploy-prod

install-deps:
	npm install

stack-build: install-deps
	npm run build -- --stage dev --region us-east-1

stack-test: stack-build
	echo npm run test

stack-deploy: stack-test
	npm run deploy -- --stage dev --region us-east-1

stack-build-prod: install-deps
	npm run build -- --stage prod --region us-east-1 --profile prod

stack-test-prod: stack-build-prod
	echo npm run test

stack-deploy-prod: stack-test-prod
	npm run deploy -- --stage prod --region us-east-1 --profile prod

clean:
	rm -rf .build build
	rm -rf .pytest_cache cdk.out
	rm -rf .sst node_modules
	rm -rf src/__pycache__
	rm -rf test/__pycache__
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
Makefile
README.md
hs_err_pid12300.log
hs_err_pid12436.log
hs_err_pid12876.log
hs_err_pid19332.log
hs_err_pid20292.log
hs_err_pid20496.log
hs_err_pid25436.log
hs_err_pid26668.log
hs_err_pid27392.log
hs_err_pid31820.log
hs_err_pid31884.log
hs_err_pid34004.log
hs_err_pid34332.log
hs_err_pid34692.log
hs_err_pid3584.log
hs_err_pid37700.log
hs_err_pid37732.log
hs_err_pid38292.log
hs_err_pid39924.log
hs_err_pid40004.log
hs_err_pid6596.log
hs_err_pid7132.log
hs_err_pid7200.log
hs_err_pid8716.log
layer
neo4j_ops
node_modules
package-lock.json
package.json
pytest.ini
seed.yml
src
sst.config.ts
stacks
tests
```

## 5. My contribution / role (evidence from git history — if available)

```text
121090e 2025-09-19 Merge pull request #38 from BotNotOrg/dev
54f0d10 2025-09-19 Feat/optimize graph query (#37)
0ffb790 2025-09-16 Merge pull request #36 from BotNotOrg/feat/fix_time_conn
862194d 2025-09-16 feat: remove time range connection
8d735db 2025-09-11 Merge pull request #35 from BotNotOrg/feat/remove_metrics
b3d2468 2025-09-11 fix: remove metrics
257a2ae 2025-08-07 Merge pull request #34 from BotNotOrg/feature/YOFI-778-processor-refactor
e7dc934 2025-05-26 fix: spanner write (#33)
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`src/main.py`**

```python
from typing import List, Optional
import os
import json
import boto3
import arrow
from maps import (ORDER_NODE, EMAIL_NODE, EMAIL_DOMAIN_NODE, CLEAN_EMAIL_NODE, PHONE_NODE, USER_IP_NODE, 
                  ADDRESS_ID_NODE, ADDRESS_STREET_NAME_NODE, ADDRESS_UNIT_NODE, ADDRESS_STREET_NUMBER_NODE, ADDRESS_ORIGINAL_NODE,
                  NETWORK_SUBNET_NODE, USER_AGENT_CONNECTION_NODE, LAST_NAME_NODE, PAYMENT_RETAILS_NODE,
                  PRODUCT_ID_NODE, PRODUCT_VARIANT_ID, TIMERANGE_NODE, GEOLOCATION_NODE, GEOLOCATION_RANGE_NODE,
                  BRO_PRINT_NODE, JA3_NODE, SESSION_PATH_NODE, DISCOUNT_NODE,
                  CUSTOMER_NODE, CLIENT_ID_NODE, BING_GAN_NODE)
from maps import POS, DEFAULT_COND_NAME, MAP_WEIGHT, NODES_SHOP_ADDRESS, OFFLINE_SHOP_ADDRESS, DEFAULT_NODE_BUCKETS
from cluster_entities import (
    ClusterConnection,
    CustomerOrderConnection,
    EmailConnection,
    ClusterEntity, Customer, Order, CustomerCreate,
    EmailDomainConnection, CleanEmailConnection,
    AddressConnection,
    UpdateWeightConnection,
    AddressOriginalConnection,
    PhoneConnection,
    UserIpConnection,
    NetworkSubnetConnection,
    UserAgentConnection,
    LastNameConnection,
    PaymentDetailsConnection,
    ProductIdConnection,
    ProductVariantConnection,
    DiscountConnection,
    TimeRangeConnection,
    GeolocationConnection,
    GeolocationRangeConnection,
    JA3Connection,
    BroPrintConnection,
    SessionPathConnection,
    ClientIdConnection,
    BingGanConnection,
    create_batch,
    create_transaction
)

from helper import (
    logger,
    mongo_client,
    find_customers_with_depth,
    get_store_settings_from_mongo
)
from spanner_lib import SPANNER, convert_object_to_json, update_connected_customer_info
from yofi_common_libs.order_event import retrieve_payload
from yofi_common_libs.universal_event_message import UniversalEventMessage
from yofi_common_libs.processor import ProcessorFactory, ProcessorStrategy  
from processors.return_processor import ReturnGraphProcessor

ProcessorFactory.register_processor(ReturnGraphProcessor)   

secretsManager = boto3.clie

…(truncated)…
```

**`src/test/main.py`**

```python
#!/usr/bin/env python

# Copyright 2016 Google, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This application demonstrates how to do basic operations using Cloud
Spanner.

For more information, see the README.rst under /spanner.
"""

import argparse
import base64
import datetime
import decimal
import json
import logging
import time

from google.cloud import spanner
from google.cloud.spanner_admin_instance_v1.types import spanner_instance_admin
from google.cloud.spanner_v1 import DirectedReadOptions, param_types
from google.cloud.spanner_v1.data_types import JsonObject
from google.protobuf import field_mask_pb2  # type: ignore


OPERATION_TIMEOUT_SECONDS = 240


# [START spanner_create_instance]
def create_instance(instance_id):
    """Creates an instance."""
    from google.cloud.spanner_admin_instance_v1.types import \
        spanner_instance_admin

    spanner_client = spanner.Client()

    config_name = "{}/instanceConfigs/regional-us-central1".format(
        spanner_client.project_name
    )

    operation = spanner_client.instance_admin_api.create_instance(
        parent=spanner_client.project_name,
        instance_id=instance_id,
        instance=spanner_instance_admin.Instance(
            config=config_name,
            display_name="This is a display name.",
            node_count=1,
            labels={
                "cloud_spanner_samples": "true",
                "sample_name": "snippets-create_instance-explicit",
                "created": str(int(time.time())),
            },
            edition=spanner_instance_admin.Instance.Edition.STANDARD,  # Optional
   

…(truncated)…
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`yofi-lambda-graph-spanner-service`** capabilities aligned with **persistence** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yofi-lambda-graph-spanner-service`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

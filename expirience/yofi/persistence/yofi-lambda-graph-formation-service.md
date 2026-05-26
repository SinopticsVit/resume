# yofi-lambda-graph-formation-service

**Path:** `D:/botnot/yofi-lambda-graph-formation-service`  
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
```

### `package.json`

```
{
  "engines": {
    "node": ">=18.0.0",
    "npm": "9.5.0"
  },
  "name": "botnot-lambda-graph-db-edit-processing",
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
    "jszip": ">=3.7.0",
    "sst": "^2.43.7",
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
            name: "graph-formation-lambda",
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
layer
neo4j_ops
node_modules
package-lock.json
package.json
seed.yml
src
sst.config.ts
stacks
```

## 5. My contribution / role (evidence from git history — if available)

```text
04392b9 2024-11-18 rename cluster_info to cluster_info_neo4j
ab1887a 2024-11-18 stop-push feature analytics lambda
621d07d 2024-11-04 fix: add more info to cluster_info
b3c2258 2024-11-01 fix: limit connected customers
0185816 2024-10-31 feat: add connected connections
659ac97 2024-10-31 fix: code clean, remove logs
509be27 2024-10-17 [DEFAULT_COND_NAME]
6bf4bea 2024-10-11 fix: pip
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`src/main.py`**

```python
from typing import List
from neo4j import GraphDatabase
import arrow
import os
from maps import (DISCOUNT_NODE, CLEAN_EMAIL_NODE, ORDER_NODE, EMAIL_NODE, EMAIL_DOMAIN_NODE, ADDRESS_STREET_NAME_NODE,
                  ADDRESS_STREET_NUMBER_NODE, ADDRESS_UNIT_NODE, ADDRESS_ORIGINAL_NODE, PHONE_NODE, USER_IP_NODE,
                  NETWORK_SUBNET_NODE, USER_AGENT_CONNECTION_NODE, LAST_NAME_NODE, PAYMENT_RETAILS_NODE,
                  PRODUCT_ID_NODE, PRODUCT_VARIANT_ID, TIMERANGE_NODE, GEOLOCATION_NODE, GEOLOCATION_RANGE_NODE,
                  BRO_PRINT_NODE, JA3_NODE, SESSION_PATH_NODE, CUSTOMER_NODE)
from maps import POS, DEFAULT_COND_NAME, MAP_WEIGHT, OFFLINE_SHOP_ADDRESS, NODES_SHOP_ADDRESS
from cluster_entities import (
    ClusterEntity, Customer, Order, CustomerCreate,
    ClusterConnection,
    CustomerOrderConnection,
    EmailConnection,
    EmailDomainConnection,
    CleanEmailConnection,
    AddressConnection,
    AddressOriginalConnection,
    PhoneConnectoin,
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
)
from features import *
from helper import (
    logger,
    mongo_client,
    find_customers_with_depth,
    get_entity_from_mongo,
    update_shop_address_id_address,
    find_customers_connected_with_node,
    find_orders_connected_with_node
)
from secret_manager import get_secret

secretsManager = boto3.client('secretsmanager')
sns = boto3.client('sns')
sqs = boto3.client('sqs')
lambda_client = boto3.client('lambda')

HIGH_EVENT_THRESHOLD = 500  # This means event is rising quickly
LOW_EVENT_THRESHOLD = 50 # This means event is decreasing
HIGH_PRIORITY_EVENT_SQS_URL = os.environ["HIGH_PRIORITY_EVENT_SQS_URL"]
LOW_PRIORITY_EVENT_SQS_ARN = os.environ["LOW_PRIORITY_EVENT_SQS_ARN"]
AWS_LAMBDA_FUNCTION_NAME=os.environ["AWS_LAMBDA_FUNCTION_NAME"]

neo4j_credentia

…(truncated)…
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`yofi-lambda-graph-formation-service`** capabilities aligned with **persistence** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yofi-lambda-graph-formation-service`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

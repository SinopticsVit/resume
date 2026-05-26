# botnot-lambda-mongodb-edit-processing

**Path:** `D:/botnot/botnot-lambda-mongodb-edit-processing`  
**Category:** persistence  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# Order Edit Processing Lambda

MongoDB version

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

### `README.md`

```
# Order Edit Processing Lambda

MongoDB version
```

### `readme.md`

```
# Order Edit Processing Lambda

MongoDB version
```

### `Readme.md`

```
# Order Edit Processing Lambda

MongoDB version
```

### `package.json`

```
{
  "name": "botnot-lambda-mongodb-edit-processing",
  "engines": {
    "node": ">=18.0.0",
    "npm": "9.5.0"
  },
  "version": "1.4.2",
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
    "sst": "2.48.5",
    "ts-node": "^10.9.1",
    "typescript": "^4.8.4"
  }
}
```

### `sst.config.ts`

```
import type {SSTConfig} from "sst"

// @ts-ignore
import {MlGatewayServiceStack} from "./stacks/MainStack.ts"

export default {
    config(input) {
        return {
            name: "yofi-backend-lambda-mongodb-edit-event-processor",
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

        app.stack(MlGatewayServiceStack, {id: "sst-stack"})
    },
} satisfies SSTConfig
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
layer
node_modules
package.json
seed.yml
src
sst.config.ts
stacks
venv
```

## 5. My contribution / role (evidence from git history — if available)

```text
9f11c1d 2025-06-25 update sst 2.48.5
46cb847 2025-06-25 Merge remote-tracking branch 'origin/dev' into dev
76531a0 2025-06-23 add partner_order_id
8696a4c 2025-04-15 fixed editor
51c3396 2025-04-14 fix: change concurrency to 2
6e0ff2b 2025-04-10 feat: Change to diffrent dedup group
d300360 2025-03-31 feat: 2025-Mar-31: No need to build cluster for customer without order
297ae6e 2025-03-19 Merge pull request #32 from BotNotOrg/feature/YOFI-256-repredict-if-tag-change
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`src/customer/main.py`**

```python
import json

import pymongo
from libs.default_logging import logger
import yofi_common_libs
import os
import boto3
import time
from pymongo.errors import DuplicateKeyError

from libs.shared_mongo_code.convert_shopify_order import convert_customer_to_internal_format
from libs.persist_to_spanner import persist_customer_to_spanner, get_customer_from_spanner
from .util import extract_all_tags, get_yofi_label_changes, get_tag_set

mongodb_client = yofi_common_libs.YofiMongoClient()
sqs = boto3.client('sqs')
sns_client = boto3.client('sns')

CUSTOMER_TAGS_APPLY_SQS_URL = os.environ['CUSTOMER_TAGS_APPLY_SQS_URL']
GRAPH_FORMATION_INTERACTION_SERVICE_ARN = os.environ['GRAPH_FORMATION_INTERACTION_SERVICE_ARN']

def handler(event: dict, context):
    for record in event['Records']:
        process_record(record)


def process_record(record):
    body = json.loads(record['body'])
    webhook_topic = body['detail']['metadata']['X-Shopify-Topic']
    shop_url = body['detail']['metadata']['X-Shopify-Shop-Domain']
    payload = body['detail']

    logger.info(f"Got event({webhook_topic}) of {shop_url}")
    logger.debug(f'Upstream (original) payload object: {payload}')
    shopify_raw_customer = payload['payload']
    shopify_raw_customer['shop_url'] = shop_url

    current_customer = convert_customer_to_internal_format(shopify_raw_customer)

    label_rules = get_rules(shop_url)
    tags_from_event = get_tag_set(current_customer)
    if label_rules:
        # set latest tags and save to mongodb later
        final_tags = extract_all_tags(current_customer, label_rules)
        if final_tags != tags_from_event:
            current_customer['tags'] = ", ".join(final_tags)

    previous_customer = get_customer_from_spanner(shop_url, shopify_raw_customer.get('id'))
    save_customer_to_spanner(current_customer, shopify_raw_customer)

    if webhook_topic == 'customers/create':
        # 2025-Mar-31: No need to build cluster for customer without order
        # publish_graph_formation_task(current_customer, shop_url)
        return

    label_rules = label_rules or {'tags_rules': {}, 'note_rules': {}}
    # 

…(truncated)…
```

**`src/main.py`**

```python
import json

from libs.constants import ORDERS_UPDATED, ORDERS_CANCELLED, ORDERS_DELETE, REFUNDS_CREATE, RETURN_RELATED_EVENTS
from libs.default_logging import logger
from libs.webhook_event_processor import OrderProcessor, OrderUpdateProcessor, OrderCanceledProcessor, \
    OrderDeletedProcessor, RefundCreatedProcessor, ReturnUpdatedProcessor

return_processors = {_event: ReturnUpdatedProcessor for _event in RETURN_RELATED_EVENTS}
processors = {
    ORDERS_UPDATED: OrderUpdateProcessor,
    ORDERS_CANCELLED: OrderCanceledProcessor,
    ORDERS_DELETE: OrderDeletedProcessor,
    REFUNDS_CREATE: RefundCreatedProcessor,
    **return_processors,
}


def handler(event: dict, context):
    """Handle incoming event and process based on its type."""
    # logger.debug(f'Incoming payload: {json.dumps(event)}')

    for record in event['Records']:
        body = json.loads(record['body'])
        webhook_topic = body['detail']['metadata']['X-Shopify-Topic']
        shop_url = body['detail']['metadata']['X-Shopify-Shop-Domain']
        payload = body['detail']

        logger.info(f"Got event({webhook_topic}) of {shop_url}")
        logger.debug(f'Upstream (original) payload object: {payload}')

        processor: OrderProcessor = processors.get(webhook_topic)(payload, shop_url, webhook_topic)

        if processor:
            processor.process()
        else:
            logger.error('MONGODB-EDITOR: Unknown webhook topic %s in record=%s', webhook_topic, record)
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`botnot-lambda-mongodb-edit-processing`** capabilities aligned with **persistence** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `botnot-lambda-mongodb-edit-processing`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

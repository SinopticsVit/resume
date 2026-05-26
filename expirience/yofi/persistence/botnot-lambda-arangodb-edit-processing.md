# botnot-lambda-arangodb-edit-processing

**Path:** `D:/botnot/botnot-lambda-arangodb-edit-processing`  
**Category:** persistence  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

Internal **Yofi** repository `botnot-lambda-arangodb-edit-processing` under category **persistence**. Supports Yofi/Botnot platform capabilities (e-commerce intelligence, anti-fraud adjacent services, data plane, or infrastructure) as evidenced by repository layout and manifests.

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

### `package.json`

```
{
  "name": "botnot-lambda-arangodb-edit-processing",
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
  "dependencies": {
    "@serverless-stack/cli": "0.69.7",
    "@serverless-stack/resources": "0.69.7",
    "@aws-cdk/aws-lambda-python-alpha": "2.15.0-alpha.0",
    "aws-cdk-lib": "2.15.0",
    "ts-node": "^10.9.1",
    "async": ">=2.6.4",
    "jszip": ">=3.7.0"
  }
}
```

### `sst.json`

```
{
  "name": "botnot-lambda-arangodb-edit-processing",
  "type": "@serverless-stack/resources",
  "region": "us-east-1",
  "main": "stacks/index.js"
}
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
layer
package.json
seed.yml
src
sst.json
stacks
```

## 5. My contribution / role (evidence from git history — if available)

```text
8c51406 2023-05-30 add logRetention: "one_year"
38dc367 2023-05-29 add logRetention: "one_month"
5d0815e 2023-05-22 push updated order to downsteam
976c387 2023-05-22 fix datetime json parse error
34c77fa 2023-05-20 fix arango host env var
3beced1 2023-05-19 fix JsonDecode error
6a06f2d 2023-05-19 fix arango host env var
bf48337 2023-05-19 add requirements
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`src/main.py`**

```python
import json

from libs.persist_to_arango import update_order_arango_converter_version, save_history_arango
from libs.default_logging import logger
from libs.downstream import push_to_downstream_elasticsearch
from libs.refund import insert_created_refunds_into_original_order
from libs.arangoid import arangoid_order_unique_id


def process_order(order):
    logger.info(f'ARANGODB-EDITOR: Updating order object to ARANGODB instance ...')
    updated_order = update_order_arango_converter_version(order)
    logger.info(f'ARANGODB-EDITOR: Order object updated successfully')

    if updated_order and updated_order.get("customer"):
        logger.info(f'ARANGODB-EDITOR: Pushing order object to downstream (search-lambda) to save into ElasticSearch ...')
        push_to_downstream_elasticsearch(updated_order)
        logger.info(f'ARANGODB-EDITOR: Order object pushed to downstream successfully')
    else:
        logger.info(f'ARANGODB-EDITOR: Nothing to push to downstream')

def handler(event, _):
    logger.info(f'DEBUG: Incoming payload: {event}')

    for record in event['Records']:
        body = json.loads(record['body'])
        webhook_topic = body['detail']['metadata']['X-Shopify-Topic']
        shop_url = body['detail']['metadata']['X-Shopify-Shop-Domain']
        payload = body['detail']['payload']
        logger.warning(f'ARANGODB-EDITOR: {webhook_topic} webhook topic received for {shop_url}')
        logger.info(f'ARANGODB-EDITOR: Upstream (original) payload object: {payload}')
        if _detect_event_errors(body['detail']):
            return

        is_order_event = webhook_topic in ['orders/updated', 'orders/cancelled']
        is_refund_event = webhook_topic in ['refunds/create']

        payload['shop_url'] = shop_url
        payload['partner_id'] = '1'

        raw_order_id = payload['id'] if is_order_event else payload['order_id'] if is_refund_event else None
        arango_order_id = arangoid_order_unique_id({
            'partner_id': payload['partner_id'],
            'shop_url': payload['shop_url'],
            'id': raw_order_id
        })
        save_history_arango(payload, arang

…(truncated)…
```

**`stacks/index.js`**

```text
import MyStack from './Stack';
import { Runtime, Tracing } from 'aws-cdk-lib/aws-lambda';
import { Duration } from 'aws-cdk-lib';

export default function main(app) {
  app.setDefaultFunctionProps({
    srcPath: 'src',
    runtime: Runtime.PYTHON_3_9,
    tracing: Tracing.ACTIVE,
    timeout: Duration.seconds(30)
  });

  new MyStack(app, 'sst-stack', { prefix: 'botnot-lambda', name: 'arangodb-edit' });
}
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`botnot-lambda-arangodb-edit-processing`** capabilities aligned with **persistence** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `botnot-lambda-arangodb-edit-processing`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

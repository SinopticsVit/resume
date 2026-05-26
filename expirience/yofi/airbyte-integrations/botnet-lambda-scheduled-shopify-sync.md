# botnet-lambda-scheduled-shopify-sync

**Path:** `D:/botnot/botnet-lambda-scheduled-shopify-sync`  
**Category:** airbyte-integrations  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# Shopify Orders Scheduled Sync
This lambda will be triggered even N hours to sync Shopify orders with our orders in MongoDB.

# Purge Logic:
 - Get order ids from mongodb from 2 hours ago
 - Send a [find] request by Shopify API with all ids we found
 - Filter original order ids with returned ones
 - Move non-existent orders from [order] to [order_moved]

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

### `README.md`

```
# Shopify Orders Scheduled Sync
This lambda will be triggered even N hours to sync Shopify orders with our orders in MongoDB.

# Purge Logic:
 - Get order ids from mongodb from 2 hours ago
 - Send a [find] request by Shopify API with all ids we found
 - Filter original order ids with returned ones
 - Move non-existent orders from [order] to [order_moved]
```

### `readme.md`

```
# Shopify Orders Scheduled Sync
This lambda will be triggered even N hours to sync Shopify orders with our orders in MongoDB.

# Purge Logic:
 - Get order ids from mongodb from 2 hours ago
 - Send a [find] request by Shopify API with all ids we found
 - Filter original order ids with returned ones
 - Move non-existent orders from [order] to [order_moved]
```

### `Readme.md`

```
# Shopify Orders Scheduled Sync
This lambda will be triggered even N hours to sync Shopify orders with our orders in MongoDB.

# Purge Logic:
 - Get order ids from mongodb from 2 hours ago
 - Send a [find] request by Shopify API with all ids we found
 - Filter original order ids with returned ones
 - Move non-existent orders from [order] to [order_moved]
```

### `package.json`

```
{
  "name": "botnet-lambda-scheduled-shopify-sync",
  "version": "0.0.1",
  "private": true,
  "scripts": {
    "start": "sst start",
    "build": "sst build",
    "deploy": "sst deploy",
    "remove": "sst remove",
    "console": "sst console",
    "typecheck": "tsc --noEmit",
    "test": "sst bind -- vitest run"
  },
  "eslintConfig": {
    "extends": [
      "serverless-stack"
    ]
  },
  "devDependencies": {
    "@aws-cdk/aws-lambda-python-alpha": "2.39.1-alpha.0",
    "aws-cdk-lib": "2.39.1",
    "@serverless-stack/cli": "1.16.1",
    "@serverless-stack/resources": "1.16.1",
    "typescript": "^4.8.4",
    "@tsconfig/node16": "1.0.3",
    "vitest": "^0.24.5"
  }
}
```

### `sst.json`

```
{
  "name": "botnet-lambda-scheduled-shopify-sync",
  "region": "us-east-1",
  "main": "stacks/index.js"
}
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

stack-build-prod:
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
	rm -f cdk.context.json
```

### `tsconfig.json`

```
{
  "extends": "@tsconfig/node16/tsconfig.json",
  "include": [
    "stacks"
  ]
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
Makefile
README.md
layer
package.json
src
sst.json
stacks
tsconfig.json
```

## 5. My contribution / role (evidence from git history — if available)

```text
fc67f45 2023-09-06 remove commented code
7e9c427 2023-09-04 ass ssm permission
8a13eef 2023-09-04 get shopify version by ssm (#15)
be816c2 2023-07-14 Fixing get_order_ids_existing_in_shopify (chunks)
87cf6ba 2023-07-14 fix: need to extract the ids so that it can compare with mongo
c183e88 2023-07-14 fix: ids
d384212 2023-07-14 fix: use only one shopify session
44731c0 2023-07-13 Fixing order_ids issue
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`src/work-distributor-function/main.py`**

```python
import json
import logging
import os
import typing
from datetime import datetime, timedelta

import boto3
from bson.json_util import dumps
from mongo import MongoDB

logger = logging.getLogger()
logger.setLevel(logging.INFO)

SNS = 'sns'
POST = 'post'
SCHEDULE = 'schedule'
REEVALUATION = 'reevaluation'

mongo = MongoDB(os.environ['MONGO_INSTANCE_URL_PRIVATE'], 'billing')


def handler(event, context):
    json_dumps = json.dumps(event)
    logger.info("Processing Event -> " + json_dumps)
    items = mongo.find('detail', {
        "is_service_suspended": False,
        "is_installed": True
    })
    items_json = json.loads(dumps(items))
    if items_json:
        for item in items_json:
            logger.info(f'record={item}')
            shop_url = item["shop_url"]
            api_page_limit = int(os.environ['LIMIT_ITEMS_PER_API_CALL'])
            delta_in_hours = int(os.environ['TIMEDELTA_FOR_SCHEDULED_SYNK_HOURS'])
            max_orders_to_process = int(os.environ['MAX_NUMBER_OR_ORDERS_TO_PROCESS_PER_SYNC'])
            worker_parameters = _generate_worker_parameters(shop_url, max_orders_to_process, api_page_limit, delta_in_hours)
            _send_event_to_workers_sns(worker_parameters)


def _generate_worker_parameters(shop_url, max_orders_to_process, api_page_limit, delta_in_hours):
    return dict(
        shop_url=shop_url,
        created_at_min=str(
            datetime.now() - timedelta(hours=delta_in_hours)
        ),
        created_at_max=str(
            datetime.now() - timedelta(minutes=15)
        ),
        max_orders_to_process=max_orders_to_process,
        api_page_limit=api_page_limit,
        status='any'
    )


def _send_event_to_workers_sns(params):
    client = boto3.client('sns')
    client.publish(
        TargetArn=os.environ["WORKERS_PROCESSING_TOPIC"],
        Message=json.dumps({'default': json.dumps(params)}),
        MessageStructure='json'
    )


def _resp(status: int, message: str) -> typing.Dict:
    return {
        "statusCode": status,
        "message": json.dumps(dict(
            message=message
        ))
    }
```

**`src/worker-function/main.py`**

```python
import json
import logging
import os
import math
import time
from datetime import datetime, timedelta

import boto3
import shopify
from bson.json_util import dumps
from mongo import MongoDB

from helper_utils import get_orders_first_page, get_orders_next_page, UnavaliableShopException

logger = logging.getLogger()
logger.setLevel(logging.INFO)

mongo_ecommerce = MongoDB(os.environ['MONGO_INSTANCE_URL_PRIVATE'], 'ecommerce')

SLEEP_TIME_AFTER_SHOPIFY_REQUEST = 1


def get_shopify_api_version():
    client = boto3.client('ssm')
    response = client.get_parameter(Name='shopify_api_version', WithDecryption=False)
    return response.get('Parameter', {}).get('Value', '')


def handler(event, context):
    logger.info("Processing Event -> {}".format(json.dumps(event)))

    for record in event["Records"]:
        worker_params = json.loads(record["body"])
        logger.info(f"Worker Params Received -> {worker_params}")
        shop_url = worker_params['shop_url']
        created_at_min = worker_params['created_at_min']
        created_at_max = worker_params['created_at_max']
        max_orders_to_process = worker_params['max_orders_to_process']
        api_page_limit = worker_params['api_page_limit']
        status = worker_params['status']
       
        credentials = _get_shop_credentials(shop_url)
        with shopify.Session.temp(**credentials):
            _ingest_missed_orders_for_shop(
                shop_url, created_at_min, created_at_max, max_orders_to_process,
                api_page_limit, status)
            _purge_mongodb_orders_by_existing_ids(shop_url)
            logger.info("All orders successfully injected!")


def _get_shop_credentials(shop_url):
    dynamodb = boto3.resource('dynamodb', region_name=os.environ['AWS_REGION'])
    table = dynamodb.Table(os.environ['STORE_TOKEN_DYNAMO_DB_TABLE'])
    response = table.get_item(Key={'id': shop_url})
    if 'Item' not in response:
        logger.error(f'No credentials for:{shop_url}')
        raise Exception(f"No credentials for:{shop_url}")
    response = response['Item']
    access_token = response.get('access_token', No

…(truncated)…
```

**`stacks/index.js`**

```text
import MyStack from "./MyStack";

export default function main(app) {
    // Set default runtime for all functions
    app.setDefaultFunctionProps({
        srcPath: 'src',
        memorySize: 1024,
        handler: 'lambda.handler',
        runtime: "python3.9",
        tracing: "pass_through",
        timeout: 30,
        permissions: [
            'secretsmanager',
            'sns',
            'ssm',
            'dynamodb',
            'xray'
        ]
    });

    new MyStack(app, 'sst-stack', {prefix: "yofi-backend", name: "shopify-synk"});
}
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`botnet-lambda-scheduled-shopify-sync`** capabilities aligned with **airbyte integrations** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `botnet-lambda-scheduled-shopify-sync`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

# yofi-lambda-arangodb-persistor

**Path:** `D:/botnot/yofi-lambda-arangodb-persistor`  
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
  "name": "yofi-lambda-arangodb-persistor",
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
    "@serverless-stack/cli": "1.4.0",
    "@serverless-stack/resources": "1.4.0",
    "@aws-cdk/aws-lambda-python-alpha": "2.24.0-alpha.0",
    "aws-cdk-lib": "2.24.0",
    "async": ">=2.6.4",
    "jszip": ">=3.7.0"
  }
}
```

### `sst.json`

```
{
  "name": "yofi-lambda-arangodb-persistor",
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
.github
.gitignore
.idea
README.md
cdk.context.json
layer
package.json
seed.yml
src
sst.json
stacks
test
```

## 5. My contribution / role (evidence from git history — if available)

```text
e881648 2023-05-30 add logRetention: "one_year"
26f5c41 2023-05-29 add logRetention: "one_month"
b563b3a 2023-05-23 clean code
5ef474d 2023-05-22 handle all incoming orders not first
cd452b1 2023-05-19 add unique_id for each order
fde24b2 2023-05-19 add events_history db
98f8209 2023-05-19 add events_history db
52b0e27 2023-05-11 add order to geolocation range using polygon and transaction
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`src/connection/main.py`**

```python
import hashlib
import json
import os
import boto3
from arango import ArangoClient
from arango.exceptions import AQLQueryExecuteError
from datetime import datetime, timedelta
import ipaddress
from helpers import *
from collections import deque, defaultdict

secrets_manager = boto3.client('secretsmanager')
secret = secrets_manager.get_secret_value(SecretId="Arango_db_credentials")
secret_json = json.loads(secret["SecretString"])

client = ArangoClient(hosts=os.environ['ARANGO_HOST'] + os.environ['ARANGO_PORT'])
sys_db = client.db('_system', username=secret_json['username'], password=secret_json['password'])


def find_time_range_vertex(created_at, col):
    if created_at:
        created_at_dt = datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S%z')
        fixed_range_start, fixed_range_end = get_fixed_time_range(created_at_dt)

        query = f"""
        FOR time_range IN {col}
            FILTER DATE_TIMESTAMP(time_range.start) <= {int(fixed_range_start.timestamp() * 1000)} AND DATE_TIMESTAMP(time_range.end) > {int(fixed_range_end.timestamp() * 1000)}
            RETURN time_range
        """
        cursor = db.aql.execute(query)
        results = [result for result in cursor]

        if results:
            return results[0]
        else:
            return None
    return None


def create_time_range_vertex(created_at, col, shop):
    if created_at and shop:
        created_at_dt = datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S%z')
        fixed_range_start, fixed_range_end = get_fixed_time_range(created_at_dt)
        overlapping_vertex = find_time_range_vertex(created_at, col)
        if overlapping_vertex is not None:
            return overlapping_vertex

        time_range_key = f"{fixed_range_start.isoformat()}-{fixed_range_end.isoformat()}_{shop}"
        time_range_vertex = upsert_vertex(col, time_range_key, {
            'start': fixed_range_start.isoformat(),
            'end': fixed_range_end.isoformat()
        })

        return time_range_vertex
    return {}


def get_fixed_time_range(dt):
    minute = dt.minute // 10 * 10
    fixed_range_start = dt.replace(minut

…(truncated)…
```

**`stacks/index.js`**

```text
import LambdaStack from './ArangoConnection';
import {Runtime, Tracing} from 'aws-cdk-lib/aws-lambda';
import {Fn, Duration} from 'aws-cdk-lib';

export default function main(app) {
    // Set default runtime for all functions
    app.setDefaultFunctionProps({
        runtime: 'python3.9',
    });

    new LambdaStack(app, 'sst-stack', {prefix: "botnot-backend", name: "yofi-lambda-arangodb-persistor"});
}
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`yofi-lambda-arangodb-persistor`** capabilities aligned with **persistence** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yofi-lambda-arangodb-persistor`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

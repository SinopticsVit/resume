# yofi-lambda-neo4j-clustering

**Path:** `D:/botnot/yofi-lambda-neo4j-clustering`  
**Category:** persistence  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# yofi-lambda-neo4j-clustering

Yofi lambda function for running neo4j cypher queries, primarily for clustering.

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

### `README.md`

```
# yofi-lambda-neo4j-clustering

Yofi lambda function for running neo4j cypher queries, primarily for clustering.
```

### `readme.md`

```
# yofi-lambda-neo4j-clustering

Yofi lambda function for running neo4j cypher queries, primarily for clustering.
```

### `Readme.md`

```
# yofi-lambda-neo4j-clustering

Yofi lambda function for running neo4j cypher queries, primarily for clustering.
```

### `package.json`

```
{
  "name": "yofi-lambda-ml-gateway",
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
  "name": "yofi-lambda-neo4j-clustering",
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
README.md
get_pypi.sh
layer-common
package.json
seed.yml
src
sst.json
stacks
```

## 5. My contribution / role (evidence from git history — if available)

```text
9e44772 2024-02-20 add condition for get node
fbca0bf 2024-02-19 change neo4j credentials
59884c3 2023-11-16 fix: try different aws cdk lib
5ef42a2 2023-11-16 fix: again
8ec48c5 2023-11-16 wip: try fixing imports
36df350 2023-11-16 fix: try adding more stuff
ab060b9 2023-11-16 fix: try to fix dependency
5dbab85 2023-11-16 Merge github.com:BotNotOrg/yofi-lambda-neo4j-clustering into dev
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`src/main.py`**

```python
from neo4j_db import Neo4jDatabase
from secret_manager import get_neo4j_credentials


def lambda_handler(event, context):
    # Get Query from event
    cypher_query = event['query']

    # Handle input query
    if cypher_query is None:
        raise Exception("No query provided")
    else:
        print("Query: " + cypher_query)


    print("Connecting to Neo4j...")
    neo4j_credentials = get_neo4j_credentials()
    neo4j = Neo4jDatabase(neo4j_credentials["host"], neo4j_credentials["username"], neo4j_credentials["password"])
    
    print('Exporting clusters to S3...')
    summary = neo4j.run_query(cypher_query)

    print("Closing connection to Neo4j...")
    neo4j.close()

    return {
        'statusCode': 200,
        'body': f'Query executed successfully. Summary: {summary}'
    }
```

**`stacks/index.js`**

```text
/**
 * Copyright 2023 YoFi Inc., or its associates. All Rights Reserved.
 *
 * Description: Lambda for ML models gateway
 * Author: Eugenio Grytsenko
 **/

import Stack from './Stack';
import { Runtime, Tracing } from 'aws-cdk-lib/aws-lambda';
import { Duration } from 'aws-cdk-lib';

export default function main(app) {
    // Set default runtime for all functions
    app.setDefaultFunctionProps({
        srcPath: 'src',
        runtime: Runtime.PYTHON_3_9,
        tracing: Tracing.DISABLED,
        timeout: Duration.seconds(180)
    });

    new Stack(app, 'sst-stack', {
        prefix: 'yofi-lambda',
        name: 'neo4j-clustering'
    });
}
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`yofi-lambda-neo4j-clustering`** capabilities aligned with **persistence** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yofi-lambda-neo4j-clustering`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

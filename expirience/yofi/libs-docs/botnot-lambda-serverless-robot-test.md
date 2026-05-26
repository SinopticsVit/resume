# botnot-lambda-serverless-robot-test

**Path:** `D:/botnot/botnot-lambda-serverless-robot-test`  
**Category:** libs-docs  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# AWS Lambda for Serverless Robot Framework Test execution
- Author: Yofi Team
- Last updated: 2023-04-19 v1422

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

### `README.md`

```
# AWS Lambda for Serverless Robot Framework Test execution
- Author: Yofi Team
- Last updated: 2023-04-19 v1422
```

### `readme.md`

```
# AWS Lambda for Serverless Robot Framework Test execution
- Author: Yofi Team
- Last updated: 2023-04-19 v1422
```

### `Readme.md`

```
# AWS Lambda for Serverless Robot Framework Test execution
- Author: Yofi Team
- Last updated: 2023-04-19 v1422
```

### `package.json`

```
{
  "engines": {
    "node": ">=18.0.0"
  },
  "name": "yofi-lambda-serverless-robot-test",
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
    "@tsconfig/node16": "1.0.3",
    "typescript": "^4.8.4",
    "sst": "2.41.4",
    "constructs": "10.3.0",
    "@aws-cdk/aws-lambda-python-alpha": "2.132.1-alpha.0",
    "aws-cdk-lib": "2.132.1",
    "ts-node": "^10.9.1",
    "async": ">=2.6.4",
    "jszip": ">=3.8.0"
  }
}
```

### `sst.config.ts`

```
import type {SSTConfig} from "sst"
import {MyStack} from "./stacks/MyStack"

export default {
    config(input) {
        return {
            name: "yofi-robot-e2e-test",
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

        app
            .stack(MyStack, {id: "sst-stack"})
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
.github
.gitignore
.idea
README.md
layer
node_modules
package-lock.json
package.json
pytest.ini
seed.yml
src
sst.config.ts
stacks
test
```

## 5. My contribution / role (evidence from git history — if available)

```text
dadba78 2025-05-06 Fixing tests
4cbfd27 2025-05-06 Fixing tests
7a3d6fa 2025-05-06 Fixing tests
b71f0c8 2025-05-06 Fixing tests
bf280c0 2025-05-06 Fixing tests
4599292 2025-05-06 Fixing tests
6810ad3 2025-05-06 Fixing tests
e0e8578 2025-05-05 Fixing tests
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`stacks/MyStack.ts`**

```typescript
import {Duration, Fn, RemovalPolicy} from "aws-cdk-lib";
import type {StackContext} from "sst/constructs";
import {Cron, Function, Queue, Topic, Bucket} from "sst/constructs";
import * as sns from "aws-cdk-lib/aws-sns";
import {ITopic, Topic as SNSTopic} from "aws-cdk-lib/aws-sns";
import {Vpc} from 'aws-cdk-lib/aws-ec2';
// import {Bucket} from 'aws-cdk-lib/aws-s3';
import {PythonLayerVersion} from '@aws-cdk/aws-lambda-python-alpha';
import {Runtime} from "aws-cdk-lib/aws-lambda";
import * as path from "path";
import {fileURLToPath} from 'url';
import {Effect, PolicyStatement, Role} from 'aws-cdk-lib/aws-iam';
import * as sqs from 'aws-cdk-lib/aws-sqs';
import {RuleTargetInput} from "aws-cdk-lib/aws-events";
import {Construct} from "constructs";
import * as fs from 'fs';
import {createLambdaPythonFunction} from "./Commons";

// Create ES module compatible path references
// @ts-ignore
const currentFilePath = fileURLToPath(import.meta.url);
const currentDir = path.dirname(currentFilePath);

// Resolve layer path - use environment variable from sst.config.ts if set
const layerPath = process.env.LAYER_PATH || path.join(currentDir, '..', 'layer');
console.log('MyStack - Layer path:', layerPath);
console.log('MyStack - Layer exists:', fs.existsSync(layerPath));

// Define interface for queue subscription options
interface QueueSubscriptionOptions {
    timeout?: Duration;
    batchSize?: number;
    maxConcurrency?: number;
    maxBatchingWindow?: Duration;
    maxReceiveCount?: number;
    rawMessageDelivery?: boolean;
}

// Define interface for stack properties extending the standard props
interface MyStackProps {
    prefix: string;
    name: string;
    shop_per_stage: {
        [key: string]: string;
    };
}

/**
 * Creates a queue subscription for a service
 */
const createQueueSubscription = function (
    scope: Construct,
    serviceName: string, 
    topicExportName: string, 
    lambdaFunction: Function, 
    options: QueueSubscriptionOptions
): Topic {
    const {
        timeout = Duration.seconds(40),
        batchSize = 5,
        maxConcurrency = 200,
        maxBatchin

…(truncated)…
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`botnot-lambda-serverless-robot-test`** capabilities aligned with **libs docs** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `botnot-lambda-serverless-robot-test`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

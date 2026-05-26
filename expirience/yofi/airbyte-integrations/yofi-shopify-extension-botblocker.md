# yofi-shopify-extension-botblocker

**Path:** `D:/botnot/yofi-shopify-extension-botblocker`  
**Category:** airbyte-integrations  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# INTRO

This is a lambda to regularly deploying the shopify extension for botblocker
- the botblocker extension code is already included here
  - it means if you want to update the extension, then just update here it the extension
  - to deploy the extension immediately, you need to send a event to the deployer function 
- this deployer-wrapper-lambda will deploy the extension every hour
  - update both the hour file and the encrypt-key file

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

### `README.md`

```
# INTRO

This is a lambda to regularly deploying the shopify extension for botblocker
- the botblocker extension code is already included here
  - it means if you want to update the extension, then just update here it the extension
  - to deploy the extension immediately, you need to send a event to the deployer function 
- this deployer-wrapper-lambda will deploy the extension every hour
  - update both the hour file and the encrypt-key file
```

### `readme.md`

```
# INTRO

This is a lambda to regularly deploying the shopify extension for botblocker
- the botblocker extension code is already included here
  - it means if you want to update the extension, then just update here it the extension
  - to deploy the extension immediately, you need to send a event to the deployer function 
- this deployer-wrapper-lambda will deploy the extension every hour
  - update both the hour file and the encrypt-key file
```

### `Readme.md`

```
# INTRO

This is a lambda to regularly deploying the shopify extension for botblocker
- the botblocker extension code is already included here
  - it means if you want to update the extension, then just update here it the extension
  - to deploy the extension immediately, you need to send a event to the deployer function 
- this deployer-wrapper-lambda will deploy the extension every hour
  - update both the hour file and the encrypt-key file
```

### `package.json`

```
{
  "name": "botnot-backend-lambda-moonsense-webhook-api",
  "version": "1.0.0",
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
    "@serverless-stack/cli": ">=1.18.4 <2.0.0",
    "@serverless-stack/resources": ">=1.18.4 <2.0.0",
    "@aws-cdk/aws-lambda-python-alpha": "^2.50.0-alpha.0",
    "aws-cdk-lib": "^2.50.0",
    "async": ">=2.6.4",
    "jszip": ">=3.7.0"
  }
}
```

### `sst.json`

```
{
  "name": "yofi-backend-lambda-shopify-extension",
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
package.json
pytest.ini
seed.yml
src_extension_deployer
sst.json
stacks
test
```

## 5. My contribution / role (evidence from git history — if available)

```text
fa7c126 2023-08-09 Tracing.DISABLED,
048226b 2023-08-08 remove Tracing
6b5ad6c 2023-08-04 feat: only act as new hour when minute > 50
0ea6f8f 2023-08-04 fix: hour should be 0-23, cannot be 24
60b9776 2023-08-02 fix: decoding text and remove color codes
310b20a 2023-08-02 feat: rollback sh which cannot run in aws: "out of pty devices"
1765f06 2023-08-02 feat: add log check for deployer
a267ec4 2023-07-24 fix: run at the end of hour
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`stacks/index.js`**

```text
import LambdaStack from './MyStack';
import {Runtime, Tracing} from 'aws-cdk-lib/aws-lambda';
import {Fn, Duration} from 'aws-cdk-lib';

export default function main(app) {
    // Set default runtime for all functions
    app.setDefaultFunctionProps({
        runtime: 'python3.9',
    });

    new LambdaStack(app, 'sst-stack', {prefix: "botnot-backend", name: "lambda-moonsense-webhook-api"});
}
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`yofi-shopify-extension-botblocker`** capabilities aligned with **airbyte integrations** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yofi-shopify-extension-botblocker`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

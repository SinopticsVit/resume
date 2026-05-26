# yofi-partner-event-webhook

**Path:** `D:/botnot/yofi-partner-event-webhook`  
**Category:** airbyte-integrations  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# AWS Lambda and API-gateway for partner sending events

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

### `README.md`

```
# AWS Lambda and API-gateway for partner sending events
```

### `readme.md`

```
# AWS Lambda and API-gateway for partner sending events
```

### `Readme.md`

```
# AWS Lambda and API-gateway for partner sending events
```

### `package.json`

```
{
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "test": "sst test",
    "start": "sst start",
    "build": "sst build",
    "deploy": "sst deploy",
    "remove": "sst remove",
    "test:graph_v3": "jest src/customer/graph_v3/main.test.js --testTimeout=120000",
    "test:similarity_v2": "jest src/customer/similarity_v2/main.test.js --testTimeout=120000"
  },
  "eslintConfig": {
    "extends": [
      "serverless-stack"
    ]
  },
  "dependencies": {
    "@aws-cdk/aws-lambda-python-alpha": "2.136.1-alpha.0",
    "aws-cdk-lib": "2.136.1",
    "aws4": "^1.12.0",
    "constructs": "10.3.0",
    "sst": "^2.41.4",
    "ts-node": "^10.9.1",
    "vitest": "^0.24.5"
  }
}
```

### `sst.config.ts`

```
import type { SSTConfig } from 'sst';
import { APIStack } from './stacks/APIStack';

export default {
    config(input) {
        return {
            name: 'yofi-partner-event-webhook',
            region: 'us-east-1',
            profile: input.stage === 'prod' ? 'prod' : 'dev',
        };
    },
    stacks(app) {
        app.setDefaultFunctionProps({
            // handler: 'src/lambda.handler',
            runtime: 'python3.11',
            tracing: "disabled",
            timeout: 30,
            permissions: [
                'secretsmanager:*',
                'dynamodb:*',
                'sns:*',
                'sqs:*',
                'ssm',
                'ec2:*',
                'xray:*',
                'lambda:*',
                'athena:*',
                's3:*',
                'glue:*'
            ]
        })
        app.stack(APIStack);
    },
} satisfies SSTConfig;
```

### `Makefile`

```
#
# Makefile for BotNot.IO / Yofi.AI
#
#include .env
#export $(shell sed 's/=.*//' .env)

all:	stack-deploy
all-prod: stack-deploy-prod

install-deps:
	npm install

stack-build: install-deps
	npm run build -- --stage dev --region us-east-1 --profile dev

stack-test: stack-build
	echo npm run test

stack-deploy: stack-test
	npm run deploy -- --stage dev --region us-east-1 --profile dev

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
	rm -rf src/auth/__pycache__
	rm -rf test/__pycache__
	rm -f cdk.context.json
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
layer_python
package.json
seed.yml
src
sst.config.ts
stacks
```

## 5. My contribution / role (evidence from git history — if available)

```text
4b1cbb2 2025-05-09 Merge pull request #21 from BotNotOrg/feature/redo-fixes
4e7aea8 2025-05-09 feat: Disable as for now because sometime redo needs to send order with deactivated customer
d5e2633 2025-05-09 feat: update status code to be more informative
478f371 2025-05-01 Merge pull request #20 from BotNotOrg/dev
9d4ce54 2025-05-01 refactor: claim now use id instead of claim_id
b624eff 2025-05-01 refactor: change ClaimModel to require id instead of claim_id
8f52d0d 2025-04-29 Merge pull request #19 from BotNotOrg/dev
83fab60 2025-04-29 fix: update POST_PURCHASE_DOWNSTREAM_SQS_URL to a new standard sqs
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets

_No snippet candidates matched (handler.py / stack.ts / template.yaml etc.). Expand manually after opening the repo._

## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`yofi-partner-event-webhook`** capabilities aligned with **airbyte integrations** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yofi-partner-event-webhook`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

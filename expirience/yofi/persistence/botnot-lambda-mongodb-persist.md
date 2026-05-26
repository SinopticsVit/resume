# botnot-lambda-mongodb-persist

**Path:** `D:/botnot/botnot-lambda-mongodb-persist`  
**Category:** persistence  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# Lambda for data persistence to MongoDB

### Run tests
0. Install packages
   `pip install pytest-asyncio httpx pytest-env cryptography pytest-cov`
1. cd to root directory
2. run `pytest -s`  (-s will output print to cli)
    - Run specified test like: `pytest -s test/test_clean_order.py::test_stop_strip_s_from_field_name`

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

### `README.md`

```
# Lambda for data persistence to MongoDB

### Run tests
0. Install packages
   `pip install pytest-asyncio httpx pytest-env cryptography pytest-cov`
1. cd to root directory
2. run `pytest -s`  (-s will output print to cli)
    - Run specified test like: `pytest -s test/test_clean_order.py::test_stop_strip_s_from_field_name`
```

### `readme.md`

```
# Lambda for data persistence to MongoDB

### Run tests
0. Install packages
   `pip install pytest-asyncio httpx pytest-env cryptography pytest-cov`
1. cd to root directory
2. run `pytest -s`  (-s will output print to cli)
    - Run specified test like: `pytest -s test/test_clean_order.py::test_stop_strip_s_from_field_name`
```

### `Readme.md`

```
# Lambda for data persistence to MongoDB

### Run tests
0. Install packages
   `pip install pytest-asyncio httpx pytest-env cryptography pytest-cov`
1. cd to root directory
2. run `pytest -s`  (-s will output print to cli)
    - Run specified test like: `pytest -s test/test_clean_order.py::test_stop_strip_s_from_field_name`
```

### `package.json`

```
{
  "name": "mongodb-persist",
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
import {OrderCheckoutPersistStack} from "./stacks/MainStack"

export default {
    config(input) {
        return {
            name: "yofi-mongodb-persist-service",
            region: "us-east-1",
            profile: input.stage === "prod" ? "prod" : "dev",
        }
    },
    stacks(app) {
        app.setDefaultFunctionProps({
            runtime: 'python3.9',
            tracing: "disabled",
            timeout: 90
        })

        app
            .stack(OrderCheckoutPersistStack, {id: "sst-stack"})
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
.vscode
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
```

## 5. My contribution / role (evidence from git history — if available)

```text
5501d14 2025-06-22 add partner_order_id
bd8021b 2025-06-06 fix: app_id
b05eb31 2025-06-06 fix: partner_id (#90)
d63ad3e 2025-06-06 Merge branch 'dev' of github.com:BotNotOrg/botnot-lambda-mongodb-persist into dev
7be5046 2025-06-06 Feature/add (#88)
b58cb25 2025-06-06 Merge branch 'main' into dev
968f154 2025-06-06 Feature/yofi 569 add org id app id partner id to returns/claim/fullfillment tables (#86)
166a64c 2025-05-16 Merge pull request #84 from BotNotOrg/dev
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets

_No snippet candidates matched (handler.py / stack.ts / template.yaml etc.). Expand manually after opening the repo._

## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`botnot-lambda-mongodb-persist`** capabilities aligned with **persistence** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `botnot-lambda-mongodb-persist`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

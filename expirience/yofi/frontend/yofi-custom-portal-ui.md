# yofi-custom-portal-ui

**Path:** `D:/botnot/yofi-custom-portal-ui`  
**Category:** frontend  
**Primary language:** JavaScript  
**Status:** present on disk

## 1. Purpose (2-3 lines)



## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** JavaScript
- **Top-level layout:** see listing below.

### `README.md`

```
## Getting started

### Requirements

1. You must [download and install Node.js](https://nodejs.org/en/download/) if you don't already have it.
2. You must [create a Shopify partner account](https://partners.shopify.com/signup) if you don’t have one.
3. You must [create a development store](https://help.shopify.com/en/partners/dashboard/development-stores#create-a-development-store) if you don’t have one.


### local develop

in the local evn to develop some feature you just need get a token to use it in the 'frontend/src/utils/interceptor.js'
just replace the local test token, and the run like this

Using yarn:

```shell
cd frontend
yarn run test
```

#### get test token
1、you need have a AWS account and been invited to our group
2、visit this page and click test button to get the token : https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/functions/dev-bootnot-admin-api-sst-devbootnotadminapitokeng-Usu556CmAH1X?tab=testing


## Deployment

### dev deploy

```shell
make stack-deploy
```

also you can change the apiKey and apiSecret in 'stacks/MyStack.js' to test the app in your shopily store


# Start Pre-Prod
Before you start, need to have below items intalled:
1. [Nodejs](https://nodejs.org/en)
2. [Git bash](https://git-scm.com/) and [setup your SSH key](https://github.com/settings/keys)
3. [Visual Studio Code](https://code.visualstudio.com/) or any other IDEs
   
### Steps
1. Clone the source code of this repo (please skip this step if you have cloned it)
2. Check out `dev` branch and pull the latest changes.
3. Login aws account for `production`.
4. Search `apitoken` in the Lambda functions and go to the `Test` tab in the function or open this [link](https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/functions/prod-bootnot-admin-api-ss-prodbootnotadminapitoken-vzhaP8gV06hC?tab=testing) directly
5. In the `Event JSON`, enter a content like below, make sure the `shop_url` is the shop you want to test.

```javascript
{
  "shop_url": "https://stashedsf.myshopify.com"
}
```
6. Click on the `Test` button and wait a while, and then copy the token(without `token:`) in the testing log output.
```
token:some-token-here
```
7. Replace the value of `VITE_TEST_TOKEN` in `frontend/.env.pre-prod` with the copid token, then save.
8. Run below command to start serving the portal
```
cd frontend
npm run pre-prod
```
the URL will be shown in the console.
```

### `readme.md`

```
## Getting started

### Requirements

1. You must [download and install Node.js](https://nodejs.org/en/download/) if you don't already have it.
2. You must [create a Shopify partner account](https://partners.shopify.com/signup) if you don’t have one.
3. You must [create a development store](https://help.shopify.com/en/partners/dashboard/development-stores#create-a-development-store) if you don’t have one.


### local develop

in the local evn to develop some feature you just need get a token to use it in the 'frontend/src/utils/interceptor.js'
just replace the local test token, and the run like this

Using yarn:

```shell
cd frontend
yarn run test
```

#### get test token
1、you need have a AWS account and been invited to our group
2、visit this page and click test button to get the token : https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/functions/dev-bootnot-admin-api-sst-devbootnotadminapitokeng-Usu556CmAH1X?tab=testing


## Deployment

### dev deploy

```shell
make stack-deploy
```

also you can change the apiKey and apiSecret in 'stacks/MyStack.js' to test the app in your shopily store


# Start Pre-Prod
Before you start, need to have below items intalled:
1. [Nodejs](https://nodejs.org/en)
2. [Git bash](https://git-scm.com/) and [setup your SSH key](https://github.com/settings/keys)
3. [Visual Studio Code](https://code.visualstudio.com/) or any other IDEs
   
### Steps
1. Clone the source code of this repo (please skip this step if you have cloned it)
2. Check out `dev` branch and pull the latest changes.
3. Login aws account for `production`.
4. Search `apitoken` in the Lambda functions and go to the `Test` tab in the function or open this [link](https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/functions/prod-bootnot-admin-api-ss-prodbootnotadminapitoken-vzhaP8gV06hC?tab=testing) directly
5. In the `Event JSON`, enter a content like below, make sure the `shop_url` is the shop you want to test.

```javascript
{
  "shop_url": "https://stashedsf.myshopify.com"
}
```
6. Click on the `Test` button and wait a while, and then copy the token(without `token:`) in the testing log output.
```
token:some-token-here
```
7. Replace the value of `VITE_TEST_TOKEN` in `frontend/.env.pre-prod` with the copid token, then save.
8. Run below command to start serving the portal
```
cd frontend
npm run pre-prod
```
the URL will be shown in the console.
```

### `Readme.md`

```
## Getting started

### Requirements

1. You must [download and install Node.js](https://nodejs.org/en/download/) if you don't already have it.
2. You must [create a Shopify partner account](https://partners.shopify.com/signup) if you don’t have one.
3. You must [create a development store](https://help.shopify.com/en/partners/dashboard/development-stores#create-a-development-store) if you don’t have one.


### local develop

in the local evn to develop some feature you just need get a token to use it in the 'frontend/src/utils/interceptor.js'
just replace the local test token, and the run like this

Using yarn:

```shell
cd frontend
yarn run test
```

#### get test token
1、you need have a AWS account and been invited to our group
2、visit this page and click test button to get the token : https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/functions/dev-bootnot-admin-api-sst-devbootnotadminapitokeng-Usu556CmAH1X?tab=testing


## Deployment

### dev deploy

```shell
make stack-deploy
```

also you can change the apiKey and apiSecret in 'stacks/MyStack.js' to test the app in your shopily store


# Start Pre-Prod
Before you start, need to have below items intalled:
1. [Nodejs](https://nodejs.org/en)
2. [Git bash](https://git-scm.com/) and [setup your SSH key](https://github.com/settings/keys)
3. [Visual Studio Code](https://code.visualstudio.com/) or any other IDEs
   
### Steps
1. Clone the source code of this repo (please skip this step if you have cloned it)
2. Check out `dev` branch and pull the latest changes.
3. Login aws account for `production`.
4. Search `apitoken` in the Lambda functions and go to the `Test` tab in the function or open this [link](https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/functions/prod-bootnot-admin-api-ss-prodbootnotadminapitoken-vzhaP8gV06hC?tab=testing) directly
5. In the `Event JSON`, enter a content like below, make sure the `shop_url` is the shop you want to test.

```javascript
{
  "shop_url": "https://stashedsf.myshopify.com"
}
```
6. Click on the `Test` button and wait a while, and then copy the token(without `token:`) in the testing log output.
```
token:some-token-here
```
7. Replace the value of `VITE_TEST_TOKEN` in `frontend/.env.pre-prod` with the copid token, then save.
8. Run below command to start serving the portal
```
cd frontend
npm run pre-prod
```
the URL will be shown in the console.
```

### `package.json`

```
{
  "name": "botnot-frontend-vue-portal",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "start": "sst start",
    "build": "sst build",
    "deploy": "sst deploy",
    "remove": "sst remove",
    "console": "sst console",
    "typecheck": "tsc --noEmit",
    "test": "vitest run"
  },
  "devDependencies": {
    "aws-cdk-lib": "^2.100.0",
    "@serverless-stack/cli": "^1.18.4",
    "@serverless-stack/resources": "^1.18.4",
    "vitest": "^0.24.5"
  },
  "workspaces": [
    "frontend"
  ]
}
```

### `sst.json`

```
{
  "name": "botnot-frontend-vue-portal",
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

stack-build:
	npm run build -- --stage dev --region us-east-1

stack-test: stack-build
	npm run test

stack-deploy: install-deps
	npm run deploy -- --stage dev --region us-east-1

stack-build-prod: install-deps
	npm run build -- --stage prod --region us-east-1

stack-test-prod: stack-build-prod
	npm run test

stack-deploy-prod: install-deps
	npm run deploy -- --stage prod --region us-east-1

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
.github
.gitignore
Makefile
README.md
cloudfront
frontend
lambda-install-finish
layers
package.json
sst.json
stacks
```

## 5. My contribution / role (evidence from git history — if available)

```text
0d1482f 2024-07-15 Merge pull request #1 from BotNotOrg/dependabot/pip/layers/install-start-layer/requests-2.32.0
e7a64ba 2024-05-21 --- updated-dependencies: - dependency-name: requests   dependency-type: direct:production ...
f135a5e 2024-04-10 Merge pull request #253 from BotNotOrg/dev
cce09c1 2024-04-10 Add time range to customer impact chart (#260)
982d274 2024-04-09 update style
42fa5a4 2024-04-09 Timezone (#258)
5e18db7 2024-04-09 hide show all shops (#259)
3cc9a31 2024-04-07 add alert
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`frontend/src/api/index.js`**

```text
import request from '@/utils/request';
import constants from '@/utils/constants';

let url = {
    shopifyDataImportState: '/shopify/data_import_state',
    shopifyInstalltionFinish: '/installation/finish',
    dashboard: '/ecommerce/dashboard',
    dashboardLossChart: '/ecommerce/dashboard/loss-chart',
    customersList: '/ecommerce/customers/list',
    customersProfileState: '/ecommerce/customers/profile-stat',
    customersStatistics: '/ecommerce/customers/statistics/list',
    customersSegments: '/ecommerce/customers/segments',
    customersGraph: '/ecommerce/customers/graph-v2',
    customersGraphV3: '/ecommerce/customers/graph-v3',
    customersDetails: '/ecommerce/customers/details',
    customersSimilarity: '/ecommerce/customers/similarity-v2',
    graphDetails: '/ecommerce/graph-v2/details',
    productsList: '/ecommerce/products/list',
    productNameList: '/botblock/products/query',
    ordersList: '/ecommerce/orders/list',
    ordersCancel: '/ecommerce/orders/cancel',
    ordersDetails: '/ecommerce/orders/details',
    raffleList: '/ecommerce/raffles/list',
    raffleDetails: '/ecommerce/raffles/details',
    raffleStatistics: '/ecommerce/raffles/statistics',
    raffleParticipations: '/ecommerce/raffle_participations/list',
    billingList: '/billing/tier/list',
    billingEdit: '/billing/details/edit',
    billingDetailsGet: '/billing/details/get',
    billingCreate: '/billing/app_subscriptions/create',
    preventionList: '/botblock/config_items/list',
    preventionCreate: '/botblock/config_items/create',
    preventionEdit: '/botblock/config_items/edit',
    preventionSwitch: '/botblock/config_items/switch',
    preventionDel: '/botblock/config_items/delete',
    preventionDetailCheckoutList: '/ecommerce/checkout/list',
    preventionDetailOrderBlockList: '/ecommerce/order_protected/list',
    preventionDetailCheckoutAggr: '/ecommerce/checkout/aggr',
    preventionDetailOrderBlockAggr: '/ecommerce/order_protected/aggr',
    profitList: '/ecommerce/klaviyo/campaign/list',
    profitDetail: '/ecommerce/klaviyo/campaign/detail',
    shopifyStoreList: '/portal/installed-shops',
};

expo

…(truncated)…
```

**`frontend/src/components/CustomerDetail/index.js`**

```text
export { default as CustomerDetail } from './index.vue';
```

**`frontend/src/components/CustomerGraph/index.js`**

```text
export * from './entity';
export * from './render';
export { default as CustomerGraph } from './customer-graph.vue';
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`yofi-custom-portal-ui`** capabilities aligned with **frontend** delivery.
- Applied **JavaScript** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yofi-custom-portal-ui`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

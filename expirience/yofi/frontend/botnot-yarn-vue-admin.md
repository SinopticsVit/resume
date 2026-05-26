# botnot-yarn-vue-admin

**Path:** `D:/botnot/botnot-yarn-vue-admin`  
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
    "aws-cdk-lib": "2.39.1",
    "@serverless-stack/cli": "^1.16.1",
    "@serverless-stack/resources": "^1.16.1",
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
.idea
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
37df3c8 2023-04-27 Merge remote-tracking branch 'origin/dev'
4368831 2023-04-27 modify the reason value for backend
fcb17dc 2023-04-27 add input value check and modify reason select value
2a6b44b 2023-04-27 Merge remote-tracking branch 'origin/dev'
4d287a7 2023-04-27 modify the order list default sort by
b1555c5 2023-04-27 Merge remote-tracking branch 'origin/dev'
d6fd13a 2023-04-27 show the order id in customer table
3ace997 2023-04-27 Merge remote-tracking branch 'origin/dev'
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`frontend/src/api/index.js`**

```text
import request from '@/utils/request'

let url = {
  shopifyDataImportState: '/shopify/data_import_state',
  shopifyInstalltionFinish: '/installation/finish',

  dashboard: '/ecommerce/dashboard',
  customersList: '/ecommerce/customers/list',
  customersSegments: '/ecommerce/customers/segments',
  customersGraph: '/ecommerce/customers/graph',
  customersDetails: '/ecommerce/customers/details',
  productsList: '/ecommerce/products/list',
  ordersList: '/ecommerce/orders/list',
  ordersCancel: '/ecommerce/orders/cancel',
  ordersDetails: '/ecommerce/orders/details',
  raffleList: '/ecommerce/raffles/list',
  raffleDetails:'/ecommerce/raffles/details',
  raffleStatistics:'/ecommerce/raffles/statistics',
  raffleParticipations:'/ecommerce/raffle_participations/list',
  billingList: '/billing/tier/list',
  billingEdit: '/billing/details/edit',
  billingDetailsGet: '/billing/details/get',
  billingCreate: '/billing/app_subscriptions/create',
}

export default {
  shopifyDataImportState(data, options) {
    return request.get(url.shopifyDataImportState, data, options)
  },
  shopifyInstalltionFinish(data, options) {
    return request.get(url.shopifyInstalltionFinish, data, options)
  },
  dashboard(data, options) {
    return request.post(url.dashboard, data, options)
  },
  customersList(data, options) {
    return request.post(url.customersList, data, options)
  },
  customersSegments(data) {
    return request.post(url.customersSegments, data)
  },
  customersGraph(data) {
    return request.post(url.customersGraph, data)
  },
  customersDetails(data) {
    return request.post(url.customersDetails, data)
  },
  productsList(data,options) {
    return request.post(url.productsList, data,options)
  },
  ordersList(data, options) {
    return request.post(url.ordersList, data, options)
  },
  ordersCancel(data) {
    return request.post(url.ordersCancel, data)
  },
  ordersDetails(data) {
    return request.post(url.ordersDetails, data)
  },
  raffleList(data) {
    return request.post(url.raffleList, data)
  },
  raffleDetails(data) {
    return request.post(url.raffleDetails, data)
 

…(truncated)…
```

**`frontend/src/router/index.js`**

```text
import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(), // hash模式：createWebHashHistory，history模式：createWebHistory
  routes: [
    {
        path: "/",
        redirect: "/dashboard",
        isHide: true,
    },
    {
        path: "/dashboard",
        name: "dashboard",
        title: "Dashboard",
        icon: "Menu",
        isHide: false,
        component: () => import("../views/dashboard/index.vue"),
    },
    {
      path: "/onboard",
      title: "Onboard",
      isHide: true,
      component: () => import("../views/onboard.vue"),
      beforeEnter: function (to, from, next) {
        //do some thing
        next()
      }
    },
    {
      path: "/customers",
      name: "customers",
      title: "Customers",
      icon: "UserFilled",
      isHide: false,
      component: () => import("../views/customers/index.vue"),
    },
    {
      path: "/customers/customersDetail",
      name: "customerDetail",
      title: "customerDetail",
      icon: "Tickets",
      isHide: true,
      component: () => import("../views/customers/detail.vue"),
    },
	  {
		  path: "/customers/customersDetail2",
		  name: "customerDetail2",
		  title: "customerDetail2",
		  icon: "Tickets",
		  isHide: true,
		  component: () => import("../views/customers/detail_newfeature.vue"),
	  },
    {
      path: "/orders",
      name: "orders",
      title: "Orders",
      icon: "Tickets",
      isHide: false,
      component: () => import("../views/orders/index.vue"),
    },
    {
      path: "/orders/ordersDetail",
      name: "ordersDetail",
      title: "ordersDetail",
      icon: "Tickets",
      isHide: true,
      component: () => import("../views/orders/detail.vue"),
    },
    {
      path: "/raffle",
      name: "raffle",
      title: "Raffle",
      icon: "Film",
      isHide: true,
      component: () => import("../views/raffle/index.vue"),
    },
	  {
		  path: "/raffles",
		  name: "raffles",
		  title: "Raffle",
		  icon: "Aim",
		  isHide: true,
		  component: () => import("../views/raffle/index_newfun

…(truncated)…
```

**`frontend/src/store/index.js`**

```text
import { defineStore } from 'pinia'
export const userStore = defineStore('user', {
    state: () => {
        return {
            count: 1,
            arr: [],
            appInstalled:false,
            appDataImported:true
        }
    },
    getters: {

    },
    actions: {  }
})
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`botnot-yarn-vue-admin`** capabilities aligned with **frontend** delivery.
- Applied **JavaScript** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `botnot-yarn-vue-admin`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

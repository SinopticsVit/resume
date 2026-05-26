# botnot-frontend-svelte-portal

**Path:** `D:/botnot/botnot-frontend-svelte-portal`  
**Category:** frontend  
**Primary language:** JavaScript  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# BotNot SvelteKit Frontend Webapp (SST)

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** JavaScript
- **Top-level layout:** see listing below.

### `README.md`

```
# BotNot SvelteKit Frontend Webapp (SST)

## Setup
```bash
git clone ....
npm ci
cd frontend/
npm ci
npm run dev -- --open
```

(note: use `npm ci` rather than `npm i` where possible to ensure that we respect `package-lock.json` files)

## Local Development
There are 2 options to develop locally with this app: tunneled (ie: available to the World Wide Web) and local (ie: available only on localhost).
Generally speaking, we want to run the app **tunneled** so that we can embed directly in to Shopify. This is wonderfully easy with Ngrok!
### Create an ngrok account
(editors' note: we may have a pro subscription soon - so don't pay for it yourself!)

Sign up at https://ngrok.com/ and copy your auth token
```bash
npm i -g ngrok
ngrok config add-authtoken <YOUR AUTH TOKEN>
```

### Set up the tunnel
```bash
node dev.js
```
That's literally it. The `dev.js` script will set up a local Vite server (just like the `vite dev` command) and then expose it to Ngrok.
You'll get a message in your terminal like:
```
Ngrok tunnel available @ https://subdomain.ngrok.io
  > Local: http://localhost:3000/
  > Network: use `--host` to expose
```

You can now visit the Ngrok tunnel to show a public facing version of your local environment!

### Testing with Playwright
Playwright lets us run end-to-end tests locally - and pretty damn fast, too. You'll need some set up, however:
```bash
npx playwright install
npx playwright install-deps
npm run test:e2e
```

## Architecture
Deployed to SST as a SvelteKit site
```

### `readme.md`

```
# BotNot SvelteKit Frontend Webapp (SST)

## Setup
```bash
git clone ....
npm ci
cd frontend/
npm ci
npm run dev -- --open
```

(note: use `npm ci` rather than `npm i` where possible to ensure that we respect `package-lock.json` files)

## Local Development
There are 2 options to develop locally with this app: tunneled (ie: available to the World Wide Web) and local (ie: available only on localhost).
Generally speaking, we want to run the app **tunneled** so that we can embed directly in to Shopify. This is wonderfully easy with Ngrok!
### Create an ngrok account
(editors' note: we may have a pro subscription soon - so don't pay for it yourself!)

Sign up at https://ngrok.com/ and copy your auth token
```bash
npm i -g ngrok
ngrok config add-authtoken <YOUR AUTH TOKEN>
```

### Set up the tunnel
```bash
node dev.js
```
That's literally it. The `dev.js` script will set up a local Vite server (just like the `vite dev` command) and then expose it to Ngrok.
You'll get a message in your terminal like:
```
Ngrok tunnel available @ https://subdomain.ngrok.io
  > Local: http://localhost:3000/
  > Network: use `--host` to expose
```

You can now visit the Ngrok tunnel to show a public facing version of your local environment!

### Testing with Playwright
Playwright lets us run end-to-end tests locally - and pretty damn fast, too. You'll need some set up, however:
```bash
npx playwright install
npx playwright install-deps
npm run test:e2e
```

## Architecture
Deployed to SST as a SvelteKit site
```

### `Readme.md`

```
# BotNot SvelteKit Frontend Webapp (SST)

## Setup
```bash
git clone ....
npm ci
cd frontend/
npm ci
npm run dev -- --open
```

(note: use `npm ci` rather than `npm i` where possible to ensure that we respect `package-lock.json` files)

## Local Development
There are 2 options to develop locally with this app: tunneled (ie: available to the World Wide Web) and local (ie: available only on localhost).
Generally speaking, we want to run the app **tunneled** so that we can embed directly in to Shopify. This is wonderfully easy with Ngrok!
### Create an ngrok account
(editors' note: we may have a pro subscription soon - so don't pay for it yourself!)

Sign up at https://ngrok.com/ and copy your auth token
```bash
npm i -g ngrok
ngrok config add-authtoken <YOUR AUTH TOKEN>
```

### Set up the tunnel
```bash
node dev.js
```
That's literally it. The `dev.js` script will set up a local Vite server (just like the `vite dev` command) and then expose it to Ngrok.
You'll get a message in your terminal like:
```
Ngrok tunnel available @ https://subdomain.ngrok.io
  > Local: http://localhost:3000/
  > Network: use `--host` to expose
```

You can now visit the Ngrok tunnel to show a public facing version of your local environment!

### Testing with Playwright
Playwright lets us run end-to-end tests locally - and pretty damn fast, too. You'll need some set up, however:
```bash
npx playwright install
npx playwright install-deps
npm run test:e2e
```

## Architecture
Deployed to SST as a SvelteKit site
```

### `package.json`

```
{
  "name": "botnot-frontend-svelte-portal",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "start": "sst start",
    "build": "sst build",
    "deploy": "sst deploy",
    "remove": "sst remove",
    "console": "sst console",
    "typecheck": "tsc --noEmit",
    "test": "vitest run",
    "preinstall": "echo '=================>>>>' && node -v "
  },
  "devDependencies": {
    "aws-cdk-lib": "2.24.0",
    "@serverless-stack/cli": "^1.2.35",
    "@serverless-stack/resources": "^1.2.35",
    "vitest": "^0.16.0"
  },
  "workspaces": [
    "services",
    "frontend"
  ]
}
```

### `sst.json`

```
{
  "name": "botnot-frontend-svelte-portal",
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

stack-deploy: stack-build
	npm run deploy -- --stage dev --region us-east-1

stack-build-prod: install-deps
	npm run build -- --stage prod --region us-east-1

stack-test-prod: stack-build-prod
	npm run test

stack-deploy-prod: stack-build-prod
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
package-lock.json
package.json
sst.json
stacks
```

## 5. My contribution / role (evidence from git history — if available)

```text
b2486ca 2022-10-13 feat: add write_script_tags to app permission scope
1b6f5f8 2022-10-11 Adding some padding to the main container to stop the helpscout button from overlapping
fb02ed3 2022-10-04 Removing work in progress functionality to merge for production
0f8eb56 2022-10-04 Revert "minor changes"
fcf28ef 2022-10-04 minor changes
359c3d0 2022-10-03 changes for details page
8efe21f 2022-10-03 changes for details page
0dfc577 2022-09-22 Small changes to stat cards & currency renderers to fix some bugs in individual customer page
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`stacks/index.js`**

```text
import MyStack from "./MyStack";
import { Runtime } from 'aws-cdk-lib/aws-lambda';

export default function main(app) {
    // Set default runtime for all functions
    // app.setDefaultFunctionProps({
    //     runtime: "nodejs16.x",
    // });

    // Define sst-stack
    new MyStack(app, "sst-stack", { prefix: "botnot-frontend", name: "svelte-portal" });
}
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`botnot-frontend-svelte-portal`** capabilities aligned with **frontend** delivery.
- Applied **JavaScript** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `botnot-frontend-svelte-portal`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

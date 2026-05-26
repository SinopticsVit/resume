# yofi-embed-portal-ui

**Path:** `D:/botnot/yofi-embed-portal-ui`  
**Category:** frontend  
**Primary language:** JavaScript  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# Yofi Embeddable UI

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** JavaScript
- **Top-level layout:** see listing below.

### `README.md`

```
# Yofi Embeddable UI

## Quick Start

### 1. Embed with iframe

To embed the Yofi UI into your website, use the following code snippet:

```jsx
<iframe
    ref={iframeRef}
    title="portal"
    src="THE-EMBED-URL"
    style={{ border: 'none', width: '100%', height: '100%' }}
></iframe>
```

### 2. Send events to the iframe

You can send messages to the iframe using `postMessage`. Here is an example:

```js
const message = {
    type: "EVENT_TYPE",
    data: "YOUR_DATA"
};
iframeRef.current.contentWindow.postMessage(message, 'THE-EMBED-ORIGIN');
```

#### Supported Messages

| Event                | Message Sample                                                                                |
| -------------------- | --------------------------------------------------------------------------------------------- |
| Show customer detail | `{ type: 'SHOW_CUSTOMER_DETAIL', data: { id: 'CUSTOMER-ID', token: 'JWT-TOKEN(OPTIONAL)' } }` |
| Show order detail    | `{ type: 'SHOW_ORDER_DETAIL', data: { id: 'ORDER-ID', token: 'JWT-TOKEN(OPTIONAL)' } }`       |
| Set auth token       | `{ type: 'SET_TOKEN', data: 'JWT-TOKEN' }`                                                    |
| Reload page          | `{ type: 'RELOAD' }`                                                                          |

### 3. Listen to events from the iframe in your app

The iframe may send messages back to your application. For instance, it might send a `TOKEN_REFRESH` event if the token expires. Here's how you can listen for messages from the iframe:

```js
window.addEventListener('message', (event) => {
    // Ensure the message is coming from the trusted origin
    if (event.origin !== "THE-EMBED-ORIGIN") {
        return;
    }

    if (event.data.type === 'TOKEN_REFRESH') {
        // Handle the token refresh logic here, e.g., send a new token
        const newTokenMessage = {
            type: 'SET_TOKEN',
            data: 'NEW_JWT_TOKEN'
        };
        iframeRef.current.contentWindow.postMessage(newTokenMessage, event.origin);
    }
});
```

## React Sample

Here is a complete example of how you might integrate this into a React component:

```jsx
import { useEffect, useRef } from 'react';

export default function ReactSample() {
    const urlOrigin = 'https://embed.botnot.io';
    const iframeRef = useRef(null);
    const token = 'YOUR_JWT_TOKEN';
    const customerId = '7701204009245';

    const postMessageToIframe = (message) => {
        if (iframeRef.current && iframeRef.current.contentWindow) {
            // Post the message to the iframe
            iframeRef.current.contentWindow.postMessage(message, urlOrigin);
        }
    };

    const sendToken = () => {
        postMessageToIframe({
            type: 'SET_TOKEN',
            data: token,
        });
    };

    const showCustomerDetail = (id) => {
        postMessageToIframe({
            type: 'SHOW_CUSTOMER_DETAIL',
            data: { id },
        });
    };

    const handleIframeMessage = (event) => {
        // Ensure the message is coming from Yofi origin
        if (event.

…(truncated)…
```

### `readme.md`

```
# Yofi Embeddable UI

## Quick Start

### 1. Embed with iframe

To embed the Yofi UI into your website, use the following code snippet:

```jsx
<iframe
    ref={iframeRef}
    title="portal"
    src="THE-EMBED-URL"
    style={{ border: 'none', width: '100%', height: '100%' }}
></iframe>
```

### 2. Send events to the iframe

You can send messages to the iframe using `postMessage`. Here is an example:

```js
const message = {
    type: "EVENT_TYPE",
    data: "YOUR_DATA"
};
iframeRef.current.contentWindow.postMessage(message, 'THE-EMBED-ORIGIN');
```

#### Supported Messages

| Event                | Message Sample                                                                                |
| -------------------- | --------------------------------------------------------------------------------------------- |
| Show customer detail | `{ type: 'SHOW_CUSTOMER_DETAIL', data: { id: 'CUSTOMER-ID', token: 'JWT-TOKEN(OPTIONAL)' } }` |
| Show order detail    | `{ type: 'SHOW_ORDER_DETAIL', data: { id: 'ORDER-ID', token: 'JWT-TOKEN(OPTIONAL)' } }`       |
| Set auth token       | `{ type: 'SET_TOKEN', data: 'JWT-TOKEN' }`                                                    |
| Reload page          | `{ type: 'RELOAD' }`                                                                          |

### 3. Listen to events from the iframe in your app

The iframe may send messages back to your application. For instance, it might send a `TOKEN_REFRESH` event if the token expires. Here's how you can listen for messages from the iframe:

```js
window.addEventListener('message', (event) => {
    // Ensure the message is coming from the trusted origin
    if (event.origin !== "THE-EMBED-ORIGIN") {
        return;
    }

    if (event.data.type === 'TOKEN_REFRESH') {
        // Handle the token refresh logic here, e.g., send a new token
        const newTokenMessage = {
            type: 'SET_TOKEN',
            data: 'NEW_JWT_TOKEN'
        };
        iframeRef.current.contentWindow.postMessage(newTokenMessage, event.origin);
    }
});
```

## React Sample

Here is a complete example of how you might integrate this into a React component:

```jsx
import { useEffect, useRef } from 'react';

export default function ReactSample() {
    const urlOrigin = 'https://embed.botnot.io';
    const iframeRef = useRef(null);
    const token = 'YOUR_JWT_TOKEN';
    const customerId = '7701204009245';

    const postMessageToIframe = (message) => {
        if (iframeRef.current && iframeRef.current.contentWindow) {
            // Post the message to the iframe
            iframeRef.current.contentWindow.postMessage(message, urlOrigin);
        }
    };

    const sendToken = () => {
        postMessageToIframe({
            type: 'SET_TOKEN',
            data: token,
        });
    };

    const showCustomerDetail = (id) => {
        postMessageToIframe({
            type: 'SHOW_CUSTOMER_DETAIL',
            data: { id },
        });
    };

    const handleIframeMessage = (event) => {
        // Ensure the message is coming from Yofi origin
        if (event.

…(truncated)…
```

### `Readme.md`

```
# Yofi Embeddable UI

## Quick Start

### 1. Embed with iframe

To embed the Yofi UI into your website, use the following code snippet:

```jsx
<iframe
    ref={iframeRef}
    title="portal"
    src="THE-EMBED-URL"
    style={{ border: 'none', width: '100%', height: '100%' }}
></iframe>
```

### 2. Send events to the iframe

You can send messages to the iframe using `postMessage`. Here is an example:

```js
const message = {
    type: "EVENT_TYPE",
    data: "YOUR_DATA"
};
iframeRef.current.contentWindow.postMessage(message, 'THE-EMBED-ORIGIN');
```

#### Supported Messages

| Event                | Message Sample                                                                                |
| -------------------- | --------------------------------------------------------------------------------------------- |
| Show customer detail | `{ type: 'SHOW_CUSTOMER_DETAIL', data: { id: 'CUSTOMER-ID', token: 'JWT-TOKEN(OPTIONAL)' } }` |
| Show order detail    | `{ type: 'SHOW_ORDER_DETAIL', data: { id: 'ORDER-ID', token: 'JWT-TOKEN(OPTIONAL)' } }`       |
| Set auth token       | `{ type: 'SET_TOKEN', data: 'JWT-TOKEN' }`                                                    |
| Reload page          | `{ type: 'RELOAD' }`                                                                          |

### 3. Listen to events from the iframe in your app

The iframe may send messages back to your application. For instance, it might send a `TOKEN_REFRESH` event if the token expires. Here's how you can listen for messages from the iframe:

```js
window.addEventListener('message', (event) => {
    // Ensure the message is coming from the trusted origin
    if (event.origin !== "THE-EMBED-ORIGIN") {
        return;
    }

    if (event.data.type === 'TOKEN_REFRESH') {
        // Handle the token refresh logic here, e.g., send a new token
        const newTokenMessage = {
            type: 'SET_TOKEN',
            data: 'NEW_JWT_TOKEN'
        };
        iframeRef.current.contentWindow.postMessage(newTokenMessage, event.origin);
    }
});
```

## React Sample

Here is a complete example of how you might integrate this into a React component:

```jsx
import { useEffect, useRef } from 'react';

export default function ReactSample() {
    const urlOrigin = 'https://embed.botnot.io';
    const iframeRef = useRef(null);
    const token = 'YOUR_JWT_TOKEN';
    const customerId = '7701204009245';

    const postMessageToIframe = (message) => {
        if (iframeRef.current && iframeRef.current.contentWindow) {
            // Post the message to the iframe
            iframeRef.current.contentWindow.postMessage(message, urlOrigin);
        }
    };

    const sendToken = () => {
        postMessageToIframe({
            type: 'SET_TOKEN',
            data: token,
        });
    };

    const showCustomerDetail = (id) => {
        postMessageToIframe({
            type: 'SHOW_CUSTOMER_DETAIL',
            data: { id },
        });
    };

    const handleIframeMessage = (event) => {
        // Ensure the message is coming from Yofi origin
        if (event.

…(truncated)…
```

### `package.json`

```
{
  "name": "yofi-embed-portal-ui",
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
    "sst": "2.41.2",
    "aws-cdk-lib": "2.132.1",
    "constructs": "10.3.0",
    "ts-node": "^10.9.1",
    "vitest": "^3.0.7"
  },
  "workspaces": [
    "frontend"
  ]
}
```

### `sst.config.ts`

```
import type { SSTConfig } from 'sst';
import { PortalStack } from './stacks/PortalStack';

export default {
    config(input) {
        return {
            name: 'botnot-frontend-embed-portal-ui',
            region: 'us-east-1',
            profile: input.stage === 'prod' ? 'prod' : 'dev',
        };
    },
    stacks(app) {
        app.stack(PortalStack);
    },
} satisfies SSTConfig;
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
package-lock.json
package.json
sst.config.ts
stacks
```

## 5. My contribution / role (evidence from git history — if available)

```text
64e1791 2025-08-29 Bump form-data from 4.0.0 to 4.0.4 (#37)
e2644d1 2025-08-29 Merge pull request #36 from BotNotOrg/dependabot/npm_and_yarn/multi-a1c2ce69a2
c2d8bef 2025-05-23 Merge pull request #35 from BotNotOrg/dependabot/npm_and_yarn/vite-5.4.19
04e89aa 2025-05-14 Bump vite from 5.4.16 to 5.4.19
99a43d3 2025-05-14 Merge pull request #34 from BotNotOrg/dev
1eb8603 2025-05-14 Update devDependencies: downgrade sst to 2.41.2 and aws-cdk-lib to 2.132.1 in package.json
6a40077 2025-05-14 Add FTID Fraud score and recommended action to constants and actions (#32) (#33)
fd4dbad 2025-05-14 Add FTID Fraud score and recommended action to constants and actions (#32)
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`frontend/src/api/index.js`**

```text
import request from '@/utils/request';
import { Neo4JAddress } from '@/components/CustomerGraph/entity.js';
import constants, { OrderRiskTypes } from '@/utils/constants'

// used by Recommended Actions tab
const formatPredictions = (rows) => {
    // const fields = ['bot_abuse_score', 'discount_abuse_score', 'resell_abuse_score', 'return_abuse_score']
    const fields = OrderRiskTypes.map((x) => x.key)
    rows.forEach((x) => {
      x.predictions = { indicators: [] }
      fields.forEach((field) => {
        const predictions = x.model_predictions || {}
        x.predictions.indicators = x.predictions.indicators.concat(
          predictions[field]?.indicators?.map((i) => {
            return { ...i, field }
          }) || []
        )
        x.predictions[field] = predictions[field]?.score || 0
      })
      //delete x.model_predictions
    })
  }

export default {
    getPurchasedProducts(data) {
        return request.post('/ecommerce/product/purchased', data, {
            loading: false,
        });
    },
    customersGraph(data) {
        return request
            .post('/ecommerce/customers/graph-v4', data)
            .then((res) => {
                formatPredictions([res.root_customer_data]);
                formatPredictions(res.connected_customers);
                res.connected_addresses = res.connected_addresses.map(
                    (x) => new Neo4JAddress(x)
                );
                return res;
            });
    },
    customersDetails(data) {
        return request
            .post('/ecommerce/customers/details', data)
            .then((res) => {
                formatPredictions([res]);
                formatPredictions(res.orders || []);
                return res;
            });
    },
    customersSimilarity(data) {
        return request.post('/ecommerce/customers/similarity-v4', data, {
            loading: false,
        });
    },

    ordersList(data, options) {
        return request
            .post('/ecommerce/orders/list', data, options)
            .then((res) => {
                formatPredictions(res.data.items);
            

…(truncated)…
```

**`frontend/src/components/CustomerBasicInfo/index.js`**

```text
export { default as CustomerBasicInfo } from './index.vue';
```

**`frontend/src/components/CustomerDetail/index.js`**

```text
export { default as CustomerDetail } from './index.vue';
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`yofi-embed-portal-ui`** capabilities aligned with **frontend** delivery.
- Applied **JavaScript** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yofi-embed-portal-ui`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

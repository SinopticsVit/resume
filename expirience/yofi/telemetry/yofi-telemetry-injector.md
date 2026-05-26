# yofi-telemetry-injector

**Path:** `D:/botnot/yofi-telemetry-injector`  
**Category:** telemetry  
**Primary language:** TypeScript  
**Status:** present on disk

## 1. Purpose (2-3 lines)

Internal **Yofi** repository `yofi-telemetry-injector` under category **telemetry**. Supports Yofi/Botnot platform capabilities (e-commerce intelligence, anti-fraud adjacent services, data plane, or infrastructure) as evidenced by repository layout and manifests.

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** TypeScript
- **Top-level layout:** see listing below.

### `package.json`

```
{
  "name": "yofi-telemetry-build",
  "private": true,
  "version": "0.0.1",
  "type": "module",
  "scripts": {
    "test": "vite",
    "build:dev": "tsc && vite build --mode development && cd yofi-telemetry-for-wp && zip -r ../yofi-telemetry-for-wp-dev.zip . -x '*.DS_Store'",
    "build": "tsc && vite build --mode production && cd yofi-telemetry-for-wp && zip -r ../yofi-telemetry-for-wp-prod.zip . -x '*.DS_Store'"
  },
  "dependencies": {
    "@yofi-ai/telemetry-web-sdk": "0.0.78"
  },
  "devDependencies": {
    "typescript": "^5.0.2",
    "vite": "^4.4.5"
  }
}
```

### `tsconfig.json`

```
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "module": "ESNext",
    "lib": [
      "ES2020",
      "DOM",
      "DOM.Iterable"
    ],
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": [
    "src"
  ],
  "references": [
    {
      "path": "./tsconfig.node.json"
    }
  ]
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
.npmrc
docker-compose.yaml
index.html
package-lock.json
package.json
src
tsconfig.json
tsconfig.node.json
vite.config.ts
yofi-telemetry-for-wp
yofi-telemetry-for-wp-dev.zip
yofi-telemetry-for-wp-prod.zip
```

## 5. My contribution / role (evidence from git history — if available)

```text
f20c1a5 2025-08-26 Merge pull request #3 from BotNotOrg/feature/YOFI-859-update-telemetry-version
bb75a8f 2025-03-11 Merge pull request #2 from BotNotOrg/support-access-token
cffde91 2025-03-11 update sdk to 73
3d96557 2025-03-11 Merge pull request #1 from BotNotOrg/support-access-token
f7d979a 2025-03-11 update
d66e531 2025-02-22 update
32baf85 2025-02-22 update
1139d5e 2025-02-21 use empty user id if not login
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`src/index.ts`**

```typescript
import { SdkConfig, YofiTelemetry } from '@yofi-ai/telemetry-web-sdk';
declare var __yofi_telemetry_data: any;

(function () {
    const config: SdkConfig = {
        publicToken: __yofi_telemetry_data.public_token,
        journeyIdSalt: __yofi_telemetry_data.journey_id_salt,
        accessToken: __yofi_telemetry_data.access_token
    };
    if ((import.meta as any).env.MODE === 'development') {
        config.defaultDataPlaneUrl =
            'https://server.telemetry.services-dev.yofi.ai';
        config.defaultNetworkUrl =
            'https://server.telemetry.services-dev.yofi.ai';
    }

    YofiTelemetry.initialize(config);

    // Initial labels if any
    let initLabels: { [key: string]: string } = {};

    if (__yofi_telemetry_data?.user_id) {
        initLabels['userId'] = `${__yofi_telemetry_data?.user_id}`;
    }

    if (__yofi_telemetry_data?.seller_id) {
        initLabels['sellerId'] = `${__yofi_telemetry_data?.seller_id}`;
    }

    if (Object.keys(__yofi_telemetry_data?.labels || {}).length) {
        initLabels = { ...initLabels, ...__yofi_telemetry_data.labels };
    }

    const session = YofiTelemetry.startSession({
        duration: 900 * 1000, // 15mins
        labels: initLabels, // Optional
        networkTelemetryConfig: {
            ip: true,
        },
    });
    // Expose YofiTelemetry and session instance to window object for external scripts
    Object.defineProperties(window, {
        YofiTelemetry: {
            value: YofiTelemetry,
            writable: false,
            configurable: false,
        },
        YofiSessionInstance: {
            value: session,
            writable: false,
            configurable: false,
        },
    });
})();
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`yofi-telemetry-injector`** capabilities aligned with **telemetry** delivery.
- Applied **TypeScript** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yofi-telemetry-injector`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

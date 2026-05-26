# yofi-telemetry-lite-sdk

**Path:** `D:/botnot/yofi-telemetry-lite-sdk`  
**Category:** telemetry  
**Primary language:** TypeScript  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# Telemetry Lite SDK


### Quick Started
```typescript
import {
    TelemetryLite,
    TelemetryLiteConfig,
} from '@yofi-ai/yofi-telemetry-lite-sdk';

const shopifyAPI = {};
const config: TelemetryLiteConfig = {
    publicToken: 'THE-PUBLIC-TOKEN',
    webPixelApi: shopifyAPI,
};

const telemetry = new TelemetryLite(config);
telemetry.start();
```

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** TypeScript
- **Top-level layout:** see listing below.

### `README.md`

```
# Telemetry Lite SDK


### Quick Started
```typescript
import {
    TelemetryLite,
    TelemetryLiteConfig,
} from '@yofi-ai/yofi-telemetry-lite-sdk';

const shopifyAPI = {};
const config: TelemetryLiteConfig = {
    publicToken: 'THE-PUBLIC-TOKEN',
    webPixelApi: shopifyAPI,
};

const telemetry = new TelemetryLite(config);
telemetry.start();
```
```

### `readme.md`

```
# Telemetry Lite SDK


### Quick Started
```typescript
import {
    TelemetryLite,
    TelemetryLiteConfig,
} from '@yofi-ai/yofi-telemetry-lite-sdk';

const shopifyAPI = {};
const config: TelemetryLiteConfig = {
    publicToken: 'THE-PUBLIC-TOKEN',
    webPixelApi: shopifyAPI,
};

const telemetry = new TelemetryLite(config);
telemetry.start();
```
```

### `Readme.md`

```
# Telemetry Lite SDK


### Quick Started
```typescript
import {
    TelemetryLite,
    TelemetryLiteConfig,
} from '@yofi-ai/yofi-telemetry-lite-sdk';

const shopifyAPI = {};
const config: TelemetryLiteConfig = {
    publicToken: 'THE-PUBLIC-TOKEN',
    webPixelApi: shopifyAPI,
};

const telemetry = new TelemetryLite(config);
telemetry.start();
```
```

### `package.json`

```
{
  "name": "@yofi-ai/yofi-telemetry-lite-sdk",
  "version": "0.0.12",
  "type": "module",
  "module": "lib/yofi-telemetry-lite-sdk.es.js",
  "typings": "lib/index.d.ts",
  "files": [
    "lib/**/*"
  ],
  "sideEffects": false,
  "scripts": {
    "dev": "vite",
    "build": "vite build -- --mode production",
    "test": "vitest"
  },
  "devDependencies": {
    "@rollup/plugin-terser": "^0.4.4",
    "@testing-library/dom": "^10.4.0",
    "@testing-library/jest-dom": "^6.5.0",
    "@types/node": "^22.7.4",
    "@types/uuid": "^10.0.0",
    "@vitest/ui": "^2.1.1",
    "jsdom": "^25.0.1",
    "typescript": "^5.5.3",
    "vite": "^5.4.14",
    "vite-plugin-dts": "^4.2.3",
    "vitest": "^2.1.9"
  },
  "dependencies": {
    "detectincognitojs": "1.3.6",
    "fflate": "^0.8.2",
    "jwt-decode": "^4.0.0",
    "uuid": "^10.0.0"
  }
}
```

### `tsconfig.json`

```
{
  "compilerOptions": {
    "declaration": true,
    "declarationDir": "./lib/",
    "target": "ES2020",
    "useDefineForClassFields": true,
    "module": "ESNext",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "isolatedModules": true,
    "moduleDetection": "force",
    "noEmit": true,

    /* Linting */
    "strict": false,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "removeComments": true,
  },
  "include": ["src"]
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
.env
.github
.gitignore
README.md
ReleaseNotes.md
example
package-lock.json
package.json
src
tests
tsconfig.json
vite.config.ts
vitest.setup.ts
```

## 5. My contribution / role (evidence from git history — if available)

```text
e129655 2025-04-01 Merge pull request #12 from BotNotOrg/dependabot/npm_and_yarn/example/multi-b64c723da5
1db94c5 2025-04-01 Merge pull request #11 from BotNotOrg/dependabot/npm_and_yarn/vitest-2.1.9
c0f9cff 2025-03-11 Bump esbuild, @vitejs/plugin-react and vite in /example
489fbc2 2025-03-11 Bump vitest from 2.1.1 to 2.1.9
da120c2 2025-03-11 Merge pull request #10 from BotNotOrg/dependabot/npm_and_yarn/vite-5.4.14
0c54e08 2025-01-22 Bump vite from 5.4.8 to 5.4.14
2dc81d5 2024-12-17 Bump nanoid from 3.3.7 to 3.3.8 in /example (#9)
c70b726 2024-12-17 Bump nanoid from 3.3.7 to 3.3.8 (#8)
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`src/BingGan/index.ts`**

```typescript
import {
    additionalDetectors,
    BingGanDetectors,
    bingGanSource,
} from './sources';
import { sortObjectKeys } from './utils/data';
import { hashing } from './utils/hashing';

export interface DetectResult {
    [key: string]: string;
}

export interface BingGanData {
    elapsed: number;
    data: DetectResult;
    hash: string;
    addition: DetectResult;
}

export class BingGan {
    async get(): Promise<BingGanData> {
        const startTs = performance.now();
        const { bingGanData, additionalData } = await this.detectAll();
        const hash = await this.generateHash(bingGanData);
        const endTs = performance.now();
        return {
            elapsed: endTs - startTs,
            data: bingGanData,
            addition: additionalData || {},
            hash: hash,
        };
    }

    private async detectAll() {
        try {
            const [bingGanData, additionalData] = await Promise.all([
                this.detect(bingGanSource),
                this.detect(additionalDetectors),
            ]);
            return { bingGanData, additionalData };
        } catch (error) {
            return { bingGanData: {}, additionalData: {} };
        }
    }

    private async generateHash(bingGanData: DetectResult): Promise<string> {
        const hash = await hashing(JSON.stringify(sortObjectKeys(bingGanData)));
        return `A2:${hash}`;
    }

    private async detect(detectors: BingGanDetectors) {
        const keys = Object.keys(detectors);
        const res = await Promise.all(
            keys.map((x) => {
                try {
                    return detectors[x]();
                } catch (error) {
                    return 'unknown';
                }
            }),
        );
        const data: DetectResult = {};
        keys.forEach((k, i) => {
            data[k] = res[i];
        });
        return sortObjectKeys(data);
    }
}
```

**`src/BingGan/sources/index.ts`**

```typescript
import { getArchitecture } from './architecture';
import { getBattery } from './battery';
import { getCanvasFingerprint } from './canvas';
import { getColorDepth } from './color_depth';
import { getCookiesEnabled } from './cookie';
import { getDeviceMemory } from './device_memory';
import { getFontsFingerprint } from './fonts';
import { getHardwareConcurrency } from './hardware_concurrency';
import { getLanguages } from './languages';
import { getMathTan } from './math_tan';
import { getPlugins } from './plugins';
import { getDevicePlatform } from './device_platform';
import { getStorageEnabled } from './storage';
import { getTouchSupport } from './touch_support';
import { getWebGLFingerprint } from './webgl';
import { getWebGLInfo } from './webgl_info';
import { getDevicePixelRatio } from './device_pixel_ratio';
import { getScreenResolution } from './screen_resolution';
import { getBrowser } from './browser';
import { getIncognitoMode } from './incognito';
import { getTimezone } from './timezone';
import { getColorGamut } from './color_gamut';
import { getContrastPreference } from './contrast';
import { getMaxTouchPoints } from './max_touch_points';
import { getVersion } from './version';

export interface BingGanDetectors {
    [key: string]: () => Promise<string>;
}

/**
 * When add new sources here, also need to add it to
 * src/base/generated/protos/dataplane/SessionMetadata.ts
 */

export const bingGanSource: BingGanDetectors = {
    architecture: getArchitecture,
    battery: getBattery,
    browser: getBrowser,
    canvas: getCanvasFingerprint,
    color_depth: getColorDepth,
    color_gamut: getColorGamut,
    contrast: getContrastPreference,
    cookie: getCookiesEnabled,
    device_memory: getDeviceMemory,
    device_pixel_ratio: getDevicePixelRatio,
    device_platform: getDevicePlatform,
    fonts: getFontsFingerprint,
    hardware_concurrency: getHardwareConcurrency,
    languages: getLanguages,
    math_tan: getMathTan,
    max_touch_points:getMaxTouchPoints,
    plugin: getPlugins,
    screen_resolution: getScreenResolution,
    storage: getStorageEnabled,
    touch_suppor

…(truncated)…
```

**`src/core/index.ts`**

```typescript
export * from './TelemetryLite';
export * from './DataPlane';
export * from './TokenManager';
export * from './UuidManager';
export * from './models';
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`yofi-telemetry-lite-sdk`** capabilities aligned with **telemetry** delivery.
- Applied **TypeScript** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yofi-telemetry-lite-sdk`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

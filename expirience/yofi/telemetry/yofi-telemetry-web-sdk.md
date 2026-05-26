# yofi-telemetry-web-sdk

**Path:** `D:/botnot/yofi-telemetry-web-sdk`  
**Category:** telemetry  
**Primary language:** TypeScript  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# Telemetry Web SDK 

### Prerequisites

Please contact Yofi team to get your own tokens:

1. NPM access token: Used for installing npm packages
2. Telemetry public token: Used for using the telemetry SDK 

### Install

1. [Setup your `.npmrc`](https://docs.npmjs.com/cli/v10/configuring-npm/npmrc#files).
   
.npmrc sample:
```
@yofi-ai:registry=https://registry.npmjs.org/
//registry.npmjs.org/:_authToken=YOUR-NPM-ACCESS-TOKEN-HERE
```

2. Install the package via npm cli
```
npm install @yofi-ai/telemetry-web-sdk@TARGET_VESION
```
or install via package.json
```
"@yofi-ai/telemetry-web-sdk": "TARGET_VESION"
```

> `TARGET_VESION` can be found on npm registry, or use `stable` for a stable version
> 
> `latest` also support, but automatically 

…(truncated)…

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** TypeScript
- **Top-level layout:** see listing below.

### `README.md`

```
# Telemetry Web SDK 

### Prerequisites

Please contact Yofi team to get your own tokens:

1. NPM access token: Used for installing npm packages
2. Telemetry public token: Used for using the telemetry SDK 

### Install

1. [Setup your `.npmrc`](https://docs.npmjs.com/cli/v10/configuring-npm/npmrc#files).
   
.npmrc sample:
```
@yofi-ai:registry=https://registry.npmjs.org/
//registry.npmjs.org/:_authToken=YOUR-NPM-ACCESS-TOKEN-HERE
```

2. Install the package via npm cli
```
npm install @yofi-ai/telemetry-web-sdk@TARGET_VESION
```
or install via package.json
```
"@yofi-ai/telemetry-web-sdk": "TARGET_VESION"
```

> `TARGET_VESION` can be found on npm registry, or use `stable` for a stable version
> 
> `latest` also support, but automatically updating to the latest version of a package can introduce breaking changes to your project  

### Quick Start

```javascript
import { YofiTelemetry, LogLevel, AvailableSensors} from '@yofi-ai/telemetry-web-sdk'

const publicToken = 'YOUR-PUBLIC-TOKEN';

YofiTelemetry.initialize({
    publicToken: publicToken, 
    // journeyIdSalt used to generate journey id. If you have different websites, you can use different Salts.
    journeyIdSalt: 'yofiscakes.myshopify.com'
});

// Initial labels if any
const initLabels = {
    'some-label': 'some-value'
};

const session = YofiTelemetry.startSession({
    duration: 900 * 1000, // 15mins
    labels: initLabels,   // Optional
    networkTelemetryConfig: {
        ip: true
    }
});

```

To terminate all existing sessions and initiate a new one, set the `stopAllSessions` parameter of `startSession` to `true`.

```js
const session = YofiTelemetry.startSession(yourSessionConfig, true);
```


### Starting a New Journey


To start a new journey, follow the steps below. You can set labels and other configuration options via `yourSessionConfig`.

Note: Before calling `startNewJourney`, make sure you have already called `YofiTelemetry.initialize`.
```js
const session = await YofiTelemetry.startNewJourney(yourSessionConfig);
```


### Session Labels

You can add labels to a session, the value of each label must be string.

```js
const existingLabels = session.getLabels();

const newLabels = {
    'new-label': 'new-value'
};
// Note: Starting from v0.0.41, addLabels returns a Promise object.
// If an exception occurs, it will throw an Error object.
await session.addLabels(newLabels);
```

You can wait for the result of `addLabels` using the following approachs.

```js

// Async/await approach
async function asyncApproach(newLabels) {
    try {
        await session.addLabels(newLabels);
        // Label addition completed successfully
    } catch(error) {
        // Handle error thrown during label addition
    }
}

// Promise approach
function promiseApproach(newLabels) {
    session.addLabels(newLabels)
    .then(() => {
        // Label addition success
    })
    .catch((error) => {
        // Handle error from label addition
    });
}
```

### Advanced Configuration

#### 1. Configure Sensors

To specify which sensors should cease 

…(truncated)…
```

### `readme.md`

```
# Telemetry Web SDK 

### Prerequisites

Please contact Yofi team to get your own tokens:

1. NPM access token: Used for installing npm packages
2. Telemetry public token: Used for using the telemetry SDK 

### Install

1. [Setup your `.npmrc`](https://docs.npmjs.com/cli/v10/configuring-npm/npmrc#files).
   
.npmrc sample:
```
@yofi-ai:registry=https://registry.npmjs.org/
//registry.npmjs.org/:_authToken=YOUR-NPM-ACCESS-TOKEN-HERE
```

2. Install the package via npm cli
```
npm install @yofi-ai/telemetry-web-sdk@TARGET_VESION
```
or install via package.json
```
"@yofi-ai/telemetry-web-sdk": "TARGET_VESION"
```

> `TARGET_VESION` can be found on npm registry, or use `stable` for a stable version
> 
> `latest` also support, but automatically updating to the latest version of a package can introduce breaking changes to your project  

### Quick Start

```javascript
import { YofiTelemetry, LogLevel, AvailableSensors} from '@yofi-ai/telemetry-web-sdk'

const publicToken = 'YOUR-PUBLIC-TOKEN';

YofiTelemetry.initialize({
    publicToken: publicToken, 
    // journeyIdSalt used to generate journey id. If you have different websites, you can use different Salts.
    journeyIdSalt: 'yofiscakes.myshopify.com'
});

// Initial labels if any
const initLabels = {
    'some-label': 'some-value'
};

const session = YofiTelemetry.startSession({
    duration: 900 * 1000, // 15mins
    labels: initLabels,   // Optional
    networkTelemetryConfig: {
        ip: true
    }
});

```

To terminate all existing sessions and initiate a new one, set the `stopAllSessions` parameter of `startSession` to `true`.

```js
const session = YofiTelemetry.startSession(yourSessionConfig, true);
```


### Starting a New Journey


To start a new journey, follow the steps below. You can set labels and other configuration options via `yourSessionConfig`.

Note: Before calling `startNewJourney`, make sure you have already called `YofiTelemetry.initialize`.
```js
const session = await YofiTelemetry.startNewJourney(yourSessionConfig);
```


### Session Labels

You can add labels to a session, the value of each label must be string.

```js
const existingLabels = session.getLabels();

const newLabels = {
    'new-label': 'new-value'
};
// Note: Starting from v0.0.41, addLabels returns a Promise object.
// If an exception occurs, it will throw an Error object.
await session.addLabels(newLabels);
```

You can wait for the result of `addLabels` using the following approachs.

```js

// Async/await approach
async function asyncApproach(newLabels) {
    try {
        await session.addLabels(newLabels);
        // Label addition completed successfully
    } catch(error) {
        // Handle error thrown during label addition
    }
}

// Promise approach
function promiseApproach(newLabels) {
    session.addLabels(newLabels)
    .then(() => {
        // Label addition success
    })
    .catch((error) => {
        // Handle error from label addition
    });
}
```

### Advanced Configuration

#### 1. Configure Sensors

To specify which sensors should cease 

…(truncated)…
```

### `Readme.md`

```
# Telemetry Web SDK 

### Prerequisites

Please contact Yofi team to get your own tokens:

1. NPM access token: Used for installing npm packages
2. Telemetry public token: Used for using the telemetry SDK 

### Install

1. [Setup your `.npmrc`](https://docs.npmjs.com/cli/v10/configuring-npm/npmrc#files).
   
.npmrc sample:
```
@yofi-ai:registry=https://registry.npmjs.org/
//registry.npmjs.org/:_authToken=YOUR-NPM-ACCESS-TOKEN-HERE
```

2. Install the package via npm cli
```
npm install @yofi-ai/telemetry-web-sdk@TARGET_VESION
```
or install via package.json
```
"@yofi-ai/telemetry-web-sdk": "TARGET_VESION"
```

> `TARGET_VESION` can be found on npm registry, or use `stable` for a stable version
> 
> `latest` also support, but automatically updating to the latest version of a package can introduce breaking changes to your project  

### Quick Start

```javascript
import { YofiTelemetry, LogLevel, AvailableSensors} from '@yofi-ai/telemetry-web-sdk'

const publicToken = 'YOUR-PUBLIC-TOKEN';

YofiTelemetry.initialize({
    publicToken: publicToken, 
    // journeyIdSalt used to generate journey id. If you have different websites, you can use different Salts.
    journeyIdSalt: 'yofiscakes.myshopify.com'
});

// Initial labels if any
const initLabels = {
    'some-label': 'some-value'
};

const session = YofiTelemetry.startSession({
    duration: 900 * 1000, // 15mins
    labels: initLabels,   // Optional
    networkTelemetryConfig: {
        ip: true
    }
});

```

To terminate all existing sessions and initiate a new one, set the `stopAllSessions` parameter of `startSession` to `true`.

```js
const session = YofiTelemetry.startSession(yourSessionConfig, true);
```


### Starting a New Journey


To start a new journey, follow the steps below. You can set labels and other configuration options via `yourSessionConfig`.

Note: Before calling `startNewJourney`, make sure you have already called `YofiTelemetry.initialize`.
```js
const session = await YofiTelemetry.startNewJourney(yourSessionConfig);
```


### Session Labels

You can add labels to a session, the value of each label must be string.

```js
const existingLabels = session.getLabels();

const newLabels = {
    'new-label': 'new-value'
};
// Note: Starting from v0.0.41, addLabels returns a Promise object.
// If an exception occurs, it will throw an Error object.
await session.addLabels(newLabels);
```

You can wait for the result of `addLabels` using the following approachs.

```js

// Async/await approach
async function asyncApproach(newLabels) {
    try {
        await session.addLabels(newLabels);
        // Label addition completed successfully
    } catch(error) {
        // Handle error thrown during label addition
    }
}

// Promise approach
function promiseApproach(newLabels) {
    session.addLabels(newLabels)
    .then(() => {
        // Label addition success
    })
    .catch((error) => {
        // Handle error from label addition
    });
}
```

### Advanced Configuration

#### 1. Configure Sensors

To specify which sensors should cease 

…(truncated)…
```

### `package.json`

```
{
  "name": "@yofi-ai/telemetry-web-sdk",
  "version": "0.0.76",
  "description": "Yofi telemetry SDK to capture sensor data",
  "main": "lib/yofi-telemetry-web-sdk.js",
  "typings": "lib/cloud/YofiTelemetry.d.ts",
  "files": [
    "lib/**/*"
  ],
  "scripts": {
    "test": "jest",
    "watch": "webpack --watch",
    "build:dev": "NODE_ENV=development webpack",
    "build": "NODE_ENV=production webpack"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/BotNotOrg/yofi-telemetry-web-sdk.git"
  },
  "author": "Yofi",
  "license": "UNLICENSED",
  "dependencies": {
    "@fingerprintjs/botd": "1.9.1",
    "detectincognitojs": "1.3.6",
    "fetch-retry": "^5.0.6",
    "fflate": "^0.8.0",
    "jwt-decode": "^4.0.0",
    "uuid": "^9.0.0"
  },
  "devDependencies": {
    "@types/jest": "^27.5.2",
    "@types/node": "^12.20.11",
    "@types/w3c-generic-sensor": "^1.0.6",
    "dotenv": "^16.0.3",
    "javascript-obfuscator": "^4.1.1",
    "jest": "^27.2.0",
    "terser-webpack-plugin": "^5.3.9",
    "ts-jest": "^27.0.5",
    "ts-loader": "^9.4.4",
    "ts-node": "^10.2.1",
    "typescript": "^4.9.5",
    "webpack": "^5.88.2",
    "webpack-cli": "^5.1.4",
    "webpack-obfuscator": "^3.5.1"
  }
}
```

### `tsconfig.json`

```
{
  "compilerOptions": {
    /* Visit https://aka.ms/tsconfig.json to read more about this file */

    /* Basic Options */
    // "incremental": true,                         /* Enable incremental compilation */
    "target": "ES2017" /* Specify ECMAScript target version: 'ES3' (default), 'ES5', 'ES2015', 'ES2016', 'ES2017', 'ES2018', 'ES2019', 'ES2020', or 'ESNEXT'. */,
    "module": "es2015" /* Specify module code generation: 'none', 'commonjs', 'amd', 'system', 'umd', 'es2015', 'es2020', or 'ESNext'. */,
    // "lib": [],                                   /* Specify library files to be included in the compilation. */
    "allowJs": true,                             /* Allow javascript files to be compiled. */
    // "checkJs": true,                             /* Report errors in .js files. */
    // "jsx": "preserve",                           /* Specify JSX code generation: 'preserve', 'react-native', 'react', 'react-jsx' or 'react-jsxdev'. */
    "declaration": true /* Generates corresponding '.d.ts' file. */,
    // "declarationMap": true,                      /* Generates a sourcemap for each corresponding '.d.ts' file. */
    // "sourceMap": true,                           /* Generates corresponding '.map' file. */
    // "outFile": "./",                             /* Concatenate and emit output to single file. */
    "outDir": "./lib/" /* Redirect output structure to the directory. */,
    // "rootDir": "./",                             /* Specify the root directory of input files. Use to control the output directory structure with --outDir. */
    // "composite": true,                           /* Enable project compilation */
    // "tsBuildInfoFile": "./",                     /* Specify file to store incremental compilation information */
    // "removeComments": true,                      /* Do not emit comments to output. */
    // "noEmit": true,                              /* Do not emit outputs. */
    // "importHelpers": true,                       /* Import emit helpers from 'tslib'. */
    // "downlevelIteration": true,                  /* Provide full support for iterables in 'for-of', spread, and destructuring when targeting 'ES5' or 'ES3'. */
    // "isolatedModules": true,                     /* Transpile each file as a separate module (similar to 'ts.transpileModule'). */

    /* Strict Type-Checking Options */
    "strict": false /* Enable all strict type-checking options. */,
    // "noImplicitAny": true,                       /* Raise error on expressions and declarations with an implied 'any' type. */
    "strictNullChecks": false,                    /* Enable strict null checks. */
    // "strictFunctionTypes": true,                 /* Enable strict checking of function types. */
    // "strictBindCallApply": true,                 /* Enable strict 'bind', 'call', and 'apply' methods on functions. */
    "strictPropertyInitialization": false,        /* Enable strict checking of property initialization in classes. */
    // "noImplicitThis": true,                      /* Raise error on 'this' expressions with an implied 'any' type. */
    // "alwaysStrict": 

…(truncated)…
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
.prettierrc
README.md
ReleaseNotes.md
Sensors.md
e2e
example
jest.config.js
package-lock.json
package.json
src
telemetry.excalidraw
test
tsconfig.json
webpack.config.js
```

## 5. My contribution / role (evidence from git history — if available)

```text
f984630 2025-05-15 Merge pull request #161 from BotNotOrg/dev
1ee63e4 2025-05-15 Merge pull request #160 from BotNotOrg/sinisa_client_ui_update
463bb5c 2025-05-15 fix for last_update_at field for cluster bubbles labeling
5cd0f44 2025-05-15 merged from dev update on package lock. added warning console output if connected client in cluster has last_update_at set to null or missing
d839f63 2025-05-14 Bugfix npmrc (#159)
da0b099 2025-05-14 Merge pull request #158 from BotNotOrg/sinisa_client_ui_update
0f37b8c 2025-05-14 fixed yaml
403fceb 2025-05-14 fixed merge conflict with dev branch
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`example/telemetry-data-viewer/src/entity/index.ts`**

```typescript
export * from './JourneyData';
export * from './ViewerSettings';
export * from './Response';
export * from './ClusterConnection';
```

**`example/telemetry-data-viewer/src/utils/index.ts`**

```typescript
import dayjs from 'dayjs';
import { readSettings, saveSettings } from './cache';
export * from './api';

export function getRandomRGBColor(): string {
    const getRandomValue = () => Math.floor(Math.random() * 256);

    const r = getRandomValue();
    const g = getRandomValue();
    const b = getRandomValue();

    return `rgb(${r}, ${g}, ${b})`;
}

export function formatDate(date: string | number) {
    return dayjs(date).format('YYYY-MM-DD HH:mm:ss');
}

export function getEnumKeyByValue(
    enumObj: any,
    value: number,
): string | undefined {
    return Object.keys(enumObj).find((key) => enumObj[key] === value);
}

export function saveSelectedAuthorizedApp(appId: string) {
    const settings = readSettings();
    settings.app_id = appId;
    saveSettings(settings);
}

export function saveSearchModeApp(searchMode: string) {
    const settings = readSettings();
    settings.search_mode = searchMode;
    saveSettings(settings);
}

export function getRequestCacheKey(name: string): string {
    const settings = readSettings();
    return settings.app_id ? `${settings.app_id}_${name}` : name;
}
```

**`src/base/generated/protos/bundle/index.ts`**

```typescript
export { Accelerometer, IAccelerometer } from './Accelerometer';
export { AppLifeCycleEvent, IAppLifeCycleEvent } from './AppLifeCycleEvent';
export { Battery, IBattery } from './Battery';
export { Bundle, IBundle } from './Bundle';
export { Click, IClick } from './Click';
export { Clock, IClock } from './Clock';
export { ClosedRange, IClosedRange } from './ClosedRange';
export { ContextMenuEvent, IContextMenuEvent } from './ContextMenuEvent';
export { CustomEvent, ICustomEvent } from './CustomEvent';
export { FocusChange, IFocusChange } from './FocusChange';
export { FormSubmitEvent, IFormSubmitEvent } from './FormSubmitEvent';
export { FrameRateEvent, IFrameRateEvent } from './FrameRateEvent';
export { Gyroscope, IGyroscope } from './Gyroscope';
export { InputChange, IInputChange } from './InputChange';
export { KeyPress, IKeyPress } from './KeyPress';
export { Location, ILocation } from './Location';
export { Magnetometer, IMagnetometer } from './Magnetometer';
export { MouseWheel, IMouseWheel } from './MouseWheel';
export { Offset2D, IOffset2D } from './Offset2D';
export { Orientation, IOrientation } from './Orientation';
export { PermissionEvent, IPermissionEvent } from './PermissionEvent';
export { Pointer, IPointer } from './Pointer';
export { SealedBundle, ISealedBundle } from './SealedBundle';
export { TargetElement, ITargetElement } from './TargetElement';
export { TextChange, ITextChange } from './TextChange';
export { ViewportScroll, IViewportScroll } from './ViewportScroll';
export { ViewportSizeEvent, IViewportSizeEvent } from './ViewportSizeEvent';
export { ConsoleEvent, IConsoleEvent } from './ConsoleEvent';
export { NetworkEvent, INetworkEvent } from './NetworkEvent';
export { ExceptionEvent, IExceptionEvent } from './ExceptionEvent';
export { ClipboardEvent, IClipboardEvent } from './ClipboardEvent';
export { BotD, IBotD } from './BotD';
export { ClientInfo, IClientInfo } from './ClientInfo';
export { SelectionEvent, ISelectionEvent } from './SelectionEvent';
export { RoundTripTime, IRoundTripTime } from './RoundTripTime';
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`yofi-telemetry-web-sdk`** capabilities aligned with **telemetry** delivery.
- Applied **TypeScript** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yofi-telemetry-web-sdk`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

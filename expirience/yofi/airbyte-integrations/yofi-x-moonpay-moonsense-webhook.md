# yofi-x-moonpay-moonsense-webhook

**Path:** `D:/botnot/yofi-x-moonpay-moonsense-webhook`  
**Category:** airbyte-integrations  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# yofi-x-moonpay-moonsense-webhook
THIS iS ONLY FOR MOONPAY
This lambda is to build a api server to subscibe to webhooks of moonsense, so that we can receive data of that shop.

# Docs of moonsense webhook
https://docs.moonsense.io/articles/cloud/webhooks

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

### `README.md`

```
# yofi-x-moonpay-moonsense-webhook
THIS iS ONLY FOR MOONPAY
This lambda is to build a api server to subscibe to webhooks of moonsense, so that we can receive data of that shop.

# Docs of moonsense webhook
https://docs.moonsense.io/articles/cloud/webhooks
```

### `readme.md`

```
# yofi-x-moonpay-moonsense-webhook
THIS iS ONLY FOR MOONPAY
This lambda is to build a api server to subscibe to webhooks of moonsense, so that we can receive data of that shop.

# Docs of moonsense webhook
https://docs.moonsense.io/articles/cloud/webhooks
```

### `Readme.md`

```
# yofi-x-moonpay-moonsense-webhook
THIS iS ONLY FOR MOONPAY
This lambda is to build a api server to subscibe to webhooks of moonsense, so that we can receive data of that shop.

# Docs of moonsense webhook
https://docs.moonsense.io/articles/cloud/webhooks
```

### `package.json`

```
{
  "name": "yofi-x-moonpay-lambda-moonsense-webhook",
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
  "name": "yofi-x-moonpay-lambda-moonsense-webhook",
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
layer
ml_layer
package.json
pytest.ini
seed.yml
src_ml_predict
src_webhook_receiver
sst.json
stacks
test
```

## 5. My contribution / role (evidence from git history — if available)

```text
041d450 2023-08-09 Tracing.DISABLED
a20235c 2023-08-08 delete Tracing
96489fd 2023-07-28 feat: add field relation
491fe50 2023-07-28 feat: switched to http request
5e4637b 2023-07-28 fix: remove fingerprint_pro_server_api_sdk because it's not supported in lambda
254f7d4 2023-07-27 fix: add fingerprint downloading
f033924 2023-07-25 fix: the certificate of ssl
39b0a6b 2023-07-24 fix: add 3 labels for prediction
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`src_ml_predict/app.py`**

```python
from log import logger
import json
import util
import os
from dataclasses import dataclass
from typing import Optional


# call the model and return the result.
MoonseModel_obj = util.MoonseModel()


@dataclass
class PredictResult:
    is_bot_ml_prediction: float
    is_predicted_with_partial_features: bool


def request_prediction_journey(journey_id) -> Optional[PredictResult]:
    logger.info(f"Requesting ml prediction for journey_id: {journey_id}")
    FeatureEngineering_obj = util.FeatureEngineering(None, journey_id)

    # this code is disabled until we enable bundles from our mongodb source and launch the new model
    # ss_features = util.get_session_sampling_features_for_journey(journey_id)
    # logger.info("session sampling features: {}".format(json.dumps(ss_features)))

    features = FeatureEngineering_obj.get_journey_features()
    elapsed_time = features["journey_duration"]
    logger.info("journey features: {}".format(json.dumps(features)))
    if not features:
        logger.warning(
            f"No features returned from feature engineering for the journey id {journey_id}"
        )
    return prediction(FeatureEngineering_obj, features)


def request_prediction_session(moonsense_session_id) -> Optional[PredictResult]:
    logger.info(f"Requesting ml prediction for session_id: {moonsense_session_id}")

    FeatureEngineering_obj = util.FeatureEngineering(moonsense_session_id)
    features = FeatureEngineering_obj.get_session_features()
    logger.info("session features: {}".format(json.dumps(features)))
    if not features:
        logger.warning(
            f"No features returned from feature engineering for the session id {moonsense_session_id}"
        )
        return None

    # just keep the following name from the .
    names = os.environ.get(
        "features",
        [
            "gesture_velocity_min",
            "gesture_curviness_mean",
            "mouse_wheel_inversions_mean",
            "mouse_wheel_inversions_count",
            "pointer_off_page_time_max",
            "pointer_off_page_time_min",
            "pointer_off_page_time_mean",
      

…(truncated)…
```

**`stacks/index.js`**

```text
import LambdaStack from './MyStack';
import {Tracing} from 'aws-cdk-lib/aws-lambda';

export default function main(app) {
    // Set default runtime for all functions
    app.setDefaultFunctionProps({
        runtime: 'python3.9',
        tracing: Tracing.DISABLED
    });

    new LambdaStack(app, 'sst-stack', {prefix: "yofi-x-moonpay", name: "lambda-moonsense-webhook"});
}
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`yofi-x-moonpay-moonsense-webhook`** capabilities aligned with **airbyte integrations** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yofi-x-moonpay-moonsense-webhook`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

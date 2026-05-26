# botnot-lambda-moonsense-webhook-api

**Path:** `D:/botnot/botnot-lambda-moonsense-webhook-api`  
**Category:** airbyte-integrations  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# botnot-moonsense-webhook
This lambda is to build a api server to subscibe to webhooks of moonsense, so that we can receive data of that shop.

# Docs of moonsense webhook
https://docs.moonsense.io/articles/cloud/webhooks

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

### `README.md`

```
# botnot-moonsense-webhook
This lambda is to build a api server to subscibe to webhooks of moonsense, so that we can receive data of that shop.

# Docs of moonsense webhook
https://docs.moonsense.io/articles/cloud/webhooks
```

### `readme.md`

```
# botnot-moonsense-webhook
This lambda is to build a api server to subscibe to webhooks of moonsense, so that we can receive data of that shop.

# Docs of moonsense webhook
https://docs.moonsense.io/articles/cloud/webhooks
```

### `Readme.md`

```
# botnot-moonsense-webhook
This lambda is to build a api server to subscibe to webhooks of moonsense, so that we can receive data of that shop.

# Docs of moonsense webhook
https://docs.moonsense.io/articles/cloud/webhooks
```

### `package.json`

```
{
  "name": "botnot-backend-lambda-moonsense-webhook-api",
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
  "name": "botnot-backend-lambda-moonsense-webhook-api",
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
src_save_to_redis
src_webhook_receiver
sst.json
stacks
test
```

## 5. My contribution / role (evidence from git history — if available)

```text
3f3a377 2023-11-16 add checking feature existing
0ca10c3 2023-11-16 fix prediction argument
61341ba 2023-11-16 fix name dynamo table
8ceaabf 2023-11-16 add print dynamo query
e0e50cf 2023-11-16 add print dynamo query
9e7709f 2023-11-16 add freg_counter in ml_layer
8c2640f 2023-11-16 add config in ml_layer
d751e93 2023-11-16 add dynamo in ml_layer
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
    def __init__(self, is_bot_ml_prediction: Optional[float], is_predicted_with_partial_features: bool, features: str):
        self.is_bot_ml_prediction = is_bot_ml_prediction
        self.is_predicted_with_partial_features = is_predicted_with_partial_features
        self.features = features


def request_prediction_journey(journey_id: str, extra_features: dict) -> Optional[PredictResult]:
    if not journey_id:
        logger.error("No journey ID provided for ML prediction.")
        return None
    logger.info(f"Requesting ML prediction for journey_id: {journey_id}")
    feature_engineering_obj = util.FeatureEngineering(None, journey_id)
    features, features_exist = feature_engineering_obj.get_journey_features_from_yofitelemetry()
    if not features_exist:
        logger.warning(f"No features returned from feature engineering for journey_id {journey_id}")
        return PredictResult(None, feature_engineering_obj.is_feature_partial, "")
    features.update(extra_features)
    features_str = json.dumps(features)
    # TODO: Implement actual ML prediction logic here
    return PredictResult(0, feature_engineering_obj.is_feature_partial, features_str)


def prediction(FeatureEngineering_obj, features):
    logger.info(f"requesting with filtered features: {features}")
    try:
        prediction_results = MoonseModel_obj.request_moonse_endpoint(features)
    except Exception as e:
        logger.info(f"Error with model request: {e}")
        logger.info(f"Did moonsense return features? Attempting fallback model...")
        prediction_results = MoonseModel_obj.request_fallback_moonse_endpoint(features)

    if not prediction_results.predictions:
        logger.error("No predictions returned from google AI endpoint")
    else:
        prediction_dict = dict(prediction_results.predictions[0])
        logger.info(f"Got prediction from google AI endpoint: {prediction_di

…(truncated)…
```

**`stacks/index.js`**

```text
import LambdaStack from './MyStack';
import {Runtime, Tracing} from 'aws-cdk-lib/aws-lambda';
import {Fn, Duration} from 'aws-cdk-lib';

export default function main(app) {
    // Set default runtime for all functions
    app.setDefaultFunctionProps({
        runtime: 'python3.9',
        tracing: Tracing.DISABLED
    });

    new LambdaStack(app, 'sst-stack', {prefix: "botnot-backend", name: "lambda-moonsense-webhook-api"});
}
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`botnot-lambda-moonsense-webhook-api`** capabilities aligned with **airbyte integrations** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `botnot-lambda-moonsense-webhook-api`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

# botnot-lambda-mongodb-config

**Path:** `D:/botnot/botnot-lambda-mongodb-config`  
**Category:** persistence  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# MongoDB config stack with lambda example
> the overall mongodb setup docs is here: https://app.clickup.com/25534717/v/dc/rb87x-2803/rb87x-863

### What this repo contains
- automatic network config stack deployment to create Private Network access between AWS lambda and MongoDB Atlas
  - Code: https://github.com/BotNotOrg/botnot-lambda-mongodb-config/blob/dev/src_config/network.py
  - Docs: https://app.clickup.com/25534717/v/dc/rb87x-2803/rb87x-883
- automatic authentication config stack deployment to create a shared authenticated IAM role for lambda connection to mongo
  - Code: https://github.com/BotNotOrg/botnot-lambda-mongodb-config/blob/dev/src_config/iam_auth.py 
  - Docs: https://app.clickup.com/25534717/v/dc/rb87x-2803/rb87x-903
- automatic schema en

…(truncated)…

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

### `README.md`

```
# MongoDB config stack with lambda example
> the overall mongodb setup docs is here: https://app.clickup.com/25534717/v/dc/rb87x-2803/rb87x-863

### What this repo contains
- automatic network config stack deployment to create Private Network access between AWS lambda and MongoDB Atlas
  - Code: https://github.com/BotNotOrg/botnot-lambda-mongodb-config/blob/dev/src_config/network.py
  - Docs: https://app.clickup.com/25534717/v/dc/rb87x-2803/rb87x-883
- automatic authentication config stack deployment to create a shared authenticated IAM role for lambda connection to mongo
  - Code: https://github.com/BotNotOrg/botnot-lambda-mongodb-config/blob/dev/src_config/iam_auth.py 
  - Docs: https://app.clickup.com/25534717/v/dc/rb87x-2803/rb87x-903
- automatic schema enforcement
  - Code: https://github.com/BotNotOrg/botnot-lambda-mongodb-config/blob/dev/src_config/schema.py 


### some thoughts
This is our mongodb repository; a little tutorial on mongodb

I imagine that we're going to be using atlas.


We probably want to prefer making views over using vanilla find etc. For the purposes of constructing views there are the following
operations that one may perform
```

$match
$sort
$limit
$or
$and
$eq
$ne
$gte
$lte
$not

```

The preferred method of MongoDB is to construct views and to do all processing with small atoms 


The following find indebted accounts and returns there id and name
```
"$expr" #allows us to compare fields e.g.

db.accounts.find("$expr":{"$gte": ["$debt", "$balance"]}, {"account_id":1, "name": 1})
```

For updates we need to include the selector and the operation to perform.  

```
db.test_table.update_one({"race": "oompaloopa"}, {"$set": {"gender": False}})

```


Note the use of $ to reference columns inside of `expr` 




Some notes on encrypting fields (note that encryption will affect non-matching search operations):
https://www.mongodb.com/developer/languages/python/python-quickstart-fle/
```

### `readme.md`

```
# MongoDB config stack with lambda example
> the overall mongodb setup docs is here: https://app.clickup.com/25534717/v/dc/rb87x-2803/rb87x-863

### What this repo contains
- automatic network config stack deployment to create Private Network access between AWS lambda and MongoDB Atlas
  - Code: https://github.com/BotNotOrg/botnot-lambda-mongodb-config/blob/dev/src_config/network.py
  - Docs: https://app.clickup.com/25534717/v/dc/rb87x-2803/rb87x-883
- automatic authentication config stack deployment to create a shared authenticated IAM role for lambda connection to mongo
  - Code: https://github.com/BotNotOrg/botnot-lambda-mongodb-config/blob/dev/src_config/iam_auth.py 
  - Docs: https://app.clickup.com/25534717/v/dc/rb87x-2803/rb87x-903
- automatic schema enforcement
  - Code: https://github.com/BotNotOrg/botnot-lambda-mongodb-config/blob/dev/src_config/schema.py 


### some thoughts
This is our mongodb repository; a little tutorial on mongodb

I imagine that we're going to be using atlas.


We probably want to prefer making views over using vanilla find etc. For the purposes of constructing views there are the following
operations that one may perform
```

$match
$sort
$limit
$or
$and
$eq
$ne
$gte
$lte
$not

```

The preferred method of MongoDB is to construct views and to do all processing with small atoms 


The following find indebted accounts and returns there id and name
```
"$expr" #allows us to compare fields e.g.

db.accounts.find("$expr":{"$gte": ["$debt", "$balance"]}, {"account_id":1, "name": 1})
```

For updates we need to include the selector and the operation to perform.  

```
db.test_table.update_one({"race": "oompaloopa"}, {"$set": {"gender": False}})

```


Note the use of $ to reference columns inside of `expr` 




Some notes on encrypting fields (note that encryption will affect non-matching search operations):
https://www.mongodb.com/developer/languages/python/python-quickstart-fle/
```

### `Readme.md`

```
# MongoDB config stack with lambda example
> the overall mongodb setup docs is here: https://app.clickup.com/25534717/v/dc/rb87x-2803/rb87x-863

### What this repo contains
- automatic network config stack deployment to create Private Network access between AWS lambda and MongoDB Atlas
  - Code: https://github.com/BotNotOrg/botnot-lambda-mongodb-config/blob/dev/src_config/network.py
  - Docs: https://app.clickup.com/25534717/v/dc/rb87x-2803/rb87x-883
- automatic authentication config stack deployment to create a shared authenticated IAM role for lambda connection to mongo
  - Code: https://github.com/BotNotOrg/botnot-lambda-mongodb-config/blob/dev/src_config/iam_auth.py 
  - Docs: https://app.clickup.com/25534717/v/dc/rb87x-2803/rb87x-903
- automatic schema enforcement
  - Code: https://github.com/BotNotOrg/botnot-lambda-mongodb-config/blob/dev/src_config/schema.py 


### some thoughts
This is our mongodb repository; a little tutorial on mongodb

I imagine that we're going to be using atlas.


We probably want to prefer making views over using vanilla find etc. For the purposes of constructing views there are the following
operations that one may perform
```

$match
$sort
$limit
$or
$and
$eq
$ne
$gte
$lte
$not

```

The preferred method of MongoDB is to construct views and to do all processing with small atoms 


The following find indebted accounts and returns there id and name
```
"$expr" #allows us to compare fields e.g.

db.accounts.find("$expr":{"$gte": ["$debt", "$balance"]}, {"account_id":1, "name": 1})
```

For updates we need to include the selector and the operation to perform.  

```
db.test_table.update_one({"race": "oompaloopa"}, {"$set": {"gender": False}})

```


Note the use of $ to reference columns inside of `expr` 




Some notes on encrypting fields (note that encryption will affect non-matching search operations):
https://www.mongodb.com/developer/languages/python/python-quickstart-fle/
```

### `package.json`

```
{
  "name": "mongodb-config",
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
    "@serverless-stack/cli": "1.4.0",
    "@serverless-stack/resources": "1.4.0",
    "@aws-cdk/aws-lambda-python-alpha": "2.24.0-alpha.0",
    "aws-cdk-lib": "2.24.0",
    "async": ">=2.6.4",
    "jszip": ">=3.7.0"
  }
}
```

### `sst.json`

```
{
  "name": "botnot-mongodb",
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
.env
.flake8
.github
.gitignore
.idea
README.md
layer
package.json
pytest.ini
requirements-dev.txt
src
sst.json
stacks
test
```

## 5. My contribution / role (evidence from git history — if available)

```text
290c419 2024-12-24 feat: add double type
1d3c901 2024-12-24 fix: order schema
ec6f963 2024-10-16 feat: pip
8cba86a 2024-10-16 feat: index for customer checkout in fastapi
5e07c3c 2024-09-10 feat: add step function permission
bdd8419 2024-09-09 feat: allow state machine to use this
4a82632 2024-08-29 add schema for rules (#92)
adc52d2 2024-08-29 create index for ecommerce.rules table (#91)
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`stacks/index.js`**

```text
import ConfigStack from './MongoConfigStack';
import {Runtime, Tracing} from 'aws-cdk-lib/aws-lambda';
import {Fn, Duration} from 'aws-cdk-lib';

export default function main(app) {
    // Set default runtime for all functions
    app.setDefaultFunctionProps({
        runtime: 'python3.9',
        tracing: Tracing.DISABLED
    });

    new ConfigStack(app, 'config-sst-stack');
}
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`botnot-lambda-mongodb-config`** capabilities aligned with **persistence** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `botnot-lambda-mongodb-config`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

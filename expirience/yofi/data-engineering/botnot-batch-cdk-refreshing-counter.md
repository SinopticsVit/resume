# botnot-batch-cdk-refreshing-counter

**Path:** `D:/botnot/botnot-batch-cdk-refreshing-counter`  
**Category:** data-engineering  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# Welcome to your CDK Python project!

This is a blank project for Python development with CDK.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following

…(truncated)…

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

### `README.md`

```
# Welcome to your CDK Python project!

This is a blank project for Python development with CDK.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
```

### `readme.md`

```
# Welcome to your CDK Python project!

This is a blank project for Python development with CDK.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
```

### `Readme.md`

```
# Welcome to your CDK Python project!

This is a blank project for Python development with CDK.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
```

### `requirements.txt`

```
aws-cdk-lib>=2.0.0
constructs>=10.0.0
aws-cdk.aws-codestar-alpha>=2.0.0alpha1
aws_cdk.aws_batch_alpha
aws_cdk.aws_lambda_python_alpha
pymongo~=4.2.0
```

### `Makefile`

```
all:	stack-deploy

install-deps:
	npm install

stack-build: update-dbmodels-framework install-deps
	npm run build -- --stage dev --region us-east-1 --profile dev

stack-test: stack-build
	echo npm run test

stack-deploy: stack-test
	npm run deploy -- --stage dev --region us-east-1 --profile dev

update-dbmodels-framework:
	test -d botnot-central-SQL-data-definitions/generated ||\
		git clone https://github.com/BotNotOrg/botnot-central-SQL-data-definitions
	cd botnot-central-SQL-data-definitions/generated &&\
		git pull
	cp botnot-central-SQL-data-definitions/generated/generated_billing.py\
		layer_rds/db_models/billing.py
	cp botnot-central-SQL-data-definitions/generated/generated_ecommerce.py\
		layer_rds/db_models/ecommerce.py
	diff botnot-central-SQL-data-definitions/generated/generated_billing.py\
		layer_rds/db_models/billing.py
	diff botnot-central-SQL-data-definitions/generated/generated_ecommerce.py\
		layer_rds/db_models/ecommerce.py

clean:
	rm -rf .build build
	rm -rf .pytest_cache cdk.out
	rm -rf .sst node_modules
	rm -rf src/__pycache__
	rm -rf test/__pycache__
	rm -rf botnot-central-SQL-data-definitions
	rm -f cdk.context.json
```

### `cdk.json`

```
{
  "app": "python3 app.py",
  "busket": "python3 busket.py",
  "watch": {
    "include": [
      "**"
    ],
    "exclude": [
      "README.md",
      "cdk*.json",
      "requirements*.txt",
      "source.bat",
      "**/__init__.py",
      "python/__pycache__",
      "tests"
    ]
  },
  "context": {
    "@aws-cdk/aws-apigateway:usagePlanKeyOrderInsensitiveId": true,
    "@aws-cdk/core:stackRelativeExports": true,
    "@aws-cdk/aws-rds:lowercaseDbIdentifier": true,
    "@aws-cdk/aws-lambda:recognizeVersionProps": true,
    "@aws-cdk/aws-cloudfront:defaultSecurityPolicyTLSv1.2_2021": true,
    "@aws-cdk-containers/ecs-service-extensions:enableDefaultLogDriver": true,
    "@aws-cdk/aws-ec2:uniqueImdsv2TemplateName": true,
    "@aws-cdk/core:target-partitions": [
      "aws",
      "aws-cn"
    ]
  }
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
.github
.gitignore
.idea
.python-version
Makefile
README.md
app.py
bootstrap-template.yaml
cdk.context.json
cdk.json
container
events
layer
requirements.txt
source.bat
src
venv
```

## 5. My contribution / role (evidence from git history — if available)

```text
3e44456 2022-08-17 refreshing query change gte add exist for max count
e9123e9 2022-08-16 change to shop_url and refactoring
f33cf5d 2022-08-16 change filter from shop_id to shop_url
cce11e8 2022-08-13 fis if run in yml
98a83ca 2022-08-13 add dev and prod in YML
3c03fef 2022-08-13 add dev and prod in YML
6f78829 2022-08-13 refactoring query and update
c716e18 2022-08-12 add fixing update suspended current date
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`app.py`**

```python
import os
from aws_cdk import (
    aws_ec2 as ec2,
    aws_batch_alpha as batch,
    aws_ecr_assets as assets,
    aws_ecs as ecs,
    aws_iam as iam,
    App,
    Stack,
    CfnOutput,
    aws_events as events,
    aws_events_targets as targets,
    Duration,
    Environment,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions,
    aws_lambda as lmb_tools,
    Fn
)

from aws_cdk.aws_lambda import (
    Runtime,
    Function,
    Code
)

# import aws_cdk as cdk
from constructs import Construct
# add layer to Lambda
from aws_cdk.aws_lambda_python_alpha import PythonLayerVersion
# for MongoDB
import logging
logger = logging.getLogger()


class BatchFargateStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        upload_env_name = self.node.try_get_context("uploadEnvName")
        redis_cluster_value = Fn.import_value("botnot-backend-elasticache-cluster-redis-endpoint")
        redis_cluster_port = Fn.import_value("botnot-backend-elasticache-cluster-redis-port")
        errorTopicArn = Fn.import_value("lambda-execution-error-event-sns-topic-arn")
        vps_var ="botnot-backend-global-vpc"
        mongo_instance = Fn.import_value('botnot-mongodb-instance-url-private')
        vpc = ec2.Vpc.from_lookup(self, 'ImportVPC', is_default=False, tags={"LookupName": vps_var})
        vpc_subnets = ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT)

        # To create number of Batch Compute Environment
        fargate_batch_ce = []
        name = "refcount-backend-%s-fargate-env" % upload_env_name
        fargate_spot_environment = batch.ComputeEnvironment(self, name,
                                                            compute_resources=batch.ComputeResources(
                                                                type=batch.ComputeResourceType.FARGATE,
                                                                vpc_subnets=vpc_subnets,
                                                                vpc=vpc
                                                            )
     

…(truncated)…
```

**`src/app.py`**

```python
import logging
import boto3
import json
import os

# from aws_xray_sdk.core import xray_recorder
# from aws_xray_sdk.core import patch_all

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# patch_all()
client = boto3.client('sns')
client_alarm = boto3.client('cloudwatch')


def lambda_handler(event, ctx):
    logger.warning('Data from sns:%s', json.dumps(event))
    i = 0
    for record in event['Records']:
        logger.warning(record)
        data = json.dumps(record)
        logger.warning('Message:%s',record['Sns']['Message'])
        massage=json.loads(record['Sns']['Message'])
        logger.warning(f'massage:{massage}')
        account=massage['account']
        time=massage['time']
        batch_name=massage['detail']['jobName']
                # account=massage.get("account",None)
        logger.warning(f'account:{account},{time},{batch_name}')
        batch_alert=f'Batch Job Execution falied: {batch_name}'
        sns_log={"version": "0",
                "id": massage['account'],
                "detail-type": batch_alert,
                "source": massage['source'],
                "account":account ,
                "time": time,
                "region": "us-east-1",
                "resources": [],
                "detail": massage['detail']
                }
        logger.warning(f'Publish alert: {sns_log}')
        # client.publish(
        #     TargetArn=os.environ['SNS_TOPIC_EMAIL'],
        #     Message=json.dumps({'default': batch_alert}),
        #     MessageStructure='json'
        # )
        client.publish(
             TargetArn=os.environ['SNS_TOPIC2'],
            #  Message=json.dumps({'default': json.dumps(record['Sns']['Message'])}),
            Message=json.dumps({'default': json.dumps(sns_log)}),
             MessageStructure='json'
         )
    logger.warning('Successfully finished function')
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`botnot-batch-cdk-refreshing-counter`** capabilities aligned with **data engineering** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `botnot-batch-cdk-refreshing-counter`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

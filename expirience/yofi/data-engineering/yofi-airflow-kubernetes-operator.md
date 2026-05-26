# yofi-airflow-kubernetes-operator

**Path:** `D:/botnot/yofi-airflow-kubernetes-operator`  
**Category:** data-engineering  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# Airflow-Kubernetes Job Orchestration

An architecture for data processing workflows using Airflow for orchestration and GKE (Google Kubernetes Engine) for executing compute jobs.

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

### `README.md`

```
# Airflow-Kubernetes Job Orchestration

An architecture for data processing workflows using Airflow for orchestration and GKE (Google Kubernetes Engine) for executing compute jobs.

## Project Structure

```text
📁 BotNotOrg/yofi-airflow-kubernetes-operator (this repo)
├── task_images/
│   └── [task_name]/
│       ├── src/
│       │   └── main.py              # Example Python script
│       ├── Dockerfile               # Docker image for example
│       ├── .dockerignore            # Docker ignore file
│       └── requirements.txt         # Dependencies for example
├── cloudbuild/
│   ├── cloudbuild.yaml              # CloudBuild configuration
│   └── scripts/
│       └── build_images.sh          # Script to build Docker images
└── README.md                        # This file

📁 BotNotOrg/yofi-airflow-codebase
├── dags/
│   └── tools/
│       └── kpo.py                   # Helper for creating KubernetesPodOperator tasks
```

> [!IMPORTANT]
> The Airflow DAGs and configurations are maintained in a separate repository at [https://github.com/BotNotOrg/yofi-airflow-codebase](https://github.com/BotNotOrg/yofi-airflow-codebase).

## Using the System

### Adding a New Task

- In this repository (yofi-airflow-kubernetes-operator):

  1. Create a new directory under `task_images/` with your task name
  2. Set up the Python project structure:
     - Create a `src/` directory with your Python script(s), starting with `main.py`
     - Add `Dockerfile`, `.dockerignore`, and `requirements.txt`
  3. Update the CloudBuild configuration:
     - Add the new project image names (both latest and short_sha) to the `cloudbuild.yaml`:
       - `'${IMAGE_REPOSITORY}/[task_name]:${SHORT_SHA}'`
       - `'${IMAGE_REPOSITORY}/[task_name]:latest'`

- In the Airflow repository (yofi-airflow-codebase), use the following code template to create a KPO task:

    ```py
    from airflow.models.variable import Variable
    from tools.kpo import create_kpo_task

    PROJECT_ID: str = Variable.get("project_id")
    IMAGE_REPOSITORY: str = (
        f"us-central1-docker.pkg.dev/{PROJECT_ID}/yofi-batch-airflow-pods"
    )

    task = create_kpo_task(
        task_id="kpo_task_name",
        image=f"{IMAGE_REPOSITORY}/task_name:latest",
        arguments=["--option1", "value1", "--option2", "value2"],
        env_vars={"ENV_VAR1": "value1", "ENV_VAR2": "value2"}
    )
    ```

An example of a KPO task is available at [BotNotOrg/yofi-data-eng-scripts/kpo_example](https://github.com/BotNotOrg/yofi-data-eng-scripts/tree/main/kpo_example).

### Best Practices for Task Arguments

When designing tasks, follow these best practices for handling arguments and environment variables:

#### Essential Arguments

Include this argument in your task implementations to ensure proper environment separation and allow local testing:

- **`--project-id`**: The Google Cloud project ID where resources (BigQuery, GCS, etc.) are located
  - Corresponds to the PROJECT_ID airflow variable
  - Example: `--project-id=yofi-prod-environment` or `--project-id=yofi-dev-environment`

### Image creation

New images are

…(truncated)…
```

### `readme.md`

```
# Airflow-Kubernetes Job Orchestration

An architecture for data processing workflows using Airflow for orchestration and GKE (Google Kubernetes Engine) for executing compute jobs.

## Project Structure

```text
📁 BotNotOrg/yofi-airflow-kubernetes-operator (this repo)
├── task_images/
│   └── [task_name]/
│       ├── src/
│       │   └── main.py              # Example Python script
│       ├── Dockerfile               # Docker image for example
│       ├── .dockerignore            # Docker ignore file
│       └── requirements.txt         # Dependencies for example
├── cloudbuild/
│   ├── cloudbuild.yaml              # CloudBuild configuration
│   └── scripts/
│       └── build_images.sh          # Script to build Docker images
└── README.md                        # This file

📁 BotNotOrg/yofi-airflow-codebase
├── dags/
│   └── tools/
│       └── kpo.py                   # Helper for creating KubernetesPodOperator tasks
```

> [!IMPORTANT]
> The Airflow DAGs and configurations are maintained in a separate repository at [https://github.com/BotNotOrg/yofi-airflow-codebase](https://github.com/BotNotOrg/yofi-airflow-codebase).

## Using the System

### Adding a New Task

- In this repository (yofi-airflow-kubernetes-operator):

  1. Create a new directory under `task_images/` with your task name
  2. Set up the Python project structure:
     - Create a `src/` directory with your Python script(s), starting with `main.py`
     - Add `Dockerfile`, `.dockerignore`, and `requirements.txt`
  3. Update the CloudBuild configuration:
     - Add the new project image names (both latest and short_sha) to the `cloudbuild.yaml`:
       - `'${IMAGE_REPOSITORY}/[task_name]:${SHORT_SHA}'`
       - `'${IMAGE_REPOSITORY}/[task_name]:latest'`

- In the Airflow repository (yofi-airflow-codebase), use the following code template to create a KPO task:

    ```py
    from airflow.models.variable import Variable
    from tools.kpo import create_kpo_task

    PROJECT_ID: str = Variable.get("project_id")
    IMAGE_REPOSITORY: str = (
        f"us-central1-docker.pkg.dev/{PROJECT_ID}/yofi-batch-airflow-pods"
    )

    task = create_kpo_task(
        task_id="kpo_task_name",
        image=f"{IMAGE_REPOSITORY}/task_name:latest",
        arguments=["--option1", "value1", "--option2", "value2"],
        env_vars={"ENV_VAR1": "value1", "ENV_VAR2": "value2"}
    )
    ```

An example of a KPO task is available at [BotNotOrg/yofi-data-eng-scripts/kpo_example](https://github.com/BotNotOrg/yofi-data-eng-scripts/tree/main/kpo_example).

### Best Practices for Task Arguments

When designing tasks, follow these best practices for handling arguments and environment variables:

#### Essential Arguments

Include this argument in your task implementations to ensure proper environment separation and allow local testing:

- **`--project-id`**: The Google Cloud project ID where resources (BigQuery, GCS, etc.) are located
  - Corresponds to the PROJECT_ID airflow variable
  - Example: `--project-id=yofi-prod-environment` or `--project-id=yofi-dev-environment`

### Image creation

New images are

…(truncated)…
```

### `Readme.md`

```
# Airflow-Kubernetes Job Orchestration

An architecture for data processing workflows using Airflow for orchestration and GKE (Google Kubernetes Engine) for executing compute jobs.

## Project Structure

```text
📁 BotNotOrg/yofi-airflow-kubernetes-operator (this repo)
├── task_images/
│   └── [task_name]/
│       ├── src/
│       │   └── main.py              # Example Python script
│       ├── Dockerfile               # Docker image for example
│       ├── .dockerignore            # Docker ignore file
│       └── requirements.txt         # Dependencies for example
├── cloudbuild/
│   ├── cloudbuild.yaml              # CloudBuild configuration
│   └── scripts/
│       └── build_images.sh          # Script to build Docker images
└── README.md                        # This file

📁 BotNotOrg/yofi-airflow-codebase
├── dags/
│   └── tools/
│       └── kpo.py                   # Helper for creating KubernetesPodOperator tasks
```

> [!IMPORTANT]
> The Airflow DAGs and configurations are maintained in a separate repository at [https://github.com/BotNotOrg/yofi-airflow-codebase](https://github.com/BotNotOrg/yofi-airflow-codebase).

## Using the System

### Adding a New Task

- In this repository (yofi-airflow-kubernetes-operator):

  1. Create a new directory under `task_images/` with your task name
  2. Set up the Python project structure:
     - Create a `src/` directory with your Python script(s), starting with `main.py`
     - Add `Dockerfile`, `.dockerignore`, and `requirements.txt`
  3. Update the CloudBuild configuration:
     - Add the new project image names (both latest and short_sha) to the `cloudbuild.yaml`:
       - `'${IMAGE_REPOSITORY}/[task_name]:${SHORT_SHA}'`
       - `'${IMAGE_REPOSITORY}/[task_name]:latest'`

- In the Airflow repository (yofi-airflow-codebase), use the following code template to create a KPO task:

    ```py
    from airflow.models.variable import Variable
    from tools.kpo import create_kpo_task

    PROJECT_ID: str = Variable.get("project_id")
    IMAGE_REPOSITORY: str = (
        f"us-central1-docker.pkg.dev/{PROJECT_ID}/yofi-batch-airflow-pods"
    )

    task = create_kpo_task(
        task_id="kpo_task_name",
        image=f"{IMAGE_REPOSITORY}/task_name:latest",
        arguments=["--option1", "value1", "--option2", "value2"],
        env_vars={"ENV_VAR1": "value1", "ENV_VAR2": "value2"}
    )
    ```

An example of a KPO task is available at [BotNotOrg/yofi-data-eng-scripts/kpo_example](https://github.com/BotNotOrg/yofi-data-eng-scripts/tree/main/kpo_example).

### Best Practices for Task Arguments

When designing tasks, follow these best practices for handling arguments and environment variables:

#### Essential Arguments

Include this argument in your task implementations to ensure proper environment separation and allow local testing:

- **`--project-id`**: The Google Cloud project ID where resources (BigQuery, GCS, etc.) are located
  - Corresponds to the PROJECT_ID airflow variable
  - Example: `--project-id=yofi-prod-environment` or `--project-id=yofi-dev-environment`

### Image creation

New images are

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
.gitignore
README.md
cloudbuild
roles
task_images
```

## 5. My contribution / role (evidence from git history — if available)

```text
cdf3d2c 2025-09-09 Merge pull request #24 from BotNotOrg/dev
9752fde 2025-09-09 chore: update package versions
047889f 2025-08-21 Merge pull request #23 from BotNotOrg/dev
21e2ca4 2025-08-20 Merge pull request #22 from BotNotOrg/feat/add-notifications
6297108 2025-08-20 chore: add debug print statement for CONFIG in send_notification.py
0c18fd7 2025-08-19 Merge pull request #21 from BotNotOrg/feat/add-notifications
e675e18 2025-08-19 chore: add GITHUB_TOKEN as build argument in Dockerfile and build script
417df80 2025-08-19 Merge pull request #20 from BotNotOrg/feat/add-notifications
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`task_images/notification-service-sender/main.py`**

```python
#!/usr/bin/env python3

import sys
import json
from src import send_notification_from_env


def main():
    """
    Main entry point for the notification service Docker container.
    Reads configuration from environment variables and sends notifications.
    """
    print("Starting notification service...")
    
    try:
        result = send_notification_from_env()
        
        print(f"Notification service result: {json.dumps(result, indent=2)}")
        
        if result["success"]:
            print("Notification service completed successfully")
            sys.exit(0)
        else:
            print("Notification service completed with errors")
            sys.exit(1)
            
    except Exception as e:
        print(f"Critical error in notification service: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```

**`task_images/order-protection-claim-image-analysis/src/main.py`**

```python
#!/usr/bin/env python
"""
Image Analysis for Order Protection Claims.

This script downloads images from GCS URLs stored in BigQuery, extracts metadata,
computes image hashes, and uploads the results back to BigQuery for use in fraud detection.

The script supports both full refresh and incremental processing modes:
- Full refresh: Process all images in the source table
- Incremental: Process only new images not already in the target table

Features:
- Parallel downloading of images from GCS
- Parallel processing of images using multiprocessing
- Extraction of EXIF metadata including device info and GPS coordinates
- Computation of perceptual hash (phash) for image similarity detection

Environment:
- Requires Google Cloud credentials for BigQuery and GCS access

Usage:
  python main.py [--full-refresh] [--cache-dir DIR]
                 [--download-workers N] [--processing-workers N]

Options:
  --project-id           Project ID (default: PROJECT_ID environment variable)
  --full-refresh         Process all images, ignoring existing data
  --cache-dir            Directory to store cached images (default: .cache/op_images)
  --download-workers     Number of concurrent download workers (default: 16)
  --processing-workers   Number of concurrent image processing workers (default: CPU count)
"""

import argparse
import json
import multiprocessing
import os
from datetime import datetime
from typing import Any

import exif
import numpy as np
from google.cloud import bigquery, storage
from tqdm.auto import tqdm

from gcs_utils import download_images_bulk
from image_processor import ImageProcessor

# Database table configuration
SOURCE_TABLE_FORMAT = "{project_id}.dw_order_protection.claim_item_image"
TARGET_TABLE_FORMAT = (
    "{project_id}.dw_delta_order_protection.order_protection_image_info"
)

# BigQuery schema definition for the target table
SCHEMA = [
    bigquery.SchemaField("url", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("created_at", "TIMESTAMP"),
    bigquery.SchemaField("created_at_offset", "FLOAT"),
    bigquery.SchemaField("modified_at", "TIMESTAMP"),
    bigquery.

…(truncated)…
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`yofi-airflow-kubernetes-operator`** capabilities aligned with **data engineering** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yofi-airflow-kubernetes-operator`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

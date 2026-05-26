# yofi-data-eng-scripts

**Path:** `D:/botnot/yofi-data-eng-scripts`  
**Category:** data-engineering  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# yofi-data-eng-scripts
Contains ad-hoc, experimental and local scripts used for data engineering processes

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

### `README.md`

```
# yofi-data-eng-scripts
Contains ad-hoc, experimental and local scripts used for data engineering processes
```

### `readme.md`

```
# yofi-data-eng-scripts
Contains ad-hoc, experimental and local scripts used for data engineering processes
```

### `Readme.md`

```
# yofi-data-eng-scripts
Contains ad-hoc, experimental and local scripts used for data engineering processes
```

### `pyproject.toml`

```
[project]
name = "yofi-data-eng-scripts"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "boto3>=1.37.35",
    "dotenv>=0.9.9",
    "google-cloud-bigquery>=3.31.0",
    "google-cloud-bigquery-storage>=2.31.0",
    "google-cloud-secret-manager>=2.23.2",
    "google-cloud-storage>=3.1.0",
    "ipykernel>=6.29.5",
    "pandas-gbq>=0.28.0",
    "pymongo[srv]>=4.12.1",
    "tqdm>=4.67.1",
]
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
.python-version
17track_extract
README.md
address_normalization
airbyte_api
bad_actor_scraper
copy_dataset
ebay_embeddings
order_protection
pyproject.toml
uv.lock
wcc_clustering_address
```

## 5. My contribution / role (evidence from git history — if available)

```text
68ab76d 2025-07-07 Merge pull request #10 from BotNotOrg/feat/add_wcc
d26c13d 2025-07-07 add wcc
bb849f1 2025-06-04 Merge pull request #9 from BotNotOrg/feat/airbyte_api_scripts
7ae177a 2025-06-02 feat: add notebooks for interaction with airbyte API
359a365 2025-04-30 Merge pull request #6 from BotNotOrg/feat/add-script-to-copy-datasets
8666d6d 2025-04-30 feat: add BigQuery dataset copier script with usage documentation
c806d27 2025-04-23 Merge pull request #5 from BotNotOrg/feat/add_17track
502bbe5 2025-04-23 feat: update 17track script for shopify
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`bad_actor_scraper/main.py`**

```python
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
import asyncio
import time
import aiohttp
import gcsfs
from aiohttp import ClientSession
import functions_framework


# Retry parameters
MAX_RETRIES = 5
BACKOFF_FACTOR = 0.5

# GCS settings
BUCKET_NAME = 'tmp-miura'  # replace with your bucket name
INPUT_FILE = 'turn5_sample_2.csv'

POST_REQUEST_SLEEP_SECONDS = 0.2

async def fetch_with_retry(session, url, params=None):
    retries = 0
    while retries < MAX_RETRIES:
        try:
            async with session.get(url, params=params) as response:
                response.raise_for_status()
                return await response.text()
        except (aiohttp.ClientError, aiohttp.http_exceptions.HttpProcessingError) as e:
            retries += 1
            wait_time = BACKOFF_FACTOR * (2 ** retries)
            print(f"Error fetching {url}: {e}. Retrying in {wait_time} seconds...")
            await asyncio.sleep(wait_time)
    raise Exception(f"Failed to fetch {url} after {MAX_RETRIES} retries")

async def search_bad_buyer_list(session, search_term, source):
    base_url = "https://badbuyerlist.org/search"
    response_text = await fetch_with_retry(session, base_url, params={"q": search_term})

    time.sleep(POST_REQUEST_SLEEP_SECONDS)

    print(f"Searching for: {search_term}")

    soup = BeautifulSoup(response_text, 'html.parser')
    table = soup.find("table")
    matches = []

    if table:
        rows = table.find_all("tr")[1:]  # Skip header row
        for row in rows:
            columns = row.find_all("td")
            if len(columns) >= 4:  # Ensure there are enough columns
                name = columns[0].text.strip()
                email = columns[1].text.strip()
                phone = columns[2].text.strip() if len(columns) > 2 else ""
                reported_at = columns[3].text.strip() if len(columns) > 3 else ""
                link = columns[0].find('a')['href']
                details = await get_buyer_details(session, f"https://badbuyerlist.org{link}")
                match = {
                    "name": name,

…(truncated)…
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`yofi-data-eng-scripts`** capabilities aligned with **data engineering** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yofi-data-eng-scripts`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

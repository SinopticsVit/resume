# yofi-admin-slackbot

**Path:** `D:/botnot/yofi-admin-slackbot`  
**Category:** frontend  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

Internal **Yofi** repository `yofi-admin-slackbot` under category **frontend**. Supports Yofi/Botnot platform capabilities (e-commerce intelligence, anti-fraud adjacent services, data plane, or infrastructure) as evidenced by repository layout and manifests.

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

### `package.json`

```
{
  "name": "yofi-admin-slackbot",
  "version": "0.0.1",
  "private": true,
  "eslintConfig": {
    "extends": [
      "serverless-stack"
    ]
  },
  "dependencies": {
    "sst": "^2.41.2",
    "constructs": "^10.3.0",
    "@aws-cdk/aws-lambda-python-alpha": "^2.133.0-alpha.0",
    "aws-cdk-lib": "^2.133.0"
  }
}
```

### `sst.config.ts`

```
import type { SSTConfig } from "sst"
import { Tracing } from 'aws-cdk-lib/aws-lambda';
import {AdminToolsStack} from "./stacks/admin_tools";


export default {
  config(input) {
    return {
      name: "yofi-admin-slackbot",
      region: "us-east-1",
      profile: input.stage === "prod" ? "prod" : "dev",
    }
  },
  stacks(app) {
    app.setDefaultFunctionProps({
        // handler: 'src/lambda.handler',
        runtime: 'python3.11',
        tracing: "active",
        timeout: 30,
        permissions: [
            'secretsmanager:*',
            'rds:*',
            'rds-data:*',
            'rds-db:*',
            'sns:*',
            'elasticache:*',
            'dynamodb:*',
            'xray:*',
        ]
    })

    app.stack(AdminToolsStack) // name like: {app}-AdminToolsStack
  },
} satisfies SSTConfig
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
_MK_old_code_for_GCP
layer
package.json
seed.yml
src
sst.config.ts
stacks
```

## 5. My contribution / role (evidence from git history — if available)

```text
bb5c130 2024-03-19 add todo
5527251 2024-03-19 feat: use function url
ec64e03 2024-03-19 fix: text
f0262b4 2024-03-19 fix: message
6de80ba 2024-03-19 fix: prefix
78a9d6b 2024-03-19 fix: env
0457b86 2024-03-19 feat: add ENV
6adc919 2024-03-19 feat: ready for PROD
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`_MK_old_code_for_GCP/src/discord_monitor/main.py`**

```python
from ast import parse
import os
import shutil
from .match_to_orders import run_matching, get_high_confidence_matches
from .run_many import run_from_date
from .parse_bot_discord_chat_log import bulk_parse
import pandas as pd
import datetime as dt

def archive_previous_export(in_path="discord_monitor/exports/json", out_path="discord_monitor/exports/old_json"):
    files = os.listdir(in_path)
    for file in files:
        if ".json" in file:
            in_file = os.path.join(in_path, file)
            out_file = os.path.join(out_path, file)
            shutil.move(in_file, out_file)

def export_latest(discord_token, parsed_logs_path="discord_monitor/exports/csv/", raw_logs_path="discord_monitor/exports/json/"):
    latest_date = pd.to_datetime("2011-01-01", utc=True)
    have_previous_export = False
    files = os.listdir(parsed_logs_path)
    for file in files:
        if ".csv" in file:
            have_previous_export = True
            file_path = os.path.join(parsed_logs_path, file)
            data = pd.read_csv(file_path)
            _date = pd.to_datetime(data['message_time'], utc=True).max()
            latest_date = max([_date, latest_date])
    print(f"got latest date: {latest_date}")
    run_date = latest_date - dt.timedelta(days=1)
    run_date = run_date.date()
    if not have_previous_export:
        run_date = None
    print(f"running since {run_date}.")
    run_from_date(discord_token, export_path=raw_logs_path, date=run_date)

def collect_all_logs(parsed_logs_path="discord_monitor/exports/csv/"):
    files = os.listdir(parsed_logs_path)
    output = []
    for file in files:
        if "-checkout-log.csv" in file:
            filepath = os.path.join(parsed_logs_path, file)
            name = file.replace("-checkout-log.csv", "")
            _df = pd.read_csv(filepath)
            _df['bot_used'] = name
            output.append(_df)
    return pd.concat(output)


def parse_latest(parsed_logs_path="discord_monitor/exports/csv/", raw_logs_path="discord_monitor/exports/json/"):
    bulk_parse(input_path=raw_logs_path, output_path=parsed_logs_path)

def main(discord_token, app=N

…(truncated)…
```

**`_MK_old_code_for_GCP/src/raffles/main.py`**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from tqdm import tqdm
from datetime import datetime
from Levenshtein import distance
import requests

from .datalake import run_sql
from .seedcms import fetch_campaigns_for_shop
from .mongo import get_latest_line_items, get_mongo_client

url = "https://us-central1-launches-by-seed.cloudfunctions.net/partnerGetSubmissions"
# campaign_id = "OzZQ7HpQuQckiI2OChou"
params = {
    "id":"",
    "limit":1000,
    "page":1
}

def get_customer_address(row):
    co = row.get('customer_object')
    if isinstance(co, str):
        co = json.loads(co)
    addresses = co.get('addresses')
    if len(addresses) > 0:
        address = addresses[0]
    else:
        address = {
            'first_name': "None", 
            "last_name":"None", 
            'country':"None"
        }
    return address

def map_api_resp(df, shop_url):
    df['shop_url'] = shop_url
    df['domain'] = df['domain_name']
    df['account_verified'] = df['shopify_account_verified']
    df['address'] = None#df.apply(lambda x: get_customer_address(x), axis=1)
    df['capcha_results'] = None
    df['created_at'] = pd.to_datetime(df['created_at'], utc=True)
    df['secret_id'] = df['id'].astype(str)
    keep_cols = list(df.columns)
    keep_cols = safe_remove_from_list(keep_cols, 'castle_request_token') #.remove('castle_request_token')
    keep_cols = safe_remove_from_list(keep_cols, 'customer_message')#.remove('customer_message')
    df = df[keep_cols]
    return df

def safe_remove_from_list(l, value):
    if value in l:
        l.remove(value)
    return 

to_remove = [
    'customer_message',
    'geo_location',
    'customer_object',
    'castle_request_token',
    'castle_signals'
]

def remove_fields(x, to_remove=to_remove):
    out = dict()
    for key in x:
        if key not in to_remove:
            out[key] = x[key]
    return out

def download_campaign(campaign_id, shop_url=None):

    print(f'downloading campaign {campaign_id} for shop {shop_url or "unknown shop"}.')

    submissions = []
    params['id'] = campaign_id

…(truncated)…
```

**`_MK_old_code_for_GCP/src/segments/main.py`**

```python
from itertools import combinations

from google.cloud import bigquery
import pandas as pd
import networkx as nx
from tqdm import tqdm
from fuzzywuzzy import process
import time
from .klaviyo import get_klaviyo_profiles_for_email_list, creds
from .datalake import get_max_bot_risks_for_shop
from .mongo import get_mongo_client, get_latest_line_items_for_shop

def export_cp_for_shop(shop_url, since_date="2000-01-0"):
    client = bigquery.Client(
        project="yofi-prod-environment"
    )
    # get cutoff date 180 days ago
    cutoff_date = time.strftime('%Y-%m-%d', time.gmtime(time.time() - 60 * 60 * 24 * 180))
    sql = f"""
    SELECT od.id, customer.email, title, od.created_at FROM `yofi-prod-environment.dw_ecommerce.line_items` li JOIN `yofi-prod-environment.dw_ecommerce.order` od ON od._id = li._order_id WHERE od.shop_url like '{shop_url}' AND od.created_at > '{cutoff_date}' ORDER BY od.created_at DESC LIMIT 88000
    """
    df = client.query(sql).to_dataframe()
    mongo_client = get_mongo_client()
    # latest_df = get_latest_line_items_for_shop(mongo_client, shop_url, since_date="2000-01-1")
    latest_df = get_latest_line_items_for_shop(mongo_client, shop_url)
    if latest_df is not None:
        output_df = pd.concat([df, latest_df])
    else:
        print("no recent records found in mongo...")
        output_df = df
    # output_df = latest_df
    print(f"outputting {len(output_df)} line item records...")
    return output_df

def custom_weighted_projected_graph(g, nodes):
    out_edges = dict()
    all_neighbors = []
    print('fetching neighbors...')
    for node in tqdm(nodes):
        edges = g.edges(node)
        neighbors = []
        for edge in edges:
            neighbors.append(edge[1])
        all_neighbors.extend(neighbors)
    all_neighbors = list(set(all_neighbors))
    right_nodes = all_neighbors
    print('projecting bipartite graph...')
    for node in tqdm(right_nodes):
        edges = g.edges(node)
        neighbors = []
        for edge in edges:
            neighbors.append(edge[1])
        combs = [x for x in combinations(neighbors, 2) if x[0] != x[1]]
  

…(truncated)…
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`yofi-admin-slackbot`** capabilities aligned with **frontend** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yofi-admin-slackbot`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

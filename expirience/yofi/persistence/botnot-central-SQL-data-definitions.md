# botnot-central-SQL-data-definitions

**Path:** `D:/botnot/botnot-central-SQL-data-definitions`  
**Category:** persistence  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# SQL-DDL generation of MoonGodess and other members of the pentaguard

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

### `README.md`

```
# SQL-DDL generation of MoonGodess and other members of the pentaguard
## Background and Motivation

### "_One Definition To Rule Them All_" - Andrii (a.k.a. Man of Gucci)
 
The most common repeated form of failure at scale is (in my experience) out of sync data definitions.
 The goal of this package is to solve this issue.  From table DDL python sqlalchemy is generated (in addition to
some necesary SQL).  Several alterations are made to accomodate our most common usage (as enumerated below)


## Usage 
You can find the table definitions within
the ```Tables``` class in ```tables.py```. Each independent table may be a json object
or string, in the event of the latter (json) the following keys are used

#### *table*
* The SQL Table definition
#### *unique_indices* 
* Unique indices around which retrieval functions are build. At the moment only one unique index is used.
#### *representation_columns*
* Columns to appear in the ```__repr__``` method of the class
#### *index_mappings*
    A map of id columns to representative tables named in a non standard way.  
 * An example of this is billing_address and shipping_address in the ecommerce_customers table.  Standard naming would entail 

 * The non-id suffixed name will be retrievable as
 its sql class from a ```get_{idless_column_name}(session)``` (e.g. get_cow(session) from cow_id in the table ecommerce_cows), 
 where session is a database session.  If this class is altered it must be upserted on its own
#### *dictionary_remappings*
In the event that a json dictionary is passed as ```**kwargs``` to initialize the SQLAlchemy record this dictionary is used to remap the arguments to the attributes as shown below:
```python
class Something(Base):
  def __init__(self, **kwargs):
    self.__dict__.update({dictionary_remappings[k] if k in dictionary_remappings else k : v for k,v in kwargs.items()})
```
### Invocation
From the aforementioned parameters sqlalchemy classes are generated in addition to sql. To use run the file ```main.py```  

Scripts here are designed to fail loudly; when unknown operating conditions are experienced they are designed to throw
an error.  For those who update this library please continue in this tradition.  The goal of these at the moment is to serve as a 
sane jumping off point for insertions into external libraries but more will come.


## General Naming Conventions ##
* SQL Tables are prefixed with ```ecommerce_``` or ```billing_``` and suffixed with the language appropriate ```s``` or ```es```
* The python class names are not.  Note that 
* A _uid suffix indicates that the integer corresponds to an unique external ID


## Code Generation
To generate the sql, python, and (least of all) javascript use the ```python main.py``` script.
To have a convenient 

## Using Generated Code



## SCHEMA notes 
 * Most relevant order mutations should be present in the ```ecommerce_post_order_modification``` table. 
 * Try to track important account mutations (and keep track of e.g. historic addresses) 
 * For any table that does not include partner_id the id is expected to correspond to an internal id 


…(truncated)…
```

### `readme.md`

```
# SQL-DDL generation of MoonGodess and other members of the pentaguard
## Background and Motivation

### "_One Definition To Rule Them All_" - Andrii (a.k.a. Man of Gucci)
 
The most common repeated form of failure at scale is (in my experience) out of sync data definitions.
 The goal of this package is to solve this issue.  From table DDL python sqlalchemy is generated (in addition to
some necesary SQL).  Several alterations are made to accomodate our most common usage (as enumerated below)


## Usage 
You can find the table definitions within
the ```Tables``` class in ```tables.py```. Each independent table may be a json object
or string, in the event of the latter (json) the following keys are used

#### *table*
* The SQL Table definition
#### *unique_indices* 
* Unique indices around which retrieval functions are build. At the moment only one unique index is used.
#### *representation_columns*
* Columns to appear in the ```__repr__``` method of the class
#### *index_mappings*
    A map of id columns to representative tables named in a non standard way.  
 * An example of this is billing_address and shipping_address in the ecommerce_customers table.  Standard naming would entail 

 * The non-id suffixed name will be retrievable as
 its sql class from a ```get_{idless_column_name}(session)``` (e.g. get_cow(session) from cow_id in the table ecommerce_cows), 
 where session is a database session.  If this class is altered it must be upserted on its own
#### *dictionary_remappings*
In the event that a json dictionary is passed as ```**kwargs``` to initialize the SQLAlchemy record this dictionary is used to remap the arguments to the attributes as shown below:
```python
class Something(Base):
  def __init__(self, **kwargs):
    self.__dict__.update({dictionary_remappings[k] if k in dictionary_remappings else k : v for k,v in kwargs.items()})
```
### Invocation
From the aforementioned parameters sqlalchemy classes are generated in addition to sql. To use run the file ```main.py```  

Scripts here are designed to fail loudly; when unknown operating conditions are experienced they are designed to throw
an error.  For those who update this library please continue in this tradition.  The goal of these at the moment is to serve as a 
sane jumping off point for insertions into external libraries but more will come.


## General Naming Conventions ##
* SQL Tables are prefixed with ```ecommerce_``` or ```billing_``` and suffixed with the language appropriate ```s``` or ```es```
* The python class names are not.  Note that 
* A _uid suffix indicates that the integer corresponds to an unique external ID


## Code Generation
To generate the sql, python, and (least of all) javascript use the ```python main.py``` script.
To have a convenient 

## Using Generated Code



## SCHEMA notes 
 * Most relevant order mutations should be present in the ```ecommerce_post_order_modification``` table. 
 * Try to track important account mutations (and keep track of e.g. historic addresses) 
 * For any table that does not include partner_id the id is expected to correspond to an internal id 


…(truncated)…
```

### `Readme.md`

```
# SQL-DDL generation of MoonGodess and other members of the pentaguard
## Background and Motivation

### "_One Definition To Rule Them All_" - Andrii (a.k.a. Man of Gucci)
 
The most common repeated form of failure at scale is (in my experience) out of sync data definitions.
 The goal of this package is to solve this issue.  From table DDL python sqlalchemy is generated (in addition to
some necesary SQL).  Several alterations are made to accomodate our most common usage (as enumerated below)


## Usage 
You can find the table definitions within
the ```Tables``` class in ```tables.py```. Each independent table may be a json object
or string, in the event of the latter (json) the following keys are used

#### *table*
* The SQL Table definition
#### *unique_indices* 
* Unique indices around which retrieval functions are build. At the moment only one unique index is used.
#### *representation_columns*
* Columns to appear in the ```__repr__``` method of the class
#### *index_mappings*
    A map of id columns to representative tables named in a non standard way.  
 * An example of this is billing_address and shipping_address in the ecommerce_customers table.  Standard naming would entail 

 * The non-id suffixed name will be retrievable as
 its sql class from a ```get_{idless_column_name}(session)``` (e.g. get_cow(session) from cow_id in the table ecommerce_cows), 
 where session is a database session.  If this class is altered it must be upserted on its own
#### *dictionary_remappings*
In the event that a json dictionary is passed as ```**kwargs``` to initialize the SQLAlchemy record this dictionary is used to remap the arguments to the attributes as shown below:
```python
class Something(Base):
  def __init__(self, **kwargs):
    self.__dict__.update({dictionary_remappings[k] if k in dictionary_remappings else k : v for k,v in kwargs.items()})
```
### Invocation
From the aforementioned parameters sqlalchemy classes are generated in addition to sql. To use run the file ```main.py```  

Scripts here are designed to fail loudly; when unknown operating conditions are experienced they are designed to throw
an error.  For those who update this library please continue in this tradition.  The goal of these at the moment is to serve as a 
sane jumping off point for insertions into external libraries but more will come.


## General Naming Conventions ##
* SQL Tables are prefixed with ```ecommerce_``` or ```billing_``` and suffixed with the language appropriate ```s``` or ```es```
* The python class names are not.  Note that 
* A _uid suffix indicates that the integer corresponds to an unique external ID


## Code Generation
To generate the sql, python, and (least of all) javascript use the ```python main.py``` script.
To have a convenient 

## Using Generated Code



## SCHEMA notes 
 * Most relevant order mutations should be present in the ```ecommerce_post_order_modification``` table. 
 * Try to track important account mutations (and keep track of e.g. historic addresses) 
 * For any table that does not include partner_id the id is expected to correspond to an internal id 


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
README.md
__init__.py
drop.py
generated
main.py
make_up.sh
requirements_hard.txt
setup.py
src
test
yass_daddy.json
```

## 5. My contribution / role (evidence from git history — if available)

```text
3c3fcd5 2022-08-11 fix: order schema
4cae43f 2022-08-10 fix: expand fields
f1c1a94 2022-08-10 feat: add billing.notification
d5199b1 2022-08-10 fix: change lineitems
f1f7535 2022-08-09 fix: makes ml-order-state-prediction as a object not array
9f3f04f 2022-08-05 format: use format after run main.py
98b89d2 2022-08-05 revert: order schema back to commit/3e9619bda534201c10244cc0398e3f6e864cc262
1884c56 2022-08-05 * add client_details to mongodb schema for ecommerce.order
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`main.py`**

```python
import os
import pathlib
from json import dump, load
from os import makedirs, path

from pymongo.errors import CollectionInvalid

from src.sql_translate_to_json import make_json_sql_retrieval_function, make_mongodb_validator
from src.sql_translate_to_python_etc import table_def_to_sql_alchemy_sql, write_imports, TableParser, \
  sql_table_python_class_name, get_tbl_as_dict, real_ends_with, strip_table_name
from src.template.tables import Tables
from src.template.billing_tables import Tables as BillingTables
from typing import List, Dict, Union, Iterable, Set

import re

INDICE_FINALS = set()

def make_index_name(tb_name: str, ind: List[str], creation=False):
  global INDICE_FINALS
  t = "_".join([tb_name] + [x.lower() for x in ind])
  if len(t) < 64:
    assert not creation or t not in INDICE_FINALS, f"Should not have {t} already present"
    INDICE_FINALS.add(t)
    return t
  else:
    new_t = t[:63]
    assert not creation or new_t not in INDICE_FINALS, f"Should not have {t} already present"
    return new_t

def make_index_text(tb_name: str, ind: List[str], col_rev: Iterable[str], unique: bool):
  col_str = ", ".join([x.lower() + " DESC" if x in col_rev else x.lower() for x in ind])
  maybe_uniq = "UNIQUE" if unique else ""
  return f"CREATE {maybe_uniq} INDEX " + make_index_name(tb_name, ind, True) + f" ON {tb_name}({col_str});\n"
BIND_FUNCTION_TEXT = r"""
#REPL_START
import re
from json import dumps
SQL_ESCAPES = re.compile(r"([\'])")
repl_it = re.compile(r'(?<!:):([a-zA-Z_0-9]+)')
DEFAULT_INSTITUTION_ID = None


def set_default_partner_id(partner_id: int):
  global DEFAULT_INSTITUTION_ID
  assert isinstance(partner_id, int), "brah institution_id must be int"
  
  DEFAULT_INSTITUTION_ID = partner_id


def get_default_institution_id() -> int:
  global DEFAULT_INSTITUTION_ID
  assert DEFAULT_INSTITUTION_ID is not None, "brah, you must set_default_institution_id to be able to get dis brah"
  return  DEFAULT_INSTITUTION_ID
  

#def format_jsonb_var(var):
  

QUOTE=re.compile(r"'")
def format_var(var, is_outer=True):
  if var is None:
    return "NULL"
  if isinstance(var, float)

…(truncated)…
```

**`test/lambda_update/app.py`**

```python
import json
from test.lambda_update.libs.aurora import AuroraDB
from test.lambda_update.utils.default_logging import logger
#from aws_xray_sdk.core import patch_all
#from aws_xray_sdk.core import xray_recorder

from test.lambda_update.elastic_search.update_es import update_order, save_refund_es, save_order_rds
# added by Vitaly
import logging
logger_logging = logging.getLogger()
logger_logging.setLevel(logging.INFO)
#patch_all()


db = AuroraDB("shopify")
def primary_function(order):
  #  Connecting to aurora db
  #push_to_downstream(order)
  #a comment for the fuckedityness of aws bullshits
  save_order_rds(db, order)
  db.close()


#@xray_recorder.capture('error_message')
def lambda_handler_mend(event, _):
  logger.info(f'Update Event: {event}')

  updated_order_ids = []
  try:
    for record in event['Records']:
      message = json.loads(record['body'])
      message = message["Message"] if "Message" in message else message
      if isinstance(message, str):
        message = json.loads(message)
      message = message["data"] if "data" in message else message
      if isinstance(message, str):
        message = json.loads(message)

      if message['shopifyState'] == 'orders/updated':
        update_order(db, message)
      elif message['shopifyState'] == 'orders/cancelled':
        update_order(db, message)
      elif message['shopifyState'] == 'refunds/create':
        primary_function(message)
        save_refund_es(message)
      else:
        logger.warning('Unknown message: %s', record)

    return dict(
      statusCode=200,
      body=dict(
        message='Success',
        order_ids=json.dumps(
          updated_order_ids
        )
      )
    )
  except Exception as e:
    logger.error("messed up processing because %s", e)


    return dict(
      statusCode=500,
      body=dict(
        message=f'Error{e}',



      )
    )
    # from opensearchpy import OpenSearch, RequestsHttpConnection
# from libs.aurora import AuroraDB
# from datetime import datetime as dt
# import logging
# import json
# import os
#
#
# es_connection = OpenSearch(
#     hosts=

…(truncated)…
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`botnot-central-SQL-data-definitions`** capabilities aligned with **persistence** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `botnot-central-SQL-data-definitions`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

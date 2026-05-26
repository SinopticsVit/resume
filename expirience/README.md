# Experience knowledge base (`resume/expirience`)

English-language **evidence pack** for resume and interview prep. It mirrors local code checkouts:

| Company | Local root | Generated docs |
|---------|------------|------------------|
| **Yofi / Botnot** | `D:\botnot\` | `yofi/**` (89 repos) |
| **Sinoptics AI** | `D:\_sinoptics_git\` | `sinoptics/repos/**` (18 dirs + `system-architecture.md`) |

## Quick start

1. (Optional) Refresh scans after pulling new code:  
   `python resume/expirience/_generate_repo_docs.py`
2. Open **`SYSTEM_PROMPT.md`** — copy the system block into your AI assistant before asking for a tailored resume.
3. Open **`yofi/_master.md`** and **`sinoptics/_master.md`** for architecture posters, stack matrices, bullet banks, and links to every per-repo page.

## Repo → category map (Yofi)

| Folder under `yofi/` | Scope |
|----------------------|-------|
| `infra/` | SAM/CloudFormation env stacks, VPC, Cognito, RDS, secrets, static assets, GCP Pulumi base, integration-test env |
| `api-gateways/` | Public/admin API stacks, Swagger proxy, Lululemon API, portal gateway, Knative gateway, global webhooks, hub |
| `lambdas-business/` | Orders, products, raffles, billing, notifications, ingestion/processing |
| `persistence/` | SQL definitions, Mongo/Arango/graph Lambdas, Neo4j, Spanner services |
| `data-engineering/` | Airflow codebase & DAGs, K8s operator, dbt, Spark, batch CDK, Beam/Dataflow |
| `airbyte-integrations/` | Airbyte fork & Klaviyo sources, Shopify ingest/export, Moonsense/Moonpay, partner webhooks |
| `ml-bot-detection/` | ML gateway/controller/export router, bot detection, analytics triggers, severity, predictions |
| `telemetry/` | Injector, SDKs, services, web SDK |
| `frontend/` | Svelte portal, Vue admin, portal UIs, Slack admin bot |
| `libs-docs/` | Shared Python libs, rules monorepo, GitBook, Robot Framework harness |

## Sinoptics layout

- `sinoptics/repos/*.md` — one file per directory under `D:\_sinoptics_git\` (folder `_hh_tasks` → `hh_tasks.md`).
- `sinoptics/repos/system-architecture.md` — full architecture narrative (Mermaid + compliance themes).

## Maintainer notes

- **Generator:** `_generate_repo_docs.py` walks manifests (`package.json`, `template.yaml`, `Pulumi.yaml`, …), shallow README, bounded file-tree snippets, and short `git log` samples.  
- **Skips unreadable paths** (e.g. Docker volume mounts with locked `.venv` trees).  
- **Manual deep dives:** edit the generator or maintain a `_notes/` folder if you need immutable prose — re-running the script overwrites per-repo `.md` files.

## Canonical resume examples

- [Backend_Engineer_Constructor_RetailMedia_EN.md](../backend%20engineer/Backend_Engineer_Constructor_RetailMedia_EN.md) — structure + cross-role mapping table pattern.

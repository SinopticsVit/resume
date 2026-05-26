#!/usr/bin/env python3
"""
Scan local Yofi (D:\\botnot) and Sinoptics (D:\\_sinoptics_git) repos and emit
per-repo markdown under resume/expirience/ following the plan template.
Run from repo root: python resume/expirience/_generate_repo_docs.py
"""
from __future__ import annotations

import json
import re
import subprocess
import textwrap
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[2]  # heath/
OUT = ROOT / "resume" / "expirience"
BOTNOT = Path(r"D:\botnot")
SINOPTICS = Path(r"D:\_sinoptics_git")

YOFI_CATEGORIES: dict[str, list[str]] = {
    "infra": [
        "botnot-env-base-resources",
        "botnot-env-cognito-resources",
        "botnot-env-ec2-resources",
        "botnot-env-eventbridge-resources",
        "botnot-env-rds-res",
        "botnot-env-secrets-resources",
        "botnot-env-vpc-resources",
        "botnot-static-resources",
        "yofi-gcp-base-resources-pulumi",
        "botnot-integration-test-environment",
    ],
    "api-gateways": [
        "botnot-backend-swagger-api-proxing-",
        "botnot-documentation-api-stack",
        "botnot-lambda-admin-api",
        "botnot-lambda-api-gateway",
        "botnot-lululemon-api",
        "yofi-custom-portal-api-gateway",
        "yofi-knative-api-gateway",
        "yofi-global-webhoook-gateway",
        "yofi-hub",
    ],
    "lambdas-business": [
        "botnot-lambda-order-edit-processing",
        "botnot-lambda-order-persist",
        "botnot-lambda-order-state-prediction3",
        "botnot-lambda-order-validations",
        "botnot-lambda-order-webhook",
        "botnot-lambda-update-processing",
        "botnot-lambda-cluster-order-injection",
        "botnot-lambda-recursive-order-ingestion",
        "botnot-lambda-processing-results-exporter",
        "botnot-lambda-products-ingestion",
        "botnot-lambda-products-processing",
        "botnot-lambda-raffles-processing",
        "botnot-lambda-billing-flags-update",
        "botnot-lambda-billing-quota-validation",
        "botnot-lambda-notification",
    ],
    "persistence": [
        "botnot-central-SQL-data-definitions",
        "botnot-lambda-mongodb-config",
        "botnot-lambda-mongodb-edit-processing",
        "botnot-lambda-mongodb-persist",
        "botnot-lambda-arangodb-edit-processing",
        "botnot-lambda-graph-db-edit-processing",
        "yofi-lambda-arangodb-persistor",
        "yofi-lambda-graph-formation-service",
        "yofi-lambda-graph-spanner-service",
        "yofi-lambda-neo4j-clustering",
    ],
    "data-engineering": [
        "yofi-airflow-codebase",
        "Yofi-airflow-dags",
        "yofi-airflow-kubernetes-operator",
        "yofi-dbt-models",
        "yofi-dbt-models_old",
        "yofi-data-eng-scripts",
        "Yofi-Spark-jobs",
        "botnot-batch-cdk-refreshing-counter",
        "botnot-gps-dataflow-beam",
    ],
    "airbyte-integrations": [
        "airbyte-yofi-fork",
        "yofi-airbyte-klaviyo-source",
        "yofi-airbyte-klaviyo-source-",
        "yofi-airbyte-klaviyo-source-temp",
        "yofi-lambda-airbyte-connection",
        "botnot-shopify-historical-ingestion",
        "botnot-lambda-shopify-app-installer",
        "yofi-lambda-shopify-exporter",
        "yofi-shopify-extension-botblocker",
        "botnot-lambda-moonsense-webhook-api",
        "yofi-x-moonpay-moonsense-webhook",
        "yofi-partner-event-webhook",
        "botnet-lambda-scheduled-shopify-sync",
    ],
    "ml-bot-detection": [
        "botnot-lambda-ml-bot-detection",
        "yofi-lambda-ml-controller",
        "yofi-lambda-ml-export-router",
        "yofi-lambda-ml-gateway",
        "yofi-lambda-feature-analytics",
        "yofi-lambda-analytics-pipeline-trigger",
        "yofi-lambda-interaction-service",
        "yofi-lambda-lululemon-cluster-formation-service",
        "yofi-realtime-severity-engine",
        "yofi-telemetry-predictions",
    ],
    "telemetry": [
        "yofi-telemetry-injector",
        "yofi-telemetry-lite-sdk",
        "yofi-telemetry-services",
        "yofi-telemetry-web-sdk",
    ],
    "frontend": [
        "botnot-frontend-svelte-portal",
        "botnot-yarn-vue-admin",
        "yofi-custom-portal-ui",
        "yofi-embed-portal-ui",
        "yofi-admin-slackbot",
    ],
    "libs-docs": [
        "yofi-common-libs-py",
        "yofi-rules-monorepo",
        "yofi-docs-gitbook",
        "botnot-lambda-serverless-robot-test",
    ],
}

MANIFEST_FILES = [
    "README.md",
    "readme.md",
    "Readme.md",
    "package.json",
    "pyproject.toml",
    "requirements.txt",
    "Pipfile",
    "sst.json",
    "sst.config.ts",
    "template.yaml",
    "serverless.yml",
    "Pulumi.yaml",
    "pulumi.yaml",
    "Chart.yaml",
    "docker-compose.yml",
    "Dockerfile",
    "Makefile",
    "cdk.json",
    "tsconfig.json",
]


def read_text_safe(path: Path, max_bytes: int = 12000) -> str | None:
    if not path.is_file():
        return None
    try:
        data = path.read_bytes()[:max_bytes]
    except OSError:
        return None
    for enc in ("utf-8", "utf-8-sig", "latin-1"):
        try:
            return data.decode(enc)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


def truncate(s: str, limit: int = 3500) -> str:
    s = s.strip()
    if len(s) <= limit:
        return s
    return s[: limit - 20] + "\n\n…(truncated)…"


def _skip_path(rel: str) -> bool:
    bad = ("node_modules", ".venv", "venv/", "dist/", "docker/volumes", "plugin_daemon", "__pycache__")
    return any(b in rel for b in bad)


def detect_primary_language(repo: Path) -> str:
    """Shallow scan only — avoids unreadable deep trees (e.g. Docker volume mounts)."""
    counts: dict[str, int] = {}
    exts = {".py": "Python", ".ts": "TypeScript", ".tsx": "TypeScript", ".js": "JavaScript", ".go": "Go", ".java": "Java", ".scala": "Scala", ".sql": "SQL", ".tf": "Terraform", ".yaml": "YAML", ".yml": "YAML"}
    max_depth = 5

    def walk(d: Path, depth: int) -> None:
        if depth > max_depth:
            return
        try:
            rel = str(d.relative_to(repo)).replace("\\", "/") if d != repo else ""
        except ValueError:
            rel = ""
        if rel and _skip_path(rel):
            return
        try:
            entries = list(d.iterdir())
        except OSError:
            return
        for e in entries:
            try:
                if e.is_dir():
                    walk(e, depth + 1)
                elif e.is_file():
                    suf = e.suffix.lower()
                    if suf in exts:
                        counts[exts[suf]] = counts.get(exts[suf], 0) + 1
            except OSError:
                continue

    walk(repo, 0)
    if not counts:
        return "Unknown"
    return max(counts, key=counts.get)


def find_snippet_candidates(repo: Path) -> list[tuple[str, str]]:
    """Return up to 4 (relative_path, excerpt) for notable code (depth-limited walk)."""
    roots = [repo, repo / "src", repo / "stacks", repo / "lib", repo / "packages"]
    target_names = {
        "handler.py",
        "main.py",
        "app.py",
        "index.ts",
        "index.js",
        "stack.ts",
        "MyStack.ts",
        "Pulumi.yaml",
        "template.yaml",
    }
    out: list[tuple[str, str]] = []
    seen: set[str] = set()
    max_depth = 6

    def walk_dir(d: Path, depth: int) -> None:
        if depth > max_depth or len(out) >= 4:
            return
        try:
            rel = str(d.relative_to(repo)).replace("\\", "/") if d != repo else ""
        except ValueError:
            rel = ""
        if rel and _skip_path(rel):
            return
        try:
            for e in sorted(d.iterdir(), key=lambda p: p.name.lower()):
                if len(out) >= 4:
                    return
                try:
                    r = str(e.relative_to(repo)).replace("\\", "/")
                except ValueError:
                    continue
                if _skip_path(r):
                    continue
                if e.is_dir():
                    walk_dir(e, depth + 1)
                elif e.is_file() and e.name in target_names:
                    txt = read_text_safe(e, 8000)
                    if not txt or len(txt) < 40 or r in seen:
                        continue
                    excerpt = truncate(txt, 2200)
                    out.append((r, excerpt))
                    seen.add(r)
        except OSError:
            return

    for root in roots:
        if root.is_dir():
            walk_dir(root, 0)
        if len(out) >= 4:
            break
    return out


def git_last_log(repo: Path, n: int = 8) -> str | None:
    try:
        r = subprocess.run(
            ["git", "-C", str(repo), "log", "-n", str(n), "--pretty=format:%h %ad %s", "--date=short"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if r.returncode != 0 or not r.stdout.strip():
            return None
        return truncate(r.stdout.strip(), 2500)
    except (OSError, subprocess.TimeoutExpired):
        return None


def top_level_listing(repo: Path, limit: int = 40) -> str:
    try:
        names = sorted([p.name for p in repo.iterdir() if p.name not in (".git",)])
    except OSError:
        return "(unreadable)"
    if len(names) > limit:
        return "\n".join(names[:limit]) + f"\n… +{len(names) - limit} more"
    return "\n".join(names)


def stack_block(repo: Path) -> str:
    lines: list[str] = []
    for name in MANIFEST_FILES:
        p = repo / name
        if p.is_file():
            content = read_text_safe(p, 6000)
            if not content:
                continue
            if name.endswith(".json"):
                try:
                    obj = json.loads(content)
                    content = json.dumps(obj, indent=2)[:4000]
                except json.JSONDecodeError:
                    pass
            lines.append(f"### `{name}`\n\n```\n{truncate(content, 3200)}\n```\n")
    if not lines:
        return "_No common manifest files found at repository root._\n"
    return "\n".join(lines)


def build_doc(
    *,
    company: str,
    category: str,
    repo_name: str,
    base: Path,
) -> str:
    repo = base / repo_name
    exists = repo.is_dir()
    primary = detect_primary_language(repo) if exists else "N/A"
    readme = None
    for rn in ("README.md", "readme.md", "Readme.md"):
        if exists:
            readme = read_text_safe(repo / rn, 8000)
            if readme:
                break

    purpose = (
        f"Internal **{company}** repository `{repo_name}` under category **{category}**. "
        "Supports Yofi/Botnot platform capabilities (e-commerce intelligence, anti-fraud adjacent services, data plane, or infrastructure) as evidenced by repository layout and manifests."
    )
    if readme:
        purpose = truncate(readme.split("\n## ")[0].strip(), 800)

    arch_mermaid = ""
    if category in ("api-gateways", "lambdas-business", "ml-bot-detection"):
        arch_mermaid = textwrap.dedent(
            """
            ```mermaid
            flowchart LR
              subgraph ingress [Ingress]
                APIGW[API_Gateway_or_HTTP]
                EVT[EventBridge_SQS_SNS]
              end
              subgraph compute [Compute]
                LAM[Lambda_or_Container]
              end
              subgraph data [Data_and_External]
                DB[(MongoDB_PostgreSQL_Redis_etc)]
                EXT[Shopify_Partners_SaaS]
              end
              APIGW --> LAM
              EVT --> LAM
              LAM --> DB
              LAM --> EXT
            ```
            """
        ).strip()
    elif category == "infra":
        arch_mermaid = textwrap.dedent(
            """
            ```mermaid
            flowchart TB
              subgraph iac [IaC]
                CFN[CloudFormation_SAM_or_CDK]
                PUL[Pulumi_Terraform]
              end
              subgraph cloud [Cloud_Account]
                VPC[VPC_Subnets]
                IAM[IAM_Roles]
                DATA[RDS_Secrets_Cognito_etc]
              end
              CFN --> VPC
              PUL --> cloud
            ```
            """
        ).strip()
    elif company == "Sinoptics":
        arch_mermaid = textwrap.dedent(
            """
            ```mermaid
            flowchart LR
              subgraph edge [Clients]
                UI[Web_or_Bot]
              end
              subgraph orch [Orchestration]
                WF[n8n_or_K8s_or_FastAPI]
              end
              subgraph ai [AI_Data]
                OCR[OCR_LLM]
                PG[(PostgreSQL_Redis)]
              end
              UI --> WF
              WF --> OCR
              WF --> PG
            ```
            """
        ).strip()

    snippets = find_snippet_candidates(repo) if exists else []
    snippet_md = ""
    for rel, ex in snippets[:3]:
        lang = "python" if rel.endswith(".py") else "typescript" if rel.endswith((".ts", ".tsx")) else "yaml" if rel.endswith((".yaml", ".yml")) else "text"
        snippet_md += f"\n**`{rel}`**\n\n```{lang}\n{ex}\n```\n"

    gitlog = git_last_log(repo) if exists else None

    bullets = [
        f"Owned or extended **`{repo_name}`** capabilities aligned with **{category.replace('-', ' ')}** delivery.",
        f"Applied **{primary}** stack patterns and repository-local IaC/config where present.",
        "Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.",
        f"Integrated with **{company}** platform services (data stores, queues, gateways) per dependency manifests in-repo.",
        "Documented operational expectations (deploy, test, local dev) via README and automation files when available.",
    ]

    interview = [
        f"What is the main entrypoint and trigger for `{repo_name}`?",
        "How are secrets and non-prod environments separated?",
        "What failure modes are handled (retries, DLQ, idempotency)?",
        "How would you observe this service in production (metrics, logs, traces)?",
    ]

    path_display = str(repo).replace("\\", "/")
    status_line = "present on disk" if exists else "MISSING — path not found"
    stack_section = stack_block(repo) if exists else "_Repository path missing — cannot scan._"
    arch_section = arch_mermaid or "_High-level: see README and `stacks/` / `src/` layout for service-specific flow._"
    listing = top_level_listing(repo) if exists else "(n/a)"
    nl = "\n"
    if gitlog:
        gitlog_block = "```text" + nl + gitlog + nl + "```"
    else:
        gitlog_block = "_No readable `git log` in this working copy (shallow clone, missing .git, or not a git repo)._"
    snippet_section = snippet_md or "_No snippet candidates matched (handler.py / stack.ts / template.yaml etc.). Expand manually after opening the repo._"
    resume_lines = nl.join("- " + b for b in bullets)
    interview_lines = nl.join("- " + q for q in interview)

    doc = (
        f"# {repo_name}{nl}{nl}"
        f"**Path:** `{path_display}`  {nl}"
        f"**Category:** {category}  {nl}"
        f"**Primary language:** {primary}  {nl}"
        f"**Status:** {status_line}{nl}{nl}"
        f"## 1. Purpose (2-3 lines){nl}{nl}"
        f"{purpose}{nl}{nl}"
        f"## 2. Tech stack (from manifests and file-type mix){nl}{nl}"
        f"- **Detected primary language:** {primary}{nl}"
        f"- **Top-level layout:** see listing below.{nl}{nl}"
        f"{stack_section}{nl}{nl}"
        f"## 3. Architecture{nl}{nl}"
        f"{arch_section}{nl}{nl}"
        f"- **Inbound:** HTTP (API Gateway / ALB), scheduled triggers, queues (SQS/SNS), EventBridge rules, or batch — infer from `stacks/`, `template.yaml`, `sst.config.ts`, or `src/` handlers.{nl}"
        f"- **Outbound:** databases and external HTTP APIs per layers and `package.json` / Python imports in handlers.{nl}"
        f"- **IaC pattern:** SST/CDK, SAM/CloudFormation, Pulumi, Helm, Terraform, or raw scripts — see manifests section.{nl}{nl}"
        f"## 4. Key files (auto-discovered){nl}{nl}"
        f"- **Top-level entries:**{nl}{nl}```{nl}{listing}{nl}```{nl}{nl}"
        f"## 5. My contribution / role (evidence from git history — if available){nl}{nl}"
        f"{gitlog_block}{nl}{nl}"
        f"_Use commit messages only as hints; corroborate in interviews._"
        f"{nl}{nl}"
        f"## 6. Notable patterns / snippets{nl}{nl}"
        f"{snippet_section}{nl}{nl}"
        f"## 7. Metrics / SLO / scale (if available){nl}{nl}"
        f"_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._"
        f"{nl}{nl}"
        f"## 8. Resume bullets (ready-to-paste, English){nl}{nl}"
        f"{resume_lines}{nl}{nl}"
        f"## 9. Interview talking points{nl}{nl}"
        f"{interview_lines}{nl}"
    )
    return doc


def write_category(company: str, base: Path, category: str, names: Iterable[str]) -> None:
    sub = "yofi" if company == "Yofi" else "sinoptics"
    if sub == "yofi":
        out_dir = OUT / "yofi" / category
    else:
        out_dir = OUT / "sinoptics" / "repos"
    out_dir.mkdir(parents=True, exist_ok=True)
    for name in names:
        body = build_doc(company=company, category=category, repo_name=name, base=base)
        fname = re.sub(r"[^a-zA-Z0-9._-]+", "_", name).strip("_") + ".md"
        (out_dir / fname).write_text(body, encoding="utf-8")


def sinoptics_repos() -> list[str]:
    if not SINOPTICS.is_dir():
        return []
    return sorted([p.name for p in SINOPTICS.iterdir() if p.is_dir()])


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for cat, repos in YOFI_CATEGORIES.items():
        write_category("Yofi", BOTNOT, cat, repos)
    for name in sinoptics_repos():
        write_category("Sinoptics", SINOPTICS, "sinoptics-repo", [name])
    # system-architecture.md companion
    sa = SINOPTICS / "system-architecture.md"
    if sa.is_file():
        excerpt = read_text_safe(sa, 15000) or ""
        p = OUT / "sinoptics" / "repos" / "system-architecture.md"
        p.write_text(
            f"""# system-architecture.md (repo root file)

**Path:** `{str(sa).replace(chr(92), '/')}`  
**Category:** architecture-reference  
**Primary language:** Markdown / Mermaid  

## Full copy (truncated if huge)

```markdown
{truncate(excerpt, 14000)}
```

## 8. Resume bullets

- Documented **end-to-end invoice / compliance automation** architecture spanning **n8n**, **OCR**, **LLM**, specialized **AI agents**, and external **API connectors** (e.g. Tianyancha, QCC).
- Captured **security and compliance** themes: encryption at rest/in transit, **RBAC**, audit logging, GDPR and regional data-law awareness in design narrative.
- Described **scalability** patterns: horizontal scaling, queues, caching, monitoring and alerting at platform level.

## 9. Interview talking points

- How does the orchestrator route work across agents under load?
- Where is human-in-the-loop enforced and how are corrections replayed idempotently?
- What third-party dependencies are rate-limited or cached?
""",
            encoding="utf-8",
        )
    print("Wrote docs under", OUT)


if __name__ == "__main__":
    main()

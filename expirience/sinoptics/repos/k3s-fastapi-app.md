# k3s-fastapi-app

**Path:** `D:/_sinoptics_git/k3s-fastapi-app`  
**Category:** sinoptics-repo  
**Primary language:** Python  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# FastAPI Microservice on K3S

A simple FastAPI microservice deployment for K3S cluster with CI/CD using GitHub Actions, AWS CodeCommit, and CodeBuild.

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** Python
- **Top-level layout:** see listing below.

### `README.md`

```
# FastAPI Microservice on K3S

A simple FastAPI microservice deployment for K3S cluster with CI/CD using GitHub Actions, AWS CodeCommit, and CodeBuild.

## 本地测试

### 方式A：Docker Compose一键启动（推荐）

1. 准备环境变量

```bash
cp .env.example .env
```

2. 启动API + Worker + Redis + Postgres

```bash
docker compose up --build
```

3. 触发任务与查看状态

```bash
curl -s -X POST http://localhost:8000/api/v2025-12/process-documents | jq
curl -s http://localhost:8000/api/v2025-12/task-status/<task_id> | jq
curl -s http://localhost:8000/api/v2025-12/documents | jq
```

如果你希望明确传入要处理的文件列表（而不是让Worker去列桶），可以传入files：

```bash
curl -s -X POST http://localhost:8000/api/v2025-12/process-documents \\
  -H 'Content-Type: application/json' \\
  -d '{\"files\":[{\"document_id\":\"doc1\",\"verification_id\":\"v1\",\"file_path\":\"path/in/yandex/file.pdf\",\"file_name\":\"file.pdf\",\"file_type\":\"pdf\"}]}' | jq
```

### 方式B：本机直接启动（不使用Docker）

1. 启动Redis与Postgres（可用你已有的服务，或只用docker起这两个）

```bash
docker compose up -d redis postgres
```

2. 配置.env（同上），然后启动API与Worker

```bash
uvicorn main:app --reload
celery -A celery_app:celery_app worker --loglevel=info
```

### 常见注意事项

- OCR 使用 LLM (Qwen-VL-Max) 进行处理，不再依赖本地 tesseract。请确保配置了 `OPENAI_API_KEY`。
- 如果没有配置Yandex/S3凭证，任务会失败，但你依然可以验证“API触发任务/任务状态查询”的链路是否通。


## 测试

项目使用 pytest 进行测试，所有测试文件按功能分类组织在 `tests/` 目录中。

### 测试目录结构

```
tests/
├── unit/          # 单元测试（模型、工具类等）
├── integration/   # 集成测试（API、任务流程等）
├── services/      # 服务测试（OCR、第三方API等）
├── storage/       # 存储测试（S3、Yandex等）
└── fixtures/      # 测试数据文件
```

### 运行测试

```bash
# 运行所有测试
pytest

# 运行特定类别的测试
pytest tests/unit/          # 单元测试
pytest tests/integration/   # 集成测试
pytest tests/services/      # 服务测试
pytest tests/storage/       # 存储测试

# 运行特定测试文件
pytest tests/unit/test_models.py -v

# 运行特定测试函数
pytest tests/unit/test_models.py::test_verification_model -v
```
## Architecture

This project uses a hybrid CI/CD approach:
- **GitHub Actions**: Syncs code to AWS CodeCommit
- **AWS CodeBuild**: Builds Docker images and pushes to ECR (runs inside AWS, faster for China region)
- **K3S**: Deploys the application

## Quick Deployment Guide

### Prerequisites
- K3S cluster running on AWS EC2 instances
- AWS account with ECR, CodeCommit, and CodeBuild access
- GitHub repository with Actions enabled

## 🚀 Setup Instructions

### Step 1: Create AWS Resources

#### 1.1 Create ECR Repository
```bash
aws ecr create-repository \
  --repository-name k3s-fastapi-app \
  --region cn-northwest-1
```

Note the repository URI: `YOUR_ACCOUNT_ID.dkr.ecr.cn-northwest-1.amazonaws.com.cn/k3s-fastapi-app`

#### 1.2 Create CodeCommit Repository
```bash
aws codecommit create-repository \
  --repository-name k3s-fastapi-app \
  --region cn-northwest-1
```

#### 1.3 Create CodeBuild Project

1. Go to AWS Console → CodeBuild → Create build project
2. **Project configuration**:
   - Project name: `k3s-fastapi-app-build`
   - Description: Build and push Docker image to ECR
3. **Source**:
   - Source provider: AWS CodeCommit
   - Repository: `k3s-fastapi-app`
   - Branch:

…(truncated)…
```

### `readme.md`

```
# FastAPI Microservice on K3S

A simple FastAPI microservice deployment for K3S cluster with CI/CD using GitHub Actions, AWS CodeCommit, and CodeBuild.

## 本地测试

### 方式A：Docker Compose一键启动（推荐）

1. 准备环境变量

```bash
cp .env.example .env
```

2. 启动API + Worker + Redis + Postgres

```bash
docker compose up --build
```

3. 触发任务与查看状态

```bash
curl -s -X POST http://localhost:8000/api/v2025-12/process-documents | jq
curl -s http://localhost:8000/api/v2025-12/task-status/<task_id> | jq
curl -s http://localhost:8000/api/v2025-12/documents | jq
```

如果你希望明确传入要处理的文件列表（而不是让Worker去列桶），可以传入files：

```bash
curl -s -X POST http://localhost:8000/api/v2025-12/process-documents \\
  -H 'Content-Type: application/json' \\
  -d '{\"files\":[{\"document_id\":\"doc1\",\"verification_id\":\"v1\",\"file_path\":\"path/in/yandex/file.pdf\",\"file_name\":\"file.pdf\",\"file_type\":\"pdf\"}]}' | jq
```

### 方式B：本机直接启动（不使用Docker）

1. 启动Redis与Postgres（可用你已有的服务，或只用docker起这两个）

```bash
docker compose up -d redis postgres
```

2. 配置.env（同上），然后启动API与Worker

```bash
uvicorn main:app --reload
celery -A celery_app:celery_app worker --loglevel=info
```

### 常见注意事项

- OCR 使用 LLM (Qwen-VL-Max) 进行处理，不再依赖本地 tesseract。请确保配置了 `OPENAI_API_KEY`。
- 如果没有配置Yandex/S3凭证，任务会失败，但你依然可以验证“API触发任务/任务状态查询”的链路是否通。


## 测试

项目使用 pytest 进行测试，所有测试文件按功能分类组织在 `tests/` 目录中。

### 测试目录结构

```
tests/
├── unit/          # 单元测试（模型、工具类等）
├── integration/   # 集成测试（API、任务流程等）
├── services/      # 服务测试（OCR、第三方API等）
├── storage/       # 存储测试（S3、Yandex等）
└── fixtures/      # 测试数据文件
```

### 运行测试

```bash
# 运行所有测试
pytest

# 运行特定类别的测试
pytest tests/unit/          # 单元测试
pytest tests/integration/   # 集成测试
pytest tests/services/      # 服务测试
pytest tests/storage/       # 存储测试

# 运行特定测试文件
pytest tests/unit/test_models.py -v

# 运行特定测试函数
pytest tests/unit/test_models.py::test_verification_model -v
```
## Architecture

This project uses a hybrid CI/CD approach:
- **GitHub Actions**: Syncs code to AWS CodeCommit
- **AWS CodeBuild**: Builds Docker images and pushes to ECR (runs inside AWS, faster for China region)
- **K3S**: Deploys the application

## Quick Deployment Guide

### Prerequisites
- K3S cluster running on AWS EC2 instances
- AWS account with ECR, CodeCommit, and CodeBuild access
- GitHub repository with Actions enabled

## 🚀 Setup Instructions

### Step 1: Create AWS Resources

#### 1.1 Create ECR Repository
```bash
aws ecr create-repository \
  --repository-name k3s-fastapi-app \
  --region cn-northwest-1
```

Note the repository URI: `YOUR_ACCOUNT_ID.dkr.ecr.cn-northwest-1.amazonaws.com.cn/k3s-fastapi-app`

#### 1.2 Create CodeCommit Repository
```bash
aws codecommit create-repository \
  --repository-name k3s-fastapi-app \
  --region cn-northwest-1
```

#### 1.3 Create CodeBuild Project

1. Go to AWS Console → CodeBuild → Create build project
2. **Project configuration**:
   - Project name: `k3s-fastapi-app-build`
   - Description: Build and push Docker image to ECR
3. **Source**:
   - Source provider: AWS CodeCommit
   - Repository: `k3s-fastapi-app`
   - Branch:

…(truncated)…
```

### `Readme.md`

```
# FastAPI Microservice on K3S

A simple FastAPI microservice deployment for K3S cluster with CI/CD using GitHub Actions, AWS CodeCommit, and CodeBuild.

## 本地测试

### 方式A：Docker Compose一键启动（推荐）

1. 准备环境变量

```bash
cp .env.example .env
```

2. 启动API + Worker + Redis + Postgres

```bash
docker compose up --build
```

3. 触发任务与查看状态

```bash
curl -s -X POST http://localhost:8000/api/v2025-12/process-documents | jq
curl -s http://localhost:8000/api/v2025-12/task-status/<task_id> | jq
curl -s http://localhost:8000/api/v2025-12/documents | jq
```

如果你希望明确传入要处理的文件列表（而不是让Worker去列桶），可以传入files：

```bash
curl -s -X POST http://localhost:8000/api/v2025-12/process-documents \\
  -H 'Content-Type: application/json' \\
  -d '{\"files\":[{\"document_id\":\"doc1\",\"verification_id\":\"v1\",\"file_path\":\"path/in/yandex/file.pdf\",\"file_name\":\"file.pdf\",\"file_type\":\"pdf\"}]}' | jq
```

### 方式B：本机直接启动（不使用Docker）

1. 启动Redis与Postgres（可用你已有的服务，或只用docker起这两个）

```bash
docker compose up -d redis postgres
```

2. 配置.env（同上），然后启动API与Worker

```bash
uvicorn main:app --reload
celery -A celery_app:celery_app worker --loglevel=info
```

### 常见注意事项

- OCR 使用 LLM (Qwen-VL-Max) 进行处理，不再依赖本地 tesseract。请确保配置了 `OPENAI_API_KEY`。
- 如果没有配置Yandex/S3凭证，任务会失败，但你依然可以验证“API触发任务/任务状态查询”的链路是否通。


## 测试

项目使用 pytest 进行测试，所有测试文件按功能分类组织在 `tests/` 目录中。

### 测试目录结构

```
tests/
├── unit/          # 单元测试（模型、工具类等）
├── integration/   # 集成测试（API、任务流程等）
├── services/      # 服务测试（OCR、第三方API等）
├── storage/       # 存储测试（S3、Yandex等）
└── fixtures/      # 测试数据文件
```

### 运行测试

```bash
# 运行所有测试
pytest

# 运行特定类别的测试
pytest tests/unit/          # 单元测试
pytest tests/integration/   # 集成测试
pytest tests/services/      # 服务测试
pytest tests/storage/       # 存储测试

# 运行特定测试文件
pytest tests/unit/test_models.py -v

# 运行特定测试函数
pytest tests/unit/test_models.py::test_verification_model -v
```
## Architecture

This project uses a hybrid CI/CD approach:
- **GitHub Actions**: Syncs code to AWS CodeCommit
- **AWS CodeBuild**: Builds Docker images and pushes to ECR (runs inside AWS, faster for China region)
- **K3S**: Deploys the application

## Quick Deployment Guide

### Prerequisites
- K3S cluster running on AWS EC2 instances
- AWS account with ECR, CodeCommit, and CodeBuild access
- GitHub repository with Actions enabled

## 🚀 Setup Instructions

### Step 1: Create AWS Resources

#### 1.1 Create ECR Repository
```bash
aws ecr create-repository \
  --repository-name k3s-fastapi-app \
  --region cn-northwest-1
```

Note the repository URI: `YOUR_ACCOUNT_ID.dkr.ecr.cn-northwest-1.amazonaws.com.cn/k3s-fastapi-app`

#### 1.2 Create CodeCommit Repository
```bash
aws codecommit create-repository \
  --repository-name k3s-fastapi-app \
  --region cn-northwest-1
```

#### 1.3 Create CodeBuild Project

1. Go to AWS Console → CodeBuild → Create build project
2. **Project configuration**:
   - Project name: `k3s-fastapi-app-build`
   - Description: Build and push Docker image to ECR
3. **Source**:
   - Source provider: AWS CodeCommit
   - Repository: `k3s-fastapi-app`
   - Branch:

…(truncated)…
```

### `docker-compose.yml`

```
services:
#  fastapi-redis:
#    image: redis:7-alpine
#    container_name: yandex-doc-processor-redis
#    ports:
#      - "6379:6379"
#    volumes:
#      - redis_data:/data
#    command: redis-server --appendonly yes

  postgres:
    image: postgres:15
    container_name: yandex-doc-processor-postgres
    environment:
      POSTGRES_DB: yandex_doc_processor
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    ports:
      - "35432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  # Celery Worker
#  worker:
#    build: .
#    container_name: yandex-doc-processor-worker
#    depends_on:
#      - fastapi-redis
#      - postgres
#    volumes:
#      - .:/app
#      - ~/.aws:/root/.aws:ro
#    environment:
#      - DATABASE_URL=postgresql://user:password@postgres:5432/yandex_doc_processor
#      - REDIS_HOST=fastapi-redis
#      - CELERY_BROKER_URL=redis://fastapi-redis:6379/0
#      - CELERY_RESULT_BACKEND=redis://fastapi-redis:6379/0
#      - SKIP_MTLS=true
#      - AWS_REGION=cn-northwest-1
#    command: celery -A celery_app:celery_app worker --loglevel=info

  # Hatchet Worker
  # 单独启动: docker compose up --build hatchet-worker
  hatchet-worker:
    build:
      context: .
      dockerfile: Dockerfile.worker
    container_name: yandex-doc-processor-hatchet-worker
    depends_on:
      - postgres
    volumes:
      - .:/app
      - ~/.aws:/root/.aws:ro
    environment:
      - DATABASE_URL=postgresql://user:password@postgres:5432/yandex_doc_processor
      - AWS_REGION=cn-northwest-1
    command: python -m my_hatchet.worker

  api:
    build: .
    container_name: yandex-doc-processor-api
    depends_on:
#      - fastapi-redis
      - postgres
    volumes:
      - .:/app
      - ~/.aws:/root/.aws:ro
    environment:
      - DATABASE_URL=postgresql://user:password@postgres:5432/yandex_doc_processor
#      - REDIS_HOST=fastapi-redis
#      - CELERY_BROKER_URL=redis://fastapi-redis:6379/0
#      - CELERY_RESULT_BACKEND=redis://fastapi-redis:6379/0
      - SKIP_MTLS=true
      - AWS_REGION=cn-northwest-1
    ports:
      - "8000:8000"
    command: uvicorn main:app --host 0.0.0.0 --port 8000 --reload

#  # Flower (Celery monitoring)
#  flower:
#    image: mher/flower:2.0
#    container_name: yandex-doc-processor-flower
#    depends_on:
#      - fastapi-redis
#    environment:
#      - CELERY_BROKER_URL=redis://fastapi-redis:6379/0
#      - FLOWER_PORT=5555
#    ports:
#      - "5555:5555"
#    # Start flower via celery command
#    command: ["celery", "--broker=redis://fastapi-redis:6379/0", "flower", "--port=5555"]

volumes:
#  redis_data:
  postgres_data:
```

### `Dockerfile`

```
FROM public.ecr.aws/docker/library/python:3.11-slim

# Use Aliyun mirror for apt (China AWS region has slow access to deb.debian.org)
RUN sed -i 's|deb.debian.org|mirrors.aliyun.com|g' /etc/apt/sources.list.d/debian.sources

RUN apt-get update && apt-get install -y \
    poppler-utils \
    ca-certificates \
    && update-ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements-api.txt .
RUN pip install --no-cache-dir -r requirements-api.txt -i https://mirrors.aliyun.com/pypi/simple/ \
    --extra-index-url https://pypi.tuna.tsinghua.edu.cn/simple/

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### `Makefile`

```
# Hatchet Testing Makefile
# Assumes worker is already running (start with: hatchet worker dev -p <profile>)

HATCHET_PROFILE ?= default
WORKFLOW ?= invoice-verification
TEST_INPUT ?= invoice_simple
PYTHON ?= python

.PHONY: help hatchet-test hatchet-test-complex hatchet-debug hatchet-replay hatchet-logs

help:
	@echo "Hatchet Testing Commands (assumes worker is running):"
	@echo ""
	@echo "  make hatchet-test              Run test with simple input"
	@echo "  make hatchet-test-complex      Run test with complex input"
	@echo ""
	@echo "  make hatchet-debug RUN_ID=<id> Debug a specific run"
	@echo "  make hatchet-replay RUN_ID=<id> Replay a failed run"
	@echo "  make hatchet-logs RUN_ID=<id>  Get logs for a run"
	@echo ""
	@echo "Variables:"
	@echo "  HATCHET_PROFILE=<profile>      Use specific profile (default: default)"
	@echo "  WORKFLOW=<name>                Specify workflow name"
	@echo "  TEST_INPUT=<name>              Specify test input file"

# ============================================================================
# Testing
# ============================================================================

hatchet-test:
	@echo "Running test: $(TEST_INPUT)..."
	$(PYTHON) scripts/hatchet_test.py -w $(WORKFLOW) -i $(TEST_INPUT)

hatchet-test-complex:
	@echo "Running test: invoice_complex..."
	$(PYTHON) scripts/hatchet_test.py -w $(WORKFLOW) -i invoice_complex

# ============================================================================
# Debug and Replay
# ============================================================================

hatchet-debug:
ifndef RUN_ID
	@echo "Usage: make hatchet-debug RUN_ID=<run_id>"
	@exit 1
endif
	@echo "Debugging run: $(RUN_ID)"
	$(PYTHON) scripts/hatchet_test.py --debug $(RUN_ID)

hatchet-replay:
ifndef RUN_ID
	@echo "Usage: make hatchet-replay RUN_ID=<run_id>"
	@exit 1
endif
	hatchet replay -r $(RUN_ID) -p $(HATCHET_PROFILE)

hatchet-logs:
ifndef RUN_ID
	@echo "Usage: make hatchet-logs RUN_ID=<run_id>"
	@exit 1
endif
	hatchet runs logs $(RUN_ID) -p $(HATCHET_PROFILE)

hatchet-run-info:
ifndef RUN_ID
	@echo "Usage: make hatchet-run-info RUN_ID=<run_id>"
	@exit 1
endif
	hatchet runs get $(RUN_ID) -o json -p $(HATCHET_PROFILE)
```


## 3. Architecture

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

- **Inbound:** HTTP (API Gateway / ALB), scheduled triggers, queues (SQS/SNS), EventBridge rules, or batch — infer from `stacks/`, `template.yaml`, `sst.config.ts`, or `src/` handlers.
- **Outbound:** databases and external HTTP APIs per layers and `package.json` / Python imports in handlers.
- **IaC pattern:** SST/CDK, SAM/CloudFormation, Pulumi, Helm, Terraform, or raw scripts — see manifests section.

## 4. Key files (auto-discovered)

- **Top-level entries:**

```
.claude
.cursor
.cursorrules
.env.example
.github
.gitignore
.pytest_cache
.trae
.traerules
AGENTS.md
CLAUDE.md
DB_CHANGES_LAST_2_STEPS.md
DEPLOYMENT_SPEC_EN.md
Dockerfile
Dockerfile.worker
Makefile
README.md
__pycache__
_tmp_find_birth_cert.ps1
agent_check_synthesizer.py
agent_prompts
alembic
alembic.ini
app.py
auth.py
aws_secret.py
buildspec.yml
celery_app.py
changes.b64
config.py
contracts
deploy-ydb-tables.yml
deploy.b64
deployment.yaml
docker-compose.yml
docs
document_converter.py
document_processing_schema.py
downloaded_invoice.pdf
export_ocr_prompt.py
… +32 more
```

## 5. My contribution / role (evidence from git history — if available)

```text
9739f0e 2026-05-14 Merge pull request #94 from SinopticsAI/scrum-117-business-field-extraction
6934c11 2026-05-14 Reduce SCRUM-117 visual import coupling
b4e7bde 2026-05-14 Implement SCRUM-117 business field extraction
c28c801 2026-05-14 Merge pull request #93 from SinopticsAI/scrum-117-strip-docling-uri
545e0f0 2026-05-14 Strip Docling embedded URIs from extract output
d9980ea 2026-05-13 Merge pull request #92 from SinopticsAI/feat/codebuild-docker-layer-cache
fb7c63b 2026-05-13 fix(ci): use separate docker tag instead of multiple -t flags
635101f 2026-05-13 Merge pull request #91 from SinopticsAI/feat/codebuild-docker-layer-cache
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets


**`app.py`**

```python
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from models import create_tables
from log import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialization on application startup
    print("正在初始化数据库...")
    create_tables()  # Create database tables
    print("数据库初始化完成")
    yield
    # Cleanup on application shutdown
    print("应用正在关闭...")


def create_app():
    app = FastAPI(
        title="Yandex文档处理微服务",
        version="1.0.0",
        lifespan=lifespan
    )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        logger.error(f"Request {request.url.path} validation error: {exc.errors()}")
        return JSONResponse(
            status_code=422,
            content={"detail": exc.errors()},
        )

    return app
```

**`main.py`**

```python
from fastapi import HTTPException, APIRouter, Depends, Query
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy.orm.attributes import flag_modified
from celery.result import AsyncResult
from celery_app import celery_app
from models import Verification, VerificationItem, SessionLocal, VerificationStatus, VerificationReport, CompanyData
from ocr_schema import InvoiceExtractionSchema
from schemas import (
    VerificationItem as VerificationItemSchema,
    VerificationRequest,
    VerificationFinishRequest,
    VerificationFinishResponse,
    VerificationReportResponse,
    ReportJsons,
    LocalizedVerificationReport,
    SubAgentReportRequest,
    VerificationWithReportsResponse,
    CompanyBaseinfoResponse,
    CompanyDataActionRequest,
    CompanyDataActionResponse,
    SaveOcrParsedDataResponse,
    VerificationProblem,
    ErrorReportRequest,
    ErrorReportData,
    ErrorProblem,
    ErrorContent,
)
from app import create_app
from auth import authenticate
from config import settings
from log import logger
from tianyancha_client import fetch_company_baseinfo, TianyanchaClientError
from seller_company_name_resolver.api import router as resolver_router
from translation_service import get_translation_service
from agent_prompts.agent_defs import get_agent_by_role, ALL_AGENTS
from report_service import ReportService
from services.verification_service import VerificationService, initialize_verification
import arrow
from datetime import datetime
from typing import Any, cast, Optional
import uuid
import asyncio
import httpx


# Create the app instance using the application factory
app = create_app()

# Unified API Version Management - Business API Router
api_router_v2025_12 = APIRouter(
    prefix="/api/v2025-12",
    tags=["Business API v2025-12"],
    dependencies=[Depends(authenticate)]
)

# New v2026-03 Router - Hatchet Workflow Version
api_router_v2026_03 = APIRouter(
    prefix="/api/v2026-03",
    tags=["Business API v2026-03"],
    dependencies=[Depends(authenticate)]
)


de

…(truncated)…
```


## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`k3s-fastapi-app`** capabilities aligned with **sinoptics repo** delivery.
- Applied **Python** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Sinoptics** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `k3s-fastapi-app`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

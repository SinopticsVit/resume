# yandex-keycloak

**Path:** `D:/_sinoptics_git/yandex-keycloak`  
**Category:** sinoptics-repo  
**Primary language:** YAML  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# Keycloak Deployment to Yandex VM

> CI/CD workflow for deploying Keycloak as OIDC provider on Yandex Cloud VM with PostgreSQL backend.

---

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** YAML
- **Top-level layout:** see listing below.

### `README.md`

```
# Keycloak Deployment to Yandex VM

> CI/CD workflow for deploying Keycloak as OIDC provider on Yandex Cloud VM with PostgreSQL backend.

---

## ✅ Deployment Status

**Keycloak полностью работает!**

| Component | Status |
|-----------|--------|
| HTTPS с wildcard сертификатом | ✅ Настроен |
| OIDC Discovery endpoint | ✅ Работает |
| Keycloak | ✅ Отвечает корректно |
| PostgreSQL подключение | ✅ Активно |

### OIDC Endpoints

| Endpoint | URL |
|----------|-----|
| Discovery | `https://auth.sinoptics.ru/realms/master/.well-known/openid-configuration` |
| JWKS | `https://auth.sinoptics.ru/realms/master/protocol/openid-connect/certs` |
| Issuer | `https://auth.sinoptics.ru/realms/master` |
| Authorization | `https://auth.sinoptics.ru/realms/master/protocol/openid-connect/auth` |
| Token | `https://auth.sinoptics.ru/realms/master/protocol/openid-connect/token` |

### Admin Console

| Parameter | Value |
|-----------|-------|
| URL | `https://auth.sinoptics.ru/admin/` |
| User | `admin` |
| Password | GitHub Secret `KEYCLOAK_ADMIN_PASSWORD` |

### ⚠️ DNS Configuration Required

Для внешнего доступа необходимо настроить DNS:

```
auth.sinoptics.ru → A → 158.160.72.16
```

**Прямой доступ для тестирования:** `http://158.160.72.16:8080/admin/`

---

## Overview

This repository contains infrastructure and deployment templates for:
- Deploying Keycloak on Yandex Cloud VM via Docker
- Configuring Keycloak to use PostgreSQL as persistent storage
- Setting up HTTPS via nginx reverse proxy with Let's Encrypt
- GitHub Actions CI/CD workflow for automated deployments

**Keycloak Hostname:** `auth.sinoptics.ru`  
**API Endpoint:** `api.sinoptics.ru`

---

## Prerequisites

### 1. Yandex VM Requirements
- **OS:** Ubuntu 22.04+ / Debian 11+
- **Public IP:** `158.160.72.16`
- **User:** `vmroot` (with sudo privileges)
- **Container Runtime:** Docker (will be installed by CI if missing)
- **Open Ports:** 80, 443, 8080 (internal)

### 2. PostgreSQL Database
PostgreSQL is already deployed on the VM:
- **Host:** `localhost`
- **Port:** `5432`
- **Database:** `sinopptics_postgasql`
- **User:** `cicd_user`
- **Password:** Stored in GitHub Secret `DB_PASSWORD`

### 3. DNS Configuration
Ensure DNS records are configured:
- `auth.sinoptics.ru` → `158.160.72.16` (A record pointing to VM IP)
- `api.sinoptics.ru` → Your API endpoint

---

## Required GitHub Secrets

Add the following secrets in your GitHub repository settings (`Settings > Secrets and variables > Actions`):

| Secret Name | Description | Example Value |
|-------------|-------------|---------------|
| `YA_VM_SSH` | OpenSSH private key for VM access | `-----BEGIN OPENSSH PRIVATE KEY-----...` |
| `DB_PASSWORD` | PostgreSQL password | `<your-password>` |
| `KEYCLOAK_ADMIN_PASSWORD` | Keycloak admin password | `<your-admin-password>` |

### Environment Variables (hardcoded in workflow)

The following values are configured directly in the workflow file:

| Variable | Value |
|----------|-------|
| `VM_HOST` | `158.160.72.16` |
| `VM_USER` | `vmroot` |
| `KEYCLOAK_HOSTNAME` | `auth.sinoptics.r

…(truncated)…
```

### `readme.md`

```
# Keycloak Deployment to Yandex VM

> CI/CD workflow for deploying Keycloak as OIDC provider on Yandex Cloud VM with PostgreSQL backend.

---

## ✅ Deployment Status

**Keycloak полностью работает!**

| Component | Status |
|-----------|--------|
| HTTPS с wildcard сертификатом | ✅ Настроен |
| OIDC Discovery endpoint | ✅ Работает |
| Keycloak | ✅ Отвечает корректно |
| PostgreSQL подключение | ✅ Активно |

### OIDC Endpoints

| Endpoint | URL |
|----------|-----|
| Discovery | `https://auth.sinoptics.ru/realms/master/.well-known/openid-configuration` |
| JWKS | `https://auth.sinoptics.ru/realms/master/protocol/openid-connect/certs` |
| Issuer | `https://auth.sinoptics.ru/realms/master` |
| Authorization | `https://auth.sinoptics.ru/realms/master/protocol/openid-connect/auth` |
| Token | `https://auth.sinoptics.ru/realms/master/protocol/openid-connect/token` |

### Admin Console

| Parameter | Value |
|-----------|-------|
| URL | `https://auth.sinoptics.ru/admin/` |
| User | `admin` |
| Password | GitHub Secret `KEYCLOAK_ADMIN_PASSWORD` |

### ⚠️ DNS Configuration Required

Для внешнего доступа необходимо настроить DNS:

```
auth.sinoptics.ru → A → 158.160.72.16
```

**Прямой доступ для тестирования:** `http://158.160.72.16:8080/admin/`

---

## Overview

This repository contains infrastructure and deployment templates for:
- Deploying Keycloak on Yandex Cloud VM via Docker
- Configuring Keycloak to use PostgreSQL as persistent storage
- Setting up HTTPS via nginx reverse proxy with Let's Encrypt
- GitHub Actions CI/CD workflow for automated deployments

**Keycloak Hostname:** `auth.sinoptics.ru`  
**API Endpoint:** `api.sinoptics.ru`

---

## Prerequisites

### 1. Yandex VM Requirements
- **OS:** Ubuntu 22.04+ / Debian 11+
- **Public IP:** `158.160.72.16`
- **User:** `vmroot` (with sudo privileges)
- **Container Runtime:** Docker (will be installed by CI if missing)
- **Open Ports:** 80, 443, 8080 (internal)

### 2. PostgreSQL Database
PostgreSQL is already deployed on the VM:
- **Host:** `localhost`
- **Port:** `5432`
- **Database:** `sinopptics_postgasql`
- **User:** `cicd_user`
- **Password:** Stored in GitHub Secret `DB_PASSWORD`

### 3. DNS Configuration
Ensure DNS records are configured:
- `auth.sinoptics.ru` → `158.160.72.16` (A record pointing to VM IP)
- `api.sinoptics.ru` → Your API endpoint

---

## Required GitHub Secrets

Add the following secrets in your GitHub repository settings (`Settings > Secrets and variables > Actions`):

| Secret Name | Description | Example Value |
|-------------|-------------|---------------|
| `YA_VM_SSH` | OpenSSH private key for VM access | `-----BEGIN OPENSSH PRIVATE KEY-----...` |
| `DB_PASSWORD` | PostgreSQL password | `<your-password>` |
| `KEYCLOAK_ADMIN_PASSWORD` | Keycloak admin password | `<your-admin-password>` |

### Environment Variables (hardcoded in workflow)

The following values are configured directly in the workflow file:

| Variable | Value |
|----------|-------|
| `VM_HOST` | `158.160.72.16` |
| `VM_USER` | `vmroot` |
| `KEYCLOAK_HOSTNAME` | `auth.sinoptics.r

…(truncated)…
```

### `Readme.md`

```
# Keycloak Deployment to Yandex VM

> CI/CD workflow for deploying Keycloak as OIDC provider on Yandex Cloud VM with PostgreSQL backend.

---

## ✅ Deployment Status

**Keycloak полностью работает!**

| Component | Status |
|-----------|--------|
| HTTPS с wildcard сертификатом | ✅ Настроен |
| OIDC Discovery endpoint | ✅ Работает |
| Keycloak | ✅ Отвечает корректно |
| PostgreSQL подключение | ✅ Активно |

### OIDC Endpoints

| Endpoint | URL |
|----------|-----|
| Discovery | `https://auth.sinoptics.ru/realms/master/.well-known/openid-configuration` |
| JWKS | `https://auth.sinoptics.ru/realms/master/protocol/openid-connect/certs` |
| Issuer | `https://auth.sinoptics.ru/realms/master` |
| Authorization | `https://auth.sinoptics.ru/realms/master/protocol/openid-connect/auth` |
| Token | `https://auth.sinoptics.ru/realms/master/protocol/openid-connect/token` |

### Admin Console

| Parameter | Value |
|-----------|-------|
| URL | `https://auth.sinoptics.ru/admin/` |
| User | `admin` |
| Password | GitHub Secret `KEYCLOAK_ADMIN_PASSWORD` |

### ⚠️ DNS Configuration Required

Для внешнего доступа необходимо настроить DNS:

```
auth.sinoptics.ru → A → 158.160.72.16
```

**Прямой доступ для тестирования:** `http://158.160.72.16:8080/admin/`

---

## Overview

This repository contains infrastructure and deployment templates for:
- Deploying Keycloak on Yandex Cloud VM via Docker
- Configuring Keycloak to use PostgreSQL as persistent storage
- Setting up HTTPS via nginx reverse proxy with Let's Encrypt
- GitHub Actions CI/CD workflow for automated deployments

**Keycloak Hostname:** `auth.sinoptics.ru`  
**API Endpoint:** `api.sinoptics.ru`

---

## Prerequisites

### 1. Yandex VM Requirements
- **OS:** Ubuntu 22.04+ / Debian 11+
- **Public IP:** `158.160.72.16`
- **User:** `vmroot` (with sudo privileges)
- **Container Runtime:** Docker (will be installed by CI if missing)
- **Open Ports:** 80, 443, 8080 (internal)

### 2. PostgreSQL Database
PostgreSQL is already deployed on the VM:
- **Host:** `localhost`
- **Port:** `5432`
- **Database:** `sinopptics_postgasql`
- **User:** `cicd_user`
- **Password:** Stored in GitHub Secret `DB_PASSWORD`

### 3. DNS Configuration
Ensure DNS records are configured:
- `auth.sinoptics.ru` → `158.160.72.16` (A record pointing to VM IP)
- `api.sinoptics.ru` → Your API endpoint

---

## Required GitHub Secrets

Add the following secrets in your GitHub repository settings (`Settings > Secrets and variables > Actions`):

| Secret Name | Description | Example Value |
|-------------|-------------|---------------|
| `YA_VM_SSH` | OpenSSH private key for VM access | `-----BEGIN OPENSSH PRIVATE KEY-----...` |
| `DB_PASSWORD` | PostgreSQL password | `<your-password>` |
| `KEYCLOAK_ADMIN_PASSWORD` | Keycloak admin password | `<your-admin-password>` |

### Environment Variables (hardcoded in workflow)

The following values are configured directly in the workflow file:

| Variable | Value |
|----------|-------|
| `VM_HOST` | `158.160.72.16` |
| `VM_USER` | `vmroot` |
| `KEYCLOAK_HOSTNAME` | `auth.sinoptics.r

…(truncated)…
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
.github
.gitignore
.vscode
README.md
deployment
docs
iac
keycloak-config
prompt
sert
test_payload.json
tmp
```

## 5. My contribution / role (evidence from git history — if available)

```text
5041170 2026-03-04 Update 2026-03-04 17:52
192d16c 2026-01-15 Update 2026-01-15 16:06
f925fd9 2026-01-15 Update 2026-01-15 15:42
473bb42 2026-01-15 Update 2026-01-15 14:13
6ffa931 2026-01-13 Update 2026-01-13 10:31
db0ce47 2026-01-13 Update 2026-01-13 00:18
cd75aad 2026-01-12 Update 2026-01-12 23:02
9a71472 2026-01-12 Update 2026-01-12 22:54
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets

_No snippet candidates matched (handler.py / stack.ts / template.yaml etc.). Expand manually after opening the repo._

## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`yandex-keycloak`** capabilities aligned with **sinoptics repo** delivery.
- Applied **YAML** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Sinoptics** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yandex-keycloak`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

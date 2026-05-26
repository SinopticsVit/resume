# yofi-telemetry-services

**Path:** `D:/botnot/yofi-telemetry-services`  
**Category:** telemetry  
**Primary language:** YAML  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# yofi-telemetry-services
Backend services for Yofi Telemetry

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** YAML
- **Top-level layout:** see listing below.

### `README.md`

```
# yofi-telemetry-services
Backend services for Yofi Telemetry


## Create function

With kn func

```bash
kn func create -l typescript -t http helloworld
cd helloworld
npm i
```

Without kn func
```
mkdir token
cd token
go mod init main
go mod edit -replace yofi.ai/common=../common 
go get github.com/gin-gonic/gin
go get yofi.ai/common
touch main.go
```



## Performance

```
hey -z 10s -c 10000 "http://ginfunc.yofi-telemetry.dev.telemetry.yofi.ai/hello" && kubectl get pods -n yofi-telemetry
hey -z 10s -c 10000 "http://hellogo.yofi-telemetry.dev.telemetry.yofi.ai" && kubectl get pods -n yofi-telemetry

hey -m POST -c 10 -z 10s  -H 'Content-Type: application/json' -d '{"public_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJBU2djSlhCcGpYNWc1aEZqZWp1NzJoIiwidHlwZSI6MX0.KjwHz2OC8EJWzKyR6fnlO0TEhO9-yHRryJkDVNGvH1E"}' "http://tokens.yofi-telemetry.dev.telemetry.yofi.ai/upgrade" && kubectl get pods -n yofi-telemetry
```


kn service create tokens -n yofi-telemetry --image 111747068850.dkr.ecr.us-west-1.amazonaws.com/yofi-telemetry/tokens:dev --force --scale 1..10
```

### `readme.md`

```
# yofi-telemetry-services
Backend services for Yofi Telemetry


## Create function

With kn func

```bash
kn func create -l typescript -t http helloworld
cd helloworld
npm i
```

Without kn func
```
mkdir token
cd token
go mod init main
go mod edit -replace yofi.ai/common=../common 
go get github.com/gin-gonic/gin
go get yofi.ai/common
touch main.go
```



## Performance

```
hey -z 10s -c 10000 "http://ginfunc.yofi-telemetry.dev.telemetry.yofi.ai/hello" && kubectl get pods -n yofi-telemetry
hey -z 10s -c 10000 "http://hellogo.yofi-telemetry.dev.telemetry.yofi.ai" && kubectl get pods -n yofi-telemetry

hey -m POST -c 10 -z 10s  -H 'Content-Type: application/json' -d '{"public_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJBU2djSlhCcGpYNWc1aEZqZWp1NzJoIiwidHlwZSI6MX0.KjwHz2OC8EJWzKyR6fnlO0TEhO9-yHRryJkDVNGvH1E"}' "http://tokens.yofi-telemetry.dev.telemetry.yofi.ai/upgrade" && kubectl get pods -n yofi-telemetry
```


kn service create tokens -n yofi-telemetry --image 111747068850.dkr.ecr.us-west-1.amazonaws.com/yofi-telemetry/tokens:dev --force --scale 1..10
```

### `Readme.md`

```
# yofi-telemetry-services
Backend services for Yofi Telemetry


## Create function

With kn func

```bash
kn func create -l typescript -t http helloworld
cd helloworld
npm i
```

Without kn func
```
mkdir token
cd token
go mod init main
go mod edit -replace yofi.ai/common=../common 
go get github.com/gin-gonic/gin
go get yofi.ai/common
touch main.go
```



## Performance

```
hey -z 10s -c 10000 "http://ginfunc.yofi-telemetry.dev.telemetry.yofi.ai/hello" && kubectl get pods -n yofi-telemetry
hey -z 10s -c 10000 "http://hellogo.yofi-telemetry.dev.telemetry.yofi.ai" && kubectl get pods -n yofi-telemetry

hey -m POST -c 10 -z 10s  -H 'Content-Type: application/json' -d '{"public_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJBU2djSlhCcGpYNWc1aEZqZWp1NzJoIiwidHlwZSI6MX0.KjwHz2OC8EJWzKyR6fnlO0TEhO9-yHRryJkDVNGvH1E"}' "http://tokens.yofi-telemetry.dev.telemetry.yofi.ai/upgrade" && kubectl get pods -n yofi-telemetry
```


kn service create tokens -n yofi-telemetry --image 111747068850.dkr.ecr.us-west-1.amazonaws.com/yofi-telemetry/tokens:dev --force --scale 1..10
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
.vscode
API.md
README.md
devops
eks_cdk
functions
schema
```

## 5. My contribution / role (evidence from git history — if available)

```text
e1c9a53 2023-10-10 Merge pull request #12 from BotNotOrg/update-sst-deps
9686d76 2023-10-10 add api readme
29e3880 2023-10-10 update iam yaml
d8ac224 2023-10-10 update k8c1.yaml
fbcde77 2023-10-09 Merge branch 'main' of github.com:BotNotOrg/yofi-telemetry-services into update-sst-deps
d444f48 2023-10-09 Merge pull request #15 from BotNotOrg/update-test
0d16a6f 2023-10-02 update read me and test suite
b55cf43 2023-10-02 update postman
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets

_No snippet candidates matched (handler.py / stack.ts / template.yaml etc.). Expand manually after opening the repo._

## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`yofi-telemetry-services`** capabilities aligned with **telemetry** delivery.
- Applied **YAML** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Yofi** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `yofi-telemetry-services`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

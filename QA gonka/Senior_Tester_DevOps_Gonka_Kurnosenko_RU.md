# Виталий Курносёнко

**Senior Tester-DevOps | E2E-автоматизация | CI/CD и качество релизов | Cloud / Kubernetes | AI-платформы**

Remote (UTC+8) | Telegram: @vitaly_kur | Email: rikkimortycrypt@gmail.com  
Гражданство: Россия  
Языки: английский — B2+ (рабочий); русский — родной; китайский — HSK 4

---

## Целевая роль

- **Senior Tester-DevOps** — фуллтайм, remote: качество + доставка для **testnet/mainnet Gonka** — ловить регрессии до выкладки, усиливать пайплайны деплоя, стабилизировать AI-compute / L1-флоу
- Фокус: **E2E и integration**, **тестовые окружения**, **CI quality gates**, **observability**, уверенность в релизах децентрализованной сети AI-вычислений

---

## Профиль

Инженер на стыке **QA-автоматизации** и **DevOps**: строю end-to-end тест-системы против реальных облачных стеков, встраиваю их в **CI/CD** и отношусь к стабильности релизов как к инженерному продукту.

В **Yofi** (USA, fintech / anti-fraud, масштаб Shopify) владел **serverless Robot Framework E2E** (`botnot-lambda-serverless-robot-test`, SST-стек `yofi-robot-e2e-test`): сюиты API, жизненного цикла магазина и performance — инжект **SNS/SQS**, вызовы API и ассерты состояния в **Spanner/Mongo**. Также вёл **integration-test environment** (SAM/pytest) против **ES / RDS / Neptune**. В **Sinoptics** — **Playwright** E2E и гибридная доставка **GitHub Actions → CodeBuild → ECR → K3S** для AI-нагрузок.

Комфортно с **распределёнными системами**, **AI inference/training** пайплайнами и инцидентным режимом. Готов перенести тот же подход к hardening релизов на **Gonka** (Cosmos SDK / Go L1, API + ML-ноды, Proof of Compute).

---

## Fit — Senior Tester-DevOps @ Gonka

| Потребность | Опыт |
|-------------|------|
| Меньше багов при выкатке | Регрессионный E2E: API + async-пайплайны + состояние БД; smoke + teardown для чистых прогонов |
| E2E / integration | **Robot Framework** (API / shop / performance); **pytest** integration env; **Playwright** UI E2E |
| Tester + DevOps | И тесты, и рантайм: **SST/CDK Lambda** runner, SAM, **K8s**, GitHub Actions / CodeBuild / Cloud Build |
| Окружения | Отдельный **integration-test-environment**; stage-aware SST (`dev`/`prod`) |
| Distributed / async | SNS/SQS → persist → API assert; webhooks, retries, изоляция данных |
| AI / compute | ML-routing и bot-detection в Yofi; on-prem **LLM/OCR** (Dify, Hatchet на K8s) в Sinoptics |
| Observability | Prometheus/Grafana (Helm), Slack-алерты, structured logs, участие в инцидентах |
| Blockchain L1 (Cosmos/Go) | Сильный бэкграунд по distributed systems; быстрый ramp-up на Cosmovisor, testnet, харнессы node/API/ML |

---

## Ключевые навыки

| Область | Инструменты и практика |
|---------|------------------------|
| E2E и API | **Robot Framework**, Python libraries, fixture events/expected JSON, **pytest**, **Playwright** |
| Test design | Smoke / regression / performance SLA; негативные сценарии; teardown и изоляция данных |
| CI/CD | **GitHub Actions**, AWS CodeBuild/CodeCommit, Google Cloud Build |
| IaC | **SST + AWS CDK**, SAM/CloudFormation, **Pulumi**, Helm |
| Runtime | AWS Lambda, API Gateway, SNS/SQS, **Kubernetes** (GKE, K3S), Docker |
| Валидация данных | Spanner, MongoDB, PostgreSQL/RDS, Elasticsearch, Neptune |
| Observability | Prometheus, Grafana, Cloud Logging/Monitoring, Slack |
| Домены | Fintech anti-fraud, AI/LLM-платформы, высоконагруженные event-пайплайны |

---

## E2E (Yofi / botnot) — ключевые факты

### Serverless Robot Framework E2E — `botnot-lambda-serverless-robot-test`

- SST-приложение **`yofi-robot-e2e-test`**: прогон **Robot Framework** в **AWS Lambda** (Python 3.9), CDK layers, stage profiles
- **API flow**: заказы в **PERSIST_TOPIC** → ассерт Spanner → проверка dashboard/customer/order API по expected JSON
- **Shop flow**: install/finish, billing upgrade, Shopify webhook/API, teardown продуктов/заказов
- **Performance flow**: latency-гейты на customer/order list (например, ответ ≤ 10s)
- Поддержка сюит при миграции ассертов Mongo → Spanner; стабилизация flaky-тестов

### Integration test environment — `botnot-integration-test-environment`

- SAM/pytest-харнес против **Elasticsearch, RDS, Neptune**
- CLI/conftest; задел под GitHub Actions

### UI E2E (Sinoptics + порталы Yofi)

- **Playwright**: auth, upload, multi-domain Next.js
- E2E-паттерны в Svelte merchant portal (`test:e2e`)

---

## Опыт работы

### QA / Platform Engineer — Sinoptics (AI / compliance)

*Март 2025 — н.в. · Remote*

- Качество web/platform: **Playwright** E2E, API/component checks, валидация перед деплоем
- Миграция **FastAPI + Celery + Redis** на **K3S**; CI/CD **GitHub Actions → CodeBuild → ECR → kubectl**
- On-prem **AI**-стек (Dify, PostgreSQL, Hatchet на K8s) — LLM/OCR как прод с бэкапами, TLS и алертами

### Data / Backend Engineer & Test Automation — Yofi (fintech / AI, USA)

*Февраль 2022 — март 2025 · Remote*

- **Serverless Robot Framework E2E** для Shopify anti-fraud платформы
- **Integration-test environments** и **pytest** по Lambda/data-сервисам
- **CI/CD** и IaC (SST/CDK, SAM, Pulumi); GKE, Spark/Airflow; документация API
- E2E валидация async-пайплайнов: webhooks → очереди → persist → API (аналог off-chain compute + on-chain учёт)

### Ранее — IT / системы (финансы)

*2003 — 2017*

- Руководство IT / финансовыми системами: ERP, отчётность, операционная надёжность

---

## Образование

- MBA, РАНХиГС (CIO), 2007
- К.ф.-м.н., Южный федеральный университет, 2003
- Специалист, радиофизика, ЮФУ, 1999

---

## Дополнительно

- Часовой пояс **UTC+8**; удобен async remote
- Сильные стороны: ownership релизов, воспроизводимые тест-окружения, понятные отчёты об отказах
- Мотивация: идея Gonka («AI compute as currency») и стабильные, «скучные» релизы testnet/mainnet

---

*Резюме для вакансии Senior Tester-DevOps @ Gonka (gonka.ai / github.com/gonka-ai/gonka)*

# Виталий Курносенко

**Senior ML Engineer | LLM · RAG · Document Intelligence · Agents**

**Местонахождение:** Шанхай, Китай (рассматриваю удалённый / гибридный формат)  
**Telegram:** @vitaly_kur  
**Email:** rikkimortycrypt@gmail.com  
**Языки:** Русский — родной; Английский — B2 (чтение технической документации и статей); Китайский — HSK 4

---

## О себе

ML / AI Engineer с практическим опытом построения **production-систем извлечения и анализа информации из документов** (PDF, сканы, изображения, HTML, DOCX) и **RAG / агентных пайплайнов** для финансовых и корпоративных сценариев. Сочетаю **3+ года hands-on ML/AI в продакшне** (Yofi Inc., Sinoptics AI) с **15+ годами опыта в финансах и корпоративном управлении**: МСФО/IFRS, казначейство, бюджетирование, финансовый контроль, аудит, работа с договорами и платёжными документами.

Понимаю банковский и корпоративный контекст изнутри: какие поля критичны в договоре, счёте-фактуре, коносаменте или регламенте; как проектировать **структурированный вывод (JSON Schema)**, валидацию и human-in-the-loop. Покрываю полный цикл: ingestion → OCR / парсинг → chunking / embedding → retrieval → LLM-генерация → постпроцессинг → оценка качества → эксплуатация.

---

## Ключевые навыки

| Область | Технологии и практики |
|---------|----------------------|
| **Извлечение из документов** | OCR (Vision LLM, специализированные OCR-сервисы), парсинг PDF / HTML / DOCX / XML, обработка сканов и фото, шаблонная и LLM-экстракция полей, NER, JSON Schema, constrained output, постпроцессинг и валидация |
| **RAG** | Dify, векторные индексы, semantic + metadata chunking, hybrid retrieval (dense + lexical), reranking, freshness / versioning KB, faithfulness / groundedness checks |
| **Агентные системы** | n8n, Dify workflows, LangChain-совместимые паттерны, multi-agent orchestration, tool calling, обработка ошибок и retry-логика |
| **LLM / NLP** | OpenAI-compatible API, prompt engineering, LLM-as-judge, structured extraction, multi-agent pipelines |
| **ML в продакшне** | Python, PyTorch-экосистема (Hugging Face Transformers, PEFT — практическое знакомство), feature engineering, классические ML-модели, A/B-тестирование, мониторинг качества |
| **Данные и инфра** | PostgreSQL, Redis, MongoDB, BigQuery, S3/GCS, Airflow, Spark, FastAPI, Celery, Docker, Kubernetes (K3S/GKE) |
| **Финансы (домен)** | МСФО/IFRS, управленческий и бухгалтерский учёт, казначейство, cash-flow, финансовый контроль, аудит, ERP/QAD, обработка инвойсов и договоров |
| **Оценка качества** | Golden datasets, precision/recall retrieval, faithfulness, human-in-the-loop review, A/B-эксперименты, регрессионные проверки пайплайнов |

---

## Опыт работы

### ML / AI Platform Engineer — Sinoptics AI
*Октябрь 2025 — наст. время · удалённо*

Платформа **AI-обработки корпоративных и финансовых документов**: счета-фактуры, договоры, транспортные накладные (коносаменты, ЖДН, авианакладные), compliance-материалы. End-to-end ownership: от ingestion до структурированного отчёта и risk assessment.

**Document Intelligence / парсинг:**

- Спроектировал и внедрил **мультиагентный пайплайн обработки документов**: ingestion (Telegram, WeChat, email, web, API) → OCR / Vision LLM → LLM-структурирование → оркестратор → специализированные агенты (Finance, Accounting, Lawyer, Logistics) → агрегированный validation / compliance / risk report.
- Реализовал **Dify workflow** (24 узла, 34 связи) для due diligence поставщиков: приём PDF/изображений → OCR / PDF parsing → LLM-извлечение полей инвойса → внешняя верификация контрагента → параллельный анализ 5 доменных агентов → итоговый отчёт.
- Разработал **OCR forms pipeline** (`ocr_forms`): шаблонная экстракция из сканов транспортных и торговых документов, заполнение структурированных форм, постпроцессинг и валидация извлечённых полей.
- Обеспечил **структурированный вывод** через JSON Schema и LLM-prompting: реквизиты, суммы, даты, контрагенты, условия договора; валидация и human-in-the-loop на этапе review.
- Интегрировал **парсинг web-источников и внешних API** (Tianyancha, QCC) для обогащения и верификации данных по контрагентам.

**RAG и агенты:**

- Построил **RAG-систему** на базе Dify для поиска по корпоративной базе знаний: chunking с метаданными (тип документа, версия, дата), векторные индексы, retrieval-контекст для агентов.
- Оркестрировал **n8n workflows** и **multi-agent architecture** (orchestrator → domain agents → aggregator) с RBAC, audit logs, обработкой ошибок и retry.
- Развернул **on-premise LLM-платформу** (Dify v1.10): Docker Compose, PostgreSQL, nginx + Let's Encrypt; миграция FastAPI + Celery в **K3S** на AWS EC2.

**Стек:** Python, FastAPI, Dify, n8n, LLM (OpenAI-compatible API), OCR / Vision AI, RAG, PostgreSQL, Redis, Docker, K3S/Kubernetes, AWS (EC2, ECR, CodeBuild, Secrets Manager), Yandex Cloud.

---

### ML Engineer / Data Engineer — Yofi Inc. (США)
*Февраль 2022 — Октябрь 2025 · удалённо*

Anti-fraud / customer intelligence платформа для enterprise Shopify-мерчантов (Lululemon). Полный ML-цикл в production: данные → модели → инференс → мониторинг.

- Разрабатывал **production ML-пайплайны**: bot-detection, скоринг злоупотреблений, feature engineering из поведенческих данных, real-time scoring через AWS SageMaker.
- Строил **ML gateway и A/B-тестирование моделей**: shadow-predicts, маршрутизация по фильтрам, безопасный rollout новых версий без риска для продакшна.
- Обрабатывал **1B+ событий** в Data Lake (GCS, BigQuery, Hudi/Delta); Spark-задачи на Kubernetes для подготовки обучающих выборок.
- Внедрил **мониторинг качества данных и моделей**, автоматическое тестирование пайплайнов, снижение инцидентов из-за data drift.

**Стек:** Python, SQL, PySpark, AWS SageMaker, Lambda, SQS/SNS, MongoDB, Neo4j, BigQuery, Airflow, dbt, Docker, Kubernetes (GKE).

---

### Руководитель корпоративных финансов / CFO — Shanghai (международная компания)
*2018 — наст. время · Шанхай*

- Построил **финансовые процессы с нуля**: бюджетирование, plan-fact, cash-flow planning, платёжный контроль, отчётность в QAD/ERP, материалы для совета директоров.
- Обеспечивал **финансовый контроль и audit-ready data flows**: сверки, внутренние контроли, взаимодействие с аудиторами, IFRS/CAS reporting.
- Работал с **юридическими и финансовыми документами**: договоры, инвойсы, банковские документы, compliance с HQ-процедурами.
- Автоматизировал отчётность и data workflows с **Python, SQL, Excel** — снижение ручного труда и повышение точности.

---

### Руководитель IT и финансового отдела — Engineering Solutions LLC
*Март 2013 — Декабрь 2017 · Москва*

- Руководил IT-инфраструктурой и **финансовыми системами**; внедрял ERP, автоматизацию управленческой и бухгалтерской отчётности.

### Начальник IT-отдела — New Engineering Solution
*Апрель 2003 — Февраль 2013 · Москва*

- Владел ERP, корпоративной IT-инфраструктурой и системами отчётности; внедрял структурированное управление данными.

---

## Релевантные проекты (document AI + финансы)

- **Telegram Supplier Due Diligence** — webhook-пайплайн: PDF/сканы → OCR → LLM parsing → 5 параллельных агентов (в т.ч. Finance, Accounting) → compliance / risk report.
- **OCR Forms** — извлечение данных из сканов коносаментов, ЖДН, авианакладных в структурированные шаблоны.
- **Invoice Bot (Yandex Cloud)** — автоматизация приёма и первичной обработки счетов-фактур.
- **Finance automation** — Python-скрипты для сверок, заполнения Excel-шаблонов, OCR + LLM для финансовых документов.

---

## Образование

- **РАНХиГС** — MBA, Информационные технологии *(2005–2007)*
- **Южный федеральный университет** (бывший РГУ) — аспирантура, кандидат физико-математических наук *(1994–2003)*

---

## Сертификаты

- **Certified Accountant Practitioner (CAP)** — финансовый учёт и отчётность (МСФО), управленческий учёт

---

## Дополнительно

- Уникальное сочетание **финансового домена (15+ лет) и production ML/LLM (3+ года)** — понимаю, какие данные извлекать из банковских и корпоративных документов и как валидировать результат.
- Готов обсуждать кейсы: **OCR + LLM extraction**, **RAG для регламентов и KB**, **multi-agent orchestration**, **A/B и quality monitoring**, **структурированный вывод и faithfulness**.
- Английский — на уровне чтения профессиональных статей, документации Hugging Face, OpenAI, Dify и технических RFC.

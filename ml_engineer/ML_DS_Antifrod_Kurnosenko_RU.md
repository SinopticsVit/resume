# Виталий Курносенко

**ML Engineer / Data Scientist | Антифрод и аномалии | Python · SQL · LLM**

**Местонахождение:** Азия (рассматриваю удалённый формат)  
**Telegram:** @vitaly_kur  
**Email:** rikkimortycrypt@gmail.com  
**Языки:** Русский — родной; Английский — B2 (Upper-Intermediate); Китайский — HSK 4

---

## О себе

ML Engineer / Data Scientist с практическим опытом разработки и эксплуатации антифрод-систем в production: детекция ботов, скоринг подозрительных заказов, фичеризация поведенческих данных, кластеризация покупателей. 3+ года работы в команде Yofi Inc. (США) — платформа защиты от мошенничества для Shopify-ритейлеров (Lululemon и другие enterprise-клиенты).

Покрываю полный ML-цикл: сбор и обработка данных → feature engineering → обучение моделей → интеграция в продакшн → мониторинг. Уверенно работаю с табличными данными, логами, событийными потоками и мультимодальными источниками. Имею опыт интеграции LLM-инструментов в прикладные задачи (Sinoptics AI).

---

## Ключевые навыки

| Область | Технологии |
|---------|-----------|
| **Языки** | Python (основной), SQL (PostgreSQL, BigQuery, Spanner, MSSQL, Trino) |
| **ML / антифрод** | Классические ML-модели (бот-детекция, скоринг злоупотреблений скидками, возвратами), AWS SageMaker, feature engineering, поведенческая аналитика, real-time scoring |
| **LLM / NLP** | Dify (LLM-платформа), RAG-пайплайны, LLM-агенты, OCR + LLM-обработка документов |
| **Данные** | Apache Spark (PySpark), Airflow, dbt, Airbyte, Hudi/Delta Lake, BigQuery, GCS, S3 |
| **Базы данных** | PostgreSQL, MongoDB, Neo4j (графовые сети мошенников), ArangoDB, Redis, Spanner |
| **Инфраструктура** | AWS (Lambda, SageMaker, SQS/SNS, EventBridge, S3), GCP (GKE, BigQuery, Pub/Sub), Docker, Kubernetes |
| **CI/CD** | GitHub Actions, AWS CodeBuild/CodeCommit, Google Cloud Build |

---

## Опыт работы

### ML Engineer / Data Engineer — Yofi Inc. (США)
*Февраль 2022 — Октябрь 2025 · удалённо*

Yofi — anti-fraud / customer intelligence платформа для Shopify-мерчантов (enterprise: Lululemon). Участвовал в разработке и поддержке ML-системы детекции мошенничества end-to-end: от инжиниринга признаков до вывода моделей в прод и мониторинга.

**ML / Антифрод:**

- Разрабатывал и сопровождал **pipeline bot-detection**: Lambda-сервис на Python получает события заказов (SQS), вызывает SageMaker-эндпоинты (модели: `botnot-botdetection-v2`, `discount_abuse`, `refund_model`), вычисляет `is_bot_score`, риски/доверие и публикует результаты в SNS для downstream-систем.
- Строил **feature-engineering сервис** (`yofi-lambda-feature-analytics`): извлечение поведенческих признаков покупателей из Shopify-заказов (паттерны возвратов, fuzzy-совпадения, геоданные, временные метрики), персистирование в Spanner, публикация в downstream ML-пайплайны.
- Участвовал в **ML-маршрутизации** (`yofi-lambda-ml-gateway`, `yofi-lambda-ml-controller`): серверный слой выбора модели по фильтрам, shadow-предикты в MongoDB, A/B-тестирование моделей без риска для продакшна.
- Разрабатывал **telemetry predictions** (`yofi-telemetry-predictions`): FastAPI-сервис для ML-предсказаний на основе поведенческой телеметрии пользователей (cloudBehavioral, journeyMetadata) — детекция бот-трафика по паттернам взаимодействия.
- Участвовал в проектировании **real-time severity engine** (`yofi-realtime-severity-engine`): движок real-time оценки серьёзности риска по событиям.
- Строил **кластеризацию покупателей** (`yofi-lambda-lululemon-cluster-formation-service`): кластеризация для сегментации подозрительной активности Lululemon.
- Работал с **графовыми базами данных** (Neo4j, ArangoDB) для построения сетей связей между аккаунтами, устройствами и поведенческими паттернами — обнаружение аномалий через граф-анализ.

**Данные и инфраструктура:**

- Построил Data Lake на основе GCS + BigLake + Hudi/Delta для аналитики фрода: хранение 1B+ событий (транзакции, сессии, логи Shopify) с партиционированием и оптимизацией для ad-hoc запросов.
- Поддерживал ~25 Airflow DAG в продакшне, включая пайплайны подготовки данных для ML: `raffles_to_hudi`, `mongodb_to_biglake`, `spanner_to_bigquery`, `analytics/sessions/stats`.
- Запускал **Spark-задачи на Kubernetes** (PySpark, Dataproc Serverless) для обработки исторических данных заказов и подготовки обучающих выборок.
- Интегрировал данные из Shopify, Klaviyo, Moonsense (поведенческая биометрия) через кастомные Airbyte-коннекторы и webhook-пайплайны.

**Стек:** Python, SQL, PySpark, AWS SageMaker, AWS Lambda, SQS/SNS, EventBridge, MongoDB, Neo4j, ArangoDB, Spanner, Redis, BigQuery, GCS, Hudi, Delta Lake, Airflow, dbt, Airbyte, Docker, Kubernetes (GKE), Pulumi.

---

### DataOps / AI Platform Engineer — Sinoptics AI
*Октябрь 2025 — Май 2026 · удалённо*

- Развернул **on-premise LLM-платформу** (Dify v1.10) для интеллектуальной обработки документов (счета-фактуры, договоры): Docker Compose, Ubuntu 22.04, PostgreSQL, nginx + Let's Encrypt.
- Спроектировал **мультиагентный пайплайн обработки документов**: n8n → специализированные AI-агенты (извлечение сущностей, классификация) → агрегатор → структурированный отчёт. Интегрировал OCR + LLM для понимания документов произвольного формата.
- Построил RAG-систему для поиска по корпоративной базе знаний; настроил векторные индексы и retrieval-контекст для агентов.
- Мигрировал FastAPI + Celery микросервис в **K3S кластер** на AWS EC2 (Китай): гибридный CI/CD (GitHub Actions → CodeCommit → CodeBuild → ECR → kubectl), секреты в AWS Secrets Manager.

**Стек:** Python, FastAPI, Dify, n8n, LLM (OpenAI-compatible API), RAG, Docker, K3S/Kubernetes, AWS (EC2, ECR, CodeBuild, Secrets Manager), PostgreSQL, nginx.

---

### Руководитель IT и финансового отдела — Engineering Solutions LLC
*Март 2013 — Декабрь 2017*

- Руководил IT-инфраструктурой и финансовыми системами; внедрял ERP и автоматизацию отчётности.

### Начальник IT-отдела — New Engineering Solution
*Апрель 2003 — Февраль 2013*

- Владел ERP, корпоративной IT-инфраструктурой и системами отчётности; внедрял структурированное управление данными.

---

## Образование

- **РАНХиГС** — MBA, Информационные технологии *(2005–2007)*
- **Южный федеральный университет** (бывший РГУ) — аспирантура, кандидат физико-математических наук *(1994–2003)*

---

## Сертификаты

- **Certified Accountant Practitioner (CAP)**
- Финансовый учёт и отчётность (МСФО), Управленческий учёт

---

## Дополнительно

- Опыт работы в международных командах (США, Китай, Таиланд, Россия), глубокое понимание cross-cultural коммуникации.
- Интерес к прикладным задачам безопасности и детекции аномалий; слежу за развитием ML-экосистемы и LLM-инструментов.
- Готов брать ownership за задачи end-to-end: от идеи и анализа данных до вывода в продакшн и мониторинга.

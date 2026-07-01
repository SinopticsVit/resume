# Курносенко Виталий Николаевич

**Antifraud Analyst (Senior)** | Правила антифрода · SQL-пайплайны · ML-скоринг · Платёжные риски

**Локация:** Шанхай, Китай (удалённо, GMT+8)  
**Гражданство:** Россия  
**Телефон:** +86 15601694273  
**Email:** vitaly@sinoptics.ai  
**WeChat:** porohnya  
**Telegram:** vitaly_kur  
**Языки:** русский — родной; английский — A1 рабочий уровень; китайский (мандарин) — HSK 4

---

## Профессиональное резюме

Senior antifraud analyst и инженер с **5+ годами** полного цикла ответственности за production **e-commerce anti-fraud платформу** (Yofi, США — enterprise Shopify-мерчанты, включая Lululemon). Проектирую, разрабатываю и поддерживаю правила детекции мошенничества, **SQL- и dbt-трансформации**, таблицы признаков и аналитические пайплайны; настраиваю пороги и контролирую баланс **ложных срабатываний / пропусков** в production.

Ориентирован на продукт и работаю самостоятельно: перевожу новые схемы мошенничества в data-driven контроли, провожу back-tests на исторических event data и доношу выводы до разработки, продукта и бизнес-стейкхолдеров. Практический опыт **скоринга заказов в реальном времени**, мультисигнальной валидации (BIN, IP, email, phone, address, device signals) и event-based ingestion на высоких объёмах.

**Кандидат физико-математических наук** — теория вероятностей и статистическое моделирование применяются к анализу эффективности правил и scoring logic. Дополнительно **15+ лет** в корпоративных финансах и банковских операциях — платёжные потоки, казначейство, карточные и переводные процессы, финансовый контроль — редкий предметный контекст для типологий мошенничества, связанных с платежами.

---

## Ключевые навыки

**Antifraud & Rules**  
Проектирование правил антифрода, YAML/config-driven параметры, настройка порогов, управление allowlist/blocklist, мультисигнальная валидация заказов (BIN, IP, email, phone, user agent, address), типологии bot/return/resell/claim/FTID abuse, классификация severity в реальном времени

**ML & Scoring**  
Скоринг на SageMaker, context-aware маршрутизация моделей, shadow predictions для offline validation, feature engineering для fraud signals, скоринг злоупотреблений на уровне customer/order (bot, return, resell, claim, fake profile)

**Data & SQL**  
Python, продвинутый SQL (CTEs, window functions, complex joins), dbt на BigQuery, оркестрация Airflow (~25 production DAGs), Spark на Kubernetes, Google Cloud Spanner, MongoDB, PostgreSQL; data quality tests и centralized schema definitions

**Payment & Banking**  
BIN validation, проведение платежей, казначейские операции, банковская документация, account management, card/transfer flows, cross-border transactions, financial compliance (IFRS/CAS)

**Tooling & Infrastructure**  
AWS Lambda, SQS/SNS/EventBridge, Git/GitHub Actions, CI-based rule updates, Airbyte ingestion, lakehouse patterns на GCS (Hudi/Delta); Advanced Excel и MS SQL для financial analytics

---

## Опыт работы

### Antifraud Analyst / Data Engineer — **Yofi Inc.** (США, удалённо)  
*Февраль 2022 — Октябрь 2025*

Anti-fraud и customer-intelligence платформа для **Shopify**-мерчантов (enterprise-клиенты, включая **Lululemon**). Миссия: детекция и предотвращение bot purchases, return fraud, discount abuse, reseller abuse и fake profiles в реальном времени.

**Правила антифрода и управление порогами**
- Владел **central fraud rules repository** — единый источник параметров детекции для мерчантов; per-client YAML configurations, настройка порогов, управление allowlist/blocklist.
- Построил автоматическую синхронизацию между runtime Python logic и batch SQL (dbt macros); PR-based rule updates через CI с parity checks между online и offline rule logic.
- Настраивал production thresholds — conservative merchant lists, return-rate parameters, allowlisted domains — балансируя detection coverage и false positive rate.

**ML-скоринг и маршрутизация**
- Построил и поддерживал **real-time ML scoring** (SageMaker + Lambda): bot probability, discount abuse, refund risk; blocklist/allowlist и trust/risk signal logic, управляющие downstream actions.
- Расширил **ML routing layer** — context-aware model selection для return abusers, resellers, claim abusers, LLM-based abuse и FTID fraud; shadow predictions сохранялись для offline validation и back-testing.
- Участвовал в **real-time severity classification**, питающей alert и escalation workflows.

**Валидация заказов и event data**
- Поддерживал **multi-signal order validation**: IP geolocation, user agent, credit card BIN, email, phone, shipping/billing address — интегрировано в fraud decision pipeline.
- Поддерживал **event-based ingestion** — orders, webhooks, partner streams — в analytical и operational stores для rules и models.

**Feature analytics и back-testing**
- Выпустил **return analytics и back-testing datasets**: return rates, refund line-item analysis, fuzzy customer pattern matching, new fraud typology detection; persisted в operational stores для batch model consumption.
- Построил **SQL rule logic и marts в BigQuery/dbt** для historical back-testing, rule efficiency analysis и monitoring scoring metrics.
- Проводил deep-dive analysis по confirmed abuse cases; переводил patterns в rule и feature updates.

**Data platform**
- Операционно управлял **~25 Airflow DAGs** и **Spark** workloads на Kubernetes для fraud data pipelines (GCS, BigLake, Hudi/Delta formats).
- Расширил **Airbyte** connectors для Shopify historical loads и partner data sources (Klaviyo, Moonsense).

**Стек:** Python, SQL, dbt, Airflow, Spark, SageMaker, BigQuery, Spanner, MongoDB, PostgreSQL, AWS, GCP.

### Business Analyst / AI Platform — **Sinoptics AI** (удалённо)  
*Март 2025 — настоящее время*

- Собирал и структурировал требования к document-processing workflows; определял **правила валидации** и acceptance criteria — включая false-positive review и risk assessment outputs.
- Строил **data flows на Python и SQL**, превращая semi-structured inputs в reusable datasets для product analytics и AI-assisted validation features.
- Координировал pilots и cross-functional delivery; готовил понятный status и risk reporting для non-technical stakeholders.

### CFO — **Shanghai Aircraft Design Limited Company** (Шанхай, Китай)  
*Ноябрь 2017 — 2022*

- С нуля спроектировал многоуровневые **контроли авторизации платежей**, spending limits и compliance frameworks для нового international entity.
- Полный цикл **banking relationship management**: account administration, payment execution, dispute resolution с financial institutions.

### Executive Director — **Engineering Solutions** / **New Technologies** (Китай / Россия)  
*2008 — 2017*

- Cross-border trade operations: **counterparty due diligence**, payment flow control, pricing and contract compliance в российской и китайской regulatory environments.
- Management accounting и financial control над procurement, sales и international payment cycles.

---

## Образование

- **Кандидат физико-математических наук**, Южный федеральный университет, 2000–2003  
  *Теория вероятностей, статистическое моделирование, математический анализ*
- **Диплом физика (специалист)**, Южный федеральный университет, 1994–1999
- **MBA**, РАНХиГС, 2005–2007
- **Колледж радиоэлектронной аппаратуры**, 1991–1995

---

## Сертификаты

- **CAP** — Certified Accountant Practitioner
- **Курсы профессионального развития CPA Russia:** финансовый учёт и IFRS reporting, управленческий учёт

---

# Eqvilent: подготовка по trading-аналитике

Этот файл — целевая прокачка под слабую сторону твоего профиля: **trading domain knowledge**. Базовый prep kit и mock drill уже есть в соседних файлах. Здесь — конкретно: как устроены данные, что Finance с ними делает, какие вопросы по трейдингу будут на интервью и как на них отвечать.

---

## 0. Map: твой реальный GitHub → Eqvilent talking points

Это самое важное. У тебя есть мощный технический портфель, но он не сформулирован как «релевантный финтехy». Ниже — каждый репо переведён на язык вакансии Eqvilent. Используй эти формулировки буквально, когда тебя спросят про опыт.

### `k3s-fastapi-app` — production document processing pipeline

**Что это:** FastAPI микросервис + Celery workers + Redis + Postgres + S3-storage. Развёрнут на K3s через AWS ECR/CodeBuild/CodeCommit, kubeconfig в AWS Secrets Manager. API с версионированием (`/api/v2025-12/process-documents`), task queue с polling статуса, тесты в `tests/unit`, `tests/integration`, `tests/services`, `tests/storage`.

**Как продавать в Eqvilent:**
> «Я строил production-grade pipeline для обработки документов: FastAPI как entry point, Celery для асинхронных задач, Postgres для metadata, S3-совместимое хранилище для файлов, Redis для очередей и кэша. Логика та же самая, что нужна для broker/exchange data ingestion: API получает запрос на обработку батча файлов, ставит задачу в очередь, worker качает данные из storage, обрабатывает их и пишет результат в Postgres со статусом для polling. Замени "documents" на "broker statements" — это та же архитектура, которую обычно строит Finance Engineering команда.»

**Ключевые слова для интервью:** `production pipeline`, `task queue`, `idempotency`, `task status polling`, `versioned API`, `S3 storage`, `Postgres metadata`, `pytest test pyramid`, `CI/CD`.

### `dify-workflow` + `dify_workflow_dsl` + `dify_devops_on_k3s` — workflow automation platform

**Что это:** Workflow для Telegram supplier due diligence: webhook принимает файлы, OCR/PDF parser извлекает данные, LLM парсит invoice, идёт валидация поставщика через Qichacha API, дальше **5 параллельных агентов** — Lawyer, Logistics, **Finance**, Marketing, **Accounting**. Финал — orchestration и validation report. **24 ноды, 34 ребра, parallel execution.** DSL в формате Dify App v0.4.0, конвертеры между версиями DSL, DevOps на K3s.

**Как продавать в Eqvilent:**
> «У меня есть production workflow с 24 нодами и параллельной обработкой через несколько агентов, включая Finance- и Accounting-agent. Это прямой аналог того, что Eqvilent описывает в вакансии — Make / n8n / Workato. Dify — это open-source workflow platform с похожей моделью: webhook-triggered, file ingestion, parallel branches, conditional routing, LLM nodes. Я не только строил эти workflows, но и писал tooling вокруг DSL: convert_to_dify_format.py для миграции между версиями формата и compare_format.py для diff структур. Если в Eqvilent есть существующие n8n/Workato workflows и их нужно переделать или мигрировать — у меня есть точно такой же опыт.»

**Ключевые слова:** `workflow automation`, `webhook-triggered`, `parallel agents`, `DSL versioning`, `multi-agent orchestration`, `Dify`, `n8n analog`.

### `checkinvoice-bot-yandex-env` — serverless invoice automation

**Что это:** Telegram bot `@checkinvoice_bot` на Yandex Cloud Functions (Python 3.12) + API Gateway (webhook routing) + Object Storage. 7-шаговый bash setup: install CLI → configure profile → service account → bucket → function → API Gateway → Telegram webhook. Полный teardown скрипт `cleanup.sh`.

**Как продавать:**
> «Это маленький, но показательный кейс: Telegram бот для check invoice на полностью serverless архитектуре. Function-based, без серверов, с автоматическим scaling. Ровно то, что Finance Team часто хочет: "вот PDF инвойса в Telegram → бот сразу даёт structured ответ". В Eqvilent такой же паттерн можно использовать для broker confirmations: trader или operations кидает PDF, serverless функция парсит, валидирует и пишет в БД.»

### `ocr_forms` — production OCR для transport/finance documents

**Что это:** Python скрипты для генерации шаблонов и заполнения структурированных документов: BL (Bills of Lading / коносаменты), JDN (ЖДН — железнодорожные накладные), AVIA (авиа накладные). Файлы: `create_template.py`, `create_bl_template.py`, `create_jdn_template.py`, `fill_all.py`, `fill_bl.py`, `fill_jdn.py`. Папки с реальными отсканированными документами.

**Как продавать:**
> «У меня есть боевой опыт с OCR и заполнением финансово-юридически значимых документов: коносаменты, железнодорожные и авиа накладные. Это документы, которые в логистике/торговле имеют ту же критичность, что broker statements в trading: расхождение в одной цифре превращается в financial loss или legal liability. Я разработал и template-генерацию, и autofill, и протестировал на реальных сканах. Тот же подход применим к broker statements: structured field extraction, validation rules, exception handling, output в стандартизованный формат.»

### `ocr_solutions_benchmark` — vendor evaluation

**Что это:** Сравнительный benchmark разных OCR подходов: text-only, text + location, vision-based, DeepSeek support. Тестируется на реальном `test_invoice.pdf`. Есть `schema.py` для структурированной валидации результата.

**Как продавать:**
> «У меня есть опыт vendor evaluation и benchmarking: я сравнивал text-only, text+location и vision-based решения для извлечения данных из инвойсов. Это та же задача, что выбор инструмента для парсинга broker reports: одни брокеры присылают чистые CSV, другие — PDF, третьи — Excel со sheet-ами разной структуры. У меня есть готовый pattern: structured schema → multi-vendor benchmark → выбор подхода по цене/качеству → integration.»

### `yandex-cloud-functions` + `yandex-db` + `postgresql-yandex-vm` + `yandex-cloud-env` + `yandex-keycloak` + `dify-vm-ubuntu`

**Как продавать (одной фразой):**
> «У меня полный hands-on experience с serverless functions, managed databases, self-hosted Postgres, IAM/Keycloak, Docker и K3s. То есть я могу не только написать Python-скрипт, но и довести его до production: контейнер, deployment, secrets management, monitoring, rollback. Для Finance Team это означает, что мои automations не сломаются через неделю, а будут жить годами с auditable changelog в Git.»

### Pitch одной фразой про GitHub в целом

> «У меня в `SinopticsAI` 17 приватных репозиториев — production document processing pipeline на FastAPI/Celery/Postgres/Redis/K3s, multi-agent workflow automation на Dify (24 ноды, параллельная обработка с Finance- и Accounting-agent), serverless Telegram bot для invoice checking, OCR для финансово-чувствительных документов, vendor benchmark, и полная cloud infrastructure под всё это. Это не "я учился Python", это production code, который работает в бизнесе.»

---

## 1. Базовая модель: как зарабатывает quant trading firm и что в этом важно для Finance

Без понимания этого ты не сможешь правильно отвечать на вопросы про PnL, fees и reconciliation. Запомни эту картину.

### Откуда деньги у фирмы типа Eqvilent

Eqvilent — **proprietary quantitative trading firm**: торгует своим капиталом, не управляет клиентскими деньгами. Источники дохода:

1. **Spread capture (market making):** ставят bid и ask, зарабатывают на разнице между покупкой и продажей. Тысячи мелких сделок в день, маленькая прибыль на каждой, большая в сумме.
2. **Statistical arbitrage:** модели находят временные mispricing между связанными инструментами (например, акция и её ETF, фьючерс и спот, два связанных futures).
3. **Latency arbitrage:** быстрее всех замечают новость или ценовое движение и торгуют на нём.
4. **Exchange rebates:** биржи **платят** market maker'ам за добавление ликвидности (так называемая `maker-taker` модель). Это часть PnL.

### Куда уходят деньги (cost side — где Finance играет роль)

1. **Exchange fees:** биржи берут плату за каждую сделку (для taker-ов), за market data, за connectivity, за co-location серверов.
2. **Broker / clearing fees:** комиссия брокера за исполнение и комиссия клирингового хауса за settlement.
3. **Financing / borrow costs:** если шортишь акцию — платишь borrow fee владельцу акции; если используешь leverage — платишь margin interest.
4. **Technology costs:** сервера, market data feeds (Bloomberg, Reuters, прямые exchange feeds), софт.
5. **Salaries и bonuses:** обычно крупнейшая статья.
6. **Regulatory & compliance:** licensing fees, audit, legal.

### Где Finance Team в этой картине

Finance делает **четыре вещи**, которые напрямую упомянуты в вакансии:

1. **Reconciliation:** убедиться, что то, что фирма "думает что наторговала", совпадает с тем, что брокеры/биржи показывают в своих отчётах. Это про точность данных.
2. **Fee analysis:** убедиться, что брокеры и биржи берут с фирмы ровно то, что прописано в контракте, и оптимизировать структуру комиссий (например, если по объёму вы попали в более выгодный tier — потребовать пересчёт).
3. **PnL attribution:** разложить PnL по источникам (по стратегиям, по asset classes, по биржам, по причинам), чтобы трейдеры и менеджмент понимали что именно работает.
4. **Cash & funding:** обеспечить, что у фирмы достаточно ликвидности на margin calls, settlement, broker funding, и оптимизировать использование капитала.

**Главная мысль для интервью:** Finance в quant firm — это не "посчитай бюджет на год". Это **continuous data quality function** для торговой деятельности.

---

## 2. Trade lifecycle: от order до cash settlement

Это **обязательно знать наизусть**. Вопрос «опиши жизненный цикл сделки» прозвучит почти точно. Ниже — упрощённая, но реалистичная картина.

### Шаг 1. Order (заявка)

Trader или algo генерирует заявку:
- `instrument: AAPL`
- `side: BUY`
- `quantity: 1000`
- `order_type: LIMIT`
- `price: 180.50`
- `account: PROP-ACC-01`
- `broker: BrokerA`
- `exchange: NASDAQ`
- `time_in_force: DAY`

Заявка летит брокеру или напрямую в exchange (если есть direct market access).

### Шаг 2. Order routing

Брокер маршрутизирует заявку. Может быть:
- direct to exchange (например, NASDAQ),
- через smart order router (заявка разбивается между несколькими venue),
- internalisation (брокер сам исполняет против своей книги).

### Шаг 3. Execution / Fill

Заявка пересекается с противоположной стороной. Может быть:
- **Full fill** — все 1000 акций исполнены по 180.50.
- **Partial fill** — например, 600 по 180.49, ещё 400 по 180.51.
- **Multiple fills** — заявка на 1000 разбивается на 12 fill-ов по 5–200 акций по разным микро-ценам.

Каждый fill = отдельная запись в системе с уникальным `fill_id`, `execution_timestamp` (в микро- или наносекундах), `venue`, `liquidity_flag` (maker/taker).

### Шаг 4. Trade booking

Внутренняя система фирмы записывает trade. Появляется `trade_id` (часто отличается от `order_id` и `fill_id`). Поля:
- `trade_id`, `parent_order_id`
- `instrument`, `side`, `quantity`, `price`, `currency`
- `trade_timestamp` (время исполнения)
- `value_date` / `settlement_date` (когда деньги/бумаги фактически перейдут)
- `broker`, `exchange`, `account`
- `commission`, `exchange_fee`, `clearing_fee`, `regulatory_fee`
- `pnl_strategy_id` (какая стратегия сгенерировала)

### Шаг 5. Allocation (если есть)

Если trader торгует на несколько sub-accounts или strategies, общий fill распределяется. Например, fill на 1000 акций → 600 в Strategy A, 400 в Strategy B.

### Шаг 6. Confirmation

Брокер присылает trade confirmation (часто через FIX message или end-of-day file). Это **первая точка сверки**: внутренняя запись фирмы vs broker confirmation.

### Шаг 7. Clearing

В большинстве регулируемых рынков сделки идут через clearing house (например, OCC для опционов в США, LCH для derivatives в Европе). Clearing house становится контрагентом для обеих сторон ("novation"). Считаются:
- net positions,
- margin requirements,
- fees clearing house.

### Шаг 8. Settlement

Финальная передача денег и бумаг. Стандарты:
- **Equities:** обычно T+1 в США (с 2024), T+2 в Европе.
- **FX spot:** T+2.
- **Futures:** daily mark-to-market, итоговый settlement на expiry.

В этот день деньги уходят / приходят на bank account, бумаги — на custodian account. Это **вторая точка сверки**: cash movements vs internal expectation.

### Шаг 9. PnL booking & reporting

В конце дня/недели/месяца:
- считается realized PnL (от закрытых позиций),
- unrealized PnL (от открытых позиций по mark-to-market),
- attributable PnL (по стратегиям, asset classes, traders),
- fees уходят в P&L как расход,
- всё попадает в management reporting.

### Что важно для аналитика FP&A

В каждой точке (Booking, Confirmation, Clearing, Settlement, PnL) могут быть **breaks** — расхождения. Работа Finance Analyst — найти, классифицировать и **закрыть** их.

---

## 3. Что Finance делает с trading data: 10 типичных задач

Когда тебя спросят «как ты понимаешь свою daily/weekly работу», у тебя должен быть готов список:

1. **Daily trade reconciliation:** свериться с broker statement по всем сделкам за день. Найти missing trades, duplicates, price/quantity mismatches.
2. **Position reconciliation:** на конец дня internal position должна совпадать с broker position и custodian position.
3. **Cash reconciliation:** все cash movements (settlements, fees, financing, transfers) должны совпадать между internal records и bank statements.
4. **Fee verification:** проверить, что комиссии брокера и биржи совпадают с контрактными ставками и достигнутыми tier-ами по объёму.
5. **Rebate tracking:** для market making — отследить exchange rebates, убедиться что начислены корректно, claim discrepancies.
6. **PnL attribution:** разложить дневной PnL по причинам (price move, новые сделки, comissions, financing).
7. **Margin & funding monitoring:** отследить margin requirements у всех брокеров, обеспечить funding, минимизировать idle cash.
8. **Corporate actions handling:** dividends, splits, mergers, tender offers — убедиться что внутренние данные обновлены и что фирма получила/заплатила правильные суммы.
9. **Regulatory & tax reporting:** подготовка данных для regulators, налогов, аудиторов.
10. **Process automation:** превратить пп. 1–9 из ручной работы в автоматический pipeline с alerts только по material breaks.

Если тебя спросят «что бы ты делал в первые 90 дней» — назови пп. 1, 2, 4 как фундамент, который надо взять под контроль, плюс п. 10 как долгосрочную цель.

---

## 4. Reconciliation deep dive: 4 типа

В вакансии `reconciliations` упомянуты **отдельной строкой**. Готовься, что спросят детально.

### 4.1 Trade reconciliation

**Что сверяем:** internal trade log vs broker confirmation.

**Источники:**
- Internal: trading system → внутренняя БД → CSV/Parquet или прямой DB query.
- External: broker daily file (CSV/Excel), FIX drop-copy, broker API, end-of-day statement (PDF).

**Matching key:**
- Идеально: единый `trade_id` или `external_id`.
- Если нет: composite key из `instrument + side + quantity + price + timestamp_bucket + broker + account`.
- Проблемные кейсы: брокер агрегирует наши fill-ы в один trade или наоборот.

**Типы breaks:**
- Missing in broker (мы видим, брокер нет).
- Missing internally (брокер видит, мы нет).
- Quantity mismatch.
- Price mismatch (даже на $0.0001 в HFT — это red flag).
- Side mismatch (BUY vs SELL).
- Timestamp / date mismatch (особенно из-за timezone).
- Duplicate trade.

**Tolerance rules:** в HFT часто допускается mismatch до 1 cent на mid-cap equity, 0 для futures, $0 для options.

### 4.2 Position reconciliation

**Что сверяем:** end-of-day position в internal system vs broker statement vs custodian.

**Почему отдельно от trade recon:** trades могут все совпасть, а position — нет. Причины: corporate action, transfer между accounts, manual adjustment, settlement date difference.

**Формула sanity check:**
```
opening_position 
  + sum(buys today)  
  - sum(sells today) 
  + corporate_action_adjustments 
  + transfers_in 
  - transfers_out
= closing_position
```

Если левая и правая части не совпадают — что-то потерялось между trade-level и position-level.

### 4.3 Cash reconciliation

**Что сверяем:** все денежные движения за день vs bank statement.

**Источники cash movements:**
- Settlements от закрытых сделок (T+1, T+2 etc).
- Margin calls / margin returns.
- Fees и commissions (списываются периодически).
- Interest на cash balances.
- Financing costs / borrow fees.
- Transfers между accounts.
- Dividend / coupon receipts.

**Главная боль:** разные cash movements падают на счёт в разные дни, не всегда одним общим bookings. Brokerы консолидируют по-своему.

**Approach:** строить ожидаемые cash movements per trade per value-date, агрегировать, сравнивать с bank statement, классифицировать unexpected items.

### 4.4 Fee reconciliation

**Что сверяем:** фактические fees от брокеров/бирж vs ожидаемые по контракту.

**Категории fees:**
- **Commission** (брокер): обычно cents per share / basis points от notional / fixed per contract.
- **Exchange fee:** maker/taker модель — taker платит, maker иногда получает rebate.
- **Clearing fee:** clearing house.
- **Regulatory fee:** SEC fee, FINRA TAF (US), FTT в некоторых юрисдикциях.
- **Connectivity / market data:** обычно monthly fixed, но бывает per-message.

**Tier rebates:** если за месяц объём превысил threshold — следующий месяц по более низкой ставке. Часто брокер забывает применить новый tier — Finance должен поймать.

**Approach:**
1. Для каждого trade посчитать expected_fee по правилам контракта.
2. Сравнить с actual_fee из broker statement.
3. Group by broker, exchange, asset class, tier.
4. Найти systematic overcharges → claim refund.

**Полезная цифра для интервью:** в крупных prop-firmах fee optimization может приносить **6–7-значные суммы в год**, поэтому Finance с этим серьёзно работает.

---

## 5. PnL для Finance Analyst: что разложить и как

PnL в quant firm — не одна строчка `revenue - cost`. Это разложение, которое Finance делает каждый день.

### Базовое разложение PnL дня

```
Daily PnL = Realized PnL + Unrealized PnL Δ - Fees - Financing
```

Где:
- **Realized PnL:** из закрытых сделок дня. Для long: `(sell_price - cost_basis) * qty`. Для short: `(short_entry_price - cover_price) * qty`.
- **Unrealized PnL Δ:** изменение mark-to-market по открытым позициям между вчерашним close и сегодняшним close.
- **Fees:** commissions + exchange + clearing + regulatory.
- **Financing:** margin interest, borrow costs (для shorts), funding rate (для perps в crypto).

### Attribution dimensions (по чему раскладывать)

- **Strategy / Algo:** какая стратегия сгенерировала сделки.
- **Asset class:** equities, futures, options, FX, crypto.
- **Venue:** NASDAQ, NYSE, CME, ICE, и т.д.
- **Trader / Desk.**
- **Time:** intraday hourly / daily / monthly.
- **Liquidity flag:** maker vs taker (важно для market making).

### Variance analysis (классический FP&A навык, переведённый на trading)

Если сегодняшний PnL хуже вчерашнего — почему? Раскладка:
- разница в gross PnL (price moves),
- разница в volume (меньше сделок),
- разница в fees (новый broker / новый tier / unusual venue mix),
- разница в financing,
- one-offs (corporate action, fat finger, system outage).

Это **прямое продолжение твоего опыта `plan-vs-actual`**, просто units другие. На интервью именно так и говори: «variance analysis для меня знаком на budget level — здесь логика та же, только dimensions другие».

---

## 6. Fees: как устроена структура и что с ней делает Finance

Готовься к вопросу «расскажи, как устроена комиссия за сделку».

### Maker / Taker модель

- **Maker:** ты добавил ликвидность (твоя limit-заявка стояла в книге, кто-то её "съел"). Часто получаешь rebate, например `-$0.0020 per share` (то есть exchange платит тебе).
- **Taker:** ты съел ликвидность (твоя marketable заявка пересеклась с уже стоящей). Платишь fee, например `+$0.0030 per share`.

В US equity market типичная картина: net `+$0.0010 per share` для taker против рынка. Для market maker (Eqvilent — это они и есть) задача — максимизировать долю maker fills.

### Tiered pricing

Большинство бирж дают объёмные скидки:
- Tier 1: до 0.1% market share → стандартные ставки.
- Tier 2: 0.1–0.5% → лучшие ставки.
- Tier 3: 0.5%+ → самые низкие.

Finance отслеживает monthly volume и **публично подтверждает у брокера/биржи** новый tier, а потом проверяет что fees пересчитаны.

### Other fees

- **Regulatory:** SEC fee на sells equities (~$22.10 per $1M в США, меняется), FINRA TAF (~$0.000166 per share). Маленькие, но в HFT суммируются.
- **Clearing:** OCC ($0.02–0.05 per options contract).
- **FTT:** Financial Transaction Tax в некоторых странах (Франция, Италия) — фиксированный % от notional.

### Fee analysis pattern

Когда говоришь «я бы построил fee analysis» — конкретно расскажи:
1. Загрузить все trades за период.
2. Посчитать `expected_fee` по правилам fee schedule.
3. Сравнить с `actual_fee` из broker invoices.
4. Group by `broker, exchange, asset_class, liquidity_flag, tier_period`.
5. Highlight `actual - expected > tolerance`.
6. Дать summary: total overcharge $XXX, by counterparty, with recommended action (claim refund / contract renegotiation / fix internal calc).

---

## 7. Capital, margin и financing — что должен знать Finance

Это часть, которую junior FP&A обычно не знает. Если расскажешь грамотно — сразу +1 в глазах интервьюера.

### Margin

Брокеры требуют залог под открытые позиции:
- **Initial margin:** при открытии.
- **Maintenance margin:** минимум для удержания.
- Если cushion упал ниже maintenance → **margin call**.

Finance мониторит:
- сколько margin usage по каждому брокеру (обычно как % от account equity),
- проекцию margin при экстремальных market moves (stress test),
- эффективность распределения капитала между брокерами (если у одного 80% used, у другого 20% — есть смысл переразложить).

### Financing

- **Long positions:** если на margin → платится `margin interest` (обычно benchmark + spread, например SOFR + 0.5%).
- **Short positions:** платится `borrow fee` (зависит от того, насколько hard-to-borrow акция).
- **Perpetual futures (crypto):** периодические `funding payments` между long и short (каждые 8 часов в большинстве exchanges).

### Cash management

- Минимизировать idle cash (он не зарабатывает).
- Поддерживать buffer для неожиданных margin calls.
- Управлять FX exposure (если торгуешь на нескольких continents — часть PnL в EUR, часть в JPY).

### Что говорить на интервью

Если вопрос «как бы ты помогал управлять капиталом» — скажи:
> «Я бы построил daily snapshot по каждому брокеру: equity, used margin, available margin, % utilization, ожидаемые settlement-cash flows на ближайшие T+1/T+2. Поверх этого — alert, если utilization превышает порог (например 70%), и weekly view на cross-broker оптимизацию. У меня есть прямой опыт `cash-flow projections under different scenarios` с CRAIC и Shanghai 929 — здесь та же логика, просто dimensions это брокеры и asset classes, а не контракты с поставщиками.»

---

## 8. Q&A bank: 18 вопросов с готовыми ответами

Это самые вероятные вопросы. Заучи структуру ответов, не дословно.

### Q1. Опиши жизненный цикл сделки от order до settlement

> Order → routing → execution с одним или несколькими fill-ами → trade booking с уникальным trade_id → allocation между sub-accounts → confirmation от брокера → clearing через clearing house → settlement в T+1 или T+2 в зависимости от инструмента → PnL booking и попадание в reporting. На каждом этапе возможны breaks: расхождение между internal log и broker confirmation, position vs custodian, expected vs actual cash movement, expected vs actual fee. Работа Finance — поймать и закрыть эти breaks ежедневно.

### Q2. Как бы ты делал daily trade reconciliation?

> Сначала уточнил бы цель: completeness, fee validation, position support или cash. Дальше — нормализация обоих datasets к общей schema: trade_id, instrument, broker, exchange, side, quantity, price, currency, trade_timestamp, settlement_date, fees, account. Match по trade_id если он есть, иначе composite key. Классификация breaks: missing internally, missing at broker, quantity, price, fee, currency, timestamp, settlement, duplicate. Reporting: summary by broker/exchange/asset_class/severity + detailed exception list для investigation. Автоматизация: daily run, alerts только на material breaks.

### Q3. Что такое maker/taker и почему это важно для Eqvilent?

> Maker добавляет ликвидность limit-заявкой и часто получает rebate, taker берёт ликвидность marketable заявкой и платит fee. Для market making firm типа Eqvilent это критично, потому что значительная часть P&L может идти от rebates, и доля maker fills — это KPI. Finance должен отслеживать долю maker/taker per venue, валидировать что rebates корректно начислены и что tier по объёму применяется правильно.

### Q4. Что такое broker statement и какие в нём бывают проблемы?

> Это ежедневный/ежемесячный отчёт от брокера с trades, positions, cash movements и fees за период. Типичные проблемы: разные форматы у разных брокеров (CSV, Excel со множеством sheet-ов, PDF), inconsistent column naming, агрегация trades по-своему (брокер может склеить наши 5 fill-ов в один trade или разбить), timezone разница в timestamp, fees не разнесены по конкретным trades а сложены в total per day, missing fields, late corrections к предыдущим дням.

### Q5. Чем equity сделки отличаются от futures с точки зрения Finance?

> Главные различия: settlement (equities T+1/T+2 vs futures daily mark-to-market), margin (equities — partial если на margin account, futures — initial+maintenance margin), fee structure (equities — commission+exchange+SEC/TAF, futures — exchange+clearing+broker), corporate actions (только у equities), borrow (только у equities если short), expiration (futures — да, equities — нет). Для Finance это значит разные модели расчёта PnL, разные cash flow patterns и разные reconciliation routines.

### Q6. Что такое slippage?

> Разница между ожидаемой ценой исполнения (например, mid-price в момент заявки или benchmark VWAP за период) и фактической ценой fill-а. Slippage отражает рыночный impact и качество execution. Для Finance это input в TCA (transaction cost analysis), который обычно делается совместно с trading desk. Для market maker slippage менее релевантен, потому что они limit-заявками и обычно не "съедают" ликвидность.

### Q7. Что такое clearing house и зачем он нужен?

> Это посредник между двумя сторонами сделки. После execution clearing house становится контрагентом для обеих сторон — это называется novation. Зачем: убирает counterparty risk (если ваш counterparty обанкротится, вы получаете settlement от clearing house), позволяет netting позиций, считает margin requirements централизованно, упрощает settlement. Примеры: OCC для опционов в США, LCH, Eurex Clearing, CME Clearing.

### Q8. Какие fees бывают и как их верифицировать?

> Categories: commission брокеру, exchange fee (maker rebate / taker fee), clearing fee, regulatory (SEC fee на sells, FINRA TAF), market data, connectivity. Tier-based pricing — чем больше объём, тем ниже ставка. Verification: для каждого trade посчитать expected fee по контракту, сравнить с actual, group by broker/exchange/asset_class/tier_period, найти systematic overcharges, claim refund. Часто брокер забывает применить новый tier после превышения порога — это типичный pattern, который Finance ловит.

### Q9. Как разложить дневной PnL?

> Realized PnL (из закрытых сделок) + изменение unrealized PnL (mark-to-market по открытым) − fees − financing. Дальше attribution по dimensions: strategy, asset class, venue, trader, liquidity flag, time. Variance analysis vs предыдущий период: что объясняет изменение — gross PnL move, volume, fee mix, financing, one-offs (corporate action, outage, fat finger).

### Q10. Расскажи про margin

> Initial margin — залог при открытии, maintenance margin — минимум для удержания. Если cushion падает ниже maintenance — margin call. Finance мониторит utilization per broker (как % от equity), проектирует margin при стресс-сценариях, оптимизирует распределение капитала между брокерами чтобы минимизировать idle cash и снизить риск margin calls. Для derivatives — initial+variation margin per clearing house rules, перерасчёт ежедневно по mark-to-market.

### Q11. Как ты бы автоматизировал ежедневный reconciliation процесс?

> Архитектурно: scheduled job (Airflow / Prefect / cron / Make / n8n) — забирает broker file из SFTP/email/API, забирает internal data из DB, нормализует обе стороны через pandas, делает merge по trade_id или composite key, классифицирует breaks по types, пишет результат в DB и Excel report, отправляет alert (Slack/email) только если material breaks. У меня есть прямой опыт похожей архитектуры в моём `k3s-fastapi-app`: API trigger → Celery task → S3/storage fetch → processing → Postgres write → polling status. Тот же pattern переносится один-в-один на reconciliation pipeline.

### Q12. Что бы ты сделал в первые 30/60/90 дней?

> 30 дней: разобраться в текущих процессах finance, ключевых брокерах/биржах/asset classes, существующих tooling (Python/SQL/Make/n8n), увидеть какие reconciliations уже работают, какие painful. Документировать текущие process maps. 60 дней: взять 1–2 painful manual processes, заавтоматизировать их под supervision senior. Параллельно — fee analysis с claim potential. 90 дней: делать ownership одного-двух daily reconciliations, начать proactively искать optimization opportunities, приносить metrics (часы сэкономлены, fees recovered).

### Q13. Расскажи про твой опыт с Python в финансовом контексте

> Используй конкретные репо: `k3s-fastapi-app` (production pipeline), `dify-workflow` (multi-agent automation с Finance/Accounting agents), `checkinvoice-bot-yandex-env` (serverless invoice automation), `ocr_forms` и `ocr_solutions_benchmark` (production OCR с benchmark и schema validation). Подчеркни — это **не учебные проекты**, это код, который сейчас в production на Yandex Cloud / AWS / K3s.

### Q14. Если расхождение в reconciliation — твой process?

> 1. Severity check: материально или нет (например, > $X в notional или > $Y в fees). 2. Категория: missing trade, quantity diff, price diff, fee diff, settlement timing? 3. Источник: internal mistake, broker mistake, timing issue, configuration issue? 4. Communication: trader/operations если internal, broker contact если broker-side. 5. Resolution: adjustment / refund / process fix. 6. Documentation: запись в issue tracker, обновление runbook если new pattern. 7. Prevention: если pattern повторяется — предложить process change или automation.

### Q15. Что такое corporate action и почему это важно для Finance?

> Событие по ценной бумаге: dividend payment, stock split, reverse split, merger, spin-off, tender offer, rights issue. Для Finance важно: корректная adjustment cost basis, проверка что ожидаемые cash receipts (dividends) пришли, что position adjustments применены, что налоги правильно удержаны. Mismatch здесь обычно становится причиной "phantom" position breaks или unexpected cash discrepancies на следующий день.

### Q16. Как бы ты подошёл к выбору workflow automation tool (Make vs n8n vs Workato vs Python)?

> Зависит от: complexity of integrations (готовые connectors vs custom code), volume (lightweight automation vs heavy ETL), requirements на data quality and audit trail, team skill mix (low-code для finance team или Python для engineering ownership), security/compliance (где хранятся credentials, есть ли SOC 2 у вендора), cost. Моё general правило: для simple integrations с готовыми connectors — n8n/Make (быстро, версионируемо, accessible для non-engineers). Для heavy data processing с custom logic и production criticality — Python service. Для гибридных кейсов — n8n как orchestrator вызывает Python microservices. У меня есть production опыт с Dify (близкий аналог n8n с LLM агентами) — workflow с 24 нодами и параллельной обработкой.

### Q17. Какие KPI ты бы трекал для своей работы?

> Operational: daily reconciliation completion time, # breaks open / closed / aging, broker SLA compliance. Quality: % auto-resolved vs manual, mean time to resolution, recurring vs new break types. Financial: fees recovered through claims, cost savings from automation, capital efficiency improvement. Process: workflows automated, hours saved per week, processes documented. Communication: stakeholder satisfaction (trader/management/audit).

### Q18. Почему мы должны взять тебя на эту позицию?

> У меня уникальное сочетание трёх вещей: (1) **15+ лет finance discipline** — controls, reconciliations, audit, IFRS, treasury, plan-vs-actual, board reporting, я понимаю почему точность критична и как её обеспечивать; (2) **production-grade Python и automation experience** — у меня в SinopticsAI 17 приватных репозиториев с FastAPI/Celery/Postgres/K3s/Yandex Cloud, multi-agent workflows на Dify, serverless functions, OCR/document processing — это код, который работает в бизнесе сейчас; (3) **process design mindset** — я строил finance functions с нуля, написал procedure framework для procurement/contracts/payments/budgeting в Shanghai 929. Я не junior с Python и не senior без рук. Я hybrid, который сразу даёт value на reconciliation, fee analysis, automation и process improvement.

---

## 9. Тактика «не знаю» — как выкручиваться правильно

Если спрашивают про что-то узко-специфическое, чего ты не знаешь — **не выдумывай**. Используй один из паттернов:

### Паттерн A: «Не знаю, но знаю похожее»

> «Я конкретно с этим инструментом / стандартом не работал, но похожая логика есть в [твой опыт]. Думаю, базовая механика [твоё предположение]. Если попадёт в work scope — быстро дочитаю первоисточник.»

Пример:
> «Я не работал напрямую с CME Clearing, но clearing house mechanic в принципе похожа: novation, daily margining, variation margin. Я бы начал с rulebook и broker contract — там всё расписано.»

### Паттерн B: «Не знаю, и это разумный gap»

> «Честно — не знаком с [X]. Это знание приходит обычно изнутри trading firm, я в нём пока не варился. Но базовая логика [Y] мне понятна, и я быстро учусь — у меня в GitHub есть свидетельство, что я с нуля разобрался в OCR, Yandex Cloud, K3s, FastAPI и Dify.»

### Паттерн C: «Уточняющий вопрос»

Иногда вопрос неоднозначный. Не отвечай наугад — переспроси:

> «Уточню: вы про reconciliation на trade-level или на position-level? Подходы разные.»

Это **признак сильного аналитика**, а не слабого: ты сначала уточняешь scope, потом отвечаешь.

### Чего НЕ делать

- Не говорить уверенно неправильное (интервьюер сразу слышит).
- Не оправдываться долго («я бы конечно мог если бы…») — звучит слабо.
- Не сводить всё к «у меня нет опыта» — после fact дай позитив (как закроешь gap).

---

## 10. Что ожидать на технический screen / Python case

Если будет live-кодинг или take-home, скорее всего это будет один из паттернов:

### Pattern A: Reconciliation case

Дают два датасета (CSV/JSON) — internal trades и broker statement. Просят:
1. Загрузить и нормализовать.
2. Найти missing, duplicates, mismatches.
3. Собрать exception report.

**Минимально достаточный pandas-skeleton (что показывать):**

```python
import pandas as pd

internal = pd.read_csv("internal_trades.csv")
broker = pd.read_csv("broker_statement.csv")

for df in (internal, broker):
    df["trade_date"] = pd.to_datetime(df["trade_date"])
    df["price"] = df["price"].astype(float)
    df["quantity"] = df["quantity"].astype(int)
    df["fee"] = df["fee"].astype(float)

merged = internal.merge(
    broker,
    on="trade_id",
    how="outer",
    suffixes=("_int", "_brk"),
    indicator=True,
)

missing_in_broker = merged[merged["_merge"] == "left_only"]
missing_in_internal = merged[merged["_merge"] == "right_only"]

both = merged[merged["_merge"] == "both"].copy()

both["qty_diff"] = both["quantity_int"] - both["quantity_brk"]
both["price_diff"] = both["price_int"] - both["price_brk"]
both["fee_diff"] = both["fee_int"] - both["fee_brk"]

PRICE_TOLERANCE = 0.01
FEE_TOLERANCE = 0.005

quantity_breaks = both[both["qty_diff"] != 0]
price_breaks = both[both["price_diff"].abs() > PRICE_TOLERANCE]
fee_breaks = both[both["fee_diff"].abs() > FEE_TOLERANCE]

with pd.ExcelWriter("recon_report.xlsx") as writer:
    missing_in_broker.to_excel(writer, sheet_name="missing_in_broker", index=False)
    missing_in_internal.to_excel(writer, sheet_name="missing_in_internal", index=False)
    quantity_breaks.to_excel(writer, sheet_name="quantity_breaks", index=False)
    price_breaks.to_excel(writer, sheet_name="price_breaks", index=False)
    fee_breaks.to_excel(writer, sheet_name="fee_breaks", index=False)
```

У тебя точно такой же подход уже реализован в `eqvilent_reconciliation_mini_case.py`. **Открой его перед интервью** и держи в голове: импорт → нормализация → merge → классификация → отчёт.

### Pattern B: Fee analysis case

Дают trades + fee schedule. Посчитать expected vs actual fees, найти overcharges.

Логика:
```python
def expected_fee(row, schedule):
    rate = schedule.loc[
        (schedule["broker"] == row["broker"])
        & (schedule["exchange"] == row["exchange"])
        & (schedule["asset_class"] == row["asset_class"]),
        "rate_per_share",
    ].iloc[0]
    return rate * row["quantity"]

trades["expected_fee"] = trades.apply(lambda r: expected_fee(r, schedule), axis=1)
trades["fee_diff"] = trades["actual_fee"] - trades["expected_fee"]

summary = (
    trades.groupby(["broker", "exchange", "asset_class"])
    .agg(total_diff=("fee_diff", "sum"), n_trades=("trade_id", "count"))
    .sort_values("total_diff", ascending=False)
)
```

### Pattern C: SQL case

Базовые: aggregations, joins, window functions. Не углубляйся в редкое — основа: `GROUP BY`, `JOIN`, `LEFT JOIN`, `LAG/LEAD`, `ROW_NUMBER() OVER (PARTITION BY)`, CTEs.

### Что говорить вслух во время кодинга

- Сначала формулируй approach, потом пишешь код.
- Проговаривай assumptions: «Я предполагаю, что trade_id уникален в обоих файлах, иначе нужен composite key».
- Когда пишешь — комментируй edge cases: «А если price пришёл как строка с запятой вместо точки — нужен парсер».
- В конце — что бы добавил для production: tests, logging, error handling, idempotency, alerting.

---

## 11. Чек-лист «прокачать перед интервью»

Перед интервью пройдись по этому списку. Если на каждый можешь ответить за 60 секунд — ты готов.

### Trading vocab (must-have)
- [ ] Maker vs taker
- [ ] Trade lifecycle: order → fill → trade → confirmation → clearing → settlement
- [ ] T+1 / T+2 settlement
- [ ] Initial margin vs maintenance margin
- [ ] Realized vs unrealized PnL
- [ ] Long vs short, borrow fee
- [ ] Equities vs futures vs options vs FX — basic differences
- [ ] Corporate action examples
- [ ] Clearing house role (OCC / LCH / CME Clearing)
- [ ] Slippage / TCA basic concept

### Finance domain
- [ ] 4 типа reconciliation (trade, position, cash, fee)
- [ ] Fee categories (commission, exchange, clearing, regulatory)
- [ ] Tiered pricing logic
- [ ] PnL attribution dimensions
- [ ] Margin monitoring KPI
- [ ] Cash management basics для multi-broker setup

### Твой own portfolio
- [ ] Один pitch-line про каждый из 6 ключевых репо (см. секция 0)
- [ ] Готовый ответ «расскажи про самый сложный технический проект»
- [ ] Готовый ответ «расскажи про процесс automation, который ты автоматизировал»
- [ ] Готовый ответ «как ты пришёл от finance к technical work»

### Поведенческое
- [ ] Все 4 STAR-истории отрепетированы (из основного prep kit)
- [ ] Salary разговор отрепетирован (из основного prep kit)
- [ ] 3 вопроса им (выбрать заранее)

### Технически готовое
- [ ] `eqvilent_reconciliation_mini_case.py` запущен сегодня — `eqvilent_reconciliation_report.xlsx` под рукой
- [ ] Резюме `Financial_Analyst_Kurnosenko_EN.pdf` ещё раз перечитан, чтобы ты помнил даты и формулировки
- [ ] GitHub `SinopticsAI` ты можешь показать с экрана если попросят (даже если репо приватные — ты можешь screen-share структуру)
- [ ] Тихая комната, наушники, проверенный микрофон, стабильный интернет
- [ ] Стакан воды

---

## 12. Финальный mindset для входа в интервью

**Ты не junior, который выпрашивает работу.** У тебя 15 лет finance leadership experience и production technical portfolio. Ты пришёл обсудить, **подойдёт ли вам ваша роль вашему профилю** — это разговор двух взрослых людей.

**Ты не должен знать всё про trading.** Eqvilent ищет аналитика, а не trader-а. Им важно, что ты понимаешь **финансовую дисциплину** (это у тебя есть железно), умеешь **структурировать данные и автоматизировать** (это у тебя есть в production), и **быстро учишься домейну** (это видно из того, как ты выучил K3s, FastAPI, Dify, Yandex Cloud за 1–2 года).

**Главное правило по trading-вопросам:** если знаешь — отвечай чётко и кратко. Если не знаешь — честно скажи, дай ближайшую аналогию из своего опыта, обозначь как закроешь gap. Это **сильнее**, чем выдумывать.

Удачи. Ты готов лучше, чем тебе кажется.

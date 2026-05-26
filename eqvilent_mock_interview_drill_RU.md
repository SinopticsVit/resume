# Mock Interview Drill на русском для Eqvilent

## Как использовать

Прогнать два раза:

1. Первый прогон: отвечать свободно, записать себя, не останавливаясь.
2. Второй прогон: сократить каждый ответ до 60-90 секунд и держать структуру.

Целевой тон: спокойный, точный, senior, hands-on. Не оправдываться за отсутствие trading desk опыта, а показывать быстрый ramp-up и сильную базу в finance controls, data и automation.

## 0-5 минут: Opening pitch

### Вопрос

Расскажите о себе.

### Целевой ответ

Я финансовый и операционный специалист, сейчас базируюсь в Шанхае. У меня более 15 лет опыта в budgeting, treasury, cash-flow planning, management reporting, financial control, audit support и cross-border operations. В последних ролях я строил финансовые процессы с нуля, готовил budgets и plan-vs-actual analysis, занимался payment planning и banking workflows, взаимодействовал с аудиторами и настраивал reporting logic в QAD/ERP.

Моя сильная сторона для этой роли — сочетание финансовой дисциплины и технического исполнения. Я использую Excel, SQL, Python и automation, чтобы структурировать данные, уменьшать ручную работу и создавать повторяемые reporting workflows. Также у меня есть hands-on проекты: OCR/document processing, Excel automation, FastAPI, PostgreSQL, Docker/K3s, Celery/Redis и cloud deployment.

Эта позиция мне особенно интересна, потому что она объединяет finance operations, trading data analysis, reconciliations, Python и workflow automation. Это именно то направление, в котором я хочу развиваться.

## 5-15 минут: Motivation and fit

### Почему Eqvilent?

Eqvilent интересен мне как quantitative trading company, где финансы тесно связаны с data, speed, accuracy и automation. Мне интересна среда, где финансовые процессы — это не только routine reporting, но и data flows, controls, exceptions и technical workflows.

Мне также близка remote-first и technical culture компании. По описанию видно, что компания ценит precision, speed, independent thinking и сильную инфраструктуру. Это совпадает с типом среды, где я могу быть полезен и расти.

### Почему эта роль?

Потому что она объединяет несколько направлений, которые мне интересны: finance operations, data analysis, Python, reconciliation и process automation. У меня сильная финансовая база, но я не ищу только традиционную finance management role. Я хочу более technical finance role, где можно работать напрямую с данными и улучшать workflows.

### Почему переход с CFO / senior finance роли на Analyst?

Для меня сейчас важнее не title, а содержание роли и среда. Мне интересна hands-on работа с data и process improvement в сильной quant trading company. Мой CFO experience помогает, потому что я понимаю financial controls, governance, reporting quality и stakeholder expectations. При этом мне комфортно делать детальную работу: cleaning data, checking exceptions, writing scripts и building reports.

## 15-25 минут: Finance experience

### Расскажите о finance process, который вы построили с нуля

Ключевой ответ:

В Shanghai Nine-Two-Nine Aircraft Design Limited Company нужно было запустить финансовую функцию практически с нуля для международной команды в Китае. Необходимо было выстроить procurement, contract approval, payment controls, budgeting, cash-flow planning, reporting и audit interaction.

Я разработал процедуры согласования закупок и договоров, правила budgeting и financial control, payment planning, cash-flow scenarios и reporting materials. Координировал работу с banks, auditors, founders and board. Также создал structured process для document control и approval flow.

Результат: компания получила рабочую finance operating model с controlled payments, clearer budgeting, audit-ready documentation и better management visibility. Для Eqvilent это релевантно, потому что роль требует process mapping, finance operations, controls и workflow optimization.

### Как вы обеспечиваете accuracy in financial data?

Я начинаю с source control: откуда приходят данные, кто их owner и сохраняется ли raw data. Затем определяю consistent structure: dates, currencies, entities, accounts, categories и responsible owners. После этого использую reconciliation checks, variance thresholds, duplicate checks, missing-value checks и approval logic. Финальный output должен быть explainable: summary report, detailed exception list и clear ownership по каждому break.

Для Eqvilent я бы применял тот же подход к broker and exchange data: raw source preservation, normalization, matching logic, exception classification и automated reporting.

### Как вы делаете plan-vs-actual analysis?

Plan-vs-actual analysis — это не просто сравнение цифр. Сначала нужно определить структуру: period, department, cost category, project, entity, currency и responsible owner. Затем сравнить actuals with budget и выделить material variances. После этого важно классифицировать variances: timing, price, volume, FX, one-off, structural change или data issue. Финальный шаг — объяснить, какое действие требуется: update forecast, control spending, investigate data или adjust assumptions.

## 25-40 минут: Trading data and reconciliation

### Как бы вы сверяли internal trading data с broker data?

Сначала я бы уточнил objective reconciliation: trade completeness, fees, cash, positions или PnL support. Затем определил бы data sources и schema: trade ID, instrument, broker, exchange, account, side, quantity, price, currency, timestamp, settlement date and fees.

Далее я бы нормализовал оба datasets: column names, date formats, time zones, currencies, instrument identifiers и numeric precision. Если есть trade ID, я бы match by trade ID. Если trade ID отсутствует или unreliable, использовал бы composite key: instrument, side, quantity, price, broker, account и timestamp bucket.

После matching я бы классифицировал exceptions: missing internally, missing at broker, quantity difference, price difference, fee difference, currency mismatch, settlement date mismatch, duplicate или aggregation issue. Output должен включать summary by broker, exchange, asset class and severity, плюс detailed exception report for investigation.

### Какие common breaks бывают?

- Missing trade on one side.
- Duplicate trade.
- Quantity mismatch.
- Price mismatch.
- Fee or commission mismatch.
- Currency mismatch.
- Timezone or timestamp issue.
- Settlement date mismatch.
- Instrument identifier mismatch.
- Aggregation issue between trade-level and daily summary data.

### Как бы вы решали timezone problems?

Сначала я бы определил source timezone для каждой системы и сохранил original timestamp. Затем привел бы все timestamps к одному стандарту, обычно UTC, и при необходимости оставил отдельные колонки: raw timestamp, source timezone, normalized timestamp. Для matching я бы не полагался только на exact timestamp, потому что между системами могут быть delays. Лучше использовать trade ID, а если его нет — tolerance window.

### Как бы вы проверяли broker fees?

Я бы сравнивал broker-reported fees с expected fees based on exchange, broker, asset class, instrument, quantity и fee schedule. Затем группировал бы differences по broker, exchange, asset class and date, чтобы увидеть systematic differences. После этого классифицировал бы differences: rounding, FX conversion, fee schedule change, missing fee component или data issue.

## 40-50 минут: Python and automation

### Объясните mini-case

Я подготовил небольшой reconciliation mini-case с internal trades и broker statement data. Скрипт нормализует даты, строки и числовые колонки, делает merge двух datasets по trade ID, классифицирует exceptions и формирует Excel report с raw data, exceptions и summary.

Exception types включают missing trades, fee mismatch, quantity mismatch и currency mismatch. В реальном workflow я бы расширил это composite-key matching, time tolerance, fee schedules, daily automation и alerting.

### Что бы вы автоматизировали первым?

Сначала я бы mapped current manual workflow и нашел highest-volume repeated steps. Обычно лучший первый target — data ingestion and normalization: получать broker/exchange files или API data, стандартизировать schema и формировать clean input dataset. Второй target — reconciliation checks и exception reporting. Третий — alerts and scheduled reporting.

Главное — не over-automate до того, как controls ясны. Сначала сделать logic correct and explainable, потом автоматизировать.

### Как бы вы описали workflow?

Data source -> ingestion -> normalization -> validation -> reconciliation -> exception classification -> report/dashboard -> alert/escalation -> archived raw data.

Можно сказать так:

> I would first make the process transparent and controlled, and only then automate it. In finance data, a fast wrong process is worse than a slower controlled process.

## 50-55 минут: Salary

### Основная версия

С учетом гибридного характера роли, где сочетаются finance operations, trading data analysis, Python-based reporting, reconciliations и workflow automation, я бы ориентировался на диапазон примерно USD 90,000-105,000 gross annually. Финальная цифра зависит от scope, seniority level, bonus structure и общего benefits package.

### Более мягкая версия

Я готов обсуждать диапазон USD 80,000-100,000 gross annual, в зависимости от полного scope роли и total compensation package.

### Если давят ниже

Я понимаю, что compensation может зависеть от internal level и scope. Для роли с таким сочетанием finance, Python, trading data, reconciliation и automation я бы предпочел оставаться выше USD 80,000 gross annually. Но я готов обсуждать full package, включая bonus, growth path, responsibilities и timeline for review.

## 55-60 минут: Questions to ask them

Задать 4-6 вопросов, не все сразу.

1. What are the main data sources for this role: brokers, exchanges, internal systems, databases, files, or APIs?
2. What reconciliation breaks are most painful for the Finance Team today?
3. How much of the role is recurring reporting vs process automation?
4. What Python stack and workflow tools does the team use?
5. What would success look like after 3 and 6 months?
6. Is compensation structured as base only, or is there also a bonus component?

## Финальное closing

Спасибо за разговор. Роль мне еще более интересна, потому что она находится ровно на пересечении finance operations, trading data, Python automation и process improvement. Я считаю, что могу принести сильную financial discipline и hands-on technical execution, при этом быстро войти в вашу специфику broker and exchange data flows.

## Быстрый чек-лист перед интервью

- Pitch на 60 секунд выучен.
- Готов ответ на вопрос “Why Eqvilent?”.
- Готов ответ “Why Analyst after CFO?”.
- Готов honest answer про отсутствие direct trading desk experience.
- Повторены trade, order, fill, broker statement, exchange fee, settlement, clearing, margin, PnL.
- Готов reconciliation case на 2 минуты.
- Готов пример Python/automation project.
- Готов salary answer: USD 90k-105k или мягко USD 80k-100k.
- Подготовлены 4-6 вопросов интервьюеру.


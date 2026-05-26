# Eqvilent Interview Insights на основе реальных отзывов

Файл основан на 41 интервью-отзыве и 20 employee reviews из feedback-документа. Цель — дать тактику именно под их специфический процесс, а не общие советы.

## 1. Что нужно знать про их процесс

### Многоэтапность

- Типичный процесс: 4-8 этапов, 2-8 недель.
- Для аналитических ролей характерно: HR screening, take-home test, технический интервью, behavioral, hiring manager, иногда CEO.
- Они сами в ответах подтверждают, что "process is thorough by design" и "we are building long-term teams".
- Вывод: настраивайся на марафон, а не спринт. Не выгорай морально на 2-3 этапе.

### NDA и non-compete

- Тема всплывает почти в каждом отзыве. У них есть NDA, который обсуждается с первого звонка.
- Часть кандидатов жаловалась на длинный non-compete (упоминания 2 лет, в одном отзыве даже про 15 лет, на что компания ответила "such terms are only for CEO").
- Они защищают свою бизнес-конфиденциальность, поэтому даже фидбек после rejection часто скрыт за NDA.
- Тактика: спокойно принять NDA как часть процесса. Не надо торговаться или возмущаться. Можно мягко уточнить срок non-compete после probation period.

### Take-home assignments

- Почти все технические роли проходят через home test.
- Для Data Analyst это был "Python script for web scraping of OKX crypto exchange".
- Для Quantitative Analyst — "go through and identify all the errors in a HFT data set".
- Time investment: от 2 часов до недели, обычно 1-2 рабочих дня.
- Один кандидат жаловался, что задание выглядело как реальная работа компании. Они отвечают: "designed for evaluation, not for production".
- Тактика: для FP&A ожидай задание с реальными trading-data flavored файлами. Скорее всего: даны broker/exchange data, нужно очистить, сверить и выявить exceptions.

### Коммуникация

- Часто медленная: 2-4 недели между этапами.
- Иногда теряют кандидатов или не дают финальный feedback.
- Компания признает это и работает над улучшением.
- Тактика: не паникуй при молчании. Переспрашивай вежливо, но не чаще раза в 7-10 дней. Держи параллельные процессы.

### Стиль interview

- Многие пишут: "more like a conversation than examination".
- Любят разговор о challenges, projects, мотивации.
- Любят, когда кандидат задает вопросы.
- Ценят personality, не только skills (история про лошадей стала ice-breaker для одного кандидата).
- Тактика: вести себя как partner, не как кандидат на коленях. Спокойно, по-взрослому, с personal hooks.

### Feedback после rejection

- Часто отказывают без детального feedback.
- Это политика компании, не личное.
- Тактика: не пытайся вытащить feedback силой, не пиши гневные письма. Это сильно влияет на внутреннюю репутацию (видно по отзыву Infrastructure Security Engineer, где кандидат пошел искать Head of Recruitment через OSINT — выглядит дико).

## 2. Предполагаемый процесс для Analyst (FP&A)

На основе отзывов Data Analyst, Quantitative Analyst, Financial Analyst-смежных ролей:

1. HR screening (30-45 минут).
2. Take-home assignment (1-7 дней).
3. Technical interview по результатам assignment.
4. Hiring manager interview (Finance Team lead).
5. Behavioral / culture interview (HR + senior).
6. Meeting с top management / CEO (по их паттерну для senior-level кандидатов).

Между этапами — паузы, иногда 1-3 недели.

## 3. Тактика по этапам

### Этап 1: HR screening

Что они проверяют:

- Английский (mandatory).
- Мотивацию: Why Eqvilent? Why this role?
- Salary expectations.
- Готовность к NDA.
- Background и логику последних переходов.
- Soft signal: насколько ты приятен в общении.

Что говорить:

- Краткий pitch (60 секунд).
- Конкретное "почему Eqvilent": quant trading, data, automation, remote, technical culture.
- Salary в диапазоне USD 90,000-105,000 gross annually (мягкая версия 80-100).
- "I am comfortable with NDA, please share details so I can review them properly."
- Про non-compete: "I am open to discuss reasonable non-compete terms after probation period, depending on scope."

Что НЕ делать:

- Не спорить про NDA на первом звонке.
- Не быть слишком технически глубоким — это не нужно тут.
- Не жаловаться на прошлых работодателей.

### Этап 2: Take-home assignment

Что ожидать (для Analyst FP&A):

- Скорее всего, данные: trades, orders, broker statements, exchange fees, PnL, или похожее.
- Задание: identify errors / reconcile / aggregate / produce report / write Python script.
- Возможные форматы: CSV/Excel/JSON, иногда API.

Тактика выполнения:

- Прочитать задание полностью два раза. Отметить, что оценивается: accuracy, code quality, communication, или business reasoning.
- Сделать структурный README: assumptions, methodology, results, limitations.
- Использовать pandas, чистый Python, openpyxl. Не пытаться использовать redundant ML или сложный stack.
- Подготовить Excel-отчет с несколькими листами: raw, cleaned, exceptions, summary.
- Документировать каждое решение коротко: "I assumed X because Y."
- Если задача занимает больше времени, чем сказали — лучше сделать меньше, но качественно. Они ценят thoughtful approach.

Использовать готовый mini-case `eqvilent_reconciliation_mini_case.py` как шаблон скелета: normalize, merge, classify, summary, export.

### Этап 3: Technical interview по результатам assignment

Что они спросят:

- Почему ты выбрал такой подход.
- Что бы ты сделал иначе с большим временем.
- Edge cases и assumptions.
- Как масштабировать решение.
- Базовые pandas вопросы: merge, groupby, missing data, performance.
- Возможно SQL базово.
- Возможно basic Python вопросы: data structures, exceptions, типизация.

Тактика:

- Не защищаться, а объяснять trade-offs.
- Признавать gaps честно: "I went with simple approach because X, but in production I would add Y."
- Подсветить связь с финансовыми контролями: "I separated completeness and value breaks because the investigation path is different."

### Этап 4: Hiring manager interview (Finance Team)

Что они спросят:

- Конкретный finance experience: budgeting, cash flow, reconciliations, audit.
- Опыт работы с многочисленными источниками данных.
- Как ты улучшал finance процессы.
- Как ты работаешь со stakeholders.
- Опыт с Python/SQL/Excel в финансах.

Тактика:

- Использовать STAR-истории из `eqvilent_interview_prep_kit_RU.md`.
- Каждая история должна заканчиваться "this is relevant to Eqvilent because..."
- Подсветить, что ты не CFO, который ищет CFO позицию: "I want a hands-on role with data and process focus."

### Этап 5: Behavioral / culture interview

Что они спросят (по отзывам, повторяющиеся вопросы):

- "Tell me about the most challenging project you worked on."
- "Describe complex cases I had handled and how I approached them."
- "Tell me about a time you led a project."
- "Why are you looking for a new role?"
- "How do you handle disagreements?"

Тактика:

- 4 готовых истории из prep kit.
- Не критиковать текущего работодателя.
- Подчеркивать самостоятельность, ownership, structured thinking.
- Можно мягко добавить personal hook: интерес к китайскому языку (HSK 4), MBA, PhD по физике-математике. Это запоминается.

### Этап 6: Top management / CEO

Если дойдешь — это сильный сигнал.

Что они оценивают:

- Mindset и долгосрочный fit.
- Способность ясно говорить о finance, data и automation.
- Личность и intellectual maturity.
- Что ты привнесешь в команду.

Тактика:

- Говори стратегически, не тактически.
- Не льсти и не нервничай.
- Подготовь 2-3 умных вопроса про finance function в quant trading: how does Finance support trading? How are reconciliations evolving as the firm scales? What does data quality mean for the Finance Team?

## 4. Повторяющиеся вопросы из отзывов и сильные ответы

### "What is your expected compensation?"

Этот вопрос упоминается в отзывах HR Recruiter, ML Engineer, Quantitative Analyst, Infrastructure Security Engineer.

Сильный ответ:

> Given the hybrid nature of the role — finance operations, trading data analysis, Python-based reporting, reconciliations, and workflow automation — my expected range would be around USD 90,000-105,000 gross annually. The final number depends on the scope, seniority level, bonus structure, and overall benefits package.

### "Describe complex cases you handled"

Использовать STAR-историю про запуск finance function с нуля или про reconciliation/audit поддержку. Структура: ситуация, конкретные шаги, результат, что вынес для себя.

### "Tell me about the most challenging project you worked on"

Хорошо подходит история про building finance function from scratch in international environment. Подчеркнуть multi-stakeholder coordination, structured process design, и что ты делал hands-on, а не только руководил.

### "Tell me about a time you led a project"

История про CFO роль или CRAIC budgeting/reporting. Фокус: ownership, planning, communication, delivery.

### "Why are you looking for a new role?"

> I am looking for a more technical and data-driven finance environment. My recent roles were strong on finance operations and management, but I want to focus more on data, Python, automation, and modern finance workflows. Eqvilent is exactly the type of company where finance, data, and trading operations come together.

### "What do you know about the company?"

> Eqvilent is an international quantitative trading firm with strong technical infrastructure, remote-first culture, and global presence in Dubai, London, Lisbon, Mumbai, and Malta. The company emphasizes precision, intellectual work, and strong teams. The finance function in such a company is closer to data and operations than to classical accounting.

### "Why Eqvilent?"

Сильный ответ:

> Three reasons. First, the role itself combines finance, trading data, Python, reconciliations, and automation — exactly the intersection I want to develop in. Second, the company culture: technically strong, remote-first, fast feedback loops, and serious investment in infrastructure. Third, the long-term direction: a growing quant trading firm with global presence creates strong learning and growth potential.

### "How comfortable are you with NDA?"

> I am comfortable with NDA. I treat confidentiality as part of professional standards, especially in finance and trading. I would just like to review the document properly before signing, which I assume is the standard process.

## 5. Конкретные риски и как их закрывать

### Риск 1: Они увидят CFO/seniority и решат, что overqualified

Закрывать так:

> I am not looking for a finance leadership title right now. I am looking for a hands-on role with data, Python, trading operations, and process work. My senior finance background is useful as context, but I am very comfortable doing detailed work directly.

### Риск 2: Trading desk gap

Закрывать так:

> My direct experience is not from a trading desk, but the underlying discipline is identical: source data control, normalization, reconciliation, exception handling, reporting, and stakeholder communication. I am already mapping the trading data domain and can ramp up quickly.

### Риск 3: Python depth

Закрывать так:

> I do not position myself as a software engineer. I position myself as a finance professional who uses Python practically: pandas, file processing, automation, OCR/document processing, FastAPI services, PostgreSQL, Docker. I have GitHub projects that show real working systems, not just notebooks.

### Риск 4: Remote setup

Закрывать так:

> I have been working with international teams in China for many years, including Russian and Chinese stakeholders, banks, auditors, and management across time zones. I am very comfortable with structured written communication, async work, and self-managed deadlines.

### Риск 5: Длинный процесс и молчание между этапами

- Не отправляй гневные письма.
- Раз в 7-10 дней короткий status-check, не более.
- Параллельно держи другие процессы открытыми.
- Психологически принять, что это часть их culture.

### Риск 6: NDA / non-compete на первом звонке

Не возмущаться. Сказать:

> I understand the importance of NDA in this industry. I am open to signing a reasonable agreement. For non-compete, I am open to discussing terms that are proportional to the role and the probation period. Could you share the pro
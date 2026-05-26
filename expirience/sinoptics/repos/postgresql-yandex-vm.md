# postgresql-yandex-vm

**Path:** `D:/_sinoptics_git/postgresql-yandex-vm`  
**Category:** sinoptics-repo  
**Primary language:** SQL  
**Status:** present on disk

## 1. Purpose (2-3 lines)

# Автоматический деплой PostgreSQL на Ubuntu

Набор скриптов для автоматической установки, настройки и резервного копирования PostgreSQL на Ubuntu.

## 2. Tech stack (from manifests and file-type mix)

- **Detected primary language:** SQL
- **Top-level layout:** see listing below.

### `README.md`

```
# Автоматический деплой PostgreSQL на Ubuntu

Набор скриптов для автоматической установки, настройки и резервного копирования PostgreSQL на Ubuntu.

## 📋 Содержимое

- `deploy_postgresql.sh` - Основной скрипт деплоя PostgreSQL
- `backup_postgresql.sh` - Скрипт для автоматического резервного копирования

## 🚀 Быстрый старт

### 1. Клонирование и подготовка

```bash
# Сделать скрипты исполняемыми
chmod +x deploy_postgresql.sh backup_postgresql.sh
```

### 2. Настройка параметров (опционально)

Отредактируйте переменные в начале файла `deploy_postgresql.sh`:

```bash
POSTGRES_PASSWORD="SecurePassword123!"    # Пароль для пользователя postgres
DB_NAME="myappdb"                          # Имя базы данных
DB_USER="myappuser"                        # Имя пользователя
DB_USER_PASSWORD="UserPassword456!"        # Пароль пользователя
LISTEN_ADDRESSES="localhost"               # Адреса ('*' для внешних подключений)
MAX_CONNECTIONS="100"                      # Максимум подключений
```

### 3. Запуск деплоя

```bash
sudo ./deploy_postgresql.sh
```

## 📦 Что делает скрипт деплоя

| Шаг | Описание |
|-----|----------|
| 1 | Установка PostgreSQL через `apt` |
| 2.1 | Установка пароля для пользователя `postgres` |
| 2.2 | Открытие порта 5432 в фаерволе UFW |
| 2.3 | Настройка `listen_addresses` и `max_connections` |
| 3 | Создание базы данных и пользователя |
| 4 | Включение автозапуска службы |
| 5 | Перезапуск PostgreSQL |
| 6 | Проверка статуса службы |
| 7 | Создание бекапа базы данных |

## 💾 Резервное копирование

### Ручной бекап

```bash
sudo ./backup_postgresql.sh myappdb
```

### Автоматический бекап (cron)

Добавьте задание в crontab для ежедневного бекапа в 2:00:

```bash
sudo crontab -e
```

Добавьте строку:

```cron
0 2 * * * /path/to/backup_postgresql.sh myappdb
```

### Параметры бекапа

В файле `backup_postgresql.sh`:

```bash
BACKUP_DIR="/var/backups/postgresql"  # Директория бекапов
RETENTION_DAYS=7                       # Хранить бекапы N дней
LOG_FILE="/var/log/postgresql_backup.log"
```

## 🔌 Подключение к базе данных

### psql

```bash
psql -h localhost -U myappuser -d myappdb
```

### Строка подключения

```
postgresql://myappuser:UserPassword456!@localhost:5432/myappdb
```

### Python (psycopg2)

```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="myappdb",
    user="myappuser",
    password="UserPassword456!"
)
```

### Node.js (pg)

```javascript
const { Pool } = require('pg');

const pool = new Pool({
    host: 'localhost',
    port: 5432,
    database: 'myappdb',
    user: 'myappuser',
    password: 'UserPassword456!'
});
```

## 🔧 Полезные команды

```bash
# Проверка статуса PostgreSQL
sudo systemctl status postgresql

# Перезапуск PostgreSQL
sudo systemctl restart postgresql

# Просмотр логов
sudo tail -f /var/log/postgresql/postgresql-*-main.log

# Вход в psql как postgres
sudo -u postgres psql

# Список баз данных
sudo -u postgres psql -c "\l"

# Список пользователей
sudo -u postgres psql -c "\du"

# Восстановле

…(truncated)…
```

### `readme.md`

```
# Автоматический деплой PostgreSQL на Ubuntu

Набор скриптов для автоматической установки, настройки и резервного копирования PostgreSQL на Ubuntu.

## 📋 Содержимое

- `deploy_postgresql.sh` - Основной скрипт деплоя PostgreSQL
- `backup_postgresql.sh` - Скрипт для автоматического резервного копирования

## 🚀 Быстрый старт

### 1. Клонирование и подготовка

```bash
# Сделать скрипты исполняемыми
chmod +x deploy_postgresql.sh backup_postgresql.sh
```

### 2. Настройка параметров (опционально)

Отредактируйте переменные в начале файла `deploy_postgresql.sh`:

```bash
POSTGRES_PASSWORD="SecurePassword123!"    # Пароль для пользователя postgres
DB_NAME="myappdb"                          # Имя базы данных
DB_USER="myappuser"                        # Имя пользователя
DB_USER_PASSWORD="UserPassword456!"        # Пароль пользователя
LISTEN_ADDRESSES="localhost"               # Адреса ('*' для внешних подключений)
MAX_CONNECTIONS="100"                      # Максимум подключений
```

### 3. Запуск деплоя

```bash
sudo ./deploy_postgresql.sh
```

## 📦 Что делает скрипт деплоя

| Шаг | Описание |
|-----|----------|
| 1 | Установка PostgreSQL через `apt` |
| 2.1 | Установка пароля для пользователя `postgres` |
| 2.2 | Открытие порта 5432 в фаерволе UFW |
| 2.3 | Настройка `listen_addresses` и `max_connections` |
| 3 | Создание базы данных и пользователя |
| 4 | Включение автозапуска службы |
| 5 | Перезапуск PostgreSQL |
| 6 | Проверка статуса службы |
| 7 | Создание бекапа базы данных |

## 💾 Резервное копирование

### Ручной бекап

```bash
sudo ./backup_postgresql.sh myappdb
```

### Автоматический бекап (cron)

Добавьте задание в crontab для ежедневного бекапа в 2:00:

```bash
sudo crontab -e
```

Добавьте строку:

```cron
0 2 * * * /path/to/backup_postgresql.sh myappdb
```

### Параметры бекапа

В файле `backup_postgresql.sh`:

```bash
BACKUP_DIR="/var/backups/postgresql"  # Директория бекапов
RETENTION_DAYS=7                       # Хранить бекапы N дней
LOG_FILE="/var/log/postgresql_backup.log"
```

## 🔌 Подключение к базе данных

### psql

```bash
psql -h localhost -U myappuser -d myappdb
```

### Строка подключения

```
postgresql://myappuser:UserPassword456!@localhost:5432/myappdb
```

### Python (psycopg2)

```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="myappdb",
    user="myappuser",
    password="UserPassword456!"
)
```

### Node.js (pg)

```javascript
const { Pool } = require('pg');

const pool = new Pool({
    host: 'localhost',
    port: 5432,
    database: 'myappdb',
    user: 'myappuser',
    password: 'UserPassword456!'
});
```

## 🔧 Полезные команды

```bash
# Проверка статуса PostgreSQL
sudo systemctl status postgresql

# Перезапуск PostgreSQL
sudo systemctl restart postgresql

# Просмотр логов
sudo tail -f /var/log/postgresql/postgresql-*-main.log

# Вход в psql как postgres
sudo -u postgres psql

# Список баз данных
sudo -u postgres psql -c "\l"

# Список пользователей
sudo -u postgres psql -c "\du"

# Восстановле

…(truncated)…
```

### `Readme.md`

```
# Автоматический деплой PostgreSQL на Ubuntu

Набор скриптов для автоматической установки, настройки и резервного копирования PostgreSQL на Ubuntu.

## 📋 Содержимое

- `deploy_postgresql.sh` - Основной скрипт деплоя PostgreSQL
- `backup_postgresql.sh` - Скрипт для автоматического резервного копирования

## 🚀 Быстрый старт

### 1. Клонирование и подготовка

```bash
# Сделать скрипты исполняемыми
chmod +x deploy_postgresql.sh backup_postgresql.sh
```

### 2. Настройка параметров (опционально)

Отредактируйте переменные в начале файла `deploy_postgresql.sh`:

```bash
POSTGRES_PASSWORD="SecurePassword123!"    # Пароль для пользователя postgres
DB_NAME="myappdb"                          # Имя базы данных
DB_USER="myappuser"                        # Имя пользователя
DB_USER_PASSWORD="UserPassword456!"        # Пароль пользователя
LISTEN_ADDRESSES="localhost"               # Адреса ('*' для внешних подключений)
MAX_CONNECTIONS="100"                      # Максимум подключений
```

### 3. Запуск деплоя

```bash
sudo ./deploy_postgresql.sh
```

## 📦 Что делает скрипт деплоя

| Шаг | Описание |
|-----|----------|
| 1 | Установка PostgreSQL через `apt` |
| 2.1 | Установка пароля для пользователя `postgres` |
| 2.2 | Открытие порта 5432 в фаерволе UFW |
| 2.3 | Настройка `listen_addresses` и `max_connections` |
| 3 | Создание базы данных и пользователя |
| 4 | Включение автозапуска службы |
| 5 | Перезапуск PostgreSQL |
| 6 | Проверка статуса службы |
| 7 | Создание бекапа базы данных |

## 💾 Резервное копирование

### Ручной бекап

```bash
sudo ./backup_postgresql.sh myappdb
```

### Автоматический бекап (cron)

Добавьте задание в crontab для ежедневного бекапа в 2:00:

```bash
sudo crontab -e
```

Добавьте строку:

```cron
0 2 * * * /path/to/backup_postgresql.sh myappdb
```

### Параметры бекапа

В файле `backup_postgresql.sh`:

```bash
BACKUP_DIR="/var/backups/postgresql"  # Директория бекапов
RETENTION_DAYS=7                       # Хранить бекапы N дней
LOG_FILE="/var/log/postgresql_backup.log"
```

## 🔌 Подключение к базе данных

### psql

```bash
psql -h localhost -U myappuser -d myappdb
```

### Строка подключения

```
postgresql://myappuser:UserPassword456!@localhost:5432/myappdb
```

### Python (psycopg2)

```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="myappdb",
    user="myappuser",
    password="UserPassword456!"
)
```

### Node.js (pg)

```javascript
const { Pool } = require('pg');

const pool = new Pool({
    host: 'localhost',
    port: 5432,
    database: 'myappdb',
    user: 'myappuser',
    password: 'UserPassword456!'
});
```

## 🔧 Полезные команды

```bash
# Проверка статуса PostgreSQL
sudo systemctl status postgresql

# Перезапуск PostgreSQL
sudo systemctl restart postgresql

# Просмотр логов
sudo tail -f /var/log/postgresql/postgresql-*-main.log

# Вход в psql как postgres
sudo -u postgres psql

# Список баз данных
sudo -u postgres psql -c "\l"

# Список пользователей
sudo -u postgres psql -c "\du"

# Восстановле

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
.vscode
README.md
backup_postgresql.sh
deploy_postgresql.sh
examples
```

## 5. My contribution / role (evidence from git history — if available)

```text
c2df466 2026-01-12 chore: deploy
486a97f 2025-12-03 chore: deploy
8473c9c 2025-12-02 chore: deploy
```

_Use commit messages only as hints; corroborate in interviews._

## 6. Notable patterns / snippets

_No snippet candidates matched (handler.py / stack.ts / template.yaml etc.). Expand manually after opening the repo._

## 7. Metrics / SLO / scale (if available)

_Extract from Airflow DAG params, load tests, README, or CloudFormation `ReservedConcurrentExecutions` when present — not auto-inferred to avoid fabrication._

## 8. Resume bullets (ready-to-paste, English)

- Owned or extended **`postgresql-yandex-vm`** capabilities aligned with **sinoptics repo** delivery.
- Applied **SQL** stack patterns and repository-local IaC/config where present.
- Collaborated on production-grade defaults: structured logging, retries, and least-privilege IAM patterns where applicable.
- Integrated with **Sinoptics** platform services (data stores, queues, gateways) per dependency manifests in-repo.
- Documented operational expectations (deploy, test, local dev) via README and automation files when available.

## 9. Interview talking points

- What is the main entrypoint and trigger for `postgresql-yandex-vm`?
- How are secrets and non-prod environments separated?
- What failure modes are handled (retries, DLQ, idempotency)?
- How would you observe this service in production (metrics, logs, traces)?

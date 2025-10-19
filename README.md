# ETL--API-SQL--
Python-скрипт, который обращается к API, собирает данные в pandas DataFrame, очищает и сохраняет их в базу данных PostgreSQL / ClickHouse. Используемые инструменты: Python, requests, pandas, SQLAlchemy.

ETL: API → pandas → SQL (PostgreSQL / ClickHouse)

Готовый мини‑проект, демонстрирующий путь данных **из внешнего API** в **SQL‑базу** через Python:
1) **Extract** — запрос к API (`requests`)
2) **Transform** — преобразование JSON → DataFrame (`pandas`)
3) **Load** — загрузка в **PostgreSQL** (`sqlalchemy+psycopg2`) или **ClickHouse** (`clickhouse-connect`)

## Быстрый старт
```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python main.py --target postgres
# или
python main.py --target clickhouse

# PostgreSQL metadata (DDL) grabber and comparer

## Dependencies

* [Python 3](https://www.python.org/downloads/)
* [psycopg2](https://pypi.org/project/psycopg2/)

## Installation

```bash
pip install psycopg2 pg-metadata
```

## Usage

1 ) Create file `_Connect.py` with connection params:

```python
# Source database for comparing
# Database for grabbing
PG_SOURCE = {
    "host"      : "",
    "port"      : 5432,
    "database"  : "",
    "username"  : "",
    "password"  : "",
}

# Target database for comparing
PG_TARGET = {
    "host"      : "",
    "port"      : 5432,
    "database"  : "",
    "username"  : "",
    "password"  : "",
}

# Excluded namespaces
EXCLUDE_SCHEMAS = [
    "information_schema",
    "pg_catalog",
    "pg_temp",
    "pg_temp_1",
    "pg_toast",
    "pg_toast_temp_1"
]

# Path with compare folder
PATH_COMPARE = "./compare"
```

2 ) To grab database metadata run `zzz_Grabber.py`.

3 ) To compare databases run `zzz_Compare.py`.

## Links

* [GitHub](https://github.com/ish1mura/pg_metadata)
* [PyPI](https://pypi.org/project/pg-metadata/)

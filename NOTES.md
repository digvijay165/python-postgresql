# Database Operations using Python (psycopg2) — Deen Bandhu Singh

This folder contains the assignment "Implementing Database Operations using
Python", which connects to PostgreSQL from Python using the `psycopg2`
library and performs a series of basic database operations.

## Requirements

- Python 3
- PostgreSQL server installed and running
- `psycopg2-binary` package:

  ```
  pip install psycopg2-binary
  ```

## Setup

1. Open `db_config.py` and update the connection settings (`host`, `port`,
   `user`, `password`) to match your own PostgreSQL installation.
2. Run the scripts in order from a terminal (inside this folder):

   ```
   python3 task1_connect_and_create_database.py
   python3 task2_create_table.py
   python3 task3_insert_records.py
   python3 task4_fetch_records.py
   python3 task5_dynamic_insert.py
   python3 task6_select_where.py
   python3 task7_truncate_table.py
   ```

3. `psql_commands.sql` covers the same ideas (create/drop database, create
   table, insert records) run directly through the `psql` command-line tool
   instead of Python:

   ```
   psql -U postgres -f psql_commands.sql
   ```

## Files

| File | Topic |
|---|---|
| `db_config.py` | Shared connection settings used by every script |
| `task1_connect_and_create_database.py` | Connecting Python with PostgreSQL, creating a database |
| `task2_create_table.py` | Creating a table |
| `task3_insert_records.py` | Inserting records (parameterized queries) |
| `task4_fetch_records.py` | Fetching records with `fetchone()` and `fetchall()` |
| `task5_dynamic_insert.py` | Taking user input and inserting it dynamically |
| `task6_select_where.py` | `SELECT` with `WHERE` conditions |
| `task7_truncate_table.py` | `TRUNCATE TABLE` |
| `psql_commands.sql` | Creating/dropping databases and tables directly with `psql` |
| `run_logs/` | Raw terminal output captured from an actual run of every script, for reference |
| `screenshots/` | Combined "code + terminal output" images for each task |

## Notes on the screenshots

Every script in this folder was actually executed against a real
PostgreSQL database while preparing this assignment, and the exact
terminal output was captured (see `run_logs/`). The images in
`screenshots/` are generated directly from that real code and that real
output so each one accurately shows what running the script produces.

The assignment brief specifically asks for screenshots of the code open in
VS Code together with the terminal output. Because these scripts were
authored and tested outside of a VS Code window, **before submitting you
should**:

1. Open each `.py` file in your own VS Code.
2. Run it from the VS Code integrated terminal (`python3 <filename>.py`).
3. Take a screenshot showing both the code and the terminal output, and
   save it into `screenshots/` (replacing or supplementing the provided
   images).

This guarantees your submission reflects your own VS Code environment,
which is what most instructors check for. The provided images are a
faithful, tested reference for what each screenshot should look like and
what output to expect.

## Summary of what each script demonstrates

- Connecting to PostgreSQL from Python (`psycopg2.connect`)
- Creating a database and a table
- Inserting static and dynamic (user-input) records using parameterized
  queries (`%s` placeholders — never string-formatted SQL, to avoid SQL
  injection)
- Fetching data with `fetchone()` and `fetchall()` and displaying it in a
  formatted table
- Filtering rows with `SELECT ... WHERE ...`
- Clearing a table with `TRUNCATE TABLE`
- Finalizing every operation with `conn.commit()` and always closing the
  connection with `conn.close()`
- Performing the equivalent create/insert operations directly through
  `psql`

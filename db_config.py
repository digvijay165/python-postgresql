"""
db_config.py
-------------
Central place to store the PostgreSQL connection settings so every
script in this assignment connects the same way.

Edit the values below to match your own PostgreSQL installation
before running any of the task scripts.
"""

DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "user": "postgres",
    "password": "postgres",   # change to your own postgres password
}

# Name of the database we create and use for this assignment
DATABASE_NAME = "student_db"

# Name of the table we create and use for this assignment
TABLE_NAME = "students"

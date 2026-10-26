"""
Task 1: Connect to PostgreSQL from Python and create a database.

Topics covered:
    - Connecting Python with PostgreSQL
    - Creating a database

Notes:
    CREATE DATABASE cannot run inside a transaction block, so we
    connect to the default 'postgres' database first and switch the
    connection to autocommit mode before issuing the CREATE DATABASE
    statement.
"""

import psycopg2
from psycopg2 import sql
from db_config import DB_CONFIG, DATABASE_NAME


def connect_to_postgres():
    """Connect to the default 'postgres' database."""
    conn = psycopg2.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        dbname="postgres",
    )
    print("Connected to PostgreSQL server successfully!")
    return conn


def create_database(conn, db_name):
    """Create a new database if it does not already exist."""
    conn.autocommit = True  # required for CREATE DATABASE
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s;", (db_name,))
    exists = cursor.fetchone()

    if exists:
        print(f"Database '{db_name}' already exists. Skipping creation.")
    else:
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
        print(f"Database '{db_name}' created successfully!")

    cursor.close()


if __name__ == "__main__":
    connection = connect_to_postgres()
    create_database(connection, DATABASE_NAME)
    connection.close()
    print("Connection closed.")

"""
Task 2: Create a table inside the database.

Topics covered:
    - Creating tables
    - cursor.execute() for running SQL queries
    - conn.commit() and conn.close() for finalizing operations
"""

import psycopg2
from db_config import DB_CONFIG, DATABASE_NAME, TABLE_NAME


def create_table():
    conn = psycopg2.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        dbname=DATABASE_NAME,
    )
    cursor = conn.cursor()

    create_query = f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL,
            course VARCHAR(100) NOT NULL
        );
    """

    cursor.execute(create_query)
    conn.commit()
    print(f"Table '{TABLE_NAME}' created successfully in database '{DATABASE_NAME}'!")

    cursor.close()
    conn.close()
    print("Connection closed.")


if __name__ == "__main__":
    create_table()

"""
Task 6: SELECT with WHERE conditions.

Topics covered:
    - SELECT queries with WHERE conditions
    - Parameterized queries in WHERE clauses
"""

import psycopg2
from db_config import DB_CONFIG, DATABASE_NAME, TABLE_NAME


def select_with_where():
    conn = psycopg2.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        dbname=DATABASE_NAME,
    )
    cursor = conn.cursor()

    # Example 1: students older than 20
    print("--- Students with age > 20 ---")
    cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE age > %s ORDER BY id;", (20,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Example 2: students in a specific course
    print("\n--- Students enrolled in 'Data Science' ---")
    cursor.execute(
        f"SELECT * FROM {TABLE_NAME} WHERE course = %s ORDER BY id;",
        ("Data Science",),
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
    print("\nConnection closed.")


if __name__ == "__main__":
    select_with_where()

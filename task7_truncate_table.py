"""
Task 7: TRUNCATE TABLE.

Topics covered:
    - TRUNCATE TABLE (quickly removes all rows from a table while
      keeping its structure, faster than DELETE for clearing a table)
"""

import psycopg2
from db_config import DB_CONFIG, DATABASE_NAME, TABLE_NAME


def truncate_table():
    conn = psycopg2.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        dbname=DATABASE_NAME,
    )
    cursor = conn.cursor()

    # Show row count before truncating
    cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME};")
    before_count = cursor.fetchone()[0]
    print(f"Row count before TRUNCATE: {before_count}")

    cursor.execute(f"TRUNCATE TABLE {TABLE_NAME} RESTART IDENTITY;")
    conn.commit()
    print(f"Table '{TABLE_NAME}' truncated successfully!")

    # Show row count after truncating
    cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME};")
    after_count = cursor.fetchone()[0]
    print(f"Row count after TRUNCATE: {after_count}")

    cursor.close()
    conn.close()
    print("Connection closed.")


if __name__ == "__main__":
    truncate_table()

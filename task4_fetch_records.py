"""
Task 4: Fetch and display data from the table.

Topics covered:
    - Fetching records (fetchone, fetchall)
"""

import psycopg2
from db_config import DB_CONFIG, DATABASE_NAME, TABLE_NAME


def fetch_records():
    conn = psycopg2.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        dbname=DATABASE_NAME,
    )
    cursor = conn.cursor()

    print("\n--- Using fetchone() : first record ---")
    cursor.execute(f"SELECT * FROM {TABLE_NAME} ORDER BY id;")
    first_row = cursor.fetchone()
    print(first_row)

    print("\n--- Using fetchall() : all records ---")
    cursor.execute(f"SELECT * FROM {TABLE_NAME} ORDER BY id;")
    all_rows = cursor.fetchall()

    print(f"{'ID':<5}{'Name':<20}{'Age':<5}{'Course':<25}")
    print("-" * 55)
    for row in all_rows:
        row_id, name, age, course = row
        print(f"{row_id:<5}{name:<20}{age:<5}{course:<25}")

    print(f"\nTotal records fetched: {len(all_rows)}")

    cursor.close()
    conn.close()
    print("Connection closed.")


if __name__ == "__main__":
    fetch_records()

"""
Task 3: Insert records into the table.

Topics covered:
    - Inserting records
    - Parameterized queries (safe way to insert data, avoids SQL injection)
"""

import psycopg2
from db_config import DB_CONFIG, DATABASE_NAME, TABLE_NAME


def insert_records():
    conn = psycopg2.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        dbname=DATABASE_NAME,
    )
    cursor = conn.cursor()

    students = [
        ("Aarav Sharma", 21, "Computer Science"),
        ("Priya Verma", 22, "Information Technology"),
        ("Rohan Gupta", 20, "Electronics"),
        ("Sneha Kulkarni", 23, "Data Science"),
    ]

    insert_query = f"INSERT INTO {TABLE_NAME} (name, age, course) VALUES (%s, %s, %s);"

    for student in students:
        cursor.execute(insert_query, student)

    conn.commit()
    print(f"{len(students)} records inserted successfully into '{TABLE_NAME}'!")

    cursor.close()
    conn.close()
    print("Connection closed.")


if __name__ == "__main__":
    insert_records()

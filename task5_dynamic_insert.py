"""
Task 5: Take user input and insert it dynamically using parameterized
queries.

Topics covered:
    - Taking user input and using parameterized queries
    - cursor.execute() with placeholders (%s) to avoid SQL injection
"""

import psycopg2
from db_config import DB_CONFIG, DATABASE_NAME, TABLE_NAME


def insert_dynamic_record():
    conn = psycopg2.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        dbname=DATABASE_NAME,
    )
    cursor = conn.cursor()

    # Take input from the user
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter student course: ")

    insert_query = f"INSERT INTO {TABLE_NAME} (name, age, course) VALUES (%s, %s, %s);"
    cursor.execute(insert_query, (name, age, course))
    conn.commit()

    print(f"\nRecord for '{name}' inserted successfully using a parameterized query!")

    cursor.close()
    conn.close()
    print("Connection closed.")


if __name__ == "__main__":
    insert_dynamic_record()

##phonebook.py
import os
import psycopg2
from connect import get_connection


def _load_sql(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def setup_database():
    create_table = """
        CREATE TABLE IF NOT EXISTS phonebook (
            id         SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name  VARCHAR(50) NOT NULL,
            phone      VARCHAR(20) NOT NULL,
            UNIQUE (first_name, last_name)
        );
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(create_table)
            cur.execute(_load_sql("functions.sql"))
            cur.execute(_load_sql("procedures.sql"))
        conn.commit()


def search_contacts(pattern):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_contacts(%s);", (pattern,))
            rows = cur.fetchall()
            cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in rows]


def upsert_contact(first_name, last_name, phone):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL upsert_contact(%s, %s, %s);", (first_name, last_name, phone))
        conn.commit()


def bulk_insert_contacts(names, phones):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL bulk_insert_contacts(%s::text[], %s::text[]);", (names, phones))
            conn.commit()
            cur.execute("SELECT * FROM invalid_contacts;")
            rows = cur.fetchall()
            cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in rows]


def get_contacts_page(page=1, page_size=10):
    offset = (page - 1) * page_size
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (page_size, offset))
            rows = cur.fetchall()
            cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in rows]


def delete_by_phone(phone):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_contact(p_phone => %s);", (phone,))
        conn.commit()


def delete_by_name(first_name, last_name):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_contact(p_first_name => %s, p_last_name => %s);", (first_name, last_name))
        conn.commit()


if __name__ == "__main__":
    setup_database()

    while True:
        print("""
1. Add or Update Contact
2. Search Contact
3. Show Contacts
4. Bulk Insert
5. Delete by Name
6. Delete by Phone
7. Exit
""")

        choice = input("Choose: ")

        if choice == "1":
            first = input("First name: ")
            last = input("Last name: ")
            phone = input("Phone: ")
            upsert_contact(first, last, phone)
            print("Done!")

        elif choice == "2":
            pattern = input("Search: ")
            result = search_contacts(pattern)
            for row in result:
                print(row)

        elif choice == "3":
            page = int(input("Page: "))
            size = int(input("Page size: "))
            result = get_contacts_page(page, size)
            for row in result:
                print(row)

        elif choice == "4":
            count = int(input("How many contacts: "))
            names = []
            phones = []

            for i in range(count):
                names.append(input("Full name: "))
                phones.append(input("Phone: "))

            invalid = bulk_insert_contacts(names, phones)
            print("Invalid:", invalid)

        elif choice == "5":
            first = input("First name: ")
            last = input("Last name: ")
            delete_by_name(first, last)
            print("Deleted!")

        elif choice == "6":
            phone = input("Phone: ")
            delete_by_phone(phone)
            print("Deleted!")

        elif choice == "7":
            break

        else:
            print("Wrong choice!")
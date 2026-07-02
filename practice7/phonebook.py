from connect import get_connection

def add_contact():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)",
        (first_name, last_name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()

def show_all():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def search_contact():
    value = input("Enter name or phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
    """
    SELECT * FROM phonebook
    WHERE first_name ILIKE %s
       OR last_name ILIKE %s
       OR phone LIKE %s
    """,
    (f"%{value}%", f"%{value}%", f"%{value}%")
)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def update_contact():
    old_first_name = input("Enter first name to update: ")
    new_first_name = input("New first name: ")
    new_last_name = input("New last name: ")
    new_phone = input("New phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE phonebook
        SET first_name=%s, last_name=%s, phone=%s
        WHERE first_name=%s
        """,
        (new_first_name, new_last_name, new_phone, old_first_name)
    )

    conn.commit()
    cur.close()
    conn.close()

def delete_contact():
    value = input("Enter name or phone to delete: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
    """
    DELETE FROM phonebook
    WHERE first_name=%s
       OR last_name=%s
       OR phone=%s
    """,
    (value, value, value)
)
    conn.commit()
    cur.close()
    conn.close()

def menu():
    while True:
        print("\nPHONEBOOK MENU")
        print("1. Add contact")
        print("2. Show all contacts")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_all()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice!")

menu()
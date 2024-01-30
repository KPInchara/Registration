import sqlite3
from sqlite3 import Error

# Function to create a database connection
def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print(f"Connected to {db_file}")
        return connection
    except Error as e:
        print(e)

    return connection

# Function to execute SQL queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(e)

# Function to create the 'Registration' table
def create_registration_table(connection):
    try:
        with open('create_registration_table.sql', 'r') as file:
            query = file.read()
            execute_query(connection, query)
            print("Table created successfully")
    except Error as e:
        print(e)

# Function to insert a new record into the 'Registration' table
def create_record(connection, name, email, date_of_birth):
    query = f"INSERT INTO Registration (Name, Email, DateOfBirth) VALUES ('{name}', '{email}', '{date_of_birth}')"
    execute_query(connection, query)

# Function to retrieve records from the 'Registration' table
def read_records(connection):
    query = "SELECT * FROM Registration"
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

# Function to update an existing record in the 'Registration' table
def update_record(connection, record_id, new_name, new_email, new_date_of_birth):
    query = f"UPDATE Registration SET Name = '{new_name}', Email = '{new_email}', DateOfBirth = '{new_date_of_birth}' WHERE ID = {record_id}"
    execute_query(connection, query)

# Function to delete a record from the 'Registration' table
def delete_record(connection, record_id):
    query = f"DELETE FROM Registration WHERE ID = {record_id}"
    execute_query(connection, query)

# Function to interactively perform CRUD operations
def perform_crud_operations(connection):
    while True:
        print("\nOptions:")
        print("1. Create Record")
        print("2. Read Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            dob = input("Enter Date of Birth (YYYY-MM-DD): ")
            create_record(connection, name, email, dob)
        elif choice == "2":
            records = read_records(connection)
            print("\nAll Records:")
            for record in records:
                print(record)
        elif choice == "3":
            record_id = input("Enter Record ID to Update: ")
            new_name = input("Enter New Name: ")
            new_email = input("Enter New Email: ")
            new_dob = input("Enter New Date of Birth (YYYY-MM-DD): ")
            update_record(connection, record_id, new_name, new_email, new_dob)
        elif choice == "4":
            record_id = input("Enter Record ID to Delete: ")
            delete_record(connection, record_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    db_file = "registration_database.db"
    connection = create_connection(db_file)

    if connection:
        create_registration_table(connection)

        # Allow the user to perform CRUD operations from the terminal
        perform_crud_operations(connection)

        connection.close()

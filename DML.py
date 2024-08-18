import mysql.connector
from mysql.connector import Error

def insert_data():
    try:
        # Insert data into the Customers table
        cursor.execute("""
        INSERT INTO Customers (customer_id, customer_name, country, city)
        VALUES (%s, %s, %s, %s)
        """, (1, 'John Doe', 'USA', 'New York'))

        cursor.execute("""
        INSERT INTO Customers (customer_id, customer_name, country, city)
        VALUES (%s, %s, %s, %s)
        """, (2, 'Jane Smith', 'Canada', 'Toronto'))
    except Error as e:
        print(f"Error inserting data: {e}")
    
def update_data():
    try:
        # Update data in the Customers table
        cursor.execute("""
        UPDATE Customers
        SET city = %s
        WHERE customer_id = %s
        """, ('Los Angeles', 1))

    except Error as e:
        print(f"Error updating data: {e}")
    
def delete_data():
    try:
        # Delete data from the Customers table
        cursor.execute("""
        DELETE FROM Customers
        WHERE customer_id = %s
        """, (2,))
    except Error as e:
        print(f"Error deleting data: {e}")
   
def query_data():
    try:
        # Query data from the Customers table
        cursor.execute("SELECT * FROM Customers")
        rows = cursor.fetchall()

        print("Query result:")
        for row in rows:
            print(row)

    except Error as e:
        print(f"Error querying data: {e}")
    
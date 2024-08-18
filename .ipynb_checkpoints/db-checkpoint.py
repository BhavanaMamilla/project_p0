import mysql.connector
from mysql.connector import Error
import os

def create_database(cursor, database_name):
    """
    Creates a database with the given name if it doesn't exist.
    """
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"Database '{database_name}' created .")
    except Error as err:
        print(f"Error: {err}")

def view_databases(cursor):
    """
    Retrieves and prints all databases.
    """
    try:
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        print("Databases:")
        for db in databases:
            print(db[0])
    except Error as err:
        print(f"Error: {err}")
def use_database(cursor, database_name):
    """
    Selects the specified database to be used.
    """
    try:
        cursor.execute(f"USE {database_name}")
        print(f"Using database '{database_name}'.")
    except Error as err:
        print(f"Error: {err}")

def delete_database(cursor, database_name):
    """
    Drops the specified database.
    """
    try:
        cursor.execute(f"DROP DATABASE IF EXISTS {database_name}")
        print(f"Database '{database_name}' deleted.")
    except Error as err:
        print(f"Error: {err}")
        
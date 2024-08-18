def create_table(cursor, table_name, queries):
    """
    Creates a table with the specified name and SQL queries.
    """
    try:
        cursor.execute(queries)
        print(f"Table '{table_name}' created successfully.")
    except Error as err:
        print(f"Error in creating table: {err}")


def alter_table(cursor, table_name, alter_query):
    """
    Alters the specified table based on the provided SQL query.
    """
    try:
        cursor.execute(alter_query)
        print(f"Table '{table_name}' altered successfully.")
    except Error as err:
        print(f"Error in modifying table: {err}")


def view_tables(cursor):
    """
    Retrieves and prints all tables in the current database.
    """
    try:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print("Tables:")
        for table in tables:
            print(table[0])
    except Error as err:
        print(f"Error: {err}")
        
def drop_table(cursor, table_name):
    """
    Drops the specified table if it exists.
    """
    try:
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        print(f"Table '{table_name}' dropped successfully.")
    except Error as err:
        print(f"Error in deleting table: {err}")



def truncate_table(cursor,table_name):
    try:
        # Truncate the Orders table (removes all rows but keeps the table structure)
        cursor.execute("TRUNCATE TABLE Orders")
        print("Table Orders truncated successfully")
    except Error as e:
        print(f"Error truncating table: {e}")


def rename_table(cursor,table_name):
    try:
        # Rename the Orders table to Orders_Backup
        cursor.execute("RENAME TABLE Orders TO Orders_Backup")
        print("Table Orders renamed to Orders_Backup successfully")

    except Error as e:
        print(f"Error renaming table: {e}")
    
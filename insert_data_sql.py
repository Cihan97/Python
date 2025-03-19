# insert_data_sql.py
# This file is used to insert data into SQL Server.
# It adds a new customer to the 'Customers' table.

import pyodbc
from sql_server_Connection import connect_to_db

def insert_data():
    conn = connect_to_db()  # Start to  database connection  
    cursor = conn.cursor()

    # Insert SQL QUERY
    insert_query = """
    INSERT INTO Customers (FirstName, LastName, Email, Phone) 
    VALUES (?, ?, ?, ?)
    """

    # Insert Data
    customer_data = ("John", "Doe", "john.doe@example.com", "555-555-5555")

    try: 
        # Run the query
        cursor.execute(insert_query, customer_data)

        # Commit the transaction
        conn.commit()
        print("Data inserted successfully!")
    except Exception as e:
        print("Data insertion error:", e)
    finally: 
        # Close the connection
        conn.close()

if __name__ == '__main__':
    insert_data()  # call the function


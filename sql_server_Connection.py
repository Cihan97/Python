# sql_server_connection.py
# This file provides the necessary function to connect to SQL Server.
# The connection is made using Windows Authentication.

import pyodbc

def connect_to_db():
    print("Connection is starting...")  # Write the message to the console
    server = 'DESKTOP-EMQQEDE'  # Hostname of the SQL Server
    database = 'CustomerDB'      # The name of the database you want to connect to

    try:
        # Connect to SQL Server using Windows Authentication
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes;')
        print("Successfully connected to SQL Server!")  # Print the success message
        return conn
    except Exception as e:
        print("Connection error occurred:", e)

# Main part of the program
if __name__ == '__main__':
    connect_to_db()  # Call the function


#!/usr/bin/python3
"""Script to create the alxbookstore database in MySQL"""

import mysql.connector
from sys import argv

def create_database():
    """Create the alxbookstore database if it doesn't exist"""
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host="localhost",
            user=argv[1],
            password=argv[2],
            port=3306
        )
        
        # Create a cursor object
        cursor = connection.cursor()
        
        # Create database (IF NOT EXISTS prevents errors if DB already exists)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
        
        print("Database 'alxbookstore' created successfully!")
        
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        
    finally:
        # Close the connection if it was established
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: python MySQLServer.py <mysql_username> <mysql_password>")
    else:
        create_database()
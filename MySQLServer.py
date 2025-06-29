#!/usr/bin/python3
"""Script to create the alx_book_store database in MySQL"""

import MySQLdb
from sys import argv

def create_database():
    """Create the alx_book_store database if it doesn't exist"""
    try:
        # Connect to MySQL server (without specifying a database)
        connection = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            port=3306
        )
        
        # Create a cursor object
        cursor = connection.cursor()
        
        # Create database (IF NOT EXISTS prevents errors if DB already exists)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        print("Database 'alx_book_store' created successfully!")
        
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        
    finally:
        # Close the connection if it was established
        if 'connection' in locals() and connection.open:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: python MySQLServer.py <mysql_username> <mysql_password>")
    else:
        create_database()
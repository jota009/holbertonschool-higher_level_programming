#!/usr/bin/python3
"""
Lists all states with names starting with 'N' from the database hbtn_0e_0_usa
Usage: ./filter_states.py <username> <password> <database>
"""


import MySQLdb
import sys


if __name__ == "__main__":
    # Get credentials from command line arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )

    # Create cursos and execute query
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Print results
    for row in cursor.fetchall():
        print(row)

    # Close connection
    cursor.close()
    db.close()

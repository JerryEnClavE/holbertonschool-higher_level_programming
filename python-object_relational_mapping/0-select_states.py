#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL username, password, and database name from arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to retrieve all states ordered by states.id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print all results from the executed query
    for state in cursor.fetchall():
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

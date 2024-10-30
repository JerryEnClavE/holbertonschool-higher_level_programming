#!/usr/bin/python3
"""Lists states matching the argument"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()

    # Use format to create the SQL query with user input
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC".format(argv[4])

    cur.execute(query)
    query_rows = cur.fetchall()

    # Display results
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()

#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    try:
        # Establish the database connection
        conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                               passwd=argv[2], db=argv[3], charset="utf8")

        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM states ORDER BY id ASC")
            query_rows = cur.fetchall()

            for row in query_rows:
                print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

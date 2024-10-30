#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FORM satates\
                WHERE Binary name LIKE '{}' ORDER BY name ASC".format(argv[4]))

    rows = cursor.fetchall()

    for row in rows:
        print("{}".format(row))

    cursor.close()
    conn.close()

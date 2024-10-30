#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: ./script.py <mysql_username> <mysql_password> <database_name> <state_name>")
        exit(1)

    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                               passwd=argv[2], db=argv[3], charset="utf8")
        cur = conn.cursor()
        
        query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY states.id ASC"
        cur.execute(query, (argv[4],))
        
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
    
    except MySQLdb.Error as e:
        print(f"Error {e.args[0]}: {e.args[1]}")
    
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

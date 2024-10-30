#!/usr/bin/python3
"""task 5 orm"""
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Wrong Usage")

    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=sys.argv[1],
                           password=sys.argv[2],
                           db=sys.argv[3])
    cursor = conn.cursor()
    query = "SELECT cities.name FROM cities JOIN states ON\
        states.id = cities.state_id WHERE states.name = %s\
            ORDER BY cities.id ASC"
    cursor.execute(query, (sys.argv[4],))
    cities = cursor.fetchall()
    print(", ".join(city[0] for city in cities))
    cursor.close()
    conn.close()

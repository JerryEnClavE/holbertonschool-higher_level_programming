#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                               passwd=argv[2], db=argv[3], charset="utf8")
        cur = conn.cursor()
        
        # Usar parámetros en lugar de formatear la consulta directamente
        query = """
        SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY states.id ASC"""
        cur.execute(query, (argv[4],))
        
        query_rows = cur.fetchall()
        for row in query_rows:
            # Imprimir el id y el nombre del estado de forma clara
            print(f"{row[0]}: {row[1]}")  # Suponiendo que el id es el primer campo y el nombre el segundo
        
        cur.close()
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

#!/usr/bin/python3
"""Lists states from a MySQL database where the state name starts with 'N'."""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    try:
        # Conectarse a la base de datos
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8"
        )
        cursor = connection.cursor()

        # Ejecutar consulta SQL
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
        rows = cursor.fetchall()

        # Filtrar e imprimir filas
        for row in rows:
            if row[1].startswith("N"):
                print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        # Cerrar el cursor y la conexión solo si fueron abiertos exitosamente
        if cursor:
            cursor.close()
        if connection:
            connection.close()

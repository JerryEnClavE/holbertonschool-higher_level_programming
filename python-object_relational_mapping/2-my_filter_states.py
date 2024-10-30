#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Recopilar argumentos de línea de comandos
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Conectar a la base de datos MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Crear un objeto cursor
    cursor = db.cursor()

    # Crear la consulta SQL
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Obtener todos los resultados
    results = cursor.fetchall()

    # Imprimir los resultados en el formato requerido
    for row in results:
        print(row)

    # Cerrar el cursor y la conexión
    cursor.close()
    db.close()

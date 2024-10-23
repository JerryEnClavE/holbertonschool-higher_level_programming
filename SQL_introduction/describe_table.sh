#!/bin/bash

# Verifica si el nombre de la base de datos fue proporcionado como argumento
if [ $# -eq 0 ]; then
    echo "Uso: $0 <nombre_base_de_datos>"
    exit 1
fi

# Asigna el primer argumento a la variable DB_NAME
DB_NAME=$1

# Ejecuta el comando SHOW CREATE TABLE para la tabla 'first_table'
mysql -u root -p -e "SHOW CREATE TABLE ${DB_NAME}.first_table\G" | grep -v "Using a password"

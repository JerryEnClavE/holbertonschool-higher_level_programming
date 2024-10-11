import requests
import csv

# Función para obtener y guardar los posts en un archivo CSV
def fetch_and_save_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    
    # Si la solicitud es exitosa, guardar los datos en un archivo CSV
    if response.status_code == 200:
        posts = response.json()  # Analizar el JSON en una lista de diccionarios

        # Eliminar el campo 'userId' si no lo necesitas
        for post in posts:
            if 'userId' in post:
                del post['userId']
        
        # Preparar los datos para el CSV con claves seleccionadas: 'id', 'title', 'body'
        fieldnames = ['id', 'title', 'body']
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # Escribir la cabecera basada en las claves
            writer.writerows(posts)  # Escribir las filas de los posts

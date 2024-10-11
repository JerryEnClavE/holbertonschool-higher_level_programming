import requests
import csv

# Función para obtener y mostrar los posts
def fetch_and_print_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    
    # Imprimir el código de estado
    print(f"Código de estado: {response.status_code}")
    
    # Si la solicitud es exitosa, analizar y mostrar los títulos de los posts
    if response.status_code == 200:
        posts = response.json()  # Analizar el JSON en una lista de diccionarios
        for post in posts:
            print(post['title'])

# Función para obtener y guardar los posts en un archivo CSV
def fetch_and_save_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    
    # Si la solicitud es exitosa, guardar los datos en un archivo CSV
    if response.status_code == 200:
        posts = response.json()  # Analizar el JSON en una lista de diccionarios
        
        # Preparar los datos para el CSV con claves seleccionadas: 'id', 'title', 'body'
        fieldnames = ['id', 'title', 'body']
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # Escribir la cabecera basada en las claves
            writer.writerows(posts)  # Escribir la lista de diccionarios en el archivo CSV

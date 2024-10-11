import requests
import csv

# Function to fetch and print posts
def fetch_and_print_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    
    # Print the status code
    print(f"Status Code: {response.status_code}")
    
    # If the request is successful, parse and print post titles
    if response.status_code == 200:
        posts = response.json()  # Parse JSON into Python list of dictionaries
        for post in posts:
            print(post['title'])

# Function to fetch and save posts to a CSV file
def fetch_and_save_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    
    # If the request is successful, save the data to a CSV
    if response.status_code == 200:
        posts = response.json()  # Parse JSON into Python list of dictionaries
        
        # Prepare data for CSV with selected keys: 'id', 'title', 'body'
        fieldnames = ['id', 'title', 'body']
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # Write header based on the fieldnames
            writer.writerows(posts)  # Write the list of dictionaries to the CSV file

#!/usr/bin/python3

import requests
import csv


# Function to fetch and print posts
def fetch_and_print_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.ok:
        posts = response.json()  # Parse JSON into Python list of dictionaries
        for post in posts:
            print(f"{post['title']}")
    else:
        print(f"Failed to fesh posts. Status Code: {response.status_code}")


# Function to fetch and save posts to a CSV file
def fetch_and_save_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    # If the request is successful, save the data to a CSV
    if response.status_code == 200:
        posts = response.json()  # Parse JSON into Python list of dictionaries
        structured_data = [{'id': post['id'], 'title': post['title'],
                            'body': post['body']} for post in posts]

        # Prepare data for CSV with selected keys: 'id', 'title', 'body'
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # Write header based on the fieldnames
            writer.writerows(structured_data)
        print("Data has been successfully written to posts.csv")
    else:
        print(f"Failed to fetch posts. Status Code: {response.status_code}")

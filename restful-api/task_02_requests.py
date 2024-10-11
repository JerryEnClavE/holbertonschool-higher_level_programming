import requests
import csv


def fetch_and_display_posts():
    """
    Fetches posts from the API and prints their titles.
    
    Sends a GET request to JSONPlaceholder and prints the
    titles if successful. Handles request errors.
    """

    url = 'https://www.jsonplaceholder.org/posts'

    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        response.raise_for_status()

        posts = response.json()

        for post in posts:
            print(f"Post Title: {post['title']}")
    
    except requests.exceptions.RequestException as error:
        print(f"Error: {error}")


def fetch_and_store_posts_to_csv():
    """
    Fetches posts and saves them to a CSV file.
    
    Retrieves data from the API and stores the 'id', 'title', and 'body'
    of each post in 'posts_data.csv'. Handles request errors.
    """
    
    url = 'https://jsonplaceholder.typicode.com/posts'

    try:
        response = requests.get(url)
        print(f"Response Status: {response.status_code}")
        response.raise_for_status()

        posts = response.json()

        posts_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']}
                      for post in posts]

        with open('posts_data.csv', mode='w', newline='', encoding='utf-8') as file:
            csv_writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            csv_writer.writeheader()
            csv_writer.writerows(posts_data)

        print(f"Data saved to posts_data.csv")

    except requests.exceptions.RequestException as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    fetch_and_display_posts()
    fetch_and_store_posts_to_csv()

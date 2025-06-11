# task_02_requests.py

import requests


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder and print their titles.
    Prints the response status code first.
    """

    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post["title"])

import requests
import csv


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

def fetch_and_save_posts():
    """
    Fetch all posts from JSONPlaceholder and save selected fields
    (id, title, body) into posts.csv.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        data = response.json()

        posts_list = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in data
        ]

        with open("posts.csv", mode="w", newline="") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts_list)

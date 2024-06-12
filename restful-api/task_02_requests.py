import requests
import csv

def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post['title'])

def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        data = response.json()
        # Write data to CSV
        with open('posts.csv', mode='w', newline='') as file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for post in data:
                writer.writerow({'id': post['id'], 'title': post['title'], 'body': post['body']})

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()


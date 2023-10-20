import requests
import json
url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(url)
data = response.json()
for item in data:
    if item['completed'] == 'true':
        print(f"ID: {item['id']}, Title: {item['title']}")
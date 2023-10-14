import requests
import json
url = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    titles = [post['title'] for post in data]
    print(titles)
else:
    print("Error:", response.status_code, response.reason)
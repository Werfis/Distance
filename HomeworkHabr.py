import requests
from bs4 import BeautifulSoup
def save_article(soup, article_number):
    with open(f'{article_number}.html', 'w') as file:
        file.write(str(soup))
def get_articles():
    link = 'https://habr.com/ru/articles/top/weekly/'
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    for h2 in soup.find_all('h2'):
        a = h2.find('a')
import requests
from bs4 import BeautifulSoup

test_url = 'http://books.toscrape.com/catalogue' \
      '/sorting-the-beef-from-the-bull-the-science-of-food-fraud-forensics_736' \
      '/index.html'


def get_book_info(book_url):
    response = requests.get(book_url)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find('title').text
        print(title)
    

get_book_info(test_url)

import pprint

import requests
from bs4 import BeautifulSoup


def get_books_url_from_category_url(category_url: str):
    response = requests.get(category_url)

    # example URL :
    # http://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html

    if response.ok:

        def get_page_books():
            soup = BeautifulSoup(response.content, "lxml")
            books = soup.select("section div ol li a")
            return books





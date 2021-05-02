import requests
from bs4 import BeautifulSoup


def get_books_url_from_category(category_url: str):
    """
    :param category_url: string
    :return category_books_list: dict
    """

    response = requests.get(category_url)
    category_books_list = {}

    # example URL :
    # http://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html

    if response.ok:
        soup = BeautifulSoup(response.content)
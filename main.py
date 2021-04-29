import requests
from bs4 import BeautifulSoup

'''Url de test'''
test_url = 'http://books.toscrape.com/catalogue/the-little-prince_72/index.html'


def get_book_data(book_url):
    """
    
    :rtype: dict
    """
    response = requests.get(book_url)
    book_data = {}
    if response.ok:
        soup = BeautifulSoup(response.text, "lxml")

        def get_the_data(cat):
            book_data[cat] = soup.find(class_=str(cat)).text

        get_the_data('active')
        get_the_data('price_color')
        get_the_data('')

    return book_data


print(get_book_data(test_url))
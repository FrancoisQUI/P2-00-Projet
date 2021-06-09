from pprint import pprint

import requests
from Color_Console import ctext
from bs4 import BeautifulSoup

from modules.book_actions import scrape_a_book_and_hydrate_csv


def get_books_url_from_category_url(category_url: str):
    books_links_to_scrape = []

    response = requests.get(category_url)

    # example URL :
    # http://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html
    if response.ok:

        def get_page_books():
            soup = BeautifulSoup(response.content, "lxml")
            page_books_link = soup.select('section div ol li h3 a')
            for book_link in page_books_link:
                book_uri = book_link.get("href").replace('../../..', '')
                book_url = "http://books.toscrape.com/catalogue" + book_uri
                books_links_to_scrape.append(book_url)
            return books_links_to_scrape

        books_url = get_page_books()

    else:
        print("Erreur de requête", response)
        return False

    return books_url


def get_category_next_page(category_url: str):
    response = requests.get(category_url)
    if response.ok:
        def get_category_url_name():
            pos = category_url.rfind("/") + 1
            category_url_name = category_url[:pos]
            return category_url_name

        soup = BeautifulSoup(response.content, "lxml")
        next_page = soup.select(".next a")

        if len(next_page) > 0:
            next_page_uri = next_page[0].get("href")
            next_page_url = str(get_category_url_name()) + next_page_uri
            return next_page_url

        else:
            return False


def scrape_category(first_category_page, site_url="http://books.toscrape.com"):
    page_to_scrape = first_category_page
    pre_books_to_scrape = []
    books_to_scrape = []
    while True:
        ctext("Category page book list", "yellow")
        category_books = get_books_url_from_category_url(page_to_scrape)
        pprint(category_books)
        ctext("Next category page", "yellow")
        page_to_scrape = get_category_next_page(page_to_scrape)
        print(page_to_scrape)
        pre_books_to_scrape.append(category_books)
        if not page_to_scrape:
            break

    for book_list in pre_books_to_scrape:
        for book in book_list:
            books_to_scrape.append(book)
    ctext("Full Book list from category to scrape :", "green")
    pprint(books_to_scrape)
    ctext(f"there are {len(books_to_scrape)} books to scrape", 'green')

    for book_to_scrape in books_to_scrape:
        scrape_a_book_and_hydrate_csv(book_to_scrape, site_url)

    ctext("Done")

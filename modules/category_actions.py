import requests
from bs4 import BeautifulSoup


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
        print("Erreur de requête")
        return False

    return books_url


def get_category_next_page(category_url: str):
    response = requests.get(category_url)
    if response.ok:
        def get_category_url_name():
            category_url_name = category_url.replace(
                "index.html", "")
            return category_url_name

        soup = BeautifulSoup(response.content, "lxml")
        next_page = soup.select(".next a")

        if len(next_page) > 0:
            next_page_uri = next_page[0].get("href")
            next_page_url = str(get_category_url_name()) + next_page_uri
            return next_page_url

        else:
            return False



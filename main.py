from pprint import pprint

import modules.book_actions as book_actions
import modules.category_actions as cat_actions
from Color_Console import *

OUTPUT_FILE_MAIN_DIR = "output_files"
SITE_URL = "http://books.toscrape.com"
TEST_FUNCTION = "Category"  # None, Book, Category


def scrape_a_book_and_hydrate_cvs(book_url: str,
                                  site_url: str):
    one_book = book_actions.get_book_data(book_url, site_url)
    cvs_file_name = OUTPUT_FILE_MAIN_DIR + "/" + one_book['category'] + ".csv"
    book_actions.book_data_to_csv(one_book, cvs_file_name)


def test_function(function_to_test):
    if function_to_test == "Book":
        ctext("Book's functions test :", 'blue')
        user_input = input("Url Page to scrape :\n     ")
        TEST_URL = user_input if user_input != '' \
            else "http://books.toscrape.com/catalogue/the-little-prince_72/index.html"

        # ie : http://books.toscrape.com/catalogue/the-little-prince_72/index.html

        a_book = book_actions.get_book_data(TEST_URL, SITE_URL)
        pprint(a_book)
        book_actions.book_data_to_csv(a_book,
                                      OUTPUT_FILE_MAIN_DIR
                                      + '/'
                                      + a_book["universal_product_code"] + "-"
                                      + str(a_book["title"]).replace(" ", "")
                                      + ".csv")

    elif function_to_test == "Category":
        ctext("Categories functions test : ", "blue")

        user_input = input("Category to scrape :\n     ")
        TESTED_CAT_URL = user_input if user_input != '' \
            else "http://books.toscrape.com/catalogue/category/books/romance_8/index.html"

        page_to_scrape = TESTED_CAT_URL
        pre_books_to_scrape = []
        books_to_scrape = []

        while True:
            ctext("Category page book list", "yellow")
            category_books = cat_actions.get_books_url_from_category_url(page_to_scrape)
            pprint(category_books)
            ctext("Next category page", "yellow")
            page_to_scrape = cat_actions.get_category_next_page(page_to_scrape)
            print(page_to_scrape)
            pre_books_to_scrape.append(category_books)
            if not page_to_scrape:
                break

        for book_list in pre_books_to_scrape:
            for book in book_list:
                books_to_scrape.append(book)

        pprint(books_to_scrape)
        ctext(f"there are {len(books_to_scrape)} books to scrape", 'green')

        for book_to_scrape in books_to_scrape:
            scrape_a_book_and_hydrate_cvs(book_to_scrape, SITE_URL)

        ctext("Done")

    elif function_to_test == "None":
        ctext("WIP", "red")

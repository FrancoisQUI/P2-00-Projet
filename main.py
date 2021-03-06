import os
from pprint import pprint

import modules.book_actions as book_actions
import modules.category_actions as cat_actions
import modules.site_actions as site_actions

from Color_Console import *

OUTPUT_FILE_MAIN_DIR = "output_files"
SITE_URL = "http://books.toscrape.com"
TEST_FUNCTION = "All"  # All, Book, Category


def check_and_create_dir(output_dir: str):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)


def test_function(function_to_test):
    check_and_create_dir(OUTPUT_FILE_MAIN_DIR)
    if function_to_test == "Book":
        ctext("Book's functions test :", 'blue')
        user_input = input("Url Page to scrape :\n     ")
        test_url = user_input if user_input != '' \
            else "http://books.toscrape.com/catalogue/the-little-prince_72/index.html"

        # ie : http://books.toscrape.com/catalogue/the-little-prince_72/index.html

        a_book = book_actions.get_book_data(test_url, SITE_URL)
        pprint(a_book)
        book_actions.download_book_img(a_book)
        book_actions.book_data_to_csv(a_book,
                                      OUTPUT_FILE_MAIN_DIR
                                      + '/'
                                      + a_book["universal_product_code"] + "-"
                                      + str(a_book["title"]).replace(" ", "")
                                      + ".csv")

    elif function_to_test == "Category":
        ctext("Categories functions test : ", "blue")

        user_input = input("Category to scrape :\n     ")
        tested_cat_url = user_input if user_input != '' \
            else "http://books.toscrape.com/catalogue/category/books" \
                 "/romance_8/index.html"
        cat_actions.scrape_category(tested_cat_url)

    elif function_to_test == "All":

        categories_url_to_scrape = site_actions.get_all_categories(SITE_URL)

        for category_url_to_scrape in categories_url_to_scrape:
            cat_actions.scrape_category(category_url_to_scrape)


test_function(TEST_FUNCTION)

from pprint import pprint

import modules.book_actions as book_actions
import modules.category_actions as cat_actions
from Color_Console import *

OUTPUT_FILE_MAIN_DIR = "output_files"
SITE_URL = "http://books.toscrape.com"
TEST_FUNCTION = "Category"  # None, Book, Category

if TEST_FUNCTION == "Book":
    ctext("Test des fonctions livres en cours")
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

elif TEST_FUNCTION == "Category":
    ctext("Test de Catégorie en cours.", "blue")

    user_input = input("Category to scrape :\n     ")
    TESTED_CAT_URL = user_input if user_input != '' \
        else"http://books.toscrape.com/catalogue/category/books/romance_8/index.html"

    ctext("Liste des livres de la page", "yellow")
    category_books = cat_actions.get_books_url_from_category_url(TESTED_CAT_URL)
    pprint(category_books)
    ctext("Recherche d'une page next", "yellow")
    next_page = cat_actions.get_category_next_page(TESTED_CAT_URL)
    pprint(next_page)

elif TEST_FUNCTION == "None":
    ctext("WIP", "red")

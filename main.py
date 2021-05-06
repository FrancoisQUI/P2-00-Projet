from pprint import pprint

import modules.book_actions as book_actions
import modules.category_actions as cat_actions

OUTPUT_FILE_MAIN_DIR = "output_files"
SITE_URL = "http://books.toscrape.com"
test_function = "Category"  # None, Book, Category

if test_function == "Book":
    user_input = input("Url Page to scrape :\n     ")
    TEST_URL = user_input if user_input != '' else "http://books.toscrape.com/catalogue/the-little-prince_72/index.html"

    # ie : http://books.toscrape.com/catalogue/the-little-prince_72/index.html

    a_book = book_actions.get_book_data(TEST_URL, SITE_URL)
    pprint(a_book)
    book_actions.book_data_to_csv(a_book,
                                  OUTPUT_FILE_MAIN_DIR
                                  + '/'
                                  + a_book["universal_product_code"] + "-"
                                  + str(a_book["title"]).replace(" ", "")
                                  + ".csv")

elif test_function == "Category":
    category_books = cat_actions.get_books_url_from_category_url(
        "http://books.toscrape.com/catalogue"
        "/category/books/add-a-comment_18/index.html")
    pprint(category_books)

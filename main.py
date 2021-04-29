from pprint import pprint

import requests
from bs4 import BeautifulSoup

'''Url de test'''

user_input = input("Url Page to scrape :\n    ")
test_url = user_input if user_input != '' else "http://books.toscrape.com/catalogue/the-little-prince_72/index.html"

# ie : http://books.toscrape.com/catalogue/the-little-prince_72/index.html


def clean_string(string: str):
    string = string.replace("Â£", '')
    return string


def get_book_data(book_url: str):
    """
    :rtype: dict
    """
    response = requests.get(book_url)
    book_data = {'product_page_url': book_url}
    if response.ok:
        soup = BeautifulSoup(response.text, "lxml")

        def get_data_from_table():
            """
            Read the table and push data in the book_data dict
            """
            table_lines = soup.findAll("tr")
            for table_line in table_lines:
                index = clean_string(table_line.find("th").get_text())
                data = clean_string(table_line.find("td").get_text())

                if index.lower() == "upc".lower():
                    book_data["universal_ product_code"] = data
                elif index.lower() == "Price (excl. tax)".lower():
                    book_data["price_including_tax"] = data
                elif index.lower() == "Price (incl. tax)".lower():
                    book_data["price_excluding_tax"] = data
                elif index.lower() == "Availability".lower():
                    data = data.replace("In stock (", "")
                    data = data.replace(" available)", "")
                    book_data["number_available"] = data

        def get_book_title():
            title = soup.find("h1").get_text()
            book_data["title"] = title

        def get_book_description():
            description = soup.find(id="product_description").find_next("p").get_text()
            book_data['product_description'] = description

        def get_book_category():
            category_link = soup.select(".breadcrumb li:nth-child(3) a")
            # TODO: Don't use CSS selector, but Bs methods instead
            category = category_link[0].get_text()
            book_data['category'] = category

        get_book_title()
        get_book_description()
        get_book_category()
        get_data_from_table()

    # to scrape : product_description, review_rating, image_url

    return book_data


pprint(get_book_data(test_url))

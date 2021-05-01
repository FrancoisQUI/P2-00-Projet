from pprint import pprint
import csv

import requests
from bs4 import BeautifulSoup

user_input = input("Url Page to scrape :\n    ")
test_url = user_input if user_input != '' else "http://books.toscrape.com/catalogue/the-little-prince_72/index.html"

# ie : http://books.toscrape.com/catalogue/the-little-prince_72/index.html

site_url = "http://books.toscrape.com"


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
                    book_data["universal_product_code"] = data
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

        def get_image_url():
            image = soup.select(".thumbnail img")
            image = image[0].get("src")
            image = str(image).replace("../..", site_url)
            book_data['image_url'] = image

        def get_review_rating():
            rating = soup.select_one(".star-rating")
            rating = rating.get("class")[1]
            if rating.lower() == "one":
                book_data['review_rating'] = '1'
            elif rating.lower() == "two":
                book_data['review_rating'] = '2'
            elif rating.lower() == "three":
                book_data['review_rating'] = '3'
            elif rating.lower() == "four":
                book_data['review_rating'] = '4'
            elif rating.lower() == "five":
                book_data['review_rating'] = '5'
            else:
                book_data['review_rating'] = 'error'

        get_book_title()
        get_book_description()
        get_book_category()
        get_data_from_table()
        get_image_url()
        get_review_rating()

    return book_data


def book_data_to_csv(book_data: dict, filename: str):
    desired_order = ["product_page_url",
                     "universal_product_code",
                     "title",
                     "price_including_tax",
                     "price_excluding_tax",
                     "number_available",
                     "product_description",
                     "category",
                     "review_rating",
                     "image_url"]

    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=desired_order)

        writer.writeheader()
        writer.writerow(book_data)


a_book = get_book_data(test_url)
pprint(a_book)
book_data_to_csv(a_book, 'test.csv')
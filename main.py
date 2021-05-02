from pprint import pprint

import modules.book_actions as book_actions

user_input = input("Url Page to scrape :\n    ")
test_url = user_input if user_input != '' else "http://books.toscrape.com/catalogue/the-little-prince_72/index.html"

# ie : http://books.toscrape.com/catalogue/the-little-prince_72/index.html

site_url = "http://books.toscrape.com"

a_book = book_actions.get_book_data(test_url)
pprint(a_book)
book_actions.book_data_to_csv(a_book, 'test.csv')

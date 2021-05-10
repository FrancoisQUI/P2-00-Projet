import requests
from bs4 import BeautifulSoup


def get_all_categories(site_url: str = "http://books.toscrape.com"):
    categories_link_to_scrape = []

    response = requests.get(site_url)

    if response.ok:
        soup = BeautifulSoup(response.content, "lxml")
        categories_link = soup.select(".side_categories ul li ul li a")
        for category_link in categories_link:
            categories_link_to_scrape.append("http://books.toscrape.com"
                                             + "/"
                                             + category_link.get("href"))
    else:
        print("Erreur de requête", response)
        return False

    return categories_link_to_scrape

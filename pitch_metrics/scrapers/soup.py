import requests
from bs4 import BeautifulSoup


def get_main_soup(url):
    response = requests.get(url)
    main_soup = BeautifulSoup(response.text, "html.parser")

    return main_soup

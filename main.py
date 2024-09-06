import re

import requests
from bs4 import BeautifulSoup

URL_DOMAIN = "https://pitchfork.com/reviews/albums/"


def get_main_soup(url):

    response = requests.get(url)
    main_soup = BeautifulSoup(response.text, "html.parser")

    return main_soup


def get_review_link(soup):

    a_list = soup.find_all("a",
                           class_="SummaryItemHedLink-civMjp PNQqc summary-"
                                  "item-tracking__hed-link summary-item__"
                                  "hed-link summary-item__hed-link--"
                                  "underline-disable")

    return a_list


def get_review_data(urls):

    reviews_list = []

    for url in urls:

        valid_links = f"https://pitchfork.com{url["href"]}"
        # print(valid_links)

        soup = get_main_soup(valid_links)

        try:
            artist = soup.find("div", class_=re.compile(
                "^BaseWrap-sc-gjQpdd BaseText-ewhhUZ "
                "SplitScreenContentHeaderArtist")).text

            album = soup.find("h1", class_=re.compile(
                "^BaseWrap-sc-gjQpdd BaseText-ewhhUZ "
                "SplitScreenContentHeaderHed")).text

            rating = soup.find("p", class_=re.compile(
                "^BaseWrap-sc-gjQpdd BaseText-ewhhUZ Rating")).text

            release_date = soup.find("time", class_=re.compile(
                "^SplitScreenContentHeaderReleaseYear")).text

            genre = soup.find("p", class_=re.compile(
                "^BaseWrap-sc-gjQpdd BaseText-ewhhUZ InfoSliceValue")).text

            review = f"{artist} - {album} : {rating}"
            print(review)
            print(release_date)
            print(genre)
            reviews_list.append(review)
            
        except:
            print(f"error with{valid_links}")

    return reviews_list


main_soup = get_main_soup(URL_DOMAIN)
albums_links = get_review_link(main_soup)

reviews = get_review_data(albums_links)

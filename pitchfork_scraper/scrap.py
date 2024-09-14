import re

import requests
from bs4 import BeautifulSoup
from pitchfork_scraper.insert import insert_artists, insert_albums
from pitchfork_scraper.models import session


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

            artist_record = insert_artists(session, artist)

            new_album = {'name': album,
                         'genre': genre,
                         'release_date': release_date,
                         'rating': rating,
                         'artist_id': artist_record.id}

            insert_albums(session, new_album)

            # print(f"{album} Added")

        except Exception as e:
            print(f"Error with {valid_links}")
            print(e)

    return reviews_list

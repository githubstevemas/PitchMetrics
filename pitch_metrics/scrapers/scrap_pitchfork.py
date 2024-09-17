import re

from pitch_metrics.scrapers.insert import insert_artist, insert_country
from pitch_metrics.stats.models import session
from pitch_metrics.scrapers.scrap_musicbrainz import get_artist_data
from pitch_metrics.scrapers.soup import get_main_soup


def get_review_link(soup):
    a_list = soup.find_all("a",
                           class_="SummaryItemHedLink-civMjp PNQqc summary-"
                                  "item-tracking__hed-link summary-item__"
                                  "hed-link summary-item__hed-link--"
                                  "underline-disable")

    return a_list


def get_review_data(url):
    valid_links = f"https://pitchfork.com{url["href"]}"

    soup = get_main_soup(valid_links)

    try:
        artist_name = soup.find("div", class_=re.compile(
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

        artist_country = get_artist_data(artist_name)

        country_id = insert_country(session, artist_country)

        new_artist = {'name': artist_name,
                      'country_id': country_id}

        artist_id = insert_artist(session, new_artist)

        new_album = {'name': album,
                     'genre': genre,
                     'release_date': release_date,
                     'rating': rating,
                     'artist_id': artist_id}

        return new_artist, new_album

    except Exception as e:
        print(f"Error with {valid_links}")
        print(e)

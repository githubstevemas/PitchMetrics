# https://musicbrainz.org/search?query=paris+sous+les+bombes&type=work
# tag bdi = nom du disque

import re

from pitch_metrics.scrapers.soup import get_main_soup


def get_artist_data(artist):
    artist_query = re.sub(r' ', '+', artist)

    query_link = \
        f"https://musicbrainz.org/search?query={artist_query}&type=artist"

    soup = get_main_soup(query_link)
    country = soup.find_all("td")[4].text

    return country


def get_album_label(album_data, artist):
    album_query = re.sub(r' ', "+", album_data["name"])
    artist_query = re.sub(r' ', '+', artist['name'])

    query_link = \
        (f"https://musicbrainz.org/taglookup/"
         f"index?tag-lookup.artist={artist_query}"
         f"&tag-lookup.release={album_query}")

    soup = get_main_soup(query_link)

    label = soup.find_all("td")[5].text

    return label

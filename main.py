from pitchfork_scraper.insert import insert_album, insert_label
from pitchfork_scraper.models import session
from pitchfork_scraper.scrap_musicbrainz import get_album_label
from pitchfork_scraper.scrap_pitchfork import get_main_soup, get_review_link, \
    get_review_data


def main():

    url = "https://pitchfork.com/reviews/albums/"
    page_nb = 1

    while True:
        print(f"Page {page_nb} in progress...")

        main_soup = get_main_soup(url)

        albums_links = get_review_link(main_soup)

        for album_url in albums_links:
            try:
                artist, album = get_review_data(album_url)

                label_name = get_album_label(album, artist)

                label_id = insert_label(session, label_name)

                insert_album(session, album, label_id)

                print(f"{artist['name']}, from {artist['country_id']}. album : "
                      f"{album['name']} {album['genre']} {album['release_date']} "
                      f"{album['rating']} {label_name}")

            except Exception as e:
                print(e)

        page_nb += 1

        url = f"https://pitchfork.com/reviews/albums/?page={page_nb}"


if __name__ == "__main__":
    main()

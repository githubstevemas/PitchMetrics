from pitchfork_scraper.scrap import get_main_soup, get_review_link, \
    get_review_data


def main():

    url = "https://pitchfork.com/reviews/albums/"
    page_nb = 1

    while True:
        try:

            print(f"Page {page_nb} in progress...")
            main_soup = get_main_soup(url)
            albums_links = get_review_link(main_soup)

            get_review_data(albums_links)
            page_nb += 1

            url = f"https://pitchfork.com/reviews/albums/?page={page_nb}"

        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()

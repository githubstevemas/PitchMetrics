from sqlalchemy.dialects.postgresql import insert

from pitchfork_scraper.models import Album, Artist


def insert_albums(session, album_data):

    stmt = insert(Album).values({
        'name': album_data['name'],
        'genre': album_data['genre'],
        'release_date': album_data['release_date'],
        'rating': album_data['rating'],
        'artist_id': album_data['artist_id']
    })

    stmt = stmt.on_conflict_do_nothing(index_elements=['name', 'artist_id'])

    result = session.execute(stmt)
    session.commit()

    if result.rowcount == 0:
        print(f"Album {album_data['name']} already insert.")
    else:
        print(f"Album {album_data['name']} successfully insert.")


def insert_artists(session, artist):

    stmt = insert(Artist).values({'name': artist})

    stmt = stmt.on_conflict_do_nothing(index_elements=['name'])

    session.execute(stmt)
    session.commit()

    return session.query(Artist).filter_by(name=artist).first()

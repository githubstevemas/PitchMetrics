from sqlalchemy.dialects.postgresql import insert

from pitch_metrics.stats.models import Album, Artist, Country, Label


def insert_label(session, label_name):

    stmt = insert(Label).values({'name': label_name})
    stmt = stmt.on_conflict_do_nothing(index_elements=['name'])

    session.execute(stmt)
    session.commit()

    return session.query(Label).filter_by(name=label_name).first().id


def insert_country(session, country_name):

    stmt = insert(Country).values({'name': country_name})
    stmt = stmt.on_conflict_do_nothing(index_elements=['name'])

    session.execute(stmt)
    session.commit()

    return session.query(Country).filter_by(name=country_name).first().id


def insert_album(session, album_data, label_id):

    stmt = insert(Album).values({
        'name': album_data['name'],
        'genre': album_data['genre'],
        'release_date': album_data['release_date'],
        'rating': album_data['rating'],
        'artist_id': album_data['artist_id'],
        'label_id': label_id
    })

    stmt = stmt.on_conflict_do_nothing(index_elements=['name', 'artist_id'])

    session.execute(stmt)
    session.commit()


def insert_artist(session, artist):

    stmt = insert(Artist).values({
        'name': artist['name'],
        'country_id': artist['country_id']
    })
    stmt = stmt.on_conflict_do_nothing(index_elements=["name"])

    session.execute(stmt)
    session.commit()

    return session.query(Artist).filter_by(name=artist['name']).first().id

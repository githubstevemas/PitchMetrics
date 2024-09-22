from django.shortcuts import render
from sqlalchemy.orm import joinedload

from stats.models import Label, Album, Artist
from scrapers.config import SessionLocal


def explore_labels_view(request):

    session = SessionLocal()

    try:
        labels_list = session.query(Label).order_by(Label.name.asc()).all()

        clear_label_list = labels_list[2:]

        context = {'labels_list': clear_label_list}

        return render(request, 'explore/index.html', context)

    finally:
        session.close()


def label_details_view(request, label_id):

    session = SessionLocal()

    try:
        label = session.query(Label).filter_by(id=label_id).first()
        albums = session.query(Album).filter_by(label_id=label_id).options(
            joinedload(Album.artist).joinedload(Artist.country)
        ).all()

    finally:
        session.close()

    context = {'label': label,
               'albums_list': albums}

    return render(request, 'explore/label_details.html', context)

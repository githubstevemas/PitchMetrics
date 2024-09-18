from sqlalchemy import Column, Integer, String, Float, ForeignKey, \
    UniqueConstraint
from sqlalchemy.orm import relationship, sessionmaker

from scrapers.config import Base, engine


class Artist(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    country_id = Column(Integer, ForeignKey('countries.id'))

    albums = relationship("Album", back_populates="artist")
    country = relationship("Country", back_populates="artists")


class Album(Base):
    __tablename__ = 'albums'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    artist_id = Column(Integer, ForeignKey('artists.id'))
    genre = Column(String)
    release_date = Column(String)
    rating = Column(Float)
    label_id = Column(Integer, ForeignKey('labels.id'))

    __table_args__ = (
        UniqueConstraint('name', 'artist_id', name='_album_artist_uc'),
    )

    artist = relationship("Artist", back_populates="albums")
    label = relationship("Label", back_populates="albums")


class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    artists = relationship("Artist", back_populates="country")


class Label(Base):
    __tablename__ = 'labels'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    albums = relationship("Album", back_populates="label")


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

from sqlalchemy import Column, Integer, String, Float, ForeignKey, \
    UniqueConstraint
from sqlalchemy.orm import relationship, sessionmaker

from pitchfork_scraper.config import Base, engine


class Artist(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    albums = relationship("Album", back_populates="artist")


class Album(Base):
    __tablename__ = 'albums'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    artist_id = Column(Integer, ForeignKey('artists.id'))
    genre = Column(String)
    release_date = Column(String)
    rating = Column(Float)

    __table_args__ = (
        UniqueConstraint('name', 'artist_id', name='_album_artist_uc'),
    )
    artist = relationship("Artist", back_populates="albums")


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

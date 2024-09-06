class Artist:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)


class Album:

    def __init__(self, name, artist, genre, release_date, rating):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.release_date = release_date
        self.rating = rating

        artist.add_album(self)

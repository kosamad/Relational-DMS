# note due to the database using album-id instead of AlbumId I'm not sure if everything here is PEP8 complient. Need to make sure I do that for my own work 


from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String, 
) 

# note there is no table or metadata now above

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the chinook database
# the base class grabs the metadata producted by the databaseand creates a subclass to map it within the variable 
db = create_engine("postgresql:///chinook")
base = declarative_base()

#building normal python objects that subclasses"base"
class Artist(base):
    __tablename__="artist"
    artist_id = Column(Integer, primary_key=True)
    name = Column(String)

# create a class-based model for the "Album" table
class Album(base):
    __tablename__ = "album"
    album_id = Column(Integer, primary_key=True)
    title = Column(String)
    artist_id= Column(Integer, ForeignKey("artist.artist_id"))

# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "track"
    track_id = Column(Integer, primary_key=True)
    name = Column(String)
    album_id = Column(Integer, ForeignKey("album.album_id"))
    media_type_id= Column(Integer, primary_key=False)
    genre_id = Column(Integer, primary_key=False)
    composer = Column(String)
    milliseconds = Column(Integer, primary_key=False)
    bytes = Column(Integer, primary_key=False)
  


# note the cases of the sessions
# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database subclass using declarative_base subclass
base.metadata.create_all(db)


# Query 1 - select all records from the "Artist" table. sep = the separator we want between columns
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.artist_id, artist.name, sep=" | ")


# Query 2 - select only the "Name" column from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.name)


# Query 3 - select only "Queen" from the "Artist" table. first gives us only the first item as this is what we are expecting
# artist = session.query(Artist).filter_by(name="Queen").first()
# print(artist.artist_id, artist.name, sep=" | ")


# Query 4 - select only by "artist_id" #51 from the "Artist" table
# artist = session.query(Artist).filter_by(artist_id=51).first()
# print(artist.artist_id, artist.name, sep=" | ")


# Query 5 - select only the albums with "artist_id" #51 on the "Album" table
# albums = session.query(Album).filter_by(artist_id=51)
# for album in albums:
#     print(album.album_id, album.title, album.artist_id, sep=" | ")

# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
tracks = session.query(Track).filter_by(composer="Queen")
for track in tracks:
    print(track.track_id, track.name, sep=" | ")
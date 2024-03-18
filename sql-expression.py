# note due to the database using album-id instead of AlbumId I'm not sure if everything here is PEP8 complient. Need to make sure I do that for my own work 


from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
) 

# exectuing the instructions from our local host "chinook" db. Linking the python file to our database. \\\ = database is hosted locally within the postgres server
db = create_engine("postgresql:///chinook")

# MetaData class contains a collection of our table objects and associated data
meta = MetaData()

# construct the table
# create variable for the "artist" table using the table import method and the name of the table we want to get with the meta schema
# then define the columns (name, type of data presented, other optional fields)
artist_table = Table(
    "artist", meta, 
    Column("artist_id", Integer, primary_key = True),
    Column("name", String))

# create a variable for the "album" table
album_table = Table(
    "album", meta,
    Column("album_id", Integer, primary_key = True),
    Column("title", String),
    Column("artist_id", Integer, ForeignKey("artist_table.artist_id")))

# create a variable for the "track" table
track_table = Table(
    "track", meta,
    Column("track_id", Integer, primary_key = True),
    Column("name", String),
    Column("album_id", Integer, ForeignKey("album_table.album_id")),
    Column("media_type_id", Integer, primary_key = False),
    Column("genre_id", Integer, primary_key = False),
    Column("composer", String),
    Column("milliseconds", Integer),
    Column("bytes", Integer),  
)


# making the connection which is saved to the database in "connection"
# as have used the same variable select-query have commented out each query in turn 

with db.connect() as connection:
    # Query 1 - select all records from the "artist" table
    # select_query = artist_table.select()

    # Query 2 - select only the "name" column from the "artist" table. .c identifys a specific colum header
    # select_query = artist_table.select().with_only_columns([artist_table.c.name])

    # Query 3 - select only Queen from the artist table 
    # select_query = artist_table.select().where(artist_table.c.name == "Queen")

    # Query 4 - select only artist_id #51 from the artist table
    # select_query = artist_table.select().where(artist_table.c.artist_id == 51)

    # Query 5 - select only the albums with 'ArtistId' #51 on the "Album" table
    # select_query = album_table.select().where(album_table.c.artist_id== 51)

    # Query 6 - select all tracks where the composer is 'Queen' from the "Track" table
    select_query = track_table.select().where(track_table.c.composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)
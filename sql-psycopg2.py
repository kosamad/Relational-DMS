import psycopg2

# connect to chinook database using connect() method
connection = psycopg2.connect(database = "chinook")

# build a cursor object of the database (from what we query)
cursor = connection.cursor()

# coded out prev queries to avoid duplicates

# Query 1 - select all records from the "artist" table
# the quote use here has to be EXACTLY THE SAME
# cursor.execute('SELECT * FROM "artist"')

# Query 2 - select only the "name" column from the "artist" table
# cursor.execute('SELECT "name" FROM "artist"')

# Query 3 - select only Queen from the artist table (therefore use with fetchone)
# cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["Queen"])

# Query 4 - select only artist_id #51 from the artist table
# cursor.execute('SELECT * FROM "artist" WHERE "artist_id" = %s', [51])

# # Query 5 - select on albums with the artist ID #51 on the album table
# cursor.execute('SELECT * FROM "album" WHERE "artist_id" = %s', [51])

# Query 5 - select on albums with the artist ID #51 on the album table
# cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["Queen"])

# # Query 6 - select only 'Jack Johnson' from the artist table (therefore use with fetchone)
# cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["Jack Johnson"])

# Query 6 - select only 'test' from the artist table- doesn't work!
cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["test"])

# # fetch the results from the cursor (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close connection
connection.close()

# print results (to get each individually, need a for loop)
for result in results:
    print(result)
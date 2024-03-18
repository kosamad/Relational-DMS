import psycopg2

# connect to chinook database using connect() method
connection = psycopg2.connect(database = "chinnok")

# build a cursor object of the database (from what we query)
cursor = connection.cursor()

# fetch the results from the cursor (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close connection
connection.close()

# print results (to get each individually, need a for loop)
for result in results:
    print(result)
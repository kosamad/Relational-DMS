# note due to the database using album-id instead of AlbumId I'm not sure if everything here is PEP8 complient. Need to make sure I do that for my own work 

# Here's the typical workflow for using SQLAlchemy sessions:

# Open Session: Create a new session instance using Session = sessionmaker(db) and then open a session using session = Session().

# Perform Database Operations: Use the session to perform database operations such as querying, adding, updating, or deleting records.

# Commit or Rollback Transactions: If you've made changes to the database within a transaction, commit or rollback the transaction using session.commit() or session.rollback().

# Close Session: Once you're done with the session and no longer need to interact with the database, close the session using session.close().

# Repeat: If you need to perform further database operations later, repeat the process by opening a new session.

# if you make a mistake you can rollback() the session. 



from sqlalchemy import (
    create_engine, Column, Integer, String, 
) 


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the chinook database
# the base class grabs the metadata producted by the databaseand creates a subclass to map it within the variable 
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model fo rthe "programmer" table

class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True) # auto increments
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# note the cases of the sessions
# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database subclass using declarative_base subclass
base.metadata.create_all(db)


# creating records on our Progammer table using name as the variable and uses the programmer object (above) to define the key value pairs.
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

karen_samad = Programmer(
    first_name="Karen",
    last_name="Samad",
    gender="F",
    nationality="British",
    famous_for="Being the best new start coder"
)



# Think like github, this is how we add the records to the table
# 1 add to session
# 2 commit the session
# 3 check it's worked using the 1st query below
# if adding programmers individually need to comment out otherwise get more than one record for each

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
session.add(karen_samad)



#REMEMEBER CAN ONLY DO ONE QUERY AT ONCE SO NEED TO COMMENT OUT PART WE AREN'T USING

# updating a single record on the programmer table therefore need the .first
# programmer = session.query(Programmer).filter_by(id=11).first()
# programmer.id = 6

# commit our session to the database to save the changes when updating. 
session.commit()


# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit() # needs to be part of the loop

# deleting a record. need to identify records with something unique. but if we don't know the 1' ID we can use python input()
# doens't need a commit
# fname = input("Enter a first name: ") # use both first name and last name to make sure finding right person
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# # defensive programming checks the right person has been found
# if programmer is not None:
#     print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")


# query the database to find all Programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
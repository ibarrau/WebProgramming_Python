import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#postgresql://user@server:password@server/database
engine = create_engine('postgresql://user@server:password@server/database')
db = scoped_session(sessionmaker(bind=engine))

def insert_csv():
    f = open("flights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration) ",
            {"origin":origin, "destination":destination, "duration":duration} )
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
    db.commit()
    db.close()

if __name__ == "__main__":
    insert_csv()
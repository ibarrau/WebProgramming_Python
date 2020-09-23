import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#postgresql://user@server:password@server/database
engine = create_engine('postgresql://user@server:password@server/database')
db = scoped_session(sessionmaker(bind=engine))

def read():
    flights = db.execute("SELECT origin, destination, duration from flights")
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")
    db.close()

if __name__ == "__main__":
    read()
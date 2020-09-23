import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#postgresql://user@server:password@server/database
engine = create_engine('postgresql://user@server:password@server/database')
db = scoped_session(sessionmaker(bind=engine))

def read():
    # List flights
    flights = db.execute("SELECT origin, destination, duration from flights")
    for flight in flights:
        print(f"Flight {flight.origin} to {flight.destination}, {flight.duration} minutes.")
    
    # Check flight
    flight_id = int(input("\nFlight ID: "))
    flight = db.execute("SELECT origin, destination, duration FROM flights where id = :id",
        {"id":flight_id}).fetchone()

    # Make sure flight is valid
    if flights is None:
        print("Error: No such flight.")
        return

    # List passenger
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
        {"flight_id":flight_id}).fetchall()
    print("\nPassengers: ")
    for passenger in passengers:
        print(passenger.name)
    if len(passengers) == 0:
        print("No passengers.")

    db.close()

if __name__ == "__main__":
    read()
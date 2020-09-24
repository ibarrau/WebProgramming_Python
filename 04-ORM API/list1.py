import csv
from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://user@server:password@server/database'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def read():
    flights = Flight.query.all()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

def query():
    # SELECT * FROM flights WHERE origin = "Paris"
    primero = Flight.query.filter_by(origin="Paris").first()
    # SELECT count(*) FROM flights WHERE origin = "Paris"
    contar = Flight.query.filter_by(origin="Paris").count()
    # SELECT * FROM flight WHERE id = 28
    contar = Flight.query.get(28)
    # SELECT * FROM flights ORDER BY origin DESC;
    order = Flight.query.order_by(Flight.origin.desc()).all()
    # SELECT * FROM flights WHERE origin != 'Paris'
    noigual = Flight.query.filter(Flight.origin != "Paris").all()
    # SELECT * FROM flights WHERE origin LIKE '%a%'
    like = Flight.query.filter(Flight.origin.like("%a%")).all()
    # SELECT * FROM flights WHERE origin IN ('Paris', 'Roma')
    instate = Flight.query.filter(Flight.origin.in_(["Paris","Roma"])).all()
    # SELECT * FROM flights WHERE origin = 'Paris' AND/OR duration > 500;
    andor = Flight.query.filter(and_(Flight.origin == 'Paris', Flight.duration > 500)).all()
    # SELECT * FROM flights JOIN passengers ON flights.id = passengers.flight_id;
    joiny = db.session.query(Flight, Passenger).filter(Flight.id == Passenger.flight_id).all()
    # SELECT * FROM flights JOIN passengers ON flight.id = passengers.flight_id WHERE passengers.name = 'Alice';
    flightsalice = Passenger.query.filter_by(name="Alice").first().flight

def update():
    #UPDATE flights SET duration=200 WHERE id=28;
    flight = Flight.query.get(28)
    flight.duration = 200

def delete():
    #DELETE FROM flights WHERE id=28
    flight = Flight.query.get(28)
    db.session.delete(flight)

if __name__ == "__main__":
    with app.app_context():
        read()
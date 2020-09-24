from flask import Flask, render_template, request, session, jsonify
from flask_session import Session
import datetime
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://user@server:password@server/database'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    flights = Flight.query.all()
    return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
    """Book a flight."""
    # Get form information.
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        render_template("error.html", message = "No such flight number.")
    
    # Make book
    # Validate the id exists
    f = Flight.query.get(flight_id)
    if f is None:
        return render_template("success.html", message = "No such flight with that id.")
    
    # Object way
    f.add_passenger(name=name)
    
    # Old regular DB way
    # pas = Passenger(name=name, flight_id=flight_id)
    # db.session.add(pas)
    # db.session.commit()
    return render_template("success.html")

@app.route("/flights")
def flights():
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """List details of Flight"""
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="Flight error.")
    
    # Get passengers
    # passengers = Passengers.query.filter_by(flight_id=flight_id).all()
    # passengers = Passengers.query.filter(Passengers.flight_id= flight_id).all()
    passengers = flight.passengers
    return render_template("flight.html", flight=flight, passengers=passengers)

@app.route("/api/flights/<int:flight_id>")
def flight_api(flight_id):
    flight = Flight.query.get(flight_id)
    if flight is None:
        return jsonify({"error":"Invalid flight_id"}), 422
    
    passengers = flight.passengers
    names = []
    for p in passengers:
        names.append(p.name)
    # jsonify converts a python dict to json
    return jsonify({
        "origin": flight.origin,
        "destination": flight.destination,
        "duration": flight.duration,
        "passengers": names
    })
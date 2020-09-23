from flask import Flask, render_template, request, session
from flask_session import Session
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#postgresql://user@server:password@server/database
engine = create_engine('postgresql://user@server:password@server/database')
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
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
    if db.execute("SELECT * FROM flights where id = :id", {"id":flight_id}).rowcount == 0:
        return render_template("success.html", message = "No such flight with that id.")
    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id) ",
            {"name":name, "flight_id":flight_id} )
    db.commit()
    return render_template("success.html")

@app.route("/flights")
def flights():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("flights.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """List details of Flight"""
    flight = db.execute("SELECT * FROM flights WHERE id= :id", 
        {"id":flight_id}).fetchone()
    if flight is None:
        return render_template("error.html", message="Flight error.")
    
    passengers = db.execute("SELECT * FROM passengers WHERE flight_id=:flight_id", 
        {"flight_id":flight_id}).fetchall()
    for p in passengers:
        print(p.name)
    return render_template("flight.html", flight=flight, passengers=passengers)
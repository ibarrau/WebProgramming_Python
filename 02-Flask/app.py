# Change environment variables to use different name on flask app
# In cmd run export FLASK_APP=application.py

from flask import Flask, render_template, request, session
from flask_session import Session
import datetime

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

#Default page
@app.route("/")
def index():
    return "Hello world!"
    
# Functio name doesn't have to match
# @app.route("/<string:name>")
# def hello(name):
#     name = name.capitalize()
#     return f"<h1>Hello {name}!</h1>"

@app.route("/view")
def view():
    #index.html will be default for "/"
    return render_template("view.html")

# The {{ name }} is Jinja2 language
@app.route("/variable")
def variable():
    headline = "Hello world!"
    return render_template("variable.html", headline=headline)

@app.route("/bye")
def bye():
    headline = "Goodbye!"
    return render_template("variable.html")

@app.route("/condition")
def condition():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template("condition.html", new_year=new_year)

@app.route("/loop")
def loop():
    names = ["Alice", "Bob", "Charlie"]
    return render_template("loop.html", names=names)

@app.route("/indexxx")
def indexxx():
    return render_template("indexxx.html")

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/inheritance")
def inheritance():
    return render_template("inheritance.html")

@app.route("/indexform")
def indexform():
    return render_template("indexform.html")

@app.route("/hello", methods=["POST"])
def hello():
    if request.method == "GET":
        return "Please submit the form instead."
    name = request.form.get("name")
    return render_template("hello.html", name=name)

@app.route("/notas", methods=["GET","POST"])
def notas():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)
    return render_template("notas.html", notes=session["notes"])
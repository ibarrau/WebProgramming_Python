from flask import Flask, render_template, request, session, jsonify
from flask_session import Session
import datetime
import requests

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

#Default page
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/convert", methods = ["POST"])
def convert():
    currency = request.form.get("currency")
    res = requests.get("https://data.fixer.io/api/latest", 
        params ={ "base":"USD", "symbols":currency} )

    if res.status_code != 200:
        return jsonify({"success":False})

    data = res.json()
    #if currency not in data["error"]:
        #return jsonify({"success": False})
    return jsonify({"success": True, "code": data["error"]["code"]})
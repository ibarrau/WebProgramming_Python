import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

#Default page
@app.route("/")
def index():
    return render_template('index.html')

texts = ["Texto largo Texto largo Texto largo Texto largo Texto largo Texto largo Texto largo.", "Segundo largo", "Tercer largo"]

#Default page
@app.route("/first")
def first():
    return texts[0]

@app.route("/second")
def second():
    return texts[1]

@app.route("/third")
def third():
    return texts[2]

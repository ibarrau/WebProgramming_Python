import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

#Default page
@app.route("/")
def first():
    return render_template('first.html')

@app.route("/second")
def second():
    return render_template('second.html')

@app.route("/third")
def third():
    return render_template('third.html')

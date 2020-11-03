import os
from flask import Flask, request, render_template, jsonify
import time 

app = Flask(__name__)

#Default page
@app.route("/")
def index():
    return render_template('index.html')    

#Default page
@app.route("/posts", methods = ["POST"])
def posts():
    # Get start and end point for posts to generate.
    start = int(request.form.get("start") or 0)
    end = int(request.form.get("end") or (start + 9))

    # Generate list of posts
    data = []
    for i in range(start, end +1):
        data.append(f"Post #{i}")
    
    # Artificially delay speed of response
    time.sleep(1)

    return jsonify(data)

@app.route("/second")
def second():
    return texts[1]

@app.route("/third")
def third():
    return texts[2]

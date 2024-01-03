from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def countdown():

    launchTime = datetime(2024, 1, 22)
    currentTime = datetime.now()
    diff = launchTime - currentTime
    numberOfMilliseconds = int(diff.total_seconds() * 1000)

    return render_template(
        "countdown.html",
        time=numberOfMilliseconds
    )
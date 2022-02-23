from flask import Flask, render_template
from datetime import date
app = Flask(__name__)


today = date.today()
@app.route('/')
def index():
    return render_template("index.html", time=today)


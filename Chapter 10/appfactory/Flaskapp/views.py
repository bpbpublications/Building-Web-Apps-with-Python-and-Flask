from flask import current_app as app
from flask import render_template

@app.route("/")
def index():
    return "Hello Flask"

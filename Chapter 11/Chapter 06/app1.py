from flask import Flask, render_template
print (__name__)
app = Flask(__name__)

@app.route('/<name>')
def hello(name):
    return render_template("btn.html", name=name)

from flask import Flask, url_for
print (__name__)
app = Flask(__name__)

@app.route('/')
def index():
    url1=url_for('hello')
    url2=url_for('welcome')
    return "<a href={}>click here for hello()</a>".format(url1)+\
           "<br><a href={}>click here for welcome()</a>".format(url2)

def hello():
    return "Hello World!"

def welcome():
    return 'Welcome to Flask Framework'

app.add_url_rule('/hello', 'hello', hello)
app.add_url_rule('/welcome','welcome',welcome)

from flask import Flask
print (__name__)
app = Flask(__name__)

#@app.route('/hello')
def hello():
    return 'Hello World!'

def welcome():
    return 'Welcome to Flask Framework'

app.add_url_rule('/hello', 'hello', hello)
app.add_url_rule('/welcome','welcome',welcome)

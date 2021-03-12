from flask import Flask, request, g
app = Flask(__name__)

@app.before_first_request
def first_request():
    print ("This function is run before first request")    

@app.before_request
def each_request():
g.user='guest'
    print ("This is run before {} visits '{}'".format(g.user, request.path))

@app.after_request
def after_request(response):
    print ("This executes after exiting '{}'".format(request.path))
    return response

@app.route('/')
def index():
    return "<h2>Your IP address is {}</h2>".format(request.remote_addr)
@app.route('/hello')
def hello():
    string="<h2 style='text-align:center'>Hello <i>{}</i>. Welcome to Flask</h2>".format(g.user)
    return string

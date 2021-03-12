from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/')
def index():
    name=request.args.get('name')
    age=request.args.get('age')
    return "<h1> Data Received by GET method<br> name:{} age:{}</h1>".format(name,age)
@app.route('/form')
def about():
    return render_template('form.html')

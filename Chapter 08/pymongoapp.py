from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydata"
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("register.html")
@app.route('/addrec',methods=['POST', 'GET'])
def addrec():
    if request.method=='POST':
        print (request.form.to_dict())
        students_collection=mongo.db.students
        students_collection.insert(request.form.to_dict())
        return 'added successfully'

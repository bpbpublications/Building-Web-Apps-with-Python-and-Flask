from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'mydata',
    'host': 'localhost',
    'port':27017
}
db = MongoEngine(app)

import mongoengine as me
class students(me.Document):
    name=me.StringField(required=True)
    course=me.StringField()
    gender=me.StringField()
    mobile=me.IntField()
    username=me.StringField(required=True, primary_key=True)
    password=me.StringField()

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/addrec', methods=['GET', 'POST'])

def addrec():
    if request.method=='POST':
        student=students(name=request.form['name'])
        student.course=request.form['course']
        student.gender=request.form['gender']
        student.mobile=request.form['mobile']
        student.username=request.form['user']
        student.password=request.form['pwd']
        student.save()
    return 'success'
@app.route('/list')
def studentlist():
    docs=students.objects
    return render_template("studentlist.html", docs=docs)

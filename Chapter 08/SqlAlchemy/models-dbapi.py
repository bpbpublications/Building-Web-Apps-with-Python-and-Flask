from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydata.db'
app.config['SECRET_KEY']="random string"
db = SQLAlchemy(app)

class students(db.Model):
  name=db.Column(db.String(20))
  course=db.Column(db.String(20))
  gender=db.Column(db.String(10))
  mobile=db.Column(db.Integer)
  username=db.Column(db.String(6), primary_key=True)
  password=db.Column(db.String(8), nullable=False)

  def __init__(self, name, course, gender, mobile,username,password):
    self.name=name
    self.course=course
    self.gender=gender
    self.mobile=mobile
    self.username=username
    self.password=password

class books(db.Model):
  bookID=db.Column(db.Integer, primary_key=True)
  title=db.Column(db.String(100))
  author=db.Column(db.String(50))
  borrower=db.Column(db.String(6), db.ForeignKey('students.username'))

def __init__(self, id, title, author, borrower):
  self.id=id
  self.title=title
  self.author=author
  self.borrower=borrower
  

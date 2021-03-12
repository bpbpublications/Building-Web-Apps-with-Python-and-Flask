from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///flaskdatabase.db'
app.config['SECRET_KEY']="random string"
db = SQLAlchemy(app)

class books(db.Model):
  bookID=db.Column(db.String(6), primary_key=True)
  title=db.Column(db.String(20))
  category=db.Column(db.String(20))
  publisher=db.Column(db.String(50))
  price=db.Column(db.Integer)

  def __init__(self, id, title, ctg, publisher, price):
    self.bookID=id
    self.title=title
    self.category=ctg
    self.publisher=publisher
    self.price=price
  

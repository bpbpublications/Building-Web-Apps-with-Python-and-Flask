from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///flaskdatabase.db'
app.config['SECRET_KEY']="random string"
db = SQLAlchemy(app)

class books(db.Model):
  bookID=db.Column(db.String(6), primary_key=True)
  title=db.Column(db.String(20))
  Author=db.Column(db.String(20))
  price=db.Column(db.Integer)

  def __init__(self, id, title, author, price):
    self.bookID=id
    self.title=title
    self.Author=author
    self.price=price

  def serialize(self):
    return {"bookID":self.bookID,
            "title":self.title,
            "author":self.Author,
            "price":self.price
            }
  

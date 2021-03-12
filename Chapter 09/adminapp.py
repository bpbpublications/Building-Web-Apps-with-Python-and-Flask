from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_admin import Admin 
from flask_admin.contrib.sqla import ModelView
from models import book
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydata.db'
app.config['SECRET_KEY'] = 'something'
db = SQLAlchemy(app)
admin = Admin()
admin.add_view(ModelView(book, db.session))

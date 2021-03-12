from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse

from models import app,db, books
app = Flask(__name__)
api = Api(app)

todos = {}
parser = reqparse.RequestParser()
parser.add_argument('bookID')
parser.add_argument('title')
parser.add_argument('Author')
parser.add_argument('price')
class Books(Resource):
    def get(self):
        res=books.query.all()
        lb=[]
        for i in res:
            s=i.serialize()
            lb.append(s)    
        return jsonify({"books":lb})
        

##class Book(Resource):
##    def get(self, id):
##        res=books.query.filter_by(bookID=id).first()
##        book=res.serialize()
##        return book#jsonify({"book":book})
            


#api.add_resource(Book, '/books/<string:id>')
api.add_resource(Books, '/books')

if __name__ == '__main__':
    app.run()

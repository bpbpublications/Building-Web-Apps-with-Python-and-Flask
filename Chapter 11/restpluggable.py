from flask.views import MethodView
from flask import Flask, request, jsonify
from models import app,db, books

class BookAPI(MethodView):

    def get(self, id):
            if id is None:
                res=books.query.all()
                lb=[]
                for i in res:
                    s=i.serialize()
                    lb.append(s)    
                return jsonify({"books":lb})
            else:
                res=books.query.filter_by(bookID=id).first()
                book=res.serialize()
                return jsonify({"book":book})

    def post(self):
            book = books(request.json['bookID'],request.json['title'],request.json['Author'],request.json['price'])
            db.session.add(book)
            db.session.commit()
            res=books.query.all()
            lb=[]
            for i in res:
                s=i.serialize()
                lb.append(s)    
            return jsonify({"books":lb})

    def delete(self, id):
            res=books.query.filter_by(bookID=id).first()
            db.session.delete(res)
            db.session.commit()
            res=books.query.all()
            lb=[]
            for i in res:
                s=i.serialize()
                lb.append(s)    
            return jsonify({"books":lb})

    def put(self, id):
            id=request.json['bookID']
            price=request.json['price']
            res=books.query.filter_by(bookID=id).first()
            res.price=price
            db.session.commit()
            book=res.serialize()
            return jsonify({'book':book})

book_view = BookAPI.as_view('book_api')
app.add_url_rule('/books/', defaults={'id': None}, view_func=book_view, methods=['GET',])
app.add_url_rule('/books/', view_func=book_view, methods=['POST',])
app.add_url_rule('/books/<id>', view_func=book_view,methods=['GET', 'PUT', 'DELETE'])

if __name__ == '__main__':
  db.create_all()
  app.run(debug=True)

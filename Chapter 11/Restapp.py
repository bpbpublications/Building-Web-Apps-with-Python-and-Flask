from flask import Flask, request, jsonify
from models import app,db, books

@app.route('/books', methods=['GET'])
def allbooks():
    res=books.query.all()
    lb=[]
    for i in res:
        s=i.serialize()
        lb.append(s)    
    return jsonify({"books":lb})

@app.route('/books/<id>', methods=['GET'])
def getbook(id):
    res=books.query.filter_by(bookID=id).first()
    book=res.serialize()
    return jsonify({"book":book})

@app.route('/books',methods=['POST'])
def addbook():
    book = books(request.json['bookID'],request.json['title'],
                           request.json['Author'],
                           request.json['price'])
    db.session.add(book)
    db.session.commit()
    #return redirect(url_for('allbooks'))
    res=books.query.all()
    lb=[]
    for i in res:
        s=i.serialize()
        lb.append(s)    
    return jsonify({"books":lb})

@app.route('/books/<id>',methods=['PUT'])
def updatebook(id):
    id=request.json['bookID']
    price=request.json['price']
    res=books.query.filter_by(bookID=id).first()
    res.price=price
    db.session.commit()
    book=res.serialize()
    return jsonify({'book':book})

@app.route('/books/<id>',methods=['DELETE'])
def deletebook(id):
    res=books.query.filter_by(bookID=id).first()
    db.session.delete(res)
    db.session.commit()
    res=books.query.all()
    lb=[]
    for i in res:
        s=i.serialize()
        lb.append(s)    
    return jsonify({"books":lb})


if __name__ == '__main__':
  db.create_all()
  app.run(debug=True)

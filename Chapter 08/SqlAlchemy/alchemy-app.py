
from flask import Flask, request, flash, url_for, redirect, render_template
from models import app,db, books



@app.route('/')
def show_all():
  return render_template('show_all.html', books=books.query.all()  )

@app.route('/new', methods=['GET', 'POST'])
def new():
  if request.method == 'POST':
    print (request.form)
    book = books(request.form['bookid'],request.form['title'],
                           request.form['category'],
                           request.form['publisher'],
                           request.form['price'])
    db.session.add(book)
    db.session.commit()
    flash('Record was successfully added')
    return redirect(url_for('show_all'))
  return render_template('book.html')

@app.route('/show')
def show():
    id=request.args.get('bookid')
    book=books.query.filter_by(bookID=id).first()
    print (book.title)
    return render_template('show.html', book=book)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method=='POST':
        msg=''
        
        bookid=request.form['bookid']
        ttl=request.form['title']
        ctg=request.form['category']
        pub=request.form['publisher']            
        price=request.form['price']
        print (bookid,ttl,ctg,pub,price)
        try:
            book=books.query.filter_by(bookID=bookid).first()
            book.bookid=request.form['bookid']
            book.title=request.form['title']
            book.category=request.form['category']
            book.publisher=request.form['publisher']            
            book.price=request.form['price']
            db.session.commit()
            flash("Record successfully updated")
        except Exception as e:
            db.session.rollback()
            flash("error in UPDATE operation")
        finally:
            return redirect(url_for('show_all'))
@app.route('/del')
def delrec():
    bookid=request.args.get('bookid')
    try:
            book=books.query.filter_by(bookID=bookid).first()
            db.session.delete(book)
            db.session.commit()
            flash("Record successfully deleted")
    except Exception as e:
            db.session.rollback()
            flash("error in delete operation")
    return redirect(url_for("show_all"))
  
if __name__ == '__main__':
  db.create_all()
  app.run(debug=True)


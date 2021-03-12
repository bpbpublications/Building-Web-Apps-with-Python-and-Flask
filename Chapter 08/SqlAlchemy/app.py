
from flask import Flask, request, flash, url_for, redirect, render_template
from models import app,db, students, books



@app.route('/')
def show_all():
  return render_template('show_all.html', students=students.query.all()  )

@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields', 'error')
        else:
            student = students(request.form['name'],
                               request.form['city'],
                               request.form['addr'],
                               request.form['pin'])
    
            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    
    return render_template('new.html')

@app.route('/books')
def booklist():
  q=db.session.query(books,students)
  rows=q.filter(books.borrower==students.username).all()
  return render_template('showbooks.html', rows=rows)
  
if __name__ == '__main__':
  db.create_all()
  app.run(debug=True)


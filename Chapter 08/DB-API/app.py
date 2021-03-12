from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from encryption import encpwd

app = Flask(__name__)
app.secret_key='1@3$5^7*'
con=sqlite3.connect("mydata.db")
cur=con.cursor()
createqry='''
CREATE TABLE IF NOT EXISTS Students (
Name STRING (20) NOT NULL,
Course STRING (20),
Gender STRING (20),
Mobile INTEGER (10),
Username STRING (6) PRIMARY KEY NOT NULL,
Password TEXT (8) NOT NULL
);
'''
cur.execute(createqry)
    
@app.route('/')
def register():
    return render_template('register.html')

@app.route('/addrec',methods=['POST', 'GET'])
def addrec():
    if request.method=='POST':
        con=sqlite3.connect("mydata.db")
        cur=con.cursor()
        msg=''
        try:
            nm=request.form['name']
            gndr=request.form['gender']
            course=request.form['course']
            mob=request.form['mobile']
            usr=request.form['user']
            pw=request.form['pwd']
            ins="INSERT INTO Students VALUES (?,?,?,?,?,?)"
            cur.execute(ins,(nm,gndr,course,mob,usr,encpwd(pw)) )
            con.commit()
            flash("Record successfully added")
        except Exception as e:
            con.rollback()
            print ("sss",str(e))
            flash("error in insert operation")
    return redirect(url_for("list"))
@app.route('/list')
def list():
    con=sqlite3.connect("mydata.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Students;")
    students=cur.fetchall();
    return render_template("studentlist.html",students=students)
@app.route('/show')
def show():
    user=request.args.get('username')
    con=sqlite3.connect("mydata.db")
    cur = con.cursor()
    cur.execute("select * from Students where username=?",(user,))
    student=cur.fetchone();
    return render_template('show.html', student=student)
@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method=='POST':
        con=sqlite3.connect("mydata.db")
        cur=con.cursor()
        msg=''
        
        nm=request.form['name']
        gndr=request.form['gender']
        course=request.form['course']
        mob=request.form['mobile']
        usr=request.form['User']
        ins="UPDATE students set name=?, Gender=?, Course=?, mobile=?, username=? where username=?"
        try:
            cur.execute(ins,(nm,gndr,course,mob,usr,usr) )
            con.commit()
            msg= "Record successfully updated"
        except Exception as e:
            con.rollback()
            print ("sss",str(e))
            
            msg= "error in UPDATE operation"
        finally:
            return redirect(url_for('list'))
@app.route('/del')
def delrec():
    user=request.args.get('username')
    con=sqlite3.connect("mydata.db")
    cur = con.cursor()
    try:
            cur.execute("DELETE from Students where username=?",(user,))
            con.commit()
            msg= "Record successfully deleted"
    except Exception as e:
            con.rollback()
            print ("sss",str(e))
            
            msg= "error in delete operation"
    print (msg)
    cur.execute("select * from Students;")
    students=cur.fetchall();
    return redirect(url_for("list"))    
    
if __name__ == '__main__':
    app.run(debug=True)

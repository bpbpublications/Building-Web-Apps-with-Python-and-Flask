from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password']=='' or request.form['username']=='':
                flash('User name and password is required', 'error')
                return redirect(url_for('login'))
        if len(request.form['password'])in range(1,9):
                flash('Weak password!', 'warning')
        if request.form['username'] not in ['admin', 'manager', 'supervisor'] :
            flash('You were successfully logged in', 'info')
            return redirect(url_for('success'))
        else:
            flash('User name unavailable', 'error')            
            return redirect(url_for('login'))        
    return render_template('log_in.html')
@app.route('/success')
def success():
    return render_template('success.html')

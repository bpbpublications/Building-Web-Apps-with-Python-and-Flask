from flask import Flask, render_template, request, make_response
from flask import session
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/changebg')
def changebg():
    if 'bgi' in session:
        bgi=session['bgi']
    bgfile= url_for('static', filename=bgi)
    return render_template('changebg.html',bgfile=bgfile)
@app.route("/newbg", methods=['GET', 'POST'])
def newbg():
    if request.method=='POST':
        bgi=request.form['bgi']
        session['bgi']=bgi
        return redirect(url_for('index'))


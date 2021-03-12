from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap
from myform import LoginForm, Registration, AdmissionForm
app = Flask(__name__)
app.secret_key='1!2@3#4$5%'
bs=Bootstrap(app)
@app.route('/login')
def login():
    form=LoginForm()
    return render_template("loginform.html", form=form)
@app.route('/')
def index():
    form = AdmissionForm()
    return render_template("admission.html", form=form)
@app.route('/register', methods=['GET', 'POST'])
def register():
  form = Registration()
 
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('register.html', form=form)
    else:
      return render_template('success.html')
 
  elif request.method == 'GET':
    return render_template('register.html', form=form)
@app.route('/admission', methods=['GET', 'POST'])
def admission():
  form = AdmissionForm()
 
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('admission.html', form=form)
    else:
      return '''
<h1>Form successfully submitted</h1>
<h2>Form Data Received</h2>
<b>Name :{}<br>
DOB : {} <br>
Branch : {}</b>
'''.format(form.student.data, form.dob.data, form.branch.data) 
  elif request.method == 'GET':
    return render_template('admission.html', form=form)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      return render_template('success.html')
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

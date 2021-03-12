from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def form():        
    return render_template('form.html')
@app.route('/upload', methods = ['GET', 'POST'])
def upload():
   if request.method == 'POST':
      f = request.files['file']
      f.save('/uploads'+f.filename)
      return 'file uploaded successfully'

from flask import Blueprint, render_template
engg=Blueprint('engg', __name__,template_folder='templates',static_folder='static')
@engg.route('/')
def index():
    return render_template('engindex.html')
@engg.route('/courses')
def courses():
    return '<h1>list of courses in Enginnering</h1>'
@engg.route('/faculty')
def faculty():
    return '<h1>list of Engineering faculty members</h1>'
@engg.route('/form')
def form():
    return render_template('form.html')

from flask import Flask
app=Flask(__name__)
app.register_blueprint(engg)
if __name__=='__main__':
    app.run(debug=True)

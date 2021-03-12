from flask import Blueprint
mngmnt=Blueprint('mngmnt', __name__)
@mngmnt.route('/courses')
def courses():
    return '<h1>list of courses</h1>'
@mngmnt.route('/faculty')
def faculty():
    return "<h2 align='center'>List of Faculty Members in HiTech Institute of Management</h2>"

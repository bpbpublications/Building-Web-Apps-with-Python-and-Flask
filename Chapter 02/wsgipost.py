from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
import cgi

def app(environ, start_response):
    form=open('register.html')
    html = (form.read()).encode('utf-8')

    if environ['REQUEST_METHOD'] == 'POST':
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        form = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True
        )

        name=form.getvalue('name')
        gender=form.getvalue('gender')
        course=form.getvalue('course')
        mobile=form.getvalue('mobile')
        result=open('regdata.html')
        html=result.read()
        html=(html.format(name=name, gender=gender, course=course, mobile=mobile)).encode('utf-8')
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [html]


httpd = make_server('', 8000, app)
print('Serving on port 8000...')
httpd.serve_forever()
    

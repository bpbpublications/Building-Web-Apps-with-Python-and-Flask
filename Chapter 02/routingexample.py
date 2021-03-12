from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
import fnmatch
def index(environ, start_response):
    start_response("200 OK", [("Content-type", "text/html")])
    f=open('index.html')
    ret = (f.read()).encode('utf-8')
    return [ret]
def register(environment, start_response):
    start_response("200 OK", [("Content-type", "text/html")])
    f=open('registration.html')
    ret = (f.read()).encode('utf-8')
    return [ret]

def loginresult(environ, start_response):
    qry=parse_qs(environ['QUERY_STRING'])
    name=qry.get('name', [''])[0]
    ret=""
    if name!=None:
        pwd=qry.get('pwd',[''])[0]
        if pwd=="1234":
            ret="<h2>Welcome {}</h2>".format(name)
            start_response("200 OK", [("Content-type", "text/html")])
        else:
            ret="<h2>Incorrect password</h2>"
            start_response("404 Not Found", [("Content-type", "text/html")])
    else:
        ret=''
    return [ret.encode('utf-8')]
def regok(environ, start_response):
    ret='''
<h2>You have been successfully registered</h2>
<a href="http://localhost:8000/"><b>Main Menu</b></a>
'''
    start_response("200 OK", [("Content-type", "text/html")])
    return [ret.encode('utf-8')]
def login(environ, start_response):
    f=open('login.html')
    ret = (f.read()).encode('utf-8')
    start_response("200 OK", [("Content-type", "text/html")])
    return [ret]
    
routes=[('/', index),('/register',register), ('/loginresult', loginresult),\
        ('/regok', regok), ('/login', login)]

def application(environ, start_response):
    for path, app in routes: 
        if fnmatch.fnmatch(environ['PATH_INFO'], path): 
            return app(environ, start_response)

server = make_server('localhost', 8000, application)
server.serve_forever()

from wsgiref.validate import validator
from wsgiref.simple_server import make_server

def app(environ, start_response):
    status = '200 OK'  
    headers = [('Content-type', 'text/plain')]  
    start_response(status, headers)

    # application should return a list, but here it is returning string
    return b"Hello World"

wrap_app = validator(app)

with make_server('', 8000, wrap_app) as httpd:
    print("Listening on port 8000....")
    httpd.serve_forever()

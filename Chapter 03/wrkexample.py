from werkzeug.wrappers import Response
from werkzeug.serving import run_simple

def application(environ, start_response):
    response = Response('<h2>Hello World!</h2>', mimetype='text/html')
    return response(environ, start_response)

run_simple('127.0.0.1', 5000, application)

import sys
from werkzeug.wrappers import Response
from jinja2 import Template
name = sys.argv[1]

tm = Template("Hello {{ name }}")
msg = tm.render(name=name)

defapplication(environ, start_response):
    response = Response(msg, mimetype='text/html')
    return response(environ, start_response)

from werkzeug.serving import run_simple
run_simple('127.0.0.1', 5000, application)

from wsgiref.simple_server import make_server

def application(environ, start_response):
    host=environ.get('HTTP_HOST')
    start_response("200 OK", [("Content-type", "text/html")])
    ret = [("<h2>Hello World!<br/> From WSGI Server :%s</h2>" % (host)).encode("utf-8")]
    return ret

server = make_server('localhost', 8000, application)
server.serve_forever()

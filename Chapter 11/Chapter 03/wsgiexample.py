from wsgiref.simple_server import make_server

class Application:
    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])
        ret = ["<h2>Hello World!</h2>".encode("utf-8")]
        return ret

app = Application()

server = make_server('localhost', 8000, app)
server.serve_forever()

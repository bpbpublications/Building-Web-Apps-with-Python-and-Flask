from wsgiref.simple_server import make_server
from urllib.parse import parse_qs

form = '''
<html>
    <head>
        <title>Hello User!</title>
    </head>
    <body>
        <form method="GET" action="">
            <label>Hello</label>
            <input type="text" name="name">
            <input type="submit" name="submit" value="Go">
        </form>
    </body>
</html>
'''

def app(environ, start_response):
    html = form
    
    if environ['REQUEST_METHOD'] == 'GET':
        d = parse_qs(environ['QUERY_STRING'])
        if d.get('submit',[''])[0]=='Go':
    
            user = d.get('name', [''])[0] 
            html = ('<h2>Hello, ' + str(user) + '!</h2>')

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [html.encode('utf-8')]

httpd = make_server('', 8000, app)
print('Serving on port 8000...')
httpd.serve_forever()


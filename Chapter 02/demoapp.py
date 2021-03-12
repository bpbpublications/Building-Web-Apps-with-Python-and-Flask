from wsgiref.simple_server import make_server, demo_app

server = make_server('', 8000, demo_app)
print ("Serving HTTP on port 8000...")

# Respond to requests until process is killed
server.serve_forever()

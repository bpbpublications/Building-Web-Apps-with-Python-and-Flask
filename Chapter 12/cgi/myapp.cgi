#!c:\python37\python.exe
from wsgiref.handlers import CGIHandler
from myapp import app
print("Content-Type: text/html")    
print()
CGIHandler().run(app)

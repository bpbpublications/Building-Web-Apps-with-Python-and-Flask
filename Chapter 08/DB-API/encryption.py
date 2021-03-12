import base64
def encpwd(pwd):
    e=base64.b64encode(pwd.encode('utf-8'))
    secpwd=e.decode('utf-8')
    return secpwd
def decpwd(pwd):
    p1=base64.b64decode(pwd.encode('utf-8'))
    origpwd=p1.decode('utf-8')
    return origpwd

    
    

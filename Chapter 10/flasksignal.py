from flask import Flask, current_app, request
from blinker import Namespace
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = 'qwe123'

nmspc = Namespace()


def test_signal(app, message, **extra):
    logging.debug(message)


test = nmspc.signal('test')
test.connect(test_signal, app)


@app.route('/', methods=['POST', 'GET'])
def home():
    test.send(current_app._get_current_object(), message='Send client IP address : '+request.remote_addr)
    test.send(current_app._get_current_object(), message='send second signal')
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)

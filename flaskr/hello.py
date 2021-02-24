from flask import Flask
app = Flask(__name__)
@app.route('/')
def whatever(env, resp):
    resp('200 OK', [('Content-Type', 'text/plain')])
    return [b'hello, world']

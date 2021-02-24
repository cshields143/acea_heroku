from flask import Flask
app = Flask(__name__)
@app.route('/')
def whatever(*args):
    return 'hello, world'

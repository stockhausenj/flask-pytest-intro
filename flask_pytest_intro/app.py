from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    text = 'Hello, World!'
    resp = app.make_response(text)
    resp.mimetype = "text/plain"
    return resp

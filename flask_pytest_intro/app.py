from flask import Flask, jsonify
import subprocess
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    text = 'Hello, World!'
    resp = app.make_response(text)
    resp.mimetype = "text/plain"
    return resp


@app.route('/lscpu')
def lscpu():
    result = json.loads(subprocess.check_output(["lscpu", "-J"]))
    return jsonify(result)

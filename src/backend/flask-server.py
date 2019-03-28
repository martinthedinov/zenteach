from flask import Flask, request, json, url_for
from dotenv import load_dotenv
import glob
from flask_cors import CORS
import sys
import os

import zlib
import base64

dirname = os.path.dirname(__file__)
app = Flask(__name__)
cors = CORS(app)

# def misc_function(json_result):
#     compressed_json_result = base64.b64encode(zlib.compress(json.dumps(json_result, ensure_ascii=False).encode('utf-8')))
#     return compressed_json_result

@app.route('/list_class')
def list_class():
    class_data = request.args.get('class_name')
    return (json.jsonify(class_data))

@app.route('/get_quiz')
def list_class():
    quiz_data = request.args.get('quiz_name')
    return (json.jsonify(quiz_data))

@app.route("/")
def site_map():
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    # links is now a list of url, endpoint tuples
    return(json.jsonify(links))
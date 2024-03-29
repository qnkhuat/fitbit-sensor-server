from flask import Flask, jsonify, make_response, request, abort, redirect
import logging
import base64
import json
import time
import traceback
import os

app = Flask(__name__)

@app.route('/api/json', methods=['GET', 'POST', 'DELETE', 'PUT'])
def add():
    os.makedirs("data/", exist_ok = True)
    sensor = request.args.get('sensor')
    time = request.args.get('time')
    filename = f"data/{sensor}_{time}.json"
    data = request.json
    with open(filename, 'w') as f : 
        json.dump(data, f, indent=4)
    return jsonify(data)

@app.errorhandler(400)
def bad_request(error):
    print(error)
    return make_response(jsonify({'message': 'We cannot process the file sent in the request.'}), 400)

@app.errorhandler(404)
def not_found(error):
    print(error)
    return make_response(jsonify({'message': 'Resource not found.'}), 404)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

# app.py
from flask import Flask, request, jsonify
import os
app = Flask(__name__)

@app.route('/auth/face-verify/', methods=['POST'])
def respond():

    response = {}

    response["isFaceVerified"] = True
    # Return the response in json format
    return jsonify(response)

@app.route('/auth/audio-verify/', methods=['POST'])
def post_something():

    response = {}

    response["isAudioVerified"] = True
    # Return the response in json format
    return jsonify(response)

@app.route('/')
def index():
    return "<h1>Welcome to TutoringBrains !!</h1>"

if __name__ == '__main__':
    port = int(os.getenv('PORT') or 5000)
    app.run(threaded=True, port=port)
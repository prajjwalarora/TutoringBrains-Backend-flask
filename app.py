# app.py
import re
from flask import Flask, request, jsonify,make_response
# from face import face_recog
from flask_cors import CORS
from audio import audio_recog
import os
app = Flask(__name__)
CORS(app)
@app.route('/auth/face-verify/', methods=['POST', "OPTIONS"])
def face_verify():
    if request.method == "OPTIONS": 
        return _build_cors_preflight_response()
    else:
        reqBody = request.get_json()
    # userImg =reqBody["userImg"]
    # verifyImg =reqBody["verifyImg"]
    # result = face_recog(userImg,verifyImg)
    # Return the response in json format
        return _corsify_actual_response(jsonify(reqBody))

@app.route('/auth/audio-verify/', methods=['POST',"OPTIONS"])
def audio_verify():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    else:
        reqBody = request.get_json();
        userAudio =reqBody["userAudio"]
        result = audio_recog(userAudio)
        return _corsify_actual_response(jsonify(result))

def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/')
def index():
    return "<h1>Welcome to TutoringBrains !!</h1>"

if __name__ == '__main__':
    port = int(os.getenv('PORT') or 5000)
    app.run(threaded=True, port=port)
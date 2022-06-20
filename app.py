# app.py
import re
from flask import Flask, request, jsonify
# from face import face_recog
from audio import audio_recog
import os
app = Flask(__name__)

@app.route('/auth/face-verify/', methods=['POST'])
def face_verify():
    reqBody = request.get_json();
    # userImg =reqBody["userImg"]
    # verifyImg =reqBody["verifyImg"]
    # result = face_recog(userImg,verifyImg)
    # Return the response in json format
    return jsonify(reqBody)

@app.route('/auth/audio-verify/', methods=['POST'])
def audio_verify():
    
    reqBody = request.get_json();
    userAudio =reqBody["userAudio"]
    result = audio_recog(userAudio)
    
    #print(message)
    #response = {}

    #response["isAudioVerified"] = True
    # Return the response in json format
    return jsonify(result)

@app.route('/')
def index():
    return "<h1>Welcome to TutoringBrains !!</h1>"

if __name__ == '__main__':
    port = int(os.getenv('PORT') or 5000)
    app.run(threaded=True, port=port)
import speech_recognition as sr
import base64
def audio_recog(userAudio):
    
    r = sr.Recognizer()
    response = {}
    response["isValid"] = True
    with sr.AudioFile("audio.wav") as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        response["text"] = text
    except:
        print("PLease speak it again")
        response["isValid"] = True
    base64_message = userAudio
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii') 
    response["text"] = message
    return response
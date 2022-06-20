import speech_recognition as sr
def audio_recog(userAudio):
    
    r = sr.Recognizer()
    response = {}
    response["isValid"] = True
    with sr.AudioFile(userAudio) as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        response["text"] = text
    except:
        response["isValid"] = False
        
    return response
import speech_recognition as sr
def audio_recog(userAudio):
    r = sr.Recognizer()
    response = {}
    response["isValid"] = True
    with sr.AudioFile(userAudio) as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("\n")
        print("Wait the file is processsing !!!!!! \n")
        print("Converting the Mp3 file: ",text)
        response["text"] = text
    except:
        print("PLease speak it again")
        response["isValid"] = False
        
    return response
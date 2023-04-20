# module to convert text to voice and vice versa 

import pyttsx3
import speech_recognition as sr


# initialising text to voice engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# defining functions for the assistant

def speak(sentence):
    engine.say(sentence)
    engine.runAndWait()

def getCommand():

    command = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        # command.pause_threshold = 1
        audio = command.listen(source)

    try:
        ##
        ##  add this to smart mirror ui somehow
        ##
        print("Computing...")
        query = command.recognize_google(audio)

        # remove after testing 
        print("user said: {query} \n")

    except Exception as error:
        ##
        ##  add this to smart mirror ui somehow
        ##
        print(error)
        print("Unable to compute")
    
    return query 





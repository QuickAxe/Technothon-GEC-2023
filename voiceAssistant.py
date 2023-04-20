import wolframalpha
import pyttsx3
import speech_recognition as sr
import datetime


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
        command.pause_threshold = 1
        audio = command.listen(source)

    try:
        ##
        ##  add this to smart mirror ui somehow
        ##
        print("Computing...")
        query = command.recognise_google(audio, language = 'en-in')

        # remove after testing 
        print("user said: {query} \n")

    except Exception as error:
        ##
        ##  add this to smart mirror ui somehow
        ##
        print(error)
        print("Unable to compute")
    
    return query 





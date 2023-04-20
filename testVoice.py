import voiceAssistant as vs 

query = vs.getCommand().lower()

print(query)

vs.speak(query)

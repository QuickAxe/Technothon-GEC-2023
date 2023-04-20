## For testing only 

import voiceParser as vs 

query = vs.getCommand().lower()

print(query)

vs.speak(query)

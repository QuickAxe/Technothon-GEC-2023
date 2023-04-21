## For testing only 

import voiceParser as vs 
import news 

query = news.getNews()


for words in query["articles"]:
    vs.speak(words)

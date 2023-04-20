# returns news in a json file, in this format, under "articles"
# 
# {
#     "source" : "..."
#     "author" : "...",
#     "title" : "...",
#     "description" : "...",
#     "url" : "...",
#     "urlToImage" : "...",
#     "publishedAt" : "...",
# }

import json
import requests 
from urllib.request import urlopen
import voiceParser as vp

def getNews():

    #"apiKey" : "a43bbf8815e84611860412499d7710ac"
    # fetching data in a json file
    res = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=a43bbf8815e84611860412499d7710ac")
    data = res.json()

    return data

print(json.dumps(getNews()))

           

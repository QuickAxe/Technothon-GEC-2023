# returns news in a json file, in this format, under "articles"
# 
# {
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

    queryParams = {
        "source" : "bbc-news",
        "sortBy" : "top",
        "apiKey" : "a43bbf8815e84611860412499d7710ac"
    }

    mainUrl = "https://newsapi.org/v1/articles"

    # fetching data in a json file
    res = requests.get(mainUrl, params = queryParams)

    data = res.json()

    return data

           
      
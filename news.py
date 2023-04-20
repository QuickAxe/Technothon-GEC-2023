# returns news as a python dictionary, in this format, under "articles", as an array
# 
# {
#     "source" : "..."
#     "author" : "...",
#     "title" : "...",
#     "description" : "...",
#     "url" : "...",
#     "urlToImage" : "...",
#     "publishedAt" : "...",
#     "content" : "... too big, ignore...."
# }

import json
import requests 
from urllib.request import urlopen

def getNews():

    #"apiKey" : "a43bbf8815e84611860412499d7710ac"
    # fetching data in a json file
    res = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=a43bbf8815e84611860412499d7710ac")
    data = res.json()

    return data



           

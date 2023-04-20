import json
import requests 
from urllib.request import urlopen
import voiceParser as vp


queryParams = {
    "source" : "bbc-news",
    "sortBy" : "top",
    "apiKey" : "a43bbf8815e84611860412499d7710ac"
}

mainUrl = "https://newsapi.org/v1/articles"

# fetching data in a json file
res = requests.get(mainUrl, params = queryParams)

data = res.json()
i = 1
             
vp.speak('here is some top news from BBC news')
print('''=============== BBC ============'''+ '\n')
                
for item in data['articles']:
    print(str(i) + '. ' + item['title'] + '\n')
    print(item['description'] + '\n')
    vp.speak(str(i) + '. ' + item['title'] + '\n')
    i += 1                    
                    
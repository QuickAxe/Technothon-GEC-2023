# module to find what news the user wants and suggest news accordingly 
# input the description of the news to the recommendedNews() function
#######################################################################
#  WARNING 
## !! its boud to run out of bouds at some point, correct at some point 

from nltk.tokenize import word_tokenize 
from nltk.probability import FreqDist
from nltk.corpus import stopwords

import json
import heapq


def recommendedNews(news):
   
    f = open('database.json', "+r")
    data = json.load(f)
    
    wordTokens = word_tokenize(news)

    # removing stopwords(words that are not tokens, like "the", "a", "is"...)

    stopWords = (stopwords.words("English"))

    filteredTokens = []

    for sw in wordTokens :
        if sw not in stopWords and (sw != ',' or sw != '.' or sw != '...' or sw != "'" or sw != '"' or sw != '$'):
            filteredTokens.append(sw)
    
    # creating a frequency distribution of the 10 most common words 

    keyWords = FreqDist(filteredTokens)
    tokens = keyWords.most_common(10)

    touple = []
    
    for words in tokens:
        if(words[0] in data["userNewsLikings"]) : 
            data["userNewsLikings"][words[0]] += 1

        else :        
            data["userNewsLikings"][words[0]] =  1

    touple = [(int(data["userNewsLikings"][key]), key) for key in data["userNewsLikings"]]

    heapq._heapify_max(touple)

    formattedData = dict()
    
    for i, word in touple:
        formattedData[word] =i 
    
    data["userNewsLikings"] = formattedData

    f.seek(0)
    json.dump(data, f)
    f.truncate()

    






# module to find what news the user wants and suggest news accordingly 
# input the description of the news to the recommendedNews() function 

from nltk.tokenize import word_tokenize 
from nltk.probability import FreqDist
from nltk.corpus import stopwords

import json


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

    #print(tokens)
    
    for item in data["userNewsLikings"] :
       for key, value in tokens :
             if(value == item):
                




    






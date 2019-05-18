from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

#TODO find the way how to handle "don't", "can't" ...
#TODO make lammetization work better -> https://www.machinelearningplus.com/nlp/lemmatization-examples-python/

def tweet_to_wordlist(tweet, remove_stopwords=False):
    """
       Function to convert a document to a sequence of words.
       
       Returns a list of words  
    """

    # 1. Remove HTML
    tweet_text = BeautifulSoup(tweet,"lxml").get_text()

    # 2. Remove of URLs
    tweet_text = re.sub(r"http\S+", "", tweet_text)
    
    # 3. Remove of mentions
    tweet_text = re.sub("@[^\s]*", "", tweet_text)

    # 4. Remove non-letters        
    tweet_text = re.sub("[^a-zA-Z]", " ", tweet_text) 

    # Convert to lower case, split into individual words
    words = tweet_text.lower().split()                             
                
    # 5. Optionally Remove stop words
    if remove_stopwords:
        stops = set(stopwords.words("english"))  
        words = [w for w in words if not w in stops]   

    # 6. Word lemmatization
    lemmatizer = WordNetLemmatizer()
    
    count = 0
    for word in words:
        words[count] = lemmatizer.lemmatize(word, pos="v")
        count += 1
 
    # Return a list of words
    return words

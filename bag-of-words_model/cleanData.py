from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def twitts_to_words(tweet):
    """
       Function to convert a raw review to a string of words
       The input is a single string (a raw movie review), and 
       the output is a single string (a preprocessed movie review)        
    """

    # 1. Remove HTML
    tweet_text = BeautifulSoup(tweet, "lxml").get_text()

    # 2. Remove of URLs
    tweet_text = re.sub(r"http\S+", "", tweet_text)
    
    # 3. Remove of mentions
    tweet_text = re.sub("@[^\s]*", "", tweet_text)

    # 4. Remove non-letters        
    letters_only = re.sub("[^a-zA-Z]", " ", tweet_text)
    
    # 5. Remove 2-char-length words cause literally no meaning
    letters_only = re.sub(r'\b\w{1,2}\b', '', letters_only)

    # Convert to lower case, split into individual words
    words = letters_only.lower().split()                             

    # Convert stopwords to set type for speading
    stops = set(stopwords.words("english"))                  

    # 6. Remove stop words
    meaningful_words = [w for w in words if not w in stops]   
  
    # 7. Word lemmatization  --> process of grouping together the different 
    #    inflected forms of a word so they can be analysed as a single item
    lemmatizer = WordNetLemmatizer()
    return " ".join([lemmatizer.lemmatize(word) for word in meaningful_words])

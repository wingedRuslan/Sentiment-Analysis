import pandas as pd
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords

# to train Word2Vec it is better not to remove stop words because the algorithm relies on the broader context of the sentence in order to produce high-quality word vectors.

def review_to_wordlist(review, remove_stopwords=False):
    """
       Function to convert a document to a sequence of words.
       
       Returns a list of words  
    """

    # 1. Remove HTML
    review_text = BeautifulSoup(review,"lxml").get_text()

    # 2. Remove non-letters        
    review_text = re.sub("[^a-zA-Z]", " ", review_text) 

    # Convert to lower case, split into individual words
    words = review_text.lower().split()                             
                
    # 3. Optionally Remove stop words
    if remove_stopwords:
            stops = set(stopwords.words("english"))  
            words = [w for w in words if not w in stops]   
 
    # Return a list of words
    return words

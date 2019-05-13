import pandas as pd
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords

def twitts_to_words(raw_review):
    """
       Function to convert a raw review to a string of words
       The input is a single string (a raw movie review), and 
       the output is a single string (a preprocessed movie review)        
    """

    # 1. Remove HTML
    review_text = BeautifulSoup(raw_review,"lxml").get_text()

    # 2. Remove non-letters        
    letters_only = re.sub("[^a-zA-Z]", " ", review_text) 

    # Convert to lower case, split into individual words
    words = letters_only.lower().split()                             

    # Convert stopwords to set type for speading
    stops = set(stopwords.words("english"))                  

    # 3. Remove stop words
    meaningful_words = [w for w in words if not w in stops]   
  
    # Join the words back into one string separated by space, 
    # Return the result.
    return( " ".join(meaningful_words))  

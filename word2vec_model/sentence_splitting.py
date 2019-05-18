import nltk
from cleanData_word2vec import tweet_to_wordlist

def tweet_to_sentences(tweet, tokenizer, remove_stopwords=False):
    """
    Function to split a tweet into parsed sentences. 
    Returns a list of sentences, where each sentence is a list of words
    """

    # 1. Use the NLTK tokenizer to split the paragraph into sentences
    raw_sentences = tokenizer.tokenize(tweet.strip())
    
    # 2. Loop over each sentence
    sentences = []
    for raw_sentence in raw_sentences:
        # If a sentence is empty, skip it
        if len(raw_sentence) > 0:
            # Otherwise, call review_to_wordlist to get a list of words
            sentences.append(tweet_to_wordlist(raw_sentence,remove_stopwords))
 
    # Return a list of sentences (each sentence is a list of words)
    return sentences

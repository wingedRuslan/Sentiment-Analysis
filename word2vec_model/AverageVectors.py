import numpy as np

def makeFeatureVec(words, model, num_features):
    """
        Function to average all of the word vectors in a given
        paragraph
    """
   
    # Pre-initialize an empty numpy array
    featureVec = np.zeros((num_features,),dtype="float32")
   
    nwords = 0.
     
    # Index2word is a list that contains the names of the words in 
    # the model's vocabulary. Convert it to a set, for speed 
    index2word_set = set(model.wv.index2word)
    
    # Loop over each word in the review and, if it is in the model's
    # vocaublary, add its feature vector to the total
    for word in words:
        if word in index2word_set: 
            nwords = nwords + 1.
            featureVec = np.add(featureVec,model[word])
     
    # Divide the result by the number of words to get the average
    featureVec = np.divide(featureVec,nwords)
    return featureVec


def getAvgFeatureVecs(tweets, model, num_features):
    """
        Given a set of tweets (each one a list of words), calculate 
          the average feature vector for each one and return a 2D numpy array 
    
    """
     
    # Initialize a counter
    counter = 0.
    
    # Preallocate a 2D numpy array, for speed
    tweetFeatureVecs = np.zeros((len(tweets),num_features),dtype="float32")
    
    for tweet in tweets:
        # Print a status message every 1000th review
        #if (counter%1000. == 0.):
        #    print("Review {} of {}".format(counter, len(tweets)))
     
        # Makes average feature vectors
        tweetFeatureVecs[int(counter)] = makeFeatureVec(tweet, model, num_features)
        
        counter = counter + 1.
    
    return tweetFeatureVecs

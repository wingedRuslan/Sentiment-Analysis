
def create_bag_of_centroids(wordlist, word_centroid_map):
    """
        a function to create bags of centroids
    """
    
    # The number of clusters is equal to the highest cluster index in the word / centroid map
    num_centroids = max( word_centroid_map.values() ) + 1
    
    # Pre-allocate the bag of centroids vector (for speed)
    bag_of_centroids = np.zeros(num_centroids, dtype="float32")
    
    # Loop over the words in the tweet. If the word is in the vocabulary,
    # find which cluster it belongs to, and increment that cluster count by one
    for word in wordlist:
        if word in word_centroid_map:
            index = word_centroid_map[word]
            bag_of_centroids[index] += 1
    
    # Return numpy array
    return bag_of_centroids

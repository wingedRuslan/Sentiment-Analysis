import os
from twython import Twython
from twython import TwythonAuthError, TwythonError, TwythonRateLimitError

def search_hashtag(hashtag, count=100):
    """Return list of most recent tweets with the hashtag"""

    # ensure count is valid
    if count < 1 or count > 100:
        raise RuntimeError("invalid count")

    # ensure environment variables are set
    if not os.environ.get("API_KEY"):
        raise RuntimeError("API_KEY not set")
    if not os.environ.get("API_SECRET"):
        raise RuntimeError("API_SECRET not set")

    try:
        twitter = Twython(os.environ.get("API_KEY"), os.environ.get("API_SECRET"))
        try:
            search_results = twitter.search(q=hashtag, count=3)
            return search_results
        except TwythonError as e:
            raise e
    except TwythonAuthError:
        raise RuntimeError("invalid API_KEY and/or API_SECRET") from None
    except TwythonRateLimitError:
        raise RuntimeError("you've hit a rate limit") from None
    except TwythonError:
        return None


def main():
    hashtag = "csvconf"
    search_results = search_hashtag(hashtag)
    
    print(search_results)
    print("==============================")
    print(search_results['statuses'])
    print("==============================")
    

    for tweet in search_results['statuses']:
        print("Tweet from @{} Date: {}".format(tweet['user']['screen_name'].encode('utf-8'),tweet['created_at']))
        print(tweet['text'].encode('utf-8'))

        
if __name__ == "__main__":
    main()

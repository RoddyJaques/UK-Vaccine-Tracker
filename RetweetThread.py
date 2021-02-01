import tweepy_auth

if __name__ == "__main__":
    api = tweepy_auth.twitter_api()

    with open("tweet_id.txt","r") as tweet_id:
        RetweetId = tweet_id.read()

    api.retweet(RetweetId)
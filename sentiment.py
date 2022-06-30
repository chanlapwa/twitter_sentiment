import tweepy
import keys
from textblob import TextBlob

try:
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.token_secret)
    tweets_api = tweepy.API(auth)
except:
    print("Error: Authentication Failed")

tweets = tweets_api.search_tweets(q = "job", count = "100", lang = "en", result_type = "popular")

for tweet in tweets:
    # tweet_dict = {}
    # tweet_dict["name"] = tweet.user.name
    # tweet_dict["location"] = tweet.user.location
    # tweet_dict["followers"] = tweet.user.followers_count

    if (tweet.user.followers_count > 100000):
        print(tweet.user.name)
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)

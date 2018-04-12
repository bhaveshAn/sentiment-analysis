import tweepy
from textblob import TextBlob

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

query = str(input("Enter a key to search Tweets: "))
public_tweets = api.search(query)

for tweet in public_tweets:
    print(tweet)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    

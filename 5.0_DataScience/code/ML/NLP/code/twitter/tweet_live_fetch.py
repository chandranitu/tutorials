from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

import twitter_credentials

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"]
        print(tweet)
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["portugal"])
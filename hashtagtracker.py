#credit to Marco Bonzanini for his python mining tutorials- 
#https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/

from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler

consumer_key = 'consumerkey'
consumer_secret = 'consumersecret'
access_token = 'accesstoken'
access_secret = 'accesssecret'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('./programdata/python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            #print(Error on_data: %s&quot; % str(e))
            print("error"+str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#thetweet']) #put in whatever tweet you're looking for 

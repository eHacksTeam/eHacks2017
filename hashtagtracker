from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler

consumer_key = 'am7XecLTFWFz2lb7HSCVDN6OH'
consumer_secret = 'zKnIYzqzWwixVXffBro9uHUS3V1HaUz9U43px3s3A5lLE3JW33'
access_token = '2159929704-6aIhGqJRdpkOuTYKI3zEQlQZzXUO0dl931uXYbP'
access_secret = 'K5j8jFl0w09RIlp5FRMdUMq7c2CW6mDdNqxck1VYwkRFv'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
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
twitter_stream.filter(track=['#Trump'])

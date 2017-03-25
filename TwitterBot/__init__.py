import tweepy

# !/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

argfile = "input.txt"

# enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'fcThscxsJM0QI4myazCTjPIRc'  # keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'BWZQA7NmZA6Ypf8ptIN6MIa1deSX8W4hVj8PlhnjIEjasTCNio'  # keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '845541669370023936-RFA65KEuv8cO3Xt0Ek9rJEkXrKCyu2a'  # keep the quotes, replace this with your access token
ACCESS_SECRET = 'aMRRjxU1ExVceX40fFN9lGOiJkCIzBqx1YPwL0ZG5Cjox'  # keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open(argfile, 'r')
f = filename.readlines()
filename.close()


while True:
    for line in f:
        print(line)
        results = api.search(q=str(line))
        for tweet in results:
            api.retweet(tweet.id)
            # time.sleep(900)  # Tweet every 15 minutes

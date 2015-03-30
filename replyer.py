#!/usr/bin/env python
import tweepy
#from our keys module (keys.py), import the keys dictionary


CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''



 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
 
twts = api.search(q="Hello World!")     
 
#list of specific strings we want to check for in Tweets
t = ['Hello world!',
    'Hello World!',
    'Hello World!!!',
    'Hello world!!!',
    'Hello, world!',
    'Hello, World!']
 
for s in twt:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "@%s Hello!" % (sn)
            s = api.update_status(m, s.id)

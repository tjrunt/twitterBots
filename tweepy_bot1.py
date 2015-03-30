#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

#rgfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = ''#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = ''#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = ''#keep the quotes, replace this with your access token
ACCESS_SECRET = ''#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
#
##
###
#### format text and check for max character length
###
##
#
#filename=open("positive_text.txt",'r')


filename=open("Rime.txt",'r')
# 

f=filename.readlines()
filename.close()

for line in f:
    try:
        api.update_status(status=line)
        #time.sleep(900)#Tweet every 15 minutes
        time.sleep(10)#Tweet every ?? minutes
        #print(len(line))
    except:
        print('error for this text: ', line)
        pass





#myFollowers = api.followers('')



user = api.me()
print(user.name, user.location, user.friends_count)

#toFollow = user.followers()


otherUser = api.get_user('@fart_robot')
ou2 = api.get_user('@ColumbiaYC')
#ou2.follow()
#ou2.unfollow()


#follow followers
ee =tweepy.Cursor(api.followers).items()
userNames= []
for i in ee:
    userNames.append(i.screen_name)
 

# gets followers and follow or unfollow them
for i in userNames:
    print('@'+ i)
    toFollow = api.get_user('@'+ i)
    #toFollow.unfollow()
    toFollow.follow()


## gets a user then statue info then most recent post
getUser = api.get_user(userNames[0])
getStatus = getUser.status
getPost = getStatus.text
getPostId= getStatus.id

## retweet
#api.retweet(getPostId)



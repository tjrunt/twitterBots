#! /usr/bin/python
import tweepy
#from keys import keys

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)



#myFollowers = api.followers()




##for follower in tweepy.Cursor(api.followers).items():
##    #follower.follow()
##    print (follower.screen_name)





##
##followers = []
##for follower in tweepy.Cursor(api.followers).items():
##    followers.append(follower)
##
##friends = []
##for friend in tweepy.Cursor(api.friends).items():
##    friends.append(friend)
##
##print ("Stats for %s:" % username)
##print ("%d following" % len(friends))
##print ("%d followers" % len(followers))
##print ("...")
##
### creating dictionaries based on id's is handy too
##
##friend_dict = {}
##for friend in friends:
##    friend_dict[friend.id] = friend
##
##follower_dict = {}
##for follower in followers:
##    follower_dict[follower.id] = follower
##
### now we find all your "non_friends" - people who don't follow you
### even though you follow them.
##
##non_friends = [friend for friend in friends if friend.id not in follower_dict]
##
### double check, since this could be a rather traumatic operation.
##
##print ("Here are the %s people who don't follow you back" % len(non_friends))
##
### actually start the removal process. In the event of a failure (thanks,
### twitter), retry once after five seconds. An error on same record again
### is probably more serious issue, exit and error occurs
##
##for nf in non_friends:
##    print (nf.screen_name)

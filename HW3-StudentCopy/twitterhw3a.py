# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy

# Unique code from Twitter
access_token = "1454475356-onACrHpDMComjV1rB3oGRtp77JwJKtnupsu44MR"
access_token_secret = ""
consumer_key = "6ftTHfh9nKAARv162a0p3NnAd"
consumer_secret = ""

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

try:
	twitter = tweepy.API(auth)
	img = "media/um.jpg"
	tweet = twitter.update_with_media(img, status="#UMSI-206 #Proj3")
	print ("Your tweet has been posted.")
except:
	print ("Your tweet was not posted. Please edit your post and try again.")

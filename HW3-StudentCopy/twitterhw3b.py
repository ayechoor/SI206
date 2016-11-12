# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.
import tweepy
from textblob import TextBlob
import re

# Unique code from Twitter
access_token = "1454475356-onACrHpDMComjV1rB3oGRtp77JwJKtnupsu44MR"
access_token_secret = "NeiVkWMj7vkEpbHRdikQvVAA9McxVDIbl9qwOfMPEtndQ"
consumer_key = "6ftTHfh9nKAARv162a0p3NnAd"
consumer_secret = "o1sY41Ku4CrdpqvHfqUBRgATua179GsuTnuNUbMki4LBOXCWGV"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

polarity=[]
subjectivity=[]

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	polarity.append(analysis.sentiment.polarity)
	subjectivity.append(analysis.sentiment.subjectivity)

avg_polarity = sum(polarity)/len(polarity)
avg_subjectivity = sum(subjectivity)/len(subjectivity)

print ()
print("Average polarity is", avg_polarity)
print("Average subjectivity is", avg_subjectivity)

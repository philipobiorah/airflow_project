#import packages

import tweepy
import pandas as pandas
import json
from datetime import datetime
import s3fs
import os
from dotenv import load_dotenv


#Access keys

# Load environment variables from .env file
load_dotenv()

access_key = os.environ.get('TWEEPY_ACCESS_KEY')
access_secret = os.environ.get('TWEEPY_ACCESS_SECRET')
consumer_key = os.environ.get('TWEEPY_CONSUMER_KEY')
consumer_secret = os.environ.get('TWEEPY_CONSUMER_SECRET')



#Twitter authentication
# auth = tweepy.OAuthHandler(access_key, access_secret)
auth = tweepy.OAuthHandler(access_key,access_secret)
auth.set_access_token(consumer_key, consumer_secret)

#Creating an API object
api = tweepy.API(auth)

# Get user information for @elonmusk
user = api.get_user(screen_name="philipobiorah")

# Print some details
print(f"User: {user.name}")
print(f"Twitter ID: {user.id}")
print(f"Location: {user.location}")
print(f"Description: {user.description}")
print(f"Followers: {user.followers_count}")
print(f"Following: {user.friends_count}")
print(f"Total Tweets: {user.statuses_count}")

#API.user_timeline(*, user_id, screen_name, since_id,
   # count, max_id, trim_user, exclude_replies, include_rts)

# tweets = api.user_timeline(screen_name='@elonmusk', 
#                            count=20,
#                            include_rts = False,
#                            tweet_mode= 'extended')



# print(tweets)
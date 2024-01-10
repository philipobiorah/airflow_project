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




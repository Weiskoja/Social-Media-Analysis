import tweepy
import json
import os
import sqlite3
from secrets import jbw_keychain, umich_keychain
import constants


def hashtag_tweets():
    return None
def important_location_tweets():
    return None
def opponent_tweets(twitter_handler, opposing_schools_list = "default to predefined list"):
    #gets recent tweets from opposing schools, sends to ingest to write to opposing school tables
    #iterate thru list of names, using names as keys to dictionary for link to official twitter
    return None


#relevant fields for tweet objects: non_public_metrics,organic_metrics,public_metrics
# add media field parameter to get type of tweet (i.e. video, image, etc) (media_fields: type)

#tweepy client object handler   
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)


def create_client(keychain):
    client = tweepy.client(
        bearer_token = keychain.BEARER_TOKEN, 
        consumer_key= keychain.CONSUMER_KEY, consumer_secret = keychain.CONSUMER_SECRET,
        access_token = keychain.ACCESS_TOKEN, access_token_secret = keychain.ACCESS_TOKEN_SECRET
        )

    return client
personal_client = create_client(jbw_keychain)

def get_new_tweets(accounts):
    for opponent in constants.OPPONENT_DIRECTORY:
        personal_client.client.get_users_tweets(opponent.id,)
   

#get_new_tweets



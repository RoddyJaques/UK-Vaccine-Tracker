import tweepy
import requests
import os

def twitter_api():
    twitter_auth_keys = { 
        "consumer_key"        : "XXXXXXXXXXXXXX",
        "consumer_secret"     : "XXXXXXXXXXXXXXXXXXXXXXX",
        "access_token"        : "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "access_token_secret" : "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    }
 
    auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
            )
    auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )
    api = tweepy.API(auth)
    return api

import tweepy
import requests
import os

def twitter_api():
    twitter_auth_keys = { 
        "consumer_key"        : "bOdgOZG0DDgwcIPlToEVtkPVn",
        "consumer_secret"     : "4xThryNVL2TiKv8xEYgfUXtXZelNTrhCQ493lsTOoWBjdrOvJU",
        "access_token"        : "1350801847150374912-oYSYCqjFX2IsGyDawqUWNdPqVnSFHx",
        "access_token_secret" : "vdM5m8cjLjkKreSs3f7F2zYB2FKDRmW70RQRBf4kwUACH"
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

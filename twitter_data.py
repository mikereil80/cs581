#   Author: Cheryl Dugas

#  This program accesses data from a twitter user site (hard-coded as Stevens)

#  To run in a terminal window:   python3  twitter_data.py

# Michael Reilly
# I pledge my honor that I have abided by the Stevens Honor System.


import tweepy

### PUT AUTHENTICATOIN KEYS HERE ###
CONSUMER_KEY = "qHL6Di3m3bxh2EGRuMsMr24JO"
CONSUMER_KEY_SECRET = "E1xr35Ps1hOe5Sa34uV6bS64tRAqRRFWwhprIwhZusbGg9kmhV"
ACCESS_TOKEN = "1325961820738347008-Yk45ckkwOTKIZZJAixoOULTRPG36f0"
ACCESS_TOKEN_SECRET = "qGMQekJKTOHtb0qd0ENsAmPn01UIsnsmc2ZOg0YKCCUun"

# Authentication

authenticate = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
authenticate.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#  use wait_on_rate_limit to avoid going over Twitter's rate limits
api = tweepy.API(authenticate, wait_on_rate_limit=True, 
                 wait_on_rate_limit_notify=True)
                 
# Get Information About a Twitter User Account

twitter_user = api.get_user('FollowStevens')

# Get Basic Account Information
print("twitter_user id: ", twitter_user.id)

print("twitter_user name: ", twitter_user.name)

# Determine an Account’s Friends 
friends = []

print("\nFirst 5 friends:")

# Creating a Cursor
cursor = tweepy.Cursor(api.friends, screen_name='FollowStevens')

# Get and print 5 friends
for account in cursor.items(5):
    print(account.screen_name)
    
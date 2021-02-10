#   Author: Michael Reilly

#  This program accesses data from a twitter user site (hard-coded as Stevens)

#  To run in a terminal window:   python3  Reilly_HW7.py

# Runs the code and enters the while loop afer authenticating the developer account.
# Then from there infinitely loops as the user gives screen names until "STOP" is called.
# If the user does not enter "STOP", the code gets information such as user name, ID, location
# As well as information about their most recent followers and five most recent tweets. 
# Entering "STOP" as the screen name ends code execution.

# This code is based on the original twitter_data.py file given to us, just modified

# Michael Reilly
# I pledge my honor that I have abided by the Stevens Honor System.


import tweepy

### PUT AUTHENTICATOIN KEYS HERE ###
CONSUMER_KEY = "qHL6Di3m3bxh2EGRuMsMr24JO"
CONSUMER_KEY_SECRET = "E1xr35Ps1hOe5Sa34uV6bS64tRAqRRFWwhprIwhZusbGg9kmhV"
ACCESS_TOKEN = "1325961820738347008-Yk45ckkwOTKIZZJAixoOULTRPG36f0"
ACCESS_TOKEN_SECRET = "qGMQekJKTOHtb0qd0ENsAmPn01UIsnsmc2ZOg0YKCCUun"

# Every part of the code before the while True statement is code from twitter_data.py
# Authentication
authenticate = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
authenticate.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#  use wait_on_rate_limit to avoid going over Twitter's rate limits
api = tweepy.API(authenticate, wait_on_rate_limit=True, 
                wait_on_rate_limit_notify=True)

while True:
        
    # The call for string input of User Screen Name
    screenName=input("Input Twitter User Screen Name: ")
    if screenName=="STOP":
        # Will only occur if STOP is entered
        print("Stop Execution.")
        break

    # Get Information About a Twitter User Account

    twitter_user = api.get_user(screenName)

    # Get Basic Account Information
    # This is all retrieved as a User Object with the get_user function
    print("User Screen Name: ", screenName)

    print("User Name: ", twitter_user.name)

    print("User ID: ", twitter_user.id)

    print("User Description: ", twitter_user.description)

    print("Location: ", twitter_user.location)

    print("Number of Friends: ", str(twitter_user.friends_count))

    print("Number of Followers: ", str(twitter_user.followers_count))

    # a counter to make sure we only print the 5 most recent followers
    count_followers=0
    print("\n5 most recent followers: ")
    # api.followers gets the 20 most recent user's followers, so we will get the most recent five from here
    for follower in api.followers(screenName):
        # new line for each follower for readability
        print(follower.screen_name)
        count_followers+=1
        # the check for only up to five followers
        if count_followers>=5:
            break
    
    print("\n")

    # a counter to make sure we only print out the 5 most recent tweets
    count_status=0
    # api.user_timeline gets the 20 most recent user's statuses, so we will get the most recent five from here
    for status in tweepy.Cursor(api.user_timeline, screen_name=screenName).items():
        count_status+=1
        # Print Statement according to the assignment guidelines of Tweet N: {text} \n
        print("Tweet ", str(count_status), ": ", status.text, "\n")
        # the check for only up to five tweets
        if count_status>=5:
            break
    
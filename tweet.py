#!/usr/bin/python
#credited to https://dev.twitter.com/streaming/overview/request-parameters
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import time
import sys


#Variables that contains the user credentials to access Twitter API 
access_token = "3527076748-HflTXP74NjSWDIyuAmakc69VqTAZ29WIUVfdgjE"
access_token_secret = "XSKSRbfQ2baQFJ5Sc9WrSPf6AT05NvdpMtQi6fGLajEoR"
consumer_key = "X8B3WiESc1q6v8NQqRcP3kUvw"
consumer_secret = "Wb619BUbvSOTZ3Azoe1oYkCmVRE7yD3TkZMjFobDoi64XEcCLX"
#input kinds of secert key

Google='20536157'
IBM = '18994444'
Yahoo='19380829'
Amazon ='20793816'
Microsoft='74286565'  #get 5 companies user id in twitter, so that i can follow them

#This is a basic listener that just prints received tweets 
class StdOutListener(StreamListener):

    def on_status(self,status):
        print json.dumps({"t": time.time()})    # transform data format to json and print out
        sys.stdout.flush()

#This handles Twitter authetification and the connection to Twitter Streaming API
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)  # Using kinds of keys to 
stream = Stream(auth, l)  
stream.filter(follow=[Google,Microsoft,IBM,Amazon,Yahoo],languages = ["en"]) #get the data which are sent by those companies
#This line filter Twitter Streams to follow the tweets which are sent by official accounts

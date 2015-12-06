#!/usr/bin/python

import sys
import os.path
import tweepy
from ConfigParser import ConfigParser
import logging

twitterConfigPath = 'twitter.conf'

if(os.path.isfile(twitterConfigPath) == False):
	print "Could not find the config file '%s'" % (twitterConfigPath)
	sys.exit(1)


config = ConfigParser();
logging.debug("Reading the config file at '%'", twitterConfigPath)
config.read(twitterConfigPath)

twitterConsumerKey = ''
twitterConsumerSecret = ''
twitterAccessKey = ''
twitterAccessSecret = ''

try:
	logging.debug("Fetching the consumer key")
	twitterConsumerKey = config.get('consumer', 'key')
except:
	logging.fatal("Could not find consumer key in config file '%s'", twitterConfigPath)
	sys.exit(1)	

try:
	logging.debug("Fetching the consumer secret")
	twitterConsumerSecret = config.get('consumer', 'secret')
except:
	logging.fatal("Could not find consumer secret in config file '%s'", twitterConfigPath)
	sys.exit(1)	

try:
	logging.debug("Fetching the access key")
	twitterAccessKey = config.get('access', 'key')
except:
	logging.fatal("Could not find access key in config file '%s'", twitterConfigPath)
	sys.exit(1)	

try:
	logging.debug("Fetching the access secret")
	twitterAccessSecret = config.get('access', 'secret')
except:
	logging.fatal("Could not find access secret in config file '%s'", twitterConfigPath)
	sys.exit(1)	


logging.debug("Creating auth token object")
twitterAuth = tweepy.OAuthHandler(twitterConsumerKey, twitterConsumerSecret)
twitterAuth.set_access_token(twitterAccessKey, twitterAccessSecret)
logging.debug("Connecting to Twitter API")
twitterHandle = tweepy.API(twitterAuth)
logging.debug("Connection complete")

try:
	logging.debug("Attempting to fetch user information to ensure authentication was successful")
	twitterHandle.me()
except tweepy.error.TweepError as e:
	logging.fatal("Could not connect to Twitter.  Check the network connection and/or authentication information located in %s", twitterConfigPath)
	logging.fatal("Exception details: %s", e.message)
	sys.exit(1)	




#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import time
import webbrowser

try:
	import tweepy as twitter
except ImportError:
	sys.exit("'python-tweepy' is not installed.\n Install it via: \n\n 'sudo apt-get install python-tweepy'")
	
def app_credentials():
	consumer_token = 'jK4IqH0x6xuafrgQGCWdA'
	consumer_secret = '2t85Uvuf5nhx3SQkSnYzcdfOprE3aNS8mneyfAv220'
	auth = twitter.OAuthHandler(consumer_token, consumer_secret)
	
	try:
		redirect_url = auth.get_authorization_url()
		webbrowser.open(redirect_url)
	except twitter.TweepError:
		print 'Error! Failed to get request token.'
		
	time.sleep(10)
	print("\n")
	pin_verifier = raw_input('Please Authorize The PIN: ').strip()
	auth.get_access_token(pin_verifier)
	print "access_key = '%s'" % auth.access_token.key
	print "access_secret = '%s'" % auth.access_token.secret
		
	#filename = "access.text"
	with open(".access.text", 'w+') as data:
		data.write(auth.access_token.key + ':' + auth.access_token.secret)
	data.close()
	
if __name__ == '__main__':
	app_credentials()
	


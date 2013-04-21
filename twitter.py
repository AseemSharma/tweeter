#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
#import credentials

try:
	import tweepy as twitter
except ImportError:
	sys.exit("'python-tweepy' is not installed.\n Install it via: \n\n 'sudo apt-get install python-tweepy'")


def get_access():
	with open(".access.text", 'r') as file:
		for line in file:
			(token, secret) = line.split(':')
		access = (token, secret)
		file.close()
		return access
			
def update_status():
	status_msg = raw_input("What's Happening: ")
	api = twitter.API(auth)
	api.update_status(status_msg)
	print "Tweeted\n"

def following():
	print("Top 20 people you are following: \n")
	for friend in twitter.Cursor(api.friends).items(20):
		print "\n", friend.screen_name
	

def followers():
	print("Top 20 of your followers: \n")
	for followers in twitter.Cursor(api.followers).items(20):
		print "\n", followers.screen_name
	
	
def trends(woeid_id):
	print("\n")
	trends_woeid = api.trends_location(woeid_id)
	print ("Trending Now: \n")
	for trend in trends_woeid[0] ["trends"]:
		print u"\n", trend["name"]
	print("\n")
		
		
def trending_now():
	print("Trending is now by location: \n")
	print("\n")
	print(" > 1.World\n > 2.India\n > 3.United States\n > 4.Your Location\n")
	choose_location = int(raw_input("Choose Trends by Location: \n"))
	if choose_location == 1:
		trends_world = trends(1)
	elif choose_location == 2:
		trends_india = trends(23424848)
	elif choose_location == 3:
		trends_us = trends(23424977)
	else:
		print("Get your WOEID [Where On Earth ID] from http://isithackday.com/geoplanet-explorer/ \n")
		time.sleep(30)
		w_id = int(raw_input("Enter Your WOEID :\n"))
		trends_woeid = trends(w_id)
	
def search():
	search = raw_input("\n Enter a #hashtag or a keyword: ")
	searched = api.search(search)
	for searches in searched:
		a = searches.text.splitlines()
		for line in a :
			print u"\n",line

def timeline():
	for status in twitter.Cursor(api.home_timeline).items(20):
		print "\n", status.text
			
def app_main():
	running = True
	while running:
		print " > 1.New Tweet\n > 2.Following\n > 3.Followers\n > 4.Trending Now\n > 5.Discover\n > 6.Timeline\n > 7.Quit\n"
		choose = int(raw_input("Choose: \n"))
		if choose == 1:
			update_status()
		elif choose == 2:
			following()
		elif choose == 3:
			followers()
		elif choose == 4:
			trending_now()
		elif choose == 5:
			search()
		elif choose == 6:
			timeline()
		else:
			print("Bye!")
			running = False
			
	
	
	
if __name__ == '__main__':
	consumer_token = 'jK4IqH0x6xuafrgQGCWdA'
	consumer_secret = '2t85Uvuf5nhx3SQkSnYzcdfOprE3aNS8mneyfAv220'
	auth = twitter.OAuthHandler(consumer_token, consumer_secret)
	api = twitter.API(auth)
	access = get_access()
	auth.set_access_token(access[0], access[1])
	print "\t\t\t\tTwitter\t\t\t\t"
	print ""
	print ""
	app_main()
	
	

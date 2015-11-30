# import twitter API library
from TwitterAPI import TwitterAPI
# import regular expression library
import re
# import Indico
import indicoio
# import GUI
from Tkinter import *

class WhatWeShare:
	# get authentication
	api = TwitterAPI('1KxHa1hlPbRdsggvL5yfBgHPY', 'afQVw38uLX3Q1YdILflyG4FjWhjkMzXgSP9ypLee4LM4QIMOea', '2786140432-npYkBKUXdUj3ulYj5f2N7LLN7dVJD6L6KdoyyLi', 'qwOdzFwyNfBKcmO6tq2TbOElrDHfd0ooiXNhMy4a7kUMd')
	indicoio.config.api_key = 'e2637d8d80afb64412b3dda3dda64bdd'

	# search twits
	r = api.request('search/tweets', {'q':'Vietnam'})
	for item in r:
		# filter out patterns
		patterns = re.compile(', u\'text\': u\'(.*?), u\'is_quote_status\':')
		if patterns is None:
			patterns = re.compile(', u\'text\': u\"(.*?), u\'is_quote_status\':')
		# search for patterns from twits
		text = patterns.search(str(item))
		# if found
		if text:
			# group into a text
			twit = text.group(1)
			print(twit)
			# send twit to indico to get sentiment analyzed
			sentimentNum = indicoio.sentiment_hq(twit)
			print(sentimentNum)
			if sentimentNum < 0.3:
				print("Positive")
			elif sentimentNum > 0.7:
				print("Negative")
			else:
				print("Neutral")
			print('\n')

def main():
	# create the window
	root = Tk()
	root.title("WhatWeShare")
	root.geometry("800x500")
	root.centerWindow()
	# event loop
	root.mainloop()

if __name__ == '__main__':
    main()





	# print('Here\'s the item')
	# print(item)
	# print('\n')

# take text between {u'contributors': None, u'truncated': False, u'text': u'
# and , u'is_quote_status': False

# import tweepy
# from tweepy import OAuthHandler
 
# consumer_key = '1KxHa1hlPbRdsggvL5yfBgHPY'
# consumer_secret = 'afQVw38uLX3Q1YdILflyG4FjWhjkMzXgSP9ypLee4LM4QIMOea'
# access_token = '2786140432-npYkBKUXdUj3ulYj5f2N7LLN7dVJD6L6KdoyyLi'
# access_secret = 'qwOdzFwyNfBKcmO6tq2TbOElrDHfd0ooiXNhMy4a7kUMd'
 
# auth = OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_secret)
 
# api = tweepy.API(auth)



# for status in tweepy.Cursor(api.home_timeline).items(10):
#     # Process a single status
#     print(status.text) 


# import requests
# import re
# r = requests.get('https://twitter.com/mtholyoke/followers')
# # test = re.findall(b'<a\b[^>]*>(.*?)</a>', r.content)
# print(r.content)


# for status in tweepy.Cursor(api.home_timeline).items(10):
#     # Process a single status
#     print(status.text)



# import requests
# # import lxml.html
# import re
# import urllib

# import ConfigParser
# from twython import Twython
 
# config = ConfigParser.ConfigParser()
# config.read('scraper.cfg')
 
# # spin up twitter api
# APP_KEY    = config.get('credentials','1KxHa1hlPbRdsggvL5yfBgHPY')
# APP_SECRET = config.get('credentials','afQVw38uLX3Q1YdILflyG4FjWhjkMzXgSP9ypLee4LM4QIMOea')
# OAUTH_TOKEN        = config.get('credentials','2786140432-npYkBKUXdUj3ulYj5f2N7LLN7dVJD6L6KdoyyLi')
# OAUTH_TOKEN_SECRET = config.get('credentials','qwOdzFwyNfBKcmO6tq2TbOElrDHfd0ooiXNhMy4a7kUMd')
 
# twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
# twitter.verify_credentials()


# username = "sociu2001@gmail.com"
# password = "20011995"

# class LinkedInParser(object):

#     def __init__(self, login, password):
#         """ Start up... """
#         self.login = login
#         self.password = password

#         # Simulate browser with cookies enabled
#         # self.cj = cookielib.MozillaCookieJar(cookie_filename)
#         # if os.access(cookie_filename, os.F_OK):
#         self.cj.load()
#         self.opener = urllib.request.build_opener(
#             urllib.request.HTTPRedirectHandler(),
#             urllib.request.HTTPHandler(debuglevel=0),
#             urllib.request.HTTPSHandler(debuglevel=0),
#             urllib.request.HTTPCookieProcessor(self.cj)
#         )
#         self.opener.addheaders = [
#             ('User-agent', ('Mozilla/4.0 (compatible; MSIE 6.0; '
#                            'Windows NT 5.2; .NET CLR 1.1.4322)'))
#         ]

#         # Login
#         self.loginPage()

#         title = self.loadTitle()

# r = requests.get('https://twitter.com/mtholyoke/followers')
# test = re.findall(b'<a\b[^>]*>(.*?)</a>', r.content)
# print(test)

# # tree = lxml.html.fromstring(r.text)

# # import scrapy

# # class MySpider(scrapy.Spider):
# # 	name = 'https://www.facebook.com/Microsoft'
# # 	allowed_domains = ['https://www.facebook.com/Microsoft']
# # 	start_urls = ['https://www.facebook.com/Microsoft',]

# # 	def parse(self, response):
# # 		msg = 'A response from %s just arrived!' % response.start_urls
# # 		self.logger.info(msg)
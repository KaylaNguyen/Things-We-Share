# import system module
import sys
# import parallel module
import pp
# import regular expression library
import re

# import twitter API library
from TwitterAPI import TwitterAPI
# import Indico
import indicoio

# method to craw twits related to term, extract sentiment from them 
# and compute the average sentiment score
def crawlTwits(term):
    # get authentication
    api = TwitterAPI('1KxHa1hlPbRdsggvL5yfBgHPY', 'afQVw38uLX3Q1YdILflyG4FjWhjkMzXgSP9ypLee4LM4QIMOea', '2786140432-npYkBKUXdUj3ulYj5f2N7LLN7dVJD6L6KdoyyLi', 'qwOdzFwyNfBKcmO6tq2TbOElrDHfd0ooiXNhMy4a7kUMd')
    indicoio.config.api_key = 'e2637d8d80afb64412b3dda3dda64bdd'

    # keep a counter to sum the sentiment score
    scoreSum = 0
    # keep a counter to sum the number of twits
    twitsNum = 0
    # keep a list of keywords
    listKeyWords = ""

    # search twits
    r = api.request('search/tweets', {'q':term})
    for item in r:
        # filter out patterns
        patterns = re.compile(', u\'text\': u\'(.*?)\', u\'is_quote_status\':')
        if patterns is None:
            patterns = re.compile(', u\'text\': u\"(.*?), u\'is_quote_status\':')
        # search for patterns from twits
        text = patterns.search(str(item))
        # if found
        if text:
            # group into a text
            twit = text.group(1)

            # send twit to indico to get sentiment analyzed
            sentimentNum = indicoio.sentiment_hq(twit)
            # sent twit to indico to get keywords
            json_keyWords = indicoio.keywords(twit)
            # go through dict object
            for key, value in json_keyWords.items():
            	# if the key is relevant enough
            	if value >= 0.2:
	            	# add keywords to the list
    	        	listKeyWords += key + ", "

            # add up score sum
            scoreSum += sentimentNum
            # increment number of twits
            twitsNum += 1

            # Uncomment lines below to debug
            # print(twit)
            # print(sentimentNum)
            # if sentimentNum < 0.3:
            #     print("Negative")
            # elif sentimentNum > 0.7:
            #     print("Positive")
            # else:
            #     print("Neutral")
            # print('\n')

    # compute the average sentiment score
    average = scoreSum/twitsNum
    # get the evaluation
    if average <= 0.2:
        rate = "very negative"
    elif average <= 0.4:
        rate = "slightly negative"
    elif average >= 0.8:
        rate = "very positive"
    elif average >= 0.6:
    	rate = "slightly positive"
    else:
        rate = "neutral"
    # string to return
    string = "an average score of " + str(average) + "\nOverall, it is " + str(rate) + "\nKeywords are " + listKeyWords
    return string

def main():
	# Set up job server
	# tuple of all parallel python servers to connect with
	ppservers = ()
	#ppservers = ("127.0.0.1:60000", )

	# take in inputs from user
	terms = raw_input("Give me a list of terms separated with <> to be searched in parallel!\nThe number of terms is the number of processors\n")
	# split them base on commas
	inputs = terms.strip().split("<>")

	# Creates jobserver with len(inputs) workers
	job_server = pp.Server(len(inputs), ppservers=ppservers)

	print "Starting pp with", job_server.get_ncpus(), "workers"

	# Submit a job of crawling twits for execution.
	# crawTwits - the function
	# (input,) - tuple with arguments for crawTwits
	# () - tuple with functions on which function sum_primes depends
	# ("from TwitterAPI import TwitterAPI", "re", "indicoio", ) 
	# - tuple with module names which must be imported before crawTwits execution
	jobs = [(input, job_server.submit(crawlTwits, (input, ), (),
	    ("from TwitterAPI import TwitterAPI", "re", "indicoio", ))) for input in inputs]

	for input, job in jobs:
	    print "\nTwits regarding", input, "have", job()

	job_server.print_stats()

# run the main method
if __name__ == '__main__':
    main()
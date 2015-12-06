# 

import math
import sys
import pp

# import twitter API library
from TwitterAPI import TwitterAPI
# import regular expression library
import re
# import Indico
import indicoio
# import GUI
# from Tkinter import *

def crawlTwits(term):
    # get authentication
    api = TwitterAPI('1KxHa1hlPbRdsggvL5yfBgHPY', 'afQVw38uLX3Q1YdILflyG4FjWhjkMzXgSP9ypLee4LM4QIMOea', '2786140432-npYkBKUXdUj3ulYj5f2N7LLN7dVJD6L6KdoyyLi', 'qwOdzFwyNfBKcmO6tq2TbOElrDHfd0ooiXNhMy4a7kUMd')
    indicoio.config.api_key = 'e2637d8d80afb64412b3dda3dda64bdd'

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
            print(twit)
            # send twit to indico to get sentiment analyzed
            sentimentNum = indicoio.sentiment_hq(twit)
            print(sentimentNum)
            if sentimentNum < 0.3:
                print("Negative")
            elif sentimentNum > 0.7:
                print("Positive")
            else:
                print("Neutral")
            print('\n')

def sum_primes(n):
    """Calculates sum of all primes below given integer n"""
    return sum([x for x in xrange(2, n) if isprime(x)])


print """Usage: python sum_primes.py [ncpus]
    [ncpus] - the number of workers to run in parallel,
    if omitted it will be set to the number of processors in the system"""

# Set up job server
# tuple of all parallel python servers to connect with
#  like an array
ppservers = ()
#ppservers = ("127.0.0.1:60000", )

if len(sys.argv) > 1:
    terms = sys.argv[1]
    inputs = terms.split(',')
    # Creates jobserver with ncpus workers
    # build a job server, like a box with worker
    # make # of workers
    job_server = pp.Server(len(inputs), ppservers=ppservers)
else:
    # Creates jobserver with automatically detected number of workers
    job_server = pp.Server(ppservers=ppservers)

print "Starting pp with", job_server.get_ncpus(), "workers"

# Submit a job of calulating sum_primes(100) for execution.
# sum_primes - the function
# (100,) - tuple with arguments for sum_primes
# (isprime,) - tuple with functions on which function sum_primes depends
# ("math",) - tuple with module names which must be imported before
#             sum_primes execution
# Execution starts as soon as one of the workers will become available
# give the boss the job and broadcast job for all
# job1 = job_server.submit(sum_primes, (100, ), (isprime, ), ("math", ))

# Retrieves the result calculated by job1
# The value of job1() is the same as sum_primes(100)
# If the job has not been finished yet, execution will
# wait here until result is available
# result = job1()

# print "Sum of primes below 100 is", result


# The following submits 8 jobs and then retrieves the results
# List/vector
# inputs = (100000, 100100, 100200, 100300, 100400, 100500, 100600, 100700)
# jobs = [(input, job_server.submit(sum_primes, (input, ), (isprime, ),
        # ("math", ))) for input in inputs]
jobs = [(input, job_server.submit(crawlTwits, (input, ), 
    ("TwitterAPI", "re", "indicoio", ))) for input in inputs]

for input, job in jobs:
    print "Twits regarding", input, "are", job()

job_server.print_stats()

# Parallel Python Software: http://www.parallelpython.com

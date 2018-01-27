from TwitterSearch import *
from PyTS import *
import numpy as np
import codecs, json 
import time

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['ice40']) # let's define all words we would like to have a look for
    tso.set_include_entities(False) # and don't give us all those entity information
    
    tmp = []
     # this is where the fun actually starts :)
        
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        tmp.append(tweet)
        
except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)

tstamp = time.time()
A = ts.get_tweets()

with open(str(tstamp)+".json", 'w') as outfile:
    json.dump(A, outfile)

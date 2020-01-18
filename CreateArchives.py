from TwitterSearch import *
from PyTS import *
import numpy as np
import codecs, json 
import time

KW = ["ecp5","lit3rick","un0rick","lattice ultra plus","ulx3s","up5k","arachne-pr","fpga_dave","ultraplus", "icecube2", "oe1cxw", "ice40", "icezum", "icoBoard", "iceZero", "BlackIce", "TinyFPGA", "foss fpga", "BeagleWire", "openfpga", "nextpnr", "yosyshq", "icebreaker fpga", "Icestorm","upduino","icoprog","1Bitsy","fpgawars","fpga_dave","@mithro","@bml_khubbard","SymbiFlow"]

for kw in KW:
	try:
	    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
	    tso.set_keywords([kw],False) # let's define all words we would like to have a look for
	    tso.set_include_entities(False) # and don't give us all those entity information
	    
	    tmp = []
	     # this is where the fun actually starts :)
		
	    for tweet in ts.search_tweets_iterable(tso):
		#print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
		tmp.append(tweet)
		
	except TwitterSearchException as e: # take care of all those ugly errors if there are some
	    print(e)

	tstamp = time.time()
	A = ts.get_tweets()

	with open(str(tstamp)+"-"+kw.replace(" ","_")+".json", 'w') as outfile:
	    json.dump(A, outfile)

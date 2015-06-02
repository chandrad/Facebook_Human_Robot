# 
# Note: file wont give you the submission file... it is a variant that tries to match the bots algorithm.
# the output file gives you a feature with a list of bidders and their @ the reaction time at the end of the auction.


import os
import pandas as pd
import numpy as np
from collections import defaultdict

os.chdir("C:\\Users\\*\\Desktop\\Ktk\\Facebook")
bids = pd.read_csv("bidsSmallest.csv")
auctions = pd.read_csv("uniqueauctions.csv")
#labels_to_write = ['auction','bidder_id', 'reactionTimeinLast10bids']
bidder_dict = defaultdict(int)
for j in xrange(0,len(auctions)):
	auction_id = auctions.iat[j,0]
	if j %1000 == 0:
		print j
	tempdf = bids[bids['auction'] == auction_id]
	tempdf = tempdf.sort('time', ascending = True)
	tempdf['time'] = tempdf['time'] - tempdf['time'].min()
	tempdf['timediff']  = tempdf['time'] - tempdf['time'].shift(1)
	tempdf['timediff'] = tempdf['timediff'].apply(lambda x: round(x/52631579))
	lenDF = len(tempdf)
	for i in xrange(max(0,lenDF-10), lenDF):
		if tempdf.iat[i,9] >= 1 and tempdf.iat[i,9] <=3:
			b_Id = tempdf.iat[i,5]
			bidder_dict[b_Id] +=1
	#row_dict = {k: None for k in labels_to_write}
	
print bidder_dict
pdDF = pd.DataFrame(bidder_dict, index = ['no of bids'])
pdDF = pdDF.transpose()
pdDF.to_csv("firstMyOut.csv",sep =",")


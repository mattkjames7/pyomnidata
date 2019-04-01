import os
from . import Globals
import numpy as np

def _CompareUpdates(newdates,newfiles,idx):
	'''
	This routine will compare the FTP data with the local data to see 
	which need updating.
	
	Inputs:
		newdates: list of update dates as read in from the FTP site
		newfiles: list of file names (original) from fTP site
		idx: local index of stored data files
		
	Returns:
		Boolean array
	
	'''
	
	nf = np.size(newfiles)
	update = np.zeros(nf,dtype='bool')
	for i in range(0,nf):
		#check if new file matches old file
		if newfiles[i] in idx.OldFileName:
			use = np.where(idx.OldFileName == newfiles[i])[0][0]
			#compare update dates
			if newdates[i] > idx.UpdateDate[use]:
				update[i] = True
		else:
			#if we get to this point then we need to update
			update[i] = True
	
	return update
		

from . import Globals
import numpy as np
import os

def _CompareUpdates(newdates,newfiles,idx,yearRange=None):
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
		year = int(os.path.splitext(newfiles[i])[0][-4:])

		#check if new file matches old file
		if newfiles[i] in idx.OldFileName:
			use = np.where(idx.OldFileName == newfiles[i])[0][0]
			#compare update dates
			if newdates[i] != idx.UpdateDate[use]:
				update[i] = True
		else:
			#if we get to this point then we need to update
			update[i] = True

		if isinstance(yearRange,(tuple,list)):
			if year < yearRange[0] or year > yearRange[1]:
				update[i] = False

	return update
		

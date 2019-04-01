import os

def _DeleteFTPFile(fname):
	'''
	Calls the linux rm command to remove the original data file after
	conversion.
	
	Inputs:
		fname: full path to file to delete
	
	'''
	os.system('rm -v '+fname)
	

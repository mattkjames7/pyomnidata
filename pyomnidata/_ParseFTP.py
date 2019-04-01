import os
from . import Globals
import PyFileIO as pf
import numpy as np

def _ParseFTP():
	'''
	This routine will read the FTP index file looking for file names
	and their associated update dates.
	
	'''
	#read the file in
	fname = Globals.DataPath+'tmp/index.html'
	lines = pf.ReadASCIIFile(fname)
	nl = np.size(lines)
	
	#firstly, search for the lines which contain 'omni_min' or 'omni_5min'
	use = np.zeros(nl,dtype='int')
	for i in range(0,nl):
		if 'omni_min' in lines[i]:
			use[i] = 1
		elif 'omni_5min' in lines[i]:
			use[i] = 5
	keep = np.where(use > 0)[0]
	Res = use[keep]
	lines = lines[keep]
	nl = lines.size
	
	#now to extract the FTP address, file name and update dates
	UpdateDates = np.zeros(nl,dtype='int32')
	Addresses = np.zeros(nl,dtype='object')
	FileNames = np.zeros(nl,dtype='object')
	Months = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,
				'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
	
	for i in range(0,nl):
		#deal with date first
		s = lines[i].split()
		yr = np.int32(s[0])
		mn = Months[s[1]]
		dy = np.int32(s[2])
		UpdateDates[i] = yr*10000 + mn*100 + dy
		
		#now let's get the ftp address
		s = lines[i].split('"')
		Addresses[i] = s[1]
		
		#now the file name
		s = s[1].split('/')
		FileNames[i] = s[-1]
		
	return FileNames,Addresses,UpdateDates,Res
	

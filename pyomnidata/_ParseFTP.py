from . import Globals
import PyFileIO as pf
import numpy as np
import copy
import re

def _HTMLStrip(line):
	'''
	Strips the HTML crap off a string, leaving spaces in its place.
	
	'''
	#copy the string
	a = copy.deepcopy(line)

	#find all instances of < and >
	lt = np.array([m.start() for m in re.finditer('<',a)])
	gt = np.array([m.start() for m in re.finditer('>',a)])

	#replace each substring with spaces
	n = np.min([lt.size,gt.size])
	for i in range(0,n):
		a = a.replace(a[lt[i]:gt[i]+1],' '*(gt[i]-lt[i]+1))
		
	return a

def _ParseFTP():
	'''
	This routine will read the FTP index file looking for file names
	and their associated update dates.
	
	'''
	#read the file in
	fname = f"{Globals.DataPath}/tmp/index.html"
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
	UpdateDates = np.zeros(nl,dtype='object')
	Addresses = np.zeros(nl,dtype='object')
	FileNames = np.zeros(nl,dtype='object')
	
	for i in range(0,nl):
		#deal with date first
		s = lines[i].split()
		UpdateDates[i] = s[1]
		
		#now let's get the ftp address
		#s = lines[i].split('"')
		Addresses[i] = 'https://spdf.gsfc.nasa.gov/pub/data/omni/high_res_omni/'+s[0]
		
		#now the file name
		#s = s[1].split('/')
		FileNames[i] = s[0]
		
	return FileNames,Addresses,UpdateDates,Res
	

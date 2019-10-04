import os
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
		lstr = _HTMLStrip(lines[i])
		s = lstr.split()
		ds = s[1].split('-')
		yr = np.int32(ds[0])
		mn = np.int32(ds[1])
		dy = np.int32(ds[2])
		UpdateDates[i] = yr*10000 + mn*100 + dy
		
		#now let's get the ftp address
		#s = lines[i].split('"')
		Addresses[i] = 'https://spdf.gsfc.nasa.gov/pub/data/omni/high_res_omni/'+s[0]
		
		#now the file name
		#s = s[1].split('/')
		FileNames[i] = s[0]
		
	return FileNames,Addresses,UpdateDates,Res
	

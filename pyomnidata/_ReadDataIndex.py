import os
from . import Globals
import PyFileIO as pf

def _ReadDataIndex():
	'''
	Reads an index file containing the file names, update dates and
	resolutions.
	'''
	#define the datatype
	dtype = [('FileName','U'),('OldFileName','U'),('UpdateDate','int32'),('Res','int32')]
	
	#check if the index file exists
	fname = Globals.DataPath+'DataIndex.dat'
	if not os.path.isfile(fname):
		return np.recarray(0,dtype=dtype)
		
	#if it does exist, then read it
	data = pf.ReadASCIIData(fname,Header=False,dtype=dtype)

	return data

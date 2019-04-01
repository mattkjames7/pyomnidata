import os 
from . import Globals
import PyFileIO as pf

def _UpdateDataIndex(idx):
	'''
	Updates the data index file.
	
	Input:
		idx: numpy.recarray containing the file names, time resolution 
			and dates for all data files
	'''
	
	fname = Globals.DataPath+'DataIndex.dat'
	pf.WriteASCIIData(fname,idx)

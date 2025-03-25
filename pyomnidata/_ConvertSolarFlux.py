import numpy as np
from . import Globals
import RecarrayTools as RT
import DateTimeTools as TT
import PyFileIO as pf

def _ConvertSolarFlux():
	'''
	Convert the ascii file from OMNI to a binary file
	'''

	#get the ascii file name
	fname0 = f"{Globals.DataPath}/F107.lst"
	#read the ascii file
	lines = pf.ReadASCIIFile(fname0)
	
	#remove the header
	for i in range(0,lines.size):
		if lines[i][:4] == 'YEAR':
			lines = lines[i+1:]
			break
	#remove the crap at the end
	for i in range(0,lines.size):
		if lines[i][0] == '<':
			lines = lines[:i]
			break
				
	n = lines.size
			
	#split into separate strings
	s = np.array([l.split() for l in lines],dtype='object')

	#create the output array
	data = np.recarray(n,dtype=Globals.fdtype)
	yr = np.int32(s[:,0])
	doy = np.int32(s[:,1])
	data.Date = TT.DayNotoDate(yr,doy)	
	
	data.ut = np.float32(s[:,2])
	data.utc = TT.ContUT(data.Date,data.ut)
	
	data.F10_7 = np.float32(s[:,3])
	
	#save the new file
	fname1 = f"{Globals.DataPath}/F107.bin"
	RT.SaveRecarray(data,fname1)

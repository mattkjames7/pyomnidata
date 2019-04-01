from . import Globals
import numpy as np
import os
import RecarrayTools as RT

def ReadOMNI(Year,Res=5):
	'''
	Read in the converted OMNI data for one year.
	
	Inputs:
		Year: integer year.
		Res: 1 or 5 for 1 minute or 5 minute data.
		
	Returns: 
		numpy.recarray
	'''
	if Res == 1:
		dtype = Globals.dtype1
	else:
		dtype = Globals.dtype5
		
	fname = Globals.DataPath+'{:1d}/'.format(Res)+'OMNI-{:1d}min-{:4d}.bin'.format(Res,Year)
	
	if not os.path.isfile(fname):
		print('File not found: '+fname)
		return np.recarray(0,dtype=dtype)
	
	return RT.ReadRecarray(fname,dtype)

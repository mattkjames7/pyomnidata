import numpy as np
from . import Globals
from .ReadOMNI import ReadOMNI
import RecarrayTools as RT

def GetOMNI(Year,Res=5):
	'''
	Retrieves OMNI data from memory, or from file if it hasn't been 
	loaded yet.
	
	Inputs:
		Year: Integer year, or two element integer years for loading a 
			range of years.

			
	Returns:
		numpy.recarray
	'''

	#list all of the years to load
	if np.size(Year) == 1:
		yrs = np.array([Year]).flatten()
	else:
		yrs = np.arange(Year[1] - Year[0] + 1) + Year[0]
	nyr = np.size(yrs)

	#select appropriate data pointer
	if Res == 1:
		data = Globals.loaded1
	else:
		data = Globals.loaded5

	#loop through loading each one
	for i in range(0,nyr):
		newkey = '{:4d}'.format(yrs[i])
		keys = list(data.keys())
		if not newkey in keys:
			data[newkey] = ReadOMNI(yrs[i],Res)

			
		#create output variable
		if i == 0:
			out = data[newkey]
		else:
			out = RT.JoinRecarray(out,data[newkey])
				
	return out

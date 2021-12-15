import numpy as np
from . import Globals
from ._ReadSolarFlux import _ReadSolarFlux
import os

def GetSolarFlux(Date=None):
	'''
	Return the solar flux data.
	
	Inputs
	======
	Date : None or int or [int,int]
		If None - all data will be returned.
		If a single integer date is supplied then only solar flux data
		from that date will be returned.
		If a 2-element array-like object with start and end dates is 
		supplied then all dates within that range will be returned.
		
	Returns
	=======
	out : numpy.recarray
		solar flux data
	'''


	if Globals.SolarFlux is None:
		Globals.SolarFlux = _ReadSolarFlux()
		
	out = Globals.SolarFlux

	if Date is None:
		pass
	elif np.size(Date) == 1:
		use = np.where(out.Date == Date)[0]
		out = out[use]
	elif np.size(Date) == 2:
		use = np.where((out.Date >= Date[0]) & (out.Date <= Date[1]))[0]
		out = out[use]
	
	return out

import numpy as np
from ._DownloadF107 import _DownloadF107
from ._ConvertSolarFlux import _ConvertSolarFlux

def UpdateSolarFlux(EndDate=20210124):
	'''
	Download the lates Solar flux data
	
	Inputs
	======
	EndDate : int
		Last date to ask for F10.7 flux (this is probably usually a few
		days prior to the current date)
	'''
	
	#download the new list
	_DownloadF107(EndDate)
	
	#now convert it
	_ConvertSolarFlux()
	

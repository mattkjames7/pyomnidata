from ._DownloadF107 import _DownloadF107
from ._ConvertSolarFlux import _ConvertSolarFlux
import os
from datetime import datetime

def UpdateSolarFlux(EndDate=None):
	'''
	Download the lates Solar flux data
	
	Inputs
	======
	EndDate : int
		Last date to ask for F10.7 flux (this is probably usually a few
		days prior to the current date)
	'''

	if EndDate is None:
		EndDate = int(datetime.now().strftime("%Y%m%d"))
	
	#download the new list
	_DownloadF107(EndDate)
	
	#now convert it
	_ConvertSolarFlux()
	

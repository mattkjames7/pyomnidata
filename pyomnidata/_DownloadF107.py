import numpy as np
import os
from . import Globals
import requests
import re

def _requestF107(EndDate):

	# Define the end date and construct the data payload as a dictionary.
	EndDate = 20250319
	payload = {
		'activity': 'retrieve',
		'res': 'daily',
		'spacecraft': 'omni2_daily',
		'start_date': '19631128',
		'end_date': f'{EndDate:08d}',  # formatted as an 8-digit number
		'vars': '50',
		'scale': 'Linear',
		'ymin': '',
		'ymax': '',
		'view': '0',
		'charsize': '',
		'xstyle': '0',
		'ystyle': '0',
		'symbol': '0',
		'symsize': '',
		'linestyle': 'solid',
		'table': '0',
		'imagex': '640',
		'imagey': '480',
		'color': '',
		'back': ''
	}

	url = 'https://omniweb.gsfc.nasa.gov/cgi/nx1.cgi'

	# Send the POST request using requests.
	response = requests.post(url, data=payload)
	return response.text

def _parseEndDate(text):

	pattern = r'correct range:\s*(\d+)\s*-\s*(\d+)'
	match = re.search(pattern, text)
	if match:
		maxdate = match.group(2)
		return maxdate
	else:
		raise requests.RequestException("Failed to parse end date")
	

def _DownloadF107(EndDate):
	'''
	Download F10.7 index data from OMNI
	
	'''
	#the output file:
	ofile = f"{Globals.DataPath}/F107.lst"


	text = _requestF107(EndDate)
	if "Error" in text:
		EndDate = _parseEndDate(text)
		text = _requestF107(text)
		
	#save it
	f = open(ofile,'w')
	f.write(text)
	f.close()

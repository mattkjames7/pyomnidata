import os
from . import Globals

def _DownloadFTPIndex():
	'''
	This routine downloads the index.html of the omni FTP site:
	ftp://spdf.gsfc.nasa.gov/pub/data/omni/high_res_omni/
	
	Returns:
		Boolean, True if index file exists
	
	'''
	#check that the temporary folder exists
	if not os.path.isdir(Globals.DataPath+'tmp/'):
		os.system('mkdir -pv '+Globals.DataPath+'tmp/')

	#download using wget
	os.system('wget https://spdf.gsfc.nasa.gov/pub/data/omni/high_res_omni/ -O '+Globals.DataPath+'tmp/index.html')
	

	#check that the file exists, return True if so
	return os.path.isfile(Globals.DataPath+'tmp/index.html')
	
